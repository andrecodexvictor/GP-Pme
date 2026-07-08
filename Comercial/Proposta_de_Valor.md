# GP-PME — Proposta de Valor

> Fontes: `README.md`, `GP-PME antigravity/INDEX.md` (v2.0), `Docs/PRD.md`, `Simulacao/Calculadora_ROI.md`.
> Nota de metodologia: na data desta proposta os perfis de simulação (`Simulacao/Perfil_A..D.md`) ainda estavam em elaboração por outra frente de trabalho. Os números de impacto abaixo usam os **exemplos resolvidos da própria Calculadora de ROI** (fórmulas oficiais do framework, premissas conservadoras e declaradas) — não são case reais de cliente. Assim que os perfis existirem, substitua pelos valores específicos de cada porte.

---

## Posicionamento

O GP-PME é o framework de governança de TI para PMEs que traduz ISO 38500, COBIT 2019, ITIL 4, NIST CSF e CIS Controls v8 em processos de 1 página que um técnico solo ou uma equipe de 5 pessoas conseguem operar sem contratar consultoria pesada nem parar a operação — com ou sem IA, e com IA como acelerador quando a empresa quiser.

## Elevator Pitch (30 segundos)

"A maioria das PMEs não tem problema de tecnologia, tem problema de governança: a TI apaga incêndio o dia inteiro, ninguém sabe se o backup funciona de verdade e o dono decide investimento no escuro. O GP-PME resolve isso com 4 pilares simples — governança, execução ágil, segurança crítica e IA opcional — que cabem em templates de 1 página e entregam o primeiro resultado mensurável em 30 dias, a Fase Zero. Não é ITIL nem COBIT completos: é a versão enxuta que uma PME real consegue rodar."

---

## As 7 Dores Clássicas da TI de PME

Para cada dor: o custo típico (metodologia `Calculadora_ROI.md`), a capacidade do GP-PME que resolve e a prova (norma + artefato).

### 1. TI reativa, sem alinhamento com o negócio
**Custo típico**: decisões de investimento em TI tomadas sem critério — CD-TI inexistente, dono descobre problema quando o sistema já caiu.
**Capacidade GP-PME**: Comitê CD-TI Lite (30 min quinzenais) + Matriz 4 Quadrantes de 1 página, conectando iniciativas de TI a objetivos de faturamento.
**Prova**: ISO/IEC 38500:2024 (modelo EDM → ADM-Lite) e COBIT 2019 — `Guia_Pilar_1_Governanca_Essencial.md`.

### 2. Canais de suporte fragmentados (WhatsApp, corredor, ligação pessoal)
**Custo típico**: retrabalho por perda de rastreabilidade. Usando `CRM = Horas_Retrabalho_Mês × Cu`, 70h/mês de retrabalho a R$ 25/h = **R$ 1.750/mês** perdidos só em trabalho refeito.
**Capacidade GP-PME**: Canal Único de Suporte — todo pedido entra por um ponto só, elimina fragmentação.
**Prova**: ITIL 4 (Sistema de Valor de Serviço) — `Guia_Pilar_2_Execucao_Agil.md`.

### 3. Multitarefa sem limite — todo mundo "trabalhando em tudo"
**Custo típico**: `CTD = Horas_TI_Desperdiçadas_Mês × Ch`. 60h/mês de tempo de TI disperso a R$ 53/h = **R$ 3.180/mês** de capacidade técnica desperdiçada em troca de contexto.
**Capacidade GP-PME**: Kanban com WIP Limit = 3 e sprints de 1 semana — força conclusão antes de abrir nova frente.
**Prova**: Princípios Lean/Kanban + ITIL 4 — `Guia_Pilar_2_Execucao_Agil.md`.

### 4. Dívida técnica invisível, sem visibilidade financeira
**Custo típico**: `DAN = (Esforço_Refatoração_h × Custo_Hora_TI) / Orçamento_Anual_TI`. Exemplo da Calculadora: 800h acumuladas a R$ 53/h sobre orçamento de R$ 220.000/ano → **DAN = 0,193 (zona de Alerta 🟡)** — dívida que já começa a frear projetos novos, mas invisível sem a métrica.
**Capacidade GP-PME**: métrica DAN + COT institucionalizadas no CD-TI Lite, com zonas de risco (saudável/alerta/crítico) monitoradas mensalmente.
**Prova**: COBIT 2019 (gestão de portfólio) — `Guia_KPIs_e_Quick_Wins.md §3`.

### 5. Backup não testado / sem plano de resposta a incidente
**Custo típico**: probabilidade de incidente grave (ransomware) sem controles ~20%/ano, custo médio R$ 80.000 → exposição esperada de **R$ 16.000/ano**. Com os controles do Pilar III, a Calculadora estima queda para ~5%/ano → **Risco_Evitado = (0,20 − 0,05) × 80.000 = R$ 12.000/ano**.
**Capacidade GP-PME**: Backups 3-2-1 testados + PRI (Plano de Resposta a Incidentes) de 1 página.
**Prova**: NIST CSF 2.0 (Proteger/Recuperar) + CIS Controls v8 IG1 — `Guia_Pilar_3_Seguranca_Critica.md`.

### 6. Acessos sem controle — sem MFA, sem privilégio mínimo
**Custo típico**: mesma exposição de risco do item 5; MFA e LUA (privilégio mínimo) são dois dos cinco controles que sustentam a queda de probabilidade de 20% para 5%.
**Capacidade GP-PME**: Inventário 80/20 de ativos críticos + Princípio do Privilégio Mínimo (LUA) + MFA mandatório.
**Prova**: CIS Controls v8 IG1 (defesas essenciais e priorizadas) — `Guia_Pilar_3_Seguranca_Critica.md`.

### 7. Sem métricas visíveis — dono decide no escuro
**Custo típico**: sem IDSC/TMpR/ISU, a diretoria não distingue TI cara de TI ineficiente; decisões de contratação/corte são feitas por percepção, não por dado.
**Capacidade GP-PME**: painel de 3 KPIs Visíveis (IDSC > 99,5%, TMpR, ISU > 4,5/5,0), medidos desde a Fase Zero.
**Prova**: `Guia_KPIs_e_Quick_Wins.md` + `Guia_Pilar_1_Governanca_Essencial.md`.

---

## Diferenciais

**Vs. consultoria tradicional de TI**: consultoria entrega diagnóstico e vai embora; o GP-PME entrega o método operacional (templates, kanban, playbook de 30 dias) que a própria PME roda depois, sem depender de reunião mensal de consultor para continuar funcionando.

**Vs. implantação completa de ITIL/COBIT**: frameworks de mercado completos exigem meses de maturação, comitês formais e, geralmente, um analista de governança dedicado — inviável para uma equipe de TI de 1 a 8 pessoas. O GP-PME destila as mesmas normas em artefatos de 1 página operáveis por um técnico solo, com a Fase Zero entregando resultado mensurável em 30 dias.

**Vs. não fazer nada**: o custo de não agir não é zero — é o retrabalho, o tempo de TI desperdiçado e a exposição a incidente que a Calculadora de ROI já quantifica linha a linha (seção 4 e 5 de `Calculadora_ROI.md`). "Não decidir" é decidir continuar pagando esses três custos todo mês.
