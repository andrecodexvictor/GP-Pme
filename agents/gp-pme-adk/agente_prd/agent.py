"""Assistência opcional GEAR: agente_prd.

Fonte vigente: framework/templates/prd-aceite.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os
from datetime import date

from google.adk.agents import Agent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server import core as _core


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Preparar problema, evidência, beneficiário, escopo, exclusões, dependências, aceite, risco e plano de retorno. Critérios precisam ser observáveis. Aceite não demonstra benefício financeiro; hipótese exige acompanhamento.\nFontes: framework/README.md e guias correspondentes.\n'

# Títulos históricos preservados para compatibilidade da triagem lexical.
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
    """Gera o esqueleto de um PRD Simplificado GEAR pronto para preencher.

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
        f"# PRD [GEAR]: {nome_projeto}\n\n"
        "## 1. Visão Geral e Valor de Negócio\n"
        f"- Data de Solicitação: {hoje}  |  Versão: 1.0\n"
        "- Dono do Produto (Product Owner): [Nome do Gestor/Solicitante]\n"
        "- Técnico Executor: [Nome do Técnico ou Equipe de TI]\n"
        "- Dor de Negócio (O Problema): [até 3 frases sobre o problema "
        "observado e sua evidência]\n"
        "- Dependências e fontes: [serviço, sistema, origem do dado e responsável]\n"
        "- Objetivo do piloto: [resultado, escopo, capacidade e prazo acordados]\n\n"
        "## 2. Histórias de Usuário\n"
        "- História 1: Como [perfil do colaborador], eu quero [funcionalidade "
        "simplificada] para que eu possa [benefício de negócio].\n"
        "- História 2: Como [perfil], eu quero [funcionalidade] para que eu "
        "possa [benefício].\n\n"
        "## 3. Critérios de Aceitação (Modelo Passa / Não Passa)\n"
        "- Cenário 1: Dado que [contexto inicial], quando [ação executada], "
        "então [resultado esperado].\n"
        "- Cenário 2: Dado que [contexto], quando [ação], então [resultado].\n\n"
        "## 4. Escopo Negativo (exclusões acordadas)\n"
        "- Exclusão 1: [item fora do escopo acordado]\n"
        "- Exclusão 2: [item excluído nesta fase]\n\n"
        "## 5. Requisitos Não Funcionais\n"
        "- Desempenho: [ex.: telas e consultas em até 2s em conexão móvel "
        "comum]\n"
        "- Segurança: [ex.: autenticação individual + privilégio mínimo (LUA)]\n"
        "- Usabilidade: [ex.: interface responsiva, sem manual complexo]\n\n"
        "- Risco e plano de retorno: [efeito, condição de suspensão e recuperação]\n\n"
        "## 6. Métrica de Negócio Afetada (KPI do Projeto)\n"
        "- Métrica de Negócio: [ex.: redução de X% no TMpR do setor / "
        "aumento de Y% em faturamento/ISU; hipótese a verificar]\n"
        "- Origem, janela, linha de base e responsável pela medição: [...]\n\n"
        "## 7. Aprovações e revisão responsável\n"
        "- Validação Técnica (TI/QA): [ ] Aprovado  [ ] Necessita Ajustes  |  "
        "Data: ___/___/___\n"
        "- Assinatura do Aprovador (PO/Negócios): "
        "_____________________________________\n"
    )


def validar_prd(texto: str) -> dict:
    """Confere presença lexical dos títulos históricos e palavras de aceite.

    Presença não comprova conteúdo, viabilidade ou aprovação. O campo
    completo permanece por compatibilidade e significa apenas esta triagem.
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
            "Títulos e palavras esperados encontrados. Conferir requisitos, "
            "aceite, dependências e aprovação responsável."
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
        "limite": "Triagem lexical: não valida coerência, viabilidade, critérios ou aprovação. completo é um campo estrutural de compatibilidade.",
    }


root_agent = Agent(
    name="agente_prd",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Analista de Execução Ágil: prepara rascunhos e verifica menções em PRDs GEAR "
        "(1-2 páginas), histórias de usuário e critérios Dado/Quando/Então."
    ),
    instruction=INSTRUCTION,
    tools=[esqueleto_prd, validar_prd],
)
