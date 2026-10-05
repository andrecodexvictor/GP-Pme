# GEAR — contratos de busca

Este contrato descreve os arquivos e interfaces vigentes. Nomes e campos históricos permanecem quando necessários à compatibilidade. A fonte editorial é `framework/`; regras de geração estão em `ingest.py`, `build_index.py` e `export_web.py`.

## 1. Corpus

`data/corpus.jsonl` contém um objeto JSON por linha, em UTF-8:

```json
{
  "id": "identificador-estavel-do-trecho",
  "doc": "framework/caminho.md",
  "titulo_doc": "Título do documento",
  "secao": "Título da seção",
  "breadcrumb": "Percurso de leitura",
  "texto": "Conteúdo da seção ou sua parte",
  "keywords": [],
  "pilar": "",
  "tipo": "guia",
  "anchor": "titulo-da-secao"
}
```

O exemplo descreve o formato, sem afirmar existência de documento ou score. `id` usa caminho slugificado e índice sequencial. Títulos H1/H2/H3 determinam seções; títulos dentro de blocos de código são ignorados. Alvo de chunking: 300–500 palavras, preservando parágrafos e âncora nas continuações.

Entradas: todos os Markdown em `framework/` e README raiz. Versões antigas, fontes externas, agentes, dados do usuário e `.context/` ficam fora. Metadados históricos de RAG não tornam um documento fonte vigente.

Os tipos canônicos classificam guias, templates, referências, explicações e tutoriais. `pilar` é campo legado, conservado para consumidores; não acrescenta um quarto domínio ao GEAR. `anchor` deve corresponder ao renderizador HTML, inclusive para títulos repetidos.

## 2. Embeddings opcionais

`data/embeddings.npz` contém `ids` Unicode na ordem do corpus e `vectors` float32, dimensão N × dim e normalização L2. Carga usa `allow_pickle=False`.

`index_meta.json` registra `model`, `dim`, `n_chunks`, `created` e `corpus_sha256`. A disponibilidade semântica exige hash correspondente ao corpus atual e dependências. O modelo configurado é `paraphrase-multilingual-MiniLM-L12-v2`. Sem o caminho disponível, a consulta recorre a BM25 e informa o modo efetivo.

## 3. BM25

`data/bm25.json` contém `df`, `doc_len`, `avgdl`, `postings` e `n_docs`. Cada posting liga termo, id e frequência. Tokenização em minúsculas, sem acentos, com separação por caracteres não alfanuméricos e stopwords locais.

Parâmetros: k1 = 1,5 e b = 0,75. A consulta híbrida combina 0,6 × similaridade normalizada e 0,4 × BM25 normalizado. São decisões da implementação; score não é probabilidade de correção.

## 4. CLI e APIs

```text
python -m search.query "termo" --k 5 --modo bm25 --json
```

Modos aceitos: `hibrido`, `semantico`, `bm25`. Saída humana apresenta ranking, score, documento, seção e contexto. JSON é lista de objetos do corpus acrescidos de score.

API de busca: `GET /search?q=&k=&modo=` → consulta, modo efetivo e resultados; `GET /health` → estado, quantidade e modelo disponível. API do núcleo: `GET /buscar`, com contrato próprio em [server](../server/README.md). Índice ausente produz erro e orientação, sem resultado inventado.

## 5. Exportação web

`search-index.json` possui `gerado_em`, `modo: lexical`, `edicao` e `docs`. Cada documento conserva campos do corpus, com texto truncado a 800 caracteres, além de `href` para página documental e âncora.

`search-data.js` expõe `window.GEAR_INDEX` e alias `window.GPPME_INDEX`. A página usa script local, sem fetch necessário para o arquivo de índice. A busca do portal tem ranking lexical próprio: título/seção, corpo e keywords recebem pesos 5, 1 e 2. O primeiro resultado não implica verificação da afirmação. Não chamar esse ranking de BM25 ou semântico.

## 6. Reconstrução e compatibilidade

Executar pela raiz e declarar UTF-8 em leitura/escrita. Sequência: ingestão, índice, exportação. `--bm25-only` evita geração ou download de embeddings. Regerar ao editar fontes. Não usar vetores históricos com corpus diferente.

Testes verificam títulos em código, âncoras repetidas, corpus permitido e recuperação lexical. Verificação no navegador cobre resultado, contexto e navegação à seção. [Uso e limites](README.md).

