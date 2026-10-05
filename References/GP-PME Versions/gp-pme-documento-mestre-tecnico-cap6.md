# GEAR: Assistência e revisão

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: Sem autoria, versão ou data declaradas neste arquivo; não atribuídas por inferência.

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Usar assistência por IA](#usar-assistencia-por-ia)
- [Instrução de tarefa e assistência](#instrucao-de-tarefa-e-assistencia)
- [Prompts para quatro funções de assistência](#prompts-para-quatro-funcoes-de-assistencia)
- [Contratos para etapas de elaboração](#contratos-para-etapas-de-elaboracao)
- [Instruções para revisar requisitos e rotina](#instrucoes-para-revisar-requisitos-e-rotina)
- [Revisão de uma saída assistida por IA](#revisao-de-uma-saida-assistida-por-ia)
- [Comparar uma tarefa com e sem assistência](#comparar-uma-tarefa-com-e-sem-assistencia)

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


## Instrução de tarefa e assistência

Use para delegar uma tarefa a uma pessoa ou preparar um pedido de assistência por IA. O responsável fornece contexto autorizado e define quem revisa. O formato conserva o antigo Formulário de Alinhamento de Instrução (FAI), sem presumir que uma persona ou lista impede erro.

### Modelo copiável

```text
Tarefa e papel necessário: [ação delimitada e especialização pertinente].
Contexto: [serviço, processo, problema observado e pessoas afetadas].
Dados autorizados: [origem, data, unidade, período e limitações].
Restrições: [capacidade, orçamento conhecido, permissões e dependências].
Entradas: [documentos e dados fornecidos, separados das instruções].
Etapas: [ações necessárias e pontos de conferência].
Saída: [formato, seções, extensão adequada e critérios verificáveis].
Autoridade: [quem revisa e quem pode aprovar efeitos].
Lacunas: registrar dado insuficiente e o que obter; não preencher por suposição.
Estimativas: informar fonte, unidade, período, método e incerteza.
Fontes externas: conferir versão e trecho; citar junto à afirmação.
Fatos, hipóteses e propostas permanecem identificados.
Comandos, configurações e mudanças só são executados com autorização adequada.
```

Para uma pessoa, combinar papel, dados, etapas, saída e alçada antes de iniciar. Para IA, limitar acesso aos dados necessários e conferir a saída. Nenhuma forma elimina o trabalho de revisão. Dados históricos de mercado só entram como premissa quando sua fonte e pertinência foram verificadas; não suprem custo real da organização.

### Exemplo fictício: preparar migração de e-mail

O exemplo anterior mencionava Advocacia Lima, dez usuários, provedor IMAP, histórico de dois anos e licenças Microsoft 365 Business Basic. Esses dados são um cenário didático, sem evidência de organização real, aquisição ou viabilidade de migração.

```text
Tarefa: preparar uma proposta de migração de e-mail para avaliação humana.
Contexto fictício: escritório jurídico com dez usuários e histórico de dois
anos em provedor IMAP; licenças Microsoft 365 Business Basic informadas.
Janela desejada: sexta-feira às 19h; gestão DNS informada no Registro.br.
Saída: etapas de preparação, preservação e conferência das mensagens,
opções de janela, condição de retorno e testes de envio/recebimento.
Campos a conferir: domínio, caixas, volume, autenticação, ferramentas de
migração suportadas, registros DNS, retenção e dependências do fornecedor.
Indicar a fonte oficial e versão para qualquer procedimento específico.
Deixar valores DNS pendentes até conferência; não inventar servidores.
Não garantir tempo de propagação nem ausência de interrupção.
O responsável por TI confere viabilidade; autoridade aprova a mudança.
```

O exemplo é um pedido de planejamento, não roteiro técnico verificado de Microsoft 365 ou Registro.br. A menção antiga a PST, TXT, MX, SPF, DKIM e TTL passa a ser lista de aspectos a investigar conforme o ambiente e documentação oficial; nenhum valor ou prazo é prescrito aqui.

Concluir a preparação quando tarefa, dados, saída, lacunas e revisão estão claros. Aplicação: [usar IA](<../../framework/guias/usar-ia.md>). Contratos específicos: [quatro funções](<../../framework/templates/prompts-assistencia.md>).


## Prompts para quatro funções de assistência

Use quando a equipe escolhe assistência por IA para uma tarefa delimitada. Estes textos preservam as quatro funções do capítulo técnico anterior; não descrevem a quantidade de especialistas de software nem autorizam execução. Quem prepara informa contexto e dados autorizados; quem tem alçada revisa a saída. Uma equipe pode executar a mesma tarefa sem IA.

### Direção e prioridades

```text
Tarefa: preparar uma pauta ou minuta de decisão do GEAR.
Contexto: [processo, demandas, capacidade, decisões anteriores e riscos].
Dados autorizados: [origem, janela, unidades e limitações].
Autoridade de decisão: [pessoa e alçada].
Saída: problema, alternativas, finalidade de negócio, recurso necessário,
risco, responsável, prazo, evidência esperada e próxima revisão.
Relacionar a iniciativa a receita, custos, experiência ou resiliência,
declarando hipótese de benefício e efeitos secundários quando houver.
Usar português direto, títulos informativos e registro breve consultável.
Informar dados insuficientes e decisões pendentes. Conferir cálculos com
regra determinística; indicar fontes externas no ponto da afirmação.
A pessoa responsável revisa a pauta; a autoridade identificada decide.
```

### Requisitos e entrega

```text
Tarefa: preparar PRD e critérios verificáveis para uma melhoria do GEAR.
Contexto: [problema observado, usuário e processo beneficiado].
Dados autorizados: [fontes e evidências disponíveis].
Restrições: [permissões, dependências, recurso, capacidade e prazo].
Saída: problema, hipótese, escopo, exclusões, histórias de usuário,
critérios Dado/Quando/Então, riscos, teste, retorno e aceite esperado.
Uma ou duas semanas podem orientar um piloto se o escopo couber na
capacidade informada. Se faltar informação, registrar a pergunta e seu
responsável. Estimativas devem ter origem, unidade e incerteza.
Conferir cada etapa antes de preparar a seguinte. Código inicial e roteiro
de teste são propostas; registrar separadamente execução e resultado.
Dono do processo aprova requisitos e aceite; TI confere viabilidade.
```

### Segurança e continuidade

```text
Tarefa: preparar análise de lacunas ou plano breve de resposta do GEAR.
Contexto: [serviço, ativos, dependências, risco observado e controles].
Dados autorizados: [relato, configuração, evidência e limites de acesso].
Autoridade: [quem decide contenção, comunicação e recuperação].
Saída: fatos, hipóteses, dados insuficientes, opções de tratamento,
responsável, contatos a conferir, verificação e risco residual.
Priorizar conforme criticidade do serviço, sem usar 80/20 como medida de
risco. Comparar alternativas por cobertura, esforço e manutenção.
Conferir CVEs e fontes primárias antes de citar uma vulnerabilidade.
Propor contenção apropriada ao ambiente, preservando evidências. A pessoa
com alçada autoriza a ação; o executor verifica recuperação com o negócio.
Dez verificações locais não equivalem ao NIST CSF ou CIS IG1 completos.
```

### Indicadores e revisão

```text
Tarefa: conferir premissas, unidades, cálculos e referências do GEAR.
Entrada: [documento, dados, período, moeda, origem e limitações].
DAN financeiro local = custo estimado de refatoração / orçamento anual TI.
Indicar método, escopo e incerteza; não atribuir faixas universais de risco.
ROI líquido no período = (benefício bruto - recorrência - investimento)
/ investimento * 100. Razão bruta = benefício bruto / investimento.
Payback simples mensal = investimento / benefício líquido mensal positivo,
somente se fluxos forem constantes. Sem benefício positivo, não é finito.
Horas liberadas são capacidade potencial salvo redução de despesa comprovada.
Manter precisão no cálculo e declarar arredondamento na apresentação.
Conferir a afirmação na fonte citada e distinguir proposta, simulação e
resultado observado. Se faltar moeda, custo ou período, registrar a lacuna;
informar horas isoladamente não permite afirmar ROI financeiro.
Saída: memória de cálculo, divergências, incerteza e revisão humana necessária.
```

### Conferir o uso

Aplicar o [registro de revisão](<../../framework/templates/revisao-ia.md>). Um texto aprovado deve permitir localizar fatos, premissas, fontes e pessoa responsável. A adesão do prompt a um formato não comprova correção da saída.

Origem: quatro system prompts em `GP-PME antigravity/GP-Pme complete/Capitulo_6_Motor_de_IA_e_Engenharia_de_Prompts.md`. As instruções foram revistas para retirar garantia de proteção, faixas financeiras sem suporte e prazo obrigatório de MVP. São contratos locais de assistência. Convenções: [financeiros](<../../framework/indicadores/financeiros.md>); contexto: [usar IA](<../../framework/guias/usar-ia.md>).


## Contratos para etapas de elaboração

Use quando uma tarefa precisar de histórias, código inicial, testes, relatório ou exercício de resposta. Os cinco contratos preservam a biblioteca estendida de fevereiro de 2026. São instruções locais, sem garantia de acerto, redução de tempo ou execução. IA permanece opcional.

Fornecer o recorte autorizado, dados e fontes pertinentes. Conferir a saída antes de encadear outra etapa; informação ausente permanece pendente. Tamanho P/M/G, quantidade de critérios e extensão do relatório dependem do contexto. A pessoa responsável decide uso, implantação, comunicação ou publicação.

### Histórias e critérios

```text
Tarefa: transformar o PRD fornecido em histórias e critérios verificáveis.
Entrada: [PRD, regras conhecidas, perfis, contexto e fontes autorizadas].
Saída: Como [perfil], quero [ação], para [finalidade]; critérios pertinentes
em Dado/Quando/Então, dependências e lacunas por história.
Preservar problema, escopo e exclusões acordados. Distinguir requisito
fornecido, hipótese e proposta; não inventar tela, regra ou integração.
Se pedido, propor tamanho P/M/G com fatores e incerteza para a capacidade
informada. Tamanho relativo não é estimativa comprovada de prazo.
Critérios descrevem condição, ação, resultado e modo de verificar.
Segurança, erro e recuperação entram quando pertinentes ao efeito.
Entregar minuta e pendências para revisão técnica e do dono do processo.
```

### Código inicial delimitado

```text
Tarefa: preparar estrutura inicial para a história e critérios fornecidos.
Entrada: [história, ambiente, linguagem, framework, versões e restrições].
Saída: proposta de arquivos, interfaces e código no recorte solicitado,
com dependências, configuração necessária, lacunas e modo de verificar.
Python/Flask é uma opção do exemplo histórico, não tecnologia obrigatória.
Se esse ambiente for confirmado, preparar rota, método HTTP, validação
pertinente e placeholder explícito da lógica ainda não implementada.
Separar exemplo de uso e resultado executado. Segredo fica em configuração
apropriada, nunca incorporado ao exemplo. Conferir entrada, acesso e erro.
Não declarar endpoint funcional, integração real ou implantação por gerar
código. Registrar ferramenta executada e resultado somente quando ocorrer.
Pessoa responsável revisa dependências, código, testes e autorização.
```

### Testes por comportamento

```text
Tarefa: preparar testes pertinentes para código e critérios fornecidos.
Entrada: [código, história, critérios, ambiente e dependências].
Saída: testes ou roteiro para sucesso, falha e fronteiras materiais,
indicando qual critério cada caso verifica e que efeito fica fora do recorte.
Python/Pytest é opção histórica; confirmar linguagem e executor disponíveis.
Evitar teste que só repita o código sem verificar comportamento necessário.
Distinguir falha da implementação, falha do ambiente e requisito ambíguo.
Marcar roteiro ou código preparado como não executado até haver resultado.
Informar comando, ambiente, resultado e limite quando a execução ocorrer.
Aprovação técnica não comprova benefício financeiro ou aceite do negócio.
```

### Relatório para revisão de direção

```text
Tarefa: preparar relatório executivo com os registros fornecidos.
Entrada: [indicadores com origem/período, carteira, decisões, riscos e metas].
Saída: situação, evidências, prioridades, riscos, alternativas, decisão
necessária e pendências com responsável. Usar linguagem direta.
Escolher indicadores pela decisão: disponibilidade/restauração/satisfação
ou custo TI/receita/prazo e orçamento, conforme dados e definições conhecidas.
Não chamar esses dois conjuntos de trio único obrigatório do framework.
Conferir numerador, denominador, janela, amostra e memória de cálculo.
Usar metas acordadas; falta de dado não vira resultado ou causa presumida.
Uma página pode orientar síntese, sem omitir informação material.
Identificar minuta e pessoa com alçada; aprovação e reunião não são simuladas.
```

### Exercício de mesa de resposta

```text
Tarefa: preparar cenário fictício de exercício de mesa de incidente.
Entrada: [serviço/ativo, ameaça escolhida, dependências, PRI e participantes].
Saída: objetivo, limites, descrição fictícia, linha do tempo de eventos,
perguntas por etapa, decisões/alçadas, comunicação e registro de correções.
Exemplos históricos: e-commerce, serviço de arquivos, ransomware ou phishing
com acesso indevido. A escolha não confirma ocorrência ou vulnerabilidade.
Indicar os dados necessários para avaliar contenção e recuperação; não
prescrever desligamento, isolamento ou formatação para qualquer ambiente.
O exercício discute decisões. Alterar sistemas, executar varredura ou enviar
comunicação real exige escopo e autorização próprios.
Registrar participantes, decisões observadas, lacunas, responsáveis e revisão.
Um exercício não comprova eficácia de resposta em qualquer incidente.
```

### Exemplo fictício: acompanhamento de pedido

O prompt histórico descrevia e-commerce com estados “Processando”, “Enviado”, “Em trânsito” e “Entregue”, atualização a partir da logística, aviso por e-mail e link de acompanhamento. Conservar essas necessidades como cenário; regras de acesso e integração precisam de definição. “Tempo real” precisa de tolerância e modo de medir.

- História de consulta: cliente autorizado visualiza o estado fornecido pela logística. Conferir pedido próprio, estado conhecido, falha de atualização e apresentação no dispositivo combinado.
- História de aviso: mudança válida de estado gera aviso conforme regra acordada. Conferir destinatário autorizado, conteúdo, repetição e comportamento de falha. Opção de deixar de receber depende da regra aplicável, sem presumir equivalência entre aviso transacional e marketing.
- História de acesso: link leva ao acompanhamento com autorização apropriada. O exemplo antigo admitia pedido público sem login; a revisão deixa acesso e exposição para decisão explícita, sem publicar dados por padrão.

O PRD do exemplo sugeria reduzir chamadas em 20% e elevar satisfação em 10%. São alvos fictícios sem definição de baseline ou unidade; não são resultados nem metas do GEAR. Preparar coleta e forma de comparação antes de avaliar efeito. Logística, suporte, TI e cliente eram os perfis do exercício, sem presumir responsáveis de uma empresa real.

### Rever e manter a biblioteca

Registrar tarefa, versão, responsável, ambiente/modelo quando usado, fontes, exemplos, comportamento esperado e resultado da verificação. Rever após mudança material de fonte, processo, permissões ou ferramenta. Manter alternativa manual e histórico, sem tornar a biblioteca condição de maturidade.

Fornecer exemplos e dividir etapas são opções de preparação; autorrevisão por modelo continua assistência. A justificativa deve apresentar fonte, cálculo e limite verificáveis. Solicitar raciocínio interno extenso não substitui evidência. Fine-tuning ou troca de modelo, citados no acervo, exigem avaliação própria; não se afirma que eliminem erros ou que prompt seja sempre mais importante que o modelo.

Saída: minuta por etapa e revisão registrada. Concluir quando a tarefa tem limites, critérios, fontes disponíveis e pendências, com decisão de uso atribuída. Modelos relacionados: [instrução de assistência](<../../framework/templates/instrucao-assistencia.md>), [quatro funções](<../../framework/templates/prompts-assistencia.md>) e [revisão de saída](<../../framework/templates/revisao-ia.md>).


## Instruções para revisar requisitos e rotina

Contratos locais recuperados da biblioteca acadêmica anterior. Usar dados autorizados e revisar a saída antes de agir. Campo sem dado permanece pendente. Nenhuma instrução exige uso de IA no método.

### Refinar um PRD

```text
Tarefa: revisar o PRD fornecido, sem adicionar escopo aprovado.
Entradas: PRD, objetivo, usuários, restrições, dependências e critério de aceite.
Saída: trecho ambíguo; consequência; proposta de redação; pergunta pendente;
requisito afetado; fonte da informação. Separar sugestão de requisito aprovado.
Conferir escopo, exclusões, autorização de acesso, requisitos não funcionais,
testabilidade e medidas com unidade, período, responsável e origem.
Não presumir prazo ou benefício. Dono do processo aprova requisitos; TI confere viabilidade.
```

### Preparar cenários de teste

```text
Tarefa: propor testes para a história e os critérios fornecidos.
Entradas: história aprovada, critérios, perfis de acesso, regras, ambiente e restrições.
Saída por teste: requisito; contexto; ação; resultado esperado; dados;
caso positivo, negativo ou limite; forma de observar; responsável.
Apontar critério não testável e pedir a decisão necessária. Não inventar comportamento.
Não afirmar que testes foram executados. Pessoa responsável confere cobertura e ambiente.
```

### Preparar um plano de resposta

```text
Tarefa: preparar minuta de PRI para o serviço e cenário informados.
Entradas: serviço, dependências, sintomas, controles, cópias, contatos, alçadas,
tolerâncias de recuperação e perda de dados, comunicação e apoio externo.
Saída: reconhecer e registrar; acionar contatos; opções de contenção e seus riscos;
preservar evidências; recuperar em ambiente autorizado; verificar serviço e dados;
comunicar fatos confirmados; atribuir pendências e revisão.
Não inventar telefones, comprometimento, prazo legal ou alçada. Não prescrever
desligamento, formatação ou isolamento como ação universal. Plano depende de
aprovação da autoridade, conferência dos contatos e exercício. Incidente real
segue a competência e o plano aprovados, sem aguardar esta minuta.
```

### Examinar registros de operação

```text
Tarefa: examinar os registros autorizados fornecidos.
Entradas: logs, período, fuso, serviço, evento investigado e limites de coleta.
Saída: ocorrência com referência ao registro; padrão observado; explicações
possíveis; dados faltantes; verificação proposta; responsável e alçada.
Separar observação de hipótese. Não inferir causa ou ataque de correlação isolada.
Não fabricar CVE. Não executar correção nem divulgar registros sensíveis.
```

### Propor uma melhoria de processo

```text
Tarefa: rever o processo descrito e preparar opções de melhoria.
Entradas: etapas reais, responsáveis, tempos, bloqueios, demanda, capacidade,
restrições, registros disponíveis e objetivo de negócio.
Saída: problema observado; opção; alternativa; custo/esforço; risco;
hipótese de benefício; piloto; aceite; medida; dono; decisão necessária.
Não prometer redução de tempo nem atribuir procedimento local ao ITIL integral.
Quantidade de opções e cadência são ajustáveis. Autoridade decide; executor testa;
dono do processo aceita e revê o benefício no período acordado.
```

### Conferir e conservar

Concluir quando entradas, lacunas, proposta e responsável pela revisão estão visíveis. Na biblioteca, registrar versão da instrução, ferramenta/modelo, exemplo fictício, resultado conferido e data de revisão. Uma justificativa produzida pela ferramenta não substitui evidência externa ou teste técnico.

Consulta: [assistência opcional](<../../framework/guias/usar-ia.md>), [PRD e aceite](<../../framework/templates/prd-aceite.md>), [incidente](<../../framework/templates/incidente.md>) e [fontes](<../../framework/referencias/fontes.md>). Os contratos são propostas do GEAR, sem validação causal atribuída à literatura.


## Revisão de uma saída assistida por IA

Aplicar antes de usar uma saída de IA em decisão, comunicação ou mudança. O responsável humano pela tarefa verifica conteúdo e autorização. Não enviar dado restrito a uma ferramenta sem permissão e controles adequados.

- Tarefa, data, responsável e ferramenta/modelo quando conhecido: [preencher]
- Informações fornecidas e classificação: [preencher sem reproduzir segredo]
- Saída pretendida e autoridade para usá-la: [preencher]
- Fatos conferidos e fontes consultadas: [preencher]
- Citações verificadas no documento original: [preencher]
- Cálculos, unidades e premissas conferidos: [preencher]
- Dados pessoais ou confidenciais removidos/protegidos: [preencher]
- Limitações, erro observado e correção: [preencher]
- Aprovação, rejeição ou necessidade de investigação: [pessoa e motivo]
- Evidência da versão usada e próxima revisão: [preencher]

Uma resposta fluente não é evidência. Se não for possível verificar uma afirmação material, retirá-la, restringi-la ou identificá-la como hipótese. A assinatura do revisor não substitui acesso à fonte.

Conclusão: somente a saída revisada e autorizada segue para uso. A equipe pode executar a mesma tarefa sem IA.

### Conferências por tipo de saída

Aplicar os blocos pertinentes ao efeito proposto, registrando motivo quando um item não se aplica. Uma conferência feita por outro modelo pode ajudar a localizar divergências, mas não substitui o revisor humano nem comprova ausência de erro.

#### Rastreabilidade

- [ ] Fatos correspondem aos dados fornecidos ou a fontes conferidas?
- [ ] Sistemas, interfaces e configurações reais estão separados das propostas?
- [ ] Lacunas, estimativas e incertezas estão explícitas?
- [ ] Referências indicam versão e trecho que sustenta a afirmação?
- [ ] Cálculos usam moeda, unidades, período e premissas compatíveis?

Uma alternativa de ferramenta pode ser proposta com justificativa, custo e verificação pendentes; ela não passa a ser uma aquisição real. Não exigir marcas já compradas para toda análise nem considerar qualquer sugestão uma configuração existente.

#### Requisitos

- [ ] História descreve usuário, comportamento e finalidade verificáveis?
- [ ] Critério informa condição, ação e resultado observável?
- [ ] Escopo e exclusões foram acordados com o negócio?
- [ ] Dependências e capacidade tornam o recorte viável ou têm lacunas atribuídas?

#### Segurança e continuidade

- [ ] Acesso proposto é necessário ao efeito e suas exceções foram revistas?
- [ ] Controles têm cobertura e evidência, sem promessa de proteção integral?
- [ ] Recuperação e contenção consideram ambiente, autoridade e preservação de evidências?
- [ ] Recursos e manutenção foram considerados, inclusive para soluções nativas?

#### Código e configuração

- [ ] Dependências, APIs, comandos e valores foram conferidos na versão aplicável?
- [ ] Entrada, acesso e erros relevantes foram testados em ambiente autorizado?
- [ ] Segredos e detalhes internos não aparecem indevidamente na saída?
- [ ] Regras de negócio implementadas têm revisão e critérios acordados?
- [ ] Placeholder, demonstração e integração real estão identificados?
- [ ] Plano de retorno e aprovação para a mudança estão registrados?

Código inicial pode conter lacunas explícitas; não é apto ao uso operacional apenas por ser executável. Também não há proibição universal de gerar lógica completa: seu uso exige revisão, testes e autorização apropriados.

### Registrar o resultado

| Item/afirmação | Evidência consultada ou teste | Resultado e limitação | Correção necessária | Responsável |
| --- | --- | --- | --- | --- |
| [preencher] | | | | |

Decisão: [aprovado para o uso delimitado / ajustar / rejeitar / investigar], com pessoa, data, motivo, versão e pendências. Aprovação editorial não autoriza automaticamente implantação. Erro material exige correção ou restrição do uso; registrar divergência sem prometer “zero alucinações”. Duração de cinco minutos e revisão de três fatos não são critérios de qualidade.


## Comparar uma tarefa com e sem assistência

Use quando houver uma decisão sobre continuar, ajustar ou suspender o uso de IA. A pessoa responsável pela tarefa define o recorte; quem aceita a entrega confere qualidade; direção decide investimento. A equipe pode atingir qualquer nível de maturidade sem adotar IA.

### Preparar uma comparação útil

Escolher tarefas comparáveis, registrar dificuldade, experiência do executor, ferramenta, versão, dados permitidos e critério de aceite. Medir todo o esforço: preparação, geração, leitura, conferência, correção e teste. Cronometrar somente a geração omite trabalho necessário.

| Medida local | Cálculo ou registro | Limite de interpretação |
| --- | --- | --- |
| Tempo por entrega aceita | Esforço total até o aceite | Comparar tarefas com escopo e qualidade equivalentes |
| Variação relativa de tempo | (tempo de referência − tempo assistido) / tempo de referência × 100 | Referência positiva; valor negativo indica aumento de esforço |
| Aceitação sem revisão relevante | Entregas aceitas sem correção relevante / entregas avaliadas × 100 | Definir “relevante”; aceite não prova ausência de erro |
| Erros por entrega | Erros identificados / entregas verificadas | Manter o mesmo método e profundidade de verificação |
| Custo por entrega aceita | Custos atribuíveis / entregas aceitas | Incluir ferramenta, revisão, correção e infraestrutura |
| Capacidade recuperada | Horas de referência − horas assistidas | Tempo potencial, sem equivalência automática a economia financeira |

Os nomes históricos TGA, TMRIA, TAA, CAG e TEIA descreviam tempo, aceitação, custo ou variação. A edição vigente exige unidade e evento de início/fim explícitos. Resposta inicial, restauração de serviço e fechamento administrativo são medidas distintas. Não atribuir causalidade à IA se o processo, a equipe ou o tipo de demanda também mudou.

### Decidir com os resultados

1. Conferir amostra, exclusões, falhas e tarefas não concluídas.
2. Comparar esforço e qualidade, conservando os registros individuais.
3. Examinar se a vantagem depende de dados, pessoa, fornecedor ou contexto específicos.
4. Registrar continuar, ajustar, ampliar o teste ou suspender; indicar dono e próxima verificação.

Concluir quando a decisão pode ser reconstruída a partir das entradas e das entregas verificadas. Sem baseline, registrar apenas a medição atual. Sem denominador ou observações comparáveis, não preencher percentual. A antiga meta de redução de 60% não é requisito do GEAR.

Fundamento: instrumento local de avaliação, derivado dos indicadores candidatos do acervo. Estudos sobre assistência têm tarefas e populações próprios; seus resultados não predizem o ganho desta equipe. Consulte [a bibliografia do manuscrito](<../../GP-Pme%20Article/overleaf/references.bib>) e os [limites de atribuição das fontes](<../../framework/referencias/fontes.md>).

Consulta: [comparação da rotina](<../../framework/indicadores/negocio-comparacao.md>) e [revisão de saída assistida](<../../framework/templates/revisao-ia.md>).


## Rever riscos de adoção

Resistência, sobrecarga inicial, pouco uso dos registros e expectativas indevidas são riscos de aplicação presentes no acervo. TI e direção escolhem um recorte dentro da capacidade, explicam o acordo e observam o uso com as pessoas afetadas. Treinamento e gamificação não garantem adesão. Ajustar ferramenta ou registro quando o esforço não apoiar uma decisão.

Falta de direção exige alçada e decisão identificáveis; reunião sem decisão não resolve a lacuna. Requisitos ambíguos exigem conversa e critério testável. Falsa sensação de segurança exige conferir cobertura e teste; política ou compra não prova proteção. Biblioteca desatualizada exige curadoria somente se houver uso de assistência. Registrar dono, ação, evidência e próxima revisão para cada risco relevante.

Os percentuais, prazos e gates das versões anteriores eram propostas locais sem validação. Segurança urgente não espera nível de maturidade, implantação de quadro ou conclusão de outro módulo. A revisão de aplicação real continua necessária; testes deste repositório não comprovam efetividade organizacional.


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
