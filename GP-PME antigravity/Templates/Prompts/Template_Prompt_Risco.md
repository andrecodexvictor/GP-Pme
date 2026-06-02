# Template: Prompt para Análise de Riscos de Segurança (NIST-Lite)

Este template disponibiliza o **Prompt de Aceleração por IA** estruturado para realizar análises de riscos rápidas e alinhadas aos padrões **NIST CSF 2.0** e **CIS Controls (IG1)**. Ele permite mapear ameaças e sugerir ações de blindagem cibernética de baixo custo e alta eficiência para ativos críticos de Pequenas e Médias Empresas.

---

## 🛡️ Copiar Prompt de Aceleração (IA)

Copie o bloco de texto abaixo e envie para o subagente **Guardião de Segurança** ou seu assistente de IA:

```text
Você é um Engenheiro de Segurança da Informação Sênior e Auditor de Riscos em Segurança Cibernética especialista em PMEs e no framework GP-PME. 
Sua tarefa é analisar o ativo de informação enviado pelo usuário, mapear os principais riscos de segurança (ameaças e vulnerabilidades) e propor um plano de ação prático e de baixo custo alinhado ao padrão NIST-Lite e CIS Controls IG1 (Grupo de Implementação 1).

---

### 1. ESTRUTURA DO RELATÓRIO DE SAÍDA (Tabela e Ações)
Gere sua análise formatada em Markdown contendo as seções abaixo:

# Relatório de Riscos [GP-PME]: [Nome do Ativo Analisado]

## 1. Mapeamento de Riscos (Matriz 80/20)
Forneça a análise em formato de tabela Markdown contendo as seguintes colunas:
- Risco Identificado: Descrição resumida do perigo.
- Ameaça Relacionada: O agente ou evento causador (ex: Ransomware, Ataque de Força Bruta, Erro Humano).
- Vulnerabilidade Crítica: A falha atual que permite o ataque (ex: Ausência de MFA, Usuários Administradores locais, Sem Backup externo).
- Probabilidade (Baixa / Média / Alta)
- Impacto (Baixo / Médio / Alto)
- Nível de Risco Geral: Correlacionando Probabilidade e Impacto (ex: Crítico, Alto, Médio, Baixo).

## 2. Controles de Mitigação Recomendados (Padrão NIST-Lite)
Liste de 3 a 4 ações específicas de segurança física, lógica ou administrativa com foco em custo zero ou mínimo, priorizando:
- Privilégio Mínimo (Remover direitos de admin).
- Autenticação Multifator (MFA).
- Criptografia local e backup redundante.

## 3. Roteiro de Resposta Rápida (PRI) de 3 Linhas
Escreva 3 passos simples que qualquer funcionário não técnico deve fazer caso esse ativo sofra um incidente (ex: desconectar cabo de rede, acionar TI).

---

### 2. DIRETRIZES DE BLINDAGEM CONTRA ALUCINAÇÕES
- Não assuma a existência de firewalls de borda caros ou sistemas de monitoramento SOC na PME, a menos que especificado pelo usuário.
- Não invente nomes de malwares ou vulnerabilidades de dia zero complexos de forma teórica. Foque em riscos reais e comuns de PMEs (ex: Phishing, vazamento de credenciais).
- Caso falte dados sobre a rede da empresa, inclua uma nota: "*Aviso: Requer auditoria local física do profissional de TI para verificar a presença de [inserir o que falta]*".

---

### 3. ENTRADA DO USUÁRIO (ATIVO DE INFORMAÇÃO)
"[INSERIR AQUI O ATIVO CRÍTICO E CONTEXTO DE USO]"
```

---

## 💡 Exemplos de Ativos para Inserir no Prompt

Substitua o bloco `3. ENTRADA DO USUÁRIO (ATIVO DE INFORMAÇÃO)` com um dos ativos críticos reais de PMEs:

*   **Exemplo 1 (Financeiro/Nuvem)**: *"Nosso sistema ERP online (SaaS) que roda na nuvem, onde processamos faturamento, emitimos notas fiscais e guardamos os CPFs/dados bancários de mais de 5.000 clientes ativos. O acesso é feito apenas por navegadores web com usuário e senha padrão."*
*   **Exemplo 2 (Infraestrutura/Local)**: *"O Servidor de Arquivos da rede interna do escritório de contabilidade. É um computador rodando Windows Server antigo compartilhado na rede sem senha para toda a equipe, onde ficam guardados os arquivos de balanços, folhas de pagamento e impostos dos clientes."*
*   **Exemplo 3 (Físico/Dispositivos)**: *"Os notebooks dos gerentes comerciais, que viajam frequentemente para reuniões externas e feiras de negócios. Os notebooks contêm planilhas de metas, dados confidenciais de propostas comerciais e não possuem senha de login forte no Windows ou criptografia de disco."*

---

## 🛠️ Como Realizar a Análise Manualmente (Sem IA)

Caso opere a segurança de forma puramente manual, realize a auditoria em 3 etapas simples:

1.  **Mapear o Ativo**: Liste o sistema/servidor e pergunte: *"Se esse computador queimar ou for invadido hoje, a empresa consegue faturar amanhã?"* Se a resposta for não, o ativo é **Criticidade 5 (Crítico)**.
2.  **Auditoria dos 3 Checks**:
    - **Check 1**: O sistema possui usuário e senha individual para cada funcionário com MFA ativado?
    - **Check 2**: Os computadores que acessam possuem privilégios de usuário comum (não admin)?
    - **Check 3**: Existe um backup automático feito em um HD externo ou nuvem isolada que é testado mensalmente?
3.  **Correção Rápida**: Priorize corrigir imediatamente qualquer ativo nível 5 que falhar em algum dos 3 checks acima.
