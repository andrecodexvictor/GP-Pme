# GEAR: Maturidade com evidências: guia técnico

Edição editorial GEAR 2026.10. Framework de governança e gestão de TI para pequenas e médias empresas. Origem: GP-PME 1.0, 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor. Direitos conforme LICENSE.md. Caminho anterior preservado para compatibilidade.

## Percurso de leitura

- [Maturidade com evidências](#maturidade-com-evidencias)
- [Fichas de desenvolvimento das práticas](#fichas-de-desenvolvimento-das-praticas)
- [Registro de maturidade](#registro-de-maturidade)
- [Planejar reaplicações](#planejar-reaplicacoes)

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


## Registro de maturidade

Preencher com TI e dono do processo usando o [questionário](<../../framework/adocao/maturidade.md>). Comparar apenas aplicações com contexto e janela conhecidos.

**Organização/processo:** [preencher]  
**Data, janela de evidência e avaliadores:** [preencher]

| Pergunta | Resposta 0/1 | Evidência, data e limite | Ação quando insuficiente |
| --- | --- | --- | --- |
| 1. Registro e responsável | | | |
| 2. Capacidade e fluxo | | | |
| 3. Orientações verificadas | | | |
| 4. Prioridades decididas | | | |
| 5. Escopo e aceite | | | |
| 6. Dependências críticas | | | |
| 7. Recuperação testada | | | |
| 8. Acesso controlado | | | |
| 9. Indicadores rastreáveis | | | |
| 10. Revisão responsável | | | |

**IM-TI e nível descritivo:** [soma e faixa].  
**Mudanças em relação à aplicação anterior:** [prática, evidência e contexto].  
**Até três ações prioritárias:** [responsável e prazo].  
**Lacunas críticas e risco aceito:** [aprovação e motivo].  
**Próxima revisão:** [data e responsável].

Concluir com evidências consultáveis e pendências atribuídas. Este registro não constitui certificação nem exige IA.


## Planejar reaplicações

Aplicar no início, depois de mudanças relevantes e na janela de revisão acordada. O intervalo antigo de seis meses é uma possibilidade, não requisito normativo. Preservar edição, evidência por pergunta, observações e plano; comparar somente depois de conferir diferenças de instrumento e contexto.

Direção aprova recursos e risco; dono do processo verifica efeitos; TI organiza a aplicação. O objetivo é localizar lacunas e sustentar a prática, sem promoção presumida do profissional, comprovação de segurança pelo total ou certificação por assinatura.

## Fontes e continuidade

Fundamentos e limites: [referências completas](../../framework/referencias/fontes.md). Regra vigente: [documentação modular](../../framework/README.md). Próxima tarefa: [catálogo de guias](../../framework/guias/README.md). IA é opcional, inclusive na maturidade máxima. As fontes conceituais não validam automaticamente metas ou instrumentos locais.
