"""Ferramentas ADK de plataforma — a "mão" do Orquestrador GP-PME no Kanban.

Estas são funções Python puras (sem estado escondido além do quadro corrente)
que o Google ADK expõe ao modelo como *tools*. O ADK usa a **docstring** de cada
função como descrição da ferramenta para o LLM, por isso elas são ricas e em
PT-BR: descrevem o que a ferramenta faz, quando usá-la e o que ela retorna.

Todas operam sobre o *adapter ativo* (:func:`adapters.adapter_ativo`), resolvido
a partir de ``GPPME_PLATAFORMA``. Em modo dry-run (sem credenciais) nada é
enviado à rede: os retornos são simulados e realistas, e cada retorno traz o
campo ``dry_run`` para o agente deixar claro ao humano que foi uma simulação.

O "quadro corrente" (onde as tarefas são criadas/movidas) fica em
:data:`_quadro_atual` e é definido por :func:`instalar_gp_pme_na_plataforma`.
"""
from __future__ import annotations

from dataclasses import asdict
from typing import Any

from . import PLATAFORMAS, adapter_ativo
from .base import COLUNAS_GP_PME, Quadro

# Quadro sobre o qual as demais ferramentas operam. Definido ao instalar o
# GP-PME numa plataforma. ponytail: estado global de módulo — a sessão do agente
# gerencia um quadro por vez; multi-quadro só se o produto pedir.
_quadro_atual: Quadro | None = None


def _exigir_quadro() -> Quadro:
    """Garante que já existe um quadro instalado; senão, erro amigável (PT-BR)."""
    if _quadro_atual is None:
        raise ValueError(
            "Nenhum quadro GP-PME está ativo ainda. "
            "Use primeiro a ferramenta 'instalar_gp_pme_na_plataforma' para criar "
            "o quadro canônico (4 colunas + tarefas da Fase Zero)."
        )
    return _quadro_atual


def instalar_gp_pme_na_plataforma(nome_quadro: str = "GP-PME — Gestão de TI") -> dict:
    """Instala o quadro Kanban canônico do GP-PME na plataforma ativa.

    Cria o quadro do Pilar 2 (Execução Ágil) com as 4 colunas do Ciclo
    Micro-Adaptativo — 'A Fazer', 'Em Andamento (máx 3)' (limite WIP=3), 'Em Teste'
    e 'Concluído' — e já popula a coluna inicial com as 8 tarefas da Fase Zero de
    implantação. Este quadro passa a ser o "quadro corrente" das demais
    ferramentas de plataforma.

    Use esta ferramenta uma vez, no início da implantação, depois do diagnóstico
    de maturidade. A plataforma de destino vem de GPPME_PLATAFORMA (padrão Trello).

    Args:
        nome_quadro: título do quadro a criar na plataforma.

    Returns:
        Dicionário com o quadro criado (id, nome, colunas, url), a plataforma, a
        flag ``dry_run`` (True quando simulado, sem credenciais) e a lista de
        tarefas da Fase Zero adicionadas.
    """
    global _quadro_atual
    adapter = adapter_ativo()
    quadro = adapter.configurar_quadro_gp_pme(nome_quadro)
    _quadro_atual = quadro
    relatorio = adapter.relatorio_quadro(quadro)
    return {
        "plataforma": adapter.nome,
        "dry_run": adapter.dry_run,
        "quadro": asdict(quadro),
        "colunas": COLUNAS_GP_PME,
        "tarefas_iniciais": relatorio["total"],
        "mensagem": (
            f"Quadro GP-PME instalado em '{adapter.nome}' "
            f"({'simulação (dry-run)' if adapter.dry_run else 'plataforma real'}) "
            f"com {relatorio['total']} tarefas da Fase Zero."
        ),
    }


def criar_tarefa(titulo: str, descricao: str = "", raia_rapida: bool = False) -> dict:
    """Cria uma nova tarefa (card) na coluna inicial 'A Fazer' do quadro GP-PME.

    Toda demanda de TI entra pelo Canal Único e vira um card em 'A Fazer'. Marque
    ``raia_rapida=True`` apenas para itens de expedição (incidentes/urgências que
    furam a fila) — eles recebem a etiqueta '🔥 Raia Rápida'. Exige que o quadro
    já tenha sido instalado com 'instalar_gp_pme_na_plataforma'.

    Args:
        titulo: título curto e acionável da tarefa.
        descricao: contexto/detalhes (opcional).
        raia_rapida: se True, marca a tarefa como expedição na raia rápida.

    Returns:
        Dicionário com o card criado (id, titulo, coluna, raia_rapida, url) e a
        flag ``dry_run``.
    """
    adapter = adapter_ativo()
    quadro = _exigir_quadro()
    cartao = adapter.criar_cartao(
        quadro, titulo, COLUNAS_GP_PME[0], descricao=descricao, raia_rapida=raia_rapida
    )
    return {
        "plataforma": adapter.nome,
        "dry_run": adapter.dry_run,
        "cartao": asdict(cartao),
    }


def mover_tarefa(cartao_id: str, coluna_destino: str) -> dict:
    """Move uma tarefa para outra coluna do fluxo GP-PME.

    Reflete o avanço do trabalho no Ciclo Micro-Adaptativo. As colunas válidas
    são as 4 canônicas: 'A Fazer', 'Em Andamento (máx 3)', 'Em Teste', 'Concluído'.
    Ao puxar trabalho para 'Em Andamento', respeite o limite WIP=3 — verifique
    antes com 'verificar_wip'.

    Args:
        cartao_id: identificador do card a mover.
        coluna_destino: nome exato da coluna de destino (uma das 4 canônicas).

    Returns:
        Dicionário com o card atualizado e a flag ``dry_run``; inclui um aviso se
        o nome da coluna não corresponder às colunas canônicas do GP-PME.
    """
    adapter = adapter_ativo()
    quadro = _exigir_quadro()
    resultado: dict[str, Any] = {"plataforma": adapter.nome, "dry_run": adapter.dry_run}
    if coluna_destino not in COLUNAS_GP_PME:
        resultado["aviso"] = (
            f"'{coluna_destino}' não é uma coluna canônica do GP-PME. "
            f"Colunas válidas: {', '.join(COLUNAS_GP_PME)}."
        )
    cartao = adapter.mover_cartao(quadro, cartao_id, coluna_destino)
    resultado["cartao"] = asdict(cartao)
    return resultado


def verificar_wip() -> dict:
    """Verifica o limite de trabalho em progresso (WIP=3) na coluna 'Em Andamento'.

    Regra central do Pilar 2: no máximo 3 itens simultâneos em andamento. Use esta
    ferramenta antes de puxar novo trabalho e nas cadências semanais. Exige quadro
    instalado.

    Returns:
        Dicionário com: coluna monitorada, nº de cards em andamento, o limite (3),
        se está 'estourado' (bool) e uma recomendação prática em PT-BR.
    """
    adapter = adapter_ativo()
    quadro = _exigir_quadro()
    diagnostico = adapter.verificar_wip(quadro)
    diagnostico["plataforma"] = adapter.nome
    diagnostico["dry_run"] = adapter.dry_run
    return diagnostico


def relatorio_do_quadro() -> dict:
    """Gera o resumo do quadro GP-PME para a cadência (contagem por coluna + WIP).

    Panorama rápido do fluxo: total de cards, distribuição por coluna, quantos
    estão na raia rápida e o diagnóstico de WIP. Insumo para a revisão semanal e
    para as métricas do Pilar 2. Exige quadro instalado.

    Returns:
        Dicionário com quadro, total, por_coluna, raia_rapida e o bloco 'wip'.
    """
    adapter = adapter_ativo()
    quadro = _exigir_quadro()
    relatorio = adapter.relatorio_quadro(quadro)
    relatorio["plataforma"] = adapter.nome
    relatorio["dry_run"] = adapter.dry_run
    return relatorio


def listar_plataformas_suportadas() -> list:
    """Lista as plataformas de gestão suportadas pelo GP-PME.

    Útil para orientar o usuário sobre onde o quadro pode ser instalado e qual
    valor usar na variável de ambiente GPPME_PLATAFORMA.

    Returns:
        Lista de nomes de plataformas, ex.: ['clickup', 'notion', 'trello',
        'jira', 'linear'].
    """
    return list(PLATAFORMAS)


__all__ = [
    "instalar_gp_pme_na_plataforma",
    "criar_tarefa",
    "mover_tarefa",
    "verificar_wip",
    "relatorio_do_quadro",
    "listar_plataformas_suportadas",
]
