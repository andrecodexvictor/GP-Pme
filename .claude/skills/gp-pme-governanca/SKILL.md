---
name: gp-pme-governanca
description: Use para operar a governança essencial do GP-PME (Pilar I - ADM-Lite) - montar a pauta e a ata do CD-TI Lite (reunião quinzenal de 30 min entre CEO e Gestor de TI), preencher a Matriz 4 Quadrantes de alinhamento de iniciativas de TI com metas de negócio, ou gerar o RACI-Lite de responsabilidades. Gatilhos - "pauta do CD-TI Lite", "reunião de TI com o CEO", "matriz 4 quadrantes", "RACI-Lite", "quem é responsável por isso na TI", "ata da reunião de TI", "alinhar TI com o negócio", "aprovar verba de TI".
---

# GP-PME Governança — CD-TI Lite, RACI-Lite e Matriz 4 Quadrantes

Este skill opera os 3 artefatos de governança do Pilar I (ADM-Lite: Avaliar, Dirigir, Monitorar): a reunião CD-TI Lite, a Matriz 4 Quadrantes e a Matriz RACI-Lite. Gera atas e artefatos prontos para uso, sempre em 1 página.

## QUANDO USAR

- Usuário precisa preparar ou conduzir a reunião quinzenal entre CEO e Gestor de TI.
- Usuário quer decidir em qual quadrante de valor uma iniciativa de TI se encaixa antes de pedir verba.
- Usuário reclama de ambiguidade de papéis ("ninguém é dono disso") e precisa de um RACI.
- Usuário quer gerar a ata de uma reunião já realizada.
- **Não usar** para gestão operacional do dia a dia do quadro Kanban (isso é `gp-pme-kanban`) nem para cálculo de KPIs numéricos avançados (isso é `gp-pme-metricas`) — governança aqui é sobre ritual de decisão e alinhamento, não sobre execução ou cálculo.

## FLUXO PASSO A PASSO

1. **Identificar qual dos 3 artefatos o usuário precisa** (podem ser combinados numa única reunião):
   - Pauta/condução da reunião → passo 2.
   - Priorização de iniciativas → passo 3 (Matriz 4 Quadrantes).
   - Definição de responsabilidades → passo 4 (RACI-Lite).
   - Fechamento formal → passo 5 (ata).

2. **Montar a pauta rígida de 30 minutos do CD-TI Lite.** Não exceda o tempo por etapa — a rigidez é o que garante que o CEO participe de forma sustentável:
   | Tempo | Etapa | Objetivo | Artefato de apoio |
   |---|---|---|---|
   | 5 min | Revisão dos KPIs | Apresentar uptime (IDSC) e agilidade de suporte (TMpR) da última quinzena | Planilha dos 3 KPIs Visíveis (delegar cálculo para `gp-pme-metricas` se ainda não estiver pronta) |
   | 15 min | Alinhamento e Matriz | Analisar cartões de projetos de TI vs. metas do negócio | Matriz 4 Quadrantes |
   | 5 min | Análise de Riscos | Ameaças urgentes de segurança + indicador DAN | Inventário 80/20 + Planilha DAN (delegar cálculo detalhado para `gp-pme-metricas` se necessário) |
   | 5 min | Próximos Passos | Aprovar verbas emergenciais/otimização (COT), formalizar decisões | Ata de 1 página |

   - Decisão: se o usuário ainda não tem os 3 KPIs nem o DAN calculados, não bloqueie a reunião por isso — rode a pauta com o que existe e marque como pendência para a próxima quinzena, referenciando `gp-pme-metricas` para fechar o gap antes do próximo ciclo.

3. **Preencher a Matriz 4 Quadrantes.** Cada iniciativa de TI da quinzena entra em exatamente um quadrante — se o usuário tentar encaixar uma iniciativa em mais de um, force a escolha do impacto primário:
   | Quadrante | Foco |
   |---|---|
   | Q1 — Injeção de Receita | Iniciativas que ajudam a vender mais |
   | Q2 — Redução de Custos | Iniciativas que economizam |
   | Q3 — Experiência do Cliente/Usuário | Iniciativas que agilizam atendimento/uso |
   | Q4 — Resiliência e Segurança | Iniciativas que protegem o negócio |
   - Para cada iniciativa, capture: nome curto, quadrante, meta de negócio conectada (do CEO), status no Kanban (referenciar `gp-pme-kanban` se o status precisar ser consultado no quadro real).

4. **Preencher a Matriz RACI-Lite.** Para cada processo/atividade crítica, atribuir exatamente **1 Aprovador (A)** por linha — nunca mais de um, isso é o erro mais comum que gera ambiguidade de novo:
   | Papel | Significado |
   |---|---|
   | R | Responsável — quem executa |
   | A | Aprovador — decide e responde pelo resultado (único por linha) |
   | C | Consultado — fornece input antes da execução |
   | I | Informado — recebe atualização depois |
   - Modelo de referência de colunas: CEO/Dono, Gestor de TI, Gestor de Área, Técnico IA (Bot, opcional).
   - Atividades típicas a mapear: definição de orçamento anual de TI, priorização de demandas no Kanban, triagem de incidentes Nível 1, auditoria/teste de backup, validação de PRD para micro-inovação.

5. **Gerar a ata de 1 página.** Estrutura mínima: data, presentes, KPIs revisados (números), decisões da Matriz 4 Quadrantes (o que foi aprovado/rejeitado e por quê), riscos identificados (DAN/segurança), verbas aprovadas, próximos passos com responsável e prazo. A ata deve caber em 1 página — se estiver maior, é sinal de que a pauta não respeitou os tempos do passo 2.

6. **Se o usuário quiser acelerar com IA**, ofereça o atalho opcional descrito no framework: alimentar o Orquestrador Estratégico com os dados brutos do Kanban/status de projetos para gerar o briefing de pauta automaticamente, ou sugerir 3 iniciativas de baixo custo para preencher o Quadrante 2 a partir de uma meta anual do CEO (ex: "reduzir despesas operacionais em 5%") — mas sempre reforce o protocolo HITL: toda pauta/matriz gerada por IA passa por revisão humana do Gestor de TI antes de ir ao CEO. Nunca entregue uma ata ou matriz "final" sem esse aviso quando a origem foi assistida por IA.

7. **O ciclo ADM-Lite por trás de cada artefato — use para explicar o "porquê" ao usuário, não só o "como":**
   ```
   [ AVALIAR ]  -> compreender riscos e performance da TI sob a ótica de negócio
        |
   [ DIRIGIR ]  -> Matriz 4 Quadrantes: prioridades claras, verba autorizada
        |
   [ MONITORAR ] -> 3 KPIs Visíveis acompanhados no próprio CD-TI Lite
   ```
   Cada etapa da pauta de 30 min (passo 2) mapeia para uma fase do ciclo: Revisão de KPIs = Monitorar; Alinhamento e Matriz = Dirigir; Análise de Riscos = Avaliar. Se uma reunião pular a fase "Avaliar" (riscos) sistematicamente, o CD-TI Lite degenera em prestação de contas sem gestão de risco — reintroduza o bloco de 5 min mesmo sob pressão de agenda.

8. **RACI-Lite — exemplo de referência já validado no framework** (adaptar nomes de cargo, manter a estrutura de 1 Aprovador por linha):
   | Processo / Atividade | CEO/Dono | Gestor de TI | Gestor de Área | Técnico IA (Bot) |
   |---|:---:|:---:|:---:|:---:|
   | Definição do Orçamento Anual de TI | A | R | C | I |
   | Priorização das Demandas no Kanban | A | R | C | I |
   | Triagem Inicial de Incidentes (Nível 1) | I | A | I | R |
   | Auditoria e Teste de Backup Crítico | I | A | - | R |
   | Validação de PRD para Micro-Inovação | C | A | R | I |

9. **Erro comum a vetar ativamente:** tratar a reunião do CD-TI Lite como espaço para debater detalhes técnicos de implementação (ex: qual biblioteca usar, como configurar um servidor). Se isso acontecer, interrompa e redirecione — a pauta é estratégica (KPIs, prioridade, risco, verba), não técnica; questões técnicas ficam para o dia a dia do Kanban (`gp-pme-kanban`).

## FONTES NO FRAMEWORK

| Caminho | O que extrair |
|---|---|
| `GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md` | Seção 2 (ciclo ADM-Lite: Avaliar/Dirigir/Monitorar), seção 3 (pauta rígida de 30 min do CD-TI Lite), seção 4 (RACI-Lite, Matriz 4 Quadrantes, 3 KPIs Visíveis), seção 5 (aceleração opcional com IA + protocolo HITL) |
| `GP-PME antigravity/Templates_GP-PME.md` | Template 1 (RACI-Lite pronto com colunas e exemplos de atividades) e Template 2 (Matriz 4 Quadrantes em ASCII pronta para preencher) |
| `GP-PME antigravity/guide-for-dummies/Guia_Leigo_Pilar_1.md` | Versão sem jargão para explicar o CD-TI Lite e a Matriz 4 Quadrantes a um CEO não técnico |

## SAÍDAS ESPERADAS

- Pauta de 30 minutos pronta para a próxima reunião (com os 4 blocos de tempo preenchidos).
- Matriz 4 Quadrantes com as iniciativas da quinzena classificadas.
- Matriz RACI-Lite com 1 Aprovador único por linha.
- Ata de 1 página da reunião realizada, com decisões e responsáveis.

## EXEMPLOS

**Exemplo 1 — primeira reunião CD-TI Lite da empresa.**
Usuário: "Nunca fizemos essa reunião de TI com o CEO, como eu monto a primeira pauta?"
→ Monta a pauta de 30 min com os 4 blocos; para o bloco de KPIs, pergunta se já existem números (se não, marca "baseline a ser coletado" e sugere `gp-pme-metricas`); para o bloco de Matriz 4 Quadrantes, pede as 2-3 iniciativas de TI em andamento e classifica cada uma num quadrante junto com a meta de negócio do CEO.

**Exemplo 2 — conflito de responsabilidade.**
Usuário: "Ninguém sabe quem aprova as demandas urgentes de TI, sempre trava."
→ Gera o RACI-Lite para a atividade "Priorização das Demandas no Kanban", atribuindo A ao CEO ou ao Gestor de TI (força a escolha de um único aprovador), R ao Gestor de TI, C ao Gestor de Área solicitante, I ao restante — resolvendo a ambiguidade com uma linha objetiva da matriz.
