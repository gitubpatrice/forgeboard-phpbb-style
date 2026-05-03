"""
Generates a clean SVG smiley set in ForgeBoard style.
Round soft yellow face with simple expressions.
Run from theme/images/smilies/:  python _generate_smileys.py
"""
import os

OUTDIR = os.path.dirname(os.path.abspath(__file__)) or '.'
SIZE = 22

YELLOW = '#fcd34d'
YELLOW_DARK = '#f59e0b'
RED = '#ef4444'
BLUE = '#3b82f6'
GRAY = '#374151'
WHITE = '#ffffff'


def face(expression, extra='', bg=YELLOW, border=YELLOW_DARK):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" '
        f'width="{SIZE}" height="{SIZE}">\n'
        f'  <circle cx="11" cy="11" r="10" fill="{bg}" stroke="{border}" stroke-width="0.7"/>\n'
        f'  {expression}\n'
        f'  {extra}\n'
        f'</svg>'
    )


# Eye / mouth / brow primitives
EYE_DOT_L = f'<circle cx="7.5" cy="9" r="1.2" fill="{GRAY}"/>'
EYE_DOT_R = f'<circle cx="14.5" cy="9" r="1.2" fill="{GRAY}"/>'
EYE_LINE_L = f'<path d="M6 9 L9 9" stroke="{GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_LINE_R = f'<path d="M13 9 L16 9" stroke="{GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_WINK_L = f'<path d="M6 9 Q7.5 8 9 9" stroke="{GRAY}" stroke-width="1.2" fill="none" stroke-linecap="round"/>'
EYE_X_L = f'<path d="M6 8L9 10M9 8L6 10" stroke="{GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_X_R = f'<path d="M13 8L16 10M16 8L13 10" stroke="{GRAY}" stroke-width="1.2" stroke-linecap="round"/>'
EYE_HEART_L = f'<path d="M6 8.5 Q6 7.5 7 7.5 Q7.5 7.5 7.5 8 Q7.5 7.5 8 7.5 Q9 7.5 9 8.5 Q9 9.5 7.5 10.5 Q6 9.5 6 8.5 Z" fill="{RED}"/>'
EYE_HEART_R = f'<path d="M13 8.5 Q13 7.5 14 7.5 Q14.5 7.5 14.5 8 Q14.5 7.5 15 7.5 Q16 7.5 16 8.5 Q16 9.5 14.5 10.5 Q13 9.5 13 8.5 Z" fill="{RED}"/>'

MOUTH_SMILE = f'<path d="M7 13 Q11 17 15 13" stroke="{GRAY}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
MOUTH_BIG_SMILE = f'<path d="M6 13 Q11 19 16 13 Z" fill="#fff" stroke="{GRAY}" stroke-width="1.2" stroke-linejoin="round"/>'
MOUTH_FROWN = f'<path d="M7 16 Q11 12 15 16" stroke="{GRAY}" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
MOUTH_FLAT = f'<path d="M8 15 L14 15" stroke="{GRAY}" stroke-width="1.4" stroke-linecap="round"/>'
MOUTH_O = f'<circle cx="11" cy="15" r="1.5" fill="{GRAY}"/>'
MOUTH_TONGUE = f'<path d="M7 13 Q11 17 15 13" stroke="{GRAY}" stroke-width="1.4" fill="none"/><path d="M9 14.5 Q11 18 13 14.5 Z" fill="{RED}"/>'
MOUTH_KISS = f'<path d="M9 15 Q11 12 13 15 Q11 17 9 15 Z" fill="{RED}"/>'
MOUTH_GRIN = f'<path d="M6 13 L16 13 Q15 17 11 17 Q7 17 6 13 Z" fill="#fff" stroke="{GRAY}" stroke-width="1"/>'
MOUTH_ZIP = f'<path d="M6 14 L16 14" stroke="{GRAY}" stroke-width="1.5"/><path d="M8 13.2 L8 14.8 M10 13.2 L10 14.8 M12 13.2 L12 14.8 M14 13.2 L14 14.8" stroke="{GRAY}" stroke-width="0.8"/>'

TEAR = f'<path d="M14 11 Q14.5 13 14 14 Q13.5 13 14 11 Z" fill="{BLUE}"/>'
SWEAT = f'<path d="M16 7 Q17 9 16 10 Q15 9 16 7 Z" fill="{BLUE}"/>'
SUNGLASSES = f'<rect x="4.5" y="7.5" width="6" height="3.5" rx="1" fill="{GRAY}"/><rect x="11.5" y="7.5" width="6" height="3.5" rx="1" fill="{GRAY}"/><path d="M10.5 9 L11.5 9" stroke="{GRAY}" stroke-width="0.8"/>'
HALO = f'<ellipse cx="11" cy="2" rx="5" ry="1.2" fill="none" stroke="{YELLOW_DARK}" stroke-width="1"/>'
HORNS = f'<path d="M5 4 Q4 1 6 2 Q7 3 7 5 Z" fill="{RED}"/><path d="M17 4 Q18 1 16 2 Q15 3 15 5 Z" fill="{RED}"/>'

# Smiley map: filename -> face content
smileys = {
    'icon_e_smile.svg':       face(EYE_DOT_L + EYE_DOT_R + MOUTH_SMILE),
    'icon_e_biggrin.svg':     face(EYE_DOT_L + EYE_DOT_R + MOUTH_BIG_SMILE),
    'icon_e_grin.svg':        face(EYE_LINE_L + EYE_LINE_R + MOUTH_GRIN),
    'icon_e_wink.svg':        face(EYE_WINK_L + EYE_DOT_R + MOUTH_SMILE),
    'icon_e_sad.svg':         face(EYE_DOT_L + EYE_DOT_R + MOUTH_FROWN),
    'icon_e_cry.svg':         face(EYE_DOT_L + EYE_DOT_R + MOUTH_FROWN, TEAR),
    'icon_e_surprised.svg':   face(EYE_DOT_L + EYE_DOT_R + MOUTH_O),
    'icon_e_confused.svg':    face(EYE_DOT_L + EYE_DOT_R + MOUTH_FLAT),
    'icon_e_tongue.svg':      face(EYE_DOT_L + EYE_DOT_R + MOUTH_TONGUE),
    'icon_e_kiss.svg':        face(EYE_LINE_L + EYE_LINE_R + MOUTH_KISS, EYE_HEART_L + EYE_HEART_R),
    'icon_e_love.svg':        face(EYE_HEART_L + EYE_HEART_R + MOUTH_SMILE),
    'icon_e_dead.svg':        face(EYE_X_L + EYE_X_R + MOUTH_FLAT),
    'icon_e_geek.svg':        face(SUNGLASSES + MOUTH_SMILE),
    'icon_e_cool.svg':        face(SUNGLASSES + MOUTH_FLAT),
    'icon_e_angel.svg':       face(EYE_DOT_L + EYE_DOT_R + MOUTH_SMILE, HALO),
    'icon_e_devil.svg':       face(EYE_DOT_L + EYE_DOT_R + MOUTH_GRIN, HORNS, bg=RED, border='#b91c1c'),
    'icon_e_oops.svg':        face(EYE_DOT_L + EYE_DOT_R + MOUTH_O, SWEAT),
    'icon_e_zip.svg':         face(EYE_DOT_L + EYE_DOT_R + MOUTH_ZIP),
    'icon_e_neutral.svg':     face(EYE_DOT_L + EYE_DOT_R + MOUTH_FLAT),
    'icon_e_lol.svg':         face(EYE_X_L + EYE_X_R + MOUTH_BIG_SMILE),
    # Status / emotion
    'icon_mad.svg':           face(EYE_LINE_L + EYE_LINE_R + MOUTH_FROWN, bg='#fb923c', border='#c2410c'),
    'icon_thinking.svg':      face(EYE_DOT_L + EYE_DOT_R + MOUTH_FLAT, '<path d="M14 17 L14 19" stroke="' + GRAY + '" stroke-width="1.2"/><circle cx="14" cy="20" r="0.8" fill="' + GRAY + '"/>'),
    'icon_idea.svg':          face(EYE_DOT_L + EYE_DOT_R + MOUTH_SMILE, '<path d="M11 1 L11 3" stroke="#fbbf24" stroke-width="1"/><circle cx="11" cy="2" r="1.5" fill="#fde047"/>'),
}

for name, content in smileys.items():
    with open(os.path.join(OUTDIR, name), 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Wrote {len(smileys)} smiley SVG files to {OUTDIR}")
