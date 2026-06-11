# Builds a clean ForgeBoard release ZIP for phpBB.com validation.
# Run from styles/ForgeBoard/:  powershell -File build-release.ps1
#
# Output: ForgeBoard-X.Y.Z.zip in this folder.
#
# Notes:
#   - Uses Python's zipfile module so entries use FORWARD slashes
#     (PowerShell's Compress-Archive uses backslashes which phpBB.com
#     validation flags as non-standard).
#   - Strips all dev tooling (_*.py, _*.csv, .bak, IDE files, etc.).

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
# phpBB.com validation only expects: style.cfg, license.txt, template/, theme/
$include = @(
    "style.cfg",
    "template",
    "theme"
)

# Filename patterns to EXCLUDE inside copied folders (dev tooling, IDE files)
$excludePatterns = @(
    "*.bak", "*.bak2", "*.bak3",
    "_*.py", "_*.csv",
    "*.psd",
    "Thumbs.db", ".DS_Store",
    "package.json", "package-lock.json", ".stylelintrc.json", ".stylelintignore"
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

# Add license.txt (phpBB convention is lowercase .txt). Accept common variants.
$licenseSrc = @("license.txt", "licence.txt", "LICENSE", "licence") |
    ForEach-Object { Join-Path $root $_ } | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($licenseSrc) {
    Copy-Item $licenseSrc (Join-Path $dest "license.txt") -Force
}

# Strip dev tooling from copied tree
foreach ($pattern in $excludePatterns) {
    Get-ChildItem $dest -Recurse -File -Filter $pattern -ErrorAction SilentlyContinue |
        Remove-Item -Force
}

# Build the ZIP using Python for forward-slash compliance.
$zipPath = Join-Path $root $zipName
if (Test-Path $zipPath) { Remove-Item $zipPath -Force }

$pyScript = @"
import os, sys, zipfile
src = r'$staging'
dest = r'$zipPath'
with zipfile.ZipFile(dest, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for root, dirs, files in os.walk(src):
        # Stable order
        dirs.sort(); files.sort()
        for name in files:
            full = os.path.join(root, name)
            rel = os.path.relpath(full, src).replace('\\', '/')
            zf.write(full, rel)
"@

$tmpPy = Join-Path $env:TEMP "forgeboard-zip-$version.py"
$pyScript | Out-File -FilePath $tmpPy -Encoding ASCII
python $tmpPy
Remove-Item $tmpPy -Force

# Cleanup staging
Remove-Item $staging -Recurse -Force

$size = (Get-Item $zipPath).Length
Write-Host "Built: $zipPath" -ForegroundColor Green
Write-Host ("Size:  {0:N0} bytes ({1:N1} KB)" -f $size, ($size / 1KB))
