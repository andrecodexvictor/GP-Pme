"""Agente PRD — Analista de Execução Ágil (Redação de PRD Simplificado).

Consultor virtual que transforma dores de negócio ou ideias soltas em um
Product Requirements Document (PRD) Simplificado no padrão GP-PME: 1-2
páginas, histórias de usuário, critérios de aceitação em Dado/Quando/Então
e escopo negativo rígido, viabilizando MVPs de até 2 semanas.

Fontes:
GP-PME antigravity/Templates/PRDs/Template_PRD_Completo.md
GP-PME antigravity/Templates/Prompts/Template_Prompt_PRD.md
"""
from __future__ import annotations

import os
from datetime import date

from google.adk.agents import Agent

INSTRUCTION = """\
PERSONA:
Você é o "Analista de Execução Ágil" do framework GP-PME — um Product Owner
sênior virtual especialista em traduzir dores de negócio de Pequenas e
Médias Empresas brasileiras em especificações enxutas e testáveis. Fala com
o Gestor de TI, o CEO ou o técnico terceirizado que vai construir o MVP.

CONTEXTO DO FRAMEWORK:
O GP-PME opera sob TI Enxuta: equipes pequenas ou "One-Man-Band", orçamento
restrito e necessidade de validação rápida. O PRD Simplificado do GP-PME tem
no máximo 1 a 2 páginas e força foco em valor de negócio, evitando o
desperdício de especificações longas que nunca são lidas. Toda funcionalidade
vira um MVP de no máximo 2 semanas. As seções obrigatórias do PRD são: (1)
Visão Geral e Valor de Negócio (dor + objetivo do MVP), (2) Histórias de
Usuário (formato "Como [perfil], eu quero [ação] para que eu possa
[benefício]"), (3) Critérios de Aceitação em modelo Dado/Quando/Então -
Passa/Não Passa, (4) Escopo Negativo (o que fica de fora do MVP,
explicitamente), (5) Requisitos Não Funcionais (desempenho, segurança,
usabilidade), (6) Métrica de Negócio Afetada (KPI que o projeto deve mover)
e (7) Aprovações e Fluxo HITL (Human-in-the-loop) — validação técnica e
assinatura do aprovador de negócio.

O QUE VOCÊ FAZ:
1. Gera o esqueleto de um novo PRD Simplificado a partir do nome do
   projeto/funcionalidade, pronto para ser preenchido em reunião de 15-20
   minutos, usando a tool `esqueleto_prd`.
2. Valida um PRD já rascunhado (texto em Markdown) contra as 7 seções
   obrigatórias e os critérios de aceite no formato Dado/Quando/Então,
   apontando o que falta, usando a tool `validar_prd`.
3. Ajuda o usuário a redigir histórias de usuário e critérios de aceitação
   testáveis a partir de uma dor de negócio descrita em texto livre.
4. Orienta sobre a entrevista de 10 minutos que precede o preenchimento
   (pergunta-chave: "qual tarefa toma mais tempo ou gera mais erro hoje?").

COMO RESPONDE:
- Português corporativo simples e direto, sem jargão técnico desnecessário.
- Sempre entrega o PRD (ou a validação) em Markdown, respeitando o limite de
  1 a 2 páginas — corte perfumaria antes de estourar o limite.
- Ao gerar histórias de usuário, produz no mínimo 2 e no máximo 3, cada uma
  com pelo menos 1 critério de aceitação em Dado/Quando/Então.
- Ao validar um PRD, aponta lacunas seção por seção, nunca em prosa corrida.
- Reforça a Seção 4 (Escopo Negativo) como a mais importante: tudo que
  ameaçar o prazo de 2 semanas deve ser explicitamente excluído do MVP.

RESTRIÇÕES:
- Nunca invente métricas de negócio, nomes de sistemas legados, integrações
  ou promessas de ROI. Se faltar informação, marque "DADO INSUFICIENTE:
  requer validação do Gestor de TI/PO" em vez de assumir.
- Não decide sozinho o que entra ou sai do escopo — apenas propõe; a decisão
  final e a assinatura (Seção 7, HITL) são sempre humanas.
- Não gera código-fonte nem arquitetura técnica detalhada — o PRD descreve
  o "o quê" e o "porquê" de negócio, não o "como" de implementação.
- Não aprova o próprio PRD que ajudou a redigir; sempre lembra o usuário de
  buscar a validação técnica (TI/QA) e a assinatura do aprovador de negócio.

FONTES:
GP-PME antigravity/Templates/PRDs/Template_PRD_Completo.md
GP-PME antigravity/Templates/Prompts/Template_Prompt_PRD.md
"""

# As 7 seções obrigatórias do PRD Simplificado GP-PME (Template_PRD_Completo.md).
SECOES_OBRIGATORIAS: list[str] = [
    "VISÃO GERAL E VALOR DE NEGÓCIO",
    "HISTÓRIAS DE USUÁRIO",
    "CRITÉRIOS DE ACEITAÇÃO",
    "ESCOPO NEGATIVO",
    "REQUISITOS NÃO FUNCIONAIS",
    "MÉTRICA DE NEGÓCIO",
    "APROVAÇÕES",
]


def esqueleto_prd(nome_projeto: str) -> str:
    """Gera o esqueleto de um PRD Simplificado GP-PME pronto para preencher.

    Produz o documento de 1-2 páginas no padrão oficial do framework, com
    as 7 seções obrigatórias, 2 histórias de usuário de exemplo e 2 cenários
    de critério de aceitação em formato Dado/Quando/Então, prontos para
    serem editados em reunião rápida com a equipe de negócio e TI.

    Args:
        nome_projeto: nome do projeto ou funcionalidade a especificar (ex.:
            "Automação de Cobrança de Boletos"). Se vazio, usa um placeholder.

    Returns:
        Texto Markdown do PRD Simplificado, com placeholders "[...]" nos
        campos que exigem preenchimento humano.
    """
    nome_projeto = (nome_projeto or "").strip() or "[NOME DO PROJETO OU FUNCIONALIDADE]"
    hoje = date.today().strftime("%d/%m/%Y")
    return (
        f"# PRD [GP-PME]: {nome_projeto}\n\n"
        "## 1. Visão Geral e Valor de Negócio\n"
        f"- Data de Solicitação: {hoje}  |  Versão: 1.0\n"
        "- Dono do Produto (Product Owner): [Nome do Gestor/Solicitante]\n"
        "- Técnico Executor: [Nome do Técnico ou Equipe de TI]\n"
        "- Dor de Negócio (O Problema): [até 3 frases sobre o problema "
        "operacional, custo ou tempo perdido hoje]\n"
        "- Objetivo do MVP (A Solução): [o que será construído em até 2 "
        "semanas, de forma enxuta, para resolver a dor]\n\n"
        "## 2. Histórias de Usuário\n"
        "- História 1: Como [perfil do colaborador], eu quero [funcionalidade "
        "simplificada] para que eu possa [benefício de negócio].\n"
        "- História 2: Como [perfil], eu quero [funcionalidade] para que eu "
        "possa [benefício].\n\n"
        "## 3. Critérios de Aceitação (Modelo Passa / Não Passa)\n"
        "- Cenário 1: Dado que [contexto inicial], quando [ação executada], "
        "então [resultado esperado].\n"
        "- Cenário 2: Dado que [contexto], quando [ação], então [resultado].\n\n"
        "## 4. Escopo Negativo (o que NÃO faremos neste MVP)\n"
        "- Exclusão 1: [item de complexidade excessiva para o MVP de 2 "
        "semanas]\n"
        "- Exclusão 2: [item excluído nesta fase]\n\n"
        "## 5. Requisitos Não Funcionais\n"
        "- Desempenho: [ex.: telas e consultas em até 2s em conexão móvel "
        "comum]\n"
        "- Segurança: [ex.: autenticação individual + privilégio mínimo (LUA)]\n"
        "- Usabilidade: [ex.: interface responsiva, sem manual complexo]\n\n"
        "## 6. Métrica de Negócio Afetada (KPI do Projeto)\n"
        "- Métrica de Negócio: [ex.: redução de X% no TMpR do setor / "
        "aumento de Y% em faturamento/ISU]\n\n"
        "## 7. Aprovações e Fluxo HITL (Human-in-the-loop)\n"
        "- Validação Técnica (TI/QA): [ ] Aprovado  [ ] Necessita Ajustes  |  "
        "Data: ___/___/___\n"
        "- Assinatura do Aprovador (PO/Negócios): "
        "_____________________________________\n"
    )


def validar_prd(texto: str) -> dict:
    """Valida um rascunho de PRD contra o padrão GP-PME.

    Verifica se as 7 seções obrigatórias estão presentes (por título,
    case-insensitive) e se a seção de Critérios de Aceitação contém pelo
    menos um cenário no formato Dado/Quando/Então.

    Args:
        texto: conteúdo em Markdown do PRD a validar.

    Returns:
        dict com "completo" (bool), "secoes_presentes" (lista),
        "secoes_faltantes" (lista), "tem_criterio_dado_quando_entao" (bool)
        e "recomendacao" (texto curto com o próximo passo).
    """
    texto = texto or ""
    texto_lower = texto.lower()

    presentes = [s for s in SECOES_OBRIGATORIAS if s.lower() in texto_lower]
    faltantes = [s for s in SECOES_OBRIGATORIAS if s not in presentes]

    tem_dado = "dado que" in texto_lower
    tem_quando = "quando" in texto_lower
    tem_entao = "então" in texto_lower or "entao" in texto_lower
    tem_criterio = tem_dado and tem_quando and tem_entao

    completo = not faltantes and tem_criterio

    if completo:
        recomendacao = (
            "PRD estruturalmente completo. Encaminhar para validação técnica "
            "(TI/QA) e assinatura do aprovador de negócio (Seção 7)."
        )
    else:
        pendencias = list(faltantes)
        if not tem_criterio:
            pendencias.append(
                "critério de aceitação no formato Dado/Quando/Então"
            )
        recomendacao = (
            "PRD incompleto. Pendências: " + "; ".join(pendencias) + "."
        )

    return {
        "completo": completo,
        "secoes_presentes": presentes,
        "secoes_faltantes": faltantes,
        "tem_criterio_dado_quando_entao": tem_criterio,
        "recomendacao": recomendacao,
    }


root_agent = Agent(
    name="agente_prd",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Analista de Execução Ágil: gera e valida PRDs Simplificados GP-PME "
        "(1-2 páginas), histórias de usuário e critérios Dado/Quando/Então."
    ),
    instruction=INSTRUCTION,
    tools=[esqueleto_prd, validar_prd],
)
