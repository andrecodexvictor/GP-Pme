# GEAR: Primeiros 30 dias

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: **Autor**: Manus AI (sob a direção de Andre Victor) **Versão**: 1.0 **Data**: 22 de Fevereiro de 2026

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Primeiros 30 dias](#primeiros-30-dias)
- [Preparar a adoção e distribuir as primeiras ações](#preparar-a-adocao-e-distribuir-as-primeiras-acoes)
- [Maturidade com evidências](#maturidade-com-evidencias)
- [Fichas de desenvolvimento das práticas](#fichas-de-desenvolvimento-das-praticas)
- [Indicadores de negócio e comparação da rotina](#indicadores-de-negocio-e-comparacao-da-rotina)

## Primeiros 30 dias

Este percurso ensina a iniciar o GEAR em uma equipe pequena. Ao final, a direção deve conseguir localizar a fila de TI, suas prioridades, os riscos mais urgentes e as evidências disponíveis. Trinta dias são uma janela de planejamento local; não garantem implantação completa nem avanço de maturidade.

### Preparar a adoção

O responsável por TI combina com a direção quem aprova prioridades e recursos. Escolhem um processo de negócio para acompanhar, um registro de demandas e um lugar para decisões. Não é necessário comprar uma plataforma. Antes de iniciar, confirmam tempo disponível, acesso aos responsáveis e autorização para os testes previstos.

A **verificação pré-projeto** decide se uma iniciativa específica deve começar: problema, patrocinador, viabilidade, risco e capacidade. É diferente da antiga “Fase Zero” de adoção. Um projeto pode ser recusado enquanto a rotina do GEAR continua funcionando.

### Semana 1: tornar o trabalho visível

1. Aplicar o [questionário de maturidade](<../../framework/adocao/maturidade.md>), registrando evidência e lacunas.
2. Escolher até três problemas prioritários com o dono do processo. Anotar o impacto observado, sem estimar ganhos como se já fossem resultados.
3. Criar a fila: A Fazer, Em Andamento, Em Teste e Concluído. Registrar executor, solicitante, prioridade e aceite em cada item.
4. Comunicar o registro oficial. Uma urgência recebida por telefone deve entrar na fila assim que o atendimento permitir.
5. Aplicar o limite inicial de três itens iniciados por executor. Testes e bloqueios entram na contagem; suspensões conservam histórico.

**Evidência:** fila com trabalho real e registro de quem decide. Se ninguém puder assumir a aprovação, resolver essa lacuna antes de ampliar o método.

### Semana 2: conhecer dependências e recuperação

Mapear primeiro os ativos e fornecedores que sustentam o processo escolhido. Registrar proprietário, dados tratados, acesso, suporte, backup e dependências. Essa priorização por criticidade substitui a interpretação literal de “inventário 80/20”.

Executar um [teste de restauração](<../../framework/guias/testar-restauracao.md>) autorizado, em ambiente seguro. Definir com o negócio o tempo e a perda de dados toleráveis. Documentar resultado, limitações e correções. Preparar uma orientação para uma dúvida recorrente, verificando-a com alguém que precise usá-la.

**Evidência:** inventário inicial, teste com resultado e instrução utilizável. Backup diário ou recuperação em 30 minutos só são requisitos se o contexto justificar essas escolhas.

### Semana 3: decidir e responder

Preencher o [plano de incidente](<../../framework/templates/incidente.md>), conferir contatos e exercitar um cenário simples. Reunir direção, TI e dono do processo para decidir prioridades, riscos aceitos e recursos. Uma revisão de 30 minutos a cada duas semanas é uma configuração inicial; ajustar quando não permitir decisões suficientes.

**Evidência:** responsáveis localizáveis, decisão com prazo e risco atribuído. Um documento assinado não comprova que a resposta funcionará; o exercício revela dependências.

### Semana 4: verificar e ajustar

Escolher os [indicadores](<../../framework/indicadores/operacionais.md>) que respondem às dúvidas reais da equipe. Registrar janela, origem e limitações. Reaplicar a maturidade com evidências da prática; dez respostas positivas não dispensam verificação de continuidade e responsabilidade.

Na revisão, decidir quais práticas manter, simplificar ou ampliar. Registrar próximos responsáveis e prazos. Se uma entrega ou teste não couber na janela, informar o motivo e reagendar, sem certificar uma transição inexistente.

**Evidência de conclusão do percurso:** comparação entre situação inicial e atual, pendências atribuídas e próxima revisão marcada. O percurso pode terminar com riscos ainda abertos.

### Exemplo de um começo possível

Uma empresa registra pedidos de acesso que antes chegavam por mensagens. O primeiro resultado verificável é a visibilidade de solicitante, aprovador e situação. O eventual efeito sobre tempo de atendimento precisa ser medido posteriormente. Consulte o [caso didático](<../../framework/exemplos/caso-didatico.md>) para acompanhar um percurso completo.

Fundamento: adoção proporcional e governança de riscos no NIST para pequenas empresas [F01](<../../framework/referencias/fontes.md#f01>); organização de tutorial conforme Diátaxis [F08](<../../framework/referencias/fontes.md#f08>). A janela de 30 dias e as semanas são propostas locais do GEAR.

Anterior: [Escopo](<../../framework/nucleo/escopo-principios.md>). Próxima leitura: [Maturidade](<../../framework/adocao/maturidade.md>).


## Preparar a adoção e distribuir as primeiras ações

Use este roteiro quando direção e TI já concordaram em tornar a rotina visível. Ele conserva o início em duas horas e os nove passos dos guias antigos como opções de planejamento. Durações e dias são parâmetros locais; confirmar disponibilidade, permissões e responsáveis antes de usá-los.

### Uma preparação de duas horas

O resultado esperado é um primeiro conjunto de registros e pendências. A preparação não comprova implantação, recuperação ou maturidade. Se houver incidente ou risco urgente, sua resposta pode alterar a agenda.

| Janela sugerida | Ação | Saída a conferir |
| --- | --- | --- |
| Primeiros 30 minutos | Escolher registro oficial e meio alternativo quando indisponível | Canal, responsável por captura e comunicado de transição |
| Próximos 30 minutos | Criar quadro e registrar demandas conhecidas | Solicitante, executor, situação, prioridade e lacunas |
| Próximos 30 minutos | Examinar prioridades com autoridade do negócio | Até três problemas escolhidos com motivo e capacidade |
| Últimos 30 minutos | Preparar contatos e alçadas de resposta | Minuta de PRI, contatos conferidos e pendências atribuídas |

Demandas recebidas por telefone ou conversa continuam acessíveis ao registro; uma emergência não aguarda o formulário. Não apagar tarefas por classificação de quadrante. Registrar recusa, adiamento ou pedido de informação com motivo. Contatos não fornecidos ficam pendentes. Imprimir o PRI pode ajudar no acesso durante indisponibilidade, mas seu conteúdo e autoridade precisam ser conferidos.

Limite inicial: até três itens iniciados por executor, incluindo teste e bloqueio sob sua responsabilidade. Uma equipe de uma pessoa concentra a execução em uma atividade de cada vez. Se a captura das demandas não terminar na janela, registrar cobertura e plano de continuação.

### Nove passos em uma janela de 30 dias

O percurso detalha os [primeiros 30 dias](<../../framework/adocao/primeiros-30-dias.md>). Os intervalos conservam a sequência histórica; alterar a ordem conforme dependências e risco. Segurança não precisa aguardar a segunda semana. Registrar mudança de data com motivo.

| Intervalo proposto | Ação | Evidência esperada |
| --- | --- | --- |
| Dias 1–2 | Aplicar maturidade e discutir problemas observados | Respostas com evidência, lacunas e prioridades atribuídas |
| Dias 3–5 | Organizar quadro e capacidade | Demandas conhecidas migradas; testes e bloqueios visíveis |
| Dias 6–7 | Comunicar registro oficial e alternativa | Pessoas sabem pedir ajuda e acompanhar a situação |
| Dias 8–10 | Preparar orientações recorrentes | FAQ testada por usuário, responsável e revisão combinada |
| Dias 11–14 | Mapear dependências críticas e testar restauração | Inventário inicial, requisitos de recuperação, resultado e limites |
| Dias 15–18 | Conferir e exercitar resposta | Contatos, alçadas, comunicação e lacunas do PRI |
| Dias 19–21 | Rever prioridades com o negócio | Decisões, recursos, responsáveis e próxima verificação |
| Dias 22–25 | Coletar indicadores úteis | Origem, janela, unidade, amostra e lacunas |
| Dias 26–30 | Comparar registros e planejar continuidade | Ações mantidas, ajustadas ou adiadas; próxima revisão |

Cinco orientações podem ser um começo para a FAQ, quando houver cinco necessidades recorrentes conhecidas. A quantidade não é critério de conclusão. Testar permissões e instruções de acesso; não fornecer credenciais no documento.

### Assistência opcional em cada etapa

TI pode pedir uma minuta de quadro, orientação, PRI, pauta ou relatório a uma ferramenta de IA com dados autorizados. A ferramenta pode organizar evidências fornecidas; não responde maturidade por suposição nem inventa contatos. Toda configuração real e integração exigem autorização, teste e revisão compatíveis com o efeito.

Para indicadores, usar cálculo determinístico e conferir unidades. Para FAQ ou bot, oferecer encaminhamento humano e medir resolução confirmada. O tempo total inclui preparação, conferência e correção. Sem IA, executar o mesmo roteiro com pessoas, quadros e registros.

### Encerrar a janela

TI apresenta registros e limitações; dono do processo confirma o que foi verificado; direção decide continuidade e risco. Pendências têm responsável e nova data. Não emitir certificação automática de nível 1 nem exigir DAN, nuvem, IA ou um projeto novo para encerrar a adoção inicial.

Fundamento conceitual de cobertura de riscos: NIST [F01](<../../framework/referencias/fontes.md#f01>). Agenda, número de passos e janelas são propostas locais, sem garantia de resultado no período.

Anterior: [Primeiros 30 dias](<../../framework/adocao/primeiros-30-dias.md>). Consulta: [Maturidade](<../../framework/adocao/maturidade.md>) e [comparação da rotina](<../../framework/indicadores/negocio-comparacao.md>).


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


## Fichas de desenvolvimento das práticas

Estas fichas preservam a matriz extensa dos guias anteriores em blocos consultáveis. Descrevem possibilidades de desenvolvimento por domínio, com entradas, saídas e observações. São propostas locais para planejar melhorias; não constituem critérios adicionais de pontuação ou uma escala validada.

O nível descritivo é calculado pelo [IM-TI vigente](<../../framework/adocao/maturidade.md>). Uma empresa pode ter práticas desenvolvidas de modo desigual. Usar uma ficha quando ela corresponde à lacuna observada, mesmo que o nível do total seja outro. IA é opcional em todas as fichas.

### Visão de consulta

| Nível descritivo | Foco de desenvolvimento possível | Conferência necessária |
| --- | --- | --- |
| 0: rotina pouco visível | Identificar responsáveis e o trabalho existente | O que está conhecido e o que falta registrar |
| 1: organização inicial | Tornar fila e controles consultáveis | Se os registros refletem a prática |
| 2: práticas repetidas | Decidir e executar com critérios e evidência | Lacunas de continuidade e alçada |
| 3: rotina acompanhada | Comparar resultados e investigar diferenças | Premissas, limites e efeitos observados |
| 4: práticas verificadas | Adaptar o método às mudanças do contexto | Sustentação das práticas e novos riscos |

### Ficha 0: conhecer a situação

**Governança.** Entradas: reclamações, demandas e restrições conhecidas. Ação: identificar quem pode decidir e quais acordos já existem. Saída: responsáveis, prioridades provisórias e lacunas. Observação: ausência de atas não comprova ausência de toda decisão.

**Execução.** Entradas: pedidos verbais, mensagens e trabalho já iniciado. Ação: reconciliar demandas sem duplicar e atribuir executor. Saída: fila inicial, bloqueios e alcance da captura. Medida possível: quantidade registrada e itens sem responsável.

**Segurança.** Entradas: serviços, contas, fornecedores e cópias conhecidos. Ação: identificar dependências e risco imediato. Saída: inventário inicial e verificação autorizada a planejar. Observação: desconhecer o backup exige investigar; não permite declarar perda ou probabilidade de ataque.

**Assistência opcional.** Organizar relatos em minuta com origem, sem preencher informações ausentes. Saída humana equivalente: registro das mesmas evidências.

### Ficha 1: organizar a rotina

**Governança.** Entradas: fila, responsáveis e primeiros dados. Ação: definir alçadas e uma revisão compatível com a necessidade. Saída: decisões atribuídas e próximas verificações. Medida possível: decisões com acompanhamento, sem exigir uma quantidade de atas.

**Execução.** Entradas: solicitações identificadas e capacidade disponível. Ação: aplicar estados, limite de trabalho e registro oficial; preparar orientação recorrente. Saída: cartões com critério de conclusão e FAQ verificada. Medidas: trabalho iniciado e tempo de fluxo, com lacunas declaradas.

**Segurança.** Entradas: inventário parcial, acesso e registros de cópia. Ação: conferir privilégios e proteção; distinguir execução de backup e restauração. Saída: cobertura, exceções e teste planejado ou executado. Um job aprovado não prova recuperação.

**Assistência opcional.** Rascunhar orientação ou triagem, com revisão e encaminhamento humano. Não exigir bot nem 40% de resolução para alcançar o nível.

### Ficha 2: repetir e verificar

**Governança.** Entradas: demandas, indicadores, risco e alternativas. Ação: revisar com direção e dono do processo, usando finalidades de negócio. Saída: decisão, recurso, motivo, prazo e responsável. Medidas: indicadores selecionados com tolerâncias locais, sem mínimos universais de IDSC ou ISU.

**Execução.** Entradas: solicitações e critérios de impacto, urgência e dependência. Ação: ordenar a fila e verificar entregas. Saída: aceite ou encerramento justificado, bloqueios e exceções de capacidade. Medidas: fluxo e restauração, mantidos separados.

**Segurança.** Entradas: dependências críticas, requisitos de recuperação e contatos. Ação: testar o escopo autorizado e exercitar o PRI. Saída: duração observada, resultado, limites e correções. RTO é objetivo; duração medida é resultado do teste. Nem trimestre nem 30 minutos são requisitos universais.

**Assistência opcional.** Reutilizar prompts revisados com contexto autorizado. Saída: proposta rastreável; a decisão continua atribuída a uma pessoa.

### Ficha 3: acompanhar efeitos

**Governança.** Entradas: cenários de custo, benefício e resultados observados. Ação: comparar hipóteses ao ocorrido e decidir recursos. Saída: revisão de investimento e roteiro de melhorias. DAN e COT só entram se ajudarem a decisão; estimativa não comprova retorno.

**Execução.** Entradas: problema, PRD e condição de retorno. Ação: testar melhoria delimitada com usuário. Saída: piloto verificado e decisão de continuar, ajustar ou encerrar. Medidas: tempo de lançamento, aceite e benefício observado, cada um com origem e período.

**Segurança.** Entradas: exceções de acesso, vulnerabilidades verificadas e mudanças do serviço. Ação: planejar correções por exposição e capacidade, conferindo configuração e dependências. Saída: correções verificadas e risco residual atribuído. Relatório de scanner isolado não comprova mitigação completa.

**Assistência opcional.** Elaborar PRD, histórias, código e teste por etapas revisadas. Saída: minuta ou artefato verificado; roteiro de teste não substitui sua execução.

### Ficha 4: adaptar com evidências

**Governança.** Entradas: mudanças de escala, serviço, fornecedor ou estratégia. Ação: rever alçadas, orçamento, dependências e método. Saída: plano atualizado com alternativas e riscos. Não exigir fusão empresarial, arquitetura em nuvem nem DAN abaixo de 0,15.

**Execução.** Entradas: histórico de capacidade, filas e entregas. Ação: adaptar limites, critérios e cadência, preservando comparabilidade quando possível. Saída: política revisada e acompanhamento. Não exigir TEIA acima de 60% ou qualquer automação.

**Segurança.** Entradas: testes, incidentes, acesso e obrigações aplicáveis. Ação: revisar cobertura, resposta e recuperação após mudanças. Saída: lacunas tratadas ou riscos aceitos por autoridade apropriada. Não definir excelência por “zero vazamentos” ou “zero paradas”; ausência de registro também pode ser lacuna de detecção.

**Assistência opcional.** Comparar utilidade, revisão, correção e permissões das ferramentas. Saída: manter, restringir ou retirar a assistência conforme evidências. Procedimentos manuais podem sustentar o nível máximo.

### Transformar uma lacuna em ação

1. Vincular a ação a uma evidência ausente ou insuficiente, sem presumir que todo o domínio falhou.
2. Definir responsável, recurso, dependência, prazo e como verificar.
3. Selecionar até três ações compatíveis com a capacidade. Emergências podem mudar a ordem.
4. Executar e registrar resultado, incluindo falha ou limitação.
5. Rever a prática na janela combinada e reaplicar a pergunta correspondente.

As antigas listas de transição passam a ser opções: capturar demandas, controlar trabalho iniciado, verificar FAQ, testar recuperação, conferir PRI, rever prioridades ou testar melhoria. Prompts e agentes só entram quando escolhidos. Uma assinatura registra aprovação; não certifica avanço sustentado.

Responsável: TI, com verificação do dono do processo e alçada da direção. Entrada: resultado por pergunta e evidências. Saída: plano de melhoria e histórico preservado. Concluir quando cada ação selecionada tem resultado verificável ou pendência atribuída.

Anterior: [Maturidade](<../../framework/adocao/maturidade.md>). Modelo: [Registro de maturidade](<../../framework/templates/maturidade.md>). Para compreender: [Origens e adaptações](<../../framework/fundamentos/origens-adaptacoes.md>).


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


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
