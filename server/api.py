"""API REST (FastAPI) do framework GP-PME — espelha 1:1 a camada `core`.

Projetada para ambientes hostis a ferramentas de gestão (sem ClickUp/Jira):
qualquer automação interna consome as regras de negócio do GP-PME por HTTP/curl.
Toda a lógica vive em `core.py`; este módulo é apenas a fachada web (validação
de entrada, OpenAPI em PT-BR, CORS e autenticação opcional).

Executar:
    uvicorn server.api:app --host 127.0.0.1 --port 8766

Autenticação (opcional): defina a variável de ambiente GPPME_API_KEY para exigir
o header `X-API-Key` em todas as rotas. Sem a variável, a API fica aberta.
"""
from __future__ import annotations

import os
from typing import List, Optional

from fastapi import Depends, FastAPI, Header, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from . import core

app = FastAPI(
    title="GP-PME — API REST",
    version="1.0.0",
    description=(
        "Framework de gestão de TI para PMEs brasileiras. Expõe maturidade, KPIs, "
        "DAN, COT, ROI, Kanban, Fase Zero, segurança e busca no corpus. Feita para "
        "ambientes hostis a ferramentas de gestão: use com `curl`."
    ),
)

# CORS liberado — a API serve automações internas confiáveis (rede interna).
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Autenticação opcional via GPPME_API_KEY (header X-API-Key) ────────────────
def verificar_api_key(x_api_key: Optional[str] = Header(default=None)) -> None:
    """Exige X-API-Key só quando GPPME_API_KEY está definida no ambiente."""
    esperada = os.environ.get("GPPME_API_KEY")
    if esperada and x_api_key != esperada:
        raise HTTPException(status_code=401, detail="X-API-Key inválida ou ausente.")


# ── Modelos Pydantic (corpo dos POSTs) ────────────────────────────────────────
class RespostasMaturidade(BaseModel):
    respostas: List[int] = Field(
        ...,
        description="Exatamente 10 respostas (1=Sim, 0=Não) na ordem do questionário.",
        json_schema_extra={"example": [1, 1, 0, 1, 0, 1, 1, 0, 0, 1]},
    )


class EntradaKPIs(BaseModel):
    horas_indisponibilidade: float = Field(..., description="Horas fora do ar no período.", examples=[2])
    horas_totais: float = Field(..., description="Horas totais do período (ex.: 720 = 30 dias).", examples=[720])
    tempos_resposta_horas: List[float] = Field(
        default_factory=list, description="Tempos de primeira resposta (h) por chamado.", examples=[[1.5, 3.0, 2.0]]
    )
    notas_satisfacao: List[float] = Field(
        default_factory=list, description="Notas de satisfação (escala 1-5).", examples=[[5, 4, 5]]
    )


class EntradaDAN(BaseModel):
    itens_legados: int = Field(..., ge=0, description="Itens legados/obsoletos do inventário 80/20.", examples=[3])
    itens_totais: int = Field(..., gt=0, description="Total de itens do inventário 80/20.", examples=[10])


class EntradaCOT(BaseModel):
    custo_otimizacao: float = Field(..., gt=0, description="Aporte único do COT (R$).", examples=[9000])
    ganho_mensal: float = Field(..., gt=0, description="Ganho/economia mensal recorrente (R$).", examples=[3000])


class EntradaROI(BaseModel):
    investimento: float = Field(..., gt=0, description="Aporte único da iniciativa (R$).", examples=[9000])
    retorno_mensal: float = Field(..., gt=0, description="Retorno mensal recorrente (R$).", examples=[3000])


_dep = [Depends(verificar_api_key)]


# ── Rotas GET (consultas / catálogos) ─────────────────────────────────────────
@app.get("/health", summary="Verifica se a API está no ar", tags=["Sistema"], dependencies=_dep)
def health() -> dict:
    """Retorna status básico e versão — use para healthcheck de deploy."""
    return {"ok": True, "servico": "gp-pme-api", "versao": app.version}


@app.get("/artefatos", summary="Lista os documentos do framework", tags=["Conhecimento"], dependencies=_dep)
def artefatos(
    categoria: str = Query("", description="Filtro opcional: Portal, Guia ou Template.")
) -> dict:
    """Catálogo curado dos documentos GP-PME. Cada 'caminho' serve a /documento."""
    return core.listar_artefatos(categoria)


@app.get("/documento", summary="Lê um documento .md do repositório", tags=["Conhecimento"], dependencies=_dep)
def documento(
    caminho: str = Query(..., description="Caminho relativo à raiz, como retornado por /artefatos.")
) -> dict:
    """Leitura segura de .md (anti path-traversal; só .md; limite de 200 KB)."""
    r = core.obter_documento(caminho)
    if not r.get("ok"):
        raise HTTPException(status_code=404, detail=r.get("erro", "Documento indisponível."))
    return r


@app.get("/buscar", summary="Busca semântica/BM25 no corpus", tags=["Conhecimento"], dependencies=_dep)
def buscar(
    q: str = Query(..., description="Texto da consulta.", examples=["como montar o Kanban"]),
    k: int = Query(5, ge=1, le=50, description="Número de trechos a retornar."),
    modo: str = Query("hibrido", description="hibrido, semantico ou bm25."),
) -> dict:
    """Retorna os `k` trechos mais relevantes. Degrada com 'erro' se o índice não existir."""
    return core.buscar_conhecimento(q, k=k, modo=modo)


@app.get("/kanban/protocolo", summary="Protocolo Kanban + tarefas-semente", tags=["Execução"], dependencies=_dep)
def kanban_protocolo() -> dict:
    """Especificação do Kanban (4 colunas, WIP=3, Raia Rápida) e 8 tarefas da Fase Zero."""
    return core.protocolo_kanban()


@app.get("/fase-zero", summary="Checklist dos 30 dias da Fase Zero", tags=["Execução"], dependencies=_dep)
def fase_zero() -> dict:
    """Os 9 passos ordenados da Fase Zero (30 dias)."""
    return core.checklist_fase_zero()


@app.get("/seguranca/checklist", summary="10 controles NIST-Lite / CIS IG1", tags=["Segurança"], dependencies=_dep)
def seguranca_checklist() -> dict:
    """Checklist dos 10 controles mínimos de segurança (todos nascem 'pendente')."""
    return core.checklist_10_controles()


# ── Rotas POST (cálculos) ─────────────────────────────────────────────────────
@app.post("/maturidade", summary="Calcula o IM-TI (0-10) e o nível (0-4)", tags=["Diagnóstico"], dependencies=_dep)
def maturidade(entrada: RespostasMaturidade) -> dict:
    """Índice de Maturidade da TI a partir das 10 respostas do questionário."""
    r = core.avaliar_maturidade(entrada.respostas)
    if "erro" in r:
        raise HTTPException(status_code=422, detail=r["erro"])
    return r


@app.post("/kpis", summary="Calcula os 3 KPIs Visíveis (IDSC, TMpR, ISU)", tags=["Diagnóstico"], dependencies=_dep)
def kpis(entrada: EntradaKPIs) -> dict:
    """IDSC (>99,5%), TMpR (<4h) e ISU (>4,5). Campos sem dado retornam 'DADO INSUFICIENTE'."""
    return core.calcular_kpis(
        entrada.horas_indisponibilidade,
        entrada.horas_totais,
        entrada.tempos_resposta_horas,
        entrada.notas_satisfacao,
    )


@app.post("/dan", summary="Calcula a Dívida de Arquitetura Normalizada", tags=["Diagnóstico"], dependencies=_dep)
def dan(entrada: EntradaDAN) -> dict:
    """DAN = legados/totais; zonas: <0,15 saudável, 0,15-0,35 alerta, >0,35 crítico."""
    return core.calcular_dan(entrada.itens_legados, entrada.itens_totais)


@app.post("/cot", summary="Payback e ROI anual de um COT", tags=["Diagnóstico"], dependencies=_dep)
def cot(entrada: EntradaCOT) -> dict:
    """Payback (meses) e ROI anual (%) de um investimento de otimização (COT)."""
    return core.calcular_cot(entrada.custo_otimizacao, entrada.ganho_mensal)


@app.post("/roi", summary="ROI operacional simplificado", tags=["Diagnóstico"], dependencies=_dep)
def roi(entrada: EntradaROI) -> dict:
    """ROI anual e payback de qualquer iniciativa com retorno mensal recorrente."""
    return core.calcular_roi_simplificado(entrada.investimento, entrada.retorno_mensal)
