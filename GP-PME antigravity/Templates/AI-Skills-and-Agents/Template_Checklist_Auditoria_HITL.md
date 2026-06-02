# Template: Checklist de Auditoria Human-in-the-Loop (HITL)

Este é o **Checklist de Auditoria Human-in-the-Loop (HITL)** oficial do framework **GP-PME**. Ele serve como o filtro de segurança final obrigatório aplicável por gestores e profissionais de tecnologia de pequenas e médias empresas antes de homologarem e publicarem qualquer entregável gerado por Inteligências Artificiais Generativas (como códigos-fonte, PRDs ou análises de risco), prevenindo de forma absoluta a introdução de "alucinações" ou falhas técnicas na operação real do negócio.

---

## 📋 Checklist de Auditoria HITL

*Aplique esta lista de verificação para cada documento ou trecho de código produzido pela IA antes de sua aprovação.*

**ID do Entregável**: [ex: PRD-04 / Código ERP-01]  |  **IA Emissora**: [ex: Analista de Execução Ágil]  
**Data da Auditoria**: ___/___/2026  |  **Auditor Humano**: [Nome do Profissional de TI ou PO]

---

### 🛡️ BLOCO 1: RASTREABILIDADE E GROUNDING (CONFORMIDADE)
- `[ ]` **Check 1.1: Sem Dados Inventados (Zero Alucinação)**
  - *O que verificar*: O documento gerado baseia-se apenas nas informações, sistemas, restrições e premissas explicitamente fornecidas no prompt ou contexto do projeto?
  - *Critério de Falha*: O documento cita bancos de dados fictícios, chaves de API imaginárias, rotas ou nomes de cargos inexistentes na empresa.
- `[ ]` **Check 1.2: Citação Direta de Fontes Homologadas**
  - *O que verificar*: As referências a softwares, versões ou infraestruturas mencionam exatamente os ativos listados no **Inventário 80/20** da PME?
  - *Critério de Falha*: A IA propõe o uso de ferramentas de software que a empresa não adquiriu ou de marcas não autorizadas.
- `[ ]` **Check 1.3: Tratamento de Destaques e Gaps ("Dado Insuficiente")**
  - *O que verificar*: Em caso de dados ausentes, a IA utilizou corretamente o marcador estipulado ("DADO INSUFICIENTE: Requer validação do profissional de TI para...") em vez de preencher as lacunas com suposições teóricas?
  - *Critério de Falha*: A IA tomou uma decisão técnica arriscada sobre o sistema (ex: escolheu um método de backup sem confirmar se o servidor possui espaço em disco).

---

### 💻 BLOCO 2: AUDITORIA DE REQUISITOS (PRD)
*(Aplicável a documentos de especificação de funcionalidades)*
- `[ ]` **Check 2.1: Histórias de Usuário Viáveis**
  - *O que verificar*: As histórias de usuário são simples e condizentes com o fluxo de trabalho real dos colaboradores da PME?
  - *Critério de Falha*: A história exige que o vendedor opere um painel excessivamente burocrático que causará gargalos na rotina comercial.
- `[ ]` **Check 2.2: Critérios de Aceitação Testáveis (Dado/Quando/Então)**
  - *O que verificar*: Os critérios de aceitação descrevem testes objetivos do tipo "passa ou não passa" que qualquer pessoa consegue reproduzir na tela do sistema?
  - *Critério de Falha*: Critérios vagos como *"o sistema deve carregar de forma rápida"* ou *"a tela deve ser bonita"*.
- `[ ]` **Check 2.3: Blindagem do Escopo Negativo**
  - *O que verificar*: O PRD possui a seção de Escopo Negativo identificando claramente os recursos de alta complexidade que estão banidos do MVP de 2 semanas?
  - *Critério de Falha*: O escopo está em aberto, abrindo espaço para que o desenvolvedor gaste tempo criando perfumarias técnicas ou relatórios complexos.

---

### 🛡️ BLOCO 3: SEGURANÇA E RESILIÊNCIA (NIST-LITE)
*(Aplicável a análises de risco, planos de ação e códigos-fonte)*
- `[ ]` **Check 3.1: Validação de Privilégio Mínimo (LUA)**
  - *O que verificar*: A recomendação de segurança ou o código gerado segue a política de menor privilégio, garantindo que usuários comuns e rotinas de aplicação não executem como administrador global?
  - *Critério de Falha*: O código exige acesso 'root' ou 'admin' na base de dados para realizar um SELECT simples.
- `[ ]` **Check 3.2: Ativação de MFA e Controles Simples**
  - *O que verificar*: Propostas de segurança evitam firewalls corporativos caros e focam nas correções rápidas e de custo zero (MFA, backup, senhas individuais fortes)?
  - *Critério de Falha*: Recomendações de investimentos dispendiosos incompatíveis com a TI Enxuta.

---

### ⚙️ BLOCO 4: ENGENHARIA DE CÓDIGO (BOILERPLATES)
*(Aplicável a códigos-fonte gerados por IA)*
- `[ ]` **Check 4.1: Placeholder de Lógica de Negócio**
  - *O que verificar*: O código gerado pela IA restringe-se ao esqueleto (boilerplate) estruturado da funcionalidade, contendo rotas e validações de dados corretas, mantendo placeholders claros para que o desenvolvedor humano programe as regras críticas da empresa?
  - *Critério de Falha*: A IA gerou a lógica completa de faturamento ou cálculo matemático crítico sem auditoria, arriscando erros contábeis ocultos.
- `[ ]` **Check 4.2: Tratamento de Erros e Validações Primárias**
  - *O que verificar*: O código de recepção de dados valida as entradas (ex: impede injeções de código ou dados vazios) e trata possíveis quedas de banco de dados sem expor mensagens internas do sistema na tela?
  - *Critério de Falha*: Códigos vulneráveis a SQL Injection ou que exibem caminhos de arquivos do servidor em caso de exceções.

---

## 🏆 Status Final da Auditoria
*   **[  ] APROVADO PARA IMPLANTAÇÃO**: O entregável passou em todos os cheques de verificação sem qualquer sinal de alucinações ou riscos.
*   **[  ] REPROVADO**: Apresenta falhas de rastreabilidade ou técnicos nos itens: [indique os Checks reprovados]. O entregável deve ser devolvido ao assistente de IA com as devidas correções detalhadas.

---

## 🛠️ Como Operar o HITL Manualmente

Para garantir que a auditoria humana ocorra de forma rotineira e eficaz na PME, implemente o seguinte ritual:

1.  **Gargalo de Homologação (Portão de Produção)**: Nenhum código ou PRD gerado por IA pode ser enviado ao programador ou servidor final de produção sem que o **Gestor de TI** abra este checklist Markdown e realize a auditoria física.
2.  **O Ritual dos 5 Minutos**: A verificação dos checks do Bloco 1 e Bloco 2 toma menos de 5 minutos de leitura atenta e protege a empresa contra dias de retrabalho causados por alucinações de inteligência artificial.
3.  **Registro de Conformidade**: Salve cada checklist preenchido como um arquivo `.md` na pasta do respectivo projeto no repositório de documentação de TI. Isso assegura a conformidade histórica e a auditabilidade do processo técnico.
