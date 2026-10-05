# GEAR: Guia para direção

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: **Autor**: Manus AI (sob a direção de Andre Victor) **Versão**: 1.0 (Final) **Data**: 21 de Fevereiro de 2026

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Começar pela rotina

GEAR ajuda uma equipe pequena a registrar necessidades, decidir prioridades e verificar entregas. Direção define recursos e riscos; TI organiza a execução; o dono do processo explica o problema e aceita o resultado. Uma pessoa pode acumular funções, desde que isso fique visível.

Não é necessário comprar uma plataforma ou usar IA. Um quadro e registros consultáveis podem apoiar a gestão; backup e proteção de contas continuam exigindo tecnologia apropriada. O método não garante aumento de faturamento, proteção integral ou promoção do profissional de TI.

## Entender as três frentes

| Frente | Decisão prática | Registro útil |
| --- | --- | --- |
| Governança e direção | O que fazer, por qual motivo e com qual recurso | Prioridade, responsável e prazo |
| Execução e serviços | O que iniciar e como verificar a saída | Quadro, critério de conclusão e aceite |
| Segurança e continuidade | O que precisa continuar e como recuperar | Dependências, controles e teste |

Adoção, indicadores e maturidade ajudam a rever essas frentes. IA pode preparar minutas e cálculos, sob revisão humana; seu uso é opcional inclusive no nível máximo de maturidade.

## Direção: decidir e acompanhar

O manual anterior chamava essa participação de DAA: direcionar, agir e acompanhar. Na prática, direção decide a prioridade, TI executa o autorizado e ambos confrontam o resultado com evidências. ADM-Lite é o nome local de avaliar, dirigir e monitorar; não é o método ADM do TOGAF.

A revisão CD-TI Lite reúne direção, TI e dono do processo. Quinze dias e 30 minutos são um começo possível, ajustável à necessidade. A pauta pode distribuir cinco minutos para indicadores, quinze para prioridades, cinco para riscos e cinco para decisões. Uma emergência pode exigir decisão antes da reunião.

Registrar decisão, motivo, alternativas, aprovador, executor, prazo e próxima revisão. Se a mesma pessoa executa e aprova uma ação relevante, declarar o acúmulo e definir segunda conferência quando necessária. O registro deve permitir que uma pessoa ausente entenda o acordo.

A Matriz 4 Quadrantes relaciona iniciativas a receita, custos, experiência e resiliência. Configurar Pix pode ter hipótese de receita; rever licenças, hipótese de custo; preparar uma orientação, hipótese de experiência; testar recuperação, finalidade de continuidade. Nenhuma dessas classificações prova um benefício.

## Execução: tornar o trabalho visível

Use um registro oficial para a fila, com solicitante, executor, prioridade e saída esperada. Pedidos recebidos por telefone ou mensagem são registrados; uma emergência é atendida e entra na fila assim que viável. “Canal único” não significa recusar ajuda porque o formulário está indisponível.

| Estado | Significado |
| --- | --- |
| A Fazer | Ainda não iniciado |
| Em Andamento | Trabalho iniciado |
| Em Teste | Verificação técnica ou de negócio pendente |
| Concluído | Saída aceita ou encerramento justificado |

Comece com até três itens iniciados por executor, contando andamento, teste e bloqueio. Esse limite é parâmetro local de capacidade, não garantia de rapidez. Uma equipe de uma pessoa mantém foco em uma atividade de cada vez. Bloquear ou suspender um cartão conserva seu início e seu histórico.

Para uma emergência, registrar quem decidiu interromper, qual trabalho foi suspenso e que capacidade ficou comprometida. Depois da recuperação, decidir quando retomar o item. Uma quarta tarefa comum aguarda capacidade.

Uma melhoria começa com um PRD curto: problema, beneficiário, escopo, exclusões e critério de aceite. Uma ou duas semanas podem delimitar um piloto; se a entrega não couber, renegociar prazo ou escopo. TI verifica a solução e o dono do processo aceita o resultado. Aceite técnico não comprova retorno financeiro.

## Continuidade: conhecer dependências e testar

Identifique o serviço que precisa continuar, seus dados, contas, equipamentos e fornecedores. Comece pelas dependências críticas e registre o que falta mapear. O nome antigo “Inventário 80/20” expressava priorização; não prova que 20% dos ativos geram 80% do faturamento.

Contas individuais, acesso necessário e MFA reduzem exposições específicas, sem impedir todo ataque. Registre cobertura e exceções. MFA é autenticação multifator; um código de celular é apenas uma implementação possível, não a definição completa.

Combine frequência e retenção de backup com a perda de dados tolerável. Proteja a cópia e teste restauração em ambiente autorizado. Um arquivo recuperado não comprova recuperação do serviço inteiro. Os antigos parâmetros de backup diário, teste trimestral e 30 minutos precisam de justificativa local.

Prepare o PRI com contatos conferidos, autoridade para contenção, comunicação e passos de recuperação. No incidente, preserve evidências e confirme serviço e dados com seu dono. Formatação e desligamento não são instruções universais. Obrigações legais vão à competência responsável.

## Verificar sem confundir documento com resultado

- [ ] As demandas têm responsável, prioridade e critério de saída?
- [ ] O quadro mostra testes, bloqueios e exceções de capacidade?
- [ ] As decisões têm aprovador e próxima revisão?
- [ ] As dependências críticas têm proprietário e lacunas registradas?
- [ ] O teste de restauração registra escopo, resultado e limitações?
- [ ] Os contatos e alçadas do PRI foram conferidos em exercício?

Disponibilidade, tempo de restauração e satisfação são indicadores candidatos, escolhidos conforme a decisão. Informar período e origem. As antigas metas de 99,5% e 4,5/5 são referências locais, não exigências universais. Sem respostas, satisfação é dado insuficiente; sem incidentes restaurados, não existe média de restauração calculável.

## Usar IA quando for útil

Fornecer tarefa, dados autorizados, restrições e saída pretendida. Conferir fontes, cálculos e lacunas. A resposta deve separar informação fornecida, hipótese e recomendação. A pessoa com alçada decide se a saída pode ser usada. Um prompt não elimina erros; a equipe pode executar a mesma tarefa sem IA.

Quatro funções conceituais organizam a assistência: direção, entrega, segurança e auditoria. O software histórico tem um orquestrador e oito especialistas. As contagens descrevem camadas distintas e não criam novos domínios.

## Planejar os primeiros 30 dias

| Janela local | Foco | Evidência esperada |
| --- | --- | --- |
| Semana 1 | Registrar demandas e capacidade | Fila real, responsáveis e prioridades |
| Semana 2 | Conhecer dependências e testar recuperação | Inventário inicial e teste com limites |
| Semana 3 | Decidir prioridades e exercitar resposta | Decisão e PRI com contatos conferidos |
| Semana 4 | Rever evidências e pendências | Comparação por pergunta e próxima revisão |

Trinta dias são planejamento, sem garantir implantação ou avanço de maturidade. Períodos antigos de 31–90 e 91–180 dias exprimiam expansão pretendida; hoje a próxima etapa depende das lacunas e da capacidade. Não há ganho automático de 80% do suporte.

O IM-TI soma dez práticas verificadas, de 0 a 10. As faixas locais descrevem a rotina e ajudam a localizar lacunas; não certificam segurança nem comparam organizações diferentes. As perguntas foram revistas; resultados antigos exigem reaplicação. IA não é condição de resposta positiva.

## Termos para consulta

| Termo | Uso neste manual |
| --- | --- |
| Kanban | Quadro para tornar fila e trabalho iniciado visíveis |
| WIP | Trabalho iniciado sob responsabilidade do executor |
| PRD | Registro de problema, escopo e critérios de uma melhoria |
| PRI | Plano de resposta com contatos, alçadas e recuperação |
| RTO e RPO | Tolerâncias de tempo de recuperação e perda de dados |
| MVP | Recorte de solução para testar uma hipótese |
| Frame-sim | Nome histórico de proposta de simulação, sem equivalência com validação de campo |
| DAN e COT | Estimativa local de dívida e investimento de otimização, com premissas explícitas |

## Fontes e próxima tarefa

Conceitos de continuidade: NIST CSF 2.0 e guia para pequenas empresas, F01–F02. Desenvolvimento incremental: Scrum Guide 2020, F03; retirar elementos impede chamar o método de Scrum integral. Adaptação de governança e serviço: páginas oficiais COBIT e ITIL, F09–F10. Documentação: Diátaxis, F08. Referências completas e limites constam da lista vinculada abaixo. Cadências, WIP e IM-TI são propostas locais do GEAR.


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
