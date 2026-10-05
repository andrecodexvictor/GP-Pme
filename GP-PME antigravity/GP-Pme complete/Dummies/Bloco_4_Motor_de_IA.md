# Usar assistência opcional por IA

Edição editorial GEAR 2026.10. Documento completo no caminho anterior para compatibilidade; regras vigentes em `framework/`. Direitos conforme LICENSE.md.

## Percurso de leitura

- [Usar IA quando for útil](#usar-ia-quando-for-util)
- [Preparar uma solicitação](#preparar-uma-solicitacao)

## Usar IA quando for útil

Fornecer tarefa, dados autorizados, restrições e saída pretendida. Conferir fontes, cálculos e lacunas. A resposta deve separar informação fornecida, hipótese e recomendação. A pessoa com alçada decide se a saída pode ser usada. Um prompt não elimina erros; a equipe pode executar a mesma tarefa sem IA.

Quatro funções conceituais organizam a assistência: direção, entrega, segurança e auditoria. O software histórico tem um orquestrador e oito especialistas. As contagens descrevem camadas distintas e não criam novos domínios.

## Preparar uma solicitação

Use para rascunhar uma pauta, requisito, orientação ou cálculo que uma pessoa possa revisar. Responsável pela tarefa fornece dados autorizados; quem tem alçada decide o uso. Entrada: contexto, tarefa, restrições e fontes. Saída: minuta verificada ou lacunas explícitas.

Exemplo fictício de contexto: loja de roupas com dez computadores e vendas em nuvem. O exemplo descreve entrada, sem comprovar configuração ou segurança.

```text
Contexto: [serviço, pessoas afetadas, dependências e dados autorizados].
Tarefa: preparar uma lista breve de lacunas de continuidade.
Formato: problema, evidência, pergunta pendente, responsável e próximo passo.
Informar origem, data e limite de cada dado. Conferir fontes externas.
Separar fatos, hipótese e proposta; registrar informação insuficiente.
Autoridade humana: [quem revisa e pode aprovar efeitos organizacionais].
```

| Função de assistência | Minuta possível | Conferência humana |
| --- | --- | --- |
| Direção | Pauta e alternativas | Alçada, prioridade e recursos |
| Entrega | PRD e critérios | Viabilidade e aceite |
| Segurança | Lacunas e plano | Evidência, contenção e recuperação |
| Indicadores | Memória de cálculo | Premissas, unidades e fonte |

Concluir somente após verificar a saída e registrar aprovação, correção ou rejeição. Manter lacunas com responsável para obter o dado. A ferramenta pode errar mesmo quando segue o formato pedido; não equivale a uma equipe inteira de TI nem possui tempo garantido de resposta. A estrutura e a revisão são propostas locais; referências conceituais e limites estão nas fontes do GEAR.

## Próxima tarefa e referências

- [Usar assistência por IA](<../../../framework/guias/usar-ia.md>)
- [Prompts para quatro funções de assistência](<../../../framework/templates/prompts-assistencia.md>)

Fontes F01–F12 e limites de consulta: [referências completas](<../../../framework/referencias/fontes.md>). Os originais e o registro de revisão são preservados em `.context/`.
