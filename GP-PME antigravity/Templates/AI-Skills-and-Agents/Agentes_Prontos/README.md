# GEAR: contratos de assistência por IA

Esta pasta contém nove contratos copiáveis: coordenação e oito especialidades.
São instruções consultivas, não agentes já ativos nem resultados de validação
do modelo. A IA é opcional em todo o framework e no nível máximo de maturidade.
Os nomes de arquivos anteriores permanecem como compatibilidade.

## Escolher pela tarefa

| Contrato | Uso | Arquivo |
| --- | --- | --- |
| Coordenação do GEAR | Preparar diagnóstico, roteiro de adoção e visão conjunta; encaminhar assuntos à função pertinente. | [abrir](Agente_Orquestrador_Gestor_GP-PME.md) |
| Governança e direção | Preparar pauta, responsabilidades, finalidades e ata de decisão. | [abrir](Agente_Governanca.md) |
| Execução e serviços | Preparar lista de trabalho, diagnóstico de capacidade e resposta a interrupções. | [abrir](Agente_Execucao_Agil.md) |
| Segurança e continuidade | Preparar lacunas de controles, análise contextual e plano de resposta. | [abrir](Agente_Seguranca.md) |
| Indicadores e revisão | Conferir premissas, cálculos e afirmações; preparar registro de revisão humana. | [abrir](Agente_Metricas_e_Auditoria.md) |
| Maturidade com evidências | Apresentar dez perguntas, conferir evidências e preparar ações de melhoria. | [abrir](Agente_Maturidade.md) |
| Adoção inicial | Preparar a agenda de trinta dias e acompanhar evidências e pendências. | [abrir](Agente_Fase_Zero.md) |
| Requisitos e aceite | Preparar PRD, histórias, critérios e proposta de recorte para aprovação. | [abrir](Agente_PRD.md) |
| Instruções de assistência | Preparar, conferir ou adaptar instruções e organizar sua manutenção. | [abrir](Agente_Engenheiro_de_Prompts.md) |

Se o pedido reúne temas, começar por coordenação. O encaminhamento recomenda
uma função; acionamento real depende de ferramentas disponíveis e autorização.
Quatro funções conceituais do método e oito especialistas de software são
formas diferentes de organizar a assistência, sem criar domínios adicionais.

## Configurar uma primeira verificação

1. Selecionar o contrato pertinente e conferir o contexto necessário.
2. Fornecer fontes vigentes, dados autorizados e pessoa que revisa.
3. Inserir a instrução no recurso disponível do provedor ou em um chat.
4. Usar um exemplo fictício ou tarefa delimitada com saída verificável.
5. Conferir recuperação, cálculo, afirmações e efeitos; registrar limites.
6. Decidir o uso e repetir a verificação após mudanças relevantes.

Cada contrato conserva opções Claude Projects, GPT personalizado, chat comum
e Google ADK. Fluxos e permissões do provedor exigem conferência própria. Não
há prazo garantido de instalação ou garantia de grounding. Arquivos PRD e
Prompts existem no pacote ADK; a afirmação antiga de ausência foi corrigida.

## Executar ferramentas e manter contratos

[README ADK](<../../../../agents/gp-pme-adk/README.md>) registra instalação, módulos, credenciais e limites. [Convenções](<../../../../agents/gp-pme-adk/CONVENTIONS.md>) define integração e verificação. Ausência de credenciais da plataforma ou `GPPME_DRY_RUN=1` ativa propostas locais nos adaptadores; conversa ADK ainda depende de acesso ao modelo. Testes locais não comprovam SDK ou efeitos nas plataformas.

Ao mudar uma regra do método, conferir a fonte canônica pertinente e regenerar os contratos com `tools/build_agent_contracts.py`. Ao mudar ferramentas ou variáveis, conferir código e README do pacote. Manter histórico, exemplos e critérios de revisão. A versão de origem foi preservada com hashes antes da reescrita.

[Documentação vigente](<../../../../framework/README.md>) · [Quatro funções](<../../../../framework/templates/prompts-assistencia.md>) · [Revisão humana](<../../../../framework/templates/revisao-ia.md>)
