# Perfil D — Serviços com dados pessoais

Cenário didático do GEAR para 100 colaboradores. Os valores de partida e de melhoria são **premissas fictícias do acervo**, preservadas para comparar hipóteses. Não descrevem uma implantação realizada. Cálculos: [Calculadora de ROI](Calculadora_ROI.md); convenções: [indicadores financeiros](../framework/indicadores/financeiros.md).

## 1. Retrato e escopo

| Item | Premissa |
| --- | --- |
| Setor | Serviços B2B com dados pessoais, como saúde, finanças ou educação |
| Pessoas | 100 |
| Faturamento anual | R$ 45.000.000,00 |
| Equipe | Seis pessoas: coordenador, três analistas de suporte e infraestrutura, desenvolvedor de integrações e especialista de segurança. Faixa histórica de cinco a oito pessoas. O papel de encarregado de dados exige definição própria. |
| Orçamento anual de TI | R$ 1.200.000,00 |
| Ambiente | ERP e CRM em nuvem, atendimento próprio, Microsoft 365, ambiente de dados com acesso restrito, mais de 100 estações, APIs e duas filiais. |

Os valores de faturamento e orçamento situam o exercício. Não constituem benchmark de porte, pessoal ou gasto. A alocação de salários e infraestrutura do texto antigo não foi verificada como orçamento de uma empresa real.

## 2. Situação de partida

Há um canal oficial, mas gerentes também ligam ao coordenador. Cada analista prioriza sem regra comum. Integrações entre CRM, atendimento e ERP falham. O inventário de dados e a revisão de acesso são insuficientes para examinar o tratamento de dados pessoais.

A linha de base adota custo TI de R$ 70,00/h, custo de usuário de R$ 25/h e janela anual de 4.500 h. Pessoas afetadas pela indisponibilidade: 80. Volume hipotético: 2.400 incidentes/ano, equivalente a 200,00 por mês e 2,00 por pessoa/mês.

Os custos-hora são valores arredondados do exemplo histórico, sem pesquisa salarial. Encargos de 1,55 e jornada de 176 h/mês são hipóteses locais, a substituir pelo custo real.

O DAN inicial usa 3.000 h de refatoração × R$ 70,00/h ÷ R$ 1.200.000,00: 0,175. As antigas cores e faixas não são limites financeiros validados.

A soma dos três componentes de tempo da situação de partida é R$ 30.350,00/mês. Esse valor representa capacidade avaliada monetariamente, sem receita perdida, impostos ou dupla contagem entre categorias. Se as horas de indisponibilidade já estiverem nas horas de retrabalho, retirar a sobreposição.

## 3. Plano inicial de 30 dias

TI organiza a execução; o dono do processo negocia prioridades e verifica entregas. [Primeiros 30 dias](../framework/adocao/primeiros-30-dias.md) define o percurso. Esforço hipotético inicial: 90 h somadas, distribuídas abaixo; ajustar à capacidade real.

| Janela | Trabalho | Evidência de conclusão | Horas |
| --- | --- | --- | ---: |
| Dias 1–7 | Diagnóstico; canal oficial; quadro e responsáveis | Pedidos migrados e política de trabalho iniciado acordada | 30 |
| Dias 8–14 | Orientações para senha, acesso, crm, erp e atendimento; inventário de erp, crm, plataforma de atendimento, apis e dados pessoais; revisão de cópias | Escopo inventariado e teste de restauração registrado | 24 |
| Dias 15–21 | Plano de incidente; revisão conjunta de prioridades; matriz valor/esforço | Alçadas, contatos e decisões registradas | 20 |
| Dias 22–30 | Indicadores necessários; retrospectiva; reaplicação do questionário | Origem dos dados, lacunas e próximas ações | 16 |

O ponto de partida local para WIP é três itens por executor, contando execução, teste e bloqueio. Emergências têm alçada, efeito e exceção registrados. Um quadro em papel, Trello, Planner ou Jira pode servir conforme o contexto. A adoção de ferramenta não demonstra aplicação da regra.

Depois do dia 30, selecionar melhorias conforme evidência e capacidade. Reduzir digitação entre CRM e ERP, catalogar integrações e revisar decisões a partir de indicadores. Aprovar e verificar mudanças que envolvam dados pessoais. O acervo chamava esse percurso de Fases Um a Três; os nomes não impõem calendário anual, sprint semanal ou MVP obrigatório de duas semanas. O restante das 540 h de implantação inclui melhorias posteriores, e não é todo trabalho realizado no primeiro mês.

IA pode auxiliar triagem, rascunhos de PRD, consulta de fontes e organização de indicadores, com revisão responsável. ADK e MCP são opções técnicas, inclusive neste porte. Caso adotados, acrescentar seus custos e restrições de dados; nenhum resultado abaixo depende da obrigatoriedade de IA. Um teste de restauração verifica seu escopo e duração; o prazo histórico de 30 minutos não é garantia universal.

## 4. Hipóteses de melhoria

Hipóteses históricas para 90 dias: TMpR de 4,5 h, disponibilidade de 99,3% e autoatendimento de 45% das dúvidas recorrentes. Esses números não têm observações ou estudo que confirmem sua realização; não entram na conta anual. A linha posterior abaixo conserva as hipóteses usadas pelo exercício original para um estado estabilizado.

| Indicador | Partida hipotética | Estado posterior hipotético | Unidade |
| --- | ---: | ---: | --- |
| Disponibilidade | 98,50 | 99,70 | % da janela de serviço |
| Indisponibilidade | 67,50 | 13,50 | h/ano |
| Resolução média | 6,50 | 3,50 | h por chamado |
| Satisfação | 3,60 | 4,60 | média de 1 a 5 |
| Tempo TI não aproveitado | 180,00 | 60,00 | h/mês |
| Retrabalho do usuário | 260,00 | 70,00 | h/mês |
| DAN financeiro | 0,17 | 0,11 | custo de refatoração/orçamento anual |

Canal oficial e quadro podem ajudar a localizar pedidos e bloqueios. Orientações podem resolver dúvidas recorrentes. Melhorias nas integrações podem reduzir digitação duplicada. Cópias verificadas podem apoiar recuperação. A contribuição de cada prática depende de aplicação, falhas, escopo e contexto; as diferenças da tabela não foram causalmente demonstradas.

O questionário histórico atribuía 4 respostas positivas à partida e sugeria 10 no horizonte anual. Nenhuma transição está assegurada. As perguntas foram revistas nesta edição: reaplicar [IM-TI com evidências](../framework/adocao/maturidade.md), sem transferir os scores antigos. Nível máximo permanece possível sem IA.

## 5. Comparação operacional e verificação

| Área | Situação descrita no cenário | Prática proposta | O que verificar |
| --- | --- | --- | --- |
| Demanda | Pedidos dispersos ou fora da regra | Canal oficial com rota para urgência | Amostra de pedidos registrados e encaminhados |
| Execução | Priorização e interrupções sem critério comum | Quadro, WIP por executor e aceite | Idade, bloqueios, testes e exceções |
| Continuidade | Cópias sem evidência suficiente | Escopo, retenção e restauração | Dependências, RTO/RPO e limitações do teste |
| Melhorias | Rotinas manuais e integrações frágeis | PRD curto e decisão valor/esforço | Teste com dono do processo e efeito observado |
| Relação com negócio | Expectativa sem decisão rastreável | Revisão conjunta de prioridades | Responsável, alçada, recurso e decisão |

```mermaid
flowchart LR
    A[Registrar a situação] --> B[Escolher prática e responsável]
    B --> C[Executar e verificar]
    C --> D[Medir na mesma janela]
    D --> E[Rever a hipótese e a decisão]
```

O diagrama representa o método de avaliação. Não expressa um antes/depois já observado.

## 6. Memória financeira e sensibilidade

| Componente | Conta | Valor |
| --- | --- | ---: |
| Capacidade TI potencial | (180 − 60) h/mês × R$ 70,00/h | R$ 8.400,00/mês |
| Capacidade do usuário potencial | (260 − 70) h/mês × R$ 25/h | R$ 4.750,00/mês |
| Capacidade por menor indisponibilidade | (67,50 − 13,50) h/ano × 80 pessoas × R$ 25/h ÷ 12 | R$ 9.000,00/mês |
| Benefício bruto condicional | Soma sem arredondamento intermediário | R$ 22.150,00/mês |
| Investimento inicial | 540 h × R$ 70,00/h + R$ 10.000,00 de treinamento/implantação | R$ 47.800,00 |
| Operação anual incremental | Cópias R$ 10.000,00 + plataformas R$ 8.000,00 | R$ 18.000,00/ano |

As plataformas dos perfis C e D são classificadas como despesa anual recorrente neste exercício; o texto antigo não informava o período. Confirmar contratos antes de aplicar. O treinamento/licenças iniciais do perfil A foi mantido como implantação. Horas internas são custo de uso de capacidade, mesmo que a folha já seja paga. Para uma análise de caixa, separar desembolso incremental e custo de oportunidade.

Horizonte ilustrativo: 12 meses em estado estabilizado. `ROI líquido = ((benefício mensal − custo mensal) × 12 − investimento) / investimento × 100`. `Payback simples = investimento / (benefício mensal − custo mensal)`, se o denominador for positivo. Não é uma previsão de payback desde o início: benefícios graduais e trabalhos posteriores requerem fluxo mensal datado.

| Parcela do benefício realizada | Benefício bruto mensal | Benefício líquido mensal | ROI líquido em 12 meses | Payback simples |
| --- | ---: | ---: | ---: | ---: |
| 0% | R$ 0,00 | R$ -1.500,00 | -137,66% | Sem payback finito |
| 60% | R$ 13.290,00 | R$ 11.790,00 | 195,98% | 4,05 meses |
| 100% | R$ 22.150,00 | R$ 20.650,00 | 418,41% | 2,31 meses |

As parcelas de 0%, 60% e 100% são testes de sensibilidade; não representam probabilidade, piso conservador ou resultado esperado. Nenhuma redução de despesa foi comprovada. A conta exclui inflação, impostos, valor do dinheiro no tempo, receita perdida e risco de segurança. Conferir sobreposição de horas e a realização do benefício antes de decidir.

O total histórico de custos do primeiro ano, que misturava investimento e recorrência, era R$ 65.800,00. Sua preservação explica o número anterior; o cálculo antigo `benefício anual / total × 100` era uma razão bruta, sem subtrair investimento e operação.

## 7. Risco, controles e limites

O cenário combina recuperação operacional, comunicação de incidente e possível exposição de dados pessoais; sanção e reputação não são perdas certas. O exemplo histórico usava probabilidade anual de 20% antes e 4% depois, com perda por incidente de R$ 250.000,00. A conta `(p antes − p depois) × perda` resulta em R$ 40.000,00/ano. **As probabilidades e a perda são arbitrárias**: o valor não demonstra risco evitado, média setorial ou proteção obtida. Ele foi preservado somente como exercício de valor esperado e não é somado ao benefício financeiro.

Abaixo estão dez áreas de atenção do acervo, com evidência a coletar. Não se trata da lista completa do CIS IG1 nem de controles já implantados. Estado de todas as linhas: **não verificado neste cenário**. [Segurança e continuidade](../framework/nucleo/seguranca-continuidade.md) relaciona a seleção local ao NIST CSF 2.0; [fontes e limites](../framework/referencias/fontes.md) registra também CIS e o acesso às demais referências.

Contexto específico: ERP, CRM, Microsoft 365 e APIs; acesso por necessidade; proteção gerenciada, segregação de ambientes e catálogo de dados pessoais.

| Nº | Área | Evidência a coletar | Exposição a examinar |
| --- | --- | --- | --- |
| 1 | Inventário de equipamentos | Lista com responsável, serviço e lacunas de cobertura | Ativos desconhecidos ou sem manutenção |
| 2 | Inventário de software e dados | Versões, licenças, integrações e fluxos de dados | Dependências desconhecidas e uso sem rastreabilidade |
| 3 | Vulnerabilidades | Prioridade de correção, teste e exceções documentadas | Exploração de falhas conhecidas |
| 4 | Configuração segura | Revisão de serviços expostos e teste da configuração | Exposição desnecessária e propagação |
| 5 | Identidade e MFA | Cobertura de contas críticas e exceções | Comprometimento de credenciais |
| 6 | Privilégio mínimo | Aprovação, revisão e remoção de acesso excedente | Uso indevido de privilégios |
| 7 | Proteção contra malware | Cobertura, atualização, alertas e encaminhamento | Código malicioso e ransomware |
| 8 | Cópias e recuperação | Retenção, separação e restauração do escopo escolhido | Perda de dados e recuperação inviável |
| 9 | Rede e perímetro | Regras revisadas e teste de segmentação | Acesso indevido e movimento lateral |
| 10 | Conscientização e resposta | Orientação, exercício, contatos e alçadas | Fraude e resposta descoordenada |

### Dados pessoais e resposta

O plano deve identificar o controlador, quem avalia o incidente e quem comunica titulares e autoridade. O catálogo de dados, o uso de MCP e a presença de IA não comprovam conformidade com a LGPD. Não pressupor que o especialista técnico de segurança acumule automaticamente o papel de encarregado.

O prazo geral de comunicação pelo controlador à ANPD e aos titulares é de **três dias úteis**, para incidentes que possam acarretar risco ou dano relevante aos titulares, ressalvadas regras específicas. O antigo prazo de “72 horas” foi retirado. Conferir marco inicial, contagem, conteúdo e regime aplicável antes de usar um playbook operacional. ANPD, orientação CIS, pergunta 4, que reproduz os arts. 6 e 9 da Resolução CD/ANPD nº 15/2024; consulta em 04.10.2026: [Orientação oficial](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis). O acesso ao regulamento integral falhou; não foram verificadas exceções para pequeno porte.

A multa simples prevista no art. 52, II, da LGPD pode alcançar 2% do faturamento da pessoa jurídica de direito privado, grupo ou conglomerado no Brasil no último exercício, excluídos tributos, limitada a R$ 50 milhões por infração. Sua aplicação depende de processo administrativo e critérios legais. R$ 900 mil seria apenas a multiplicação de 2% pelo faturamento hipotético de R$ 45 milhões; não é multa estimada nem perda provável deste cenário. [Lei nº 13.709/2018, texto atualizado, arts. 48 e 52](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html), consulta em 04.10.2026.

Origem: perfil autoral histórico preservado em `.context/originais/gear-2026-10-04/Simulacao/`. Adaptação e fórmulas são locais; não são equações atribuídas a ISO, COBIT, ITIL, NIST ou CIS. Para usar: substituir hipóteses, registrar origem e data, conferir com finanças e dono do processo e decidir dentro da alçada.

Voltar: [Índice dos cenários](README.md). Consultar: [Calculadora](Calculadora_ROI.md).
