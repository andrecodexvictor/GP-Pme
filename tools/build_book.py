"""Livro GEAR com fontes locais, marcadores e sumário a partir do manifesto."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
    PageBreak, Spacer, Table, TableStyle, KeepTogether, Preformatted, CondPageBreak)
from reportlab.platypus.tableofcontents import TableOfContents
from tools.editorial import ROOT, PORTAL, blocks, render, slug
from tools.book_design import PETROL, PAPER, PARTS, ChapterHeading, RecordBlock, cover

INK=colors.HexColor('#202321');COPPER=colors.HexColor('#8a421e');MUTED=colors.HexColor('#555d59');LINE=colors.HexColor('#d6dcd7');SOFT=colors.HexColor('#f3f5f2')

def fonts():
    base=PORTAL/'assets/fonts'
    for name,folder,file in [('Public','public-sans','PublicSans-Regular'),('PublicBold','public-sans','PublicSans-Bold'),('PublicItalic','public-sans','PublicSans-Italic'),('Serif','source-serif-4','SourceSerif4-Regular'),('SerifBold','source-serif-4','SourceSerif4-Bold'),('SerifItalic','source-serif-4','SourceSerif4-It')]:
        pdfmetrics.registerFont(TTFont(name,str(base/folder/(file+'.ttf'))))
    pdfmetrics.registerFontFamily('Serif',normal='Serif',bold='SerifBold',italic='SerifItalic',boldItalic='SerifBold')
    pdfmetrics.registerFontFamily('Public',normal='Public',bold='PublicBold',italic='PublicItalic',boldItalic='PublicBold')

def styles():
    return {
        'body':ParagraphStyle('Body',fontName='Serif',fontSize=10.8,leading=15.8,textColor=INK,spaceAfter=8,allowWidows=0,allowOrphans=0),
        'small':ParagraphStyle('Small',fontName='Public',fontSize=8.4,leading=12,textColor=MUTED,spaceAfter=6),
        'h1':ParagraphStyle('H1',fontName='PublicBold',fontSize=25,leading=30,textColor=PETROL,spaceAfter=18,keepWithNext=True),
        'h2':ParagraphStyle('H2',fontName='PublicBold',fontSize=14,leading=18,textColor=PETROL,spaceBefore=14,spaceAfter=8,keepWithNext=True),
        'h3':ParagraphStyle('H3',fontName='PublicBold',fontSize=11,leading=15,textColor=INK,spaceBefore=10,spaceAfter=6,keepWithNext=True),
        'cell':ParagraphStyle('Cell',fontName='Public',fontSize=8,leading=11,textColor=INK,spaceAfter=0),
        'cellhead':ParagraphStyle('CellHead',fontName='PublicBold',fontSize=8,leading=11,textColor=colors.white,spaceAfter=0),
        'cover':ParagraphStyle('Cover',fontName='PublicBold',fontSize=62,leading=70,textColor=INK,spaceAfter=22),
        'subtitle':ParagraphStyle('Subtitle',fontName='Serif',fontSize=22,leading=29,textColor=INK,spaceAfter=24),
    }

def key(source,anchor):return slug(source.relative_to(ROOT/'framework').as_posix())+'--'+anchor

def inline(text,source,known):
    tokens=[]
    def hold(v):tokens.append(v);return f'\x00{len(tokens)-1}\x00'
    text=re.sub(r'`([^`]+)`',lambda m:hold('<font name="Public">'+html.escape(m[1])+'</font>'),text)
    def link(m):
        target=m[2].strip('<>');p=urlsplit(target)
        if p.scheme in ('https','http','mailto'):dest=target
        elif not p.scheme:
            file=(source.parent/unquote(p.path)).resolve() if p.path else source
            if file in known:dest='#'+key(file,p.fragment or known[file])
            else:return html.escape(m[1])
        else:return html.escape(m[1])
        return hold('<link href="'+html.escape(dest,quote=True)+'" color="#8a421e">'+html.escape(m[1])+'</link>')
    text=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,text)
    text=html.escape(text).replace('—','-').replace('–','-')
    text=re.sub(r'\*\*([^*]+)\*\*',r'<b>\1</b>',text)
    text=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',text)
    return re.sub(r'\x00(\d+)\x00',lambda m:tokens[int(m[1])],text)

class Book(BaseDocTemplate):
    def __init__(self,path,date):
        super().__init__(str(path),pagesize=A4,leftMargin=52,rightMargin=52,topMargin=52,bottomMargin=48,title='GEAR: governança e gestão de TI para PMEs',author='Andre Victor',lang='pt-BR',pageCompression=1)
        self.addPageTemplates(PageTemplate(id='reading',frames=[Frame(52,48,A4[0]-104,A4[1]-100,id='normal')],onPage=self.page_style))
        self.edition_date=date
    def page_style(self,canvas,doc):
        if doc.page==1:
            cover(canvas,A4,self.edition_date);return
        canvas.saveState();canvas.setStrokeColor(LINE);canvas.line(52,42,A4[0]-52,42)
        canvas.setFont('PublicBold',8);canvas.setFillColor(PETROL);canvas.drawString(52,28,'GEAR');canvas.setFont('Public',8);canvas.setFillColor(MUTED);canvas.drawString(84,28,'Edição editorial 2026.10');canvas.drawRightString(A4[0]-52,28,str(doc.page));canvas.restoreState()
    def afterFlowable(self,flow):
        if hasattr(flow,'bookmark'):
            self.canv.bookmarkPage(flow.bookmark)
            self.canv.addOutlineEntry(flow.getPlainText(),flow.bookmark,level=flow.outline_level,closed=False)
            if flow.outline_level==0:self.notify('TOCEntry',(0,flow.getPlainText(),self.page,flow.bookmark))

def build(output):
    fonts();ss=styles();manifest=json.loads((ROOT/'framework/publicacoes.json').read_text(encoding='utf-8'))
    sources=[ROOT/'framework'/v for v in manifest['capitulos']]
    known={s:next(v for k,v in blocks(s.read_text(encoding='utf-8')) if k=='h1') for s in sources}
    known={s:slug(t) for s,t in known.items()}
    story=[Spacer(1,1),PageBreak()]
    story+=[Paragraph('Como ler esta edição',ss['h1']),Paragraph('O livro reúne o núcleo, o percurso de adoção, guias de tarefas, indicadores, exemplos e modelos. A documentação modular é a fonte editorial; o manuscrito científico tem protocolo e estrutura próprios.',ss['body']),Paragraph('Comece por escopo e princípios. Para aplicar, use os primeiros 30 dias e selecione um guia conforme o problema. Modelos servem ao registro; fundamentos e fontes explicam as adaptações e seus limites.',ss['body']),Paragraph('GEAR evolui do acervo GP-PME e NEXUS-PME. Práticas e instrumentos locais não constituem certificação. Exemplos são ilustrativos e não comprovam efetividade organizacional. IA é assistência opcional, inclusive no nível máximo de maturidade.',ss['body']),Paragraph('Direitos e distribuição',ss['h2']),Paragraph('© 2026 Andre Victor. Todos os direitos reservados. O acesso destina-se à avaliação pessoal conforme LICENSE.md do repositório. Reprodução, distribuição, obras derivadas e uso comercial dependem de autorização escrita ou licença válida nos termos daquele documento. Esta edição não altera suas permissões.',ss['small']),Paragraph('As fontes tipográficas Public Sans e Source Serif 4 conservam suas licenças SIL OFL 1.1. Documentos externos são citados, sem atribuir seus direitos ao autor do método.',ss['small']),Paragraph('Situação da publicação',ss['h2']),Paragraph('Edição consolidada do acervo autoral. O registro de publicação documenta revisão, preservação, verificações e limites. A aplicação organizacional continua sujeita a avaliação própria. A autoria, os créditos e a declaração de uso de IA do manuscrito científico permanecem próprios daquele documento.',ss['small']),PageBreak()]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='Public',fontSize=9,leading=12,leftIndent=0,firstLineIndent=0,spaceBefore=1,spaceAfter=0,textColor=INK)]
    story += [Paragraph('Sumário',ss['h1']),toc,PageBreak()]
    master=[];chapter_manifest=[];htmlchapters=[]
    for index,source in enumerate(sources,1):
        text=source.read_text(encoding='utf-8');master.append(text)
        chapter_manifest.append({'ordem':index,'source':source.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
        part=PARTS.get(source.relative_to(ROOT/'framework').parts[0],PARTS['referencias'])
        body,hs=render(text,source,ROOT/'book/livro_framework.html');htmlchapters.append('<section class="chapter"><p class="book-part">'+html.escape(part)+f' · Capítulo {index:02d}</p>'+body+'</section>')
        if index>1:story.append(PageBreak())
        chapter_start=len(story)
        counts={}
        for kind,value in blocks(text):
            if kind.startswith('h'):
                # Divisões editoriais equilibram capítulos de duas páginas.
                # Não comprimir o corpo ou deixar uma seção final isolada.
                if kind=='h2' and (source.name,value) in {
                    ('escopo-principios.md','Núcleo, aplicação e explicação'),
                    ('tratar-incidentes.md','Verificar recuperação'),
                    ('caso-didatico.md','Hipótese financeira'),
                    ('tasklist.md','Encerrar e revisar'),
                    ('risco-continuidade.md','Análise qualitativa e assistência opcional'),
                    ('assistencia.md','Decidir com os resultados'),
                    ('evolucao-indicadores.md','Benefício, custo e decisão'),
                }:story.append(PageBreak())
                if source.name=='fluxos-de-trabalho.md' and kind=='h2':story.append(CondPageBreak(520))
                base=slug(value);n=counts.get(base,0);counts[base]=n+1;anchor=base+(f'-{n}' if n else '')
                label=(f'{index:02d}. ' if kind=='h1' else '')+inline(value,source,known)
                if kind=='h1':p=ChapterHeading(index,inline(value,source,known),part,key(source,anchor))
                else:
                    p=Paragraph(label,ss[kind if kind in ss else 'h3']);p.bookmark=key(source,anchor);p.outline_level=1
                # H3 não cria um nível que exija H2 prévio no outline.
                story.append(p)
            elif kind=='p':
                navigation=value.startswith(('Modelo:', 'Modelos:', 'Consultar:', 'Anterior:', 'Fundamento:', 'Fundamentos:'))
                story.append(Paragraph(inline(value,source,known),ss['small' if navigation else 'body']))
            elif kind in ('ul','ol'):
                for i,v in enumerate(value,1):story.append(Paragraph(inline(v,source,known),ss['body'],bulletText=f'{i}.' if kind=='ol' else '•'))
            elif kind=='table':
                cells=[[Paragraph(inline(v,source,known),ss['cellhead' if i==0 else 'cell']) for v in row] for i,row in enumerate(value)]
                ncols=max(len(r) for r in cells)
                widths=[(A4[0]-104)/ncols]*ncols
                table=Table(cells,colWidths=widths,repeatRows=1,hAlign='LEFT')
                padding={'glossario.md':4,'assistencia.md':3,'responsabilidades.md':2.5,'README.md':5,'inventario-dependencias.md':4}.get(source.name,7)
                table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PETROL),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,SOFT]),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.4,LINE),('TOPPADDING',(0,0),(-1,-1),padding),('BOTTOMPADDING',(0,0),(-1,-1),padding),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7)]))
                story+=[table,Spacer(1,10)]
            elif kind=='code':
                group=[RecordBlock(value,ss['small'])]
                if isinstance(story[-1],Paragraph) and story[-1].style.name in ('H2','H3'):
                    group.insert(0,story.pop())
                story.append(KeepTogether(group))
            elif kind=='image':
                alt,target=value
                name=Path(target.strip('<>')).stem
                from tools.build_flowcharts import drawing,FLOWS
                if name not in FLOWS:raise ValueError('Figura sem renderizador vetorial: '+target)
                figure=drawing(name);factor=min((A4[0]-104)/figure.width,435/figure.height)
                figure.scale(factor,factor);figure.width*=factor;figure.height*=factor
                figure.hAlign='CENTER'
                story.append(KeepTogether([figure,Spacer(1,8),Paragraph(html.escape(alt),ss['small'])]))
        if source.name=='fontes.md':
            # Cada ficha Fxx mantém título, identificação, links e limite juntos.
            flows=story[chapter_start:];groups=[];pending=[]
            for flow in flows:
                if isinstance(flow,Paragraph) and flow.style.name=='H2':
                    if pending:groups.append(KeepTogether(pending));pending=[]
                if pending or isinstance(flow,Paragraph) and flow.style.name=='H2':pending.append(flow)
                else:groups.append(flow)
            if pending:groups.append(KeepTogether(pending))
            story[chapter_start:]=groups
    output.parent.mkdir(parents=True,exist_ok=True);doc=Book(output,manifest['data']);doc.multiBuild(story)
    # O mestre é uma saída derivada fora do corpus, com fontes e hashes por capítulo.
    (output.parent/'GEAR_documento_mestre.md').write_text('# GEAR: documento mestre derivado\n\nFonte: framework/publicacoes.json. Direitos: LICENSE.md.\n\n'+'\n\n'.join(master),encoding='utf-8')
    (output.parent/'GEAR_livro_manifesto.json').write_text(json.dumps({'edicao':manifest['edicao'],'capitulos':chapter_manifest,'pdf_sha256':hashlib.sha256(output.read_bytes()).hexdigest()},ensure_ascii=False,indent=2),encoding='utf-8')
    bookhtml='<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>GEAR: livro</title><link rel="stylesheet" href="../GP-Pme%20Article/assets/gear.css"><link rel="stylesheet" href="../GP-Pme%20Article/assets/book.css"></head><body><main class="book"><header class="book-cover"><p>Governança e gestão de TI para PMEs</p><h1>GEAR</h1><p class="book-subtitle">Gestão, Execução, Agilidade e Risco</p><p>Decidir · Executar · Verificar · Revisar</p><p>Andre Victor · Edição 2026.10</p></header>'+'\n'.join(htmlchapters)+'</main></body></html>'
    (ROOT/'book/livro_framework.html').write_text(bookhtml,encoding='utf-8')
    print(f'Livro gerado: {output}; {len(sources)} capítulos.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'.context/publicacoes/GEAR_livro_2026-10.pdf');args=p.parse_args();build(args.output.resolve())

if __name__=='__main__':main()
