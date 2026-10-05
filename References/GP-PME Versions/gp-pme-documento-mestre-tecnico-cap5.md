# GEAR: Indicadores e decisão financeira

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: Sem autoria, versão ou data declaradas neste arquivo; não atribuídas por inferência.

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Indicadores financeiros e hipóteses](#indicadores-financeiros-e-hipoteses)
- [Indicadores operacionais](#indicadores-operacionais)
- [Indicadores de negócio e comparação da rotina](#indicadores-de-negocio-e-comparacao-da-rotina)
- [Como interpretar indicadores das versões anteriores](#como-interpretar-indicadores-das-versoes-anteriores)

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


## Como interpretar indicadores das versões anteriores

As versões GP-PME empregavam fórmulas diferentes sob o nome DAN. Não transportar valores antigos para a edição GEAR sem recuperar definição, entradas, unidades, período e método de estimativa.

### Três definições históricas

| Definição encontrada | Unidade | Tratamento nesta edição |
| --- | --- | --- |
| Custo de remediação / tamanho do ativo × fator de complexidade | Depende do numerador e do tamanho escolhido | Preservada como proposta histórica; não comparar horas por linha com reais por servidor |
| Custo anual de retrabalho atribuído à arquitetura / gasto anual de TI | Proporção no mesmo período | Indicador histórico de composição do gasto; diferente do esforço futuro de remediação |
| Estimativa monetária de remediação / orçamento anual de TI | Razão de valores monetários | Convenção local vigente, com escopo e premissas documentados |

O exemplo histórico de 100 horas, 10.000 linhas e fator 1,5 produz 0,015 **hora por linha**, não 1,5% de risco. O fator de complexidade não foi calibrado. O exemplo de R$ 20.000 de retrabalho em R$ 100.000 de gasto anual produz 20% de composição estimada do gasto; não demonstra que a remediação custará esse valor.

ATDx 2020 normaliza violações por elementos de código, com análise estatística; não valida essas fórmulas financeiras. EA Debt 2019 propõe uma definição contextual de dívida. As faixas locais 0,15 e 0,35 não diagnosticam segurança, probabilidade de falha ou saúde arquitetural. [F13–F14 e limites bibliográficos](<../../framework/referencias/fontes.md>).

### Benefício, custo e decisão

O rascunho de R$ 50.000 de investimento e R$ 25.000 de benefício anual chamava a razão 50% de ROI. Assumindo recorrência zero, doze meses estabilizados e nenhum outro custo, a razão bruta é 0,5 e o retorno líquido condicional é **−50%**. Com benefício distribuído igualmente e constante, o payback simples seria 24 meses; manter a hipótese por esse período não é resultado observado.

Refatoração, migração, automação, treinamento, licenças e transição entram na estimativa quando atribuíveis. Separar desembolso inicial, recorrência e capacidade interna; evitar contar duas vezes salários e horas ou contabilizar receita hipotética como despesa evitada. [Convenções financeiras vigentes](<../../framework/indicadores/financeiros.md>).

A antiga tabela DAN alta/baixa versus COT alto/baixo pode iniciar uma discussão, mas não determina investimento. Conferir obrigação, risco, dependências, alternativas, capacidade e sensibilidade. Um índice baixo não justifica adiar correção urgente; um índice alto não autoriza desativar serviço necessário.

### Migrar uma série antiga

Guardar a fórmula original com os dados. Recalcular na definição vigente somente quando as entradas forem suficientes. Se o numerador mudou, iniciar nova série e indicar a quebra de comparabilidade. A pessoa responsável pela estimativa confere a conta; a autoridade decide o investimento. Ausência de orçamento impede a DAN financeira, mas não impede registrar horas e discutir o problema.


## Rever riscos de adoção

Resistência, sobrecarga inicial, pouco uso dos registros e expectativas indevidas são riscos de aplicação presentes no acervo. TI e direção escolhem um recorte dentro da capacidade, explicam o acordo e observam o uso com as pessoas afetadas. Treinamento e gamificação não garantem adesão. Ajustar ferramenta ou registro quando o esforço não apoiar uma decisão.

Falta de direção exige alçada e decisão identificáveis; reunião sem decisão não resolve a lacuna. Requisitos ambíguos exigem conversa e critério testável. Falsa sensação de segurança exige conferir cobertura e teste; política ou compra não prova proteção. Biblioteca desatualizada exige curadoria somente se houver uso de assistência. Registrar dono, ação, evidência e próxima revisão para cada risco relevante.

Os percentuais, prazos e gates das versões anteriores eram propostas locais sem validação. Segurança urgente não espera nível de maturidade, implantação de quadro ou conclusão de outro módulo. A revisão de aplicação real continua necessária; testes deste repositório não comprovam efetividade organizacional.


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
