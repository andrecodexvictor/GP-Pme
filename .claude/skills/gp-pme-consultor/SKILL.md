---
name: gp-pme-consultor
description: Porta de entrada do framework GP-PME. Use quando o usuário não sabe por onde começar, diz "não sei o que priorizar na TI", "estou perdido no framework", "qual pilar eu ativo primeiro", "minha TI é um caos", "quero um diagnóstico rápido", "qual meu nível de maturidade", ou pede para escolher entre governança/kanban/segurança/métricas. Diagnostica a dor dominante da PME, roda a autoavaliação rápida de maturidade (IM-TI) e roteia para o guia, skill ou template certo do framework — nunca implementa a fundo, apenas direciona.
---

# GP-PME Consultor — Triagem e Roteamento

Este skill é o **motor de triagem**, não um executor. Ele lê o sintoma do usuário, calcula (ou estima) o nível de maturidade, e aponta o próximo passo concreto — guia para ler, skill para engatar, template para preencher. Todo conhecimento vive no framework; este skill nunca reescreve o conteúdo dos guias, apenas referencia caminhos.

## QUANDO USAR

- Usuário chega sem contexto: "por onde eu começo com o GP-PME?".
- Usuário descreve uma dor de negócio ("meu técnico só apaga incêndio", "não sei se estamos seguros", "ninguém decide nada na TI") e precisa saber qual pilar/guia resolve.
- Usuário quer saber "em que nível de maturidade estou" antes de investir tempo em um guia específico.
- Usuário já rodou outra skill do GP-PME e quer confirmar o próximo passo da jornada.
- **Não usar** quando o usuário já sabe exatamente o que quer (ex: "monte meu kanban" → vá direto para `gp-pme-kanban`; "quero a pauta do CD-TI Lite" → `gp-pme-governanca`). Nesses casos o roteamento é desnecessário — a skill específica lida com isso sozinha.

## FLUXO PASSO A PASSO

1. **Capturar o sintoma dominante.** Peça (ou infira da mensagem) uma frase curta descrevendo a dor. Classifique em uma das 4 categorias de dor + 1 categoria de "não sei":
   - **Caos operacional** ("demandas perdidas", "WhatsApp pessoal", "não sei o que está pendente") → Pilar II.
   - **Falta de alinhamento com o negócio** ("CEO não participa de decisões de TI", "ninguém aprova verba", "TI é vista como custo") → Pilar I.
   - **Risco de segurança** ("nunca testamos backup", "não sei se temos vírus", "não temos plano de crise") → Pilar III.
   - **Falta de visibilidade / métricas** ("não sei se a TI está funcionando bem", "quero provar valor pro CEO") → KPIs / DAN-COT.
   - **"Não sei por onde começar"** → pule direto para o passo 2 (diagnóstico completo).

2. **Decidir a profundidade do diagnóstico.**
   - Se o usuário quer resposta rápida (1 dor específica, já sabe o contexto): pule para o passo 4 com a tabela de roteamento direto.
   - Se o usuário quer visão completa ou disse "não sei": rode o **questionário de 10 perguntas binárias** do `Guia_Modelo_de_Maturidade.md` (seção 4). Apresente as 10 perguntas, colete Sim/Não.

3. **Calcular o Índice de Maturidade da TI (IM-TI).** Some 1 ponto por resposta "Sim" e classifique:
   | Pontos | Nível | Rótulo |
   |---|---|---|
   | 0–2 | Nível 0 | Caótico → **rotear para `gp-pme-fase-zero` imediatamente**, é urgente |
   | 3–5 | Nível 1 | Reativo Organizado → focar em segurança essencial e governança de alinhamento |
   | 6–8 | Nível 2 | Governança Básica → pronto para ciclos de MVP/inovação |
   | 9 | Nível 3 | Inovação Incremental → focar em DAN/COT e débito técnico |
   | 10 | Nível 4 | Governança Adaptativa → formalizar os 4 agentes de IA com HITL |

4. **Rotear com base na dor + nível.** Use a tabela de decisão:
   | Dor / Situação | Nível medido | Rota recomendada |
   |---|---|---|
   | Caos operacional, IM-TI 0–2 | 0 | `gp-pme-fase-zero` (implantação dos 30 dias) |
   | Caos operacional, IM-TI ≥3 (kanban já existe mas está bagunçado) | 1+ | `gp-pme-kanban` |
   | Falta de alinhamento com negócio | qualquer | `gp-pme-governanca` |
   | Risco de segurança / backup não testado | qualquer | `Guides/Guia_Pilar_3_Seguranca_Critica.md` (não há skill própria — apontar o guia e o Template 6/7) |
   | Quer provar valor com números | Nível 2+ | `Guides/Guia_KPIs_e_Quick_Wins.md` + Template 3 (Dashboard 3 KPIs) |
   | Quer medir dívida técnica | Nível 3+ | `GP-PME_Documento_Mestre_Consolidado.md` (seção DAN/COT) |
   | Quer formalizar agentes de IA | Nível 4 | `Guides/Guia_Pilar_4_Assistencia_IA_e_Agentes.md` |
   | "Não sei o que é o framework" | — | `INDEX.md` (trilha por persona: CEO / Gestor de TI / Consultor / Dev) |

5. **Checar pré-requisito antes de rotear para um pilar avançado.** Regra de bloqueio: não recomende Pilar III (segurança formal), Pilar IV (agentes de IA) ou DAN/COT antes de o usuário confirmar que Canal Único + Kanban (perguntas 1–2 do questionário) já estão ativos. Se não estiverem, redirecione primeiro para `gp-pme-fase-zero` — governança e segurança avançadas sem a base operacional geram burocracia sem sustentação.

6. **Entregar o resultado em formato de plano.** Sempre encerre com: (a) nível de maturidade atual, (b) a rota escolhida e por quê, (c) o próximo checkpoint mensurável (ex: "em 30 dias, reaplique o questionário e confira se saiu do Nível 0 para o Nível 1").

7. **Se o usuário pedir profundidade adicional no diagnóstico** (ex: "quero o plano de transição completo, não só o roteamento, com plano de ação"), entregue para `gp-pme-maturidade` em vez de tentar produzir a matriz completa aqui — este skill só faz triagem rápida, não substitui a skill de maturidade dedicada (que cobre a matriz 5×4 completa e o plano de transição).

8. **Se a dor detectada já tem skill dedicada dentro do catálogo atual do framework**, prefira sempre a skill específica ao guia bruto — a tabela do passo 4 lista as skills quando existem e cai para o caminho de guia/template só quando não há skill própria ainda. Catálogo de skills conhecidas para roteamento: `gp-pme-fase-zero` (implantação 0→1), `gp-pme-kanban` (operação do quadro), `gp-pme-governanca` (CD-TI Lite/RACI/4Q), `gp-pme-seguranca` (NIST-Lite/PRI/matriz de risco), `gp-pme-metricas` (KPIs/DAN/COT), `gp-pme-maturidade` (diagnóstico profundo e plano de transição), `gp-pme-prd` (PRD Simplificado para MVPs).

## REFERÊNCIA RÁPIDA — OS 5 NÍVEIS DE MATURIDADE

Use esta tabela para situar o usuário sem precisar reabrir o guia fonte:

| Nível | Rótulo | Característica dominante | Foco |
|---|---|---|---|
| 0 | Caótico | Faz-tudo sobrecarregado, chamados via WhatsApp/corredor, zero visibilidade de custo | Sobrevivência e contenção do caos |
| 1 | Reativo Organizado | Canal Único + Kanban de 4 colunas + WIP=3 ativos, FAQs básicas disponíveis | Organização de demandas |
| 2 | Governança Básica | CD-TI Lite quinzenal + Matriz 4 Quadrantes, Inventário 80/20, backup 3-2-1 testado, PRI na parede | Alinhamento estratégico e mitigação de risco crítico |
| 3 | Inovação Incremental | Ciclo Ideia-MVP-Feedback de 2 semanas rodando, DAN/COT medidos sistematicamente | Geração de valor comercial rápido |
| 4 | Governança Adaptativa | 4 Agentes de IA operando sob protocolo HITL, planejamento de escala de longo prazo | Automação avançada sem overhead |

## REFERÊNCIA RÁPIDA — AS 10 PERGUNTAS DO QUESTIONÁRIO

Aplique literalmente (Sim/Não, cada Sim = 1 ponto) quando for rodar o diagnóstico completo do passo 2:

1. Canal Único: existe um único canal formalizado de suporte, sem chamados informais (WhatsApp pessoal)?
2. Kanban Ativo: quadro de 4 colunas (A Fazer/Em Andamento/Em Teste/Concluído) com WIP Limit ≤ 3?
3. FAQs Operacionais: FAQ ou chatbot resolve autonomamente mais de 40% das dúvidas básicas?
4. CD-TI Lite: CEO e Gestor de TI se reúnem 30 min periodicamente para revisar métricas e aprovar verbas?
5. Matriz 4 Quadrantes: toda iniciativa de TI é priorizada com base no impacto em faturamento/despesas?
6. Inventário 80/20: existe planilha atualizada dos 20% de ativos que representam 80% do risco?
7. Backups Testados: backup automático em nuvem com teste físico de restauração no último trimestre (< 30 min)?
8. PRI de 1 Página: plano de resposta a incidentes assinado pelo CEO, impresso na sala de TI?
9. Métricas DAN/COT: o gestor calcula e apresenta ao CD-TI Lite a Dívida de Arquitetura e o ROI do COT?
10. Auditoria HITL: existe checklist de auditoria de alucinações para saídas de IA antes de irem a produção?

## REFERÊNCIA RÁPIDA — CHECKLISTS DE TRANSIÇÃO ENTRE NÍVEIS

Quando o usuário perguntar "o que falta para eu subir de nível", use estes checklists objetivos em vez de reexplicar o conceito de maturidade:

**Nível 0 → 1:** unificar chamados em canal único · ativar Kanban 4 colunas · WIP Limit = 3 · FAQ inicial de 5 itens · registrar TMpR baseline.
**Nível 1 → 2:** agenda quinzenal de 30 min do CEO travada (CD-TI Lite) · Matriz 4 Quadrantes preenchida · Inventário 80/20 mapeado · backup diário + teste físico de restauração · PRI de 1 página na parede.
**Nível 2 → 3:** primeiro ciclo MVP de 2 semanas lançado · PRDs Simplificados padronizados · DAN calculado com proposta de otimização por ROI · biblioteca de prompts canônicos homologada.
**Nível 3 → 4:** os 4 Agentes de IA instanciados (Orquestrador, Analista, Guardião, Auditor) · prompts de contexto/restrição institucionalizados · checklist HITL aplicado a 100% das saídas de IA · plano de arquitetura elástica de longo prazo aprovado no CD-TI Lite.

Cada item não cumprido do nível atual é, por si só, a próxima tarefa concreta a devolver ao usuário — não precisa esperar rodar o questionário completo de novo para dar esse retorno.

## INTEGRAÇÃO COM OUTRAS SKILLS

Este skill nunca executa a fundo — ele delega. Ao final de toda triagem, a resposta deve nomear explicitamente qual skill assume a partir daqui (`gp-pme-fase-zero`, `gp-pme-kanban`, `gp-pme-governanca`, `gp-pme-seguranca`, `gp-pme-metricas`, `gp-pme-maturidade` ou `gp-pme-prd`). Se duas dores coexistirem (ex: caos operacional + segurança nunca testada), rotear pela dor de maior risco de parada de faturamento primeiro — segurança/backup não testado normalmente supera caos de kanban em urgência, salvo se o IM-TI for 0-2, caso em que a Fase Zero sempre vem primeiro porque ela já inclui o primeiro passo de segurança (backup) na Semana 2.

## FONTES NO FRAMEWORK

| Caminho | O que extrair |
|---|---|
| `GP-PME antigravity/INDEX.md` | Trilhas por persona (CEO/Gestor/Consultor/Dev), catálogo completo de artefatos, tabela de "Comece em 30 Minutos" |
| `README.md` | Visão geral da estrutura de pastas do repositório, filosofias centrais (TI Enxuta, Quick Wins, IA opcional) |
| `GP-PME antigravity/Guides/Guia_Modelo_de_Maturidade.md` | Seção 2 (5 níveis de maturidade), seção 3 (matriz por pilar), seção 4 (questionário de 10 perguntas + cálculo do IM-TI), seção 5 (checklists de transição de nível) |
| `GP-PME antigravity/Templates/Mapeamento_Maturidade/Template_Mapeamento_Maturidade.md` | Template de folha de pontuação para registrar a resposta do questionário |
| `GP-PME antigravity/Guides/Guia_Pilar_1_Governanca_Essencial.md` | Quando a dor for de alinhamento/governança — confirmar o que a rota vai cobrir |
| `GP-PME antigravity/Guides/Guia_Pilar_2_Execucao_Agil.md` | Quando a dor for de caos operacional — confirmar o que a rota vai cobrir |
| `GP-PME antigravity/Guides/Guia_Pilar_3_Seguranca_Critica.md` | Quando a dor for de segurança — não há skill dedicada, apontar direto o guia |

## SAÍDAS ESPERADAS

- Diagnóstico curto: sintoma → nível de maturidade (com pontuação) → rota recomendada com caminho de arquivo/skill exato.
- Quando o questionário completo foi rodado: lista das 10 respostas Sim/Não e o IM-TI calculado.
- Um único próximo passo acionável (nunca uma lista de "leia tudo") — o usuário deve sair sabendo exatamente qual skill/guia abrir a seguir.

## EXEMPLOS

**Exemplo 1 — dor específica, sem diagnóstico completo.**
Usuário: "O CEO não participa de nada da TI, decisões de verba demoram semanas."
→ Classificado como "falta de alinhamento com o negócio". Sem necessidade de questionário completo (dor já é clara).
→ Rota: `gp-pme-governanca`, especificamente o CD-TI Lite (reunião quinzenal de 30 min) e a Matriz 4 Quadrantes.
→ Resposta: "Isso é dor de Pilar I. Vou te levar para `gp-pme-governanca`, que monta a pauta do CD-TI Lite e o RACI-Lite. Antes disso, confirma: vocês já têm Canal Único e Kanban ativos? Se não, a raiz do problema pode ser caos operacional, não falta de governança."

**Exemplo 2 — "não sei por onde começar".**
Usuário: "Sou dono de uma PME, não sei nada de TI, meu técnico está sempre correndo atrás do prejuízo."
→ Aplica o questionário de 10 perguntas. Suponha 2 "Sim" (só pergunta 1 e 3).
→ IM-TI = 2 → Nível 0: Caótico.
→ Rota: `gp-pme-fase-zero`, com urgência ("Urgente: implantar Fase Zero do GP-PME", conforme seção 4 do Guia de Maturidade).
→ Resposta: "Sua TI está no Nível 0 (Caótico) — 2 de 10 pontos. A prioridade absoluta é rodar a Fase Zero (30 dias). Vou engatar `gp-pme-fase-zero` para montar o cronograma semana a semana."
