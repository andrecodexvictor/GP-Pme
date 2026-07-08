"""Servidor MCP (stdio) do GP-PME — expõe `core` como ferramentas para um agente.

Roda em ambientes hostis a ferramentas de gestão: um cliente MCP (Claude Code,
Claude Desktop) conversa com este processo via stdio e obtém as regras de negócio
do GP-PME (maturidade, KPIs, DAN, COT, ROI, Kanban, Fase Zero, segurança) e a
busca no corpus, sem depender de ClickUp/Jira.

As docstrings PT-BR abaixo são a DESCRIÇÃO que o cliente MCP mostra ao modelo —
por isso são ricas e orientam quando/como usar cada ferramenta.

Executar:
    python -m server.mcp_server
"""
from __future__ import annotations

from typing import Any, List

from mcp.server.fastmcp import FastMCP

from . import core

mcp = FastMCP("gp-pme")


@mcp.tool()
def buscar_conhecimento(q: str, k: int = 5, modo: str = "hibrido") -> dict[str, Any]:
    """Busca os trechos mais relevantes do corpus GP-PME para responder uma dúvida.

    Use SEMPRE que precisar embasar uma resposta nos guias do framework (maturidade,
    pilares, segurança, Fase Zero) em vez de responder de memória.

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
    """Lista os documentos do framework GP-PME (catálogo curado).

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
    dentro do repositório: caminhos com "../", absolutos ou não-.md são recusados
    por segurança (proteção anti path-traversal).

    Args:
        caminho: caminho relativo à raiz, como retornado por `listar_artefatos`.
    """
    return core.obter_documento(caminho)


@mcp.tool()
def avaliar_maturidade(respostas: List[int]) -> dict[str, Any]:
    """Calcula o Índice de Maturidade da TI (IM-TI 0-10 e nível 0-4).

    Aplique o questionário de 10 perguntas Sim/Não (na ordem do guia) e passe as
    respostas aqui. Retorna o nível global, a interpretação e o nível por pilar.

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
    """Calcula os 3 KPIs Visíveis do GP-PME: IDSC, TMpR e ISU.

    IDSC = disponibilidade % (meta >99,5%); TMpR = tempo médio de resposta em horas
    (meta <4h); ISU = satisfação média 1-5 (meta >4,5). Campos sem dado retornam
    "DADO INSUFICIENTE" em vez de estimar.

    Args:
        horas_indisponibilidade: horas fora do ar no período.
        horas_totais: horas totais do período (ex.: 720 = 30 dias).
        tempos_resposta_horas: lista de tempos de primeira resposta, em horas.
        notas_satisfacao: lista de notas de satisfação (escala 1-5).
    """
    return core.calcular_kpis(
        horas_indisponibilidade, horas_totais, tempos_resposta_horas, notas_satisfacao
    )


@mcp.tool()
def calcular_dan(itens_legados: int, itens_totais: int) -> dict[str, Any]:
    """Calcula a Dívida de Arquitetura Normalizada (DAN) por proxy de inventário.

    DAN = itens_legados / itens_totais. Zonas: <0,15 saudável, 0,15-0,35 alerta,
    >0,35 crítico. Use com o inventário 80/20 do cliente.

    Args:
        itens_legados: itens legados/obsoletos.
        itens_totais: total de itens do inventário.
    """
    return core.calcular_dan(itens_legados, itens_totais)


@mcp.tool()
def calcular_cot(custo_otimizacao: float, ganho_mensal: float) -> dict[str, Any]:
    """Calcula o payback (meses) e o ROI anual (%) de um investimento de COT.

    Payback = custo/ganho_mensal; ROI anual = ganho_mensal*12/custo*100. Use para
    justificar um Custo de Otimização Técnica ao CD-TI Lite.

    Args:
        custo_otimizacao: aporte único do COT (R$).
        ganho_mensal: ganho/economia mensal recorrente (R$).
    """
    return core.calcular_cot(custo_otimizacao, ganho_mensal)


@mcp.tool()
def calcular_roi(investimento: float, retorno_mensal: float) -> dict[str, Any]:
    """Calcula ROI anual e payback de qualquer iniciativa de TI (versão geral do COT).

    Use para qualquer aporte único com retorno mensal recorrente (perdas evitadas
    ou ganho de produtividade). Retorna também um "veredito" de apoio à decisão.

    Args:
        investimento: aporte único (R$).
        retorno_mensal: retorno mensal recorrente (R$).
    """
    return core.calcular_roi_simplificado(investimento, retorno_mensal)


@mcp.tool()
def protocolo_kanban() -> dict[str, Any]:
    """Retorna a especificação do Kanban do GP-PME + 8 tarefas-semente da Fase Zero.

    Use para montar o quadro: 4 colunas, WIP Limit = 3, cadência semanal e a
    mecânica da Raia Rápida (Expedite) para incidentes críticos.
    """
    return core.protocolo_kanban()


@mcp.tool()
def checklist_fase_zero() -> dict[str, Any]:
    """Retorna o checklist ordenado dos 30 dias da Fase Zero (9 passos).

    Use para guiar a implantação inicial do framework do dia 1 ao dia 30.
    """
    return core.checklist_fase_zero()


@mcp.tool()
def checklist_seguranca() -> dict[str, Any]:
    """Retorna os 10 controles mínimos de segurança (NIST-Lite / CIS IG1).

    Use para auditar a segurança essencial da PME. Todos os itens nascem
    "pendente" — a verificação de conclusão é sempre humana (HITL).
    """
    return core.checklist_10_controles()


def main() -> None:
    """Ponto de entrada do transporte stdio (usado por `python -m server.mcp_server`)."""
    mcp.run()


if __name__ == "__main__":
    main()
