# Verificações locais de segurança

Edição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.

## Origem e decisão editorial

A lista de dez itens era seleção autoral, não numeração oficial de controles CIS nem implementação integral de IG1. Hardware, software, contas, configuração, vulnerabilidades, logs, e-mail, malware, backup e orientação permanecem como verificações locais abaixo. Frequência, cobertura, correção e exceções exigem contexto; preencher checklist não comprova conformidade.

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

Fundamento: NIST [F01](<../framework/referencias/fontes.md#f01>), [F02](<../framework/referencias/fontes.md#f02>) e CISA [F12](<../framework/referencias/fontes.md#f12>). O formato é uma adaptação local.

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

Modelo complementar: [inventário de dependências](<../framework/templates/inventario-dependencias.md>). Para resposta operacional: [incidente](<../framework/templates/incidente.md>).


## Segurança e continuidade

Este domínio relaciona serviços críticos, controles e capacidade de recuperação. O conjunto inicial cobre inventário, identidade e acesso, cópias de segurança e resposta a incidentes. Ele é uma seleção autoral de práticas; não oferece proteção integral nem certificação de conformidade.

O NIST CSF 2.0 reúne seis funções: Governar, Identificar, Proteger, Detectar, Responder e Recuperar. O guia do NIST para pequenas empresas apresenta ações e perguntas aplicáveis a organizações com planos de cibersegurança modestos ou inexistentes. GEAR usa essa referência para organizar cobertura e lacunas. [F01](<../framework/referencias/fontes.md#f01>) [F02](<../framework/referencias/fontes.md#f02>)

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

A seleção local deve indicar quais resultados do CSF ela cobre, quais ficam pendentes e qual risco é aceito pela direção. O CSF não prescreve uma implementação única nem valida as metas numéricas do GEAR. [F02](<../framework/referencias/fontes.md#f02>)

### Recuperação

Definir com o dono do processo quanto tempo o serviço pode ficar indisponível e qual perda de dados é tolerável. Esses requisitos orientam retenção, frequência de cópia e teste. RTO é o objetivo de tempo de recuperação; RPO expressa a perda de dados tolerável em tempo. Registrar também dependências e recursos de restauração.

A regra 3-2-1 é um arranjo de cópias a avaliar, não sinônimo de backup testado. Sincronização de arquivos pode propagar alterações ou exclusões; verificar a retenção e o comportamento da solução antes de chamá-la de cópia recuperável. Um teste de arquivo prova um recorte; a restauração de um serviço exige suas dependências.

### Resposta proporcional

O Plano de Resposta a Incidentes identifica quem aciona, decide contenção, comunica e verifica recuperação. Ações concretas dependem do incidente e do ambiente. Não transformar uma lista curta em ordem universal de formatar equipamentos, desligar serviços ou apagar evidências.

Após o incidente, registrar causa conhecida ou hipótese, efeito, decisões e correções. A ausência de causa confirmada deve permanecer explícita. A equipe deve encaminhar investigação especializada quando o problema excede sua capacidade.

Para executar: [Testar restauração](<../framework/guias/testar-restauracao.md>) e [tratar incidentes](<../framework/guias/tratar-incidentes.md>). Modelo: [Risco e continuidade](<../framework/templates/risco-continuidade.md>).

