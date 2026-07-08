---
name: gp-pme-kanban
description: Use para montar ou operar o quadro Kanban do GP-PME (Pilar II - Execução Ágil). Gatilhos - "montar meu kanban", "organizar as demandas de TI", "meu WIP está estourado", "muita tarefa em andamento", "chegou uma emergência, o que faço com meu kanban", "quero rodar minha sprint semanal", "meu quadro está travado", "priorizar chamados". Configura as 4 colunas, o WIP Limit de 3, o Canal Único, a cadência semanal de sprint e a mecânica da Raia Rápida para incidentes críticos; também diagnostica gargalos num quadro já existente.
---

# GP-PME Kanban — Ciclo de Serviço Micro-Adaptativo

Este skill monta e opera o quadro Kanban de TI do GP-PME (Pilar II), incluindo o tratamento de emergências (Raia Rápida) e o ciclo de inovação One-Man-Band. Cobre tanto a configuração inicial de um quadro novo quanto o diagnóstico/desbloqueio de um quadro já em uso.

## QUANDO USAR

- Usuário nunca teve um Kanban de TI e precisa montar um do zero (fora do contexto de Fase Zero completa — se for a implantação inicial de 30 dias, prefira `gp-pme-fase-zero`, que engloba isso na Semana 1).
- Quadro já existe mas está com gargalo (cartões acumulados, WIP estourado, prioridade confusa).
- Usuário quer saber como rodar a cadência semanal (planejamento, checkpoint diário, retrospectiva).
- Ocorreu uma emergência e o usuário não sabe como tratar isso sem quebrar o WIP Limit.
- **Não usar** para questões de alinhamento estratégico com o CEO ou aprovação de verba — isso é `gp-pme-governanca`. O Kanban é gestão do fluxo operacional, não governança.

## FLUXO PASSO A PASSO

1. **Verificar se o quadro já existe.**
   - Se não existe: vá para o passo 2 (montagem).
   - Se existe e está gerando dor (gargalo, caos): pule para o passo 6 (diagnóstico de gargalos).
   - Se existe e funciona, mas o usuário só quer rodar a sprint da semana: vá para o passo 4 (cadência).

2. **Montar as 4 colunas estritas** (não adicionar colunas extras — a simplicidade é a regra, mais colunas = mais overhead administrativo que o método existe para evitar):
   | Coluna | Regra |
   |---|---|
   | A Fazer / Backlog | Ordenada de cima para baixo por prioridade do CD-TI Lite / Matriz 4 Quadrantes |
   | Em Andamento | **WIP Limit = 3 tarefas simultâneas por técnico** — regra rígida, sem exceção manual |
   | Em Teste | Aguardando validação do usuário solicitante |
   | Concluído | Testado, em produção, com feedback assinado |

3. **Configurar o Canal Único de entrada.** Todo cartão nasce a partir de uma solicitação registrada no Canal Único (e-mail/formulário único). Chamados informais (WhatsApp pessoal, corredor) não geram cartão — devem ser redirecionados ao Canal Único antes de entrar no quadro. Isso é pré-requisito, não opcional: sem Canal Único o Kanban vira só mais uma lista dispersa.

4. **Rodar a cadência semanal (Sprint de 1 semana):**
   - **Planejamento (15 min, segunda de manhã):** revisar "A Fazer", selecionar 3–5 cartões para a semana com base na Matriz 4 Quadrantes.
   - **Checkpoint diário (5 min, antes de iniciar o dia):** 3 perguntas — o que moveu para "Concluído" ontem? em que vou trabalhar hoje? há algum impedimento?
   - **Retrospectiva (15 min, fim da semana):** taxa de cumprimento da sprint (meta > 80% dos cartões planejados entregues) + TMpR do período.

5. **Classificar e priorizar novos chamados** com a Matriz de Priorização (Eisenhower Adaptada):
   | Severidade \ Urgência | Alta (parada de sistema) | Média (lentidão) | Baixa (dúvida/estética) |
   |---|:---:|:---:|:---:|
   | **Alto** (faturamento/ERP) | Crítico — fazer agora | Alto — resolver hoje | Médio — agendar na sprint |
   | **Médio** (setor/fila) | Alto — resolver hoje | Médio — agendar na sprint | Baixo — fila comum |
   | **Baixo** (individual) | Médio — agendar | Baixo — fila comum | Descarte — eliminar se sem valor |

   - Decisão de emergência: se a severidade for **Crítico**, não entra na fila normal — acione a Raia Rápida (passo 6) imediatamente, mesmo fora do ciclo de planejamento semanal.

6. **Tratar interrupções — decisão obrigatória por chamado novo:**
   - **Baixa/Média prioridade:** não interrompe a tarefa atual. Registra no Canal Único, entra no fim do backlog "A Fazer", planejada na próxima sprint.
   - **Crítica (parada geral/incidente de segurança):** ativar a **Raia Rápida (Expedite)**:
     1. Escolher, entre as tarefas "Em Andamento", a de menor prioridade comercial.
     2. Devolvê-la para "A Fazer" (libera espaço no WIP = 3).
     3. Colocar o cartão de emergência no topo do quadro (destaque visual).
     4. Dedicar 100% do esforço até a mitigação.
     5. Assim que resolvido e movido para "Concluído", resgatar a tarefa suspensa de volta para "Em Andamento".
   - Nunca ultrapasse o WIP=3 para "encaixar" a emergência sem suspender outra tarefa — isso é o erro mais comum que quebra o método.

7. **Diagnosticar gargalo num quadro já existente** (quando chamado para desbloqueio, não montagem):
   - Cartões acumulados em "Em Andamento" acima de 3 por técnico → violação de WIP, força a suspensão manual das excedentes de volta para "A Fazer".
   - Cartões parados em "Em Teste" por muito tempo → falta de retorno do usuário solicitante; escalar via Canal Único, não perseguir informalmente.
   - Backlog "A Fazer" crescendo sem nunca esvaziar → sinal de que a priorização (passo 5) não está sendo aplicada antes de aceitar novos cartões; revisar a Matriz de Priorização com o time.

8. **Se o usuário pedir para acelerar a redação de PRDs/MVPs dentro do ciclo de inovação** (Ideia → PRD Simplificado → MVP em até 2 semanas → Piloto/Feedback), delegue a produção do PRD para `gp-pme-prd` — este skill cuida do fluxo do quadro, não da redação do documento.

9. **Ciclo de inovação One-Man-Band — quando o usuário quer lançar um MVP, não só operar suporte.** O fluxo corre em paralelo ao Kanban de suporte, mas os cartões de MVP também respeitam o WIP=3:
   ```
   [ IDEIA / DOR ] -> [ PRD SIMPLIFICADO (1 pág) ] -> [ MVP (máx. 2 semanas) ] -> [ PILOTO & FEEDBACK ]
   ```
   - PRD Simplificado: dor de origem, histórias de usuário ("Como usuário, eu quero... para..."), critérios de aceitação binários (passa/não passa) — delegar a redação em si para `gp-pme-prd`.
   - MVP: a versão mais simples possível do recurso, nunca a "solução perfeita" — se o escopo cresceu além de 2 semanas, é sinal de que não é mais MVP, é projeto grande demais para este ciclo.
   - Piloto: liberar para um grupo controlado de usuários reais, coletar feedback imediato, não esperar "lançamento oficial" para validar.

10. **Diferenciar cartão de suporte de cartão de projeto/MVP no mesmo quadro.** Ambos competem pelo mesmo WIP=3 — não crie uma coluna paralela "projetos" que ignore o limite, isso reintroduz a multitarefa que o método existe para eliminar. Se o volume de suporte estiver sistematicamente engolindo o espaço para inovação, é sinal para revisar a Matriz de Priorização com o CD-TI Lite (via `gp-pme-governanca`), não para burlar o WIP.

## FONTES NO FRAMEWORK

| Caminho | O que extrair |
|---|---|
| `GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md` | Seção 2 (mecânica do Ciclo Micro-Adaptativo, cadência, Raia Rápida), seção 3 (4 colunas do Kanban, Canal Único, Matriz de Priorização Eisenhower), seção 4 (ciclo de inovação One-Man-Band) |
| `GP-PME antigravity/Templates/Tasklists/Template_Tasklist_Operacional.md` | Formato de checklist com legenda `[ ]/[/]/[x]` para registrar cartões e tarefas de sprint com Ação/Responsável/Critério de Validação |
| `GP-PME antigravity/guide-for-dummies/Guia_Leigo_Pilar_2.md` | Versão simplificada para explicar WIP=3 e Canal Único a um usuário não técnico |

## SAÍDAS ESPERADAS

- Quadro Kanban configurado (4 colunas, WIP=3, Canal Único apontado como única porta de entrada).
- Plano da sprint da semana: 3–5 cartões selecionados e priorizados pela Matriz de Priorização.
- Em caso de emergência: sequência exata de ações da Raia Rápida com o cartão suspenso identificado.
- Em caso de diagnóstico: causa raiz do gargalo (violação de WIP, falta de retorno do usuário, ou priorização não aplicada) + ação corretiva.

## EXEMPLOS

**Exemplo 1 — montagem do zero (fora do fluxo de Fase Zero).**
Usuário: "Já fizemos a Fase Zero há meses, mas nunca ligamos o Kanban de verdade, só uma planilha bagunçada."
→ Monta as 4 colunas com WIP=3, confirma que o Canal Único já existe (Fase Zero já rodou), migra os itens da planilha para "A Fazer" ordenados pela Matriz de Priorização, e agenda o primeiro Planejamento de 15 min de segunda-feira.

**Exemplo 2 — emergência em andamento.**
Usuário: "O ERP caiu agora e eu tenho 3 tarefas em andamento, o que eu faço?"
→ Classifica como Crítico (Alto impacto + Urgência alta) → aciona Raia Rápida: pede para escolher, das 3 tarefas em andamento, a de menor prioridade comercial, devolvê-la para "A Fazer", colocar o cartão do ERP no topo com destaque, e focar 100% até resolver — reforçando que a tarefa suspensa retorna para "Em Andamento" assim que o incidente for encerrado.
