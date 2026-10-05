# Requisitos do GEAR

Edição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.

## Origem e decisão editorial

Crédito declarado no PRD de 02/06/2026: Antigravity AI, sob direção de Andre Victor. A declaração antiga de prontidão de mercado não é evidência de implantação. O produto consiste em documentação e software de apoio; segurança, operação e recuperação dependem de tecnologia e competência apropriadas, mesmo sem IA. Uma página ou duas são preferências de síntese, não critérios suficientes de qualidade.

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


## Revisão de uma saída assistida por IA

Aplicar antes de usar uma saída de IA em decisão, comunicação ou mudança. O responsável humano pela tarefa verifica conteúdo e autorização. Não enviar dado restrito a uma ferramenta sem permissão e controles adequados.

- Tarefa, data, responsável e ferramenta/modelo quando conhecido: [preencher]
- Informações fornecidas e classificação: [preencher sem reproduzir segredo]
- Saída pretendida e autoridade para usá-la: [preencher]
- Fatos conferidos e fontes consultadas: [preencher]
- Citações verificadas no documento original: [preencher]
- Cálculos, unidades e premissas conferidos: [preencher]
- Dados pessoais ou confidenciais removidos/protegidos: [preencher]
- Limitações, erro observado e correção: [preencher]
- Aprovação, rejeição ou necessidade de investigação: [pessoa e motivo]
- Evidência da versão usada e próxima revisão: [preencher]

Uma resposta fluente não é evidência. Se não for possível verificar uma afirmação material, retirá-la, restringi-la ou identificá-la como hipótese. A assinatura do revisor não substitui acesso à fonte.

Conclusão: somente a saída revisada e autorizada segue para uso. A equipe pode executar a mesma tarefa sem IA.

### Conferências por tipo de saída

Aplicar os blocos pertinentes ao efeito proposto, registrando motivo quando um item não se aplica. Uma conferência feita por outro modelo pode ajudar a localizar divergências, mas não substitui o revisor humano nem comprova ausência de erro.

#### Rastreabilidade

- [ ] Fatos correspondem aos dados fornecidos ou a fontes conferidas?
- [ ] Sistemas, interfaces e configurações reais estão separados das propostas?
- [ ] Lacunas, estimativas e incertezas estão explícitas?
- [ ] Referências indicam versão e trecho que sustenta a afirmação?
- [ ] Cálculos usam moeda, unidades, período e premissas compatíveis?

Uma alternativa de ferramenta pode ser proposta com justificativa, custo e verificação pendentes; ela não passa a ser uma aquisição real. Não exigir marcas já compradas para toda análise nem considerar qualquer sugestão uma configuração existente.

#### Requisitos

- [ ] História descreve usuário, comportamento e finalidade verificáveis?
- [ ] Critério informa condição, ação e resultado observável?
- [ ] Escopo e exclusões foram acordados com o negócio?
- [ ] Dependências e capacidade tornam o recorte viável ou têm lacunas atribuídas?

#### Segurança e continuidade

- [ ] Acesso proposto é necessário ao efeito e suas exceções foram revistas?
- [ ] Controles têm cobertura e evidência, sem promessa de proteção integral?
- [ ] Recuperação e contenção consideram ambiente, autoridade e preservação de evidências?
- [ ] Recursos e manutenção foram considerados, inclusive para soluções nativas?

#### Código e configuração

- [ ] Dependências, APIs, comandos e valores foram conferidos na versão aplicável?
- [ ] Entrada, acesso e erros relevantes foram testados em ambiente autorizado?
- [ ] Segredos e detalhes internos não aparecem indevidamente na saída?
- [ ] Regras de negócio implementadas têm revisão e critérios acordados?
- [ ] Placeholder, demonstração e integração real estão identificados?
- [ ] Plano de retorno e aprovação para a mudança estão registrados?

Código inicial pode conter lacunas explícitas; não é apto ao uso operacional apenas por ser executável. Também não há proibição universal de gerar lógica completa: seu uso exige revisão, testes e autorização apropriados.

### Registrar o resultado

| Item/afirmação | Evidência consultada ou teste | Resultado e limitação | Correção necessária | Responsável |
| --- | --- | --- | --- | --- |
| [preencher] | | | | |

Decisão: [aprovado para o uso delimitado / ajustar / rejeitar / investigar], com pessoa, data, motivo, versão e pendências. Aprovação editorial não autoriza automaticamente implantação. Erro material exige correção ou restrição do uso; registrar divergência sem prometer “zero alucinações”. Duração de cinco minutos e revisão de três fatos não são critérios de qualidade.


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


## Comparar uma tarefa com e sem assistência

Use quando houver uma decisão sobre continuar, ajustar ou suspender o uso de IA. A pessoa responsável pela tarefa define o recorte; quem aceita a entrega confere qualidade; direção decide investimento. A equipe pode atingir qualquer nível de maturidade sem adotar IA.

### Preparar uma comparação útil

Escolher tarefas comparáveis, registrar dificuldade, experiência do executor, ferramenta, versão, dados permitidos e critério de aceite. Medir todo o esforço: preparação, geração, leitura, conferência, correção e teste. Cronometrar somente a geração omite trabalho necessário.

| Medida local | Cálculo ou registro | Limite de interpretação |
| --- | --- | --- |
| Tempo por entrega aceita | Esforço total até o aceite | Comparar tarefas com escopo e qualidade equivalentes |
| Variação relativa de tempo | (tempo de referência − tempo assistido) / tempo de referência × 100 | Referência positiva; valor negativo indica aumento de esforço |
| Aceitação sem revisão relevante | Entregas aceitas sem correção relevante / entregas avaliadas × 100 | Definir “relevante”; aceite não prova ausência de erro |
| Erros por entrega | Erros identificados / entregas verificadas | Manter o mesmo método e profundidade de verificação |
| Custo por entrega aceita | Custos atribuíveis / entregas aceitas | Incluir ferramenta, revisão, correção e infraestrutura |
| Capacidade recuperada | Horas de referência − horas assistidas | Tempo potencial, sem equivalência automática a economia financeira |

Os nomes históricos TGA, TMRIA, TAA, CAG e TEIA descreviam tempo, aceitação, custo ou variação. A edição vigente exige unidade e evento de início/fim explícitos. Resposta inicial, restauração de serviço e fechamento administrativo são medidas distintas. Não atribuir causalidade à IA se o processo, a equipe ou o tipo de demanda também mudou.

### Decidir com os resultados

1. Conferir amostra, exclusões, falhas e tarefas não concluídas.
2. Comparar esforço e qualidade, conservando os registros individuais.
3. Examinar se a vantagem depende de dados, pessoa, fornecedor ou contexto específicos.
4. Registrar continuar, ajustar, ampliar o teste ou suspender; indicar dono e próxima verificação.

Concluir quando a decisão pode ser reconstruída a partir das entradas e das entregas verificadas. Sem baseline, registrar apenas a medição atual. Sem denominador ou observações comparáveis, não preencher percentual. A antiga meta de redução de 60% não é requisito do GEAR.

Fundamento: instrumento local de avaliação, derivado dos indicadores candidatos do acervo. Estudos sobre assistência têm tarefas e populações próprios; seus resultados não predizem o ganho desta equipe. Consulte [a bibliografia do manuscrito](<../GP-Pme%20Article/overleaf/references.bib>) e os [limites de atribuição das fontes](<../framework/referencias/fontes.md>).

Consulta: [comparação da rotina](<../framework/indicadores/negocio-comparacao.md>) e [revisão de saída assistida](<../framework/templates/revisao-ia.md>).

