"""Backend MCP GEAR: cálculos, instrumentos locais e busca no corpus.

O identificador técnico gp-pme preserva compatibilidade. A integração deste
usuário usa o hub HTTP global; clientes não iniciam seus próprios processos
stdio. Este módulo fornece o backend ao hub conforme server/README.md.
As docstrings são descrições de ferramentas apresentadas aos modelos.
"""
from __future__ import annotations

from typing import Any, List

from mcp.server.fastmcp import FastMCP

from . import core

mcp = FastMCP("gp-pme")


@mcp.tool()
def buscar_conhecimento(q: str, k: int = 5, modo: str = "hibrido") -> dict[str, Any]:
    """Busca trechos do corpus canônico GEAR para fundamentar uma resposta.

    Use SEMPRE que precisar embasar uma resposta nos guias do framework (maturidade,
    domínios, segurança, adoção) em vez de responder de memória.

    Args:
        q: pergunta ou termo de busca em português.
        k: quantos trechos retornar (1 a 50; padrão 5).
        modo: "hibrido" (padrão), "semantico" ou "bm25".

    Retorna dict com "ok" e "resultados"; se o índice ainda não foi gerado,
    "ok" vem False e "erro" explica como resolver (nunca lança exceção).
    """
    return core.buscar_conhecimento(q, k=k, modo=modo)


@mcp.tool()
def listar_artefatos(categoria: str = "") -> dict[str, Any]:
    """Lista documentos do GEAR no catálogo curado.

    Use para descobrir quais guias/templates existem antes de ler um deles.

    Args:
        categoria: filtro opcional — "Portal", "Guia" ou "Template". Vazio = todos.

    Cada item traz um "caminho" que você passa direto para `obter_documento`.
    """
    return core.listar_artefatos(categoria)


@mcp.tool()
def obter_documento(caminho: str) -> dict[str, Any]:
    """Lê o conteúdo de um documento .md do framework.

    Use depois de `listar_artefatos` para ler o guia/template completo. Só lê .md
    dentro do repositório: o caminho resolvido deve permanecer na raiz,
    inclusive após resolver symlinks; arquivos externos ou não-.md são recusados.

    Args:
        caminho: caminho relativo à raiz, como retornado por `listar_artefatos`.
    """
    return core.obter_documento(caminho)


@mcp.tool()
def avaliar_maturidade(respostas: List[int]) -> dict[str, Any]:
    """Calcula o Índice de Maturidade da TI (IM-TI 0-10 e nível 0-4).

    Aplique o questionário de 10 perguntas Sim/Não (na ordem do guia) e passe as
    respostas aqui. Retorna níveis locais, interpretação e resultado por domínio.
    A chave histórica "pilar" permanece; nenhum nível exige IA. Conferir evidências.

    Args:
        respostas: EXATAMENTE 10 valores (1=Sim, 0=Não) na ordem do questionário.
    """
    return core.avaliar_maturidade(respostas)


@mcp.tool()
def calcular_kpis(
    horas_indisponibilidade: float,
    horas_totais: float,
    tempos_resposta_horas: List[float],
    notas_satisfacao: List[float],
) -> dict[str, Any]:
    """Calcula disponibilidade, tempo médio de restauração e satisfação.

    IDSC = disponibilidade %; TMpR = tempo médio até restauração em horas;
    ISU = satisfação média 1-5. Valores de meta retornados são referências
    históricas locais; a organização deve acordar metas e janela de observação.
    Campos sem dado retornam "DADO INSUFICIENTE".

    Args:
        horas_indisponibilidade: horas fora do ar no período.
        horas_totais: horas totais do período (ex.: 720 = 30 dias).
        tempos_resposta_horas: lista de tempos até restauração, em horas.
        notas_satisfacao: lista de notas de satisfação (escala 1-5).
    """
    return core.calcular_kpis(
        horas_indisponibilidade, horas_totais, tempos_resposta_horas, notas_satisfacao
    )


@mcp.tool()
def calcular_dan(itens_legados: int, itens_totais: int) -> dict[str, Any]:
    """API histórica de proporção legada, distinta de DAN financeiro.

    Proporção legada = itens_legados / itens_totais. Zonas: <0,15 saudável, 0,15-0,35 alerta,
    >0,35 crítico. Faixas locais históricas não validam risco financeiro.

    Args:
        itens_legados: itens legados/obsoletos.
        itens_totais: total de itens do inventário.
    """
    return core.calcular_dan(itens_legados, itens_totais)


@mcp.tool()
def calcular_cot(custo_otimizacao: float, ganho_mensal: float, custo_recorrente_mensal: float = 0) -> dict[str, Any]:
    """Calcula o payback (meses) e o ROI anual (%) de um investimento de COT.

    ROI líquido anual = ((ganho_mensal-custo_recorrente_mensal)*12-custo)/custo*100.
    Payback simples existe quando benefício líquido mensal é positivo.
    Cenário condicional; não comprova ganho observado.

    Args:
        custo_otimizacao: aporte único do COT (R$).
        ganho_mensal: ganho/economia mensal recorrente (R$).
    """
    return core.calcular_cot(custo_otimizacao, ganho_mensal, custo_recorrente_mensal)


@mcp.tool()
def calcular_roi(investimento: float, retorno_mensal: float, custo_recorrente_mensal: float = 0) -> dict[str, Any]:
    """Calcula ROI anual e payback de qualquer iniciativa de TI (versão geral do COT).

    Cenário com aporte único e benefício mensal potencial estabilizado durante
    doze meses. Horas recuperadas não são automaticamente redução de despesa.
    Retorna ROI líquido, razão bruta e payback; verificar premissas e recorrência.

    Args:
        investimento: aporte único (R$).
        retorno_mensal: retorno mensal recorrente (R$).
    """
    return core.calcular_roi_simplificado(investimento, retorno_mensal, custo_recorrente_mensal)


@mcp.tool()
def calcular_dan_financeiro(custo_refatoracao: float, orcamento_anual_ti: float) -> dict[str, Any]:
    """Custo estimado de refatoração / orçamento anual, na mesma moeda; instrumento local."""
    return core.calcular_dan_financeiro(custo_refatoracao, orcamento_anual_ti)


@mcp.tool()
def protocolo_kanban() -> dict[str, Any]:
    """Retorna a política local de Kanban e oito propostas iniciais de trabalho.

    Quatro estados; até três iniciados por executor, incluindo teste e bloqueio.
    Cadência semanal é referência ajustável. Emergências exigem autorização,
    exceção visível e histórico do trabalho suspenso.
    """
    return core.protocolo_kanban()


@mcp.tool()
def checklist_fase_zero() -> dict[str, Any]:
    """Retorna o checklist ordenado dos 30 dias da Fase Zero (9 passos).

    Janela local de planejamento; não garante conclusão nem avanço de maturidade.
    """
    return core.checklist_fase_zero()


@mcp.tool()
def checklist_seguranca() -> dict[str, Any]:
    """Retorna dez verificações de segurança selecionadas localmente.

    Use para auditar a segurança essencial da PME. Todos os itens nascem
    "pendente" — a verificação de conclusão é humana. A seleção não equivale
    ao NIST CSF completo nem às salvaguardas CIS IG1 e não certifica conformidade.
    """
    return core.checklist_10_controles()


def main() -> None:
    """Ponto de entrada do transporte stdio (usado por `python -m server.mcp_server`)."""
    mcp.run()


if __name__ == "__main__":
    main()
