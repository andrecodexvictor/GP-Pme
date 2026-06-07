# Guia do Pilar 2: Execução Ágil (Ciclo de Serviço Micro-Adaptativo)

**Autor**: Antigravity AI (sob a direção de Andre Victor)
**Versão**: 5.2 (Consolidada - Filosofia TI Enxuta Integrada)
**Data**: 02 de Junho de 2026

---

## 1. Introdução ao Pilar 2: Execução Ágil

O Pilar 2 foca na **Gestão de TI**, traduzindo as prioridades estratégicas da Governança (Pilar 1) em ações e entregas semanais rápidas. Ele destila os conceitos do **ITIL 4** para gestão de serviços de TI e as práticas do **Scrum** para desenvolvimento de projetos de forma adaptável, criando o **Ciclo de Serviço Micro-Adaptativo**.

### A Execução na TI Enxuta
Na TI Enxuta, a execução é dividida em etapas evolutivas fundamentais para empoderar o time técnico e entregar inovação real sem investimentos massivos:

*   **Fase 1: Orquestração do Valor e Fim do Caos**:
    Em equipes pequenas ou com um único profissional (*One-Man-Band*), a prioridade número um é organizar o caos do cotidiano. Em vez de implementar metodologias complexas de uma só vez, a adoção é estritamente modular. Ativa-se primeiro o **Módulo de Gestão de Incidentes e Requisitos** por meio de um Canal Único e um Quadro Kanban. Isso centraliza e organiza o fluxo de trabalho, eliminando planilhas fragmentadas e chamados informais via WhatsApp ou e-mail, liberando tempo valioso para atividades de maior impacto.
*   **Fase 2: O Laboratório de Inovação e o Ciclo "One-Man-Band"**:
    Com a rotina estabilizada e tempo livre (até 80% do tempo de atendimento rotineiro economizado), o profissional de TI passa a atuar como o principal motor de inovação da PME. A inovação não exige projetos gigantescos e caros; ela acontece em um **Laboratório de Baixo Risco**, desenvolvendo **Pilotos de Inovação** (pequenas funcionalidades ou automações internas focadas, por exemplo, em otimizar as vendas ou o financeiro) através de ciclos curtos de **2 semanas (MVP)** baseados no feedback contínuo dos usuários.

Este pilar opera de forma **100% manual**, utilizando quadros visuais simples, formulários unificados e testes pragmáticos que dispensam softwares caros. A Inteligência Artificial Generativa pode ser incorporada de forma opcional como um assistente de documentação de requisitos e gerador de especificações.

---

## 2. O Ciclo de Serviço Micro-Adaptativo (Scrum + ITIL Lite)

O **Ciclo de Serviço Micro-Adaptativo** é o motor de execução ágil do GP-PME. Ele resolve o paradoxo clássico da TI em PMEs: como executar projetos estratégicos de inovação quando a rotina diária é inundada de incidentes de suporte urgentes? 

### 2.1. Metadados do Ciclo Micro-Adaptativo
*   **O que é**: Um processo adaptável de desenvolvimento e suporte que concilia o desenvolvimento de projetos (Scrum) com o suporte diário (ITIL 4) em ciclos curtos de trabalho, sem gerar overhead administrativo.
*   **Por que existe**: Para permitir que equipes de TI reduzidas (ou *One-Man-Band*) operem de forma organizada e adaptativa, absorvendo incidentes sem comprometer o planejamento estratégico e sem gerar estresse operacional.
*   **Quando deve ser usado**: Diariamente para gerenciar o fluxo de chamados e semanalmente para planejar e revisar as entregas operacionais.
*   **Quem é o dono**: O **Gestor de TI** (Orquestrador de Valor).
*   **Inputs**: Solicitações do Canal Único de Suporte e prioridades do CD-TI Lite (Matriz 4 Quadrantes).
*   **Outputs**: Cartões Kanban concluídos, novos MVPs testados de 2 semanas, incidentes mitigados.
*   **Como o sucesso é medido**: Pela taxa de cumprimento da Sprint (>80% dos cartões planejados entregues) e pelo Tempo Médio para Resolução (TMpR).

---

### 2.2. A Mecânica Prática de Funcionamento

O ciclo micro-adaptativo opera através de engrenagens simples que se adaptam dinamicamente às interrupções cotidianas:

```
+---------------------------------------------------------------------------------+
|                              CADÊNCIA SEMANAL (SPRINTS)                         |
|  Planejamento (15 min) -> Execução com WIP Limit (3) -> Retrospectiva (15 min) |
+---------------------------------------------------------------------------------+
                                         |
                                         v
+---------------------------------------------------------------------------------+
|                       TRATAMENTO DINÂMICO DE INTERRUPÇÕES                       |
|   Chamado Urgente?                                                              |
|   -> SIM: Ativar "Raia Rápida" (Expedite) -> Suspender menor WIP -> Resolver.    |
|   -> NÃO: Fica no Backlog "A Fazer" -> Aguarda a próxima Sprint.               |
+---------------------------------------------------------------------------------+
```

#### 1. Cadência de Sprint de 1 Semana
O trabalho é planejado em ciclos de apenas **1 semana**. Na segunda-feira de manhã, o técnico realiza um **Planejamento de 15 minutos**:
*   Revisa a coluna *A Fazer* no Kanban, alimentada pelas prioridades da Matriz 4 Quadrantes.
*   Seleciona no máximo **3 a 5 cartões** para serem entregues na semana (compromisso da Sprint).
*   Foca estritamente nesses itens.

#### 2. Checkpoint Diário de Auto-Alinhamento (5 minutos)
Substituindo a tradicional "reunião diária" do Scrum, em equipes de uma única pessoa, o profissional realiza um **checkpoint visual diário** de 5 minutos antes de iniciar as atividades:
*   *O que eu fiz ontem que moveu cartões para "Concluído"?*
*   *Em quais cartões vou trabalhar hoje?*
*   *Existe algum impedimento técnico ou falta de feedback de usuário?*

#### 3. Regra de Amortecimento de Incidentes e a "Raia Rápida (Expedite)"
Para que o planejamento da semana não seja destruído por problemas que surgem repentinamente, o técnico adota a **mecânica da Raia Rápida**:

*   **Interrupção Comum (Baixa/Média Prioridade)**:
    Se um colaborador solicita uma ajuda não urgente (ex: reconfigurar assinatura de e-mail), o chamado **não pode interromper** a tarefa atual. Ele é registrado no Canal Único, entra no fim do backlog da coluna *A Fazer* e será planejado na próxima semana. O técnico continua focado na tarefa em andamento.
*   **Interrupção Crítica (Emergência/Parada Geral)**:
    Se ocorre um incidente de nível *Crítico* (ex: banco de dados do ERP caiu ou ataque de vírus), o técnico deve interromper seu trabalho atual imediatamente, aplicando as seguintes etapas:
    1.  **Suspender a Tarefa Menos Crítica**: Escolha a tarefa atualmente "Em Andamento" com menor prioridade comercial.
    2.  **Devolver ao Backlog**: Mova esse cartão temporariamente de volta para a coluna *A Fazer*. Isso libera um espaço no limite de WIP (WIP Limit de 3).
    3.  **Ativar a Raia Rápida (Expedite)**: Coloque o cartão da emergência no topo do quadro (pode usar um cartão vermelho ou uma fita de destaque).
    4.  **Resolver a Crise**: Dedique 100% de esforço para mitigar o incidente.
    5.  **Restabelecer o Fluxo**: Assim que o incidente for resolvido e movido para *Concluído*, resgate a tarefa suspensa da coluna *A Fazer*, mova-a de volta para *Em Andamento* e continue o trabalho.

Essa mecânica impede a multitarefa (multitasking) crônica, que é o maior fator de perda de produtividade na TI de pequenas empresas, garantindo que as emergências sejam tratadas sem comprometer a organização e a visibilidade do Kanban.

---

## 3. Gestão do Fluxo de Trabalho (Kanban e Suporte Único)

### 3.1. Quadro Kanban de TI
O gerenciamento diário de todas as demandas (incidentes de suporte e melhorias) é feito visualmente em um quadro Kanban contendo 4 colunas estritas:

1.  **Backlog / A Fazer**: Demandas em espera, ordenadas de cima para baixo por prioridade do CD-TI Lite.
2.  **Em Andamento**: O que o técnico de TI está executando no momento.
    *   *Regra de Ouro (Manual)*: O limite de Trabalho em Progresso (**WIP - Work in Progress**) deve ser de **no máximo 3 tarefas simultâneas** por técnico, garantindo foco e rapidez no encerramento de pendências.
3.  **Em Teste**: Funcionalidades prontas aguardando a validação ou teste do usuário final solicitante.
4.  **Concluído**: Demandas devidamente testadas, implantadas em produção e com feedback assinado.

### 3.2. Canal Único de Suporte (Unificação)
Para eliminar a perda de chamados e o estresse operacional de solicitações dispersas em múltiplos chats (WhatsApp pessoal, e-mail pessoal, ligações), a PME deve utilizar um **ponto de entrada unificado obrigatório** (ex: formulário simples ou e-mail de suporte). O técnico só inicia chamados que estejam registrados no Canal Único, o qual gera automaticamente cartões para a coluna *A Fazer* do Kanban.

### 3.3. Matriz de Priorização (Eisenhower Adaptada)
Classificação ágil de chamados e solicitações com base no impacto real da TI no faturamento da empresa:

| Severidade de Impacto | Urgência Alta (Parada de Sistemas) | Urgência Média (Lentidão/Dificuldade) | Urgência Baixa (Dúvida/Estética) |
|:---|:---:|:---:|:---:|
| **Alto** (Para Faturamento/ERP) | **Crítico** (Fazer Agora) | **Alto** (Resolver hoje) | **Médio** (Agendar na Sprint) |
| **Médio** (Para Setor/Fila) | **Alto** (Resolver hoje) | **Médio** (Agendar na Sprint) | **Baixo** (Tratar no Backlog) |
| **Baixo** (Individual) | **Médio** (Agendar) | **Baixo** (Fila comum) | **Descarte** (Eliminar se sem valor) |

---

## 4. O Ciclo de Inovação "One-Man-Band" (Ideação, MVP e Feedback)

O profissional de TI orquestra sozinho o ciclo completo de entrega de valor comercial de forma enxuta:

```
[ IDEIA / DOR ] -> [ PRD SIMPLIFICADO ] -> [ MVP (MÁX 2 SEMANAS) ] -> [ PILOTO & FEEDBACK ]
```

### 4.1. PRD Simplificado
Para novos recursos ou aquisições tecnológicas, o Gestor de TI elabora um **Product Requirements Document (PRD) Simplificado** de apenas **1 página**, detalhando a dor de origem do solicitante, as histórias de usuário ("Como usuário, eu quero... para...") e os critérios de aceitação binários (passa / não passa). Isso evita escopos inchados e mal compreendidos.

### 4.2. Inovação Ideia-MVP-Feedback
Em vez de desenhar soluções perfeitas, caras e demoradas, o gestor de TI desenvolve a versão mais simples possível do recurso (**MVP - Produto Mínimo Viável**) em no máximo **2 semanas**, implantando-o como um **Piloto de Inovação** para um grupo controlado de usuários reais. O feedback é coletado imediatamente para validar o valor prático do projeto para os negócios e planejar melhorias incrementais.

---

## 5. Aceleração Opcional com Inteligência Artificial

Caso a PME adote o **Pilar IV (Aceleração por IA)**, o Gestor de TI pode acionar o **Agente 2: Analista de Execução Ágil (Scrum/ITIL)** para automatizar a burocracia do Pilar 2:

*   **Redação Automática de PRDs**: O gestor dita a dor de negócio (ex: "precisamos de um Pix nas maquininhas pois faltam moedas no caixa") e a IA especialista preenche instantaneamente o template oficial de PRD do GP-PME com histórias de usuário detalhadas e critérios binários.
*   **Prompt Chaining de Desenvolvimento**: A IA especialista encadeia prompts para acelerar entregas: o PRD gera histórias de usuário, que geram a estrutura de código base (*boilerplate*), que gera automaticamente os roteiros de planos de testes do MVP.
*   **HITL obrigatório**: O Gestor de TI humano deve revisar, validar as histórias e assinar os critérios de aceitação antes de os cartões entrarem em execução no Kanban.
