# GEAR: Execução e serviços: guia técnico

Edição editorial GEAR 2026.10. Framework de governança e gestão de TI para pequenas e médias empresas. Origem: GP-PME 5.2, 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor. Direitos conforme LICENSE.md. Caminho anterior preservado para compatibilidade.

## Percurso de leitura

- [Execução e serviços](#execucao-e-servicos)
- [Priorizar demandas de TI](#priorizar-demandas-de-ti)
- [Tratar um incidente](#tratar-um-incidente)
- [Entregar uma melhoria pequena](#entregar-uma-melhoria-pequena)
- [PRD curto e registro de aceite](#prd-curto-e-registro-de-aceite)
- [Usar assistência por IA](#usar-assistencia-por-ia)
- [Alternativa local: três graus de impacto e urgência](#alternativa-local-tres-graus-de-impacto-e-urgencia)
- [Rever a semana e as interrupções](#rever-a-semana-e-as-interrupcoes)

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


## Usar assistência por IA

IA pode ajudar a recuperar conteúdo, preparar uma minuta, classificar solicitações ou conferir requisitos. Seu uso é opcional. Uma equipe que mantém as mesmas práticas e evidências de forma manual pode alcançar qualquer nível de maturidade do GEAR.

Responsável por TI ou dono da tarefa seleciona o contexto; pessoa com autoridade adequada revisa decisões e aprova efeitos organizacionais. Entrada: dados autorizados, fontes, tarefa e critérios de saída. Saída: proposta revisada ou registro de insuficiência de dados.

### Quatro funções de assistência

O modelo conceitual separa orquestração, análise de entrega, apoio a segurança e auditoria de indicadores. A implementação histórica contém um orquestrador e oito especialistas. Esses números descrevem níveis distintos: funções do método e componentes de software. Não são pilares adicionais nem prova de autonomia.

### Preparar e revisar

1. Explicitar tarefa, dados disponíveis, restrições e formato de saída.
2. Separar fontes de instruções. Um documento recuperado pode conter texto incorreto ou instruções que não pertencem à tarefa.
3. Solicitar que lacunas apareçam como dado insuficiente, sem criar cifra, contato, configuração ou referência.
4. Executar cálculos com regras determinísticas e conferir as unidades.
5. Revisar alegações contra as fontes e distinguir proposta de ação executada.
6. Obter aprovação humana antes de priorizar, investir, mudar acesso, conter incidente ou publicar.

### Elaborar uma melhoria por etapas

O mestre técnico de junho de 2026 propunha quatro etapas de elaboração: PRD, histórias e critérios, código inicial e roteiros de teste. Essa sequência pode ser usada com ou sem IA. Ao usar assistência, revisar a saída de cada etapa antes de fornecer contexto à seguinte; uma lacuna não se torna fato por ter sido repetida por outro agente.

1. Preparar problema, beneficiário, escopo e hipóteses no PRD.
2. Transformar o comportamento esperado em histórias e critérios verificáveis, com aceite pelo dono do processo.
3. Se houver desenvolvimento, preparar código em ambiente autorizado, conferir dependências e manter condição de retorno.
4. Definir e executar testes que verifiquem os critérios; registrar resultado, limites e aprovação.

O código preparado não comprova funcionamento. O roteiro não comprova que o teste ocorreu. Um teste técnico aprovado não comprova benefício financeiro. A pessoa responsável mantém essas distinções no registro da entrega. A sequência é proposta local preservada do manual técnico, não validação empírica de agentes encadeados.

### Decidir sobre utilidade

Comparar esforço total de preparação, revisão e correção com a rotina manual. Registrar tipo de tarefa, amostra e período. Fluência da resposta, quantidade de texto e confiança declarada pelo sistema não medem correção ou ganho de produtividade.

HITL significa revisão humana com responsabilidade e critério; uma confirmação automática de toda saída não torna o processo controlado. A ausência de IA não é uma lacuna metodológica.

Modelos: [contratos de histórias, código, testes, relatório e exercício](<../../framework/templates/prompts-etapas.md>) e [revisão de saída assistida](<../../framework/templates/revisao-ia.md>). Para a fundamentação e limites: [Origens e adaptações](<../../framework/fundamentos/origens-adaptacoes.md>).


## Alternativa local: três graus de impacto e urgência

O capítulo anterior também continha uma matriz de nove combinações. Ela é uma alternativa didática à matriz de duas faixas, não uma tabela de SLA validada. Definir os graus com exemplos do serviço; urgência é consequência de adiar, não sinônimo de dificuldade. O dono do processo confirma impacto; a autoridade decide prioridade; TI confere capacidade e dependências.

| Impacto | Urgência alta | Urgência média | Urgência baixa |
| --- | --- | --- | --- |
| Alto | Avaliar resposta imediata e alçada de emergência | Acordar prazo conforme consequência | Planejar com capacidade e dependências |
| Médio | Conferir prazo e serviço afetado | Ordenar com as demandas concorrentes | Manter fila com responsável |
| Baixo | Verificar se há obrigação ou risco que altera a ordem | Comparar com prioridades vigentes | Questionar necessidade; registrar decisão |

Os antigos rótulos “resolver hoje” e “descarte” foram retirados: contexto, risco e obrigação podem exigir outra decisão. Impacto individual não autoriza eliminar automaticamente uma demanda. Registrar decisão, motivo e comunicação ao solicitante.

## Rever a semana e as interrupções

O responsável por TI prepara o plano com demandas, dependências e capacidade. Três a cinco cartões na semana eram uma sugestão de seleção, não limite de WIP nem compromisso universal. Uma revisão diária pode conferir concluídos, próximo trabalho e bloqueios sem criar reunião quando há um executor. Ao encerrar o ciclo, comparar plano inicial, entregas, alterações e capacidade consumida por incidentes.

Pedidos comuns são ordenados pela consequência de adiar; não precisam esperar a semana seguinte por regra automática. Emergência registra alçada, trabalho suspenso e exceção de capacidade. Trabalho iniciado não volta a ser novo nem perde o histórico. Após recuperação, rever prioridade de retomada e comunicar aos afetados.

Uma orientação ou mudança pequena pode dispensar implantação em produção. Conclusão exige o critério adequado à demanda ou encerramento justificado. O indicador de entregas em prazo e orçamento não mede sozinho utilidade ou desempenho do suporte.

## Fontes e continuidade

Fundamentos e limites: [referências completas](../../framework/referencias/fontes.md). Regra vigente: [documentação modular](../../framework/README.md). Próxima tarefa: [catálogo de guias](../../framework/guias/README.md). IA é opcional, inclusive na maturidade máxima. As fontes conceituais não validam automaticamente metas ou instrumentos locais.
