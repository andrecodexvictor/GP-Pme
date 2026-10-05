# Uma adoção ilustrativa

Este caso é fictício e serve para exercitar os registros. Não é estudo de campo, depoimento ou resultado médio esperado. A empresa do exemplo tem 25 pessoas, um responsável por TI e suporte terceirizado; depende de um sistema de pedidos para faturar.

## Situação inicial

Pedidos de acesso chegam por mensagem, falhas são resolvidas sem horário registrado e há backup com status de sucesso, mas sem teste recente. Direção e TI escolhem acompanhar o processo de faturamento. O dono do processo confirma impacto; TI organiza as dependências e o fornecedor confirma suas responsabilidades.

## Uma decisão de prioridade

Há três demandas: corrigir acesso indevido, testar recuperação e automatizar um relatório. A primeira requer contenção conforme impacto; o teste verifica uma dependência crítica; a automação pode aguardar capacidade. A matriz de impacto e urgência ajuda a discutir; esforço e dependências são registrados separadamente. Risco e obrigação impedem uma ordenação puramente aritmética.

TI registra aprovador, executor e aceite. Duas tarefas em execução e uma em teste já ocupam o limite inicial de três. Uma quarta melhoria permanece na fila. Quando surge incidente crítico, a autoridade registra a exceção e qual trabalho foi suspenso, mantendo seu histórico e o bloqueio visíveis.

## Recuperação e aprendizado

O teste autorizado restaura uma cópia de dados em ambiente separado. A verificação encontra uma dependência de licença que impede iniciar o serviço. A conclusão correta é “dados restaurados; serviço ainda não recuperado”. O fornecedor assume a correção e outro teste é marcado. Não há declaração de continuidade comprovada.

## Hipótese financeira

O relatório consome 20 horas/mês estimadas por observação. Atribuir R$ 50/hora produz R$ 1.000/mês de capacidade potencial. Investimento de R$ 3.000 e manutenção de R$ 100/mês, se as 20 horas forem liberadas integralmente, dão benefício bruto anual de R$ 12.000, custo recorrente de R$ 1.200, ROI líquido estimado de 260% e payback simples de 3,33 meses.

Se apenas metade das horas for liberada, benefício de R$ 500/mês: ROI líquido estimado de 60% e payback de 7,5 meses. Se as horas liberadas não reduzirem despesa, os valores representam capacidade, e não economia realizada. O benefício precisa de medição posterior e não pode ser lançado como receita da empresa.

## Revisão

Ao fim da janela, a equipe compara registros e evidências por pergunta de maturidade. Pode ter melhorado a visibilidade da fila sem concluir a recuperação. Registra esse resultado parcial, responsáveis e próxima decisão. O aprendizado útil é localizar a lacuna e tratá-la, sem forçar uma narrativa de sucesso.

Práticas: [Priorizar](../guias/priorizar-demandas.md), [Testar restauração](../guias/testar-restauracao.md), [Entregar melhoria](../guias/entregar-melhoria.md). Convenções: [Financeiros](../indicadores/financeiros.md).
