# GEAR: Indicadores e primeiras melhorias: guia técnico

Edição editorial GEAR 2026.10. Framework de governança e gestão de TI para pequenas e médias empresas. Origem: GP-PME 6.0, 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor. Direitos conforme LICENSE.md. Caminho anterior preservado para compatibilidade.

## Percurso de leitura

- [Indicadores operacionais](#indicadores-operacionais)
- [Indicadores de negócio e comparação da rotina](#indicadores-de-negocio-e-comparacao-da-rotina)
- [Indicadores financeiros e hipóteses](#indicadores-financeiros-e-hipoteses)
- [Preparar a adoção e distribuir as primeiras ações](#preparar-a-adocao-e-distribuir-as-primeiras-acoes)
- [Conferir o cenário financeiro antigo](#conferir-o-cenario-financeiro-antigo)

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

Os guias antigos também atribuíam a DAN ao ATDx e o ROI do COT à dívida de arquitetura empresarial. ATDx normaliza violações por elementos de código e usa análise estatística; Hacks et al. propõem uma definição contextual com casos fictícios. Esses textos apoiam conceitos de dívida arquitetural, mas não as fórmulas financeiras ou faixas do GEAR. [F13](<../../framework/referencias/fontes.md#f13>) [F14](<../../framework/referencias/fontes.md#f14>)

Anterior: [Indicadores operacionais](<../../framework/indicadores/operacionais.md>). Aplicação: [Caso didático](<../../framework/exemplos/caso-didatico.md>).


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


## Conferir o cenário financeiro antigo

O guia supunha três horas diárias de atividade manual para dez pessoas e atribuía R$ 3.000 por mês ao esforço. Faltavam dias de trabalho, custo-hora e proporção recuperável para derivar esse valor. Os relatos ficam preservados como premissas incompletas; a conta financeira usa R$ 3.000/mês como benefício independente hipotético, sem inferir salário ou calendário.

Com R$ 9.000 de investimento inicial, recorrência zero, benefício estabilizado por doze meses e sem duplicação, a conta condicional resulta em benefício anual de R$ 36.000, razão bruta 4, ROI líquido de 300% e payback simples de três meses. A expressão antiga de 400% era benefício bruto sobre investimento. Se apenas metade do benefício ocorrer, ROI líquido anual de 100% e payback de seis meses; com benefício nulo, ROI de −100% e sem payback finito. O exemplo com R$ 500/mês de recorrência acima mostra outra hipótese, não um custo originalmente observado.

Nem automação nem nuvem demonstram economia realizada ou eliminação da dívida. Conferir esforço, licença, manutenção, adoção e benefício observado. DAN financeira, COT e ROI são instrumentos locais; artigos sobre dívida arquitetural não validam suas fórmulas por proximidade de tema.

## Fontes e continuidade

Fundamentos e limites: [referências completas](../../framework/referencias/fontes.md). Regra vigente: [documentação modular](../../framework/README.md). Próxima tarefa: [catálogo de guias](../../framework/guias/README.md). IA é opcional, inclusive na maturidade máxima. As fontes conceituais não validam automaticamente metas ou instrumentos locais.
