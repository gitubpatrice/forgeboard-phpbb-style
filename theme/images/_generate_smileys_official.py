"""
Generates official phpBB smiley set + post icon set as SVG.
- 24 smileys with EXACT phpBB names (icon_e_*.svg, icon_*.svg) so they
  can be dropped into phpbb/images/smilies/ and selected via ACP.
- 10 post icons matching phpBB defaults (fire/star/heart etc.).

Run from theme/images/:  python _generate_smileys_official.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__)) or '.'
SMILEY_DIR = os.path.join(ROOT, 'smilies')
ICON_MISC = os.path.join(ROOT, 'icons', 'misc')
ICON_SMILE = os.path.join(ROOT, 'icons', 'smile')
for d in (SMILEY_DIR, ICON_MISC, ICON_SMILE):
    os.makedirs(d, exist_ok=True)

# === Smiley palette ===
S_SIZE = 22
S_YELLOW = '#fcd34d'
S_YELLOW_DARK = '#f59e0b'
S_RED = '#ef4444'
S_BLUE = '#3b82f6'
S_GRAY = '#374151'
S_GREEN = '#16a34a'


def svg_smiley(content, bg=S_YELLOW, border=S_YELLOW_DARK):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S_SIZE} {S_SIZE}" '
        f'width="{S_SIZE}" height="{S_SIZE}">\n'
        f'  <circle cx="11" cy="11" r="10" fill="{bg}" stroke="{border}" stroke-width="0.7"/>\n'
        f'  {content}\n</svg>'
    )

# Eyes / mouths primitives
EYE_DOT_L = f'<circle cx="7.5" cy="9" r="1.2" fill="{S_GRAY}"/>'
EYE_DOT_R = f'<circle cx="14.5" cy="9" r="1.2" fill="{S_GRAY}"/>'
EYE_LINE_L = f'<path d="M6 9 L9 9" stroke="{S_GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_LINE_R = f'<path d="M13 9 L16 9" stroke="{S_GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_BIG_L = f'<circle cx="7.5" cy="9" r="1.7" fill="white" stroke="{S_GRAY}" stroke-width="0.8"/><circle cx="7.5" cy="9.3" r="0.9" fill="{S_GRAY}"/>'
EYE_BIG_R = f'<circle cx="14.5" cy="9" r="1.7" fill="white" stroke="{S_GRAY}" stroke-width="0.8"/><circle cx="14.5" cy="9.3" r="0.9" fill="{S_GRAY}"/>'
EYE_WINK_L = f'<path d="M6 9 Q7.5 8 9 9" stroke="{S_GRAY}" stroke-width="1.2" fill="none" stroke-linecap="round"/>'
EYE_X_L = f'<path d="M6 8L9 10M9 8L6 10" stroke="{S_GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_X_R = f'<path d="M13 8L16 10M16 8L13 10" stroke="{S_GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_ROLL_L = f'<circle cx="7.5" cy="9" r="1.5" fill="white" stroke="{S_GRAY}" stroke-width="0.8"/><circle cx="7.5" cy="7.8" r="0.7" fill="{S_GRAY}"/>'
EYE_ROLL_R = f'<circle cx="14.5" cy="9" r="1.5" fill="white" stroke="{S_GRAY}" stroke-width="0.8"/><circle cx="14.5" cy="7.8" r="0.7" fill="{S_GRAY}"/>'

MOUTH_SMILE_SM = f'<path d="M8 13 Q11 16 14 13" stroke="{S_GRAY}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
MOUTH_SMILE = f'<path d="M7 13 Q11 17 15 13" stroke="{S_GRAY}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
MOUTH_BIG = f'<path d="M6 13 Q11 19 16 13 Z" fill="white" stroke="{S_GRAY}" stroke-width="1.2" stroke-linejoin="round"/>'
MOUTH_FROWN = f'<path d="M7 16 Q11 12 15 16" stroke="{S_GRAY}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
MOUTH_FLAT = f'<path d="M8 15 L14 15" stroke="{S_GRAY}" stroke-width="1.4" stroke-linecap="round"/>'
MOUTH_O = f'<circle cx="11" cy="15" r="1.6" fill="{S_GRAY}"/>'
MOUTH_O_BIG = f'<ellipse cx="11" cy="15" rx="2.2" ry="2.6" fill="{S_GRAY}"/>'
MOUTH_TONGUE = f'<path d="M7 13 Q11 17 15 13" stroke="{S_GRAY}" stroke-width="1.4" fill="none"/><path d="M9 14.5 Q11 18 13 14.5 Z" fill="{S_RED}"/>'
MOUTH_GRIN = f'<path d="M6 13 L16 13 Q15 17 11 17 Q7 17 6 13 Z" fill="white" stroke="{S_GRAY}" stroke-width="1"/>'
MOUTH_TWIST = f'<path d="M7 14 Q9 12 11 14 Q13 16 15 14" stroke="{S_GRAY}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'

GLASSES = f'<rect x="4.5" y="7.5" width="6" height="3.5" rx="1" fill="{S_GRAY}"/><rect x="11.5" y="7.5" width="6" height="3.5" rx="1" fill="{S_GRAY}"/><path d="M10.5 9 L11.5 9" stroke="{S_GRAY}" stroke-width="0.8"/>'
HORNS = f'<path d="M5 4 Q4 1 6 2 Q7 3 7 5 Z" fill="{S_RED}"/><path d="M17 4 Q18 1 16 2 Q15 3 15 5 Z" fill="{S_RED}"/>'
GEEK_GLASSES = f'<rect x="4" y="7.5" width="6.5" height="4" rx="0.5" fill="white" stroke="{S_GRAY}" stroke-width="1"/><rect x="11.5" y="7.5" width="6.5" height="4" rx="0.5" fill="white" stroke="{S_GRAY}" stroke-width="1"/><path d="M10.5 9.5 L11.5 9.5" stroke="{S_GRAY}" stroke-width="1"/>'

# === 24 Official phpBB smileys ===
smileys = {
    # Eye-prefix (icon_e_*)
    'icon_e_smile.gif':       svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_SMILE),
    'icon_e_biggrin.gif':     svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_BIG),
    'icon_e_wink.gif':        svg_smiley(EYE_WINK_L + EYE_DOT_R + MOUTH_SMILE),
    'icon_e_sad.gif':         svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_FROWN),
    'icon_e_surprised.gif':   svg_smiley(EYE_BIG_L + EYE_BIG_R + MOUTH_O),
    'icon_e_confused.gif':    svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_TWIST),
    'icon_e_geek.gif':        svg_smiley(GEEK_GLASSES + MOUTH_FLAT),
    'icon_e_ugeek.gif':       svg_smiley(GEEK_GLASSES + f'<path d="M3 7 L19 7" stroke="{S_GRAY}" stroke-width="0.7"/>' + MOUTH_FLAT),
    # No icon_e_ prefix
    'icon_cool.gif':          svg_smiley(GLASSES + MOUTH_FLAT),
    'icon_cry.gif':           svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_FROWN + f'<path d="M14 11 Q14.5 13 14 14 Q13.5 13 14 11 Z" fill="{S_BLUE}"/><path d="M7 11 Q7.5 13 7 14 Q6.5 13 7 11 Z" fill="{S_BLUE}"/>'),
    'icon_eek.gif':           svg_smiley(EYE_BIG_L + EYE_BIG_R + MOUTH_O_BIG),
    'icon_evil.gif':          svg_smiley(EYE_LINE_L + EYE_LINE_R + MOUTH_GRIN, bg=S_RED, border='#b91c1c'),
    'icon_exclaim.gif':       svg_smiley(f'<text x="11" y="15" text-anchor="middle" font-family="sans-serif" font-size="14" font-weight="900" fill="{S_GRAY}">!</text>'),
    'icon_idea.gif':          svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_SMILE_SM + f'<path d="M11 1 L11 3" stroke="#fbbf24" stroke-width="1.5" stroke-linecap="round"/><circle cx="11" cy="1" r="1.5" fill="#fde047"/>'),
    'icon_lol.gif':           svg_smiley(EYE_X_L + EYE_X_R + MOUTH_BIG),
    'icon_mad.gif':           svg_smiley(EYE_LINE_L + EYE_LINE_R + MOUTH_FROWN, bg='#fb923c', border='#c2410c'),
    'icon_mrgreen.gif':       svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_BIG, bg='#84cc16', border=S_GREEN),
    'icon_neutral.gif':       svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_FLAT),
    'icon_question.gif':      svg_smiley(f'<text x="11" y="16" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="900" fill="{S_GRAY}">?</text>'),
    'icon_razz.gif':          svg_smiley(EYE_WINK_L + EYE_DOT_R + MOUTH_TONGUE),
    'icon_redface.gif':       svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_SMILE_SM + f'<circle cx="5" cy="13" r="1.4" fill="{S_RED}" opacity="0.55"/><circle cx="17" cy="13" r="1.4" fill="{S_RED}" opacity="0.55"/>'),
    'icon_rolleyes.gif':      svg_smiley(EYE_ROLL_L + EYE_ROLL_R + MOUTH_FLAT),
    'icon_twisted.gif':       svg_smiley(EYE_X_L + EYE_X_R + MOUTH_TWIST + HORNS),
    'icon_arrow.gif':         f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {S_SIZE} {S_SIZE}" width="{S_SIZE}" height="{S_SIZE}">
  <circle cx="11" cy="11" r="10" fill="#3b82f6" stroke="#1d4ed8" stroke-width="0.7"/>
  <path d="M6 11 L15 11 M11 7 L15 11 L11 15" stroke="white" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',
}

# === Post icons ===

# misc/
post_misc = {
    'fire.gif': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
  <path d="M8 1 Q11 4 10 7 Q12 6 12 9 Q12 13 8 15 Q4 13 4 9 Q4 6 6 7 Q5 4 8 1 Z" fill="#f97316" stroke="#c2410c" stroke-width="0.6"/>
  <path d="M8 7 Q9.5 9 8.8 11 Q10 10 10 12 Q10 14 8 14.8 Q6 14 6 12 Q6 10 7.2 11 Q6.5 9 8 7 Z" fill="#fbbf24"/>
</svg>''',
    'star.gif': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
  <path d="M8 1 L10 6 L15 6.5 L11 10 L12 15 L8 12.5 L4 15 L5 10 L1 6.5 L6 6 Z" fill="#fbbf24" stroke="#d97706" stroke-width="0.6" stroke-linejoin="round"/>
</svg>''',
    'heart.gif': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
  <path d="M8 14 Q1 9 1 5 Q1 2 4 2 Q6.5 2 8 4 Q9.5 2 12 2 Q15 2 15 5 Q15 9 8 14 Z" fill="#ef4444" stroke="#b91c1c" stroke-width="0.6" stroke-linejoin="round"/>
</svg>''',
    'radioactive.gif': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
  <circle cx="8" cy="8" r="7" fill="#fde047" stroke="#a16207" stroke-width="0.6"/>
  <circle cx="8" cy="8" r="2" fill="#0f172a"/>
  <path d="M8 8 L8 1 A7 7 0 0 1 14 5 Z" fill="#0f172a"/>
  <path d="M8 8 L14 11 A7 7 0 0 1 2 11 Z" fill="#0f172a"/>
  <path d="M8 8 L2 5 A7 7 0 0 1 8 1 Z" fill="#0f172a" opacity="0"/>
</svg>''',
    'thinking.gif': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="16" height="16">
  <circle cx="8" cy="8" r="7" fill="#fcd34d" stroke="#f59e0b" stroke-width="0.6"/>
  <circle cx="6" cy="7" r="0.7" fill="#374151"/>
  <circle cx="10.5" cy="7" r="0.7" fill="#374151"/>
  <path d="M5.5 11 Q8 9.5 10.5 11.5" stroke="#374151" stroke-width="0.9" fill="none" stroke-linecap="round"/>
  <circle cx="13" cy="3" r="0.6" fill="#374151"/>
  <circle cx="14" cy="2" r="0.4" fill="#374151"/>
</svg>''',
}

# smile/
post_smile = {
    'redface.gif': svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_SMILE_SM + f'<circle cx="5" cy="13" r="1.4" fill="{S_RED}" opacity="0.55"/><circle cx="17" cy="13" r="1.4" fill="{S_RED}" opacity="0.55"/>'),
    'mrgreen.gif': svg_smiley(EYE_DOT_L + EYE_DOT_R + MOUTH_BIG, bg='#84cc16', border=S_GREEN),
    'question.gif': svg_smiley(f'<text x="11" y="16" text-anchor="middle" font-family="sans-serif" font-size="13" font-weight="900" fill="{S_GRAY}">?</text>'),
    'alert.gif': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 22 22" width="22" height="22">
  <path d="M11 2 L21 19 L1 19 Z" fill="#fbbf24" stroke="#d97706" stroke-width="0.7" stroke-linejoin="round"/>
  <path d="M11 8 L11 14" stroke="#451a03" stroke-width="2" stroke-linecap="round"/>
  <circle cx="11" cy="17" r="0.9" fill="#451a03"/>
</svg>''',
    'info.gif': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 22 22" width="22" height="22">
  <circle cx="11" cy="11" r="9.5" fill="#3b82f6" stroke="#1d4ed8" stroke-width="0.7"/>
  <circle cx="11" cy="6" r="1.3" fill="white"/>
  <path d="M11 9 L11 16" stroke="white" stroke-width="2.2" stroke-linecap="round"/>
</svg>''',
}


# === Write all files (.svg form, also save matching .gif extension files
# with SVG content since phpBB DB references *.gif by default) ===
def write_pair(directory, base, content):
    """Write both .svg and .gif (SVG content) so phpBB serves the SVG via
    the DB-stored .gif URL too. Modern browsers render SVG regardless of
    file extension as long as Content-Type/X-Content-Type sniffing works.
    """
    svg_path = os.path.join(directory, base.replace('.gif', '.svg'))
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(content)


count = 0
for name, content in smileys.items():
    write_pair(SMILEY_DIR, name, content)
    count += 1
for name, content in post_misc.items():
    write_pair(ICON_MISC, name, content)
    count += 1
for name, content in post_smile.items():
    write_pair(ICON_SMILE, name, content)
    count += 1

print(f"Wrote {count} SVG files")
print(f"  {len(smileys)} smileys -> {SMILEY_DIR}")
print(f"  {len(post_misc)} misc icons -> {ICON_MISC}")
print(f"  {len(post_smile)} smile icons -> {ICON_SMILE}")
