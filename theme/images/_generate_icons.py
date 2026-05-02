"""
Generates all 41 phpBB imageset icons as SVG (27x27 to match Prosilver).
Monochrome-by-default (uses currentColor). Each icon = 1 base shape +
optional state badges (locked, mine, hot, sublink).

Run from theme/images/:
    python _generate_icons.py
"""
import os

OUTDIR = os.path.dirname(os.path.abspath(__file__)) or '.'
SIZE = 27

# Color tokens — each icon uses currentColor so the parent element's
# color drives it. Status colors are baked in for clarity.
RED = '#c83e4d'        # unread / danger
BLUE = '#1f6feb'       # info / link
MUTED = '#8a96a3'      # read / muted
ORANGE = '#f97316'     # hot
GREEN = '#1f883d'      # mine indicator
YELLOW = '#eab308'     # sticky color


def svg(content, viewbox=f'0 0 {SIZE} {SIZE}'):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" '
        f'width="{SIZE}" height="{SIZE}" fill="none" '
        f'stroke="currentColor" stroke-width="1.6" '
        f'stroke-linecap="round" stroke-linejoin="round">\n'
        f'{content}\n'
        f'</svg>'
    )


def folder_open(color):
    return f'''<path d="M3 8 L3 21 Q3 22 4 22 L23 22 L25 12 L7 12 L6 9 L4 9 Q3 9 3 8 Z" fill="{color}" fill-opacity="0.18" stroke="{color}"/>
  <path d="M3 8 L3 6 Q3 5 4 5 L11 5 L13 7 L23 7 Q24 7 24 8 L24 11" stroke="{color}"/>'''


def folder_closed(color):
    return f'''<path d="M3 8 Q3 7 4 7 L11 7 L13 9 L23 9 Q24 9 24 10 L24 21 Q24 22 23 22 L4 22 Q3 22 3 21 Z" fill="{color}" fill-opacity="0.18" stroke="{color}"/>'''


def file_filled(color):
    return f'''<path d="M7 4 L17 4 L22 9 L22 23 Q22 24 21 24 L7 24 Q6 24 6 23 L6 5 Q6 4 7 4 Z" fill="{color}" fill-opacity="0.22" stroke="{color}"/>
  <path d="M17 4 L17 9 L22 9" stroke="{color}"/>'''


def file_outline(color):
    return f'''<path d="M7 4 L17 4 L22 9 L22 23 Q22 24 21 24 L7 24 Q6 24 6 23 L6 5 Q6 4 7 4 Z" stroke="{color}"/>
  <path d="M17 4 L17 9 L22 9" stroke="{color}"/>'''


def lock_badge():
    """Small padlock badge in the bottom-right corner."""
    return '''<g stroke-width="1.3" transform="translate(15 14)">
    <rect x="1" y="5" width="9" height="6" rx="1.2" fill="#0d1117" stroke="currentColor"/>
    <path d="M3 5 L3 3 Q3 1 5.5 1 Q8 1 8 3 L8 5" stroke="currentColor" fill="none"/>
  </g>'''


def mine_badge():
    """Green dot bottom-right indicating 'I have posted in this'."""
    return f'''<circle cx="22" cy="22" r="3.2" fill="{GREEN}" stroke="#0d1117" stroke-width="1"/>'''


def hot_badge():
    """Flame on top of the icon for hot topics."""
    return f'''<path d="M19 4 Q22 7 21 10 Q24 9 24 12 Q24 15 21 16 Q22 13 20 12 Q21 10 19 9 Q18 6 19 4 Z" fill="{ORANGE}" stroke="{ORANGE}" stroke-width="1"/>'''


def sublink_badge(color):
    """Small forum-link arrow for subforums."""
    return f'''<path d="M18 16 L23 16 L23 21" stroke="{color}" stroke-width="1.4"/>
  <path d="M14 21 L23 16" stroke="{color}" stroke-width="1.4"/>'''


def push_pin(color, fill_alpha=0.22):
    return f'''<path d="M14 2 L20 8 L17 11 L21 15 L15 21 L11 17 L8 20 L7 19 L10 16 L6 12 L9 9 Z" fill="{color}" fill-opacity="{fill_alpha}" stroke="{color}"/>
  <path d="M9 9 L17 17" stroke="{color}"/>'''


def megaphone(color, fill_alpha=0.22):
    return f'''<path d="M5 12 L5 18 Q5 19 6 19 L9 19 L9 11 L6 11 Q5 11 5 12 Z" fill="{color}" fill-opacity="{fill_alpha}" stroke="{color}"/>
  <path d="M9 11 L20 5 L20 25 L9 19 Z" fill="{color}" fill-opacity="{fill_alpha}" stroke="{color}"/>
  <path d="M11 19 L13 24" stroke="{color}"/>'''


def link_arrow(color):
    return f'''<path d="M3 8 L3 6 Q3 5 4 5 L11 5 L13 7 L23 7 Q24 7 24 8 L24 21 Q24 22 23 22 L4 22 Q3 22 3 21 Z" fill="{color}" fill-opacity="0.15" stroke="{color}"/>
  <path d="M14 13 L21 13 L21 20" stroke="{color}" stroke-width="1.6"/>
  <path d="M11 20 L21 13" stroke="{color}" stroke-width="1.6"/>'''


def moved_arrow(color):
    return f'''<path d="M7 4 L17 4 L22 9 L22 23 Q22 24 21 24 L7 24 Q6 24 6 23 L6 5 Q6 4 7 4 Z" fill="{color}" fill-opacity="0.15" stroke="{color}"/>
  <path d="M17 4 L17 9 L22 9" stroke="{color}"/>
  <path d="M9 14 L19 14" stroke="{color}" stroke-width="1.8"/>
  <path d="M16 11 L19 14 L16 17" stroke="{color}" stroke-width="1.8"/>'''


# === Build map of files to generate ===
icons = {
    # --- FORUMS ---
    'forum_read.gif':              folder_closed(MUTED),
    'forum_read_locked.gif':       folder_closed(MUTED) + '\n  ' + lock_badge(),
    'forum_read_subforum.gif':     folder_closed(MUTED) + '\n  ' + sublink_badge(MUTED),
    'forum_unread.gif':            folder_open(RED),
    'forum_unread_locked.gif':     folder_open(RED) + '\n  ' + lock_badge(),
    'forum_unread_subforum.gif':   folder_open(RED) + '\n  ' + sublink_badge(RED),
    'forum_link.gif':              link_arrow(BLUE),

    # --- TOPICS ---
    'topic_read.gif':              file_outline(MUTED),
    'topic_read_mine.gif':         file_outline(MUTED) + '\n  ' + mine_badge(),
    'topic_read_locked.gif':       file_outline(MUTED) + '\n  ' + lock_badge(),
    'topic_read_locked_mine.gif':  file_outline(MUTED) + '\n  ' + lock_badge() + '\n  ' + mine_badge(),
    'topic_read_hot.gif':          file_outline(MUTED) + '\n  ' + hot_badge(),
    'topic_read_hot_mine.gif':     file_outline(MUTED) + '\n  ' + hot_badge() + '\n  ' + mine_badge(),
    'topic_unread.gif':            file_filled(RED),
    'topic_unread_mine.gif':       file_filled(RED) + '\n  ' + mine_badge(),
    'topic_unread_locked.gif':     file_filled(RED) + '\n  ' + lock_badge(),
    'topic_unread_locked_mine.gif': file_filled(RED) + '\n  ' + lock_badge() + '\n  ' + mine_badge(),
    'topic_unread_hot.gif':        file_filled(RED) + '\n  ' + hot_badge(),
    'topic_unread_hot_mine.gif':   file_filled(RED) + '\n  ' + hot_badge() + '\n  ' + mine_badge(),
    'topic_moved.gif':             moved_arrow(MUTED),

    # --- STICKY ---
    'sticky_read.gif':                push_pin(MUTED),
    'sticky_read_mine.gif':           push_pin(MUTED) + '\n  ' + mine_badge(),
    'sticky_read_locked.gif':         push_pin(MUTED) + '\n  ' + lock_badge(),
    'sticky_read_locked_mine.gif':    push_pin(MUTED) + '\n  ' + lock_badge() + '\n  ' + mine_badge(),
    'sticky_unread.gif':              push_pin(BLUE),
    'sticky_unread_mine.gif':         push_pin(BLUE) + '\n  ' + mine_badge(),
    'sticky_unread_locked.gif':       push_pin(BLUE) + '\n  ' + lock_badge(),
    'sticky_unread_locked_mine.gif':  push_pin(BLUE) + '\n  ' + lock_badge() + '\n  ' + mine_badge(),

    # --- ANNOUNCE ---
    'announce_read.gif':              megaphone(MUTED),
    'announce_read_mine.gif':         megaphone(MUTED) + '\n  ' + mine_badge(),
    'announce_read_locked.gif':       megaphone(MUTED) + '\n  ' + lock_badge(),
    'announce_read_locked_mine.gif':  megaphone(MUTED) + '\n  ' + lock_badge() + '\n  ' + mine_badge(),
    'announce_unread.gif':            megaphone(RED),
    'announce_unread_mine.gif':       megaphone(RED) + '\n  ' + mine_badge(),
    'announce_unread_locked.gif':     megaphone(RED) + '\n  ' + lock_badge(),
    'announce_unread_locked_mine.gif': megaphone(RED) + '\n  ' + lock_badge() + '\n  ' + mine_badge(),
}


# --- Misc utility icons ---
no_avatar = svg('''<rect x="2" y="2" width="23" height="23" rx="4" fill="#21262d" stroke="#30363d"/>
  <circle cx="13.5" cy="11" r="4.5" fill="#8a96a3"/>
  <path d="M5 23 Q5 17 13.5 17 Q22 17 22 23" fill="#8a96a3"/>''')

loading = svg('''<circle cx="13.5" cy="13.5" r="9" stroke="#30363d" stroke-width="2.5" fill="none"/>
  <path d="M13.5 4.5 A9 9 0 0 1 22.5 13.5" stroke="#1f6feb" stroke-width="2.5" fill="none">
    <animateTransform attributeName="transform" type="rotate" from="0 13.5 13.5" to="360 13.5 13.5" dur="0.9s" repeatCount="indefinite"/>
  </path>''')

# Site logo (SD badge) — bigger viewbox for decent rendering
site_logo = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" '
    'width="64" height="64">\n'
    '  <rect x="2" y="2" width="60" height="60" rx="14" fill="url(#g)" stroke="#cbd5df"/>\n'
    '  <defs>\n'
    '    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">\n'
    '      <stop offset="0%" stop-color="#ffffff"/>\n'
    '      <stop offset="100%" stop-color="#dbeafe"/>\n'
    '    </linearGradient>\n'
    '  </defs>\n'
    '  <text x="32" y="42" text-anchor="middle" '
    'font-family="-apple-system, BlinkMacSystemFont, Segoe UI, sans-serif" '
    'font-weight="900" font-size="26" fill="#0d1117" letter-spacing="-1">SD</text>\n'
    '</svg>'
)


# Write all files
written = 0
# Write SVGs as .svg AND keep .gif extension as a simple SVG file inside
# (phpBB serves them as binary blobs; modern browsers display SVG inside
#  any extension if the Content-Type is right. To stay 100% safe we ALSO
#  write the .svg variant, and let users prefer either via an imageset.)
for name, content in icons.items():
    base = name.rsplit('.', 1)[0]
    # Write .svg version (recommended)
    svg_path = os.path.join(OUTDIR, base + '.svg')
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg(content))
    written += 1

# Misc files
with open(os.path.join(OUTDIR, 'no_avatar.svg'), 'w', encoding='utf-8') as f:
    f.write(no_avatar)
written += 1

with open(os.path.join(OUTDIR, 'loading.svg'), 'w', encoding='utf-8') as f:
    f.write(loading)
written += 1

with open(os.path.join(OUTDIR, 'site_logo.svg'), 'w', encoding='utf-8') as f:
    f.write(site_logo)
written += 1

print(f"Wrote {written} SVG files to {OUTDIR}")
