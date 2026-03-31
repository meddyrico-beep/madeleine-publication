$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$OutDir = Join-Path $RepoRoot "artifacts\snapshots"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

$ts = Get-Date -Format "yyyyMMdd_HHmmss"
$zip = Join-Path $OutDir ("snapshot_" + $ts + ".zip")
$tmp = Join-Path $env:TEMP ("madeleine_publication_" + $ts)

New-Item -ItemType Directory -Force -Path $tmp | Out-Null
Copy-Item (Join-Path $RepoRoot "manuscript") (Join-Path $tmp "manuscript") -Recurse -Force
Copy-Item (Join-Path $RepoRoot "tools") (Join-Path $tmp "tools") -Recurse -Force
Copy-Item (Join-Path $RepoRoot "README.md") (Join-Path $tmp "README.md") -Force
Copy-Item (Join-Path $RepoRoot "MANIFESTO.md") (Join-Path $tmp "MANIFESTO.md") -Force
Copy-Item (Join-Path $RepoRoot "ADMISSION_RULES.md") (Join-Path $tmp "ADMISSION_RULES.md") -Force

Compress-Archive -Path (Join-Path $tmp "*") -DestinationPath $zip -Force
$hash = Get-FileHash -Algorithm SHA256 $zip
$hashLine = "SHA256  $($hash.Hash)  $(Split-Path $zip -Leaf)"
$hashLine | Set-Content -Path ($zip + ".sha256.txt") -Encoding utf8

Remove-Item $tmp -Recurse -Force
Write-Host "OK SNAPSHOT: $zip"
