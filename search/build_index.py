"""Indexação do corpus GP-PME: gera `data/bm25.json` (sempre) e
`data/embeddings.npz` + `data/index_meta.json` (se `sentence-transformers`
estiver instalado).

Uso:
    python -m search.build_index

Ver `search/SCHEMA.md` §2 e §3 para o contrato completo dos artefatos gerados.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from datetime import datetime, timezone
from typing import Any

from search._common import DIR_DADOS, carregar_corpus, tokenizar

MODELO_EMBEDDINGS = "paraphrase-multilingual-MiniLM-L12-v2"

BM25_PATH = DIR_DADOS / "bm25.json"
EMBEDDINGS_PATH = DIR_DADOS / "embeddings.npz"
INDEX_META_PATH = DIR_DADOS / "index_meta.json"


def construir_bm25(chunks: list[dict[str, Any]]) -> dict[str, Any]:
    """Monta o índice BM25 (SCHEMA §3) a partir dos chunks do corpus."""
    df: Counter[str] = Counter()
    doc_len: dict[str, int] = {}
    postings: dict[str, dict[str, int]] = {}

    for chunk in chunks:
        doc_id = chunk["id"]
        tokens = tokenizar(chunk.get("texto", ""))
        doc_len[doc_id] = len(tokens)
        tf = Counter(tokens)
        for termo, freq in tf.items():
            postings.setdefault(termo, {})[doc_id] = freq
        df.update(tf.keys())

    n_docs = len(chunks)
    avgdl = (sum(doc_len.values()) / n_docs) if n_docs else 0.0

    return {
        "df": dict(df),
        "doc_len": doc_len,
        "avgdl": avgdl,
        "postings": postings,
        "n_docs": n_docs,
    }


def construir_embeddings(chunks: list[dict[str, Any]]) -> bool:
    """Gera `embeddings.npz` + `index_meta.json` (SCHEMA §2). Retorna True se gerou."""
    try:
        import numpy as np
        from sentence_transformers import SentenceTransformer
    except ImportError:
        print(
            "Aviso: pacote 'sentence-transformers' não instalado — pulando geração de "
            "embeddings semânticos. Instale com 'pip install -r search/requirements.txt' "
            "para habilitar busca semântica/híbrida.",
            file=sys.stderr,
        )
        return False

    ids = [c["id"] for c in chunks]
    textos = [c.get("texto", "") for c in chunks]

    modelo = SentenceTransformer(MODELO_EMBEDDINGS)
    vetores = modelo.encode(
        textos,
        batch_size=32,
        show_progress_bar=True,
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype("float32")

    np.savez(
        EMBEDDINGS_PATH,
        # dtype unicode (não object): permite np.load com allow_pickle=False
        ids=np.array(ids, dtype="U"),
        vectors=vetores,
    )

    meta = {
        "model": MODELO_EMBEDDINGS,
        "dim": int(vetores.shape[1]) if vetores.size else 0,
        "n_chunks": len(ids),
        "created": datetime.now(timezone.utc).isoformat(),
    }
    with INDEX_META_PATH.open("w", encoding="utf-8") as arq:
        json.dump(meta, arq, ensure_ascii=False, indent=2)

    return True


def main() -> int:
    chunks = carregar_corpus()
    if not chunks:
        print(
            "Erro: search/data/corpus.jsonl vazio ou ausente. "
            "Rode 'python -m search.ingest' primeiro.",
            file=sys.stderr,
        )
        return 1

    DIR_DADOS.mkdir(parents=True, exist_ok=True)

    bm25 = construir_bm25(chunks)
    with BM25_PATH.open("w", encoding="utf-8") as arq:
        json.dump(bm25, arq, ensure_ascii=False)
    print(f"OK: bm25.json gravado ({bm25['n_docs']} docs, {len(bm25['postings'])} termos).")

    if construir_embeddings(chunks):
        print(f"OK: embeddings.npz + index_meta.json gravados ({len(chunks)} chunks).")
    else:
        print("OK: build_index concluído somente com BM25 (sem embeddings semânticos).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
