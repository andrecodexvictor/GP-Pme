# Identidade de leitura GEAR

O portal deve parecer um instrumento de consulta mantido por quem usa o método. Organização funcional de IBM/Carbon e estruturas docs-page/blog-post do Open Design orientam navegação e hierarquia. A identidade resultante é própria: não usa logotipos, fontes ou declarações de vínculo com IBM.

## Cor e tipografia

Superfície `#ffffff`; tinta `#202321`; texto secundário `#555d59`; superfície de apoio `#f3f5f2`; borda `#d6dcd7`; cobre interativo `#8a421e`; foco `#124e67`. A identidade editorial acrescenta petróleo `#173f43`, papel quente `#f7f3ec` e cobre claro `#e8ad83`. Petróleo ancora capa, aberturas e cabeçalhos; cobre escuro identifica links e rótulos em fundo claro; cobre claro sinaliza o percurso sobre petróleo. Cor identifica função, sem substituir texto. Links no portal têm sublinhado.

Public Sans v2.001 em navegação e títulos; Source Serif 4 v4.005 na leitura longa. Arquivos locais regulares, itálicos e pesos 600/700, com OFL 1.1 e manifesto de origem. Fallbacks: Arial e Georgia. Corpo documental 18px, entrelinha 1,65, largura até 70 caracteres como escolha a validar; rótulos 14–16px; H1 responsivo de 36 a 64px.

## Composição

Grade de intervalos 4/8/12/16/24/32/48/64px. Cabeçalho simples, conteúdo com início claro, navegação lateral contextual e sumário local. Listagens usam linhas e descrições; não repetir cartões decorativos. Home distingue entrada de adoção, mapa do método e biblioteca. Blog tem lista por tema e artigos com autoria, data, referências e próxima leitura.

Tabelas mantêm cabeçalhos semânticos e podem rolar horizontalmente quando a comparação exigir duas dimensões. Parágrafos, títulos e controles se adaptam a telas estreitas. Sem alturas fixas na leitura; sem texto em gradiente, vidro, sombras redundantes ou bordas laterais grossas.

## Interação e estados

Menu móvel é um disclosure nativo. Foco visível de 3px, sem cabeçalho que esconda âncoras. Busca tem campo rotulado, filtro por tipo, resultado com contexto/origem, estado inicial, consulta vazia e erro de índice. Resultados usam links reais. JavaScript não esconde o conteúdo documental. Não há animação necessária à leitura; respeitar movimento reduzido.

## Impressão e PDF

Capa ocupa uma página breve. Pré-textuais compactos, sumário com links, capítulos e subtítulos identificados; texto selecionável, fontes incorporadas, idioma e metadados. Margens independentes do layout de tela. Tabelas podem continuar com cabeçalho repetido. Evitar título isolado e bloco maior que a página protegido contra quebra.

### Identidade do livro

A capa combina um campo petróleo, o nome GEAR em Public Sans Bold, a expansão do nome em Source Serif 4 e uma base de papel quente com autoria e edição. O percurso decidir, executar, verificar e revisar aparece como geometria de orientação; não é um conjunto de novos pilares. A marca tipográfica dispensa engrenagens, fotografias genéricas e ícones decorativos.

As aberturas têm número de capítulo, parte editorial e título em um único bloco. Oito partes organizam núcleo, adoção, guias, indicadores, exemplos, modelos, fundamentos e vocabulário/fontes. A parte é sempre escrita, permitindo orientação sem depender da cor. Não há páginas vazias de separação entre partes.

O corpo permanece branco, com Serif 10,8pt e entrelinha 15,8pt; títulos de capítulo têm Public Sans Bold 23pt/28pt; subtítulos 14pt/18pt. Margens de 52pt mantêm a coluna de leitura. Tabelas usam cabeçalho petróleo com texto branco, linhas alternadas discretas e cabeçalhos repetidos. Campos copiáveis usam papel quente, margem interna de 12pt e contorno leve; exemplos conservam rótulos de caráter ilustrativo. Fluxogramas são vetoriais e preservam ramificações, rótulos e alternativa textual.

Os contrastes branco/petróleo, cobre claro/petróleo, cobre escuro/branco e tinta/papel são registrados na verificação da revisão. Cobre claro não serve ao corpo sobre fundo branco. A conferência numérica orienta escolhas, sem constituir certificação de acessibilidade do PDF.

`tools/book_design.py` concentra os componentes editoriais; `tools/build_book.py` aplica-os às fontes canônicas. A versão HTML do livro usa `assets/book.css` com os mesmos papéis visuais e adapta a largura a telas pequenas. O portal aprovado conserva sua composição; o artigo científico mantém convenções acadêmicas e usa a identidade nas figuras e links.

## Rastreabilidade de design

Referências de composição: Open Design, catálogo local em 04/10/2026, IBM, docs-page, blog-post e craft typography/hierarchy/rtl. Critérios: Impeccable 3.9.1. Os placeholders e controles demonstrativos dos templates foram descartados. A verificação real determina o aceite; o detector orienta correções e não comprova autoria ou acessibilidade.
