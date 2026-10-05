---
name: gp-pme-seguranca
description: Use para conferir controles de segurança, mapear risco de dependências, preparar recuperação ou resposta a incidente e resumo para decisão.
---

# GEAR: controles, risco e resposta

Identificador GP-PME preservado para chamadas existentes. Edição editorial 2026.10; escopo consultivo e IA opcional. O método tem três domínios e camadas transversais de adoção, indicadores e maturidade.

## Executar a tarefa

1. Distinguir verificação de controles, análise de dependência, recuperação, incidente ativo ou resumo. Incidente ativo segue para acionamento e decisão apropriados ao ambiente, sem aguardar checklist completo.
2. Consultar verificações complementares locais e evidência de cada controle. Registrar implementado no recorte verificado, em andamento, ausente ou não verificado; intenção não confirma configuração.
3. Identificar serviço, proprietário, ativos, dados e dependências. Conferir impacto, exposição e controles antes de estimar categoria de probabilidade. Classificação só usa critérios acordados, com incerteza.
4. Usar três perguntas iniciais quando útil: identidade/MFA, privilégio e recuperação. Elas ajudam a encontrar lacunas, sem substituir todos os controles. Escolher ações por exposição, consequência e capacidade, sem ordem rígida ou quatro itens obrigatórios.
5. Para PRI, conferir contatos, autoridade, comunicação, preservação de evidências, recuperação e aceite. Contenção concreta exige contexto e alçada; evitar comandos universais de desligar, isolar ou formatar.
6. Registrar frequência de revisão, cobertura, responsável e teste conforme risco e requisito local. Mensal, trimestral ou semestral são opções, sem obrigação normativa do GEAR. O plano precisa ser acessível na crise, em meio adequado.
7. Para resumo, informar cobertura conhecida, lacunas, consequência, alternativa e decisão necessária. Quantidade implementada não é certificação NIST ou CIS IG1.
8. Encerrar a minuta com evidências e ações atribuídas. Investigação fora da capacidade exige encaminhamento a profissional apropriado; orçamento pequeno não reduz a consequência possível.

## Consultar conforme o pedido

- [Segurança e continuidade](<../../../framework/nucleo/seguranca-continuidade.md>): abrir quando a tarefa exigir esse assunto.
- [Inventário de ativos e dependências](<../../../framework/templates/inventario-dependencias.md>): abrir quando a tarefa exigir esse assunto.
- [Risco e continuidade](<../../../framework/templates/risco-continuidade.md>): abrir quando a tarefa exigir esse assunto.
- [Plano breve de resposta a incidente](<../../../framework/templates/incidente.md>): abrir quando a tarefa exigir esse assunto.
- [Testar restauração](<../../../framework/guias/testar-restauracao.md>): abrir quando a tarefa exigir esse assunto.

Lista e grade históricas: [verificações complementares locais](<../../../framework/templates/risco-continuidade.md>). Usar somente com critérios e cobertura explícitos.

As fontes canônicas distinguem referência primária, adaptação e hipótese. Quando a plataforma não acessar os arquivos, solicitar os trechos pertinentes e registrar o limite. Arquivo anexado não garante recuperação correta.

## Entregar e conferir

Entregar artefato adequado ao recorte, dados com origem e período, memória dos cálculos pertinentes, fontes de pesquisa junto à afirmação e lacunas atribuídas. Informação ausente fica como DADO INSUFICIENTE, com próximo passo necessário. Exemplos são fictícios.

Minuta, cálculo e diagnóstico textual não comprovam execução no ambiente. Usar somente ferramentas disponíveis para efeitos autorizados e registrar entrada, resultado e limite. Aprovação, recurso, contenção, comunicação externa, implantação e publicação pertencem à autoridade humana indicada. Revisão por outro modelo é assistência.

[Registro de revisão](<../../../framework/templates/revisao-ia.md>): consultar quando houver saída assistida com efeito material.

## Exemplos fictícios para conferência

### Caso 1

Entrada: Backup em nuvem não testado; senha de administrador compartilhada.

Conferência esperada: Registrar relatos e cobertura desconhecida; conferir contas, privilégios e teste de restauração. Não atribuir probabilidade ou prazo de quinze dias por palavras.

### Caso 2

Entrada: ERP SaaS com CPF e dados bancários de cinco mil clientes; senha padrão.

Conferência esperada: Conferir acesso, MFA, permissões, dados e dependências. Manter hipótese separada de exposição confirmada.

### Caso 3

Entrada: Relato de arquivos sendo criptografados por ransomware.

Conferência esperada: Acionar responsável e autoridade urgentemente, avaliar contenção no ambiente e preservar evidências. Recuperação depende de cópia e serviço verificados.

### Caso 4

Entrada: Preparar resumo para reunião de direção amanhã.

Conferência esperada: Usar somente controles e riscos documentados; sete de dez e verba R$ X do exemplo antigo são cenário fictício, sem preencher a empresa atual.

### Caso 5

Entrada: Começar segurança sem diagnóstico prévio.

Conferência esperada: Começar pelo serviço e lacunas de inventário, acesso, cópia e resposta; demais controles permanecem visíveis, sem adiamento universal.

Concluir quando artefato, evidências disponíveis e pendências tiverem responsável e próximo passo. Campos de decisão ficam para quem tem alçada.
