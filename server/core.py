"""Núcleo de serviço do GP-PME — lógica de negócio pura, sem framework web.

Este módulo é a fonte única de verdade da camada de servidor. Ele reproduz as
regras de negócio exatas dos guias do framework (Maturidade, KPIs/Quick Wins,
Fase Zero, Pilar 2 Execução Ágil, Pilar 3 Segurança Crítica) e integra a busca
semântica/BM25 já existente em `search/`.

Fontes normativas (regras de negócio EXATAS):
    GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md
    GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md
    GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md
    GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md
    GP-PME antigravity/Guides/Guia_Pilar_3_Seguranca_Critica.md

DUPLICAÇÃO DELIBERADA: a lógica de `calcular_kpis`, `calcular_dan`, `calcular_cot`,
`avaliar_maturidade`, `checklist_fase_zero` e `checklist_10_controles` foi copiada
e adaptada dos agentes ADK (agents/gp-pme-adk/...). O servidor NÃO importa dos
agentes de propósito, para não acoplar esta camada ao runtime ADK/Google. Se uma
regra de negócio mudar num guia, atualize AQUI e no agente correspondente.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

# Raiz do repositório: server/core.py -> server/ -> raiz.
RAIZ_REPO: Path = Path(__file__).resolve().parents[1]

# Limite anti-DoS para leitura de documentos via obter_documento.
MAX_DOC_BYTES = 200 * 1024  # 200 KB

# Limite de WIP (Work in Progress) do Kanban — Guia Pilar 2, seção 3.1.
LIMITE_WIP = 3


# ────────────────────────────────────────────────────────────────────────────
# 1. BUSCA NO CONHECIMENTO (integração com search/, com fallback claro)
# ────────────────────────────────────────────────────────────────────────────
def buscar_conhecimento(q: str, k: int = 5, modo: str = "hibrido") -> dict[str, Any]:
    """Busca os `k` trechos mais relevantes do corpus GP-PME para a pergunta `q`.

    Encapsula `search.query.buscar` (busca híbrida semântica + BM25 já existente).
    Degrada com mensagem clara — nunca levanta exceção para o chamador — quando o
    módulo de busca não está disponível ou os índices ainda não foram gerados.

    Args:
        q: texto da pergunta/consulta.
        k: número de resultados (1 a 50).
        modo: "hibrido" (default), "semantico" ou "bm25".

    Returns:
        dict com "ok" (bool), "query", "modo", "resultados" (lista de trechos com
        score) e, em caso de degradação, "erro" com orientação de como resolver.
    """
    q = (q or "").strip()
    if not q:
        return {"ok": False, "query": q, "modo": modo, "resultados": [],
                "erro": "DADO INSUFICIENTE: informe um texto de consulta não vazio."}
    k = max(1, min(50, int(k)))
    modo = modo if modo in ("hibrido", "semantico", "bm25") else "hibrido"

    try:
        from search.query import buscar as _buscar  # import tardio: search é opcional
    except Exception as exc:  # ImportError, ou erro de dependências de search
        return {
            "ok": False, "query": q, "modo": modo, "resultados": [],
            "erro": (
                "Módulo de busca (search/) indisponível: "
                f"{type(exc).__name__}: {exc}. "
                "Verifique se o pacote 'search' está no PYTHONPATH."
            ),
        }

    try:
        resultados = _buscar(q, k=k, modo=modo)
    except RuntimeError as exc:
        # Corpus/índices ainda não gerados — mensagem acionável do próprio search.
        return {"ok": False, "query": q, "modo": modo, "resultados": [], "erro": str(exc)}
    except Exception as exc:  # rede/embeddings — falha inesperada, não derruba o servidor
        return {
            "ok": False, "query": q, "modo": modo, "resultados": [],
            "erro": f"Falha inesperada na busca: {type(exc).__name__}: {exc}",
        }

    return {"ok": True, "query": q, "modo": modo, "resultados": resultados}


# ────────────────────────────────────────────────────────────────────────────
# 2. CATÁLOGO DE ARTEFATOS E LEITURA SEGURA DE DOCUMENTOS
# ────────────────────────────────────────────────────────────────────────────
# Catálogo embutido da estrutura real do framework (caminhos relativos à raiz,
# separador "/"). Mantido à mão para dar títulos/categorias curados a um agente
# — não é uma varredura de diretório (que traria ruído e arquivos gerados).
_CATALOGO: list[dict[str, str]] = [
    {"id": "index", "categoria": "Portal",
     "titulo": "INDEX — Portal Central do GP-PME",
     "caminho": "GP-PME antigravity/INDEX.md"},
    {"id": "documento-mestre", "categoria": "Portal",
     "titulo": "Documento Mestre Consolidado",
     "caminho": "GP-PME antigravity/GP-PME_Documento_Mestre_Consolidado.md"},
    # Guias normativos (regras de negócio)
    {"id": "guia-maturidade", "categoria": "Guia",
     "titulo": "Modelo de Maturidade (5 níveis, IM-TI)",
     "caminho": "GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md"},
    {"id": "guia-kpis", "categoria": "Guia",
     "titulo": "KPIs e Quick Wins (IDSC, TMpR, ISU, DAN, COT)",
     "caminho": "GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md"},
    {"id": "guia-fase-zero", "categoria": "Guia",
     "titulo": "Implementação da Fase Zero (30 dias)",
     "caminho": "GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md"},
    {"id": "guia-pilar-1", "categoria": "Guia",
     "titulo": "Pilar 1 — Governança Essencial (CD-TI Lite)",
     "caminho": "GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md"},
    {"id": "guia-pilar-2", "categoria": "Guia",
     "titulo": "Pilar 2 — Execução Ágil (Kanban, WIP=3, Raia Rápida)",
     "caminho": "GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md"},
    {"id": "guia-pilar-3", "categoria": "Guia",
     "titulo": "Pilar 3 — Segurança Crítica (NIST-Lite, 10 controles)",
     "caminho": "GP-PME antigravity/Guides/Guia_Pilar_3_Seguranca_Critica.md"},
    {"id": "guia-pilar-4", "categoria": "Guia",
     "titulo": "Pilar 4 — Assistência por IA e Agentes",
     "caminho": "GP-PME antigravity/Guides/Guia_Pilar_4_Assistencia_IA_e_Agentes.md"},
    # Templates operacionais
    {"id": "tpl-maturidade", "categoria": "Template",
     "titulo": "Mapeamento de Maturidade",
     "caminho": "GP-PME antigravity/Templates/Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md"},
    {"id": "tpl-checklist-hitl", "categoria": "Template",
     "titulo": "Checklist de Auditoria HITL",
     "caminho": "GP-PME antigravity/Templates/AI-Skills-and-Agents/Template_Checklist_Auditoria_HITL.md"},
    {"id": "tpl-system-prompt", "categoria": "Template",
     "titulo": "System Prompt de Agentes",
     "caminho": "GP-PME antigravity/Templates/AI-Skills-and-Agents/Template_System_Prompt_Agentes.md"},
    {"id": "tpl-prd-completo", "categoria": "Template",
     "titulo": "PRD Completo",
     "caminho": "GP-PME antigravity/Templates/PRDs/Template_PRD_Completo.md"},
    {"id": "tpl-prompt-mestre", "categoria": "Template",
     "titulo": "Prompt Mestre",
     "caminho": "GP-PME antigravity/Templates/Prompts/Template_Prompt_Mestre.md"},
    {"id": "tpl-prompt-prd", "categoria": "Template",
     "titulo": "Prompt de PRD",
     "caminho": "GP-PME antigravity/Templates/Prompts/Template_Prompt_PRD.md"},
    {"id": "tpl-prompt-risco", "categoria": "Template",
     "titulo": "Prompt de Análise de Risco",
     "caminho": "GP-PME antigravity/Templates/Prompts/Template_Prompt_Risco.md"},
    {"id": "tpl-tasklist", "categoria": "Template",
     "titulo": "Tasklist Operacional (Sprint semanal)",
     "caminho": "GP-PME antigravity/Templates/Tasklists/Template_Tasklist_Operacional.md"},
]


def listar_artefatos(categoria: str = "") -> dict[str, Any]:
    """Lista os documentos do framework GP-PME (catálogo curado da estrutura real).

    Args:
        categoria: filtro opcional por categoria ("Portal", "Guia", "Template").
            Vazio = todos. Case-insensitive.

    Returns:
        dict com "total", "categorias" (lista de categorias disponíveis) e
        "artefatos" (lista de dicts com "id", "categoria", "titulo", "caminho").
        Cada "caminho" é aceito diretamente por `obter_documento`.
    """
    cat = (categoria or "").strip().lower()
    itens = [dict(a) for a in _CATALOGO if not cat or a["categoria"].lower() == cat]
    categorias = sorted({a["categoria"] for a in _CATALOGO})
    return {"total": len(itens), "categorias": categorias, "artefatos": itens}


def obter_documento(caminho: str) -> dict[str, Any]:
    """Lê com segurança um documento .md do repositório GP-PME.

    Proteções (não relaxar — fronteira de confiança):
      * Anti path-traversal: o caminho resolvido tem de ficar DENTRO da raiz do
        repositório. "../", caminhos absolutos externos e symlinks para fora são
        rejeitados.
      * Só arquivos .md (evita servir código-fonte, .env, binários, etc.).
      * Limite de 200 KB (evita exaurir memória com arquivos gigantes).

    Args:
        caminho: caminho relativo à raiz do repositório (ex.:
            "GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md"), tal como
            retornado por `listar_artefatos`.

    Returns:
        dict com "ok". Em sucesso: "caminho", "tamanho_bytes", "conteudo".
        Em falha: "erro" descrevendo o motivo (nunca vaza caminho absoluto do host).
    """
    caminho = (caminho or "").strip().replace("\\", "/")
    if not caminho:
        return {"ok": False, "erro": "DADO INSUFICIENTE: caminho vazio."}
    if not caminho.lower().endswith(".md"):
        return {"ok": False, "erro": "Somente arquivos .md podem ser lidos."}

    # Resolve contra a raiz e confirma contenção (defesa contra ../ e absolutos).
    alvo = (RAIZ_REPO / caminho).resolve()
    try:
        alvo.relative_to(RAIZ_REPO)
    except ValueError:
        return {"ok": False, "erro": "Caminho fora do repositório não é permitido."}

    if not alvo.is_file():
        return {"ok": False, "erro": f"Documento não encontrado: {caminho}"}

    tamanho = alvo.stat().st_size
    if tamanho > MAX_DOC_BYTES:
        return {"ok": False,
                "erro": f"Documento excede o limite de {MAX_DOC_BYTES // 1024} KB "
                        f"({tamanho // 1024} KB)."}

    conteudo = alvo.read_text(encoding="utf-8", errors="replace")
    return {"ok": True, "caminho": caminho, "tamanho_bytes": tamanho, "conteudo": conteudo}


# ────────────────────────────────────────────────────────────────────────────
# 3. MATURIDADE (Guia_Modelo_de_Maturidade.md) — 10 perguntas, IM-TI, 5 níveis
# ────────────────────────────────────────────────────────────────────────────
_PERGUNTAS_MATURIDADE: list[dict[str, Any]] = [
    {"id": 1, "pilar": "Pilar II — Execução Ágil",
     "pergunta": "Canal Único: existe um único canal formalizado para receber solicitações, "
                 "erradicando chamados informais (WhatsApp pessoal)?"},
    {"id": 2, "pilar": "Pilar II — Execução Ágil",
     "pergunta": "Kanban Ativo: há um Kanban de 4 colunas (A Fazer, Em Andamento, Em Teste, "
                 "Concluído) com WIP Limit de no máximo 3 por técnico?"},
    {"id": 3, "pilar": "Pilar IV — Engenharia de Prompts e IA",
     "pergunta": "FAQs Operacionais: existe FAQ ou chatbot que resolve autonomamente >40% "
                 "das dúvidas básicas?"},
    {"id": 4, "pilar": "Pilar I — Governança Essencial",
     "pergunta": "CD-TI Lite: CEO e Gestor de TI fazem reuniões de 30 min (quinzenal/mensal) "
                 "para revisar métricas e aprovar verbas?"},
    {"id": 5, "pilar": "Pilar I — Governança Essencial",
     "pergunta": "Matriz 4 Quadrantes: a TI prioriza iniciativas pelo impacto no faturamento "
                 "e nas despesas do negócio?"},
    {"id": 6, "pilar": "Pilar III — Segurança Crítica",
     "pergunta": "Inventário 80/20: há planilha atualizada dos 20% de ativos que representam "
                 "80% do risco operacional?"},
    {"id": 7, "pilar": "Pilar III — Segurança Crítica",
     "pergunta": "Backups Testados: há backup automático em nuvem e teste de restauração "
                 "bem-sucedido (<30 min) no último trimestre?"},
    {"id": 8, "pilar": "Pilar III — Segurança Crítica",
     "pergunta": "PRI de 1 Página: existe Plano de Resposta a Incidentes de 1 página, assinado "
                 "pelo CEO e afixado na sala de TI?"},
    {"id": 9, "pilar": "Pilar I — Governança Essencial",
     "pergunta": "Métricas DAN/COT: o gestor calcula e apresenta ao CD-TI Lite a DAN e o ROI "
                 "do COT?"},
    {"id": 10, "pilar": "Pilar IV — Engenharia de Prompts e IA",
     "pergunta": "Auditoria HITL: outputs de IA passam por checklist de auditoria de "
                 "alucinações antes de ir para produção?"},
]

_NIVEIS: dict[int, str] = {
    0: "Nível 0: Caótico",
    1: "Nível 1: Reativo Organizado",
    2: "Nível 2: Governança Básica",
    3: "Nível 3: Inovação Incremental",
    4: "Nível 4: Governança Adaptativa",
}

_INTERPRETACOES: dict[int, str] = {
    0: "Urgente: implantar a Fase Zero do GP-PME para sair do caos operacional.",
    1: "O caos foi controlado. Foco agora em blindar a segurança essencial e "
       "formalizar a governança de alinhamento com o negócio.",
    2: "Operação segura e alinhada ao negócio. Pronta para buscar ciclos de "
       "inovação e MVPs rápidos.",
    3: "TI ágil, proativa e orientada a valor comercial, com controle de débitos "
       "técnicos (DAN/COT).",
    4: "Excelência operacional acelerada por IA sob estrito controle humano (HITL).",
}


def questionario_maturidade() -> list[dict[str, Any]]:
    """Retorna as 10 perguntas binárias (Sim/Não) da autoavaliação de maturidade."""
    return [dict(p) for p in _PERGUNTAS_MATURIDADE]


def _nivel_por_pontos(pontos: float, maximo: int) -> int:
    """Converte pontuação (escalada para base 10) no nível 0-4.

    Faixas oficiais (Guia_Modelo_de_Maturidade.md §4): 0-2=N0, 3-5=N1, 6-8=N2,
    9=N3, 10=N4.
    """
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


def avaliar_maturidade(respostas: list[int]) -> dict[str, Any]:
    """Calcula o Índice de Maturidade da TI (IM-TI) a partir de 10 respostas.

    Soma os "Sim" (1 ponto cada) para o IM-TI global (0-10) e o nível (0-4), e
    agrupa por pilar para o nível de cada um dos 4 pilares.

    Args:
        respostas: lista com EXATAMENTE 10 valores na ordem do questionário
            (1=Sim, 0=Não; valores truthy/falsy também aceitos).

    Returns:
        Em entrada inválida, dict com "erro". Caso contrário: "im_ti" (0-10),
        "nivel_global" (0-4), "nivel_global_nome", "interpretacao", "pilares"
        (por pilar: "pontos", "maximo", "nivel", "nivel_nome") e "fonte".
    """
    respostas = list(respostas or [])
    if len(respostas) != len(_PERGUNTAS_MATURIDADE):
        return {"erro": (
            f"DADO INSUFICIENTE: esperadas {len(_PERGUNTAS_MATURIDADE)} respostas "
            f"(0=Não, 1=Sim) na ordem do questionário, recebidas {len(respostas)}.")}

    binarias = [1 if r else 0 for r in respostas]
    im_ti = sum(binarias)
    nivel_global = _nivel_por_pontos(im_ti, len(_PERGUNTAS_MATURIDADE))

    pilares: dict[str, dict[str, Any]] = {}
    for pergunta, resposta in zip(_PERGUNTAS_MATURIDADE, binarias):
        info = pilares.setdefault(pergunta["pilar"], {"pontos": 0, "maximo": 0})
        info["pontos"] += resposta
        info["maximo"] += 1
    for info in pilares.values():
        nivel = _nivel_por_pontos(info["pontos"], info["maximo"])
        info["nivel"] = nivel
        info["nivel_nome"] = _NIVEIS[nivel]

    return {
        "im_ti": im_ti,
        "nivel_global": nivel_global,
        "nivel_global_nome": _NIVEIS[nivel_global],
        "interpretacao": _INTERPRETACOES[nivel_global],
        "pilares": pilares,
        "fonte": "GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md",
    }


# ────────────────────────────────────────────────────────────────────────────
# 4. KPIs, DAN, COT e ROI (Guia_KPIs_e_Quick_Wins.md)
# ────────────────────────────────────────────────────────────────────────────
def calcular_kpis(
    horas_indisponibilidade: float,
    horas_totais: float,
    tempos_resposta_horas: list[float],
    notas_satisfacao: list[float],
) -> dict[str, Any]:
    """Calcula os 3 KPIs Visíveis do GP-PME: IDSC, TMpR e ISU.

    IDSC = ((horas_totais - horas_indisponibilidade) / horas_totais) * 100  (meta > 99,5%)
    TMpR = média de `tempos_resposta_horas`                                 (meta < 4h)
    ISU  = média de `notas_satisfacao` (escala 1-5)                         (meta > 4,5)

    Campos com dados ausentes/inválidos retornam "DADO INSUFICIENTE" no lugar de
    estimar (nunca inventa entrada).
    """
    resultado: dict[str, Any] = {}

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

    resultado["metas"] = {"idsc": "> 99,5%", "tmpr": "< 4h", "isu": "> 4,5"}
    return resultado


def calcular_dan(itens_legados: int, itens_totais: int) -> dict[str, Any]:
    """Calcula a Dívida de Arquitetura Normalizada (DAN) por proxy de inventário.

    DAN = itens_legados / itens_totais. Zonas oficiais (Guia_KPIs §3.1):
        < 0,15         -> saudável
        0,15 a 0,35    -> alerta
        > 0,35         -> crítico

    Proxy simplificado para quando o Gestor de TI ainda não levantou horas de
    refatoração / custo-hora / orçamento anual da fórmula financeira completa.
    """
    if not itens_totais or itens_totais <= 0:
        return {"dan": "DADO INSUFICIENTE", "zona": "DADO INSUFICIENTE",
                "recomendacao": "Informe o total de itens do inventário 80/20 para calcular a DAN."}

    dan = itens_legados / itens_totais
    if dan < 0.15:
        zona, recomendacao = "saudavel", (
            "Dívida técnica sob controle. Mantenha a modernização e priorize inovação "
            "(Fase 2) sem urgência de investimento.")
    elif dan <= 0.35:
        zona, recomendacao = "alerta", (
            "Os juros da dívida técnica começam a cobrar preço em atrasos e bugs. "
            "Planeje um investimento de COT nos próximos ciclos do CD-TI Lite.")
    else:
        zona, recomendacao = "critico", (
            "Alto risco de parada de faturamento. Requer intervenção imediata e aporte "
            "de COT aprovado com urgência pelo CD-TI Lite.")

    return {"dan": round(dan, 4), "zona": zona, "recomendacao": recomendacao,
            "fonte": "GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md (§3.1)"}


def calcular_cot(custo_otimizacao: float, ganho_mensal: float) -> dict[str, Any]:
    """Calcula o payback e o ROI anual de um investimento de COT (Guia_KPIs §3.2).

    Payback (meses) = custo_otimizacao / ganho_mensal
    ROI anual (%)   = (ganho_mensal * 12 / custo_otimizacao) * 100
    """
    if not custo_otimizacao or custo_otimizacao <= 0 or not ganho_mensal or ganho_mensal <= 0:
        return {"payback_meses": "DADO INSUFICIENTE", "roi_anual_percent": "DADO INSUFICIENTE",
                "erro": "custo_otimizacao e ganho_mensal devem ser maiores que zero."}

    return {
        "payback_meses": round(custo_otimizacao / ganho_mensal, 2),
        "roi_anual_percent": round((ganho_mensal * 12 / custo_otimizacao) * 100, 2),
        "fonte": "GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md (§3.2)",
    }


def calcular_roi_simplificado(investimento: float, retorno_mensal: float) -> dict[str, Any]:
    """ROI operacional simplificado de qualquer iniciativa de TI (Guia_KPIs §3.2).

    Generalização da fórmula do ROI do COT para qualquer investimento pontual com
    retorno mensal recorrente (perdas evitadas OU ganho de produtividade):
        ROI anual (%) = (retorno_mensal * 12 / investimento) * 100
        Payback       = investimento / retorno_mensal

    Args:
        investimento: aporte único total da iniciativa (R$).
        retorno_mensal: economia/ganho mensal recorrente gerado (R$).

    Returns:
        dict com "payback_meses", "roi_anual_percent", "veredito" (texto de apoio
        à decisão) — ou "erro" se as entradas não forem positivas.
    """
    if not investimento or investimento <= 0 or not retorno_mensal or retorno_mensal <= 0:
        return {"payback_meses": "DADO INSUFICIENTE", "roi_anual_percent": "DADO INSUFICIENTE",
                "erro": "investimento e retorno_mensal devem ser maiores que zero."}

    payback = investimento / retorno_mensal
    roi = (retorno_mensal * 12 / investimento) * 100
    if payback <= 6:
        veredito = "Payback rápido (<= 6 meses): forte candidato à aprovação no CD-TI Lite."
    elif payback <= 12:
        veredito = "Payback dentro de 12 meses: retorno saudável, avaliar prioridade."
    else:
        veredito = "Payback acima de 12 meses: justificar o aporte com ganhos estratégicos."

    return {"payback_meses": round(payback, 2), "roi_anual_percent": round(roi, 2),
            "veredito": veredito,
            "fonte": "GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md (§3.2)"}


# ────────────────────────────────────────────────────────────────────────────
# 5. PROTOCOLO KANBAN (Guia_Pilar_2_Execucao_Agil.md)
# ────────────────────────────────────────────────────────────────────────────
# 8 tarefas-semente da Fase Zero para popular o backlog inicial do Kanban.
_TAREFAS_KANBAN_FASE_ZERO: list[dict[str, str]] = [
    {"titulo": "Aplicar o Questionário de Maturidade (IM-TI baseline)",
     "entregavel": "Planilha de maturidade preenchida + 3 prioridades da TI.", "coluna": "A Fazer"},
    {"titulo": "Montar o quadro Kanban de 4 colunas com WIP = 3",
     "entregavel": "Quadro Kanban ativo e operacional.", "coluna": "A Fazer"},
    {"titulo": "Estabelecer o Canal Único de suporte",
     "entregavel": "Canal Único ativo, integrado ao Kanban.", "coluna": "A Fazer"},
    {"titulo": "Criar a Base de FAQs das 5 dúvidas mais frequentes",
     "entregavel": "Base de FAQs ativa (documento ou chatbot).", "coluna": "A Fazer"},
    {"titulo": "Levantar o Inventário 80/20 e testar backups",
     "entregavel": "Inventário 80/20 + backup diário testado em <30 min.", "coluna": "A Fazer"},
    {"titulo": "Preencher e afixar o PRI de 1 página",
     "entregavel": "PRI de 1 página assinado pelo CEO.", "coluna": "A Fazer"},
    {"titulo": "Realizar o primeiro CD-TI Lite e a Matriz 4 Quadrantes",
     "entregavel": "Primeira ata CD-TI Lite de 1 página.", "coluna": "A Fazer"},
    {"titulo": "Definir e coletar os 3 KPIs Visíveis (IDSC, TMpR, ISU)",
     "entregavel": "Painel de monitoramento de KPIs ativo.", "coluna": "A Fazer"},
]


def protocolo_kanban() -> dict[str, Any]:
    """Retorna a especificação do Kanban do GP-PME + tarefas-semente da Fase Zero.

    Especificação (Guia Pilar 2): 4 colunas estritas, WIP Limit = 3 em "Em
    Andamento", cadência semanal de sprint, e a mecânica da Raia Rápida (Expedite)
    para incidentes críticos. Inclui 8 tarefas iniciais da Fase Zero prontas para
    popular a coluna "A Fazer".
    """
    return {
        "colunas": ["A Fazer", "Em Andamento", "Em Teste", "Concluído"],
        "wip_limit": LIMITE_WIP,
        "coluna_com_wip": "Em Andamento",
        "cadencia": {
            "sprint": "1 semana",
            "planejamento": "Segunda-feira, 15 min — seleciona 3 a 5 cartões da 'A Fazer'.",
            "checkpoint_diario": "5 min — o que movi para 'Concluído'? no que vou trabalhar? há impedimento?",
            "retrospectiva": "Fim da semana — meta > 80% dos cartões planejados entregues.",
        },
        "canal_unico": (
            "Ponto de entrada único obrigatório (formulário/e-mail de suporte); só se "
            "inicia chamado registrado no Canal Único, que gera cartão em 'A Fazer'."
        ),
        "raia_rapida": {
            "quando": "Incidente CRÍTICO (ex.: ERP/banco de dados fora do ar).",
            "passos": [
                "1. Suspender a tarefa 'Em Andamento' de menor prioridade comercial.",
                "2. Devolvê-la a 'A Fazer', liberando espaço no WIP (máx 3).",
                "3. Ativar a Raia Rápida: cartão do incidente no topo do quadro (etiqueta 🔥).",
                "4. Dedicar 100% do esforço até mitigar o incidente.",
                "5. Concluído o incidente, resgatar a tarefa suspensa de volta a 'Em Andamento'.",
            ],
        },
        "tarefas_semente_fase_zero": [dict(t) for t in _TAREFAS_KANBAN_FASE_ZERO],
        "fonte": "GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md",
    }


# ────────────────────────────────────────────────────────────────────────────
# 6. CHECKLIST DA FASE ZERO (Guia_de_Implementacao_Fase_Zero.md)
# ────────────────────────────────────────────────────────────────────────────
_CHECKLIST_FASE_ZERO: list[dict[str, Any]] = [
    {"id": 1, "semana": 1, "dias": "Dia 1-2", "duracao_dias": 2,
     "titulo": "Diagnóstico Rápido e Priorização de Maturidade",
     "acao_manual": "Aplicar o Questionário de Maturidade para fixar o IM-TI baseline e "
                    "priorizar os 3 principais gargalos.",
     "entregavel": "Planilha de maturidade preenchida (IM-TI baseline) e 3 prioridades."},
    {"id": 2, "semana": 1, "dias": "Dia 3-5", "duracao_dias": 3,
     "titulo": "Implantação do Quadro Kanban de TI",
     "acao_manual": "Criar quadro (físico/digital) com 4 colunas estritas e WIP Limit = 3 por técnico.",
     "entregavel": "Quadro Kanban de TI ativo e operacional."},
    {"id": 3, "semana": 1, "dias": "Dia 6-7", "duracao_dias": 2,
     "titulo": "Estabelecendo o Canal Único de Suporte",
     "acao_manual": "Criar ponto único de entrada e comunicar o fim dos canais informais.",
     "entregavel": "Canal Único ativo e integrado ao Kanban."},
    {"id": 4, "semana": 2, "dias": "Dia 8-10", "duracao_dias": 3,
     "titulo": "Base de FAQs (Nível 1)",
     "acao_manual": "Documentar o passo a passo das 5 dúvidas de TI mais frequentes.",
     "entregavel": "Base de FAQs ativa (documento ou chatbot)."},
    {"id": 5, "semana": 2, "dias": "Dia 11-14", "duracao_dias": 4,
     "titulo": "Inventário 80/20 de Ativos Críticos e Backups",
     "acao_manual": "Mapear os 20% de ativos críticos, configurar backup diário e testar "
                    "restauração em <30 min.",
     "entregavel": "Planilha de Inventário 80/20 e backups diários testados."},
    {"id": 6, "semana": 3, "dias": "Dia 15-18", "duracao_dias": 4,
     "titulo": "Plano de Resposta a Incidentes (PRI) de 1 Página",
     "acao_manual": "Preencher o PRI com contatos emergenciais e checklist de isolamento; "
                    "fixar impresso na TI.",
     "entregavel": "PRI de 1 página assinado pelo CEO."},
    {"id": 7, "semana": 3, "dias": "Dia 19-21", "duracao_dias": 3,
     "titulo": "Primeiro CD-TI Lite e Matriz 4 Quadrantes",
     "acao_manual": "Executar a primeira reunião de 30 min (CEO + Gestor de TI) e preencher "
                    "a Matriz 4 Quadrantes.",
     "entregavel": "Primeira ata CD-TI Lite de 1 página."},
    {"id": 8, "semana": 4, "dias": "Dia 22-25", "duracao_dias": 4,
     "titulo": "Definindo e Coletando os 3 KPIs Visíveis",
     "acao_manual": "Configurar a planilha de IDSC, TMpR e ISU e iniciar a coleta de satisfação.",
     "entregavel": "Painel de monitoramento de KPIs ativo."},
    {"id": 9, "semana": 4, "dias": "Dia 26-30", "duracao_dias": 5,
     "titulo": "Retrospectiva, Reavaliação e Transição de Fase",
     "acao_manual": "Reaplicar o Questionário de Maturidade e certificar a transição ao "
                    "Nível 1 (IM-TI entre 3 e 5).",
     "entregavel": "Relatório de transição com novo IM-TI certificado e assinatura do CEO."},
]


def checklist_fase_zero() -> dict[str, Any]:
    """Retorna o checklist ordenado dos 30 dias oficiais da Fase Zero (9 passos)."""
    return {
        "total_passos": len(_CHECKLIST_FASE_ZERO),
        "duracao_total_dias": 30,
        "passos": [dict(p) for p in _CHECKLIST_FASE_ZERO],
        "fonte": "GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md",
    }


# ────────────────────────────────────────────────────────────────────────────
# 7. CHECKLIST DE SEGURANÇA (Guia_Pilar_3_Seguranca_Critica.md) — NIST-Lite / CIS IG1
# ────────────────────────────────────────────────────────────────────────────
_CONTROLES_SEGURANCA: list[tuple] = [
    ("Inventário 80/20 de Ativos Críticos registrado em planilha", "Identificar",
     "CIS 1 (Inventário de Ativos Corporativos)"),
    ("Privilégio Mínimo (LUA): remoção de admin local das contas do dia a dia", "Proteger",
     "CIS 5 (Gestão de Contas)"),
    ("MFA ativo em 100% das contas de e-mail", "Proteger",
     "CIS 6 (Gestão de Controle de Acesso)"),
    ("MFA ativo em 100% dos sistemas financeiros", "Proteger",
     "CIS 6 (Gestão de Controle de Acesso)"),
    ("Senha individual forte por colaborador (sem contas compartilhadas)", "Proteger",
     "CIS 5 (Gestão de Contas)"),
    ("Backups diários automatizados em nuvem (regra 3-2-1)", "Proteger",
     "CIS 11 (Recuperação de Dados)"),
    ("Teste de restauração de backup a cada 3 meses, com registro em ata", "Recuperar",
     "CIS 11 (Recuperação de Dados)"),
    ("Revisão periódica de contas ociosas ou com privilégios excessivos", "Detectar",
     "CIS 5 (Gestão de Contas)"),
    ("Checklist de higiene cibernética (senhas, phishing) treinado com a equipe", "Proteger",
     "CIS 14 (Conscientização e Treinamento)"),
    ("PRI de 1 página preenchido, assinado pelo CEO e fixado na TI", "Responder",
     "CIS 17 (Gestão de Resposta a Incidentes)"),
]


def checklist_10_controles() -> dict[str, Any]:
    """Gera o checklist dos 10 controles mínimos NIST-Lite / CIS IG1.

    Todos os itens nascem com status "pendente" — a auditoria de conclusão é
    sempre humana (Human-in-the-loop).
    """
    itens = [
        {"id": i + 1, "controle": controle, "funcao_nist": funcao,
         "referencia_cis": ref, "status": "pendente"}
        for i, (controle, funcao, ref) in enumerate(_CONTROLES_SEGURANCA)
    ]
    return {
        "total_controles": len(itens),
        "controles": itens,
        "fonte": "GP-PME antigravity/Guides/Guia_Pilar_3_Seguranca_Critica.md",
    }


# Autoteste mínimo (ponytail: valida os caminhos de negócio não triviais).
def _demo() -> None:
    assert avaliar_maturidade([1] * 10)["nivel_global"] == 4
    assert avaliar_maturidade([0] * 10)["nivel_global"] == 0
    assert avaliar_maturidade([1, 1, 1, 0, 0, 0, 0, 0, 0, 0])["im_ti"] == 3
    assert "erro" in avaliar_maturidade([1, 1, 1])
    assert calcular_dan(3, 10)["zona"] == "alerta"          # 0,30 -> alerta
    assert calcular_dan(1, 10)["zona"] == "saudavel"        # 0,10 -> saudável
    assert calcular_dan(5, 10)["zona"] == "critico"         # 0,50 -> crítico
    assert calcular_dan(1, 0)["dan"] == "DADO INSUFICIENTE"
    assert calcular_cot(9000, 3000)["payback_meses"] == 3.0
    assert calcular_cot(9000, 3000)["roi_anual_percent"] == 400.0
    assert calcular_roi_simplificado(9000, 3000)["roi_anual_percent"] == 400.0
    kpis = calcular_kpis(2, 720, [1.0, 3.0], [5, 4])
    assert kpis["idsc_meta_atingida"] is True and kpis["tmpr_meta_atingida"] is True
    assert calcular_kpis(0, 0, [], [])["idsc_percent"] == "DADO INSUFICIENTE"
    # Anti path-traversal: leitura fora do repo / não-.md deve falhar.
    assert obter_documento("../x")["ok"] is False
    assert obter_documento("../../etc/passwd")["ok"] is False
    assert obter_documento("server/core.py")["ok"] is False  # só .md
    assert len(checklist_10_controles()["controles"]) == 10
    assert len(checklist_fase_zero()["passos"]) == 9
    assert protocolo_kanban()["wip_limit"] == 3
    assert len(protocolo_kanban()["tarefas_semente_fase_zero"]) == 8
    print("core._demo OK")


if __name__ == "__main__":
    _demo()
