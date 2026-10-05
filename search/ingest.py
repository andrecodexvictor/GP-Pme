"""Ingestão do corpus GP-PME: varre os .md do framework e gera `data/corpus.jsonl`.

Uso:
    python -m search.ingest

Ver `search/SCHEMA.md` §1 para o contrato completo do formato de saída.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path
from typing import Any

from search._common import DIR_DADOS, RAIZ_REPO

# Pastas varridas em busca de .md (relativas à raiz do repo), com um "codigo"
# curto usado no `id` do chunk (ver `_slugificar_caminho`).
PASTAS_FONTE: dict[str, str] = {
    "framework": "gear",
}

# Nomes de pasta (em qualquer nível) que nunca devem ser varridos.
PASTAS_EXCLUIDAS = {
    "References",
    "SKill folder",
    "agents",
    "search",
    "server",
    "graphify-out",
    ".claude",
    ".context",
}

PALAVRAS_ALVO_MIN = 300
PALAVRAS_ALVO_MAX = 500

RE_HEADING = re.compile(r"^(#{1,3})\s+(.*?)\s*$")


def _caminho_excluido(caminho: Path) -> bool:
    return any(parte in PASTAS_EXCLUIDAS for parte in caminho.parts)


def _listar_markdown() -> list[tuple[Path, str]]:
    """Retorna [(caminho_absoluto, codigo_pasta_fonte)] para todo .md a ingerir."""
    arquivos: list[tuple[Path, str]] = []

    for pasta, codigo in PASTAS_FONTE.items():
        base = RAIZ_REPO / pasta
        if not base.is_dir():
            continue
        for md in sorted(base.rglob("*.md")):
            if _caminho_excluido(md.relative_to(RAIZ_REPO)):
                continue
            arquivos.append((md, codigo))

    readme = RAIZ_REPO / "README.md"
    if readme.is_file():
        arquivos.append((readme, "readme"))

    return arquivos


def _remover_acentos(texto: str) -> str:
    normalizado = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in normalizado if not unicodedata.combining(c))


def _slug(texto: str) -> str:
    """Slugifica um segmento de nome (lowercase, sem acento, `-` como separador)."""
    limpo = _remover_acentos(texto.lower())
    limpo = re.sub(r"[^a-z0-9]+", "-", limpo).strip("-")
    return limpo or "x"


def _slugificar_caminho(caminho_rel: Path, codigo_pasta: str) -> str:
    """Gera o prefixo de `id` (sem sufixo sequencial) a partir do caminho relativo."""
    partes = list(caminho_rel.parts[1:]) if codigo_pasta != "readme" else ["readme"]
    partes_slug = [_slug(Path(p).stem) if p.endswith(".md") else _slug(p) for p in partes]
    if not partes_slug:
        partes_slug = [_slug(caminho_rel.stem)]
    return "/".join([codigo_pasta, *partes_slug]) if codigo_pasta != "readme" else "readme"


# ---------------------------------------------------------------------------
# Classificação de tipo / pilar (heurística por caminho+título — não é ciência
# exata; o objetivo é filtragem útil na busca, não uma taxonomia perfeita).
# ---------------------------------------------------------------------------

def _classificar_tipo(caminho_rel: Path) -> str:
    partes = [p.lower() for p in caminho_rel.parts]
    nome = caminho_rel.name.lower()

    if "framework" in partes:
        if "guias" in partes:
            return "guia"
        if "templates" in partes:
            return "template"
        if "adocao" in partes:
            return "tutorial"
        if "fundamentos" in partes or "exemplos" in partes:
            return "explicacao"
        return "referencia"

    if nome == "index.md":
        return "index"
    if "docs" in partes:
        return "docs"
    if "simulacao" in partes:
        return "simulacao"
    if "comercial" in partes:
        return "comercial"
    if "dummies" in partes or "guide-for-dummies" in partes:
        return "dummies"
    if "templates" in partes:
        return "template"
    if nome.startswith("capitulo_"):
        return "capitulo"
    if "guides" in partes:
        return "guia"
    if "documento_mestre" in nome or "documento mestre" in nome:
        return "master"
    return "outro"


# (padrão, pilar) — primeiro padrão que casar (após remover acentos, lowercase) vence.
_REGRAS_PILAR = [
    (re.compile(r"pilar[\s_-]*1\b"), "1"),
    (re.compile(r"pilar[\s_-]*2\b"), "2"),
    (re.compile(r"pilar[\s_-]*3\b"), "3"),
    (re.compile(r"pilar[\s_-]*4\b"), "4"),
    (re.compile(r"governan[c]a|adm-?lite|estrategic"), "1"),
    (re.compile(r"execu[c]ao[\s_-]*agil|kanban|scrum"), "2"),
    (re.compile(r"seguranca"), "3"),
    (re.compile(r"assistencia[\s_-]*ia|motor[\s_-]*de[\s_-]*ia|agentes[\s_-]*(de[\s_-]*)?ia|orquestrador"), "4"),
]


def _classificar_pilar(caminho_rel: Path, titulo_doc: str) -> str:
    alvo = _remover_acentos(f"{caminho_rel} {titulo_doc}".lower())
    for padrao, pilar in _REGRAS_PILAR:
        if padrao.search(alvo):
            return pilar
    return ""


# ---------------------------------------------------------------------------
# Parse do bloco <rag-metadata> de INDEX.md (parse tolerante via regex; não é
# XML estrito — o bloco mistura texto livre e não vale a pena puxar um parser
# XML completo para isso).
# ---------------------------------------------------------------------------

RE_DOCUMENTO = re.compile(
    r'<document\s+file="([^"]+)">(.*?)</document>', re.DOTALL
)
RE_KEYWORDS = re.compile(r"<keywords>([^<]*)</keywords>", re.DOTALL)


def _carregar_keywords_por_basename() -> dict[str, list[str]]:
    """Lê `GP-PME antigravity/INDEX.md` e mapeia basename(file) -> keywords.

    Tolerante: se o arquivo ou o bloco não existir, retorna {} (todo chunk
    recebe keywords=[] — comportamento previsto pelo SCHEMA §1).
    """
    index_md = RAIZ_REPO / "GP-PME antigravity" / "INDEX.md"
    if not index_md.is_file():
        return {}

    conteudo = index_md.read_text(encoding="utf-8")
    mapa: dict[str, list[str]] = {}
    for file_attr, corpo in RE_DOCUMENTO.findall(conteudo):
        basename = Path(file_attr.rstrip("/")).name
        if not basename:
            continue
        m = RE_KEYWORDS.search(corpo)
        if not m:
            continue
        kws = [k.strip() for k in m.group(1).split(",") if k.strip()]
        if kws:
            mapa[basename] = kws
    return mapa


# ---------------------------------------------------------------------------
# Chunking por H2/H3
# ---------------------------------------------------------------------------

class _Secao:
    def __init__(self, titulo: str, breadcrumb: str, anchor: str = "") -> None:
        self.titulo = titulo
        self.breadcrumb = breadcrumb
        self.paragrafos: list[str] = []
        self.anchor = anchor or _slug(titulo)


def _dividir_em_secoes(linhas: list[str], titulo_doc: str) -> list[_Secao]:
    """Divide as linhas do documento (sem a linha de H1) em seções por H2/H3."""
    secoes: list[_Secao] = []
    atual = _Secao(titulo_doc, titulo_doc)
    h2_corrente = ""
    paragrafo_buf: list[str] = []
    heading_counts = {_slug(titulo_doc): 1}
    in_code = False

    def fechar_paragrafo() -> None:
        if paragrafo_buf:
            atual.paragrafos.append("\n".join(paragrafo_buf).strip())
            paragrafo_buf.clear()

    for linha in linhas:
        if linha.startswith("```"):
            in_code = not in_code
            paragrafo_buf.append(linha)
            continue
        if in_code:
            paragrafo_buf.append(linha)
            continue
        m = RE_HEADING.match(linha)
        if m and len(m.group(1)) in (2, 3):
            fechar_paragrafo()
            if atual.paragrafos:
                secoes.append(atual)
            texto_heading = m.group(2).strip()
            if len(m.group(1)) == 2:
                h2_corrente = texto_heading
                breadcrumb = f"{titulo_doc} > {texto_heading}"
            else:
                breadcrumb = (
                    f"{titulo_doc} > {h2_corrente} > {texto_heading}"
                    if h2_corrente
                    else f"{titulo_doc} > {texto_heading}"
                )
            base = _slug(texto_heading)
            n = heading_counts.get(base, 0)
            heading_counts[base] = n + 1
            atual = _Secao(texto_heading, breadcrumb, base + (f"-{n}" if n else ""))
            continue
        if m and len(m.group(1)) == 1:
            # H1 dentro do corpo (raro) — ignora a linha, não quebra seção.
            continue
        if linha.strip() == "":
            fechar_paragrafo()
        else:
            paragrafo_buf.append(linha)

    fechar_paragrafo()
    if atual.paragrafos:
        secoes.append(atual)
    return secoes


def _dividir_por_palavras(paragrafos: list[str]) -> list[list[str]]:
    """Agrupa parágrafos em blocos de ~300-500 palavras, sem quebrar parágrafos."""
    blocos: list[list[str]] = []
    bloco: list[str] = []
    palavras_bloco = 0

    for p in paragrafos:
        n = len(p.split())
        if bloco and palavras_bloco >= PALAVRAS_ALVO_MIN and palavras_bloco + n > PALAVRAS_ALVO_MAX:
            blocos.append(bloco)
            bloco = [p]
            palavras_bloco = n
        else:
            bloco.append(p)
            palavras_bloco += n

    if bloco:
        blocos.append(bloco)
    return blocos


def _extrair_titulo_doc(linhas: list[str], caminho: Path) -> tuple[str, list[str]]:
    """Extrai o H1 (se houver) como titulo_doc; retorna (titulo, linhas_restantes)."""
    for i, linha in enumerate(linhas):
        if linha.strip() == "":
            continue
        m = RE_HEADING.match(linha)
        if m and len(m.group(1)) == 1:
            return m.group(2).strip(), linhas[:i] + linhas[i + 1 :]
        break
    # Sem H1 explícito: usa o nome do arquivo "bonito".
    titulo = caminho.stem.replace("_", " ").replace("-", " ").strip()
    return titulo, linhas


def _processar_documento(
    caminho: Path, codigo_pasta: str, keywords_por_basename: dict[str, list[str]]
) -> list[dict[str, Any]]:
    caminho_rel = caminho.relative_to(RAIZ_REPO)
    texto_bruto = caminho.read_text(encoding="utf-8")
    linhas = texto_bruto.splitlines()

    titulo_doc, linhas_corpo = _extrair_titulo_doc(linhas, caminho)
    secoes = _dividir_em_secoes(linhas_corpo, titulo_doc)

    tipo = _classificar_tipo(caminho_rel)
    pilar = _classificar_pilar(caminho_rel, titulo_doc)
    keywords = keywords_por_basename.get(caminho.name, [])
    prefixo_id = _slugificar_caminho(caminho_rel, codigo_pasta)
    doc_rel_str = str(caminho_rel).replace("\\", "/")

    chunks: list[dict[str, Any]] = []
    seq = 1
    for secao in secoes:
        for i, bloco in enumerate(_dividir_por_palavras(secao.paragrafos)):
            texto = "\n\n".join(bloco).strip()
            if not texto:
                continue
            nome_secao = secao.titulo if i == 0 else f"{secao.titulo} (cont.)"
            chunks.append(
                {
                    "id": f"{prefixo_id}#{seq:02d}",
                    "doc": doc_rel_str,
                    "titulo_doc": titulo_doc,
                    "secao": nome_secao,
                    "breadcrumb": secao.breadcrumb,
                    "texto": texto,
                    "keywords": keywords,
                    "pilar": pilar,
                    "tipo": tipo,
                    "anchor": secao.anchor,
                }
            )
            seq += 1
    return chunks


def gerar_corpus() -> list[dict[str, Any]]:
    keywords_por_basename = _carregar_keywords_por_basename()
    chunks: list[dict[str, Any]] = []
    for caminho, codigo_pasta in _listar_markdown():
        chunks.extend(_processar_documento(caminho, codigo_pasta, keywords_por_basename))
    return chunks


def main() -> int:
    chunks = gerar_corpus()

    DIR_DADOS.mkdir(parents=True, exist_ok=True)
    saida = DIR_DADOS / "corpus.jsonl"
    with saida.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False))
            f.write("\n")

    n_docs = len({c["doc"] for c in chunks})
    print(f"OK: {len(chunks)} chunks de {n_docs} documentos gravados em {saida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
