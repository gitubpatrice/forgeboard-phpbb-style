"""
Targeted :where() pass on forgeboard.css.

Only transforms selectors with 2+ ID selectors. Wraps the leading
non-final tokens in :where() so the IDs no longer contribute to
specificity.

Example:
  .forgeboard #page-footer #nav-footer .breadcrumbs a:hover
becomes:
  :where(.forgeboard #page-footer #nav-footer .breadcrumbs) a:hover

Specificity drops from (2,3,1) to (0,0,1).

Run from theme/:  python _specificity_pass.py
"""
import re

with open('forgeboard.css', 'r', encoding='utf-8') as f:
    s = f.read()

n = len(s)
out = []
i = 0
changes = 0

# at-rules whose bodies contain nested rules (not declarations)
NESTED_AT_RULES = ('@media', '@supports', '@document', '@-moz-document')


def transform_selector(sel):
    if sel.count('#') < 2:
        return sel
    if ':where(' in sel:
        return sel
    sel = sel.strip()
    if '>' in sel or '+' in sel or '~' in sel:
        return sel  # skip combinators (safer)
    parts = sel.split()
    if len(parts) < 2:
        return sel
    head = parts[:-1]
    tail = parts[-1]
    head_str = ' '.join(head)
    if head_str.count('#') < 2:
        return sel
    return ':where(' + head_str + ') ' + tail


def transform_selector_list(text):
    parts = [p.strip() for p in text.split(',')]
    transformed = [transform_selector(p) for p in parts]
    sep = ',\n' if any('\n' in p for p in parts) else ', '
    return sep.join(transformed)


def is_nested_at_rule(prelude):
    """Return True if this @-rule contains nested rules (vs declarations)."""
    p = prelude.lstrip()
    for ar in NESTED_AT_RULES:
        if p.startswith(ar) and (len(p) == len(ar) or not p[len(ar)].isalpha()):
            return True
    return False


def find_block_end(text, start):
    """Given text and index of an opening '{', find matching '}'."""
    assert text[start] == '{'
    depth = 1
    j = start + 1
    nn = len(text)
    while j < nn and depth > 0:
        c = text[j]
        if c == '/' and j + 1 < nn and text[j+1] == '*':
            e = text.find('*/', j+2)
            j = (e + 2) if e != -1 else nn
            continue
        if c == '"' or c == "'":
            quote = c
            j += 1
            while j < nn and text[j] != quote:
                if text[j] == '\\':
                    j += 2
                    continue
                j += 1
            j += 1
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        j += 1
    return j  # index past the closing '}'


def process_top(text):
    """Process the top of a rule scope: emit rules + @-rules verbatim or
    transformed. Inside rule bodies, declarations are emitted unchanged."""
    global changes
    nn = len(text)
    j = 0
    chunks = []
    while j < nn:
        c = text[j]
        if c in ' \t\n\r':
            chunks.append(c)
            j += 1
            continue
        if text.startswith('/*', j):
            e = text.find('*/', j + 2)
            chunks.append(text[j:(e+2) if e != -1 else nn])
            j = (e + 2) if e != -1 else nn
            continue
        if c == '@':
            # at-rule: read prelude until { or ;
            k = j
            while k < nn and text[k] not in '{;':
                if text[k] == '/' and k+1 < nn and text[k+1] == '*':
                    e = text.find('*/', k+2)
                    k = (e + 2) if e != -1 else nn
                    continue
                k += 1
            if k >= nn:
                chunks.append(text[j:])
                break
            prelude = text[j:k+1]
            if text[k] == ';':
                chunks.append(prelude)
                j = k + 1
                continue
            # at-block
            block_start = k  # position of '{'
            block_end = find_block_end(text, block_start)
            inner = text[block_start+1:block_end-1]
            chunks.append(prelude)
            if is_nested_at_rule(prelude):
                # Recurse into inner content (it has nested rules)
                chunks.append(process_top(inner))
            else:
                # Treat as opaque body (e.g. @keyframes, @font-face)
                chunks.append(inner)
            chunks.append('}')
            j = block_end
            continue
        # Plain rule: read selector list until '{', then copy body verbatim.
        k = j
        while k < nn and text[k] != '{':
            if text[k] == '/' and k+1 < nn and text[k+1] == '*':
                e = text.find('*/', k+2)
                k = (e + 2) if e != -1 else nn
                continue
            k += 1
        if k >= nn:
            chunks.append(text[j:])
            break
        sel_text = text[j:k]
        new_sel = transform_selector_list(sel_text)
        if new_sel.strip() != sel_text.strip():
            changes += 1
        chunks.append(new_sel)
        # body — copy verbatim (do NOT recurse into property declarations)
        block_end = find_block_end(text, k)
        chunks.append(text[k:block_end])
        j = block_end
    return ''.join(chunks)


new_s = process_top(s)

# Sanity check braces
ob, cb = new_s.count('{'), new_s.count('}')
if ob != cb:
    print(f"!! Brace mismatch: open={ob} close={cb} — aborting write")
    raise SystemExit(1)

with open('forgeboard.css', 'w', encoding='utf-8') as f:
    f.write(new_s)

print(f"Selectors transformed (wrapped in :where()): {changes}")
print(f"Lines: {new_s.count(chr(10)) + 1}")
print(f"Braces: open={ob} close={cb} — OK")
