# Contratos para etapas de elaboração

Use quando uma tarefa precisar de histórias, código inicial, testes, relatório ou exercício de resposta. Os cinco contratos preservam a biblioteca estendida de fevereiro de 2026. São instruções locais, sem garantia de acerto, redução de tempo ou execução. IA permanece opcional.

Fornecer o recorte autorizado, dados e fontes pertinentes. Conferir a saída antes de encadear outra etapa; informação ausente permanece pendente. Tamanho P/M/G, quantidade de critérios e extensão do relatório dependem do contexto. A pessoa responsável decide uso, implantação, comunicação ou publicação.

## Histórias e critérios

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

## Código inicial delimitado

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

## Testes por comportamento

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

## Relatório para revisão de direção

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

## Exercício de mesa de resposta

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

## Exemplo fictício: acompanhamento de pedido

O prompt histórico descrevia e-commerce com estados “Processando”, “Enviado”, “Em trânsito” e “Entregue”, atualização a partir da logística, aviso por e-mail e link de acompanhamento. Conservar essas necessidades como cenário; regras de acesso e integração precisam de definição. “Tempo real” precisa de tolerância e modo de medir.

- História de consulta: cliente autorizado visualiza o estado fornecido pela logística. Conferir pedido próprio, estado conhecido, falha de atualização e apresentação no dispositivo combinado.
- História de aviso: mudança válida de estado gera aviso conforme regra acordada. Conferir destinatário autorizado, conteúdo, repetição e comportamento de falha. Opção de deixar de receber depende da regra aplicável, sem presumir equivalência entre aviso transacional e marketing.
- História de acesso: link leva ao acompanhamento com autorização apropriada. O exemplo antigo admitia pedido público sem login; a revisão deixa acesso e exposição para decisão explícita, sem publicar dados por padrão.

O PRD do exemplo sugeria reduzir chamadas em 20% e elevar satisfação em 10%. São alvos fictícios sem definição de baseline ou unidade; não são resultados nem metas do GEAR. Preparar coleta e forma de comparação antes de avaliar efeito. Logística, suporte, TI e cliente eram os perfis do exercício, sem presumir responsáveis de uma empresa real.

## Rever e manter a biblioteca

Registrar tarefa, versão, responsável, ambiente/modelo quando usado, fontes, exemplos, comportamento esperado e resultado da verificação. Rever após mudança material de fonte, processo, permissões ou ferramenta. Manter alternativa manual e histórico, sem tornar a biblioteca condição de maturidade.

Fornecer exemplos e dividir etapas são opções de preparação; autorrevisão por modelo continua assistência. A justificativa deve apresentar fonte, cálculo e limite verificáveis. Solicitar raciocínio interno extenso não substitui evidência. Fine-tuning ou troca de modelo, citados no acervo, exigem avaliação própria; não se afirma que eliminem erros ou que prompt seja sempre mais importante que o modelo.

Saída: minuta por etapa e revisão registrada. Concluir quando a tarefa tem limites, critérios, fontes disponíveis e pendências, com decisão de uso atribuída. Modelos relacionados: [instrução de assistência](instrucao-assistencia.md), [quatro funções](prompts-assistencia.md) e [revisão de saída](revisao-ia.md).
