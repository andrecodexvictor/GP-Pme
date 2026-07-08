# Agentes GP-PME (Google ADK) — Convenções do Pacote

> CONTRATO entre os módulos deste pacote. Todo agente e adapter DEVE seguir isto.

## Layout

```
agents/gp-pme-adk/
├── CONVENTIONS.md
├── README.md                  # PT-BR: instalação, adk run/web, env vars
├── requirements.txt           # google-adk, httpx, python-dotenv
├── .env.example
├── adapters/                  # pacote python "adapters" (ferramentas de plataforma)
│   ├── __init__.py            # get_adapter(nome) -> PlataformaGestao
│   ├── base.py                # classe abstrata + dataclasses + modo dry_run  [JÁ CRIADO]
│   ├── clickup.py │ notion.py │ trello.py │ jira.py │ linear.py
│   └── tools.py               # funções-ferramenta ADK que embrulham o adapter ativo
├── orquestrador_gp_pme/       # root multi-agente
│   ├── __init__.py            # from .agent import root_agent
│   └── agent.py
├── agente_governanca/         # e demais especialistas, mesmo padrão:
│   ├── __init__.py            # from .agent import root_agent
│   └── agent.py
├── agente_execucao_agil/  agente_seguranca/  agente_metricas_auditoria/
├── agente_maturidade/  agente_fase_zero/  agente_prd/  agente_prompts/
└── tests/
    └── test_adapters_dry_run.py
```

## Padrão de agente (`agent.py`)

```python
from google.adk.agents import Agent  # LlmAgent alias

root_agent = Agent(
    name="agente_governanca",                      # snake_case, = nome do diretório
    model=os.environ.get("GPPME_MODEL", "gemini-2.5-flash"),
    description="1 frase — usada pelo orquestrador para rotear.",
    instruction=INSTRUCTION,                        # constante no mesmo arquivo
    tools=[...],                                    # funções python simples, docstring PT-BR
)
```

- `INSTRUCTION` em PT-BR, estruturada: PERSONA / CONTEXTO DO FRAMEWORK / O QUE VOCÊ FAZ /
  COMO RESPONDE / RESTRIÇÕES (nunca inventar métricas; citar o guia-fonte; HITL para decisões críticas).
- Cada instruction cita os documentos-fonte com caminho repo-relativo em um bloco
  `FONTES:` ao final (ex.: `GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md`).
- Conteúdo da instruction: DESTILADO dos guias (não colar o guia inteiro; máx ~150 linhas).
- Ferramentas locais (sem rede) preferidas: cálculo de KPIs, scoring de maturidade,
  geração de artefatos em texto. Só o orquestrador usa os adapters de plataforma.

## Orquestrador

```python
root_agent = Agent(
    name="orquestrador_gp_pme",
    ...,
    sub_agents=[<os 8 especialistas importados via from agente_x.agent import root_agent as agente_x>],
    tools=[<funções de adapters/tools.py>],
)
```
Import dos sub-agentes: os diretórios de agentes são irmãos; o orquestrador adiciona
o diretório pai ao sys.path OU usa import relativo via pacote — padrão adotado:
`agents/gp-pme-adk/` contém um `conftest.py`-style `sys.path` helper NÃO; em vez disso,
cada `agente_x/agent.py` NÃO importa nada de outros agentes, e `orquestrador_gp_pme/agent.py`
faz `sys.path.insert(0, str(Path(__file__).resolve().parents[1]))` antes dos imports.

## Adapters

- Interface em `adapters/base.py` (já criado): implementar TODOS os métodos abstratos.
- Auth SOMENTE por env vars (ver `.env.example`): `CLICKUP_TOKEN`, `NOTION_TOKEN`,
  `TRELLO_KEY`/`TRELLO_TOKEN`, `JIRA_URL`/`JIRA_EMAIL`/`JIRA_TOKEN`, `LINEAR_API_KEY`.
- `GPPME_DRY_RUN=1` (default se credencial ausente): métodos não chamam rede; retornam
  payloads simulados realistas e acumulam em `self.acoes_planejadas` (lista de dicts).
- HTTP via `httpx` síncrono, timeout 30s, raise_for_status com mensagem PT-BR amigável.
- WIP=3: plataformas sem suporte nativo a WIP recebem o limite no NOME/descrição da coluna
  («Em Andamento (máx 3)») + verificação em `verificar_wip()`.

## Quadro canônico GP-PME (o que `configurar_quadro_gp_pme()` cria)

Colunas: `A Fazer` → `Em Andamento (máx 3)` → `Em Teste` → `Concluído`; label/tag
`🔥 Raia Rápida` para expedite; tasks da Fase Zero criadas de
`GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md` (resumidas em base.py:FASE_ZERO_TASKS).

## Regras gerais

- Python ≥3.10, Windows-safe, encoding utf-8 explícito, sem dependências além de
  requirements.txt. Docstrings e mensagens em PT-BR.
- Nenhum agente modifica arquivos do framework.
- Testes: `tests/test_adapters_dry_run.py` cobre cada adapter em dry-run (sem rede).
