# GEAR: Questionário e registro de maturidade

Edição editorial GEAR 2026.10. Caminho GP-PME preservado para compatibilidade. Modelos completos, revistos a partir da biblioteca anterior; preencher com dados reais e registrar lacunas. IA é opcional. Direitos conforme LICENSE.md.

## Percurso de leitura

- [Maturidade com evidências](#maturidade-com-evidencias)
- [Registro de maturidade](#registro-de-maturidade)

## Maturidade com evidências

O IM-TI é um instrumento local para discutir a rotina de TI. Ele soma dez respostas binárias, de 0 a 10. Não é escala validada cientificamente, certificação ou comparação confiável entre empresas com contextos diferentes. Seu uso principal é encontrar lacunas e acompanhar a mesma organização ao longo do tempo.

### Aplicar o questionário

TI e dono do processo respondem juntos. Marcar 1 somente quando a prática ocorre e existe evidência consultável; marcar 0 quando ausente ou insuficiente. Registrar “não verificado” na observação quando faltar informação, contabilizando 0 provisoriamente. Não excluir perguntas para elevar a pontuação.

| Nº | Prática a verificar | Evidência possível |
| --- | --- | --- |
| 1 | Demandas têm registro oficial e responsável | Amostra da fila com solicitante e executor |
| 2 | Trabalho iniciado respeita a capacidade definida, incluindo testes e bloqueios | Quadro com testes, bloqueios e exceções |
| 3 | Orientações recorrentes são mantidas e verificadas | Instrução revisada por usuário, com responsável |
| 4 | Negócio e TI decidem prioridades em revisão registrada | Decisão com motivo, alçada e prazo |
| 5 | Melhorias têm problema, escopo e aceite acordados | PRD curto e verificação pelo dono do processo |
| 6 | Ativos e dependências críticos estão identificados | Inventário com proprietário e criticidade |
| 7 | Recuperação foi testada na janela combinada | Registro de restauração e limitações |
| 8 | Acessos críticos são controlados e revistos | Revisão de privilégios, MFA e exceções |
| 9 | Indicadores usados têm origem, período e revisão | Registro de dados e decisão vinculada |
| 10 | Decisões e mudanças passam por revisão responsável | Aprovação, verificação e correção registradas |

Nenhuma pergunta exige chatbot, agente, modelo generativo ou percentual de automação. O nível máximo pode ser alcançado com procedimentos manuais e controles tecnológicos apropriados.

### Interpretar sem ocultar lacunas

| IM-TI | Nível descritivo | Próxima ação típica |
| --- | --- | --- |
| 0–2 | 0: rotina pouco visível | Identificar responsáveis e registrar demandas |
| 3–5 | 1: organização inicial | Verificar continuidade e critérios de aceite |
| 6–8 | 2: práticas repetidas | Investigar lacunas e dependências entre práticas |
| 9 | 3: rotina acompanhada | Rever qualidade das evidências e resultados |
| 10 | 4: práticas verificadas | Manter a revisão e adequar o método ao contexto |

As faixas são convenções locais preservadas para continuidade do instrumento. As perguntas desta edição foram revistas: resultados antigos não são diretamente comparáveis sem reaplicação. As faixas não indicam probabilidade de ataque, retorno financeiro ou superioridade organizacional. Uma organização com pontuação alta e restauração não testada continua exposta.

### Decidir uma transição

Comparar a aplicação atual à anterior na mesma janela de evidência. Registrar o que passou a ocorrer, quem verificou e o que permanece incerto. O score pode mudar imediatamente; a **transição sustentada** exige observar a prática na rotina, por um período acordado. Não declarar avanço automático no dia 30.

Selecionar até três ações de melhoria por impacto e capacidade. Manter o resultado por pergunta junto ao total. Se uma resposta for contestada, revisar a evidência e corrigir o histórico, sem apagar a avaliação anterior.

Responsável pela aplicação: TI. Responsável pela validação de efeitos no negócio: dono do processo. Direção aceita recursos e riscos conforme a alçada. Modelo: [Registro de maturidade](<../../../framework/templates/maturidade.md>).

Para planejar uma melhoria específica, consultar as [fichas por domínio](<../../../framework/adocao/fichas-maturidade.md>). Elas preservam a matriz detalhada das versões anteriores como opções de desenvolvimento, sem acrescentar condições ao IM-TI.

Anterior: [Primeiros 30 dias](<../../../framework/adocao/primeiros-30-dias.md>). Para compreender: [Fundamentos e adaptações](<../../../framework/fundamentos/origens-adaptacoes.md>).


## Registro de maturidade

Preencher com TI e dono do processo usando o [questionário](<../../../framework/adocao/maturidade.md>). Comparar apenas aplicações com contexto e janela conhecidos.

**Organização/processo:** [preencher]  
**Data, janela de evidência e avaliadores:** [preencher]

| Pergunta | Resposta 0/1 | Evidência, data e limite | Ação quando insuficiente |
| --- | --- | --- | --- |
| 1. Registro e responsável | | | |
| 2. Capacidade e fluxo | | | |
| 3. Orientações verificadas | | | |
| 4. Prioridades decididas | | | |
| 5. Escopo e aceite | | | |
| 6. Dependências críticas | | | |
| 7. Recuperação testada | | | |
| 8. Acesso controlado | | | |
| 9. Indicadores rastreáveis | | | |
| 10. Revisão responsável | | | |

**IM-TI e nível descritivo:** [soma e faixa].  
**Mudanças em relação à aplicação anterior:** [prática, evidência e contexto].  
**Até três ações prioritárias:** [responsável e prazo].  
**Lacunas críticas e risco aceito:** [aprovação e motivo].  
**Próxima revisão:** [data e responsável].

Concluir com evidências consultáveis e pendências atribuídas. Este registro não constitui certificação nem exige IA.

