# GP-PME: Framework de Governança de TI para PMEs - Documento Mestre Consolidado

**Autor**: Antigravity AI (sob a direção de Andre Victor)
**Versão**: 5.2 (Consolidada - Filosofia TI Enxuta Integrada)
**Data**: 02 de Junho de 2026

---

## Resumo Executivo

O **GP-PME (Governança Prática para Pequenas e Médias Empresas)** é um framework de Governança e Gestão de TI integrado, enxuto e adaptativo, desenhado especificamente para suprir as dores operacionais e riscos cibernéticos enfrentados por PMEs. Através da arquitetura modular do **"Iceberg Invertido"**, o framework destila e simplifica as normas globais mais reconhecidas de governança e infraestrutura crítica (ISO/IEC 38500:2024, COBIT 2019, ITIL 4, NIST CSF 2.0 e CIS Controls v8) em processos simples e de baixíssimo overhead operacional.

---

## 1. O Diferencial Comercial: A Filosofia da TI Enxuta

O principal diferencial comercial do GP-PME em relação aos grandes frameworks de mercado (como COBIT e ITIL corporativos) é a **Filosofia da TI Enxuta**. Enquanto os modelos tradicionais exigem departamentos de conformidade inteiros e geram custos burocráticos inviáveis para PMEs, o GP-PME reconhece que o framework deve se adaptar ao tamanho da equipe, e não o contrário. 

A TI Enxuta empodera a equipe técnica reduzida—frequentemente composta por um único profissional (*One-Man-Band*)—a transitar de um "faz-tudo" reativo para um **Orquestrador de Valor** e, eventualmente, parceiro estratégico do negócio (**Chief Innovation Officer**).

### A Jornada de Evolução da TI Enxuta:
```
[ TÉCNICO FAZ-TUDO ] -> Opera em reatividade, estresse e caos operacional.
        |
        v (Fase 1: Ativação do Módulo de Incidentes e Kanban / Opcional IA)
[ ORQUESTRADOR DE VALOR ] -> Caos organizado, tempo liberado (até 80% em FAQs).
        |
        v (Fase 2: Laboratório de Inovação e ciclo de MVP de 2 semanas)
[ AGENTE DE MUDANÇA ] -> Prototipagem rápida e inovações de baixíssimo custo.
        |
        v (Fase 3: CD-TI Lite quinzenal / semanal como bússola de crescimento)
[ PARCEIRO ESTRATÉGICO ] -> Lidera a tecnologia alinhada ao faturamento e risco.
```

---

## 2. Capítulo 1: Arquitetura Geral do GP-PME e Princípios Fundamentais

### 2.1. O Modelo "Iceberg Invertido" e a Modularidade para Leigos
O framework GP-PME é concebido sob o modelo do **Iceberg Invertido**. Na superfície, apresenta ferramentas de acessibilidade imediata e rápida injeção de valor (*Quick Wins*):

```
                   A PONTA DO ICEBERG (Acessibilidade Imediata)
                  - Fase Zero: Playbook Salva-Vidas de 30 Dias
                  - Mapeamento Manual de Canais de Suporte
                  - Kanban de TI de 4 Colunas
     -----------------------------------------------------------------
                   O CORPO DO ICEBERG (Extensão Modular)
                  - Pilar I: ADM-Lite (CD-TI Lite e 4 Quadrantes)
                  - Pilar II: Execução Ágil (PRD e MVP)
                  - Pilar III: NIST-Lite (Inventário 80/20, Backups, PRI)
     -----------------------------------------------------------------
                   A BASE DO ICEBERG (Opcionais e Métricas)
                  - Pilar IV: Aceleração por IA (Agentes e Prompts)
                  - Pilar V: Métricas Avançadas (DAN e COT)
```

Essa modularidade garante que a PME possa evoluir no seu próprio ritmo, sem sobrecarga ou necessidade de aportes financeiros iniciais elevados.

---

## 3. Capítulo 2: Pilar I: Governança Essencial (ADM-Lite)

Focado em alinhar a TI com a estratégia de negócio do CEO de forma enxuta e puramente manual:

### 3.1. O Ciclo ADM-Lite (Manual)
*   **Avaliar (A)**: O CEO e o Gestor de TI avaliam quinzenalmente o andamento da tecnologia contra as metas de vendas e custos.
*   **Dirigir (D)**: As decisões e verbas são direcionadas utilizando a **Matriz 4 Quadrantes**.
*   **Monitorar (M)**: O desempenho geral é medido através do acompanhamento manual dos **3 KPIs Visíveis**.

### 3.2. O Ritual CD-TI Lite (A Bússola do Crescimento Seguro)
Reunião executiva quinzenal ou mensal de **30 minutos**, com pauta e tempo rígidos. Em vez de discutir detalhes técnicos de cabos e servidores, a governança atua como uma bússola de crescimento baseada em resultados concretos (horas salvas, satisfação de clientes e perdas evitadas):
1.  **Revisão dos KPIs (5 minutos)**: Análise do Uptime e agilidade do suporte da última quinzena.
2.  **Alinhamento Estratégico (15 minutos)**: Monitoramento de cartões na Matriz 4 Quadrantes.
3.  **Decisões e Prioridades (10 minutos)**: Aprovação rápida de verbas e encerramento.

### 3.3. Artefatos Manuais Chave
*   **Matriz de Responsabilidades Simplificada (RACI-Lite)**: Tabela de 1 página contendo quem executa (R) e quem aprova (A) cada tarefa de TI.
*   **Matriz 4 Quadrantes**: Painel de alinhamento visual de 1 página conectando metas comerciais e financeiras aos cartões de prioridade de TI.
*   **3 KPIs Visíveis**:
    1.  *IDSC (Índice de Disponibilidade de Serviços Críticos)*: Meta **> 99.5%**.
    2.  *TMpR (Tempo Médio para Resolução)*.
    3.  *ISU (Índice de Satisfação do Usuário)*: Meta **> 4.5/5.0**.

---

## 4. Capítulo 3: Pilar II: Execução Ágil (Ciclo de Serviço Micro-Adaptativo)

Operacionaliza a gestão das solicitações diárias de suporte e projetos na PME. É a materialização da **Fase 1 (Orquestração do Valor)** e **Fase 2 (Laboratório de Inovação)**:

### 4.1. Fluxo de Trabalho Kanban
*   **Quadro Kanban Manual**: Quadro físico de cartões (post-its) ou digital simples, dividido nas colunas: *A Fazer*, *Em Andamento*, *Em Teste / Validação*, e *Concluído*.
*   **Limite de Trabalho em Progresso (WIP)**: Estipulado em no máximo **3 tarefas simultâneas** por técnico, evitando sobrecarga e garantindo foco.

### 4.2. Atendimento e Suporte
*   **Canal Único de Suporte**: Um ponto de entrada unificado para recebimento de solicitações (ex: um formulário simples ou e-mail de suporte dedicado), eliminando chamados informais dispersos.
*   **Matriz de Priorização Urgência vs. Impacto**: Matriz lógica para classificar chamados baseados na parada de faturamento ou de setores.

### 4.3. Desenvolvimento de Soluções e Laboratório de Inovação
*   **PRD Simplificado**: Documento padrão de 1 página para especificação de requisitos funcionais de software ou aquisições.
*   **MVP (Produto Mínimo Viável)**: Desenvolvimento da versão mais simples de uma funcionalidade em no máximo **2 semanas**, implantando imediatamente em um grupo controlado de usuários (*piloto de inovação*) para coletar feedbacks rápidos sem desperdício de tempo e recursos.

---

## 5. Capítulo 4: Pilar III: Segurança Crítica (NIST-Lite)

Proteção essencial dos dados e sistemas baseando-se em controles binários manuais de baixo custo, garantindo que o crescimento acelerado da PME seja seguro:

### 5.1. Os 4 Controles Críticos Mínimos
1.  **Inventário 80/20 de Ativos Críticos**: Planilha contendo o mapeamento dos 20% de softwares, notebooks de diretores e bancos de dados que geram 80% do faturamento da empresa.
2.  **Princípio do Privilégio Mínimo (LUA)**: Remoção sistemática de acessos de administrador local dos colaboradores nos computadores e ativação mandatória de MFA (Autenticação de Dois Fatores).
3.  **Backups Automatizados e Testados**: Configuração de backups diários automáticos para a nuvem de dados essenciais, contendo rotinas de testes manuais trimestrais de restauração concluídos em menos de 30 minutos.
4.  **Plano de Resposta a Incidentes (PRI) de 1 Página**: Folha física impressa fixada na TI listando os contatos de emergência e os 3 passos imediatos de contenção (ex: desplugar cabos de rede) caso a empresa sofra um ataque de ransomware ou vírus.

---

## 6. Capítulo 5: Métricas Avançadas (DAN e COT)

Quantifica a saúde técnica e financeira da TI da PME, servindo de elo de diálogo com o financeiro:

### 6.1. Dívida de Arquitetura Normalizada (DAN)
Expressa a proporção acumulada de passivos tecnológicos (gargalos técnicos e sistemas sem suporte) em relação ao orçamento disponível na PME:

$$\text{DAN} = \frac{\text{Custo Estimado de Refatoração da Dívida Técnica (Horas Técnicas $\times$ Custo-Hora)}}{\text{Orçamento Anual de TI da PME}}$$

*   **Zonas de Risco**:
    *   *DAN < 0.15*: Saudável. Baixa complexidade e alta agilidade.
    *   *0.15 $\le$ DAN $\le$ 0.35*: Alerta. Gargalos de arquitetura começam a atrasar projetos comerciais.
    *   *DAN > 0.35*: Crítico. Alto risco de parada geral de faturamento; exige injeção imediata de COT.

### 6.2. Custo da Otimização Tecnológica (COT)
Representa o aporte de verbas focado na redução da dívida técnica de arquitetura (reduzir o DAN), migrações de nuvem ou automações. O gestor calcula o ROI da otimização relacionando a redução de custos de horas de parada operacional evitadas em relação ao investimento aportado.

---

## 7. Capítulo 6: Pilar IV: Aceleração com IA (Habilitador Opcional)

A Inteligência Artificial atua como um multiplicador de produtividade do *One-Man-Band*, operando sob regras rígidas para garantir conformidade profissional de mercado:

### 7.1. Os 4 Subagentes Especialistas de IA
1.  **Orquestrador Estratégico (ADM-Lite)**: Gera briefings, pautas e resumos de performance para a reunião quinzenal CD-TI Lite.
2.  **Analista de Execução Ágil (Scrum/ITIL)**: Auxilia no desdobramento de demandas no Kanban e gera rascunhos de PRDs Simplificados em formato Markdown.
3.  **Guardião de Segurança (NIST-Lite)**: Sugere melhorias em checklists de backups, audita políticas de MFA e analisa logs de logs em busca de anomalias.
4.  **Engenheiro de Prompts e Métricas (DAN/COT)**: Realiza os cálculos do DAN, simula ROI de projetos de infraestrutura e executa auditoria de alucinações técnicas.

### 7.2. Protocolo de Tratamento de Alucinações (Alucination Treatment Protocol)
*   **Ancoragem de Contexto (Grounding)**: Toda e qualquer saída dos agentes deve ser ancorada na base de dados reais da PME e nas referências metodológicas dos guias locais.
*   **Human-in-the-loop (HITL)**: Proibição de executar ações em produção geradas autonomamente por IAs. O Gestor de TI humano deve revisar, validar e assinar todas as especificações geradas pela IA.
*   **Controle de Gaps**: Se informações técnicas cruciais forem omitidas no prompt, o agente deve se abster de inventar e sinalizar o gap explicitamente como uma pendência no final do documento gerado.

---

## Referências Bibliográficas

*   **[1]** ISO/IEC 38500:2024. *Information technology — Governance of IT for the organization*.
*   **[2]** ISACA. (2019). *COBIT 2019 Framework: Governance and Management Objectives*.
*   **[3]** Axelos. (2019). *ITIL Foundation: ITIL 4 edition*.
*   **[4]** NIST. (2024). *NIST Cybersecurity Framework (CSF) 2.0*.
*   **[5]** CIS. (2023). *CIS Controls Version 8: A Community Defense Guide*.
*   **[6]** Verdecchia, R. (2022). *Empirical evaluation of an architectural technical debt index in software-intensive systems*.
