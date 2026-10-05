# GEAR: Manual técnico completo

Framework de governança e gestão de TI para pequenas e médias empresas.

Edição editorial: GEAR 2026.10, 05/10/2026. Origem: GP-PME 6.0, 02/06/2026. Crédito declarado na versão de origem: Antigravity AI, sob a direção de Andre Victor. Direitos conforme LICENSE.md; a revisão não altera permissões. O caminho anterior foi mantido para compatibilidade.

Esta versão conserva um manual completo para seu público. Regras compartilhadas são derivadas das fontes modulares vigentes; as contribuições próprias dos mestres foram incorporadas aos fundamentos e ao guia de assistência. A preservação da versão de origem e o mapa de seções constam da matriz de proveniência em `.context/gear-execution/`.

## Percurso de leitura

- [Escopo e princípios](#escopo-e-principios)
- [Governança e direção](#governanca-e-direcao)
- [Execução e serviços](#execucao-e-servicos)
- [Segurança e continuidade](#seguranca-e-continuidade)
- [Indicadores operacionais](#indicadores-operacionais)
- [Indicadores financeiros e hipóteses](#indicadores-financeiros-e-hipoteses)
- [Usar assistência por IA](#usar-assistencia-por-ia)
- [Priorizar demandas de TI](#priorizar-demandas-de-ti)
- [Entregar uma melhoria pequena](#entregar-uma-melhoria-pequena)
- [Tratar um incidente](#tratar-um-incidente)
- [Testar restauração](#testar-restauracao)
- [Conduzir uma revisão de direção](#conduzir-uma-revisao-de-direcao)
- [Primeiros 30 dias](#primeiros-30-dias)
- [Maturidade com evidências](#maturidade-com-evidencias)
- [Origens, adaptações e evolução](#origens-adaptacoes-e-evolucao)
- [Glossário](#glossario)
- [Fontes e limites de uso](#fontes-e-limites-de-uso)

## Escopo e princípios

GEAR ajuda a direção e o responsável por TI a manter um ciclo de decisão: registrar uma necessidade, avaliar impacto e capacidade, atribuir responsabilidade, executar, verificar a saída e revisar o resultado. O recorte é a TI de pequenas e médias empresas, inclusive equipes internas reduzidas e serviços terceirizados.

### Problemas tratados

O framework aborda demandas dispersas, prioridades conflitantes, decisões sem responsável, trabalho iniciado sem capacidade disponível, controles de continuidade sem evidência e benefícios financeiros apresentados sem premissas. Esses são problemas de aplicação do método, não uma afirmação sobre toda PME.

Não substitui gestão contábil, obrigação legal, avaliação especializada de segurança ou um sistema completo de gestão empresarial. Um risco jurídico ou regulatório identificado deve ser encaminhado à competência responsável, em vez de receber uma resposta improvisada de TI.

### Princípios de aplicação

1. **Responsabilidade identificada.** Cada demanda e decisão têm executor e autoridade de aprovação. Uma pessoa pode acumular funções; o registro torna esse acúmulo visível.
2. **Adoção proporcional.** Ativar uma prática porque resolve uma necessidade observada. Rever complexidade, capacidade e manutenção antes de ampliar o método.
3. **Evidência antes de conclusão.** Uma política escrita, um backup concluído e um serviço restaurado são evidências diferentes. Registrar a que conclusão cada uma permite chegar.
4. **Fluxo visível.** Mostrar fila, trabalho iniciado, bloqueios e exceções. Um incidente não apaga o histórico do trabalho que interrompeu.
5. **Inspeção e adaptação.** Rever prioridades e hipóteses em uma cadência sustentável. Ajustes de duração e capacidade devem ter motivo registrado.
6. **Assistência opcional.** O núcleo pode ser operado com reunião, quadro e registros. IA pode preparar saídas; pessoas permanecem responsáveis pelas decisões.

### Núcleo, aplicação e explicação

O núcleo define termos e invariantes. Os guias explicam tarefas. Templates facilitam o registro. Fundamentos apresentam as adaptações e seus limites. Essa separação atende a necessidades distintas de documentação, seguindo a orientação Diátaxis. [F08](<../framework/referencias/fontes.md#f08>)

Uma equipe pode usar software de chamados, planilha ou quadro físico. O suporte escolhido precisa preservar responsável, situação, critério de conclusão e evidência. Operação manual significa independência de uma plataforma de gestão, não ausência de tecnologia para executar backup ou proteger contas.

### Situação da evidência

GEAR é uma composição autoral de práticas. Cenários demonstrativos e testes de software comprovam apenas o que efetivamente verificam. Metas de prazo, percentuais de melhoria e faixas de indicadores não são resultados médios esperados nem parâmetros normativos universais.

A avaliação acadêmica prevista utiliza casos sintéticos pareados. Até a produção de dados, o protocolo permanece prospectivo. Uma comparação com referências adaptadas precisa declarar escopo e condições de cada configuração, sem construir alternativas deliberadamente fracas.

Próxima leitura: [Governança e direção](<../framework/nucleo/governanca.md>). Para executar: [Primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>).


## Governança e direção

Este domínio conecta decisões de TI a necessidades do negócio e a riscos conhecidos. A direção define prioridades e autoriza recursos; o responsável por TI organiza a execução e apresenta evidências. A prática admite papéis acumulados, mas exige que cada decisão tenha uma autoridade identificada.

### Avaliar, dirigir e monitorar

O acervo chama o ciclo de **ADM-Lite**: avaliar, dirigir e monitorar. No GEAR, avaliar é examinar situação, alternativas, custos e riscos; dirigir é decidir prioridade, limites e responsabilidade; monitorar é confrontar a decisão com evidências e rever a ação.

Essa sigla local não designa o Architecture Development Method do TOGAF. A correspondência detalhada com ISO/IEC 38500 exige consulta à edição oficial; o conteúdo fechado não foi verificado na pesquisa que sustenta esta edição. A apresentação pública do COBIT oferece evidência de dimensionamento e adaptação da governança, sem validar o instrumento local. [F09](<../framework/referencias/fontes.md#f09>)

### Papéis e acordos

| Função | Responsabilidade | Evidência mínima |
| --- | --- | --- |
| Direção ou patrocinador | Autorizar prioridade, recurso e aceitação de risco | Decisão com data e condição de revisão |
| Responsável por TI | Preparar alternativas e conduzir a execução | Registro de demanda, responsável e situação |
| Dono do processo de negócio | Explicar impacto e validar a entrega | Critério de aceite e confirmação da saída |
| Usuário afetado | Informar necessidade e efeito percebido | Solicitação e feedback contextualizados |

Um técnico terceirizado pode executar sem poder aprovar orçamento. Um proprietário pode ser também dono de processo. Quando o executor é o aprovador, registrar a limitação e buscar revisão de outra pessoa em ações de maior impacto, conforme os controles já existentes na organização.

Use a [matriz de responsabilidades](<../framework/templates/responsabilidades.md>). RACI-Lite é um suporte de registro: R executa; A aprova; C é consultado; I é informado. Não precisa criar cargos adicionais.

### Matriz de quatro finalidades

A Matriz 4 Quadrantes relaciona iniciativas a receita, custos, experiência e resiliência. Uma iniciativa pode ter finalidade principal e efeitos secundários. A classificação não garante benefício: precisa de hipótese, medida e responsável.

Antes de aprovar, perguntar: qual problema observável será tratado; quem recebe o resultado; que condição indicará conclusão; qual recurso será comprometido; que risco permanece; que alternativa é viável? Uma proposta sem essas informações volta para refinamento ou tem a lacuna explicitada na decisão.

### Revisão de direção

CD-TI Lite é o nome histórico da revisão de direção. Uma reunião quinzenal de 30 minutos é o ponto de partida do método, não uma duração obrigatória para toda empresa. A pauta pode reservar cinco minutos para indicadores, quinze para demandas, cinco para riscos e cinco para decisões. Uma emergência pode exigir uma decisão fora dessa cadência.

Registrar decisão, alternativas consideradas, motivo, responsável, prazo e evidência esperada. Comunicar às pessoas afetadas o que mudou e qual canal usar. O registro de conflito entre negócio e TI evita que uma discordância fique escondida sob um status de tarefa.

### Critério de funcionamento

O domínio está operacional quando decisões relevantes têm autoridade, justificativa e acompanhamento, e quando a equipe consegue localizar o acordo vigente. A quantidade de atas produzidas não mede a qualidade da governança.

Para executar: [Conduzir uma revisão](<../framework/guias/conduzir-revisao.md>). Modelo: [Decisão e prioridades](<../framework/templates/decisoes-prioridades.md>).


## Execução e serviços

Este domínio organiza solicitações, incidentes e melhorias em um fluxo observável. O objetivo é compatibilizar capacidade e prioridade, registrando interrupções e critérios de conclusão. A combinação de práticas é própria do GEAR; não constitui uma implementação integral de Scrum ou ITIL. [F03](<../framework/referencias/fontes.md#f03>) [F10](<../framework/referencias/fontes.md#f10>)

### Entrada de demandas

Canal único significa **um registro oficial da fila**, com responsável e situação. Pode receber solicitações por formulário, e-mail ou integração. Um pedido recebido por outro meio deve ser registrado ou encaminhado; não se recusa uma emergência porque chegou por telefone.

Definir quem registra incidentes quando o solicitante não consegue acessar o canal. Informar como pedir ajuda e como acompanhar a resposta. Uma mudança de canal precisa de transição e comunicação para evitar demandas perdidas.

### Estados de trabalho

| Estado | O que representa | Condição para avançar |
| --- | --- | --- |
| A Fazer | Demanda ainda não iniciada | Prioridade, responsável e capacidade acordados |
| Em Andamento | Trabalho iniciado sob responsabilidade do executor | Saída preparada para verificação |
| Em Teste | Verificação técnica ou de negócio ainda pendente | Critério de aceite atendido e evidência registrada |
| Concluído | Saída aceita ou encerramento justificado | Motivo e evidência acessíveis |

Bloqueio e suspensão são atributos visíveis do cartão, com motivo e próxima ação. Não transformar trabalho iniciado em tarefa nova nem reiniciar seu relógio para melhorar uma métrica.

### Limite de trabalho em progresso

O ponto de partida é **até três itens iniciados por executor**, contando Em Andamento e Em Teste sob sua responsabilidade. Trabalho bloqueado permanece visível e conta enquanto mantém compromisso de capacidade. A equipe pode escolher limite menor ou revê-lo após observar capacidade e filas. Registrar exceções temporárias, motivo e prazo de revisão.

Esse número é um parâmetro local de adoção, sem validação universal. Em equipe de uma pessoa, três cartões no sistema não significam três atividades executadas ao mesmo tempo. A concentração do trabalho deve permanecer explícita.

### Cadência e entrega

Usar planejamento semanal curto para selecionar trabalho compatível com a capacidade e fazer uma verificação diária da fila. Revisar ao final do ciclo o que terminou, ficou bloqueado e mudou de prioridade. As durações históricas de 15, 5 e 15 minutos são referências iniciais de agenda.

Uma melhoria pequena pode ser planejada como um piloto de uma ou duas semanas. Definir escopo que caiba no período ou negociar sua alteração; o método não garante que qualquer MVP será concluído em duas semanas. A revisão precisa de usuário ou dono de processo, mesmo quando o desenvolvimento é feito por uma pessoa.

### Emergências

A raia rápida atende incidentes com impacto que justifique interrupção. Quem reconhece o incidente comunica a prioridade; o executor registra o trabalho suspenso e concentra a resposta. Se o limite for ultrapassado, documentar a exceção e a capacidade comprometida. Após recuperação, decidir quando retomar o item interrompido.

Um incidente precisa de condição de recuperação e comunicação aos afetados. Resolver o chamado e prevenir recorrência podem produzir tarefas distintas, ligadas pelo histórico.

Para executar: [Priorizar demandas](<../framework/guias/priorizar-demandas.md>), [tratar incidentes](<../framework/guias/tratar-incidentes.md>) e [entregar uma melhoria](<../framework/guias/entregar-melhoria.md>).


## Segurança e continuidade

Este domínio relaciona serviços críticos, controles e capacidade de recuperação. O conjunto inicial cobre inventário, identidade e acesso, cópias de segurança e resposta a incidentes. Ele é uma seleção autoral de práticas; não oferece proteção integral nem certificação de conformidade.

O NIST CSF 2.0 reúne seis funções: Governar, Identificar, Proteger, Detectar, Responder e Recuperar. O guia do NIST para pequenas empresas apresenta ações e perguntas aplicáveis a organizações com planos de cibersegurança modestos ou inexistentes. GEAR usa essa referência para organizar cobertura e lacunas. [F01](<../framework/referencias/fontes.md#f01>) [F02](<../framework/referencias/fontes.md#f02>)

### Serviço, ativo e dependência

Começar pelo serviço que precisa continuar, identificar seus dados, contas, equipamentos, fornecedores e responsáveis. Priorizar sistemas críticos não equivale a conhecer todos os ativos. O termo histórico “Inventário 80/20” é uma estratégia de início por criticidade, não a prova de que 20% dos ativos representam exatamente 80% do risco ou da receita.

Registrar o que ainda não foi inventariado, o responsável pela ampliação e como novas dependências entram no registro. Contas de nuvem e integrações também podem ser ativos relevantes.

### Controles e evidência

| Prática | Evidência útil | Limite da conclusão |
| --- | --- | --- |
| Inventário | Ativo, serviço, responsável, criticidade e revisão | Lista parcial não demonstra cobertura completa |
| Identidade e acesso | Contas individuais, acesso necessário, MFA e revisão | Um controle isolado não impede todo comprometimento |
| Cópias de segurança | Execução, retenção, separação e teste de restauração | Job concluído não prova recuperação do serviço |
| Resposta | Contatos, autoridade, passos e exercício do plano | Plano escrito não demonstra capacidade sob qualquer incidente |

A seleção local deve indicar quais resultados do CSF ela cobre, quais ficam pendentes e qual risco é aceito pela direção. O CSF não prescreve uma implementação única nem valida as metas numéricas do GEAR. [F02](<../framework/referencias/fontes.md#f02>)

### Recuperação

Definir com o dono do processo quanto tempo o serviço pode ficar indisponível e qual perda de dados é tolerável. Esses requisitos orientam retenção, frequência de cópia e teste. RTO é o objetivo de tempo de recuperação; RPO expressa a perda de dados tolerável em tempo. Registrar também dependências e recursos de restauração.

A regra 3-2-1 é um arranjo de cópias a avaliar, não sinônimo de backup testado. Sincronização de arquivos pode propagar alterações ou exclusões; verificar a retenção e o comportamento da solução antes de chamá-la de cópia recuperável. Um teste de arquivo prova um recorte; a restauração de um serviço exige suas dependências.

### Resposta proporcional

O Plano de Resposta a Incidentes identifica quem aciona, decide contenção, comunica e verifica recuperação. Ações concretas dependem do incidente e do ambiente. Não transformar uma lista curta em ordem universal de formatar equipamentos, desligar serviços ou apagar evidências.

Após o incidente, registrar causa conhecida ou hipótese, efeito, decisões e correções. A ausência de causa confirmada deve permanecer explícita. A equipe deve encaminhar investigação especializada quando o problema excede sua capacidade.

Para executar: [Testar restauração](<../framework/guias/testar-restauracao.md>) e [tratar incidentes](<../framework/guias/tratar-incidentes.md>). Modelo: [Risco e continuidade](<../framework/templates/risco-continuidade.md>).


## Indicadores operacionais

Escolha um indicador quando houver uma decisão a tomar. TI coleta os dados; o dono do serviço confirma o que foi medido; direção e TI definem tolerâncias. Uma meta sem janela, origem e responsável não permite avaliar a rotina.

### Definições

| Indicador | Cálculo e unidade | Limite de interpretação |
| --- | --- | --- |
| IDSC: disponibilidade de serviço crítico | `(horas observadas − horas indisponíveis) / horas observadas × 100`, em % | Definir serviço, horário coberto e exclusões; não somar incidentes simultâneos duas vezes |
| TMpR: tempo médio para restauração | Soma dos tempos de recuperação / incidentes encerrados, em horas | Informar quantidade e distribuição; a média pode ocultar um incidente longo |
| ISU: satisfação do usuário | Soma das notas / respostas válidas, em escala 1 a 5 | Informar taxa de resposta e pergunta; ausência de respostas é dado insuficiente |
| Trabalho iniciado | Quantidade por executor em andamento, teste ou bloqueio | Não confundir tamanho da fila com WIP |
| Tempo de fluxo | Conclusão menos início, na unidade escolhida | Informar política de pausa e itens ainda abertos |

### Coletar e revisar

1. Definir decisão e serviço: por exemplo, se a recuperação atende à necessidade do faturamento.
2. Escolher período e fonte. Preservar horários e identificador do incidente.
3. Validar domínios: horas observadas positivas, indisponibilidade entre zero e o período; duração não negativa; notas de 1 a 5.
4. Calcular e informar amostra, lacunas e exclusões.
5. Comparar com tolerância local e períodos comparáveis.
6. Registrar ação, responsável e data de revisão.

Sem incidentes encerrados, TMpR é **dado insuficiente**, não zero. Um período sem incidentes registrados pode indicar falta de coleta. Indicadores não substituem testes de restauração nem a avaliação de riscos.

### Metas e compatibilidade

As versões anteriores usavam disponibilidade >99,5%, TMpR <4 horas e ISU >4,5. São exemplos de metas locais, sem validade universal. A calculadora mantém esses padrões para compatibilidade e permite configuração; o resultado deve declarar as metas aplicadas. Igualdade no limite não satisfaz uma comparação estrita.

### DORA para entrega de software

As métricas DORA consultadas em 2026 são frequência de implantação, tempo de entrega de mudanças, tempo de recuperação de implantação com falha, taxa de falha de mudanças e taxa de retrabalho de implantação. Seu recorte é entrega de software. Não substituir TMpR de incidentes gerais pelo tempo de recuperação de uma implantação com falha. Consultar definições e contexto antes de incorporar uma métrica [F05](<../framework/referencias/fontes.md#f05>), [F06](<../framework/referencias/fontes.md#f06>).

Exemplo: 720 horas observadas e 2 horas de indisponibilidade produzem IDSC de 99,7222%. Dois incidentes restaurados em 1 e 3 horas produzem TMpR de 2 horas. Duas respostas 5 e 4 produzem ISU de 4,5; a amostra é pequena e não prova satisfação de todos.

Próxima leitura: [Indicadores financeiros](<../framework/indicadores/financeiros.md>). Modelo: [Decisões e prioridades](<../framework/templates/decisoes-prioridades.md>).

Consulta complementar: [indicadores de negócio e comparação da rotina](<../framework/indicadores/negocio-comparacao.md>), com definições para custos, canais, entregas e autoatendimento.


## Indicadores financeiros e hipóteses

Use estas convenções para discutir uma melhoria, seu custo e suas premissas. TI estima esforço e dependências; finanças confere valores; o dono do processo verifica o benefício; direção decide. Todos os valores devem estar na mesma moeda e base de preços, com período declarado.

### Não confundir as medidas

| Medida | Fórmula | Significado |
| --- | --- | --- |
| Razão benefício/investimento | `B / I` | Quantas unidades de benefício bruto estimado correspondem a uma unidade investida |
| ROI líquido no período | `(B − C − I) / I × 100` | Retorno após investimento e custos recorrentes do período |
| Payback simples | `I / (b − c)` | Meses para recuperar investimento, se benefício e custo mensais constantes e benefício líquido positivo |
| Economia potencial de capacidade | `horas liberadas × custo por hora` | Valor atribuído ao tempo; pode não reduzir despesa paga |
| DAN financeiro local | `custo estimado de refatoração / orçamento anual de TI` | Peso de uma estimativa de dívida sobre o orçamento; sem faixas universais |
| Proporção de itens legados | `itens legados / itens totais` | Composição do inventário; não mede custo de refatoração |

`I` é investimento inicial positivo; `B` e `C` são benefício bruto e custo recorrente no período; `b` e `c` são seus valores mensais. Escrever “400% de ROI” para `B/I × 100` confunde razão bruta e retorno líquido.

### Exemplo calculado

Investimento de R$ 9.000; benefício bruto estimado de R$ 3.000/mês; custo recorrente de R$ 500/mês; horizonte de 12 meses. Benefício bruto anual: R$ 36.000. Custo recorrente anual: R$ 6.000. Razão benefício/investimento: 4. ROI líquido anual: `(36.000 − 6.000 − 9.000) / 9.000 × 100 = 233,33%`. Payback simples: `9.000 / 2.500 = 3,6 meses`.

Sem custo recorrente, o mesmo cenário tem ROI líquido de 300% e razão bruta de 4, equivalente a 400% do investimento. São resultados condicionais de uma conta, não retorno observado do GEAR.

### COT e tempo liberado

COT significa **Custo de Otimização Tecnológica** nesta edição. Registrar o investimento inicial, seus componentes e os custos de operação separadamente. Não usar COT como sinônimo de custo de oportunidade ou como fórmula de ROI.

Se uma automação libera 20 horas por mês a R$ 50/hora, há R$ 1.000/mês de capacidade potencial. Para tratá-la como redução de despesa, demonstrar uma alteração efetiva de gasto ou contratação. Se as horas forem realocadas, medir a nova entrega, sem contar simultaneamente capacidade e receita derivada como benefícios independentes.

### Sensibilidade e decisão

Apresentar cenários conservador, central e favorável variando adoção, benefício, manutenção e investimento. Se o benefício líquido mensal for zero ou negativo, não há payback simples finito. A fórmula não contempla inflação, tributos, risco, valor do dinheiro no tempo ou fluxos irregulares; investimentos que dependem desses fatores exigem análise financeira apropriada.

DAN financeiro exige estimativa explicada: sistema, escopo de correção, método, data e incerteza. Uma proporção de 30% de itens legados não demonstra DAN financeiro de 0,30 nem risco de falência. A API antiga mantém faixas abaixo de 0,15, de 0,15 a 0,35 e acima de 0,35 apenas como critérios locais da proporção de inventário, explicitamente rotulados. Outras versões usavam limites diferentes; nenhum deles foi validado como limiar financeiro.

Saída: memória de cálculo, fonte das premissas, responsável e decisão. Evidência de conclusão: finanças e dono do processo conferiram unidades e hipóteses. Estas fórmulas são convenções locais; não há atribuição ao NIST, COBIT ou ITIL.

Os guias antigos também atribuíam a DAN ao ATDx e o ROI do COT à dívida de arquitetura empresarial. ATDx normaliza violações por elementos de código e usa análise estatística; Hacks et al. propõem uma definição contextual com casos fictícios. Esses textos apoiam conceitos de dívida arquitetural, mas não as fórmulas financeiras ou faixas do GEAR. [F13](<../framework/referencias/fontes.md#f13>) [F14](<../framework/referencias/fontes.md#f14>)

Anterior: [Indicadores operacionais](<../framework/indicadores/operacionais.md>). Aplicação: [Caso didático](<../framework/exemplos/caso-didatico.md>).


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

Modelos: [contratos de histórias, código, testes, relatório e exercício](<../framework/templates/prompts-etapas.md>) e [revisão de saída assistida](<../framework/templates/revisao-ia.md>). Para a fundamentação e limites: [Origens e adaptações](<../framework/fundamentos/origens-adaptacoes.md>).


## Priorizar demandas de TI

Este guia ajuda a transformar pedidos concorrentes em uma fila com decisões e capacidade visíveis. Use quando solicitações chegam por vários meios, a equipe inicia mais trabalho do que consegue encerrar ou o negócio discorda da ordem de atendimento.

Responsável pela preparação: responsável por TI. A direção ou autoridade delegada decide conflitos que comprometem recursos, prioridades de negócio ou risco. Entrada: demandas registradas, capacidade disponível, serviços afetados e acordos existentes. Saída: fila ordenada, itens selecionados, responsáveis e motivos.

### Preparar o registro

Para cada demanda, registrar solicitante, necessidade, serviço afetado, consequência de adiar, prazo real, responsável e condição de conclusão. “Urgente” sem consequência identificada é informação insuficiente para decidir prioridade.

Uma solicitação incompleta permanece na fila como “aguardando informação”, com quem fornecerá o dado. Um incidente crítico recebe tratamento imediato e registro assim que viável. O canal único não é uma barreira ao acesso de quem está com o sistema indisponível.

### Executar a priorização

1. Separar recuperação de serviço, atendimento recorrente e melhoria planejada. Demandas de naturezas distintas podem exigir critérios e prazos diferentes.
2. Avaliar impacto, urgência e dependências. Usar as quatro finalidades de negócio para explicar valor, sem somar notas arbitrárias como se fossem medidas objetivas.
3. Conferir itens iniciados, incluindo teste e bloqueio. O limite inicial é três por executor; reduzir quando a capacidade disponível exigir.
4. Selecionar trabalho para o próximo ciclo e obter a decisão da autoridade responsável quando houver conflito.
5. Registrar ordem, decisão, responsável e critério de conclusão. Comunicar ao solicitante o próximo passo, inclusive quando a demanda foi adiada.

### Tratar exceções

Um incidente com interrupção relevante pode usar a raia rápida. Tornar visível o item suspenso, sua dependência e a revisão de prazo. Não devolvê-lo à fila como se nunca tivesse sido iniciado.

Se há várias emergências, a direção decide qual serviço recebe a capacidade limitada e quem comunica as consequências. Um limite de WIP sozinho não resolve essa escolha.

### Exemplo ilustrativo

Uma equipe de uma pessoa recebe pedido de relatório gerencial, erro que impede faturamento e troca de assinatura de e-mail. O incidente de faturamento recebe a primeira resposta porque há serviço indisponível. O relatório fica planejado após confirmar seu prazo e dono do processo. A assinatura entra na fila comum. A ordenação precisa do impacto observado; o exemplo não fixa uma prioridade universal para esses tipos de pedido.

### Encerrar

A priorização terminou quando cada item selecionado tem executor e critério de saída, itens adiados têm motivo e a equipe conhece a capacidade comprometida. Na revisão seguinte, confrontar decisão e efeito. Não avaliar sucesso pela quantidade de cartões iniciados.

Modelo: [Decisão e prioridades](<../framework/templates/decisoes-prioridades.md>). Referência: [Execução e serviços](<../framework/nucleo/execucao-servicos.md>). Próxima tarefa: [Entregar uma melhoria](<../framework/guias/entregar-melhoria.md>).


## Entregar uma melhoria pequena

Use para uma alteração de TI com resultado verificável por um processo de negócio. Responsável por TI prepara a solução; dono do processo define e verifica o aceite; direção aprova recursos e riscos conforme a alçada. Entrada: necessidade, situação atual, restrições e capacidade. Saída: mudança verificada, registro de aceite e efeito a acompanhar.

### Delimitar

Registrar problema, beneficiário, escopo, exclusões e condição de sucesso em um PRD curto. Uma ou duas semanas podem ser o intervalo de um piloto; se o escopo não couber, reduzir a entrega ou negociar outro prazo. A duração não substitui uma estimativa de capacidade.

Um requisito pode usar “Dado/Quando/Então”: dado um pedido autorizado, quando o relatório é solicitado, então os campos definidos aparecem sem edição manual. Esse exemplo descreve comportamento esperado, não afirma que a solução já foi implementada.

### Executar

1. Conferir dados, permissões, integrações e dependências.
2. Definir executor e quem aceitará a saída.
3. Registrar critério de verificação, risco e retorno à condição anterior.
4. Selecionar trabalho compatível com a fila e seu limite.
5. Construir e testar o recorte acordado.
6. Verificar com o usuário ou dono do processo; registrar aceite ou correções.
7. Acompanhar a hipótese de benefício na janela definida.

### Aprender com a entrega

Uma solução aceita pode não produzir o benefício esperado. Medir uso, efeito e esforço de manutenção. Se a hipótese falhar, registrar o resultado e decidir adaptar ou interromper, sem reclassificá-lo como sucesso apenas porque houve implementação.

As práticas de inspeção e adaptação são compatíveis com a inspiração ágil; retirar elementos de Scrum impede chamar qualquer ciclo curto de implementação integral desse framework. [F03](<../framework/referencias/fontes.md#f03>)

Modelo: [PRD e aceite](<../framework/templates/prd-aceite.md>). Próxima tarefa: [Conduzir uma revisão](<../framework/guias/conduzir-revisao.md>).


## Tratar um incidente

Use quando há interrupção de serviço ou suspeita de comprometimento que exige coordenação. A pessoa que recebe o relato inicia o registro; a autoridade definida no plano decide contenção e comunicação; o executor técnico verifica a recuperação. Entrada: relato, serviços afetados, contatos e plano vigente. Saída: serviço recuperado ou alternativa acordada, decisões registradas e ações posteriores identificadas.

### Reconhecer e avaliar

Registrar momento de identificação, sinais observados, serviço e usuários afetados. Distinguir fato de hipótese. “Sistema indisponível” é observação; “ataque de ransomware” exige evidência adicional. A falta de certeza não impede acionar o responsável.

Estimar impacto e comunicar à autoridade competente. Se o caso excede a capacidade local, acionar fornecedor ou especialista conforme os contatos do plano. A pessoa afetada não precisa preencher um formulário inacessível para receber ajuda.

### Conduzir a resposta

1. Identificar quem coordena e como a equipe atualizará a situação.
2. Registrar prioridades, trabalho suspenso e exceção de capacidade.
3. Avaliar contenção apropriada ao ambiente e preservar informações necessárias à investigação. Não aplicar formatação ou desligamento como regra automática.
4. Comunicar estado e alternativa operacional aos afetados, evitando declarar causa não confirmada.
5. Recuperar a partir de uma condição conhecida e verificar serviço, dados e dependências com o dono do processo.
6. Registrar horários, decisões, evidências e necessidade de acompanhamento.

As seis funções do CSF articulam governança, identificação, proteção, detecção, resposta e recuperação; elas não oferecem um único roteiro de ações técnicas para todo incidente. [F01](<../framework/referencias/fontes.md#f01>) [F02](<../framework/referencias/fontes.md#f02>)

### Verificar recuperação

Confirmar que o processo necessário funciona e que a equipe conhece restrições temporárias. O desaparecimento de uma mensagem de erro não é suficiente para encerrar. Se uma alternativa foi adotada, declarar se o serviço original segue pendente.

O relógio de resolução começa no registro definido para a métrica e termina na condição de encerramento acordada. Registrar também o momento de identificação quando diferente. Não excluir incidentes longos de um indicador sem mostrar o critério.

### Rever e prevenir recorrência

Preparar revisão proporcional: o que ocorreu, quais decisões ajudaram, onde faltou informação e qual ação tem responsável. Correção definitiva pode ser uma melhoria vinculada ao incidente. “Causa ainda não confirmada” é uma conclusão válida, com próximo passo.

Modelo: [Plano de resposta](<../framework/templates/incidente.md>). Próxima tarefa: [Testar restauração](<../framework/guias/testar-restauracao.md>).


## Testar restauração

Este guia verifica um recorte definido da capacidade de recuperar dados ou um serviço. Use antes de depender de um backup, após alteração relevante da solução e na cadência acordada para o serviço. Responsável técnico prepara o teste; dono do processo valida a saída. Entrada: cópia disponível, ambiente apropriado, autorização, dependências e objetivos de recuperação. Saída: evidência do teste e plano de correção de lacunas.

### Definir o recorte

Especificar serviço ou conjunto de dados, versão, momento da cópia, dependências, condição de sucesso e limite do teste. Um arquivo restaurado não demonstra a restauração completa de ERP, identidade, rede e integrações.

Definir RTO e RPO com o negócio. A referência histórica de restauração em 30 minutos não é meta universal; a necessidade do processo e os recursos disponíveis orientam o requisito.

### Executar

1. Confirmar acesso à cópia e às chaves necessárias, seguindo as permissões e controles da organização.
2. Preparar ambiente isolado ou autorizado, sem sobrescrever a operação por conveniência do teste.
3. Restaurar o recorte, registrando início, fim, versão e erros.
4. Verificar integridade e funcionalidade com o dono do processo.
5. Comparar tempo e perda de dados com os objetivos acordados.
6. Registrar escopo aprovado, limitações, evidências e correções com responsável e prazo.

### Interpretar

“Backup executado” indica execução do mecanismo. “Arquivo restaurado” indica recuperação daquele recorte. “Serviço recuperado” exige verificação das dependências e da funcionalidade definida. Preservar essa diferença na ata e nos indicadores.

Se faltou credencial, a cópia não existia ou o tempo excedeu o objetivo, registrar a falha e rever o plano. Não substituir o resultado por sucesso estimado.

A orientação NIST para pequenas empresas inclui recuperação e ações ligadas à continuidade. A implementação do teste e sua frequência precisam considerar o contexto. [F01](<../framework/referencias/fontes.md#f01>)

Modelo: [Risco e continuidade](<../framework/templates/risco-continuidade.md>). Próxima leitura: [Indicadores operacionais](<../framework/indicadores/operacionais.md>).


## Conduzir uma revisão de direção

Use para decidir prioridades, recursos e tratamento de risco com base na situação atual de TI. Responsável por TI prepara a pauta; direção ou autoridade delegada decide; dono de processo contribui quando há impacto direto. Entrada: fila, indicadores com contexto, decisões anteriores e riscos. Saída: registro de decisões, responsáveis e próximos pontos de verificação.

### Preparar

Reunir dados da mesma janela, itens bloqueados, incidentes relevantes e propostas que exigem decisão. Mostrar a origem de cada informação e o que falta. Uma tabela com três indicadores sem período, amostra e critério de coleta não basta para decidir.

Distribuir o material antes da reunião quando isso for viável. Não preparar dezenas de páginas para uma decisão que cabe em um registro curto. Questões que exigem análise técnica podem receber responsável e prazo fora da reunião.

### Decidir

1. Retomar decisões anteriores e suas evidências.
2. Examinar fila, capacidade e conflitos de prioridade.
3. Relacionar propostas às finalidades de receita, custo, experiência e resiliência.
4. Examinar riscos, lacunas e alternativas.
5. Registrar decisão, motivo, autoridade, executor, limite de recurso, prazo e condição de revisão.
6. Comunicar alterações às pessoas afetadas.

### Conferir o registro

A ata precisa permitir que uma pessoa ausente entenda a decisão e encontre seu responsável. “A TI deve melhorar” não define saída. “Responsável por TI apresenta teste de recuperação do serviço de faturamento até a data acordada” cria um compromisso verificável, desde que escopo e recursos estejam definidos.

A frequência inicial quinzenal e os 30 minutos são parâmetros locais. Rever a cadência quando decisões pendentes ou indisponibilidade da direção tornam o ritual insuficiente. Adaptação é parte do método, não descumprimento de uma norma externa. [F09](<../framework/referencias/fontes.md#f09>) [F10](<../framework/referencias/fontes.md#f10>)

Modelo: [Decisão e prioridades](<../framework/templates/decisoes-prioridades.md>). Próxima leitura: [Maturidade](<../framework/adocao/maturidade.md>).


## Primeiros 30 dias

Este percurso ensina a iniciar o GEAR em uma equipe pequena. Ao final, a direção deve conseguir localizar a fila de TI, suas prioridades, os riscos mais urgentes e as evidências disponíveis. Trinta dias são uma janela de planejamento local; não garantem implantação completa nem avanço de maturidade.

### Preparar a adoção

O responsável por TI combina com a direção quem aprova prioridades e recursos. Escolhem um processo de negócio para acompanhar, um registro de demandas e um lugar para decisões. Não é necessário comprar uma plataforma. Antes de iniciar, confirmam tempo disponível, acesso aos responsáveis e autorização para os testes previstos.

A **verificação pré-projeto** decide se uma iniciativa específica deve começar: problema, patrocinador, viabilidade, risco e capacidade. É diferente da antiga “Fase Zero” de adoção. Um projeto pode ser recusado enquanto a rotina do GEAR continua funcionando.

### Semana 1: tornar o trabalho visível

1. Aplicar o [questionário de maturidade](<../framework/adocao/maturidade.md>), registrando evidência e lacunas.
2. Escolher até três problemas prioritários com o dono do processo. Anotar o impacto observado, sem estimar ganhos como se já fossem resultados.
3. Criar a fila: A Fazer, Em Andamento, Em Teste e Concluído. Registrar executor, solicitante, prioridade e aceite em cada item.
4. Comunicar o registro oficial. Uma urgência recebida por telefone deve entrar na fila assim que o atendimento permitir.
5. Aplicar o limite inicial de três itens iniciados por executor. Testes e bloqueios entram na contagem; suspensões conservam histórico.

**Evidência:** fila com trabalho real e registro de quem decide. Se ninguém puder assumir a aprovação, resolver essa lacuna antes de ampliar o método.

### Semana 2: conhecer dependências e recuperação

Mapear primeiro os ativos e fornecedores que sustentam o processo escolhido. Registrar proprietário, dados tratados, acesso, suporte, backup e dependências. Essa priorização por criticidade substitui a interpretação literal de “inventário 80/20”.

Executar um [teste de restauração](<../framework/guias/testar-restauracao.md>) autorizado, em ambiente seguro. Definir com o negócio o tempo e a perda de dados toleráveis. Documentar resultado, limitações e correções. Preparar uma orientação para uma dúvida recorrente, verificando-a com alguém que precise usá-la.

**Evidência:** inventário inicial, teste com resultado e instrução utilizável. Backup diário ou recuperação em 30 minutos só são requisitos se o contexto justificar essas escolhas.

### Semana 3: decidir e responder

Preencher o [plano de incidente](<../framework/templates/incidente.md>), conferir contatos e exercitar um cenário simples. Reunir direção, TI e dono do processo para decidir prioridades, riscos aceitos e recursos. Uma revisão de 30 minutos a cada duas semanas é uma configuração inicial; ajustar quando não permitir decisões suficientes.

**Evidência:** responsáveis localizáveis, decisão com prazo e risco atribuído. Um documento assinado não comprova que a resposta funcionará; o exercício revela dependências.

### Semana 4: verificar e ajustar

Escolher os [indicadores](<../framework/indicadores/operacionais.md>) que respondem às dúvidas reais da equipe. Registrar janela, origem e limitações. Reaplicar a maturidade com evidências da prática; dez respostas positivas não dispensam verificação de continuidade e responsabilidade.

Na revisão, decidir quais práticas manter, simplificar ou ampliar. Registrar próximos responsáveis e prazos. Se uma entrega ou teste não couber na janela, informar o motivo e reagendar, sem certificar uma transição inexistente.

**Evidência de conclusão do percurso:** comparação entre situação inicial e atual, pendências atribuídas e próxima revisão marcada. O percurso pode terminar com riscos ainda abertos.

### Exemplo de um começo possível

Uma empresa registra pedidos de acesso que antes chegavam por mensagens. O primeiro resultado verificável é a visibilidade de solicitante, aprovador e situação. O eventual efeito sobre tempo de atendimento precisa ser medido posteriormente. Consulte o [caso didático](<../framework/exemplos/caso-didatico.md>) para acompanhar um percurso completo.

Fundamento: adoção proporcional e governança de riscos no NIST para pequenas empresas [F01](<../framework/referencias/fontes.md#f01>); organização de tutorial conforme Diátaxis [F08](<../framework/referencias/fontes.md#f08>). A janela de 30 dias e as semanas são propostas locais do GEAR.

Anterior: [Escopo](<../framework/nucleo/escopo-principios.md>). Próxima leitura: [Maturidade](<../framework/adocao/maturidade.md>).


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

Responsável pela aplicação: TI. Responsável pela validação de efeitos no negócio: dono do processo. Direção aceita recursos e riscos conforme a alçada. Modelo: [Registro de maturidade](<../framework/templates/maturidade.md>).

Para planejar uma melhoria específica, consultar as [fichas por domínio](<../framework/adocao/fichas-maturidade.md>). Elas preservam a matriz detalhada das versões anteriores como opções de desenvolvimento, sem acrescentar condições ao IM-TI.

Anterior: [Primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>). Para compreender: [Fundamentos e adaptações](<../framework/fundamentos/origens-adaptacoes.md>).


## Origens, adaptações e evolução

GEAR reúne práticas do acervo GP-PME e NEXUS-PME em uma edição coerente. A mudança de nome foi uma decisão editorial: Gestão, Execução, Agilidade e Risco descrevem as atividades do método sem criar um quarto domínio. O acervo contém versões com diferentes recortes; sua data não determina, por si, a qualidade ou completude.

### Referência, adaptação e proposta local

| Referência | Conceito consultado | Adaptação do GEAR e limite |
| --- | --- | --- |
| NIST CSF 2.0 [F01](<../framework/referencias/fontes.md#f01>), [F02](<../framework/referencias/fontes.md#f02>) | Governar, Identificar, Proteger, Detectar, Responder e Recuperar | Priorização por serviço crítico e registro breve; seleção não cobre todo o CSF |
| Scrum Guide 2020 [F03](<../framework/referencias/fontes.md#f03>) | Inspeção, adaptação, transparência e responsabilidade | Ciclos curtos e aceite; omitir elementos significa não implementar Scrum integralmente |
| TOGAF [F04](<../framework/referencias/fontes.md#f04>) | Estrutura de conteúdo fundamental e guias de configuração | ADM-Lite é proposta local; não se afirma execução do ADM ou equivalência de fases |
| COBIT [F09](<../framework/referencias/fontes.md#f09>) | Governança ajustada ao contexto | Alçadas e revisão breve; não representa todo o sistema COBIT |
| ITIL 4 [F10](<../framework/referencias/fontes.md#f10>) | Gestão de serviços adaptável | Registro, recuperação e melhoria; não é implantação integral do ITIL |
| CIS [F11](<../framework/referencias/fontes.md#f11>) e CISA [F12](<../framework/referencias/fontes.md#f12>) | Higiene cibernética e recuperação | Controles priorizados com evidência; quatro práticas não equivalem às 56 salvaguardas IG1 |
| Diátaxis [F08](<../framework/referencias/fontes.md#f08>) | Aprender, executar, consultar e compreender | Percursos de documentação; organização editorial, não método de gestão |

WIP de três, revisão de 30 minutos, percurso de 30 dias, IM-TI, DAN financeiro e templates são escolhas locais. Não atribuir esses parâmetros às referências acima. Prazos e metas devem ser ajustados com motivo registrado.

### O que foi consolidado

Versões anteriores chamavam IA de quarto pilar e adoção de quinto pilar. O modelo vigente mantém três domínios; IA é assistência opcional, e adoção, indicadores e maturidade são transversais. Os quatro papéis conceituais de IA descrevem funções; o software implementado tem um orquestrador e oito especialistas. Essas contagens pertencem a camadas diferentes.

Foram preservados mecanismos relacionais: conversa com o negócio, revisão de prioridades, comunicação de impedimentos, dono do processo, papéis acumulados e aprovação segundo alçada. Uma equipe pequena pode concentrar funções; precisa tornar visíveis os conflitos e buscar segunda conferência quando a decisão exigir.

“Fase Zero” de adoção foi separada da verificação pré-projeto. Razão benefício/investimento foi separada de ROI líquido; proporção de itens legados foi separada de DAN financeiro. IM-TI não exige IA para alcançar o nível máximo.

### Adoção gradual e linguagem introdutória

Os mestres de junho de 2026 usavam “Iceberg Invertido” para representar uma entrada simples seguida de aprofundamento. A contribuição preservada é a **divulgação progressiva**: começar pela necessidade observada, mostrar a prática correspondente e consultar fundamentos quando forem necessários. A metáfora não estabelece uma escala científica nem exige ativar todos os módulos em uma ordem fixa.

“TI Enxuta” designa essa escolha de dimensionar registro, revisão e execução à capacidade disponível. Uma orientação recorrente pode ajudar antes de um chatbot; uma decisão registrada pode ajudar antes de um comitê formal. A possibilidade de reduzir esforço depende da aplicação e deve ser observada, sem pressupor custo zero.

O manual introdutório também usava DAA, “direcionar, agir e acompanhar”, para explicar a participação da direção. Trata-se de uma descrição didática da responsabilidade: decidir o que importa, executar o autorizado e verificar o efeito. Não substitui o ciclo ADM-Lite nem cria outro domínio. Os nomes antigos “orquestrador de valor”, “agente de mudança” e “parceiro estratégico” expressavam funções pretendidas, sem comprovar promoção de cargo ou transformação profissional.

Origem documental: mestres leigo e técnico em `GP-PME/` e mestre consolidado em `GP-PME antigravity/`, versões declaradas 6.0 e 5.2, de 02/06/2026. Essas contribuições são escolhas autorais, sem atribuição a uma norma externa.

### Versões e direitos

GEAR 2026.10 identifica a edição editorial. Números antigos 2.0, 5.2 e 6.0 são metadados de suas respectivas versões, não versões simultâneas do produto vigente. Identificadores de software GP-PME permanecem quando necessários à compatibilidade. O histórico de origem deve acompanhar a migração de conteúdo.

Os direitos seguem [LICENSE.md](<../LICENSE.md>). Não há nova certificação, validação de marca ou concessão de direitos nesta consolidação.

### Evidência acadêmica

O manuscrito mantém um protocolo prospectivo com casos sintéticos. Nenhuma simulação comprova ganho de campo. Silva, Mira da Silva e Pereira (2018), DOI [10.1109/CBI.2018.10044](https://doi.org/10.1109/CBI.2018.10044), é uma referência bibliográfica verificada; não se infere que valide GEAR. O conjunto de título, periódico e ano da referência antiga de Verdecchia não foi confirmado. A pesquisa identificou um estudo ATDx de 2022 na PeerJ e um artigo de teoria de 2021 no Journal of Systems and Software, ambos distintos da entrada antiga. Metadados e resumo não sustentam a fórmula de DAN financeiro; nenhum artigo foi adotado como substituto automático. Veja [fontes e limites](<../framework/referencias/fontes.md#bibliografia-e-acesso-limitado>). Acesso limitado à ISO e a livros licenciados impede atribuição de detalhes não consultados.

Consulta: [Fontes e limites](<../framework/referencias/fontes.md>). Análise aplicada: [Caso didático](<../framework/exemplos/caso-didatico.md>).


## Glossário

| Termo | Uso no GEAR |
| --- | --- |
| Aceite | Verificação do resultado acordado por quem responde pelo processo |
| ADM-Lite | Nome histórico da adaptação local de direção e revisão; não é TOGAF ADM |
| Canal oficial | Registro de demandas que reúne histórico e responsáveis, inclusive urgências recebidas por outros meios |
| CD-TI Lite | Revisão breve entre direção, TI e donos dos processos, conforme necessidade |
| COT | Custo de Otimização Tecnológica: investimento para uma melhoria delimitada |
| DAN financeiro | Estimativa de refatoração dividida pelo orçamento anual de TI; instrumento local |
| Domínio | Uma das três áreas essenciais: governança e direção, execução e serviços, segurança e continuidade |
| Fase Zero | Nome histórico do percurso inicial de adoção; nesta edição, “Primeiros 30 dias” |
| GEAR | Gestão, Execução, Agilidade e Risco; nome do framework, sem equivalência com quatro pilares |
| GP-PME / NEXUS-PME | Denominações anteriores preservadas em histórico, caminhos e identificadores de compatibilidade |
| IM-TI | Soma de dez práticas verificadas; instrumento local de maturidade de 0 a 10 |
| MVP | Recorte de solução usado para testar uma hipótese; prazo e benefício dependem do escopo |
| NIST-Lite | Expressão histórica para seleção local de práticas inspiradas no NIST; não é perfil certificado |
| PRI | Plano de resposta a incidentes com contatos, alçadas, ações e recuperação |
| PRD | Registro de problema, escopo, restrições e critérios de verificação de uma melhoria |
| Proporção legada | Itens classificados como legados / itens totais; distinta de DAN financeiro |
| RPO | Perda de dados tolerável expressa como tempo |
| RTO | Tempo de recuperação tolerável para o serviço |
| WIP | Trabalho iniciado por executor, incluindo teste e bloqueio; limite inicial de três |

As definições operacionais e suas exceções estão nos guias correspondentes. Um nome histórico não deve ser interpretado como conformidade com a referência externa.


## Fontes e limites de uso

Consultas realizadas em **4 e 5 de outubro de 2026**, com data e recorte em cada entrada. Fontes primárias fundamentam conceitos; não demonstram efetividade do GEAR nem validam suas faixas, pesos, prazos ou fórmulas.

### F01

*NIST Cybersecurity Framework 2.0: Small Business Quick-Start Guide*, Daniel Eliot, NIST. NIST SP 1300, publicado em 26/02/2024.

[Registro oficial](https://www.nist.gov/publications/nist-cybersecurity-framework-20-small-business-quick-start-guide), [DOI](https://doi.org/10.6028/NIST.SP.1300), [PDF oficial](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1300.pdf).

Seção consultada e limite: Resumo e pp. 2–8. Guia suplementar para pequenas organizações; não valida parâmetros do GEAR. Consulta: 04/10/2026.

### F02

*The NIST Cybersecurity Framework (CSF) 2.0*, NIST. NIST CSWP 29, 26/02/2024.

[DOI](https://doi.org/10.6028/NIST.CSWP.29), [PDF oficial](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf).

Seção consultada e limite: Resumo, Executive Summary e seção 3. Resultados e perfis; não prescreve uma implementação única. Consulta: 04/10/2026.

### F03

*O Guia do Scrum: O Guia Definitivo para o Scrum: As Regras do Jogo*, Ken Schwaber e Jeff Sutherland. Novembro de 2020; tradução brasileira distribuída no site oficial, arquivo PortugueseBR-3.0.

[Índice oficial](https://scrumguides.org/download.html), [PDF em português brasileiro](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf).

Seção consultada e limite: Definição de Scrum e Scrum Team, pp. 2, 4, 6–8. Práticas inspiradas não equivalem a Scrum completo. Consulta: 04/10/2026.

### F04

*TOGAF*, The Open Group. Página pública com apresentação da 10ª edição; a página também apresenta a versão 9.2.

[Página oficial](https://www.opengroup.org/togaf).

Seção consultada e limite: Apresentação pública da 10ª edição. Capítulos detalhados redirecionaram a autenticação; ADM-Lite é local. Consulta: 04/10/2026.

### F05

*DORA's software delivery performance metrics*, Nathen Harvey, DORA / Google Cloud. Atualizada em 05/01/2026.

[Guia oficial](https://dora.dev/guides/dora-metrics/).

Seção consultada e limite: Key insights e Common pitfalls. Cinco métricas para entrega de software; não métricas gerais de governança. Consulta: 04/10/2026.

### F06

*A history of DORA's software delivery metrics*, Nathen Harvey, DORA / Google Cloud. Publicada e atualizada em 02/01/2026.

[Histórico oficial](https://dora.dev/insights/dora-metrics-history/).

Seção consultada e limite: Refining definitions e From four keys to five. Distingue recuperação de implantação com falha de MTTR geral. Consulta: 04/10/2026.

### F07

*Web Content Accessibility Guidelines (WCAG) 2.2*, W3C. Recomendação de 12/12/2024, versão servida na consulta.

[Versão fixa](https://www.w3.org/TR/2024/REC-WCAG22-20241212/), [URL da versão publicada mais recente](https://www.w3.org/TR/WCAG22/).

Seção consultada e limite: Critérios 1.4.3, 1.4.10, 1.4.12, 2.1.1, 2.4.7, 2.4.11 e 2.5.8. Alvo de teste; sem declaração de conformidade. Consulta: 04/10/2026.

### F08

*Diátaxis*, Daniele Procida. Site em evolução; data de publicação e número de versão não declarados nas páginas consultadas.

[Apresentação](https://diataxis.fr/), [Introdução de cinco minutos](https://diataxis.fr/start-here/), [Autoria e citação](https://diataxis.fr/colophon/).

Seção consultada e limite: Start here e Colophon. Orientação editorial, sem estudo de usabilidade específico do GEAR. Consulta: 04/10/2026.

### F09

*COBIT*, ISACA. Página sobre COBIT 2019, sem data única de publicação.

[Página oficial](https://www.isaca.org/resources/cobit).

Seção consultada e limite: Why COBIT e Practical Guidance. Adaptação ao contexto; não se atribuem fórmulas locais à ISACA. Consulta: 04/10/2026.

### F10

*ITIL 4 Foundation*, PeopleCert. Página específica do ITIL 4 Foundation, sem data única de publicação.

[Página oficial](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-foundation-2565).

Seção consultada e limite: What will you learn? e Guiding principles. Escopo ITIL 4, sem alegação sobre edição mais recente do portfólio. Consulta: 04/10/2026.

### F11

Center for Internet Security. *CIS Critical Security Controls Implementation Groups*. Página institucional, sem data única declarada. [Fonte oficial](https://www.cisecurity.org/controls/implementation-groups). Seção IG1: 56 salvaguardas de higiene cibernética. Consulta: 04/10/2026. Uma seleção de quatro práticas ou dez verificações locais não equivale à implantação integral do IG1.

### F12

CISA, MS-ISAC, NSA e FBI. *#StopRansomware Guide*. Guia institucional, versão consultada em 04/10/2026. [Página oficial](https://www.cisa.gov/stopransomware/ransomware-guide). Seções sobre prevenção e resposta: backups offline e encriptados, teste regular, MFA resistente a phishing e menor privilégio. O guia não oferece garantia de proteção nem sustenta o percentual de 95% anunciado em versões históricas.

### F13

Verdecchia, Roberto; Lago, Patricia; Malavolta, Ivano; Ozkaya, Ipek. *ATDx: Building an Architectural Technical Debt Index*. ENASE 2020, SciTePress, 2020, pp. 531–539. DOI [10.5220/0009577805310539](https://doi.org/10.5220/0009577805310539). [Manuscrito do primeiro autor](https://robertoverdecchia.github.io/papers/ENASE_2020.pdf); [registro institucional VU](https://research.vu.nl/en/publications/22b62e22-79f4-4cbb-a552-9151b7353862).

Seções consultadas: §§ 2.1–2.2, 4.1.6, 4.2 e 6; páginas 2–3 e 6–8 do PDF do autor. A normalização usa violações por elementos de código e análise estatística de projetos; não orçamento de TI. O texto não fundamenta DAN financeira, faixas 0,15/0,35, COT ou ROI em PME. Consulta: 05/10/2026. Paginação do manuscrito difere do registro dos anais; não foi transposta.

### F14

Hacks, Simon; Höfert, Hendrik; Salentin, Johannes; Yeong, Yoon Chow; Lichter, Horst. *Towards the Definition of Enterprise Architecture Debts*. IEEE EDOCW, 2019, pp. 9–16. DOI [10.1109/EDOCW.2019.00016](https://doi.org/10.1109/EDOCW.2019.00016). [Registro e versão dos autores](https://arxiv.org/abs/1907.00677); [preprint v1, 28/06/2019](https://arxiv.org/pdf/1907.00677v1).

Seções consultadas: §§ 2, 4–7, páginas 2 e 4–7 do preprint. Propõe uma definição de dívida de arquitetura empresarial com ponderação contextual e demonstração por casos fictícios; avaliação real está fora do escopo. Não fundamenta COT, ROI, DAN financeira ou faixas para PME. Consulta: 05/10/2026. Metadados IEEE conferidos; o texto final dos anais não foi comparado integralmente ao preprint.

### F15

Brasil. *Lei nº 13.709, de 14 de agosto de 2018: Lei Geral de Proteção de Dados Pessoais (LGPD)*. Texto atualizado disponibilizado pela Câmara dos Deputados. [Texto oficial](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html).

Captura oficial realizada em 04/10/2026; releitura dos arts. 6º, 7º, 18, 37, 46 e 48 em 05/10/2026. Os dispositivos fundamentam princípios, hipóteses legais, direitos, registros, segurança e comunicação de incidentes. A seleção não é análise integral de conformidade, nem permite presumir enquadramento especial de uma PME. O registro local do GEAR não substitui a avaliação das obrigações aplicáveis.

### F16

Autoridade Nacional de Proteção de Dados. *Comunicação de Incidentes de Segurança — CIS*. Página publicada em 23/12/2022; modificação indicada em 26/08/2026 na consulta. [Orientação oficial](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis).

Consulta e captura: 04/10/2026. Perguntas 4–6: prazo geral de três dias úteis para comunicação à ANPD e aos titulares nos casos sujeitos à obrigação, ressalvado prazo em legislação específica; comunicação complementar não substitui a inicial. A página referencia a Resolução nº 15/2024, cujo texto integral não foi obtido nesta pesquisa. Marco inicial, contagem e exceções requerem conferência do ato aplicável. As regras de agentes de pequeno porte não foram verificadas integralmente; não se atribui prazo diferenciado pelo número de empregados.

### Tipografia local

US Web Design System / GSA. *Public Sans*, v2.001. [Repositório oficial](https://github.com/uswds/public-sans). Adobe. *Source Serif*, v4.005. [Repositório oficial](https://github.com/adobe-fonts/source-serif). Consulta: 04/10/2026. Arquivos distribuídos com SIL Open Font License 1.1; versões, commits, URLs dos binários e SHA-256 registrados no manifesto de fontes que acompanha os ativos. Os arquivos não foram modificados.

### Bibliografia e acesso limitado

Silva, David; Mira da Silva, Miguel; Pereira, Ruben. *Baseline Mechanisms for Enterprise Governance of IT in SMEs*. IEEE CBI, 2018, pp. 32–41. DOI [10.1109/CBI.2018.10044](https://doi.org/10.1109/CBI.2018.10044). Metadados verificados; não demonstra eficácia do GEAR.

A entrada histórica atribuída a Verdecchia em 2022 mistura um título e periódico que não foram confirmados em conjunto. Dois trabalhos reais foram identificados: *Empirical evaluation of an architectural technical debt index in the context of the Apache and ONAP ecosystems* (Verdecchia, Malavolta, Lago e Ozkaya, **PeerJ Computer Science**, 8:e833, 07/02/2022), DOI [10.7717/peerj-cs.833](https://doi.org/10.7717/peerj-cs.833); e *Building and evaluating a theory of architectural technical debt in software-intensive systems* (Verdecchia, Kruchten, Lago e Malavolta, **Journal of Systems and Software**, 176:110925, junho de 2021), DOI [10.1016/j.jss.2021.110925](https://doi.org/10.1016/j.jss.2021.110925).

Fontes consultadas em 04/10/2026: registros depositados pelas editoras no Crossref, [2022](https://api.crossref.org/works/10.7717/peerj-cs.833) e [2021](https://api.crossref.org/works/10.1016/j.jss.2021.110925). Foram verificados metadados e resumo do artigo de 2022, que descreve ATDx baseado em SonarQube nos ecossistemas Apache e ONAP; somente metadados do artigo de 2021. O texto integral não foi acessado. Nenhum foi usado como substituição automática da referência antiga nem valida a fórmula financeira de DAN ou o ROI do GEAR. A similaridade de títulos não comprova qual documento originou a entrada histórica.

O catálogo/OBP ISO retornou bloqueio de acesso; capítulos TOGAF exigiram autenticação. Não atribuir detalhes dessas normas ou de livros licenciados como se tivessem sido lidos. As sínteses históricas do acervo são material de trabalho, não substitutos dos documentos originais.



Documentação modular: [GEAR](<../framework/README.md>). Referências completas: [Fontes e limites](<../framework/referencias/fontes.md>). Tarefa inicial: [Primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>).
