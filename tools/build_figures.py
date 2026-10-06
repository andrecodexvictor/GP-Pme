"""Diagramas vetoriais do artigo, com rótulos extraídos das fontes Mermaid.

Layouts são explícitos por ID, sem dependência de navegador ou pacote remoto.
"""
import hashlib
import json
import re
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from tools.build_book import fonts
from tools.editorial import ROOT

BASE=ROOT/'GP-Pme Article/overleaf/figures'
INK=colors.HexColor('#202321');COPPER=colors.HexColor('#8a421e');SOFT=colors.HexColor('#f7f3ec');LINE=colors.HexColor('#173f43')

def labels(path):
    text=path.read_text(encoding='utf-8')
    return {id:label.replace('R1--R6','R1–R6').replace('5--20','5–20').split('<br/>') for id,label in re.findall(r'(\w+)\["([^"]+)"\]',text)}

def draw_box(c,rect,text,optional=False):
    x,y,w,h=rect;c.setStrokeColor(COPPER if optional else LINE);c.setFillColor(SOFT if optional else colors.white);c.setLineWidth(.7)
    if optional:c.setDash(3,2)
    c.rect(x,y,w,h,stroke=1,fill=1);c.setDash()
    lines=[]
    for line in text:
        words=line.split();current=''
        for word in words:
            candidate=(current+' '+word).strip()
            if pdfmetrics.stringWidth(candidate,'Public',8)>w-16 and current:lines.append(current);current=word
            else:current=candidate
        if current:lines.append(current)
    c.setFillColor(INK);c.setFont('Public',8)
    yy=y+h/2+(len(lines)-1)*5.5
    for line in lines:c.drawCentredString(x+w/2,yy,line);yy-=11

def arrow(c,a,b,dashed=False):
    c.setStrokeColor(COPPER);c.setFillColor(COPPER);c.setLineWidth(.8)
    if dashed:c.setDash(3,2)
    c.line(*a,*b);c.setDash()
    import math
    angle=math.atan2(b[1]-a[1],b[0]-a[0]);size=4
    p=c.beginPath();p.moveTo(*b);p.lineTo(b[0]-size*math.cos(angle-.45),b[1]-size*math.sin(angle-.45));p.lineTo(b[0]-size*math.cos(angle+.45),b[1]-size*math.sin(angle+.45));p.close();c.drawPath(p,stroke=0,fill=1)

def build():
    fonts();out=BASE/'generated';out.mkdir(exist_ok=True);manifest=[]
    for name in ['gppme-architecture','research-pipeline','results-template']:
        source=BASE/'mermaid'/(name+'.mmd');texts=labels(source)
        width,height=(560,310) if name!='research-pipeline' else (560,130)
        c=canvas.Canvas(str(out/(name+'.pdf')),pagesize=(width,height));c.setTitle('GEAR: '+name);c.setAuthor('Andre Victor')
        if name=='gppme-architecture':
            boxes={'Z':(145,253,270,42),'P1':(15,156,165,76),'P2':(198,156,165,76),'P3':(381,156,165,76),'X':(15,83,165,52),'AI':(198,83,348,52),'H':(145,14,270,42)}
            for id,rect in boxes.items():draw_box(c,rect,texts[id],id=='AI')
            for x in (98,280,463):arrow(c,(280,253),(x,232))
            arrow(c,(180,194),(198,194));arrow(c,(363,194),(381,194))
            arrow(c,(98,135),(98,156));arrow(c,(280,135),(280,156),True);arrow(c,(463,135),(463,156),True)
            for x in (98,280,463):arrow(c,(x,83),(280,56),x!=98)
        elif name=='research-pipeline':
            xs=(8,120,232,344,456)
            for i,id in enumerate(('A','B','C','D','E')):
                draw_box(c,(xs[i],28,96,76),texts[id],id in ('D','E'))
                if i<4:arrow(c,(xs[i]+96,66),(xs[i+1],66))
        else:
            boxes={'A':(8,116,85,68),'B1':(116,222,84,50),'B2':(116,126,84,50),'B3':(116,30,84,50),'C':(224,116,84,68),'D':(331,105,94,90),'E1':(452,243,100,48),'E2':(452,170,100,48),'E3':(452,97,100,48),'E4':(452,24,100,48)}
            for id,rect in boxes.items():draw_box(c,rect,texts[id],id.startswith('E'))
            for y in (247,151,55):arrow(c,(93,150),(116,y));arrow(c,(200,y),(224,150))
            arrow(c,(308,150),(331,150))
            for y in (267,194,121,48):arrow(c,(425,150),(452,y))
        c.showPage();c.save();manifest.append({'source':source.relative_to(ROOT).as_posix(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'renderer':'tools/build_figures.py','output':(out/(name+'.pdf')).relative_to(ROOT).as_posix()})
    (out/'manifesto.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print('Três diagramas vetoriais gerados a partir dos rótulos Mermaid.')

if __name__=='__main__':build()
