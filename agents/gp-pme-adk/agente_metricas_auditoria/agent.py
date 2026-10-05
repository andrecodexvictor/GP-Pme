"""Assistência opcional GEAR: agente_metricas_auditoria.

Fonte vigente: framework/indicadores/financeiros.md e framework/indicadores/operacionais.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os

from google.adk.agents import Agent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server import core as _core


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Calcular indicadores com origem, janela e unidade. Distinguir ROI líquido de razão bruta, capacidade potencial de redução de despesa e proporção legada de DAN financeiro. Não inferir risco financeiro das faixas históricas de inventário.\nFontes: framework/README.md e guias correspondentes.\n'


def calcular_kpis(horas_indisponibilidade: float, horas_totais: float, tempos_resposta_horas: list, notas_satisfacao: list) -> dict:
    """Indicadores operacionais com validação de domínios."""
    return _core.calcular_kpis(horas_indisponibilidade, horas_totais, tempos_resposta_horas, notas_satisfacao)


def calcular_dan(itens_legados: int, itens_totais: int) -> dict:
    """Alias histórico da proporção de inventário; não DAN financeiro."""
    return _core.calcular_dan(itens_legados, itens_totais)


def calcular_cot(custo_otimizacao: float, ganho_mensal: float, custo_recorrente_mensal: float = 0) -> dict:
    """Retorno líquido com custo recorrente e horizonte de 12 meses."""
    return _core.calcular_cot(custo_otimizacao, ganho_mensal, custo_recorrente_mensal)


def checklist_auditoria_hitl() -> list:
    """Prepara dez verificações locais de dados, requisitos, segurança e código.

    Todos os itens começam pendentes. O roteiro não substitui conferência,
    não comprova aprovação e não garante ausência de erro.
    """
    checks = [
        (
            "Bloco 1: Rastreabilidade e fontes",
            "Check 1.1: Conferência de dados e hipóteses",
            "O documento gerado baseia-se apenas nas informações, sistemas e "
            "premissas explicitamente fornecidas no prompt/contexto do projeto?",
            "O documento cita bancos de dados, chaves de API, rotas ou cargos "
            "inexistentes na empresa.",
        ),
        (
            "Bloco 1: Rastreabilidade e fontes",
            "Check 1.2: Origem e disponibilidade das fontes",
            "As referências a softwares/versões/infraestruturas citam exatamente "
            "os ativos listados no Inventário 80/20 da PME?",
            "Ferramenta é apresentada como já disponível sem evidência, ou "
            "uma proposta omite custo, autorização e restrições.",
        ),
        (
            "Bloco 1: Rastreabilidade e fontes",
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
            "Check 2.3: Exclusões acordadas",
            "O PRD informa exclusões, prazo e capacidade acordados para o piloto?",
            "Escopo sem limites ou alteração sem decisão registrada.",
        ),
        (
            "Bloco 3: Segurança e continuidade",
            "Check 3.1: Validação de Privilégio Mínimo (LUA)",
            "A recomendação/código segue o menor privilégio, sem exigir admin "
            "global para operações simples?",
            "O código exige acesso root/admin no banco para um SELECT simples.",
        ),
        (
            "Bloco 3: Segurança e continuidade",
            "Check 3.2: Ativação de MFA e Controles Simples",
            "A proposta examina risco, cobertura, compatibilidade e custo dos "
            "controles, incluindo acesso e recuperação?",
            "Custo, exposição ou exceção omitidos da decisão.",
        ),
        (
            "Bloco 4: Engenharia de Código (Boilerplates)",
            "Check 4.1: Placeholder de Lógica de Negócio",
            "A lógica crítica tem requisitos, revisão responsável e testes; "
            "placeholders e limitações estão explícitos?",
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
        "Assistência opcional para indicadores e roteiro de conferência "
        "humana; não certifica dados ou entregas."
    ),
    instruction=INSTRUCTION,
    tools=[calcular_kpis, calcular_dan, calcular_cot, checklist_auditoria_hitl],
)
