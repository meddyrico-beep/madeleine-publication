param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern("^[A-Za-z0-9._-]+$")]
    [string]$Version
)

$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Parent $PSScriptRoot
$ReleaseRoot = Join-Path $RepoRoot "release"
$SnapshotTool = Join-Path $PSScriptRoot "snapshot.ps1"

function Write-Utf8NoBom {
    param(
        [string]$Path,
        [string[]]$Lines
    )

    $utf8 = New-Object System.Text.UTF8Encoding($false)

    [System.IO.File]::WriteAllText(
        $Path,
        (($Lines -join "`n") + "`n"),
        $utf8
    )
}

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
        throw "El release requiere un árbol Git limpio."
    }

    $head = (git rev-parse HEAD).Trim()
    $short = (git rev-parse --short=12 HEAD).Trim()
    $branch = (git rev-parse --abbrev-ref HEAD).Trim()

    $artifacts = @(
        @{
            Source = "artifacts\pdf\tomo1.pdf"
            Dest = "pdf\MADELEINE_Tomo_I_Fundamento_Blindaje_Significado.pdf"
            Role = "PUBLIC"
        },
        @{
            Source = "artifacts\pdf\tomo2.pdf"
            Dest = "pdf\MADELEINE_Tomo_II_Canon_Transicion_Jerarquia.pdf"
            Role = "PUBLIC"
        },
        @{
            Source = "artifacts\pdf\tomo3.pdf"
            Dest = "pdf\MADELEINE_Tomo_III_Metodo_Demos_Claims.pdf"
            Role = "PUBLIC"
        },
        @{
            Source = "artifacts\pdf\internal\base_axiomatica.pdf"
            Dest = "internal\MADELEINE_Base_Axiomatica_Internal.pdf"
            Role = "INTERNAL"
        }
    )

    foreach ($artifact in $artifacts) {
        $source = Join-Path $RepoRoot $artifact.Source

        if (-not (Test-Path $source)) {
            throw "Falta artefacto requerido: $($artifact.Source)"
        }
    }

    if (-not (Test-Path $SnapshotTool)) {
        throw "No existe tools\snapshot.ps1."
    }

    Write-Host "Generating commit-exact snapshot..."
    & $SnapshotTool

    $snapshot = Get-ChildItem (Join-Path $RepoRoot "artifacts\snapshots") -File |
        Where-Object {
            $_.Name -like "snapshot_*_${short}.zip"
        } |
        Sort-Object LastWriteTime -Descending |
        Select-Object -First 1

    if (-not $snapshot) {
        throw "No se encontró snapshot correspondiente a HEAD $short."
    }

    $snapshotMeta = $snapshot.FullName + ".sha256.txt"

    if (-not (Test-Path $snapshotMeta)) {
        throw "Falta metadata SHA256 del snapshot."
    }

    $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $created = Get-Date -Format "yyyy-MM-ddTHH:mm:ssK"

    $packageName = "MADELEINE_publication_${Version}_${stamp}"
    $packageDir = Join-Path $ReleaseRoot $packageName

    if (Test-Path $packageDir) {
        throw "El directorio de release ya existe: $packageDir"
    }

    New-Item -ItemType Directory -Force -Path $ReleaseRoot | Out-Null
    New-Item -ItemType Directory -Force -Path $packageDir | Out-Null
    New-Item -ItemType Directory -Force -Path (Join-Path $packageDir "pdf") | Out-Null
    New-Item -ItemType Directory -Force -Path (Join-Path $packageDir "internal") | Out-Null
    New-Item -ItemType Directory -Force -Path (Join-Path $packageDir "snapshot") | Out-Null

    foreach ($artifact in $artifacts) {
        $source = Join-Path $RepoRoot $artifact.Source
        $dest = Join-Path $packageDir $artifact.Dest
        Copy-Item $source $dest -Force
    }

    Copy-Item $snapshot.FullName `
        (Join-Path $packageDir ("snapshot\" + $snapshot.Name)) `
        -Force

    Copy-Item $snapshotMeta `
        (Join-Path $packageDir ("snapshot\" + (Split-Path $snapshotMeta -Leaf))) `
        -Force

    $readmeLines = @(
        "MADELEINE — Release package",
        "",
        "VERSION  $Version",
        "HEAD     $head",
        "BRANCH   $branch",
        "CREATED  $created",
        "",
        "PUBLIC CONTENT",
        "- pdf/MADELEINE_Tomo_I_Fundamento_Blindaje_Significado.pdf",
        "- pdf/MADELEINE_Tomo_II_Canon_Transicion_Jerarquia.pdf",
        "- pdf/MADELEINE_Tomo_III_Metodo_Demos_Claims.pdf",
        "",
        "INTERNAL TECHNICAL SUPPORT",
        "- internal/MADELEINE_Base_Axiomatica_Internal.pdf",
        "",
        "REPRODUCIBLE SOURCE SNAPSHOT",
        "- snapshot/$($snapshot.Name)",
        "- snapshot/$(Split-Path $snapshotMeta -Leaf)",
        "",
        "INTEGRITY",
        "- MANIFEST_PUBLICATION.txt",
        "- SHA256SUMS.txt",
        "",
        "The source snapshot contains REPRODUCIBILITY.md.",
        "",
        "Scientific scope:",
        "Internal formal and numerical results do not by themselves constitute external physical validation."
    )

    Write-Utf8NoBom `
        -Path (Join-Path $packageDir "README_RELEASE.txt") `
        -Lines $readmeLines

    $manifestLines = @(
        "MADELEINE — Publication Manifest",
        "",
        "VERSION  $Version",
        "HEAD     $head",
        "BRANCH   $branch",
        "CREATED  $created",
        "TREE     CLEAN",
        ""
    )

    foreach ($artifact in $artifacts) {
        $dest = Join-Path $packageDir $artifact.Dest
        $file = Get-Item $dest
        $hash = (Get-FileHash -Algorithm SHA256 $dest).Hash
        $rel = $artifact.Dest.Replace("\", "/")

        $manifestLines += "$($artifact.Role)  $rel"
        $manifestLines += "SIZE     $($file.Length)"
        $manifestLines += "SHA256   $hash"
        $manifestLines += ""
    }

    $snapshotDest = Join-Path $packageDir ("snapshot\" + $snapshot.Name)
    $snapshotHash = (Get-FileHash -Algorithm SHA256 $snapshotDest).Hash
    $snapshotSize = (Get-Item $snapshotDest).Length

    $manifestLines += "SNAPSHOT  snapshot/$($snapshot.Name)"
    $manifestLines += "SIZE      $snapshotSize"
    $manifestLines += "SHA256    $snapshotHash"
    $manifestLines += ""
    $manifestLines += "SCOPE  internal formal/numerical evidence; no external physical validation asserted"

    Write-Utf8NoBom `
        -Path (Join-Path $packageDir "MANIFEST_PUBLICATION.txt") `
        -Lines $manifestLines

    $filesToHash = Get-ChildItem $packageDir -Recurse -File |
        Where-Object { $_.Name -ne "SHA256SUMS.txt" } |
        Sort-Object FullName

    $sumLines = @()

    foreach ($file in $filesToHash) {
        $hash = (Get-FileHash -Algorithm SHA256 $file.FullName).Hash
        $relative = $file.FullName.Substring($packageDir.Length + 1).Replace("\", "/")
        $sumLines += "$hash  $relative"
    }

    Write-Utf8NoBom `
        -Path (Join-Path $packageDir "SHA256SUMS.txt") `
        -Lines $sumLines

    $zipPath = Join-Path $ReleaseRoot ($packageName + ".zip")

    Compress-Archive `
        -Path (Join-Path $packageDir "*") `
        -DestinationPath $zipPath `
        -Force

    if (-not (Test-Path $zipPath)) {
        throw "No se creó el ZIP final."
    }

    $zipHash = (Get-FileHash -Algorithm SHA256 $zipPath).Hash
    $zipMeta = $zipPath + ".sha256.txt"

    $zipMetaLines = @(
        "SHA256  $zipHash  $(Split-Path $zipPath -Leaf)",
        "VERSION $Version",
        "HEAD    $head",
        "BRANCH  $branch",
        "CREATED $created"
    )

    Write-Utf8NoBom -Path $zipMeta -Lines $zipMetaLines

    $statusAfter = @(git status --porcelain)

    if ($statusAfter.Count -gt 0) {
        git status --short
        throw "El empaquetado alteró el árbol Git."
    }

    Write-Host ""
    Write-Host "OK RELEASE PACKAGE"
    Write-Host "DIR:     $packageDir"
    Write-Host "ZIP:     $zipPath"
    Write-Host "SHA256:  $zipHash"
    Write-Host "META:    $zipMeta"
    Write-Host "VERSION: $Version"
    Write-Host "HEAD:    $head"
}
finally {
    Pop-Location
}
