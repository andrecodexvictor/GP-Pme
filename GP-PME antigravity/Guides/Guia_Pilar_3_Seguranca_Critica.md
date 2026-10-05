# GEAR: Segurança e continuidade: guia técnico

Edição editorial GEAR 2026.10. Framework de governança e gestão de TI para pequenas e médias empresas. Origem: GP-PME 5.2, 02/06/2026. Crédito declarado: Antigravity AI, sob a direção de Andre Victor. Direitos conforme LICENSE.md. Caminho anterior preservado para compatibilidade.

## Percurso de leitura

- [Segurança e continuidade](#seguranca-e-continuidade)
- [Testar restauração](#testar-restauracao)
- [Tratar um incidente](#tratar-um-incidente)
- [Risco e continuidade](#risco-e-continuidade)
- [Plano breve de resposta a incidente](#plano-breve-de-resposta-a-incidente)
- [Assistência opcional e exercício de resposta](#assistencia-opcional-e-exercicio-de-resposta)
- [Conferir acesso e cópias](#conferir-acesso-e-copias)

## Segurança e continuidade

Este domínio relaciona serviços críticos, controles e capacidade de recuperação. O conjunto inicial cobre inventário, identidade e acesso, cópias de segurança e resposta a incidentes. Ele é uma seleção autoral de práticas; não oferece proteção integral nem certificação de conformidade.

O NIST CSF 2.0 reúne seis funções: Governar, Identificar, Proteger, Detectar, Responder e Recuperar. O guia do NIST para pequenas empresas apresenta ações e perguntas aplicáveis a organizações com planos de cibersegurança modestos ou inexistentes. GEAR usa essa referência para organizar cobertura e lacunas. [F01](<../../framework/referencias/fontes.md#f01>) [F02](<../../framework/referencias/fontes.md#f02>)

### Serviço, ativo e dependência

Começar pelo serviço que precisa continuar, identificar seus dados, contas, equipamentos, fornecedores e responsáveis. Priorizar sistemas críticos não equivale a conhecer todos os ativos. O termo histórico “Inventário 80/20” é uma estratégia de início por criticidade, não a prova de que 20% dos ativos representam exatamente 80% do risco ou da receita.

Registrar o que ainda não foi inventariado, o responsável pela ampliação e como novas dependências entram no registro. Contas de nuvem e integrações também podem ser ativos relevantes.

### Controles e evidência

| Prática | Evidência útil | Limite da conclusão |
| --- | --- | --- |
| Inventário | Ativo, serviço, responsável, criticidade e revisão | Lista parcial não demonstra cobertura completa |
| Identidade e acesso | Contas individuais, acesso necessário, MFA e revisão | Um controle isolado não impede todo comprometimento |
| Cópias de segurança | Execução, retenção, separação e teste de restauração | Job concluído não prova recuperação do serviço |
| Resposta | Contatos, autoridade, passos e exercício do plano | Plano escrito não demonstra capacidade sob qualquer incidente |

A seleção local deve indicar quais resultados do CSF ela cobre, quais ficam pendentes e qual risco é aceito pela direção. O CSF não prescreve uma implementação única nem valida as metas numéricas do GEAR. [F02](<../../framework/referencias/fontes.md#f02>)

### Recuperação

Definir com o dono do processo quanto tempo o serviço pode ficar indisponível e qual perda de dados é tolerável. Esses requisitos orientam retenção, frequência de cópia e teste. RTO é o objetivo de tempo de recuperação; RPO expressa a perda de dados tolerável em tempo. Registrar também dependências e recursos de restauração.

A regra 3-2-1 é um arranjo de cópias a avaliar, não sinônimo de backup testado. Sincronização de arquivos pode propagar alterações ou exclusões; verificar a retenção e o comportamento da solução antes de chamá-la de cópia recuperável. Um teste de arquivo prova um recorte; a restauração de um serviço exige suas dependências.

### Resposta proporcional

O Plano de Resposta a Incidentes identifica quem aciona, decide contenção, comunica e verifica recuperação. Ações concretas dependem do incidente e do ambiente. Não transformar uma lista curta em ordem universal de formatar equipamentos, desligar serviços ou apagar evidências.

Após o incidente, registrar causa conhecida ou hipótese, efeito, decisões e correções. A ausência de causa confirmada deve permanecer explícita. A equipe deve encaminhar investigação especializada quando o problema excede sua capacidade.

Para executar: [Testar restauração](<../../framework/guias/testar-restauracao.md>) e [tratar incidentes](<../../framework/guias/tratar-incidentes.md>). Modelo: [Risco e continuidade](<../../framework/templates/risco-continuidade.md>).


## Testar restauração

Este guia verifica um recorte definido da capacidade de recuperar dados ou um serviço. Use antes de depender de um backup, após alteração relevante da solução e na cadência acordada para o serviço. Responsável técnico prepara o teste; dono do processo valida a saída. Entrada: cópia disponível, ambiente apropriado, autorização, dependências e objetivos de recuperação. Saída: evidência do teste e plano de correção de lacunas.

### Definir o recorte

Especificar serviço ou conjunto de dados, versão, momento da cópia, dependências, condição de sucesso e limite do teste. Um arquivo restaurado não demonstra a restauração completa de ERP, identidade, rede e integrações.

Definir RTO e RPO com o negócio. A referência histórica de restauração em 30 minutos não é meta universal; a necessidade do processo e os recursos disponíveis orientam o requisito.

### Executar

1. Confirmar acesso à cópia e às chaves necessárias, seguindo as permissões e controles da organização.
2. Preparar ambiente isolado ou autorizado, sem sobrescrever a operação por conveniência do teste.
3. Restaurar o recorte, registrando início, fim, versão e erros.
4. Verificar integridade e funcionalidade com o dono do processo.
5. Comparar tempo e perda de dados com os objetivos acordados.
6. Registrar escopo aprovado, limitações, evidências e correções com responsável e prazo.

### Interpretar

“Backup executado” indica execução do mecanismo. “Arquivo restaurado” indica recuperação daquele recorte. “Serviço recuperado” exige verificação das dependências e da funcionalidade definida. Preservar essa diferença na ata e nos indicadores.

Se faltou credencial, a cópia não existia ou o tempo excedeu o objetivo, registrar a falha e rever o plano. Não substituir o resultado por sucesso estimado.

A orientação NIST para pequenas empresas inclui recuperação e ações ligadas à continuidade. A implementação do teste e sua frequência precisam considerar o contexto. [F01](<../../framework/referencias/fontes.md#f01>)

Modelo: [Risco e continuidade](<../../framework/templates/risco-continuidade.md>). Próxima leitura: [Indicadores operacionais](<../../framework/indicadores/operacionais.md>).


## Tratar um incidente

Use quando há interrupção de serviço ou suspeita de comprometimento que exige coordenação. A pessoa que recebe o relato inicia o registro; a autoridade definida no plano decide contenção e comunicação; o executor técnico verifica a recuperação. Entrada: relato, serviços afetados, contatos e plano vigente. Saída: serviço recuperado ou alternativa acordada, decisões registradas e ações posteriores identificadas.

### Reconhecer e avaliar

Registrar momento de identificação, sinais observados, serviço e usuários afetados. Distinguir fato de hipótese. “Sistema indisponível” é observação; “ataque de ransomware” exige evidência adicional. A falta de certeza não impede acionar o responsável.

Estimar impacto e comunicar à autoridade competente. Se o caso excede a capacidade local, acionar fornecedor ou especialista conforme os contatos do plano. A pessoa afetada não precisa preencher um formulário inacessível para receber ajuda.

### Conduzir a resposta

1. Identificar quem coordena e como a equipe atualizará a situação.
2. Registrar prioridades, trabalho suspenso e exceção de capacidade.
3. Avaliar contenção apropriada ao ambiente e preservar informações necessárias à investigação. Não aplicar formatação ou desligamento como regra automática.
4. Comunicar estado e alternativa operacional aos afetados, evitando declarar causa não confirmada.
5. Recuperar a partir de uma condição conhecida e verificar serviço, dados e dependências com o dono do processo.
6. Registrar horários, decisões, evidências e necessidade de acompanhamento.

As seis funções do CSF articulam governança, identificação, proteção, detecção, resposta e recuperação; elas não oferecem um único roteiro de ações técnicas para todo incidente. [F01](<../../framework/referencias/fontes.md#f01>) [F02](<../../framework/referencias/fontes.md#f02>)

### Verificar recuperação

Confirmar que o processo necessário funciona e que a equipe conhece restrições temporárias. O desaparecimento de uma mensagem de erro não é suficiente para encerrar. Se uma alternativa foi adotada, declarar se o serviço original segue pendente.

O relógio de resolução começa no registro definido para a métrica e termina na condição de encerramento acordada. Registrar também o momento de identificação quando diferente. Não excluir incidentes longos de um indicador sem mostrar o critério.

### Rever e prevenir recorrência

Preparar revisão proporcional: o que ocorreu, quais decisões ajudaram, onde faltou informação e qual ação tem responsável. Correção definitiva pode ser uma melhoria vinculada ao incidente. “Causa ainda não confirmada” é uma conclusão válida, com próximo passo.

Modelo: [Plano de resposta](<../../framework/templates/incidente.md>). Próxima tarefa: [Testar restauração](<../../framework/guias/testar-restauracao.md>).


## Risco e continuidade

Use quando uma dependência pode impedir o serviço ou expor informações. Proprietário do serviço descreve impacto; TI verifica controles e recuperação; direção aceita risco dentro da alçada.

| Campo | Registro |
| --- | --- |
| Serviço, proprietário e data | |
| Ativos, dados e fornecedores críticos | |
| Evento e consequência | |
| Evidência de exposição e incerteza | |
| Controles existentes e verificação | |
| Tratamento escolhido, responsável e prazo | |
| Risco residual e aprovador | |
| Tempo de recuperação tolerável (RTO) | |
| Perda de dados tolerável (RPO) | |
| Backup, proteção, retenção e responsável | |
| Teste: cenário, ambiente, horários e resultado | |
| Validação do serviço pelo negócio | |
| Pendências e próxima revisão | |

O teste pode recuperar um arquivo, uma base ou o serviço inteiro. Declarar o recorte para que a conclusão corresponda à evidência. Se o tempo medido exceder a tolerância, registrar o desvio e decidir tratamento, sem alterar o objetivo retroativamente para declarar sucesso.

Fundamento: NIST [F01](<../../framework/referencias/fontes.md#f01>), [F02](<../../framework/referencias/fontes.md#f02>) e CISA [F12](<../../framework/referencias/fontes.md#f12>). O formato é uma adaptação local.

### Análise qualitativa e assistência opcional

Se usar probabilidade e impacto baixo/médio/alto, definir critérios, origem e incerteza antes de combinar categorias. Sem evidência, registrar hipótese a investigar, sem converter rótulo em probabilidade numérica. A análise local não certifica conformidade NIST ou CIS.

```text
Tarefa: preparar minuta de análise de risco do GEAR.
Entrada: [serviço, ativo, uso, dependências e evidências autorizadas].
Saída: evento, exposição verificada ou hipótese, consequência, controles
existentes, lacunas, alternativas, esforço, responsável e verificação.
Quando houver classificação qualitativa, usar os critérios informados.
Não inferir vulnerabilidade, CVE, configuração ou probabilidade por marca.
Não garantir custo zero, proteção integral ou recuperação em prazo fixo.
Conferir fontes externas junto à afirmação, incluindo versão e trecho.
Identificar autoridade para contenção, comunicação e aceitação de risco.
Deixar contato não fornecido pendente; não prescrever isolamento universal.
A pessoa responsável confere a análise e autoriza os efeitos apropriados.
```

### Cenários fictícios dos modelos anteriores

- ERP em nuvem com dados cadastrais e financeiros. O exemplo mencionava cinco mil clientes e acesso por senha; é hipótese didática. Conferir identidade, MFA, dados tratados, permissões e recuperação antes de avaliar exposição.
- Serviço de arquivos de escritório contábil com versão antiga de Windows Server e acesso compartilhado. Confirmar versão, suporte, permissões e cópia; “antigo” não identifica sozinho uma vulnerabilidade ou CVE.
- Notebooks usados em viagens com propostas e planilhas confidenciais. Conferir acesso, criptografia, atualização, guarda e recuperação; não inferir configuração real pelo cargo do usuário.

Na análise manual, partir do efeito sobre o serviço, conferir acesso e evidências de cópia e recuperação, depois comparar tratamentos. Frequência mensal ou trimestral depende do requisito local. Uma falha de controle precisa de investigação e resposta proporcional, não de ordem automática de alteração sem alçada.

### Verificações complementares locais

As skills anteriores mantinham dez verificações de segurança. Esta lista conserva a cobertura do modelo, como seleção autoral a adaptar. Ela não representa o catálogo completo do NIST CSF ou do CIS IG1, nem demonstra conformidade por quantidade de itens marcados.

| Verificação | Evidência a obter no recorte |
| --- | --- |
| Hardware e dispositivos | Inventário, proprietário, uso, localização e cobertura desconhecida |
| Software e serviços | Versões, uso autorizado, responsável e dependências |
| Vulnerabilidades | Origem da informação, aplicabilidade, correção ou exceção e verificação |
| Configuração | Baseline local, funções necessárias, alterações e revisão |
| Contas e autenticação | Contas individuais, cobertura de MFA, exceções e recuperação de acesso |
| Privilégio | Permissões necessárias, contas administrativas e revisão |
| Proteção contra malware | Cobertura, atualização, alertas e resposta no ambiente |
| Cópias e recuperação | Retenção, separação, proteção e teste com resultado e limites |
| Rede | Fluxos necessários, regras e conferência de filtragem no recorte |
| Orientação de pessoas | Situações abordadas, participação, modo de verificar e atualização |

Para cada item, registrar implementado no recorte verificado, em andamento, ausente ou não verificado, com fonte, data, responsável e próxima ação. O resumo informa cobertura conhecida; não converter evidência de um equipamento em cobertura de toda a empresa.

As três perguntas manuais de identidade, privilégio e recuperação ajudam a iniciar a análise. Elas complementam a lista, sem substituí-la. A ordem dos controles e a frequência de revisão dependem da exposição e do serviço; a antiga escolha de quatro itens por menor esforço não demonstrava redução de risco medida.

### Grade qualitativa opcional

Esta grade preserva a combinação usada nas skills anteriores. Seus rótulos são convenções locais; definir primeiro o significado dos eixos, sua evidência e incerteza. A ausência de dado sobre probabilidade permanece não verificada, sem escolher “baixa” por padrão.

| Probabilidade local / impacto local | Baixo | Médio | Alto |
| --- | --- | --- | --- |
| Alta | Médio | Alto | Crítico |
| Média | Baixo | Médio | Alto |
| Baixa | Baixo | Baixo | Médio |

A classificação orienta conversa e tratamento; não estima frequência de ataque, não autoriza alteração automática e não substitui a análise de consequência e alçada. Registrar o risco residual e o motivo da decisão.

Modelo complementar: [inventário de dependências](<../../framework/templates/inventario-dependencias.md>). Para resposta operacional: [incidente](<../../framework/templates/incidente.md>).


## Plano breve de resposta a incidente

Preparar antes de uma ocorrência. Durante o incidente, usar o registro para coordenar ações e preservar evidências. Segurança ou TI mantém o plano; direção confirma alçadas; dono do serviço define tolerância de interrupção.

- Serviço e dados afetados: [preencher]
- Responsável e substituto: [preencher]
- Contatos conferidos em: [data; TI, fornecedor, direção, jurídico quando aplicável]
- Como reconhecer e classificar: [impacto e critério local]
- Quem pode isolar, suspender acesso e autorizar recuperação: [preencher]
- Onde registrar horários, decisões e evidências: [preencher]
- Comunicação: [destinatários, canal, frequência, aprovador]
- Recuperação: [cópia, dependências, ambiente, teste de integridade e aceite]
- Obrigações a avaliar: [competência responsável; não improvisar requisito legal]

### Durante e depois

1. Registrar descoberta, impacto conhecido e incertezas.
2. Acionar responsáveis; conter conforme autorização e preservar evidências.
3. Atualizar negócio com fatos verificados e próxima atualização.
4. Recuperar em condição segura e conferir serviço com seu dono.
5. Registrar encerramento, limitações e correções atribuídas.

**Exercício:** [cenário, data, participantes, resultado e próxima revisão]. Não considerar o plano testado só por ter sido assinado. Não colocar credenciais no documento.

Fundamento: orientação CISA [F12](<../../framework/referencias/fontes.md#f12>), adaptada a um registro breve do GEAR.


## Assistência opcional e exercício de resposta

Uma equipe pode usar IA para preparar orientações contra phishing, examinar um relatório de permissões autorizado ou representar um incidente em exercício de mesa. Os dados devem ser adequados ao acesso da ferramenta. Menção textual a uma conta não comprova configuração, vulnerabilidade nem risco medido; a verificação depende de evidência técnica.

No exercício, escolher serviço, cenário, participantes e autoridade. Registrar quem reconhece o problema, aciona contatos, decide contenção, comunica e verifica recuperação. Discutir lacunas e atribuir correção. A IA pode narrar o cenário; não autoriza ações no ambiente real. O exercício não comprova capacidade sob qualquer incidente nem conformidade legal.

## Conferir acesso e cópias

Contas individuais e permissões necessárias reduzem exposições específicas. Separar administração e uso cotidiano quando o ambiente permitir; conferir exceções e procedimentos antes de retirar um privilégio. Privilégio mínimo não impede toda instalação ou propagação de malware. MFA é autenticação multifator, não sinônimo de SMS ou de exatamente dois fatores.

Para contas críticas, registrar cobertura, método, exceção, responsável e data de revisão. O proprietário confirma necessidade do acesso. Para cópias, registrar fonte, frequência, retenção, proteção, dependência e teste. Nuvem e automação são opções tecnológicas; sua simples presença não comprova segurança ou recuperação. Soluções nativas também podem exigir custo, operação e suporte.

As quatro práticas locais não equivalem às 56 salvaguardas do CIS IG1 [F11](../../framework/referencias/fontes.md#f11). Cobertura do NIST deve incluir lacunas de governança e detecção, sem apresentar seleção curta como implementação integral.

## Fontes e continuidade

Fundamentos e limites: [referências completas](../../framework/referencias/fontes.md). Regra vigente: [documentação modular](../../framework/README.md). Próxima tarefa: [catálogo de guias](../../framework/guias/README.md). IA é opcional, inclusive na maturidade máxima. As fontes conceituais não validam automaticamente metas ou instrumentos locais.
