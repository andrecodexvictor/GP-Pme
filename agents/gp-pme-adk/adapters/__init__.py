"""Pacote de adapters de plataformas de gestão do GP-PME.

Um *adapter* traduz o "quadro canônico GP-PME" (4 colunas, WIP=3, raia rápida e
tarefas da Fase Zero) para uma plataforma concreta (ClickUp, Notion, Trello,
Jira ou Linear). Cada plataforma vive em seu próprio módulo (`adapters/<nome>.py`)
e expõe uma classe `Adapter` que herda de `base.PlataformaGestao`.

Este `__init__` oferece a "porta de entrada":

* :func:`get_adapter` — resolve e instancia o adapter de uma plataforma pelo nome.
* :func:`adapter_ativo` — singleton que resolve a plataforma corrente a partir da
  variável de ambiente ``GPPME_PLATAFORMA`` (padrão: ``trello``).

Todos os adapters funcionam em *dry-run* (sem credenciais/sem rede), então é
seguro chamar estas funções em qualquer ambiente — inclusive em testes e demos.
"""
from __future__ import annotations

import importlib
import os

from .base import PlataformaGestao

#: Plataformas de gestão suportadas pelo GP-PME (nome do módulo em ``adapters/``).
PLATAFORMAS: list[str] = ["clickup", "notion", "trello", "jira", "linear"]

#: Plataforma usada quando ``GPPME_PLATAFORMA`` não está definida.
PLATAFORMA_PADRAO = "trello"

# Cache do singleton de :func:`adapter_ativo` (chaveado pelo nome da plataforma).
_adapter_ativo: PlataformaGestao | None = None
_adapter_ativo_nome: str | None = None


def get_adapter(nome: str) -> PlataformaGestao:
    """Instancia o adapter da plataforma ``nome``.

    Importa preguiçosamente o módulo ``adapters.<nome>`` (assim uma dependência
    de uma plataforma que você não usa nunca é carregada) e instancia a sua
    classe ``Adapter``.

    Args:
        nome: nome curto da plataforma, ex.: ``"trello"`` — ver :data:`PLATAFORMAS`.

    Returns:
        Uma instância de :class:`~adapters.base.PlataformaGestao` pronta para uso
        (em dry-run se as credenciais não estiverem no ambiente).

    Raises:
        ValueError: se a plataforma for desconhecida ou se o módulo existir mas
            não expuser a classe ``Adapter`` esperada. A mensagem é em PT-BR e
            lista as plataformas válidas.
    """
    chave = (nome or "").strip().lower()
    if chave not in PLATAFORMAS:
        suportadas = ", ".join(PLATAFORMAS)
        raise ValueError(
            f"Plataforma '{nome}' não é suportada pelo GP-PME. "
            f"Escolha uma destas: {suportadas}. "
            f"Você pode defini-la na variável de ambiente GPPME_PLATAFORMA."
        )

    try:
        modulo = importlib.import_module(f".{chave}", __package__)
    except ImportError as exc:
        raise ValueError(
            f"A plataforma '{chave}' é reconhecida, mas o seu adapter ainda não "
            f"está disponível (módulo 'adapters/{chave}.py' ausente ou com erro de "
            f"importação): {exc}. "
            f"Enquanto isso, use uma plataforma já implementada ({', '.join(PLATAFORMAS)})."
        ) from exc

    adapter_cls = getattr(modulo, "Adapter", None)
    if adapter_cls is None:
        raise ValueError(
            f"O módulo 'adapters/{chave}.py' existe mas não expõe a classe 'Adapter' "
            f"exigida pelo contrato do GP-PME (ver CONVENTIONS.md)."
        )
    return adapter_cls()


def adapter_ativo() -> PlataformaGestao:
    """Retorna o adapter da plataforma corrente (singleton).

    A plataforma corrente vem de ``GPPME_PLATAFORMA`` (padrão:
    :data:`PLATAFORMA_PADRAO` = ``"trello"``). A instância é criada uma única vez
    e reaproveitada; se ``GPPME_PLATAFORMA`` mudar entre chamadas, o singleton é
    recriado para a nova plataforma.

    É tolerante a adapters ainda inexistentes: se o módulo da plataforma escolhida
    não estiver pronto, propaga um :class:`ValueError` com mensagem clara em PT-BR
    (via :func:`get_adapter`) em vez de um erro de importação opaco.
    """
    global _adapter_ativo, _adapter_ativo_nome
    nome = os.environ.get("GPPME_PLATAFORMA", PLATAFORMA_PADRAO).strip().lower() or PLATAFORMA_PADRAO
    if _adapter_ativo is None or _adapter_ativo_nome != nome:
        _adapter_ativo = get_adapter(nome)
        _adapter_ativo_nome = nome
    return _adapter_ativo


__all__ = ["PLATAFORMAS", "PLATAFORMA_PADRAO", "get_adapter", "adapter_ativo"]
