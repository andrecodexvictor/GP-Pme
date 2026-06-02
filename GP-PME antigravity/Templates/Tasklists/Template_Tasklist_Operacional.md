# Template: Lista de Tarefas Operacional (Tasklist)

Esta é a **Lista de Tarefas Operacional (Tasklist)** oficial do framework **GP-PME**. Ela serve como um roteiro prático e acionável para planejar, executar e monitorar qualquer projeto de implantação tecnológica de curto prazo (como um MVP de 2 semanas) ou rotinas recorrentes de TI, garantindo a rastreabilidade das ações e o critério rigoroso de validação técnica.

---

## 🏗️ Modelo de Tasklist de Sprint / Projeto

*Copie a estrutura abaixo para organizar as entregas técnicas da sua equipe.*

```markdown
# Tasklist: [NOME DO PROJETO OU SPRINT]

**Período**: DD/MM/AAAA a DD/MM/AAAA  |  **Responsável Geral**: [Nome do Gestor de TI]

---

## 📋 Legenda de Acompanhamento
- `[ ]` **Tarefa Não Iniciada**: Atividade planejada aguardando início.
- `[/]` **Tarefa Em Andamento**: Trabalho ativamente sendo executado.
- `[x]` **Tarefa Concluída**: Atividade concluída e validada com sucesso.

---

## FASE 1: PREPARAÇÃO E AMBIENTE (Semana 1 - Dias 1 a 5)

- `[ ]` **Tarefa 1.1: [Nome Curto da Tarefa]**
  - **Ação**: [O que deve ser feito fisicamente - ex: Configurar o banco de dados no provedor de nuvem]
  - **Responsável**: [Nome do Executor / Técnico]
  - **Critério de Validação**: [O teste prático que comprova a entrega - ex: Acesso realizado com sucesso a partir de IP externo autorizado]
  
- `[ ]` **Tarefa 1.2: [Nome Curto da Tarefa]**
  - **Ação**: [ex: Criar repositório privado no GitHub e convidar os membros da equipe]
  - **Responsável**: [Nome]
  - **Critério de Validação**: [ex: Repositório acessível por todos os membros com permissões corretas]

---

## FASE 2: DESENVOLVIMENTO E IMPLANTAÇÃO (Semana 2 - Dias 6 a 10)

- `[ ]` **Tarefa 2.1: [Nome Curto da Tarefa]**
  - **Ação**: [ex: Desenvolver a tela de formulário de contato responsiva]
  - **Responsável**: [Nome]
  - **Critério de Validação**: [ex: Testado em dispositivos móveis e desktop, validando campos de e-mail e telefone]

- `[ ]` **Tarefa 2.2: [Nome Curto da Tarefa]**
  - **Ação**: [ex: Implementar rotina de envio de e-mails via API de terceiros]
  - **Responsável**: [Nome]
  - **Critério de Validação / Anti-Hallucination**: [ex: O e-mail chega na caixa de entrada em até 10 segundos sem simular envios fictícios no console]

---

## FASE 3: AUDITORIA, SEGURANÇA E HITL (Dias 11 a 12)

- `[ ]` **Tarefa 3.1: Auditoria de Segurança e MFA (NIST-Lite)**
  - **Ação**: [ex: Validar as regras de acesso à base de dados, remover permissões de admin de teste e ativar MFA nos logins de administração]
  - **Responsável**: [Gestor de TI]
  - **Critério de Validação**: [ex: Tentativa de login sem MFA bloqueada; permissões revisadas conforme o Inventário 80/20]

- `[ ]` **Tarefa 3.2: Homologação com Usuário Final (HITL)**
  - **Ação**: [ex: Apresentar o recurso funcionando ao solicitante da área de negócios para teste real]
  - **Responsável**: [Product Owner / Gestor]
  - **Critério de Validação**: [ex: Assinatura física ou digital do PRD no campo de validação de entregáveis]

---

## FASE 4: PUBLICAÇÃO E ENCERRAMENTO (Dias 13 a 14)

- `[ ]` **Tarefa 4.1: Publicação em Produção e Backup**
  - **Ação**: [ex: Publicar o sistema no servidor final e gerar backup de segurança manual imediatamente após o deploy]
  - **Responsável**: [Técnico de TI]
  - **Critério de Validação**: [ex: Backup armazenado na nuvem redundante verificado e sistema operacional funcionando no link oficial]
```

---

## 📋 Como Criar e Operar uma Tasklist Manualmente

Para garantir que a lista de tarefas funcione como uma ferramenta de gestão ativa na sua PME e não apenas como um documento estático esquecido na gaveta, siga estes 4 princípios:

1.  **Foco em Validação Prática (O Coração da Tasklist)**: Nunca crie uma tarefa sem definir seu **Critério de Validação**. Dizer *"Desenvolver funcionalidade de pagamentos"* é inútil. Dizer *"Realizar 1 transação de teste com cartão de crédito e verificar se o saldo caiu na conta de teste em menos de 10 segundos"* é operacional e passível de auditoria.
2.  **O Poder das Três Marcações**:
    - Use `[ ]` para planejar tudo o que é necessário.
    - Use `[/]` obrigatoriamente quando estiver focado em uma tarefa. Isso evita o vício de iniciar 5 atividades em paralelo e não terminar nenhuma (respeitando o conceito de **WIP Limit de 3** do Pilar II).
    - Use `[x]` somente quando a tarefa passar no critério de validação.
3.  **Auditorias de Segurança e HITL como Fases Obrigatórias**: Todo projeto de TI, por menor que seja, deve possuir uma fase dedicada a segurança (NIST-Lite) e validação pelo usuário final (HITL - Human-in-the-loop). Isso previne vazamentos de dados de clientes e retrabalho de desenvolvimento.
4.  **Revisão Rápida de 5 Minutos (Daily)**: Se você possui um técnico de TI ou parceiro terceirizado, gaste 5 minutos no início do dia olhando para a Tasklist e perguntando: *"Quais itens estão com `[/]` hoje e o que precisamos fazer para movê-los para `[x]`?"*
