"""
Generates BBCode toolbar SVG icons (24x24 monochrome, currentColor).
Run from theme/images/:  python _generate_bbcode.py
"""
import os

OUTDIR = os.path.dirname(os.path.abspath(__file__)) or '.'
SIZE = 24


def svg(content):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" '
        f'width="{SIZE}" height="{SIZE}" fill="none" stroke="currentColor" '
        f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">\n'
        f'{content}\n</svg>'
    )


icons = {
    'bbcode_bold.svg': svg(
        '<path d="M6 4h6.5a3.5 3.5 0 0 1 0 7H6z" fill="currentColor" stroke="none"/>'
        '<path d="M6 11h7.5a3.5 3.5 0 0 1 0 7H6z" fill="currentColor" stroke="none"/>'
    ),
    'bbcode_italic.svg': svg(
        '<path d="M14 4h-4M8 20h4M14 4l-4 16"/>'
    ),
    'bbcode_underline.svg': svg(
        '<path d="M7 4v8a5 5 0 0 0 10 0V4M5 21h14"/>'
    ),
    'bbcode_strike.svg': svg(
        '<path d="M16 6a4 4 0 0 0-4-2c-2 0-4 1-4 3 0 4 8 3 8 7 0 2-2 3-4 3a4 4 0 0 1-4-2"/>'
        '<path d="M3 12h18"/>'
    ),
    'bbcode_quote.svg': svg(
        '<path d="M5 7h6v6H7v3l-2 1zM13 7h6v6h-4v3l-2 1z" fill="currentColor" stroke="none"/>'
    ),
    'bbcode_code.svg': svg(
        '<path d="M9 7l-5 5 5 5M15 7l5 5-5 5"/>'
    ),
    'bbcode_url.svg': svg(
        '<path d="M10 14a4 4 0 0 0 5.66 0l3-3a4 4 0 0 0-5.66-5.66l-1 1"/>'
        '<path d="M14 10a4 4 0 0 0-5.66 0l-3 3a4 4 0 0 0 5.66 5.66l1-1"/>'
    ),
    'bbcode_img.svg': svg(
        '<rect x="3" y="4" width="18" height="16" rx="2"/>'
        '<circle cx="8.5" cy="9.5" r="1.5" fill="currentColor"/>'
        '<path d="M21 16l-5-5-9 9"/>'
    ),
    'bbcode_list.svg': svg(
        '<path d="M9 6h12M9 12h12M9 18h12"/>'
        '<circle cx="4" cy="6" r="1.5" fill="currentColor" stroke="none"/>'
        '<circle cx="4" cy="12" r="1.5" fill="currentColor" stroke="none"/>'
        '<circle cx="4" cy="18" r="1.5" fill="currentColor" stroke="none"/>'
    ),
    'bbcode_list_ordered.svg': svg(
        '<path d="M10 6h11M10 12h11M10 18h11"/>'
        '<text x="2" y="8"  font-family="sans-serif" font-size="7" font-weight="700" fill="currentColor" stroke="none">1</text>'
        '<text x="2" y="14" font-family="sans-serif" font-size="7" font-weight="700" fill="currentColor" stroke="none">2</text>'
        '<text x="2" y="20" font-family="sans-serif" font-size="7" font-weight="700" fill="currentColor" stroke="none">3</text>'
    ),
    'bbcode_color.svg': svg(
        '<circle cx="12" cy="12" r="9"/>'
        '<circle cx="12"  cy="6"  r="2.2" fill="#ef4444" stroke="none"/>'
        '<circle cx="6.5" cy="14" r="2.2" fill="#3b82f6" stroke="none"/>'
        '<circle cx="17.5" cy="14" r="2.2" fill="#10b981" stroke="none"/>'
    ),
    'bbcode_size.svg': svg(
        '<text x="3"  y="20" font-family="serif" font-size="14" font-weight="700" fill="currentColor" stroke="none">A</text>'
        '<text x="13" y="20" font-family="serif" font-size="20" font-weight="700" fill="currentColor" stroke="none">A</text>'
    ),
    'bbcode_smiley.svg': svg(
        '<circle cx="12" cy="12" r="9"/>'
        '<circle cx="9"  cy="10" r="1" fill="currentColor" stroke="none"/>'
        '<circle cx="15" cy="10" r="1" fill="currentColor" stroke="none"/>'
        '<path d="M8 14a4 4 0 0 0 8 0"/>'
    ),
    'bbcode_attach.svg': svg(
        '<path d="M21 11.5l-9.5 9.5a5 5 0 0 1-7-7L13 5.5a3.5 3.5 0 0 1 5 5L9 19.5a2 2 0 0 1-3-3L14 8.5"/>'
    ),
    'bbcode_eraser.svg': svg(
        '<path d="M16 5l-9 9 4 4h6l5-5z" fill="currentColor" stroke="none" fill-opacity="0.18"/>'
        '<path d="M16 5l-9 9 4 4h6l5-5z"/>'
        '<path d="M9 13l4 4M5 21h12"/>'
    ),
    'bbcode_preview.svg': svg(
        '<circle cx="12" cy="12" r="3" fill="currentColor" stroke="none"/>'
        '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/>'
    ),
    'bbcode_undo.svg': svg(
        '<path d="M3 7h12a5 5 0 0 1 0 10h-7"/>'
        '<path d="M7 3L3 7l4 4"/>'
    ),
    'bbcode_redo.svg': svg(
        '<path d="M21 7H9a5 5 0 0 0 0 10h7"/>'
        '<path d="M17 3l4 4-4 4"/>'
    ),
}

for name, content in icons.items():
    with open(os.path.join(OUTDIR, name), 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Wrote {len(icons)} BBCode SVG icons to {OUTDIR}")
