"""Testes das funções locais ADK sem importar ou simular o SDK de modelo."""
import ast
from datetime import date
from pathlib import Path
import unittest
from server import core

ROOT=Path(__file__).resolve().parents[1]

def functions(module):
    tree=ast.parse((ROOT/'agents/gp-pme-adk'/module/'agent.py').read_text(encoding='utf-8'))
    # Extrai apenas funções puras e constantes usadas; não testa o SDK ADK.
    nodes=[node for node in tree.body if isinstance(node,ast.FunctionDef) or
           isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in
           ('PERGUNTAS','NIVEIS','INTERPRETACOES','TRANSICOES') for t in node.targets) or
           isinstance(node,ast.AnnAssign) and isinstance(node.target,ast.Name) and
           node.target.id in ('SECOES_OBRIGATORIAS','RESTRICOES_ANTI_ALUCINACAO')]
    scope={'_core':core,'date':date}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),str(module),'exec'),scope)
    return scope

class AgentToolTests(unittest.TestCase):
    def test_maturity_plan_rejects_invalid_levels_and_reviews_high_scores(self):
        fn=functions('agente_maturidade')['plano_transicao']
        for current,target in ((-1,4),(0,5),(0,2.9),(True,4),('0',4)):
            self.assertIn('erro',fn(current,target))
        self.assertIn('Rever lacunas',fn(4,4)['mensagem'])
        self.assertEqual(len(fn(0,4)['transicoes_cobertas']),4)
        self.assertIn('Não garantem',fn(0,4)['limite'])

    def test_governance_pauta_uses_local_targets_and_authority(self):
        r=functions('agente_governanca')['gerar_pauta_cdti']('Falha de restauração')
        self.assertIn('metas acordadas',r)
        self.assertIn('autoridade responsável',r)
        self.assertNotIn('99,5%',r)
        self.assertNotIn('4,5/5',r)

    def test_risk_mentions_cannot_produce_measured_risk(self):
        fn=functions('agente_seguranca')['avaliar_risco']
        r=fn('Servidor ERP financeiro sem mfa e sem backup')
        self.assertTrue(r['vulnerabilidades_detectadas'])
        for field in ('probabilidade','impacto','nivel_risco'):
            self.assertEqual(r[field],'DADO INSUFICIENTE')
        self.assertIn('lexical',r['limite'])
        self.assertFalse(fn('Manual de administração disponível')['vulnerabilidades_detectadas'])

    def test_incident_draft_preserves_authorization_and_uncertainty(self):
        fn=functions('agente_seguranca')['plano_resposta_incidente']
        for kind in ('ransomware','phishing','vazamento de dados','acesso indevido','outro'):
            r=fn(kind)
            self.assertIn('não autoriza execução',r)
            self.assertIn('autorização',r.lower())
            self.assertIn('evidências',r.lower())
        self.assertIn('controlador',fn('vazamento de dados').lower())

    def test_presence_checks_expose_their_limits(self):
        prd=functions('agente_prd')
        r=prd['validar_prd'](prd['esqueleto_prd']('Exercício'))
        self.assertTrue(r['completo'])
        self.assertIn('lexical',r['limite'])
        # Placeholders still need review even when titles are present.
        self.assertIn('aprovação',r['limite'])
        prompt=functions('agente_prompts')
        r=prompt['avaliar_prompt']('Persona contexto instruções output dado insuficiente')
        self.assertEqual(r['score'],5)
        self.assertIn('não verifica',r['limite'])
        self.assertIn('conferir conteúdo',r['veredito'])

    def test_audit_is_pending_and_does_not_certify_outputs(self):
        r=functions('agente_metricas_auditoria')['checklist_auditoria_hitl']()
        self.assertEqual(len(r),10)
        self.assertTrue(all(item['status']=='pendente' for item in r))

if __name__=='__main__':unittest.main()
