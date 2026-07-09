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

## 🧱 Diagrama de blocos (visão em quadradinhos)

A mesma arquitetura em blocos, camada por camada, com o fluxo que cada coisa segue —
de onde o conhecimento nasce (topo) até quem consome (base):

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                     📚 NÚCLEO DE CONHECIMENTO (fonte da verdade)               │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌───────────────────────┐  │
│  │  INDEX.md    │ │  Guides/     │ │  Templates/  │ │  dummies + capítulos  │  │
│  │  v2.0 + rag- │ │  7 guias dos │ │  7 artefatos │ │  + documentos mestre  │  │
│  │  metadata    │ │  4 pilares   │ │  de 1 página │ │  (leigos e técnico)   │  │
│  └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ └───────────┬───────────┘  │
└─────────┼────────────────┼────────────────┼─────────────────────┼──────────────┘
          │ keywords       │ chunking / destilação / fórmulas     │
          ▼                ▼                ▼                     ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                          🔎 CAMADA DE DESCOBERTA                               │
│  ┌───────────┐   ┌──────────────┐   ┌─────────────┐   ┌────────────────────┐  │
│  │ ingest.py │──▶│ corpus.jsonl │──▶│ bm25.json + │──▶│ CLI · API /search  │  │
│  │ (chunks)  │   │  675 chunks  │   │ embeddings  │   │ · busca.html (off) │  │
│  └───────────┘   └──────┬───────┘   └─────────────┘   └────────────────────┘  │
│                         │ export_web        ┌──────────────────────────────┐  │
│                         └───────────────▶   │ graphify-out/ (grafo:        │  │
│                                             │ graph.html + query + report) │  │
│                                             └──────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                    🤖 ECOSSISTEMA DE IA (4 camadas, leve → integrado)          │
│                                                                                │
│  ① ┌────────────────────┐  ② ┌────────────────────┐                            │
│    │ .claude/skills/    │    │ Agentes_Prontos/   │                            │
│    │ 8 skills gp-pme-*  │    │ 9 system prompts   │                            │
│    │ (Claude Code)      │    │ (Projects/GPTs)    │                            │
│    └────────────────────┘    └────────────────────┘                            │
│                                                                                │
│  ③ ┌─────────────────────────────────────────────┐                             │
│    │        agents/gp-pme-adk/ (Google ADK)      │                             │
│    │  ┌───────────────┐   ┌────────────────────┐ │                             │
│    │  │ orquestrador  │──▶│ 8 especialistas    │ │                             │
│    │  │ Gestor GP-PME │   │ gov·agil·seg·metr· │ │                             │
│    │  └───────┬───────┘   │ mat·fz·prd·prompts │ │                             │
│    │          │           └────────────────────┘ │                             │
│    │          ▼                                  │                             │
│    │  ┌───────────────────────────────────────┐  │                             │
│    │  │ adapters/ (base + 5 plataformas)      │  │                             │
│    │  └──────────────────┬────────────────────┘  │                             │
│    └─────────────────────┼───────────────────────┘                             │
│                          ▼                                                     │
│    ┌────────┐ ┌────────┐ ┌────────┐ ┌──────┐ ┌────────┐                        │
│    │ClickUp │ │ Notion │ │ Trello │ │ Jira │ │ Linear │  🏢 plataformas        │
│    └────────┘ └────────┘ └────────┘ └──────┘ └────────┘                        │
│                                                                                │
│  ④ ┌─────────────────────────────────────────────┐                             │
│    │   server/ (para ambientes restritos)        │                             │
│    │  ┌─────────┐    ┌──────────┐  ┌───────────┐ │                             │
│    │  │ core.py │───▶│ api.py   │  │ mcp_      │ │                             │
│    │  │ (regras │    │ REST ·12 │  │ server.py │ │                             │
│    │  │  puras) │───▶│ rotas    │  │ ·11 tools │ │                             │
│    │  └─────────┘    └──────────┘  └───────────┘ │                             │
│    └─────────────────────────────────────────────┘                             │
└───────────────────────────────────────────────────────────────────────────────┘
          │
          ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                          💼 CAMADA DE NEGÓCIO                                  │
│  ┌─────────────────────────────┐        ┌─────────────────────────────────┐   │
│  │ Simulacao/                  │───────▶│ Comercial/                      │   │
│  │ 4 perfis (10→100 func.)     │números │ proposta · one-pager ·          │   │
│  │ + Calculadora_ROI           │        │ precificação · onboarding 30d   │   │
│  └─────────────────────────────┘        └─────────────────────────────────┘   │
└───────────────────────────────────────────────────────────────────────────────┘
          │
          ▼
   ┌─────────────────┐
   │ 👤 CLIENTE /    │   consome por qualquer porta: busca.html, CLI, API,
   │    CONSULTOR    │   MCP, agentes, skills, simulação e kit comercial
   └─────────────────┘
```

## 🕸️ Grafo de relações entre componentes

Visão em grafo (estilo knowledge graph): quem **deriva de**, **consome** ou **opera** quem.

```mermaid
graph LR
    GUIAS(("Guias dos<br/>4 Pilares"))
    TPL(("Templates<br/>1 página"))
    RAG(("rag-metadata<br/>do INDEX"))

    CORPUS["corpus.jsonl"]
    IDX["índices<br/>BM25 + embeddings"]
    BHTML["busca.html"]
    GRAFO["graph.json<br/>(graphify)"]

    SKILLS["8 skills<br/>gp-pme-*"]
    PRONTOS["9 agentes<br/>markdown"]
    ADK["9 agentes<br/>ADK"]
    ADAPT["5 adapters"]
    CORE["server/core.py"]
    REST["API REST"]
    MCPS["MCP server"]

    SIM["Simulação<br/>4 perfis"]
    COM["Kit<br/>Comercial"]
    KAN["Quadro Kanban<br/>na plataforma"]

    GUIAS -- "chunking" --> CORPUS
    TPL -- "chunking" --> CORPUS
    RAG -- "keywords" --> CORPUS
    CORPUS --> IDX
    CORPUS -- "export_web" --> BHTML
    GUIAS -- "extração LLM" --> GRAFO

    GUIAS -- "destilados em" --> SKILLS & PRONTOS & ADK
    TPL -- "geram artefatos via" --> ADK
    GUIAS -- "fórmulas exatas" --> CORE
    CORE --> REST & MCPS
    IDX -- "buscar()" --> CORE

    ADK -- "usa tools de" --> ADAPT
    ADAPT -- "cria/opera" --> KAN

    GUIAS -- "metodologia" --> SIM
    SIM -- "números-âncora" --> COM

    classDef fonte fill:#1a5276,color:#fff
    class GUIAS,TPL,RAG fonte
```

## 🔁 Fluxograma do protocolo de gestão (o que os agentes executam)

O protocolo operacional do framework — é este fluxo que o orquestrador "Gestor GP-PME",
as skills e os agentes prontos conduzem na empresa:

```mermaid
flowchart TD
    START(["Empresa adota o GP-PME"]) --> DIAG["Autoavaliação de maturidade<br/>(10 perguntas → IM-TI)"]
    DIAG --> NIVEL{"Nível de<br/>maturidade?"}
    NIVEL -- "0-1 (caos)" --> FZ["FASE ZERO (30 dias):<br/>1. Nomear Dono da TI + CD-TI Lite<br/>2. Canal Único de demandas<br/>3. Kanban 4 colunas, WIP=3<br/>4. Matriz 4 Quadrantes<br/>5. KPIs IDSC/TMpR/ISU<br/>6. Checklist 10 controles<br/>7. Primeiro sprint semanal"]
    NIVEL -- "2+" --> KANOP
    FZ --> KANOP["OPERAÇÃO SEMANAL<br/>Sprint de 1 semana"]

    KANOP --> PUXA["Puxar tarefa de 'A Fazer'<br/>para 'Em Andamento'"]
    PUXA --> WIP{"WIP ≤ 3?"}
    WIP -- "não" --> TERMINA["Terminar um item antes<br/>de puxar outro"] --> PUXA
    WIP -- "sim" --> EXEC["Executar → Em Teste → Concluído"]

    EXEC --> EMERG{"Emergência<br/>crítica?"}
    EMERG -- "sim" --> RAIA["🔥 RAIA RÁPIDA:<br/>suspende tarefa menos prioritária,<br/>foco 100% no incidente"] --> PRI["Plano de Resposta<br/>a Incidentes (PRI)"] --> EXEC
    EMERG -- "não" --> RETRO["Retrospectiva semanal<br/>+ atualizar tasklist"]

    RETRO --> MES{"Fim do<br/>mês?"}
    MES -- "não" --> KANOP
    MES -- "sim" --> PAINEL["Painel mensal:<br/>IDSC · TMpR · ISU · DAN · COT"]
    PAINEL --> CDTI["Reunião CD-TI Lite<br/>(quinzenal, 30 min, CEO + TI)"]
    CDTI --> DECIDE{"DAN > 0,35<br/>ou KPI crítico?"}
    DECIDE -- "sim" --> INVEST["Aprovar investimento COT<br/>(Matriz 4 Quadrantes)"] --> KANOP
    DECIDE -- "não" --> KANOP

    CDTI -. "a cada trimestre" .-> DIAG
```

## 📊 Pipeline de dados da busca semântica

```mermaid
flowchart LR
    MD["62 documentos .md<br/>do framework"] --> I["ingest.py<br/>split H2/H3<br/>300-500 palavras"]
    META["rag-metadata<br/>(INDEX.md)"] -- keywords --> I
    I --> C[("corpus.jsonl<br/>675 chunks")]
    C --> B["build_index.py"]
    B --> BM[("bm25.json<br/>índice lexical<br/>stdlib")]
    B -. "se sentence-transformers<br/>instalado" .-> E[("embeddings.npz<br/>MiniLM 384d<br/>L2-norm")]
    C --> X["export_web.py"] --> W[("search-data.js +<br/>search-index.json")]

    Q(["pergunta do usuário"]) --> QP["query.py :: buscar()"]
    BM --> QP
    E -. "0,6·cos + 0,4·bm25" .-> QP
    QP --> R1["CLI"] & R2["GET /search<br/>(search/api.py)"] & R3["tool MCP<br/>buscar_conhecimento"]
    W --> R4["busca.html<br/>(offline no navegador)"]

    QP --> OUT(["top-k chunks com<br/>doc § seção + score"])
```

## 🤝 Sequência: instalando o GP-PME numa plataforma de gestão

```mermaid
sequenceDiagram
    autonumber
    actor U as Gestor da PME
    participant O as Orquestrador<br/>(Gestor GP-PME)
    participant M as agente_maturidade
    participant F as agente_fase_zero
    participant A as Adapter<br/>(ex.: Trello)
    participant P as Plataforma

    U->>O: "Instale o GP-PME no meu Trello"
    O->>M: delega diagnóstico
    M-->>U: 10 perguntas da autoavaliação
    U-->>M: respostas
    M-->>O: IM-TI + nível (ex.: Nível 1)
    O->>F: solicita plano de implantação
    F-->>O: checklist Fase Zero + cronograma
    O->>U: apresenta plano — confirma? (HITL)
    U-->>O: aprovado ✅
    O->>A: instalar_gp_pme_na_plataforma()
    A->>P: criar quadro + 4 colunas<br/>(Em Andamento máx 3)
    A->>P: criar 8 cards da Fase Zero
    A->>P: label 🔥 Raia Rápida
    A-->>O: quadro pronto + relatório
    O-->>U: link do quadro + próximos passos
    loop toda semana
        O->>A: verificar_wip() + relatorio_do_quadro()
        A->>P: ler estado do quadro
        O-->>U: diagnóstico do fluxo + pauta do CD-TI Lite
    end
```

## Leitura do diagrama

- **Fluxo de conhecimento:** os guias/templates são a única fonte da verdade. Tudo deriva deles — chunks da busca, instructions dos agentes, fórmulas do server, metodologia da simulação. Atualizou um guia → reindexe (`python -m search.ingest && python -m search.build_index && python -m search.export_web`) e revise o agente correspondente.
- **4 camadas de IA, do mais leve ao mais integrado:** skills (dentro do Claude Code) → agentes markdown (qualquer chat) → agentes ADK (executáveis, instalam o kanban nas plataformas) → MCP/API (o framework como serviço para ambientes restritos).
- **Duas portas para plataformas de gestão:** o orquestrador ADK opera ClickUp/Notion/Trello/Jira/Linear via adapters (com dry-run para demo); onde nada disso pode ser instalado, o `server/` expõe o protocolo via MCP ou REST.
