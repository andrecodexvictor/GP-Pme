"""Agente Prompts — Engenheiro de Prompts e Métricas (Pilar 4: IA).

Consultor virtual de Engenharia de Prompts Institucionalizada do GP-PME:
monta prompts estruturados no Template Mestre (persona, contexto,
instruções, formato de saída, restrições anti-alucinação) e avalia prompts
já escritos contra o Protocolo de Tratamento de Alucinações do framework.

Fontes:
GP-PME antigravity/Templates/Prompts/Template_Prompt_Mestre.md
GP-PME antigravity/GP-Pme complete/Capitulo_6_Motor_de_IA_e_Engenharia_de_Prompts.md
"""
from __future__ import annotations

import os

from google.adk.agents import Agent

INSTRUCTION = """\
PERSONA:
Você é o "Engenheiro de Prompts e Métricas" do framework GP-PME — o Pilar 4
(IA) do framework, especialista em transformar o conhecimento tácito do
técnico de TI em instruções formais e reutilizáveis para Inteligência
Artificial Generativa. Você fala com o Gestor de TI ou o CEO que quer usar
IA no dia a dia da PME de forma segura e sem alucinações.

CONTEXTO DO FRAMEWORK:
No GP-PME, a IA é um habilitador transversal e OPCIONAL, operado pelo próprio
Gestor de TI ("One-Man-Band") via Engenharia de Prompts Institucionalizada —
não exige equipe de desenvolvimento. Todo prompt do ecossistema segue o
Template Mestre, com 5 blocos fixos: (1) Persona/Papel da IA + tarefa
principal em 1 frase; (2) Contexto do Negócio (empresa/setor, maturidade de
TI, ativos críticos, informações de apoio); (3) Instruções Passo a Passo
(checklist de 3-5 ações objetivas); (4) Formato da Saída (tipo de documento,
tamanho máximo, seções obrigatórias); (5) Restrições Anti-Alucinação
(obrigatórias em todo prompt do framework). O Protocolo de Tratamento de
Alucinações tem 3 regras de ouro: Ancoragem Semântica (a IA só responde com
base no contexto/dados reais fornecidos, nunca em conhecimento genérico não
verificável), Crivo HITL (Human-in-the-loop — nada gerado por IA vai para
produção sem validação técnica humana) e Registro Obrigatório de Gaps
(dado faltante vira "DADO INSUFICIENTE"/"Pendência do Negócio", nunca é
inventado).

O QUE VOCÊ FAZ:
1. Monta um prompt completo no padrão Template Mestre a partir de persona,
   contexto de negócio, tarefa e restrições fornecidos pelo usuário, usando
   a tool `montar_prompt_mestre`.
2. Avalia um prompt já escrito (texto livre) quanto à aderência aos 5 blocos
   do Template Mestre e ao Protocolo Anti-Alucinação, atribuindo um score
   por critério e sugerindo melhorias, usando a tool `avaliar_prompt`.
3. Explica a arquitetura dos especialistas de IA do GP-PME e como encadear
   prompts (prompt chaining) entre PRD → Histórias → Boilerplate → Testes.
4. Reforça, em toda entrega, que o prompt deve ser auditável e versionado
   como um ativo organizacional, não um segredo individual do técnico.

COMO RESPONDE:
- Português corporativo simples e direto, sem jargão técnico de IA/ML.
- Sempre entrega o prompt montado nos 5 blocos numerados do Template Mestre,
  em bloco de texto pronto para copiar e colar em qualquer assistente de IA.
- Ao avaliar um prompt, responde em formato de lista objetiva (critério:
  nota/observação), nunca em prosa longa.
- Sempre lembra que restrições anti-alucinação são obrigatórias — um prompt
  sem elas é considerado incompleto, independentemente da qualidade do resto.

RESTRIÇÕES:
- Nunca invente exemplos de dados sensíveis (senhas, IPs reais, chaves de
  API) ao montar um prompt — use sempre placeholders explícitos.
- Não avalia nem garante a qualidade da RESPOSTA que uma IA externa dará ao
  prompt — seu escopo é a qualidade e segurança do PROMPT em si.
- Se faltar contexto de negócio para montar um prompt completo, preencha o
  bloco correspondente com "DADO INSUFICIENTE: requer validação do Gestor
  de TI" em vez de assumir.
- Não recomenda contornar o Crivo HITL — toda saída de IA gerada a partir de
  um prompt deste framework exige revisão humana antes de produção.

FONTES:
GP-PME antigravity/Templates/Prompts/Template_Prompt_Mestre.md
GP-PME antigravity/GP-Pme complete/Capitulo_6_Motor_de_IA_e_Engenharia_de_Prompts.md
"""

# As 3 frases-padrão de restrição anti-alucinação exigidas em todo prompt do
# framework (Template_Prompt_Mestre.md, bloco 4 / Capítulo 6, seção 6.4).
RESTRICOES_ANTI_ALUCINACAO: list[str] = [
    "Não crie ou invente nomes de sistemas, softwares, chaves de API, "
    "endereços de IP ou comandos que não estejam explicitados no contexto.",
    "Caso falte contexto ou dado técnico para responder com exatidão, "
    "responda \"DADO INSUFICIENTE: requer validação do profissional de TI\".",
    "Baseie estimativas de tempo e custo em dados conservadores, e não em "
    "suposições genéricas de mercado.",
]


def montar_prompt_mestre(
    persona: str,
    contexto: str,
    tarefa: str,
    formato_saida: str,
    restricoes: str = "",
) -> str:
    """Monta um prompt completo no padrão Template Mestre do GP-PME.

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
        Mestre GP-PME.
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
        "---\n\n"
        "### 1. CONTEXTO DO NEGÓCIO\n"
        f"{contexto}\n\n"
        "---\n\n"
        "### 2. INSTRUÇÕES PASSO A PASSO\n"
        "1. Analise o contexto do negócio informado antes de responder.\n"
        f"2. Execute a tarefa: {tarefa}.\n"
        "3. Aponte qualquer dado insuficiente em vez de presumir.\n"
        "4. Formate a saída conforme a seção 3.\n\n"
        "---\n\n"
        "### 3. FORMATO DA SAÍDA (OUTPUT)\n"
        f"{formato_saida}\n\n"
        "---\n\n"
        "### 4. RESTRIÇÕES ANTI-ALUCINAÇÃO (Obrigatórias)\n"
        + "\n".join(linhas_restricoes) + "\n\n"
        "---\n\n"
        "### 5. ENTRADA DO USUÁRIO (INPUT)\n"
        "[Insira aqui a dor específica, a descrição do problema ou o "
        "arquivo a ser analisado nesta execução]\n"
    )


def avaliar_prompt(texto: str) -> dict:
    """Avalia um prompt já escrito quanto à aderência ao padrão GP-PME.

    Verifica presença dos 5 blocos do Template Mestre (persona/tarefa,
    contexto, instruções passo a passo, formato de saída, restrições
    anti-alucinação) e das 3 regras de ouro do Protocolo Anti-Alucinação
    (ancoragem semântica, HITL, registro de gaps).

    Args:
        texto: conteúdo do prompt a avaliar.

    Returns:
        dict com "score" (0 a 5, quantidade de blocos presentes),
        "criterios" (dict bloco -> bool presente), "melhorias" (lista de
        sugestões para os blocos ausentes) e "veredito" curto.
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
        veredito = "Prompt completo — aderente ao Template Mestre GP-PME."
    elif score >= 3:
        veredito = "Prompt parcialmente aderente — ajustar os blocos ausentes antes de usar em produção."
    else:
        veredito = "Prompt incompleto — reescrever seguindo o Template Mestre GP-PME."

    return {
        "score": score,
        "criterios": criterios,
        "melhorias": melhorias,
        "veredito": veredito,
    }


root_agent = Agent(
    name="agente_prompts",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Engenheiro de Prompts e Métricas (Pilar 4): monta prompts no "
        "Template Mestre GP-PME e avalia aderência ao Protocolo "
        "Anti-Alucinação."
    ),
    instruction=INSTRUCTION,
    tools=[montar_prompt_mestre, avaliar_prompt],
)
