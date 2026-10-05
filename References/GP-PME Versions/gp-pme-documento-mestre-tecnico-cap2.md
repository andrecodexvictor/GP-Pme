# GEAR: Governança e direção

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: Sem autoria, versão ou data declaradas neste arquivo; não atribuídas por inferência.

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Governança e direção](#governanca-e-direcao)
- [Conduzir uma revisão de direção](#conduzir-uma-revisao-de-direcao)
- [Registro de responsabilidades](#registro-de-responsabilidades)
- [Decisão e prioridade](#decisao-e-prioridade)
- [Matriz de impacto e urgência](#matriz-de-impacto-e-urgencia)
- [Painel de indicadores e decisões](#painel-de-indicadores-e-decisoes)
- [Indicadores de negócio e comparação da rotina](#indicadores-de-negocio-e-comparacao-da-rotina)

## Governança e direção

Este domínio conecta decisões de TI a necessidades do negócio e a riscos conhecidos. A direção define prioridades e autoriza recursos; o responsável por TI organiza a execução e apresenta evidências. A prática admite papéis acumulados, mas exige que cada decisão tenha uma autoridade identificada.

### Avaliar, dirigir e monitorar

O acervo chama o ciclo de **ADM-Lite**: avaliar, dirigir e monitorar. No GEAR, avaliar é examinar situação, alternativas, custos e riscos; dirigir é decidir prioridade, limites e responsabilidade; monitorar é confrontar a decisão com evidências e rever a ação.

Essa sigla local não designa o Architecture Development Method do TOGAF. A correspondência detalhada com ISO/IEC 38500 exige consulta à edição oficial; o conteúdo fechado não foi verificado na pesquisa que sustenta esta edição. A apresentação pública do COBIT oferece evidência de dimensionamento e adaptação da governança, sem validar o instrumento local. [F09](<../../framework/referencias/fontes.md#f09>)

### Papéis e acordos

| Função | Responsabilidade | Evidência mínima |
| --- | --- | --- |
| Direção ou patrocinador | Autorizar prioridade, recurso e aceitação de risco | Decisão com data e condição de revisão |
| Responsável por TI | Preparar alternativas e conduzir a execução | Registro de demanda, responsável e situação |
| Dono do processo de negócio | Explicar impacto e validar a entrega | Critério de aceite e confirmação da saída |
| Usuário afetado | Informar necessidade e efeito percebido | Solicitação e feedback contextualizados |

Um técnico terceirizado pode executar sem poder aprovar orçamento. Um proprietário pode ser também dono de processo. Quando o executor é o aprovador, registrar a limitação e buscar revisão de outra pessoa em ações de maior impacto, conforme os controles já existentes na organização.

Use a [matriz de responsabilidades](<../../framework/templates/responsabilidades.md>). RACI-Lite é um suporte de registro: R executa; A aprova; C é consultado; I é informado. Não precisa criar cargos adicionais.

### Matriz de quatro finalidades

A Matriz 4 Quadrantes relaciona iniciativas a receita, custos, experiência e resiliência. Uma iniciativa pode ter finalidade principal e efeitos secundários. A classificação não garante benefício: precisa de hipótese, medida e responsável.

Antes de aprovar, perguntar: qual problema observável será tratado; quem recebe o resultado; que condição indicará conclusão; qual recurso será comprometido; que risco permanece; que alternativa é viável? Uma proposta sem essas informações volta para refinamento ou tem a lacuna explicitada na decisão.

### Revisão de direção

CD-TI Lite é o nome histórico da revisão de direção. Uma reunião quinzenal de 30 minutos é o ponto de partida do método, não uma duração obrigatória para toda empresa. A pauta pode reservar cinco minutos para indicadores, quinze para demandas, cinco para riscos e cinco para decisões. Uma emergência pode exigir uma decisão fora dessa cadência.

Registrar decisão, alternativas consideradas, motivo, responsável, prazo e evidência esperada. Comunicar às pessoas afetadas o que mudou e qual canal usar. O registro de conflito entre negócio e TI evita que uma discordância fique escondida sob um status de tarefa.

### Critério de funcionamento

O domínio está operacional quando decisões relevantes têm autoridade, justificativa e acompanhamento, e quando a equipe consegue localizar o acordo vigente. A quantidade de atas produzidas não mede a qualidade da governança.

Para executar: [Conduzir uma revisão](<../../framework/guias/conduzir-revisao.md>). Modelo: [Decisão e prioridades](<../../framework/templates/decisoes-prioridades.md>).


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

A frequência inicial quinzenal e os 30 minutos são parâmetros locais. Rever a cadência quando decisões pendentes ou indisponibilidade da direção tornam o ritual insuficiente. Adaptação é parte do método, não descumprimento de uma norma externa. [F09](<../../framework/referencias/fontes.md#f09>) [F10](<../../framework/referencias/fontes.md#f10>)

Modelo: [Decisão e prioridades](<../../framework/templates/decisoes-prioridades.md>). Próxima leitura: [Maturidade](<../../framework/adocao/maturidade.md>).


## Registro de responsabilidades

Preencher no início da adoção e revisar após mudanças de pessoas ou fornecedores. Direção confirma alçadas; cada pessoa confirma disponibilidade e acesso. Saída: lista consultável de responsáveis e substitutos.

**Processo/serviço:** [preencher]  
**Data e responsável pelo registro:** [preencher]

| Função | Pessoa ou fornecedor | Decide o quê | Limite da alçada | Substituto/contato |
| --- | --- | --- | --- | --- |
| Patrocinador/direção | | Recursos e risco aceito | | |
| Responsável por TI | | Organização e execução | | |
| Dono do processo | | Necessidade e aceite | | |
| Executor | | Trabalho autorizado | | |
| Segurança/continuidade | | Teste e resposta | | |

**Acúmulos e conflitos:** [quem acumula aprovação e execução; como haverá segunda conferência quando necessária].

**Comunicação:** [registro oficial, contato de urgência, frequência de atualização e destinatários].

**Verificação:** pessoas designadas confirmaram os papéis em [data/evidência]. Exceções: [ausência de substituto, serviço terceirizado, limites de disponibilidade]. Não preencher nomes fictícios no registro operacional.

### RACI-Lite por atividade

Quando houver dúvida entre funções, usar R para executor, A para autoridade de aprovação, C para pessoa consultada e I para pessoa informada. Identificar uma autoridade final por decisão; se houver mais de uma aprovação necessária, explicitar decisões e alçadas distintas.

| Atividade | R: executor | A: autoridade | C: consultado | I: informado |
| --- | --- | --- | --- | --- |
| Orçamento anual de TI | | | | |
| Priorização da fila | | | | |
| Triagem e atendimento | | | | |
| Teste de recuperação | | | | |
| Requisitos e aceite da melhoria | | | | |

Uma ferramenta pode preparar a minuta ou auxiliar o teste. Registrar a pessoa responsável pela execução e conferência; não atribuir à IA a alçada humana. Validar disponibilidade e conflitos antes de considerar a tabela vigente. A quantidade de linhas é ajustável ao serviço.


## Decisão e prioridade

Use para uma demanda, investimento ou revisão de fila. TI prepara fatos; dono do processo explica impacto; autoridade de aprovação decide. Este registro pode ser um cartão do quadro.

- Identificador, data e solicitante: [preencher]
- Problema e processo afetado: [situação observada]
- Evidências e fontes: [link, período e limitações]
- Opções consideradas: [inclusive adiar ou não executar]
- Impacto, urgência, esforço e dependências: [estimativa e incerteza]
- Riscos e proprietário: [preencher]
- Capacidade e trabalho já iniciado do executor: [preencher]
- Decisão e motivo: [preencher]
- Aprovador e limite de alçada: [preencher]
- Executor, prazo e critério de conclusão: [preencher]
- Data de revisão e comunicação ao solicitante: [preencher]

A matriz de quatro finalidades relaciona a demanda a receita, custos, experiência e resiliência. Registrar finalidade principal e efeitos secundários. Impacto e esforço ajudam a decidir a ordem; não alteram o significado dessa matriz nem dispensam risco, urgência ou dependência. Uma obrigação urgente pode anteceder uma melhoria de alto impacto.

Concluir quando a decisão estiver atribuída e comunicada. Se faltar dado essencial, registrar a investigação e seu responsável. Se a prioridade mudar, acrescentar nova decisão, preservando a anterior.


## Matriz de impacto e urgência

Use para discutir demandas concorrentes. Dono do processo explica impacto; TI verifica dependências e esforço; autoridade de aprovação decide. Esta matriz é distinta das quatro finalidades: receita, custos, experiência e resiliência.

| | Urgência menor | Urgência maior |
| --- | --- | --- |
| Impacto maior | Agendar com capacidade, dependências e prazo | Avaliar prioridade e exceções necessárias |
| Impacto menor | Questionar necessidade, adiar ou delegar | Conferir impacto e prazo; executar conforme capacidade |

Urgência alta não demonstra que a demanda é rápida ou fácil. Um bug de faturamento pode ter impacto alto; classificar pelo efeito observado. Fronteiras alto/baixo são locais e devem ter exemplos acordados.

| Demanda | Impacto e evidência | Prazo e motivo de urgência | Esforço/dependência | Decisão e responsável |
| --- | --- | --- | --- | --- |
| [preencher] | | | | |

Saída: ordem acordada, itens adiados e motivo. Concluir quando solicitantes conhecerem a decisão e cada item selecionado tiver executor e aceite. Risco, obrigação, emergência ou dependência podem alterar a ordem; registrar no [modelo de decisão](<../../framework/templates/decisoes-prioridades.md>).

Origem: template histórico `References/GP-PME Versions/matriz_4_quadrantes.md`, revisto para retirar associação automática entre urgência e facilidade. Instrumento local, sem validade universal atribuída a fonte externa.


## Painel de indicadores e decisões

Use na revisão da rotina quando houver uma decisão apoiada por medidas. TI prepara dados; dono do serviço confere o escopo; direção e TI acordam tolerâncias e ações. Um painel pode ser preenchido em planilha ou papel; não exige coleta automática.

### Identificação e cálculo

- Serviço/processo e responsável: [preencher]
- Período, horário observado e exclusões: [preencher]
- Origem dos dados, versão do cálculo e data da coleta: [preencher]

| Indicador | Dados de entrada e quantidade | Resultado/unidade | Tolerância local e comparação | Limite da interpretação |
| --- | --- | --- | --- | --- |
| IDSC | Horas observadas e indisponíveis | [%] | | |
| TMpR | Duração de restauração e incidentes encerrados | [horas; quantidade] | | |
| ISU | Notas 1–5 e respostas válidas | [média; quantidade] | | |
| Outro indicador escolhido | [definição, período e fonte] | | | |

Sem denominador válido, registrar dado insuficiente. Não usar queda da média como sinal automático de melhoria; comparar escopo, quantidade e casos longos. As metas históricas >99,5%, <4 horas e >4,5 são exemplos locais configuráveis, sem validade universal.

### Decisão e acompanhamento

| Questão a decidir | Evidência e alternativas | Decisão/motivo | Autoridade | Executor e prazo | Próxima verificação |
| --- | --- | --- | --- | --- | --- |
| [preencher] | | | | | |

Concluir quando a pessoa responsável conferiu dados e unidades e a decisão ou necessidade de coleta está atribuída. Cálculo assistido por IA exige a mesma conferência; não preencher um resultado por suposição.

Definições: [operacionais](<../../framework/indicadores/operacionais.md>) e [negócio/comparação](<../../framework/indicadores/negocio-comparacao.md>). Próximo modelo: [decisões e prioridades](<../../framework/templates/decisoes-prioridades.md>).


## Indicadores de negócio e comparação da rotina

Este catálogo recupera indicadores dos guias anteriores para decisões que os três indicadores operacionais não respondem. Selecionar somente medidas com uso definido. Financeiro confere custos e receita; dono do processo confere escopo e benefício; TI mantém os registros. As definições abaixo são convenções locais do GEAR.

### Conferir custos e canais

| Medida | Cálculo no mesmo período | O que conferir |
| --- | --- | --- |
| Custo de TI sobre receita | Custo total de TI / receita bruta × 100, em % | Incluir pessoal, serviços, licenças e infraestrutura segundo a política financeira; declarar o tratamento dos investimentos |
| Participação dos canais digitais | Receita dos canais digitais / receita total × 100, em % | Definir canais e atribuição de vendas; evitar contar a mesma venda em dois canais |

Receita positiva é necessária para calcular as proporções. Um aumento da participação digital pode decorrer de redução de outros canais, sem crescimento da receita total. A medida não demonstra a contribuição causal da TI. Custos e receita precisam de base contábil e janela comparáveis; a antiga recomendação de 2–6% não tinha suporte para uso universal.

### Conferir experiência digital

ISU é uma média de notas de 1 a 5, conforme os [indicadores operacionais](<../../framework/indicadores/operacionais.md>). Uma pesquisa com clientes pode usar média de notas ou uma proporção de respostas consideradas satisfeitas, desde que informe pergunta, escala, limiar, janela e quantidade de respostas.

Na convenção local de proporção, calcular `respostas que atendem ao critério de satisfação / respostas válidas × 100`. Uma média de 4,5 em escala de 1 a 5 não é automaticamente 90% de pessoas satisfeitas. Sem respostas, registrar dado insuficiente. Informar taxa de resposta e o universo convidado quando conhecidos.

O guia antigo misturava média, CSAT percentual e NPS na mesma linha. São instrumentos distintos. Esta edição não converte nem estabelece equivalência entre eles; NPS e seus antigos limites não integram o cálculo do GEAR. A escolha de outro instrumento exige documentar sua definição e referência específica.

### Conferir entregas e suporte

#### Tempo de lançamento

Medir `data de disponibilização acordada − data de início do PRD`, em dias corridos ou úteis declarados. Registrar aprovação, início de implementação e conclusão para distinguir espera e execução. Uma implantação técnica e a disponibilização ao usuário podem ter datas diferentes. Itens ainda abertos não entram como concluídos; mostrá-los separadamente para evitar ocultar atrasos.

Uma janela de uma ou duas semanas pode orientar um piloto pequeno. Não é meta universal de lançamento. O tempo de fluxo do quadro começa no início do trabalho; esse ponto pode diferir do início do PRD.

#### Entregas dentro de prazo e orçamento

Calcular `entregas concluídas que cumpriram prazo e orçamento / entregas concluídas elegíveis × 100`. Usar os dois critérios em conjunto e indicar quantidades. Fixar a versão do prazo e orçamento; quando houver renegociação, conservar o acordo inicial e apresentar os resultados nas duas bases. Sem entregas elegíveis, o resultado é dado insuficiente. Cancelamentos e itens abertos devem aparecer no relatório, mesmo quando excluídos da proporção.

O indicador não mede sozinho a utilidade da entrega. Aceite e benefício observado exigem evidência própria. A antiga meta de 80% era parâmetro local sem validação externa.

#### Incidentes por colaborador

Calcular `incidentes abertos no período / colaboradores do universo definido`. Declarar se o denominador é média do período ou posição em uma data. Separar incidentes de pedidos de acesso, dúvidas e mudanças. Conferir duplicatas e mudanças de cobertura.

Mais registros podem indicar melhor captura. Uma queda pode indicar menos falhas ou dificuldade de pedir ajuda. Comparar serviços, exposição, população e política de classificação antes de interpretar tendência; redução contínua não é requisito de maturidade.

### Registrar antes e depois

Definir a situação inicial pela coleta, sem preencher percentuais presumidos. Comparar períodos equivalentes e registrar outras mudanças que possam explicar o resultado. TI coleta; dono do serviço verifica; direção decide a ação. A comparação é descritiva, sem atribuir causalidade ao framework.

| Tema | Registro em cada período | Evidência e limite |
| --- | --- | --- |
| Captura de demandas | Demandas únicas observadas e quantas têm registro oficial | Reconciliar formulário, e-mail e contatos informais; denominador desconhecido impede percentual confiável |
| Restauração | Início, recuperação, serviço e incidentes encerrados | Usar TMpR para restauração; tempo até fechamento administrativo é outra medida |
| Autoatendimento | Solicitações elegíveis, resolução confirmada e regra de atribuição | Acesso à FAQ ou interação com bot não comprova resolução; registrar retorno ao suporte |
| Testes de recuperação | Escopos planejados, executados, aprovados e limitações | Um teste aprovado não garante outros serviços nem ausência de falha futura |
| Decisões com o negócio | Autoridade, motivo, recurso, prazo e acompanhamento | Ata assinada demonstra registro; verificar se a ação ocorreu e se a decisão foi revista |
| Maturidade | Resposta e evidência por pergunta, total e lacunas | Reaplicar a mesma edição; aumento do total não elimina um risco crítico |

Concluir a revisão quando dados, exclusões, diferenças e ação estão registrados com responsável e prazo. Sem comparação suficiente, descrever o que passou a ser observável e planejar a coleta; não declarar redução de 30%, resolução de 40% ou cobertura de 90% por adoção do método.

### Usar coleta assistida

Planilhas e scripts podem calcular medidas definidas. IA pode ajudar a classificar uma amostra autorizada, mas a pessoa responsável confere categorias, duplicatas e cálculos. Um painel atualizado não é previsão de anomalias validada. Se classificação ou acesso aos dados mudarem, declarar a quebra de comparabilidade.

Anterior: [Indicadores operacionais](<../../framework/indicadores/operacionais.md>). Próxima leitura: [Indicadores financeiros](<../../framework/indicadores/financeiros.md>). Para executar: [Conduzir uma revisão](<../../framework/guias/conduzir-revisao.md>).


## Rever riscos de adoção

Resistência, sobrecarga inicial, pouco uso dos registros e expectativas indevidas são riscos de aplicação presentes no acervo. TI e direção escolhem um recorte dentro da capacidade, explicam o acordo e observam o uso com as pessoas afetadas. Treinamento e gamificação não garantem adesão. Ajustar ferramenta ou registro quando o esforço não apoiar uma decisão.

Falta de direção exige alçada e decisão identificáveis; reunião sem decisão não resolve a lacuna. Requisitos ambíguos exigem conversa e critério testável. Falsa sensação de segurança exige conferir cobertura e teste; política ou compra não prova proteção. Biblioteca desatualizada exige curadoria somente se houver uso de assistência. Registrar dono, ação, evidência e próxima revisão para cada risco relevante.

Os percentuais, prazos e gates das versões anteriores eram propostas locais sem validação. Segurança urgente não espera nível de maturidade, implantação de quadro ou conclusão de outro módulo. A revisão de aplicação real continua necessária; testes deste repositório não comprovam efetividade organizacional.


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
