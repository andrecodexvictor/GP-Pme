# GP-PME — Calculadora de ROI (Fórmulas Parametrizadas)

**Uso**: Este arquivo reúne todas as fórmulas empregadas nas quatro simulações de perfil (`Perfil_A` a `Perfil_D`). Cada fórmula está parametrizada com variáveis nomeadas, traz **1 exemplo resolvido** e está pronta para o cliente substituir pelos números reais da sua PME.

**Fontes normativas** (definições e equações exatas):
- KPIs e métricas financeiras: `GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md`
- KPI ISU e metas: `GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md`
- Maturidade (IM-TI): `GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md`

> **Princípio metodológico**: todos os números das simulações são **conservadores** e partem de premissas declaradas. Nada de ROI milagroso — quando há dúvida, arredondamos o ganho **para baixo** e o custo **para cima**.

---

## 0. Premissas de custo comuns (base de todas as simulações)

Para converter tempo perdido em dinheiro, precisamos de um **custo-hora** consistente.

| Variável | Símbolo | Valor adotado nas simulações | Como obter o seu |
| :--- | :---: | :--- | :--- |
| Jornada mensal | `J` | **176 h/mês** | 22 dias úteis × 8 h |
| Fator de encargos + benefícios | `f` | **1,55** | Custo total empregador ÷ salário bruto (FGTS, INSS patronal, 13º, férias, VT, VR) |
| Horas comerciais/ano | `Hc` | **2.500 a 3.500 h** | dias de operação × horas/dia de faturamento |
| Custo-hora do usuário final (produtividade) | `Cu` | **R$ 25/h** | salário médio geral ~R$ 2.850 bruto → 2.850 × 1,55 ÷ 176 |

### Fórmula do Custo-Hora (`Ch`)

```
Ch = (Salário_bruto_mensal × f) / J
```

**Exemplo resolvido** (técnico de TI, salário R$ 6.000):
```
Ch = (6.000 × 1,55) / 176 = 9.300 / 176 = R$ 52,84/h  ≈  R$ 53/h
```

Custos-hora de TI usados nas simulações (todos derivados desta fórmula):

| Perfil | Salário bruto de referência | Custo-hora TI (`Ch`) |
| :--- | :---: | :---: |
| A (faz-tudo) | R$ 5.000 | **R$ 44/h** |
| B (pleno) | R$ 6.000 | **R$ 53/h** |
| C (técnico R$6k / gestor R$10k) | blended | **R$ 62/h** (téc. R$ 53 · gestor R$ 88) |
| D (equipe 5-8, média R$ 7.950) | blended | **R$ 70/h** |

---

## 1. KPIs Operacionais

### 1.1. IDSC — Índice de Disponibilidade de Serviços Críticos
Fonte: `Guia_KPIs_e_Quick_Wins.md §2.2`. Meta: **> 99,5%** em horário comercial.

```
IDSC (%) = ((Tempo_Total_Comercial − Tempo_de_Inatividade) / Tempo_Total_Comercial) × 100
```

**Exemplo resolvido** (mês com 250 h comerciais, 5 h de sistema fora do ar):
```
IDSC = ((250 − 5) / 250) × 100 = (245 / 250) × 100 = 98,0%
```
> Regra inversa útil para as simulações: `Horas_paradas/ano = (1 − IDSC/100) × Hc`.

### 1.2. TMpR — Tempo Médio para Resolução
Fonte: `Guia_KPIs_e_Quick_Wins.md §2.2`. Meta: **< 4 h** para incidentes de alta gravidade.

```
TMpR (h) = Soma_de_Horas(registro → fechamento) / Total_de_Chamados_Concluídos_no_Mês
```

**Exemplo resolvido** (chamados fecharam somando 180 h no mês, 30 chamados):
```
TMpR = 180 / 30 = 6,0 h por chamado
```

### 1.3. ISU — Índice de Satisfação do Usuário Final
Fonte: `Guia_Pilar_1_Governanca_Essencial.md §KPIs`. Nota média de **1 a 5 estrelas** pós-atendimento. Meta: **> 4,5/5,0**.

```
ISU = Soma_das_Notas_(1–5) / Total_de_Respostas
```

**Exemplo resolvido** (40 respostas somando 168 estrelas):
```
ISU = 168 / 40 = 4,2 / 5,0
```

### 1.4. Volume de Incidentes por Colaborador
Fonte: `Guia_KPIs_e_Quick_Wins.md §2.2`. Meta: **decréscimo mensal contínuo**.

```
Incidentes/Colaborador = Total_de_Incidentes_Abertos_no_Mês / Nº_Total_de_Colaboradores
```

**Exemplo resolvido** (62 incidentes/mês, 25 colaboradores):
```
Incidentes/Colab = 62 / 25 = 2,48 por colaborador/mês
```

---

## 2. Métricas Financeiras de Arquitetura

### 2.1. DAN — Dívida de Arquitetura Normalizada
Fonte: `Guia_KPIs_e_Quick_Wins.md §3.1`.

```
DAN = (Esforço_Refatoração_h × Custo_Hora_TI) / Orçamento_Anual_de_TI
```

Zonas de risco (do guia):
- 🟢 **Saudável**: `DAN < 0,15`
- 🟡 **Alerta**: `0,15 ≤ DAN ≤ 0,35`
- 🔴 **Crítico**: `DAN > 0,35`

**Exemplo resolvido** (800 h de refatoração acumulada, TI a R$ 53/h, orçamento anual de TI R$ 220.000):
```
DAN = (800 × 53) / 220.000 = 42.400 / 220.000 = 0,193  → 🟡 Alerta
```

### 2.2. COT — Custo de Otimização Tecnológica
Fonte: `Guia_KPIs_e_Quick_Wins.md §3.2`.

```
COT = Custos_Diretos(servidores, licenças, terceiros) + Custos_Indiretos(horas·homem internas de TI)
```

**Exemplo resolvido** (implantação: 90 h de TI a R$ 53/h + R$ 1.800 de backup em nuvem/ano + R$ 3.000 de treinamento):
```
Custos_Indiretos = 90 × 53 = 4.770
Custos_Diretos   = 1.800 + 3.000 = 4.800
COT = 4.770 + 4.800 = R$ 9.570
```

---

## 3. ROI e Payback

### 3.1. ROI do COT (% anual)
Fonte: `Guia_KPIs_e_Quick_Wins.md §3.2`.

```
ROI_COT (%) = (Redução_Anual_de_Custos_da_DAN / COT) × 100
```

Forma operacional equivalente (usada nas simulações, com base em perdas evitadas):
```
ROI_Prático (%) = (Perdas_Mensais_Evitadas × 12 / COT) × 100
```

**Exemplo resolvido** (perdas mensais evitadas R$ 5.195, COT R$ 9.570):
```
ROI_Prático = (5.195 × 12 / 9.570) × 100 = (62.340 / 9.570) × 100 = 651%
```

### 3.2. Payback (meses)

```
Payback (meses) = COT / Ganho_Mensal
```
Onde `Ganho_Mensal = Perdas_Mensais_Evitadas`.

**Exemplo resolvido** (COT R$ 9.570, ganho mensal R$ 5.195):
```
Payback = 9.570 / 5.195 = 1,84 meses  (≈ 8 semanas)
```

---

## 4. Custos das dores (componentes do Ganho Mensal)

O `Ganho_Mensal` das simulações é a soma de três parcelas tangíveis. As fórmulas abaixo geram cada parcela.

### 4.1. Custo de Retrabalho Mensal (`CRM`)

```
CRM = Horas_Retrabalho_Mês × Cu
```
**Exemplo** (70 h/mês de retrabalho manual, `Cu` = R$ 25):
```
CRM = 70 × 25 = R$ 1.750/mês
```

### 4.2. Custo do Tempo de TI Desperdiçado (`CTD`)
Tempo da equipe técnica perdido com multitarefa, fila invisível e chamados informais.

```
CTD = Horas_TI_Desperdiçadas_Mês × Ch
```
**Exemplo** (60 h/mês, `Ch` = R$ 53):
```
CTD = 60 × 53 = R$ 3.180/mês
```

### 4.3. Custo de Hora Parada (`CHP`) e perda mensal por indisponibilidade

```
CHP = (N_Colab_Impactados × Cu) + (Receita_por_Hora × %_Receita_em_Risco)
Perda_Indisponibilidade_Mês = CHP × (Horas_Paradas_Ano / 12)
```
**Exemplo** (12 colaboradores parados; ignorando margem de venda perdida para ficar conservador; 87,5 h paradas/ano):
```
CHP = (12 × 25) + 0 = R$ 300/h
Perda_Mês = 300 × (87,5 / 12) = 300 × 7,29 = R$ 2.188/mês
```
> Nas simulações mantivemos `%_Receita_em_Risco = 0` na maioria dos casos (só produtividade), para **não inflar** o ROI com margem de vendas perdida.

### 4.4. Ganho Mensal total

```
Ganho_Mensal = (CRM_antes − CRM_depois) + (CTD_antes − CTD_depois) + (Perda_Indisp_antes − Perda_Indisp_depois)
```

---

## 5. Custo de risco evitado (segurança — NIST-Lite)

Não entra no ROI principal (para mantê-lo conservador); é apresentado como **upside** na seção "Riscos Evitados" de cada perfil.

```
Custo_Esperado_Anual_Incidente = Prob_Anual × Custo_Médio_por_Incidente
Risco_Evitado_Ano = (Prob_SEM − Prob_COM) × Custo_Médio_por_Incidente
```

**Exemplo resolvido** (ransomware em PME; custo médio R$ 80.000; probabilidade cai de 20%/ano para 5%/ano com Backups 3-2-1 + MFA + LUA + PRI):
```
Risco_Evitado = (0,20 − 0,05) × 80.000 = 0,15 × 80.000 = R$ 12.000/ano
```

Controles NIST-Lite que reduzem a probabilidade (fonte: `Guia_Pilar_3_Seguranca_Critica.md` — destilação de **CIS Controls v8 IG1**):
1. **Inventário 80/20** (Identificar) — sabe-se o que proteger.
2. **Privilégio Mínimo / LUA** (Proteger) — malware não se instala nem se espalha.
3. **MFA mandatório** (Proteger) — bloqueia roubo de credenciais/phishing.
4. **Backups 3-2-1 testados** (Proteger/Recuperar) — restauração garantida < 30 min.
5. **PRI de 1 página** (Responder) — contenção rápida reduz o tempo de parada.

---

## 6. IM-TI — Índice de Maturidade da TI (referência de nível)
Fonte: `Guia_Modelo_de_Maturidade.md §4`. Some 1 ponto por "Sim" nas 10 perguntas binárias:

| Pontos | Nível |
| :---: | :--- |
| 0–2 | Nível 0 — Caótico |
| 3–5 | Nível 1 — Reativo Organizado |
| 6–8 | Nível 2 — Governança Básica |
| 9 | Nível 3 — Inovação Incremental |
| 10 | Nível 4 — Governança Adaptativa |

---

### Planilha-modelo (preencha com os seus números)

| Parâmetro | Símbolo | Seu valor |
| :--- | :---: | :--- |
| Salário bruto TI | — | R$ ____ |
| Custo-hora TI | `Ch` | R$ ____ |
| Custo-hora usuário | `Cu` | R$ 25 |
| Horas retrabalho/mês (antes) | — | ____ h |
| Horas TI desperdiçadas/mês (antes) | — | ____ h |
| Horas paradas/ano (antes) | — | ____ h |
| Esforço de refatoração | — | ____ h |
| Orçamento anual de TI | — | R$ ____ |
| COT da implantação | `COT` | R$ ____ |
| **Ganho mensal** | — | **R$ ____** |
| **ROI** | — | **____%** |
| **Payback** | — | **____ meses** |
