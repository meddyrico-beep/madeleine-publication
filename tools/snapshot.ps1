param()

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$OutDir = Join-Path $RepoRoot "artifacts\snapshots"

Push-Location $RepoRoot
try {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
        throw "Git no está disponible en PATH."
    }

    $status = @(git status --porcelain)
    if ($LASTEXITCODE -ne 0) {
        throw "No se pudo consultar git status."
    }

    if ($status.Count -gt 0) {
        throw "El snapshot requiere un árbol Git limpio."
    }

    $head = (git rev-parse HEAD).Trim()
    if ($LASTEXITCODE -ne 0) {
        throw "No se pudo resolver HEAD."
    }

    $short = (git rev-parse --short=12 HEAD).Trim()
    $branch = (git rev-parse --abbrev-ref HEAD).Trim()

    New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $zipName = "snapshot_${timestamp}_${short}.zip"
    $zipPath = Join-Path $OutDir $zipName

    $snapshotPaths = @(
        ".gitignore",
        "README.md",
        "REPRODUCIBILITY.md",
        "MANIFESTO.md",
        "ADMISSION_RULES.md",
        "manuscript",
        "lab",
        "demos",
        "notes",
        "tests",
        "tools"
    )

    $gitArgs = @(
        "archive",
        "--format=zip",
        "--output=$zipPath",
        "HEAD",
        "--"
    ) + $snapshotPaths

    & git @gitArgs

    if ($LASTEXITCODE -ne 0) {
        throw "Falló git archive."
    }

    if (-not (Test-Path $zipPath)) {
        throw "El ZIP esperado no fue creado."
    }

    $hash = Get-FileHash -Algorithm SHA256 $zipPath
    $metaPath = $zipPath + ".sha256.txt"

    $meta = @(
        "SHA256  $($hash.Hash)  $zipName",
        "HEAD    $head",
        "BRANCH  $branch",
        "CREATED_LOCAL  $(Get-Date -Format "yyyy-MM-ddTHH:mm:ssK")"
    )

    $utf8 = New-Object System.Text.UTF8Encoding($false)

    [System.IO.File]::WriteAllText(
        $metaPath,
        (($meta -join "`n") + "`n"),
        $utf8
    )

    Write-Host "OK SNAPSHOT"
    Write-Host "ZIP:    $zipPath"
    Write-Host "SHA256: $($hash.Hash)"
    Write-Host "HEAD:   $head"
    Write-Host "BRANCH: $branch"
    Write-Host "META:   $metaPath"
}
finally {
    Pop-Location
}
