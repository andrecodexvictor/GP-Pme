# GP-PME — Simulações de ROI por Perfil de PME

**O que é esta pasta**: quatro estudos de caso completos que mostram, com números conservadores e premissas declaradas, o que acontece quando uma PME brasileira sai do caos operacional e implanta o framework **GP-PME**. Cada perfil percorre o mesmo arco — *dor → implantação → resultado → ROI* — em uma faixa de porte diferente, para que o leitor encontre a empresa mais parecida com a sua e projete o próprio retorno.

Estas simulações **não** vendem "ROI milagroso". Todas seguem o princípio metodológico da Calculadora: **quando há dúvida, arredondamos o ganho para baixo e o custo para cima**. As melhorias nunca são "porque sim" — cada queda de métrica é justificada pelo mecanismo do framework que a produz (o Canal Único elimina a fila invisível de chamados; a Matriz 4 Quadrantes derruba a DAN cortando trabalho sem valor; os Backups 3-2-1 testados reduzem a probabilidade de parada por ransomware).

---

## Como ler

1. **Comece pela Calculadora**: [`Calculadora_ROI.md`](./Calculadora_ROI.md) reúne todas as fórmulas parametrizadas (IDSC, TMpR, ISU, DAN, COT, ROI, Payback) com um exemplo resolvido cada. É a fonte única das equações — os perfis apenas as aplicam.
2. **Escolha o perfil mais próximo do seu porte** na tabela abaixo e leia-o de ponta a ponta. A estrutura é idêntica nos quatro:
   - **1. Retrato** — setor, faturamento, equipe de TI e stack.
   - **2. Sem framework** — a narrativa das dores e a tabela de linha-de-base com as premissas numéricas.
   - **3. Implantação semana a semana** — Fase Zero → Fase Três, custo em horas e artefatos usados.
   - **4. Com framework** — resultados a 90 dias e 12 meses, cada um justificado pelo mecanismo.
   - **5. Antes × Depois** — tabela comparativa + diagrama.
   - **6. ROI** — COT vs. ganho anualizado, payback e cenários conservador/esperado.
   - **7. Riscos evitados** — mapeados aos 10 controles NIST-Lite (CIS IG1).
3. **Preencha a planilha-modelo** da Calculadora (§ final) com os seus próprios números. Os perfis são um piso de referência, não uma promessa.

> **Leitura sugerida das fontes normativas** (definições exatas): `GP-PME antigravity/Guides/Guia_KPIs_e_Quick_Wins.md`, `Guia_de_Implementacao_Fase_Zero.md`, `Guia_Modelo_de_Maturidade.md`, `Guia_Pilar_2_Execucao_Agil.md`, `Guia_Pilar_3_Seguranca_Critica.md`.

---

## Os 4 perfis — tabela-resumo

| Perfil | Porte | Equipe de TI | Custo-hora TI (`Ch`) | Maturidade (IM-TI): início → 12 m | Ganho mensal recuperado | COT (investimento) | **ROI anual** | **Payback** |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **[A — TI Solo](./Perfil_A_TI_Solo.md)** | ~10 funcionários | 1 (faz-tudo) | R$ 44/h | Nível 0 → Nível 2 | **R$ 2.384** | **R$ 5.280** | **542%** | **2,2 meses** |
| **[B — 25 Funcionários](./Perfil_B_25_Funcionarios.md)** | 25 funcionários | 1–2 | R$ 53/h | Nível 0 → Nível 3 | **R$ 5.195** | **R$ 9.570** | **651%** | **1,8 meses** |
| **[C — 50 Funcionários](./Perfil_C_50_Funcionarios.md)** | 50 funcionários | 3 + 1º gestor | R$ 62/h (blended) | Nível 0 → Nível 3 | **R$ 10.707** | **R$ 20.680** | **621%** | **1,9 meses** |
| **[D — 100 Funcionários](./Perfil_D_100_Funcionarios.md)** | 100 funcionários | 5–8 + compliance | R$ 70/h (blended) | Nível 1 → Nível 4 | **R$ 22.150** | **R$ 65.800** | **404%** | **3,0 meses** |

### Cenário conservador (haircut de 40% sobre o ganho)

Para o CEO cético: mesmo se o framework entregar **apenas 60%** do ganho projetado, o retorno permanece forte.

| Perfil | Ganho mensal conservador | ROI anual conservador | Payback conservador |
| :--- | :---: | :---: | :---: |
| A | R$ 1.430 | 325% | 3,7 meses |
| B | R$ 3.117 | 391% | 3,1 meses |
| C | R$ 6.424 | 373% | 3,2 meses |
| D | R$ 13.290 | 242% | 5,0 meses |

---

## Leitura dos números (por que o ROI é alto e ainda assim conservador)

O GP-PME custa pouco porque é **deliberadamente enxuto**: quase todo o COT é *tempo interno de TI* (horas que a empresa já paga), somado a ferramentas gratuitas ou de baixo custo (Google/Microsoft Forms, Trello, backup em nuvem). O denominador do ROI é pequeno. O numerador — o desperdício recuperado — é grande porque a TI reativa de uma PME em Nível 0 sangra horas por três canais simultâneos:

- **Fila invisível de chamados** (WhatsApp, corredor, e-mail pessoal) → resolvida pelo **Canal Único**.
- **Multitarefa crônica** → resolvida pelo **WIP Limit = 3** e pela **Raia Rápida** do Kanban.
- **Parada de sistemas críticos** → reduzida pelo **Inventário 80/20 + Backups 3-2-1**.

O que **não** entra no ROI principal (para não inflá-lo): margem de vendas perdida em paradas (`%_Receita_em_Risco = 0` na maioria dos casos) e o **risco de segurança evitado**, apresentado à parte como *upside* na seção 7 de cada perfil. Se esses fossem contabilizados, o retorno seria substancialmente maior — o que reforça o caráter conservador destas simulações.

---

*GP-PME — sob a direção de Andre Victor. As fórmulas desta pasta são rastreáveis a ISO/IEC 38500, COBIT 2019, ITIL v4, NIST CSF 2.0 e CIS Controls v8 (IG1).*
