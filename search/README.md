# GEAR — busca no conteúdo vigente

O motor Python oferece BM25 e um caminho opcional de embeddings. O portal oferece busca lexical local. Todos consultam conteúdo canônico de `framework/` e README raiz; versões GP-PME/NEXUS-PME, dados do usuário e documentos externos ficam fora do corpus vigente.

## Gerar e consultar

A partir da raiz, a versão lexical usa a biblioteca padrão:

```powershell
python -m search.ingest
python -m search.build_index --bm25-only
python -m search.export_web
python -m search.query "como priorizar demandas" --modo bm25 --k 3
```

`ingest.py` separa seções por títulos, ignora títulos dentro de blocos de código e conserva âncoras. `build_index.py` gera BM25. `export_web.py` produz JSON e script local; o script permite consulta pelo portal em arquivo local, sem fetch ou CDN. O contrato está em [SCHEMA](SCHEMA.md).

Cada resultado Python contém origem, seção, texto e score. `--json` emite saída estruturada. Exemplos e scores antigos foram substituídos pelo comando reproduzível acima; consultar a saída atual em vez de inferir sua relevância de um score ilustrativo.

## Caminho semântico opcional

```powershell
python -m pip install -r search/requirements.txt
python -m search.build_index
python -m search.query "priorização de backlog" --modo semantico
```

Esse caminho pode baixar o modelo configurado no código, `paraphrase-multilingual-MiniLM-L12-v2`. A disponibilidade exige embeddings, metadados, dependências e hash do corpus correspondente. Índice antigo não é combinado com corpus novo. Modo híbrido usa 0,6 da similaridade normalizada e 0,4 de BM25 normalizado, conforme implementação. Esses pesos são locais.

Sem o caminho semântico disponível, `hibrido` e `semantico` recorrem a BM25 com aviso. Não tratar fallback como validação de embeddings. A reforma gerou e verificou a saída lexical; não demonstra qualidade semântica em produção.

## API opcional e integrações

```powershell
python -m uvicorn search.api:app --host 127.0.0.1 --port 8765
```

- `GET /search?q=restauracao&k=3&modo=bm25` retorna consulta, modo efetivo e resultados.
- `GET /health` retorna estado, tamanho do corpus e modelo disponível.
- `http://127.0.0.1:8765/docs` apresenta OpenAPI.

Esta API de busca não implementa autenticação. A [API do núcleo](../server/README.md) possui autenticação opcional e também oferece consulta. Configure controles de acesso e limites no ambiente antes de exposição externa.

CLI, API e portal são três formas de consulta. O portal carrega `search-data.js`, usa pontuação lexical própria em `assets/search.js` e oferece origem, contexto, filtro e navegação à seção. Não é MiniSearch nem reproduz o ranking BM25 Python. O texto web é truncado em 800 caracteres por trecho, o que limita termos encontrados somente no restante da seção.

## Manutenção e limites

Reconstruir após editar fontes: `ingest → build_index → export_web`. `npm run build` faz a reconstrução lexical e as publicações locais. Caches, embeddings e dados privados seguem o ignore do projeto. Não indexar documentos históricos como vigentes apenas porque são mais extensos.

Se a consulta informar índice ausente, gerar os arquivos. Se importar `search` falhar, executar pela raiz com `python -m`, não de dentro da pasta. Usar aspas em caminhos com espaços e encoding UTF-8. Dependências FastAPI/Uvicorn e embeddings pertencem ao Python/ambiente de execução escolhido.

A busca recupera passagens; não verifica a veracidade de uma afirmação nem substitui leitura de suas fontes e limites. Testes conferem corpus canônico, âncoras e recuperação lexical, sem alegar qualidade semântica.

