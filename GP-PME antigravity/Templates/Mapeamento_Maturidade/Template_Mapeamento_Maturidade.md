# Template 8: Avaliação e Matriz de Maturidade GP-PME

*   **Objetivo**: Realizar a autoavaliação periódica do nível de maturidade da TI na PME, calculando o Índice de Maturidade (IM-TI) e traçando o plano de ação para transição de fases.
*   **Frequência Recomendada**: No início da implantação (Dia 1 da Fase Zero) e, posteriormente, a cada 6 meses na reunião do CD-TI Lite.

---

## 1. Questionário de Diagnóstico Rápido

Marque **[X]** apenas se a afirmação for verdadeira e houver evidência prática que a sustente.

| ID | Critério / Pergunta | Resposta | Evidência Prática (Ex: Nome do Arquivo, Data do Teste) |
|:---:|:---|:---:|:---|
| **01** | **Canal Único**: A TI possui um único canal formalizado para receber solicitações de suporte e projetos, tendo erradicado chamados informais (WhatsApp pessoal, corredor)? | `[ ] Sim  [ ] Não` | |
| **02** | **Kanban Ativo**: Existe um quadro Kanban de 4 colunas (*A Fazer, Em Andamento, Em Teste, Concluído*) ativo, com limite de trabalho em andamento (WIP Limit de no máximo 3 tarefas por técnico)? | `[ ] Sim  [ ] Não` | |
| **03** | **FAQs Operacionais**: A PME disponibiliza um documento de FAQ ou um chatbot de triagem que resolve autonomamente mais de 40% das dúvidas básicas dos colaboradores? | `[ ] Sim  [ ] Não` | |
| **04** | **CD-TI Lite**: O CEO e o Gestor de TI realizam reuniões de 30 minutos periodicamente (quinzenal ou mensal) para revisar métricas e aprovar verbas estratégicas? | `[ ] Sim  [ ] Não` | |
| **05** | **Matriz 4 Quadrantes**: A TI utiliza a Matriz 4 Quadrantes para planejar e priorizar todas as iniciativas com base no impacto no faturamento e despesas do negócio? | `[ ] Sim  [ ] Não` | |
| **06** | **Inventário 80/20**: A empresa possui uma planilha atualizada contendo os 20% de ativos tecnológicos mais críticos que representam 80% do risco operacional? | `[ ] Sim  [ ] Não` | |
| **07** | **Backups Testados**: A PME possui backups automáticos em nuvem e realizou com sucesso um teste físico de restauração em menos de 30 minutos no último trimestre? | `[ ] Sim  [ ] Não` | |
| **08** | **PRI de 1 Página**: Existe um Plano de Resposta a Incidentes (PRI) de 1 página, assinado pelo CEO e impresso na sala de TI com contatos emergenciais e etapas de isolamento físico? | `[ ] Sim  [ ] Não` | |
| **09** | **Métricas DAN/COT**: O gestor calcula e apresenta ao CD-TI Lite o índice DAN (Dívida de Arquitetura) e o ROI do COT (Custo de Otimização)? | `[ ] Sim  [ ] Não` | |
| **10** | **Auditoria HITL (IA)**: Caso utilize ferramentas de IA para gerar código ou documentos, a PME possui um checklist de auditoria de alucinações (HITL) que impede saídas de IA de irem para produção sem revisão? | `[ ] Sim  [ ] Não` | |

---

## 2. Folha de Pontuação e Nível de Maturidade

### Cálculo do Índice de Maturidade da TI (IM-TI)
$$\text{IM-TI} = \text{Total de respostas "Sim" marcadas (de 0 a 10)}$$

*   **Pontuação Obtida**: `[ ______ ] pontos`
*   **Nível de Maturidade Correspondente**:
    *   **0 a 2 pontos**: `[  ] Nível 0: Caótico` (Operação desordenada, alto risco operacional).
    *   **3 a 5 pontos**: `[  ] Nível 1: Reativo Organizado` (Operação estruturada com Kanban e Canal Único).
    *   **6 a 8 pontos**: `[  ] Nível 2: Governança Básica` (Alinhamento de negócios e segurança crítica ativa).
    *   **9 pontos**: `[  ] Nível 3: Inovação Incremental` (TI proativa, ciclos de MVP e controle de DAN/COT).
    *   **10 pontos**: `[  ] Nível 4: Governança Adaptativa` (IA como copiloto transversal operando sob HITL).

---

## 3. Plano de Ação de Transição de Nível

Descreva as ações práticas que serão implementadas para sanar os critérios marcados como "Não" no questionário:

1.  **Ação 1 (Saneamento do ID ___)**: [Descreva a iniciativa técnica ou ritual de governança a ser implantado]
    *   *Responsável*: [Nome do Responsável]
    *   *Prazo de Entrega*: [Data]
    *   *Evidência de Conclusão*: [ex: Link do Trello ou log de teste de backup]

2.  **Ação 2 (Saneamento do ID ___)**: [Descreva a iniciativa técnica ou ritual de governança a ser implantado]
    *   *Responsável*: [Nome do Responsável]
    *   *Prazo de Entrega*: [Data]
    *   *Evidência de Conclusão*: [ex: Cópia física do PRI assinada e colada na TI]

---
*Homologado por: [Nome do Gestor de TI] (Assinatura: _________________________)*  
*Aprovado por: [Nome do CEO / Dono] (Assinatura: _________________________)*  
*Data de Homologação: ___/___/2026*  

---

## 4. Diretrizes de Preenchimento

*   **Como preencher manualmente**: Imprima esta folha de template. Reúna-se por 15 minutos na sala de TI com os logs operacionais e preencha o questionário à mão. Anote a pontuação final, selecione o nível de maturidade correspondente e detalhe as ações prioritárias para mitigar as falhas identificadas. Assine e co-assine junto ao CEO durante a reunião CD-TI Lite.
*   **Prompt de Aceleração (IA)**:
    ```text
    Atuar como 'Engenheiro de Prompts e Métricas'. Receba os dados operacionais da minha TI [inserir logs, status de backup e atas] e preencha este Template de Mapeamento de Maturidade GP-PME. Calcule o IM-TI, classifique o nível correspondente e proponha um plano de ação de 3 etapas para sanar as deficiências identificadas.
    ```
