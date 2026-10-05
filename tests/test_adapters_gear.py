import importlib
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

BASE=Path(__file__).resolve().parents[1]/'agents/gp-pme-adk'
sys.path.insert(0,str(BASE))
from adapters.base import COLUNAS_GP_PME, FASE_ZERO_TASKS, Cartao

class AdapterTests(unittest.TestCase):
    def test_five_dry_run_contracts(self):
        with patch.dict(os.environ,{'GPPME_DRY_RUN':'1'}):
            for name in ('clickup','notion','trello','jira','linear'):
                with self.subTest(platform=name):
                    adapter=importlib.import_module('adapters.'+name).Adapter()
                    board=adapter.configurar_quadro_gp_pme()
                    self.assertTrue(adapter.dry_run)
                    self.assertEqual(board.colunas,COLUNAS_GP_PME)
                    cards=adapter.listar_cartoes(board)
                    self.assertEqual(len(cards),len(FASE_ZERO_TASKS))
                    for card in cards[:4]:adapter.mover_cartao(board,card.id,COLUNAS_GP_PME[1])
                    self.assertTrue(adapter.verificar_wip(board)['estourado'])

    def test_started_items_per_executor_and_missing_assignment(self):
        adapter=importlib.import_module('adapters.trello').Adapter()
        cards=[Cartao(str(i),'Tarefa','Em Teste',extra={'executor':'A' if i<4 else 'B'}) for i in range(6)]
        with patch.object(adapter,'listar_cartoes',return_value=cards):
            result=adapter.verificar_wip(None)
            self.assertTrue(result['estourado'])
            self.assertEqual(result['por_executor'],{'A':4,'B':2})
            self.assertTrue(result['verificacao_completa'])
        cards[0].extra={}
        with patch.object(adapter,'listar_cartoes',return_value=cards):
            self.assertFalse(adapter.verificar_wip(None)['verificacao_completa'])
