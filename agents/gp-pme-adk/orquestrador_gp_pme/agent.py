"""Assistência opcional GEAR: orquestrador_gp_pme.

Fonte vigente: framework/README.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os
import sys
import warnings
from pathlib import Path

from google.adk.agents import Agent  # LlmAgent

# --- sys.path: torna os diretórios de agentes irmãos importáveis (CONVENTIONS) --
_PACOTE = Path(__file__).resolve().parents[1]  # agents/gp-pme-adk/
if str(_PACOTE) not in sys.path:
    sys.path.insert(0, str(_PACOTE))

# --- Ferramentas de plataforma (adapters) ---------------------------------------
from adapters.tools import (  # noqa: E402  (após ajuste de sys.path)
    criar_tarefa,
    instalar_gp_pme_na_plataforma,
    listar_plataformas_suportadas,
    mover_tarefa,
    relatorio_do_quadro,
    verificar_wip,
)

# --- Importação tolerante dos 8 especialistas -----------------------------------
# (nome_do_modulo/diretorio) — cada um expõe `root_agent` em `<dir>/agent.py`.
_ESPECIALISTAS = [
    "agente_governanca",
    "agente_execucao_agil",
    "agente_seguranca",
    "agente_metricas_auditoria",
    "agente_maturidade",
    "agente_fase_zero",
    "agente_prd",
    "agente_prompts",
]

sub_agents = []
_indisponiveis = []
for _nome in _ESPECIALISTAS:
    try:
        _modulo = __import__(f"{_nome}.agent", fromlist=["root_agent"])
        sub_agents.append(_modulo.root_agent)
    except Exception as exc:  # noqa: BLE001 — tolerância deliberada
        _indisponiveis.append(_nome)
        warnings.warn(
            f"[GEAR] Especialista '{_nome}' indisponível e não será roteado: {exc}",
            stacklevel=2,
        )

if _indisponiveis:
    warnings.warn(
        "[GEAR] Orquestrador iniciado sem: " + ", ".join(_indisponiveis)
        + ". As perguntas para esses domínios devem ser respondidas com ressalva.",
        stacklevel=2,
    )


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Encaminhar tarefas aos oito especialistas existentes conforme necessidade. Quatro funções conceituais de assistência não equivalem à quantidade de agentes implementados. IA é opcional; decisões de prioridade, acesso, risco e investimento pertencem à pessoa autorizada.\nFontes: framework/README.md e guias correspondentes.\n'


root_agent = Agent(
    name="orquestrador_gp_pme",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Assistência opcional ao GEAR: encaminha demandas aos oito especialistas "
        "disponíveis e prepara ações de adoção e Kanban para revisão humana."
    ),
    instruction=INSTRUCTION,
    sub_agents=sub_agents,
    tools=[
        instalar_gp_pme_na_plataforma,
        criar_tarefa,
        mover_tarefa,
        verificar_wip,
        relatorio_do_quadro,
        listar_plataformas_suportadas,
    ],
)
