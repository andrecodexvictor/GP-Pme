# Agentes e ferramentas GEAR

O [pacote ADK](gp-pme-adk/README.md) contém um orquestrador e oito especialistas. Os quatro papéis conceituais da [assistência por IA](../framework/guias/usar-ia.md) são funções do método, não uma contagem de módulos.

Maturidade e finanças delegam ao [núcleo comum](../server/core.py). Módulos, variáveis `GPPME_*` e nomes de ferramentas continuam compatíveis. Editar regras nos documentos canônicos e no núcleo, depois testar consumidores.

Cinco adaptadores oferecem modo simulado sem rede. WIP inclui testes e bloqueios; sem executor informado, o diagnóstico não atesta capacidade individual. Execução real depende de configuração e autorização para os efeitos previstos.

A [revisão de saídas](../framework/templates/revisao-ia.md) exige evidência e responsabilidade humana. Relatório do agente não comprova mudança realizada. IA permanece opcional em toda a maturidade.

Verificação local: `npm run test`. A suíte existente em pytest requer suas dependências de desenvolvimento. Testes simulados não comprovam integração real com contas externas.
