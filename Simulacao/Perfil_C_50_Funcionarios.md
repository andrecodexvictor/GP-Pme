# Perfil C — Primeiro gestor de TI

Cenário didático do GEAR para 50 colaboradores. Os valores de partida e de melhoria são **premissas fictícias do acervo**, preservadas para comparar hipóteses. Não descrevem uma implantação realizada. Cálculos: [Calculadora de ROI](Calculadora_ROI.md); convenções: [indicadores financeiros](../framework/indicadores/financeiros.md).

## 1. Retrato e escopo

| Item | Premissa |
| --- | --- |
| Setor | Indústria leve com distribuição própria |
| Pessoas | 50 |
| Faturamento anual | R$ 20.000.000,00 |
| Equipe | Um analista pleno, um técnico júnior e um gestor (salário de referência de R$ 10.000) que também atende demandas. |
| Orçamento anual de TI | R$ 500.000,00 |
| Ambiente | ERP industrial, MES, Microsoft 365, servidor de arquivos, coletores, aproximadamente 50 estações e VPN para duas filiais. |

Os valores de faturamento e orçamento situam o exercício. Não constituem benchmark de porte, pessoal ou gasto. A alocação de salários e infraestrutura do texto antigo não foi verificada como orçamento de uma empresa real.

## 2. Situação de partida

O técnico registra pedidos em caderno, o analista recebe mensagens e a produção liga diretamente para a equipe. Falhas no MES interrompem apontamentos; expedição alimenta o ERP por planilhas. O gestor não dispõe de uma linha de base confiável.

A linha de base adota custo TI de R$ 62,00/h, custo de usuário de R$ 25/h e janela anual de 3.600 h. Pessoas afetadas pela indisponibilidade: 30. Volume hipotético: 1.320 incidentes/ano, equivalente a 110,00 por mês e 2,20 por pessoa/mês.

O custo-hora de R$ 62 é um parâmetro didático preservado. A expressão antiga `(53 + 53 + 88)/3` resulta em R$ 64,67, não R$ 62. Para uma média ponderada real, registrar as horas e os custos de cada profissional.

O DAN inicial usa 1.500 h de refatoração × R$ 62,00/h ÷ R$ 500.000,00: 0,186. As antigas cores e faixas não são limites financeiros validados.

A soma dos três componentes de tempo da situação de partida é R$ 15.450,00/mês. Esse valor representa capacidade avaliada monetariamente, sem receita perdida, impostos ou dupla contagem entre categorias. Se as horas de indisponibilidade já estiverem nas horas de retrabalho, retirar a sobreposição.

## 3. Plano inicial de 30 dias

TI organiza a execução; o dono do processo negocia prioridades e verifica entregas. [Primeiros 30 dias](../framework/adocao/primeiros-30-dias.md) define o percurso. Esforço hipotético inicial: 52 h somadas, distribuídas abaixo; ajustar à capacidade real.

| Janela | Trabalho | Evidência de conclusão | Horas |
| --- | --- | --- | ---: |
| Dias 1–7 | Diagnóstico; canal oficial; quadro e responsáveis | Pedidos migrados e política de trabalho iniciado acordada | 18 |
| Dias 8–14 | Orientações para senha, vpn, coletor, mes e impressora; inventário de erp, mes, servidor de arquivos e coletores; revisão de cópias | Escopo inventariado e teste de restauração registrado | 14 |
| Dias 15–21 | Plano de incidente; revisão conjunta de prioridades; matriz valor/esforço | Alçadas, contatos e decisões registradas | 12 |
| Dias 22–30 | Indicadores necessários; retrospectiva; reaplicação do questionário | Origem dos dados, lacunas e próximas ações | 8 |

O ponto de partida local para WIP é três itens por executor, contando execução, teste e bloqueio. Emergências têm alçada, efeito e exceção registrados. Um quadro em papel, Trello, Planner ou Jira pode servir conforme o contexto. A adoção de ferramenta não demonstra aplicação da regra.

Depois do dia 30, selecionar melhorias conforme evidência e capacidade. Automatizar a planilha de expedição e estudar as dependências ERP–MES; o gestor coordena prioridades e os técnicos verificam execução. O acervo chamava esse percurso de Fases Um a Três; os nomes não impõem calendário anual, sprint semanal ou MVP obrigatório de duas semanas. O restante das 140 h de implantação inclui melhorias posteriores, e não é todo trabalho realizado no primeiro mês.

IA pode auxiliar triagem, rascunhos de PRD, consulta de fontes e organização de indicadores, com revisão responsável. ADK e MCP são opções técnicas, inclusive neste porte. Caso adotados, acrescentar seus custos e restrições de dados; nenhum resultado abaixo depende da obrigatoriedade de IA. Um teste de restauração verifica seu escopo e duração; o prazo histórico de 30 minutos não é garantia universal.

## 4. Hipóteses de melhoria

Hipóteses históricas para 90 dias: TMpR de 5 h, disponibilidade de 99,0% e autoatendimento de 40% das dúvidas recorrentes. Esses números não têm observações ou estudo que confirmem sua realização; não entram na conta anual. A linha posterior abaixo conserva as hipóteses usadas pelo exercício original para um estado estabilizado.

| Indicador | Partida hipotética | Estado posterior hipotético | Unidade |
| --- | ---: | ---: | --- |
| Disponibilidade | 97,50 | 99,50 | % da janela de serviço |
| Indisponibilidade | 90,00 | 18,00 | h/ano |
| Resolução média | 8,00 | 4,00 | h por chamado |
| Satisfação | 3,30 | 4,50 | média de 1 a 5 |
| Tempo TI não aproveitado | 100,00 | 39,00 | h/mês |
| Retrabalho do usuário | 145,00 | 48,00 | h/mês |
| DAN financeiro | 0,19 | 0,12 | custo de refatoração/orçamento anual |

Canal oficial e quadro podem ajudar a localizar pedidos e bloqueios. Orientações podem resolver dúvidas recorrentes. Melhorias nas integrações podem reduzir digitação duplicada. Cópias verificadas podem apoiar recuperação. A contribuição de cada prática depende de aplicação, falhas, escopo e contexto; as diferenças da tabela não foram causalmente demonstradas.

O questionário histórico atribuía 2 respostas positivas à partida e sugeria 9 no horizonte anual. Nenhuma transição está assegurada. As perguntas foram revistas nesta edição: reaplicar [IM-TI com evidências](../framework/adocao/maturidade.md), sem transferir os scores antigos. Nível máximo permanece possível sem IA.

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
| Capacidade TI potencial | (100 − 39) h/mês × R$ 62,00/h | R$ 3.782,00/mês |
| Capacidade do usuário potencial | (145 − 48) h/mês × R$ 25/h | R$ 2.425,00/mês |
| Capacidade por menor indisponibilidade | (90,00 − 18,00) h/ano × 30 pessoas × R$ 25/h ÷ 12 | R$ 4.500,00/mês |
| Benefício bruto condicional | Soma sem arredondamento intermediário | R$ 10.707,00/mês |
| Investimento inicial | 140 h × R$ 62,00/h + R$ 6.000,00 de treinamento/implantação | R$ 14.680,00 |
| Operação anual incremental | Cópias R$ 3.600,00 + plataformas R$ 2.400,00 | R$ 6.000,00/ano |

As plataformas dos perfis C e D são classificadas como despesa anual recorrente neste exercício; o texto antigo não informava o período. Confirmar contratos antes de aplicar. O treinamento/licenças iniciais do perfil A foi mantido como implantação. Horas internas são custo de uso de capacidade, mesmo que a folha já seja paga. Para uma análise de caixa, separar desembolso incremental e custo de oportunidade.

Horizonte ilustrativo: 12 meses em estado estabilizado. `ROI líquido = ((benefício mensal − custo mensal) × 12 − investimento) / investimento × 100`. `Payback simples = investimento / (benefício mensal − custo mensal)`, se o denominador for positivo. Não é uma previsão de payback desde o início: benefícios graduais e trabalhos posteriores requerem fluxo mensal datado.

| Parcela do benefício realizada | Benefício bruto mensal | Benefício líquido mensal | ROI líquido em 12 meses | Payback simples |
| --- | ---: | ---: | ---: | ---: |
| 0% | R$ 0,00 | R$ -500,00 | -140,87% | Sem payback finito |
| 60% | R$ 6.424,20 | R$ 5.924,20 | 384,27% | 2,48 meses |
| 100% | R$ 10.707,00 | R$ 10.207,00 | 734,36% | 1,44 meses |

As parcelas de 0%, 60% e 100% são testes de sensibilidade; não representam probabilidade, piso conservador ou resultado esperado. Nenhuma redução de despesa foi comprovada. A conta exclui inflação, impostos, valor do dinheiro no tempo, receita perdida e risco de segurança. Conferir sobreposição de horas e a realização do benefício antes de decidir.

O total histórico de custos do primeiro ano, que misturava investimento e recorrência, era R$ 20.680,00. Sua preservação explica o número anterior; o cálculo antigo `benefício anual / total × 100` era uma razão bruta, sem subtrair investimento e operação.

## 7. Risco, controles e limites

Uma paralisação pode interromper apontamento de produção e expedição, com exposição a atrasos contratuais. O exemplo histórico usava probabilidade anual de 20% antes e 5% depois, com perda por incidente de R$ 120.000,00. A conta `(p antes − p depois) × perda` resulta em R$ 18.000,00/ano. **As probabilidades e a perda são arbitrárias**: o valor não demonstra risco evitado, média setorial ou proteção obtida. Ele foi preservado somente como exercício de valor esperado e não é somado ao benefício financeiro.

Abaixo estão dez áreas de atenção do acervo, com evidência a coletar. Não se trata da lista completa do CIS IG1 nem de controles já implantados. Estado de todas as linhas: **não verificado neste cenário**. [Segurança e continuidade](../framework/nucleo/seguranca-continuidade.md) relaciona a seleção local ao NIST CSF 2.0; [fontes e limites](../framework/referencias/fontes.md) registra também CIS e o acesso às demais referências.

Contexto específico: ERP, MES e Microsoft 365; proteção gerenciada das estações; segmentação entre chão de fábrica e escritório.

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
