"""
Cross-reference forgeboard.css selectors against the template audit CSV
to find rules whose target class doesn't exist in any template.

Run from theme/:  python _orphan_audit.py /path/to/audit.csv
"""
import csv, re, sys

if len(sys.argv) < 2:
    print("Usage: python _orphan_audit.py <audit.csv>")
    sys.exit(1)

# Collect all valid class names referenced in templates
template_classes = set()
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for tok in row['Classes'].split(';'):
            tok = tok.strip()
            # Keep only valid kebab/alphanum class names (no twig vars, no comments)
            if re.fullmatch(r'[a-zA-Z][a-zA-Z0-9_-]*', tok):
                template_classes.add(tok)

# Add core phpBB JS-managed classes
template_classes.update({
    'dropdown-visible', 'visible', 'hidden', 'hasjs', 'nojs', 'hastouch',
    'notouch', 'rtl', 'ltr', 'forgeboard',
    'phpbb_alert', 'darken', 'darkenwrapper', 'tooltip', 'autowidth',
    'live-search', 'attach-image', 'phpbb_alert',
})

# All class names referenced in forgeboard.css selectors
with open('forgeboard.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_classes = set(re.findall(r'\.([a-zA-Z][a-zA-Z0-9_-]+)', css))

orphans = sorted(c for c in css_classes if c not in template_classes)
print(f"Template classes:          {len(template_classes)}")
print(f"CSS classes referenced:    {len(css_classes)}")
print(f"Orphan classes (in CSS only, not in any template):")
print(f"  {len(orphans)} found")
print()
# Group by prefix
from collections import defaultdict
by_prefix = defaultdict(list)
for o in orphans:
    parts = o.split('-')
    by_prefix[parts[0]].append(o)
for prefix in sorted(by_prefix.keys()):
    items = by_prefix[prefix]
    print(f"\n  {prefix}-* ({len(items)}):")
    for c in items:
        print(f"    .{c}")
