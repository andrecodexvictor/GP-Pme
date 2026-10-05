"""Interface comum dos adapters de plataformas de gestão (GP-PME).

Todo adapter (ClickUp, Notion, Trello, Jira, Linear) herda de PlataformaGestao.
Em modo dry-run (GPPME_DRY_RUN=1 ou credenciais ausentes) nenhuma chamada de rede
é feita: as ações são simuladas e registradas em `acoes_planejadas`.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server.core import protocolo_kanban

# Colunas canônicas do quadro GP-PME (Pilar 2 — Ciclo Micro-Adaptativo)
COLUNAS_GP_PME = ["A Fazer", "Em Andamento (máx 3)", "Em Teste", "Concluído"]
ETIQUETA_RAIA_RAPIDA = "🔥 Raia Rápida"
LIMITE_WIP = 3

# Uma origem para as propostas iniciais; não são conclusões verificadas.
FASE_ZERO_TASKS = [t['titulo'] for t in protocolo_kanban()['tarefas_semente_fase_zero']]


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
    def configurar_quadro_gp_pme(self, nome: str = "GEAR — Gestão de TI") -> Quadro:
        """Cria o quadro canônico do framework: 4 colunas + tasks da Fase Zero."""
        quadro = self.criar_quadro(nome)
        quadro = self.criar_colunas(quadro, COLUNAS_GP_PME)
        for task in FASE_ZERO_TASKS:
            self.criar_cartao(quadro, task, COLUNAS_GP_PME[0],
                              descricao="Proposta inicial GEAR; conferir responsável, aceite e evidência.")
        return quadro

    def verificar_wip(self, quadro: Quadro) -> dict[str, Any]:
        """Conta trabalho iniciado por executor; ausência de executor limita a conclusão.

        Adapters podem fornecer extra['executor'] e extra['bloqueado']. O nome
        da coluna antiga permanece compatível; teste também compromete capacidade.
        """
        iniciados = [c for c in self.listar_cartoes(quadro)
                     if c.coluna.startswith("Em Andamento") or c.coluna in ("Em Teste", "Bloqueado")
                     or c.extra.get("bloqueado") or c.extra.get("iniciado")]
        por_executor: dict[str, int] = {}
        sem_executor = 0
        for cartao in iniciados:
            executor = cartao.extra.get("executor")
            if executor:
                por_executor[str(executor)] = por_executor.get(str(executor), 0) + 1
            else:
                sem_executor += 1
        estourado = any(n > LIMITE_WIP for n in por_executor.values()) or sem_executor > LIMITE_WIP
        return {
            "coluna": COLUNAS_GP_PME[1],  # Campo histórico; consultar estados_contados.
            "estados_contados": ["Em Andamento", "Em Teste", "Bloqueado"],
            "cartoes": len(iniciados),
            "limite": LIMITE_WIP,
            "estourado": estourado,
            "por_executor": por_executor,
            "sem_executor": sem_executor,
            "verificacao_completa": sem_executor == 0,
            "recomendacao": "Conferir trabalho por executor, testes, bloqueios e exceções. "
                + ("Há itens sem executor; o alerta agregado não comprova excesso individual."
                   if sem_executor else "Excesso identificado: rever capacidade antes de iniciar outro item."
                   if estourado else "Contagem por executor dentro do limite local."),
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
