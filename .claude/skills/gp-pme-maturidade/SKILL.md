---
name: gp-pme-maturidade
description: Use esta skill quando o usuário quiser fazer a autoavaliação de maturidade de TI de uma PME, calcular o IM-TI (Índice de Maturidade), posicionar a empresa na matriz 5 níveis × 4 pilares, ou montar o plano de ação de transição de nível. Gatilhos: "qual nosso nível de maturidade", "autoavaliação de TI", "IM-TI", "matriz de maturidade", "estamos no nível X ou Y", "plano de transição de fase", "questionário de maturidade".
---

# Skill: GP-PME · Modelo de Maturidade (5 Níveis × 4 Pilares)

Motor enxuto que conduz a autoavaliação oficial do GP-PME: 10 perguntas binárias → Índice de Maturidade da TI (IM-TI) → posicionamento na matriz de 5 níveis × 4 pilares → plano de ação de transição. Não estime o nível "no olho" — sempre rode o questionário completo e exija evidência prática para cada "Sim".

## QUANDO USAR

1. **Diagnóstico inicial (Dia 1)** — "não sei em que estágio nossa TI está", "faça um diagnóstico de maturidade".
2. **Checkpoint periódico** — retrospectiva de 30 dias (fim da Fase Zero) ou auditoria semestral no CD-TI Lite.
3. **Decisão de "estamos prontos para avançar de nível?"** — "podemos partir para inovação (Nível 3)?", "já saímos do caos?".
4. **Planejamento de transição** — "o que falta para chegarmos ao Nível 2?".
5. **Cruzamento com outras skills** — apoia `gp-pme-seguranca` (Pilar III) e `gp-pme-metricas` (indicador IM-TI correlacionado a DAN/IDSC) quando o usuário pede uma visão de maturidade consolidada.

Não pule perguntas do questionário para "economizar tempo" — o IM-TI só é válido com as 10 respostas. Se o usuário não souber responder alguma, registre como "Não" até haver evidência.

## FLUXO PASSO A PASSO

### 1. Aplicar o Questionário de Autoavaliação (10 perguntas Sim/Não)
Cada "Sim" exige evidência concreta (nome de arquivo, data de teste, print da reunião). Sem evidência, marque "Não".

| # | Critério | Pergunta |
|:-:|:---|:---|
| 1 | Canal Único | Existe canal único formalizado de suporte, sem chamados informais (WhatsApp/corredor)? |
| 2 | Kanban Ativo | Quadro de 4 colunas ativo com WIP Limit ≤ 3 por técnico? |
| 3 | FAQs Operacionais | FAQ/chatbot resolve autonomamente > 40% das dúvidas básicas? |
| 4 | CD-TI Lite | CEO e Gestor de TI se reúnem 30 min periodicamente para revisar métricas/verbas? |
| 5 | Matriz 4 Quadrantes | Iniciativas são priorizadas pela Matriz 4 Quadrantes (impacto no faturamento)? |
| 6 | Inventário 80/20 | Existe planilha atualizada dos 20% de ativos mais críticos? |
| 7 | Backups Testados | Backup automático em nuvem + teste físico de restauração no último trimestre? |
| 8 | PRI de 1 Página | PRI assinado pelo CEO, impresso, com contatos e etapas de isolamento? |
| 9 | Métricas DAN/COT | Gestor calcula e apresenta DAN e ROI do COT no CD-TI Lite? |
| 10 | Auditoria HITL (IA) | Se usa IA para gerar código/documentos, há checklist de auditoria humana antes de produção? |

### 2. Calcular o IM-TI
`IM-TI = total de respostas "Sim" (0 a 10 pontos)`.

| Pontuação | Nível | Descrição |
|:-:|:---|:---|
| 0–2 | **Nível 0 — Caótico** | Urgente: implantar a Fase Zero (`gp-pme-fase-zero`) |
| 3–5 | **Nível 1 — Reativo Organizado** | Caos controlado; focar em segurança essencial e alinhamento |
| 6–8 | **Nível 2 — Governança Básica** | Operação segura e alinhada; pronta para ciclos de inovação/MVP |
| 9 | **Nível 3 — Inovação Incremental** | TI proativa, orientada a valor, controlando débito técnico |
| 10 | **Nível 4 — Governança Adaptativa** | Excelência operacional acelerada por IA sob controle humano (HITL) |

### 3. Posicionar na Matriz 5 × 4 (opcional, para diagnóstico aprofundado)
Se o usuário quiser detalhe por pilar (não apenas o score único), cruze o nível obtido com a Matriz de Maturidade (Pilar I Governança, Pilar II Execução Ágil, Pilar III Segurança Crítica, Pilar IV IA) do `Guia_Modelo_de_Maturidade.md`, descrevendo características, inputs, saídas e métricas esperadas de cada pilar naquele nível.

### 4. Gerar o Plano de Ação de Transição
Para cada pergunta marcada "Não", crie uma ação com responsável, prazo e evidência de conclusão esperada, usando o checklist de transição do nível atual → próximo nível (ex.: Nível 0→1: unificar canal, ativar Kanban, WIP=3, FAQ inicial, TMpR baseline).

### 5. Registrar e homologar
Feche com a assinatura simbólica: Gestor de TI (homologação) + CEO/Dono (aprovação) e data — replicando o rito de governança do template oficial.

## FONTES NO FRAMEWORK

| Artefato | Caminho | Uso nesta skill |
|:---|:---|:---|
| Guia do Modelo de Maturidade | `GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md` | Os 5 níveis, a matriz 5×4 completa, o questionário de 10 perguntas, cálculo do IM-TI e os 4 checklists de transição |
| Template de Mapeamento de Maturidade | `GP-PME antigravity/Templates/Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md` | Formulário oficial preenchível (questionário + folha de pontuação + plano de ação + campo de assinatura) |

## SAÍDAS ESPERADAS

- **Questionário preenchido** (10 linhas: pergunta, resposta Sim/Não, evidência).
- **IM-TI calculado** (0 a 10) com o nível de maturidade correspondente nomeado.
- **Posicionamento na matriz 5×4** por pilar, quando pedido em profundidade.
- **Plano de ação de transição** com ações, responsável, prazo e evidência de conclusão para cada "Não".
- Recomendação explícita de próxima skill/guia a acionar (ex.: Nível 0 → `gp-pme-fase-zero`; lacunas de segurança → `gp-pme-seguranca`).

## EXEMPLOS

**Exemplo 1 — Diagnóstico do zero:**
> "Nunca fizemos essa avaliação. Ajuda a gente a descobrir nosso nível de maturidade."
→ Rodar as 10 perguntas uma a uma, pedindo evidência para cada "Sim", somar o IM-TI e anunciar o nível (ex.: 4 pontos → Nível 1 — Reativo Organizado).

**Exemplo 2 — Checkpoint pós-Fase Zero:**
> "Fizemos a Fase Zero há 30 dias. Canal único ✅, Kanban ✅, FAQ ✅, CD-TI Lite ✅, mas ainda não temos inventário 80/20 nem backup testado."
→ IM-TI = 4 (Nível 1); gerar plano de ação focado nos itens 6, 7, 8, 9, 10 para avançar ao Nível 2.

**Exemplo 3 — Decisão de avanço de fase:**
> "Estamos com 8 pontos no IM-TI. Podemos começar os ciclos de MVP?"
→ Nível 2 — Governança Básica confirmado; sim, pronto para iniciar Nível 3 (ciclos MVP de 2 semanas, cálculo de DAN/COT), indicar checklist de transição 2→3.
