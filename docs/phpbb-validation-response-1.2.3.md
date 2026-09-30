# phpBB.com validation response — ForgeBoard 1.2.3

Follow-up comment to post on the phpBB.com Customisations topic. 1.2.2 had
already been submitted when this was found, so this reads as a replacement
rather than a fresh submission. Excluded from the release ZIP (docs/ is not
shipped).

---

Follow-up: ForgeBoard 1.2.3 supersedes the 1.2.2 currently in the queue.

Testing a real attachment upload turned up a defect that, once traced, explained
a whole family of dark-theme problems. I would rather have you review 1.2.3 than
1.2.2. The change is CSS only — no template, no event and no asset was touched,
so everything already covered in 1.2.2 is unchanged. Template events still
report 0 missing / 0 undocumented / 0 malformed.

**Root cause**

ForgeBoard @imports prosilver's full stylesheet chain, colours.css included.
Every literal colour declared there shows through on any element the style does
not restyle itself. Those values were written for a light board, so on the dark
theme they are simply wrong. The visible symptom was the attachment box:

    .attachbox { background-color: #FFFFFF; border-color: #C9D2D8; }

a glaring white panel on a dark post. The uploaded image rendered correctly;
only its frame was wrong.

Auditing colours.css for the same pattern — a literal colour on a selector
ForgeBoard never restyles — turned up 28 rules leaking through. I fixed the 20
that actually break on the dark theme, all by re-expressing prosilver's intent
in the style's existing colour tokens:

- attachments: the box, its separator, its captions and stats, the image border
- thumbnails: background, border and hover state
- the UCP avatar gallery picker
- ul.forums, .jumpbox-sub-link and its hover state
- the dropdown caret
- .current — prosilver sets `color: #000000 !important`, so the override needs
  !important as well or the text stays black on the dark surface
- the reported / disapproved notification labels

**The attachment box**

Two new tokens carry it, declared in all three token blocks — :root,
[data-theme="dark"], and the prefers-color-scheme fallback that serves visitors
with JavaScript disabled:

    --gb-attachbox-bg      #f7f9fb light / #181c23 dark
    --gb-attachbox-border  #7d8ea6 light / #5d6d88 dark

The fill sits deliberately close to the post surface in both themes (1.06:1
light, 1.01:1 dark), so the border alone delimits the block. That makes it a
meaningful UI boundary rather than decoration, so both borders clear 3:1 under
WCAG 1.4.11 — 3.16:1 light and 3.26:1 dark, measured against the box and against
the post surface. Text inside the dark box reads at 17.1:1 for body copy, 8.5:1
for the muted stats line and 6.8:1 for links.

The box now uses the style's --gb-radius-lg token, and its padding was raised to
match: prosilver's 6px was written for square corners and let the label run
under the corner arc once the radius was applied.

**Attachments tab: total upload progress**

posting_editor.html puts <strong class="file-total-progress"> inside the
Attachments tab link. prosilver lays it out as a display:block element with
negative margins calibrated for a display:block anchor padded 5px 9px.
ForgeBoard renders that anchor as an inline-flex row with a gap, which turned
the bar into a second flex item beside the label and pushed the text off-centre.

It is now taken out of the flow — absolutely positioned along the bottom edge of
the tab, inset by the corner radius. The anchor is already position:relative from
prosilver's cp.css, so no extra rule was needed for the containing block.

**Left as they are**

Eight leaks remain, deliberately:

- the five PM colour flags (marked, replied, friend, foe, reported) — semantic
  markers whose hues are the convention users recognise, and they are side
  borders rather than fills;
- .darken and .loading_indicator, black overlays intended to be black in both
  themes;
- .message-box textarea, where ForgeBoard's own rule already wins on source
  order at equal specificity.
