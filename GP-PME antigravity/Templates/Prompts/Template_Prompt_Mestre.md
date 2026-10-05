# GEAR: Instrução de tarefa e prompt mestre

Edição editorial GEAR 2026.10. Caminho GP-PME preservado para compatibilidade. Modelos completos, revistos a partir da biblioteca anterior; preencher com dados reais e registrar lacunas. IA é opcional. Direitos conforme LICENSE.md.

## Percurso de leitura

- [Instrução de tarefa e assistência](#instrucao-de-tarefa-e-assistencia)

## Instrução de tarefa e assistência

Use para delegar uma tarefa a uma pessoa ou preparar um pedido de assistência por IA. O responsável fornece contexto autorizado e define quem revisa. O formato conserva o antigo Formulário de Alinhamento de Instrução (FAI), sem presumir que uma persona ou lista impede erro.

### Modelo copiável

```text
Tarefa e papel necessário: [ação delimitada e especialização pertinente].
Contexto: [serviço, processo, problema observado e pessoas afetadas].
Dados autorizados: [origem, data, unidade, período e limitações].
Restrições: [capacidade, orçamento conhecido, permissões e dependências].
Entradas: [documentos e dados fornecidos, separados das instruções].
Etapas: [ações necessárias e pontos de conferência].
Saída: [formato, seções, extensão adequada e critérios verificáveis].
Autoridade: [quem revisa e quem pode aprovar efeitos].
Lacunas: registrar dado insuficiente e o que obter; não preencher por suposição.
Estimativas: informar fonte, unidade, período, método e incerteza.
Fontes externas: conferir versão e trecho; citar junto à afirmação.
Fatos, hipóteses e propostas permanecem identificados.
Comandos, configurações e mudanças só são executados com autorização adequada.
```

Para uma pessoa, combinar papel, dados, etapas, saída e alçada antes de iniciar. Para IA, limitar acesso aos dados necessários e conferir a saída. Nenhuma forma elimina o trabalho de revisão. Dados históricos de mercado só entram como premissa quando sua fonte e pertinência foram verificadas; não suprem custo real da organização.

### Exemplo fictício: preparar migração de e-mail

O exemplo anterior mencionava Advocacia Lima, dez usuários, provedor IMAP, histórico de dois anos e licenças Microsoft 365 Business Basic. Esses dados são um cenário didático, sem evidência de organização real, aquisição ou viabilidade de migração.

```text
Tarefa: preparar uma proposta de migração de e-mail para avaliação humana.
Contexto fictício: escritório jurídico com dez usuários e histórico de dois
anos em provedor IMAP; licenças Microsoft 365 Business Basic informadas.
Janela desejada: sexta-feira às 19h; gestão DNS informada no Registro.br.
Saída: etapas de preparação, preservação e conferência das mensagens,
opções de janela, condição de retorno e testes de envio/recebimento.
Campos a conferir: domínio, caixas, volume, autenticação, ferramentas de
migração suportadas, registros DNS, retenção e dependências do fornecedor.
Indicar a fonte oficial e versão para qualquer procedimento específico.
Deixar valores DNS pendentes até conferência; não inventar servidores.
Não garantir tempo de propagação nem ausência de interrupção.
O responsável por TI confere viabilidade; autoridade aprova a mudança.
```

O exemplo é um pedido de planejamento, não roteiro técnico verificado de Microsoft 365 ou Registro.br. A menção antiga a PST, TXT, MX, SPF, DKIM e TTL passa a ser lista de aspectos a investigar conforme o ambiente e documentação oficial; nenhum valor ou prazo é prescrito aqui.

Concluir a preparação quando tarefa, dados, saída, lacunas e revisão estão claros. Aplicação: [usar IA](<../../../framework/guias/usar-ia.md>). Contratos específicos: [quatro funções](<../../../framework/templates/prompts-assistencia.md>).

