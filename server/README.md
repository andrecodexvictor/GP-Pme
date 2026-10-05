# GEAR — serviços locais e ferramentas MCP

A camada `server/core.py` oferece regras locais, leitura de documentos e busca. `api.py` expõe uma API REST; `mcp_server.py` expõe ferramentas MCP para assistência opcional. Os identificadores `gp-pme` e variáveis `GPPME_*` permanecem por compatibilidade. A edição editorial vigente está em [framework](../framework/README.md).

## Arquitetura e requisitos

O núcleo usa a biblioteca padrão de Python. As bordas dependem de FastAPI/Uvicorn/Pydantic ou do SDK MCP. O pacote MCP requer Python 3.10 ou superior. Instale as dependências no ambiente destinado ao serviço:

```powershell
python -m pip install -r server/requirements.txt
```

A partir da raiz do projeto, `python -m server.core` executa uma verificação local mínima. Cálculos e checklists não comprovam implantação, ganho ou conformidade.

## MCP no ambiente deste usuário

MCPs são registrados globalmente em `%USERPROFILE%/.agents/mcp-hub/registry.json` e executados pelo hub compartilhado em `http://127.0.0.1:18888`. Os clientes usam URLs do hub; não configurar um subprocesso stdio por cliente nem criar instalação local de MCP neste projeto.

Antes de mudar o registro, ler `%USERPROFILE%/.agents/mcp-hub/README.md`. Usar `mcp-hub status`, `add NAME --config FILE`, `restart` e `sync-clients` conforme o contrato global. O backend precisa de executável absoluto, versão fixada e diretório deste projeto. A entrada `python -m server.mcp_server` é um transporte de backend para o serviço gerenciado; não é instrução de instalação no cliente. Esta reforma não registra nem publica um novo servidor por consequência.

| Ferramenta | Comportamento |
| --- | --- |
| `buscar_conhecimento` | Consulta corpus canônico; informa modo efetivo, com fallback lexical |
| `listar_artefatos` | Catálogo de documentos e caminhos relativos |
| `obter_documento` | Lê Markdown dentro da raiz, com limite de 200 KB |
| `avaliar_maturidade` | Dez respostas 0/1; IM-TI 0–10 e nível local 0–4 |
| `calcular_kpis` | Disponibilidade, resolução média e satisfação, com limites de entrada |
| `calcular_dan` | Alias histórico da proporção de itens legados; não é DAN financeiro |
| `calcular_dan_financeiro` | Custo de refatoração/orçamento anual, sem faixas universais |
| `calcular_cot` / `calcular_roi` | ROI líquido em 12 meses, razão bruta e payback simples |
| `protocolo_kanban` | Quatro colunas; três iniciados por executor, incluindo teste e bloqueio |
| `checklist_fase_zero` | Nove passos da janela inicial de 30 dias |
| `checklist_seguranca` | Dez verificações locais; não equivalem ao CIS IG1 completo |

O checklist e as sugestões começam pendentes. Campo de status ou total de pontos não demonstra verificação organizacional. O nome histórico `pilares` na resposta de maturidade agrupa três domínios.

## API REST

```powershell
python -m uvicorn server.api:app --host 127.0.0.1 --port 8766
```

OpenAPI: `http://127.0.0.1:8766/docs`. Configurar `GPPME_API_KEY` exige `X-API-Key` em todas as rotas; sem a variável, não há autenticação. O CORS atual aceita qualquer origem. Esses são limites da implementação; exposição além do ambiente local exige controles adequados.

| Método e rota | Entrada |
| --- | --- |
| GET `/health` | Estado e versão |
| GET `/artefatos?categoria=` | Categoria opcional |
| GET `/documento?caminho=` | Caminho retornado pelo catálogo |
| GET `/buscar?q=&k=&modo=` | Texto, até 50 trechos e modo |
| GET `/kanban/protocolo` | Política de fluxo |
| GET `/fase-zero` | Percurso inicial |
| GET `/seguranca/checklist` | Seleção local de verificações |
| POST `/maturidade` | `{"respostas":[1,1,0,1,0,1,1,0,0,1]}` |
| POST `/kpis` | Horas indisponíveis/totais, tempos de resolução e notas |
| POST `/dan` | `{"itens_legados":3,"itens_totais":10}` |
| POST `/dan-financeiro` | `{"custo_refatoracao":9000,"orcamento_anual_ti":30000}` |
| POST `/cot` | `{"custo_otimizacao":9000,"ganho_mensal":3000,"custo_recorrente_mensal":500}` |
| POST `/roi` | `{"investimento":9000,"retorno_mensal":3000,"custo_recorrente_mensal":500}` |

Os exemplos são entradas ilustrativas. Em COT, o exemplo retorna ROI líquido de 233,33% e payback de 3,6 meses; benefício líquido mensal não positivo retorna payback nulo. [Convenções e limites](../framework/indicadores/financeiros.md).

## Conhecimento e verificação

[Busca](../search/README.md) usa `framework/` e README raiz, excluindo versões antigas e materiais externos do corpus vigente. Índices ausentes produzem orientação de reconstrução. Embeddings ausentes ou incompatíveis com o hash do corpus conduzem a BM25. Não apresentar esse fallback como busca semântica.

Leitura resolve caminhos contra a raiz e aceita somente Markdown até 200 KB; caminhos externos são rejeitados. Isso não transforma documentos locais em conteúdo público autorizado: examinar o catálogo e a política de dados do ambiente.

Verificações: `python -m unittest discover -s tests -v`, em ambiente com FastAPI/httpx para incluir os testes HTTP. Dependência ausente pode resultar em teste pulado; isso não é aprovação. A validação do transporte MCP exige SDK e sessão própria, além das funções puras.

