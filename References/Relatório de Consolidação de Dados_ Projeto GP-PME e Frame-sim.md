# Consolidação: método e proposta de avaliação

Edição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.

## Origem e decisão editorial

A síntese reunia NotebookLM, Gemini, Claude e GitHub. A proposta de minimundo e SWOT dupla fica separada do resultado de pesquisa. A descrição de agentes CFO/CTO/CEO, RAG, Curva J e custo de não qualidade não confirma implementação nesta edição. Documentação de software, cálculo condicional e avaliação do método são evidências diferentes.

## Escopo e princípios

GEAR ajuda a direção e o responsável por TI a manter um ciclo de decisão: registrar uma necessidade, avaliar impacto e capacidade, atribuir responsabilidade, executar, verificar a saída e revisar o resultado. O recorte é a TI de pequenas e médias empresas, inclusive equipes internas reduzidas e serviços terceirizados.

### Problemas tratados

O framework aborda demandas dispersas, prioridades conflitantes, decisões sem responsável, trabalho iniciado sem capacidade disponível, controles de continuidade sem evidência e benefícios financeiros apresentados sem premissas. Esses são problemas de aplicação do método, não uma afirmação sobre toda PME.

Não substitui gestão contábil, obrigação legal, avaliação especializada de segurança ou um sistema completo de gestão empresarial. Um risco jurídico ou regulatório identificado deve ser encaminhado à competência responsável, em vez de receber uma resposta improvisada de TI.

### Princípios de aplicação

1. **Responsabilidade identificada.** Cada demanda e decisão têm executor e autoridade de aprovação. Uma pessoa pode acumular funções; o registro torna esse acúmulo visível.
2. **Adoção proporcional.** Ativar uma prática porque resolve uma necessidade observada. Rever complexidade, capacidade e manutenção antes de ampliar o método.
3. **Evidência antes de conclusão.** Uma política escrita, um backup concluído e um serviço restaurado são evidências diferentes. Registrar a que conclusão cada uma permite chegar.
4. **Fluxo visível.** Mostrar fila, trabalho iniciado, bloqueios e exceções. Um incidente não apaga o histórico do trabalho que interrompeu.
5. **Inspeção e adaptação.** Rever prioridades e hipóteses em uma cadência sustentável. Ajustes de duração e capacidade devem ter motivo registrado.
6. **Assistência opcional.** O núcleo pode ser operado com reunião, quadro e registros. IA pode preparar saídas; pessoas permanecem responsáveis pelas decisões.

### Núcleo, aplicação e explicação

O núcleo define termos e invariantes. Os guias explicam tarefas. Templates facilitam o registro. Fundamentos apresentam as adaptações e seus limites. Essa separação atende a necessidades distintas de documentação, seguindo a orientação Diátaxis. [F08](<../framework/referencias/fontes.md#f08>)

Uma equipe pode usar software de chamados, planilha ou quadro físico. O suporte escolhido precisa preservar responsável, situação, critério de conclusão e evidência. Operação manual significa independência de uma plataforma de gestão, não ausência de tecnologia para executar backup ou proteger contas.

### Situação da evidência

GEAR é uma composição autoral de práticas. Cenários demonstrativos e testes de software comprovam apenas o que efetivamente verificam. Metas de prazo, percentuais de melhoria e faixas de indicadores não são resultados médios esperados nem parâmetros normativos universais.

A avaliação acadêmica prevista utiliza casos sintéticos pareados. Até a produção de dados, o protocolo permanece prospectivo. Uma comparação com referências adaptadas precisa declarar escopo e condições de cada configuração, sem construir alternativas deliberadamente fracas.

Próxima leitura: [Governança e direção](<../framework/nucleo/governanca.md>). Para executar: [Primeiros 30 dias](<../framework/adocao/primeiros-30-dias.md>).


## Cenários fictícios do acervo

O apêndice C de fevereiro de 2026 descrevia TechSolutions, DataGuard e InovaTech como estudos de caso, com percentuais de resultado. O documento não apresentou registros de coleta, participantes, instrumentos ou dados que comprovassem observação real. Esta edição os conserva como cenários fictícios para discussão. Nomes, dimensões e números pertencem ao exercício, sem vínculo confirmado com empresas reais.

### TechSolutions: fila e decisão

Perfil do exercício: desenvolvimento de software, quinze funcionários e faturamento anual de R$ 2 milhões. Situação descrita: projetos frequentes, prazos perdidos e comunicação insuficiente com clientes. O nível inicial 0 foi uma atribuição do rascunho; não há dez respostas e evidências para confirmá-lo.

Práticas a discutir: registro oficial, quadro, orientação dos usuários, pauta de direção e definição de indicadores. A resistência inicial pode ser investigada ouvindo usuários e testando o fluxo; não presumir que treinamento ou demonstração resolvam a adoção.

O texto antigo declarava redução de 40% no tempo de resposta e aumento de 20% na satisfação. São números imaginados sem baseline, período, amostra ou definição de medida. Não calcular resultado real, nem confundir resposta inicial com restauração. Aumento de satisfação precisa explicitar se é relativo, em pontos ou outra unidade.

| Perspectiva SWOT do exercício | Questão para a decisão |
| --- | --- |
| Força: abertura a tecnologia e apoio à redação | O fluxo atende à tarefa e foi verificado pelos usuários? |
| Fraqueza: processos pouco definidos e dependência de uma pessoa | Quem substitui o responsável e onde ficam os registros? |
| Oportunidade: ampliar práticas e testes | Qual lacuna justifica a próxima ação dentro da capacidade? |
| Ameaça: perda de conhecimento e competição | Que continuidade e documentação precisam de prioridade? |

### DataGuard: acesso e recuperação

Perfil do exercício: consultoria de segurança, oito funcionários e faturamento anual de R$ 1,5 milhão. Situação descrita: plano de incidentes ausente, cópias não testadas e dificuldade de acompanhar vulnerabilidades. O nível inicial 1 também era presumido.

Práticas a discutir: inventário por serviço, acesso, teste autorizado de recuperação, contatos e alçadas do PRI, exercício de mesa e dados pessoais. Scripts ou classificação assistida são propostas a revisar, não controles já executados.

O rascunho declarava redução de 90% no tempo de resposta, “100% de conformidade” de backup e melhoria de conformidade à LGPD. Nenhuma dessas conclusões tem evidência no documento. A recuperação precisa de recorte, tolerância e resultado; conformidade legal não decorre da presença de planilha ou política.

| Perspectiva SWOT do exercício | Questão para a decisão |
| --- | --- |
| Força: conhecimento de segurança | A capacidade cobre configuração, resposta e revisão necessárias? |
| Fraqueza: equipe pequena e monitoramento limitado | Que cobertura existe e qual exposição permanece aceita? |
| Oportunidade: oferecer serviços e preparar análise de logs | Quais contratos, acessos e verificações são necessários? |
| Ameaça: mudança de ameaças e regras | Quem acompanha as fontes pertinentes e revisa o plano? |

### InovaTech: requisitos e entrega

Perfil do exercício: startup de tecnologia, vinte desenvolvedores e faturamento anual de R$ 5 milhões. Situação descrita: ciclo de desenvolvimento lento, dificuldade de preparar MVPs e retrabalho de requisitos. O nível inicial 2 não foi medido no texto.

Práticas a discutir: PRD, histórias, critérios, código, testes e piloto com revisão entre etapas; biblioteca de instruções quando houver uso de assistência. A adesão da equipe precisa de observação, não de conclusão presumida após workshop.

O texto antigo declarava redução de 50% no ciclo PRD/código, aumento de 30% na produtividade e três MVPs em seis meses. Esses dados são fictícios. Definir início/fim do ciclo, esforço de revisão e correção, amostra, custo e qualidade antes de comparar; quantidade de entregas não demonstra utilidade.

| Perspectiva SWOT do exercício | Questão para a decisão |
| --- | --- |
| Força: experiência técnica e disposição para experimentar | Quais critérios permitem avaliar o piloto? |
| Fraqueza: dependência de IA e manutenção das instruções | Qual saída exige revisão e quem mantém a biblioteca? |
| Oportunidade: novas entregas e atração de pessoas | Qual benefício é hipótese e como será observado? |
| Ameaça: custo de modelos e concorrência | Quais alternativas e sensibilidades mudam a decisão? |

### Variações do documento acadêmico completo

O mestre acadêmico continha uma segunda TechSolutions Ltda.: quinze pessoas, cinco em desenvolvimento, duas em suporte e oito em comercial/marketing. Essa composição não é a mesma do cenário de vinte pessoas chamado TechSolutions PME no rascunho de simulação. Conservar perfis separados ao usar os exercícios.

A variação de quinze pessoas supunha quadro digital, e-mail, formulário e dez FAQs. Declarava, após trinta dias, redução de 45% no tempo de resposta, 95% de requisições registradas e 60% de FAQs resolvidas. São valores fictícios sem coleta verificável. Para testar a hipótese, conferir captura de demandas, resolução confirmada e esforço de manutenção da base.

**Metalúrgica Alfa S.A.**: cenário fictício de manufatura com oitenta pessoas, um gerente de TI e dois analistas de suporte. O exercício propunha reunião mensal de 45 minutos com direção e produção, priorização e painel de custo/receita, disponibilidade e prazo de projetos. Declarava aumento de 15% no ROI e redução de 20% no custo de TI/receita em seis meses. Sem custos, benefícios, receitas, baseline ou definição de variação, esses números não permitem calcular nem comprovar resultado. A questão preservada é como produção e TI decidem recursos e verificam dependências.

**PixelBoost Agência Digital**: cenário fictício com vinte e cinco pessoas, incluindo três desenvolvedores, um designer e dois gerentes de projeto. O exercício propunha requisitos, histórias, código, testes, ciclos semanais e retrospectiva. Declarava redução de 60% no ciclo PRD/código e aumento de 30% na capacidade em três meses. São hipóteses numéricas, sem dados ou equivalência de qualidade. Medir preparação, revisão e correção antes de discutir ganho; cada etapa exige conferência, inclusive histórias e testes.

**TechSolutions PME**: minimundo fictício de vinte pessoas e um responsável por TI, com dependência de vendas e CRM e intenção de expandir. O rascunho sugeria agentes para representar direção, finanças, TI e clientes. Esse desenho não comprova que o simulador tenha sido executado ou reproduza comportamento humano. Separar entradas, regras e resultados simulados de evidência organizacional.

### Aplicar o exercício sem fabricar resultado

Escolher um cenário e preparar perfil, diagnóstico por evidência, práticas, obstáculos, resultados ou hipóteses, decisões e SWOT. A SWOT é uma lente local de discussão, não uma medição causal. Registrar dono, lacuna e próxima ação para os pontos relevantes.

Os cinco temas preservados do apêndice são adoção gradual, assistência sob revisão, comunicação, indicadores úteis e revisão da rotina. Verificar no contexto se há resistência, excesso de registro, confiança indevida na saída ou ausência de alçada. Um questionário não precisa preceder resposta a incidente ou necessidade urgente.

Para documentar uma aplicação real, indicar origem, autorização de uso dos dados, período, método de coleta, instrumentos, amostra, mudanças concorrentes e limitações. O protocolo acadêmico do projeto continua prospectivo; os exercícios acima não preenchem seus resultados.

Modelos: [comparar antes e depois](<../framework/indicadores/negocio-comparacao.md>), [maturidade](<../framework/templates/maturidade.md>), [PRD e aceite](<../framework/templates/prd-aceite.md>), [risco e continuidade](<../framework/templates/risco-continuidade.md>).


## Comparar uma tarefa com e sem assistência

Use quando houver uma decisão sobre continuar, ajustar ou suspender o uso de IA. A pessoa responsável pela tarefa define o recorte; quem aceita a entrega confere qualidade; direção decide investimento. A equipe pode atingir qualquer nível de maturidade sem adotar IA.

### Preparar uma comparação útil

Escolher tarefas comparáveis, registrar dificuldade, experiência do executor, ferramenta, versão, dados permitidos e critério de aceite. Medir todo o esforço: preparação, geração, leitura, conferência, correção e teste. Cronometrar somente a geração omite trabalho necessário.

| Medida local | Cálculo ou registro | Limite de interpretação |
| --- | --- | --- |
| Tempo por entrega aceita | Esforço total até o aceite | Comparar tarefas com escopo e qualidade equivalentes |
| Variação relativa de tempo | (tempo de referência − tempo assistido) / tempo de referência × 100 | Referência positiva; valor negativo indica aumento de esforço |
| Aceitação sem revisão relevante | Entregas aceitas sem correção relevante / entregas avaliadas × 100 | Definir “relevante”; aceite não prova ausência de erro |
| Erros por entrega | Erros identificados / entregas verificadas | Manter o mesmo método e profundidade de verificação |
| Custo por entrega aceita | Custos atribuíveis / entregas aceitas | Incluir ferramenta, revisão, correção e infraestrutura |
| Capacidade recuperada | Horas de referência − horas assistidas | Tempo potencial, sem equivalência automática a economia financeira |

Os nomes históricos TGA, TMRIA, TAA, CAG e TEIA descreviam tempo, aceitação, custo ou variação. A edição vigente exige unidade e evento de início/fim explícitos. Resposta inicial, restauração de serviço e fechamento administrativo são medidas distintas. Não atribuir causalidade à IA se o processo, a equipe ou o tipo de demanda também mudou.

### Decidir com os resultados

1. Conferir amostra, exclusões, falhas e tarefas não concluídas.
2. Comparar esforço e qualidade, conservando os registros individuais.
3. Examinar se a vantagem depende de dados, pessoa, fornecedor ou contexto específicos.
4. Registrar continuar, ajustar, ampliar o teste ou suspender; indicar dono e próxima verificação.

Concluir quando a decisão pode ser reconstruída a partir das entradas e das entregas verificadas. Sem baseline, registrar apenas a medição atual. Sem denominador ou observações comparáveis, não preencher percentual. A antiga meta de redução de 60% não é requisito do GEAR.

Fundamento: instrumento local de avaliação, derivado dos indicadores candidatos do acervo. Estudos sobre assistência têm tarefas e populações próprios; seus resultados não predizem o ganho desta equipe. Consulte [a bibliografia do manuscrito](<../GP-Pme%20Article/overleaf/references.bib>) e os [limites de atribuição das fontes](<../framework/referencias/fontes.md>).

Consulta: [comparação da rotina](<../framework/indicadores/negocio-comparacao.md>) e [revisão de saída assistida](<../framework/templates/revisao-ia.md>).

