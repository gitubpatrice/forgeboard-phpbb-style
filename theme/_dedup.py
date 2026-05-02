"""
forgeboard.css full deduplication script.

Three passes:
  1. Merge multiple top-level rules with identical selector
     -> last-wins property cascade, keep merged rule at LAST position.
  2. Merge multiple @media blocks with identical query
     (e.g. four `@media (max-width: 900px) { ... }`)
     -> concatenate their inner content into a single block at LAST position.
  3. Inside each @media block, merge rules with identical selector
     -> same last-wins property cascade.

Reports counts and verifies brace balance.
"""

import re
from collections import defaultdict

with open('forgeboard.css', 'r', encoding='utf-8') as f:
    s = f.read()

orig_len = len(s)
n = len(s)


def parse_top_level(text):
    """Tokenize a CSS string into a flat list of items at top level only."""
    items = []
    i = 0
    nn = len(text)
    while i < nn:
        # whitespace
        j = i
        while j < nn and text[j] in ' \t\n\r':
            j += 1
        if j > i:
            items.append({'kind': 'ws', 'text': text[i:j]})
            i = j
            continue
        if i >= nn:
            break
        # comment
        if text.startswith('/*', i):
            end = text.find('*/', i + 2)
            if end == -1:
                items.append({'kind': 'comment', 'text': text[i:]})
                i = nn
                break
            items.append({'kind': 'comment', 'text': text[i:end+2]})
            i = end + 2
            continue
        # at-rule
        if text[i] == '@':
            k = i
            while k < nn:
                if text[k] == '{':
                    k += 1
                    d = 1
                    while k < nn and d > 0:
                        if text[k] == '/' and k+1 < nn and text[k+1] == '*':
                            end = text.find('*/', k+2)
                            if end == -1:
                                break
                            k = end + 2
                            continue
                        if text[k] == '{':
                            d += 1
                        elif text[k] == '}':
                            d -= 1
                        k += 1
                    items.append({'kind': 'atblock', 'text': text[i:k]})
                    i = k
                    break
                elif text[k] == ';':
                    items.append({'kind': 'atrule_simple', 'text': text[i:k+1]})
                    i = k + 1
                    break
                elif text[k] == '/' and k+1 < nn and text[k+1] == '*':
                    end = text.find('*/', k+2)
                    if end == -1:
                        break
                    k = end + 2
                    continue
                else:
                    k += 1
            else:
                i = nn
            continue
        # rule
        k = i
        while k < nn and text[k] != '{':
            if text[k] == '/' and k+1 < nn and text[k+1] == '*':
                end = text.find('*/', k+2)
                if end == -1:
                    break
                k = end + 2
                continue
            k += 1
        if k >= nn:
            items.append({'kind': 'tail', 'text': text[i:]})
            i = nn
            break
        sel = text[i:k].strip()
        d = 1
        k2 = k + 1
        while k2 < nn and d > 0:
            if text[k2] == '/' and k2+1 < nn and text[k2+1] == '*':
                end = text.find('*/', k2+2)
                if end == -1:
                    break
                k2 = end + 2
                continue
            if text[k2] == '{':
                d += 1
            elif text[k2] == '}':
                d -= 1
            k2 += 1
        body = text[k+1:k2-1]
        items.append({'kind': 'rule', 'selector': sel, 'body': body, 'raw': text[i:k2]})
        i = k2
    return items


def normalize_selector(sel):
    """Normalize selector for grouping: collapse whitespace, sort comma parts."""
    parts = [p.strip() for p in sel.split(',') if p.strip()]
    parts = [re.sub(r'\s+', ' ', p) for p in parts]
    parts.sort()
    return ', '.join(parts)


def normalize_atquery(prelude):
    """Get the @media (or other) query, normalized."""
    s = prelude.split('{', 1)[0].strip()
    s = re.sub(r'\s+', ' ', s)
    return s


def parse_decls(body):
    decls = []
    cur = ''
    depth = 0
    j = 0
    while j < len(body):
        c = body[j]
        if c == '/' and j+1 < len(body) and body[j+1] == '*':
            end = body.find('*/', j+2)
            if end == -1:
                cur += body[j:]
                j = len(body)
                continue
            cur += body[j:end+2]
            j = end + 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        if c == ';' and depth == 0:
            if cur.strip():
                decls.append(cur.strip())
            cur = ''
        else:
            cur += c
        j += 1
    if cur.strip():
        decls.append(cur.strip())
    return decls


def decl_key(d):
    txt = d
    while True:
        m = re.match(r'^\s*/\*.*?\*/\s*', txt, re.DOTALL)
        if not m:
            break
        txt = txt[m.end():]
    if ':' not in txt:
        return None
    name = txt.split(':', 1)[0].strip().lower()
    # Treat important and non-important as same key (last wins)
    return name


def dedup_rules(items_local):
    """Merge rules with identical normalized selector. Last-wins cascade.
    Mutates items_local in place. Returns merge count."""
    groups = defaultdict(list)
    for idx, it in enumerate(items_local):
        if it.get('kind') == 'rule':
            key = normalize_selector(it['selector'])
            groups[key].append(idx)
    merges = 0
    for key, idx_list in groups.items():
        if len(idx_list) < 2:
            continue
        merged = []
        seen = {}
        for idx in idx_list:
            for d in parse_decls(items_local[idx]['body']):
                k = decl_key(d)
                if k is None:
                    merged.append(d)
                    continue
                if k in seen:
                    merged[seen[k]] = d
                else:
                    seen[k] = len(merged)
                    merged.append(d)
        new_body_inner = ';\n\t'.join(merged)
        if new_body_inner and not new_body_inner.endswith(';'):
            new_body_inner += ';'
        last_idx = idx_list[-1]
        # Use the original selector text from the LAST occurrence (preserves
        # the developer's preferred formatting)
        sel_orig = items_local[last_idx]['selector']
        items_local[last_idx]['body'] = '\n\t' + new_body_inner + '\n'
        items_local[last_idx]['raw'] = sel_orig + ' {' + items_local[last_idx]['body'] + '}'
        for idx in idx_list[:-1]:
            items_local[idx]['_remove'] = True
            merges += 1
    return merges


def merge_atblocks(items_local):
    """Merge @media (and other @blocks) with identical query.
    Concatenates their inner content into the LAST occurrence."""
    groups = defaultdict(list)
    for idx, it in enumerate(items_local):
        if it.get('kind') == 'atblock':
            key = normalize_atquery(it['text'])
            groups[key].append(idx)
    merges = 0
    for key, idx_list in groups.items():
        if len(idx_list) < 2:
            continue
        # Combine inner content of each block
        combined_inner = ''
        for idx in idx_list:
            t = items_local[idx]['text']
            open_idx = t.find('{')
            close_idx = t.rfind('}')
            if open_idx == -1 or close_idx == -1:
                continue
            inner = t[open_idx+1:close_idx]
            combined_inner += '\n' + inner
        # Use the last block's prelude as canonical
        last_idx = idx_list[-1]
        last_t = items_local[last_idx]['text']
        prelude = last_t[:last_t.find('{')+1]
        items_local[last_idx]['text'] = prelude + combined_inner + '\n}'
        for idx in idx_list[:-1]:
            items_local[idx]['_remove'] = True
            merges += 1
    return merges


# Pass 1: parse top level
items = parse_top_level(s)

# Pass 1a: dedup top-level rules
top_merges = dedup_rules(items)

# Pass 2: merge @media with identical query
atblock_merges = merge_atblocks(items)
# Drop removed items so subsequent recursion only sees survivors
items = [it for it in items if not it.get('_remove')]

# Pass 3: dedup rules INSIDE each remaining @media block
inner_merges = 0
for it in items:
    if it.get('kind') != 'atblock':
        continue
    text = it['text']
    open_idx = text.find('{')
    close_idx = text.rfind('}')
    if open_idx == -1 or close_idx == -1:
        continue
    prelude = text[:open_idx+1]
    inner = text[open_idx+1:close_idx]
    epilogue = text[close_idx:]

    sub_items = parse_top_level(inner)
    m = dedup_rules(sub_items)
    inner_merges += m

    parts = []
    for si in sub_items:
        if si.get('_remove'):
            continue
        if si['kind'] == 'rule':
            parts.append(si.get('raw') or (si['selector'] + ' {' + si['body'] + '}'))
        else:
            parts.append(si.get('text', ''))
    new_inner = ''.join(parts)
    it['text'] = prelude + new_inner + epilogue


# Reassemble
out_parts = []
for it in items:
    if it['kind'] == 'rule':
        out_parts.append(it.get('raw') or (it['selector'] + ' {' + it['body'] + '}'))
    else:
        out_parts.append(it.get('text', ''))
new_s = ''.join(out_parts)
# Collapse 3+ blank lines
new_s = re.sub(r'\n{3,}', '\n\n', new_s)

with open('forgeboard.css', 'w', encoding='utf-8') as f:
    f.write(new_s)

print('===== forgeboard.css dedup report =====')
print('Top-level rule merges:    ', top_merges)
print('@media block merges:      ', atblock_merges)
print('Rules merged inside @media:', inner_merges)
print('Total merges:             ', top_merges + atblock_merges + inner_merges)
print()
print('Lines:  before =', s.count('\n')+1, ' / after =', new_s.count('\n')+1)
print('Bytes:  saved  =', orig_len - len(new_s))
print('Braces: open =', new_s.count('{'), '/ close =', new_s.count('}'),
      ('OK' if new_s.count('{') == new_s.count('}') else 'MISMATCH!'))
