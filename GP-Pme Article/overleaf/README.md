# Artigo GEAR: pacote LaTeX

O manuscrito começou em agosto de 2026 e foi revisto editorialmente em outubro. GP-PME é o nome da instanciação histórica citada; GEAR é a edição consolidada. Os 25 casos comparativos ainda não foram executados.

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
- URL pública e licença dos artefatos;
- identificador do protocolo e commit do Frame-sim antes dos testes.
