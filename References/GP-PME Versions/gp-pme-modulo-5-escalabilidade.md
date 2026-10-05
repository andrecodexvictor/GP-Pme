# GEAR: Rever carteira e dependências

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: **Autor**: Manus AI (sob a direção de Andre Victor) **Versão**: 2.1 (Modular Acadêmica com Implementação C) **Data**: 22 de Fevereiro de 2026

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Rever a carteira de iniciativas e serviços](#rever-a-carteira-de-iniciativas-e-servicos)
- [Registrar dados pessoais e responsabilidades](#registrar-dados-pessoais-e-responsabilidades)
- [Escolher e integrar ferramentas](#escolher-e-integrar-ferramentas)
- [Usar assistência por IA](#usar-assistencia-por-ia)
- [Maturidade com evidências](#maturidade-com-evidencias)

## Rever a carteira de iniciativas e serviços

Use quando projetos, serviços e custos precisarem ser comparados em conjunto. TI prepara registros; donos dos processos verificam uso e efeito; finanças confere custos; direção decide continuidade e recurso. Não é necessário esperar um nível de maturidade específico.

O módulo histórico de escalabilidade propunha revisão trimestral ou semestral. Essas são opções locais; escolher a janela conforme mudança, dependência e decisão necessária. Uma urgência pode exigir revisão anterior.

### Preparar a carteira

- Período, versão, responsável pela preparação e autoridade: [preencher]
- Objetivos de negócio e capacidade disponível: [preencher]
- Dados consultados e limitações de cobertura: [preencher]

| Iniciativa ou serviço | Dono e finalidade | Situação e evidência | Dependências e risco | Custo no período | Decisão necessária |
| --- | --- | --- | --- | --- | --- |
| [preencher] | | | | | |

Incluir operação, manutenção e compromissos existentes; uma carteira limitada a projetos novos pode esconder custo e dependência. Registrar benefício como hipótese ou resultado com evidência, evitando somar duas vezes capacidade liberada e sua entrega decorrente.

### Rever e decidir

1. Conferir quais itens atendem necessidade atual e quem usa seu resultado.
2. Identificar sobreposição, dependência e capacidade disputada. Dois sistemas parecidos podem ter requisitos distintos; a semelhança não autoriza encerramento.
3. Comparar continuar, ajustar, experimentar, adiar ou encerrar. Explicitar custo de transição, conservação de dados, alternativa de serviço e condição de retorno.
4. Conferir as hipóteses financeiras e suas sensibilidades. Retorno estimado favorável não elimina requisito de acesso, continuidade ou privacidade.
5. Registrar decisão, motivo, aprovador, executor, prazo e revisão. Se faltarem dados, atribuir a coleta e decidir o que pode seguir com segurança no recorte.

### Registro da decisão

| Campo | Registro |
| --- | --- |
| Item e alternativas consideradas | |
| Evidência, hipótese e lacunas | |
| Decisão e motivo | |
| Recurso e capacidade comprometidos | |
| Risco aceito e autoridade | |
| Transição, retorno e dados a conservar | |
| Executor, prazo e próxima conferência | |

### Mudança de arquitetura

O acervo associava crescimento a arquitetura evolutiva. Preservar a necessidade de conhecer dependências e custo de mudança; escolher arquitetura pela situação demonstrada. Um sistema monolítico não exige substituição automática por serviços distribuídos. Registrar o problema observável, opções, alteração mínima útil, riscos, teste e condição de retorno.

Saída: carteira com decisões localizáveis e pendências atribuídas. Concluir a revisão quando uso, custo, dependências e próximo passo estiverem explícitos para os itens discutidos. A revisão não comprova que todo investimento foi otimizado.

O formato é proposta local. A referência pública do COBIT apoia adaptação ao contexto [F09](<../../framework/referencias/fontes.md#f09>); não se afirma ter implantado integralmente APO05 ou validado esta tabela. Consulta: [indicadores financeiros](<../../framework/indicadores/financeiros.md>) e [responsabilidades](<../../framework/templates/responsabilidades.md>).


## Registrar dados pessoais e responsabilidades

Use quando um processo tratar dados pessoais ou uma mudança alterar sua coleta, acesso, compartilhamento ou conservação. Dono do processo descreve a finalidade; TI identifica sistemas e controles; a competência responsável por privacidade confere obrigações e alçadas. Direção decide recursos e riscos dentro de suas responsabilidades.

Este registro é uma adaptação local do tema de privacidade do módulo histórico de escalabilidade. Não demonstra conformidade nem substitui análise jurídica. O NIST Privacy Framework aparecia como referência no rascunho; seus detalhes não foram adotados sem consulta específica.

### Conhecer o tratamento

| Campo | Registro |
| --- | --- |
| Processo, responsável, data e versão | |
| Finalidade e pessoas cujos dados são tratados | |
| Categorias de dados e origem | |
| Hipótese legal e responsável por sua conferência | |
| Sistemas, fornecedores e compartilhamentos | |
| Quem decide o tratamento e quem o executa | |
| Acessos, controles e evidência de revisão | |
| Conservação, necessidade e condição de eliminação | |
| Atendimento de requisições do titular | |
| Exposições, consequências e pendências | |
| Resposta a incidente e competência responsável | |
| Próxima revisão e decisões registradas | |

O princípio da necessidade limita o tratamento ao mínimo necessário para sua finalidade, e o art. 7º prevê hipóteses legais além do consentimento. Portanto, obter consentimento não é uma solução universal para todo tratamento. Conferir a hipótese aplicável e requisitos específicos no contexto, inclusive quando houver dados sensíveis. [F15](<../../framework/referencias/fontes.md#f15>), arts. 6º e 7º.

O art. 37 trata do registro de operações do controlador e operador. Esta tabela ajuda a organizar informação; campos preenchidos não comprovam suficiência do registro legal ou execução dos controles. [F15](<../../framework/referencias/fontes.md#f15>), art. 37.

### Conferir a mudança

1. Identificar quais dados a tarefa realmente precisa e quais campos podem ser removidos.
2. Confirmar finalidade, responsabilidade e hipótese legal com a competência indicada.
3. Conferir acesso, compartilhamento, conservação, proteção e recuperação nas dependências conhecidas.
4. Preparar fluxo para requisições dos titulares, com pessoa responsável, canal e registro. O art. 18 reúne direitos e condições; uma instrução curta não substitui sua leitura aplicável. [F15](<../../framework/referencias/fontes.md#f15>)
5. Registrar teste dos controles pertinentes e pendências. A LGPD prevê medidas técnicas e administrativas de segurança desde a concepção até a execução do produto ou serviço. [F15](<../../framework/referencias/fontes.md#f15>), art. 46 e § 2º.
6. Submeter a decisão às pessoas com alçada e manter histórico após alteração relevante.

### Quando ocorrer um incidente

Acionar o plano e avaliar consequência para titulares, responsabilidade do controlador e obrigação de comunicação. O art. 48 trata de incidente que possa acarretar risco ou dano relevante aos titulares. A orientação da ANPD consultada informa prazo geral de três dias úteis, ressalvado prazo de legislação específica; regras de contagem, marco inicial e exceções exigem conferência do ato aplicável. “PME” do framework não comprova enquadramento jurídico especial. [F15](<../../framework/referencias/fontes.md#f15>), art. 48; [F16](<../../framework/referencias/fontes.md#f16>), perguntas 4–6.

IA pode preparar uma minuta com dados autorizados e minimizados. Não enviar dados pessoais ou segredos por conveniência, nem considerar classificação textual ou política gerada como prova de conformidade. A decisão sobre o uso das informações precisa de autoridade e condição de acesso.

Saída: registro revisado, controles verificados no recorte e pendências atribuídas. Concluir a preparação quando finalidade, dependências, responsabilidade e próxima ação estiverem localizáveis; a avaliação legal continua sob a competência apropriada. Modelos relacionados: [inventário](<../../framework/templates/inventario-dependencias.md>) e [incidente](<../../framework/templates/incidente.md>).


## Escolher e integrar ferramentas

Use quando a rotina precisar de suporte tecnológico ou a ferramenta atual limitar registro, proteção, recuperação ou entrega. TI verifica requisitos e operação; usuários testam o fluxo; finanças confere custos; direção decide contratação e risco. A escolha começa pela tarefa e sua evidência de conclusão.

Este guia é uma proposta local consolidada do apêndice de ferramentas de fevereiro de 2026. Os nomes de produtos abaixo preservam o catálogo histórico; não confirmam preços, planos, funcionalidades atuais ou adequação ao ambiente. Antes de escolher, conferir documentação oficial e termos da versão candidata, referenciando o trecho utilizado.

### Definir o que a ferramenta precisa resolver

1. Registrar o problema, quem usa, volume, dados e condição de operação. Distinguir necessidade essencial de conveniência.
2. Verificar o que já existe. Um registro consultável pode atender a gestão; proteção de contas e recuperação exigem controles tecnológicos apropriados.
3. Definir critérios observáveis: tarefa concluída, permissões corretas, dados recuperáveis e acompanhamento possível. Informar dispositivo, carga, rede e recorte do teste.
4. Comparar poucas alternativas com a mesma base de custo e operação. Incluir implantação, treinamento, integração, manutenção, suporte, recorrência e saída.
5. Executar um piloto autorizado com dados adequados. Registrar erros, esforço de operação e limitações, incluindo indisponibilidade e exportação quando pertinentes.
6. Propor a decisão com evidências e pendências. Contratação, integração com dados reais e alteração de acesso têm alçada própria.

### Comparação copiável

| Critério | Necessidade local | Alternativa e evidência | Lacuna ou custo |
| --- | --- | --- | --- |
| Uso e acessibilidade | [tarefa, usuários, dispositivo] | | |
| Dados e permissões | [dados autorizados, acesso, registro] | | |
| Continuidade | [retenção, recuperação, dependências] | | |
| Integração | [entrada, saída, formato, erro] | | |
| Custo total | [horizonte e componentes] | | |
| Operação e suporte | [responsável, atualização, atendimento] | | |
| Crescimento | [volume e restrição observável] | | |
| Saída | [exportação, substituição, encerramento] | | |

Um plano gratuito ou trial pode exigir tempo, infraestrutura e mudança futura de contrato. Código aberto também exige instalação, atualização e operação. A análise financeira usa [custos e hipóteses](<../../framework/indicadores/financeiros.md>), sem afirmar ROI por categoria ou marca.

### Catálogo histórico por tarefa

| Tarefa | Nomes citados no acervo | Conferência necessária |
| --- | --- | --- |
| Quadro e portfólio | Trello, Asana, Miro, quadro físico | Estados, responsáveis, capacidade, histórico e acesso |
| Comunicação e registro | Slack, Microsoft Teams, WhatsApp Business | Captura consultável, permissões, retenção e escalonamento |
| Orientação recorrente | ManyChat, Dialogflow, bots nativos | Conteúdo mantido, resolução confirmada e encaminhamento humano |
| Planilha e painel | Google Sheets, Microsoft Excel, Looker Studio, Power BI | Origem, janela, permissões e atualização dos dados |
| Inventário | Planilhas, CMDB simplificada, Snipe-IT | Cobertura, proprietário, revisão e dependências |
| Cópia e transferência | Google Drive, OneDrive, Veeam Backup & Replication, rsync | Retenção, separação, proteção e restauração; sincronização não comprova backup |
| Verificação técnica autorizada | OpenVAS, Nmap Scripting Engine, OWASP ZAP | Escopo autorizado, impacto, aplicabilidade dos achados e revisão especializada |
| Código e colaboração | GitHub, GitLab, Bitbucket | Histórico, permissões, revisão e recuperação |
| Desenvolvimento | VS Code, PyCharm, GitHub Copilot, Codeium | Ambiente, dependências, autorização dos dados e revisão de código |
| Testes | Selenium, Playwright, Pytest | Critérios, ambiente, resultado e limites da cobertura |
| Assistência opcional | Gemini, ChatGPT, Claude, OpenAI API, Google AI Studio, Anthropic API | Dados autorizados, modelo, custo, erro e revisão humana |
| Privacidade e documentação | OneTrust, DataGrail, Confluence, Notion, Google Docs | Registros de tratamento, acesso, direitos, revisão e conservação |

“Google Data Studio” era o nome usado em parte do catálogo; “Looker Studio” também aparecia entre parênteses. Os demais nomes são os declarados nos rascunhos, podendo ter mudado. O catálogo serve à recuperação documental, sem preferência comercial ou lista de requisitos do GEAR.

### Integrar de modo verificável

Descrever sistema de origem, destino, dados, identidade, permissão, frequência e responsável. Definir o que acontece quando a operação falha ou é repetida: como detectar, registrar, corrigir e evitar duplicidade no recorte. Testar a exportação e a condição de retorno quando a integração puder comprometer dados ou serviço.

Automação precisa de código, ferramenta registrada, credenciais apropriadas e observação do resultado. Um prompt não implementa API, monitoramento, chatbot ou teste de restauração. A geração de script é uma minuta de código a revisar; execução e efeito precisam de registros próprios.

### Encerrar a escolha

Saída: decisão com requisito, alternativas, custo no período, evidência de teste, aprovador, responsável pela operação e pendências. Concluir a escolha quando o motivo puder ser conferido e houver condição de operação e revisão. Se nenhuma alternativa atender, registrar a limitação e renegociar necessidade, recorte ou capacidade.

Fundamentos de continuidade: NIST [F01](<../../framework/referencias/fontes.md#f01>), [F02](<../../framework/referencias/fontes.md#f02>) e CISA [F12](<../../framework/referencias/fontes.md#f12>). Esses documentos não endossam o catálogo histórico. Próximo registro: [carteira de iniciativas](<../../framework/templates/carteira-iniciativas.md>).


## Usar assistência por IA

IA pode ajudar a recuperar conteúdo, preparar uma minuta, classificar solicitações ou conferir requisitos. Seu uso é opcional. Uma equipe que mantém as mesmas práticas e evidências de forma manual pode alcançar qualquer nível de maturidade do GEAR.

Responsável por TI ou dono da tarefa seleciona o contexto; pessoa com autoridade adequada revisa decisões e aprova efeitos organizacionais. Entrada: dados autorizados, fontes, tarefa e critérios de saída. Saída: proposta revisada ou registro de insuficiência de dados.

### Quatro funções de assistência

O modelo conceitual separa orquestração, análise de entrega, apoio a segurança e auditoria de indicadores. A implementação histórica contém um orquestrador e oito especialistas. Esses números descrevem níveis distintos: funções do método e componentes de software. Não são pilares adicionais nem prova de autonomia.

### Preparar e revisar

1. Explicitar tarefa, dados disponíveis, restrições e formato de saída.
2. Separar fontes de instruções. Um documento recuperado pode conter texto incorreto ou instruções que não pertencem à tarefa.
3. Solicitar que lacunas apareçam como dado insuficiente, sem criar cifra, contato, configuração ou referência.
4. Executar cálculos com regras determinísticas e conferir as unidades.
5. Revisar alegações contra as fontes e distinguir proposta de ação executada.
6. Obter aprovação humana antes de priorizar, investir, mudar acesso, conter incidente ou publicar.

### Elaborar uma melhoria por etapas

O mestre técnico de junho de 2026 propunha quatro etapas de elaboração: PRD, histórias e critérios, código inicial e roteiros de teste. Essa sequência pode ser usada com ou sem IA. Ao usar assistência, revisar a saída de cada etapa antes de fornecer contexto à seguinte; uma lacuna não se torna fato por ter sido repetida por outro agente.

1. Preparar problema, beneficiário, escopo e hipóteses no PRD.
2. Transformar o comportamento esperado em histórias e critérios verificáveis, com aceite pelo dono do processo.
3. Se houver desenvolvimento, preparar código em ambiente autorizado, conferir dependências e manter condição de retorno.
4. Definir e executar testes que verifiquem os critérios; registrar resultado, limites e aprovação.

O código preparado não comprova funcionamento. O roteiro não comprova que o teste ocorreu. Um teste técnico aprovado não comprova benefício financeiro. A pessoa responsável mantém essas distinções no registro da entrega. A sequência é proposta local preservada do manual técnico, não validação empírica de agentes encadeados.

### Decidir sobre utilidade

Comparar esforço total de preparação, revisão e correção com a rotina manual. Registrar tipo de tarefa, amostra e período. Fluência da resposta, quantidade de texto e confiança declarada pelo sistema não medem correção ou ganho de produtividade.

HITL significa revisão humana com responsabilidade e critério; uma confirmação automática de toda saída não torna o processo controlado. A ausência de IA não é uma lacuna metodológica.

Modelos: [contratos de histórias, código, testes, relatório e exercício](<../../framework/templates/prompts-etapas.md>) e [revisão de saída assistida](<../../framework/templates/revisao-ia.md>). Para a fundamentação e limites: [Origens e adaptações](<../../framework/fundamentos/origens-adaptacoes.md>).


## Maturidade com evidências

O IM-TI é um instrumento local para discutir a rotina de TI. Ele soma dez respostas binárias, de 0 a 10. Não é escala validada cientificamente, certificação ou comparação confiável entre empresas com contextos diferentes. Seu uso principal é encontrar lacunas e acompanhar a mesma organização ao longo do tempo.

### Aplicar o questionário

TI e dono do processo respondem juntos. Marcar 1 somente quando a prática ocorre e existe evidência consultável; marcar 0 quando ausente ou insuficiente. Registrar “não verificado” na observação quando faltar informação, contabilizando 0 provisoriamente. Não excluir perguntas para elevar a pontuação.

| Nº | Prática a verificar | Evidência possível |
| --- | --- | --- |
| 1 | Demandas têm registro oficial e responsável | Amostra da fila com solicitante e executor |
| 2 | Trabalho iniciado respeita a capacidade definida, incluindo testes e bloqueios | Quadro com testes, bloqueios e exceções |
| 3 | Orientações recorrentes são mantidas e verificadas | Instrução revisada por usuário, com responsável |
| 4 | Negócio e TI decidem prioridades em revisão registrada | Decisão com motivo, alçada e prazo |
| 5 | Melhorias têm problema, escopo e aceite acordados | PRD curto e verificação pelo dono do processo |
| 6 | Ativos e dependências críticos estão identificados | Inventário com proprietário e criticidade |
| 7 | Recuperação foi testada na janela combinada | Registro de restauração e limitações |
| 8 | Acessos críticos são controlados e revistos | Revisão de privilégios, MFA e exceções |
| 9 | Indicadores usados têm origem, período e revisão | Registro de dados e decisão vinculada |
| 10 | Decisões e mudanças passam por revisão responsável | Aprovação, verificação e correção registradas |

Nenhuma pergunta exige chatbot, agente, modelo generativo ou percentual de automação. O nível máximo pode ser alcançado com procedimentos manuais e controles tecnológicos apropriados.

### Interpretar sem ocultar lacunas

| IM-TI | Nível descritivo | Próxima ação típica |
| --- | --- | --- |
| 0–2 | 0: rotina pouco visível | Identificar responsáveis e registrar demandas |
| 3–5 | 1: organização inicial | Verificar continuidade e critérios de aceite |
| 6–8 | 2: práticas repetidas | Investigar lacunas e dependências entre práticas |
| 9 | 3: rotina acompanhada | Rever qualidade das evidências e resultados |
| 10 | 4: práticas verificadas | Manter a revisão e adequar o método ao contexto |

As faixas são convenções locais preservadas para continuidade do instrumento. As perguntas desta edição foram revistas: resultados antigos não são diretamente comparáveis sem reaplicação. As faixas não indicam probabilidade de ataque, retorno financeiro ou superioridade organizacional. Uma organização com pontuação alta e restauração não testada continua exposta.

### Decidir uma transição

Comparar a aplicação atual à anterior na mesma janela de evidência. Registrar o que passou a ocorrer, quem verificou e o que permanece incerto. O score pode mudar imediatamente; a **transição sustentada** exige observar a prática na rotina, por um período acordado. Não declarar avanço automático no dia 30.

Selecionar até três ações de melhoria por impacto e capacidade. Manter o resultado por pergunta junto ao total. Se uma resposta for contestada, revisar a evidência e corrigir o histórico, sem apagar a avaliação anterior.

Responsável pela aplicação: TI. Responsável pela validação de efeitos no negócio: dono do processo. Direção aceita recursos e riscos conforme a alçada. Modelo: [Registro de maturidade](<../../framework/templates/maturidade.md>).

Para planejar uma melhoria específica, consultar as [fichas por domínio](<../../framework/adocao/fichas-maturidade.md>). Elas preservam a matriz detalhada das versões anteriores como opções de desenvolvimento, sem acrescentar condições ao IM-TI.

Anterior: [Primeiros 30 dias](<../../framework/adocao/primeiros-30-dias.md>). Para compreender: [Fundamentos e adaptações](<../../framework/fundamentos/origens-adaptacoes.md>).


## Rever riscos de adoção

Resistência, sobrecarga inicial, pouco uso dos registros e expectativas indevidas são riscos de aplicação presentes no acervo. TI e direção escolhem um recorte dentro da capacidade, explicam o acordo e observam o uso com as pessoas afetadas. Treinamento e gamificação não garantem adesão. Ajustar ferramenta ou registro quando o esforço não apoiar uma decisão.

Falta de direção exige alçada e decisão identificáveis; reunião sem decisão não resolve a lacuna. Requisitos ambíguos exigem conversa e critério testável. Falsa sensação de segurança exige conferir cobertura e teste; política ou compra não prova proteção. Biblioteca desatualizada exige curadoria somente se houver uso de assistência. Registrar dono, ação, evidência e próxima revisão para cada risco relevante.

Os percentuais, prazos e gates das versões anteriores eram propostas locais sem validação. Segurança urgente não espera nível de maturidade, implantação de quadro ou conclusão de outro módulo. A revisão de aplicação real continua necessária; testes deste repositório não comprovam efetividade organizacional.


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
