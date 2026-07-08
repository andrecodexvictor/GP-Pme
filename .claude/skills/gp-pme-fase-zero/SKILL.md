---
name: gp-pme-fase-zero
description: Use para implantar a Fase Zero do GP-PME — o playbook de 30 dias para tirar uma PME do caos operacional. Gatilhos - "implantar a fase zero", "primeiros 30 dias de TI", "quick wins", "minha TI é um caos, por onde começo", "quero organizar a TI do zero", "sair do nível 0 de maturidade", "montar cronograma de implantação". Gera o cronograma semanal com checklist, responsáveis, critérios de validação e entregáveis, e confirma a prontidão de transição para o Nível 1 de maturidade.
---

# GP-PME Fase Zero — Implantação dos Primeiros 30 Dias

Este skill conduz a "Fase Zero" (Salva-Vidas / Injeção de Valor): 30 dias para tirar a TI da PME do Nível 0 (Caótico) para o Nível 1 (Reativo Organizado). É um cronograma de execução, não um guia de leitura — a cada semana gera um checklist com responsável e critério de validação, no formato da Tasklist Operacional do framework.

## QUANDO USAR

- Usuário confirmou (via `gp-pme-consultor` ou diretamente) que está no Nível 0 de maturidade (IM-TI ≤ 2).
- Usuário pede explicitamente para "organizar a TI do zero" ou "montar os primeiros 30 dias".
- Empresa nunca teve Canal Único nem Kanban ativos.
- **Não usar** se Canal Único e Kanban já existem e funcionam (IM-TI ≥ 3) — nesse caso o problema é outro; rotear para `gp-pme-kanban` (operação do quadro) ou `gp-pme-governanca` (alinhamento). Não reaplique a Fase Zero em uma TI que já saiu do caos — é regressão, não gera valor.

## FLUXO PASSO A PASSO

1. **Confirmar o baseline.** Antes de iniciar, pergunte se o usuário já tem o IM-TI de partida (via questionário de 10 perguntas). Se não tiver, aplique-o agora (fonte: `Guia_Modelo_de_Maturidade.md`, seção 4) — é o Dia 1-2 oficial da Fase Zero. Sem baseline não há como provar evolução ao final dos 30 dias.
   - Decisão: se o IM-TI de partida já for ≥ 3, avise o usuário que ele não está no cenário-alvo da Fase Zero e sugira `gp-pme-consultor` para re-rotear.

2. **Gerar o cronograma das 4 semanas**, adaptando aos dias reais do calendário do usuário (pergunte a data de início). Estrutura fixa (não comprimir nem pular semanas — a ordem existe porque cada semana depende da anterior):

   | Semana | Foco | Dias |
   |---|---|---|
   | 1 | Organizar o Caos | 1–7 |
   | 2 | Automatizar e Proteger | 8–14 |
   | 3 | Formalizar e Alinhar | 15–21 |
   | 4 | Medir e Consolidar | 22–30 |

3. **Semana 1 — Organizando o Caos Imediato.**
   - Dia 1-2: Diagnóstico de maturidade (já feito no passo 1) + Matriz de Eisenhower para as 3 prioridades da semana.
   - Dia 3-5: Montar o quadro Kanban de 4 colunas (*A Fazer, Em Andamento, Em Teste, Concluído*), WIP Limit = 3. Se o usuário quiser o detalhe operacional completo do quadro, delegue para `gp-pme-kanban` neste ponto e retome a Fase Zero na próxima semana.
   - Dia 6-7: Criar o Canal Único de suporte (e-mail ou formulário) e obter comunicado assinado pelo CEO proibindo canais informais.
   - Entregável da semana: Kanban ativo + Canal Único ativo.

4. **Semana 2 — Automatizando e Protegendo o Essencial.**
   - Dia 8-10: Documento de FAQ com as 5 dúvidas mais frequentes (senha, Wi-Fi etc.), disponível em pasta compartilhada.
   - Dia 11-14: Inventário 80/20 de ativos críticos (planilha) + rotina de backup diário em nuvem + **teste físico de restauração obrigatório** (< 30 min). Não marque este item como concluído sem o teste de restauração real — inventário sem teste de restauração é falso senso de segurança.
   - Entregável da semana: Planilha de Inventário 80/20 + backups testados.

5. **Semana 3 — Formalizando a Segurança e o Alinhamento.**
   - Dia 15-18: Plano de Resposta a Incidentes (PRI) de 1 página, impresso na sala de TI, assinado pelo CEO.
   - Dia 19-21: Primeira reunião CD-TI Lite de 30 min (CEO + Gestor de TI) e primeira Matriz 4 Quadrantes. Se o usuário precisar do detalhe da pauta e dos artefatos de governança, delegue para `gp-pme-governanca` neste ponto.
   - Entregável da semana: PRI assinado + primeira ata do CD-TI Lite.

6. **Semana 4 — Medindo o Sucesso e Consolidação.**
   - Dia 22-25: Ativar painel dos 3 KPIs Visíveis (IDSC, TMpR, ISU) e iniciar coleta de satisfação pós-atendimento.
   - Dia 26-30: Retrospectiva com o CEO, **reaplicar o questionário de maturidade** e calcular o IM-TI final.
   - Decisão de transição: confirme os critérios de transição Nível 0→1 antes de declarar sucesso:
     | Critério | Meta |
     |---|---|
     | IM-TI final | ≥ 3 (Nível 1) |
     | Centralização de solicitações no Canal Único | > 90% |
     | TMpR | redução de 30–40% frente ao baseline |
     | Resoluções por autoatendimento (FAQ) | > 40% |
     | Conformidade de backup | 100% testado e homologado |
   - Se qualquer critério não for atingido, não declare a transição — identifique qual dia/tarefa da semana correspondente ficou incompleto e retome-a antes de fechar a Fase Zero.
   - Entregável final: Relatório de transição de fase com IM-TI Nível 1 certificado e assinatura do CEO.

7. **Formatar o checklist de acompanhamento** no padrão da Tasklist Operacional do framework (`[ ]` não iniciada, `[/]` em andamento, `[x]` concluída — sempre com Ação, Responsável e Critério de Validação explícitos por tarefa). Nunca crie uma tarefa sem critério de validação verificável.

8. **Atribuir responsáveis conforme os papéis oficiais da Fase Zero** (não delegue tarefas de forma genérica — cada entregável tem um dono claro):
   | Papel | Responsabilidades na Fase Zero |
   |---|---|
   | Gestor de TI (Orquestrador) | Configurar Canal Único, operar o Kanban diariamente, alimentar a IA com FAQs comuns, preparar o Inventário 80/20 e os backups |
   | CEO / Dono da Empresa | Patrocinar o uso exclusivo do Canal Único, instruir colaboradores a abandonar canais informais, assinar o PRI e participar do primeiro CD-TI Lite |

9. **Oferecer os atalhos opcionais de IA por semana quando o usuário tiver o Pilar IV disponível** (nunca torne obrigatório — a Fase Zero deve funcionar 100% manual):
   | Semana | Atalho opcional com IA |
   |---|---|
   | 1 | Analista de Execução Ágil preenche o questionário de maturidade e gera a matriz de Eisenhower priorizada em minutos |
   | 2 | Bot de atendimento integrado ao Canal Único responde às FAQs antes de abrir cartões |
   | 3 | Guardião de Segurança audita e sugere melhorias no PRI contra ransomware |
   | 4 | Engenheiro de Prompts e Métricas calcula a evolução do IM-TI e redige o relatório de transição |

10. **Reconhecer os modos de falha mais comuns e corrigir antes de fechar a semana correspondente:**
    | Sintoma | Semana afetada | Correção |
    |---|---|---|
    | Kanban criado mas ninguém migrou os chamados antigos para ele | 1 | Forçar a migração completa antes de avançar — Kanban parcial não conta como "ativo" |
    | Canal Único criado mas CEO não comunicou oficialmente a proibição de canais informais | 1 | Bloquear a Semana 2 até o comunicado do CEO existir |
    | Backup "configurado" mas nunca testado fisicamente | 2 | Não marcar o item como concluído — exigir o teste de restauração real, não a existência da rotina |
    | PRI escrito mas não impresso/fixado na parede | 3 | Reforçar que "1 página assinada e impressa" é o critério, documento digital esquecido não vale |
    | Primeira reunião CD-TI Lite ultrapassou 30 min ou virou reunião técnica | 3 | Reencaminhar para `gp-pme-governanca` para recalibrar a pauta rígida |

## REFERÊNCIA RÁPIDA — AÇÕES GRANULARES OFICIAIS DA FASE ZERO (ROADMAP)

Use como checklist mestre de alto nível, independente do detalhamento dia a dia — se o usuário quiser só os 4 macro-itens sem o cronograma completo:

1. Mapeamento de Canais de Suporte → unificar em Canal Único (ferramenta gratuita de tickets ou formulário).
2. Implantação do Kanban de TI → painel de 4 colunas rastreando 100% das tarefas e incidentes.
3. Configuração de Agente de IA para Triagem Nível 1 (opcional) → bot respondendo FAQs de colaboradores.
4. Coleta e Registro da Baseline de TMpR → medir o tempo médio de resolução inicial para comparação futura.

Entregáveis formais da fase, conforme o Roadmap: Canal Único implantado · Quadro Kanban operacionalizado · Base de FAQs em produção · Métrica basal de TMpR documentada.

## INTEGRAÇÃO COM OUTRAS SKILLS

- Diagnóstico de maturidade antes/depois → questionário embutido no passo 1 e 6, mas para plano de transição aprofundado use `gp-pme-maturidade`.
- Detalhe operacional do quadro Kanban (cadência semanal, Raia Rápida) → `gp-pme-kanban`, engatada na Semana 1.
- Pauta e ata do primeiro CD-TI Lite → `gp-pme-governanca`, engatada na Semana 3.
- Painel de KPIs e cálculo formal de DAN → `gp-pme-metricas`, engatada na Semana 4.
- Checklist de segurança além do backup básico (MFA, privilégio mínimo) → `gp-pme-seguranca`, indicado como próximo passo pós-Fase Zero, não parte dela.

## FONTES NO FRAMEWORK

| Caminho | O que extrair |
|---|---|
| `GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md` | Cronograma completo dia a dia (seções 1–4), tabela de métricas de validação antes/depois |
| `Docs/Roadmap.md` | Seção "1. Fase Zero" — objetivo central, ações granulares, papéis e responsabilidades (Gestor de TI vs CEO), entregáveis oficiais |
| `GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md` | Seção 4 (questionário de 10 perguntas + cálculo IM-TI) para o baseline e a reavaliação final |
| `GP-PME antigravity/Templates/Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md` | Template para registrar IM-TI de partida e final |
| `GP-PME antigravity/Templates/Tasklists/Template_Tasklist_Operacional.md` | Formato de checklist (`[ ]`/`[/]`/`[x]`) com Ação/Responsável/Critério de Validação a ser usado em cada semana |

## SAÍDAS ESPERADAS

- Cronograma de 30 dias com datas reais (calendário do usuário), dividido nas 4 semanas.
- Checklist por semana no formato Tasklist (Ação, Responsável, Critério de Validação, status `[ ]/[/]/[x]`).
- Tabela de métricas antes/depois preenchida ao final (IM-TI, centralização, TMpR, autoatendimento, backup).
- Relatório de transição de fase (1 página) confirmando ou não a passagem para o Nível 1.

## EXEMPLOS

**Exemplo 1 — início do zero.**
Usuário: "Confirmei no diagnóstico, estamos no Nível 0. Quero o cronograma completo começando segunda que vem."
→ Gera cronograma com datas reais a partir da segunda-feira informada, semana a semana, com checklist Tasklist para cada entregável, começando pelo Dia 1-2 (mas o IM-TI baseline já está confirmado, então pula direto para Dia 3-5: montagem do Kanban).

**Exemplo 2 — meio do processo, travado na Semana 2.**
Usuário: "Já temos Kanban e Canal Único rodando há 2 semanas, mas nunca testamos o backup."
→ Confirma que Semana 1 está concluída. Foca no item pendente: Inventário 80/20 + teste de restauração (Dia 11-14). Avisa que sem o teste físico de restauração o critério "Conformidade de Backup: 100% testado" da Semana 4 não pode ser fechado, e isso bloqueia a certificação de transição para o Nível 1.
