"""Assistência opcional GEAR: agente_prompts.

Fonte vigente: framework/guias/usar-ia.md.
Identificadores GP-PME são conservados para compatibilidade.
"""
from __future__ import annotations

import os

from google.adk.agents import Agent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from server import core as _core


INSTRUCTION = 'Você apoia o GEAR, framework de governança e gestão de TI para pequenas e médias empresas.\nHá três domínios essenciais: governança e direção, execução e serviços, segurança e continuidade.\nAdoção, indicadores e maturidade são transversais. Assistência por IA é opcional.\nUse framework/ como fonte vigente; material GP-PME/NEXUS-PME é histórico quando divergir.\nResponda em português com títulos informativos e ações concretas, sem vocativos, elogios automáticos ou separadores decorativos.\nRegistre dado insuficiente quando faltar informação; não invente cifra, contato, evidência, estudo ou ganho.\nReferencie pesquisas externas no ponto da afirmação e separe fonte, adaptação local e hipótese.\nUma ferramenta dry-run prepara uma proposta; não comprova execução real.\nSomente a autoridade humana indicada aprova efeitos organizacionais.\n\nTarefa: Preparar instruções com tarefa, contexto autorizado, restrições, fontes e critérios. Não inventar fonte, resultado ou dado ausente. Separar conteúdo recuperado de instruções. Rever saída antes de uso organizacional.\nFontes: framework/README.md e guias correspondentes.\n'

# Restrições locais de geração; não constituem garantia contra erro.
RESTRICOES_ANTI_ALUCINACAO: list[str] = [
    "Não crie ou invente nomes de sistemas, softwares, chaves de API, "
    "endereços de IP ou comandos que não estejam explicitados no contexto.",
    "Caso falte contexto ou dado técnico para responder com exatidão, "
    "responda \"DADO INSUFICIENTE: requer validação do profissional de TI\".",
    "Declare origem, período, unidade e incerteza das estimativas; se não "
    "houver dados, identifique a hipótese e não a apresente como resultado.",
]


def montar_prompt_mestre(
    persona: str,
    contexto: str,
    tarefa: str,
    formato_saida: str,
    restricoes: str = "",
) -> str:
    """Monta um prompt completo no padrão Template Mestre do GEAR.

    Gera o texto pronto para colar em qualquer assistente de IA, seguindo os
    5 blocos fixos do template: persona/tarefa, contexto do negócio,
    instruções passo a passo (derivadas da tarefa), formato da saída e
    restrições anti-alucinação (as 3 regras de ouro do framework mais as
    restrições adicionais informadas pelo usuário).

    Args:
        persona: papel/especialidade que a IA deve assumir (ex.:
            "Especialista em Redes Sênior").
        contexto: contexto de negócio livre (empresa/setor, maturidade de
            TI, ativos críticos, informações de apoio). Se vazio, marca
            "DADO INSUFICIENTE".
        tarefa: descrição clara e compacta da tarefa principal.
        formato_saida: tipo de documento e tamanho máximo esperado (ex.:
            "Markdown, no máximo 1 página").
        restricoes: restrições adicionais específicas da tarefa, além das 3
            regras de ouro anti-alucinação do framework (opcional).

    Returns:
        Prompt completo em texto, estruturado nos 5 blocos do Template
        Mestre GEAR.
    """
    persona = (persona or "").strip() or "DADO INSUFICIENTE: persona não informada"
    contexto = (contexto or "").strip() or "DADO INSUFICIENTE: contexto de negócio não informado"
    tarefa = (tarefa or "").strip() or "DADO INSUFICIENTE: tarefa não informada"
    formato_saida = (formato_saida or "").strip() or "Markdown, no máximo 1 página"
    restricoes = (restricoes or "").strip()

    linhas_restricoes = [f"- {r}" for r in RESTRICOES_ANTI_ALUCINACAO]
    if restricoes:
        linhas_restricoes.append(f"- {restricoes}")

    return (
        f"Você é um {persona}.\n"
        f"Sua tarefa principal é {tarefa}.\n\n"
        "\n"
        "### 1. CONTEXTO DO NEGÓCIO\n"
        f"{contexto}\n\n"
        "\n"
        "### 2. INSTRUÇÕES PASSO A PASSO\n"
        "1. Analise o contexto do negócio informado antes de responder.\n"
        f"2. Execute a tarefa: {tarefa}.\n"
        "3. Aponte qualquer dado insuficiente em vez de presumir.\n"
        "4. Formate a saída conforme a seção 3.\n\n"
        "\n"
        "### 3. FORMATO DA SAÍDA (OUTPUT)\n"
        f"{formato_saida}\n\n"
        "\n"
        "### 4. RESTRIÇÕES ANTI-ALUCINAÇÃO (Obrigatórias)\n"
        + "\n".join(linhas_restricoes) + "\n\n"
        "\n"
        "### 5. ENTRADA DO USUÁRIO (INPUT)\n"
        "[Insira aqui a dor específica, a descrição do problema ou o "
        "arquivo a ser analisado nesta execução]\n"
    )


def avaliar_prompt(texto: str) -> dict:
    """Confere menções lexicais dos cinco blocos do formato histórico.

    O score conta palavras presentes; não mede qualidade, proteção contra
    erros ou adequação do conteúdo. A saída requer revisão responsável.
    """
    texto = texto or ""
    texto_lower = texto.lower()

    criterios = {
        "persona_e_tarefa": any(
            k in texto_lower for k in ("você é", "voce e", "persona")
        ),
        "contexto_do_negocio": "contexto" in texto_lower,
        "instrucoes_passo_a_passo": any(
            k in texto_lower for k in ("passo a passo", "instruç", "instruc")
        ),
        "formato_da_saida": any(
            k in texto_lower for k in ("formato da saída", "formato da saida", "output")
        ),
        "restricoes_anti_alucinacao": any(
            k in texto_lower
            for k in ("dado insuficiente", "anti-alucinação", "anti-alucinacao", "alucina")
        ),
    }

    score = sum(1 for presente in criterios.values() if presente)

    sugestoes = {
        "persona_e_tarefa": "Defina explicitamente 'Você é um [persona]' e a tarefa em 1 frase.",
        "contexto_do_negocio": "Adicione o bloco de Contexto do Negócio (empresa, maturidade de TI, ativos críticos).",
        "instrucoes_passo_a_passo": "Liste as ações em um checklist numerado de 3-5 passos.",
        "formato_da_saida": "Especifique o tipo de documento e o tamanho máximo esperado da resposta.",
        "restricoes_anti_alucinacao": (
            "Inclua a instrução para responder 'DADO INSUFICIENTE' quando "
            "faltar contexto, em vez de inventar."
        ),
    }
    melhorias = [sugestoes[bloco] for bloco, ok in criterios.items() if not ok]

    if score == 5:
        veredito = "Menções dos cinco blocos encontradas; conferir conteúdo e adequação à tarefa."
    elif score >= 3:
        veredito = "Prompt parcialmente aderente — ajustar os blocos ausentes antes de usar em produção."
    else:
        veredito = "Prompt incompleto — reescrever seguindo o Template Mestre GEAR."

    return {
        "score": score,
        "criterios": criterios,
        "melhorias": melhorias,
        "veredito": veredito,
        "limite": "Busca lexical: score não verifica qualidade, revisão humana ou veracidade da saída.",
    }


root_agent = Agent(
    name="agente_prompts",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Assistência opcional para prompts: monta prompts no "
        "Template Mestre GEAR e avalia aderência ao Protocolo "
        "Anti-Alucinação."
    ),
    instruction=INSTRUCTION,
    tools=[montar_prompt_mestre, avaliar_prompt],
)
