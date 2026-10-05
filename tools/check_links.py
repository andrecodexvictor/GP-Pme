"""Verifica links e âncoras de fontes canônicas e páginas geradas, sem rede."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote,urlsplit
from tools.editorial import ROOT,PORTAL,blocks,slug

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for attr in ('href','src'):
            if attr in a:self.links.append(a[attr])

def anchors(path):
    if path.suffix=='.html':
        p=Links();p.feed(path.read_text(encoding='utf-8'));return p.ids
    if path.suffix=='.md':
        count={};ids=set()
        for k,v in blocks(path.read_text(encoding='utf-8')):
            if k.startswith('h'):
                base=slug(v);n=count.get(base,0);count[base]=n+1;ids.add(base+(f'-{n}' if n else ''))
        return ids
    return None

def check():
    errors=[];checked=0;paths=[ROOT/'README.md',*(ROOT/'framework').rglob('*.md'),*(ROOT/'Simulacao').glob('*.md'),*(ROOT/'Comercial').glob('*.md'),ROOT/'server/README.md',ROOT/'search/README.md',ROOT/'search/SCHEMA.md',ROOT/'agents/gp-pme-adk/README.md',ROOT/'agents/gp-pme-adk/CONVENTIONS.md',*PORTAL.rglob('*.html')]
    cache={}
    paths += list((ROOT/'References').rglob('*.md'))
    paths += list((ROOT/'Docs').glob('*.md'))
    # Caminhos autorais preservados e revistos.
    paths += list((ROOT/'GP-PME').glob('*.md'))
    paths += [ROOT/'GP-PME antigravity/GP-PME_Documento_Mestre_Consolidado.md']
    paths += list((ROOT/'GP-PME antigravity/GP-Pme complete').glob('Capitulo_*.md'))
    paths += list((ROOT/'GP-PME antigravity/GP-Pme complete/Dummies').glob('*.md'))
    paths += list((ROOT/'GP-PME antigravity/guide-for-dummies').glob('*.md'))
    paths += list((ROOT/'GP-PME antigravity/Guides').glob('*.md'))
    paths += [ROOT/'GP-PME antigravity/Templates_GP-PME.md', ROOT/'GP-PME antigravity/INDEX.md']
    from tools.build_legacy_templates import TEMPLATES
    paths += [ROOT/'GP-PME antigravity/Templates'/name for name, _, _ in TEMPLATES]
    paths += list((ROOT/'GP-PME antigravity/Templates/AI-Skills-and-Agents/Agentes_Prontos').glob('*.md'))
    paths += list((ROOT/'.claude/skills').glob('*/SKILL.md'))
    for source in paths:
        text=source.read_text(encoding='utf-8')
        if source.suffix=='.html':p=Links();p.feed(text);targets=p.links
        else:targets=re.findall(r'\[[^\]]+\]\(([^)]+)\)',text)
        for target in targets:
            target=target.strip('<>');parts=urlsplit(target)
            if parts.scheme in ('https','http','mailto','data'):continue
            if parts.scheme:errors.append((str(source.relative_to(ROOT)),target,'esquema local inadequado'));continue
            dest=(source.parent/unquote(parts.path)).resolve() if parts.path else source
            checked+=1
            if not dest.exists():errors.append((str(source.relative_to(ROOT)),target,'destino ausente'));continue
            if parts.fragment and dest.is_file():
                if dest not in cache:cache[dest]=anchors(dest)
                if cache[dest] is not None and unquote(parts.fragment) not in cache[dest]:errors.append((str(source.relative_to(ROOT)),target,'âncora ausente'))
    report={'links_checked':checked,'errors':errors,'scope':'README, framework, References, Docs, Simulacao, Comercial, três mestres, seis capítulos, dez guias introdutórios, sete guias técnicos, oito templates, biblioteca, índice, nove contratos de agentes e seu README, oito skills existentes revistos; READMEs de serviços/busca/ADK e todas as páginas HTML do portal'}
    path=ROOT/'.context/gear-execution/links.json';path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=True))
    return len(errors)

if __name__=='__main__':raise SystemExit(1 if check() else 0)
