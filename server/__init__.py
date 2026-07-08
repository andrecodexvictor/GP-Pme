"""Servidor do framework GP-PME — serviço puro, API REST e servidor MCP.

Camada de servidor para ambientes hostis a ferramentas de gestão (sem
ClickUp/Jira): expõe as regras de negócio do GP-PME (maturidade, KPIs, DAN,
COT, ROI, Kanban, Fase Zero, Segurança) e a busca no corpus tanto para um
agente de IA (via MCP) quanto para automações internas (via curl na API REST).

Módulos:
    core        Serviço puro (sem framework web); toda a lógica de negócio.
    api         API REST FastAPI que expõe `core` por HTTP.
    mcp_server  Servidor MCP (stdio) que expõe `core` como tools para IA.

O servidor NÃO importa dos agentes ADK (agents/gp-pme-adk/...): a lógica de
negócio é duplicada deliberadamente em `core.py` para manter esta camada
independente do runtime de agentes. Ver server/README.md.
"""

__version__ = "1.0.0"
