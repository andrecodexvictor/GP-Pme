# Instruções para revisar requisitos e rotina

Contratos locais recuperados da biblioteca acadêmica anterior. Usar dados autorizados e revisar a saída antes de agir. Campo sem dado permanece pendente. Nenhuma instrução exige uso de IA no método.

## Refinar um PRD

```text
Tarefa: revisar o PRD fornecido, sem adicionar escopo aprovado.
Entradas: PRD, objetivo, usuários, restrições, dependências e critério de aceite.
Saída: trecho ambíguo; consequência; proposta de redação; pergunta pendente;
requisito afetado; fonte da informação. Separar sugestão de requisito aprovado.
Conferir escopo, exclusões, autorização de acesso, requisitos não funcionais,
testabilidade e medidas com unidade, período, responsável e origem.
Não presumir prazo ou benefício. Dono do processo aprova requisitos; TI confere viabilidade.
```

## Preparar cenários de teste

```text
Tarefa: propor testes para a história e os critérios fornecidos.
Entradas: história aprovada, critérios, perfis de acesso, regras, ambiente e restrições.
Saída por teste: requisito; contexto; ação; resultado esperado; dados;
caso positivo, negativo ou limite; forma de observar; responsável.
Apontar critério não testável e pedir a decisão necessária. Não inventar comportamento.
Não afirmar que testes foram executados. Pessoa responsável confere cobertura e ambiente.
```

## Preparar um plano de resposta

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

## Examinar registros de operação

```text
Tarefa: examinar os registros autorizados fornecidos.
Entradas: logs, período, fuso, serviço, evento investigado e limites de coleta.
Saída: ocorrência com referência ao registro; padrão observado; explicações
possíveis; dados faltantes; verificação proposta; responsável e alçada.
Separar observação de hipótese. Não inferir causa ou ataque de correlação isolada.
Não fabricar CVE. Não executar correção nem divulgar registros sensíveis.
```

## Propor uma melhoria de processo

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

## Conferir e conservar

Concluir quando entradas, lacunas, proposta e responsável pela revisão estão visíveis. Na biblioteca, registrar versão da instrução, ferramenta/modelo, exemplo fictício, resultado conferido e data de revisão. Uma justificativa produzida pela ferramenta não substitui evidência externa ou teste técnico.

Consulta: [assistência opcional](../guias/usar-ia.md), [PRD e aceite](prd-aceite.md), [incidente](incidente.md) e [fontes](../referencias/fontes.md). Os contratos são propostas do GEAR, sem validação causal atribuída à literatura.
