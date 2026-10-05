"""Assistência opcional GEAR: agente_execucao_agil.

Fonte vigente: framework/nucleo/execucao-servicos.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os
from typing import Any

from google.adk.agents import Agent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server import core as _core


LIMITE_WIP = 3

INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Organizar demandas e capacidade. Contar itens em andamento, teste e bloqueio por executor; limite inicial de três. Emergência deve registrar autorização, suspensão e histórico. Não devolver trabalho iniciado como se fosse novo. Prazo de MVP depende de escopo e capacidade.\nFontes: framework/README.md e guias correspondentes.\n'


def gerar_tasklist_sprint(objetivo: str) -> str:
    """Modelo inicial de ciclo; duração e capacidade dependem da decisão local."""
    return ('# Ciclo de trabalho GEAR\n\nObjetivo: '+(objetivo.strip() or 'DADO INSUFICIENTE')+
            '\n\n- Conferir prioridades com o dono do processo.\n- Selecionar itens compatíveis com capacidade.\n'
            '- Registrar executor, aceite, dependência e prazo.\n- Contar até três itens iniciados por executor, incluindo testes e bloqueios.\n'
            '- Registrar autorização e histórico das emergências.\n- Rever saídas, impedimentos e próxima decisão.\n')


def diagnosticar_fluxo(cartoes_por_coluna: dict, numero_executores: int = 1) -> dict:
    """Contagem agregada é insuficiente para atestar limite de cada executor."""
    dados=cartoes_por_coluna or {}
    if type(numero_executores) is not int or numero_executores < 1 or any(type(v) is not int or v<0 for v in dados.values()):
        return {'erro':'Contagens inteiras não negativas e número de executores positivo.'}
    started=sum(v for k,v in dados.items() if k.strip().lower() in ('em andamento','em teste','bloqueado'))
    limit=_core.LIMITE_WIP*numero_executores
    return {'total_cartoes':sum(dados.values()),'wip_em_andamento':dados.get('Em Andamento',0),
            'wip_iniciado':started,'limite_wip':_core.LIMITE_WIP,'limite_agregado':limit,
            'wip_estourado':started>limit,'gargalo':None,
            'recomendacao':'Conferir itens por executor, incluindo testes e bloqueios. Agregado não comprova equilíbrio de capacidade.'}


def planejar_raia_rapida(incidente: str) -> dict:
    """Coordena exceção com registro; preserva trabalho interrompido."""
    return {'incidente':incidente.strip() or 'DADO INSUFICIENTE', 'prioridade':'critico',
            'passos':_core.protocolo_kanban()['raia_rapida']['passos']}


root_agent = Agent(
    name="agente_execucao_agil",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Assistência a execução e serviços: tasklists de "
        "sprint, diagnóstico de fluxo Kanban e planejamento de raia rápida."
    ),
    instruction=INSTRUCTION,
    tools=[gerar_tasklist_sprint, diagnosticar_fluxo, planejar_raia_rapida],
)
