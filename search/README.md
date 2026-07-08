# Busca GP-PME

Motor de busca híbrida (semântica + léxica) sobre todo o conteúdo do framework
GP-PME: guias, templates, capítulos e material comercial. Responde em
linguagem natural ("como implantar o kanban?") e devolve os trechos exatos
dos documentos mais relevantes, com origem (`doc` § `seção`) rastreável.

## Por que híbrida

- **BM25** (léxico) acerta buscas por termo exato — sigla, nome de template,
  jargão específico do framework ("WIP", "Pilar 3", "Guia_Dummies").
- **Semântica** (embeddings multilíngues) acerta perguntas em linguagem
  natural mesmo sem as palavras exatas do texto original.
- **Modo `hibrido`** (default) combina os dois: `0.6 * cosseno + 0.4 * bm25`,
  ambos normalizados (min-max) sobre o top-50 de cada método.

Se o pacote de embeddings não estiver instalado, a busca **degrada
automaticamente** para BM25 puro — nunca quebra, só fica menos esperta (com
aviso em `stderr`).

## Arquitetura

```
GP-PME antigravity/, GP-PME/, Docs/, Simulacao/, Comercial/, README.md
                    │
                    ▼
            search/ingest.py            (*)
                    │  chunking por H2/H3, 300–500 palavras
                    ▼
          search/data/corpus.jsonl      (*)
                    │
                    ▼
          search/build_index.py         (*)
             │                  │
             ▼                  ▼
  data/embeddings.npz     data/bm25.json      (*)
  (sentence-transformers)  (puro Python)
             │                  │
             └────────┬─────────┘
                       ▼
               search/query.py   ── CLI: python -m search.query "..."
                       │
                       ▼
               search/api.py     ── FastAPI: GET /search, GET /health
                       │
                       ▼
          GP-Pme Article/busca.html   (MiniSearch, sem backend, via
          + search-index.json           search/export_web.py)          (*)
```
`(*)` — gerados por outros módulos do pacote (`ingest.py`, `build_index.py`,
`export_web.py`); este README documenta apenas `query.py` e `api.py`.

## Instalação

### Mínima (busca lexical, sem dependências)

Nenhuma instalação além do Python 3.10+. O modo `bm25` roda só com
biblioteca padrão:

```bash
python -m search.ingest          # gera data/corpus.jsonl
python -m search.build_index     # gera data/bm25.json (embeddings.npz é opcional)
python -m search.query "como implantar o kanban" --modo bm25
```

### Completa (busca semântica + API)

```bash
pip install -r search/requirements.txt
python -m search.ingest
python -m search.build_index     # agora também gera data/embeddings.npz
python -m search.query "como implantar o kanban"     # modo hibrido (default)
uvicorn search.api:app --port 8765
```

No Windows, use `py -3 -m search.ingest` se `python` não estiver no PATH, e
rode sempre a partir da raiz do repositório (`GP-PME framework/`), pois os
módulos usam `python -m search.<modulo>` (import relativo ao pacote).

## Uso — CLI

```bash
python -m search.query "como implantar o kanban" --k 3
```

Saída (formato humano):

```
[1] score=0.9143  GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md § O Quadro Kanban e o Limite WIP
    O quadro Kanban visualiza o fluxo de trabalho em colunas — A Fazer, Em
    Andamento, Concluído — e o Limite de WIP (Work In Progress) trava quantas

[2] score=0.7820  GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md § Ciclo Micro-Adaptativo
    O ciclo micro-adaptativo revisa prioridades a cada iteração curta,
    permitindo que a PME reaja a mudanças de mercado sem reescrever o plano.

[3] score=0.6104  GP-PME antigravity/Templates/Template_Kanban_Semanal.md § Como usar este template
    Preencha uma raia por responsável e mantenha o limite de WIP visível no
    topo do quadro para toda a equipe.
```

Outras opções:

```bash
python -m search.query "modelo de matriz de risco" --modo bm25      # força léxico
python -m search.query "priorização de backlog" --modo semantico    # só embeddings
python -m search.query "governança de TI" --k 5 --json              # saída JSON
```

Saída `--json` (lista de chunks do corpus + `score`):

```json
[
  {
    "id": "antigravity/guides/pilar2#03",
    "doc": "GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md",
    "titulo_doc": "Guia Pilar 2 — Execução Ágil",
    "secao": "O Quadro Kanban e o Limite WIP",
    "breadcrumb": "Pilar 2 > Ciclo Micro-Adaptativo > Kanban",
    "texto": "O quadro Kanban visualiza o fluxo de trabalho em colunas...",
    "keywords": ["kanban", "wip", "raia rápida"],
    "pilar": "2",
    "tipo": "guia",
    "score": 0.9143
  }
]
```

Se `search/data/` ainda não existir:

```
Erro: Nenhum índice encontrado em search/data/. Execute 'python -m search.ingest'
e depois 'python -m search.build_index' primeiro.
```

## Uso — API

```bash
uvicorn search.api:app --port 8765
```

```bash
curl "http://127.0.0.1:8765/search?q=como+implantar+o+kanban&k=3"
```

```json
{
  "query": "como implantar o kanban",
  "modo_efetivo": "hibrido",
  "resultados": [
    { "id": "antigravity/guides/pilar2#03", "...": "...", "score": 0.9143 }
  ]
}
```

```bash
curl "http://127.0.0.1:8765/health"
```

```json
{ "status": "ok", "chunks": 842, "modelo": "paraphrase-multilingual-MiniLM-L12-v2" }
```

Documentação interativa automática do FastAPI em
`http://127.0.0.1:8765/docs`.

## Para clientes: integrando a busca GP-PME no seu ambiente

Três formas de consumir a busca, da mais simples à mais integrada:

1. **CLI local** — qualquer script/pipeline interno pode chamar
   `python -m search.query "<pergunta>" --json` e consumir a saída
   estruturada. Sem servidor, sem rede.
2. **API REST** — suba `uvicorn search.api:app --port 8765` (ou atrás de um
   `reverse proxy`/container) e consulte `GET /search?q=...` de qualquer
   linguagem/ferramenta que fale HTTP. Use `GET /health` para checagem de
   liveness em orquestradores (Kubernetes, systemd, etc.).
3. **Busca embutida no portal (sem backend)** — o portal estático
   (`GP-Pme Article/busca.html`) já embute um índice lexical (MiniSearch,
   código inline, sem CDN) gerado por `search/export_web.py` a partir do
   mesmo corpus. É a opção recomendada para distribuir o framework a
   clientes que só têm acesso ao HTML estático, sem precisar rodar Python.

Para produção recomenda-se: gerar os índices uma vez em CI
(`ingest` → `build_index` → `export_web`), versionar `search/data/*.json*`
(o `.npz` de embeddings pode ficar fora do controle de versão se ultrapassar
50MB) e servir a API atrás de autenticação/rate-limit próprios do ambiente do
cliente — este pacote não implementa autenticação.

## Troubleshooting (Windows)

- **`ModuleNotFoundError: No module named 'search'`** — rode sempre com
  `python -m search.query ...` a partir da raiz do repositório
  (`GP-PME framework\`), nunca `python search\query.py ...` diretamente nem
  de dentro da pasta `search\`.
- **Caminho com espaço** — o repositório vive em `C:\Users\...\GP-PME
  framework\`; em scripts `.bat`/PowerShell sempre entre aspas:
  `cd "C:\Users\adm\Desktop\GP-PME framework"`.
- **Aviso "modo 'hibrido' indisponível... usando 'bm25'"** — normal se
  `sentence-transformers` não foi instalado ou `build_index.py` não gerou
  `embeddings.npz`. Instale com `pip install -r search/requirements.txt` e
  rode `build_index.py` novamente para reativar a busca semântica.
- **Erro de encoding/acentuação no console** — o PowerShell padrão do
  Windows pode não exibir UTF-8 corretamente; rode
  `chcp 65001` antes, ou redirecione a saída `--json` para um arquivo
  (`> saida.json`) e abra em um editor UTF-8.
- **`uvicorn` não encontrado** — está na seção opcional `api` de
  `requirements.txt`; confirme que o ambiente virtual correto está ativo
  (`.venv\Scripts\Activate.ps1`).
