"""Exporta search/data/corpus.jsonl para os artefatos web de busca.

Gera, dentro de "GP-Pme Article/":
  - search-index.json  (formato do SCHEMA.md secao 6, texto truncado em 800 chars)
  - search-data.js      (mesmo payload, exposto como `window.GPPME_INDEX`,
                          para a pagina de busca funcionar offline via file://)

Uso:
    python -m search.export_web
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS_PATH = ROOT / "search" / "data" / "corpus.jsonl"
OUT_DIR = ROOT / "GP-Pme Article"
OUT_JSON = OUT_DIR / "search-index.json"
OUT_JS = OUT_DIR / "search-data.js"

TEXTO_MAX_CHARS = 800

CAMPOS = ("id", "doc", "titulo_doc", "secao", "breadcrumb", "texto", "keywords", "pilar", "tipo", "anchor")


def _carregar_corpus(path: Path) -> list[dict]:
    chunks: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for numero_linha, linha in enumerate(f, start=1):
            linha = linha.strip()
            if not linha:
                continue
            try:
                chunks.append(json.loads(linha))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Linha {numero_linha} de {path} nao e JSON valido: {exc}") from exc
    return chunks


def _projetar(chunk: dict) -> dict:
    """Aplica o contrato do SCHEMA.md secao 6: mesmos campos do corpus, texto truncado."""
    texto = chunk.get("texto") or ""
    if len(texto) > TEXTO_MAX_CHARS:
        texto = texto[:TEXTO_MAX_CHARS]
    projetado = {campo: chunk.get(campo) for campo in CAMPOS}
    projetado["texto"] = texto
    projetado["keywords"] = chunk.get("keywords") or []
    from urllib.parse import quote
    doc = Path(chunk["doc"])
    if doc.parts[0] == "framework":
        page = Path("docs", *doc.parts[1:]).with_suffix(".html")
    else:
        page = Path("docs/README.html")
    projetado["href"] = quote(page.as_posix(), safe="/") + "#" + (chunk.get("anchor") or "gear")
    return projetado


def exportar() -> Path:
    if not CORPUS_PATH.exists():
        print(
            f"ERRO: corpus nao encontrado em '{CORPUS_PATH}'.\n"
            "Gere-o primeiro (ex.: 'python -m search.ingest') antes de exportar para a web.",
            file=sys.stderr,
        )
        raise SystemExit(1)

    chunks = _carregar_corpus(CORPUS_PATH)
    payload = {
        "gerado_em": datetime.now(timezone.utc).isoformat(),
        "modo": "lexical",
        "edicao": "GEAR 2026.10",
        "docs": [_projetar(c) for c in chunks],
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    with OUT_JS.open("w", encoding="utf-8") as f:
        f.write("// Gerado automaticamente por search/export_web.py -- NAO editar manualmente.\n")
        f.write("window.GEAR_INDEX = ")
        json.dump(payload, f, ensure_ascii=False)
        f.write(";\nwindow.GPPME_INDEX = window.GEAR_INDEX; // Alias de compatibilidade.\n")

    print(f"OK: {len(chunks)} chunks exportados para:\n  {OUT_JSON}\n  {OUT_JS}")
    return OUT_JSON


if __name__ == "__main__":
    exportar()
