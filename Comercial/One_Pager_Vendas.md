# GP-PME — One Pager de Vendas

> Fontes: `Comercial/Proposta_de_Valor.md`, `Simulacao/Calculadora_ROI.md`, `GP-PME antigravity/INDEX.md` (v2.0).
> Números conservadores: exemplos resolvidos da própria Calculadora de ROI (fórmulas oficiais, premissas declaradas) — não são case de cliente real. Válido como âncora até os perfis `Simulacao/Perfil_A..D.md` estarem prontos.

---

## Headline

**Sua TI apaga incêndio ou evita incêndio? O GP-PME transforma o técnico "faz-tudo" reativo em governança de 1 página — com o primeiro resultado mensurável em 30 dias.**

Framework de gestão de TI para PMEs brasileiras que destila ISO 38500, COBIT 2019, ITIL 4, NIST CSF e CIS Controls v8 em artefatos operáveis por 1 técnico solo ou uma equipe de até 8 pessoas — no papel, com IA como acelerador opcional.

---

## 3 Números de Impacto (conservadores)

| # | Número | O que significa | Fonte |
|---|---|---|---|
| 1 | **R$ 4.930/mês** recuperáveis | R$ 1.750/mês de retrabalho por perda de rastreabilidade (Canal Único) + R$ 3.180/mês de tempo de TI desperdiçado em multitarefa (Kanban WIP=3) | `Calculadora_ROI.md §4.1–4.2` |
| 2 | **R$ 12.000/ano** de risco evitado | Queda de probabilidade de incidente grave (ransomware) de 20%/ano para 5%/ano com Backup 3-2-1 + MFA + LUA + PRI | `Calculadora_ROI.md §5` |
| 3 | **Payback em ~1,8 meses** (ROI de 651% no exemplo) | Sobre um custo de implantação (COT) de R$ 9.570 no exemplo resolvido | `Calculadora_ROI.md §3` |

Esses três números somados (~R$ 71.000/ano em retrabalho + tempo desperdiçado + risco evitado) superam em várias vezes o investimento em qualquer um dos três tiers comerciais — ver `Modelo_de_Precificacao.md`.

---

## O que está incluso (por camada)

O GP-PME roda 100% no papel. As 4 camadas de IA abaixo são aceleradores opcionais — nenhuma é pré-requisito.

| Camada | O que é | Onde roda |
|---|---|---|
| **Núcleo (obrigatório)** | 4 guias de pilar + guias para leigos + 7 templates de 1 página + modelo de maturidade (IM-TI) + guia de KPIs/DAN/COT + playbook Fase Zero (30 dias) | Papel, planilha ou quadro físico |
| **1 · Skills** | 8 skills nativas do Claude Code (`consultor`, `fase-zero`, `kanban`, `governanca`, `seguranca`, `metricas`, `maturidade`, `prd`) | Terminal / Claude Code |
| **2 · Agentes Markdown** | 9 personas prontas para copiar e colar (Orquestrador, Analista, Guardião, Auditor e especialistas de pilar) | Claude Projects / GPTs — zero setup |
| **3 · Agentes ADK** | Orquestrador "Gestor GP-PME" + 8 especialistas em Python (Google ADK) que instalam o kanban GP-PME direto na sua plataforma | ClickUp, Notion, Trello, Jira, Linear |
| **4 · MCP + API REST** | Servidor programático do framework para integrar a sistemas próprios | Sua stack |
| **Extras** | Busca semântica (RAG) sobre todo o conteúdo + grafo de conhecimento interativo + simulação de ROI personalizada | Web / CLI |

---

## Para quem é

- TI solo ou equipe de até 8 pessoas numa PME (indústria, serviços, comércio, saúde, varejo).
- Dono/CEO sem tempo ou apetite para consultoria pesada, mas cansado de decidir investimento de TI no escuro.
- Gestor de TI que já sabe o que precisa fazer, mas não tem processo formalizado nem métrica para provar valor à diretoria.

## Para quem NÃO é

- Empresas que já operam ITIL/COBIT maduro com analista de governança dedicado — o GP-PME é a versão enxuta, não substitui um programa já maduro.
- Times de TI com mais de ~15-20 pessoas e múltiplas squads — nesse porte, frameworks completos de mercado se pagam melhor.
- Quem busca um produto de software pronto — o GP-PME é método + templates + aceleradores de IA, não um SaaS de ITSM.

---

## Call to Action

Quer ver o ROI com os números reais da sua empresa, não os do exemplo? Mande porte da equipe, custo-hora aproximado e horas de retrabalho/mês que você já reconhece — devolvemos a simulação personalizada (`Simulacao/`) e a proposta comercial (tier + preço) em até 2 dias úteis.

**Contato**: [inserir e-mail/telefone do consultor responsável]
