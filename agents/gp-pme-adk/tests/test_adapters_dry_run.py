"""Testes dry-run dos adapters de plataforma do GP-PME.

Cobrem, sem rede e sem credenciais (GPPME_DRY_RUN=1), o contrato mínimo que
todo adapter (`adapters/<plataforma>.py`) precisa cumprir:

1. `configurar_quadro_gp_pme()` cria as 4 colunas canônicas e popula "A Fazer"
   com as 8 tarefas da Fase Zero.
2. Puxar mais itens do que o limite WIP=3 para "Em Andamento (máx 3)" faz
   `verificar_wip()` reportar `estourado=True`.

Um adapter cujo módulo ainda não existe (ex.: `trello.py` antes de ser
implementado) é reportado como `skip`, não como falha — o pacote está em
construção incremental (ver CONVENTIONS.md).
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

# `adapters` é um pacote irmão deste diretório de testes (agents/gp-pme-adk/adapters).
# Garante que ele é importável independentemente de onde o pytest for invocado.
_PACOTE = Path(__file__).resolve().parents[1]
if str(_PACOTE) not in sys.path:
    sys.path.insert(0, str(_PACOTE))

from adapters.base import COLUNAS_GP_PME, FASE_ZERO_TASKS  # noqa: E402

PLATAFORMAS = ["clickup", "notion", "trello", "jira", "linear"]


@pytest.fixture(autouse=True)
def _forcar_dry_run(monkeypatch: pytest.MonkeyPatch) -> None:
    """Força modo dry-run em todos os testes: nenhuma chamada de rede é feita."""
    monkeypatch.setenv("GPPME_DRY_RUN", "1")


@pytest.mark.parametrize("plataforma", PLATAFORMAS)
def test_quadro_gp_pme_e_estouro_de_wip(plataforma: str) -> None:
    try:
        modulo = importlib.import_module(f"adapters.{plataforma}")
    except ImportError:
        pytest.skip(
            f"adapter '{plataforma}' ainda não implementado "
            f"(agents/gp-pme-adk/adapters/{plataforma}.py ausente)."
        )

    adapter = modulo.Adapter()
    assert adapter.dry_run is True, "GPPME_DRY_RUN=1 deve forçar dry-run mesmo sem credenciais"

    quadro = adapter.configurar_quadro_gp_pme()
    assert quadro.colunas == COLUNAS_GP_PME
    assert len(quadro.colunas) == 4

    cartoes = adapter.listar_cartoes(quadro)
    a_fazer = [c for c in cartoes if c.coluna == COLUNAS_GP_PME[0]]
    assert len(a_fazer) == len(FASE_ZERO_TASKS) == 8

    # Puxa 4 cards para "Em Andamento (máx 3)" -> estoura o limite WIP=3.
    for cartao in a_fazer[:4]:
        adapter.mover_cartao(quadro, cartao.id, COLUNAS_GP_PME[1])

    diagnostico = adapter.verificar_wip(quadro)
    assert diagnostico["cartoes"] == 4
    assert diagnostico["limite"] == 3
    assert diagnostico["estourado"] is True
