param(
    [Parameter(Mandatory=$true)][string]$CandidateDir,
    [ValidateSet("accepted","deferred","rejected")]
    [string]$Decision,
    [string]$Reason = "",
    [string]$TargetPiece = "",
    [string]$TargetSubpath = ""
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

if (-not (Test-Path $CandidateDir)) {
    throw "No existe CandidateDir: $CandidateDir"
}

$leaf = Split-Path $CandidateDir -Leaf
$dstRoot = Join-Path $RepoRoot ("migration\" + $Decision)
$dst = Join-Path $dstRoot $leaf

New-Item -ItemType Directory -Force -Path $dstRoot | Out-Null
if (Test-Path $dst) {
    throw "Ya existe destino: $dst"
}

Move-Item $CandidateDir $dst

$meta = Join-Path $dst "META.txt"
if (-not (Test-Path $meta)) {
    "ImportedAt: unknown`nDecision: pending" | Set-Content -Path $meta -Encoding utf8
}

Add-Content -Path $meta -Value ""
Add-Content -Path $meta -Value ("AdmittedAt: " + (Get-Date -Format s))
Add-Content -Path $meta -Value ("Decision: " + $Decision)
Add-Content -Path $meta -Value ("Reason: " + $Reason)

if ($Decision -eq "accepted" -and $TargetPiece -and $TargetSubpath) {
    $payload = Get-ChildItem -Path $dst -File | Where-Object { $_.Name -ne "META.txt" } | Select-Object -First 1
    if (-not $payload) {
        throw "No encontré archivo payload en $dst"
    }

    $targetDir = Join-Path $RepoRoot ("manuscript\" + $TargetPiece + "\" + $TargetSubpath)
    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
    }

    $targetFile = Join-Path $targetDir $payload.Name
    Copy-Item $payload.FullName $targetFile -Force

    Add-Content -Path $meta -Value ("InjectedTo: " + $targetFile)
    Write-Host "OK ACCEPTED + INJECTED: $targetFile"
}
else {
    Write-Host "OK DECISION: $Decision -> $dst"
}