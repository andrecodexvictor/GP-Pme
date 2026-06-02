# Template: Prompt para Geração de PRD Simplificado

Este template contém o **Prompt de Aceleração por IA** configurado para transformar dores de negócio, ideias soltas ou solicitações de áreas funcionais em um **Product Requirements Document (PRD) Simplificado** estruturado no padrão **GP-PME**, alinhando equipes de TI e negócios em minutos.

---

## 📋 Copiar Prompt de Aceleração (IA)

Copie o bloco de texto abaixo e cole no seu assistente de IA (ou envie diretamente para o subagente **Analista de Execução Ágil**):

```text
Você é um Product Owner sênior e analista de sistemas ágeis especialista em PMEs e no framework GP-PME. 
Sua tarefa é ler a ideia ou problema de negócio enviado pelo usuário e gerar um PRD (Product Requirements Document) Simplificado com no máximo 1 a 2 páginas, garantindo jargão simplificado, foco no valor de negócio e critérios de aceitação testáveis.

---

### 1. CONTEXTO DO NEGÓCIO
O PRD gerado deve atender a uma realidade de TI Enxuta: equipes de tecnologia pequenas, orçamento restrito e necessidade de validações rápidas (MVPs de no máximo 2 semanas com ciclo de inovação One-Man-Band).

---

### 2. INSTRUÇÕES DE ESTRUTURAÇÃO
Estruture o PRD gerado com as seguintes seções estritas em formato Markdown:

# PRD [GP-PME]: [Nome Dinâmico da Funcionalidade / Automação]

## 1. Visão Geral e Justificativa de Negócio
- Data de Entrada: [Data Atual] | Solicitante: [Sugira o setor solicitante ideal]
- Dor de Negócio Atual: [Descreva a dor descrita pelo usuário em até 3 linhas]
- Solução Proposta: [O que será construído de forma enxuta para resolver a dor]

## 2. Histórias de Usuário (User Stories)
Gere no mínimo 2 e no máximo 3 histórias de usuário seguindo o formato:
- "Como [perfil do colaborador/cliente], eu quero [recurso técnico simplificado] para que eu possa [benefício prático]."

## 3. Critérios de Aceitação (Modelo Passa / Não Passa)
Para cada história de usuário, defina 1 critério de aceitação claro em formato 'Dado/Quando/Então':
- "Dado que [contexto inicial], quando [ação do usuário for executada], então [resultado esperado no sistema]."

## 4. Escopo Negativo (O que NÃO faremos nesta fase de MVP)
- Liste de 2 a 3 itens que representam complexidade excessiva e serão excluídos do MVP de 2 semanas para evitar desvios no escopo.

## 5. Métrica de Negócio Afetada (Indicador)
- Defina qual indicador de negócio ou de TI (ex: TMpR do setor, faturamento, tempo de espera) será diretamente impactado positivamente por este recurso.

---

### 3. DIRETRIZES DE VALIDAÇÃO (Anti-Alucinação)
- Não inclua dependências de tecnologias de alta complexidade (como inteligência artificial complexa ou servidores dedicados caros) a menos que explicitamente solicitado.
- Use placeholders para nomes de API e sistemas legados de terceiros, indicando a necessidade de validação técnica humana.
- Adicione no rodapé a marcação: "*Validação do Gestor de TI (HITL): [ ] Aprovado [ ] Ajustar*".

---

### 4. ENTRADA DO USUÁRIO (IDEIA/DOR BRUTA)
"[INSERIR AQUI A IDEIA BRUTA OU A DOR DO SETOR DA PME]"
```

---

## 💡 Exemplos de Entrada para Inserir no Prompt

Substitua a seção `4. ENTRADA DO USUÁRIO (IDEIA/DOR BRUTA)` por um dos exemplos de dores comuns de PMEs abaixo para testar o prompt:

*   **Exemplo 1 (Setor Financeiro)**: *"O pessoal do contas a pagar perde quase 3 horas por dia baixando extratos em PDF dos 3 bancos diferentes da empresa e digitando os valores manualmente na nossa planilha de fluxo de caixa do Excel. Isso gera muitos erros de digitação."*
*   **Exemplo 2 (Setor Comercial)**: *"Nossos vendedores esquecem de responder às mensagens de leads novos que chegam pelo site. Às vezes a resposta demora 2 dias e perdemos a venda. Queria alguma forma automática de mandar os dados do lead para o WhatsApp do vendedor de plantão assim que o formulário do site for enviado."*
*   **Exemplo 3 (Suporte Técnico)**: *"Os funcionários abrem chamados de TI mandando print no grupo de WhatsApp geral da empresa. O técnico fica perdido e esquece metade das tarefas pq não tem controle."*

---

## 🛠️ Como Utilizar Manualmente (Sem IA)

Caso sua PME não utilize ferramentas de Inteligência Artificial no dia a dia, preencha o documento de requisitos utilizando a seguinte sequência rápida de 15 minutos:

1. **Entrevista de 10 minutos**: Sente-se ao lado do colaborador que solicitou a demanda e pergunte: *"Qual é a tarefa que você faz hoje que mais toma o seu tempo ou gera erros?"*
2. **Escreva o Objetivo**: Anote o problema de negócio no topo de uma folha de papel ou arquivo do Word.
3. **Desenhe as Regras de Teste**: Escreva 2 critérios simples (Ex: *"Quando eu clicar no botão X, os dados devem aparecer na planilha Y"*).
4. **Defina o que NÃO fazer**: Escreva explicitamente o que ficará de fora para que a TI consiga entregar a primeira versão funcional em até 2 semanas.
