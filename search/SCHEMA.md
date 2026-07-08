# Busca Semântica GP-PME — Contratos de Dados e Interfaces

> Este arquivo é o CONTRATO entre os módulos do motor de busca. Qualquer módulo
> (`ingest.py`, `build_index.py`, `query.py`, `api.py`, `export_web.py`, `busca.html`)
> DEVE respeitar exatamente estes formatos.

## Layout do pacote

```
search/
├── __init__.py            # pacote python "search"
├── SCHEMA.md              # este arquivo
├── ingest.py              # corpus MD -> data/corpus.jsonl
├── build_index.py         # corpus.jsonl -> data/embeddings.npz + data/bm25.json
├── query.py               # CLI de consulta (híbrido semântico + BM25)
├── api.py                 # FastAPI: GET /search
├── export_web.py          # corpus.jsonl -> ../GP-Pme Article/search-index.json
├── requirements.txt
├── README.md              # PT-BR, inclui seção "para clientes"
└── data/                  # artefatos gerados (commitáveis, exceto embeddings se >50MB)
    ├── corpus.jsonl
    ├── embeddings.npz
    └── bm25.json
```

## 1. `data/corpus.jsonl` — 1 chunk por linha (UTF-8)

```json
{
  "id": "antigravity/guides/pilar2#03",
  "doc": "GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md",
  "titulo_doc": "Guia Pilar 2 — Execução Ágil",
  "secao": "O Quadro Kanban e o Limite WIP",
  "breadcrumb": "Pilar 2 > Ciclo Micro-Adaptativo > Kanban",
  "texto": "<texto integral do chunk, sem markdown de heading>",
  "keywords": ["kanban", "wip", "raia rápida"],
  "pilar": "2",
  "tipo": "guia"
}
```

Regras de chunking:
- Divisão por heading H2/H3; alvo 300–500 "palavras" por chunk; seções maiores são divididas mantendo parágrafos íntegros e repetindo `secao`+sufixo `(cont.)`.
- `id` = caminho curto slugificado + índice sequencial de 2 dígitos.
- `keywords` vêm do bloco `<rag-metadata>` de `GP-PME antigravity/INDEX.md` quando o
  documento estiver mapeado lá; senão, lista vazia.
- `tipo` ∈ {`guia`, `template`, `master`, `dummies`, `capitulo`, `index`, `simulacao`, `comercial`, `docs`, `outro`}.
- `pilar` ∈ {"1","2","3","4",""} (vazio quando transversal).
- Corpus de entrada: todos os `.md` sob `GP-PME antigravity/`, `GP-PME/`, `Docs/`,
  `Simulacao/`, `Comercial/`, mais `README.md` raiz. EXCLUIR `References/`,
  `SKill folder/`, `agents/`, `search/`, `graphify-out/`, `.claude/`, `.context/`.

## 2. `data/embeddings.npz` (numpy)

- `ids`: array de strings (mesma ordem das linhas do corpus)
- `vectors`: float32 shape (N, dim), L2-normalizados
- Modelo: `paraphrase-multilingual-MiniLM-L12-v2` (sentence-transformers). O nome do
  modelo usado é gravado em `data/index_meta.json` (`{"model": ..., "dim": ..., "n_chunks": ..., "created": ...}`).

## 3. `data/bm25.json`

Índice BM25 puro-Python (sem dependências além de stdlib): `{"df": {termo: doc_freq}, "doc_len": {id: n_tokens}, "avgdl": float, "postings": {termo: {id: tf}}, "n_docs": int}`.
Tokenização: lowercase, remoção de acentos (unicodedata), split em `\W+`, stopwords PT-BR mínimas embutidas no código.

## 4. CLI (`query.py`)

```
python -m search.query "como implantar o kanban" [--k 5] [--modo hibrido|semantico|bm25] [--json]
```
- `hibrido` (default): score = 0.6*cos + 0.4*bm25_normalizado. Se embeddings.npz ou
  sentence-transformers indisponíveis → degrada para `bm25` com aviso em stderr.
- Saída humana: rank, score, `doc` § `secao`, 2 primeiras linhas do texto.
- Saída `--json`: lista de objetos do corpus + campo `score`.

## 5. API (`api.py`)

- `GET /search?q=<str>&k=<int=5>&modo=<hibrido>` → `{"query": ..., "modo_efetivo": ..., "resultados": [chunk+score]}`
- `GET /health` → `{"status":"ok","chunks":N,"modelo":...}`
- Rodar: `uvicorn search.api:app --port 8765`.

## 6. `GP-Pme Article/search-index.json` (web)

```json
{
  "gerado_em": "ISO-8601",
  "docs": [{"id","doc","titulo_doc","secao","breadcrumb","texto","keywords","pilar","tipo"}]
}
```
- Igual ao corpus, mas `texto` truncado em 800 chars (busca lexical no browser).
- `busca.html` embute MiniSearch (código inline, SEM CDN) e carrega este JSON via
  fetch relativo; campos indexados: `texto`, `secao`, `titulo_doc`, `keywords`;
  boost: keywords 3, secao 2. Visual: mesma paleta do portal (`index.html` usa
  Google Stitch dark/blue) — mas NUNCA modificar `index.html`.

## 7. Convenções gerais

- Python ≥3.10, Windows-safe (paths via `pathlib`, encoding="utf-8" explícito em TODO open()).
- Nenhum módulo importa outro além de: `query.py`/`api.py` podem importar utilitários
  comuns de `search/_common.py` (tokenização, carga de índices) — quem precisar cria/estende
  `_common.py` de forma aditiva.
- Raiz do repo detectada como `Path(__file__).resolve().parents[1]`.
