"""Verifica unidades, comportamento de fronteira e contratos de publicação."""
import json
import math
import tempfile
import unittest
from pathlib import Path
from server import core
from search import ingest, export_web
from search.build_index import construir_bm25
from search.query import BM25
from tools.editorial import blocks, render
from tools.build_simulations import PROFILES, inputs, profile

class FinancialTests(unittest.TestCase):
    def test_simulation_units_and_independent_recalculation(self):
        # Hours from availability must agree with the annual service window.
        expected_benefits = [28600/12, 61690/12, 10707, 22150]
        expected_first_year_cost = [5280, 9570, 20680, 65800]
        for p,benefit,total in zip(PROFILES,expected_benefits,expected_first_year_cost):
            i,b,c = inputs(p)
            self.assertAlmostEqual(b,benefit)
            self.assertAlmostEqual(i+c*12,total)
            self.assertIn('não verificado',profile(p).lower())
            self.assertIn('nenhuma transição está assegurada',profile(p).lower())
        b = PROFILES[1]
        self.assertAlmostEqual(b['downtime'][1],(1-.995)*b['hours'])
        i,benefit,c = inputs(b)
        self.assertEqual(core.calcular_cot(i,benefit,c)['roi_anual_percent'],670.79)

    def test_net_roi_and_gross_ratio_are_distinct(self):
        r=core.calcular_cot(9000,3000)
        self.assertEqual(r['roi_anual_percent'],300)
        self.assertEqual(r['razao_beneficio_investimento'],4)
        self.assertEqual(r['payback_meses'],3)

    def test_recurring_cost_and_no_finite_payback(self):
        r=core.calcular_cot(9000,3000,500)
        self.assertEqual(r['roi_anual_percent'],233.33)
        self.assertEqual(r['payback_meses'],3.6)
        r=core.calcular_cot(1000,100,100)
        self.assertEqual(r['roi_anual_percent'],-100)
        self.assertIsNone(r['payback_meses'])

    def test_financial_inputs_reject_nonfinite_negative_and_bool(self):
        for bad in (-1,math.nan,math.inf,True,'9000'):
            self.assertIn('erro',core.calcular_cot(bad,100))
        self.assertIn('erro',core.calcular_cot(0,100))
        self.assertEqual(core.calcular_cot(100,0)['roi_anual_percent'],-100)

    def test_legacy_alias_does_not_masquerade_as_financial_dan(self):
        r=core.calcular_dan(3,10)
        self.assertEqual(r['dan'],r['proporcao_legada'])
        self.assertIn('compatibilidade',r)
        self.assertEqual(core.calcular_dan_financeiro(9000,30000)['dan_financeiro'],.3)
        for args in ((11,10),(-1,10),(1,0),(1.5,10)):
            self.assertIn('erro',core.calcular_dan(*args))

class PracticeTests(unittest.TestCase):
    def test_adoption_calendar_covers_day_30_and_leap_year(self):
        r=core.cronograma_implantacao('10/02/2028')
        self.assertEqual(len(r['fases']),1)
        self.assertEqual(r['fases'][0]['fim'],'2028-03-10')
        self.assertEqual(r['semanas_fase_zero'][-1]['fim'],'2028-03-10')
        self.assertEqual(r['semanas_fase_zero'][-1]['inicio'],'2028-03-02')
        self.assertIn('erro',core.cronograma_implantacao('31/02/2026'))
        self.assertEqual(r,core.cronograma_implantacao('2028-02-10'))

    def test_maturity_boundaries_and_ai_independence(self):
        for points,expected in ((0,0),(2,0),(3,1),(5,1),(6,2),(8,2),(9,3),(10,4)):
            r=core.avaliar_maturidade([1]*points+[0]*(10-points))
            self.assertEqual(r['nivel_global'],expected)
            self.assertEqual(len(r['pilares']),3)
        self.assertFalse(any('chatbot' in q['pergunta'] or 'IA' in q['pergunta'] for q in core.questionario_maturidade()))
        self.assertIn('erro',core.avaliar_maturidade(['Não']*10))
        self.assertIn('erro',core.avaliar_maturidade([1]*9))

    def test_kpis_domains_and_strict_targets(self):
        r=core.calcular_kpis(2,720,[1,3],[4,5])
        self.assertEqual(r['idsc_percent'],99.72)
        self.assertFalse(r['isu_meta_atingida'])
        for down,total in ((-1,720),(721,720),(0,0),(math.inf,720)):
            self.assertEqual(core.calcular_kpis(down,total,[],[])['idsc_percent'],'DADO INSUFICIENTE')
        self.assertEqual(core.calcular_kpis(0,720,[-1],[6])['isu_media'],'DADO INSUFICIENTE')
        self.assertEqual(core.calcular_kpis(0,720,[],[])['tmpr_horas'],'DADO INSUFICIENTE')
        self.assertTrue(core.calcular_kpis(0,720,[3],[4.5],meta_isu=4)['isu_meta_atingida'])

    def test_wip_includes_test_and_blocked(self):
        r=core.protocolo_kanban()
        self.assertEqual(r['unidade_wip'],'por executor')
        self.assertIn('Em Teste',r['estados_contados'])
        self.assertIn('Bloqueado',r['estados_contados'])

class PublicationTests(unittest.TestCase):
    def test_historical_versions_keep_copyable_operational_contracts(self):
        from tools.editorial import ROOT
        original=ROOT/'framework/templates/prompts-revisao-operacional.md'
        projected=ROOT/'References/GP-PME Versions/gp-pme-apendice-b-biblioteca-prompts.md'
        contracts=[v for k,v in blocks(original.read_text(encoding='utf-8')) if k=='code']
        copied=[v for k,v in blocks(projected.read_text(encoding='utf-8')) if k=='code']
        self.assertEqual(len(contracts),5)
        for contract in contracts:self.assertIn(contract,copied)
        self.assertIn('IA',projected.read_text(encoding='utf-8'))

    def test_historical_financial_examples_keep_units_and_correct_return(self):
        from tools.editorial import ROOT
        path=ROOT/'References/GP-PME Versions/gp-pme-documento-mestre-tecnico-cap5.md'
        text=path.read_text(encoding='utf-8')
        self.assertIn('0,015',text)
        self.assertIn('hora por linha',text)
        self.assertIn('50%',text)
        self.assertEqual(core.calcular_cot(50000,25000/12)['roi_anual_percent'],-50)
        self.assertEqual(core.calcular_cot(50000,25000/12)['payback_meses'],24)

    def test_project_requirements_do_not_claim_observed_rollout(self):
        from tools.editorial import ROOT
        tasks=(ROOT/'Docs/Tasklist.md').read_text(encoding='utf-8')
        agents=(ROOT/'Docs/Specialist_Agents.md').read_text(encoding='utf-8')
        self.assertNotRegex(tasks.lower(),r'(?m)^\s*-\s+\[x\]')
        self.assertIn('sem apagar arquivo real',tasks)
        self.assertIn('um orquestrador e oito especialistas',agents)
        self.assertIn('não exige exposição de raciocínio interno',agents)

    def test_operational_flow_branches_preserve_emergency_and_capacity_paths(self):
        from tools.build_flowcharts import FLOWS
        for name,spec in FLOWS.items():
            nodes={row[0]:row for row in spec['nodes']}
            edges=spec['edges']
            for start,end,points,_ in edges:
                self.assertIn(start,nodes);self.assertIn(end,nodes)
                self.assertGreaterEqual(len(points),2)
            for identifier,row in nodes.items():
                if row[1]=='decision':
                    self.assertEqual({label for a,_,_,label in edges if a==identifier},{'Sim','Não'})
            reached={'inicio'}
            while True:
                current=reached|{end for start,end,_,_ in edges if start in reached}
                if current==reached:break
                reached=current
            self.assertEqual(reached,set(nodes),name)
        demand=FLOWS['demanda']['edges']
        self.assertIn(('critico','resposta'),[(a,b) for a,b,_,label in demand if label=='Sim'])
        self.assertNotIn(('resposta','capacidade'),[(a,b) for a,b,_,_ in demand])

    def test_flowchart_projection_preserves_local_image_and_text_alternative(self):
        from tools.editorial import ROOT
        source=ROOT/'framework/guias/fluxos-de-trabalho.md'
        page=ROOT/'GP-Pme Article/docs/guias/fluxos-de-trabalho.html'
        body,_=render(source.read_text(encoding='utf-8'),source,page)
        self.assertEqual(body.count('<img '),2)
        self.assertIn('../../assets/diagrams/demanda.svg',body)
        self.assertIn('tabindex="0"',body)
        self.assertIn('Se não houver capacidade acordada',body)

    def test_agent_maturity_contract_matches_executable_questionnaire(self):
        from tools.build_agent_contracts import build
        with tempfile.TemporaryDirectory() as directory:
            build(Path(directory))
            contract=Path(directory,'Agente_Maturidade.md').read_text(encoding='utf-8')
            copied=[value for kind,value in blocks(contract) if kind=='code']
            self.assertEqual(len(copied),1)
            questions=core.questionario_maturidade()
            self.assertEqual(len(questions),10)
            for question in questions:
                self.assertIn(question['pergunta'],copied[0])
            self.assertNotIn('{questions}',copied[0])

    def test_existing_skill_routes_resolve_with_preserved_identifiers(self):
        import re
        from urllib.parse import unquote
        from tools.build_existing_skills import build, SKILLS
        with tempfile.TemporaryDirectory() as directory:
            base=Path(directory)
            build(base)
            expected={'gp-pme-'+row[0] for row in SKILLS}
            self.assertEqual({p.parent.name for p in base.glob('*/SKILL.md')},expected)
            for identifier in expected:
                source=base/identifier/'SKILL.md'
                text=source.read_text(encoding='utf-8')
                self.assertIn('\nname: '+identifier+'\n',text)
                links=re.findall(r'\[[^\]]+\]\(<([^>]+)>\)',text)
                self.assertTrue(links)
                for target in links:
                    self.assertTrue((source.parent/unquote(target)).resolve().exists(),target)
            router=(base/'gp-pme-consultor/SKILL.md').read_text(encoding='utf-8')
            for identifier in expected-{'gp-pme-consultor'}:
                self.assertIn('['+identifier+']',router)

    def test_legacy_catalog_metadata_is_parseable_and_navigable(self):
        import re
        import xml.etree.ElementTree as ET
        from tools.editorial import ROOT
        source=ROOT/'GP-PME antigravity/INDEX.md'
        text=source.read_text(encoding='utf-8')
        metadata=re.search(r'```xml\n(.*?)\n```',text,re.S)[1]
        tree=ET.fromstring(metadata)
        entries=tree.findall('./document-mapping/document')
        self.assertTrue(entries)
        links=set(re.findall(r'\[abrir\]\(<([^>]+)>\)',text))
        for entry in entries:
            path=entry.attrib['file']
            self.assertIn(path,links)
            self.assertTrue((source.parent/path).resolve().exists(),path)
            self.assertTrue(entry.findtext('topic-coverage'))

    def test_copied_requirement_prompt_survives_projection_without_other_roles(self):
        from tools.editorial import ROOT
        canonical=ROOT/'framework/templates/prompts-assistencia.md'
        legacy=ROOT/'GP-PME antigravity/Templates/Prompts/Template_Prompt_PRD.md'
        contracts=[v for k,v in blocks(canonical.read_text(encoding='utf-8')) if k=='code']
        copied=[v for k,v in blocks(legacy.read_text(encoding='utf-8')) if k=='code']
        self.assertIn(contracts[1],copied)
        self.assertFalse(any(v in copied for v in (contracts[0],contracts[2],contracts[3])))
        body,headings=render(legacy.read_text(encoding='utf-8'),legacy,legacy.with_suffix('.html'))
        self.assertIn('Tarefa: preparar PRD',body)
        self.assertFalse(any('Tarefa:' in label for _,label,_ in headings))

    def test_generated_manuals_keep_navigation_and_sources_resolvable(self):
        from tools.check_links import check
        self.assertEqual(check(),0)

    def test_legacy_projection_preserves_link_destinations_across_depths(self):
        from tools.build_legacy_masters import ROOT,excerpt
        from urllib.parse import unquote,urlsplit
        import re
        source=ROOT/'framework/guias/usar-ia.md'
        target=ROOT/'GP-PME antigravity/GP-Pme complete/manual.md'
        before=re.findall(r'\[[^\]]+\]\(([^)]+)\)',source.read_text(encoding='utf-8'))
        after=re.findall(r'\[[^\]]+\]\(([^)]+)\)',excerpt('guias/usar-ia.md',target))
        self.assertEqual(len(before),len(after))
        for original,projected in zip(before,after):
            a=urlsplit(original.strip('<>'));b=urlsplit(projected.strip('<>'))
            self.assertEqual(a.fragment,b.fragment)
            self.assertEqual((source.parent/unquote(a.path)).resolve(),
                             (target.parent/unquote(b.path)).resolve())

    def test_fences_do_not_create_headings(self):
        source=Path('framework/test.md').resolve();page=Path('GP-Pme Article/docs/test.html').resolve()
        body,hs=render('# Título\n\n```py\n## Código\n```\n\n## Mesmo\n\nTexto\n\n## Mesmo\nOutro',source,page)
        self.assertEqual([a for _,_,a in hs],['titulo','mesmo','mesmo-1'])
        sections=ingest._dividir_em_secoes(['```','## Código','```','## Mesmo','Texto','## Mesmo','Outro'],'Título')
        self.assertEqual([s.anchor for s in sections],['titulo','mesmo','mesmo-1'])

    def test_ingestion_only_uses_canonical_content_and_exact_sections(self):
        chunks=ingest.gerar_corpus()
        self.assertTrue(chunks)
        self.assertTrue(all(c['doc'].startswith('framework/') or c['doc']=='README.md' for c in chunks))
        for c in chunks:
            projection=export_web._projetar(c)
            self.assertIn('#'+c['anchor'],projection['href'])
            self.assertLessEqual(len(projection['texto']),800)
        bm25=BM25(construir_bm25(chunks))
        self.assertTrue(bm25.pontuar(['restauracao']))

if __name__=='__main__':unittest.main()
