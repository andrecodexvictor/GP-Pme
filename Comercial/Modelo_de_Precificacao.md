# GP-PME — Modelo de Precificação

> Fontes: `Comercial/Proposta_de_Valor.md`, `Comercial/One_Pager_Vendas.md`, `Simulacao/Calculadora_ROI.md`.
> **Nota de metodologia**: os valores de licença abaixo são âncoras de referência calculadas sobre o custo de risco evitado e o COT de implantação da Calculadora de ROI (premissas conservadoras). Ajuste por porte real do cliente usando `Simulacao/Perfil_A..D.md` quando disponíveis; até lá, refaça a conta com os números do próprio prospect antes de fechar.

---

## A âncora: custo de 1 incidente evitado

A Calculadora de ROI estima o custo médio de um incidente grave (ransomware) em **R$ 80.000**, com exposição esperada de **R$ 16.000/ano** sem controles (probabilidade 20%/ano) caindo para **R$ 4.000/ano** com os controles do Pilar III — um **risco evitado de R$ 12.000/ano** só nesse item (`Calculadora_ROI.md §5`). Some o retrabalho evitável (R$ 1.750/mês) e o tempo de TI recuperado (R$ 3.180/mês) e o custo anual das dores não tratadas passa de **R$ 71.000/ano** (`One_Pager_Vendas.md`).

Nenhum dos três tiers abaixo custa mais que uma fração desse valor — e todos são pensados para pagar a licença sozinhos com a redução de **1 único incidente evitado**.

---

## Os 3 Tiers

### Essencial — R$ 2.400/ano por empresa
**Para**: TI solo, até ~10 colaboradores, quer estruturar sem gastar tempo de IA/dev.

- Núcleo completo: 4 guias de pilar + guias para leigos + 7 templates de 1 página + modelo de maturidade (IM-TI) + guia de KPIs/DAN/COT + playbook Fase Zero (30 dias).
- Acesso à busca semântica web (`busca.html`) e ao portal visual.
- Suporte por e-mail para dúvidas de implantação (SLA 3 dias úteis).

### Profissional — R$ 8.900/ano por empresa
**Para**: equipe de TI de 2 a 8 pessoas que quer acelerar execução com IA sem operar infraestrutura própria.

- Tudo do Essencial.
- 8 skills nativas do Claude Code (`consultor`, `fase-zero`, `kanban`, `governanca`, `seguranca`, `metricas`, `maturidade`, `prd`).
- 9 agentes markdown plug-and-play (Claude Projects / GPTs — copiar e colar, zero setup).
- Simulação de ROI personalizada com os números reais da empresa (não os exemplos da Calculadora).

### Enterprise — a partir de R$ 24.900/ano por empresa
**Para**: equipes acima de 8 pessoas, múltiplas unidades, ou quem quer o kanban GP-PME instalado direto na plataforma de gestão já em uso.

- Tudo do Profissional.
- Agentes ADK (Google) instalados: orquestrador "Gestor GP-PME" + 8 especialistas com adapters ClickUp/Notion/Trello/Jira/Linear.
- Servidor MCP + API REST para integração com sistemas próprios.
- Implantação assistida: consultor conduz os 30 dias da Fase Zero junto com o time (ver `Onboarding_Cliente.md`).

> Preço final por porte real da equipe e número de plataformas integradas — proposta fechada após diagnóstico. Faixa acima é ponto de partida.

---

## Tabela Comparativa

| Item | Essencial | Profissional | Enterprise |
|---|:---:|:---:|:---:|
| Guias de pilar + templates + modelo de maturidade | ✅ | ✅ | ✅ |
| Playbook Fase Zero (30 dias) | ✅ | ✅ | ✅ |
| Busca semântica + portal visual | ✅ | ✅ | ✅ |
| 8 skills Claude Code | — | ✅ | ✅ |
| 9 agentes markdown (Claude Projects/GPTs) | — | ✅ | ✅ |
| Simulação de ROI personalizada | — | ✅ | ✅ |
| Agentes ADK instalados (ClickUp/Notion/Trello/Jira/Linear) | — | — | ✅ |
| Servidor MCP + API REST | — | — | ✅ |
| Implantação assistida (consultor nos 30 dias) | — | — | ✅ |
| Atualizações inclusas | 12 meses | 12 meses | 12 meses |
| Licenciamento | por empresa | por empresa | por empresa |

---

## FAQ — 5 Objeções

**1. "Já pagamos consultoria de TI, por que mais um contrato?"**
Consultoria tradicional entrega diagnóstico e vai embora — você paga de novo a cada rodada. O GP-PME entrega o método operacional (templates, kanban, playbook) que a própria equipe roda depois, sem depender de reunião mensal de consultor para continuar funcionando. A licença é anual, não por hora.

**2. "Isso não é só documentação cara?"**
O núcleo é documentação, sim — mas documentação que substitui meses de maturação de ITIL/COBIT completos por artefatos de 1 página operáveis por 1 técnico. A partir do Profissional, some 8 skills e 9 agentes de IA que executam parte do trabalho, não só descrevem o processo.

**3. "Não temos orçamento agora."**
O tier Essencial custa menos que 1/3 do risco evitado anual só de segurança (R$ 12.000/ano) — sem contar retrabalho e tempo de TI recuperado. Payback esperado abaixo de 2 meses no cenário conservador da Calculadora (`Calculadora_ROI.md §3.2`). Se o caixa é o problema, comece pelo Essencial e migre de tier quando o primeiro KPI (IDSC/TMpR/ISU) mostrar resultado.

**4. "Nossa equipe é pequena demais pra isso — 1 ou 2 pessoas."**
É exatamente o público do Pilar II (ciclo One-Man-Band) e do tier Essencial. O framework foi desenhado para caber num técnico solo; não exige comitê formal nem analista de governança dedicado.

**5. "E se não der certo?"**
O critério de sucesso é objetivo e verificável em 30 dias: IM-TI sobe de Nível 0 para Nível 1, Canal Único captura >90% das solicitações, backup testado a 100%. Esses critérios estão no `Onboarding_Cliente.md` com data de checagem (D30). Se não forem atingidos por causa do método (não por falta de adesão interna), a implantação assistida (Enterprise) é reforçada sem custo adicional até o critério ser atingido.

---

## Licenciamento

- **Unidade de cobrança**: por empresa (CNPJ), não por usuário nem por número de técnicos — a equipe inteira usa sem custo incremental por assento.
- **Atualizações**: incluídas por 12 meses a partir da assinatura (novas versões de guias, templates, skills e agentes).
- **Renovação**: anual. Sem multa de cancelamento; sem renovação automática silenciosa — aviso 30 dias antes do vencimento.
- **Migração de tier**: crédito proporcional ao tempo restante da assinatura atual ao migrar para um tier superior.
