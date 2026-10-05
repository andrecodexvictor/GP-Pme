"""Assistência opcional GEAR: agente_fase_zero.

Fonte vigente: framework/adocao/primeiros-30-dias.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os
from datetime import date, timedelta

from google.adk.agents import Agent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server import core as _core


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Preparar o percurso inicial de 30 dias como janela local. Separar adoção de verificação pré-projeto. Não prometer implantação ou nível em prazo fixo. Verificar contatos, responsáveis, recuperação e pendências.\nFontes: framework/README.md e guias correspondentes.\n'

# Passos locais do percurso inicial; nenhuma conclusão certifica maturidade.
CHECKLIST_FASE_ZERO = _core.checklist_fase_zero()["passos"]


def checklist_fase_zero() -> list[dict]:
    """Retorna nove passos da janela inicial; adaptar conforme capacidade."""
    return [dict(passo) for passo in CHECKLIST_FASE_ZERO]


def cronograma_implantacao(data_inicio: str) -> dict:
    """Agenda somente os 30 dias iniciais; próximas etapas dependem da revisão."""
    return _core.cronograma_implantacao(data_inicio)


def verificar_prontidao(itens_concluidos: list[str]) -> dict:
    """Confere itens declarados; conclusão não certifica maturidade."""
    ids={str(v).strip().lower() for v in (itens_concluidos or [])}
    pending=[p['titulo'] for p in CHECKLIST_FASE_ZERO if str(p['id']) not in ids and p['titulo'].lower() not in ids]
    total=len(CHECKLIST_FASE_ZERO);done=total-len(pending)
    return {'total_passos':total,'concluidos':done,'percentual_conclusao':round(done/total*100,1),
            'passos_pendentes':pending,'pronto_para_nivel_1':False,
            'percurso_declarado_concluido':not pending,
            'mensagem':'Itens declarados devem ser verificados. Reaplicar maturidade com evidências; sem certificação automática.'}


root_agent = Agent(
    name="agente_fase_zero",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Guia de Implantação Fase Zero: checklist dos 30 dias iniciais, "
        "cronograma local e verificação de evidências e pendências, sem certificação."
    ),
    instruction=INSTRUCTION,
    tools=[checklist_fase_zero, cronograma_implantacao, verificar_prontidao],
)
