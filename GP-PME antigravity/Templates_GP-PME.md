# GP-PME Framework: Biblioteca de Templates Essenciais (Desacoplada)

Este documento consolida a biblioteca oficial de templates do framework **GP-PME**. Cada modelo foi otimizado para possuir no máximo 1 a 2 páginas, garantindo agilidade na aplicação diária por equipes de TI enxutas em pequenas e médias empresas.

**Diretrizes de Preenchimento Desacoplado**:
*   **Preenchimento Manual (Padrão)**: Siga as orientações em *Como preencher manualmente* utilizando planilhas locais, quadros brancos ou processadores de texto comuns.
*   **Aceleração Opcional com IA**: Caso decida utilizar o **Pilar IV (Aceleração por IA)**, copie e cole o *Prompt de Aceleração* fornecido em cada template no seu subagente especialista correspondente.

---

## Índice de Templates
1.  **Template 1**: Matriz de Responsabilidades Simplificada (RACI-Lite)
2.  **Template 2**: Matriz 4 Quadrantes de Alinhamento de TI
3.  **Template 3**: Dashboard de Monitoramento dos 3 KPIs Visíveis
4.  **Template 4**: Product Requirements Document (PRD) Simplificado
5.  **Template 5**: Matriz de Priorização (Urgência vs. Impacto)
6.  **Template 6**: Inventário 80/20 de Ativos Críticos
7.  **Template 7**: Plano de Resposta a Incidentes (PRI) de 1 Página
8.  **Template 8**: Avaliação e Matriz de Maturidade GP-PME

---

## Template 1: Matriz de Responsabilidades (RACI-Lite)

*   **Objetivo**: Definir responsabilidades para evitar gargalos operacionais e conflitos na PME.
*   **Legenda**:
    *   **R (Responsável)**: Quem executa a tarefa técnica.
    *   **A (Aprovador)**: Quem toma a decisão final e responde pelo resultado (apenas 1 por linha).
    *   **C (Consultado)**: Quem fornece informações de apoio antes da execução.
    *   **I (Informado)**: Quem recebe atualizações após a conclusão da atividade.

| Processo / Atividade | CEO / Dono | Gestor de TI | Gestor de Área | Técnico IA (Bot - Opcional) |
|:---|:---:|:---:|:---:|:---:|
| Definição do Orçamento Anual de TI | **A** | **R** | **C** | **I** |
| Priorização das Demandas no Kanban | **A** | **R** | **C** | **I** |
| Triagem Inicial de Incidentes (Nível 1) | **I** | **A** | **I** | **R** |
| Auditoria e Teste de Backup Crítico | **I** | **A** | **-** | **R** |
| Validação de PRD para Micro-Inovação | **C** | **A** | **R** | **I** |

*   **Como preencher manualmente**: Reúna-se com o técnico de TI por 15 minutos e preencha a tabela marcando as letras RACI correspondentes a cada atividade crítica da PME.
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Orquestrador Estratégico'. Com base na lista de cargos da minha PME [inserir cargos] e as principais atividades de TI [inserir atividades], preencha o template RACI-Lite recomendando a alocação ideal de responsabilidades (R, A, C, I).
    ```

---

## Template 2: Matriz 4 Quadrantes de Alinhamento de TI

*   **Objetivo**: Conectar as metas de faturamento e operação do CEO com as entregas de TI da quinzena.

```
+------------------------------------+------------------------------------+
|  QUADRANTE 1: INJEÇÃO DE RECEITA  |  QUADRANTE 2: REDUÇÃO DE CUSTOS   |
|                                    |                                    |
|  Metas do Negócio:                 |  Metas do Negócio:                 |
|  - [ex: Aumentar vendas em 10%]    |  - [ex: Reduzir TCO de TI em 8%]   |
|                                    |                                    |
|  Iniciativas de TI:                |  Iniciativas de TI:                |
|  - [ex: Pix automático nas maquinas]| - [ex: Desativar licenças ociosas] |
+------------------------------------+------------------------------------+
|  QUADRANTE 3: EXPERIÊNCIA CLIENTE  |   QUADRANTE 4: RESILIÊNCIA/RISCO   |
|                                    |                                    |
|  Metas do Negócio:                 |  Metas do Negócio:                 |
|  - [ex: Reduzir tempo de espera]   |  - [ex: Proteger contra vazamentos]|
|                                    |                                    |
|  Iniciativas de TI:                |  Iniciativas de TI:                |
|  - [ex: Chatbot automático Nível 1]| - [ex: Automatizar backup em nuvem]|
+------------------------------------+------------------------------------+
```

*   **Como preencher manualmente**: Desenhe este quadro na parede ou use uma planilha compartilhada. A cada quinzena (reunião CD-TI Lite), escreva as 4 metas prioritárias do CEO e as respectivas ações técnicas de TI que atendem a essas metas.
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Orquestrador Estratégico'. Receba minhas 4 metas de negócio [inserir metas] e sugira 1 iniciativa prática e de baixo custo de TI para cada quadrante da Matriz do GP-PME.
    ```

---

## Template 3: Dashboard de Monitoramento dos 3 KPIs Visíveis

*   **Objetivo**: Monitoramento rápido do desempenho operacional de TI na reunião CD-TI Lite.

```
=============================================================================
           DASHBOARD DE KPIs VISÍVEIS DE TI - [MÊS/ANO: ___/___]
=============================================================================

1. IDSC (Índice de Disponibilidade de Serviços Críticos)
   - Fórmula: [ (Tempo Total Operacional - Tempo de Queda) / Tempo Total ] * 100
   - Resultado do Mês: [ _____% ]  |  Meta: > 99.5%
   - Status: [  ] Saudável  [  ] Alerta  [  ] Crítico

2. TMpR (Tempo Médio para Resolução de Chamados)
   - Fórmula: Somatória do tempo de resolução / Nº total de chamados fechados
   - Resultado do Mês: [ _____ horas ]
   - Status: [  ] Em queda (Ótimo)  [  ] Estável  [  ] Em alta (Alerta)

3. ISU (Índice de Satisfação do Usuário Final)
   - Fórmula: Somatória das avaliações de chamados / Nº de avaliações recebidas
   - Resultado do Mês: [ _____ / 5.0 ]  |  Meta: > 4.5
   - Status: [  ] Saudável  [  ] Abaixo da Meta
=============================================================================
```

*   **Como preencher manualmente**: Ao final de cada mês, some as horas de funcionamento real dos servidores para obter o IDSC. Compute a média de horas de chamados resolvidos e a média das avaliações pós-chamados e anote os resultados nos colchetes.
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Engenheiro de Prompts e Métricas'. Com base nos dados brutos de incidentes e pesquisas da última quinzena [inserir dados], calcule automaticamente o IDSC, o TMpR e o ISU, gerando o relatório do dashboard formatado.
    ```

---

## Template 4: Product Requirements Document (PRD) Simplificado

*   **Objetivo**: Especificar demandas departamentais e projetos sem burocracia excessiva.

```markdown
# PRD [GP-PME]: [Nome da Funcionalidade / Automação]

## 1. Visão Geral e Justificativa de Negócio
*   **Data de Entrada**: ___/___/2026
*   **Solicitante**: [Nome do Gestor de Área]
*   **Problema de Negócio**: [Descreva a dor diária que está gerando custo ou perda de tempo]
*   **Objetivo do Recurso**: [O que pretendemos construir para solucionar e qual o ganho projetado]

## 2. Histórias de Usuário (User Stories)
*   **História 1**: Como [perfil do colaborador], eu quero [recurso técnico] para que eu possa [benefício prático].
*   **História 2**: Como [cliente final], eu quero [recurso técnico] para que eu possa [benefício prático].

## 3. Critérios de Aceitação (Passa / Não Passa)
*   [ ] **Critério 1**: Dado que [contexto inicial], quando [ação for executada], então [resultado esperado].
*   [ ] **Critério 2**: Dado que o usuário clica em "Confirmar", quando o sistema processar, então a tela exibe o comprovante em menos de 2 segundos.

## 4. Métricas de Negócio Afetadas (Vínculo com KPIs)
*   Este projeto impacta diretamente no indicador: [ex: TMpR do setor comercial ou IDSC do site].

---
*Validação do Gestor de TI (HITL): [  ] Aprovado  [  ] Necessita Ajuste*
*Assinatura do Aprovador: ____________________________*
```

*   **Como preencher manualmente**: Resuma em 1 página a funcionalidade solicitada descrevendo o problema, escrevendo manualmente as histórias de usuário com base no formato e definindo como testar (Critérios).
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Analista de Execução Ágil'. Com base na dor do meu cliente [inserir problema], elabore um PRD Simplificado contendo 3 Histórias de Usuário e critérios de aceitação no modelo 'Dado que, Quando, Então'. Lembre-se de respeitar o limite de 2 páginas e o protocolo contra alucinações.
    ```

---

## Template 5: Matriz de Priorização (Eisenhower Adaptada)

*   **Objetivo**: Classificação rápida de cartões e incidentes no Kanban.

| Severidade de Impacto | Urgência Alta (Parada Geral) | Urgência Média (Lentidão/Gargalo) | Urgência Baixa (Dúvida/Melhoria) |
|:---|:---:|:---:|:---:|
| **Impacto Alto** (Afeta Vendas) | **CRÍTICO** (Fazer Imediatamente) | **ALTO** (Resolver hoje) | **MÉDIO** (Agendar na Sprint) |
| **Impacto Médio** (Afeta Setor) | **ALTO** (Resolver hoje) | **MÉDIO** (Agendar na Sprint) | **BAIXO** (Tratar no Backlog) |
| **Impacto Baixo** (Individual) | **MÉDIO** (Agendar) | **BAIXO** (Fila comum) | **DESCARTE** (Eliminar se sem valor) |

---

## Template 6: Inventário 80/20 de Ativos Críticos

*   **Objetivo**: Identificar e registrar os ativos essenciais que representam 80% do risco cibernético da PME.

| ID | Nome do Ativo / Banco de Dados | Localização (Físico/Nuvem) | Criticidade (1 a 5) | Backup Ativo? (Sim/Não) | MFA Ativado? (Sim/Não) |
|:---:|:---|:---|:---:|:---:|:---:|
| 01 | Banco de Dados do ERP | Servidor Cloud AWS | **5** (Crítico) | Sim (Diário) | Sim |
| 02 | Planilha de Faturamento Mensal | Google Drive Finanças | **4** (Alto) | Sim (Semanal) | Sim |
| 03 | Notebook do Diretor Financeiro | Físico (Local) | **4** (Alto) | Sim | Sim |
| 04 | Sistema de Chamados de Suporte | Servidor Local | **3** (Médio) | Não | Não |

*   **Como preencher manualmente**: Liste em uma planilha os sistemas de rede, computadores de diretores e servidores de arquivos locais. Classifique a criticidade de 1 a 5. Foque a segurança nos de nível 4 e 5 (Inventário 80/20).
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Guardião de Segurança'. Com base no ecossistema técnico da minha PME [inserir sistemas], sugira a classificação de criticidade dos ativos para o Inventário 80/20 e audite se as rotinas de segurança padrão são suficientes.
    ```

---

## Template 7: Plano de Resposta a Incidentes (PRI) de 1 Página

*   **Objetivo**: Roteiro de ação rápida visual em momentos de crise de segurança.

```
=============================================================================
          PLANO DE RESPOSTA A INCIDENTES (PRI) - [NOME DA PME]
=============================================================================

[ PASSO 1: CONTENÇÃO IMEDIATA ]
-> Identificou atividade hacker ou vírus na máquina?
   1. DESCONECTE IMEDIATAMENTE O CABO DE REDE OU DESATIVE O WI-FI DO COMPUTADOR.
   2. Não desligue o computador da tomada (para preservar dados de análise forense).
   3. Avise imediatamente o Gestor de TI pelo ramal interno.

[ PASSO 2: ISOLAMENTO DO SERVIDOR ]
-> O Gestor de TI deve isolar o servidor afetado no painel da nuvem ou desconectar o switch físico local de rede para mitigar o alastramento na PME.

[ PASSO 3: COMUNICAÇÃO DE CONTATOS DE EMERGÊNCIA ]
-> Técnico de Infraestrutura Externo: [ Telefone: (__) _________ ]
-> Provedor de Cloud/ERP: [ Suporte Técnico Urgente: 0800-___-____ ]
-> CEO / Dono da Empresa: [ Contato Direto: (__) _________ ]

[ PASSO 4: RECUPERAÇÃO DE BACKUPS ]
-> Somente após a erradicação do malware, inicie a restauração das cópias de dados diárias mais recentes (conforme verificado no Inventário 80/20).

[ PASSO 5: RELATÓRIO PÓS-INCIDENTE ]
-> Apresentar relatório de causa raiz de 1 página na próxima reunião CD-TI Lite.
=============================================================================
```

*   **Como preencher manualmente**: Preencha manualmente os colchetes dos telefones e contatos de emergência. Imprima o roteiro de 1 página e cole em local visível na parede da sala de TI da PME.
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Guardião de Segurança'. Personalize o Plano de Resposta a Incidentes (PRI) de 1 Página gerando o checklist específico contendo etapas de isolamento para a infraestrutura de rede da minha PME [inserir infraestrutura].
    ```

---

## Template 8: Avaliação e Matriz de Maturidade GP-PME

*   **Objetivo**: Mensurar de forma prática e rápida o estágio atual da TI da PME, definindo o Índice de Maturidade da TI (IM-TI) e gerando o plano de ação de transição de fase.

*(Consulte o arquivo completo de diretrizes em [Guia_Modelo_de_Maturidade.md](file:///c:/Users/adm/Desktop/GP-PME%20framework/GP-PME%20antigravity/Guides/Guia_Modelo_de_Maturidade.md)).*

```
=============================================================================
          DIAGNÓSTICO E MATRIZ DE MATURIDADE GP-PME - AVALIAÇÃO
=============================================================================

[ QUESTIONÁRIO RÁPIDO - SIM / NÃO ]
1.  [ ] Canal Único de Suporte formalizado e ativo?
2.  [ ] Quadro Kanban ativo com limite WIP = 3?
3.  [ ] FAQs Nível 1 ativas com desvio de chamados > 40%?
4.  [ ]CD-TI Lite (reunião 30 min) quinzenal/mensal ativo?
5.  [ ] Matriz 4 Quadrantes priorizando projetos de TI?
6.  [ ] Inventário 80/20 de ativos críticos preenchido?
7.  [ ] Backups automáticos em nuvem testados (restauração < 30min)?
8.  [ ] PRI de 1 página assinado e colado na parede da TI?
9.  [ ] Indicador DAN e propostas de COT calculados?
10. [ ] Protocolo de Auditoria HITL ativo para saídas de IA?

IM-TI (Índice de Maturidade) = [ ____ / 10 ] pontos

NÍVEL DE MATURIDADE:
[  ] Nível 0: Caótico (0 a 2 pts)          [  ] Nível 3: Inovação (9 pts)
[  ] Nível 1: Reativo (3 a 5 pts)          [  ] Nível 4: Adaptativo (10 pts)
[  ] Nível 2: Gov. Básica (6 a 8 pts)

[ PLANO DE AÇÃO PARA TRANSIÇÃO DE NÍVEL ]
- Ação Prioritária 1 (Saneamento do ID __): __________________________
  Responsável: _____________ | Prazo: __/__/____
- Ação Prioritária 2 (Saneamento do ID __): __________________________
  Responsável: _____________ | Prazo: __/__/____

=============================================================================
Homologado por: _________________ (TI) | Aprovado por: _________________ (CEO)
=============================================================================
```

*   **Como preencher manualmente**: Reúna-se com o CEO por 15 minutos e preencha as 10 perguntas binárias com base em evidências operacionais objetivas. Compute a nota final, mapeie o nível de maturidade correspondente e assine a folha junto ao CEO, registrando as ações prioritárias de transição.
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Engenheiro de Prompts e Métricas'. Com base no histórico operacional da minha TI [inserir dados operacionais, status de backup e atas do CD-TI], preencha o Template de Diagnóstico de Maturidade do GP-PME. Calcule a pontuação final (IM-TI) e proponha um plano de ação detalhado para sanar os pontos identificados como falhos.
    ```

