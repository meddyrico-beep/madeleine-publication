$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

Write-Host "[MADELEINE] Limpieza conservadora de repo de publicación"

$patterns = @("*.aux","*.log","*.toc","*.out","*.nav","*.snm","*.fls","*.fdb_latexmk","*.synctex.gz","*.xdv","*.bcf","*.run.xml","*.bbl","*.blg","*.bak","*.bak_*")
foreach ($pat in $patterns) {
    Get-ChildItem -Path $RepoRoot -Recurse -File -Filter $pat -ErrorAction SilentlyContinue | Remove-Item -Force
}

$paths = @(
    "backup",
    "artifacts\snapshots",
    "migration\deferred",
    "tomo1"
)
foreach ($rel in $paths) {
    $p = Join-Path $RepoRoot $rel
    if (Test-Path $p) { Remove-Item $p -Recurse -Force }
}

Get-ChildItem -Path (Join-Path $RepoRoot "manuscript") -Recurse -File -Filter "main.pdf" -ErrorAction SilentlyContinue | Remove-Item -Force
Get-ChildItem -Path (Join-Path $RepoRoot "artifacts") -File -Filter "*.zip" -ErrorAction SilentlyContinue | Remove-Item -Force

Write-Host "[OK] Limpieza terminada. No se ha eliminado .git."
