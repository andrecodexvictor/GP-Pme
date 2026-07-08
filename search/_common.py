"""Utilitários comuns do motor de busca GP-PME.

Contrato estável (ver `search/SCHEMA.md` §7): outros módulos (`query.py`,
`api.py`) importam exatamente `tokenizar`, `RAIZ_REPO` e `carregar_corpus`
deste arquivo. Não renomeie nem altere as assinaturas abaixo.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

# Raiz do repositório (search/_common.py -> search/ -> raiz).
RAIZ_REPO = Path(__file__).resolve().parents[1]

# Pasta de artefatos gerados por ingest.py / build_index.py.
DIR_DADOS = Path(__file__).resolve().parent / "data"
ARQUIVO_CORPUS = DIR_DADOS / "corpus.jsonl"

# Stopwords PT-BR mínimas: artigos, preposições, pronomes e conectivos comuns.
# Lista deliberadamente curta (~60 termos) — não é um stemmer nem remove
# palavras de conteúdo. ponytail: lista fixa embutida, ampliar aqui se
# resultados de busca vierem poluídos por outras palavras muito frequentes.
STOPWORDS_PT = {
    "a", "as", "o", "os", "de", "do", "da", "dos", "das",
    "em", "no", "na", "nos", "nas", "num", "numa", "nuns", "numas",
    "um", "uma", "uns", "umas", "ao", "aos",
    "por", "para", "pra", "com", "sem", "sob", "sobre", "entre",
    "ate", "desde", "apos", "ante", "perante", "durante",
    "e", "ou", "mas", "que", "se", "nao", "sim",
    "sao", "foi", "ser", "estar", "esta", "estao", "era", "sera",
    "como", "mais", "menos", "muito", "muitos", "pouco", "tambem",
    "ja", "so", "ainda", "quando", "onde", "porque", "pois",
    "este", "esse", "essa", "isso", "isto", "aquele", "aquela",
    "seu", "sua", "seus", "suas", "meu", "minha", "meus", "minhas",
    "nosso", "nossa", "nossos", "nossas", "teu", "tua",
    "eles", "elas", "ele", "ela", "eu", "tu", "voce", "voces", "nos", "lhe", "lhes",
    "qual", "quais", "quem", "cada", "todo", "toda", "todos", "todas",
}


def _remover_acentos(texto: str) -> str:
    """Remove acentos/diacríticos preservando as letras base (NFKD)."""
    normalizado = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in normalizado if not unicodedata.combining(c))


def tokenizar(texto: str) -> list[str]:
    """Tokeniza texto em PT-BR para indexação/consulta BM25.

    Passos: lowercase -> remoção de acentos -> split em `\\W+` -> remoção de
    stopwords mínimas e tokens vazios. Usado tanto por `build_index.py`
    (indexação) quanto por `query.py` (consulta) para garantir consistência.
    """
    texto_normalizado = _remover_acentos(texto.lower())
    tokens_brutos = re.split(r"\W+", texto_normalizado)
    return [tok for tok in tokens_brutos if tok and tok not in STOPWORDS_PT]


def carregar_corpus() -> list[dict]:
    """Carrega `search/data/corpus.jsonl` como lista de dicionários.

    Cada linha do arquivo é um objeto JSON representando um chunk (ver
    `SCHEMA.md` §1). Retorna lista vazia se o arquivo ainda não existir.
    """
    if not ARQUIVO_CORPUS.exists():
        return []

    chunks: list[dict] = []
    with open(ARQUIVO_CORPUS, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                chunks.append(json.loads(linha))
    return chunks
