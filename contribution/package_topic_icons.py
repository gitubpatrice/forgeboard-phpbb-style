"""
Builds ForgeBoard-TopicIcons-{version}.zip — a standalone topic-icon pack
for phpBB.com Customisations Database (category: Topic icons).

The pack ships:
  - icons/misc/*.svg  (5 SVG: fire, heart, radioactive, star, thinking)
  - icons/smile/*.svg (5 SVG: alert, info, mrgreen, question, redface)
  - INSTALL.md (clear instructions)
  - migrate.sql (SQL to switch DB references from .gif to .svg)

Usage:  python contribution/package_topic_icons.py
"""
import os, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_MISC  = os.path.join(ROOT, 'theme', 'images', 'icons', 'misc')
SRC_SMILE = os.path.join(ROOT, 'theme', 'images', 'icons', 'smile')
OUT = os.path.join(ROOT, 'ForgeBoard-TopicIcons-1.0.zip')
VERSION = '1.0'

misc_files  = sorted(f for f in os.listdir(SRC_MISC)  if f.endswith('.svg'))
smile_files = sorted(f for f in os.listdir(SRC_SMILE) if f.endswith('.svg'))

INSTALL_MD = """# ForgeBoard Topic Icons — Installation

A clean SVG topic-icon set for phpBB 3.3.x — 10 topic icons grouped in two
sub-packs (`misc/` and `smile/`). Replaces the default GIF icons that ship
with phpBB.

## Why install?

- Crisp at every zoom level (SVG, no pixelation on retina screens).
- Single visual style, theme-friendly.
- Lightweight: each SVG is ~600 bytes vs the GIFs at 2-3 KB.

## Requirements

- phpBB 3.3.x (any style)
- ACP access (admin rights)

## Installation (3 steps)

### 1. Copy the SVG files

Copy every file from this pack into your phpBB installation:

    pack/icons/misc/*.svg   ->   phpbb-root/images/icons/misc/
    pack/icons/smile/*.svg  ->   phpbb-root/images/icons/smile/

The pack does NOT delete the original GIFs — keep them as fallback or
remove them later once you confirm the SVGs render correctly.

### 2. Update the database

phpBB stores each topic-icon URL in the `phpbb_icons` table. Run the SQL
in `migrate.sql` (via phpMyAdmin, or any MySQL client):

    UPDATE phpbb_icons
    SET icons_url = REPLACE(icons_url, '.gif', '.svg')
    WHERE icons_url LIKE '%.gif';

If your phpBB tables use a custom prefix (not `phpbb_`), edit `migrate.sql`
to match.

### 3. Purge the phpBB cache

ACP -> General -> Server load -> Purge the cache.

## Reverting

If you want to go back to the original GIFs:

    UPDATE phpbb_icons
    SET icons_url = REPLACE(icons_url, '.svg', '.gif');

Then purge the cache again.

## License

GPL-2.0-or-later, same as ForgeBoard.

(c) 2026 FanFanLaTuFlippe
"""

MIGRATE_SQL = """-- ForgeBoard Topic Icons: switch all phpBB topic-icon references from .gif to .svg.
-- Run this AFTER copying the .svg files into phpbb/images/icons/misc/ and phpbb/images/icons/smile/.
--
-- If your tables use a custom prefix (not "phpbb_"), edit the table name.

UPDATE phpbb_icons
SET icons_url = REPLACE(icons_url, '.gif', '.svg')
WHERE icons_url LIKE '%.gif';
"""


print(f'Building {os.path.basename(OUT)}...')
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
    for f in misc_files:
        zf.write(os.path.join(SRC_MISC, f), f'ForgeBoard-TopicIcons/icons/misc/{f}')
    for f in smile_files:
        zf.write(os.path.join(SRC_SMILE, f), f'ForgeBoard-TopicIcons/icons/smile/{f}')
    zf.writestr('ForgeBoard-TopicIcons/INSTALL.md', INSTALL_MD)
    zf.writestr('ForgeBoard-TopicIcons/migrate.sql', MIGRATE_SQL)

size = os.path.getsize(OUT)
total = len(misc_files) + len(smile_files)
print(f'Done: {total} icons ({len(misc_files)} misc + {len(smile_files)} smile) + INSTALL.md + migrate.sql')
print(f'Size: {size/1024:.1f} KB')
print(f'Path: {OUT}')
