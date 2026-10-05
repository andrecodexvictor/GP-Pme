# Perfil A — TI de uma pessoa

Cenário didático do GEAR para 10 colaboradores. Os valores de partida e de melhoria são **premissas fictícias do acervo**, preservadas para comparar hipóteses. Não descrevem uma implantação realizada. Cálculos: [Calculadora de ROI](Calculadora_ROI.md); convenções: [indicadores financeiros](../framework/indicadores/financeiros.md).

## 1. Retrato e escopo

| Item | Premissa |
| --- | --- |
| Setor | Contabilidade e serviços profissionais |
| Pessoas | 10 |
| Faturamento anual | R$ 1.800.000,00 |
| Equipe | Um técnico de TI que acumula suporte, infraestrutura e cópias de segurança; salário de referência de R$ 5.000. |
| Orçamento anual de TI | R$ 108.000,00 |
| Ambiente | Google Workspace, ERP contábil local (exemplos históricos: Domínio ou Alterdata), Wi-Fi, 12 notebooks e cópia manual em HD externo. |

Os valores de faturamento e orçamento situam o exercício. Não constituem benchmark de porte, pessoal ou gasto. A alocação de salários e infraestrutura do texto antigo não foi verificada como orçamento de uma empresa real.

## 2. Situação de partida

Pedidos chegam pelo telefone pessoal, corredor e mensagens. Um sócio não consegue acompanhar o pedido; uma interrupção de 40 minutos no ERP impede a emissão de guias. A equipe não possui registro de teste de restauração.

A linha de base adota custo TI de R$ 44,00/h, custo de usuário de R$ 25/h e janela anual de 2.500 h. Pessoas afetadas pela indisponibilidade: 8. Volume hipotético: 360 incidentes/ano, equivalente a 30,00 por mês e 3,00 por pessoa/mês.

Os custos-hora são valores arredondados do exemplo histórico, sem pesquisa salarial. Encargos de 1,55 e jornada de 176 h/mês são hipóteses locais, a substituir pelo custo real.

O DAN inicial usa 480 h de refatoração × R$ 44,00/h ÷ R$ 108.000,00: 0,196. As antigas cores e faixas não são limites financeiros validados.

A soma dos três componentes de tempo da situação de partida é R$ 3.551,67/mês. Esse valor representa capacidade avaliada monetariamente, sem receita perdida, impostos ou dupla contagem entre categorias. Se as horas de indisponibilidade já estiverem nas horas de retrabalho, retirar a sobreposição.

## 3. Plano inicial de 30 dias

TI organiza a execução; o dono do processo negocia prioridades e verifica entregas. [Primeiros 30 dias](../framework/adocao/primeiros-30-dias.md) define o percurso. Esforço hipotético inicial: 28 h somadas, distribuídas abaixo; ajustar à capacidade real.

| Janela | Trabalho | Evidência de conclusão | Horas |
| --- | --- | --- | ---: |
| Dias 1–7 | Diagnóstico; canal oficial; quadro e responsáveis | Pedidos migrados e política de trabalho iniciado acordada | 10 |
| Dias 8–14 | Orientações para senha, wi-fi, impressora, vpn e e-mail; inventário de erp, dados contábeis e notebooks dos sócios; revisão de cópias | Escopo inventariado e teste de restauração registrado | 8 |
| Dias 15–21 | Plano de incidente; revisão conjunta de prioridades; matriz valor/esforço | Alçadas, contatos e decisões registradas | 5 |
| Dias 22–30 | Indicadores necessários; retrospectiva; reaplicação do questionário | Origem dos dados, lacunas e próximas ações | 5 |

O ponto de partida local para WIP é três itens por executor, contando execução, teste e bloqueio. Emergências têm alçada, efeito e exceção registrados. Um quadro em papel, Trello, Planner ou Jira pode servir conforme o contexto. A adoção de ferramenta não demonstra aplicação da regra.

Depois do dia 30, selecionar melhorias conforme evidência e capacidade. Automatizar o relatório mensal de honorários e examinar a substituição ou correção do servidor instável. O acervo chamava esse percurso de Fases Um a Três; os nomes não impõem calendário anual, sprint semanal ou MVP obrigatório de duas semanas. O restante das 70 h de implantação inclui melhorias posteriores, e não é todo trabalho realizado no primeiro mês.

IA pode auxiliar triagem, rascunhos de PRD, consulta de fontes e organização de indicadores, com revisão responsável. ADK e MCP são opções técnicas, inclusive neste porte. Caso adotados, acrescentar seus custos e restrições de dados; nenhum resultado abaixo depende da obrigatoriedade de IA. Um teste de restauração verifica seu escopo e duração; o prazo histórico de 30 minutos não é garantia universal.

## 4. Hipóteses de melhoria

Hipóteses históricas para 90 dias: TMpR de 5,5 h, disponibilidade de 99,0% e autoatendimento de 40% das dúvidas recorrentes. Esses números não têm observações ou estudo que confirmem sua realização; não entram na conta anual. A linha posterior abaixo conserva as hipóteses usadas pelo exercício original para um estado estabilizado.

| Indicador | Partida hipotética | Estado posterior hipotético | Unidade |
| --- | ---: | ---: | --- |
| Disponibilidade | 97,50 | 99,50 | % da janela de serviço |
| Indisponibilidade | 62,50 | 12,50 | h/ano |
| Resolução média | 9,00 | 4,00 | h por chamado |
| Satisfação | 3,40 | 4,50 | média de 1 a 5 |
| Tempo TI não aproveitado | 40,00 | 15,00 | h/mês |
| Retrabalho do usuário | 30,00 | 12,00 | h/mês |
| DAN financeiro | 0,20 | 0,10 | custo de refatoração/orçamento anual |

Canal oficial e quadro podem ajudar a localizar pedidos e bloqueios. Orientações podem resolver dúvidas recorrentes. Melhorias nas integrações podem reduzir digitação duplicada. Cópias verificadas podem apoiar recuperação. A contribuição de cada prática depende de aplicação, falhas, escopo e contexto; as diferenças da tabela não foram causalmente demonstradas.

O questionário histórico atribuía 1 respostas positivas à partida e sugeria 6 no horizonte anual. Nenhuma transição está assegurada. As perguntas foram revistas nesta edição: reaplicar [IM-TI com evidências](../framework/adocao/maturidade.md), sem transferir os scores antigos. Nível máximo permanece possível sem IA.

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
| Capacidade TI potencial | (40 − 15) h/mês × R$ 44,00/h | R$ 1.100,00/mês |
| Capacidade do usuário potencial | (30 − 12) h/mês × R$ 25/h | R$ 450,00/mês |
| Capacidade por menor indisponibilidade | (62,50 − 12,50) h/ano × 8 pessoas × R$ 25/h ÷ 12 | R$ 833,33/mês |
| Benefício bruto condicional | Soma sem arredondamento intermediário | R$ 2.383,33/mês |
| Investimento inicial | 70 h × R$ 44,00/h + R$ 1.000,00 de treinamento/implantação | R$ 4.080,00 |
| Operação anual incremental | Cópias R$ 1.200,00 + plataformas R$ 0,00 | R$ 1.200,00/ano |

As plataformas dos perfis C e D são classificadas como despesa anual recorrente neste exercício; o texto antigo não informava o período. Confirmar contratos antes de aplicar. O treinamento/licenças iniciais do perfil A foi mantido como implantação. Horas internas são custo de uso de capacidade, mesmo que a folha já seja paga. Para uma análise de caixa, separar desembolso incremental e custo de oportunidade.

Horizonte ilustrativo: 12 meses em estado estabilizado. `ROI líquido = ((benefício mensal − custo mensal) × 12 − investimento) / investimento × 100`. `Payback simples = investimento / (benefício mensal − custo mensal)`, se o denominador for positivo. Não é uma previsão de payback desde o início: benefícios graduais e trabalhos posteriores requerem fluxo mensal datado.

| Parcela do benefício realizada | Benefício bruto mensal | Benefício líquido mensal | ROI líquido em 12 meses | Payback simples |
| --- | ---: | ---: | ---: | ---: |
| 0% | R$ 0,00 | R$ -100,00 | -129,41% | Sem payback finito |
| 60% | R$ 1.430,00 | R$ 1.330,00 | 291,18% | 3,07 meses |
| 100% | R$ 2.383,33 | R$ 2.283,33 | 571,57% | 1,79 meses |

As parcelas de 0%, 60% e 100% são testes de sensibilidade; não representam probabilidade, piso conservador ou resultado esperado. Nenhuma redução de despesa foi comprovada. A conta exclui inflação, impostos, valor do dinheiro no tempo, receita perdida e risco de segurança. Conferir sobreposição de horas e a realização do benefício antes de decidir.

O total histórico de custos do primeiro ano, que misturava investimento e recorrência, era R$ 5.280,00. Sua preservação explica o número anterior; o cálculo antigo `benefício anual / total × 100` era uma razão bruta, sem subtrair investimento e operação.

## 7. Risco, controles e limites

Uma paralisação pode afetar obrigações fiscais e contratos de clientes. O exemplo histórico usava probabilidade anual de 18% antes e 5% depois, com perda por incidente de R$ 40.000,00. A conta `(p antes − p depois) × perda` resulta em R$ 5.200,00/ano. **As probabilidades e a perda são arbitrárias**: o valor não demonstra risco evitado, média setorial ou proteção obtida. Ele foi preservado somente como exercício de valor esperado e não é somado ao benefício financeiro.

Abaixo estão dez áreas de atenção do acervo, com evidência a coletar. Não se trata da lista completa do CIS IG1 nem de controles já implantados. Estado de todas as linhas: **não verificado neste cenário**. [Segurança e continuidade](../framework/nucleo/seguranca-continuidade.md) relaciona a seleção local ao NIST CSF 2.0; [fontes e limites](../framework/referencias/fontes.md) registra também CIS e o acesso às demais referências.

Contexto específico: ERP e Workspace; MFA nas contas críticas e bancárias; proteção das estações e firewall do sistema e roteador.

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

Origem: perfil autoral histórico preservado em `.context/originais/gear-2026-10-04/Simulacao/`. Adaptação e fórmulas são locais; não são equações atribuídas a ISO, COBIT, ITIL, NIST ou CIS. Para usar: substituir hipóteses, registrar origem e data, conferir com finanças e dono do processo e decidir dentro da alçada.

Voltar: [Índice dos cenários](README.md). Consultar: [Calculadora](Calculadora_ROI.md).
