"""Interface comum dos adapters de plataformas de gestão (GP-PME).

Todo adapter (ClickUp, Notion, Trello, Jira, Linear) herda de PlataformaGestao.
Em modo dry-run (GPPME_DRY_RUN=1 ou credenciais ausentes) nenhuma chamada de rede
é feita: as ações são simuladas e registradas em `acoes_planejadas`.
"""
from __future__ import annotations

import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any

# Colunas canônicas do quadro GP-PME (Pilar 2 — Ciclo Micro-Adaptativo)
COLUNAS_GP_PME = ["A Fazer", "Em Andamento (máx 3)", "Em Teste", "Concluído"]
ETIQUETA_RAIA_RAPIDA = "🔥 Raia Rápida"
LIMITE_WIP = 3

# Tarefas da Fase Zero (fonte: GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md)
FASE_ZERO_TASKS = [
    "Nomear o Dono da TI e formar o CD-TI Lite (reunião quinzenal de 30 min)",
    "Definir o Canal Único de entrada de demandas de TI",
    "Montar o quadro Kanban GP-PME com 4 colunas e limite WIP = 3",
    "Preencher a Matriz 4 Quadrantes com os sistemas/ativos atuais",
    "Aplicar a autoavaliação de maturidade (IM-TI) e registrar o resultado",
    "Implantar os 3 KPIs visíveis: IDSC, TMpR e ISU",
    "Executar o checklist dos 10 controles NIST-Lite/CIS IG1",
    "Rodar o primeiro ciclo semanal (sprint de 1 semana) com retrospectiva",
]


@dataclass
class Cartao:
    """Card/tarefa normalizado entre plataformas."""

    id: str
    titulo: str
    coluna: str
    descricao: str = ""
    raia_rapida: bool = False
    url: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass
class Quadro:
    """Quadro/board normalizado."""

    id: str
    nome: str
    colunas: list[str]
    url: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


class PlataformaGestao(ABC):
    """Contrato que todo adapter implementa."""

    #: nome curto da plataforma, ex.: "clickup"
    nome: str = "base"
    #: env vars exigidas para modo real, ex.: ("CLICKUP_TOKEN",)
    credenciais_necessarias: tuple[str, ...] = ()

    def __init__(self) -> None:
        self.acoes_planejadas: list[dict[str, Any]] = []

    # ---------------------------------------------------------------- helpers
    @property
    def dry_run(self) -> bool:
        if os.environ.get("GPPME_DRY_RUN", "").strip() == "1":
            return True
        return not all(os.environ.get(v) for v in self.credenciais_necessarias)

    def _registrar(self, acao: str, **detalhes: Any) -> dict[str, Any]:
        registro = {"plataforma": self.nome, "acao": acao, "dry_run": self.dry_run, **detalhes}
        self.acoes_planejadas.append(registro)
        return registro

    # ------------------------------------------------------------ operações
    @abstractmethod
    def criar_quadro(self, nome: str) -> Quadro:
        """Cria um quadro/board vazio na plataforma."""

    @abstractmethod
    def criar_colunas(self, quadro: Quadro, colunas: list[str]) -> Quadro:
        """Garante as colunas (listas/status) no quadro, na ordem dada."""

    @abstractmethod
    def criar_cartao(
        self, quadro: Quadro, titulo: str, coluna: str,
        descricao: str = "", raia_rapida: bool = False,
    ) -> Cartao:
        """Cria um card na coluna indicada; marca raia rápida quando pedido."""

    @abstractmethod
    def listar_cartoes(self, quadro: Quadro) -> list[Cartao]:
        """Lista os cards do quadro (normalizados)."""

    @abstractmethod
    def mover_cartao(self, quadro: Quadro, cartao_id: str, coluna_destino: str) -> Cartao:
        """Move um card para outra coluna."""

    # ------------------------------------------------- protocolo GP-PME
    def configurar_quadro_gp_pme(self, nome: str = "GP-PME — Gestão de TI") -> Quadro:
        """Cria o quadro canônico do framework: 4 colunas + tasks da Fase Zero."""
        quadro = self.criar_quadro(nome)
        quadro = self.criar_colunas(quadro, COLUNAS_GP_PME)
        for task in FASE_ZERO_TASKS:
            self.criar_cartao(quadro, task, COLUNAS_GP_PME[0],
                              descricao="Tarefa da Fase Zero do GP-PME.")
        return quadro

    def verificar_wip(self, quadro: Quadro) -> dict[str, Any]:
        """Verifica o limite WIP=3 na coluna Em Andamento; retorna diagnóstico."""
        em_andamento = [c for c in self.listar_cartoes(quadro)
                        if c.coluna.startswith("Em Andamento")]
        estourado = len(em_andamento) > LIMITE_WIP
        return {
            "coluna": COLUNAS_GP_PME[1],
            "cartoes": len(em_andamento),
            "limite": LIMITE_WIP,
            "estourado": estourado,
            "recomendacao": (
                "Pare de puxar trabalho novo: termine um item antes de iniciar outro."
                if estourado else "WIP saudável."
            ),
        }

    def relatorio_quadro(self, quadro: Quadro) -> dict[str, Any]:
        """Resumo do quadro por coluna + raia rápida (para métricas do Pilar 2)."""
        cartoes = self.listar_cartoes(quadro)
        por_coluna: dict[str, int] = {}
        for c in cartoes:
            por_coluna[c.coluna] = por_coluna.get(c.coluna, 0) + 1
        return {
            "quadro": quadro.nome,
            "total": len(cartoes),
            "por_coluna": por_coluna,
            "raia_rapida": sum(1 for c in cartoes if c.raia_rapida),
            "wip": self.verificar_wip(quadro),
        }
