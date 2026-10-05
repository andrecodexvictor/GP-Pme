# GEAR — calculadora de cenários financeiros

Esta ficha reúne as convenções locais dos quatro [perfis didáticos](README.md). Use dados da organização, com origem, data, responsável e janela de medição. As fórmulas não foram extraídas de ISO, COBIT, ITIL ou NIST. O [núcleo financeiro](../framework/indicadores/financeiros.md) define seus limites; o [portal](../GP-Pme%20Article/ferramentas.html) oferece cálculos locais.

## 1. Custo-hora e período

`Custo-hora = custo mensal total do profissional / horas mensais consideradas`.

O acervo usa salário × 1,55 ÷ 176 como hipótese de custo empregador. Exemplo: `6.000 × 1,55 / 176 = R$ 52,84/h`, arredondado para R$ 53/h. Não é fator legal fixo nem pesquisa salarial. O custo de usuário de R$ 25/h também é parâmetro didático.

| Perfil | Custo TI usado | Base e limite |
| --- | ---: | --- |
| A | R$ 44/h | Salário hipotético de R$ 5.000, com fator e jornada locais |
| B | R$ 53/h | Salário hipotético de R$ 6.000 |
| C | R$ 62/h | Parâmetro preservado; `(53 + 53 + 88)/3 = 64,67`, sem ponderação documentada |
| D | R$ 70/h | Salário médio hipotético de R$ 7.950; não representa pesquisa de equipe |

Para equipe com custos distintos, usar `soma(horas de cada pessoa × seu custo-hora) / soma(horas)`. Diferenciar janela anual de serviço, horas de trabalho do profissional e período de análise financeira.

## 2. Indicadores operacionais

As metas históricas de 99,5%, quatro horas e 4,5/5 são hipóteses locais, a negociar por serviço. Uma queda contínua de incidentes não é regra universal: maior registro pode aumentar o volume conhecido.

| Indicador | Fórmula | Exemplo e limite |
| --- | --- | --- |
| IDSC | `(janela − indisponibilidade) / janela × 100` | 250 h e 5 h paradas: 98%; definir serviço e fonte de monitoramento |
| TMpR | `soma do tempo entre registro e resolução / chamados concluídos` | 180 h em 30 chamados: 6 h; declarar relógio e classe de incidente |
| ISU | `soma das notas / respostas válidas` | 168 pontos em 40 respostas: 4,2/5; publicar cobertura e viés de resposta |
| Incidentes por pessoa | `incidentes no período / pessoas` | 62 incidentes, 25 pessoas: 2,48/pessoa/mês; definir incidente e população |

Regra inversa: `indisponibilidade anual = (1 − disponibilidade/100) × janela anual`. Para 99,5% em 3.500 h, são 17,5 h. Não misturar médias de vários serviços sem método de agregação.

## 3. DAN e custo de implantação

`DAN financeiro = horas estimadas de refatoração × custo-hora / orçamento anual de TI`.

Exemplo: `800 × 53 / 220.000 = 0,1927`. A conta não informa probabilidade de falha. Os limites antigos de 0,15 e 0,35 são convenções históricas sem validação financeira. A proporção de itens legados usada por software antigo é outro indicador.

COT significa **Custo de Otimização Tecnológica** no GEAR. Separar:

- **Investimento inicial:** implantação, treinamento e serviços pontuais, incluindo tempo interno quando a análise for econômica.
- **Custo recorrente incremental:** manutenção, assinaturas, infraestrutura e serviços de operação, com período explícito.
- **Custo de oportunidade e caixa:** identificar tempo realocado e desembolso efetivo; não considerar horas internas gratuitas por já constarem na folha.

Perfil B: `90 h × R$ 53 + R$ 3.000 = R$ 7.770` de investimento; R$ 1.800/ano de cópias, equivalente a R$ 150/mês. O total histórico de R$ 9.570 mistura os dois e não é o denominador do ROI líquido desta edição.

## 4. Capacidade potencial mensal

| Parcela | Fórmula |
| --- | --- |
| Retrabalho do usuário | `(horas antes − horas depois) × custo-hora usuário` |
| Tempo de TI | `(horas antes − horas depois) × custo-hora TI` |
| Menor indisponibilidade | `(h/ano antes − h/ano depois) × pessoas afetadas × custo-hora usuário / 12` |

Somar somente parcelas independentes. Horas de retrabalho que já incluem a parada não podem ser contadas novamente. O perfil B usa:

```text
TI:                 (60 − 20) × 53              = 2.120,00/mês
Retrabalho:         (70 − 25) × 25              = 1.125,00/mês
Indisponibilidade:  (87,5 − 17,5) × 13 × 25/12 = 1.895,8333…/mês
Benefício bruto potencial                     = 5.140,8333…/mês
```

Esse valor não comprova economia paga. Medir a realocação ou redução de despesa. A fórmula histórica para custo de hora parada incluía `pessoas × custo-hora + receita por hora × parcela em risco`. Os perfis adotam parcela de receita zero; uma análise real de vendas deve usar margem, período e perda demonstrada, sem duplicar capacidade e receita derivada.

## 5. ROI líquido, razão bruta e payback

Com investimento positivo `I`, benefício bruto mensal `b`, custo recorrente mensal `c` e horizonte `m`:

```text
Benefício bruto no período = b × m
Razão benefício/investimento = (b × m) / I
ROI líquido (%) = ((b − c) × m − I) / I × 100
Payback simples (meses) = I / (b − c), apenas se b > c
```

No perfil B, `I = 7.770`, `b = 5.140,8333…`, `c = 150`, `m = 12`. Benefício bruto anual: R$ 61.690. ROI líquido: `(61.690 − 1.800 − 7.770) / 7.770 × 100 = 670,79%`. Razão bruta: `61.690 / 7.770 = 7,9395`. Payback simples: `7.770 / 4.990,8333… = 1,56 meses`.

São contas condicionais em estado estabilizado, sem dados de realização. Não inferir retorno desde o primeiro mês quando implantação e benefícios são graduais. Se `b ≤ c`, não há payback simples finito. Comparar fluxos datados quando houver rampa, tributos, inflação ou custo de capital.

## 6. Sensibilidade e exercício de risco

Variar a parcela realizada do benefício, custo recorrente, esforço inicial e janela. Os perfis usam 0%, 60% e 100% do benefício para mostrar dependência da hipótese; não são faixas de confiança. As perdas de receita e segurança ficam fora do cálculo principal.

O exemplo histórico de risco usa `valor esperado = probabilidade anual × perda por incidente`. Uma diferença hipotética de 20% para 5%, com perda de R$ 80.000, resulta em R$ 12.000/ano. As probabilidades são arbitrárias e não decorrem da implantação de MFA, cópias ou outro controle. Não apresentar a diferença como risco comprovadamente evitado. Cópias ajudam a recuperação; não garantem restauração em 30 minutos nem impedem exfiltração.

## 7. Maturidade e ficha de aplicação

O IM-TI soma dez respostas com evidências. Faixas locais: 0–2 pontos, nível 0; 3–5, nível 1; 6–8, nível 2; 9, nível 3; 10, nível 4. As perguntas foram revistas; scores históricos exigem reaplicação. IA não é requisito em nenhum nível. Use o [questionário canônico](../framework/adocao/maturidade.md).

| Registro | Preencher |
| --- | --- |
| Serviço, problema e dono do processo | ___ |
| Origem, data e janela dos dados | ___ |
| Custo-hora TI/usuário e método | ___ |
| Horas de TI e retrabalho antes/depois | ___ |
| Indisponibilidade antes/depois, janela e pessoas | ___ |
| Sobreposição de horas retirada | ___ |
| Investimento e custo recorrente separados | ___ |
| Benefício realizado, potencial ou hipótese | ___ |
| Fluxo mensal, horizonte e sensibilidade | ___ |
| ROI líquido, razão bruta e payback | ___ |
| Limites, verificador e decisão | ___ |

TI estima; finanças confere unidades e custos; o dono do processo verifica efeito; direção decide conforme alçada. As premissas e a memória de cálculo acompanham a decisão. [Voltar aos perfis](README.md).

