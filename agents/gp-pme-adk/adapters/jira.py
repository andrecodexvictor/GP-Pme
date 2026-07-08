"""Adapter Jira Cloud para o framework GP-PME.

Como obter as credenciais (PT-BR):
  1. Acesse https://id.atlassian.com/manage-profile/security/api-tokens e clique
     em "Create API token". Copie o valor gerado para a variável JIRA_TOKEN.
  2. JIRA_EMAIL é o e-mail da conta Atlassian usada para gerar o token.
  3. JIRA_URL é a URL do seu site Jira, ex.: https://suaempresa.atlassian.net
     (sem barra no final).
  4. Sem essas três variáveis definidas, o adapter roda em modo dry-run: nenhuma
     chamada de rede é feita e o estado do quadro fica só em memória.

Limitação conhecida da API do Jira (documentada para o usuário em PT-BR):
  A criação de colunas de um board Jira Software não é um recurso exposto de
  forma simples pela REST API pública — colunas são derivadas do workflow do
  projeto e configuradas pela UI do board. Este adapter contorna isso mapeando
  as 4 colunas canônicas do GP-PME para status padrão do Jira ("To Do",
  "In Progress", "In Review", "Done") e move os cards com transições de
  status. Se o workflow do projeto não tiver um status equivalente disponível,
  o adapter levanta um erro com instruções em PT-BR para o usuário criar/mapear
  o status manualmente em Configurações do Projeto > Workflows.
"""
from __future__ import annotations

import base64
import os
import re
from typing import Any

import httpx

from .base import Cartao, PlataformaGestao, Quadro

# Mapeamento coluna canônica GP-PME -> status Jira padrão de um projeto "software".
COLUNA_PARA_STATUS = {
    "A Fazer": "To Do",
    "Em Andamento (máx 3)": "In Progress",
    "Em Teste": "In Review",
    "Concluído": "Done",
}
STATUS_PARA_COLUNA = {v: k for k, v in COLUNA_PARA_STATUS.items()}

ETIQUETA_RAIA_RAPIDA_JIRA = "raia-rapida"  # labels do Jira não aceitam espaço/emoji


class Adapter(PlataformaGestao):
    """Integra o GP-PME com um projeto do Jira Cloud (REST API v3)."""

    nome = "jira"
    credenciais_necessarias = ("JIRA_URL", "JIRA_EMAIL", "JIRA_TOKEN")

    def __init__(self) -> None:
        super().__init__()
        self._url = os.environ.get("JIRA_URL", "").rstrip("/")
        self._email = os.environ.get("JIRA_EMAIL", "")
        self._token = os.environ.get("JIRA_TOKEN", "")
        # Estado em memória usado apenas em modo dry-run.
        self._quadros_dry: dict[str, Quadro] = {}
        self._cartoes_dry: dict[str, dict[str, Cartao]] = {}
        self._prox_id = 1

    # ------------------------------------------------------------- infra
    def _novo_id(self) -> str:
        cartao_id = f"dry-{self._prox_id}"
        self._prox_id += 1
        return cartao_id

    def _headers(self) -> dict[str, str]:
        cred = base64.b64encode(f"{self._email}:{self._token}".encode()).decode()
        return {
            "Authorization": f"Basic {cred}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _request(self, method: str, caminho: str, **kwargs: Any) -> Any:
        try:
            resposta = httpx.request(
                method, f"{self._url}{caminho}", headers=self._headers(), timeout=30, **kwargs
            )
            resposta.raise_for_status()
            return resposta.json() if resposta.content else None
        except httpx.HTTPStatusError as exc:
            raise RuntimeError(
                f"Jira recusou a requisição ({exc.response.status_code}) em {caminho}: "
                f"{exc.response.text[:300]}. Verifique permissões do usuário JIRA_EMAIL "
                "e se JIRA_TOKEN ainda é válido."
            ) from exc
        except httpx.RequestError as exc:
            raise RuntimeError(
                f"Falha ao conectar ao Jira em {self._url}: {exc}. Verifique JIRA_URL "
                "e sua conexão de rede."
            ) from exc

    @staticmethod
    def _texto_para_adf(texto: str) -> dict[str, Any]:
        """Converte texto simples no formato ADF exigido pela REST API v3."""
        return {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": texto}] if texto else [],
                }
            ],
        }

    @staticmethod
    def _gerar_key_projeto(nome: str) -> str:
        letras = re.sub(r"[^A-Za-z]", "", nome).upper()
        return (letras[:8] or "GPPME")

    # -------------------------------------------------------- operações
    def criar_quadro(self, nome: str) -> Quadro:
        if self.dry_run:
            quadro = Quadro(id=self._novo_id(), nome=nome, colunas=[], url="https://dry-run.local/jira")
            self._quadros_dry[quadro.id] = quadro
            self._cartoes_dry[quadro.id] = {}
            self._registrar("criar_quadro", nome=nome, quadro_id=quadro.id)
            return quadro

        eu = self._request("GET", "/rest/api/3/myself")
        payload = {
            "key": self._gerar_key_projeto(nome),
            "name": nome,
            "projectTypeKey": "software",
            "leadAccountId": eu["accountId"],
            "assigneeType": "UNASSIGNED",
        }
        projeto = self._request("POST", "/rest/api/3/project", json=payload)
        self._registrar("criar_quadro", nome=nome, key=projeto["key"])
        return Quadro(
            id=projeto["key"],
            nome=nome,
            colunas=[],
            url=f"{self._url}/jira/software/projects/{projeto['key']}/boards",
            extra={"project_id": projeto["id"]},
        )

    def criar_colunas(self, quadro: Quadro, colunas: list[str]) -> Quadro:
        if self.dry_run:
            quadro.colunas = list(colunas)
            self._quadros_dry[quadro.id] = quadro
            self._registrar("criar_colunas", quadro_id=quadro.id, colunas=colunas)
            return quadro

        # Colunas reais de um board Jira vêm do workflow do projeto; aqui apenas
        # validamos que cada coluna tem um status Jira mapeado e avisamos o
        # usuário (em PT) quando algo precisa de configuração manual.
        faltando = [c for c in colunas if c not in COLUNA_PARA_STATUS]
        if faltando:
            raise RuntimeError(
                "Não é possível criar as colunas "
                f"{faltando} automaticamente: a REST API do Jira não permite criar "
                "colunas de board diretamente. Acesse o board no Jira > Configurações "
                "da coluna, e mapeie manualmente um status do workflow para cada uma "
                "dessas colunas."
            )
        quadro.colunas = list(colunas)
        self._registrar("criar_colunas", quadro_id=quadro.id, colunas=colunas)
        return quadro

    def criar_cartao(
        self, quadro: Quadro, titulo: str, coluna: str,
        descricao: str = "", raia_rapida: bool = False,
    ) -> Cartao:
        if self.dry_run:
            cartao = Cartao(
                id=self._novo_id(), titulo=titulo, coluna=coluna, descricao=descricao,
                raia_rapida=raia_rapida, url="https://dry-run.local/jira/issue",
            )
            self._cartoes_dry.setdefault(quadro.id, {})[cartao.id] = cartao
            self._registrar("criar_cartao", quadro_id=quadro.id, titulo=titulo, coluna=coluna)
            return cartao

        payload: dict[str, Any] = {
            "fields": {
                "project": {"key": quadro.id},
                "summary": titulo,
                "description": self._texto_para_adf(descricao),
                "issuetype": {"name": "Task"},
            }
        }
        if raia_rapida:
            payload["fields"]["labels"] = [ETIQUETA_RAIA_RAPIDA_JIRA]
            payload["fields"]["priority"] = {"name": "Highest"}
        criado = self._request("POST", "/rest/api/3/issue", json=payload)
        issue_id = criado["key"]

        status_alvo = COLUNA_PARA_STATUS.get(coluna)
        if status_alvo and status_alvo != COLUNA_PARA_STATUS["A Fazer"]:
            self._transicionar(issue_id, status_alvo)

        self._registrar("criar_cartao", quadro_id=quadro.id, issue=issue_id, coluna=coluna)
        return Cartao(
            id=issue_id, titulo=titulo, coluna=coluna, descricao=descricao,
            raia_rapida=raia_rapida, url=f"{self._url}/browse/{issue_id}",
        )

    def listar_cartoes(self, quadro: Quadro) -> list[Cartao]:
        if self.dry_run:
            return list(self._cartoes_dry.get(quadro.id, {}).values())

        jql = f'project = "{quadro.id}" ORDER BY created ASC'
        dados = self._request(
            "GET", "/rest/api/3/search",
            params={"jql": jql, "fields": "summary,status,description,labels,priority"},
        )
        cartoes: list[Cartao] = []
        for issue in dados.get("issues", []):
            campos = issue["fields"]
            status_nome = campos["status"]["name"]
            labels = campos.get("labels") or []
            cartoes.append(Cartao(
                id=issue["key"],
                titulo=campos["summary"],
                coluna=STATUS_PARA_COLUNA.get(status_nome, status_nome),
                raia_rapida=ETIQUETA_RAIA_RAPIDA_JIRA in labels,
                url=f"{self._url}/browse/{issue['key']}",
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

        status_alvo = COLUNA_PARA_STATUS.get(coluna_destino)
        if status_alvo is None:
            raise RuntimeError(
                f"Coluna '{coluna_destino}' não tem status Jira mapeado. Colunas "
                f"suportadas: {list(COLUNA_PARA_STATUS)}."
            )
        self._transicionar(cartao_id, status_alvo)
        self._registrar("mover_cartao", quadro_id=quadro.id, cartao_id=cartao_id, coluna=coluna_destino)
        return Cartao(id=cartao_id, titulo="", coluna=coluna_destino, url=f"{self._url}/browse/{cartao_id}")

    def _transicionar(self, issue_id: str, status_alvo: str) -> None:
        transicoes = self._request("GET", f"/rest/api/3/issue/{issue_id}/transitions")
        alvo = next(
            (t for t in transicoes["transitions"] if t["to"]["name"] == status_alvo), None
        )
        if alvo is None:
            raise RuntimeError(
                f"Não há transição de workflow disponível para o status '{status_alvo}' "
                f"na issue {issue_id}. Verifique o workflow do projeto em Configurações "
                "do Projeto > Workflows e adicione a transição necessária."
            )
        self._request("POST", f"/rest/api/3/issue/{issue_id}/transitions", json={"transition": {"id": alvo["id"]}})
