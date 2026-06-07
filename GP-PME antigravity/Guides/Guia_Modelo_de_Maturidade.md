# Guia do Modelo e Matriz de Maturidade GP-PME

**Autor**: Antigravity AI (sob a direção de Andre Victor)  
**Versão**: 1.0 (Oficial - Filosofia TI Enxuta Integrada)  
**Data**: 02 de Junho de 2026  

---

## 1. O que é e por que existe o Modelo de Maturidade GP-PME?

O **Modelo de Maturidade GP-PME** é uma ferramenta de autoavaliação e direcionamento estratégico concebida para Pequenas e Médias Empresas (PMEs). A sua existência justifica-se pelo fato de que a governança de TI não deve ser implementada de forma abrupta, sob o risco de gerar rejeição cultural, burocracia excessiva e desperdício de recursos. Em vez disso, a evolução da TI deve ser **incremental, modular e adaptada ao tamanho da equipe**, em perfeita sintonia com a **Filosofia da TI Enxuta**.

### 1.1. Metadados do Processo
*   **O que é**: Um roteiro evolutivo estruturado em 5 níveis (0 a 4) e uma matriz operacional que cruza os 4 Pilares do GP-PME para medir o estágio de desenvolvimento da TI.
*   **Por que existe**: Para eliminar a reatividade ("apagar incêndios") de forma segura, orientando o profissional de TI a transitar de *Faz-tudo* para *Orquestrador de Valor* e, futuramente, *Parceiro Estratégico*.
*   **Quando deve ser usado**: 
    1.  No início da adoção (Dia 1 da Fase Zero) para estabelecer o baseline de diagnóstico.
    2.  Ao final de cada fase de implantação (ex: retrospectiva de 30 dias) para validar a transição de nível.
    3.  A cada 6 meses (durante o CD-TI Lite) como auditoria de melhoria contínua.
*   **Quem é o dono**: O **Gestor de TI** (como Orquestrador de Valor), com aprovação e supervisão do **CEO/Dono da PME** na reunião do CD-TI Lite.
*   **Inputs necessários**: Respostas do Questionário de Maturidade, dados operacionais do Kanban (tempo de resolução), relatórios de conformidade de backup e segurança.
*   **Outputs produzidos**: Índice de Maturidade da TI (IM-TI), Plano de Ação de Transição de Fase, Ata de Homologação de Maturidade assinada pelo CEO.
*   **Como o sucesso é medido**: Pelo aumento consistente do Índice de Maturidade (IM-TI) associado à redução do DAN (Dívida de Arquitetura) e aumento do IDSC (uptime de serviços críticos).

---

## 2. A Jornada da TI Enxuta: Os 5 Níveis de Maturidade

O modelo de evolução do GP-PME estabelece marcos claros para guiar a TI da PME do caos à adaptabilidade inteligente.

```
+------------------+     +-----------------------+     +------------------------+     +--------------------------+     +----------------------------+
| NÍVEL 0: CAÓTICO | --> | NÍVEL 1: REATIVO ORG. | --> | NÍVEL 2: GOV. BÁSICA   | --> | NÍVEL 3: INOVAÇÃO INCREM.| --> | NÍVEL 4: GOV. ADAPTATIVA   |
| (Apaga-incêndios)|     | (Caos Controlado)     |     | (Alinhamento e Risco)  |     | (Pragmatismo e Valor)    |     | (IA e Escala com HITL)     |
+------------------+     +-----------------------+     +------------------------+     +--------------------------+     +----------------------------+
```

### Nível 0: Caótico (Inexistente / Ad-hoc)
*   **Características**: A TI opera em modo puramente reativo. O profissional é um "faz-tudo" sobrecarregado e estressado. As solicitações chegam de forma desordenada (WhatsApp, e-mails, conversas de corredor). Não há visibilidade sobre os custos de TI, e o risco de parada geral de faturamento por falhas ou vírus é extremamente alto.
*   **Foco Principal**: Sobrevivência e contenção do caos visível.

### Nível 1: Reativo Organizado (Estabilizado)
*   **Características**: A operação do dia a dia foi estruturada. Todas as solicitações são centralizadas em um **Canal Único** e acompanhadas visualmente no **Kanban de 4 Colunas**, respeitando o limite de tarefas em andamento (WIP Limit de 3). FAQs básicas de suporte estão disponíveis, reduzindo a carga do técnico.
*   **Foco Principal**: Organização de demandas e liberação de capacidade produtiva.

### Nível 2: Governança Básica (Alinhado)
*   **Características**: A TI passa a dialogar com o negócio através do comitê **CD-TI Lite** (reuniões quinzenais de 30 minutos) e da **Matriz 4 Quadrantes**. A segurança essencial foi blindada: o **Inventário 80/20** de ativos críticos foi mapeado, os **backups 3-2-1** são automáticos e testados trimestralmente, e o **PRI** (Plano de Resposta a Incidentes) está na parede.
*   **Foco Principal**: Alinhamento estratégico e mitigação de riscos cibernéticos críticos.

### Nível 3: Inovação Incremental (Proativo / Motor de Valor)
*   **Características**: A TI executa projetos rápidos de desenvolvimento ou automação com foco em retorno direto. O ciclo **Ideia-MVP-Feedback** de 2 semanas está rodando, utilizando **PRDs Simplificados**. O profissional de TI mede sistematicamente a saúde financeira e técnica da infraestrutura usando os índices **DAN** (Dívida de Arquitetura Normalizada) e **COT** (Custo de Otimização).
*   **Foco Principal**: Geração de valor comercial rápido e redução de débitos técnicos.

### Nível 4: Governança Adaptativa (Otimizado / Inteligente)
*   **Características**: A Inteligência Artificial atua como copiloto transversal em todos os processos da empresa de forma formalizada. Os **4 Agentes Especialistas de IA** realizam triagem, geração de PRDs, monitoramento de riscos e cálculos do DAN. Aplica-se rigorosamente o **Protocolo HITL (Human-in-the-Loop)** para evitar alucinações de IA. Há um planejamento de transição de arquitetura de longo prazo (Escalabilidade).
*   **Foco Principal**: Automação avançada sem overhead e inteligência distribuída.

---

## 3. A Matriz de Maturidade GP-PME

A matriz abaixo detalha os requisitos práticos esperados para cada Pilar em cada nível de maturidade, servindo como referencial objetivo de auditoria.

| Pilar | Nível 0 (Caótico) | Nível 1 (Reativo Organizado) | Nível 2 (Governança Básica) | Nível 3 (Inovação Incremental) | Nível 4 (Governança Adaptativa) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Pilar I:<br>Governança Essencial<br>(ADM-Lite)** | **Características**: Sem fórum de decisões; TI vista apenas como despesa técnica.<br>**Inputs**: Reclamações.<br>**Saídas**: Nenhuma.<br>**Métricas**: Nenhuma. | **Características**: KPIs basais começam a ser medidos para comprovar valor.<br>**Inputs**: Chamados Kanban.<br>**Saídas**: Relatórios operacionais básicos.<br>**Métricas**: TMpR basal. | **Características**: CD-TI Lite quinzenal ativo; Matriz 4 Quadrantes orienta verbas.<br>**Inputs**: Planilha de 3 KPIs, Matriz 4Q.<br>**Saídas**: Atas CD-TI Lite, RACI-Lite.<br>**Métricas**: IDSC (>99.5%), ISU (>4.5), TMpR. | **Características**: Reuniões integradas com orçamento de inovação e análise DAN.<br>**Inputs**: Indicador DAN, Propostas COT.<br>**Saídas**: Roadmap de Inovação.<br>**Métricas**: ROI de Otimização. | **Características**: CD-TI Lite auxiliado por IA; governança integrada ao plano de fusões ou escala.<br>**Inputs**: Briefings gerados por IA.<br>**Saídas**: Plano de Arquitetura Futura.<br>**Métricas**: DAN < 0.15 estável. |
| **Pilar II:<br>Execução Ágil** | **Características**: Caos operacional; chamados por canais dispersos (WhatsApp).<br>**Inputs**: Pedidos verbais.<br>**Saídas**: Nenhuma.<br>**Métricas**: Nenhuma. | **Características**: Canal Único ativo; Kanban de 4 colunas; WIP Limit = 3 ativo.<br>**Inputs**: Tickets Canal Único.<br>**Saídas**: Cartões Kanban resolvidos.<br>**Métricas**: Tempo de Ciclo operacional. | **Características**: Priorização no Kanban baseada em Impacto vs Urgência.<br>**Inputs**: Chamados classificados.<br>**Saídas**: Quadro Kanban limpo.<br>**Métricas**: TMpR sob controle. | **Características**: Ciclo MVP de 2 semanas; PRD Simplificado para novos recursos.<br>**Inputs**: Ideias de Negócio.<br>**Saídas**: PRDs de 1 pág, MVPs lançados.<br>**Métricas**: Redução do Time-to-Market. | **Características**: PRDs e códigos de MVPs acelerados por IA com crivo HITL.<br>**Inputs**: Prompts de PRD/Código.<br>**Saídas**: Protótipos funcionais ágeis.<br>**Métricas**: Taxa Eficiência IA (TEIA > 60%). |
| **Pilar III:<br>Segurança Crítica<br>(NIST-Lite)** | **Características**: Vulnerabilidade extrema; backups manuais e não testados.<br>**Inputs**: Nenhum.<br>**Saídas**: Nenhuma.<br>**Métricas**: Nenhuma. | **Características**: Backups em nuvem diários ativos; privilégios de admin revisados.<br>**Inputs**: Logs de Backup.<br>**Saídas**: Planilha de controle.<br>**Métricas**: Taxa de Sucesso do Job. | **Características**: Inventário 80/20 ativo; Backups 3-2-1 com teste trimestral DR < 30min; PRI 1 pág.<br>**Inputs**: Inventário 80/20, PRI.<br>**Saídas**: Logs de Teste de DR, PRI assinado.<br>**Métricas**: Tempo de Restauração (RTO). | **Características**: Controles automatizados de MFA mandatórios; gestão de vulnerabilidades.<br>**Inputs**: Relatórios de scanner de rede.<br>**Saídas**: Plano de Mitigação.<br>**Métricas**: CVEs críticas mitigadas = 100%. | **Características**: NIST Privacy implementado; monitoramento de conformidade automatizado.<br>**Inputs**: Logs de Segurança.<br>**Saídas**: Auditoria automatizada.<br>**Métricas**: Zero vazamentos / zero paradas. |
| **Pilar IV:<br>Engenharia de Prompts e IA<br>(Opcional / Acelerador)** | **Características**: Ausência de uso de IA, ou uso ad-hoc pessoal sem governança.<br>**Inputs**: Nenhum.<br>**Saídas**: Nenhuma.<br>**Métricas**: Nenhuma. | **Características**: FAQ manual disponibilizada; chatbot simples de triagem Nível 1.<br>**Inputs**: FAQ em Markdown.<br>**Saídas**: Respostas do chatbot.<br>**Métricas**: % Desvio de chamados (>40%). | **Características**: Prompts canônicos para suporte e triagem usados pelo técnico.<br>**Inputs**: Prompts de suporte.<br>**Saídas**: Instruções de ticket.<br>**Métricas**: Tempo de triagem. | **Características**: Prompt Chaining estruturado para PRD, código e planos de teste.<br>**Inputs**: Biblioteca de Prompts (BPE).<br>**Saídas**: Esboços estruturados.<br>**Métricas**: Tempo de escrita de PRDs. | **Características**: 4 Agentes Especialistas de IA instanciados e operando sob protocolo HITL.<br>**Inputs**: Dados brutos do Kanban/Negócio.<br>**Saídas**: Briefings, PRDs, Análises.<br>**Métricas**: Acurácia das saídas da IA (100% auditadas). |

---

## 4. Questionário de Autoavaliação de Maturidade GP-PME

Este questionário rápido contém 10 perguntas binárias (Sim/Não) para mapear o estágio de maturidade da PME. Cada resposta "Sim" deve ser suportada por evidência concreta (ex: planilha de backups testados, quadro Kanban ativo).

### O Questionário
1.  **[ ] Canal Único**: A TI possui um único canal formalizado para receber solicitações de suporte e projetos, tendo erradicado os chamados informais (WhatsApp pessoal, conversas)?
2.  **[ ] Kanban Ativo**: Existe um quadro Kanban de 4 colunas (*A Fazer, Em Andamento, Em Teste, Concluído*) ativo, com limite de trabalho em andamento (WIP Limit de no máximo 3 tarefas por técnico)?
3.  **[ ] FAQs Operacionais**: A PME disponibiliza um documento de FAQ ou um chatbot de triagem que resolve autonomamente mais de 40% das dúvidas básicas dos colaboradores?
4.  **[ ] CD-TI Lite**: O CEO e o Gestor de TI realizam reuniões de 30 minutos periodicamente (quinzenal ou mensal) para revisar métricas e aprovar verbas estratégicas?
5.  **[ ] Matriz 4 Quadrantes**: A TI utiliza a Matriz 4 Quadrantes para planejar e priorizar todas as iniciativas com base no impacto no faturamento e despesas do negócio?
6.  **[ ] Inventário 80/20**: A empresa possui uma planilha atualizada contendo os 20% de ativos tecnológicos mais críticos que representam 80% do risco operacional?
7.  **[ ] Backups Testados**: A PME possui backups automáticos em nuvem e **realizou com sucesso um teste físico de restauração** em menos de 30 minutos no último trimestre?
8.  **[ ] PRI de 1 Página**: Existe um Plano de Resposta a Incidentes (PRI) de 1 página, assinado pelo CEO e impresso na sala de TI com contatos emergenciais e etapas de isolamento físico?
9.  **[ ] Métricas DAN/COT**: O gestor calcula e apresenta ao CD-TI Lite o índice DAN (Dívida de Arquitetura) e o ROI do COT (Custo de Otimização)?
10. **[ ] Auditoria HITL (IA)**: Caso utilize ferramentas de IA para gerar código ou documentos, a PME possui um checklist de auditoria de alucinações (HITL) que impede saídas de IA de irem para produção sem revisão?

### Cálculo do Índice de Maturidade da TI (IM-TI)
Some a quantidade de respostas **Sim** (1 ponto por resposta):

*   **0 a 2 pontos**: **Nível 0 - Caótico**. (Urgente: implantar Fase Zero do GP-PME).
*   **3 a 5 pontos**: **Nível 1 - Reativo Organizado**. (O caos operacional foi controlado, focar em segurança essencial e governança de alinhamento).
*   **6 a 8 pontos**: **Nível 2 - Governança Básica**. (Operação segura e alinhada. Pronto para buscar inovação e ciclos de MVP).
*   **9 pontos**: **Nível 3 - Inovação Incremental**. (TI ágil, proativa, orientada a valor comercial e controle de débitos técnicos).
*   **10 pontos**: **Nível 4 - Governança Adaptativa**. (Excelência operacional acelerada por IA sob estrito controle humano).

---

## 5. Checklists de Transição de Nível (Evolução Contínua)

Use estes checklists para estruturar os planos de ação e avançar nos degraus de maturidade da governança.

### 5.1. Transição: Nível 0 (Caótico) -> Nível 1 (Reativo Organizado)
*   [ ] Unificar todos os chamados em um único formulário ou e-mail de suporte.
*   [ ] Ativar um quadro Kanban (digital ou físico) com 4 colunas estritas.
*   [ ] Estipular o WIP Limit = 3 no Kanban.
*   [ ] Redigir a FAQ inicial de 5 itens para os problemas recorrentes.
*   [ ] Registrar a primeira métrica de tempo médio de suporte (TMpR baseline).

### 5.2. Transição: Nível 1 (Reativo Organizado) -> Nível 2 (Governança Básica)
*   [ ] Bloquear a agenda do CEO quinzenalmente para reuniões de 30 min (CD-TI Lite).
*   [ ] Preencher a Matriz 4 Quadrantes alinhada aos objetivos de receita e redução de custos do CEO.
*   [ ] Mapear o Inventário 80/20 de ativos críticos na planilha.
*   [ ] Ativar backup diário em nuvem para os ativos críticos e realizar teste físico de restauração.
*   [ ] Imprimir e colar na parede da TI o Plano de Resposta a Incidentes (PRI) de 1 página.

### 5.3. Transição: Nível 2 (Governança Básica) -> Nível 3 (Inovação Incremental)
*   [ ] Lançar o primeiro ciclo MVP de 2 semanas de inovação (ex: automação de relatórios).
*   [ ] Padronizar o preenchimento de PRDs Simplificados para novas demandas.
*   [ ] Realizar o cálculo da Dívida de Arquitetura Normalizada (DAN) e propor otimizações com base no ROI.
*   [ ] Homologar uma biblioteca de prompts canônicos compartilhada na TI para agilizar documentações.

### 5.4. Transição: Nível 3 (Inovação Incremental) -> Nível 4 (Governança Adaptativa)
*   [ ] Instanciar os 4 Agentes Especialistas de IA (Orquestrador, Analista, Guardião, Auditor).
*   [ ] Institucionalizar o uso de prompts de contexto e restrições para evitar alucinações.
*   [ ] Aplicar o checklist de auditoria humana (HITL) para 100% dos outputs gerados por IA.
*   [ ] Desenhar e aprovar no CD-TI Lite o plano de transição de infraestrutura elástica de longo prazo.
