# GEAR: Governança e direção: guia técnico

Edição editorial GEAR 2026.10. Framework de governança e gestão de TI para pequenas e médias empresas. Origem: GP-PME 5.2, 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor. Direitos conforme LICENSE.md. Caminho anterior preservado para compatibilidade.

## Percurso de leitura

- [Governança e direção](#governanca-e-direcao)
- [Conduzir uma revisão de direção](#conduzir-uma-revisao-de-direcao)
- [Registro de responsabilidades](#registro-de-responsabilidades)
- [Decisão e prioridade](#decisao-e-prioridade)
- [Indicadores operacionais](#indicadores-operacionais)
- [Preparar uma pauta com assistência opcional](#preparar-uma-pauta-com-assistencia-opcional)

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

As métricas DORA consultadas em 2026 são frequência de implantação, tempo de entrega de mudanças, tempo de recuperação de implantação com falha, taxa de falha de mudanças e taxa de retrabalho de implantação. Seu recorte é entrega de software. Não substituir TMpR de incidentes gerais pelo tempo de recuperação de uma implantação com falha. Consultar definições e contexto antes de incorporar uma métrica [F05](<../../framework/referencias/fontes.md#f05>), [F06](<../../framework/referencias/fontes.md#f06>).

Exemplo: 720 horas observadas e 2 horas de indisponibilidade produzem IDSC de 99,7222%. Dois incidentes restaurados em 1 e 3 horas produzem TMpR de 2 horas. Duas respostas 5 e 4 produzem ISU de 4,5; a amostra é pequena e não prova satisfação de todos.

Próxima leitura: [Indicadores financeiros](<../../framework/indicadores/financeiros.md>). Modelo: [Decisões e prioridades](<../../framework/templates/decisoes-prioridades.md>).

Consulta complementar: [indicadores de negócio e comparação da rotina](<../../framework/indicadores/negocio-comparacao.md>), com definições para custos, canais, entregas e autoatendimento.


## Preparar uma pauta com assistência opcional

TI pode fornecer demandas, decisões anteriores e dados autorizados para uma minuta de pauta. A pessoa responsável confere origem, lacunas, alternativas e alçadas antes da revisão. Uma meta de reduzir despesa em 5% só integra a pauta quando foi acordada com o negócio; não é meta do método. Sugestões de iniciativas precisam de custo, dependência, risco e modo de verificar benefício. Não há prazo garantido de dois minutos para produzir ou conferir o briefing.

Uma página é preferência de síntese, ajustável ao contexto. Detalhes e evidências permanecem consultáveis. RACI registra responsabilidade humana; uma ferramenta de IA não assume a aprovação nem substitui o executor responsável.

## Fontes e continuidade

Fundamentos e limites: [referências completas](../../framework/referencias/fontes.md). Regra vigente: [documentação modular](../../framework/README.md). Próxima tarefa: [catálogo de guias](../../framework/guias/README.md). IA é opcional, inclusive na maturidade máxima. As fontes conceituais não validam automaticamente metas ou instrumentos locais.
