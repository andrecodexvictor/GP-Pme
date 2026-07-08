---
name: gp-pme-seguranca
description: Use esta skill quando o usuário pedir para rodar o checklist de segurança NIST-Lite/CIS IG1 de uma PME, montar uma matriz de risco (probabilidade x impacto) para um ativo crítico, ou redigir/acionar um Plano de Resposta a Incidentes (PRI) de 1 página. Gatilhos: "checklist de segurança", "auditoria de segurança", "análise de risco", "matriz de risco", "PRI", "resposta a incidente", "backup testado", "NIST-Lite", "CIS IG1", "10 controles críticos".
---

# Skill: GP-PME · Segurança Crítica (Pilar III)

Motor enxuto que aplica o **Pilar III (Segurança Crítica / NIST-Lite)** do framework GP-PME. Esta skill não recria conteúdo — ela orquestra o preenchimento dos artefatos oficiais do framework (checklist de 10 controles, matriz de risco, PRI) usando as fontes listadas abaixo. Sempre abra e cite os arquivos-fonte antes de gerar a saída; não invente controles, normas ou ameaças fora do escopo NIST-Lite/CIS IG1.

## QUANDO USAR

Acione esta skill quando o pedido do usuário envolver qualquer um destes cenários:

1. **Auditoria de segurança da PME** — "quero saber se minha TI está protegida", "faça um checklist de segurança", "estamos em conformidade com o mínimo de segurança?".
2. **Análise de risco de um ativo específico** — "avalie o risco do nosso servidor de arquivos", "qual o risco desse sistema ERP na nuvem?", "mapeie ameaças e vulnerabilidades de [ativo]".
3. **Resposta a incidente / crise em andamento** — "fomos vítimas de ransomware, o que fazer agora?", "preciso do plano de resposta a incidentes", "monte a raia rápida de contenção".
4. **Preparação para o CD-TI Lite** — quando o comitê executivo quinzenal vai revisar postura de segurança e o usuário precisa de um resumo objetivo (controles implementados/pendentes + riscos críticos).
5. **Onboarding de segurança em PME em estágio inicial (Nível 0/1 de maturidade)** — priorizar rapidamente os 4 controles de maior impacto (Inventário 80/20, Privilégio Mínimo/MFA, Backup 3-2-1, PRI).

Não use esta skill para segurança de nível enterprise (SOC, firewalls de borda corporativos, threat hunting) — o GP-PME é deliberadamente "lite" e assume orçamento e equipe mínimos de PME. Se o usuário pedir algo fora desse escopo, avise que é preciso trazer um especialista externo.

## FLUXO PASSO A PASSO

### 1. Diagnóstico — Checklist dos 10 Controles Críticos
Abra `modulo3_10_controles_criticos.md` e preencha a tabela de 10 controles com o usuário, um a um, marcando **Implementado / Em Andamento / Não Implementado** e anotando próximos passos para cada lacuna:

| # | Controle | Pergunta de auditoria rápida |
|:-:|:---|:---|
| 1 | Inventário de Hardware | Você sabe listar todos os computadores/servidores/celulares e onde estão? |
| 2 | Inventário de Software | Você sabe listar todo software instalado nesses dispositivos? |
| 3 | Gestão de Vulnerabilidades | Existe rotina de encontrar e corrigir falhas conhecidas? |
| 4 | Configurações Seguras | Sistemas têm funções desnecessárias desativadas? |
| 5 | Gestão de Contas de Acesso | Senhas fortes + MFA em 100% das contas críticas? |
| 6 | Privilégio Mínimo (LUA) | Usuários comuns rodam sem permissão de administrador local? |
| 7 | Defesas contra Malware | Antivírus/EDR ativo e atualizado? |
| 8 | Backup 3-2-1 testado | Backup automático em nuvem + teste de restauração no último trimestre? |
| 9 | Firewall / Proteção de Rede | Tráfego de entrada/saída é filtrado? |
| 10 | Treinamento de Conscientização | Colaboradores foram treinados contra phishing/engenharia social? |

Se o tempo for curto, priorize os controles **5, 6, 8 e 10** (maior redução de risco por menor esforço, conforme o núcleo de 4 controles do Guia do Pilar 3).

### 2. Matriz de Risco (Probabilidade × Impacto)
Para cada ativo relevante (ou cada controle "Não Implementado"), gere a análise usando a estrutura do `Template_Prompt_Risco.md`:

- **Risco identificado** → **Ameaça relacionada** (ex.: ransomware, força bruta, erro humano) → **Vulnerabilidade crítica** (ex.: ausência de MFA, admin local) → **Probabilidade** (Baixa/Média/Alta) → **Impacto** (Baixo/Médio/Alto) → **Nível de Risco Geral** (cruzamento dos dois eixos: Crítico / Alto / Médio / Baixo).
- Regra prática de priorização: pergunte *"se esse ativo parar ou vazar hoje, a empresa consegue faturar amanhã?"* — se não, o ativo é Criticidade 5 (crítico) e qualquer vulnerabilidade nele sobe automaticamente o nível de risco.
- Nunca presuma infraestrutura cara não mencionada pelo usuário (firewall de borda, SOC). Se faltar dado, registre: *"Aviso: requer auditoria local física do profissional de TI para verificar [o que falta]."*

#### Grade de Cruzamento (Probabilidade × Impacto → Nível de Risco)

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|:---|:-:|:-:|:-:|
| **Alta** | Médio | Alto | Crítico |
| **Média** | Baixo | Médio | Alto |
| **Baixa** | Baixo | Baixo | Médio |

Use esta grade para não deixar a classificação "Nível de Risco Geral" subjetiva — o cruzamento dos dois eixos já informados na matriz determina o nível automaticamente.

### 3. Plano de Ação de Mitigação
Liste de 3 a 4 controles de mitigação por risco, priorizando (nessa ordem) Privilégio Mínimo → MFA → Backup/criptografia. Cada ação deve ter responsável e prazo.

### 3.1. Modo Manual (sem IA) — Auditoria em 3 Checks
Quando a PME não tem acesso a ferramentas automatizadas, conduza a auditoria manualmente em 3 perguntas por ativo:
1. **Check 1 (Identidade)** — O sistema exige usuário e senha individual por colaborador, com MFA ativo?
2. **Check 2 (Privilégio)** — Os computadores que acessam esse ativo rodam com usuário comum (não administrador)?
3. **Check 3 (Continuidade)** — Existe backup automático (HD externo ou nuvem isolada) testado mensalmente?

Qualquer ativo de Criticidade 5 que falhe em ao menos 1 dos 3 checks deve virar ação corretiva imediata, antes de qualquer outro item do checklist de 10 controles.

### 4. Plano de Resposta a Incidentes (PRI) de 1 Página
Sempre que houver um incidente ativo ou o checklist revelar risco Crítico/Alto, gere ou acione o PRI com a raia rápida de 3 etapas:

1. **Contenção** — desconectar cabo de rede / desativar Wi-Fi da máquina afetada **sem desligá-la** (preserva logs em RAM e evita propagação).
2. **Comunicação** — lista de contatos de emergência (provedor de internet, suporte do ERP, CEO, consultoria de segurança).
3. **Restauro** — passos de formatação e restauração a partir do backup em nuvem mais recente validado.

O PRI deve caber em 1 página impressa, ser assinado pelo CEO e fixado fisicamente na sala de TI.

### 5. Reporte no CD-TI Lite
Condense checklist + matriz de risco + PRI em um resumo de 1 página para a reunião quinzenal: quantos dos 10 controles estão implementados, quais riscos Críticos/Altos estão pendentes, e o pedido de verba/ação necessário.

## FREQUÊNCIA E DONOS

| Ritual | Frequência | Dono |
|:---|:---|:---|
| Checklist dos 10 controles | Semestral (ou no Dia 1 da Fase Zero) | Gestor de TI |
| Teste de restauração de backup | Trimestral | Gestor de TI, com evidência apresentada no CD-TI Lite |
| Revisão de matriz de risco de ativos críticos | A cada novo ativo crítico ou incidente | Gestor de TI |
| PRI (ativação) | Sob demanda, no momento do incidente | Gestor de TI + CEO (comunicação) |
| Reporte consolidado de segurança | Quinzenal/mensal, junto ao CD-TI Lite | Gestor de TI, aprovação do CEO |

## DIRETRIZES ANTI-ALUCINAÇÃO

- Não assuma a existência de firewalls de borda caros ou SOC de monitoramento na PME, salvo se o usuário mencionar explicitamente.
- Não invente nomes de malwares ou vulnerabilidades de dia-zero complexas de forma teórica — foque em riscos reais e recorrentes de PME (phishing, vazamento de credenciais, ransomware por engenharia social, servidor sem patch).
- Não marque um controle como "Implementado" sem que o usuário tenha descrito a evidência prática (não basta a intenção).
- Quando faltar dado técnico, sempre registre a lacuna explicitamente em vez de estimar ("Aviso: requer auditoria local física do profissional de TI para verificar [X]").

## FONTES NO FRAMEWORK

| Artefato | Caminho | Uso nesta skill |
|:---|:---|:---|
| Guia do Pilar 3 (conceitual) | `GP-PME antigravity/Guides/Guia_Pilar_3_Seguranca_Critica.md` | Fundamentação NIST-Lite, os 4 controles-núcleo, estrutura Identificar/Proteger/Responder |
| Prompt de Análise de Risco | `GP-PME antigravity/Templates/Prompts/Template_Prompt_Risco.md` | Estrutura da matriz de risco (tabela) + roteiro de auditoria manual em 3 checks |
| Checklist dos 10 Controles | `SKill folder/SKill folder/gp-pme/templates/modulo3_10_controles_criticos.md` | Tabela oficial dos 10 controles críticos mínimos (passo 1 do fluxo) |
| Higiene Cibernética | `SKill folder/SKill folder/gp-pme/templates/modulo3_checklist_higiene_cibernetica.md` | Checklist complementar de boas práticas para colaboradores |
| Plano de Resposta a Incidentes | `SKill folder/SKill folder/gp-pme/templates/modulo3_plano_resposta_incidentes.md` | Modelo do PRI de 1 página (passo 4 do fluxo) |
| Template de Análise de Risco | `SKill folder/SKill folder/gp-pme/templates/modulo3_template_analise_risco.md` | Modelo alternativo/preenchível da matriz de risco |

## SAÍDAS ESPERADAS

- **Checklist dos 10 controles** preenchido com status (Implementado/Em Andamento/Não Implementado) e próximos passos por item.
- **Matriz de risco** em tabela Markdown (Risco / Ameaça / Vulnerabilidade / Probabilidade / Impacto / Nível de Risco).
- **Plano de mitigação** com 3-4 ações priorizadas, responsável e prazo.
- **PRI de 1 página** com as 3 etapas (Contenção, Comunicação, Restauro) prontas para impressão.
- **Resumo executivo de 1 página** para o CD-TI Lite, quando solicitado.

## EXEMPLOS

**Exemplo 1 — Auditoria completa:**
> "Rode o checklist de segurança da minha PME. Temos backup em nuvem mas nunca testamos restauração, e todo mundo usa a mesma senha de admin no Windows."
→ Preencher os 10 controles (controle 6 e 8 marcados como "Em Andamento/Não Implementado"), gerar matriz de risco para o cenário de admin compartilhado (risco Crítico: força bruta/malware + ausência de LUA), e propor plano de ação com prazo de 15 dias.

**Exemplo 2 — Análise de um ativo específico:**
> "Nosso ERP SaaS guarda CPF e dados bancários de 5.000 clientes, login é só usuário e senha padrão."
→ Gerar a matriz de risco completa (Risco/Ameaça/Vulnerabilidade/Probabilidade/Impacto/Nível), com MFA como mitigação prioritária, seguindo `Template_Prompt_Risco.md`.

**Exemplo 3 — Incidente em andamento:**
> "Acabamos de identificar um ransomware criptografando arquivos no servidor. O que fazemos agora?"
→ Acionar imediatamente o PRI: instruir desconexão física de rede sem desligar a máquina, acionar lista de contatos de emergência, e iniciar avaliação do backup mais recente para restauro.

**Exemplo 4 — Preparação de pauta para o CD-TI Lite:**
> "Nossa reunião com o CEO é amanhã, preciso de um resumo de segurança."
→ Consolidar: "7 de 10 controles implementados; controles 3 (vulnerabilidades), 9 (firewall) e 10 (treinamento) pendentes; 1 risco Crítico aberto (servidor de arquivos sem MFA); pedido de verba: R$ X para licença de MFA corporativo."

**Exemplo 5 — Onboarding de PME em Nível 0 de maturidade:**
> "Estamos começando do zero, nem sabemos por onde atacar a segurança."
→ Focar exclusivamente nos 4 controles-núcleo do Guia do Pilar 3 (Inventário 80/20, Privilégio Mínimo + MFA, Backup 3-2-1 testado, PRI de 1 página), adiando os demais 6 controles do checklist completo para a próxima janela de maturidade.
