"""Parser Markdown limitado ao contrato editorial GEAR, sem rede ou HTML arbitrário."""
from __future__ import annotations
import html
import re
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PORTAL = ROOT / 'GP-Pme Article'

def slug(text: str) -> str:
    s = unicodedata.normalize('NFKD', re.sub(r'[`*_]', '', text).lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-') or 'secao'

def blocks(text: str):
    """Produz (tipo, conteúdo); preserva cercas antes de interpretar headings."""
    lines=text.splitlines(); i=0
    while i < len(lines):
        line=lines[i]
        if not line.strip(): i+=1; continue
        if line.startswith('```'):
            code=[]; i+=1
            while i<len(lines) and not lines[i].startswith('```'):code.append(lines[i]); i+=1
            i+=1; yield 'code','\n'.join(code); continue
        picture=re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)',line.strip())
        if picture:
            yield 'image',(picture[1],picture[2]);i+=1;continue
        m=re.match(r'^(#{1,6})\s+(.+)$',line)
        if m:yield 'h'+str(len(m[1])),m[2]; i+=1; continue
        if i+1<len(lines) and line.startswith('|') and re.match(r'^\|[ :|\-]+\|$',lines[i+1]):
            rows=[[c.strip() for c in line.strip('|').split('|')]]; i+=2
            while i<len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip('|').split('|')]); i+=1
            yield 'table',rows;continue
        if re.match(r'^\s*(?:[-*]|\d+\.)\s+',line):
            ordered=bool(re.match(r'^\d+\.',line)); items=[]
            while i<len(lines) and re.match(r'^\s*(?:[-*]|\d+\.)\s+',lines[i]):
                items.append(re.sub(r'^\s*(?:[-*]|\d+\.)\s+','',lines[i])); i+=1
            yield 'ol' if ordered else 'ul',items;continue
        if line.strip() in ('---','***'):yield 'hr','';i+=1;continue
        paras=[line];i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(?:#|\||```|[-*] |\d+\. )',lines[i]):
            paras.append(lines[i]);i+=1
        yield 'p',' '.join(p.strip() for p in paras)

def href_for(source: Path, target: str, page: Path) -> str:
    target=target.strip('<>'); parsed=urlsplit(target)
    if parsed.scheme:return target if parsed.scheme in ('https','http','mailto') else '#'
    if target.startswith('#'):return target
    dest=(source.parent/unquote(parsed.path)).resolve()
    if dest.is_relative_to(ROOT/'framework') and dest.suffix=='.md':
        relative=dest.relative_to(ROOT/'framework').with_suffix('.html')
        dest=PORTAL/'docs'/relative
    import os
    return quote(os.path.relpath(dest,page.parent).replace('\\','/'),safe='/')+ ('#'+parsed.fragment if parsed.fragment else '')

def inline(text: str, source: Path, page: Path) -> str:
    tokens=[]
    def hold(value):tokens.append(value);return f'\x00{len(tokens)-1}\x00'
    text=re.sub(r'`([^`]+)`',lambda m:hold('<code>'+html.escape(m[1])+'</code>'),text)
    text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:hold('<a href="'+html.escape(href_for(source,m[2],page),quote=True)+'">'+html.escape(m[1])+'</a>'),text)
    text=html.escape(text)
    text=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',text)
    text=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<em>\1</em>',text)
    return re.sub(r'\x00(\d+)\x00',lambda m:tokens[int(m[1])],text)

def render(text: str, source: Path, page: Path):
    body=[];headings=[];counts={}
    for kind,value in blocks(text):
        if kind.startswith('h'):
            base=slug(value); n=counts.get(base,0);counts[base]=n+1;anchor=base+(f'-{n}' if n else '')
            headings.append((kind,value,anchor));body.append(f'<{kind} id="{anchor}">{inline(value,source,page)}</{kind}>')
        elif kind=='image':
            alt,target=value
            body.append('<figure class="diagram"><div class="diagram-scroll" tabindex="0" role="region" aria-label="Fluxograma com rolagem horizontal"><img src="'+html.escape(href_for(source,target,page),quote=True)+'" alt="'+html.escape(alt,quote=True)+'"></div><figcaption>'+html.escape(alt)+'</figcaption></figure>')
        elif kind=='p':body.append('<p>'+inline(value,source,page)+'</p>')
        elif kind in ('ul','ol'):body.append(f'<{kind}>'+''.join('<li>'+inline(v,source,page)+'</li>' for v in value)+f'</{kind}>')
        elif kind=='table':
            rows=['<thead><tr>'+''.join('<th scope="col">'+inline(v,source,page)+'</th>' for v in value[0])+'</tr></thead>']
            rows+=['<tbody>'+''.join('<tr>'+''.join('<td>'+inline(v,source,page)+'</td>' for v in row)+'</tr>' for row in value[1:])+'</tbody>']
            body.append('<div class="table-wrap" tabindex="0" role="region" aria-label="Tabela: '+html.escape(headings[-1][1] if headings else 'consulta')+'"><table style="--columns:'+str(len(value[0]))+'">'+''.join(rows)+'</table></div>')
        elif kind=='code':body.append('<pre><code>'+html.escape(value)+'</code></pre>')
        else:body.append('<hr>')
    return '\n'.join(body),headings
