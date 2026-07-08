"""Agente Fase Zero — Implementação dos Primeiros 30 Dias do GP-PME.

Consultor virtual de implantação inicial de TI para PMEs, destilado do Guia
de Implementação Fase Zero (cronograma de 30 dias / 4 semanas: Organizar o
Caos, Automatizar e Proteger, Formalizar e Alinhar, Medir e Consolidar) e do
Roadmap Estratégico das 4 fases do framework (Zero, Um, Dois, Três). Monta o
checklist de implantação, o cronograma semana a semana e verifica se a PME
está pronta para certificar a transição ao Nível 1.

Fontes:
GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md
Docs/Roadmap.md
"""
from __future__ import annotations

import os
from datetime import date, timedelta

from google.adk.agents import Agent

INSTRUCTION = """\
PERSONA:
Você é o "Guia de Implantação Fase Zero" do framework GP-PME — um consultor
virtual especialista em conduzir PMEs brasileiras pelos primeiros 30 dias de
adoção do framework, focado em vitórias rápidas (Quick Wins) que tiram a TI
do caos operacional.

CONTEXTO DO FRAMEWORK:
A Fase Zero (Salva-Vidas / Injeção de Valor) é um cronograma de 30 dias
dividido em 4 semanas: Semana 1 "Organizar o Caos" (diagnóstico de
maturidade, quadro Kanban de 4 colunas com WIP=3, Canal Único de suporte),
Semana 2 "Automatizar e Proteger" (base de FAQs cobrindo >40% das dúvidas,
Inventário 80/20 de ativos críticos e backups testados), Semana 3
"Formalizar e Alinhar" (Plano de Resposta a Incidentes de 1 página, primeiro
CD-TI Lite e Matriz 4 Quadrantes) e Semana 4 "Medir e Consolidar" (3 KPIs
Visíveis — IDSC, TMpR, ISU — e reavaliação final do IM-TI para certificar a
transição ao Nível 1: Reativo Organizado, que exige IM-TI entre 3 e 5). Após
a Fase Zero, o Roadmap do GP-PME segue com a Fase Um (Despertar Estratégico,
60 dias — CD-TI Lite institucionalizado e NIST-Lite), a Fase Dois
(Consolidação e Escala, 90 dias — DAN/COT e Motor de IA) e a Fase Três
(Desacoplamento e Publicação, 30 dias — guias separados por pilar). Toda
ação pode ser feita 100% manual e analógica; atalhos com IA são sempre
opcionais.

O QUE VOCÊ FAZ:
1. Apresenta o checklist ordenado da Fase Zero, com a duração em dias e o
   entregável de cada passo, usando a tool `checklist_fase_zero`.
2. Gera o cronograma calendário completo (Fase Zero até Fase Três) a partir
   de uma data de início informada, usando a tool `cronograma_implantacao`.
3. Verifica a prontidão da PME para certificar a transição ao Nível 1,
   comparando os itens já concluídos contra o checklist oficial, usando a
   tool `verificar_prontidao`.
4. Reforça, a cada passo, qual é a Ação Manual mínima viável antes de
   sugerir qualquer atalho opcional com IA.

COMO RESPONDE:
- Português corporativo simples e direto, em blocos objetivos por semana.
- Sempre indica o entregável concreto esperado de cada passo (planilha,
  quadro, documento assinado) — nunca deixa a ação vaga.
- Ao apresentar o cronograma, destaca a data-limite de cada entregável para
  facilitar o acompanhamento do CD-TI Lite.
- Ao verificar prontidão, lista explicitamente o que falta antes de dizer
  que a PME está pronta para a próxima fase.

RESTRIÇÕES:
- Nunca invente prazos, datas ou percentuais de conclusão — use sempre as
  tools `cronograma_implantacao` e `verificar_prontidao` como fonte de
  verdade, nunca estime de cabeça.
- Não pula etapas do cronograma oficial (Semana 1 → 2 → 3 → 4); mesmo em
  PMEs com pressa, reforce que pular a Semana 1 (Canal Único + Kanban)
  compromete todo o resto.
- A certificação final de transição de nível é sempre assinada pelo CEO
  (Human-in-the-loop) — você prepara o relatório, não homologa sozinho.
- Não confunda o cronograma da Fase Zero (30 dias, semanal) com o Roadmap
  de 4 fases do framework (Zero, Um, Dois, Três, plurianual) — sempre deixe
  claro a qual dos dois o usuário está se referindo.

FONTES:
GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md
Docs/Roadmap.md
"""

# Checklist oficial da Fase Zero (Guia_de_Implementacao_Fase_Zero.md), na ordem
# cronológica dos 30 dias, agrupado pelas 4 semanas do cronograma.
CHECKLIST_FASE_ZERO: list[dict] = [
    {
        "id": 1,
        "semana": 1,
        "dias": "Dia 1-2",
        "duracao_dias": 2,
        "titulo": "Diagnóstico Rápido e Priorização de Maturidade",
        "acao_manual": (
            "Aplicar o Questionário de Diagnóstico de Maturidade para fixar o "
            "IM-TI de baseline (geralmente Nível 0) e priorizar os 3 principais "
            "gargalos da semana."
        ),
        "entregavel": "Planilha de Avaliação de Maturidade preenchida (IM-TI de baseline) e 3 prioridades da TI.",
    },
    {
        "id": 2,
        "semana": 1,
        "dias": "Dia 3-5",
        "duracao_dias": 3,
        "titulo": "Implantação do Quadro Kanban de TI",
        "acao_manual": (
            "Criar quadro (físico ou digital) com 4 colunas estritas — A Fazer, "
            "Em Andamento, Em Teste, Concluído — com WIP Limit = 3 por técnico."
        ),
        "entregavel": "Quadro Kanban de TI ativo e operacional.",
    },
    {
        "id": 3,
        "semana": 1,
        "dias": "Dia 6-7",
        "duracao_dias": 2,
        "titulo": "Estabelecendo o Canal Único de Suporte",
        "acao_manual": (
            "Criar um único ponto de entrada de solicitações e comunicar que "
            "canais informais (WhatsApp pessoal) não serão mais atendidos."
        ),
        "entregavel": "Canal Único ativo e integrado ao Kanban.",
    },
    {
        "id": 4,
        "semana": 2,
        "dias": "Dia 8-10",
        "duracao_dias": 3,
        "titulo": "Base de FAQs (Nível 1)",
        "acao_manual": (
            "Documentar o passo a passo das 5 dúvidas de TI mais frequentes "
            "(ex.: redefinir senha, Wi-Fi) em arquivo compartilhado."
        ),
        "entregavel": "Base de FAQs ativa (documento ou chatbot).",
    },
    {
        "id": 5,
        "semana": 2,
        "dias": "Dia 11-14",
        "duracao_dias": 4,
        "titulo": "Inventário 80/20 de Ativos Críticos e Backups",
        "acao_manual": (
            "Mapear os 20% de ativos que representam 80% do risco, configurar "
            "backup diário e realizar teste de restauração em menos de 30 min."
        ),
        "entregavel": "Planilha de Inventário 80/20 e backups diários testados em produção.",
    },
    {
        "id": 6,
        "semana": 3,
        "dias": "Dia 15-18",
        "duracao_dias": 4,
        "titulo": "Plano de Resposta a Incidentes (PRI) de 1 Página",
        "acao_manual": (
            "Preencher o PRI de 1 página com contatos emergenciais e checklist "
            "de isolamento físico; fixar impresso na sala de TI."
        ),
        "entregavel": "PRI de 1 Página assinado pelo CEO.",
    },
    {
        "id": 7,
        "semana": 3,
        "dias": "Dia 19-21",
        "duracao_dias": 3,
        "titulo": "Primeiro CD-TI Lite e Matriz 4 Quadrantes",
        "acao_manual": (
            "Executar a primeira reunião de 30 minutos entre CEO e Gestor de "
            "TI e preencher a Matriz 4 Quadrantes conectando projetos a metas."
        ),
        "entregavel": "Primeira ata CD-TI Lite de 1 página.",
    },
    {
        "id": 8,
        "semana": 4,
        "dias": "Dia 22-25",
        "duracao_dias": 4,
        "titulo": "Definindo e Coletando os 3 KPIs Visíveis",
        "acao_manual": (
            "Configurar a planilha de monitoramento de IDSC, TMpR e ISU e "
            "iniciar a coleta das pesquisas de satisfação pós-atendimento."
        ),
        "entregavel": "Painel de Monitoramento de KPIs ativo.",
    },
    {
        "id": 9,
        "semana": 4,
        "dias": "Dia 26-30",
        "duracao_dias": 5,
        "titulo": "Retrospectiva, Reavaliação e Transição de Fase",
        "acao_manual": (
            "Reaplicar o Questionário de Maturidade para computar o IM-TI "
            "final e certificar a transição ao Nível 1 (IM-TI entre 3 e 5)."
        ),
        "entregavel": "Relatório de transição de fase com novo IM-TI certificado e assinatura do CEO.",
    },
]

# Foco de cada semana da Fase Zero (para a agregação por semana no cronograma).
FOCO_SEMANA_FASE_ZERO: dict[int, str] = {
    1: "Organizar o Caos Imediato",
    2: "Automatizar e Proteger o Essencial",
    3: "Formalizando a Segurança e o Alinhamento",
    4: "Medindo o Sucesso e Consolidação",
}

# As 4 fases do Roadmap GP-PME (Docs/Roadmap.md), com duração oficial em dias
# corridos e objetivo central de cada uma.
FASES_ROADMAP: list[dict] = [
    {
        "fase": "Fase Zero: Salva-Vidas / Injeção de Valor",
        "duracao_dias": 30,
        "objetivo": "Mitigar o caos operacional e centralizar as solicitações.",
    },
    {
        "fase": "Fase Um: Despertar Estratégico",
        "duracao_dias": 60,
        "objetivo": "Estruturar o CD-TI Lite, a Matriz 4 Quadrantes e o NIST-Lite.",
    },
    {
        "fase": "Fase Dois: Consolidação e Escala",
        "duracao_dias": 90,
        "objetivo": "Consolidar o Motor de IA, medir o DAN/COT e planejar a arquitetura.",
    },
    {
        "fase": "Fase Três: Desacoplamento e Publicação",
        "duracao_dias": 30,
        "objetivo": "Separar os guias por pilar e publicar a visualização do framework.",
    },
]

_FORMATOS_DATA = ("%d/%m/%Y", "%Y-%m-%d")


def _parse_data(data_inicio: str) -> date | None:
    """Converte string em DD/MM/AAAA ou YYYY-MM-DD para date; None se inválida."""
    from datetime import datetime

    for formato in _FORMATOS_DATA:
        try:
            return datetime.strptime(data_inicio.strip(), formato).date()
        except (ValueError, AttributeError):
            continue
    return None


def checklist_fase_zero() -> list[dict]:
    """Retorna o checklist ordenado dos 30 dias oficiais da Fase Zero.

    Cada passo cobre um bloco de dias do cronograma (Guia_de_Implementacao_
    Fase_Zero.md), com a ação manual mínima e o entregável esperado.

    Returns:
        Lista de 9 dicts com as chaves "id" (ordem cronológica), "semana"
        (1-4), "dias" (intervalo de dias, ex. "Dia 1-2"), "duracao_dias",
        "titulo", "acao_manual" e "entregavel".
    """
    return [dict(passo) for passo in CHECKLIST_FASE_ZERO]


def cronograma_implantacao(data_inicio: str) -> dict:
    """Gera o cronograma calendário da implantação, da Fase Zero à Fase Três.

    Calcula, a partir da data de início informada, as datas de início/fim de
    cada uma das 4 fases do Roadmap GP-PME e o detalhamento semana a semana
    dos 30 dias da Fase Zero.

    Args:
        data_inicio: data do Dia 1 da Fase Zero, em formato "DD/MM/AAAA" ou
            "AAAA-MM-DD".

    Returns:
        Em caso de data inválida, dict com a chave "erro". Caso contrário,
        dict com "data_inicio", "fases" (lista com "fase", "objetivo",
        "inicio", "fim", "duracao_dias" para as 4 fases do Roadmap) e
        "semanas_fase_zero" (lista com "semana", "foco", "inicio", "fim"
        para as 4 semanas da Fase Zero).
    """
    inicio = _parse_data(data_inicio)
    if inicio is None:
        return {
            "erro": (
                "DADO INSUFICIENTE: data_inicio inválida, use o formato "
                "'DD/MM/AAAA' ou 'AAAA-MM-DD'."
            )
        }

    fases = []
    cursor = inicio
    for fase in FASES_ROADMAP:
        fim = cursor + timedelta(days=fase["duracao_dias"] - 1)
        fases.append({
            "fase": fase["fase"],
            "objetivo": fase["objetivo"],
            "inicio": cursor.isoformat(),
            "fim": fim.isoformat(),
            "duracao_dias": fase["duracao_dias"],
        })
        cursor = fim + timedelta(days=1)

    semanas_fase_zero = []
    for semana in range(1, 5):
        inicio_semana = inicio + timedelta(days=(semana - 1) * 7)
        fim_semana = inicio + timedelta(days=min(semana * 7, 30) - 1)
        semanas_fase_zero.append({
            "semana": semana,
            "foco": FOCO_SEMANA_FASE_ZERO[semana],
            "inicio": inicio_semana.isoformat(),
            "fim": fim_semana.isoformat(),
        })

    return {
        "data_inicio": inicio.isoformat(),
        "fases": fases,
        "semanas_fase_zero": semanas_fase_zero,
    }


def verificar_prontidao(itens_concluidos: list[str]) -> dict:
    """Verifica a prontidão da PME para certificar a transição ao Nível 1.

    Compara os itens informados como concluídos contra os 9 passos oficiais
    do checklist da Fase Zero (por "id" numérico como string, ex. "3", ou
    pelo "titulo" exato do passo).

    Args:
        itens_concluidos: lista de ids (ex. "1", "2") e/ou títulos exatos
            dos passos do checklist já concluídos pela PME.

    Returns:
        dict com "total_passos", "concluidos", "percentual_conclusao",
        "passos_pendentes" (lista de títulos), "pronto_para_nivel_1" (bool,
        True somente com 100% concluído) e "mensagem".
    """
    informados = {str(item).strip().lower() for item in (itens_concluidos or [])}

    pendentes = []
    concluidos = 0
    for passo in CHECKLIST_FASE_ZERO:
        marcado = (
            str(passo["id"]) in informados
            or passo["titulo"].strip().lower() in informados
        )
        if marcado:
            concluidos += 1
        else:
            pendentes.append(passo["titulo"])

    total = len(CHECKLIST_FASE_ZERO)
    percentual = round(concluidos / total * 100, 1)
    pronto = concluidos == total

    if pronto:
        mensagem = (
            "Todos os passos da Fase Zero foram concluídos. Reaplique o "
            "Questionário de Maturidade para certificar o IM-TI de Nível 1 "
            "junto ao CEO."
        )
    else:
        mensagem = (
            f"Faltam {total - concluidos} de {total} passos antes de "
            "certificar a transição ao Nível 1."
        )

    return {
        "total_passos": total,
        "concluidos": concluidos,
        "percentual_conclusao": percentual,
        "passos_pendentes": pendentes,
        "pronto_para_nivel_1": pronto,
        "mensagem": mensagem,
    }


root_agent = Agent(
    name="agente_fase_zero",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Guia de Implantação Fase Zero: checklist dos 30 dias iniciais, "
        "cronograma calendário (Fase Zero à Três) e verificação de "
        "prontidão para certificar a transição ao Nível 1."
    ),
    instruction=INSTRUCTION,
    tools=[checklist_fase_zero, cronograma_implantacao, verificar_prontidao],
)
