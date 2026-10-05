"""Adapter Notion (API 2022-06-28) para o GP-PME.

MODO REAL — como obter as credenciais:

1. NOTION_TOKEN (secret da integração):
   a) Acesse https://www.notion.so/my-integrations e faça login.
   b) Clique em "+ New integration", dê um nome (ex.: "GP-PME") e escolha o workspace.
   c) Em "Capabilities", habilite "Read content", "Update content" e "Insert content".
   d) Copie o "Internal Integration Secret" e defina a variável NOTION_TOKEN.

2. NOTION_PARENT_PAGE_ID (página onde o quadro/database será criado):
   a) Crie ou escolha uma página no Notion para hospedar o quadro GP-PME.
   b) Compartilhe a página com a integração: menu "..." (canto superior direito)
      -> "Add connections" -> selecione a integração criada no passo 1.
   c) Copie o ID de 32 caracteres presente na URL da página (bloco final,
      antes de "?", com ou sem hifens) e defina NOTION_PARENT_PAGE_ID.

Sem essas duas variáveis (ou com GPPME_DRY_RUN=1), o adapter roda em modo
simulado (dry-run): nenhuma chamada de rede é feita; os cartões e quadros
ficam guardados em memória, de forma consistente, durante a sessão.

Mapeamento de conceitos GP-PME -> Notion:
    quadro      -> um Database do Notion (criado dentro da página-pai)
    coluna      -> uma opção da propriedade select "Status"
    cartão      -> uma Page dentro do Database
    raia rápida -> opção "🔥 Raia Rápida" na propriedade select "Raia Rápida"
"""
from __future__ import annotations

import os
from typing import Any


from .base import Cartao, ETIQUETA_RAIA_RAPIDA, PlataformaGestao, Quadro

_BASE_URL = "https://api.notion.com/v1"
_VERSAO_API = "2022-06-28"

_DICAS_HTTP = {
    401: "token inválido/expirado — gere um novo em notion.so/my-integrations.",
    403: "a integração não tem acesso a este recurso — use 'Add connections' na página.",
    404: (
        "recurso não encontrado — confira o NOTION_PARENT_PAGE_ID e se a página "
        "foi compartilhada com a integração."
    ),
    429: "limite de requisições da API do Notion atingido — aguarde e tente novamente.",
}

_PROP_NOME = "Nome"
_PROP_STATUS = "Status"
_PROP_RAIA_RAPIDA = "Raia Rápida"
_PROP_DESCRICAO = "Descrição"


class Adapter(PlataformaGestao):
    """Adapter Notion: dry-run stateful por padrão; modo real via httpx quando
    NOTION_TOKEN e NOTION_PARENT_PAGE_ID estão definidos (e GPPME_DRY_RUN != "1").
    """

    nome = "notion"
    credenciais_necessarias = ("NOTION_TOKEN", "NOTION_PARENT_PAGE_ID")

    def __init__(self) -> None:
        super().__init__()
        self._contador = 0
        self._cartoes_por_quadro: dict[str, list[Cartao]] = {}

    # ------------------------------------------------------------- helpers
    def _novo_id(self) -> str:
        self._contador += 1
        return f"dry-{self._contador}"

    def _cliente(self) -> httpx.Client:
        import httpx  # Dependência apenas do transporte real.
        token = os.environ["NOTION_TOKEN"]
        return httpx.Client(
            base_url=_BASE_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "Notion-Version": _VERSAO_API,
                "Content-Type": "application/json",
            },
            timeout=30,
        )

    def _tratar_erro(self, resp: httpx.Response, contexto: str) -> None:
        if resp.status_code >= 400:
            dica = _DICAS_HTTP.get(resp.status_code, "verifique os parâmetros enviados.")
            raise RuntimeError(
                f"[notion] Falha ao {contexto} (HTTP {resp.status_code}): {dica} "
                f"Resposta da API: {resp.text[:300]}"
            )

    @staticmethod
    def _rich_text(texto: str) -> list[dict[str, Any]]:
        return [{"type": "text", "text": {"content": texto}}]

    # ------------------------------------------------------------ operações
    def criar_quadro(self, nome: str) -> Quadro:
        self._registrar("criar_quadro", nome=nome)
        if self.dry_run:
            quadro_id = self._novo_id()
            quadro = Quadro(
                id=quadro_id, nome=nome, colunas=[],
                url=f"https://dry-run.local/notion/database/{quadro_id}",
            )
            self._cartoes_por_quadro[quadro_id] = []
            return quadro

        parent_id = os.environ["NOTION_PARENT_PAGE_ID"]
        with self._cliente() as client:
            resp = client.post(
                "/databases",
                json={
                    "parent": {"type": "page_id", "page_id": parent_id},
                    "title": self._rich_text(nome),
                    "properties": {
                        _PROP_NOME: {"title": {}},
                        _PROP_STATUS: {"select": {"options": []}},
                        _PROP_RAIA_RAPIDA: {
                            "select": {"options": [{"name": ETIQUETA_RAIA_RAPIDA, "color": "red"}]}
                        },
                        _PROP_DESCRICAO: {"rich_text": {}},
                    },
                },
            )
            self._tratar_erro(resp, "criar quadro (Database)")
            dados = resp.json()
        return Quadro(id=dados["id"], nome=nome, colunas=[], url=dados.get("url", ""))

    def criar_colunas(self, quadro: Quadro, colunas: list[str]) -> Quadro:
        self._registrar("criar_colunas", quadro_id=quadro.id, colunas=colunas)
        quadro.colunas = list(colunas)
        if self.dry_run:
            return quadro

        with self._cliente() as client:
            resp = client.patch(
                f"/databases/{quadro.id}",
                json={
                    "properties": {
                        _PROP_STATUS: {"select": {"options": [{"name": c} for c in colunas]}}
                    }
                },
            )
            self._tratar_erro(resp, "configurar colunas (opções do select Status)")
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
                url=f"https://dry-run.local/notion/page/{self._contador}",
            )
            self._cartoes_por_quadro.setdefault(quadro.id, []).append(cartao)
            return cartao

        propriedades: dict[str, Any] = {
            _PROP_NOME: {"title": self._rich_text(titulo)},
            _PROP_STATUS: {"select": {"name": coluna}},
            _PROP_DESCRICAO: {"rich_text": self._rich_text(descricao)},
        }
        if raia_rapida:
            propriedades[_PROP_RAIA_RAPIDA] = {"select": {"name": ETIQUETA_RAIA_RAPIDA}}
        with self._cliente() as client:
            resp = client.post(
                "/pages",
                json={"parent": {"database_id": quadro.id}, "properties": propriedades},
            )
            self._tratar_erro(resp, "criar cartão (Page)")
            dados = resp.json()
        return Cartao(
            id=dados["id"], titulo=titulo, coluna=coluna, descricao=descricao,
            raia_rapida=raia_rapida, url=dados.get("url", ""),
        )

    def listar_cartoes(self, quadro: Quadro) -> list[Cartao]:
        if self.dry_run:
            return list(self._cartoes_por_quadro.get(quadro.id, []))

        with self._cliente() as client:
            resp = client.post(f"/databases/{quadro.id}/query", json={})
            self._tratar_erro(resp, "listar cartões (query do Database)")
            dados = resp.json()
        cartoes: list[Cartao] = []
        for page in dados.get("results", []):
            cartoes.append(self._cartao_de_page(page))
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
            raise ValueError(f"[notion] Cartão '{cartao_id}' não encontrado no quadro (dry-run).")

        with self._cliente() as client:
            resp = client.patch(
                f"/pages/{cartao_id}",
                json={"properties": {_PROP_STATUS: {"select": {"name": coluna_destino}}}},
            )
            self._tratar_erro(resp, "mover cartão (Page) de coluna")
            dados = resp.json()
        return self._cartao_de_page(dados)

    # -------------------------------------------------------- parsing (real)
    @staticmethod
    def _cartao_de_page(page: dict[str, Any]) -> Cartao:
        props = page.get("properties", {})
        titulo_partes = props.get(_PROP_NOME, {}).get("title", [])
        titulo = "".join(p.get("plain_text", "") for p in titulo_partes)
        status = props.get(_PROP_STATUS, {}).get("select") or {}
        raia = props.get(_PROP_RAIA_RAPIDA, {}).get("select")
        desc_partes = props.get(_PROP_DESCRICAO, {}).get("rich_text", [])
        descricao = "".join(p.get("plain_text", "") for p in desc_partes)
        return Cartao(
            id=page["id"], titulo=titulo, coluna=status.get("name", ""),
            descricao=descricao, raia_rapida=raia is not None,
            url=page.get("url", ""),
        )
