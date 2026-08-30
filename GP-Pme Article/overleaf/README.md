# Artigo GP-PME — pacote Overleaf

Este diretório contém a primeira versão do artigo em LaTeX. O manuscrito descreve o artefato e o protocolo prospectivo; os 25 testes ainda não foram executados.

## Estrutura

- `main.tex`: ponto de entrada do Overleaf.
- `sections/`: seções editáveis do manuscrito.
- `references.bib`: referências bibliográficas.
- `figures/mermaid/`: fontes Mermaid versionadas.
- `figures/generated/`: PDFs consumidos pelo LaTeX.
- `supplement/scenario-catalog.csv`: catálogo congelável dos 25 casos.

## Gerar os diagramas

Com Node.js e `npx` disponíveis, execute no PowerShell:

```powershell
.\build-figures.ps1
```

O script fixa a versão da Mermaid CLI. Os PDFs gerados devem ser enviados ao Overleaf junto com as fontes; o Overleaf não executa Mermaid diretamente.

## Compilar

No Overleaf, selecione `main.tex` como documento principal e use pdfLaTeX. A bibliografia usa BibTeX e `plainnat`, sem classe institucional específica. Antes de uma submissão, adapte classe, margens, limite de palavras e estilo bibliográfico ao veículo escolhido.

Compilação local equivalente:

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
- URL pública e licença dos artefatos;
- identificador do protocolo e commit do Frame-sim antes dos testes.
