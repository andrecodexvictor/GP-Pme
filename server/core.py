"""Regras locais GEAR; identificadores GP-PME são mantidos por compatibilidade.

Fontes: framework/adocao/maturidade.md, framework/indicadores/, framework/guias/.
Agentes delegam cálculos a este módulo para evitar divergência de regras.
"""
from __future__ import annotations

from pathlib import Path
from datetime import datetime, timedelta
import math
from typing import Any

# Raiz do repositório: server/core.py -> server/ -> raiz.
RAIZ_REPO: Path = Path(__file__).resolve().parents[1]

# Limite anti-DoS para leitura de documentos via obter_documento.
MAX_DOC_BYTES = 200 * 1024  # 200 KB

# Limite inicial por executor; conta andamento, teste e bloqueio.
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
        from search.query import buscar as _buscar, resolver_modo
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
        modo_efetivo = resolver_modo(modo)
        resultados = _buscar(q, k=k, modo=modo_efetivo)
    except RuntimeError as exc:
        # Corpus/índices ainda não gerados — mensagem acionável do próprio search.
        return {"ok": False, "query": q, "modo": modo, "resultados": [], "erro": str(exc)}
    except Exception as exc:  # rede/embeddings — falha inesperada, não derruba o servidor
        return {
            "ok": False, "query": q, "modo": modo, "resultados": [],
            "erro": f"Falha inesperada na busca: {type(exc).__name__}: {exc}",
        }

    return {"ok": True, "query": q, "modo": modo_efetivo,
            "modo_solicitado": modo, "resultados": resultados}


# ────────────────────────────────────────────────────────────────────────────
# 2. CATÁLOGO DE ARTEFATOS E LEITURA SEGURA DE DOCUMENTOS
# ────────────────────────────────────────────────────────────────────────────
# Catálogo embutido da estrutura real do framework (caminhos relativos à raiz,
# separador "/"). Mantido à mão para dar títulos/categorias curados a um agente
# — não é uma varredura de diretório (que traria ruído e arquivos gerados).
_CATALOGO: list[dict[str, str]] = [
    {"id": "index", "categoria": "Portal",
     "titulo": "GEAR: percursos de leitura",
     "caminho": "framework/README.md"},
    {"id": "documento-mestre", "categoria": "Portal",
     "titulo": "Documento Mestre Consolidado",
     "caminho": "framework/README.md"},
    # Guias normativos (regras de negócio)
    {"id": "guia-maturidade", "categoria": "Guia",
     "titulo": "Modelo de Maturidade (5 níveis, IM-TI)",
     "caminho": "framework/adocao/maturidade.md"},
    {"id": "guia-kpis", "categoria": "Guia",
     "titulo": "Indicadores operacionais (IDSC, TMpR, ISU)",
     "caminho": "framework/indicadores/operacionais.md"},
    {"id": "guia-fase-zero", "categoria": "Guia",
     "titulo": "Implementação da Fase Zero (30 dias)",
     "caminho": "framework/adocao/primeiros-30-dias.md"},
    {"id": "guia-pilar-1", "categoria": "Guia",
     "titulo": "Governança e direção (CD-TI Lite)",
     "caminho": "framework/nucleo/governanca.md"},
    {"id": "guia-pilar-2", "categoria": "Guia",
     "titulo": "Execução e serviços (Kanban e capacidade)",
     "caminho": "framework/nucleo/execucao-servicos.md"},
    {"id": "guia-pilar-3", "categoria": "Guia",
     "titulo": "Segurança e continuidade",
     "caminho": "framework/nucleo/seguranca-continuidade.md"},
    {"id": "guia-pilar-4", "categoria": "Guia",
     "titulo": "Assistência opcional por IA",
     "caminho": "framework/guias/usar-ia.md"},
    # Templates operacionais
    {"id": "tpl-maturidade", "categoria": "Template",
     "titulo": "Mapeamento de Maturidade",
     "caminho": "framework/templates/maturidade.md"},
    {"id": "tpl-checklist-hitl", "categoria": "Template",
     "titulo": "Checklist de Auditoria HITL",
     "caminho": "framework/templates/revisao-ia.md"},
    {"id": "tpl-system-prompt", "categoria": "Template",
     "titulo": "System Prompt de Agentes",
     "caminho": "GP-PME antigravity/Templates/AI-Skills-and-Agents/Template_System_Prompt_Agentes.md"},
    {"id": "tpl-prd-completo", "categoria": "Template",
     "titulo": "PRD Completo",
     "caminho": "framework/templates/prd-aceite.md"},
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
    {"id": 1, "pilar": 'Execução e serviços', "pergunta": 'Demandas têm registro oficial e responsável?'},
    {"id": 2, "pilar": 'Execução e serviços', "pergunta": 'Trabalho iniciado respeita a capacidade definida, incluindo testes e bloqueios?'},
    {"id": 3, "pilar": 'Execução e serviços', "pergunta": 'Orientações recorrentes são mantidas e verificadas?'},
    {"id": 4, "pilar": 'Governança e direção', "pergunta": 'Negócio e TI decidem prioridades em revisão registrada?'},
    {"id": 5, "pilar": 'Execução e serviços', "pergunta": 'Melhorias têm problema, escopo e aceite acordados?'},
    {"id": 6, "pilar": 'Segurança e continuidade', "pergunta": 'Ativos e dependências críticos estão identificados?'},
    {"id": 7, "pilar": 'Segurança e continuidade', "pergunta": 'Recuperação foi testada na janela combinada?'},
    {"id": 8, "pilar": 'Segurança e continuidade', "pergunta": 'Acessos críticos são controlados e revistos?'},
    {"id": 9, "pilar": 'Governança e direção', "pergunta": 'Indicadores usados têm origem, período e revisão?'},
    {"id": 10, "pilar": 'Governança e direção', "pergunta": 'Decisões e mudanças passam por revisão responsável?'},
]

_NIVEIS = {0: "Nível 0: rotina pouco visível", 1: "Nível 1: organização inicial",
           2: "Nível 2: práticas repetidas", 3: "Nível 3: rotina acompanhada",
           4: "Nível 4: práticas verificadas"}
_INTERPRETACOES = {
    0: "Identificar responsáveis e registrar demandas; verificar lacunas por pergunta.",
    1: "Verificar continuidade e critérios de aceite, sem inferir segurança pelo total.",
    2: "Investigar lacunas e dependências entre práticas.",
    3: "Rever qualidade das evidências e resultados.",
    4: "Manter a revisão e adequar as práticas ao contexto. IA é opcional.",
}

def questionario_maturidade() -> list[dict[str, Any]]:
    """Retorna as 10 perguntas binárias (Sim/Não) da autoavaliação de maturidade."""
    return [dict(p) for p in _PERGUNTAS_MATURIDADE]


def _nivel_por_pontos(pontos: float, maximo: int) -> int:
    """Converte pontuação (escalada para base 10) no nível 0-4.

    Faixas locais (framework/adocao/maturidade.md): 0-2=N0, 3-5=N1, 6-8=N2,
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
    agrupa por domínio. A chave histórica "pilar" preserva compatibilidade.

    Args:
        respostas: lista com EXATAMENTE 10 valores na ordem do questionário
            (1=Sim, 0=Não); cada resposta positiva exige evidência consultável.

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

    if any(type(r) not in (bool, int) or r not in (0, 1) for r in respostas):
        return {"erro": "Respostas devem ser 0/1 ou booleanas; não normalizar texto como evidência."}
    binarias = [int(r) for r in respostas]
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
        "fonte": "framework/adocao/maturidade.md",
        "versao_instrumento": "GEAR 2026.10",
        "limite": "Instrumento local, sem certificação; evidências devem acompanhar respostas.",
    }


# ────────────────────────────────────────────────────────────────────────────
# 4. KPIs, DAN, COT e ROI (Guia_KPIs_e_Quick_Wins.md)
# ────────────────────────────────────────────────────────────────────────────
def _numero(valor: Any, minimo: float = 0) -> bool:
    return (type(valor) in (int, float) and math.isfinite(valor) and valor >= minimo)


def calcular_kpis(horas_indisponibilidade: float, horas_totais: float,
                  tempos_resposta_horas: list[float], notas_satisfacao: list[float],
                  meta_idsc: float = 99.5, meta_tmpr: float = 4.0,
                  meta_isu: float = 4.5) -> dict[str, Any]:
    """Calcula indicadores; metas são parâmetros locais e comparações estritas."""
    ausente = "DADO INSUFICIENTE"
    resultado = {k: ausente for k in ('idsc_percent', 'idsc_meta_atingida',
                 'tmpr_horas', 'tmpr_meta_atingida', 'isu_media', 'isu_meta_atingida')}
    if not (_numero(meta_idsc) and meta_idsc <= 100 and _numero(meta_tmpr)
            and meta_tmpr > 0 and _numero(meta_isu, 1) and meta_isu <= 5):
        resultado['erro'] = 'Metas inválidas: IDSC 0–100, TMpR positivo, ISU 1–5.'
        return resultado
    if (_numero(horas_totais) and horas_totais > 0 and _numero(horas_indisponibilidade)
            and horas_indisponibilidade <= horas_totais):
        idsc = 100 * (horas_totais - horas_indisponibilidade) / horas_totais
        resultado.update(idsc_percent=round(idsc, 2), idsc_meta_atingida=idsc > meta_idsc)
    if tempos_resposta_horas and all(_numero(t) for t in tempos_resposta_horas):
        tmpr = sum(tempos_resposta_horas) / len(tempos_resposta_horas)
        resultado.update(tmpr_horas=round(tmpr, 2), tmpr_meta_atingida=tmpr < meta_tmpr)
    if notas_satisfacao and all(_numero(n, 1) and n <= 5 for n in notas_satisfacao):
        isu = sum(notas_satisfacao) / len(notas_satisfacao)
        resultado.update(isu_media=round(isu, 2), isu_meta_atingida=isu > meta_isu)
    resultado.update(metas={'idsc': f'> {meta_idsc}%', 'tmpr': f'< {meta_tmpr}h', 'isu': f'> {meta_isu}'},
                     amostras={'incidentes': len(tempos_resposta_horas or []),
                               'respostas': len(notas_satisfacao or [])},
                     fonte='framework/indicadores/operacionais.md')
    return resultado


def calcular_proporcao_legada(itens_legados: int, itens_totais: int) -> dict[str, Any]:
    """Proporção de inventário, sem inferência de custo ou risco financeiro."""
    if (type(itens_legados) is not int or type(itens_totais) is not int
            or itens_totais <= 0 or not 0 <= itens_legados <= itens_totais):
        return {'proporcao_legada': 'DADO INSUFICIENTE', 'zona': 'DADO INSUFICIENTE',
                'erro': 'Contagens inteiras: total positivo, legado entre zero e total.'}
    p = itens_legados / itens_totais
    zona = 'saudavel' if p < .15 else 'alerta' if p <= .35 else 'critico'
    return {'proporcao_legada': round(p, 4), 'zona': zona,
            'limite': 'Faixas históricas locais de inventário; não validam risco ou DAN financeiro.',
            'recomendacao': 'Avaliar criticidade, suporte e custo de correção antes de decidir.',
            'fonte': 'framework/indicadores/financeiros.md'}


def calcular_dan(itens_legados: int, itens_totais: int) -> dict[str, Any]:
    """API histórica: campo dan é alias depreciado da proporção legada, não DAN financeiro."""
    r = calcular_proporcao_legada(itens_legados, itens_totais)
    return {**r, 'dan': r['proporcao_legada'],
            'compatibilidade': 'Use calcular_proporcao_legada ou calcular_dan_financeiro conforme a unidade.'}


def calcular_dan_financeiro(custo_refatoracao: float, orcamento_anual_ti: float) -> dict[str, Any]:
    """Estimativa de custo de refatoração / orçamento anual; sem limiar universal."""
    if not (_numero(custo_refatoracao) and _numero(orcamento_anual_ti) and orcamento_anual_ti > 0):
        return {'dan_financeiro': 'DADO INSUFICIENTE', 'erro': 'Custo não negativo e orçamento positivo, na mesma moeda.'}
    return {'dan_financeiro': round(custo_refatoracao / orcamento_anual_ti, 4),
            'unidade': 'razão custo/orçamento anual', 'fonte': 'framework/indicadores/financeiros.md'}


def calcular_roi_simplificado(investimento: float, retorno_mensal: float,
                              custo_recorrente_mensal: float = 0) -> dict[str, Any]:
    """ROI líquido em 12 meses e payback simples sob fluxo mensal constante."""
    if not (_numero(investimento) and investimento > 0 and _numero(retorno_mensal)
            and _numero(custo_recorrente_mensal)):
        return {'payback_meses': 'DADO INSUFICIENTE', 'roi_anual_percent': 'DADO INSUFICIENTE',
                'erro': 'Investimento positivo; benefício e custo mensais finitos e não negativos.'}
    liquido = retorno_mensal - custo_recorrente_mensal
    return {'payback_meses': round(investimento / liquido, 2) if liquido > 0 else None,
            'roi_anual_percent': round((liquido * 12 - investimento) / investimento * 100, 2),
            'razao_beneficio_investimento': round(retorno_mensal * 12 / investimento, 4),
            'beneficio_bruto_percent_investimento': round(retorno_mensal * 12 / investimento * 100, 2),
            'beneficio_bruto_anual': retorno_mensal * 12,
            'custo_recorrente_anual': custo_recorrente_mensal * 12,
            'horizonte_meses': 12,
            'veredito': 'Cenário condicional; conferir premissas, risco e capacidade antes da decisão.',
            'compatibilidade': 'ROI corrigido para retorno líquido; razão bruta disponível em campo próprio.',
            'fonte': 'framework/indicadores/financeiros.md'}


def calcular_cot(custo_otimizacao: float, ganho_mensal: float,
                 custo_recorrente_mensal: float = 0) -> dict[str, Any]:
    """COT é investimento inicial; cálculo financeiro delegado à convenção comum."""
    return calcular_roi_simplificado(custo_otimizacao, ganho_mensal, custo_recorrente_mensal)


# ────────────────────────────────────────────────────────────────────────────
# 5. PROTOCOLO KANBAN (Guia_Pilar_2_Execucao_Agil.md)
# ────────────────────────────────────────────────────────────────────────────
# 8 tarefas-semente da Fase Zero para popular o backlog inicial do Kanban.
_TAREFAS_KANBAN_FASE_ZERO: list[dict[str, str]] = [
    {"titulo": "Aplicar o Questionário de Maturidade (IM-TI baseline)",
     "entregavel": "Planilha de maturidade preenchida + 3 prioridades da TI.", "coluna": "A Fazer"},
    {"titulo": "Montar quadro com limite inicial de três iniciados por executor",
     "entregavel": "Quadro Kanban ativo e operacional.", "coluna": "A Fazer"},
    {"titulo": "Estabelecer o Canal Único de suporte",
     "entregavel": "Canal Único ativo, integrado ao Kanban.", "coluna": "A Fazer"},
    {"titulo": "Preparar orientações para dúvidas recorrentes",
     "entregavel": "Orientação revisada, com responsável e evidência de uso.", "coluna": "A Fazer"},
    {"titulo": "Registrar dependências críticas e testar recuperação",
     "entregavel": "Escopo, janela, resultado e limitações do teste registrados.", "coluna": "A Fazer"},
    {"titulo": "Preencher e afixar o PRI de 1 página",
     "entregavel": "Plano, contatos conferidos e evidência do exercício.", "coluna": "A Fazer"},
    {"titulo": "Realizar o primeiro CD-TI Lite e a Matriz 4 Quadrantes",
     "entregavel": "Primeira ata CD-TI Lite de 1 página.", "coluna": "A Fazer"},
    {"titulo": "Escolher indicadores necessários e revisar o percurso",
     "entregavel": "Origem dos dados, decisão, lacunas e próxima revisão.", "coluna": "A Fazer"},
]


def protocolo_kanban() -> dict[str, Any]:
    """Política local de fluxo e oito propostas iniciais de trabalho.

    Limite inicial de três iniciados por executor inclui teste e bloqueio.
    A criação das tarefas não comprova adoção ou resultado organizacional.
    """
    return {
        "colunas": ["A Fazer", "Em Andamento", "Em Teste", "Concluído"],
        "wip_limit": LIMITE_WIP,
        "unidade_wip": "por executor",
        "estados_contados": ["Em Andamento", "Em Teste", "Bloqueado"],
        "excecao": "Emergência exige registro de autorização, motivo e trabalho suspenso; preservar histórico.",
        "coluna_com_wip": "Em Andamento",  # Campo histórico: consultar estados_contados.
        "compatibilidade_wip": "coluna_com_wip é legado; o limite abrange todos os estados_contados.",
        "cadencia": {
            "sprint": "Ciclo semanal inicial; não implica implementação integral de Scrum.",
            "planejamento": "Selecionar itens compatíveis com capacidade e prioridades; 15 min como referência local.",
            "checkpoint_diario": "Conferir fila, resultados e impedimentos; 5 min como referência local.",
            "retrospectiva": "Rever entregas, bloqueios e prioridades; ajustar parâmetros locais com motivo.",
        },
        "canal_unico": (
            "Registro oficial de demandas, com responsável e situação. Urgência recebida "
            "por outro meio é atendida e registrada assim que viável."
        ),
        "raia_rapida": {
            "quando": "Incidente CRÍTICO (ex.: ERP/banco de dados fora do ar).",
            "passos": [
                "1. Identificar o impacto e obter decisão sobre prioridade e trabalho a suspender.",
                "2. Registrar suspensão e bloqueio, mantendo início e histórico; autorizar exceção de capacidade se necessária.",
                "3. Ativar a Raia Rápida: cartão do incidente no topo do quadro (etiqueta 🔥).",
                "4. Concentrar a capacidade autorizada na resposta e comunicar efeitos nos demais serviços.",
                "5. Verificar recuperação; decidir quando retomar o trabalho suspenso, preservando histórico.",
            ],
        },
        "tarefas_semente_fase_zero": [dict(t) for t in _TAREFAS_KANBAN_FASE_ZERO],
        "fonte": "framework/nucleo/execucao-servicos.md",
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
     "acao_manual": "Criar quadro (físico/digital) com estados visíveis e limite inicial de 3 itens iniciados por executor, incluindo testes e bloqueios.",
     "entregavel": "Quadro Kanban de TI ativo e operacional."},
    {"id": 3, "semana": 1, "dias": "Dia 6-7", "duracao_dias": 2,
     "titulo": "Estabelecendo o Canal Único de Suporte",
     "acao_manual": "Comunicar registro oficial e contato de urgência; registrar atendimentos recebidos por outros meios.",
     "entregavel": "Canal Único ativo e integrado ao Kanban."},
    {"id": 4, "semana": 2, "dias": "Dia 8-10", "duracao_dias": 3,
     "titulo": "Orientações para dúvidas recorrentes",
     "acao_manual": "Preparar orientações para dúvidas recorrentes e verificar com usuários.",
     "entregavel": "Orientação revisada, com responsável e evidência de uso."},
    {"id": 5, "semana": 2, "dias": "Dia 11-14", "duracao_dias": 4,
     "titulo": "Dependências críticas e recuperação",
     "acao_manual": "Mapear ativos por criticidade, definir tolerâncias e testar "
                    "restauração com escopo e resultado registrados.",
     "entregavel": "Inventário inicial por criticidade e teste de recuperação com limitações."},
    {"id": 6, "semana": 3, "dias": "Dia 15-18", "duracao_dias": 4,
     "titulo": "Plano de Resposta a Incidentes (PRI) de 1 Página",
     "acao_manual": "Preparar plano com contatos e alçadas; exercitar cenário autorizado e registrar limitações.",
     "entregavel": "Plano, contatos conferidos e evidência do exercício."},
    {"id": 7, "semana": 3, "dias": "Dia 19-21", "duracao_dias": 3,
     "titulo": "Primeiro CD-TI Lite e Matriz 4 Quadrantes",
     "acao_manual": "Reunir direção, TI e dono do processo para registrar prioridades, riscos e recursos.",
     "entregavel": "Primeira ata CD-TI Lite de 1 página."},
    {"id": 8, "semana": 4, "dias": "Dia 22-25", "duracao_dias": 4,
     "titulo": "Escolher indicadores necessários à decisão",
     "acao_manual": "Escolher indicadores relevantes; declarar origem, janela, unidades e limites.",
     "entregavel": "Painel de monitoramento de KPIs ativo."},
    {"id": 9, "semana": 4, "dias": "Dia 26-30", "duracao_dias": 5,
     "titulo": "Revisão de evidências e pendências",
     "acao_manual": "Reaplicar o Questionário de Maturidade e registrar mudanças, lacunas e "
                    "ações; não certificar transição automática.",
     "entregavel": "Comparação por pergunta, lacunas atribuídas e próxima revisão."},
]


def checklist_fase_zero() -> dict[str, Any]:
    """Retorna nove passos para uma janela local de adoção de 30 dias."""
    return {
        "total_passos": len(_CHECKLIST_FASE_ZERO),
        "duracao_total_dias": 30,
        "passos": [dict(p) for p in _CHECKLIST_FASE_ZERO],
        "fonte": "framework/adocao/primeiros-30-dias.md",
    }


def cronograma_implantacao(data_inicio: str) -> dict[str, Any]:
    """Agenda os 30 dias iniciais; datas não garantem implantação ou maturidade.

    A chave histórica ``fases`` permanece, com apenas o percurso inicial.
    Etapas posteriores dependem da revisão e não recebem prazos automáticos.
    """
    inicio = None
    for formato in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            inicio = datetime.strptime(data_inicio.strip(), formato).date()
            break
        except (ValueError, AttributeError):
            continue
    if inicio is None:
        return {"erro": "DADO INSUFICIENTE: use DD/MM/AAAA ou AAAA-MM-DD."}
    focos = ["Tornar o trabalho visível", "Conhecer dependências e recuperação",
             "Decidir e responder", "Verificar e ajustar"]
    semanas = []
    for numero, foco in enumerate(focos, 1):
        fim_dia = 30 if numero == 4 else numero * 7
        semanas.append({"semana": numero, "foco": foco,
                        "inicio": (inicio + timedelta(days=(numero - 1) * 7)).isoformat(),
                        "fim": (inicio + timedelta(days=fim_dia - 1)).isoformat()})
    return {"data_inicio": inicio.isoformat(),
            "fases": [{"fase": "Adoção inicial (antiga Fase Zero)",
                       "objetivo": "Iniciar a rotina e verificar evidências e pendências.",
                       "inicio": inicio.isoformat(),
                       "fim": (inicio + timedelta(days=29)).isoformat(),
                       "duracao_dias": 30}],
            "semanas_fase_zero": semanas,
            "limite": "Janela local, sem garantia de conclusão ou transição de maturidade.",
            "proxima_etapa": "Definir após revisar evidências, riscos e capacidade.",
            "fonte": "framework/adocao/primeiros-30-dias.md"}


# ────────────────────────────────────────────────────────────────────────────
# 7. CHECKLIST DE SEGURANÇA (Guia_Pilar_3_Seguranca_Critica.md) — NIST-Lite / CIS IG1
# ────────────────────────────────────────────────────────────────────────────
_CONTROLES_SEGURANCA: list[tuple] = [
    ("Ativos e dependências críticos registrados com responsável", "Identificar",
     "CIS 1 (Inventário de Ativos Corporativos)"),
    ("Privilégio Mínimo (LUA): remoção de admin local das contas do dia a dia", "Proteger",
     "CIS 5 (Gestão de Contas)"),
    ("MFA nas contas críticas de e-mail, com cobertura e exceções registradas", "Proteger",
     "CIS 6 (Gestão de Controle de Acesso)"),
    ("MFA nos acessos financeiros críticos, com cobertura e exceções", "Proteger",
     "CIS 6 (Gestão de Controle de Acesso)"),
    ("Senha individual forte por colaborador (sem contas compartilhadas)", "Proteger",
     "CIS 5 (Gestão de Contas)"),
    ("Backups protegidos, com frequência e retenção acordadas", "Proteger",
     "CIS 11 (Recuperação de Dados)"),
    ("Teste de recuperação na janela acordada, com escopo e resultado", "Recuperar",
     "CIS 11 (Recuperação de Dados)"),
    ("Revisão periódica de contas ociosas ou com privilégios excessivos", "Detectar",
     "CIS 5 (Gestão de Contas)"),
    ("Checklist de higiene cibernética (senhas, phishing) treinado com a equipe", "Proteger",
     "CIS 14 (Conscientização e Treinamento)"),
    ("Plano de incidente com contatos e alçadas conferidos em exercício", "Responder",
     "CIS 17 (Gestão de Resposta a Incidentes)"),
]


def checklist_10_controles() -> dict[str, Any]:
    """Gera dez verificações locais de segurança; não equivale ao CIS IG1.

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
        "limite": "Seleção local; não equivale ao NIST CSF completo nem às 56 salvaguardas CIS IG1.",
        "controles": itens,
        "fonte": "framework/nucleo/seguranca-continuidade.md",
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
    assert calcular_cot(9000, 3000)["roi_anual_percent"] == 300.0
    assert calcular_roi_simplificado(9000, 3000)["roi_anual_percent"] == 300.0
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
