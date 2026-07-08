"""Adapter ClickUp (API v2) para o GP-PME.

MODO REAL — como obter as credenciais:

1. CLICKUP_TOKEN (token pessoal da API):
   a) Acesse https://app.clickup.com e faça login.
   b) Clique no seu avatar (canto inferior esquerdo) -> "Configurações" (Settings).
   c) No menu lateral, abra "Apps".
   d) Em "API Token", clique em "Gerar" (ou copie o token pessoal já existente).
   e) Defina a variável de ambiente CLICKUP_TOKEN com o valor copiado.

2. CLICKUP_SPACE_ID (Space onde o quadro GP-PME será criado):
   a) Abra o Space desejado dentro de um Workspace do ClickUp.
   b) Copie o ID que aparece na URL, no formato
      https://app.clickup.com/<team_id>/v/s/<space_id>.
   c) Defina a variável de ambiente CLICKUP_SPACE_ID com esse valor.

Sem essas duas variáveis (ou com GPPME_DRY_RUN=1), o adapter roda em modo
simulado (dry-run): nenhuma chamada de rede é feita; os cartões e quadros
ficam guardados em memória, de forma consistente, durante a sessão.

Mapeamento de conceitos GP-PME -> ClickUp:
    quadro      -> uma List do ClickUp (dentro do Space configurado)
    coluna      -> um status customizado da List (override_statuses)
    cartão      -> uma Task da List
    raia rápida -> tag "🔥 Raia Rápida" na task
"""
from __future__ import annotations

import os
from typing import Any

import httpx

from .base import Cartao, ETIQUETA_RAIA_RAPIDA, PlataformaGestao, Quadro

_BASE_URL = "https://api.clickup.com/api/v2"

_DICAS_HTTP = {
    401: "token inválido ou expirado — gere um novo em Configurações → Apps.",
    403: "token sem permissão/escopo para esta ação — verifique o acesso ao Space.",
    404: "recurso não encontrado — confira o CLICKUP_SPACE_ID e os IDs usados.",
    429: "limite de requisições da API do ClickUp atingido — aguarde e tente novamente.",
}


class Adapter(PlataformaGestao):
    """Adapter ClickUp: dry-run stateful por padrão; modo real via httpx quando
    CLICKUP_TOKEN e CLICKUP_SPACE_ID estão definidos (e GPPME_DRY_RUN != "1").
    """

    nome = "clickup"
    credenciais_necessarias = ("CLICKUP_TOKEN", "CLICKUP_SPACE_ID")

    def __init__(self) -> None:
        super().__init__()
        self._contador = 0
        self._cartoes_por_quadro: dict[str, list[Cartao]] = {}

    # ------------------------------------------------------------- helpers
    def _novo_id(self) -> str:
        self._contador += 1
        return f"dry-{self._contador}"

    def _cliente(self) -> httpx.Client:
        token = os.environ["CLICKUP_TOKEN"]
        return httpx.Client(
            base_url=_BASE_URL,
            headers={"Authorization": token, "Content-Type": "application/json"},
            timeout=30,
        )

    def _tratar_erro(self, resp: httpx.Response, contexto: str) -> None:
        if resp.status_code >= 400:
            dica = _DICAS_HTTP.get(resp.status_code, "verifique os parâmetros enviados.")
            raise RuntimeError(
                f"[clickup] Falha ao {contexto} (HTTP {resp.status_code}): {dica} "
                f"Resposta da API: {resp.text[:300]}"
            )

    # ------------------------------------------------------------ operações
    def criar_quadro(self, nome: str) -> Quadro:
        self._registrar("criar_quadro", nome=nome)
        if self.dry_run:
            quadro_id = self._novo_id()
            quadro = Quadro(
                id=quadro_id, nome=nome, colunas=[],
                url=f"https://dry-run.local/clickup/list/{quadro_id}",
            )
            self._cartoes_por_quadro[quadro_id] = []
            return quadro

        space_id = os.environ["CLICKUP_SPACE_ID"]
        with self._cliente() as client:
            resp = client.post(f"/space/{space_id}/list", json={"name": nome})
            self._tratar_erro(resp, "criar quadro (List) no ClickUp")
            dados = resp.json()
        return Quadro(
            id=str(dados["id"]), nome=dados.get("name", nome), colunas=[],
            url=f"https://app.clickup.com/t/{dados['id']}",
            extra={"space_id": space_id},
        )

    def criar_colunas(self, quadro: Quadro, colunas: list[str]) -> Quadro:
        self._registrar("criar_colunas", quadro_id=quadro.id, colunas=colunas)
        quadro.colunas = list(colunas)
        if self.dry_run:
            return quadro

        cores = ["#87909e", "#4194f6", "#f9d900", "#6bc950", "#e50000"]
        statuses: list[dict[str, Any]] = []
        for i, nome_coluna in enumerate(colunas):
            if i == 0:
                tipo = "open"
            elif i == len(colunas) - 1:
                tipo = "closed"
            else:
                tipo = "custom"
            statuses.append({
                "status": nome_coluna,
                "type": tipo,
                "orderindex": i,
                "color": cores[i % len(cores)],
            })
        with self._cliente() as client:
            resp = client.put(
                f"/list/{quadro.id}",
                json={"override_statuses": True, "statuses": statuses},
            )
            self._tratar_erro(resp, "configurar colunas (statuses) da List")
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
                url=f"https://dry-run.local/clickup/task/{self._contador}",
            )
            self._cartoes_por_quadro.setdefault(quadro.id, []).append(cartao)
            return cartao

        tags = [ETIQUETA_RAIA_RAPIDA] if raia_rapida else []
        with self._cliente() as client:
            resp = client.post(
                f"/list/{quadro.id}/task",
                json={"name": titulo, "description": descricao, "status": coluna, "tags": tags},
            )
            self._tratar_erro(resp, "criar cartão (Task)")
            dados = resp.json()
        return Cartao(
            id=str(dados["id"]), titulo=dados.get("name", titulo),
            coluna=dados.get("status", {}).get("status", coluna),
            descricao=dados.get("description") or "", raia_rapida=raia_rapida,
            url=dados.get("url", ""),
        )

    def listar_cartoes(self, quadro: Quadro) -> list[Cartao]:
        if self.dry_run:
            return list(self._cartoes_por_quadro.get(quadro.id, []))

        with self._cliente() as client:
            resp = client.get(f"/list/{quadro.id}/task", params={"include_closed": "true"})
            self._tratar_erro(resp, "listar cartões (Tasks)")
            dados = resp.json()
        cartoes: list[Cartao] = []
        for task in dados.get("tasks", []):
            nomes_tags = {t.get("name", "").lower() for t in task.get("tags", [])}
            cartoes.append(Cartao(
                id=str(task["id"]), titulo=task.get("name", ""),
                coluna=task.get("status", {}).get("status", ""),
                descricao=task.get("description") or "",
                raia_rapida=ETIQUETA_RAIA_RAPIDA.lower() in nomes_tags,
                url=task.get("url", ""),
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
            raise ValueError(f"[clickup] Cartão '{cartao_id}' não encontrado no quadro (dry-run).")

        with self._cliente() as client:
            resp = client.put(f"/task/{cartao_id}", json={"status": coluna_destino})
            self._tratar_erro(resp, "mover cartão (Task) de coluna")
            dados = resp.json()
        nomes_tags = {t.get("name", "").lower() for t in dados.get("tags", [])}
        return Cartao(
            id=str(dados["id"]), titulo=dados.get("name", ""),
            coluna=dados.get("status", {}).get("status", coluna_destino),
            descricao=dados.get("description") or "",
            raia_rapida=ETIQUETA_RAIA_RAPIDA.lower() in nomes_tags,
            url=dados.get("url", ""),
        )
