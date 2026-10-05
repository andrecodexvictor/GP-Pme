"""Assistência opcional GEAR: agente_maturidade.

Fonte vigente: framework/adocao/maturidade.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os

from google.adk.agents import Agent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server import core as _core


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Aplicar as dez perguntas com evidências, calcular IM-TI e sugerir ações por lacuna. Nenhum nível exige IA. Não certificar uma transição pela soma nem comparar pontuações de questionários diferentes sem reaplicação.\nFontes: framework/README.md e guias correspondentes.\n'

# Dez perguntas do instrumento local; fonte: framework/adocao/maturidade.md.
PERGUNTAS = [{**p, "opcoes": ["Sim", "Não"]} for p in _core.questionario_maturidade()]

# Nomes descritivos dos cinco níveis locais (0 a 4).
NIVEIS = dict(_core._NIVEIS)

# Interpretação orientada à revisão de lacunas.
INTERPRETACOES = dict(_core._INTERPRETACOES)

# Ações iniciais por domínio. A chave histórica "pilar" preserva o contrato.
TRANSICOES = {
    (0,1): [{"pilar":"Execução e serviços","acao":"Registrar demandas, responsáveis e trabalho iniciado."}],
    (1,2): [{"pilar":"Segurança e continuidade","acao":"Identificar dependências, conferir acessos e testar recuperação."}, {"pilar":"Governança e direção","acao":"Registrar decisões com negócio e alçadas."}],
    (2,3): [{"pilar":"Execução e serviços","acao":"Delimitar melhorias com aceite e acompanhar efeitos."}, {"pilar":"Governança e direção","acao":"Conferir indicadores e suas premissas."}],
    (3,4): [{"pilar":"Governança e direção","acao":"Verificar práticas por pergunta e sustentar revisão responsável, com ou sem IA."}],
}


def _nivel_por_pontos(pontos: float, maximo: int) -> int:
    return _core._nivel_por_pontos(pontos, maximo)


def questionario_maturidade() -> list[dict]:
    """Retorna as dez perguntas do instrumento local de maturidade GEAR.

    Cada pergunta é binária (Sim/Não) e exige evidência prática para ser
    marcada como "Sim" (ex.: planilha de backup testado, print do quadro
    Kanban). As perguntas cobrem os três domínios; nenhuma exige IA.

    Returns:
        Lista de 10 dicts com as chaves "id" (1-10, ordem do instrumento),
        "pilar" (domínio, chave histórica), "pergunta" (texto
        completo) e "opcoes" (["Sim", "Não"]).
    """
    return [dict(p) for p in PERGUNTAS]


def calcular_im_ti(respostas: list[int]) -> dict:
    """Instrumento GEAR; evidências acompanham respostas binárias."""
    return _core.avaliar_maturidade(respostas)


def plano_transicao(nivel_atual: int, nivel_alvo: int) -> dict:
    """Sugere ações por domínio entre dois níveis inteiros de 0 a 4.

    Níveis descritivos orientam a conversa. A revisão por pergunta e suas
    evidências decide as ações reais; o plano não certifica uma transição.
    A chave histórica "acoes_por_pilar" contém os três domínios.
    """
    if any(type(n) is not int or not 0 <= n <= 4 for n in (nivel_atual, nivel_alvo)):
        return {"erro": "DADO INSUFICIENTE: nivel_atual e nivel_alvo devem ser inteiros de 0 a 4."}

    if nivel_alvo <= nivel_atual:
        return {
            "nivel_atual": nivel_atual,
            "nivel_atual_nome": NIVEIS[nivel_atual],
            "nivel_alvo": nivel_alvo,
            "nivel_alvo_nome": NIVEIS[nivel_alvo],
            "transicoes_cobertas": [],
            "acoes_por_pilar": {},
            "mensagem": (
                "Não há intervalo ascendente a planejar. Rever lacunas por pergunta, "
                "qualidade das evidências e manutenção das práticas mesmo com score alto."
            ),
            "fonte": "framework/adocao/maturidade.md",
        }

    transicoes_cobertas = []
    acoes_por_pilar: dict[str, list] = {}
    for nivel in range(nivel_atual, nivel_alvo):
        transicoes_cobertas.append(f"{NIVEIS[nivel]} -> {NIVEIS[nivel + 1]}")
        for item in TRANSICOES.get((nivel, nivel + 1), []):
            acoes_por_pilar.setdefault(item["pilar"], []).append(item["acao"])

    return {
        "nivel_atual": nivel_atual,
        "nivel_atual_nome": NIVEIS[nivel_atual],
        "nivel_alvo": nivel_alvo,
        "nivel_alvo_nome": NIVEIS[nivel_alvo],
        "transicoes_cobertas": transicoes_cobertas,
        "acoes_por_pilar": acoes_por_pilar,
        "fonte": "framework/adocao/maturidade.md",
        "limite": "Ações sugeridas; verificar lacunas por pergunta. Não garantem transição.",
    }


root_agent = Agent(
    name="agente_maturidade",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Consultor de Maturidade GEAR: aplica o questionário de "
        "autoavaliação, calcula o IM-TI global e por domínio e sugere ações "
        "com evidências; níveis locais de 0 a 4."
    ),
    instruction=INSTRUCTION,
    tools=[questionario_maturidade, calcular_im_ti, plano_transicao],
)
