"""Inventory all forge-* classes used in ForgeBoard templates and CSS."""
import re, os, glob
from collections import defaultdict

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

classes_per_template = defaultdict(set)
all_classes = set()
for path in glob.glob(os.path.join(base, 'template', '*.html')):
    name = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    for m in re.finditer(r'\b(forge-[a-z0-9-]+)\b', html):
        classes_per_template[name].add(m.group(1))
        all_classes.add(m.group(1))

# Reverse: which templates each class is used in
class_to_templates = defaultdict(set)
for tpl, classes in classes_per_template.items():
    for c in classes:
        class_to_templates[c].add(tpl)

print(f"Total: {len(all_classes)} forge-* classes\n")

# Group by second token (forge-XXX-...)
groups = defaultdict(list)
for c in sorted(all_classes):
    parts = c.split('-')
    if len(parts) >= 2:
        groups[parts[1]].append(c)

for prefix, items in sorted(groups.items()):
    print(f"\n## forge-{prefix}-* ({len(items)})")
    for c in items:
        tpls = ', '.join(sorted(class_to_templates[c]))
        print(f"  .{c}  -> {tpls}")
