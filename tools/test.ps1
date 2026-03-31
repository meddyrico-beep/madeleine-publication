$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$files = Get-ChildItem -Path (Join-Path $RepoRoot "manuscript") -Recurse -File -Include *.tex

$errors = @()

foreach ($f in $files) {
    $raw = Get-Content $f.FullName -Raw
    if ($raw -match 'â€|â€™|â€œ|â€�|Ã|�|ç|ün') {
        $errors += "Mojibake: $($f.FullName)"
    }
    if ($raw -match 'TODO|FIXME|PLACEHOLDER|Insertar/pegar aquí|PENDIENTE') {
        $errors += "Placeholder: $($f.FullName)"
    }
}

if ($errors.Count -gt 0) {
    $errors | ForEach-Object { Write-Host $_ }
    exit 1
}

Write-Host "OK: sin errores bloqueantes."
