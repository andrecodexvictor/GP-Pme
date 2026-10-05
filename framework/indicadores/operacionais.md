# Indicadores operacionais

Escolha um indicador quando houver uma decisão a tomar. TI coleta os dados; o dono do serviço confirma o que foi medido; direção e TI definem tolerâncias. Uma meta sem janela, origem e responsável não permite avaliar a rotina.

## Definições

| Indicador | Cálculo e unidade | Limite de interpretação |
| --- | --- | --- |
| IDSC: disponibilidade de serviço crítico | `(horas observadas − horas indisponíveis) / horas observadas × 100`, em % | Definir serviço, horário coberto e exclusões; não somar incidentes simultâneos duas vezes |
| TMpR: tempo médio para restauração | Soma dos tempos de recuperação / incidentes encerrados, em horas | Informar quantidade e distribuição; a média pode ocultar um incidente longo |
| ISU: satisfação do usuário | Soma das notas / respostas válidas, em escala 1 a 5 | Informar taxa de resposta e pergunta; ausência de respostas é dado insuficiente |
| Trabalho iniciado | Quantidade por executor em andamento, teste ou bloqueio | Não confundir tamanho da fila com WIP |
| Tempo de fluxo | Conclusão menos início, na unidade escolhida | Informar política de pausa e itens ainda abertos |

## Coletar e revisar

1. Definir decisão e serviço: por exemplo, se a recuperação atende à necessidade do faturamento.
2. Escolher período e fonte. Preservar horários e identificador do incidente.
3. Validar domínios: horas observadas positivas, indisponibilidade entre zero e o período; duração não negativa; notas de 1 a 5.
4. Calcular e informar amostra, lacunas e exclusões.
5. Comparar com tolerância local e períodos comparáveis.
6. Registrar ação, responsável e data de revisão.

Sem incidentes encerrados, TMpR é **dado insuficiente**, não zero. Um período sem incidentes registrados pode indicar falta de coleta. Indicadores não substituem testes de restauração nem a avaliação de riscos.

## Metas e compatibilidade

As versões anteriores usavam disponibilidade >99,5%, TMpR <4 horas e ISU >4,5. São exemplos de metas locais, sem validade universal. A calculadora mantém esses padrões para compatibilidade e permite configuração; o resultado deve declarar as metas aplicadas. Igualdade no limite não satisfaz uma comparação estrita.

## DORA para entrega de software

As métricas DORA consultadas em 2026 são frequência de implantação, tempo de entrega de mudanças, tempo de recuperação de implantação com falha, taxa de falha de mudanças e taxa de retrabalho de implantação. Seu recorte é entrega de software. Não substituir TMpR de incidentes gerais pelo tempo de recuperação de uma implantação com falha. Consultar definições e contexto antes de incorporar uma métrica [F05](../referencias/fontes.md#f05), [F06](../referencias/fontes.md#f06).

Exemplo: 720 horas observadas e 2 horas de indisponibilidade produzem IDSC de 99,7222%. Dois incidentes restaurados em 1 e 3 horas produzem TMpR de 2 horas. Duas respostas 5 e 4 produzem ISU de 4,5; a amostra é pequena e não prova satisfação de todos.

Próxima leitura: [Indicadores financeiros](financeiros.md). Modelo: [Decisões e prioridades](../templates/decisoes-prioridades.md).

Consulta complementar: [indicadores de negócio e comparação da rotina](negocio-comparacao.md), com definições para custos, canais, entregas e autoatendimento.
