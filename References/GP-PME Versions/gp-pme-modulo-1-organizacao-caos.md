# GEAR: Registrar e organizar demandas

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: **Autor**: Manus AI (sob a direção de Andre Victor) **Versão**: 2.1 (Modular Acadêmica com Implementação C) **Data**: 22 de Fevereiro de 2026

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Execução e serviços](#execucao-e-servicos)
- [Priorizar demandas de TI](#priorizar-demandas-de-ti)
- [Lista de tarefas e verificação](#lista-de-tarefas-e-verificacao)
- [Indicadores de negócio e comparação da rotina](#indicadores-de-negocio-e-comparacao-da-rotina)

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


## Rever riscos de adoção

Resistência, sobrecarga inicial, pouco uso dos registros e expectativas indevidas são riscos de aplicação presentes no acervo. TI e direção escolhem um recorte dentro da capacidade, explicam o acordo e observam o uso com as pessoas afetadas. Treinamento e gamificação não garantem adesão. Ajustar ferramenta ou registro quando o esforço não apoiar uma decisão.

Falta de direção exige alçada e decisão identificáveis; reunião sem decisão não resolve a lacuna. Requisitos ambíguos exigem conversa e critério testável. Falsa sensação de segurança exige conferir cobertura e teste; política ou compra não prova proteção. Biblioteca desatualizada exige curadoria somente se houver uso de assistência. Registrar dono, ação, evidência e próxima revisão para cada risco relevante.

Os percentuais, prazos e gates das versões anteriores eram propostas locais sem validação. Segurança urgente não espera nível de maturidade, implantação de quadro ou conclusão de outro módulo. A revisão de aplicação real continua necessária; testes deste repositório não comprovam efetividade organizacional.


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
