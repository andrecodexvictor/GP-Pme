param(
  [string]$Tectonic = "",
  [string]$OutputDirectory = ""
)
$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
if (-not $Tectonic) { $Tectonic = Join-Path $projectRoot ".context\tools\tectonic-nupkg-032\tools\tectonic.exe" }
if (-not $OutputDirectory) { $OutputDirectory = Join-Path $projectRoot ".context\publicacoes\artigo-build" }
$articleSource = Join-Path $projectRoot "GP-Pme Article\overleaf\main.tex"
New-Item -ItemType Directory -Path $OutputDirectory -Force | Out-Null
& $Tectonic --keep-logs --outdir $OutputDirectory $articleSource
if ($LASTEXITCODE -ne 0) { throw "Compilação do artigo falhou. Fontes preservadas; consultar logs." }
$articleOutput = Join-Path (Split-Path -Parent $OutputDirectory) "GEAR_artigo_2026-10.pdf"
Copy-Item -LiteralPath (Join-Path $OutputDirectory "main.pdf") -Destination $articleOutput -Force
Write-Output "Artigo compilado em $articleOutput"
