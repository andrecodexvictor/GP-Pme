# Tratar um incidente

Use quando há interrupção de serviço ou suspeita de comprometimento que exige coordenação. A pessoa que recebe o relato inicia o registro; a autoridade definida no plano decide contenção e comunicação; o executor técnico verifica a recuperação. Entrada: relato, serviços afetados, contatos e plano vigente. Saída: serviço recuperado ou alternativa acordada, decisões registradas e ações posteriores identificadas.

## Reconhecer e avaliar

Registrar momento de identificação, sinais observados, serviço e usuários afetados. Distinguir fato de hipótese. “Sistema indisponível” é observação; “ataque de ransomware” exige evidência adicional. A falta de certeza não impede acionar o responsável.

Estimar impacto e comunicar à autoridade competente. Se o caso excede a capacidade local, acionar fornecedor ou especialista conforme os contatos do plano. A pessoa afetada não precisa preencher um formulário inacessível para receber ajuda.

## Conduzir a resposta

1. Identificar quem coordena e como a equipe atualizará a situação.
2. Registrar prioridades, trabalho suspenso e exceção de capacidade.
3. Avaliar contenção apropriada ao ambiente e preservar informações necessárias à investigação. Não aplicar formatação ou desligamento como regra automática.
4. Comunicar estado e alternativa operacional aos afetados, evitando declarar causa não confirmada.
5. Recuperar a partir de uma condição conhecida e verificar serviço, dados e dependências com o dono do processo.
6. Registrar horários, decisões, evidências e necessidade de acompanhamento.

As seis funções do CSF articulam governança, identificação, proteção, detecção, resposta e recuperação; elas não oferecem um único roteiro de ações técnicas para todo incidente. [F01](../referencias/fontes.md#f01) [F02](../referencias/fontes.md#f02)

## Verificar recuperação

Confirmar que o processo necessário funciona e que a equipe conhece restrições temporárias. O desaparecimento de uma mensagem de erro não é suficiente para encerrar. Se uma alternativa foi adotada, declarar se o serviço original segue pendente.

O relógio de resolução começa no registro definido para a métrica e termina na condição de encerramento acordada. Registrar também o momento de identificação quando diferente. Não excluir incidentes longos de um indicador sem mostrar o critério.

## Rever e prevenir recorrência

Preparar revisão proporcional: o que ocorreu, quais decisões ajudaram, onde faltou informação e qual ação tem responsável. Correção definitiva pode ser uma melhoria vinculada ao incidente. “Causa ainda não confirmada” é uma conclusão válida, com próximo passo.

Modelo: [Plano de resposta](../templates/incidente.md). Próxima tarefa: [Testar restauração](testar-restauracao.md).
