"""Contratos HTTP reais via ASGI; requer dependências de server/requirements.txt."""
import importlib.util
import unittest

AVAILABLE=all(importlib.util.find_spec(p) for p in ('fastapi','httpx'))

@unittest.skipUnless(AVAILABLE,'Runtime FastAPI/httpx indisponível neste Python')
class ApiTests(unittest.TestCase):
    def setUp(self):
        from fastapi.testclient import TestClient
        from server.api import app
        self.client=TestClient(app)

    def test_http_financial_and_maturity_contracts(self):
        r=self.client.post('/cot',json={'custo_otimizacao':9000,'ganho_mensal':3000,'custo_recorrente_mensal':500})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['roi_anual_percent'],233.33)
        r=self.client.post('/dan-financeiro',json={'custo_refatoracao':9000,'orcamento_anual_ti':30000})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['dan_financeiro'],.3)
        r=self.client.post('/maturidade',json={'respostas':[1]*10})
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['nivel_global'],4)

    def test_invalid_cost_and_authentication(self):
        import os
        from unittest.mock import patch
        self.assertEqual(self.client.post('/roi',json={'investimento':0,'retorno_mensal':100}).status_code,422)
        with patch.dict(os.environ,{'GPPME_API_KEY':'gear-test-local'}):
            self.assertEqual(self.client.get('/health').status_code,401)
            self.assertEqual(self.client.get('/health',headers={'X-API-Key':'gear-test-local'}).status_code,200)

    def test_catalogue_and_search_return_canonical_sections(self):
        r=self.client.get('/artefatos')
        self.assertEqual(r.status_code,200)
        r=self.client.get('/buscar',params={'q':'restauração','modo':'bm25'})
        self.assertEqual(r.status_code,200)
        self.assertTrue(r.json()['ok'])
        self.assertEqual(r.json()['modo'],'bm25')

if __name__=='__main__':unittest.main()
