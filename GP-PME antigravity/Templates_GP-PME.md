# GEAR: Biblioteca de registros essenciais

Edição editorial GEAR 2026.10. Caminho GP-PME preservado para compatibilidade. Modelos completos, revistos a partir da biblioteca anterior; preencher com dados reais e registrar lacunas. IA é opcional. Direitos conforme LICENSE.md.

Esta biblioteca reúne oito grupos de registros do índice anterior. Uma ou duas páginas são preferência de síntese, sem apagar evidências necessárias. Templates são instrumentos locais, sem certificação normativa. Modelos complementares e contratos de IA permanecem na biblioteca modular.

## Escolher um registro

- [Template 1: responsabilidades e RACI-Lite](#template-1-responsabilidades-e-raci-lite)
- [Template 2: quatro finalidades e decisão](#template-2-quatro-finalidades-e-decisao)
- [Template 3: painel de indicadores](#template-3-painel-de-indicadores)
- [Template 4: PRD e aceite](#template-4-prd-e-aceite)
- [Template 5: impacto e urgência](#template-5-impacto-e-urgencia)
- [Template 6: ativos e dependências](#template-6-ativos-e-dependencias)
- [Template 7: resposta a incidentes](#template-7-resposta-a-incidentes)
- [Template 8: maturidade e plano de melhoria](#template-8-maturidade-e-plano-de-melhoria)

## Template 1: responsabilidades e RACI-Lite

### Registro de responsabilidades

Preencher no início da adoção e revisar após mudanças de pessoas ou fornecedores. Direção confirma alçadas; cada pessoa confirma disponibilidade e acesso. Saída: lista consultável de responsáveis e substitutos.

**Processo/serviço:** [preencher]  
**Data e responsável pelo registro:** [preencher]

| Função | Pessoa ou fornecedor | Decide o quê | Limite da alçada | Substituto/contato |
| --- | --- | --- | --- | --- |
| Patrocinador/direção | | Recursos e risco aceito | | |
| Responsável por TI | | Organização e execução | | |
| Dono do processo | | Necessidade e aceite | | |
| Executor | | Trabalho autorizado | | |
| Segurança/continuidade | | Teste e resposta | | |

**Acúmulos e conflitos:** [quem acumula aprovação e execução; como haverá segunda conferência quando necessária].

**Comunicação:** [registro oficial, contato de urgência, frequência de atualização e destinatários].

**Verificação:** pessoas designadas confirmaram os papéis em [data/evidência]. Exceções: [ausência de substituto, serviço terceirizado, limites de disponibilidade]. Não preencher nomes fictícios no registro operacional.

#### RACI-Lite por atividade

Quando houver dúvida entre funções, usar R para executor, A para autoridade de aprovação, C para pessoa consultada e I para pessoa informada. Identificar uma autoridade final por decisão; se houver mais de uma aprovação necessária, explicitar decisões e alçadas distintas.

| Atividade | R: executor | A: autoridade | C: consultado | I: informado |
| --- | --- | --- | --- | --- |
| Orçamento anual de TI | | | | |
| Priorização da fila | | | | |
| Triagem e atendimento | | | | |
| Teste de recuperação | | | | |
| Requisitos e aceite da melhoria | | | | |

Uma ferramenta pode preparar a minuta ou auxiliar o teste. Registrar a pessoa responsável pela execução e conferência; não atribuir à IA a alçada humana. Validar disponibilidade e conflitos antes de considerar a tabela vigente. A quantidade de linhas é ajustável ao serviço.


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

## Template 2: quatro finalidades e decisão

### Decisão e prioridade

Use para uma demanda, investimento ou revisão de fila. TI prepara fatos; dono do processo explica impacto; autoridade de aprovação decide. Este registro pode ser um cartão do quadro.

- Identificador, data e solicitante: [preencher]
- Problema e processo afetado: [situação observada]
- Evidências e fontes: [link, período e limitações]
- Opções consideradas: [inclusive adiar ou não executar]
- Impacto, urgência, esforço e dependências: [estimativa e incerteza]
- Riscos e proprietário: [preencher]
- Capacidade e trabalho já iniciado do executor: [preencher]
- Decisão e motivo: [preencher]
- Aprovador e limite de alçada: [preencher]
- Executor, prazo e critério de conclusão: [preencher]
- Data de revisão e comunicação ao solicitante: [preencher]

A matriz de quatro finalidades relaciona a demanda a receita, custos, experiência e resiliência. Registrar finalidade principal e efeitos secundários. Impacto e esforço ajudam a decidir a ordem; não alteram o significado dessa matriz nem dispensam risco, urgência ou dependência. Uma obrigação urgente pode anteceder uma melhoria de alto impacto.

Concluir quando a decisão estiver atribuída e comunicada. Se faltar dado essencial, registrar a investigação e seu responsável. Se a prioridade mudar, acrescentar nova decisão, preservando a anterior.


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

## Template 3: painel de indicadores

### Painel de indicadores e decisões

Use na revisão da rotina quando houver uma decisão apoiada por medidas. TI prepara dados; dono do serviço confere o escopo; direção e TI acordam tolerâncias e ações. Um painel pode ser preenchido em planilha ou papel; não exige coleta automática.

#### Identificação e cálculo

- Serviço/processo e responsável: [preencher]
- Período, horário observado e exclusões: [preencher]
- Origem dos dados, versão do cálculo e data da coleta: [preencher]

| Indicador | Dados de entrada e quantidade | Resultado/unidade | Tolerância local e comparação | Limite da interpretação |
| --- | --- | --- | --- | --- |
| IDSC | Horas observadas e indisponíveis | [%] | | |
| TMpR | Duração de restauração e incidentes encerrados | [horas; quantidade] | | |
| ISU | Notas 1–5 e respostas válidas | [média; quantidade] | | |
| Outro indicador escolhido | [definição, período e fonte] | | | |

Sem denominador válido, registrar dado insuficiente. Não usar queda da média como sinal automático de melhoria; comparar escopo, quantidade e casos longos. As metas históricas >99,5%, <4 horas e >4,5 são exemplos locais configuráveis, sem validade universal.

#### Decisão e acompanhamento

| Questão a decidir | Evidência e alternativas | Decisão/motivo | Autoridade | Executor e prazo | Próxima verificação |
| --- | --- | --- | --- | --- | --- |
| [preencher] | | | | | |

Concluir quando a pessoa responsável conferiu dados e unidades e a decisão ou necessidade de coleta está atribuída. Cálculo assistido por IA exige a mesma conferência; não preencher um resultado por suposição.

Definições: [operacionais](<../framework/indicadores/operacionais.md>) e [negócio/comparação](<../framework/indicadores/negocio-comparacao.md>). Próximo modelo: [decisões e prioridades](<../framework/templates/decisoes-prioridades.md>).


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

## Template 4: PRD e aceite

### PRD curto e registro de aceite

Use para uma melhoria delimitada. Dono do processo valida a necessidade; TI confere viabilidade; executor verifica o comportamento; usuário ou dono do processo aceita a saída.

#### Definição

- Identificador, versão, responsável e data: [preencher]
- Problema observado e evidência: [preencher]
- Usuário/processo beneficiado: [preencher]
- Resultado esperado e hipótese de benefício: [preencher]
- Escopo incluído: [preencher]
- Exclusões: [preencher]
- Restrições, permissões e dependências: [preencher]
- Risco, proprietário e mitigação: [preencher]
- Recursos e prazo estimados: [preencher]

#### Verificação

| Critério observável | Como testar | Quem verifica | Resultado/evidência |
| --- | --- | --- | --- |
| [Dado… quando… então…] | | | |

**Plano de retorno:** [como desfazer ou mitigar falha; responsável].

**Aceite:** [pessoa, data, critérios atendidos e pendências].

**Acompanhamento do benefício:** [indicador, linha de base, janela, fonte e decisão futura]. Aceite funcional não comprova benefício financeiro. Se o recorte não couber na capacidade, renegociar escopo ou prazo antes de iniciar.

#### Histórias e requisitos operacionais

História: `Como [perfil real], quero [comportamento] para [finalidade]`. Usar quantas forem necessárias ao recorte, sem inventar persona, fluxo ou regra de negócio para atingir duas ou três histórias. Requisito desconhecido permanece como pergunta com responsável.

| Requisito | Condição e limite acordados | Ambiente e modo de verificar | Responsável |
| --- | --- | --- | --- |
| Desempenho | [ação, quantidade de dados e tempo] | [dispositivo, rede, carga e amostra] | |
| Acesso/segurança | [perfis, permissões e exceções] | [teste autorizado de permitido/negado] | |
| Usabilidade | [tarefa, usuários e dispositivos] | [verificação com usuário e limitações] | |

Uma meta de dois segundos precisa dessas condições. Erro de formulário deve ser identificável e permitir correção; não usar apenas cor para descrevê-lo. Excluir uma funcionalidade exige acordo e consequência declarados, sem retirar um requisito necessário para que o recorte seja utilizável.

#### Exemplos fictícios para iniciar uma conversa

- Financeiro: baixar extratos de três bancos e digitar valores em uma planilha consome tempo e pode gerar erro. O relato antigo de três horas por dia é hipótese do exemplo; conferir frequência, acesso, formatos e custo antes de calcular benefício.
- Comercial: leads de um formulário demoram a receber resposta. A proposta de encaminhá-los ao vendedor exige regras de atribuição, permissão, horário e teste de entrega; o relato de dois dias e venda perdida não é medição do projeto.
- Suporte: pedidos por mensagens ficam dispersos. Definir captura e acompanhamento, preservando acesso à ajuda; não supor que metade das tarefas foi perdida.

Outros exemplos dos modelos anteriores incluíam iniciar atendimento de um lead, informar campo obrigatório ausente e acompanhar pedido. São comportamentos a discutir, sem obrigação de integrar WhatsApp, coletar CPF ou criar aplicativo. Nenhuma história comprova benefício antes da avaliação.

#### Conferir o preenchimento

TI e negócio descrevem o problema, acordam critérios antes de implementar, delimitam escopo e identificam quem aprova. Uma conversa de quinze ou vinte minutos pode preparar a minuta; ampliar quando houver lacunas. Uma ou duas páginas são preferência de síntese, com evidências e detalhes vinculados. Um piloto de duas semanas depende de capacidade e escopo, sem garantia universal.

Assistência opcional: [contrato de requisitos e entrega](<../framework/templates/prompts-assistencia.md#requisitos-e-entrega>). A IA pode preparar propostas; dono do processo aprova regras e aceite, e TI confere viabilidade. Não preencher solicitante, data ou orçamento desconhecidos por inferência.


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

## Template 5: impacto e urgência

### Matriz de impacto e urgência

Use para discutir demandas concorrentes. Dono do processo explica impacto; TI verifica dependências e esforço; autoridade de aprovação decide. Esta matriz é distinta das quatro finalidades: receita, custos, experiência e resiliência.

| | Urgência menor | Urgência maior |
| --- | --- | --- |
| Impacto maior | Agendar com capacidade, dependências e prazo | Avaliar prioridade e exceções necessárias |
| Impacto menor | Questionar necessidade, adiar ou delegar | Conferir impacto e prazo; executar conforme capacidade |

Urgência alta não demonstra que a demanda é rápida ou fácil. Um bug de faturamento pode ter impacto alto; classificar pelo efeito observado. Fronteiras alto/baixo são locais e devem ter exemplos acordados.

| Demanda | Impacto e evidência | Prazo e motivo de urgência | Esforço/dependência | Decisão e responsável |
| --- | --- | --- | --- | --- |
| [preencher] | | | | |

Saída: ordem acordada, itens adiados e motivo. Concluir quando solicitantes conhecerem a decisão e cada item selecionado tiver executor e aceite. Risco, obrigação, emergência ou dependência podem alterar a ordem; registrar no [modelo de decisão](<../framework/templates/decisoes-prioridades.md>).

Origem: template histórico `References/GP-PME Versions/matriz_4_quadrantes.md`, revisto para retirar associação automática entre urgência e facilidade. Instrumento local, sem validade universal atribuída a fonte externa.


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

## Template 6: ativos e dependências

### Inventário de ativos e dependências

Use para compreender o que sustenta um serviço e preparar sua proteção e recuperação. Dono do serviço define impacto; TI verifica dependências; proprietário confirma responsabilidade. Começar pelos serviços críticos e registrar cobertura parcial. Criticidade não se deduz do cargo de quem usa o equipamento.

#### Serviço e cobertura

- Serviço/processo, proprietário e data de revisão: [preencher]
- Consequência da indisponibilidade e evidência: [preencher]
- RTO e RPO acordados, com justificativa: [preencher]
- Escopo inventariado, lacunas e responsável pela ampliação: [preencher]

| ID e ativo/dependência | Tipo e localização | Proprietário e fornecedor | Criticidade/motivo | Dados e acesso necessários |
| --- | --- | --- | --- | --- |
| [preencher] | | | | |

| ID | MFA/acesso: evidência e exceção | Cópia: frequência e retenção | Recuperação: teste e limite | Ação, responsável e prazo |
| --- | --- | --- | --- | --- |
| [vincular ao ativo] | | | | |

Registrar referência à evidência com acesso adequado; não guardar senhas ou chaves neste modelo. “MFA ativo” exige configuração verificada e escopo declarado. “Backup ativo” exige identificar solução, fonte e retenção; teste de arquivo não comprova recuperação de todo o serviço.

Se for usada criticidade de 1 a 5, definir cada faixa e exemplos com o dono do processo. A escala é local e não mede porcentagem de risco. Dependências de um ativo crítico podem precisar de tratamento mesmo quando seu uso parece secundário.

#### Conferir e atualizar

TI compara registro e ambiente; proprietário confirma uso e impacto. Registrar alteração após mudança de conta, integração, fornecedor ou serviço. Concluir o recorte quando ativos conhecidos estão atribuídos e lacunas têm plano; não declarar inventário completo enquanto faltar cobertura.

O nome anterior “Inventário 80/20” expressava priorização, sem prova de que 20% dos ativos representam 80% da receita ou risco. Exemplos antigos de ERP, planilha financeira, notebook e serviço de chamados são possibilidades de ativo, não configuração real do projeto.

Fundamento: [segurança e continuidade](<../framework/nucleo/seguranca-continuidade.md>), [NIST F01–F02](<../framework/referencias/fontes.md#f01>). Próximo modelo: [risco e continuidade](<../framework/templates/risco-continuidade.md>).


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

## Template 7: resposta a incidentes

### Plano breve de resposta a incidente

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

#### Durante e depois

1. Registrar descoberta, impacto conhecido e incertezas.
2. Acionar responsáveis; conter conforme autorização e preservar evidências.
3. Atualizar negócio com fatos verificados e próxima atualização.
4. Recuperar em condição segura e conferir serviço com seu dono.
5. Registrar encerramento, limitações e correções atribuídas.

**Exercício:** [cenário, data, participantes, resultado e próxima revisão]. Não considerar o plano testado só por ter sido assinado. Não colocar credenciais no documento.

Fundamento: orientação CISA [F12](<../framework/referencias/fontes.md#f12>), adaptada a um registro breve do GEAR.


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

## Template 8: maturidade e plano de melhoria

### Registro de maturidade

Preencher com TI e dono do processo usando o [questionário](<../framework/adocao/maturidade.md>). Comparar apenas aplicações com contexto e janela conhecidos.

**Organização/processo:** [preencher]  
**Data, janela de evidência e avaliadores:** [preencher]

| Pergunta | Resposta 0/1 | Evidência, data e limite | Ação quando insuficiente |
| --- | --- | --- | --- |
| 1. Registro e responsável | | | |
| 2. Capacidade e fluxo | | | |
| 3. Orientações verificadas | | | |
| 4. Prioridades decididas | | | |
| 5. Escopo e aceite | | | |
| 6. Dependências críticas | | | |
| 7. Recuperação testada | | | |
| 8. Acesso controlado | | | |
| 9. Indicadores rastreáveis | | | |
| 10. Revisão responsável | | | |

**IM-TI e nível descritivo:** [soma e faixa].  
**Mudanças em relação à aplicação anterior:** [prática, evidência e contexto].  
**Até três ações prioritárias:** [responsável e prazo].  
**Lacunas críticas e risco aceito:** [aprovação e motivo].  
**Próxima revisão:** [data e responsável].

Concluir com evidências consultáveis e pendências atribuídas. Este registro não constitui certificação nem exige IA.


Assistência opcional: fornecer somente dados autorizados, pedir uma minuta e registrar lacunas. Quem tem responsabilidade confere a saída e aprova o uso; o modelo não determina configuração ou alçada real.

Consulta: [biblioteca modular](../framework/templates/README.md), [instrução de tarefa](../framework/templates/instrucao-assistencia.md) e [contratos específicos](../framework/templates/prompts-assistencia.md). Fontes: [referências e limites](../framework/referencias/fontes.md).
