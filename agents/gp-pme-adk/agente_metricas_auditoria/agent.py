"""Agente Métricas e Auditoria — Termômetro de KPIs e Portão HITL.

Consultor virtual de métricas operacionais/financeiras de TI para PMEs,
destilado do Guia de KPIs e Vitórias Rápidas (IDSC, TMpR, ISU, DAN, COT) e
do Checklist de Auditoria Human-in-the-Loop (HITL) do framework GP-PME.
Calcula os 3 KPIs Visíveis, a Dívida de Arquitetura Normalizada (DAN), o
payback do Custo de Otimização Tecnológica (COT) e monta o checklist de
auditoria obrigatório antes de homologar qualquer entregável de IA.

Fontes:
GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md
GP-PME antigravity/Templates/AI-Skills-and-Agents/Template_Checklist_Auditoria_HITL.md
"""
from __future__ import annotations

import os

from google.adk.agents import Agent

INSTRUCTION = """\
PERSONA:
Você é o "Termômetro de KPIs e Portão HITL" do framework GP-PME — um
Analista de Métricas e Auditor de Qualidade virtual, especialista em
traduzir a operação de TI de uma PME em indicadores financeiros e
operacionais objetivos, e em aplicar o filtro final de auditoria humana
sobre entregáveis gerados por IA. Você fala com o Gestor de TI e prepara
os números que serão apresentados ao CEO no CD-TI Lite.

CONTEXTO DO FRAMEWORK:
O GP-PME mede o sucesso da TI Enxuta através de 3 KPIs Visíveis coletados
na Fase Zero (Semana 4): IDSC (Índice de Disponibilidade de Serviços
Críticos, meta > 99,5%), TMpR (Tempo Médio para Resolução, meta < 4h para
incidentes de alta gravidade) e ISU (Índice de Satisfação do Usuário,
notas de 1 a 5, meta > 4,5). Em estágios mais maduros (Fase 3), a TI
traduz a defasagem tecnológica em dois indicadores financeiros: a DAN
(Dívida de Arquitetura Normalizada — quantifica os "juros" pagos pela PME
em lentidão e bugs por manter sistemas legados) e o COT (Custo de
Otimização Tecnológica — o "pagamento do principal" para eliminar essa
dívida, cujo retorno é medido em payback e ROI). Nenhum entregável gerado
por IA (código, PRD, análise de risco) chega à produção sem passar pelo
Checklist de Auditoria HITL — o portão de homologação de 5 minutos que
protege a PME contra alucinações e falhas técnicas.

O QUE VOCÊ FAZ:
1. Calcula os 3 KPIs Visíveis (IDSC, TMpR, ISU) a partir de dados brutos
   de disponibilidade, tempos de resposta e notas de satisfação, usando a
   tool `calcular_kpis`.
2. Calcula a DAN (proxy simplificado por proporção de itens legados sobre
   o total do inventário, quando não há dados de horas/orçamento
   disponíveis) e classifica a zona de risco (Saudável/Alerta/Crítico),
   usando a tool `calcular_dan`.
3. Calcula o payback e o ROI anual de um investimento de COT a partir do
   custo de otimização e do ganho mensal recorrente, usando a tool
   `calcular_cot`.
4. Monta o Checklist de Auditoria HITL completo (4 blocos) com status
   "pendente" para cada item, usando a tool `checklist_auditoria_hitl`.

COMO RESPONDE:
- Português corporativo simples, direto, com os números sempre
  acompanhados da meta recomendada do framework para contexto.
- Sempre indica se o resultado calculado está dentro ou fora da meta
  (ex.: "IDSC 98,2% — ABAIXO da meta de 99,5%").
- Estrutura saídas em blocos objetivos (tabela ou lista), nunca em prosa
  longa.
- Ao calcular a DAN, sempre lembra que o cálculo aqui é um proxy por
  contagem de itens; a fórmula financeira completa (horas de refatoração
  x custo-hora / orçamento anual) exige dados que só o Gestor de TI possui.

RESTRIÇÕES:
- Nunca inventa dados de entrada (horas de indisponibilidade, notas de
  satisfação, custos). Se um dado obrigatório estiver ausente ou for
  inconsistente (ex.: divisão por zero), retorna explicitamente "DADO
  INSUFICIENTE: requer validação do Gestor de TI" em vez de estimar.
- Não gera código, scripts ou configurações de servidor — escopo é
  estritamente métricas e auditoria de entregáveis.
- O Checklist de Auditoria HITL é sempre gerado com status "pendente";
  apenas um humano (Gestor de TI ou PO) pode marcar itens como aprovados.
- Decisões de aprovação/reprovação de entregáveis de IA e de investimentos
  em COT são sempre humanas (Human-in-the-loop); você calcula e organiza,
  o Gestor de TI e o CD-TI Lite decidem.

FONTES:
GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md
GP-PME antigravity/Templates/AI-Skills-and-Agents/Template_Checklist_Auditoria_HITL.md
"""


def calcular_kpis(
    horas_indisponibilidade: float,
    horas_totais: float,
    tempos_resposta_horas: list,
    notas_satisfacao: list,
) -> dict:
    """Calcula os 3 KPIs Visíveis do GP-PME: IDSC, TMpR e ISU.

    IDSC = ((horas_totais - horas_indisponibilidade) / horas_totais) x 100
    TMpR = média das horas entre abertura e fechamento dos chamados
    ISU = média das notas de satisfação (escala de 1 a 5)

    Args:
        horas_indisponibilidade: horas de inatividade dos serviços
            críticos no período em horário comercial.
        horas_totais: total de horas comerciais do período (ex.: horas
            comerciais do mês).
        tempos_resposta_horas: lista de horas decorridas do registro ao
            fechamento de cada chamado concluído no período.
        notas_satisfacao: lista de notas de 1 a 5 coletadas nas pesquisas
            de satisfação pós-atendimento.

    Returns:
        dict com "idsc_percent", "idsc_meta_atingida" (bool), "tmpr_horas",
        "tmpr_meta_atingida" (bool), "isu_media", "isu_meta_atingida"
        (bool). Se `horas_totais` for <= 0 ou as listas estiverem vazias,
        o respectivo indicador retorna "DADO INSUFICIENTE".
    """
    resultado: dict = {}

    if horas_totais and horas_totais > 0:
        idsc = ((horas_totais - horas_indisponibilidade) / horas_totais) * 100
        resultado["idsc_percent"] = round(idsc, 2)
        resultado["idsc_meta_atingida"] = idsc > 99.5
    else:
        resultado["idsc_percent"] = "DADO INSUFICIENTE"
        resultado["idsc_meta_atingida"] = "DADO INSUFICIENTE"

    if tempos_resposta_horas:
        tmpr = sum(tempos_resposta_horas) / len(tempos_resposta_horas)
        resultado["tmpr_horas"] = round(tmpr, 2)
        resultado["tmpr_meta_atingida"] = tmpr < 4.0
    else:
        resultado["tmpr_horas"] = "DADO INSUFICIENTE"
        resultado["tmpr_meta_atingida"] = "DADO INSUFICIENTE"

    if notas_satisfacao:
        isu = sum(notas_satisfacao) / len(notas_satisfacao)
        resultado["isu_media"] = round(isu, 2)
        resultado["isu_meta_atingida"] = isu > 4.5
    else:
        resultado["isu_media"] = "DADO INSUFICIENTE"
        resultado["isu_meta_atingida"] = "DADO INSUFICIENTE"

    return resultado


def calcular_dan(itens_legados: int, itens_totais: int) -> dict:
    """Calcula a Dívida de Arquitetura Normalizada (DAN) por proxy de inventário.

    Proxy simplificado da DAN (itens legados / itens totais do inventário
    de TI) para uso quando o Gestor de TI ainda não levantou os dados de
    horas de refatoração, custo-hora e orçamento anual exigidos pela
    fórmula financeira completa do guia. Classifica o resultado nas zonas
    de risco oficiais do GP-PME.

    Args:
        itens_legados: quantidade de sistemas/ativos legados ou desatualizados
            no inventário de TI.
        itens_totais: quantidade total de sistemas/ativos no inventário.

    Returns:
        dict com "dan" (float, 0 a 1), "zona" ("saudavel"/"alerta"/
        "critico"), "recomendacao" (str). Se `itens_totais` for <= 0,
        retorna "DADO INSUFICIENTE" nos três campos.
    """
    if not itens_totais or itens_totais <= 0:
        return {
            "dan": "DADO INSUFICIENTE",
            "zona": "DADO INSUFICIENTE",
            "recomendacao": "Informe o total de itens do inventário 80/20 para calcular a DAN.",
        }

    dan = itens_legados / itens_totais

    if dan < 0.15:
        zona = "saudavel"
        recomendacao = (
            "Dívida técnica sob controle. Mantenha o ritmo de modernização "
            "atual e priorize inovação (Fase 2) sem urgência de investimento."
        )
    elif dan <= 0.35:
        zona = "alerta"
        recomendacao = (
            "Juros da dívida técnica começam a cobrar preço em atrasos e "
            "bugs. Planeje um investimento de COT nos próximos ciclos do "
            "CD-TI Lite."
        )
    else:
        zona = "critico"
        recomendacao = (
            "Alto risco de parada de faturamento. Requer intervenção "
            "imediata e aporte de COT aprovado com urgência pelo comitê "
            "CD-TI Lite."
        )

    return {"dan": round(dan, 4), "zona": zona, "recomendacao": recomendacao}


def calcular_cot(custo_otimizacao: float, ganho_mensal: float) -> dict:
    """Calcula o payback e o ROI anual de um investimento de COT.

    Payback (meses) = custo_otimizacao / ganho_mensal
    ROI anual (%) = (ganho_mensal x 12 / custo_otimizacao) x 100

    Args:
        custo_otimizacao: investimento total (direto + indireto) do Custo
            de Otimização Tecnológica.
        ganho_mensal: redução de custo ou ganho de produtividade mensal
            recorrente gerado pela otimização.

    Returns:
        dict com "payback_meses" (float) e "roi_anual_percent" (float).
        Se `custo_otimizacao` ou `ganho_mensal` forem <= 0, retorna
        "DADO INSUFICIENTE" nos dois campos.
    """
    if not custo_otimizacao or custo_otimizacao <= 0 or not ganho_mensal or ganho_mensal <= 0:
        return {
            "payback_meses": "DADO INSUFICIENTE",
            "roi_anual_percent": "DADO INSUFICIENTE",
        }

    payback_meses = custo_otimizacao / ganho_mensal
    roi_anual_percent = (ganho_mensal * 12 / custo_otimizacao) * 100

    return {
        "payback_meses": round(payback_meses, 2),
        "roi_anual_percent": round(roi_anual_percent, 2),
    }


def checklist_auditoria_hitl() -> list:
    """Monta o Checklist de Auditoria Human-in-the-Loop (HITL) completo.

    Reproduz os 4 blocos oficiais do template de auditoria (Rastreabilidade
    e Grounding, Auditoria de Requisitos/PRD, Segurança e Resiliência
    NIST-Lite, Engenharia de Código) que todo entregável gerado por IA
    deve passar antes de homologação. Todos os itens nascem com status
    "pendente" — a aprovação é sempre um ato humano.

    Returns:
        Lista de dicts, cada um com "bloco", "check", "o_que_verificar",
        "criterio_falha" e "status" (sempre "pendente" nesta geração).
    """
    checks = [
        (
            "Bloco 1: Rastreabilidade e Grounding",
            "Check 1.1: Sem Dados Inventados (Zero Alucinação)",
            "O documento gerado baseia-se apenas nas informações, sistemas e "
            "premissas explicitamente fornecidas no prompt/contexto do projeto?",
            "O documento cita bancos de dados, chaves de API, rotas ou cargos "
            "inexistentes na empresa.",
        ),
        (
            "Bloco 1: Rastreabilidade e Grounding",
            "Check 1.2: Citação Direta de Fontes Homologadas",
            "As referências a softwares/versões/infraestruturas citam exatamente "
            "os ativos listados no Inventário 80/20 da PME?",
            "A IA propõe ferramentas que a empresa não adquiriu ou marcas não "
            "autorizadas.",
        ),
        (
            "Bloco 1: Rastreabilidade e Grounding",
            "Check 1.3: Tratamento de Destaques e Gaps (\"Dado Insuficiente\")",
            "Em caso de dado ausente, a IA usou o marcador \"DADO INSUFICIENTE\" "
            "em vez de supor?",
            "A IA tomou uma decisão técnica arriscada sem confirmar premissas "
            "(ex.: escolheu método de backup sem checar espaço em disco).",
        ),
        (
            "Bloco 2: Auditoria de Requisitos (PRD)",
            "Check 2.1: Histórias de Usuário Viáveis",
            "As histórias de usuário são simples e condizentes com o fluxo real "
            "de trabalho da PME?",
            "A história exige um painel burocrático que gera gargalo comercial.",
        ),
        (
            "Bloco 2: Auditoria de Requisitos (PRD)",
            "Check 2.2: Critérios de Aceitação Testáveis (Dado/Quando/Então)",
            "Os critérios descrevem testes objetivos \"passa ou não passa\"?",
            "Critérios vagos como \"deve carregar rápido\" ou \"deve ser bonito\".",
        ),
        (
            "Bloco 2: Auditoria de Requisitos (PRD)",
            "Check 2.3: Blindagem do Escopo Negativo",
            "O PRD lista claramente os recursos banidos do MVP de 2 semanas?",
            "Escopo em aberto, permitindo perfumaria técnica fora do prazo.",
        ),
        (
            "Bloco 3: Segurança e Resiliência (NIST-Lite)",
            "Check 3.1: Validação de Privilégio Mínimo (LUA)",
            "A recomendação/código segue o menor privilégio, sem exigir admin "
            "global para operações simples?",
            "O código exige acesso root/admin no banco para um SELECT simples.",
        ),
        (
            "Bloco 3: Segurança e Resiliência (NIST-Lite)",
            "Check 3.2: Ativação de MFA e Controles Simples",
            "As propostas evitam ferramentas caras e priorizam MFA, backup e "
            "senha forte de custo zero/mínimo?",
            "Recomendação de investimento caro incompatível com a TI Enxuta.",
        ),
        (
            "Bloco 4: Engenharia de Código (Boilerplates)",
            "Check 4.1: Placeholder de Lógica de Negócio",
            "O código restringe-se ao boilerplate estruturado, com placeholders "
            "claros para a lógica crítica de negócio ser revisada por humano?",
            "A IA gerou lógica completa de faturamento/cálculo crítico sem "
            "auditoria.",
        ),
        (
            "Bloco 4: Engenharia de Código (Boilerplates)",
            "Check 4.2: Tratamento de Erros e Validações Primárias",
            "O código valida entradas (evita injeção/dados vazios) e trata "
            "falhas sem expor mensagens internas do sistema?",
            "Código vulnerável a SQL Injection ou que expõe caminhos internos "
            "em exceções.",
        ),
    ]
    return [
        {
            "bloco": bloco,
            "check": check,
            "o_que_verificar": o_que_verificar,
            "criterio_falha": criterio_falha,
            "status": "pendente",
        }
        for bloco, check, o_que_verificar, criterio_falha in checks
    ]


root_agent = Agent(
    name="agente_metricas_auditoria",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Termômetro de KPIs (IDSC, TMpR, ISU, DAN, COT) e Portão de "
        "Auditoria HITL para entregáveis de IA no framework GP-PME."
    ),
    instruction=INSTRUCTION,
    tools=[calcular_kpis, calcular_dan, calcular_cot, checklist_auditoria_hitl],
)
