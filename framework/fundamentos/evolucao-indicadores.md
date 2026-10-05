# Como interpretar indicadores das versões anteriores

As versões GP-PME empregavam fórmulas diferentes sob o nome DAN. Não transportar valores antigos para a edição GEAR sem recuperar definição, entradas, unidades, período e método de estimativa.

## Três definições históricas

| Definição encontrada | Unidade | Tratamento nesta edição |
| --- | --- | --- |
| Custo de remediação / tamanho do ativo × fator de complexidade | Depende do numerador e do tamanho escolhido | Preservada como proposta histórica; não comparar horas por linha com reais por servidor |
| Custo anual de retrabalho atribuído à arquitetura / gasto anual de TI | Proporção no mesmo período | Indicador histórico de composição do gasto; diferente do esforço futuro de remediação |
| Estimativa monetária de remediação / orçamento anual de TI | Razão de valores monetários | Convenção local vigente, com escopo e premissas documentados |

O exemplo histórico de 100 horas, 10.000 linhas e fator 1,5 produz 0,015 **hora por linha**, não 1,5% de risco. O fator de complexidade não foi calibrado. O exemplo de R$ 20.000 de retrabalho em R$ 100.000 de gasto anual produz 20% de composição estimada do gasto; não demonstra que a remediação custará esse valor.

ATDx 2020 normaliza violações por elementos de código, com análise estatística; não valida essas fórmulas financeiras. EA Debt 2019 propõe uma definição contextual de dívida. As faixas locais 0,15 e 0,35 não diagnosticam segurança, probabilidade de falha ou saúde arquitetural. [F13–F14 e limites bibliográficos](../referencias/fontes.md).

## Benefício, custo e decisão

O rascunho de R$ 50.000 de investimento e R$ 25.000 de benefício anual chamava a razão 50% de ROI. Assumindo recorrência zero, doze meses estabilizados e nenhum outro custo, a razão bruta é 0,5 e o retorno líquido condicional é **−50%**. Com benefício distribuído igualmente e constante, o payback simples seria 24 meses; manter a hipótese por esse período não é resultado observado.

Refatoração, migração, automação, treinamento, licenças e transição entram na estimativa quando atribuíveis. Separar desembolso inicial, recorrência e capacidade interna; evitar contar duas vezes salários e horas ou contabilizar receita hipotética como despesa evitada. [Convenções financeiras vigentes](../indicadores/financeiros.md).

A antiga tabela DAN alta/baixa versus COT alto/baixo pode iniciar uma discussão, mas não determina investimento. Conferir obrigação, risco, dependências, alternativas, capacidade e sensibilidade. Um índice baixo não justifica adiar correção urgente; um índice alto não autoriza desativar serviço necessário.

## Migrar uma série antiga

Guardar a fórmula original com os dados. Recalcular na definição vigente somente quando as entradas forem suficientes. Se o numerador mudou, iniciar nova série e indicar a quebra de comparabilidade. A pessoa responsável pela estimativa confere a conta; a autoridade decide o investimento. Ausência de orçamento impede a DAN financeira, mas não impede registrar horas e discutir o problema.
