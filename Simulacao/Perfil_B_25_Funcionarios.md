# Perfil B — TI com analista e estagiário

Cenário didático do GEAR para 25 colaboradores. Os valores de partida e de melhoria são **premissas fictícias do acervo**, preservadas para comparar hipóteses. Não descrevem uma implantação realizada. Cálculos: [Calculadora de ROI](Calculadora_ROI.md); convenções: [indicadores financeiros](../framework/indicadores/financeiros.md).

## 1. Retrato e escopo

| Item | Premissa |
| --- | --- |
| Setor | Comércio e distribuição regional com comércio eletrônico |
| Pessoas | 25 |
| Faturamento anual | R$ 8.000.000,00 |
| Equipe | Um analista pleno (salário de referência de R$ 6.000) e um estagiário em meio período. |
| Orçamento anual de TI | R$ 220.000,00 |
| Ambiente | ERP híbrido, comércio eletrônico integrado ao checkout, Microsoft 365, servidor de arquivos e 25 estações. |

Os valores de faturamento e orçamento situam o exercício. Não constituem benchmark de porte, pessoal ou gasto. A alocação de salários e infraestrutura do texto antigo não foi verificada como orçamento de uma empresa real.

## 2. Situação de partida

Chamados do checkout chegam por três canais. O ERP possui cerca de 40 integrações e rotinas manuais, sem análise de custo. Uma queda do servidor interrompe o faturamento de 13 pessoas. As cópias ainda não têm teste registrado.

A linha de base adota custo TI de R$ 53,00/h, custo de usuário de R$ 25/h e janela anual de 3.500 h. Pessoas afetadas pela indisponibilidade: 13. Volume hipotético: 744 incidentes/ano, equivalente a 62,00 por mês e 2,48 por pessoa/mês.

Correção desta edição: 99,5% de disponibilidade em 3.500 h corresponde a 17,5 h de indisponibilidade, não 15,5 h. O benefício foi recalculado sem arredondar parcelas intermediárias.

O DAN inicial usa 800 h de refatoração × R$ 53,00/h ÷ R$ 220.000,00: 0,193. As antigas cores e faixas não são limites financeiros validados.

A soma dos três componentes de tempo da situação de partida é R$ 7.299,79/mês. Esse valor representa capacidade avaliada monetariamente, sem receita perdida, impostos ou dupla contagem entre categorias. Se as horas de indisponibilidade já estiverem nas horas de retrabalho, retirar a sobreposição.

## 3. Plano inicial de 30 dias

TI organiza a execução; o dono do processo negocia prioridades e verifica entregas. [Primeiros 30 dias](../framework/adocao/primeiros-30-dias.md) define o percurso. Esforço hipotético inicial: 40 h somadas, distribuídas abaixo; ajustar à capacidade real.

| Janela | Trabalho | Evidência de conclusão | Horas |
| --- | --- | --- | ---: |
| Dias 1–7 | Diagnóstico; canal oficial; quadro e responsáveis | Pedidos migrados e política de trabalho iniciado acordada | 14 |
| Dias 8–14 | Orientações para senha, vpn, checkout, nota fiscal e impressora; inventário de erp, servidor de arquivos e comércio eletrônico; revisão de cópias | Escopo inventariado e teste de restauração registrado | 12 |
| Dias 15–21 | Plano de incidente; revisão conjunta de prioridades; matriz valor/esforço | Alçadas, contatos e decisões registradas | 7 |
| Dias 22–30 | Indicadores necessários; retrospectiva; reaplicação do questionário | Origem dos dados, lacunas e próximas ações | 7 |

O ponto de partida local para WIP é três itens por executor, contando execução, teste e bloqueio. Emergências têm alçada, efeito e exceção registrados. Um quadro em papel, Trello, Planner ou Jira pode servir conforme o contexto. A adoção de ferramenta não demonstra aplicação da regra.

Depois do dia 30, selecionar melhorias conforme evidência e capacidade. Automatizar as planilhas de entrada do ERP com PRD e teste de aceite; investigar cada integração antes de removê-la. O acervo chamava esse percurso de Fases Um a Três; os nomes não impõem calendário anual, sprint semanal ou MVP obrigatório de duas semanas. O restante das 90 h de implantação inclui melhorias posteriores, e não é todo trabalho realizado no primeiro mês.

IA pode auxiliar triagem, rascunhos de PRD, consulta de fontes e organização de indicadores, com revisão responsável. ADK e MCP são opções técnicas, inclusive neste porte. Caso adotados, acrescentar seus custos e restrições de dados; nenhum resultado abaixo depende da obrigatoriedade de IA. Um teste de restauração verifica seu escopo e duração; o prazo histórico de 30 minutos não é garantia universal.

## 4. Hipóteses de melhoria

Hipóteses históricas para 90 dias: TMpR de 5 h, disponibilidade de 99,0% e autoatendimento de 40% das dúvidas recorrentes. Esses números não têm observações ou estudo que confirmem sua realização; não entram na conta anual. A linha posterior abaixo conserva as hipóteses usadas pelo exercício original para um estado estabilizado.

| Indicador | Partida hipotética | Estado posterior hipotético | Unidade |
| --- | ---: | ---: | --- |
| Disponibilidade | 97,50 | 99,50 | % da janela de serviço |
| Indisponibilidade | 87,50 | 17,50 | h/ano |
| Resolução média | 8,00 | 4,00 | h por chamado |
| Satisfação | 3,30 | 4,50 | média de 1 a 5 |
| Tempo TI não aproveitado | 60,00 | 20,00 | h/mês |
| Retrabalho do usuário | 70,00 | 25,00 | h/mês |
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
| Capacidade TI potencial | (60 − 20) h/mês × R$ 53,00/h | R$ 2.120,00/mês |
| Capacidade do usuário potencial | (70 − 25) h/mês × R$ 25/h | R$ 1.125,00/mês |
| Capacidade por menor indisponibilidade | (87,50 − 17,50) h/ano × 13 pessoas × R$ 25/h ÷ 12 | R$ 1.895,83/mês |
| Benefício bruto condicional | Soma sem arredondamento intermediário | R$ 5.140,83/mês |
| Investimento inicial | 90 h × R$ 53,00/h + R$ 3.000,00 de treinamento/implantação | R$ 7.770,00 |
| Operação anual incremental | Cópias R$ 1.800,00 + plataformas R$ 0,00 | R$ 1.800,00/ano |

As plataformas dos perfis C e D são classificadas como despesa anual recorrente neste exercício; o texto antigo não informava o período. Confirmar contratos antes de aplicar. O treinamento/licenças iniciais do perfil A foi mantido como implantação. Horas internas são custo de uso de capacidade, mesmo que a folha já seja paga. Para uma análise de caixa, separar desembolso incremental e custo de oportunidade.

Horizonte ilustrativo: 12 meses em estado estabilizado. `ROI líquido = ((benefício mensal − custo mensal) × 12 − investimento) / investimento × 100`. `Payback simples = investimento / (benefício mensal − custo mensal)`, se o denominador for positivo. Não é uma previsão de payback desde o início: benefícios graduais e trabalhos posteriores requerem fluxo mensal datado.

| Parcela do benefício realizada | Benefício bruto mensal | Benefício líquido mensal | ROI líquido em 12 meses | Payback simples |
| --- | ---: | ---: | ---: | ---: |
| 0% | R$ 0,00 | R$ -150,00 | -123,17% | Sem payback finito |
| 60% | R$ 3.084,50 | R$ 2.934,50 | 353,20% | 2,65 meses |
| 100% | R$ 5.140,83 | R$ 4.990,83 | 670,79% | 1,56 meses |

As parcelas de 0%, 60% e 100% são testes de sensibilidade; não representam probabilidade, piso conservador ou resultado esperado. Nenhuma redução de despesa foi comprovada. A conta exclui inflação, impostos, valor do dinheiro no tempo, receita perdida e risco de segurança. Conferir sobreposição de horas e a realização do benefício antes de decidir.

O total histórico de custos do primeiro ano, que misturava investimento e recorrência, era R$ 9.570,00. Sua preservação explica o número anterior; o cálculo antigo `benefício anual / total × 100` era uma razão bruta, sem subtrair investimento e operação.

## 7. Risco, controles e limites

Uma paralisação afeta faturamento, estoque e pedidos do comércio eletrônico. O exemplo histórico usava probabilidade anual de 20% antes e 5% depois, com perda por incidente de R$ 80.000,00. A conta `(p antes − p depois) × perda` resulta em R$ 12.000,00/ano. **As probabilidades e a perda são arbitrárias**: o valor não demonstra risco evitado, média setorial ou proteção obtida. Ele foi preservado somente como exercício de valor esperado e não é somado ao benefício financeiro.

Abaixo estão dez áreas de atenção do acervo, com evidência a coletar. Não se trata da lista completa do CIS IG1 nem de controles já implantados. Estado de todas as linhas: **não verificado neste cenário**. [Segurança e continuidade](../framework/nucleo/seguranca-continuidade.md) relaciona a seleção local ao NIST CSF 2.0; [fontes e limites](../framework/referencias/fontes.md) registra também CIS e o acesso às demais referências.

Contexto específico: ERP, Microsoft 365 e plataforma de vendas; MFA no financeiro e contas administrativas; atualização do ERP e segmentação básica.

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
