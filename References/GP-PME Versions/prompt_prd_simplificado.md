# GEAR: Preparar e revisar requisitos

Framework de governança e gestão de TI para pequenas e médias empresas. Edição editorial 2026.10. Caminho histórico GP-PME mantido para compatibilidade.

Origem documental: Sem autoria, versão ou data declaradas neste arquivo; não atribuídas por inferência.

Direitos conforme [LICENSE.md](../../LICENSE.md). Originais preservados em `.context/originais/gear-2026-10-04/`; decisões e destinos por seção constam da matriz de proveniência. Este manual completo usa as regras canônicas vigentes.

## Percurso de consulta

- [Prompts para quatro funções de assistência](#prompts-para-quatro-funcoes-de-assistencia)
- [Instruções para revisar requisitos e rotina](#instrucoes-para-revisar-requisitos-e-rotina)

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


Consulta vigente: [documentação modular](../../framework/README.md) e [fontes e limites](../../framework/referencias/fontes.md).
