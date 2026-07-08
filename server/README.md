# Servidor GP-PME — MCP + API REST

> O framework GP-PME como **serviço**: para ambientes hostis a ferramentas de gestão —
> empresas onde não se pode instalar ClickUp/Jira/Notion, mas onde um agente de IA
> (via MCP) ou um `curl` numa API interna funcionam. Todo o conhecimento e as
> calculadoras do framework (maturidade IM-TI, KPIs, DAN, COT, ROI, protocolo kanban,
> Fase Zero, checklist de segurança) ficam acessíveis por duas portas: **MCP** e **REST**.

## Arquitetura

```
                 ┌───────────────────────────┐
                 │        server/core.py     │  ← regras de negócio puras
                 │  (sem dependências; lê os │    (fórmulas dos guias do
                 │   guias e a busca search/)│     framework, com fontes)
                 └────────────┬──────────────┘
                    ┌─────────┴──────────┐
        ┌───────────▼─────────┐ ┌────────▼────────────┐
        │  server/api.py      │ │ server/mcp_server.py │
        │  FastAPI (REST)     │ │ MCP stdio (FastMCP)  │
        │  curl / integrações │ │ Claude Code/Desktop, │
        │  internas           │ │ qualquer cliente MCP │
        └─────────────────────┘ └─────────────────────┘
```

`core.py` roda **sem nenhuma dependência externa** (stdlib). As dependências só
entram nas bordas (fastapi/uvicorn para REST, mcp para o servidor MCP).

## Requisitos

- **Python ≥ 3.10** (o SDK `mcp` exige; nesta máquina use `py -3.10`).
- `pip install -r server/requirements.txt` (mcp, fastapi, uvicorn, pydantic).

## Instalação no Claude Code / Claude Desktop (MCP)

O repositório já traz um [`.mcp.json`](../.mcp.json) na raiz — abrir o Claude Code
dentro da pasta do framework registra o servidor automaticamente. Para registrar
manualmente (Claude Desktop → `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "gp-pme": {
      "command": "python",
      "args": ["-m", "server.mcp_server"],
      "cwd": "C:/caminho/para/GP-PME framework"
    }
  }
}
```

### Tools MCP expostas

| Tool | O que faz |
|---|---|
| `buscar_conhecimento` | Busca híbrida (semântica + BM25) no corpus do framework |
| `listar_artefatos` | Catálogo de guias, templates, agentes e skills com caminhos |
| `obter_documento` | Lê um `.md` do framework (anti path-traversal, máx 200 KB) |
| `avaliar_maturidade` | Autoavaliação de 10 perguntas → IM-TI, nível 1–5 por pilar |
| `calcular_kpis` | IDSC (disponibilidade %), TMpR, ISU |
| `calcular_dan` | Dívida de Arquitetura Normalizada + zona (<0,15 / 0,15–0,35 / >0,35) |
| `calcular_cot` | Custo de Otimização Tecnológica + payback |
| `calcular_roi` | ROI simplificado de implantação por perfil de empresa |
| `protocolo_kanban` | Spec do quadro canônico (4 colunas, WIP=3, raia rápida) + 8 tasks da Fase Zero |
| `checklist_fase_zero` | Passos ordenados da implantação de 30 dias |
| `checklist_seguranca` | Os 10 controles NIST-Lite / CIS IG1 |

## API REST

Subir (nesta máquina: `py -3.10` no lugar de `python`):

```bash
python -m uvicorn server.api:app --port 8766
```

Documentação interativa (OpenAPI/Swagger): `http://127.0.0.1:8766/docs`.

| Método | Rota | Exemplo |
|---|---|---|
| GET | `/health` | `curl http://127.0.0.1:8766/health` |
| GET | `/artefatos` | `curl http://127.0.0.1:8766/artefatos` |
| GET | `/documento?caminho=` | `curl "http://127.0.0.1:8766/documento?caminho=README.md"` |
| GET | `/buscar?q=&k=&modo=` | `curl "http://127.0.0.1:8766/buscar?q=kanban&k=3"` |
| GET | `/kanban/protocolo` | `curl http://127.0.0.1:8766/kanban/protocolo` |
| GET | `/fase-zero` | `curl http://127.0.0.1:8766/fase-zero` |
| GET | `/seguranca/checklist` | `curl http://127.0.0.1:8766/seguranca/checklist` |
| POST | `/maturidade` | `curl -X POST .../maturidade -H "Content-Type: application/json" -d "{\"respostas\":[3,3,3,3,3,3,3,3,3,3]}"` |
| POST | `/kpis` | body com horas de indisponibilidade/totais, tempos de resposta, notas |
| POST | `/dan` | `-d "{\"itens_legados\":3,\"itens_totais\":10}"` |
| POST | `/cot` | `-d "{\"custo_otimizacao\":9570,\"ganho_mensal\":5195}"` |
| POST | `/roi` | perfil (`A`/`B`/`C`/`D`) + parâmetros opcionais |

## Segurança

- **Path traversal bloqueado**: `obter_documento` resolve o caminho contra a raiz do
  repositório e rejeita qualquer escape (`../`, absolutos); só serve `.md` até 200 KB.
- **API key opcional**: defina `GPPME_API_KEY` no ambiente e a API passa a exigir o
  header `X-API-Key` em toda rota (sem a env, a API fica aberta — pensada para rede
  interna; não exponha à internet sem a chave e um proxy TLS).
- **CORS liberado** por padrão para facilitar integrações internas.

## Busca semântica

`buscar_conhecimento`/`/buscar` usam o motor de [`search/`](../search/README.md).
Se os índices não existirem, a resposta orienta: `python -m search.ingest` →
`python -m search.build_index`. Sem `sentence-transformers`, a busca degrada
automaticamente para BM25 (lexical) — nenhuma dependência pesada é obrigatória.
