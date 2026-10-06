"""Identidade editorial do livro: capa, aberturas e campos de registro."""
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable, Paragraph

PETROL = colors.HexColor('#173f43')
COPPER = colors.HexColor('#8a421e')
ACCENT = colors.HexColor('#e8ad83')
PAPER = colors.HexColor('#f7f3ec')
WHITE = colors.white

PARTS = {
    'nucleo': '01 / Núcleo do método', 'adocao': '02 / Percurso de adoção',
    'guias': '03 / Guias de trabalho', 'indicadores': '04 / Medir e decidir',
    'exemplos': '05 / Exemplos comentados', 'templates': '06 / Modelos de registro',
    'fundamentos': '07 / Fundamentos e adaptações',
    'referencias': '08 / Vocabulário e fontes',
}

def cover(canvas, size, date):
    w, h = size
    canvas.saveState()
    canvas.setFillColor(PETROL); canvas.rect(0, 0, w, h, fill=1, stroke=0)
    canvas.setFillColor(ACCENT); canvas.rect(52, h-79, 44, 3, fill=1, stroke=0)
    canvas.setFont('PublicBold', 10); canvas.drawString(52, h-103, 'GOVERNANÇA E GESTÃO DE TI PARA PMEs')
    canvas.setFillColor(WHITE); canvas.setFont('PublicBold', 94)
    canvas.drawString(46, h-227, 'GEAR')
    canvas.setFont('Serif', 27)
    for y, line in [(h-277, 'Gestão, Execução,'), (h-313, 'Agilidade e Risco')]:
        canvas.drawString(52, y, line)
    # O percurso é uma chave de leitura, sem acrescentar domínios ao método.
    labels = ['DECIDIR', 'EXECUTAR', 'VERIFICAR', 'REVISAR']
    y = 271; xs = [52, 177, 302, 427]
    canvas.setStrokeColor(ACCENT); canvas.setLineWidth(1)
    canvas.line(xs[0]+5, y, xs[-1]+5, y)
    for i, (x, label) in enumerate(zip(xs, labels), 1):
        canvas.setFillColor(PETROL); canvas.circle(x+5, y, 6, stroke=1, fill=1)
        canvas.setFillColor(ACCENT); canvas.setFont('PublicBold', 9)
        canvas.drawString(x, y-30, f'{i:02d}')
        canvas.setFillColor(WHITE); canvas.setFont('Public', 8)
        canvas.drawString(x, y-47, label)
    canvas.setFillColor(PAPER); canvas.rect(0, 0, w, 139, stroke=0, fill=1)
    canvas.setFillColor(PETROL); canvas.setFont('PublicBold', 12)
    canvas.drawString(52, 101, 'Andre Victor')
    canvas.setFont('Public', 9)
    canvas.drawString(52, 79, 'Livro do framework · Edição 2026.10')
    canvas.setFont('Public', 8); canvas.drawString(52, 57, date)
    canvas.restoreState()

class ChapterHeading(Flowable):
    def __init__(self, index, title, part, bookmark):
        super().__init__()
        self.index, self.title, self.part = index, title, part
        self.bookmark, self.outline_level = bookmark, 0
        self.keepWithNext = True
        self.paragraph = Paragraph(title, ParagraphStyle(
            'ChapterTitle', fontName='PublicBold', fontSize=23, leading=28,
            textColor=WHITE))
    def getPlainText(self):
        return f'{self.index:02d}. '+self.paragraph.getPlainText()
    def wrap(self, width, height):
        self.width = width
        _, text_height = self.paragraph.wrap(width-108, height)
        self.height = max(88, text_height+61)+18
        self.text_height = text_height
        return self.width, self.height
    def draw(self):
        c = self.canv; box_h = self.height-18
        c.setFillColor(PETROL); c.rect(0, 18, self.width, box_h, stroke=0, fill=1)
        c.setFillColor(ACCENT); c.setFont('PublicBold', 8)
        c.drawString(20, self.height-24, self.part.upper())
        c.setFont('PublicBold', 39); c.drawString(18, box_h-48, f'{self.index:02d}')
        self.paragraph.drawOn(c, 90, self.height-43-self.text_height)

class RecordBlock(Flowable):
    """Campos pré-formatados com fundo de papel e margem interna."""
    def __init__(self, text, style):
        super().__init__()
        from reportlab.platypus import Preformatted
        self.content = Preformatted(text, style)
    def wrap(self, width, height):
        cw, ch = self.content.wrap(width-24, height)
        if cw > width-24+1:
            raise ValueError('Campo pré-formatado excede a largura da página')
        self.width, self.height = width, ch+24
        return width, self.height
    def draw(self):
        c=self.canv; c.setFillColor(PAPER); c.setStrokeColor(colors.HexColor('#d6dcd7'))
        c.setLineWidth(.5); c.rect(0,0,self.width,self.height,fill=1,stroke=1)
        self.content.drawOn(c,12,12)
