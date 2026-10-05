# GEAR: Escolher ferramentas

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: **Autor**: Manus AI (sob a direção de Andre Victor) **Versão**: 2.1 (Modular Acadêmica com Implementação C) **Data**: 22 de Fevereiro de 2026

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Escolher e integrar ferramentas](#escolher-e-integrar-ferramentas)
- [Rever a carteira de iniciativas e serviços](#rever-a-carteira-de-iniciativas-e-servicos)
- [Registrar dados pessoais e responsabilidades](#registrar-dados-pessoais-e-responsabilidades)

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


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
