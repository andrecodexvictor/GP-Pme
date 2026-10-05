"""Adapter Trello (API 1.0) para o GP-PME.

MODO REAL — como obter as credenciais:

1. TRELLO_KEY (chave da API):
   a) Acesse https://trello.com/power-ups/admin e faça login.
   b) Clique em "Novo" (New) para criar uma integração/Power-Up (dê um nome,
      ex.: "GP-PME").
   c) Abra a aba "Chave da API" (API Key) da integração criada e copie a
      "Key" exibida.
   d) Defina a variável de ambiente TRELLO_KEY com o valor copiado.

2. TRELLO_TOKEN (token de acesso à sua conta):
   a) Na mesma aba "Chave da API", clique no link "Token" (gerar um token
      manualmente) — isso abre uma página de autorização do Trello.
   b) Autorize o acesso de leitura e escrita à sua conta.
   c) Copie o token gerado e defina a variável de ambiente TRELLO_TOKEN.

Sem essas duas variáveis (ou com GPPME_DRY_RUN=1), o adapter roda em modo
simulado (dry-run): nenhuma chamada de rede é feita; os cartões e quadros
ficam guardados em memória, de forma consistente, durante a sessão.

Mapeamento de conceitos GP-PME -> Trello:
    quadro      -> um Board do Trello
    coluna      -> uma List do Board
    cartão      -> um Card dentro da List
    raia rápida -> label vermelha "🔥 Raia Rápida" no card
"""
from __future__ import annotations

import os


from .base import Cartao, ETIQUETA_RAIA_RAPIDA, PlataformaGestao, Quadro

_BASE_URL = "https://api.trello.com/1"

_DICAS_HTTP = {
    401: "key/token inválidos ou expirados — gere um novo token em trello.com/power-ups/admin.",
    403: "sem permissão para esta ação — confira o escopo (leitura/escrita) do token.",
    404: "recurso não encontrado — confira os IDs de board/list/card usados.",
    429: "limite de requisições da API do Trello atingido — aguarde e tente novamente.",
}


class Adapter(PlataformaGestao):
    """Adapter Trello: dry-run stateful por padrão; modo real via httpx quando
    TRELLO_KEY e TRELLO_TOKEN estão definidos (e GPPME_DRY_RUN != "1").
    """

    nome = "trello"
    credenciais_necessarias = ("TRELLO_KEY", "TRELLO_TOKEN")

    def __init__(self) -> None:
        super().__init__()
        self._contador = 0
        self._cartoes_por_quadro: dict[str, list[Cartao]] = {}

    # ------------------------------------------------------------- helpers
    def _novo_id(self) -> str:
        self._contador += 1
        return f"dry-{self._contador}"

    def _auth(self) -> dict[str, str]:
        return {"key": os.environ["TRELLO_KEY"], "token": os.environ["TRELLO_TOKEN"]}

    def _cliente(self) -> httpx.Client:
        import httpx  # Dependência apenas do transporte real.
        return httpx.Client(base_url=_BASE_URL, timeout=30)

    def _tratar_erro(self, resp: httpx.Response, contexto: str) -> None:
        if resp.status_code >= 400:
            dica = _DICAS_HTTP.get(resp.status_code, "verifique os parâmetros enviados.")
            raise RuntimeError(
                f"[trello] Falha ao {contexto} (HTTP {resp.status_code}): {dica} "
                f"Resposta da API: {resp.text[:300]}"
            )

    def _garantir_label_raia_rapida(self, client: httpx.Client, quadro: Quadro) -> str | None:
        """Cria (uma vez, cacheada em quadro.extra) a label vermelha de raia rápida."""
        label_id = quadro.extra.get("label_raia_rapida")
        if label_id:
            return label_id
        resp = client.post(
            f"/boards/{quadro.id}/labels",
            params={**self._auth(), "name": ETIQUETA_RAIA_RAPIDA, "color": "red"},
        )
        self._tratar_erro(resp, "criar label de raia rápida")
        label_id = resp.json()["id"]
        quadro.extra["label_raia_rapida"] = label_id
        return label_id

    # ------------------------------------------------------------ operações
    def criar_quadro(self, nome: str) -> Quadro:
        self._registrar("criar_quadro", nome=nome)
        if self.dry_run:
            quadro_id = self._novo_id()
            quadro = Quadro(
                id=quadro_id, nome=nome, colunas=[],
                url=f"https://dry-run.local/trello/board/{quadro_id}",
            )
            self._cartoes_por_quadro[quadro_id] = []
            return quadro

        with self._cliente() as client:
            resp = client.post("/boards", params={**self._auth(), "name": nome})
            self._tratar_erro(resp, "criar quadro (Board) no Trello")
            dados = resp.json()
        return Quadro(
            id=str(dados["id"]), nome=dados.get("name", nome), colunas=[],
            url=dados.get("url", ""), extra={"listas": {}},
        )

    def criar_colunas(self, quadro: Quadro, colunas: list[str]) -> Quadro:
        self._registrar("criar_colunas", quadro_id=quadro.id, colunas=colunas)
        quadro.colunas = list(colunas)
        if self.dry_run:
            return quadro

        listas: dict[str, str] = quadro.extra.setdefault("listas", {})
        with self._cliente() as client:
            for nome_coluna in colunas:
                resp = client.post(
                    "/lists",
                    params={**self._auth(), "name": nome_coluna, "idBoard": quadro.id, "pos": "bottom"},
                )
                self._tratar_erro(resp, f"criar coluna (List) '{nome_coluna}'")
                listas[nome_coluna] = str(resp.json()["id"])
        return quadro

    def criar_cartao(
        self, quadro: Quadro, titulo: str, coluna: str,
        descricao: str = "", raia_rapida: bool = False,
    ) -> Cartao:
        self._registrar(
            "criar_cartao", quadro_id=quadro.id, titulo=titulo,
            coluna=coluna, raia_rapida=raia_rapida,
        )
        if self.dry_run:
            cartao = Cartao(
                id=self._novo_id(), titulo=titulo, coluna=coluna,
                descricao=descricao, raia_rapida=raia_rapida,
                url=f"https://dry-run.local/trello/card/{self._contador}",
            )
            self._cartoes_por_quadro.setdefault(quadro.id, []).append(cartao)
            return cartao

        listas: dict[str, str] = quadro.extra.get("listas", {})
        id_lista = listas.get(coluna)
        if not id_lista:
            raise RuntimeError(
                f"[trello] Coluna '{coluna}' não existe no quadro — chame criar_colunas primeiro."
            )
        with self._cliente() as client:
            params = {**self._auth(), "name": titulo, "desc": descricao, "idList": id_lista}
            if raia_rapida:
                params["idLabels"] = self._garantir_label_raia_rapida(client, quadro)
            resp = client.post("/cards", params=params)
            self._tratar_erro(resp, "criar cartão (Card)")
            dados = resp.json()
        return Cartao(
            id=str(dados["id"]), titulo=dados.get("name", titulo), coluna=coluna,
            descricao=dados.get("desc") or "", raia_rapida=raia_rapida,
            url=dados.get("url", ""),
        )

    def listar_cartoes(self, quadro: Quadro) -> list[Cartao]:
        if self.dry_run:
            return list(self._cartoes_por_quadro.get(quadro.id, []))

        listas: dict[str, str] = quadro.extra.get("listas", {})
        id_para_coluna = {v: k for k, v in listas.items()}
        with self._cliente() as client:
            resp = client.get(
                f"/boards/{quadro.id}/cards",
                params={**self._auth(), "fields": "name,desc,idList,url,labels"},
            )
            self._tratar_erro(resp, "listar cartões (Cards)")
            dados = resp.json()
        cartoes: list[Cartao] = []
        for card in dados:
            nomes_labels = {lbl.get("name", "").lower() for lbl in card.get("labels", []) or []}
            cartoes.append(Cartao(
                id=str(card["id"]), titulo=card.get("name", ""),
                coluna=id_para_coluna.get(card.get("idList", ""), ""),
                descricao=card.get("desc") or "",
                raia_rapida=ETIQUETA_RAIA_RAPIDA.lower() in nomes_labels,
                url=card.get("url", ""),
            ))
        return cartoes

    def mover_cartao(self, quadro: Quadro, cartao_id: str, coluna_destino: str) -> Cartao:
        self._registrar(
            "mover_cartao", quadro_id=quadro.id, cartao_id=cartao_id,
            coluna_destino=coluna_destino,
        )
        if self.dry_run:
            for cartao in self._cartoes_por_quadro.get(quadro.id, []):
                if cartao.id == cartao_id:
                    cartao.coluna = coluna_destino
                    return cartao
            raise ValueError(f"[trello] Cartão '{cartao_id}' não encontrado no quadro (dry-run).")

        listas: dict[str, str] = quadro.extra.get("listas", {})
        id_lista = listas.get(coluna_destino)
        if not id_lista:
            raise RuntimeError(
                f"[trello] Coluna '{coluna_destino}' não existe no quadro — chame criar_colunas primeiro."
            )
        with self._cliente() as client:
            resp = client.put(f"/cards/{cartao_id}", params={**self._auth(), "idList": id_lista})
            self._tratar_erro(resp, "mover cartão (Card) de coluna")
            dados = resp.json()
        nomes_labels = {lbl.get("name", "").lower() for lbl in dados.get("labels", []) or []}
        return Cartao(
            id=str(dados["id"]), titulo=dados.get("name", ""), coluna=coluna_destino,
            descricao=dados.get("desc") or "",
            raia_rapida=ETIQUETA_RAIA_RAPIDA.lower() in nomes_labels,
            url=dados.get("url", ""),
        )
