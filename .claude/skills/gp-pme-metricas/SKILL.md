---
name: gp-pme-metricas
description: Use esta skill quando o usuário pedir para calcular KPIs do GP-PME (IDSC, TMpR, ISU), a Dívida de Arquitetura Normalizada (DAN), o Custo de Otimização Tecnológica (COT) e seu ROI/payback, ou montar o painel mensal de métricas para o CD-TI Lite. Gatilhos: "calcule o IDSC", "qual o TMpR", "qual a DAN", "calcule o COT", "payback do investimento", "dashboard de KPIs", "painel mensal", "ROI da otimização".
---

# Skill: GP-PME · Métricas e KPIs (IDSC, TMpR, ISU, DAN, COT)

Motor enxuto que **calcula** os indicadores oficiais do GP-PME a partir dos dados brutos fornecidos pelo usuário (não estima nem inventa números). Sempre peça os insumos numéricos que faltarem antes de calcular — nunca preencha uma métrica com um valor não informado. Todas as fórmulas abaixo são as fórmulas oficiais do framework; não as substitua por aproximações.

## QUANDO USAR

1. **Cálculo de KPI operacional isolado** — "qual foi nosso uptime esse mês?", "quanto tempo levamos pra resolver chamados?", "qual a nota de satisfação dos usuários?".
2. **Cálculo de dívida técnica / justificativa de investimento** — "quanto vale nossa dívida técnica?", "vale a pena migrar esse servidor?", "calcule o ROI dessa automação".
3. **Montagem do painel mensal** — "monte o dashboard de métricas para a reunião com o CEO", "prepare os KPIs para o CD-TI Lite".
4. **Classificação de zona de risco** — "estamos em zona de alerta na DAN?", "isso é crítico ou saudável?".
5. **Comparação antes/depois** — validar se uma iniciativa (ex.: Fase Zero) melhorou os indicadores.

Não use esta skill para prever métricas futuras sem dados (projeção especulativa) — ela calcula com base em números reais informados pelo usuário; se um dado estiver ausente, pergunte por ele.

## FLUXO PASSO A PASSO

### 1. Identificar quais métricas o pedido exige
Mapeie o pedido para um ou mais dos 6 indicadores abaixo. Se o usuário pedir "o painel mensal", calcule todos que tiverem dados suficientes.

### 2. Coletar os insumos numéricos
Para cada métrica, pergunte exatamente os números que a fórmula exige (veja tabela de fórmulas abaixo). Não avance sem os insumos mínimos.

### 3. Aplicar a fórmula e mostrar o cálculo
Sempre exiba a fórmula com os números substituídos (não apenas o resultado final) — isso é o que dá credibilidade ao número perante o CEO.

#### Fórmulas Oficiais

| KPI | Fórmula | Meta / Zona |
|:---|:---|:---|
| **IDSC** (Disponibilidade de Serviços Críticos) | `IDSC (%) = ((Tempo Total Comercial − Tempo de Inatividade) / Tempo Total Comercial) × 100` | > 99,5% em horário comercial |
| **TMpR** (Tempo Médio para Resolução) | `TMpR = Soma de horas do registro ao fechamento / Total de chamados concluídos no mês` | < 4h para incidentes de alta gravidade |
| **ISU** (Índice de Satisfação do Usuário) | `ISU = Soma das notas (1 a 5 estrelas) pós-atendimento / Total de respostas` | > 4,5 / 5,0 |
| **DAN** (Dívida de Arquitetura Normalizada) | `DAN = (Esforço estimado de refatoração em horas × Custo-hora do técnico) / Orçamento anual de TI da PME` | ver zonas abaixo |
| **COT** (Custo de Otimização Tecnológica) | `COT = Custos diretos (servidores, licenças, terceiros) + Custos indiretos (horas/homem internas)` | payback ideal: poucos meses |
| **ROI do COT** | `ROI (%) = (Redução mensal de custos ou perdas evitadas / Investimento total em COT) × 100`; `Payback = COT / Economia mensal` | quanto menor o payback, melhor |

#### Zonas de Risco da DAN
- `🟢 Saudável: DAN < 0,15` — arquitetura ágil, baixo risco de parada.
- `🟡 Alerta: 0,15 ≤ DAN ≤ 0,35` — gargalos começam a atrasar projetos; propor COT no CD-TI Lite.
- `🔴 Crítico: DAN > 0,35` — alto risco de parada geral de faturamento; ação imediata do CD-TI Lite.

### 4. Classificar e contextualizar o resultado
Compare o resultado com a meta/zona e diga explicitamente se está dentro ou fora do esperado (ex.: "IDSC de 98,7% está abaixo da meta de 99,5% — investigar causa do tempo de inatividade").

### 5. Montar o painel mensal (quando solicitado)
Consolide os KPIs calculados em uma tabela única com coluna de meta e status (✅/⚠️/🔴), pronta para a pauta do CD-TI Lite.

## FONTES NO FRAMEWORK

| Artefato | Caminho | Uso nesta skill |
|:---|:---|:---|
| Guia de KPIs e Quick Wins | `GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md` | Fórmulas de IDSC, TMpR, ISU, DAN, COT + metas oficiais + exemplo prático de ROI |
| Capítulo 5 — Métricas Avançadas | `GP-PME antigravity/GP-Pme complete/Capitulo_5_Metricas_Avancadas_DAN_e_COT.md` | Detalhamento acadêmico de DAN/COT, zonas de risco em Mermaid, exemplo de negócio passo a passo |
| Guia do Pilar 1 (Governança Essencial) | `GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md` | Definição operacional dos 3 KPIs Visíveis (IDSC/TMpR/ISU) usados no CD-TI Lite |
| Templates GP-PME (dashboard) | `GP-PME antigravity/Templates_GP-PME.md` | Prompt de aceleração por IA para gerar o relatório do dashboard mensal |

## SAÍDAS ESPERADAS

- **Cálculo mostrado** (fórmula + números substituídos + resultado) para cada KPI pedido.
- **Classificação** de zona/meta (dentro da meta, alerta ou crítico) com uma frase de interpretação de negócio.
- **Painel mensal consolidado** em tabela Markdown (KPI | Valor | Meta | Status), quando o pedido for amplo.
- Quando a DAN for Crítica ou o payback do COT for atrativo (< 6 meses), sinalizar explicitamente que o item deve virar pauta do CD-TI Lite.

## EXEMPLOS

**Exemplo 1 — KPI isolado:**
> "Ficamos 4 horas fora do ar em um mês com 220 horas comerciais totais. Qual o IDSC?"
→ `IDSC = ((220 − 4) / 220) × 100 = 98,18%` — abaixo da meta de 99,5%, sinalizar como ponto de atenção.

**Exemplo 2 — DAN e zona de risco:**
> "Precisamos de 300 horas de refatoração, custo-hora de R$ 80, e o orçamento anual de TI é R$ 96.000."
→ `DAN = (300 × 80) / 96.000 = 0,25` → Zona 🟡 Alerta (0,15–0,35) — recomendar proposta de COT no próximo CD-TI Lite.

**Exemplo 3 — ROI/payback de um COT:**
> "O time de faturamento perde R$ 3.000/mês com um sistema manual. Migrar custaria R$ 9.000 (pagamento único)."
→ `ROI = (3.000 / 9.000) × 100 = 33,3% ao mês` (400% ao ano); `Payback = 9.000 / 3.000 = 3 meses` — recomendar aprovação.

**Exemplo 4 — Painel mensal:**
> "Monte o painel do mês: IDSC 98,9%, TMpR 5,2h com 40 chamados, ISU com notas somando 176 em 40 respostas."
→ Calcular ISU = 176/40 = 4,4 (abaixo da meta 4,5), montar tabela final com os 3 KPIs, metas e status ⚠️/✅.
