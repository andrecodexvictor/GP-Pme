"""Regressão da publicação: conteúdo canônico e navegação no PDF."""
import tempfile
import unittest
from pathlib import Path
from pypdf import PdfReader
from tools.build_book import build
from tools.editorial import ROOT, blocks

class BookPublicationTests(unittest.TestCase):
    def test_book_keeps_all_chapters_and_copyable_fields(self):
        import json
        manifest=json.loads((ROOT/'framework/publicacoes.json').read_text(encoding='utf-8'))
        sources=[ROOT/'framework'/p for p in manifest['capitulos']]
        expected=[f'{i:02d}. '+next(v for k,v in blocks(p.read_text(encoding='utf-8')) if k=='h1')
                  for i,p in enumerate(sources,1)]
        with tempfile.TemporaryDirectory() as directory:
            pdf=Path(directory)/'book.pdf';build(pdf)
            reader=PdfReader(pdf)
            headings=[str(item['/Title']) for item in reader.outline if isinstance(item,dict)]
            self.assertEqual(headings,expected)
            text='\n'.join(page.extract_text() for page in reader.pages)
            normalized=' '.join(text.split())
            self.assertIn('Gestão, Execução, Agilidade e Risco',normalized)
            # Desenho de campos não pode eliminar os contratos copiáveis.
            for source in sources:
                for kind,value in blocks(source.read_text(encoding='utf-8')):
                    if kind=='code':
                        for line in value.splitlines():
                            if line.strip():self.assertIn(' '.join(line.split()),normalized)
            links=[a.get_object() for page in reader.pages for a in page.get('/Annots',[])]
            self.assertTrue(any(a.get('/A',{}).get('/URI','').startswith('https://') for a in links))
            self.assertTrue(any('/Dest' in a or a.get('/A',{}).get('/S')=='/GoTo' for a in links))

if __name__=='__main__':unittest.main()
