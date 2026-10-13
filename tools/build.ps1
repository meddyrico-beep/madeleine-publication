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
        $mainTex = Join-Path $work "main.tex"
        $needsBiber = Select-String `
            -Path $mainTex `
            -Pattern '\\addbibresource' `
            -Quiet

        xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
        if ($LASTEXITCODE -ne 0) { throw "Falló XeLaTeX en $Name (pasada 1)" }

        if ($needsBiber) {
            if (-not (Get-Command biber -ErrorAction SilentlyContinue)) {
                throw "Biber es requerido por $Name pero no está disponible."
            }

            biber main
            if ($LASTEXITCODE -ne 0) { throw "Falló Biber en $Name" }

            xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
            if ($LASTEXITCODE -ne 0) { throw "Falló XeLaTeX en $Name (pasada 2)" }

            xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
            if ($LASTEXITCODE -ne 0) { throw "Falló XeLaTeX en $Name (pasada 3)" }
        }
        else {
            xelatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
            if ($LASTEXITCODE -ne 0) { throw "Falló XeLaTeX en $Name (pasada 2)" }
        }

        $pdf = Join-Path $work "main.pdf"

        if ($Name -eq "base_axiomatica") {
            $dst = Join-Path $RepoRoot "artifacts\pdf\internal\base_axiomatica.pdf"
            $legacyBase = Join-Path $RepoRoot "artifacts\pdf\base_axiomatica.pdf"
        }
        else {
            $dst = Join-Path $RepoRoot ("artifacts\pdf\" + $Name + ".pdf")
            $legacyBase = $null
        }

        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dst) | Out-Null
        Copy-Item $pdf $dst -Force

        if ($legacyBase -and (Test-Path $legacyBase)) {
            Remove-Item $legacyBase -Force
        }

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
