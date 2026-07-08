---
name: gp-pme-prd
description: Use esta skill quando o usuário pedir para gerar, revisar ou validar um PRD (Product Requirements Document) no padrão GP-PME de 1-2 páginas para uma PME. Gatilhos: "escreva um PRD", "documente essa demanda", "user stories dessa funcionalidade", "critérios de aceitação", "escopo negativo", "gerar requisitos para o MVP", "valide esse PRD", "dado/quando/então".
---

# Skill: GP-PME · PRD Simplificado (Pilar II)

Motor enxuto que gera ou valida o **PRD Simplificado do GP-PME** — documento de 1 a 2 páginas que traduz uma dor de negócio em um MVP entregável em até 2 semanas. A disciplina central desta skill é o **Escopo Negativo**: cortar agressivamente tudo que não cabe no MVP de 2 semanas, e não os critérios de aceitação vagos.

## QUANDO USAR

1. **Geração de PRD a partir de uma dor de negócio** — "o financeiro perde 3h/dia baixando extratos manualmente, documenta isso pra mim".
2. **Estruturação de uma ideia solta em requisitos testáveis** — "quero automatizar o envio de leads pro WhatsApp do vendedor".
3. **Validação/revisão de um PRD já escrito** — "revisa esse PRD e me diz se está faltando escopo negativo ou critério de aceitação".
4. **Preparação de reunião rápida de 15-20 min entre negócio e TI** — estruturar a pauta da entrevista antes de escrever o documento.
5. **Checkpoint HITL antes de enviar para desenvolvimento** — confirmar que todas as 7 seções estão completas e assináveis.

Não gere PRDs de múltiplas páginas com escopo amplo — se a demanda não cabe em um MVP de 2 semanas, o trabalho correto é quebrar em mais de um PRD, não estender o documento.

## FLUXO PASSO A PASSO

### 1. Entrevista de 10 minutos (extrair a dor real)
Pergunte ao usuário: *"Qual é a tarefa que você faz hoje que mais toma tempo ou gera erros?"* Não pule direto para solução técnica — capture o problema em até 3 frases antes de propor o que construir.

### 2. Preencher as 7 seções do PRD, nesta ordem

| # | Seção | Conteúdo mínimo obrigatório |
|:-:|:---|:---|
| 1 | Visão Geral e Valor de Negócio | Data, dono do produto, técnico executor, dor de negócio (≤3 frases), objetivo do MVP |
| 2 | Histórias de Usuário | 2 a 3 histórias no formato "Como [perfil], eu quero [recurso] para que eu possa [benefício]" |
| 3 | Critérios de Aceitação | 1+ cenário por história, formato Given/When/Then ("Dado que... Quando... Então...") |
| 4 | Escopo Negativo | 2 a 3 itens explicitamente excluídos do MVP (a seção mais importante — ver passo 3) |
| 5 | Requisitos Não Funcionais | Limites de desempenho, segurança (autenticação/LUA) e usabilidade |
| 6 | Métrica de Negócio Afetada | Qual KPI (TMpR, faturamento, tempo de espera etc.) o MVP deve mover — conecta com `gp-pme-metricas` |
| 7 | Aprovações e Fluxo HITL | Checkbox de validação técnica + assinatura do aprovador de negócio |

### 3. Aplicar a "borracha" no Escopo Negativo
Esta é a etapa disciplinadora do fluxo: para cada recurso "seria legal ter", pergunte *"isso atrasa a entrega para além de 2 semanas?"* — se sim, joga para o Escopo Negativo, não para dentro do MVP. Exemplos recorrentes a excluir por padrão: integrações com sistemas legados de terceiros, relatórios/dashboards gráficos (preferir tabela simples), app mobile dedicado (preferir web responsiva).

### 4. Validar critérios de aceitação como testes, não como descrições
Cada critério deve ser verificável objetivamente ("Dado que o campo CPF está vazio, quando o usuário envia o formulário, então o sistema bloqueia o envio e mostra alerta") — se não dá para marcar passa/não passa, reescreva.

### 5. Checklist de validação final (antes de considerar o PRD pronto)
- [ ] Dor de negócio cabe em 3 frases e não menciona solução técnica prematura?
- [ ] Todas as histórias de usuário têm critério de aceitação Given/When/Then?
- [ ] Escopo Negativo tem no mínimo 2 itens reais (não vazio)?
- [ ] Métrica de negócio afetada está nomeada (não genérica)?
- [ ] Campo de aprovação HITL está presente ("[ ] Aprovado [ ] Ajustar")?

Se qualquer item falhar, o PRD não está pronto para virar tarefa no Kanban (`gp-pme-kanban`).

## FONTES NO FRAMEWORK

| Artefato | Caminho | Uso nesta skill |
|:---|:---|:---|
| Template de PRD Completo | `GP-PME antigravity/Templates/PRDs/Template_PRD_Completo.md` | Estrutura oficial das 7 seções + guia de preenchimento manual em 4 passos |
| Prompt de Geração de PRD | `GP-PME antigravity/Templates/Prompts/Template_Prompt_PRD.md` | Prompt de aceleração por IA, diretrizes anti-alucinação e exemplos de dores reais de PME |

## SAÍDAS ESPERADAS

- **PRD completo em Markdown** com as 7 seções preenchidas, pronto para colar em ferramenta de gestão ou imprimir.
- **Lista de itens em Escopo Negativo** explicitados (nunca uma seção vazia).
- **Critérios de aceitação testáveis** no formato Given/When/Then, um por cenário relevante.
- Quando em modo de **validação** (revisão de PRD existente): lista de lacunas encontradas por seção, não um novo documento do zero.

## EXEMPLOS

**Exemplo 1 — Geração a partir de dor bruta:**
> "Os vendedores esquecem de responder leads novos do site, às vezes demora 2 dias e perdemos a venda."
→ Gerar PRD com objetivo "enviar automaticamente o lead para o WhatsApp do vendedor de plantão"; Escopo Negativo deve excluir CRM completo e relatórios de conversão; métrica afetada: tempo médio de primeiro contato.

**Exemplo 2 — Validação de PRD existente:**
> "Escrevi esse PRD mas acho que está faltando alguma coisa" [cola o texto]
→ Rodar o checklist de validação final; reportar, por exemplo, "Escopo Negativo está vazio — sem isso o MVP corre risco de virar projeto de 2 meses" e "Critério de aceitação da História 2 não é testável, falta o 'Então'".

**Exemplo 3 — Entrevista completa do zero:**
> "Quero automatizar a conciliação de boletos pagos, mas não sei nem por onde começar a documentar."
→ Conduzir a entrevista de 10 min, escrever a dor em 3 frases, gerar as 7 seções, aplicar a borracha no escopo (ex.: excluir integração automática com todos os bancos, manter upload manual de extrato no MVP).
