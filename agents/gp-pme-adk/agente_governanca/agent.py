"""Assistência opcional GEAR: agente_governanca.

Fonte vigente: framework/nucleo/governanca.md.
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


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Preparar decisões com alçada, alternativas, risco e responsável. A matriz de quatro finalidades relaciona receita, custos, experiência e resiliência; não é prova de benefício. ADM-Lite é adaptação local, não TOGAF ADM. Manter papéis acumulados e comunicação com negócio visíveis.\nFontes: framework/README.md e guias correspondentes.\n'


def gerar_pauta_cdti(contexto: str) -> str:
    """Prepara uma pauta de revisão de direção com agenda inicial ajustável.

    Recebe um resumo em texto livre do contexto atual (KPIs, riscos,
    iniciativas em andamento, pendências) e devolve a pauta formatada nos
    quatro blocos iniciais de agenda, ajustáveis ao contexto: Revisão de KPIs (5 min), Alinhamento e
    Matriz 4 Quadrantes (15 min), Análise de Riscos/DAN (5 min) e Próximos
    Passos/COT (5 min).

    Args:
        contexto: descrição livre da situação atual da TI e do negócio
            (ex.: status dos KPIs, incidentes recentes, iniciativas em
            avaliação) fornecida pelo Gestor de TI.

    Returns:
        Pauta da reunião em texto formatado, pronta para leitura em 30 min.
    """
    contexto = contexto.strip() or "DADO INSUFICIENTE: contexto não informado pelo Gestor de TI."
    return (
        "PAUTA CD-TI LITE — Agenda inicial de 30 minutos, ajustável\n"
        "Cadência quinzenal como referência local; conferir capacidade e urgência.\n"
        "\n"
        "1) REVISÃO DOS KPIs (5 min)\n"
        "   - Selecionar indicadores necessários à decisão, como IDSC, TMpR ou ISU.\n"
        "     Informar origem, janela, linha de base, limitações e metas acordadas.\n\n"
        "2) ALINHAMENTO E MATRIZ 4 QUADRANTES (15 min)\n"
        "   - Revisar cartões de projetos de TI em andamento.\n"
        "   - Avaliar alinhamento com as metas comerciais do negócio.\n\n"
        "3) ANÁLISE DE RISCOS (5 min)\n"
        "   - Ameaças urgentes de segurança (backups, vírus, acessos).\n"
        "   - Debater o indicador DAN (Dívida de Arquitetura Normalizada).\n\n"
        "4) PRÓXIMOS PASSOS (5 min)\n"
        "   - Submeter recursos e riscos à autoridade responsável, conforme alçada.\n"
        "   - Registrar motivo, responsável, prazo, evidência e próxima revisão.\n\n"
        "CONTEXTO INFORMADO PARA ESTA REUNIÃO:\n"
        f"   {contexto}\n"
    )


def montar_raci_lite(atividades: list) -> dict:
    """Monta a matriz de responsabilidades RACI-Lite (Responsável/Aprovador).

    R executa, A aprova, C é consultado e I é informado. Funções podem ser
    acumuladas, com conflitos e segunda conferência registrados. Campos
    antigos de R e A permanecem para compatibilidade.

    Args:
        atividades: lista de dicts, cada um com as chaves "atividade"
            (nome/descrição da tarefa), "responsavel" (quem executa) e
            "aprovador" (quem decide/autoriza). Chaves ausentes viram
            "DADO INSUFICIENTE".

    Returns:
        dict com "matriz" (lista normalizada de linhas RACI-Lite) e
        "total_atividades".
    """
    matriz = []
    for item in atividades or []:
        item = item if isinstance(item, dict) else {}
        matriz.append({
            "atividade": item.get("atividade", "DADO INSUFICIENTE"),
            "responsavel_R": item.get("responsavel", "DADO INSUFICIENTE"),
            "aprovador_A": item.get("aprovador", "DADO INSUFICIENTE"),
            "consultado_C": item.get("consultado", "DADO INSUFICIENTE"),
            "informado_I": item.get("informado", "DADO INSUFICIENTE"),
            "acumulo_R_A": bool(item.get("responsavel") and item.get("responsavel") == item.get("aprovador")),
            "segunda_conferencia": item.get("segunda_conferencia", "DADO INSUFICIENTE"),
        })
    return {"matriz": matriz, "total_atividades": len(matriz)}


def classificar_matriz_4_quadrantes(sistemas: list) -> dict:
    """Classifica sistemas/ativos de TI nos 4 quadrantes de valor de negócio.

    Finalidades: receita, custos, experiência e resiliência/segurança.
    A classificação registra uma hipótese de valor; não comprova benefício.

    Args:
        sistemas: lista de dicts, cada um com "nome" (sistema/iniciativa) e
            "quadrante" (um de: "receita", "custos", "experiencia",
            "seguranca" — case-insensitive). Itens sem quadrante
            reconhecido caem em "nao_classificado".

    Returns:
        dict com uma chave por quadrante ("Q1_injecao_receita",
        "Q2_reducao_custos", "Q3_experiencia_cliente",
        "Q4_resiliencia_seguranca", "nao_classificado"), cada uma contendo
        a lista de nomes dos sistemas classificados ali.
    """
    mapa = {
        "receita": "Q1_injecao_receita",
        "custos": "Q2_reducao_custos",
        "experiencia": "Q3_experiencia_cliente",
        "seguranca": "Q4_resiliencia_seguranca",
    }
    resultado: dict[str, list] = {v: [] for v in mapa.values()}
    resultado["nao_classificado"] = []

    for item in sistemas or []:
        item = item if isinstance(item, dict) else {}
        nome = item.get("nome", "DADO INSUFICIENTE")
        quadrante = str(item.get("quadrante", "")).strip().lower()
        chave = mapa.get(quadrante, "nao_classificado")
        resultado[chave].append(nome)

    return resultado


root_agent = Agent(
    name="agente_governanca",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Assistência a governança e direção: pautas do CD-TI Lite, "
        "RACI-Lite e Matriz 4 Quadrantes para governança de TI de PMEs."
    ),
    instruction=INSTRUCTION,
    tools=[gerar_pauta_cdti, montar_raci_lite, classificar_matriz_4_quadrantes],
)
