# 🗺️ Arquitetura — GP-PME Edição Comercial v2.0

> Visão completa do produto: do núcleo de conhecimento às camadas de descoberta,
> IA, plataformas de gestão e negócio. Detalhes de cada componente em
> [progress.md](progress.md) e [RELATORIO_ENTREGA_v2.md](RELATORIO_ENTREGA_v2.md).

```mermaid
flowchart TB
    subgraph NUCLEO["📚 Núcleo de Conhecimento (fonte da verdade)"]
        INDEX["INDEX.md v2.0<br/>(vitrine + rag-metadata)"]
        GUIAS["Guides/ — 7 guias<br/>(Pilares 1-4, Fase Zero,<br/>KPIs, Maturidade)"]
        TPL["Templates/ — 7 artefatos<br/>de 1 página"]
        DUM["guide-for-dummies/ +<br/>GP-Pme complete/ + GP-PME/"]
    end

    subgraph BUSCA["🔎 Camada de Descoberta"]
        ING["ingest.py<br/>(chunking por heading<br/>+ keywords do rag-metadata)"]
        CORPUS[("corpus.jsonl<br/>675 chunks / 62 docs")]
        BM25[("bm25.json<br/>(stdlib, sempre)")]
        EMB[("embeddings.npz<br/>MiniLM multilíngue<br/>(opcional)")]
        CLI["CLI<br/>python -m search.query"]
        SAPI["API FastAPI<br/>/search"]
        WEB["busca.html<br/>(offline, file://)"]
        GRAPH["graphify-out/<br/>graph.html + query"]
    end

    subgraph IA["🤖 Ecossistema de IA (4 camadas)"]
        SKILLS["Skills Claude Code<br/>.claude/skills/gp-pme-*<br/>(8 skills engatáveis)"]
        PRONTOS["Agentes_Prontos/<br/>9 system prompts<br/>(Claude Projects / GPTs)"]
        subgraph ADK["Agentes Google ADK"]
            ORQ["orquestrador_gp_pme<br/>(Gestor GP-PME)"]
            ESP["8 especialistas:<br/>governança · execução ágil<br/>segurança · métricas<br/>maturidade · fase zero<br/>PRD · prompts"]
            ADAPT["adapters/<br/>base.py (contrato +<br/>quadro canônico WIP=3)"]
        end
        subgraph SRV["server/ (ambientes restritos)"]
            CORE["core.py<br/>(regras puras: IM-TI,<br/>KPIs, DAN, COT, ROI)"]
            REST["api.py<br/>FastAPI · 12 rotas"]
            MCP["mcp_server.py<br/>FastMCP · 11 tools"]
        end
    end

    subgraph PLAT["🏢 Plataformas de Gestão"]
        CU["ClickUp"]
        NO["Notion"]
        TR["Trello"]
        JI["Jira"]
        LI["Linear"]
    end

    subgraph NEGOCIO["💼 Camada de Negócio"]
        SIM["Simulacao/<br/>4 perfis + Calculadora ROI<br/>(payback 1,8-3,0 meses)"]
        COM["Comercial/<br/>proposta · one-pager ·<br/>precificação · onboarding"]
    end

    GUIAS --> ING
    TPL --> ING
    INDEX -->|rag-metadata| ING
    DUM --> ING
    ING --> CORPUS --> BM25 & EMB
    BM25 & EMB --> CLI & SAPI
    CORPUS -->|export_web| WEB
    GUIAS -.->|extração semântica| GRAPH

    GUIAS -->|fonte das instructions| ESP & PRONTOS & SKILLS
    GUIAS -->|fórmulas| CORE
    ORQ --> ESP
    ORQ --> ADAPT
    ADAPT --> CU & NO & TR & JI & LI
    CORE --> REST & MCP
    CLI -->|buscar()| CORE

    GUIAS -->|metodologia| SIM --> COM

    CLIENTE(("👤 Cliente /<br/>Consultor")) --> WEB & CLI & MCP & REST & ORQ & SKILLS & PRONTOS & SIM & COM
```

## Leitura do diagrama

- **Fluxo de conhecimento:** os guias/templates são a única fonte da verdade. Tudo deriva deles — chunks da busca, instructions dos agentes, fórmulas do server, metodologia da simulação. Atualizou um guia → reindexe (`python -m search.ingest && python -m search.build_index && python -m search.export_web`) e revise o agente correspondente.
- **4 camadas de IA, do mais leve ao mais integrado:** skills (dentro do Claude Code) → agentes markdown (qualquer chat) → agentes ADK (executáveis, instalam o kanban nas plataformas) → MCP/API (o framework como serviço para ambientes restritos).
- **Duas portas para plataformas de gestão:** o orquestrador ADK opera ClickUp/Notion/Trello/Jira/Linear via adapters (com dry-run para demo); onde nada disso pode ser instalado, o `server/` expõe o protocolo via MCP ou REST.
