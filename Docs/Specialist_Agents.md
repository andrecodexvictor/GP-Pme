# Funções de assistência e contratos

Edição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.

## Origem e decisão editorial

Quatro funções conceituais: direção, entrega, segurança e auditoria. A implementação tem um orquestrador e oito especialistas; não são quatro agentes já implantados. Entradas e instruções completas estão abaixo. A revisão verifica dados, fontes e efeitos; não exige exposição de raciocínio interno. Sem orçamento, informar estimativa de horas com unidade e origem, sem fabricar DAN financeira. Ação real requer alçada, permissão e execução conferidas.

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

Modelos: [contratos de histórias, código, testes, relatório e exercício](<../framework/templates/prompts-etapas.md>) e [revisão de saída assistida](<../framework/templates/revisao-ia.md>). Para a fundamentação e limites: [Origens e adaptações](<../framework/fundamentos/origens-adaptacoes.md>).


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

Aplicar o [registro de revisão](<../framework/templates/revisao-ia.md>). Um texto aprovado deve permitir localizar fatos, premissas, fontes e pessoa responsável. A adesão do prompt a um formato não comprova correção da saída.

Origem: quatro system prompts em `GP-PME antigravity/GP-Pme complete/Capitulo_6_Motor_de_IA_e_Engenharia_de_Prompts.md`. As instruções foram revistas para retirar garantia de proteção, faixas financeiras sem suporte e prazo obrigatório de MVP. São contratos locais de assistência. Convenções: [financeiros](<../framework/indicadores/financeiros.md>); contexto: [usar IA](<../framework/guias/usar-ia.md>).


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

Concluir a preparação quando tarefa, dados, saída, lacunas e revisão estão claros. Aplicação: [usar IA](<../framework/guias/usar-ia.md>). Contratos específicos: [quatro funções](<../framework/templates/prompts-assistencia.md>).


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

Fundamento: instrumento local de avaliação, derivado dos indicadores candidatos do acervo. Estudos sobre assistência têm tarefas e populações próprios; seus resultados não predizem o ganho desta equipe. Consulte [a bibliografia do manuscrito](<../GP-Pme%20Article/overleaf/references.bib>) e os [limites de atribuição das fontes](<../framework/referencias/fontes.md>).

Consulta: [comparação da rotina](<../framework/indicadores/negocio-comparacao.md>) e [revisão de saída assistida](<../framework/templates/revisao-ia.md>).

