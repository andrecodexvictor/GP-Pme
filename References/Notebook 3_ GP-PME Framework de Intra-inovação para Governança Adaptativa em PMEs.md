# Notebook: melhoria, fontes e assistência

Edição editorial GEAR 2026.10. Documento autoral consolidado; regras vigentes derivadas da fonte modular. Direitos conforme LICENSE.md.

## Origem e decisão editorial

O registro declarava 35 fontes e reunia intra-inovação, TI enxuta, prompts e transformação digital. A contagem histórica não comprova fontes verificadas; consultar fichas da edição vigente. ISO 27001, literatura de transformação digital e outras obras locais não implicam conformidade ou incorporação integral. As três frentes e o piloto de melhoria foram preservados.

Origem declarada no registro anterior, sem nova consulta:

- https://notebooklm.google.com/notebook/91ad76ea-57bf-4008-a291-d82830c84a39

## Entregar uma melhoria pequena

Use para uma alteração de TI com resultado verificável por um processo de negócio. Responsável por TI prepara a solução; dono do processo define e verifica o aceite; direção aprova recursos e riscos conforme a alçada. Entrada: necessidade, situação atual, restrições e capacidade. Saída: mudança verificada, registro de aceite e efeito a acompanhar.

### Delimitar

Registrar problema, beneficiário, escopo, exclusões e condição de sucesso em um PRD curto. Uma ou duas semanas podem ser o intervalo de um piloto; se o escopo não couber, reduzir a entrega ou negociar outro prazo. A duração não substitui uma estimativa de capacidade.

Um requisito pode usar “Dado/Quando/Então”: dado um pedido autorizado, quando o relatório é solicitado, então os campos definidos aparecem sem edição manual. Esse exemplo descreve comportamento esperado, não afirma que a solução já foi implementada.

### Executar

1. Conferir dados, permissões, integrações e dependências.
2. Definir executor e quem aceitará a saída.
3. Registrar critério de verificação, risco e retorno à condição anterior.
4. Selecionar trabalho compatível com a fila e seu limite.
5. Construir e testar o recorte acordado.
6. Verificar com o usuário ou dono do processo; registrar aceite ou correções.
7. Acompanhar a hipótese de benefício na janela definida.

### Aprender com a entrega

Uma solução aceita pode não produzir o benefício esperado. Medir uso, efeito e esforço de manutenção. Se a hipótese falhar, registrar o resultado e decidir adaptar ou interromper, sem reclassificá-lo como sucesso apenas porque houve implementação.

As práticas de inspeção e adaptação são compatíveis com a inspiração ágil; retirar elementos de Scrum impede chamar qualquer ciclo curto de implementação integral desse framework. [F03](<../framework/referencias/fontes.md#f03>)

Modelo: [PRD e aceite](<../framework/templates/prd-aceite.md>). Próxima tarefa: [Conduzir uma revisão](<../framework/guias/conduzir-revisao.md>).


## Fontes e limites de uso

Consultas realizadas em **4 e 5 de outubro de 2026**, com data e recorte em cada entrada. Fontes primárias fundamentam conceitos; não demonstram efetividade do GEAR nem validam suas faixas, pesos, prazos ou fórmulas.

### F01

*NIST Cybersecurity Framework 2.0: Small Business Quick-Start Guide*, Daniel Eliot, NIST. NIST SP 1300, publicado em 26/02/2024.

[Registro oficial](https://www.nist.gov/publications/nist-cybersecurity-framework-20-small-business-quick-start-guide), [DOI](https://doi.org/10.6028/NIST.SP.1300), [PDF oficial](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1300.pdf).

Seção consultada e limite: Resumo e pp. 2–8. Guia suplementar para pequenas organizações; não valida parâmetros do GEAR. Consulta: 04/10/2026.

### F02

*The NIST Cybersecurity Framework (CSF) 2.0*, NIST. NIST CSWP 29, 26/02/2024.

[DOI](https://doi.org/10.6028/NIST.CSWP.29), [PDF oficial](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf).

Seção consultada e limite: Resumo, Executive Summary e seção 3. Resultados e perfis; não prescreve uma implementação única. Consulta: 04/10/2026.

### F03

*O Guia do Scrum: O Guia Definitivo para o Scrum: As Regras do Jogo*, Ken Schwaber e Jeff Sutherland. Novembro de 2020; tradução brasileira distribuída no site oficial, arquivo PortugueseBR-3.0.

[Índice oficial](https://scrumguides.org/download.html), [PDF em português brasileiro](https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-PortugueseBR-3.0.pdf).

Seção consultada e limite: Definição de Scrum e Scrum Team, pp. 2, 4, 6–8. Práticas inspiradas não equivalem a Scrum completo. Consulta: 04/10/2026.

### F04

*TOGAF*, The Open Group. Página pública com apresentação da 10ª edição; a página também apresenta a versão 9.2.

[Página oficial](https://www.opengroup.org/togaf).

Seção consultada e limite: Apresentação pública da 10ª edição. Capítulos detalhados redirecionaram a autenticação; ADM-Lite é local. Consulta: 04/10/2026.

### F05

*DORA's software delivery performance metrics*, Nathen Harvey, DORA / Google Cloud. Atualizada em 05/01/2026.

[Guia oficial](https://dora.dev/guides/dora-metrics/).

Seção consultada e limite: Key insights e Common pitfalls. Cinco métricas para entrega de software; não métricas gerais de governança. Consulta: 04/10/2026.

### F06

*A history of DORA's software delivery metrics*, Nathen Harvey, DORA / Google Cloud. Publicada e atualizada em 02/01/2026.

[Histórico oficial](https://dora.dev/insights/dora-metrics-history/).

Seção consultada e limite: Refining definitions e From four keys to five. Distingue recuperação de implantação com falha de MTTR geral. Consulta: 04/10/2026.

### F07

*Web Content Accessibility Guidelines (WCAG) 2.2*, W3C. Recomendação de 12/12/2024, versão servida na consulta.

[Versão fixa](https://www.w3.org/TR/2024/REC-WCAG22-20241212/), [URL da versão publicada mais recente](https://www.w3.org/TR/WCAG22/).

Seção consultada e limite: Critérios 1.4.3, 1.4.10, 1.4.12, 2.1.1, 2.4.7, 2.4.11 e 2.5.8. Alvo de teste; sem declaração de conformidade. Consulta: 04/10/2026.

### F08

*Diátaxis*, Daniele Procida. Site em evolução; data de publicação e número de versão não declarados nas páginas consultadas.

[Apresentação](https://diataxis.fr/), [Introdução de cinco minutos](https://diataxis.fr/start-here/), [Autoria e citação](https://diataxis.fr/colophon/).

Seção consultada e limite: Start here e Colophon. Orientação editorial, sem estudo de usabilidade específico do GEAR. Consulta: 04/10/2026.

### F09

*COBIT*, ISACA. Página sobre COBIT 2019, sem data única de publicação.

[Página oficial](https://www.isaca.org/resources/cobit).

Seção consultada e limite: Why COBIT e Practical Guidance. Adaptação ao contexto; não se atribuem fórmulas locais à ISACA. Consulta: 04/10/2026.

### F10

*ITIL 4 Foundation*, PeopleCert. Página específica do ITIL 4 Foundation, sem data única de publicação.

[Página oficial](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-foundation-2565).

Seção consultada e limite: What will you learn? e Guiding principles. Escopo ITIL 4, sem alegação sobre edição mais recente do portfólio. Consulta: 04/10/2026.

### F11

Center for Internet Security. *CIS Critical Security Controls Implementation Groups*. Página institucional, sem data única declarada. [Fonte oficial](https://www.cisecurity.org/controls/implementation-groups). Seção IG1: 56 salvaguardas de higiene cibernética. Consulta: 04/10/2026. Uma seleção de quatro práticas ou dez verificações locais não equivale à implantação integral do IG1.

### F12

CISA, MS-ISAC, NSA e FBI. *#StopRansomware Guide*. Guia institucional, versão consultada em 04/10/2026. [Página oficial](https://www.cisa.gov/stopransomware/ransomware-guide). Seções sobre prevenção e resposta: backups offline e encriptados, teste regular, MFA resistente a phishing e menor privilégio. O guia não oferece garantia de proteção nem sustenta o percentual de 95% anunciado em versões históricas.

### F13

Verdecchia, Roberto; Lago, Patricia; Malavolta, Ivano; Ozkaya, Ipek. *ATDx: Building an Architectural Technical Debt Index*. ENASE 2020, SciTePress, 2020, pp. 531–539. DOI [10.5220/0009577805310539](https://doi.org/10.5220/0009577805310539). [Manuscrito do primeiro autor](https://robertoverdecchia.github.io/papers/ENASE_2020.pdf); [registro institucional VU](https://research.vu.nl/en/publications/22b62e22-79f4-4cbb-a552-9151b7353862).

Seções consultadas: §§ 2.1–2.2, 4.1.6, 4.2 e 6; páginas 2–3 e 6–8 do PDF do autor. A normalização usa violações por elementos de código e análise estatística de projetos; não orçamento de TI. O texto não fundamenta DAN financeira, faixas 0,15/0,35, COT ou ROI em PME. Consulta: 05/10/2026. Paginação do manuscrito difere do registro dos anais; não foi transposta.

### F14

Hacks, Simon; Höfert, Hendrik; Salentin, Johannes; Yeong, Yoon Chow; Lichter, Horst. *Towards the Definition of Enterprise Architecture Debts*. IEEE EDOCW, 2019, pp. 9–16. DOI [10.1109/EDOCW.2019.00016](https://doi.org/10.1109/EDOCW.2019.00016). [Registro e versão dos autores](https://arxiv.org/abs/1907.00677); [preprint v1, 28/06/2019](https://arxiv.org/pdf/1907.00677v1).

Seções consultadas: §§ 2, 4–7, páginas 2 e 4–7 do preprint. Propõe uma definição de dívida de arquitetura empresarial com ponderação contextual e demonstração por casos fictícios; avaliação real está fora do escopo. Não fundamenta COT, ROI, DAN financeira ou faixas para PME. Consulta: 05/10/2026. Metadados IEEE conferidos; o texto final dos anais não foi comparado integralmente ao preprint.

### F15

Brasil. *Lei nº 13.709, de 14 de agosto de 2018: Lei Geral de Proteção de Dados Pessoais (LGPD)*. Texto atualizado disponibilizado pela Câmara dos Deputados. [Texto oficial](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html).

Captura oficial realizada em 04/10/2026; releitura dos arts. 6º, 7º, 18, 37, 46 e 48 em 05/10/2026. Os dispositivos fundamentam princípios, hipóteses legais, direitos, registros, segurança e comunicação de incidentes. A seleção não é análise integral de conformidade, nem permite presumir enquadramento especial de uma PME. O registro local do GEAR não substitui a avaliação das obrigações aplicáveis.

### F16

Autoridade Nacional de Proteção de Dados. *Comunicação de Incidentes de Segurança — CIS*. Página publicada em 23/12/2022; modificação indicada em 26/08/2026 na consulta. [Orientação oficial](https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis).

Consulta e captura: 04/10/2026. Perguntas 4–6: prazo geral de três dias úteis para comunicação à ANPD e aos titulares nos casos sujeitos à obrigação, ressalvado prazo em legislação específica; comunicação complementar não substitui a inicial. A página referencia a Resolução nº 15/2024, cujo texto integral não foi obtido nesta pesquisa. Marco inicial, contagem e exceções requerem conferência do ato aplicável. As regras de agentes de pequeno porte não foram verificadas integralmente; não se atribui prazo diferenciado pelo número de empregados.

### Tipografia local

US Web Design System / GSA. *Public Sans*, v2.001. [Repositório oficial](https://github.com/uswds/public-sans). Adobe. *Source Serif*, v4.005. [Repositório oficial](https://github.com/adobe-fonts/source-serif). Consulta: 04/10/2026. Arquivos distribuídos com SIL Open Font License 1.1; versões, commits, URLs dos binários e SHA-256 registrados no manifesto de fontes que acompanha os ativos. Os arquivos não foram modificados.

### Bibliografia e acesso limitado

Silva, David; Mira da Silva, Miguel; Pereira, Ruben. *Baseline Mechanisms for Enterprise Governance of IT in SMEs*. IEEE CBI, 2018, pp. 32–41. DOI [10.1109/CBI.2018.10044](https://doi.org/10.1109/CBI.2018.10044). Metadados verificados; não demonstra eficácia do GEAR.

A entrada histórica atribuída a Verdecchia em 2022 mistura um título e periódico que não foram confirmados em conjunto. Dois trabalhos reais foram identificados: *Empirical evaluation of an architectural technical debt index in the context of the Apache and ONAP ecosystems* (Verdecchia, Malavolta, Lago e Ozkaya, **PeerJ Computer Science**, 8:e833, 07/02/2022), DOI [10.7717/peerj-cs.833](https://doi.org/10.7717/peerj-cs.833); e *Building and evaluating a theory of architectural technical debt in software-intensive systems* (Verdecchia, Kruchten, Lago e Malavolta, **Journal of Systems and Software**, 176:110925, junho de 2021), DOI [10.1016/j.jss.2021.110925](https://doi.org/10.1016/j.jss.2021.110925).

Fontes consultadas em 04/10/2026: registros depositados pelas editoras no Crossref, [2022](https://api.crossref.org/works/10.7717/peerj-cs.833) e [2021](https://api.crossref.org/works/10.1016/j.jss.2021.110925). Foram verificados metadados e resumo do artigo de 2022, que descreve ATDx baseado em SonarQube nos ecossistemas Apache e ONAP; somente metadados do artigo de 2021. O texto integral não foi acessado. Nenhum foi usado como substituição automática da referência antiga nem valida a fórmula financeira de DAN ou o ROI do GEAR. A similaridade de títulos não comprova qual documento originou a entrada histórica.

O catálogo/OBP ISO retornou bloqueio de acesso; capítulos TOGAF exigiram autenticação. Não atribuir detalhes dessas normas ou de livros licenciados como se tivessem sido lidos. As sínteses históricas do acervo são material de trabalho, não substitutos dos documentos originais.

