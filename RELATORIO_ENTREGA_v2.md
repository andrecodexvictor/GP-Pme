# 📋 Relatório de Entrega — GP-PME Edição Comercial v2.0

**Data de conclusão:** 2026-07-08
**Escopo:** transformação do repositório GP-PME (documentação de framework de gestão de TI para PMEs) em produto de nível comercial, com busca semântica, ecossistema de agentes de IA, integração com plataformas de gestão, servidor MCP/API, simulação de valor e kit de vendas.
**Método de execução:** orquestração de até 15 subagentes paralelos (Claude Opus/Sonnet) com posse exclusiva de arquivos por agente, contratos de interface escritos antes do fan-out, e integração/QA centralizados.
**Volume entregue:** ~100 arquivos novos, ~28,8 mil linhas, 10 commits lógicos.
**Restrição de ouro respeitada:** nenhuma prosa pré-existente do framework foi alterada — somente adições (as duas exceções autorizadas: INDEX.md/README.md receberam conteúdo aditivo, e o bug factual DAN/COT numa skill legada foi corrigido).

---

## 1. Contexto e diagnóstico inicial

O repositório continha ~98% documentação em PT-BR de alta qualidade (7 guias dos 4 pilares, templates de 1 página, modelo de maturidade 5×4 com índice IM-TI, guias para leigos, portal HTML), porém:

- **Zero código de busca** — a "otimização RAG" era apenas um bloco `<rag-metadata>` XML dentro do INDEX.md, sem motor que o consumisse.
- **Zero agentes executáveis** — os 4 agentes especialistas existiam só como system prompts em um template.
- **Nenhuma referência a Google ADK** — a criação de agentes ADK foi greenfield.
- **Skills fora do padrão** — havia skills em `SKill folder/` (formato Manus/Linux) não instaladas no repo, uma delas com um **bug grave de terminologia**: definia DAN/COT como padrões de *jailbreak* ("Do Anything Now"/chain-of-thought bypass), contradizendo as métricas reais do framework.
- **INDEX aquém de produto pago** e nenhum material de vendas, precificação ou demonstração de ROI.
- **`.gitignore` em modo whitelist** — só `GP-PME/`, `GP-PME antigravity/` e o README eram versionados; até o portal HTML ficava fora do git.

## 2. Ferramentas de processo utilizadas

| Ferramenta | Papel | Resultado |
|---|---|---|
| **graphify** (CLI + MCP) | Geração do grafo de conhecimento semântico | `graphify extract . --backend claude-cli` processou os 37 documentos (147k tokens) **sem chave de API**, usando o Claude CLI local; `cluster-only` gerou graph.html + GRAPH_REPORT.md. Registrado no `.mcp.json`. |
| **dotcontext** (MCP) | Harness de contexto e workflow PREVC | `.context/` inicializado (9 docs, 15 playbooks, 10 skills de scaffolding); workflow `gp-pme-edicao-comercial-v2` (escala LARGE, autônomo) criado e avançado P→R→**E**. Fechamento V→C pendente de reconexão do MCP. |
| **Subagentes paralelos** | Execução dos workstreams | 4 ondas de lançamento (15 + 11 + 8 + 3 agentes) — as 3 primeiras interrompidas por limites de sessão, com retomada incremental baseada em inventário de disco a cada onda (nenhum trabalho parcial foi perdido; agentes relançados completavam apenas o que faltava). |

## 3. Entregas por workstream

### 3.1 🔎 Motor de busca semântica (`search/` — 14 arquivos, ~1,3k linhas de código)

**Decisão de arquitetura (aprovada pelo usuário):** híbrido Python + Web.

- **Contrato primeiro**: `search/SCHEMA.md` fixa todos os formatos (corpus.jsonl, embeddings.npz, bm25.json, CLI, API, search-index.json) — foi o que permitiu 3 subagentes trabalharem em paralelo sem conflito.
- **`ingest.py`**: varre os `.md` do framework (incluindo Simulacao/ e Comercial/ criados depois — reindexado ao final), chunking por H2/H3 com alvo de 300–500 palavras, breadcrumb por documento, e **keywords herdadas do bloco `<rag-metadata>` do INDEX** (parse tolerante, associação por nome de arquivo). Resultado final: **675 chunks de 62 documentos**.
- **`build_index.py`**: gera **sempre** o índice BM25 puro-Python (k1=1.5, b=0.75, tokenização com remoção de acentos e stopwords PT-BR — zero dependências) e, **opcionalmente**, embeddings com `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` (float32, L2-normalizados). Sem o pacote, degrada graciosamente com aviso.
- **`query.py`**: CLI `python -m search.query "pergunta" [--k] [--modo hibrido|semantico|bm25] [--json]`; score híbrido = 0,6·cosseno + 0,4·BM25 normalizado; expõe `buscar()` importável (reusada pela API e pelo server MCP).
- **`api.py`**: FastAPI mínima (`GET /search`, `GET /health`).
- **`export_web.py` + `GP-Pme Article/busca.html`**: busca **offline no navegador** (via `search-data.js` com `window.GPPME_INDEX`, contornando o bloqueio de fetch em `file://`), filtros por pilar e tipo, destaque de termos, tema claro/escuro — zero instalação para o cliente final.

**Bugs encontrados e corrigidos no QA:**
1. CLI quebrava no console Windows cp1252 ao imprimir emojis → `stream.reconfigure(encoding="utf-8", errors="replace")` no `main()`.
2. `embeddings.npz` salvava ids como `dtype=object` (exigia pickle inseguro no load) → corrigido para `dtype="U"` e índice reconstruído.

**Validação:** consultas reais ("como implantar o kanban", "o que é DAN", "qual o ROI ... 50 funcionários") retornam as seções corretas, inclusive do conteúdo comercial novo.

### 3.2 🕸️ Grafo de conhecimento (`graphify-out/`)

- Extração semântica dos 37 documentos com o backend **claude-cli** (sem custo de API; a primeira tentativa falhou por coincidir com a janela de limite de sessão — reexecutada com sucesso: 147.592 tokens de entrada, 37.344 de saída).
- `graph.json` (consultável via `graphify query`/MCP `graphify.serve`), `graph.html` (visualização interativa com comunidades nomeadas) e `GRAPH_REPORT.md`.
- Complementa a busca: a busca responde "onde está X?", o grafo responde "o que conecta X a Y?".

### 3.3 🤖 Agentes Google ADK (`agents/gp-pme-adk/` — 31 arquivos, ~4,4k linhas)

**Decisão (aprovada):** código ADK executável **e** versões markdown plug-and-play.

- **Contrato primeiro**: `CONVENTIONS.md` (padrão de `agent.py`, formato da INSTRUCTION, regra de imports, quadro canônico) + `adapters/base.py` (classe abstrata `PlataformaGestao`, dataclasses `Quadro`/`Cartao`, constantes do protocolo: 4 colunas, `LIMITE_WIP=3`, etiqueta 🔥 Raia Rápida, as 8 `FASE_ZERO_TASKS`).
- **Orquestrador `orquestrador_gp_pme`** ("Gestor GP-PME"): multi-agente com os 8 especialistas como `sub_agents` (imports tolerantes — funciona mesmo com especialista ausente), ferramentas de plataforma, e INSTRUCTION com o protocolo completo (diagnóstico de maturidade → Fase Zero → quadro na plataforma → cadências semanais → métricas mensais) e regras HITL (nunca executar mudança destrutiva sem confirmação humana; citar fontes).
- **8 especialistas**, cada um com INSTRUCTION de ~100–150 linhas destilada do guia-fonte (citado no bloco FONTES) e **ferramentas Python reais**: `agente_governanca` (pauta CD-TI Lite, RACI-Lite, Matriz 4 Quadrantes), `agente_execucao_agil` (tasklist de sprint, diagnóstico de fluxo/WIP, raia rápida), `agente_seguranca` (checklist 10 controles, risco P×I, plano de resposta), `agente_metricas_auditoria` (calcular_kpis IDSC/TMpR/ISU, calcular_dan com zonas, calcular_cot/payback, auditoria HITL), `agente_maturidade` (questionário, calcular_im_ti, plano de transição), `agente_fase_zero` (checklist, cronograma, prontidão), `agente_prd` (esqueleto/validação de PRD), `agente_prompts` (prompt mestre, avaliação).
- **5 adapters de plataforma** (ClickUp v2, Notion 2022-06-28, Trello REST, Jira Cloud v3, Linear GraphQL): modo real via httpx com mensagens de erro PT amigáveis e passo a passo de credenciais na docstring; **modo dry-run stateful** (default sem credenciais) que simula quadro/cards em memória — permite demonstração completa do produto sem nenhuma conta.
- **`tests/test_adapters_dry_run.py`**: parametrizado nas 5 plataformas — cria o quadro canônico, verifica 4 colunas + 8 tasks da Fase Zero, estoura o WIP e confere o diagnóstico. **Resultado: 5/5 passed.**
- `README.md` nível produto (arquitetura mermaid, `adk run`/`adk web`, tabela de env vars, troubleshooting Windows) + `.env.example` comentado.
- *Limitação documentada:* `google-adk` não está instalado nesta máquina — validação por `py_compile` + execução real das tools + stub do SDK; execução ao vivo requer `pip install google-adk` + `GOOGLE_API_KEY`.

### 3.4 📋 Agentes Prontos (`Agentes_Prontos/` — 10 arquivos, ~1,2k linhas)

9 agentes plug-and-play (Orquestrador, Governança, Execução Ágil, Segurança, Métricas e Auditoria, Maturidade, Fase Zero, PRD, Engenheiro de Prompts) com estrutura fixa: cabeçalho (pilar, autonomia com HITL) → **Instalação em 2 minutos** (Claude Projects / GPT personalizado / Google ADK / qualquer chat, com a lista exata de documentos a anexar) → **SYSTEM PROMPT completo e auto-contido** (~80–150 linhas, com os números exatos do framework: WIP=3, zonas do DAN, fórmulas dos KPIs que o agente "simula") → 3 exemplos de uso → fontes. + `README.md` catálogo com árvore de decisão "qual agente escolher pela sua dor".

### 3.5 🧩 Skills Claude Code (`.claude/skills/` — 8 skills, ~850 linhas)

`gp-pme-consultor` (porta de entrada/roteamento), `gp-pme-fase-zero`, `gp-pme-kanban`, `gp-pme-governanca`, `gp-pme-seguranca`, `gp-pme-metricas`, `gp-pme-maturidade`, `gp-pme-prd`. **Filosofia de engate:** a skill é o motor enxuto (fluxo numerado + tabela FONTES NO FRAMEWORK caminho→o que extrair + saídas esperadas + exemplos); o conhecimento mora nos guias — qualquer repositório que contenha `GP-PME antigravity/` pluga as skills copiando a pasta. Todas ativas e registradas nesta sessão.

**Correções na skill legada `criador-de-frameworks-gestao`:** (a) bug DAN/COT eliminado (agora Dívida de Arquitetura Normalizada / Custo de Otimização Tecnológica); (b) o stub `example.py` foi substituído por `scaffold_framework.py` funcional (gera README, INDEX com esqueleto de rag-metadata, guias por pilar, templates e dummies para um novo framework; testado com execução real, incluindo `--selftest`).

### 3.6 🔌 Servidor MCP + API REST (`server/` — 6 arquivos, ~1,2k linhas) — *pedido adicional do usuário*

Para **ambientes hostis a ferramentas de gestão** (sem ClickUp/Jira, mas com um agente de IA via MCP ou `curl` interno):

- **`core.py` (664 linhas, zero dependências)**: regras de negócio puras com fórmulas rastreadas aos guias — `avaliar_maturidade` (IM-TI, nível 1–5 global e por pilar), `calcular_kpis` (IDSC/TMpR/ISU), `calcular_dan` (com zonas e recomendação citando a fonte), `calcular_cot`, `calcular_roi_simplificado` (por perfil A–D), `protocolo_kanban` (spec do quadro + 8 tasks), `checklist_fase_zero`, `checklist_10_controles`, `listar_artefatos` (catálogo), `obter_documento` (**anti path-traversal**: resolve contra a raiz e rejeita escapes; só `.md`; máx 200 KB) e `buscar_conhecimento` (integra `search/` com fallback orientado).
- **`api.py`**: 12 endpoints REST com Pydantic, OpenAPI em PT, CORS, e API key opcional via `GPPME_API_KEY`/`X-API-Key`.
- **`mcp_server.py`**: FastMCP stdio com as 11 tools em PT.
- **`.mcp.json` na raiz**: registra `gp-pme`, `dotcontext` e `graphify` — quem abre o Claude Code no repo ganha os três servidores.
- **Validação:** import e API testados em **Python 3.10** (o SDK `mcp` exige ≥3.10; documentado) — `/health` e `/maturidade` respondendo corretamente; traversal `../segredo.md` rejeitado com erro seguro.

### 3.7 📊 Simulação de implantação (`Simulacao/` — 6 arquivos, ~1,2k linhas)

Metodologia única (`Calculadora_ROI.md` com todas as fórmulas parametrizadas e exemplos resolvidos) aplicada a 4 perfis, cada um com 7 seções (retrato → cenário sem framework com linha de base e premissas explícitas → implantação semana a semana com artefatos citados → cenário com framework em 90 dias/12 meses com melhorias justificadas pelo mecanismo → antes×depois com mermaid → ROI conservador/esperado → riscos evitados mapeados aos 10 controles NIST-Lite):

| Perfil | Porte | TI | COT (implantação) | Ganho anual | ROI | Payback |
|---|---|---|---|---|---|---|
| A — TI Solo | ~10 func. | 1 | R$ 5.280 | R$ 28.608 | 542% | 2,2 meses |
| B — 25 func. | 25 | 1–2 | R$ 9.570 | R$ 62.340 | 651% | 1,8 meses |
| C — 50 func. | 50 | 3 + gestor | R$ 20.680 | R$ 128.484 | 621% | 1,9 meses |
| D — 100 func. | 100 | 5–8 + DPO | R$ 65.800 | R$ 265.800 | 404% | 3,0 meses |

A aritmética dos 4 perfis foi conferida manualmente e bate com o README da pasta (cenários conservadores incluídos: C 373%/3,2m; D 242%/5,0m). No perfil D, os agentes ADK, o servidor MCP e a LGPD são centrais na narrativa (multa LGPD citada mas mantida fora do ROI para não inflar).

### 3.8 💼 Kit comercial (`Comercial/` — 4 documentos)

- **Proposta_de_Valor.md**: 7 dores clássicas da TI de PME → capacidade do GP-PME (com artefato e caminho) → prova (norma + perfil da simulação); diferenciais vs consultoria tradicional / ITIL-COBIT completos / inércia; elevator pitch de 30s.
- **One_Pager_Vendas.md**: 3 números de impacto conservadores (R$ 4.930/mês recuperáveis; R$ 12.000/ano de risco evitado; payback ~1,8 meses).
- **Modelo_de_Precificacao.md**: tiers anuais por empresa — **Essencial R$ 2.400** (docs + templates + busca web), **Profissional R$ 8.900** (+ skills + agentes markdown + simulação personalizada), **Enterprise a partir de R$ 24.900** (+ agentes ADK instalados + MCP/API + implantação assistida) — ancorados no custo médio de um incidente evitado (R$ 80.000); FAQ com 5 objeções; licença por CNPJ com 12 meses de atualizações.
- **Onboarding_Cliente.md**: entrega D0→D30 sobre o playbook da Fase Zero, com responsável, artefato e critério de aceite por semana; script de kickoff de 60 min; e-mail-modelo.

Consistência numérica verificada entre os 4 documentos e a Simulação.

### 3.9 💎 INDEX premium v2.0 + README

INDEX reorganizado como vitrine de produto: capa com versão/tagline/proposta de valor, "Comece em 30 minutos", mapa Mermaid dos pilares, trilhas por persona com tempo estimado (CEO, gestor de TI, consultor, dev), catálogo completo "artefato | o que é | quando usar | link", seção "Ecossistema de IA em 4 camadas" (skills → agentes MD → agentes ADK → MCP/API) e changelog v1.0→v2.0. **O mapa ASCII e o bloco `<rag-metadata>` originais foram preservados integralmente** (a busca depende dele), com novas entradas apenas adicionadas. README raiz recebeu somente a seção nova "🚀 Novidades da Edição Comercial (v2.0)".

### 3.10 🔧 Infraestrutura do repositório

- `.gitignore` (whitelist) estendido com exceções para todos os entregáveis + exclusões de artefatos de execução (`__pycache__`, `.pytest_cache`, `graphify-out/cache/`, `.env`).
- O portal `GP-Pme Article/` (antes fora do git) passou a ser versionado.
- Memória persistente do projeto gravada (arquitetura, regras do repo, pegadinhas: Python 3.9 default vs 3.10 para MCP, console cp1252, graphify via claude-cli).

## 4. QA consolidado

| Verificação | Resultado |
|---|---|
| pytest adapters (5 plataformas, dry-run, quadro canônico + WIP) | ✅ 5/5 passed |
| Busca híbrida (3 consultas de controle, incl. conteúdo novo) | ✅ seções corretas |
| Fallback BM25 sem sentence-transformers | ✅ degrada com aviso |
| API REST `/health` + `/maturidade` (py 3.10) | ✅ respostas corretas |
| Import `server.mcp_server` (py 3.10) | ✅ |
| Path traversal em `obter_documento` | ✅ bloqueado |
| Links relativos em todos os docs novos + INDEX + README | ✅ 0 quebrados |
| Terminologia DAN/COT fora de References/ | ✅ 0 ocorrências do bug |
| Prosa pré-existente intocada / rag-metadata preservado | ✅ conferido |
| Aritmética da Simulação × README × Comercial | ✅ consistente |

## 5. Incidentes de processo (transparência)

- **Limites de sessão** interromperam 3 ondas de subagentes (resets 11h, 16h10, 21h10, 2h10, 10h30). Mitigação: inventário de disco a cada retomada + relançamento apenas do delta, com autorização para completar arquivos parciais da própria posse. Nenhum trabalho foi perdido; nenhuma posse de arquivo foi violada.
- **graphify** falhou 2× (sem chave de API; depois timeout do claude-cli durante a janela de limite) antes de concluir na 3ª execução.
- **dotcontext** conectou tardiamente e desconectou após o registro do workflow (fase E) — fechamento V→C pendente (1 comando ao reconectar).
- **Classificador opus indisponível** bloqueou o primeiro fan-out de 15 agentes (14 falharam no lançamento); relançados com sucesso em seguida.

## 6. Como usar (atalhos)

```bash
# Busca (qualquer Python 3.9+)
python -m search.query "como implantar o kanban" --k 5
python -m uvicorn search.api:app --port 8765          # API de busca

# Busca sem instalar nada: abrir "GP-Pme Article/busca.html" no navegador

# Servidor do framework (Python >= 3.10; nesta máquina: py -3.10)
py -3.10 -m uvicorn server.api:app --port 8766        # REST + /docs
py -3.10 -m server.mcp_server                          # MCP stdio

# Agentes ADK (requer pip install google-adk + GOOGLE_API_KEY)
cd agents/gp-pme-adk && adk web                        # UI local dos agentes
# Demonstração sem credenciais: GPPME_DRY_RUN=1

# Grafo
start graphify-out/graph.html
graphify query "o que conecta DAN ao Pilar 2?"

# Testes
cd agents/gp-pme-adk && python -m pytest tests/ -q    # 5/5
```

## 7. Próximos passos recomendados

1. Instalar `google-adk` e fazer um smoke real do orquestrador com chave Gemini (`adk web`).
2. Fechar o workflow dotcontext (V→C) e, se desejar, preencher os 33 placeholders de `.context/`.
3. Gravar um vídeo-demo de 3 min (busca.html + orquestrador em dry-run no Trello) para o kit comercial.
4. Piloto com 1 cliente do Perfil B (melhor payback) usando o Onboarding_Cliente.md.
5. Publicar o repositório privado para clientes (o `.gitignore` já protege References/ e rascunhos).

---
*Relatório gerado ao final da entrega da Edição Comercial v2.0 — GP-PME.*
