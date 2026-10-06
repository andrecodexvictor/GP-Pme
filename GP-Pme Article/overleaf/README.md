# Artigo GEAR: pacote LaTeX

O manuscrito começou em agosto de 2026 e foi revisto em 6 de outubro. Apresenta a construção do GEAR e o uso ativo de IA na pesquisa e na produção com auditoria de conteúdo. O método distingue fontes externas, adaptações autorais e hipóteses, sem estimar benefício causal da IA. MCPs, skills e integrações são apenas citados. A prova de conceito futura no [FrameSim](https://github.com/andrecodexvictor/Frame-sim) prevê 25 casos comparativos; nenhuma rodada foi executada nesta versão.

O [repositório e a branch editorial](https://github.com/andrecodexvictor/GP-Pme/tree/codex/gear-editorial) contêm as fontes; a [revisão de referência](https://github.com/andrecodexvictor/GP-Pme/tree/8386586af110ba2112694a8ee6dd7b9d94d20572) fixa o estado anterior à atualização. As referências bibliográficas têm links para documentos, DOI ou páginas institucionais. GP-PME é o nome histórico do acervo.

## Estrutura

- `main.tex`: ponto de entrada do Overleaf.
- `sections/`: seções editáveis do manuscrito.
- `references.bib`: referências bibliográficas.
- `figures/mermaid/`: fontes Mermaid versionadas.
- `figures/generated/`: PDFs consumidos pelo LaTeX.
- `supplement/scenario-catalog.csv`: catálogo congelável dos 25 casos.

## Gerar os diagramas

O fluxo vigente usa rótulos das fontes Mermaid e layouts vetoriais explícitos, sem baixar um renderizador. Na raiz do projeto:

```powershell
npm run build:figures
```

O gerador `tools/build_figures.py` conserva nomes dos PDFs consumidos pelo LaTeX e registra hashes. `build-figures.ps1` é uma alternativa histórica com Mermaid CLI fixada. Os PDFs acompanham as fontes; Overleaf não executa Mermaid diretamente.

## Compilar

No Overleaf, selecione `main.tex` como documento principal e use pdfLaTeX. A bibliografia usa BibTeX e `plainnat`, sem classe institucional específica. Antes de uma submissão, adapte classe, margens, limite de palavras e estilo bibliográfico ao veículo escolhido.

O projeto oferece `tools/build_article.ps1`, com Tectonic e saída configuráveis. Saída padrão: `.context/publicacoes/GEAR_artigo_2026-10.pdf`. O manuscrito tem vários arquivos; não achatá-lo em standalone para contornar limitações do editor.

Compilação local equivalente com uma instalação TeX:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Campos editoriais a confirmar

- coautoria e ordem de autores;
- e-mail e ORCID;
- veículo ou template de submissão;
- aprovação da redação final pelos orientadores;
- condições de distribuição conforme as licenças já publicadas;
- identificador do protocolo e commit do FrameSim antes dos testes.
