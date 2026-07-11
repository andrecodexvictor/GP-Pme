# Framework GP-PME

Bem-vindo ao repositório do **Framework GP-PME (Governança Prática para Pequenas e Médias Empresas)**.

Este repositório contém a documentação completa, guias práticos e ativos interativos do framework GP-PME. O framework foi desenhado especificamente para ajudar pequenas e médias empresas a gerenciarem sua tecnologia de forma eficiente, segura e orientada a valor, utilizando os princípios da **TI Enxuta (Lean IT)**, agentes de Inteligência Artificial especialistas e estratégias de vitórias rápidas (*Quick Wins*).

---

## 🗺️ Estrutura do Repositório

*   **`GP-PME antigravity/`**: O diretório central que contém todos os guias detalhados, guias simplificados para leigos (*dummies*), templates operacionais de 1 página e o documento mestre consolidado.
*   **`GP-PME Article/`**: Contém um portal web interativo em HTML (`index.html`) com o design "Google Stitch" para navegação visual amigável por todos os pilares e documentos do framework.
*   **`Docs/`**: Diretório contendo diretrizes do projeto (PRD, Roadmap, Lista de Tarefas, Agentes Especialistas e o guia editorial `GEMINI.MD.md`).
*   **`References/`**: Repositório de materiais bibliográficos e histórico de versões acadêmicas e técnicas do framework (`GP-PME Versions`).

---

## 🚀 Como Começar

1.  **Explore o Framework Visualmente**:
    Abra o arquivo `GP-PME Article/index.html` em qualquer navegador web para acessar a versão interativa do framework. Lá você poderá visualizar os mapas de processos, cards de pilares e ler os guias com estilo tipográfico moderno.
2.  **Leia os Guias Técnicos**:
    Se você prefere os documentos em formato Markdown bruto para leitura ou para sistemas de busca e recuperação por IA (RAG), navegue até [Guides/](file:///c:/Users/adm/Desktop/GP-PME%20framework/GP-PME%20antigravity/Guides/) para ler os guias avançados, ou até [guide-for-dummies/](file:///c:/Users/adm/Desktop/GP-PME%20framework/GP-PME%20antigravity/guide-for-dummies/) para versões explicadas com jargão zero.
3.  **Adote os Templates Operacionais**:
    Acesse [Templates/](file:///c:/Users/adm/Desktop/GP-PME%20framework/GP-PME%20antigravity/Templates/) para encontrar planilhas prontas de RACI-Lite, Matrizes 4 Quadrantes, templates de PRD de 1 página, planos de contingência de incidentes (PRI) e receitas de prompts.

---

## 🎯 Filosofias Centrais

*   **TI Enxuta (Lean IT)**: Foco estrito em maximizar a entrega de valor de negócio ao mesmo tempo em que se elimina o desperdício de tempo e recursos operacionais. A TI se adapta ao tamanho da equipe, não o contrário.
*   **Vitórias Rápidas (Quick Wins)**: Cronogramas pragmáticos como a Fase Zero (playbook de 30 dias) garantem que a empresa veja retorno financeiro e estabilidade operacional desde as primeiras 24 horas.
*   **Aceleração Opcional por IA**: A IA generativa atua como um copiloto transversal opcional (Pilar IV) para automatizar a burocracia técnica sob supervisão humana estrita (Human-in-the-loop).

---

## 🔄 Destaque: O Ciclo de Serviço Micro-Adaptativo

O **Ciclo de Serviço Micro-Adaptativo** (Pilar II: Execução Ágil) é o motor operacional do GP-PME. Em vez de forçar a PME a adotar frameworks ágeis pesados de mercado, ele funde práticas enxutas do Scrum e do ITIL 4 de forma a acomodar a realidade diária de equipes reduzidas ou de um único técnico (*One-Man-Band*).

### Como funciona na Prática:
1.  **Sprints de 1 Semana**: O planejamento é realizado em ciclos curtíssimos de 1 semana. O técnico foca apenas em 2 ou 3 cartões de projetos de valor autorizados no CD-TI Lite.
2.  **Limite Rígido de WIP (WIP Limit = 3)**: É expressamente proibido ter mais de 3 tarefas simultâneas na coluna *Em Andamento* do Kanban. Isso impede a dispersão mental e garante que tarefas iniciadas sejam rapidamente concluídas.
3.  **Filtro do Canal Único**: Todas as demandas externas (WhatsApp, e-mails pessoais, telefonemas) são bloqueadas na origem. As demandas devem obrigatoriamente entrar pelo Canal Único, o que impede interrupções que quebram o fluxo de trabalho planejado.
4.  **Amortecedor de Emergências (A "Raia Rápida")**: Quando uma emergência cibernética ou parada de faturamento crítica ocorre, o técnico aplica a regra de suspensão: ele arrasta sua tarefa menos prioritária do Kanban de volta para a coluna *A Fazer* e ativa a **Raia de Expedite (Rápida)** para focar 100% no incidente, retornando ao fluxo original imediatamente após a mitigação.

Isso garante que a TI possa ser **micro-adaptativa** — respondendo a incidentes operacionais diários sem quebrar os prazos de projetos estratégicos de negócios.

---

## 🚀 Novidades da Edição Comercial (v2.0)

O GP-PME agora é um produto completo: além da documentação, ele traz busca inteligente, agentes de IA prontos para operar a gestão e integração com as principais plataformas de mercado.

| Capacidade | O que faz | Onde está |
|---|---|---|
| 🔎 **Busca Semântica** | Pergunte em linguagem natural e receba a seção exata do framework (CLI, API REST e página web offline) | [search/](search/) · [busca.html](GP-Pme%20Article/busca.html) |
| 🕸️ **Grafo de Conhecimento** | Mapa navegável de todos os conceitos do framework e suas conexões | [graphify-out/](graphify-out/) |
| 🤖 **Agentes Google ADK** | Orquestrador "Gestor GP-PME" + 8 especialistas que instalam e operam o kanban do framework em ClickUp, Notion, Trello, Jira e Linear | [agents/gp-pme-adk/](agents/gp-pme-adk/) |
| 📋 **Agentes Plug-and-Play** | 9 system prompts prontos para copiar em Claude Projects, GPTs ou qualquer chat | [Agentes_Prontos/](GP-PME%20antigravity/Templates/AI-Skills-and-Agents/Agentes_Prontos/) |
| 🧩 **Skills Claude Code** | 8 skills engatáveis (consultor, fase zero, kanban, governança, segurança, métricas, maturidade, PRD) | [.claude/skills/](.claude/skills/) |
| 🔌 **Servidor MCP + API** | O framework como serviço para ambientes hostis a ferramentas de gestão | [server/](server/) |
| 📊 **Simulação de Implantação** | Antes × depois com ROI para empresas de 10 a 100 funcionários | [Simulacao/](Simulacao/) |
| 💼 **Kit Comercial** | Proposta de valor, one-pager, precificação e onboarding de cliente | [Comercial/](Comercial/) |

> Comece pelo novo [INDEX.md](GP-PME%20antigravity/INDEX.md) — o índice premium com trilhas por persona e o catálogo completo de artefatos.

---

*Repositório gerido sob os padrões de qualidade técnica do framework GP-PME.*

---

## ⚖️ Licença

**© 2026 Andre Victor. Todos os direitos reservados.**

Este repositório é protegido por licença proprietária. Reprodução, distribuição ou uso comercial sem autorização prévia por escrito é expressamente proibido. Consulte o arquivo [LICENSE.md](LICENSE.md) para detalhes completos.
