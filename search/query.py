"""CLI de consulta do motor de busca GP-PME (busca híbrida semântica + BM25).

Uso:
    python -m search.query "como implantar o kanban" [--k 5] [--modo hibrido|semantico|bm25] [--json]

Modos:
    hibrido   (default) score = 0.6 * cosseno_normalizado + 0.4 * bm25_normalizado
    semantico apenas similaridade de cosseno via embeddings
    bm25      apenas BM25 puro-Python (sem dependências externas)

Se `data/embeddings.npz` / `data/index_meta.json` estiverem ausentes, ou o pacote
`sentence-transformers` não estiver instalado, os modos "hibrido" e "semantico"
degradam automaticamente para "bm25", emitindo um aviso em stderr.

Ver search/SCHEMA.md para o contrato completo dos dados consumidos aqui.
"""
from __future__ import annotations

import argparse
import json
import math
import hashlib
import sys
from pathlib import Path
from typing import Any

from search._common import RAIZ_REPO, carregar_corpus, tokenizar

DATA_DIR: Path = RAIZ_REPO / "search" / "data"
BM25_PATH: Path = DATA_DIR / "bm25.json"
EMBEDDINGS_PATH: Path = DATA_DIR / "embeddings.npz"
INDEX_META_PATH: Path = DATA_DIR / "index_meta.json"

# Parâmetros clássicos do BM25 (Robertson/Sparck-Jones).
K1 = 1.5
B = 0.75

# Pesos da combinação híbrida (SCHEMA §4).
PESO_SEMANTICO = 0.6
PESO_BM25 = 0.4

MSG_SEM_DADOS = (
    "Nenhum índice encontrado em search/data/. "
    "Execute 'python -m search.ingest' e depois 'python -m search.build_index' primeiro."
)


class BM25:
    """Índice BM25 puro-Python carregado de ``data/bm25.json`` (SCHEMA §3)."""

    def __init__(self, dados: dict[str, Any]) -> None:
        self.df: dict[str, int] = dados["df"]
        self.doc_len: dict[str, int] = dados["doc_len"]
        self.avgdl: float = dados["avgdl"] or 1.0
        self.postings: dict[str, dict[str, int]] = dados["postings"]
        self.n_docs: int = dados["n_docs"]

    @classmethod
    def carregar(cls, caminho: Path) -> "BM25 | None":
        """Carrega o índice de ``caminho``; retorna ``None`` se o arquivo não existir."""
        if not caminho.exists():
            return None
        with caminho.open("r", encoding="utf-8") as arq:
            return cls(json.load(arq))

    def _idf(self, termo: str) -> float:
        n_qtd = self.df.get(termo, 0)
        return math.log((self.n_docs - n_qtd + 0.5) / (n_qtd + 0.5) + 1.0)

    def pontuar(self, termos_query: list[str]) -> dict[str, float]:
        """Retorna ``{doc_id: score_bm25}`` para todo documento com ao menos um termo em comum."""
        scores: dict[str, float] = {}
        for termo in termos_query:
            postings = self.postings.get(termo)
            if not postings:
                continue
            idf = self._idf(termo)
            for doc_id, tf in postings.items():
                dl = self.doc_len.get(doc_id, self.avgdl)
                denom = tf + K1 * (1 - B + B * dl / self.avgdl)
                scores[doc_id] = scores.get(doc_id, 0.0) + idf * (tf * (K1 + 1)) / denom
        return scores


def semantica_disponivel() -> bool:
    """``True`` se há embeddings gerados e o pacote sentence-transformers está instalado."""
    if not (EMBEDDINGS_PATH.exists() and INDEX_META_PATH.exists()):
        return False
    try:
        meta = json.loads(INDEX_META_PATH.read_text(encoding="utf-8"))
        digest = hashlib.sha256((DATA_DIR / "corpus.jsonl").read_bytes()).hexdigest()
        if meta.get("corpus_sha256") != digest:
            return False  # Não combinar um corpus novo com vetores históricos.
    except (OSError, ValueError):
        return False
    try:
        import sentence_transformers  # noqa: F401
    except ImportError:
        return False
    return True


def resolver_modo(modo: str) -> str:
    """Resolve `modo` para o modo efetivamente utilizável, avisando em stderr se degradar."""
    if modo in ("hibrido", "semantico") and not semantica_disponivel():
        print(
            f"Aviso: modo '{modo}' indisponível (embeddings.npz/index_meta.json ausentes "
            "ou pacote sentence-transformers não instalado) — usando 'bm25'.",
            file=sys.stderr,
        )
        return "bm25"
    return modo


def _normalizar_minmax(scores: dict[str, float]) -> dict[str, float]:
    """Normaliza scores para [0, 1] via min-max. Vazio ou tudo igual -> mapeamento trivial."""
    if not scores:
        return {}
    valores = scores.values()
    minimo, maximo = min(valores), max(valores)
    if maximo - minimo < 1e-12:
        return dict.fromkeys(scores, 1.0)
    return {k: (v - minimo) / (maximo - minimo) for k, v in scores.items()}


def _top50_bm25(query_tokens: list[str]) -> dict[str, float]:
    bm25 = BM25.carregar(BM25_PATH)
    if bm25 is None:
        raise RuntimeError(MSG_SEM_DADOS)
    scores = bm25.pontuar(query_tokens)
    top = dict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:50])
    return _normalizar_minmax(top)


def _top50_semantico(q: str) -> dict[str, float]:
    import numpy as np
    from sentence_transformers import SentenceTransformer

    with INDEX_META_PATH.open("r", encoding="utf-8") as arq:
        meta = json.load(arq)
    npz = np.load(EMBEDDINGS_PATH, allow_pickle=False)
    ids = npz["ids"]
    vetores = npz["vectors"]

    modelo = SentenceTransformer(meta["model"])
    q_vec = modelo.encode([q], normalize_embeddings=True)[0]
    sims = vetores @ q_vec  # vetores já L2-normalizados -> produto interno = cosseno
    top_idx = np.argsort(-sims)[:50]
    top = {str(ids[i]): float(sims[i]) for i in top_idx}
    return _normalizar_minmax(top)


def buscar(q: str, k: int = 5, modo: str = "hibrido") -> list[dict[str, Any]]:
    """Busca os `k` chunks mais relevantes do corpus GP-PME para a pergunta `q`.

    Args:
        q: texto da pergunta/consulta.
        k: número de resultados a retornar.
        modo: "hibrido" (default), "semantico" ou "bm25". Degrada automaticamente
            para "bm25" quando embeddings/sentence-transformers não estão disponíveis.

    Returns:
        Lista de até `k` dicts (chunk do corpus + campo "score"), ordenados por
        relevância decrescente.

    Raises:
        RuntimeError: se o corpus ou os índices não foram gerados ainda.
    """
    try:
        corpus = carregar_corpus()
    except FileNotFoundError as exc:
        raise RuntimeError(MSG_SEM_DADOS) from exc
    if not corpus:
        raise RuntimeError(MSG_SEM_DADOS)
    por_id = {c["id"]: c for c in corpus}

    modo_ef = resolver_modo(modo)

    bm25_norm: dict[str, float] = {}
    if modo_ef in ("bm25", "hibrido"):
        bm25_norm = _top50_bm25(tokenizar(q))

    cos_norm: dict[str, float] = {}
    if modo_ef in ("semantico", "hibrido"):
        cos_norm = _top50_semantico(q)

    if modo_ef == "bm25":
        finais = bm25_norm
    elif modo_ef == "semantico":
        finais = cos_norm
    else:  # hibrido
        ids_uniao = set(bm25_norm) | set(cos_norm)
        finais = {
            doc_id: PESO_SEMANTICO * cos_norm.get(doc_id, 0.0)
            + PESO_BM25 * bm25_norm.get(doc_id, 0.0)
            for doc_id in ids_uniao
        }

    ranking = sorted(finais.items(), key=lambda kv: kv[1], reverse=True)[:k]

    resultados: list[dict[str, Any]] = []
    for doc_id, score in ranking:
        chunk = por_id.get(doc_id)
        if chunk is None:
            continue
        item = dict(chunk)
        item["score"] = round(float(score), 4)
        resultados.append(item)
    return resultados


def _formatar_humano(resultados: list[dict[str, Any]]) -> str:
    if not resultados:
        return "Nenhum resultado encontrado."
    blocos = []
    for i, r in enumerate(resultados, start=1):
        texto = str(r.get("texto", "")).strip()
        primeiras_linhas = "\n    ".join(texto.splitlines()[:2])
        blocos.append(
            f"[{i}] score={r.get('score', 0):.4f}  "
            f"{r.get('doc', '?')} § {r.get('secao', '?')}\n"
            f"    {primeiras_linhas}"
        )
    return "\n\n".join(blocos)


def main(argv: list[str] | None = None) -> int:
    """Ponto de entrada da CLI. Retorna código de saída (0 = sucesso)."""
    # Console Windows usa cp1252 por padrão e não imprime emojis/acentos do corpus.
    for _stream in (sys.stdout, sys.stderr):
        if hasattr(_stream, "reconfigure"):
            _stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(
        prog="python -m search.query",
        description="Busca híbrida (semântica + BM25) no corpus GP-PME.",
    )
    parser.add_argument("pergunta", help="Texto da pergunta/consulta")
    parser.add_argument("--k", type=int, default=5, help="Número de resultados (default: 5)")
    parser.add_argument(
        "--modo",
        choices=["hibrido", "semantico", "bm25"],
        default="hibrido",
        help="Modo de busca (default: hibrido)",
    )
    parser.add_argument("--json", action="store_true", help="Saída em JSON")
    args = parser.parse_args(argv)

    try:
        resultados = buscar(args.pergunta, k=args.k, modo=args.modo)
    except RuntimeError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(resultados, ensure_ascii=False, indent=2))
    else:
        print(_formatar_humano(resultados))
    return 0


if __name__ == "__main__":
    sys.exit(main())
