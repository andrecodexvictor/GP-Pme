"""Agente Execução Ágil — Analista de Execução Ágil (Pilar 2: Scrum/ITIL Lite).

Consultor virtual de execução ágil para PMEs, destilado do Ciclo de Serviço
Micro-Adaptativo (Scrum + ITIL 4 Lite). Gera tasklists de sprint, diagnostica
o fluxo do Kanban (WIP, gargalos) e planeja a raia rápida (expedite) para
incidentes críticos.

Fonte: GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md
"""
from __future__ import annotations

import os
from typing import Any

from google.adk.agents import Agent

LIMITE_WIP = 3

INSTRUCTION = """\
PERSONA:
Você é o "Analista de Execução Ágil" do framework GP-PME — especialista
virtual em Scrum e gerenciamento de serviços de TI (ITIL 4), atuando como
co-piloto do Gestor de TI (frequentemente um profissional único,
"One-Man-Band") em PMEs brasileiras.

CONTEXTO DO FRAMEWORK:
O Pilar 2 (Execução Ágil) opera no Ciclo de Serviço Micro-Adaptativo: um
Kanban de 4 colunas estritas (A Fazer → Em Andamento [máx 3] → Em Teste →
Concluído), alimentado por um Canal Único de suporte. A cadência é semanal:
Planejamento de 15 min (segunda-feira, seleciona 3-5 cartões), Checkpoint
diário de 5 min (o que fiz ontem / o que farei hoje / há impedimento?) e
Retrospectiva. O limite de WIP (Work in Progress) é rígido: no máximo 3
tarefas simultâneas "Em Andamento" por técnico — isso evita multitarefa
crônica. Incidentes de baixa/média prioridade entram no fim do backlog "A
Fazer" e aguardam a próxima sprint; incidentes CRÍTICOS (ex.: ERP/banco de
dados fora do ar) acionam a "Raia Rápida" (Expedite): suspende-se a tarefa
"Em Andamento" de menor prioridade comercial (devolvendo-a a "A Fazer" para
liberar WIP), resolve-se a crise com 100% de esforço, e ao final a tarefa
suspensa retorna a "Em Andamento". A Matriz de Priorização (Eisenhower
Adaptada) classifica chamados por Severidade de Impacto × Urgência em:
Crítico, Alto, Médio, Baixo, Descarte. O ciclo de inovação
Ideia → PRD Simplificado (1 página) → MVP (máx. 2 semanas) → Piloto/Feedback
conduz as entregas de maior valor.

O QUE VOCÊ FAZ:
1. Gera a tasklist operacional da sprint semanal a partir de um objetivo
   informado, no formato do Template_Tasklist_Operacional, usando a tool
   `gerar_tasklist_sprint`.
2. Diagnostica o fluxo do Kanban (contagem por coluna, estouro de WIP,
   possíveis gargalos) a partir da contagem de cartões por coluna, usando a
   tool `diagnosticar_fluxo`.
3. Planeja a ativação da Raia Rápida para um incidente crítico — quais
   passos seguir e qual tarefa suspender — usando a tool
   `planejar_raia_rapida`.

COMO RESPONDE:
- Linguagem direta, técnica na medida certa, orientada a testes e critérios
  binários (passa/não passa) — nada de "deve ser rápido" ou "deve ser
  bonito" sem métrica objetiva.
- Toda tasklist ou plano deve caber em 1 página; evite prosa longa.
- Ao propor histórias de usuário, use sempre o formato
  "Como [persona], eu quero [recurso] para [benefício]" e critérios
  "Dado [contexto], quando [ação], então [resultado]".
- Sempre reforce o limite de WIP = 3 quando relevante.

RESTRIÇÕES:
- Não toma decisões de contratação, investimento estratégico ou política de
  segurança cibernética — isso é escopo do Agente de Governança ou do
  Agente de Segurança.
- Não invente fluxos de navegação, telas ou bancos de dados que a PME não
  possua; baseie-se estritamente no que foi informado.
- Se faltar informação para detalhar uma história de usuário ou critério de
  teste, crie uma seção "Perguntas Pendentes para o Gestor" em vez de
  assumir cenários.
- Aprovação final de escopo e priorização é sempre humana
  (Human-in-the-loop).

FONTES:
GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md
"""


def gerar_tasklist_sprint(objetivo: str) -> str:
    """Gera a tasklist operacional da sprint semanal (1 semana) a partir de um objetivo.

    Segue o formato do Template_Tasklist_Operacional do GP-PME: cadência
    semanal com planejamento de 15 min, no máximo 3 a 5 cartões
    comprometidos, WIP máximo de 3, e retrospectiva ao final.

    Args:
        objetivo: descrição livre do objetivo de negócio ou técnico da
            sprint (ex.: "reduzir tempo de resposta do suporte").

    Returns:
        Tasklist formatada em texto, pronta para colar no Kanban.
    """
    objetivo = objetivo.strip() or "DADO INSUFICIENTE: objetivo da sprint não informado."
    return (
        "TASKLIST OPERACIONAL — Sprint de 1 Semana\n"
        "===========================================\n\n"
        f"OBJETIVO DA SPRINT:\n   {objetivo}\n\n"
        "PLANEJAMENTO (15 min, segunda-feira):\n"
        "   - Revisar a coluna 'A Fazer' priorizada pela Matriz 4 Quadrantes.\n"
        "   - Selecionar no máximo 3 a 5 cartões para a semana.\n\n"
        "CARTÕES DA SEMANA (preencher com o Gestor de TI):\n"
        "   1. [DADO INSUFICIENTE: definir cartão 1]\n"
        "   2. [DADO INSUFICIENTE: definir cartão 2]\n"
        "   3. [DADO INSUFICIENTE: definir cartão 3]\n\n"
        f"REGRA DE WIP: máximo {LIMITE_WIP} cartões simultâneos em 'Em Andamento'.\n\n"
        "CHECKPOINT DIÁRIO (5 min):\n"
        "   - O que moveu cartões para 'Concluído' ontem?\n"
        "   - Em quais cartões vou trabalhar hoje?\n"
        "   - Existe impedimento técnico ou falta de feedback?\n\n"
        "RETROSPECTIVA (fim da semana):\n"
        "   - Taxa de cumprimento da sprint (meta > 80% dos cartões entregues).\n"
        "   - Pontos de melhoria para a próxima semana.\n"
    )


def diagnosticar_fluxo(cartoes_por_coluna: dict) -> dict:
    """Diagnostica o fluxo do Kanban a partir da contagem de cartões por coluna.

    Verifica o estouro do limite de WIP (máx. 3) na coluna "Em Andamento" e
    aponta possíveis gargalos (acúmulo desproporcional em uma coluna).

    Args:
        cartoes_por_coluna: dict mapeando nome da coluna (ex.: "A Fazer",
            "Em Andamento", "Em Teste", "Concluído") para a quantidade de
            cartões nela. Colunas não reconhecidas são mantidas como estão.

    Returns:
        dict com "total_cartoes", "wip_em_andamento", "wip_estourado"
        (bool), "gargalo" (nome da coluna com maior acúmulo relativo, ou
        None) e "recomendacao" (texto).
    """
    dados = {k: int(v) for k, v in (cartoes_por_coluna or {}).items()}
    total = sum(dados.values())

    em_andamento = 0
    for coluna, qtd in dados.items():
        if coluna.strip().lower().startswith("em andamento"):
            em_andamento += qtd

    wip_estourado = em_andamento > LIMITE_WIP

    gargalo = None
    if dados:
        gargalo = max(dados, key=dados.get)
        if dados[gargalo] == 0:
            gargalo = None

    if wip_estourado:
        recomendacao = (
            f"WIP estourado ({em_andamento}/{LIMITE_WIP}): pare de puxar "
            "trabalho novo, termine um cartão antes de iniciar outro."
        )
    elif gargalo and dados.get(gargalo, 0) > max(1, total // 2):
        recomendacao = (
            f"Possível gargalo na coluna '{gargalo}': concentre esforço em "
            "destravar esses cartões antes de puxar novos."
        )
    else:
        recomendacao = "Fluxo saudável: WIP dentro do limite e sem gargalo evidente."

    return {
        "total_cartoes": total,
        "wip_em_andamento": em_andamento,
        "limite_wip": LIMITE_WIP,
        "wip_estourado": wip_estourado,
        "gargalo": gargalo,
        "recomendacao": recomendacao,
    }


def planejar_raia_rapida(incidente: str) -> dict:
    """Planeja a ativação da Raia Rápida (Expedite) para um incidente crítico.

    Segue os 5 passos da mecânica de amortecimento de incidentes: suspender
    a tarefa menos crítica, devolvê-la ao backlog, ativar a raia rápida,
    resolver a crise e restabelecer o fluxo.

    Args:
        incidente: descrição livre do incidente crítico (ex.: "ERP fora do
            ar impedindo faturamento").

    Returns:
        dict com "incidente", "prioridade" ("critico"), "etiqueta"
        ("🔥 Raia Rápida") e "passos" (lista ordenada de ações a executar).
    """
    incidente = incidente.strip() or "DADO INSUFICIENTE: incidente não descrito."
    return {
        "incidente": incidente,
        "prioridade": "critico",
        "etiqueta": "🔥 Raia Rápida",
        "passos": [
            "1. Suspender a tarefa 'Em Andamento' de menor prioridade comercial.",
            "2. Devolver essa tarefa à coluna 'A Fazer', liberando espaço no WIP (máx 3).",
            "3. Ativar a Raia Rápida: colocar o cartão do incidente no topo do quadro.",
            "4. Dedicar 100% do esforço para mitigar o incidente até a resolução.",
            "5. Após concluído, resgatar a tarefa suspensa e movê-la de volta a "
            "'Em Andamento', restabelecendo o fluxo normal.",
        ],
    }


root_agent = Agent(
    name="agente_execucao_agil",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Analista de Execução Ágil do Pilar 2 (Scrum/ITIL Lite): tasklists de "
        "sprint, diagnóstico de fluxo Kanban e planejamento de raia rápida."
    ),
    instruction=INSTRUCTION,
    tools=[gerar_tasklist_sprint, diagnosticar_fluxo, planejar_raia_rapida],
)
