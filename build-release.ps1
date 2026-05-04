# Builds a clean ForgeBoard release ZIP for phpBB submission.
# Run from styles/ForgeBoard/:  powershell -File build-release.ps1
#
# Output: ForgeBoard-X.Y.Z.zip in the parent directory.

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot
$cfg = Get-Content (Join-Path $root "style.cfg") -Raw
$version = ([regex]::Match($cfg, 'style_version\s*=\s*([\d.]+)')).Groups[1].Value
if (-not $version) { $version = "0.0.0" }

$zipName = "ForgeBoard-$version.zip"
$staging = Join-Path $env:TEMP "forgeboard-release-$version"
$dest    = Join-Path $staging "ForgeBoard"

if (Test-Path $staging) { Remove-Item $staging -Recurse -Force }
New-Item -ItemType Directory -Force -Path $dest | Out-Null

# Files / folders to include in the release ZIP (relative to repo root)
$include = @(
    "style.cfg",
    "LICENSE",
    "README.md",
    "CHANGELOG.md",
    "template",
    "theme"
)

# Patterns to EXCLUDE inside copied folders (dev tooling)
$excludePatterns = @(
    "*.bak", "*.bak2", "*.bak3",
    "_generate_*.py", "_dedup.py", "_specificity_pass.py",
    "Thumbs.db", ".DS_Store"
)

foreach ($item in $include) {
    $src = Join-Path $root $item
    if (-not (Test-Path $src)) { continue }
    $target = Join-Path $dest $item
    if (Test-Path $src -PathType Container) {
        Copy-Item $src $target -Recurse -Force
    } else {
        Copy-Item $src $target -Force
    }
}

# Strip dev tooling from copied tree
foreach ($pattern in $excludePatterns) {
    Get-ChildItem $dest -Recurse -File -Filter $pattern -ErrorAction SilentlyContinue |
        Remove-Item -Force
}

# Build the ZIP at the project parent (styles/ForgeBoard/..)
$zipPath = Join-Path $root $zipName
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }
Compress-Archive -Path (Join-Path $staging "ForgeBoard") -DestinationPath $zipPath -Force

# Cleanup staging
Remove-Item $staging -Recurse -Force

$size = (Get-Item $zipPath).Length
Write-Host "Built: $zipPath" -ForegroundColor Green
Write-Host ("Size:  {0:N0} bytes ({1:N1} KB)" -f $size, ($size / 1KB))
