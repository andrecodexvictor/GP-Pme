# Tarefas e critérios de conclusão

Edição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.

## Origem e decisão editorial

Os checkboxes antigos não tinham evidência de execução em empresa e foram substituídos por modelos não preenchidos. Teste de restauração usa cópia e ambiente autorizados, sem apagar arquivo real para demonstrar o método. Convite aceito, assinatura de plano e movimentação de cartão não comprovam governança, continuidade ou efeito. Itens bloqueados permanecem no histórico e no WIP quando iniciados.

## Lista de tarefas e verificação

Use para uma mudança ou rotina que precise de passos atribuídos. TI organiza dependências e capacidade; executor registra resultado; dono do processo aceita o efeito pertinente. A lista complementa o quadro, sem criar uma segunda fila divergente.

### Preparar o recorte

- Iniciativa/rotina, período e responsável geral: [preencher]
- PRD ou decisão que autoriza, escopo e exclusões: [preencher]
- Permissões, dependências, ambiente e condição de retorno: [preencher]

| ID e ação | Executor | Dependência | Estado | Critério e modo de verificar | Resultado/evidência |
| --- | --- | --- | --- | --- | --- |
| [preencher] | | | [A Fazer/Em Andamento/Em Teste/Concluído] | | |

Bloqueio ou suspensão: [item, motivo, início, responsável pela próxima ação e revisão]. Manter o relógio e o histórico de trabalho iniciado. Contar andamento, teste e bloqueio comprometido no WIP por executor; marcar início de tarefa não cria capacidade adicional.

### Opções de organização

Agrupar por preparação e ambiente; desenvolvimento ou configuração; verificação técnica e de negócio; disponibilização e acompanhamento. Essas são opções do modelo antigo, sem impor quatro fases ou quatorze dias a toda atividade. Segurança e requisitos podem precisar de conferência antes da execução, não apenas ao final.

- Preparação: verificar acesso e dependências em ambiente autorizado.
- Implementação: executar o recorte acordado e guardar alterações.
- Verificação: testar critérios, acesso, falhas relevantes e retorno conforme o efeito.
- Disponibilização: confirmar autorização, comunicação, operação e acompanhamento.

Exemplos fictícios de critérios: membros autorizados acessam um repositório e demais não; um formulário informa um campo obrigatório ausente; mensagem de teste chega ao destino autorizado. Definir ambiente, amostra e prazo necessários; a antiga referência a dez segundos não é padrão de pagamentos ou e-mail. Mensagem de console não comprova recebimento externo.

### Encerrar e revisar

Registrar teste realizado, pessoa que verificou, aceite ou motivo de encerramento. Uma assinatura registra aprovação, sem substituir teste. Nem toda tarefa exige publicação ou implantação. Guardar pendências e condição de revisão posterior do benefício.

As marcações antigas `[ ]`, `[/]` e `[x]` podem ser mantidas como legenda em ferramentas que as suportem. Elas não representam sozinhas teste, bloqueio ou aceite; conservar esses campos explicitamente. Não apresentar `[/]` como checkbox Markdown padrão.

Saída: lista atualizada vinculada ao quadro. Concluir quando resultados e pendências são localizáveis, com responsável. Referência de uso: [entregar melhoria](<../framework/guias/entregar-melhoria.md>). Próximo modelo: [PRD e aceite](<../framework/templates/prd-aceite.md>).


## Preparar a adoção e distribuir as primeiras ações

Use este roteiro quando direção e TI já concordaram em tornar a rotina visível. Ele conserva o início em duas horas e os nove passos dos guias antigos como opções de planejamento. Durações e dias são parâmetros locais; confirmar disponibilidade, permissões e responsáveis antes de usá-los.

### Uma preparação de duas horas

O resultado esperado é um primeiro conjunto de registros e pendências. A preparação não comprova implantação, recuperação ou maturidade. Se houver incidente ou risco urgente, sua resposta pode alterar a agenda.

| Janela sugerida | Ação | Saída a conferir |
| --- | --- | --- |
| Primeiros 30 minutos | Escolher registro oficial e meio alternativo quando indisponível | Canal, responsável por captura e comunicado de transição |
| Próximos 30 minutos | Criar quadro e registrar demandas conhecidas | Solicitante, executor, situação, prioridade e lacunas |
| Próximos 30 minutos | Examinar prioridades com autoridade do negócio | Até três problemas escolhidos com motivo e capacidade |
| Últimos 30 minutos | Preparar contatos e alçadas de resposta | Minuta de PRI, contatos conferidos e pendências atribuídas |

Demandas recebidas por telefone ou conversa continuam acessíveis ao registro; uma emergência não aguarda o formulário. Não apagar tarefas por classificação de quadrante. Registrar recusa, adiamento ou pedido de informação com motivo. Contatos não fornecidos ficam pendentes. Imprimir o PRI pode ajudar no acesso durante indisponibilidade, mas seu conteúdo e autoridade precisam ser conferidos.

Limite inicial: até três itens iniciados por executor, incluindo teste e bloqueio sob sua responsabilidade. Uma equipe de uma pessoa concentra a execução em uma atividade de cada vez. Se a captura das demandas não terminar na janela, registrar cobertura e plano de continuação.

### Nove passos em uma janela de 30 dias

O percurso detalha os [primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>). Os intervalos conservam a sequência histórica; alterar a ordem conforme dependências e risco. Segurança não precisa aguardar a segunda semana. Registrar mudança de data com motivo.

| Intervalo proposto | Ação | Evidência esperada |
| --- | --- | --- |
| Dias 1–2 | Aplicar maturidade e discutir problemas observados | Respostas com evidência, lacunas e prioridades atribuídas |
| Dias 3–5 | Organizar quadro e capacidade | Demandas conhecidas migradas; testes e bloqueios visíveis |
| Dias 6–7 | Comunicar registro oficial e alternativa | Pessoas sabem pedir ajuda e acompanhar a situação |
| Dias 8–10 | Preparar orientações recorrentes | FAQ testada por usuário, responsável e revisão combinada |
| Dias 11–14 | Mapear dependências críticas e testar restauração | Inventário inicial, requisitos de recuperação, resultado e limites |
| Dias 15–18 | Conferir e exercitar resposta | Contatos, alçadas, comunicação e lacunas do PRI |
| Dias 19–21 | Rever prioridades com o negócio | Decisões, recursos, responsáveis e próxima verificação |
| Dias 22–25 | Coletar indicadores úteis | Origem, janela, unidade, amostra e lacunas |
| Dias 26–30 | Comparar registros e planejar continuidade | Ações mantidas, ajustadas ou adiadas; próxima revisão |

Cinco orientações podem ser um começo para a FAQ, quando houver cinco necessidades recorrentes conhecidas. A quantidade não é critério de conclusão. Testar permissões e instruções de acesso; não fornecer credenciais no documento.

### Assistência opcional em cada etapa

TI pode pedir uma minuta de quadro, orientação, PRI, pauta ou relatório a uma ferramenta de IA com dados autorizados. A ferramenta pode organizar evidências fornecidas; não responde maturidade por suposição nem inventa contatos. Toda configuração real e integração exigem autorização, teste e revisão compatíveis com o efeito.

Para indicadores, usar cálculo determinístico e conferir unidades. Para FAQ ou bot, oferecer encaminhamento humano e medir resolução confirmada. O tempo total inclui preparação, conferência e correção. Sem IA, executar o mesmo roteiro com pessoas, quadros e registros.

### Encerrar a janela

TI apresenta registros e limitações; dono do processo confirma o que foi verificado; direção decide continuidade e risco. Pendências têm responsável e nova data. Não emitir certificação automática de nível 1 nem exigir DAN, nuvem, IA ou um projeto novo para encerrar a adoção inicial.

Fundamento conceitual de cobertura de riscos: NIST [F01](<../framework/referencias/fontes.md#f01>). Agenda, número de passos e janelas são propostas locais, sem garantia de resultado no período.

Anterior: [Primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>). Consulta: [Maturidade](<../framework/adocao/maturidade.md>) e [comparação da rotina](<../framework/indicadores/negocio-comparacao.md>).


## Inventário de ativos e dependências

Use para compreender o que sustenta um serviço e preparar sua proteção e recuperação. Dono do serviço define impacto; TI verifica dependências; proprietário confirma responsabilidade. Começar pelos serviços críticos e registrar cobertura parcial. Criticidade não se deduz do cargo de quem usa o equipamento.

### Serviço e cobertura

- Serviço/processo, proprietário e data de revisão: [preencher]
- Consequência da indisponibilidade e evidência: [preencher]
- RTO e RPO acordados, com justificativa: [preencher]
- Escopo inventariado, lacunas e responsável pela ampliação: [preencher]

| ID e ativo/dependência | Tipo e localização | Proprietário e fornecedor | Criticidade/motivo | Dados e acesso necessários |
| --- | --- | --- | --- | --- |
| [preencher] | | | | |

| ID | MFA/acesso: evidência e exceção | Cópia: frequência e retenção | Recuperação: teste e limite | Ação, responsável e prazo |
| --- | --- | --- | --- | --- |
| [vincular ao ativo] | | | | |

Registrar referência à evidência com acesso adequado; não guardar senhas ou chaves neste modelo. “MFA ativo” exige configuração verificada e escopo declarado. “Backup ativo” exige identificar solução, fonte e retenção; teste de arquivo não comprova recuperação de todo o serviço.

Se for usada criticidade de 1 a 5, definir cada faixa e exemplos com o dono do processo. A escala é local e não mede porcentagem de risco. Dependências de um ativo crítico podem precisar de tratamento mesmo quando seu uso parece secundário.

### Conferir e atualizar

TI compara registro e ambiente; proprietário confirma uso e impacto. Registrar alteração após mudança de conta, integração, fornecedor ou serviço. Concluir o recorte quando ativos conhecidos estão atribuídos e lacunas têm plano; não declarar inventário completo enquanto faltar cobertura.

O nome anterior “Inventário 80/20” expressava priorização, sem prova de que 20% dos ativos representam 80% da receita ou risco. Exemplos antigos de ERP, planilha financeira, notebook e serviço de chamados são possibilidades de ativo, não configuração real do projeto.

Fundamento: [segurança e continuidade](<../framework/nucleo/seguranca-continuidade.md>), [NIST F01–F02](<../framework/referencias/fontes.md#f01>). Próximo modelo: [risco e continuidade](<../framework/templates/risco-continuidade.md>).


## Revisão de uma saída assistida por IA

Aplicar antes de usar uma saída de IA em decisão, comunicação ou mudança. O responsável humano pela tarefa verifica conteúdo e autorização. Não enviar dado restrito a uma ferramenta sem permissão e controles adequados.

- Tarefa, data, responsável e ferramenta/modelo quando conhecido: [preencher]
- Informações fornecidas e classificação: [preencher sem reproduzir segredo]
- Saída pretendida e autoridade para usá-la: [preencher]
- Fatos conferidos e fontes consultadas: [preencher]
- Citações verificadas no documento original: [preencher]
- Cálculos, unidades e premissas conferidos: [preencher]
- Dados pessoais ou confidenciais removidos/protegidos: [preencher]
- Limitações, erro observado e correção: [preencher]
- Aprovação, rejeição ou necessidade de investigação: [pessoa e motivo]
- Evidência da versão usada e próxima revisão: [preencher]

Uma resposta fluente não é evidência. Se não for possível verificar uma afirmação material, retirá-la, restringi-la ou identificá-la como hipótese. A assinatura do revisor não substitui acesso à fonte.

Conclusão: somente a saída revisada e autorizada segue para uso. A equipe pode executar a mesma tarefa sem IA.

### Conferências por tipo de saída

Aplicar os blocos pertinentes ao efeito proposto, registrando motivo quando um item não se aplica. Uma conferência feita por outro modelo pode ajudar a localizar divergências, mas não substitui o revisor humano nem comprova ausência de erro.

#### Rastreabilidade

- [ ] Fatos correspondem aos dados fornecidos ou a fontes conferidas?
- [ ] Sistemas, interfaces e configurações reais estão separados das propostas?
- [ ] Lacunas, estimativas e incertezas estão explícitas?
- [ ] Referências indicam versão e trecho que sustenta a afirmação?
- [ ] Cálculos usam moeda, unidades, período e premissas compatíveis?

Uma alternativa de ferramenta pode ser proposta com justificativa, custo e verificação pendentes; ela não passa a ser uma aquisição real. Não exigir marcas já compradas para toda análise nem considerar qualquer sugestão uma configuração existente.

#### Requisitos

- [ ] História descreve usuário, comportamento e finalidade verificáveis?
- [ ] Critério informa condição, ação e resultado observável?
- [ ] Escopo e exclusões foram acordados com o negócio?
- [ ] Dependências e capacidade tornam o recorte viável ou têm lacunas atribuídas?

#### Segurança e continuidade

- [ ] Acesso proposto é necessário ao efeito e suas exceções foram revistas?
- [ ] Controles têm cobertura e evidência, sem promessa de proteção integral?
- [ ] Recuperação e contenção consideram ambiente, autoridade e preservação de evidências?
- [ ] Recursos e manutenção foram considerados, inclusive para soluções nativas?

#### Código e configuração

- [ ] Dependências, APIs, comandos e valores foram conferidos na versão aplicável?
- [ ] Entrada, acesso e erros relevantes foram testados em ambiente autorizado?
- [ ] Segredos e detalhes internos não aparecem indevidamente na saída?
- [ ] Regras de negócio implementadas têm revisão e critérios acordados?
- [ ] Placeholder, demonstração e integração real estão identificados?
- [ ] Plano de retorno e aprovação para a mudança estão registrados?

Código inicial pode conter lacunas explícitas; não é apto ao uso operacional apenas por ser executável. Também não há proibição universal de gerar lógica completa: seu uso exige revisão, testes e autorização apropriados.

### Registrar o resultado

| Item/afirmação | Evidência consultada ou teste | Resultado e limitação | Correção necessária | Responsável |
| --- | --- | --- | --- | --- |
| [preencher] | | | | |

Decisão: [aprovado para o uso delimitado / ajustar / rejeitar / investigar], com pessoa, data, motivo, versão e pendências. Aprovação editorial não autoriza automaticamente implantação. Erro material exige correção ou restrição do uso; registrar divergência sem prometer “zero alucinações”. Duração de cinco minutos e revisão de três fatos não são critérios de qualidade.

