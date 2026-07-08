# Graph Report - .  (2026-07-07)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 70 nodes · 102 edges · 13 communities (7 shown, 6 thin omitted)
- Extraction: 89% EXTRACTED · 11% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e3774780`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]

## God Nodes (most connected - your core abstractions)
1. `INDEX - Hub de Conhecimento RAG` - 11 edges
2. `Biblioteca de Templates GP-PME` - 11 edges
3. `Modelo NIST-Lite` - 10 edges
4. `Documento Mestre Consolidado (v5.2)` - 8 edges
5. `Ciclo ADM-Lite (Avaliar, Dirigir, Monitorar)` - 7 edges
6. `README - Framework GP-PME` - 6 edges
7. `Comitê CD-TI Lite (Reunião de 30 minutos)` - 6 edges
8. `DAN (Dívida de Arquitetura Normalizada)` - 6 edges
9. `GP-PME Framework` - 5 edges
10. `Ciclo de Serviço Micro-Adaptativo` - 5 edges

## Surprising Connections (you probably didn't know these)
- `Documento Mestre Completo Técnico (v6.0)` --semantically_similar_to--> `Documento Mestre Consolidado (v5.2)`  [INFERRED] [semantically similar]
  GP-PME/GP-PME_Documento_Mestre_Completo_Tecnico.md → GP-PME antigravity/GP-PME_Documento_Mestre_Consolidado.md
- `README - Framework GP-PME` --references--> `Filosofia da TI Enxuta (Lean IT)`  [EXTRACTED]
  README.md → GP-PME antigravity/GP-Pme complete/Capitulo_1_Arquitetura_e_Principios.md
- `README - Framework GP-PME` --references--> `Canal Único de Suporte`  [EXTRACTED]
  README.md → GP-PME antigravity/GP-Pme complete/Capitulo_3_Execucao_Agil_Ciclo_Micro_Adaptativo.md
- `README - Framework GP-PME` --references--> `Ciclo de Serviço Micro-Adaptativo`  [EXTRACTED]
  README.md → GP-PME antigravity/GP-Pme complete/Capitulo_3_Execucao_Agil_Ciclo_Micro_Adaptativo.md
- `README - Framework GP-PME` --references--> `WIP Limit de 3 Tarefas`  [EXTRACTED]
  README.md → GP-PME antigravity/GP-Pme complete/Capitulo_3_Execucao_Agil_Ciclo_Micro_Adaptativo.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Os 4 Controles Críticos Mínimos do NIST-Lite** — capitulo_4_seguranca_critica_nist_lite_inventario_80_20, capitulo_4_seguranca_critica_nist_lite_lua, capitulo_4_seguranca_critica_nist_lite_mfa, capitulo_4_seguranca_critica_nist_lite_backups_testados, capitulo_4_seguranca_critica_nist_lite_pri [EXTRACTED 0.95]
- **Os 4 Agentes Especialistas de IA do Pilar IV** — capitulo_6_motor_de_ia_e_engenharia_de_prompts_agente_orquestrador, capitulo_6_motor_de_ia_e_engenharia_de_prompts_agente_analista, capitulo_6_motor_de_ia_e_engenharia_de_prompts_agente_guardiao, capitulo_6_motor_de_ia_e_engenharia_de_prompts_agente_auditor [EXTRACTED 0.95]
- **Pilares Modulares da Arquitetura Iceberg Invertido** — capitulo_2_governanca_essencial_adm_lite_adm_lite, capitulo_3_execucao_agil_ciclo_micro_adaptativo_ciclo_micro_adaptativo, capitulo_4_seguranca_critica_nist_lite_nist_lite, capitulo_5_metricas_avancadas_dan_e_cot_dan, capitulo_1_arquitetura_e_principios_iceberg_invertido [EXTRACTED 0.90]

## Communities (13 total, 6 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.21
Nodes (12): Bloco 1: Pilar Estratégico (Dummies), Architectural Technical Debt Index (Verdecchia, 2022), Comitê CD-TI Lite (Reunião de 30 minutos), Capítulo 2: Governança Essencial (ADM-Lite), 3 KPIs Visíveis (IDSC, TMpR, ISU), COT (Custo da Otimização Tecnológica), DAN (Dívida de Arquitetura Normalizada), Agente 4: Engenheiro de Prompts e Métricas (Auditor DAN/COT) (+4 more)

### Community 1 - "Community 1"
Cohesion: 0.23
Nodes (12): Método DAA (Direcionar, Agir, Acompanhar), Frame-sim (Simulador de Negócios), Modelo Iceberg Invertido, Filosofia da TI Enxuta (Lean IT), Documento Mestre Completo para Leigos (v6.0), Documento Mestre Completo Técnico (v6.0), GPT Best Practices: Prompt Engineering Guidelines (OpenAI, 2023), Documento Mestre Consolidado (v5.2) (+4 more)

### Community 2 - "Community 2"
Cohesion: 0.29
Nodes (10): Bloco 5: Roadmap e Frame-sim (Dummies), ITIL 4 (Axelos, 2019), The Scrum Guide (Schwaber & Sutherland, 2020), Canal Único de Suporte, Ciclo de Serviço Micro-Adaptativo, Quadro Kanban de 4 Colunas, WIP Limit de 3 Tarefas, Fase Zero (Playbook de 30 Dias) (+2 more)

### Community 3 - "Community 3"
Cohesion: 0.31
Nodes (9): CIS Controls v8 (IG1), NIST Cybersecurity Framework (CSF) 2.0, Backups Automatizados e Testados, Inventário 80/20 de Ativos Críticos, Privilégio Mínimo (LUA), MFA (Autenticação de Dois Fatores), Modelo NIST-Lite, Plano de Resposta a Incidentes (PRI) de 1 Página (+1 more)

### Community 4 - "Community 4"
Cohesion: 0.36
Nodes (8): MVP de 2 Semanas, Guia Leigo Pilar 1, Guia Leigo Pilar 2, Guia Leigo Pilar 3, Guia do Pilar 1: Governança Essencial, Guia do Pilar 2: Execução Ágil, Guia do Pilar 3: Segurança Crítica, INDEX - Hub de Conhecimento RAG

### Community 5 - "Community 5"
Cohesion: 0.40
Nodes (5): COBIT 2019 (ISACA), ISO/IEC 38500:2024, Ciclo ADM-Lite (Avaliar, Dirigir, Monitorar), Matriz 4 Quadrantes, Matriz RACI-Lite

### Community 6 - "Community 6"
Cohesion: 1.00
Nodes (3): PRD Simplificado de 1 Página, Agente 2: Analista de Execução Ágil, Pipeline de Prompts Encadeados (Prompt Chaining)

## Knowledge Gaps
- **24 isolated node(s):** `Capítulo 1: Arquitetura e Princípios`, `Capítulo 2: Governança Essencial (ADM-Lite)`, `Capítulo 3: Execução Ágil (Ciclo Micro-Adaptativo)`, `Capítulo 4: Segurança Crítica (NIST-Lite)`, `Capítulo 5: Métricas Avançadas (DAN e COT)` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Documento Mestre Consolidado (v5.2)` connect `Community 1` to `Community 0`, `Community 3`, `Community 4`, `Community 5`?**
  _High betweenness centrality (0.218) - this node is a cross-community bridge._
- **Why does `INDEX - Hub de Conhecimento RAG` connect `Community 4` to `Community 0`, `Community 1`, `Community 3`?**
  _High betweenness centrality (0.175) - this node is a cross-community bridge._
- **Why does `Biblioteca de Templates GP-PME` connect `Community 3` to `Community 0`, `Community 1`, `Community 4`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.144) - this node is a cross-community bridge._
- **What connects `Capítulo 1: Arquitetura e Princípios`, `Capítulo 2: Governança Essencial (ADM-Lite)`, `Capítulo 3: Execução Ágil (Ciclo Micro-Adaptativo)` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._