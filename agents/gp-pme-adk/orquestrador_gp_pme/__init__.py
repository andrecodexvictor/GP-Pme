"""Orquestrador GP-PME — agente-mestre "Gestor GP-PME".

Reexporta ``root_agent`` para que o Google ADK (``adk run orquestrador_gp_pme`` /
``adk web``) encontre o agente raiz do pacote.
"""
from .agent import root_agent

__all__ = ["root_agent"]
