"""
Builds ForgeBoard-Smileys-{version}.zip — a standalone smiley pack
for phpBB.com Customisations Database (category: Smiley packs).

The pack ships:
  - smilies/*.svg (24 SVG, official phpBB names)
  - INSTALL.md (clear instructions)
  - migrate.sql (SQL to switch DB references from .gif to .svg)

Usage:  python contribution/package_smileys.py
"""
import os, zipfile, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.join(ROOT, 'theme', 'images', 'smilies')
OUT = os.path.join(ROOT, 'ForgeBoard-Smileys-1.0.zip')
VERSION = '1.0'

# Read SVG files
svg_files = sorted(f for f in os.listdir(SRC_DIR)
                   if f.endswith('.svg') and not f.startswith('_'))

INSTALL_MD = """# ForgeBoard Smileys — Installation

A clean SVG smiley set for phpBB 3.3.x — 24 smileys with the official
phpBB names. Replaces the default GIF smileys that ship with phpBB.

## Why install?

- Crisp at every zoom level (SVG, no pixelation on retina screens).
- Single visual style (rounded yellow face, clean expressions).
- Lightweight: each SVG is ~600 bytes vs the GIFs at 2-3 KB.
- Adapts to any future style change (no hardcoded colors clashing).

## Requirements

- phpBB 3.3.x (any style)
- ACP access (admin rights)

## Installation (3 steps)

### 1. Copy the SVG files

Copy every file from this pack's `smilies/` directory into your phpBB:

    phpbb-root/images/smilies/

You should now have, side by side, both `icon_e_smile.gif` (original) and
`icon_e_smile.svg` (this pack), and so on for the 24 smileys.

The pack does NOT delete the original GIFs — keep them as fallback or
remove later once you confirm the SVGs render correctly.

### 2. Update the database

phpBB stores each smiley URL in the `phpbb_smilies` table. Run the SQL
in `migrate.sql` (via phpMyAdmin, or any MySQL client):

    UPDATE phpbb_smilies
    SET smiley_url = REPLACE(smiley_url, '.gif', '.svg')
    WHERE smiley_url LIKE '%.gif';

If your phpBB tables use a custom prefix (not `phpbb_`), edit `migrate.sql`
to match.

### 3. Purge the phpBB cache

ACP -> General -> Server load -> Purge the cache.

## Reverting

If you want to go back to the original GIFs:

    UPDATE phpbb_smilies
    SET smiley_url = REPLACE(smiley_url, '.svg', '.gif');

Then purge the cache again.

## License

GPL-2.0-or-later, same as ForgeBoard.

(c) 2026 FanFanLaTuFlippe
"""

MIGRATE_SQL = """-- ForgeBoard Smileys: switch all phpBB smiley references from .gif to .svg.
-- Run this AFTER copying the .svg files into phpbb/images/smilies/.
--
-- If your tables use a custom prefix (not "phpbb_"), edit the table name.

UPDATE phpbb_smilies
SET smiley_url = REPLACE(smiley_url, '.gif', '.svg')
WHERE smiley_url LIKE '%.gif';
"""


print(f'Building {os.path.basename(OUT)}...')
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    # Smileys
    for f in svg_files:
        zf.write(os.path.join(SRC_DIR, f), f'ForgeBoard-Smileys/smilies/{f}')
    # Documentation
    zf.writestr('ForgeBoard-Smileys/INSTALL.md', INSTALL_MD)
    zf.writestr('ForgeBoard-Smileys/migrate.sql', MIGRATE_SQL)

size = os.path.getsize(OUT)
print(f'Done: {len(svg_files)} smileys + INSTALL.md + migrate.sql')
print(f'Size: {size/1024:.1f} KB')
print(f'Path: {OUT}')
