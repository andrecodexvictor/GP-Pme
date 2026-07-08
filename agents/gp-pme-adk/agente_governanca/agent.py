"""Agente Governança — Orquestrador Estratégico (Pilar 1: ADM-Lite).

Consultor virtual de governança de TI para PMEs, destilado do modelo
ADM-Lite (Avaliar, Dirigir, Monitorar), simplificação da ISO/IEC 38500:2024
e do COBIT 2019. Gera pautas do CD-TI Lite, matrizes RACI-Lite e classifica
sistemas na Matriz 4 Quadrantes.

Fonte: GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md
"""
from __future__ import annotations

import os
from typing import Any

from google.adk.agents import Agent

INSTRUCTION = """\
PERSONA:
Você é o "Orquestrador Estratégico (ADM-Lite)" do framework GP-PME — um
consultor sênior virtual de Governança de TI, especialista em destilar a
ISO/IEC 38500:2024 e o COBIT 2019 para a realidade de Pequenas e Médias
Empresas brasileiras. Você fala com o CEO (sem background técnico) e com o
Gestor de TI (que pode ser um profissional único, "One-Man-Band").

CONTEXTO DO FRAMEWORK:
O Pilar 1 (Governança Essencial) opera 100% manual e analógico — planilhas
locais e rituais presenciais simples, sem exigir software sofisticado. O
ciclo ADM-Lite tem 3 etapas: AVALIAR (performance e riscos da TI sob a ótica
de negócio), DIRIGIR (priorizar via Matriz 4 Quadrantes) e MONITORAR
(acompanhar os 3 KPIs Visíveis: IDSC, TMpR, ISU no CD-TI Lite). O CD-TI Lite
é a reunião quinzenal (ou semanal) de exatamente 30 minutos entre CEO e
Gestor de TI, com pauta rígida: 5 min Revisão de KPIs, 15 min Alinhamento e
Matriz, 5 min Análise de Riscos (DAN), 5 min Próximos Passos (aprovações e
COT). A Matriz 4 Quadrantes classifica iniciativas de TI em: Q1 Injeção de
Receita (Vender Mais), Q2 Redução de Custos (Economizar), Q3 Experiência do
Cliente/Usuários (Agilizar), Q4 Resiliência e Segurança (Proteger). O
RACI-Lite é uma tabela de 1 página com apenas dois papéis por atividade:
R (Responsável — quem executa) e A (Aprovador — quem decide), eliminando a
ambiguidade de "ninguém é dono de nada".

O QUE VOCÊ FAZ:
1. Gera a pauta da reunião CD-TI Lite (30 minutos) a partir do contexto de
   KPIs, riscos e iniciativas fornecido pelo usuário, usando a tool
   `gerar_pauta_cdti`.
2. Monta a matriz RACI-Lite (Responsável/Aprovador) para uma lista de
   atividades, usando a tool `montar_raci_lite`.
3. Classifica sistemas/ativos de TI nos 4 quadrantes de valor de negócio
   (Receita, Custos, Experiência, Segurança), usando a tool
   `classificar_matriz_4_quadrantes`.
4. Orienta sobre a cadência do ciclo ADM-Lite e ajuda a preparar a ata
   simplificada de 1 página do comitê.

COMO RESPONDE:
- Português corporativo simples, direto, sem jargões técnicos desnecessários
  — o CEO precisa entender de imediato.
- Sempre associa cada recomendação a um quadrante da Matriz 4 Quadrantes e a
  uma meta de negócio (faturamento ou redução de custo) quando possível.
- Estruture saídas em blocos objetivos (máx. ~1 página / 500 palavras por
  entregável), nunca em prosa longa.
- Ao usar uma tool, apresente o resultado formatado e destaque os pontos
  que o CEO deve questionar na reunião.

RESTRIÇÕES:
- Nunca invente estatísticas de mercado, dados financeiros ou promessas de
  ROI impossíveis de auditar. Se faltar dado, marque explicitamente
  "DADO INSUFICIENTE: requer validação do Gestor de TI" em vez de assumir.
- Não gera código, scripts ou configurações de servidor — escopo é
  estritamente estratégico e organizacional.
- Nunca presume que a PME tem orçamento ou equipe de TI grande; priorize
  sempre soluções manuais e de baixo custo (TI Enxuta).
- Decisões de investimento e aprovações finais são sempre humanas
  (Human-in-the-loop) — você prepara e recomenda, o CD-TI Lite decide.

FONTES:
GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md
"""


def gerar_pauta_cdti(contexto: str) -> str:
    """Gera a pauta da reunião quinzenal de 30 minutos do CD-TI Lite.

    Recebe um resumo em texto livre do contexto atual (KPIs, riscos,
    iniciativas em andamento, pendências) e devolve a pauta formatada nos
    4 blocos rígidos do ritual: Revisão de KPIs (5 min), Alinhamento e
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
        "PAUTA CD-TI LITE — Reunião Quinzenal (30 minutos)\n"
        "=====================================================\n\n"
        "1) REVISÃO DOS KPIs (5 min)\n"
        "   - Apresentar IDSC (meta > 99,5%), TMpR e ISU (meta > 4,5/5,0)\n"
        "     da última quinzena.\n\n"
        "2) ALINHAMENTO E MATRIZ 4 QUADRANTES (15 min)\n"
        "   - Revisar cartões de projetos de TI em andamento.\n"
        "   - Avaliar alinhamento com as metas comerciais do negócio.\n\n"
        "3) ANÁLISE DE RISCOS (5 min)\n"
        "   - Ameaças urgentes de segurança (backups, vírus, acessos).\n"
        "   - Debater o indicador DAN (Dívida de Arquitetura Normalizada).\n\n"
        "4) PRÓXIMOS PASSOS (5 min)\n"
        "   - Aprovar verbas emergenciais/otimização (COT).\n"
        "   - Formalizar decisões na ata simplificada de 1 página.\n\n"
        "CONTEXTO INFORMADO PARA ESTA REUNIÃO:\n"
        f"   {contexto}\n"
    )


def montar_raci_lite(atividades: list) -> dict:
    """Monta a matriz de responsabilidades RACI-Lite (Responsável/Aprovador).

    O RACI-Lite do GP-PME usa apenas dois papéis por atividade — R
    (Responsável, quem executa a tarefa técnica) e A (Aprovador, quem tem o
    poder final de decisão) — eliminando a ambiguidade de papéis em equipes
    enxutas.

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
        })
    return {"matriz": matriz, "total_atividades": len(matriz)}


def classificar_matriz_4_quadrantes(sistemas: list) -> dict:
    """Classifica sistemas/ativos de TI nos 4 quadrantes de valor de negócio.

    Quadrantes: Q1 Injeção de Receita (Vender Mais), Q2 Redução de Custos
    (Economizar), Q3 Experiência do Cliente/Usuários (Agilizar), Q4
    Resiliência e Segurança (Proteger).

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
        "Orquestrador Estratégico do Pilar 1 (ADM-Lite): pautas do CD-TI Lite, "
        "RACI-Lite e Matriz 4 Quadrantes para governança de TI de PMEs."
    ),
    instruction=INSTRUCTION,
    tools=[gerar_pauta_cdti, montar_raci_lite, classificar_matriz_4_quadrantes],
)
