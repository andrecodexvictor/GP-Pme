# Adoção e manutenção

Edição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.

## Origem e decisão editorial

As janelas antigas de 31–90, 91–180 e 181–210 dias eram planejamento. A fase de desacoplamento e publicação descrevia produção documental, distinta da adoção por uma empresa. Marcações de concluído não comprovavam marcos organizacionais. Urgência e segurança podem exigir ação anterior à sequência; a próxima etapa depende de evidências e capacidade.

## Primeiros 30 dias

Este percurso ensina a iniciar o GEAR em uma equipe pequena. Ao final, a direção deve conseguir localizar a fila de TI, suas prioridades, os riscos mais urgentes e as evidências disponíveis. Trinta dias são uma janela de planejamento local; não garantem implantação completa nem avanço de maturidade.

### Preparar a adoção

O responsável por TI combina com a direção quem aprova prioridades e recursos. Escolhem um processo de negócio para acompanhar, um registro de demandas e um lugar para decisões. Não é necessário comprar uma plataforma. Antes de iniciar, confirmam tempo disponível, acesso aos responsáveis e autorização para os testes previstos.

A **verificação pré-projeto** decide se uma iniciativa específica deve começar: problema, patrocinador, viabilidade, risco e capacidade. É diferente da antiga “Fase Zero” de adoção. Um projeto pode ser recusado enquanto a rotina do GEAR continua funcionando.

### Semana 1: tornar o trabalho visível

1. Aplicar o [questionário de maturidade](<../framework/adocao/maturidade.md>), registrando evidência e lacunas.
2. Escolher até três problemas prioritários com o dono do processo. Anotar o impacto observado, sem estimar ganhos como se já fossem resultados.
3. Criar a fila: A Fazer, Em Andamento, Em Teste e Concluído. Registrar executor, solicitante, prioridade e aceite em cada item.
4. Comunicar o registro oficial. Uma urgência recebida por telefone deve entrar na fila assim que o atendimento permitir.
5. Aplicar o limite inicial de três itens iniciados por executor. Testes e bloqueios entram na contagem; suspensões conservam histórico.

**Evidência:** fila com trabalho real e registro de quem decide. Se ninguém puder assumir a aprovação, resolver essa lacuna antes de ampliar o método.

### Semana 2: conhecer dependências e recuperação

Mapear primeiro os ativos e fornecedores que sustentam o processo escolhido. Registrar proprietário, dados tratados, acesso, suporte, backup e dependências. Essa priorização por criticidade substitui a interpretação literal de “inventário 80/20”.

Executar um [teste de restauração](<../framework/guias/testar-restauracao.md>) autorizado, em ambiente seguro. Definir com o negócio o tempo e a perda de dados toleráveis. Documentar resultado, limitações e correções. Preparar uma orientação para uma dúvida recorrente, verificando-a com alguém que precise usá-la.

**Evidência:** inventário inicial, teste com resultado e instrução utilizável. Backup diário ou recuperação em 30 minutos só são requisitos se o contexto justificar essas escolhas.

### Semana 3: decidir e responder

Preencher o [plano de incidente](<../framework/templates/incidente.md>), conferir contatos e exercitar um cenário simples. Reunir direção, TI e dono do processo para decidir prioridades, riscos aceitos e recursos. Uma revisão de 30 minutos a cada duas semanas é uma configuração inicial; ajustar quando não permitir decisões suficientes.

**Evidência:** responsáveis localizáveis, decisão com prazo e risco atribuído. Um documento assinado não comprova que a resposta funcionará; o exercício revela dependências.

### Semana 4: verificar e ajustar

Escolher os [indicadores](<../framework/indicadores/operacionais.md>) que respondem às dúvidas reais da equipe. Registrar janela, origem e limitações. Reaplicar a maturidade com evidências da prática; dez respostas positivas não dispensam verificação de continuidade e responsabilidade.

Na revisão, decidir quais práticas manter, simplificar ou ampliar. Registrar próximos responsáveis e prazos. Se uma entrega ou teste não couber na janela, informar o motivo e reagendar, sem certificar uma transição inexistente.

**Evidência de conclusão do percurso:** comparação entre situação inicial e atual, pendências atribuídas e próxima revisão marcada. O percurso pode terminar com riscos ainda abertos.

### Exemplo de um começo possível

Uma empresa registra pedidos de acesso que antes chegavam por mensagens. O primeiro resultado verificável é a visibilidade de solicitante, aprovador e situação. O eventual efeito sobre tempo de atendimento precisa ser medido posteriormente. Consulte o [caso didático](<../framework/exemplos/caso-didatico.md>) para acompanhar um percurso completo.

Fundamento: adoção proporcional e governança de riscos no NIST para pequenas empresas [F01](<../framework/referencias/fontes.md#f01>); organização de tutorial conforme Diátaxis [F08](<../framework/referencias/fontes.md#f08>). A janela de 30 dias e as semanas são propostas locais do GEAR.

Anterior: [Escopo](<../framework/nucleo/escopo-principios.md>). Próxima leitura: [Maturidade](<../framework/adocao/maturidade.md>).


## Preparar a adoção e distribuir as primeiras ações

Use este roteiro quando direção e TI já concordaram em tornar a rotina visível. Ele conserva o início em duas horas e os nove passos dos guias antigos como opções de planejamento. Durações e dias são parâmetros locais; confirmar disponibilidade, permissões e responsáveis antes de usá-los.

### Uma preparação de duas horas

O resultado esperado é um primeiro conjunto de registros e pendências. A preparação não comprova implantação, recuperação ou maturidade. Se houver incidente ou risco urgente, sua resposta pode alterar a agenda.

| Janela sugerida | Ação | Saída a conferir |
| --- | --- | --- |
| Primeiros 30 minutos | Escolher registro oficial e meio alternativo quando indisponível | Canal, responsável por captura e comunicado de transição |
| Próximos 30 minutos | Criar quadro e registrar demandas conhecidas | Solicitante, executor, situação, prioridade e lacunas |
| Próximos 30 minutos | Examinar prioridades com autoridade do negócio | Até três problemas escolhidos com motivo e capacidade |
| Últimos 30 minutos | Preparar contatos e alçadas de resposta | Minuta de PRI, contatos conferidos e pendências atribuídas |

Demandas recebidas por telefone ou conversa continuam acessíveis ao registro; uma emergência não aguarda o formulário. Não apagar tarefas por classificação de quadrante. Registrar recusa, adiamento ou pedido de informação com motivo. Contatos não fornecidos ficam pendentes. Imprimir o PRI pode ajudar no acesso durante indisponibilidade, mas seu conteúdo e autoridade precisam ser conferidos.

Limite inicial: até três itens iniciados por executor, incluindo teste e bloqueio sob sua responsabilidade. Uma equipe de uma pessoa concentra a execução em uma atividade de cada vez. Se a captura das demandas não terminar na janela, registrar cobertura e plano de continuação.

### Nove passos em uma janela de 30 dias

O percurso detalha os [primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>). Os intervalos conservam a sequência histórica; alterar a ordem conforme dependências e risco. Segurança não precisa aguardar a segunda semana. Registrar mudança de data com motivo.

| Intervalo proposto | Ação | Evidência esperada |
| --- | --- | --- |
| Dias 1–2 | Aplicar maturidade e discutir problemas observados | Respostas com evidência, lacunas e prioridades atribuídas |
| Dias 3–5 | Organizar quadro e capacidade | Demandas conhecidas migradas; testes e bloqueios visíveis |
| Dias 6–7 | Comunicar registro oficial e alternativa | Pessoas sabem pedir ajuda e acompanhar a situação |
| Dias 8–10 | Preparar orientações recorrentes | FAQ testada por usuário, responsável e revisão combinada |
| Dias 11–14 | Mapear dependências críticas e testar restauração | Inventário inicial, requisitos de recuperação, resultado e limites |
| Dias 15–18 | Conferir e exercitar resposta | Contatos, alçadas, comunicação e lacunas do PRI |
| Dias 19–21 | Rever prioridades com o negócio | Decisões, recursos, responsáveis e próxima verificação |
| Dias 22–25 | Coletar indicadores úteis | Origem, janela, unidade, amostra e lacunas |
| Dias 26–30 | Comparar registros e planejar continuidade | Ações mantidas, ajustadas ou adiadas; próxima revisão |

Cinco orientações podem ser um começo para a FAQ, quando houver cinco necessidades recorrentes conhecidas. A quantidade não é critério de conclusão. Testar permissões e instruções de acesso; não fornecer credenciais no documento.

### Assistência opcional em cada etapa

TI pode pedir uma minuta de quadro, orientação, PRI, pauta ou relatório a uma ferramenta de IA com dados autorizados. A ferramenta pode organizar evidências fornecidas; não responde maturidade por suposição nem inventa contatos. Toda configuração real e integração exigem autorização, teste e revisão compatíveis com o efeito.

Para indicadores, usar cálculo determinístico e conferir unidades. Para FAQ ou bot, oferecer encaminhamento humano e medir resolução confirmada. O tempo total inclui preparação, conferência e correção. Sem IA, executar o mesmo roteiro com pessoas, quadros e registros.

### Encerrar a janela

TI apresenta registros e limitações; dono do processo confirma o que foi verificado; direção decide continuidade e risco. Pendências têm responsável e nova data. Não emitir certificação automática de nível 1 nem exigir DAN, nuvem, IA ou um projeto novo para encerrar a adoção inicial.

Fundamento conceitual de cobertura de riscos: NIST [F01](<../framework/referencias/fontes.md#f01>). Agenda, número de passos e janelas são propostas locais, sem garantia de resultado no período.

Anterior: [Primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>). Consulta: [Maturidade](<../framework/adocao/maturidade.md>) e [comparação da rotina](<../framework/indicadores/negocio-comparacao.md>).


## Maturidade com evidências

O IM-TI é um instrumento local para discutir a rotina de TI. Ele soma dez respostas binárias, de 0 a 10. Não é escala validada cientificamente, certificação ou comparação confiável entre empresas com contextos diferentes. Seu uso principal é encontrar lacunas e acompanhar a mesma organização ao longo do tempo.

### Aplicar o questionário

TI e dono do processo respondem juntos. Marcar 1 somente quando a prática ocorre e existe evidência consultável; marcar 0 quando ausente ou insuficiente. Registrar “não verificado” na observação quando faltar informação, contabilizando 0 provisoriamente. Não excluir perguntas para elevar a pontuação.

| Nº | Prática a verificar | Evidência possível |
| --- | --- | --- |
| 1 | Demandas têm registro oficial e responsável | Amostra da fila com solicitante e executor |
| 2 | Trabalho iniciado respeita a capacidade definida, incluindo testes e bloqueios | Quadro com testes, bloqueios e exceções |
| 3 | Orientações recorrentes são mantidas e verificadas | Instrução revisada por usuário, com responsável |
| 4 | Negócio e TI decidem prioridades em revisão registrada | Decisão com motivo, alçada e prazo |
| 5 | Melhorias têm problema, escopo e aceite acordados | PRD curto e verificação pelo dono do processo |
| 6 | Ativos e dependências críticos estão identificados | Inventário com proprietário e criticidade |
| 7 | Recuperação foi testada na janela combinada | Registro de restauração e limitações |
| 8 | Acessos críticos são controlados e revistos | Revisão de privilégios, MFA e exceções |
| 9 | Indicadores usados têm origem, período e revisão | Registro de dados e decisão vinculada |
| 10 | Decisões e mudanças passam por revisão responsável | Aprovação, verificação e correção registradas |

Nenhuma pergunta exige chatbot, agente, modelo generativo ou percentual de automação. O nível máximo pode ser alcançado com procedimentos manuais e controles tecnológicos apropriados.

### Interpretar sem ocultar lacunas

| IM-TI | Nível descritivo | Próxima ação típica |
| --- | --- | --- |
| 0–2 | 0: rotina pouco visível | Identificar responsáveis e registrar demandas |
| 3–5 | 1: organização inicial | Verificar continuidade e critérios de aceite |
| 6–8 | 2: práticas repetidas | Investigar lacunas e dependências entre práticas |
| 9 | 3: rotina acompanhada | Rever qualidade das evidências e resultados |
| 10 | 4: práticas verificadas | Manter a revisão e adequar o método ao contexto |

As faixas são convenções locais preservadas para continuidade do instrumento. As perguntas desta edição foram revistas: resultados antigos não são diretamente comparáveis sem reaplicação. As faixas não indicam probabilidade de ataque, retorno financeiro ou superioridade organizacional. Uma organização com pontuação alta e restauração não testada continua exposta.

### Decidir uma transição

Comparar a aplicação atual à anterior na mesma janela de evidência. Registrar o que passou a ocorrer, quem verificou e o que permanece incerto. O score pode mudar imediatamente; a **transição sustentada** exige observar a prática na rotina, por um período acordado. Não declarar avanço automático no dia 30.

Selecionar até três ações de melhoria por impacto e capacidade. Manter o resultado por pergunta junto ao total. Se uma resposta for contestada, revisar a evidência e corrigir o histórico, sem apagar a avaliação anterior.

Responsável pela aplicação: TI. Responsável pela validação de efeitos no negócio: dono do processo. Direção aceita recursos e riscos conforme a alçada. Modelo: [Registro de maturidade](<../framework/templates/maturidade.md>).

Para planejar uma melhoria específica, consultar as [fichas por domínio](<../framework/adocao/fichas-maturidade.md>). Elas preservam a matriz detalhada das versões anteriores como opções de desenvolvimento, sem acrescentar condições ao IM-TI.

Anterior: [Primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>). Para compreender: [Fundamentos e adaptações](<../framework/fundamentos/origens-adaptacoes.md>).


## Rever a carteira de iniciativas e serviços

Use quando projetos, serviços e custos precisarem ser comparados em conjunto. TI prepara registros; donos dos processos verificam uso e efeito; finanças confere custos; direção decide continuidade e recurso. Não é necessário esperar um nível de maturidade específico.

O módulo histórico de escalabilidade propunha revisão trimestral ou semestral. Essas são opções locais; escolher a janela conforme mudança, dependência e decisão necessária. Uma urgência pode exigir revisão anterior.

### Preparar a carteira

- Período, versão, responsável pela preparação e autoridade: [preencher]
- Objetivos de negócio e capacidade disponível: [preencher]
- Dados consultados e limitações de cobertura: [preencher]

| Iniciativa ou serviço | Dono e finalidade | Situação e evidência | Dependências e risco | Custo no período | Decisão necessária |
| --- | --- | --- | --- | --- | --- |
| [preencher] | | | | | |

Incluir operação, manutenção e compromissos existentes; uma carteira limitada a projetos novos pode esconder custo e dependência. Registrar benefício como hipótese ou resultado com evidência, evitando somar duas vezes capacidade liberada e sua entrega decorrente.

### Rever e decidir

1. Conferir quais itens atendem necessidade atual e quem usa seu resultado.
2. Identificar sobreposição, dependência e capacidade disputada. Dois sistemas parecidos podem ter requisitos distintos; a semelhança não autoriza encerramento.
3. Comparar continuar, ajustar, experimentar, adiar ou encerrar. Explicitar custo de transição, conservação de dados, alternativa de serviço e condição de retorno.
4. Conferir as hipóteses financeiras e suas sensibilidades. Retorno estimado favorável não elimina requisito de acesso, continuidade ou privacidade.
5. Registrar decisão, motivo, aprovador, executor, prazo e revisão. Se faltarem dados, atribuir a coleta e decidir o que pode seguir com segurança no recorte.

### Registro da decisão

| Campo | Registro |
| --- | --- |
| Item e alternativas consideradas | |
| Evidência, hipótese e lacunas | |
| Decisão e motivo | |
| Recurso e capacidade comprometidos | |
| Risco aceito e autoridade | |
| Transição, retorno e dados a conservar | |
| Executor, prazo e próxima conferência | |

### Mudança de arquitetura

O acervo associava crescimento a arquitetura evolutiva. Preservar a necessidade de conhecer dependências e custo de mudança; escolher arquitetura pela situação demonstrada. Um sistema monolítico não exige substituição automática por serviços distribuídos. Registrar o problema observável, opções, alteração mínima útil, riscos, teste e condição de retorno.

Saída: carteira com decisões localizáveis e pendências atribuídas. Concluir a revisão quando uso, custo, dependências e próximo passo estiverem explícitos para os itens discutidos. A revisão não comprova que todo investimento foi otimizado.

O formato é proposta local. A referência pública do COBIT apoia adaptação ao contexto [F09](<../framework/referencias/fontes.md#f09>); não se afirma ter implantado integralmente APO05 ou validado esta tabela. Consulta: [indicadores financeiros](<../framework/indicadores/financeiros.md>) e [responsabilidades](<../framework/templates/responsabilidades.md>).

