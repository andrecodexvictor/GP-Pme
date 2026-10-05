# GEAR: Início e diagnóstico

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: **Autor**: Manus AI (sob a direção de Andre Victor) **Versão**: 1.0 (Quick Start) **Data**: 21 de Fevereiro de 2026

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Escopo e princípios](#escopo-e-principios)
- [Primeiros 30 dias](#primeiros-30-dias)
- [Preparar a adoção e distribuir as primeiras ações](#preparar-a-adocao-e-distribuir-as-primeiras-acoes)
- [Maturidade com evidências](#maturidade-com-evidencias)
- [Fichas de desenvolvimento das práticas](#fichas-de-desenvolvimento-das-praticas)
- [Lista de tarefas e verificação](#lista-de-tarefas-e-verificacao)
- [PRD curto e registro de aceite](#prd-curto-e-registro-de-aceite)
- [Plano breve de resposta a incidente](#plano-breve-de-resposta-a-incidente)
- [Matriz de impacto e urgência](#matriz-de-impacto-e-urgencia)
- [Prompts para quatro funções de assistência](#prompts-para-quatro-funcoes-de-assistencia)

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

O núcleo define termos e invariantes. Os guias explicam tarefas. Templates facilitam o registro. Fundamentos apresentam as adaptações e seus limites. Essa separação atende a necessidades distintas de documentação, seguindo a orientação Diátaxis. [F08](<../../framework/referencias/fontes.md#f08>)

Uma equipe pode usar software de chamados, planilha ou quadro físico. O suporte escolhido precisa preservar responsável, situação, critério de conclusão e evidência. Operação manual significa independência de uma plataforma de gestão, não ausência de tecnologia para executar backup ou proteger contas.

### Situação da evidência

GEAR é uma composição autoral de práticas. Cenários demonstrativos e testes de software comprovam apenas o que efetivamente verificam. Metas de prazo, percentuais de melhoria e faixas de indicadores não são resultados médios esperados nem parâmetros normativos universais.

A avaliação acadêmica prevista utiliza casos sintéticos pareados. Até a produção de dados, o protocolo permanece prospectivo. Uma comparação com referências adaptadas precisa declarar escopo e condições de cada configuração, sem construir alternativas deliberadamente fracas.

Próxima leitura: [Governança e direção](<../../framework/nucleo/governanca.md>). Para executar: [Primeiros 30 dias](<../../framework/adocao/primeiros-30-dias.md>).


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


## Lista de tarefas e verificação

Use para uma mudança ou rotina que precise de passos atribuídos. TI organiza dependências e capacidade; executor registra resultado; dono do processo aceita o efeito pertinente. A lista complementa o quadro, sem criar uma segunda fila divergente.

### Preparar o recorte

- Iniciativa/rotina, período e responsável geral: [preencher]
- PRD ou decisão que autoriza, escopo e exclusões: [preencher]
- Permissões, dependências, ambiente e condição de retorno: [preencher]

| ID e ação | Executor | Dependência | Estado | Critério e modo de verificar | Resultado/evidência |
| --- | --- | --- | --- | --- | --- |
| [preencher] | | | [A Fazer/Em Andamento/Em Teste/Concluído] | | |

Bloqueio ou suspensão: [item, motivo, início, responsável pela próxima ação e revisão]. Manter o relógio e o histórico de trabalho iniciado. Contar andamento, teste e bloqueio comprometido no WIP por executor; marcar início de tarefa não cria capacidade adicional.

### Opções de organização

Agrupar por preparação e ambiente; desenvolvimento ou configuração; verificação técnica e de negócio; disponibilização e acompanhamento. Essas são opções do modelo antigo, sem impor quatro fases ou quatorze dias a toda atividade. Segurança e requisitos podem precisar de conferência antes da execução, não apenas ao final.

- Preparação: verificar acesso e dependências em ambiente autorizado.
- Implementação: executar o recorte acordado e guardar alterações.
- Verificação: testar critérios, acesso, falhas relevantes e retorno conforme o efeito.
- Disponibilização: confirmar autorização, comunicação, operação e acompanhamento.

Exemplos fictícios de critérios: membros autorizados acessam um repositório e demais não; um formulário informa um campo obrigatório ausente; mensagem de teste chega ao destino autorizado. Definir ambiente, amostra e prazo necessários; a antiga referência a dez segundos não é padrão de pagamentos ou e-mail. Mensagem de console não comprova recebimento externo.

### Encerrar e revisar

Registrar teste realizado, pessoa que verificou, aceite ou motivo de encerramento. Uma assinatura registra aprovação, sem substituir teste. Nem toda tarefa exige publicação ou implantação. Guardar pendências e condição de revisão posterior do benefício.

As marcações antigas `[ ]`, `[/]` e `[x]` podem ser mantidas como legenda em ferramentas que as suportem. Elas não representam sozinhas teste, bloqueio ou aceite; conservar esses campos explicitamente. Não apresentar `[/]` como checkbox Markdown padrão.

Saída: lista atualizada vinculada ao quadro. Concluir quando resultados e pendências são localizáveis, com responsável. Referência de uso: [entregar melhoria](<../../framework/guias/entregar-melhoria.md>). Próximo modelo: [PRD e aceite](<../../framework/templates/prd-aceite.md>).


## PRD curto e registro de aceite

Use para uma melhoria delimitada. Dono do processo valida a necessidade; TI confere viabilidade; executor verifica o comportamento; usuário ou dono do processo aceita a saída.

### Definição

- Identificador, versão, responsável e data: [preencher]
- Problema observado e evidência: [preencher]
- Usuário/processo beneficiado: [preencher]
- Resultado esperado e hipótese de benefício: [preencher]
- Escopo incluído: [preencher]
- Exclusões: [preencher]
- Restrições, permissões e dependências: [preencher]
- Risco, proprietário e mitigação: [preencher]
- Recursos e prazo estimados: [preencher]

### Verificação

| Critério observável | Como testar | Quem verifica | Resultado/evidência |
| --- | --- | --- | --- |
| [Dado… quando… então…] | | | |

**Plano de retorno:** [como desfazer ou mitigar falha; responsável].

**Aceite:** [pessoa, data, critérios atendidos e pendências].

**Acompanhamento do benefício:** [indicador, linha de base, janela, fonte e decisão futura]. Aceite funcional não comprova benefício financeiro. Se o recorte não couber na capacidade, renegociar escopo ou prazo antes de iniciar.

### Histórias e requisitos operacionais

História: `Como [perfil real], quero [comportamento] para [finalidade]`. Usar quantas forem necessárias ao recorte, sem inventar persona, fluxo ou regra de negócio para atingir duas ou três histórias. Requisito desconhecido permanece como pergunta com responsável.

| Requisito | Condição e limite acordados | Ambiente e modo de verificar | Responsável |
| --- | --- | --- | --- |
| Desempenho | [ação, quantidade de dados e tempo] | [dispositivo, rede, carga e amostra] | |
| Acesso/segurança | [perfis, permissões e exceções] | [teste autorizado de permitido/negado] | |
| Usabilidade | [tarefa, usuários e dispositivos] | [verificação com usuário e limitações] | |

Uma meta de dois segundos precisa dessas condições. Erro de formulário deve ser identificável e permitir correção; não usar apenas cor para descrevê-lo. Excluir uma funcionalidade exige acordo e consequência declarados, sem retirar um requisito necessário para que o recorte seja utilizável.

### Exemplos fictícios para iniciar uma conversa

- Financeiro: baixar extratos de três bancos e digitar valores em uma planilha consome tempo e pode gerar erro. O relato antigo de três horas por dia é hipótese do exemplo; conferir frequência, acesso, formatos e custo antes de calcular benefício.
- Comercial: leads de um formulário demoram a receber resposta. A proposta de encaminhá-los ao vendedor exige regras de atribuição, permissão, horário e teste de entrega; o relato de dois dias e venda perdida não é medição do projeto.
- Suporte: pedidos por mensagens ficam dispersos. Definir captura e acompanhamento, preservando acesso à ajuda; não supor que metade das tarefas foi perdida.

Outros exemplos dos modelos anteriores incluíam iniciar atendimento de um lead, informar campo obrigatório ausente e acompanhar pedido. São comportamentos a discutir, sem obrigação de integrar WhatsApp, coletar CPF ou criar aplicativo. Nenhuma história comprova benefício antes da avaliação.

### Conferir o preenchimento

TI e negócio descrevem o problema, acordam critérios antes de implementar, delimitam escopo e identificam quem aprova. Uma conversa de quinze ou vinte minutos pode preparar a minuta; ampliar quando houver lacunas. Uma ou duas páginas são preferência de síntese, com evidências e detalhes vinculados. Um piloto de duas semanas depende de capacidade e escopo, sem garantia universal.

Assistência opcional: [contrato de requisitos e entrega](<../../framework/templates/prompts-assistencia.md#requisitos-e-entrega>). A IA pode preparar propostas; dono do processo aprova regras e aceite, e TI confere viabilidade. Não preencher solicitante, data ou orçamento desconhecidos por inferência.


## Plano breve de resposta a incidente

Preparar antes de uma ocorrência. Durante o incidente, usar o registro para coordenar ações e preservar evidências. Segurança ou TI mantém o plano; direção confirma alçadas; dono do serviço define tolerância de interrupção.

- Serviço e dados afetados: [preencher]
- Responsável e substituto: [preencher]
- Contatos conferidos em: [data; TI, fornecedor, direção, jurídico quando aplicável]
- Como reconhecer e classificar: [impacto e critério local]
- Quem pode isolar, suspender acesso e autorizar recuperação: [preencher]
- Onde registrar horários, decisões e evidências: [preencher]
- Comunicação: [destinatários, canal, frequência, aprovador]
- Recuperação: [cópia, dependências, ambiente, teste de integridade e aceite]
- Obrigações a avaliar: [competência responsável; não improvisar requisito legal]

### Durante e depois

1. Registrar descoberta, impacto conhecido e incertezas.
2. Acionar responsáveis; conter conforme autorização e preservar evidências.
3. Atualizar negócio com fatos verificados e próxima atualização.
4. Recuperar em condição segura e conferir serviço com seu dono.
5. Registrar encerramento, limitações e correções atribuídas.

**Exercício:** [cenário, data, participantes, resultado e próxima revisão]. Não considerar o plano testado só por ter sido assinado. Não colocar credenciais no documento.

Fundamento: orientação CISA [F12](<../../framework/referencias/fontes.md#f12>), adaptada a um registro breve do GEAR.


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


## Prompts para quatro funções de assistência

Use quando a equipe escolhe assistência por IA para uma tarefa delimitada. Estes textos preservam as quatro funções do capítulo técnico anterior; não descrevem a quantidade de especialistas de software nem autorizam execução. Quem prepara informa contexto e dados autorizados; quem tem alçada revisa a saída. Uma equipe pode executar a mesma tarefa sem IA.

### Direção e prioridades

```text
Tarefa: preparar uma pauta ou minuta de decisão do GEAR.
Contexto: [processo, demandas, capacidade, decisões anteriores e riscos].
Dados autorizados: [origem, janela, unidades e limitações].
Autoridade de decisão: [pessoa e alçada].
Saída: problema, alternativas, finalidade de negócio, recurso necessário,
risco, responsável, prazo, evidência esperada e próxima revisão.
Relacionar a iniciativa a receita, custos, experiência ou resiliência,
declarando hipótese de benefício e efeitos secundários quando houver.
Usar português direto, títulos informativos e registro breve consultável.
Informar dados insuficientes e decisões pendentes. Conferir cálculos com
regra determinística; indicar fontes externas no ponto da afirmação.
A pessoa responsável revisa a pauta; a autoridade identificada decide.
```

### Requisitos e entrega

```text
Tarefa: preparar PRD e critérios verificáveis para uma melhoria do GEAR.
Contexto: [problema observado, usuário e processo beneficiado].
Dados autorizados: [fontes e evidências disponíveis].
Restrições: [permissões, dependências, recurso, capacidade e prazo].
Saída: problema, hipótese, escopo, exclusões, histórias de usuário,
critérios Dado/Quando/Então, riscos, teste, retorno e aceite esperado.
Uma ou duas semanas podem orientar um piloto se o escopo couber na
capacidade informada. Se faltar informação, registrar a pergunta e seu
responsável. Estimativas devem ter origem, unidade e incerteza.
Conferir cada etapa antes de preparar a seguinte. Código inicial e roteiro
de teste são propostas; registrar separadamente execução e resultado.
Dono do processo aprova requisitos e aceite; TI confere viabilidade.
```

### Segurança e continuidade

```text
Tarefa: preparar análise de lacunas ou plano breve de resposta do GEAR.
Contexto: [serviço, ativos, dependências, risco observado e controles].
Dados autorizados: [relato, configuração, evidência e limites de acesso].
Autoridade: [quem decide contenção, comunicação e recuperação].
Saída: fatos, hipóteses, dados insuficientes, opções de tratamento,
responsável, contatos a conferir, verificação e risco residual.
Priorizar conforme criticidade do serviço, sem usar 80/20 como medida de
risco. Comparar alternativas por cobertura, esforço e manutenção.
Conferir CVEs e fontes primárias antes de citar uma vulnerabilidade.
Propor contenção apropriada ao ambiente, preservando evidências. A pessoa
com alçada autoriza a ação; o executor verifica recuperação com o negócio.
Dez verificações locais não equivalem ao NIST CSF ou CIS IG1 completos.
```

### Indicadores e revisão

```text
Tarefa: conferir premissas, unidades, cálculos e referências do GEAR.
Entrada: [documento, dados, período, moeda, origem e limitações].
DAN financeiro local = custo estimado de refatoração / orçamento anual TI.
Indicar método, escopo e incerteza; não atribuir faixas universais de risco.
ROI líquido no período = (benefício bruto - recorrência - investimento)
/ investimento * 100. Razão bruta = benefício bruto / investimento.
Payback simples mensal = investimento / benefício líquido mensal positivo,
somente se fluxos forem constantes. Sem benefício positivo, não é finito.
Horas liberadas são capacidade potencial salvo redução de despesa comprovada.
Manter precisão no cálculo e declarar arredondamento na apresentação.
Conferir a afirmação na fonte citada e distinguir proposta, simulação e
resultado observado. Se faltar moeda, custo ou período, registrar a lacuna;
informar horas isoladamente não permite afirmar ROI financeiro.
Saída: memória de cálculo, divergências, incerteza e revisão humana necessária.
```

### Conferir o uso

Aplicar o [registro de revisão](<../../framework/templates/revisao-ia.md>). Um texto aprovado deve permitir localizar fatos, premissas, fontes e pessoa responsável. A adesão do prompt a um formato não comprova correção da saída.

Origem: quatro system prompts em `GP-PME antigravity/GP-Pme complete/Capitulo_6_Motor_de_IA_e_Engenharia_de_Prompts.md`. As instruções foram revistas para retirar garantia de proteção, faixas financeiras sem suporte e prazo obrigatório de MVP. São contratos locais de assistência. Convenções: [financeiros](<../../framework/indicadores/financeiros.md>); contexto: [usar IA](<../../framework/guias/usar-ia.md>).


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
