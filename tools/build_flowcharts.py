"""Fluxogramas operacionais vetoriais, com uma fonte comum para web e livro."""
import hashlib
import json
from pathlib import Path
from tools.editorial import ROOT, PORTAL

# Coordenadas de topo para facilitar a manutenção dos caminhos de decisão.
# No grafo, voltas dependem de mudança de situação ou nova verificação.
FLOWS={
    'demanda': dict(width=720,height=980,title='Da demanda ao encerramento',
        nodes=[
            ('inicio','terminal',350,34,190,44,['Demanda recebida']),
            ('registro','process',350,112,260,62,['Registrar necessidade,','serviço e responsável']),
            ('critico','decision',350,220,184,100,['Incidente','crítico?']),
            ('resposta','process',586,220,190,72,['Acionar resposta,','alçada e recuperação']),
            ('prioridade','process',350,340,270,62,['Conferir prioridade,','dependências e critérios']),
            ('capacidade','decision',350,448,184,100,['Há capacidade','acordada?']),
            ('espera','process',112,448,190,72,['Manter na fila','com motivo e revisão']),
            ('execucao','process',350,555,230,62,['Executar o recorte','autorizado']),
            ('teste','process',350,647,230,62,['Verificar resultado','e critério de aceite']),
            ('aceite','decision',350,758,184,100,['Saída aceita','ou encerramento','justificado?']),
            ('ajuste','process',586,758,190,72,['Registrar lacuna','e decidir correção']),
            ('fim','terminal',350,915,270,64,['Registrar evidência, motivo','e próximos passos']),
        ],
        edges=[
            ('inicio','registro',[(350,56),(350,81)],''),
            ('registro','critico',[(350,143),(350,170)],''),
            ('critico','resposta',[(442,220),(491,220)],'Sim'),
            ('critico','prioridade',[(350,270),(350,309)],'Não'),
            ('resposta','fim',[(586,256),(698,256),(698,873),(350,873),(350,883)],'Após verificação'),
            ('prioridade','capacidade',[(350,371),(350,398)],''),
            ('capacidade','espera',[(258,448),(207,448)],'Não'),
            ('espera','prioridade',[(112,412),(112,340),(215,340)],'Revisar'),
            ('capacidade','execucao',[(350,498),(350,524)],'Sim'),
            ('execucao','teste',[(350,586),(350,616)],''),
            ('teste','aceite',[(350,678),(350,708)],''),
            ('aceite','ajuste',[(442,758),(491,758)],'Não'),
            ('ajuste','execucao',[(586,722),(586,555),(465,555)],'Se autorizada'),
            ('aceite','fim',[(350,808),(350,883)],'Sim'),
        ]),
    'incidente': dict(width=720,height=830,title='Resposta e recuperação de serviço',
        nodes=[
            ('inicio','terminal',350,35,250,44,['Sinal ou relato de incidente']),
            ('registro','process',350,116,270,62,['Registrar fatos, horários','e incertezas']),
            ('acao','process',350,215,270,72,['Acionar responsável e alçada;','avaliar resposta apropriada']),
            ('capacidade','decision',350,328,184,100,['A capacidade','local atende?']),
            ('apoio','process',586,328,190,72,['Acionar fornecedor','ou especialista']),
            ('resposta','process',350,442,290,72,['Conter conforme o ambiente,','preservar evidências e comunicar']),
            ('recuperacao','process',350,548,270,62,['Recuperar ou preparar','alternativa operacional']),
            ('verificacao','decision',350,661,184,100,['Serviço ou alternativa','verificados?']),
            ('pendencia','process',112,661,190,72,['Manter pendência','e atualizar os afetados']),
            ('fim','terminal',350,787,300,64,['Registrar restrições, encerramento','e correções atribuídas']),
        ],
        edges=[
            ('inicio','registro',[(350,57),(350,85)],''),
            ('registro','acao',[(350,147),(350,179)],''),
            ('acao','capacidade',[(350,251),(350,278)],''),
            ('capacidade','apoio',[(442,328),(491,328)],'Não'),
            ('apoio','resposta',[(586,364),(586,442),(495,442)],''),
            ('capacidade','resposta',[(350,378),(350,406)],'Sim'),
            ('resposta','recuperacao',[(350,478),(350,517)],''),
            ('recuperacao','verificacao',[(350,579),(350,611)],''),
            ('verificacao','pendencia',[(258,661),(207,661)],'Não'),
            ('pendencia','recuperacao',[(112,625),(112,548),(215,548)],'Reavaliar'),
            ('verificacao','fim',[(350,711),(350,755)],'Sim'),
        ]),
}


def drawing(name):
    from reportlab.graphics.shapes import Drawing, Rect, Polygon, String, PolyLine
    from reportlab.lib import colors
    from tools.build_book import fonts
    INK=colors.HexColor('#202321');LINE=colors.HexColor('#737b75')
    COPPER=colors.HexColor('#8a421e');SOFT=colors.HexColor('#f3f5f2')
    fonts()
    spec=FLOWS[name];height=spec['height'];d=Drawing(spec['width'],height)
    for _,_,points,label in spec['edges']:
        xy=[(x,height-y) for x,y in points]
        d.add(PolyLine([v for p in xy for v in p],strokeColor=LINE,strokeWidth=1.4))
        x,y=xy[-1];px,py=xy[-2]
        import math
        angle=math.atan2(y-py,x-px);size=7
        arrow=[x,y,x-size*math.cos(angle-.45),y-size*math.sin(angle-.45),x-size*math.cos(angle+.45),y-size*math.sin(angle+.45)]
        d.add(Polygon(arrow,fillColor=LINE,strokeColor=None))
        if label:
            x1,y1=xy[0];x2,y2=xy[1]
            # Rótulos de decisão ficam fora dos nós e sobre a primeira aresta.
            xx=(x1+x2)/2;yy=(y1+y2)/2+7
            if abs(x1-x2)<1:xx+=24;yy-=3
            if label=='Após verificação':xx=613;yy=height-867
            if label=='Se autorizada':xx=629;yy=height-618
            if label in ('Revisar','Reavaliar'):xx=162;yy=(y1+y2)/2
            d.add(String(xx,yy,label,fontName='PublicBold',fontSize=13,textAnchor='middle',fillColor=COPPER))
    for _,kind,x,y,w,h,lines in spec['nodes']:
        yy=height-y
        if kind=='decision':
            shape=Polygon([x-w/2,yy,x,yy+h/2,x+w/2,yy,x,yy-h/2],fillColor=SOFT,strokeColor=COPPER,strokeWidth=1.4)
        else:
            shape=Rect(x-w/2,yy-h/2,w,h,rx=20 if kind=='terminal' else 0,ry=20 if kind=='terminal' else 0,fillColor=SOFT if kind=='terminal' else colors.white,strokeColor=LINE,strokeWidth=1.2)
        d.add(shape)
        start=yy+(len(lines)-1)*9-5
        for i,line in enumerate(lines):
            d.add(String(x,start-i*18,line,fontName='PublicBold' if kind=='decision' else 'Public',fontSize=15,textAnchor='middle',fillColor=INK))
    return d


def build():
    from reportlab.graphics import renderSVG, renderPDF
    base=PORTAL/'assets/diagrams';base.mkdir(parents=True,exist_ok=True)
    output=ROOT/'.context/gear-execution/fluxogramas';output.mkdir(parents=True,exist_ok=True)
    records=[]
    for name,spec in FLOWS.items():
        d=drawing(name);svg=base/(name+'.svg')
        renderSVG.drawToFile(d,str(svg))
        # SVG em <img> usa fontes locais do sistema como fallback; PDF usa Public Sans.
        text=svg.read_text(encoding='utf-8').replace('font-family: Public;', 'font-family: Arial, sans-serif;').replace('font-family: PublicBold;', 'font-family: Arial, sans-serif; font-weight: bold;')
        svg.write_text(text,encoding='utf-8')
        renderPDF.drawToFile(d,str(output/(name+'.pdf')))
        records.append(dict(nome=name,titulo=spec['title'],source='tools/build_flowcharts.py',svg=svg.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(svg.read_bytes()).hexdigest()))
    (output/'manifesto.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Dois fluxogramas operacionais gerados em SVG e PDF vetorial.')


if __name__=='__main__':build()
