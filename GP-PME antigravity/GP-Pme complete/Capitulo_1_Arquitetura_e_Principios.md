# GEAR: Arquitetura e princípios

Edição editorial 2026.10. Caminho GP-PME preservado para compatibilidade. Capítulo revisto a partir do acervo anterior; práticas locais não constituem certificação. Direitos conforme LICENSE.md.

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

O núcleo define termos e invariantes. Os guias explicam tarefas. Templates facilitam o registro. Fundamentos apresentam as adaptações e seus limites. Essa separação atende a necessidades distintas de documentação, seguindo a orientação Diátaxis. [F08](<../../framework/referencias/fontes.md#f08>)

Uma equipe pode usar software de chamados, planilha ou quadro físico. O suporte escolhido precisa preservar responsável, situação, critério de conclusão e evidência. Operação manual significa independência de uma plataforma de gestão, não ausência de tecnologia para executar backup ou proteger contas.

### Situação da evidência

GEAR é uma composição autoral de práticas. Cenários demonstrativos e testes de software comprovam apenas o que efetivamente verificam. Metas de prazo, percentuais de melhoria e faixas de indicadores não são resultados médios esperados nem parâmetros normativos universais.

A avaliação acadêmica prevista utiliza casos sintéticos pareados. Até a produção de dados, o protocolo permanece prospectivo. Uma comparação com referências adaptadas precisa declarar escopo e condições de cada configuração, sem construir alternativas deliberadamente fracas.

Próxima leitura: [Governança e direção](<../../framework/nucleo/governanca.md>). Para executar: [Primeiros 30 dias](<../../framework/adocao/primeiros-30-dias.md>).


## Origens, adaptações e evolução

GEAR reúne práticas do acervo GP-PME e NEXUS-PME em uma edição coerente. A mudança de nome foi uma decisão editorial: Gestão, Execução, Agilidade e Risco descrevem as atividades do método sem criar um quarto domínio. O acervo contém versões com diferentes recortes; sua data não determina, por si, a qualidade ou completude.

### Referência, adaptação e proposta local

| Referência | Conceito consultado | Adaptação do GEAR e limite |
| --- | --- | --- |
| NIST CSF 2.0 [F01](<../../framework/referencias/fontes.md#f01>), [F02](<../../framework/referencias/fontes.md#f02>) | Governar, Identificar, Proteger, Detectar, Responder e Recuperar | Priorização por serviço crítico e registro breve; seleção não cobre todo o CSF |
| Scrum Guide 2020 [F03](<../../framework/referencias/fontes.md#f03>) | Inspeção, adaptação, transparência e responsabilidade | Ciclos curtos e aceite; omitir elementos significa não implementar Scrum integralmente |
| TOGAF [F04](<../../framework/referencias/fontes.md#f04>) | Estrutura de conteúdo fundamental e guias de configuração | ADM-Lite é proposta local; não se afirma execução do ADM ou equivalência de fases |
| COBIT [F09](<../../framework/referencias/fontes.md#f09>) | Governança ajustada ao contexto | Alçadas e revisão breve; não representa todo o sistema COBIT |
| ITIL 4 [F10](<../../framework/referencias/fontes.md#f10>) | Gestão de serviços adaptável | Registro, recuperação e melhoria; não é implantação integral do ITIL |
| CIS [F11](<../../framework/referencias/fontes.md#f11>) e CISA [F12](<../../framework/referencias/fontes.md#f12>) | Higiene cibernética e recuperação | Controles priorizados com evidência; quatro práticas não equivalem às 56 salvaguardas IG1 |
| Diátaxis [F08](<../../framework/referencias/fontes.md#f08>) | Aprender, executar, consultar e compreender | Percursos de documentação; organização editorial, não método de gestão |

WIP de três, revisão de 30 minutos, percurso de 30 dias, IM-TI, DAN financeiro e templates são escolhas locais. Não atribuir esses parâmetros às referências acima. Prazos e metas devem ser ajustados com motivo registrado.

### O que foi consolidado

Versões anteriores chamavam IA de quarto pilar e adoção de quinto pilar. O modelo vigente mantém três domínios; IA é assistência opcional, e adoção, indicadores e maturidade são transversais. Os quatro papéis conceituais de IA descrevem funções; o software implementado tem um orquestrador e oito especialistas. Essas contagens pertencem a camadas diferentes.

Foram preservados mecanismos relacionais: conversa com o negócio, revisão de prioridades, comunicação de impedimentos, dono do processo, papéis acumulados e aprovação segundo alçada. Uma equipe pequena pode concentrar funções; precisa tornar visíveis os conflitos e buscar segunda conferência quando a decisão exigir.

“Fase Zero” de adoção foi separada da verificação pré-projeto. Razão benefício/investimento foi separada de ROI líquido; proporção de itens legados foi separada de DAN financeiro. IM-TI não exige IA para alcançar o nível máximo.

### Adoção gradual e linguagem introdutória

Os mestres de junho de 2026 usavam “Iceberg Invertido” para representar uma entrada simples seguida de aprofundamento. A contribuição preservada é a **divulgação progressiva**: começar pela necessidade observada, mostrar a prática correspondente e consultar fundamentos quando forem necessários. A metáfora não estabelece uma escala científica nem exige ativar todos os módulos em uma ordem fixa.

“TI Enxuta” designa essa escolha de dimensionar registro, revisão e execução à capacidade disponível. Uma orientação recorrente pode ajudar antes de um chatbot; uma decisão registrada pode ajudar antes de um comitê formal. A possibilidade de reduzir esforço depende da aplicação e deve ser observada, sem pressupor custo zero.

O manual introdutório também usava DAA, “direcionar, agir e acompanhar”, para explicar a participação da direção. Trata-se de uma descrição didática da responsabilidade: decidir o que importa, executar o autorizado e verificar o efeito. Não substitui o ciclo ADM-Lite nem cria outro domínio. Os nomes antigos “orquestrador de valor”, “agente de mudança” e “parceiro estratégico” expressavam funções pretendidas, sem comprovar promoção de cargo ou transformação profissional.

Origem documental: mestres leigo e técnico em `GP-PME/` e mestre consolidado em `GP-PME antigravity/`, versões declaradas 6.0 e 5.2, de 02/06/2026. Essas contribuições são escolhas autorais, sem atribuição a uma norma externa.

### Versões e direitos

GEAR 2026.10 identifica a edição editorial. Números antigos 2.0, 5.2 e 6.0 são metadados de suas respectivas versões, não versões simultâneas do produto vigente. Identificadores de software GP-PME permanecem quando necessários à compatibilidade. O histórico de origem deve acompanhar a migração de conteúdo.

Os direitos seguem [LICENSE.md](<../../LICENSE.md>). Não há nova certificação, validação de marca ou concessão de direitos nesta consolidação.

### Evidência acadêmica

O manuscrito mantém um protocolo prospectivo com casos sintéticos. Nenhuma simulação comprova ganho de campo. Silva, Mira da Silva e Pereira (2018), DOI [10.1109/CBI.2018.10044](https://doi.org/10.1109/CBI.2018.10044), é uma referência bibliográfica verificada; não se infere que valide GEAR. O conjunto de título, periódico e ano da referência antiga de Verdecchia não foi confirmado. A pesquisa identificou um estudo ATDx de 2022 na PeerJ e um artigo de teoria de 2021 no Journal of Systems and Software, ambos distintos da entrada antiga. Metadados e resumo não sustentam a fórmula de DAN financeiro; nenhum artigo foi adotado como substituto automático. Veja [fontes e limites](<../../framework/referencias/fontes.md#bibliografia-e-acesso-limitado>). Acesso limitado à ISO e a livros licenciados impede atribuição de detalhes não consultados.

Consulta: [Fontes e limites](<../../framework/referencias/fontes.md>). Análise aplicada: [Caso didático](<../../framework/exemplos/caso-didatico.md>).



Consulta: [fontes e limites](../../framework/referencias/fontes.md). Regra vigente: [documentação modular](../../framework/README.md).
