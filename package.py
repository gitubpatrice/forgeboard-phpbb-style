"""
Builds the phpBB.com submission ZIP for ForgeBoard.

Includes ONLY:
  - style.cfg
  - LICENSE
  - template/  (templates + included JS files)
  - theme/     (stylesheets + images + smilies + icons)

Excludes everything else (dev tooling, docs, generators, backups, etc.)

Usage:  python package.py
Output: ForgeBoard-<version>.zip in the repo root.
"""
import os
import re
import zipfile
import fnmatch

ROOT = os.path.dirname(os.path.abspath(__file__))

# Read version from style.cfg
with open(os.path.join(ROOT, 'style.cfg'), 'r', encoding='utf-8') as f:
    cfg = f.read()
m = re.search(r'style_version\s*=\s*([\d.]+)', cfg)
version = m.group(1) if m else 'dev'

OUT_NAME = f'ForgeBoard-{version}.zip'
OUT_PATH = os.path.join(ROOT, OUT_NAME)

# What to INCLUDE — exact files at root + entire dirs
INCLUDE_FILES = {'style.cfg', 'LICENSE'}
INCLUDE_DIRS = {'template', 'theme'}

# What to EXCLUDE inside included dirs (dev tooling, generators, backups)
EXCLUDE_PATTERNS = [
    '*.bak', '*.bak2', '*.bak3',
    '*.old', '*.orig', '*~',
    '.DS_Store', 'Thumbs.db',
    '_generate_*.py',     # icon/smiley generators
    '_inventory_*.py',    # inventory scripts
    '_dedup.py',
    '_orphan_audit.py',
    '_audit.csv',
]


def is_excluded(rel_path):
    """Check if a file should be excluded from the ZIP."""
    name = os.path.basename(rel_path)
    for pat in EXCLUDE_PATTERNS:
        if fnmatch.fnmatch(name, pat):
            return True
    return False


def add_file(zf, abs_path, archive_path):
    """Add a single file to the ZIP at the given archive path."""
    if is_excluded(archive_path):
        return False
    zf.write(abs_path, archive_path)
    return True


def add_dir(zf, dir_name):
    """Walk a directory and add all non-excluded files."""
    src = os.path.join(ROOT, dir_name)
    count = 0
    for root, _, files in os.walk(src):
        for f in files:
            abs_path = os.path.join(root, f)
            rel = os.path.relpath(abs_path, ROOT).replace('\\', '/')
            if add_file(zf, abs_path, f'ForgeBoard/{rel}'):
                count += 1
    return count


print(f'Building {OUT_NAME}...')
with zipfile.ZipFile(OUT_PATH, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    total = 0
    # Root-level files
    for f in INCLUDE_FILES:
        path = os.path.join(ROOT, f)
        if os.path.isfile(path):
            zf.write(path, f'ForgeBoard/{f}')
            total += 1
            print(f'  + ForgeBoard/{f}')
    # Directories
    for d in INCLUDE_DIRS:
        n = add_dir(zf, d)
        total += n
        print(f'  + ForgeBoard/{d}/  ({n} files)')

size = os.path.getsize(OUT_PATH)
print(f'\nDone: {OUT_NAME}  ({total} files, {size/1024:.1f} KB)')
print(f'Location: {OUT_PATH}')
