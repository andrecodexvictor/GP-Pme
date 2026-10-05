# GEAR: Plano de resposta a incidentes

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: Sem autoria, versão ou data declaradas neste arquivo; não atribuídas por inferência.

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Plano breve de resposta a incidente](#plano-breve-de-resposta-a-incidente)
- [Tratar um incidente](#tratar-um-incidente)

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


## Tratar um incidente

Use quando há interrupção de serviço ou suspeita de comprometimento que exige coordenação. A pessoa que recebe o relato inicia o registro; a autoridade definida no plano decide contenção e comunicação; o executor técnico verifica a recuperação. Entrada: relato, serviços afetados, contatos e plano vigente. Saída: serviço recuperado ou alternativa acordada, decisões registradas e ações posteriores identificadas.

### Reconhecer e avaliar

Registrar momento de identificação, sinais observados, serviço e usuários afetados. Distinguir fato de hipótese. “Sistema indisponível” é observação; “ataque de ransomware” exige evidência adicional. A falta de certeza não impede acionar o responsável.

Estimar impacto e comunicar à autoridade competente. Se o caso excede a capacidade local, acionar fornecedor ou especialista conforme os contatos do plano. A pessoa afetada não precisa preencher um formulário inacessível para receber ajuda.

### Conduzir a resposta

1. Identificar quem coordena e como a equipe atualizará a situação.
2. Registrar prioridades, trabalho suspenso e exceção de capacidade.
3. Avaliar contenção apropriada ao ambiente e preservar informações necessárias à investigação. Não aplicar formatação ou desligamento como regra automática.
4. Comunicar estado e alternativa operacional aos afetados, evitando declarar causa não confirmada.
5. Recuperar a partir de uma condição conhecida e verificar serviço, dados e dependências com o dono do processo.
6. Registrar horários, decisões, evidências e necessidade de acompanhamento.

As seis funções do CSF articulam governança, identificação, proteção, detecção, resposta e recuperação; elas não oferecem um único roteiro de ações técnicas para todo incidente. [F01](<../../framework/referencias/fontes.md#f01>) [F02](<../../framework/referencias/fontes.md#f02>)

### Verificar recuperação

Confirmar que o processo necessário funciona e que a equipe conhece restrições temporárias. O desaparecimento de uma mensagem de erro não é suficiente para encerrar. Se uma alternativa foi adotada, declarar se o serviço original segue pendente.

O relógio de resolução começa no registro definido para a métrica e termina na condição de encerramento acordada. Registrar também o momento de identificação quando diferente. Não excluir incidentes longos de um indicador sem mostrar o critério.

### Rever e prevenir recorrência

Preparar revisão proporcional: o que ocorreu, quais decisões ajudaram, onde faltou informação e qual ação tem responsável. Correção definitiva pode ser uma melhoria vinculada ao incidente. “Causa ainda não confirmada” é uma conclusão válida, com próximo passo.

Modelo: [Plano de resposta](<../../framework/templates/incidente.md>). Próxima tarefa: [Testar restauração](<../../framework/guias/testar-restauracao.md>).


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
