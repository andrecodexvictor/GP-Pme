"""Gera portal, documentação e blog a partir das fontes canônicas."""
from __future__ import annotations
import hashlib
import html
import json
import os
from pathlib import Path
from urllib.parse import quote
from tools.editorial import ROOT, PORTAL, render
from tools.portal_tools import tools_html
from tools.portal_migrations import migration_html

def rel(page, dest):return quote(os.path.relpath(dest,page.parent).replace('\\','/'),safe='/')
def link(page,path,label):return f'<a href="{rel(page,PORTAL/path)}">{html.escape(label)}</a>'

def shell(page,title,content,section='',extra=''):
    css=rel(page,PORTAL/'assets/gear.css'); js=rel(page,PORTAL/'assets/gear.js')
    nav=''.join(link(page,p,label) for p,label in [('docs/README.html','Documentação'),('biblioteca.html','Biblioteca'),('blog/index.html','Blog'),('busca.html','Buscar')])
    for label in ('Documentação','Biblioteca','Blog','Buscar'):
        if label==section:nav=nav.replace('>'+label+'</a>',' aria-current="page">'+label+'</a>')
    return f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · GEAR</title><meta name="description" content="Framework de governança e gestão de TI para pequenas e médias empresas."><link rel="stylesheet" href="{css}"><script defer src="{js}"></script>{extra}</head>
<body><a class="skip" href="#conteudo">Ir para o conteúdo</a><header class="site-header"><div class="header-inner">{link(page,'index.html','GEAR')}<nav class="desktop-nav" aria-label="Navegação principal">{nav}</nav><details class="mobile-nav"><summary>Menu</summary><nav aria-label="Navegação móvel">{nav}</nav></details></div></header>
<main id="conteudo">{content}</main><footer><div class="footer-inner"><p>GEAR · Gestão, Execução, Agilidade e Risco<br>Andre Victor · Edição editorial 2026.10</p><p>{link(page,'docs/referencias/fontes.html','Fontes e limites')} · {link(page,'docs/fundamentos/origens-adaptacoes.html','Evolução do método')}<br><a href="{rel(page,ROOT/'LICENSE.md')}">Direitos e licença</a></p></div></footer></body></html>'''

def write(page,title,content,section='',extra=''):
    page.parent.mkdir(parents=True,exist_ok=True);page.write_text(shell(page,title,content,section,extra),encoding='utf-8')

def main():
    docs=sorted((ROOT/'framework').rglob('*.md')); items=[];manifest=[]
    for source in docs:
        relative=source.relative_to(ROOT/'framework');page=PORTAL/'docs'/relative.with_suffix('.html')
        text=source.read_text(encoding='utf-8');body,headings=render(text,source,page)
        if relative.parts[0]=='templates' and relative.name!='README.md':
            body+='<details class="template-source"><summary>Versão Markdown para copiar</summary><pre><code>'+html.escape(text)+'</code></pre></details>'
        title=next((v for k,v,a in headings if k=='h1'),source.stem)
        items.append((relative,title,page));manifest.append({'source':source.relative_to(ROOT).as_posix(),'page':page.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'anchors':[a for k,v,a in headings]})
        side='<nav class="doc-nav" aria-label="Percurso documental"><p class="nav-label">Percursos</p>'+''.join(link(page,p,label) for p,label in [('docs/adocao/primeiros-30-dias.html','Começar'),('docs/guias/README.html','Executar'),('biblioteca.html','Consultar'),('docs/fundamentos/origens-adaptacoes.html','Compreender')])+'</nav>'
        toc='<aside class="toc"><nav aria-label="Nesta página"><p class="nav-label">Nesta página</p>'+''.join(f'<a href="#{a}">{html.escape(v)}</a>' for k,v,a in headings if k in ('h2','h3'))+'</nav></aside>'
        meta=f'<p class="meta">{link(page,"index.html","GEAR")} / Documentação · Edição editorial 2026.10</p>'
        write(page,title,'<div class="doc-layout">'+side+'<article class="prose">'+meta+body+'</article>'+toc+'</div>','Documentação')
    home=PORTAL/'index.html'
    write(PORTAL/'ferramentas.html','Ferramentas de aplicação',tools_html(),extra='<script defer src="assets/tools.js"></script>')
    hero='''<section class="hero"><div><p class="edition">Edição de leitura 2026.10</p><h1>Decisões claras.<br>Trabalho visível.</h1><p class="lead">Governança e gestão de TI para pequenas e médias empresas. Um método para decidir prioridades, executar serviços e acompanhar riscos com responsáveis e evidências.</p>'''+link(home,'docs/adocao/primeiros-30-dias.html','Começar pelos primeiros 30 dias')+'''</div><div class="method-map" role="img" aria-label="Ciclo: decidir, executar, verificar e revisar. Segurança e continuidade acompanham todas as etapas."><p>O ciclo de trabalho</p><ol><li><span>01</span>Decidir <small>Prioridade e responsabilidade</small></li><li><span>02</span>Executar <small>Capacidade e critério de aceite</small></li><li><span>03</span>Verificar <small>Resultado e evidência</small></li><li><span>04</span>Revisar <small>Risco e próxima decisão</small></li></ol><p>Segurança e continuidade em cada etapa</p></div></section>'''
    domain='<section class="section"><div class="section-heading"><h2>Três domínios, uma rotina</h2><p>Adoção, indicadores e maturidade atravessam o método. Assistência por IA é opcional.</p></div><div class="domain-list">'
    for i,p,t,desc in [(1,'governanca','Governança e direção','Definir alçadas, negociar prioridades e registrar decisões.'),(2,'execucao-servicos','Execução e serviços','Organizar demandas, acompanhar bloqueios e verificar entregas.'),(3,'seguranca-continuidade','Segurança e continuidade','Conhecer dependências, tratar exposição e testar recuperação.')]:
        domain+=f'<div class="domain"><span class="number">0{i}</span><h3>{link(home,"docs/nucleo/"+p+".html",t)}</h3><p>{desc}</p></div>'
    domain+='</div></section>'
    library='<section class="section"><h2>O que precisa fazer agora?</h2><div class="reading-list">'+''.join('<div><h3>'+link(home,p,t)+'</h3><p>'+d+'</p></div>' for p,t,d in [('docs/guias/priorizar-demandas.html','Organizar a fila','Prioridade, limite de trabalho e tratamento de urgências.'),('docs/guias/testar-restauracao.html','Verificar a recuperação','Preparar um teste e registrar o que ele comprova.'),('docs/indicadores/financeiros.html','Conferir um investimento','Premissas, unidades, retorno líquido e capacidade potencial.'),('biblioteca.html','Consultar os modelos','Registros para usar quando a tarefa exigir.')])+'</div></section>'
    evidence='<section class="evidence"><h2>Uma proposta que pode ser examinada</h2><p>O acervo evoluiu de GP-PME e NEXUS-PME. Guias, exemplos e software tornam o método inspecionável; sua efetividade organizacional ainda exige avaliação. Cenários ilustrativos não são resultados de campo.</p>'+link(home,'artigo.html','Conhecer o manuscrito e o protocolo')+'</section>'
    # Equivalências para fragmentos antigos usados por leitores.
    migrations='<nav class="migration" aria-label="Equivalências de leitura anteriores">'+''.join(f'<a id="{id}" href="{target}">{label}</a>' for id,target,label in [('workspace','docs/README.html','Visão do método'),('visao','docs/nucleo/escopo-principios.html','Visão geral'),('tecnico','docs/guias/README.html','Guias técnicos'),('dummies','docs/adocao/primeiros-30-dias.html','Adoção inicial'),('simuladores','docs/indicadores/financeiros.html','Indicadores'),('templates','biblioteca.html','Modelos')])+'</nav>'
    tools_entry='<section class="section"><h2>Conferir antes de decidir</h2><p>Calculadoras locais de retorno, capacidade potencial e dívida, com um quadro de exercício para compreender o limite de trabalho iniciado.</p>'+link(home,'ferramentas.html','Abrir ferramentas de aplicação')+'</section>'
    migrations=migration_html()
    write(home,'Governança e gestão de TI',hero+domain+library+tools_entry+evidence+migrations)
    librarypage=PORTAL/'biblioteca.html'
    listing='<section class="page-intro"><h1>Biblioteca</h1><p class="lead">Modelos e referências para consultar durante o trabalho. Escolha pelo problema que precisa resolver.</p></section><div class="library-list">'
    for relative,title,page in items:
        if relative.parts[0] in ('templates','indicadores','glossario.md','referencias'):
            if relative.name=='README.md':continue
            listing+=f'<div><h2><a href="{rel(librarypage,page)}">{html.escape(title)}</a></h2><p>{html.escape(relative.parts[0].replace(".md",""))} · Fonte canônica revisada</p></div>'
    write(librarypage,'Biblioteca',listing+'</div><p>'+link(librarypage,'ferramentas.html','Ferramentas locais: cálculos e quadro de exercício')+'</p>','Biblioteca')
    posts=[('restauracao','Continuidade','Testar uma cópia e recuperar um serviço','guias/testar-restauracao.md'),('retorno','Decisões','Como ler uma estimativa de retorno','indicadores/financeiros.md'),('maturidade','Adoção','Maturidade depende de evidências','adocao/maturidade.md')]
    blog=PORTAL/'blog/index.html'
    intro='<section class="page-intro"><h1>Notas de aplicação</h1><p class="lead">Leituras do método sobre continuidade, decisões e adoção. Cada nota remete ao guia e às fontes que a sustentam.</p></section><nav class="topic-nav" aria-label="Temas">'+''.join(f'<a href="#{slug}">{topic}</a>' for slug,topic,title,src in posts)+'</nav><div class="blog-list">'
    for slug,topic,title,src in posts:
        post=PORTAL/'blog'/f'{slug}.html';source=ROOT/'framework'/src
        body,hs=render(source.read_text(encoding='utf-8'),source,post)
        body=body.replace('<h1','<h2',1).replace('</h1>','</h2>',1)
        contents=f'<article class="prose blog-article"><p class="meta">{link(post,"blog/index.html","Notas de aplicação")} / {topic}</p><h1>{title}</h1><p class="byline">Andre Victor · Edição editorial 2026.10</p><p>Esta nota apresenta o conteúdo do guia canônico, sem acrescentar resultados de campo.</p>'+body+f'<p class="source-note">Fonte desta edição: <a href="{rel(post,PORTAL/"docs"/Path(src).with_suffix(".html"))}">guia e referências</a>.</p></article>'
        write(post,title,contents,'Blog')
        intro+=f'<article id="{slug}"><p class="meta">{topic} · Edição 2026.10</p><h2>{link(blog,"blog/"+slug+".html",title)}</h2><p>Uma leitura de aplicação com definições, exemplos e limites.</p></article>'
    write(blog,'Notas de aplicação',intro+'</div>','Blog')
    search=PORTAL/'busca.html'
    searchbody='''<section class="page-intro"><h1>Buscar no método</h1><p class="lead">Localize uma definição, prática ou modelo. A busca lexical usa palavras e seus contextos no conteúdo revisado.</p></section><section class="search-panel"><form id="search-form" role="search"><label for="query">O que você precisa consultar?</label><div class="search-controls"><input type="search" id="query" name="q" placeholder="Ex.: restauração, WIP, ROI" autocomplete="off"><button type="submit">Buscar</button></div><label for="kind">Tipo de leitura</label><select id="kind"><option value="">Todas</option><option value="guia">Guias</option><option value="template">Modelos</option><option value="referencia">Referências</option><option value="explicacao">Explicações</option><option value="tutorial">Adoção</option></select></form><p id="search-status" role="status" aria-live="polite">Digite uma palavra para começar.</p><ol id="search-results" class="search-results"></ol><noscript>A busca precisa de JavaScript. Use a documentação e a biblioteca para navegar pelo conteúdo.</noscript></section>'''
    extra='<script defer src="search-data.js"></script><script defer src="assets/search.js"></script>'
    write(search,'Busca',searchbody,'Buscar',extra)
    article=PORTAL/'artigo.html'
    write(article,'Manuscrito científico','<section class="page-intro"><h1>Pesquisa, produção e avaliação do GEAR</h1><p class="lead">Manuscrito científico de André Victor Andrade Oliveira Santos sobre a construção do framework com pesquisa assistida por IA e auditoria de conteúdo.</p></section><article class="prose"><h2>O que esta versão apresenta</h2><p>O artigo descreve a seleção de fontes, a síntese assistida, as adaptações autorais e a auditoria de afirmações, versões e cálculos. Documentos e registros permitem examinar o desenho e suas correções. MCPs, skills e integrações são apenas citados.</p><h2>Prova de conceito futura</h2><p>A prova de conceito no <a href="https://github.com/andrecodexvictor/Frame-sim">FrameSim</a> prevê 25 empresas sintéticas e 75 execuções pareadas. Nenhuma rodada foi executada nesta versão; as tabelas permanecem sem resultados. A produção com IA e os testes de software não demonstram efetividade organizacional.</p><h2>Consultar as fontes</h2><p>'+link(article,'overleaf/README.md','Fontes LaTeX, figuras e protocolo')+' · <a href="https://github.com/andrecodexvictor/GP-Pme/tree/codex/gear-editorial">Repositório e branch editorial</a></p><h2>Publicações da edição</h2><p><a href="output/pdf/GEAR_artigo_2026-10.pdf">Ler o artigo em PDF</a> · <a href="output/pdf/GEAR_livro_2026-10.pdf">Ler o livro GEAR</a></p><p>Fontes, hashes, verificações e limites estão no <a href="../framework/publicacao/README.md">registro da edição</a>.</p></article>')
    (ROOT/'.context/gear-execution').mkdir(parents=True,exist_ok=True)
    (ROOT/'.context/gear-execution/portal-manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(f'Portal gerado: {len(docs)} páginas documentais, 3 notas e 5 entradas.')

if __name__=='__main__':main()
