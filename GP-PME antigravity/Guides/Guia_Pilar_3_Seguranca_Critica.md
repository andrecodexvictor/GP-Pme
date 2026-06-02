# Guia do Pilar 3: Segurança Crítica (NIST-Lite)

**Autor**: Antigravity AI (sob a direção de Andre Victor)
**Versão**: 5.2 (Consolidada - Filosofia TI Enxuta Integrada)
**Data**: 02 de Junho de 2026

---

## 1. Introdução ao Pilar 3: Segurança Crítica

O Pilar 3 protege os ativos digitais da PME contra as ameaças de segurança cibernética mais severas e comuns do mercado (sequestro de dados por ransomware, roubo de credenciais e golpes de phishing). Baseado em simplificar as funções da norma **NIST CSF 2.0** e as defesas prioritárias do **CIS Controls v8 (Grupo de Implementação 1 - IG1)**, este pilar estabelece o modelo **NIST-Lite**.

### A Segurança na TI Enxuta (Bússola de Crescimento Seguro)
Na TI Enxuta, a segurança não é vista como um conjunto de barreiras burocráticas ou auditorias intermináveis que travam a agilidade comercial da empresa. Pelo contrário:
*   A segurança cibernética atua como a **bússola e o alicerce para o crescimento seguro e sustentável**.
*   À medida que as Fases 1 (Orquestração do Valor) e 2 (Laboratório de Inovação) são consolidadas, o faturamento e a exposição ao risco digital da PME aumentam de forma acelerada.
*   O framework NIST-Lite é ativado para mapear e mitigar os riscos mais críticos do negócio utilizando controles de baixíssimo custo e alta eficácia técnica. Isso garante que a inovação rápida gerada no laboratório seja blindada, evitando incidentes catastróficos que poderiam arruinar a saúde financeira da PME.

Todos os controles deste pilar são **100% operáveis de forma manual** por meio de planilhas de controle local, rotinas nativas nos sistemas operacionais da PME (sem custos adicionais) e checklists físicos para situações de emergência. A IA Generativa é integrada como um Pilar Transversal Opcional de apoio e auditoria de políticas.

---

## 2. A Estrutura de Controles Mínimos do NIST-Lite

A cibersegurança do GP-PME é simplificada em torno de 4 controles essenciais que geram a máxima proteção com o menor esforço e custo possíveis:

```
[ IDENTIFICAR ] -> Inventário 80/20 (Planilha Manual de Ativos Críticos)
      |
      +---> [ PROTEGER ] -> Privilégio Mínimo (MFA ativo, sem login Admin)
      |
      +---> [ PROTEGER ] -> Backups Diários Cloud (Testados a cada 3 meses)
      |
      +---> [ RESPONDER ] -> PRI de 1 Página (Checklist de Crise Físico)
```

---

## 3. Detalhamento e Operação dos 4 Controles Manuais

### 3.1. Inventário 80/20 de Ativos Críticos (Identificar)
Tentar mapear 100% da rede e computadores de uma empresa de forma contínua é inviável para equipes enxutas. O GP-PME foca na Regra de Pareto: registrar em uma planilha simples apenas os **20% dos ativos e servidores de dados que, se pararem, paralisam 80% do faturamento da empresa** (ex: o banco de dados do ERP, o computador do faturamento, contas administrativas na nuvem). 

*(Consulte o arquivo [Templates_GP-PME.md](file:///c:/Users/adm/Desktop/GP-PME%20framework/GP-PME%20antigravity/Templates_GP-PME.md) para o modelo pronto).*

### 3.2. Princípio do Privilégio Mínimo e MFA (Proteger)
*   **Privilégio Mínimo (LUA - Least User Access)**: Remover as permissões de "Administrador local" das contas de computadores utilizadas pelos colaboradores no dia a dia. Se uma conta de funcionário sofrer invasão por malware, o vírus não conseguirá se instalar ou se espalhar, pois o sistema operacional exigirá a senha de administrador da TI.
*   **MFA (Autenticação de Dois Fatores)**: Ativação mandatória de confirmação de logins (código por aplicativo de celular ou SMS) em 100% das contas de e-mail e sistemas financeiros da PME.

### 3.3. Backups Automatizados e Testados (Proteger)
*   **Automação**: Configuração de cópias de segurança diárias automáticas dos dados listados no Inventário 80/20 para a nuvem (ex: Google Drive corporativo, AWS S3, OneDrive, etc.).
*   **Testes de Recuperação**: O Gestor de TI deve realizar, a cada **3 meses**, um teste manual prático de restauração de um arquivo excluído de forma fictícia. O sucesso do teste deve ser registrado e apresentado em ata para o CD-TI Lite, garantindo que o backup funcionará em momentos de desastre.

### 3.4. Plano de Resposta a Incidentes (PRI) de 1 Página (Responder/Recuperar)
Um roteiro de emergência visual em formato de checklist de 1 página contendo os passos imediatos a serem seguidos em momentos de desastre hacker:
1.  *Contenção*: Desplugar fisicamente cabos de rede e desativar o Wi-Fi das máquinas afetadas sem desligá-las (evitando alastramento e mantendo logs na memória RAM).
2.  *Comunicação*: Relação contendo contatos emergenciais de provedores, CEO e técnicos parceiros de infraestrutura.
3.  *Restauro*: Etapas de formatação e restauração de dados a partir das mídias de backup em nuvem.

---

## 4. Aceleração Opcional com Inteligência Artificial

Caso a PME adote o **Pilar IV (Aceleração por IA)**, o Gestor de TI pode acionar o **Agente 3: Guardião de Segurança (NIST/CIS)** para acelerar as auditorias de risco:

*   **Auditoria de Configurações de MFA/Contas**: O gestor pode submeter o relatório de permissões dos usuários gerado pelo painel G Workspace ou Microsoft Active Directory à IA especialista, solicitando a identificação imediata de contas ociosas ou usuários que possuam privilégios excessivos na rede.
*   **Geração de Políticas de Segurança para Colaboradores**: O agente de IA pode formular checklists rápidos de higiene cibernética (ex: regras para criação de senhas fortes, alertas contra phishing) em português direto e de fácil leitura para treinamento da equipe da PME.
*   **Simulação de Mesa (Tabletop Simulation)**: A IA pode atuar simulando incidentes de segurança (ex: "Sua PME sofreu um sequestro de banco de dados por Ransomware X. Qual o seu primeiro passo no PRI?"), treinando o Gestor de TI para crises reais de forma interativa.
