# GEAR — cenários condicionais por porte

Quatro exercícios completos preservam retratos, problemas, planos, indicadores, cálculos e áreas de controle do acervo GP-PME. As empresas, valores e estados de melhoria são fictícios. Não há observações de implantação ou retorno medido.

Leia a [Calculadora](Calculadora_ROI.md), escolha um perfil e substitua as hipóteses por dados documentados. Cada perfil contém sete seções: contexto, partida, plano inicial, hipóteses de melhoria, verificação operacional, memória financeira e risco. Os perfis não constituem benchmark de equipe ou receita.

| Perfil | Pessoas | Investimento inicial | Operação anual incremental | Benefício mensal potencial | ROI líquido condicional, 12 meses |
| --- | ---: | ---: | ---: | ---: | ---: |
| [A — TI de uma pessoa](Perfil_A_TI_Solo.md) | 10 | R$ 4.080,00 | R$ 1.200,00 | R$ 2.383,33 | 571,57% |
| [B — TI com analista e estagiário](Perfil_B_25_Funcionarios.md) | 25 | R$ 7.770,00 | R$ 1.800,00 | R$ 5.140,83 | 670,79% |
| [C — Primeiro gestor de TI](Perfil_C_50_Funcionarios.md) | 50 | R$ 14.680,00 | R$ 6.000,00 | R$ 10.707,00 | 734,36% |
| [D — Serviços com dados pessoais](Perfil_D_100_Funcionarios.md) | 100 | R$ 47.800,00 | R$ 18.000,00 | R$ 22.150,00 | 418,41% |

O ROI supõe benefício integral e constante por 12 meses em estado estabilizado. A análise desde o início exige fluxos datados. Os perfis trazem sensibilidade a 0%, 60% e 100% de realização do benefício. Tempo liberado pode ser realocado, sem reduzir despesa paga; retirar dupla contagem entre retrabalho e indisponibilidade.

Nesta edição, investimento e recorrência foram separados, o ROI passou a ser líquido e o perfil B foi corrigido para 17,5 h de indisponibilidade a 99,5% em 3.500 h. R$ 62/h no perfil C é um parâmetro, sem média salarial comprovada. IA permanece opcional em todos os portes; maturidade e conformidade dependem de evidências.

As probabilidades de incidente dos exemplos antigos são arbitrárias e aparecem apenas como exercício isolado, sem integrar o retorno. Controles estão “não verificados”, com evidência a coletar. Consulte as [fontes do método](../framework/referencias/fontes.md) e as referências legais do perfil D.

Fontes editáveis e contas: `tools/build_simulations.py`. Os originais possuem manifesto e hashes em `.context/originais/gear-2026-10-04/`. O arquivo `dataset_framesim_nexus.json` é dado preservado do usuário e não é transformado pelo gerador.
