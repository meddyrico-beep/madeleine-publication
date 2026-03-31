param(
    [Parameter(Mandatory=$true)][string]$Source,
    [ValidateSet("base_axiomatica","tomo1","tomo2","tomo3","unknown")]
    [string]$Target = "unknown"
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

if (-not (Test-Path $Source)) {
    throw "No existe: $Source"
}

$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$base = Split-Path $Source -Leaf
$dst = Join-Path $RepoRoot ("migration\candidates\" + $ts + "__" + $base)
New-Item -ItemType Directory -Force -Path $dst | Out-Null
Copy-Item $Source (Join-Path $dst $base) -Recurse -Force

@"
ImportedAt: $(Get-Date -Format s)
Source: $Source
Target: $Target
Decision: pending
"@ | Set-Content -Path (Join-Path $dst "META.txt") -Encoding utf8

Write-Host "OK CANDIDATE: $dst"
