# 🤖 Agentes Prontos GP-PME — Plug and Play

Esta pasta reúne **9 agentes de IA prontos para uso** — prompts de sistema completos, testados e alinhados à terminologia oficial do framework GP-PME. Cada arquivo `.md` traz persona, instruções de instalação em 4 plataformas, o **SYSTEM PROMPT** pronto para copiar, exemplos de uso e as fontes do framework de onde o agente bebe.

**Filosofia HITL (Human-in-the-Loop):** nenhum agente desta pasta decide sozinho. Todos foram redigidos com o nível de autonomia **"Consultivo com HITL obrigatório"** — eles preparam diagnósticos, matrizes, checklists, cálculos e rascunhos, mas toda aprovação de orçamento, priorização estratégica, homologação de nível de maturidade ou assinatura de entregável continua sendo do CEO e/ou do Gestor de TI da PME. Os agentes aceleram a análise; humanos continuam donos da decisão.

---

## 📋 Catálogo dos agentes

| Agente | Emoji | Pilar | Quando usar | Arquivo |
|---|---|---|---|---|
| **Orquestrador — Gestor GP-PME** | 🧭 | Transversal (I a IV) | Ponto de entrada único do framework: diagnóstico de maturidade, condução da Fase Zero, manutenção do Kanban e das cadências, consolidação mensal de métricas e roteamento para o agente especialista correto | `Agente_Orquestrador_Gestor_GP-PME.md` |
| **Governança** | 🏛️ | I — Governança Essencial | Pauta do CD-TI Lite, Matriz 4 Quadrantes e RACI-Lite — conectar toda iniciativa de TI a uma meta de faturamento, custo, experiência do cliente ou segurança | `Agente_Governanca.md` |
| **Execução Ágil** | 🏃 | II — Execução Ágil | Tasklist de sprint semanal, diagnóstico do fluxo do Kanban, classificação de chamados na Matriz de Priorização, planejamento da Raia Rápida para incidentes críticos | `Agente_Execucao_Agil.md` |
| **Segurança** | 🛡️ | III — Segurança Crítica | Checklist dos 10 controles mínimos (NIST-Lite/CIS Controls v8 IG1), avaliação de risco de ativos críticos (Probabilidade × Impacto), Plano de Resposta a Incidentes de 1 página | `Agente_Seguranca.md` |
| **Métricas e Auditoria** | 📊 | Transversal (mede I a III; portão do IV) | Cálculo dos 3 KPIs Visíveis (IDSC/TMpR/ISU), da Dívida de Arquitetura Normalizada (DAN) e do ROI/payback do COT; auditoria HITL de 4 blocos sobre entregáveis de outros agentes | `Agente_Metricas_e_Auditoria.md` |
| **Maturidade** | 📈 | Transversal (I a IV) | Questionário de 10 perguntas do Modelo de Maturidade, cálculo do Índice de Maturidade da TI (IM-TI) global e por pilar, plano de ação de transição entre os níveis 0 a 4 | `Agente_Maturidade.md` |
| **Fase Zero** | 🚀 | Transversal (quick wins de I a III) | Cronograma de 30 dias (4 semanas, 9 passos), calendário completo da implantação (Fase Zero à Fase Três), verificação de prontidão para certificar a transição ao Nível 1 | `Agente_Fase_Zero.md` |
| **PRD** | 📝 | II — Execução Ágil | Traduzir uma dor de negócio em um PRD Simplificado de 1 a 2 páginas — histórias de usuário, critérios de aceitação, escopo negativo — pronto para um MVP de até 2 semanas | `Agente_PRD.md` |
| **Engenheiro de Prompts** | 🧠 | IV — Assistência por IA e Agentes (opcional/acelerador) | Redigir, auditar e adaptar prompts de sistema para qualquer IA do ecossistema GP-PME, incluindo os outros 8 agentes desta pasta | `Agente_Engenheiro_de_Prompts.md` |

---

## ⚡ Como instalar

Todo agente segue o mesmo padrão de instalação em 4 opções — abra o arquivo `.md` do agente escolhido para ver a lista exata de arquivos de conhecimento a anexar.

**(a) Claude Projects**
1. Crie um novo Project com o nome sugerido no cabeçalho do agente (ex.: "GP-PME — Governança").
2. Em *Custom Instructions*, cole o bloco **SYSTEM PROMPT** do arquivo `.md`.
3. Em *Project Knowledge*, anexe os arquivos de conhecimento listados na seção "Instalação em 2 minutos" do agente (Guias, Templates, Documento Mestre).
4. Inicie a conversa com os dados/pergunta indicados nos "Exemplos de uso" do agente.

**(b) GPT personalizado (ChatGPT)**
1. Explorar GPTs → Criar → aba *Configure*.
2. Nomeie o GPT e cole o **SYSTEM PROMPT** em *Instructions*.
3. Em *Knowledge*, faça upload dos mesmos arquivos usados no item (a).
4. Desative *Web Browsing* e *Code Interpreter* (reduz risco de alucinação).

**(c) Google ADK**
1. Use o especialista já implementado em `agents/gp-pme-adk/<agente>/agent.py` (quando ainda não implementado, o arquivo indica isso e aponta o padrão em `agents/gp-pme-adk/CONVENTIONS.md`).
2. A partir de `agents/gp-pme-adk/`, rode `adk run <nome_do_agente>` isoladamente ou deixe o `orquestrador_gp_pme` delegar automaticamente.
3. Configure `GPPME_MODEL` e as credenciais de plataforma necessárias no `.env`; sem credenciais, roda em `GPPME_DRY_RUN=1` (simulado).

**(d) Qualquer chat de IA**
1. Cole o **SYSTEM PROMPT** do agente como primeira mensagem da conversa.
2. Em seguida, cole o conteúdo (ou um resumo) dos arquivos de conhecimento indicados no arquivo do agente.

---

## 🧭 Qual agente escolher?

Comece pela dor que você está sentindo agora:

- **"Não sei por onde começar / não sei se estou fazendo certo"** → **Orquestrador** (ou **Maturidade**, se já quer medir o nível atual).
- **"Ninguém aprova nada, cada iniciativa de TI nasce sem dono nem meta"** → **Governança**.
- **"Meu time está afogado, tudo é urgente, ninguém sabe o que fazer primeiro"** → **Execução Ágil**.
- **"Tenho medo de um incidente de segurança / não sei se estamos protegidos"** → **Segurança**.
- **"Preciso provar com números que a TI está funcionando (ou não)"** → **Métricas e Auditoria**.
- **"Quero saber em que nível de maturidade estamos e o que fazer para subir"** → **Maturidade**.
- **"Estou começando a implantar o GP-PME agora"** → **Fase Zero**.
- **"Tenho uma ideia/demanda de negócio e preciso transformá-la em algo executável"** → **PRD**.
- **"Preciso escrever ou revisar o prompt de um agente de IA"** → **Engenheiro de Prompts**.

Na dúvida entre dois agentes, ou quando a demanda cruza mais de um pilar, comece sempre pelo **Orquestrador** — ele diagnostica e aciona o especialista certo.

---

## 🛠️ Nota de manutenção

A terminologia, as siglas (IM-TI, DAN, COT, IDSC/TMpR/ISU, RACI-Lite, NIST-Lite etc.) e os processos usados nos SYSTEM PROMPTs desta pasta vêm sempre dos **Guias oficiais** em `GP-PME antigravity/Guides/` e do `GP-PME_Documento_Mestre_Consolidado.md`. Sempre que um Guia for atualizado (nova métrica, novo passo, novo nome de artefato), **revise o agente correspondente** nesta pasta para manter os dois em sincronia — um agente desatualizado em relação ao seu Guia é uma fonte de alucinação, não de aceleração.
