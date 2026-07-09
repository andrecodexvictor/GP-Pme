# 📈 progress.md — GP-PME Edição Comercial v2.0

> Registro de progresso da transformação do framework GP-PME de repositório de
> documentação em **produto comercial completo**. Concluído em 2026-07-08.
> Relatório detalhado: [RELATORIO_ENTREGA_v2.md](RELATORIO_ENTREGA_v2.md).

## ✅ O que foi feito (visão geral)

| # | Workstream | Entrega | Status |
|---|---|---|---|
| 1 | 🔎 Busca semântica | `search/` (ingest, BM25 + embeddings, CLI, API) + `GP-Pme Article/busca.html` offline | ✅ 675 chunks / 62 docs, testada |
| 2 | 🕸️ Grafo de conhecimento | `graphify-out/` (graph.json, graph.html, GRAPH_REPORT.md) | ✅ extraído via claude-cli |
| 3 | 🤖 Agentes Google ADK | `agents/gp-pme-adk/` — orquestrador + 8 especialistas + 5 adapters de plataforma | ✅ pytest 5/5 (dry-run) |
| 4 | 📋 Agentes plug-and-play | `Agentes_Prontos/` — 9 system prompts + catálogo | ✅ |
| 5 | 🧩 Skills Claude Code | `.claude/skills/` — 8 skills gp-pme-* engatáveis | ✅ ativas |
| 6 | 🔌 Server MCP + API | `server/` — core + FastAPI (12 rotas) + FastMCP (11 tools) + `.mcp.json` | ✅ smoke-testado |
| 7 | 📊 Simulação de implantação | `Simulacao/` — 4 perfis (10→100 func.) + Calculadora ROI | ✅ aritmética conferida |
| 8 | 💼 Kit comercial | `Comercial/` — proposta de valor, one-pager, precificação, onboarding | ✅ |
| 9 | 💎 INDEX premium v2.0 | INDEX reorganizado como vitrine (rag-metadata preservado) + README Novidades | ✅ |
| 10 | 🔧 Infra do projeto | `.mcp.json`, `.context/` (dotcontext PREVC), `.gitignore` whitelist, memória | ✅ |

**Volume:** ~100 arquivos, ~28,8 mil linhas adicionadas, em 10 commits lógicos.

## 🗺️ Arquitetura do projeto

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

## 🧾 Linha do tempo dos commits

```
da2b696 chore: whitelist dos entregáveis da Edição Comercial no .gitignore
908b685 feat(busca): motor de busca semântica híbrida + portal de busca web
bb299e0 feat(adk): agentes Google ADK — Gestor GP-PME + 8 especialistas + 5 plataformas
b9c23d1 feat(agentes-prontos): 9 agentes plug-and-play em markdown + catálogo
9bf3c55 feat(skills): 8 skills Claude Code engatáveis do framework
41aa8f2 feat(server): MCP server + API REST do framework para ambientes restritos
66320f9 docs(simulacao): implantação simulada com/sem framework em 4 portes de empresa
2bdf458 docs(comercial): kit de vendas — proposta, one-pager, precificação e onboarding
1106ef6 feat(grafo): grafo de conhecimento do framework (graphify)
84df19a docs(index): INDEX premium v2.0 Edição Comercial + seção Novidades no README
```

## 🔬 QA executado

- ✅ `pytest` dos 5 adapters de plataforma em dry-run: **5/5 passed**
- ✅ Busca híbrida validada (kanban, DAN, ROI → seções corretas do corpus)
- ✅ API REST smoke-testada (`/health`, `/maturidade`); MCP importa em Python 3.10
- ✅ Path traversal bloqueado em `obter_documento` (fronteira de confiança)
- ✅ Checagem de links relativos em todos os docs novos: **0 quebrados**
- ✅ Terminologia: 0 ocorrências do bug "DAN = Do Anything Now" fora de References/
- ✅ Nenhuma prosa pré-existente do framework foi alterada (INDEX/README apenas aditivos; bloco `<rag-metadata>` preservado)

## ⏭️ Pendências conhecidas

1. **google-adk não instalado localmente** — agentes validados por compilação/stub; rodar ao vivo requer `pip install google-adk` + `GOOGLE_API_KEY`.
2. **Server requer Python ≥ 3.10** (SDK `mcp`); nesta máquina usar `py -3.10`.
3. **dotcontext**: workflow PREVC registrado até a fase Execute; fechar V→C quando o MCP reconectar (1 comando). Os 33 placeholders de `.context/` seguem vazios (opcional).
4. Embeddings pesam ~volume de torch; clientes sem Python usam a `busca.html` (zero instalação).
