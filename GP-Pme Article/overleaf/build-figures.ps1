param(
  [string]$MermaidCliVersion = "11.12.0"
)

$ErrorActionPreference = "Stop"
$articleRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceDir = Join-Path $articleRoot "figures\mermaid"
$outputDir = Join-Path $articleRoot "figures\generated"

New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

$figures = @(
  "research-pipeline",
  "gppme-architecture",
  "results-template"
)

foreach ($name in $figures) {
  $inputFile = Join-Path $sourceDir "$name.mmd"
  $outputFile = Join-Path $outputDir "$name.pdf"
  & npx --yes "@mermaid-js/mermaid-cli@$MermaidCliVersion" -i $inputFile -o $outputFile -b transparent --pdfFit
  if ($LASTEXITCODE -ne 0) {
    throw "Falha ao renderizar $name"
  }
}

Write-Host "Diagramas renderizados em $outputDir"
