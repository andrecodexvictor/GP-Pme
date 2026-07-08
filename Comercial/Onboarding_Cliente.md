# GP-PME — Onboarding do Cliente (D0 → D30)

> Fonte técnica: `GP-PME antigravity/Guides/Guia_de_Implementacao_Fase_Zero.md` — este documento reveste o playbook de 30 dias da Fase Zero com a camada comercial: responsáveis, critérios de aceite e materiais de kickoff. Não reescreve o conteúdo técnico; referencia os mesmos entregáveis e datas.

---

## Visão geral

| | |
|---|---|
| **Duração** | 30 dias corridos (D0 a D30) |
| **Meta de saída** | IM-TI sai do Nível 0 (Caótico) e certifica Nível 1 (Reativo Organizado) |
| **Responsável cliente** | Dono/CEO (patrocinador) + Gestor de TI ou técnico responsável (executor) |
| **Responsável GP-PME** | Consultor de implantação (tier Enterprise) ou material self-service acompanhado por e-mail (tiers Essencial/Profissional) |
| **Tier aplicável** | Enterprise inclui consultor presencial nos checkpoints; Essencial/Profissional seguem o mesmo cronograma sem acompanhamento ativo |

---

## D0 — Kickoff

| Responsável | Ação | Artefato | Critério de aceite |
|---|---|---|---|
| Consultor | Reunião de kickoff (60 min) — ver script abaixo | Ata de kickoff | CEO e Gestor de TI confirmam disponibilidade semanal e nomeiam o responsável técnico |
| Cliente | Nomear responsável técnico único pela Fase Zero | E-mail de nomeação | 1 nome, 1 e-mail, 1 telefone registrados |
| Consultor | Enviar acesso aos materiais do tier contratado | E-mail de boas-vindas (modelo abaixo) | Cliente confirma acesso a `INDEX.md`, templates e (se aplicável) skills/agentes |

---

## Semana 1 (D1–D7) — Organizar o Caos

| Dia | Responsável | Ação | Artefato | Critério de aceite |
|---|---|---|---|---|
| D1–D2 | Cliente (executa) / Consultor (revisa) | Aplicar `Template_Mapeamento_Maturidade.md` — questionário de 10 perguntas | Planilha de maturidade preenchida (IM-TI baseline) + 3 prioridades da semana | IM-TI de partida registrado (tipicamente Nível 0, ≤2 pontos) |
| D3–D5 | Cliente | Montar quadro Kanban (físico ou digital) com 4 colunas: A Fazer / Em Andamento / Em Teste / Concluído, WIP=3 por técnico | Quadro Kanban ativo | Todas as tarefas em aberto migradas para o quadro; WIP respeitado |
| D6–D7 | Cliente / Consultor valida | Criar Canal Único de suporte + comunicado do CEO proibindo canais informais | Canal Único ativo e divulgado | >90% das novas solicitações chegam pelo canal em 7 dias |

---

## Semana 2 (D8–D14) — Automatizar e Proteger

| Dia | Responsável | Ação | Artefato | Critério de aceite |
|---|---|---|---|---|
| D8–D10 | Cliente | Escrever base de FAQs com as 5 dúvidas mais frequentes | FAQ ativa (documento ou bot) | Arquivo publicado e acessível a todos os colaboradores |
| D11–D14 | Cliente (execução) / Consultor (auditoria) | Inventário 80/20 de ativos críticos + configurar backup diário + testar restauração | Planilha de inventário + backup em produção | Restauração testada com sucesso em <30 min |

---

## Semana 3 (D15–D21) — Formalizar e Alinhar

| Dia | Responsável | Ação | Artefato | Critério de aceite |
|---|---|---|---|---|
| D15–D18 | Cliente (preenche) / Consultor (revisa contra ransomware) | Preencher PRI de 1 página, fixar na sala de TI | PRI assinado pelo CEO | Documento impresso/afixado + contatos de emergência validados |
| D19–D21 | CEO + Gestor de TI (reunião) / Consultor facilita a 1ª sessão | Primeira reunião CD-TI Lite (30 min) + Matriz 4 Quadrantes | Ata CD-TI Lite de 1 página | Metas de faturamento conectadas aos projetos do Kanban |

---

## Semana 4 (D22–D30) — Medir e Consolidar (Handover)

| Dia | Responsável | Ação | Artefato | Critério de aceite |
|---|---|---|---|---|
| D22–D25 | Cliente | Configurar painel dos 3 KPIs (IDSC, TMpR, ISU) e iniciar coleta de satisfação | Painel de KPIs ativo | Pelo menos 1 ciclo de coleta registrado |
| D26–D29 | Cliente + Consultor | Retrospectiva com o CEO + reaplicar questionário de maturidade | IM-TI final calculado | IM-TI ≥ 3 (Nível 1), com Canal Único, Kanban e FAQ ativos |
| D30 | Consultor | Reunião de handover — entrega do relatório de transição de fase | Relatório de transição assinado pelo CEO | Todos os 6 indicadores da tabela "Antes/Depois" da Fase Zero atingidos (ver abaixo); cliente assume operação autônoma |

### Critérios de aceite consolidados (D30)

| Indicador | Baseline (D0) | Meta (D30) |
|---|---|---|
| Maturidade da TI (IM-TI) | Nível 0 (≤2) | Nível 1 (≥3) |
| Centralização de solicitações | <30% | >90% no Canal Único |
| Tempo de resposta (TMpR) | Indefinido / >24h | Redução de 30-40% |
| Resoluções por autoatendimento | 0% | >40% via FAQ |
| Conformidade de backup | Incerta / sem teste | 100% testado |
| Alinhamento do CEO | Sem visibilidade financeira | 100% via Matriz 4 Quadrantes |

Se algum critério não for atingido por falha do método (não por falta de adesão interna do cliente), tier Enterprise reforça acompanhamento sem custo adicional até a meta ser atingida (ver `Modelo_de_Precificacao.md` FAQ 5).

---

## Script do Kickoff (D0, 60 min)

1. **Abertura (5 min)** — apresentação do consultor e objetivo da reunião: alinhar expectativas e confirmar responsáveis antes de iniciar os 30 dias.
2. **Diagnóstico rápido (15 min)** — perguntar ao CEO: qual é a dor mais visível hoje (retrabalho, backup, prazo, falta de métrica)? Isso define a prioridade nas primeiras 3 tarefas do Kanban.
3. **Apresentar o cronograma (15 min)** — percorrer as 4 semanas (Organizar → Automatizar/Proteger → Formalizar → Medir), deixando claro que cada semana tem entregável verificável, não apenas leitura.
4. **Nomear responsáveis (10 min)** — confirmar quem é o executor técnico do dia a dia e quem é o patrocinador (CEO) que participa do CD-TI Lite.
5. **Definir cadência de checkpoint (10 min)** — agendar as reuniões de D7, D14, D21 e D30 (Enterprise) ou confirmar que o cliente seguirá sozinho com suporte por e-mail (Essencial/Profissional).
6. **Fechamento (5 min)** — recapitular os 3 primeiros entregáveis (Semana 1) e confirmar prazo de envio do e-mail de boas-vindas com os acessos.

---

## E-mail-modelo de Boas-vindas (pós-kickoff)

```
Assunto: GP-PME — Seus acessos e os primeiros passos (Fase Zero, D1–D7)

Olá [Nome],

Foi ótimo conversar hoje. Como combinado, aqui estão os acessos e o primeiro passo
da Fase Zero — os próximos 30 dias até sua TI sair do caos e ter governança de
1 página funcionando.

Seus acessos ([tier contratado]):
- Portal e índice geral: [link INDEX.md / portal visual]
- Templates de 1 página: [link Templates_GP-PME.md]
- [Se Profissional/Enterprise] Skills Claude Code e agentes markdown: [link]
- [Se Enterprise] Agentes ADK e integração com [ClickUp/Notion/Trello/Jira/Linear]: [link]

Sua primeira tarefa (D1–D2, ~1h):
Preencha o questionário de maturidade em [link Template_Mapeamento_Maturidade.md].
Não existe resposta errada — o objetivo é fotografar o ponto de partida (IM-TI
baseline) para medirmos a evolução em 30 dias.

Próximo checkpoint: [data D7] — confirmamos Kanban e Canal Único ativos.

Qualquer dúvida, responda este e-mail ou me chame em [telefone/canal].

[Nome do consultor]
GP-PME
```
