# Fluxogramas de decisão e execução

Os fluxos abaixo tornam visíveis decisão, execução, espera e retorno. Retângulos são ações; losangos são decisões; formas arredondadas delimitam entrada ou encerramento. “Sim” e “não” identificam o caminho escolhido. Eles resumem práticas locais do GEAR, sem substituir os critérios e alçadas dos guias.

## Da demanda ao encerramento

![Fluxo de demanda: reconhecer incidente crítico, conferir capacidade, executar, verificar e registrar o encerramento.](../../GP-Pme%20Article/assets/diagrams/demanda.svg)

1. Receber e registrar necessidade, serviço e responsável. Uma emergência é atendida e registrada assim que viável.
2. Se houver incidente crítico, acionar resposta e autoridade apropriadas. Encerrar somente após a verificação descrita no guia de incidentes.
3. Para a fila comum, conferir prioridade, dependências e critérios. Contar andamento, teste e bloqueio comprometido na capacidade por executor.
4. Se não houver capacidade acordada, manter motivo e revisão na fila. Retomar a decisão quando houver mudança de prioridade, dependência ou capacidade.
5. Executar o recorte autorizado e verificar a saída. Se houver lacuna, registrar e decidir a correção; o retorno à execução depende de autorização e capacidade.
6. Registrar evidência, motivo de encerramento e próximos passos. Cancelamento ou outra forma de encerramento precisa de justificativa, sem se apresentar como entrega aceita.

Bloqueio ou suspensão conserva histórico e relógio; o diagrama não autoriza ocultar trabalho iniciado para liberar WIP. Para critérios completos: [priorizar demandas](priorizar-demandas.md), [execução e serviços](../nucleo/execucao-servicos.md) e [entregar melhoria](entregar-melhoria.md).

## Resposta e recuperação

![Fluxo de incidente: registrar sinais, acionar alçada, verificar capacidade, responder, recuperar e conferir serviço ou alternativa.](../../GP-Pme%20Article/assets/diagrams/incidente.svg)

1. Registrar fatos, horário e incertezas; acionar responsável e autoridade sem aguardar causa confirmada.
2. Se a capacidade local for insuficiente, acionar fornecedor ou especialista pelos contatos conferidos. A resposta depende do ambiente e da alçada, com preservação de evidências.
3. Comunicar fatos verificados e próxima atualização. Recuperar o serviço ou preparar uma alternativa operacional.
4. Se a verificação com o dono do processo falhar, manter pendência, atualizar os afetados e reavaliar a recuperação. Uma alternativa aceita não significa que o serviço original voltou.
5. Registrar limitações, encerramento e correções atribuídas. Investigar causa e prevenção em tarefas ligadas ao incidente, quando necessário.

O fluxo não prescreve isolamento, desligamento ou formatação universais. Critérios, contatos e obrigação de comunicação permanecem no [guia de incidentes](tratar-incidentes.md) e no [plano breve](../templates/incidente.md). Fundamentos: NIST [F01](../referencias/fontes.md#f01), [F02](../referencias/fontes.md#f02) e CISA [F12](../referencias/fontes.md#f12); a sequência gráfica é uma adaptação local.

As figuras são vetoriais. Na tela pequena, a região permite rolagem horizontal e os passos textuais conservam o conteúdo para leitura. A imagem de rotina diária fornecida pelo usuário orientou as formas e as ramificações; suas atividades não fazem parte do método.
