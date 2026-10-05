# GEAR: Guia de execução

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: **Autor**: Manus AI (sob a direção de Andre Victor) **Versão**: 3.0 (Concisa - Guia de Suporte) **Data**: 05 de Março de 2026

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Execução e serviços](#execucao-e-servicos)
- [Priorizar demandas de TI](#priorizar-demandas-de-ti)
- [Entregar uma melhoria pequena](#entregar-uma-melhoria-pequena)
- [Lista de tarefas e verificação](#lista-de-tarefas-e-verificacao)
- [PRD curto e registro de aceite](#prd-curto-e-registro-de-aceite)
- [Fluxogramas de decisão e execução](#fluxogramas-de-decisao-e-execucao)

## Execução e serviços

Este domínio organiza solicitações, incidentes e melhorias em um fluxo observável. O objetivo é compatibilizar capacidade e prioridade, registrando interrupções e critérios de conclusão. A combinação de práticas é própria do GEAR; não constitui uma implementação integral de Scrum ou ITIL. [F03](<../../framework/referencias/fontes.md#f03>) [F10](<../../framework/referencias/fontes.md#f10>)

### Entrada de demandas

Canal único significa **um registro oficial da fila**, com responsável e situação. Pode receber solicitações por formulário, e-mail ou integração. Um pedido recebido por outro meio deve ser registrado ou encaminhado; não se recusa uma emergência porque chegou por telefone.

Definir quem registra incidentes quando o solicitante não consegue acessar o canal. Informar como pedir ajuda e como acompanhar a resposta. Uma mudança de canal precisa de transição e comunicação para evitar demandas perdidas.

### Estados de trabalho

| Estado | O que representa | Condição para avançar |
| --- | --- | --- |
| A Fazer | Demanda ainda não iniciada | Prioridade, responsável e capacidade acordados |
| Em Andamento | Trabalho iniciado sob responsabilidade do executor | Saída preparada para verificação |
| Em Teste | Verificação técnica ou de negócio ainda pendente | Critério de aceite atendido e evidência registrada |
| Concluído | Saída aceita ou encerramento justificado | Motivo e evidência acessíveis |

Bloqueio e suspensão são atributos visíveis do cartão, com motivo e próxima ação. Não transformar trabalho iniciado em tarefa nova nem reiniciar seu relógio para melhorar uma métrica.

### Limite de trabalho em progresso

O ponto de partida é **até três itens iniciados por executor**, contando Em Andamento e Em Teste sob sua responsabilidade. Trabalho bloqueado permanece visível e conta enquanto mantém compromisso de capacidade. A equipe pode escolher limite menor ou revê-lo após observar capacidade e filas. Registrar exceções temporárias, motivo e prazo de revisão.

Esse número é um parâmetro local de adoção, sem validação universal. Em equipe de uma pessoa, três cartões no sistema não significam três atividades executadas ao mesmo tempo. A concentração do trabalho deve permanecer explícita.

### Cadência e entrega

Usar planejamento semanal curto para selecionar trabalho compatível com a capacidade e fazer uma verificação diária da fila. Revisar ao final do ciclo o que terminou, ficou bloqueado e mudou de prioridade. As durações históricas de 15, 5 e 15 minutos são referências iniciais de agenda.

Uma melhoria pequena pode ser planejada como um piloto de uma ou duas semanas. Definir escopo que caiba no período ou negociar sua alteração; o método não garante que qualquer MVP será concluído em duas semanas. A revisão precisa de usuário ou dono de processo, mesmo quando o desenvolvimento é feito por uma pessoa.

### Emergências

A raia rápida atende incidentes com impacto que justifique interrupção. Quem reconhece o incidente comunica a prioridade; o executor registra o trabalho suspenso e concentra a resposta. Se o limite for ultrapassado, documentar a exceção e a capacidade comprometida. Após recuperação, decidir quando retomar o item interrompido.

Um incidente precisa de condição de recuperação e comunicação aos afetados. Resolver o chamado e prevenir recorrência podem produzir tarefas distintas, ligadas pelo histórico.

Para executar: [Priorizar demandas](<../../framework/guias/priorizar-demandas.md>), [tratar incidentes](<../../framework/guias/tratar-incidentes.md>) e [entregar uma melhoria](<../../framework/guias/entregar-melhoria.md>).


## Priorizar demandas de TI

Este guia ajuda a transformar pedidos concorrentes em uma fila com decisões e capacidade visíveis. Use quando solicitações chegam por vários meios, a equipe inicia mais trabalho do que consegue encerrar ou o negócio discorda da ordem de atendimento.

Responsável pela preparação: responsável por TI. A direção ou autoridade delegada decide conflitos que comprometem recursos, prioridades de negócio ou risco. Entrada: demandas registradas, capacidade disponível, serviços afetados e acordos existentes. Saída: fila ordenada, itens selecionados, responsáveis e motivos.

### Preparar o registro

Para cada demanda, registrar solicitante, necessidade, serviço afetado, consequência de adiar, prazo real, responsável e condição de conclusão. “Urgente” sem consequência identificada é informação insuficiente para decidir prioridade.

Uma solicitação incompleta permanece na fila como “aguardando informação”, com quem fornecerá o dado. Um incidente crítico recebe tratamento imediato e registro assim que viável. O canal único não é uma barreira ao acesso de quem está com o sistema indisponível.

### Executar a priorização

1. Separar recuperação de serviço, atendimento recorrente e melhoria planejada. Demandas de naturezas distintas podem exigir critérios e prazos diferentes.
2. Avaliar impacto, urgência e dependências. Usar as quatro finalidades de negócio para explicar valor, sem somar notas arbitrárias como se fossem medidas objetivas.
3. Conferir itens iniciados, incluindo teste e bloqueio. O limite inicial é três por executor; reduzir quando a capacidade disponível exigir.
4. Selecionar trabalho para o próximo ciclo e obter a decisão da autoridade responsável quando houver conflito.
5. Registrar ordem, decisão, responsável e critério de conclusão. Comunicar ao solicitante o próximo passo, inclusive quando a demanda foi adiada.

### Tratar exceções

Um incidente com interrupção relevante pode usar a raia rápida. Tornar visível o item suspenso, sua dependência e a revisão de prazo. Não devolvê-lo à fila como se nunca tivesse sido iniciado.

Se há várias emergências, a direção decide qual serviço recebe a capacidade limitada e quem comunica as consequências. Um limite de WIP sozinho não resolve essa escolha.

### Exemplo ilustrativo

Uma equipe de uma pessoa recebe pedido de relatório gerencial, erro que impede faturamento e troca de assinatura de e-mail. O incidente de faturamento recebe a primeira resposta porque há serviço indisponível. O relatório fica planejado após confirmar seu prazo e dono do processo. A assinatura entra na fila comum. A ordenação precisa do impacto observado; o exemplo não fixa uma prioridade universal para esses tipos de pedido.

### Encerrar

A priorização terminou quando cada item selecionado tem executor e critério de saída, itens adiados têm motivo e a equipe conhece a capacidade comprometida. Na revisão seguinte, confrontar decisão e efeito. Não avaliar sucesso pela quantidade de cartões iniciados.

Modelo: [Decisão e prioridades](<../../framework/templates/decisoes-prioridades.md>). Referência: [Execução e serviços](<../../framework/nucleo/execucao-servicos.md>). Próxima tarefa: [Entregar uma melhoria](<../../framework/guias/entregar-melhoria.md>).


## Entregar uma melhoria pequena

Use para uma alteração de TI com resultado verificável por um processo de negócio. Responsável por TI prepara a solução; dono do processo define e verifica o aceite; direção aprova recursos e riscos conforme a alçada. Entrada: necessidade, situação atual, restrições e capacidade. Saída: mudança verificada, registro de aceite e efeito a acompanhar.

### Delimitar

Registrar problema, beneficiário, escopo, exclusões e condição de sucesso em um PRD curto. Uma ou duas semanas podem ser o intervalo de um piloto; se o escopo não couber, reduzir a entrega ou negociar outro prazo. A duração não substitui uma estimativa de capacidade.

Um requisito pode usar “Dado/Quando/Então”: dado um pedido autorizado, quando o relatório é solicitado, então os campos definidos aparecem sem edição manual. Esse exemplo descreve comportamento esperado, não afirma que a solução já foi implementada.

### Executar

1. Conferir dados, permissões, integrações e dependências.
2. Definir executor e quem aceitará a saída.
3. Registrar critério de verificação, risco e retorno à condição anterior.
4. Selecionar trabalho compatível com a fila e seu limite.
5. Construir e testar o recorte acordado.
6. Verificar com o usuário ou dono do processo; registrar aceite ou correções.
7. Acompanhar a hipótese de benefício na janela definida.

### Aprender com a entrega

Uma solução aceita pode não produzir o benefício esperado. Medir uso, efeito e esforço de manutenção. Se a hipótese falhar, registrar o resultado e decidir adaptar ou interromper, sem reclassificá-lo como sucesso apenas porque houve implementação.

As práticas de inspeção e adaptação são compatíveis com a inspiração ágil; retirar elementos de Scrum impede chamar qualquer ciclo curto de implementação integral desse framework. [F03](<../../framework/referencias/fontes.md#f03>)

Modelo: [PRD e aceite](<../../framework/templates/prd-aceite.md>). Próxima tarefa: [Conduzir uma revisão](<../../framework/guias/conduzir-revisao.md>).


## Lista de tarefas e verificação

Use para uma mudança ou rotina que precise de passos atribuídos. TI organiza dependências e capacidade; executor registra resultado; dono do processo aceita o efeito pertinente. A lista complementa o quadro, sem criar uma segunda fila divergente.

### Preparar o recorte

- Iniciativa/rotina, período e responsável geral: [preencher]
- PRD ou decisão que autoriza, escopo e exclusões: [preencher]
- Permissões, dependências, ambiente e condição de retorno: [preencher]

| ID e ação | Executor | Dependência | Estado | Critério e modo de verificar | Resultado/evidência |
| --- | --- | --- | --- | --- | --- |
| [preencher] | | | [A Fazer/Em Andamento/Em Teste/Concluído] | | |

Bloqueio ou suspensão: [item, motivo, início, responsável pela próxima ação e revisão]. Manter o relógio e o histórico de trabalho iniciado. Contar andamento, teste e bloqueio comprometido no WIP por executor; marcar início de tarefa não cria capacidade adicional.

### Opções de organização

Agrupar por preparação e ambiente; desenvolvimento ou configuração; verificação técnica e de negócio; disponibilização e acompanhamento. Essas são opções do modelo antigo, sem impor quatro fases ou quatorze dias a toda atividade. Segurança e requisitos podem precisar de conferência antes da execução, não apenas ao final.

- Preparação: verificar acesso e dependências em ambiente autorizado.
- Implementação: executar o recorte acordado e guardar alterações.
- Verificação: testar critérios, acesso, falhas relevantes e retorno conforme o efeito.
- Disponibilização: confirmar autorização, comunicação, operação e acompanhamento.

Exemplos fictícios de critérios: membros autorizados acessam um repositório e demais não; um formulário informa um campo obrigatório ausente; mensagem de teste chega ao destino autorizado. Definir ambiente, amostra e prazo necessários; a antiga referência a dez segundos não é padrão de pagamentos ou e-mail. Mensagem de console não comprova recebimento externo.

### Encerrar e revisar

Registrar teste realizado, pessoa que verificou, aceite ou motivo de encerramento. Uma assinatura registra aprovação, sem substituir teste. Nem toda tarefa exige publicação ou implantação. Guardar pendências e condição de revisão posterior do benefício.

As marcações antigas `[ ]`, `[/]` e `[x]` podem ser mantidas como legenda em ferramentas que as suportem. Elas não representam sozinhas teste, bloqueio ou aceite; conservar esses campos explicitamente. Não apresentar `[/]` como checkbox Markdown padrão.

Saída: lista atualizada vinculada ao quadro. Concluir quando resultados e pendências são localizáveis, com responsável. Referência de uso: [entregar melhoria](<../../framework/guias/entregar-melhoria.md>). Próximo modelo: [PRD e aceite](<../../framework/templates/prd-aceite.md>).


## PRD curto e registro de aceite

Use para uma melhoria delimitada. Dono do processo valida a necessidade; TI confere viabilidade; executor verifica o comportamento; usuário ou dono do processo aceita a saída.

### Definição

- Identificador, versão, responsável e data: [preencher]
- Problema observado e evidência: [preencher]
- Usuário/processo beneficiado: [preencher]
- Resultado esperado e hipótese de benefício: [preencher]
- Escopo incluído: [preencher]
- Exclusões: [preencher]
- Restrições, permissões e dependências: [preencher]
- Risco, proprietário e mitigação: [preencher]
- Recursos e prazo estimados: [preencher]

### Verificação

| Critério observável | Como testar | Quem verifica | Resultado/evidência |
| --- | --- | --- | --- |
| [Dado… quando… então…] | | | |

**Plano de retorno:** [como desfazer ou mitigar falha; responsável].

**Aceite:** [pessoa, data, critérios atendidos e pendências].

**Acompanhamento do benefício:** [indicador, linha de base, janela, fonte e decisão futura]. Aceite funcional não comprova benefício financeiro. Se o recorte não couber na capacidade, renegociar escopo ou prazo antes de iniciar.

### Histórias e requisitos operacionais

História: `Como [perfil real], quero [comportamento] para [finalidade]`. Usar quantas forem necessárias ao recorte, sem inventar persona, fluxo ou regra de negócio para atingir duas ou três histórias. Requisito desconhecido permanece como pergunta com responsável.

| Requisito | Condição e limite acordados | Ambiente e modo de verificar | Responsável |
| --- | --- | --- | --- |
| Desempenho | [ação, quantidade de dados e tempo] | [dispositivo, rede, carga e amostra] | |
| Acesso/segurança | [perfis, permissões e exceções] | [teste autorizado de permitido/negado] | |
| Usabilidade | [tarefa, usuários e dispositivos] | [verificação com usuário e limitações] | |

Uma meta de dois segundos precisa dessas condições. Erro de formulário deve ser identificável e permitir correção; não usar apenas cor para descrevê-lo. Excluir uma funcionalidade exige acordo e consequência declarados, sem retirar um requisito necessário para que o recorte seja utilizável.

### Exemplos fictícios para iniciar uma conversa

- Financeiro: baixar extratos de três bancos e digitar valores em uma planilha consome tempo e pode gerar erro. O relato antigo de três horas por dia é hipótese do exemplo; conferir frequência, acesso, formatos e custo antes de calcular benefício.
- Comercial: leads de um formulário demoram a receber resposta. A proposta de encaminhá-los ao vendedor exige regras de atribuição, permissão, horário e teste de entrega; o relato de dois dias e venda perdida não é medição do projeto.
- Suporte: pedidos por mensagens ficam dispersos. Definir captura e acompanhamento, preservando acesso à ajuda; não supor que metade das tarefas foi perdida.

Outros exemplos dos modelos anteriores incluíam iniciar atendimento de um lead, informar campo obrigatório ausente e acompanhar pedido. São comportamentos a discutir, sem obrigação de integrar WhatsApp, coletar CPF ou criar aplicativo. Nenhuma história comprova benefício antes da avaliação.

### Conferir o preenchimento

TI e negócio descrevem o problema, acordam critérios antes de implementar, delimitam escopo e identificam quem aprova. Uma conversa de quinze ou vinte minutos pode preparar a minuta; ampliar quando houver lacunas. Uma ou duas páginas são preferência de síntese, com evidências e detalhes vinculados. Um piloto de duas semanas depende de capacidade e escopo, sem garantia universal.

Assistência opcional: [contrato de requisitos e entrega](<../../framework/templates/prompts-assistencia.md#requisitos-e-entrega>). A IA pode preparar propostas; dono do processo aprova regras e aceite, e TI confere viabilidade. Não preencher solicitante, data ou orçamento desconhecidos por inferência.


## Fluxogramas de decisão e execução

Os fluxos abaixo tornam visíveis decisão, execução, espera e retorno. Retângulos são ações; losangos são decisões; formas arredondadas delimitam entrada ou encerramento. “Sim” e “não” identificam o caminho escolhido. Eles resumem práticas locais do GEAR, sem substituir os critérios e alçadas dos guias.

### Da demanda ao encerramento

![Fluxo de demanda: reconhecer incidente crítico, conferir capacidade, executar, verificar e registrar o encerramento.](<../../GP-Pme%20Article/assets/diagrams/demanda.svg>)

1. Receber e registrar necessidade, serviço e responsável. Uma emergência é atendida e registrada assim que viável.
2. Se houver incidente crítico, acionar resposta e autoridade apropriadas. Encerrar somente após a verificação descrita no guia de incidentes.
3. Para a fila comum, conferir prioridade, dependências e critérios. Contar andamento, teste e bloqueio comprometido na capacidade por executor.
4. Se não houver capacidade acordada, manter motivo e revisão na fila. Retomar a decisão quando houver mudança de prioridade, dependência ou capacidade.
5. Executar o recorte autorizado e verificar a saída. Se houver lacuna, registrar e decidir a correção; o retorno à execução depende de autorização e capacidade.
6. Registrar evidência, motivo de encerramento e próximos passos. Cancelamento ou outra forma de encerramento precisa de justificativa, sem se apresentar como entrega aceita.

Bloqueio ou suspensão conserva histórico e relógio; o diagrama não autoriza ocultar trabalho iniciado para liberar WIP. Para critérios completos: [priorizar demandas](<../../framework/guias/priorizar-demandas.md>), [execução e serviços](<../../framework/nucleo/execucao-servicos.md>) e [entregar melhoria](<../../framework/guias/entregar-melhoria.md>).

### Resposta e recuperação

![Fluxo de incidente: registrar sinais, acionar alçada, verificar capacidade, responder, recuperar e conferir serviço ou alternativa.](<../../GP-Pme%20Article/assets/diagrams/incidente.svg>)

1. Registrar fatos, horário e incertezas; acionar responsável e autoridade sem aguardar causa confirmada.
2. Se a capacidade local for insuficiente, acionar fornecedor ou especialista pelos contatos conferidos. A resposta depende do ambiente e da alçada, com preservação de evidências.
3. Comunicar fatos verificados e próxima atualização. Recuperar o serviço ou preparar uma alternativa operacional.
4. Se a verificação com o dono do processo falhar, manter pendência, atualizar os afetados e reavaliar a recuperação. Uma alternativa aceita não significa que o serviço original voltou.
5. Registrar limitações, encerramento e correções atribuídas. Investigar causa e prevenção em tarefas ligadas ao incidente, quando necessário.

O fluxo não prescreve isolamento, desligamento ou formatação universais. Critérios, contatos e obrigação de comunicação permanecem no [guia de incidentes](<../../framework/guias/tratar-incidentes.md>) e no [plano breve](<../../framework/templates/incidente.md>). Fundamentos: NIST [F01](<../../framework/referencias/fontes.md#f01>), [F02](<../../framework/referencias/fontes.md#f02>) e CISA [F12](<../../framework/referencias/fontes.md#f12>); a sequência gráfica é uma adaptação local.

As figuras são vetoriais. Na tela pequena, a região permite rolagem horizontal e os passos textuais conservam o conteúdo para leitura. A imagem de rotina diária fornecida pelo usuário orientou as formas e as ramificações; suas atividades não fazem parte do método.


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
