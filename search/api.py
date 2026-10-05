"""API REST do motor de busca GP-PME.

Reusa ``buscar()`` de :mod:`search.query` — nenhuma lógica de ranking duplicada aqui.

Rodar:
    uvicorn search.api:app --port 8765

Instalação (dependências opcionais "api"):
    pip install -r search/requirements.txt
"""
from __future__ import annotations

import json
from typing import Any

try:
    from fastapi import FastAPI, HTTPException, Query
except ImportError as exc:  # pragma: no cover - depende de ambiente
    raise SystemExit(
        "Erro: FastAPI não instalado. Rode: pip install -r search/requirements.txt "
        "(seção 'api')."
    ) from exc

from search._common import carregar_corpus
from search.query import INDEX_META_PATH, buscar, resolver_modo, semantica_disponivel

app = FastAPI(
    title="GEAR: busca no conteúdo vigente",
    description="Corpus canônico com consulta lexical e caminho semântico opcional; informa modo efetivo.",
    version="2026.10",
)


def _modelo_atual() -> str | None:
    """Nome do modelo de embeddings em uso, ou ``None`` se ainda não indexado."""
    if not semantica_disponivel():
        return None
    try:
        with INDEX_META_PATH.open("r", encoding="utf-8") as arq:
            return json.load(arq).get("model")
    except (json.JSONDecodeError, OSError):
        return None


@app.get("/search")
def search(
    q: str = Query(..., min_length=1, description="Texto da consulta"),
    k: int = Query(5, ge=1, le=50, description="Número de resultados"),
    modo: str = Query(
        "hibrido",
        pattern="^(hibrido|semantico|bm25)$",
        description="hibrido | semantico | bm25",
    ),
) -> dict[str, Any]:
    """``GET /search`` — SCHEMA §5. Retorna a lista de chunks mais relevantes para `q`."""
    modo_efetivo = resolver_modo(modo)
    try:
        resultados = buscar(q, k=k, modo=modo)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    return {"query": q, "modo_efetivo": modo_efetivo, "resultados": resultados}


@app.get("/health")
def health() -> dict[str, Any]:
    """``GET /health`` — SCHEMA §5. Status do serviço e tamanho do corpus indexado."""
    try:
        n_chunks = len(carregar_corpus())
    except FileNotFoundError:
        n_chunks = 0
    return {"status": "ok", "chunks": n_chunks, "modelo": _modelo_atual()}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("search.api:app", host="127.0.0.1", port=8765, reload=False)
