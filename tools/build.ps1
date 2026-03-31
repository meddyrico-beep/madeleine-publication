param(
    [ValidateSet("base_axiomatica","tomo1","tomo2","tomo3","all")]
    [string]$Piece = "tomo1"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

function Build-One([string]$Name) {
    $work = Join-Path $RepoRoot ("manuscript\" + $Name)
    Push-Location $work
    try {
        xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
        if ($LASTEXITCODE -ne 0) { throw "Falló XeLaTeX en $Name (pasada 1)" }
        xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
        if ($LASTEXITCODE -ne 0) { throw "Falló XeLaTeX en $Name (pasada 2)" }

        $pdf = Join-Path $work "main.pdf"
        $dst = Join-Path $RepoRoot ("artifacts\pdf\" + $Name + ".pdf")
        Copy-Item $pdf $dst -Force
        Write-Host "OK PDF: $dst"
    }
    finally {
        Pop-Location
    }
}

if ($Piece -eq "all") {
    "base_axiomatica","tomo1","tomo2","tomo3" | ForEach-Object { Build-One $_ }
} else {
    Build-One $Piece
}
