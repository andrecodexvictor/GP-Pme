"""Adapter Linear para o framework GP-PME.

Como obter as credenciais (PT-BR):
  1. Acesse https://linear.app/settings/account/security (Settings > Security
     & access > Personal API keys) na sua conta Linear.
  2. Clique em "New API key", dê um nome (ex.: "GP-PME") e copie o valor para
     a variável de ambiente LINEAR_API_KEY. O valor só é mostrado uma vez.
  3. Sem LINEAR_API_KEY definida, o adapter roda em modo dry-run: nenhuma
     chamada de rede é feita e o estado do quadro fica só em memória.

O board GP-PME é mapeado para um "Team" do Linear: as 4 colunas canônicas
viram "workflow states" do time e cada card vira uma "Issue".
"""
from __future__ import annotations

import os
from typing import Any

import httpx

from .base import ETIQUETA_RAIA_RAPIDA, Cartao, PlataformaGestao, Quadro

URL_GRAPHQL = "https://api.linear.app/graphql"

# Coluna canônica GP-PME -> tipo de workflow state do Linear.
COLUNA_PARA_TIPO_ESTADO = {
    "A Fazer": "unstarted",
    "Em Andamento (máx 3)": "started",
    "Em Teste": "started",
    "Concluído": "completed",
}
COR_PADRAO_ESTADO = {
    "A Fazer": "#e2e2e2",
    "Em Andamento (máx 3)": "#f2c94c",
    "Em Teste": "#2f80ed",
    "Concluído": "#27ae60",
}


class Adapter(PlataformaGestao):
    """Integra o GP-PME com um time do Linear (API GraphQL)."""

    nome = "linear"
    credenciais_necessarias = ("LINEAR_API_KEY",)

    def __init__(self) -> None:
        super().__init__()
        self._api_key = os.environ.get("LINEAR_API_KEY", "")
        # Estado em memória usado apenas em modo dry-run.
        self._quadros_dry: dict[str, Quadro] = {}
        self._cartoes_dry: dict[str, dict[str, Cartao]] = {}
        self._estados_dry: dict[str, dict[str, str]] = {}  # quadro_id -> {coluna: state_id}
        self._prox_id = 1

    # ------------------------------------------------------------- infra
    def _novo_id(self) -> str:
        item_id = f"dry-{self._prox_id}"
        self._prox_id += 1
        return item_id

    def _graphql(self, query: str, variaveis: dict[str, Any] | None = None) -> dict[str, Any]:
        try:
            resposta = httpx.post(
                URL_GRAPHQL,
                json={"query": query, "variables": variaveis or {}},
                headers={"Authorization": self._api_key, "Content-Type": "application/json"},
                timeout=30,
            )
            resposta.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(
                f"Linear recusou a requisição ({exc.response.status_code}): "
                f"{exc.response.text[:300]}. Verifique se LINEAR_API_KEY ainda é válida."
            ) from exc
        except httpx.RequestError as exc:
            raise RuntimeError(
                f"Falha ao conectar à API do Linear: {exc}. Verifique sua conexão de rede."
            ) from exc

        dados = resposta.json()
        if dados.get("errors"):
            mensagens = "; ".join(e.get("message", "erro desconhecido") for e in dados["errors"])
            raise RuntimeError(f"Linear retornou erro na consulta GraphQL: {mensagens}")
        return dados["data"]

    # -------------------------------------------------------- operações
    def criar_quadro(self, nome: str) -> Quadro:
        if self.dry_run:
            quadro = Quadro(id=self._novo_id(), nome=nome, colunas=[], url="https://dry-run.local/linear")
            self._quadros_dry[quadro.id] = quadro
            self._cartoes_dry[quadro.id] = {}
            self._estados_dry[quadro.id] = {}
            self._registrar("criar_quadro", nome=nome, quadro_id=quadro.id)
            return quadro

        existentes = self._graphql(
            "query($nome: String!) { teams(filter: {name: {eq: $nome}}) { nodes { id name url } } }",
            {"nome": nome},
        )
        nodes = existentes["teams"]["nodes"]
        if nodes:
            time = nodes[0]
        else:
            chave = "".join(ch for ch in nome.upper() if ch.isalnum())[:5] or "GPPME"
            criado = self._graphql(
                "mutation($input: TeamCreateInput!) { teamCreate(input: $input) "
                "{ success team { id name url } } }",
                {"input": {"name": nome, "key": chave}},
            )
            time = criado["teamCreate"]["team"]

        self._registrar("criar_quadro", nome=nome, team_id=time["id"])
        return Quadro(id=time["id"], nome=time["name"], colunas=[], url=time.get("url", ""))

    def criar_colunas(self, quadro: Quadro, colunas: list[str]) -> Quadro:
        if self.dry_run:
            quadro.colunas = list(colunas)
            self._quadros_dry[quadro.id] = quadro
            self._estados_dry[quadro.id] = {c: self._novo_id() for c in colunas}
            self._registrar("criar_colunas", quadro_id=quadro.id, colunas=colunas)
            return quadro

        existentes = self._graphql(
            "query($id: String!) { team(id: $id) { states { nodes { id name } } } }",
            {"id": quadro.id},
        )
        estados_atuais = {e["name"]: e["id"] for e in existentes["team"]["states"]["nodes"]}

        for coluna in colunas:
            if coluna in estados_atuais:
                continue
            tipo = COLUNA_PARA_TIPO_ESTADO.get(coluna, "unstarted")
            cor = COR_PADRAO_ESTADO.get(coluna, "#bec2c8")
            self._graphql(
                "mutation($input: WorkflowStateCreateInput!) { workflowStateCreate(input: $input) "
                "{ success workflowState { id name } } }",
                {"input": {"teamId": quadro.id, "name": coluna, "type": tipo, "color": cor}},
            )

        quadro.colunas = list(colunas)
        self._registrar("criar_colunas", quadro_id=quadro.id, colunas=colunas)
        return quadro

    def _id_estado(self, quadro: Quadro, coluna: str) -> str:
        if self.dry_run:
            estado = self._estados_dry.get(quadro.id, {}).get(coluna)
            if estado is None:
                raise RuntimeError(f"Coluna '{coluna}' não existe no quadro '{quadro.nome}'.")
            return estado

        dados = self._graphql(
            "query($id: String!) { team(id: $id) { states { nodes { id name } } } }",
            {"id": quadro.id},
        )
        for estado in dados["team"]["states"]["nodes"]:
            if estado["name"] == coluna:
                return estado["id"]
        raise RuntimeError(
            f"Coluna '{coluna}' não existe como workflow state no time Linear. "
            "Rode configurar_quadro_gp_pme() novamente ou crie o estado manualmente "
            "em Settings > Teams > Workflow."
        )

    def _id_label_raia_rapida(self, quadro: Quadro) -> str:
        dados = self._graphql(
            "query($id: String!) { team(id: $id) { labels { nodes { id name } } } }",
            {"id": quadro.id},
        )
        for label in dados["team"]["labels"]["nodes"]:
            if label["name"] == ETIQUETA_RAIA_RAPIDA:
                return label["id"]
        criado = self._graphql(
            "mutation($input: IssueLabelCreateInput!) { issueLabelCreate(input: $input) "
            "{ success issueLabel { id } } }",
            {"input": {"teamId": quadro.id, "name": ETIQUETA_RAIA_RAPIDA, "color": "#eb5757"}},
        )
        return criado["issueLabelCreate"]["issueLabel"]["id"]

    def criar_cartao(
        self, quadro: Quadro, titulo: str, coluna: str,
        descricao: str = "", raia_rapida: bool = False,
    ) -> Cartao:
        if self.dry_run:
            cartao = Cartao(
                id=self._novo_id(), titulo=titulo, coluna=coluna, descricao=descricao,
                raia_rapida=raia_rapida, url="https://dry-run.local/linear/issue",
            )
            self._cartoes_dry.setdefault(quadro.id, {})[cartao.id] = cartao
            self._registrar("criar_cartao", quadro_id=quadro.id, titulo=titulo, coluna=coluna)
            return cartao

        entrada: dict[str, Any] = {
            "teamId": quadro.id,
            "title": titulo,
            "description": descricao,
            "stateId": self._id_estado(quadro, coluna),
        }
        if raia_rapida:
            entrada["labelIds"] = [self._id_label_raia_rapida(quadro)]

        criado = self._graphql(
            "mutation($input: IssueCreateInput!) { issueCreate(input: $input) "
            "{ success issue { id identifier url } } }",
            {"input": entrada},
        )
        issue = criado["issueCreate"]["issue"]
        self._registrar("criar_cartao", quadro_id=quadro.id, issue=issue["id"], coluna=coluna)
        return Cartao(
            id=issue["id"], titulo=titulo, coluna=coluna, descricao=descricao,
            raia_rapida=raia_rapida, url=issue["url"],
        )

    def listar_cartoes(self, quadro: Quadro) -> list[Cartao]:
        if self.dry_run:
            return list(self._cartoes_dry.get(quadro.id, {}).values())

        dados = self._graphql(
            "query($id: ID!) { team(id: $id) { issues { nodes { id title url description "
            "state { name } labels { nodes { name } } } } } }",
            {"id": quadro.id},
        )
        cartoes: list[Cartao] = []
        for issue in dados["team"]["issues"]["nodes"]:
            labels = [n["name"] for n in issue["labels"]["nodes"]]
            cartoes.append(Cartao(
                id=issue["id"],
                titulo=issue["title"],
                coluna=issue["state"]["name"],
                descricao=issue.get("description") or "",
                raia_rapida=ETIQUETA_RAIA_RAPIDA in labels,
                url=issue["url"],
            ))
        return cartoes

    def mover_cartao(self, quadro: Quadro, cartao_id: str, coluna_destino: str) -> Cartao:
        if self.dry_run:
            cartoes = self._cartoes_dry.get(quadro.id, {})
            cartao = cartoes.get(cartao_id)
            if cartao is None:
                raise RuntimeError(f"Card {cartao_id} não encontrado no quadro dry-run.")
            if coluna_destino not in quadro.colunas:
                raise RuntimeError(
                    f"Coluna '{coluna_destino}' não existe no quadro '{quadro.nome}'."
                )
            cartao.coluna = coluna_destino
            self._registrar("mover_cartao", quadro_id=quadro.id, cartao_id=cartao_id, coluna=coluna_destino)
            return cartao

        state_id = self._id_estado(quadro, coluna_destino)
        self._graphql(
            "mutation($id: String!, $input: IssueUpdateInput!) { issueUpdate(id: $id, input: $input) "
            "{ success issue { id title url } } }",
            {"id": cartao_id, "input": {"stateId": state_id}},
        )
        self._registrar("mover_cartao", quadro_id=quadro.id, cartao_id=cartao_id, coluna=coluna_destino)
        return Cartao(id=cartao_id, titulo="", coluna=coluna_destino, url="")
