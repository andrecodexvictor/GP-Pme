# GEAR — convenções do pacote ADK

Ao alterar regras do método, ler o [núcleo canônico](../../framework/README.md) e a prática afetada. Ao alterar instalação ou variáveis, conferir [README](README.md), `.env.example` e o código. Ao alterar adaptadores, ler `adapters/base.py` e executar testes dry-run. O código e seus contratos são a fonte dos nomes técnicos.

## Modelo e regras compartilhadas

O framework tem três domínios essenciais; adoção, indicadores, maturidade e IA opcional são transversais. Um orquestrador e oito especialistas são distribuição técnica de tarefas. Usar `framework/` como conteúdo vigente; referências antigas servem à proveniência.

Cálculos, questionário, cronograma e tarefas-semente pertencem a `server/core.py`. Delegar a essa camada quando a regra já existe; manter fonte, unidade e limite na resposta. Campos históricos permanecem por compatibilidade e recebem explicação quando o significado foi corrigido.

## Agentes e ferramentas

Cada diretório de agente expõe `root_agent` por seu `__init__.py`; o módulo define `INSTRUCTION`, descrição de roteamento, modelo configurável e ferramentas. Os especialistas importam o núcleo; o orquestrador importa os especialistas irmãos e as ferramentas de plataforma.

Instruções em português descrevem tarefa, contexto autorizado, fontes e critérios de saída. Produzir ações concretas e dado insuficiente quando a informação faltar. A resposta conserva evidências e identifica propostas locais. Revisão humana e decisão pertencem à autoridade do processo.

Docstrings descrevem comportamento executado e seus limites. Triagem por palavras é lexical; presença de títulos não valida requisitos. Dry-run é proposta registrada; não comprova efeito na plataforma. Instruções de geração não garantem ausência de erro do modelo.

## Adaptadores e efeitos externos

Implementar todos os métodos abstratos de `PlataformaGestao`. Credenciais são variáveis de ambiente. `GPPME_DRY_RUN=1` força simulação; ausência de credenciais também ativa esse modo. As ações planejadas conservam `dry_run` e dados de proposta, sem chamadas de rede.

No caminho real, conferir destino e autorização. HTTP usa `httpx` síncrono, timeout de 30 segundos e erros que possam ser tratados. O módulo de ferramentas mantém um quadro corrente; o estado é local ao processo e não oferece isolamento de múltiplas sessões concorrentes.

O quadro tem quatro colunas. O rótulo histórico “Em Andamento (máx 3)” é compatibilidade visual; WIP abrange itens iniciados por executor, incluindo teste e bloqueio. Usar informações de executor e início; campos ausentes limitam a conclusão. Emergências registram efeito sobre trabalho interrompido. Tarefas-semente vêm do núcleo, sem cópia divergente em cada adaptador.

## Verificação e manutenção

Python 3.10 ou superior para o pacote ADK; caminhos com `pathlib` e encoding UTF-8 explícito. Dependências vêm de `requirements.txt`. Os agentes consultam fontes e preparam saídas; este pacote não edita documentos do framework como parte da conversa.

Executar a suíte do projeto na raiz. A suíte original de adaptadores fica em `tests/test_adapters_dry_run.py` e roda a partir desta pasta. Testes locais verificam propostas, contratos e cálculos. Testes de funções extraídas por AST não comprovam carregamento do SDK ADK; chamadas reais exigem verificação específica com ambiente e credenciais válidos.

Registrar mudança de comportamento e compatibilidade no README. Conferir que docs, prompts, catálogo e busca remetem ao mesmo conteúdo vigente. MCPs deste usuário seguem o hub global; nenhuma instalação local por consequência.

