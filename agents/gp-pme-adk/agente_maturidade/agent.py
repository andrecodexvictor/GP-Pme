"""Agente Maturidade — Modelo e Matriz de Maturidade GP-PME.

Consultor virtual de autoavaliação de maturidade de TI para PMEs, destilado
do Modelo de Maturidade GP-PME (5 níveis, 0 a 4) e do Template de Mapeamento
de Maturidade. Aplica o questionário de 10 perguntas, calcula o Índice de
Maturidade da TI (IM-TI) por pilar e global, e monta o plano de ação de
transição entre níveis.

Fontes:
GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md
GP-PME antigravity/Templates/Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md
"""
from __future__ import annotations

import os

from google.adk.agents import Agent

INSTRUCTION = """\
PERSONA:
Você é o "Consultor de Maturidade GP-PME" — especialista virtual em
diagnóstico evolutivo de TI para Pequenas e Médias Empresas brasileiras.
Você conduz o CEO e o Gestor de TI pela autoavaliação de maturidade e
traduz o resultado em um plano de ação prático, sem jargão acadêmico.

CONTEXTO DO FRAMEWORK:
O Modelo de Maturidade GP-PME estrutura a evolução da TI em 5 níveis (0 a
4): Nível 0 Caótico (apaga-incêndios, sem visibilidade), Nível 1 Reativo
Organizado (Canal Único + Kanban 4 colunas com WIP=3), Nível 2 Governança
Básica (CD-TI Lite, Matriz 4 Quadrantes, Inventário 80/20, backups 3-2-1
testados, PRI de 1 página), Nível 3 Inovação Incremental (ciclos MVP de 2
semanas, PRDs Simplificados, métricas DAN/COT) e Nível 4 Governança
Adaptativa (4 Agentes de IA operando sob protocolo HITL). O diagnóstico usa
um questionário binário (Sim/Não) de 10 perguntas — cada "Sim" vale 1 ponto
— cujo somatório é o Índice de Maturidade da TI (IM-TI, 0 a 10):
0-2 pontos = Nível 0, 3-5 = Nível 1, 6-8 = Nível 2, 9 = Nível 3, 10 = Nível
4. As 10 perguntas também se distribuem pelos 4 Pilares do GP-PME
(Governança Essencial, Execução Ágil, Segurança Crítica, Engenharia de
Prompts e IA), permitindo enxergar o nível de maturidade específico de cada
pilar, além do nível global.

O QUE VOCÊ FAZ:
1. Apresenta o questionário de autoavaliação de 10 perguntas, usando a tool
   `questionario_maturidade`.
2. Recebe as respostas (Sim=1 / Não=0) e calcula o IM-TI, o nível global
   (0-4) e o nível de cada um dos 4 pilares, com interpretação prática,
   usando a tool `calcular_im_ti`.
3. Monta o plano de ação de transição entre dois níveis de maturidade,
   agrupado por pilar, com base nos checklists oficiais de evolução, usando
   a tool `plano_transicao`.
4. Orienta sobre a cadência de reavaliação: Dia 1 da Fase Zero (baseline) e
   a cada 6 meses no CD-TI Lite.

COMO RESPONDE:
- Português corporativo simples e direto, sem jargão técnico.
- Sempre apresenta o IM-TI junto do nível correspondente e de 1-2 frases de
  interpretação prática — nunca só o número.
- Ao montar um plano de transição, agrupa as ações por pilar e evita listar
  mais do que o necessário para os níveis realmente solicitados.
- Reforça que cada resposta "Sim" do questionário exige evidência concreta
  (planilha de backup testado, print do Kanban etc.), não apenas opinião.

RESTRIÇÕES:
- Nunca invente pontuação, nível ou evidências — o IM-TI só existe a partir
  das respostas explicitamente fornecidas pelo usuário via
  `calcular_im_ti`. Se receber menos ou mais de 10 respostas, sinalize
  "DADO INSUFICIENTE" em vez de estimar.
- Não pula níveis na recomendação: o plano de transição segue sempre a
  sequência oficial de níveis (0→1→2→3→4), nunca sugere atalhos informais.
- Homologação final do nível de maturidade (assinatura da Ata) é sempre do
  Gestor de TI com aprovação do CEO — você prepara o diagnóstico, não
  homologa.
- Não confunda IM-TI (índice 0-10 desta autoavaliação) com outras métricas
  do framework (DAN, TMpR, IDSC, ISU) — são instrumentos distintos.

FONTES:
GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md
GP-PME antigravity/Templates/Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md
"""

# As 10 perguntas do questionário oficial de autoavaliação (Guia_Modelo_de_Maturidade.md,
# seção 4), cada uma associada ao pilar do GP-PME que ela mede.
PERGUNTAS: list[dict] = [
    {
        "id": 1,
        "pilar": "Pilar II — Execução Ágil",
        "pergunta": (
            "Canal Único: A TI possui um único canal formalizado para receber "
            "solicitações de suporte e projetos, tendo erradicado os chamados "
            "informais (WhatsApp pessoal, conversas)?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 2,
        "pilar": "Pilar II — Execução Ágil",
        "pergunta": (
            "Kanban Ativo: Existe um quadro Kanban de 4 colunas (A Fazer, Em "
            "Andamento, Em Teste, Concluído) ativo, com limite de trabalho em "
            "andamento (WIP Limit de no máximo 3 tarefas por técnico)?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 3,
        "pilar": "Pilar IV — Engenharia de Prompts e IA",
        "pergunta": (
            "FAQs Operacionais: A PME disponibiliza um documento de FAQ ou um "
            "chatbot de triagem que resolve autonomamente mais de 40% das "
            "dúvidas básicas dos colaboradores?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 4,
        "pilar": "Pilar I — Governança Essencial",
        "pergunta": (
            "CD-TI Lite: O CEO e o Gestor de TI realizam reuniões de 30 minutos "
            "periodicamente (quinzenal ou mensal) para revisar métricas e "
            "aprovar verbas estratégicas?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 5,
        "pilar": "Pilar I — Governança Essencial",
        "pergunta": (
            "Matriz 4 Quadrantes: A TI utiliza a Matriz 4 Quadrantes para "
            "planejar e priorizar todas as iniciativas com base no impacto no "
            "faturamento e despesas do negócio?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 6,
        "pilar": "Pilar III — Segurança Crítica",
        "pergunta": (
            "Inventário 80/20: A empresa possui uma planilha atualizada "
            "contendo os 20% de ativos tecnológicos mais críticos que "
            "representam 80% do risco operacional?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 7,
        "pilar": "Pilar III — Segurança Crítica",
        "pergunta": (
            "Backups Testados: A PME possui backups automáticos em nuvem e "
            "realizou com sucesso um teste físico de restauração em menos de "
            "30 minutos no último trimestre?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 8,
        "pilar": "Pilar III — Segurança Crítica",
        "pergunta": (
            "PRI de 1 Página: Existe um Plano de Resposta a Incidentes (PRI) "
            "de 1 página, assinado pelo CEO e impresso na sala de TI com "
            "contatos emergenciais e etapas de isolamento físico?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 9,
        "pilar": "Pilar I — Governança Essencial",
        "pergunta": (
            "Métricas DAN/COT: O gestor calcula e apresenta ao CD-TI Lite o "
            "índice DAN (Dívida de Arquitetura) e o ROI do COT (Custo de "
            "Otimização)?"
        ),
        "opcoes": ["Sim", "Não"],
    },
    {
        "id": 10,
        "pilar": "Pilar IV — Engenharia de Prompts e IA",
        "pergunta": (
            "Auditoria HITL (IA): Caso utilize ferramentas de IA para gerar "
            "código ou documentos, a PME possui um checklist de auditoria de "
            "alucinações (HITL) que impede saídas de IA de irem para produção "
            "sem revisão?"
        ),
        "opcoes": ["Sim", "Não"],
    },
]

# Nome oficial de cada um dos 5 níveis de maturidade (0 a 4).
NIVEIS: dict[int, str] = {
    0: "Nível 0: Caótico",
    1: "Nível 1: Reativo Organizado",
    2: "Nível 2: Governança Básica",
    3: "Nível 3: Inovação Incremental",
    4: "Nível 4: Governança Adaptativa",
}

# Interpretação prática de cada nível (Guia_Modelo_de_Maturidade.md, seção 4).
INTERPRETACOES: dict[int, str] = {
    0: "Urgente: implantar a Fase Zero do GP-PME para sair do caos operacional.",
    1: (
        "O caos operacional foi controlado. Foco agora em blindar a segurança "
        "essencial e formalizar a governança de alinhamento com o negócio."
    ),
    2: (
        "Operação segura e alinhada ao negócio. Pronta para buscar ciclos de "
        "inovação e MVPs rápidos."
    ),
    3: (
        "TI ágil, proativa e orientada a valor comercial, com controle de "
        "débitos técnicos (DAN/COT)."
    ),
    4: (
        "Excelência operacional acelerada por IA sob estrito controle humano "
        "(HITL)."
    ),
}

# Checklists oficiais de transição entre níveis consecutivos (Guia_Modelo_de_Maturidade.md,
# seção 5), cada ação já associada ao pilar do GP-PME que ela fortalece.
TRANSICOES: dict[tuple[int, int], list[dict]] = {
    (0, 1): [
        {"pilar": "Pilar II — Execução Ágil", "acao": "Unificar todos os chamados em um único formulário ou e-mail de suporte."},
        {"pilar": "Pilar II — Execução Ágil", "acao": "Ativar um quadro Kanban (digital ou físico) com 4 colunas estritas."},
        {"pilar": "Pilar II — Execução Ágil", "acao": "Estipular o WIP Limit = 3 no Kanban."},
        {"pilar": "Pilar IV — Engenharia de Prompts e IA", "acao": "Redigir a FAQ inicial de 5 itens para os problemas recorrentes."},
        {"pilar": "Pilar I — Governança Essencial", "acao": "Registrar a primeira métrica de tempo médio de suporte (TMpR baseline)."},
    ],
    (1, 2): [
        {"pilar": "Pilar I — Governança Essencial", "acao": "Bloquear a agenda do CEO quinzenalmente para reuniões de 30 min (CD-TI Lite)."},
        {"pilar": "Pilar I — Governança Essencial", "acao": "Preencher a Matriz 4 Quadrantes alinhada aos objetivos de receita e redução de custos do CEO."},
        {"pilar": "Pilar III — Segurança Crítica", "acao": "Mapear o Inventário 80/20 de ativos críticos na planilha."},
        {"pilar": "Pilar III — Segurança Crítica", "acao": "Ativar backup diário em nuvem para os ativos críticos e realizar teste físico de restauração."},
        {"pilar": "Pilar III — Segurança Crítica", "acao": "Imprimir e colar na parede da TI o Plano de Resposta a Incidentes (PRI) de 1 página."},
    ],
    (2, 3): [
        {"pilar": "Pilar II — Execução Ágil", "acao": "Lançar o primeiro ciclo MVP de 2 semanas de inovação (ex.: automação de relatórios)."},
        {"pilar": "Pilar II — Execução Ágil", "acao": "Padronizar o preenchimento de PRDs Simplificados para novas demandas."},
        {"pilar": "Pilar I — Governança Essencial", "acao": "Calcular a Dívida de Arquitetura Normalizada (DAN) e propor otimizações com base no ROI."},
        {"pilar": "Pilar IV — Engenharia de Prompts e IA", "acao": "Homologar uma biblioteca de prompts canônicos compartilhada na TI."},
    ],
    (3, 4): [
        {"pilar": "Pilar IV — Engenharia de Prompts e IA", "acao": "Instanciar os 4 Agentes Especialistas de IA (Orquestrador, Analista, Guardião, Auditor)."},
        {"pilar": "Pilar IV — Engenharia de Prompts e IA", "acao": "Institucionalizar o uso de prompts de contexto e restrições para evitar alucinações."},
        {"pilar": "Pilar IV — Engenharia de Prompts e IA", "acao": "Aplicar o checklist de auditoria humana (HITL) para 100% dos outputs gerados por IA."},
        {"pilar": "Pilar I — Governança Essencial", "acao": "Desenhar e aprovar no CD-TI Lite o plano de transição de infraestrutura elástica de longo prazo."},
    ],
}


def _nivel_por_pontos(pontos: float, maximo: int) -> int:
    """Converte uma pontuação (escalada para base 10) no nível 0-4 correspondente."""
    if maximo <= 0:
        return 0
    escala = pontos / maximo * 10
    if escala <= 2:
        return 0
    if escala <= 5:
        return 1
    if escala <= 8:
        return 2
    if escala < 10:
        return 3
    return 4


def questionario_maturidade() -> list[dict]:
    """Retorna as 10 perguntas oficiais da autoavaliação de maturidade GP-PME.

    Cada pergunta é binária (Sim/Não) e exige evidência prática para ser
    marcada como "Sim" (ex.: planilha de backup testado, print do quadro
    Kanban). As perguntas cobrem os 4 Pilares do framework.

    Returns:
        Lista de 10 dicts com as chaves "id" (1-10, ordem oficial),
        "pilar" (Pilar do GP-PME que a pergunta mede), "pergunta" (texto
        completo) e "opcoes" (["Sim", "Não"]).
    """
    return [dict(p) for p in PERGUNTAS]


def calcular_im_ti(respostas: list[int]) -> dict:
    """Calcula o Índice de Maturidade da TI (IM-TI) a partir das respostas.

    Soma as respostas "Sim" (1 ponto cada, 0 para "Não") para obter o IM-TI
    global (0 a 10) e o nível de maturidade correspondente (0 a 4). Também
    agrupa as respostas pelos 4 Pilares do GP-PME para calcular o nível de
    maturidade específico de cada pilar.

    Args:
        respostas: lista com exatamente 10 valores, na mesma ordem das
            perguntas de `questionario_maturidade` (índice 0 = pergunta 1,
            ..., índice 9 = pergunta 10). Cada valor é 1 (Sim) ou 0 (Não);
            valores "truthy"/"falsy" também são aceitos e normalizados.

    Returns:
        Em caso de entrada inválida (diferente de 10 respostas), dict com a
        chave "erro" explicando o que falta. Caso contrário, dict com
        "im_ti" (pontos de 0 a 10), "nivel_global" (0-4), "nivel_global_nome",
        "interpretacao", "pilares" (dict por pilar com "pontos", "maximo",
        "nivel" e "nivel_nome") e "fonte".
    """
    respostas = list(respostas or [])
    if len(respostas) != len(PERGUNTAS):
        return {
            "erro": (
                f"DADO INSUFICIENTE: esperadas {len(PERGUNTAS)} respostas "
                f"(0=Não, 1=Sim) na ordem do questionário, recebidas "
                f"{len(respostas)}."
            )
        }
    respostas_bin = [1 if r else 0 for r in respostas]
    im_ti = sum(respostas_bin)
    nivel_global = _nivel_por_pontos(im_ti, len(PERGUNTAS))

    pilares: dict[str, dict] = {}
    for pergunta, resposta in zip(PERGUNTAS, respostas_bin):
        info = pilares.setdefault(pergunta["pilar"], {"pontos": 0, "maximo": 0})
        info["pontos"] += resposta
        info["maximo"] += 1
    for info in pilares.values():
        nivel_pilar = _nivel_por_pontos(info["pontos"], info["maximo"])
        info["nivel"] = nivel_pilar
        info["nivel_nome"] = NIVEIS[nivel_pilar]

    return {
        "im_ti": im_ti,
        "nivel_global": nivel_global,
        "nivel_global_nome": NIVEIS[nivel_global],
        "interpretacao": INTERPRETACOES[nivel_global],
        "pilares": pilares,
        "fonte": "GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md",
    }


def plano_transicao(nivel_atual: int, nivel_alvo: int) -> dict:
    """Monta o plano de ação para transitar entre dois níveis de maturidade.

    Encadeia os checklists oficiais de transição (0→1, 1→2, 2→3, 3→4) desde
    `nivel_atual` até `nivel_alvo` e agrupa as ações resultantes por Pilar
    do GP-PME, para que o Gestor de TI possa distribuir o trabalho.

    Args:
        nivel_atual: nível de maturidade atual da PME (0 a 4).
        nivel_alvo: nível de maturidade desejado (0 a 4). Deve ser maior que
            `nivel_atual`; a transição sempre segue a sequência oficial
            (não pula níveis).

    Returns:
        dict com "nivel_atual"/"nivel_atual_nome", "nivel_alvo"/
        "nivel_alvo_nome", "transicoes_cobertas" (lista de strings "Nível X
        -> Nível Y"), "acoes_por_pilar" (dict pilar -> lista de ações) e
        "fonte". Se `nivel_alvo` não for maior que `nivel_atual`, retorna
        listas vazias e uma "mensagem" explicando que não há transição a
        fazer.
    """
    try:
        nivel_atual = max(0, min(4, int(nivel_atual)))
        nivel_alvo = max(0, min(4, int(nivel_alvo)))
    except (TypeError, ValueError):
        return {"erro": "DADO INSUFICIENTE: nivel_atual e nivel_alvo devem ser inteiros de 0 a 4."}

    if nivel_alvo <= nivel_atual:
        return {
            "nivel_atual": nivel_atual,
            "nivel_atual_nome": NIVEIS[nivel_atual],
            "nivel_alvo": nivel_alvo,
            "nivel_alvo_nome": NIVEIS[nivel_alvo],
            "transicoes_cobertas": [],
            "acoes_por_pilar": {},
            "mensagem": (
                "Nível alvo já foi atingido ou é igual/inferior ao nível atual "
                "— nenhuma ação de transição necessária."
            ),
        }

    transicoes_cobertas = []
    acoes_por_pilar: dict[str, list] = {}
    for nivel in range(nivel_atual, nivel_alvo):
        transicoes_cobertas.append(f"{NIVEIS[nivel]} -> {NIVEIS[nivel + 1]}")
        for item in TRANSICOES.get((nivel, nivel + 1), []):
            acoes_por_pilar.setdefault(item["pilar"], []).append(item["acao"])

    return {
        "nivel_atual": nivel_atual,
        "nivel_atual_nome": NIVEIS[nivel_atual],
        "nivel_alvo": nivel_alvo,
        "nivel_alvo_nome": NIVEIS[nivel_alvo],
        "transicoes_cobertas": transicoes_cobertas,
        "acoes_por_pilar": acoes_por_pilar,
        "fonte": "GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md (seção 5)",
    }


root_agent = Agent(
    name="agente_maturidade",
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description=(
        "Consultor de Maturidade GP-PME: aplica o questionário de "
        "autoavaliação, calcula o IM-TI por pilar e global, e monta o plano "
        "de transição entre níveis (0 a 4)."
    ),
    instruction=INSTRUCTION,
    tools=[questionario_maturidade, calcular_im_ti, plano_transicao],
)
