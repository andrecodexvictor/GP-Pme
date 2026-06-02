# Template: Product Requirements Document (PRD) Completo

Este é o modelo oficial de **PRD Completo** do framework **GP-PME**. Ele foi projetado para conciliar a agilidade de preenchimento (limite estrito de 1 a 2 páginas) com a clareza técnica necessária para que equipes enxutas ou desenvolvedores terceirizados compreendam e entreguem o projeto no prazo máximo de **2 semanas (MVP)**, evitando desvios de escopo comuns.

---

## 🏗️ Modelo de PRD para Preenchimento

*Copie o conteúdo abaixo para iniciar a especificação de uma nova funcionalidade ou sistema.*

```markdown
# PRD [GP-PME]: [NOME DO PROJETO OU FUNCIONALIDADE]

## 1. VISÃO GERAL E VALOR DE NEGÓCIO
- **Data de Solicitação**: DD/MM/AAAA  |  **Versão**: 1.0
- **Dono do Produto (Product Owner)**: [Nome do Gestor/Solicitante]
- **Técnico Executor**: [Nome do Técnico ou Equipe de TI]
- **Dor de Negócio (O Problema)**:
  [Descreva em até 3 frases o problema operacional diário, custo gerado ou tempo perdido atualmente.]
- **Objetivo do MVP (A Solução)**:
  [O que pretendemos construir em até 2 semanas de forma simplificada para erradicar essa dor.]

---

## 2. HISTÓRIAS DE USUÁRIO (USER STORIES)
As histórias abaixo definem os perfis e os benefícios esperados na prática:

*   **História 1**: Como [perfil do colaborador - ex: Vendedor], eu quero [funcionalidade técnica simplificada - ex: ver os novos leads no painel do ERP] para que eu possa [benefício de negócio - ex: iniciar o atendimento em menos de 10 minutos].
*   **História 2**: Como [perfil - ex: Cliente Final], eu quero [funcionalidade - ex: receber um link de rastreio automático via SMS] para que eu possa [benefício - ex: acompanhar meu pedido sem precisar ligar no suporte].

---

## 3. CRITÉRIOS DE ACEITAÇÃO (MODELO PASSA / NÃO PASSA)
Os cenários de teste abaixo determinam se a funcionalidade funciona corretamente antes de ir para produção:

*   **Cenário 1: [Nome da Ação Principal]**
    - **Dado que** [contexto inicial - ex: o vendedor está logado no painel e possui 1 novo lead pendente],
    - **Quando** [ação executada - ex: o vendedor clica no botão "Iniciar Atendimento"],
    - **Então** [resultado esperado - ex: o status do lead muda para 'Em Atendimento' e abre a tela de conversa no WhatsApp].

*   **Cenário 2: [Nome do Teste de Segurança ou Desempenho]**
    - **Dado que** [contexto - ex: o usuário tenta enviar o formulário de cadastro],
    - **Quando** [ação - ex: deixa o campo obrigatório 'CPF' em branco e clica em enviar],
    - **Então** [resultado - ex: o sistema impede o envio, exibe um alerta em vermelho e não recarrega a página].

---

## 4. ESCOPO NEGATIVO (O QUE NÃO FAREMOS NO MVP)
Para garantir a entrega do projeto em até **2 semanas**, os seguintes itens estão **EXCLUÍDOS** desta fase e serão reavaliados no futuro:
- *Exclusão 1*: [ex: Integração automatizada com sistemas de faturamento externos].
- *Exclusão 2*: [ex: Relatórios estatísticos e painéis gráficos (usar tabelas simples no banco de dados)].
- *Exclusão 3*: [ex: Aplicativo móvel dedicado (utilizar interface web responsiva no navegador)].

---

## 5. REQUISITOS NÃO FUNCIONAIS (LIMITES OPERACIONAIS)
- **Desempenho**: O carregamento da tela e as consultas principais não devem ultrapassar [ex: 2.0 segundos] sob conexão móvel comum.
- **Segurança**: Autenticação individual via [ex: Usuário e Senha corporativa] e ativação de controle de acessos (LUA).
- **Usabilidade**: Interface adaptada para [ex: celulares e computadores] sem necessidade de manual complexo de treinamento.

---

## 6. MÉTICA DE NEGÓCIO AFETADA (KPI DO PROJETO)
O sucesso da entrega técnica deste projeto será medido diretamente pelo impacto no indicador:
*   [ ] **Métrica de Negócio**: [ex: Redução de 20% no tempo médio de primeiro contato com o lead / Aumento de 5% no faturamento do setor].

---

## 7. APROVAÇÕES E FLUXO HITL (HUMAN-IN-THE-LOOP)
- **Validação Técnica (TI/QA)**: [  ] Aprovado  [  ] Necessita Ajustes  |  Data: ___/___/___
- **Assinatura do Aprovador (PO/Negócios)**: _____________________________________________
```

---

## 📋 Como Preencher Manualmente (Passo a Passo)

Caso opte por preencher o PRD de forma manual em reuniões rápidas de 20 minutos com a equipe de negócios e TI, siga este fluxo simplificado:

1.  **Foco na Dor Real (Seção 1)**: Não comece discutindo código ou banco de dados. Escreva exatamente o que está incomodando a empresa (ex: *"Perdemos 2 dias para conciliar boletos pagos"*).
2.  **Crie os Testes Antes do Código (Seção 3)**: Descreva em português claro como o usuário vai testar a entrega física. Se o teste passar, o projeto é considerado concluído.
3.  **Use a Borracha no Escopo (Seção 4)**: Esta é a seção mais importante de todas. Seja extremamente rígido em remover tudo o que for perfumaria ou complexidade. Se um recurso atrasar a entrega para além de 2 semanas, **jogue-o para o Escopo Negativo**.
4.  **Assine no Papel (Seção 7)**: O hábito da assinatura e da validação técnica e de negócio gera responsabilidade compartilhada e evita o retrabalho.
