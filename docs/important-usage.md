# `!important` usage in ForgeBoard

This document lists **every** `!important` in the CSS and explains why it is
needed. Reference for phpBB reviewers and future maintenance.

> **General rule** — `!important` is only used in 3 legitimate cases:
> 1. To beat a Prosilver `!important` (specificity alone is not enough)
> 2. To beat a Prosilver / legacy override placed AFTER the ForgeBoard rule (cascade source-order)
> 3. To lock down absolute-positioned dropdowns that other rules might disturb

Total: **25 occurrences** in `theme/forgeboard.css`.

---

## 1. Hover state of "reported" topics — 2× (lines 300-301)

```css
.forgeboard ul.topiclist li.row.reported:hover { ... }
```

**Why**: Prosilver `colours.css:300` contains:

```css
li.reported:hover { background-color: #ECD5D8 !important; }
```

With Prosilver itself using `!important`, **no** higher-specificity rule on
the author side can beat it. The only way to override in standard CSS is
also `!important`. This is a case where Prosilver imposes the pattern.

---

## 2. Topbar responsive stacking — 2× (lines 7112-7113)

```css
@media (max-width: 1100px) {
  .forgeboard .forge-topbar {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
  }
}
```

**Why**: 4 non-media rules target `.forgeboard .forge-topbar` later in the
file (legacy passes accumulated over time). Same specificity (1,1,0) → the
later non-media rule won by source-order, which re-imposed the 2-column
grid on mobile and broke the layout.

`!important` at the mobile breakpoint is the clean fix since we don't want
to reorganise the whole file (regression risk).

---

## 3. Forum grid placeholders hidden on mobile — 1× (line 7162)

```css
@media (max-width: 760px) {
  .forge-forum-grid::before,
  .forge-forum-grid::after,
  .forge-forum-grid:has(> .forge-forum-card:only-child)::before,
  ... { display: none !important; }
}
```

**Why**: the placeholder pseudo-elements have `display: block` forced by
the `:has()` rule earlier in the file. To hide them on mobile despite that
`display: block` (same specificity, unfavourable source-order), `!important`
is required.

Non-`!important` alternative: declare an even more specific selector at the
breakpoint, but that means stacking more classes (`#wrap .forgeboard...`).
`!important` is more readable here.

---

## 4. Notification dropdown positioning — 5× (lines 7389-7393)

```css
.forgeboard #notification_list,
.forgeboard .forge-nav-user-notify > #notification_list,
.forgeboard #notification_list.dropdown {
  left: auto !important;
  right: 0 !important;
  margin: 0 !important;
  margin-right: 0 !important;
  width: min(340px, calc(100vw - 24px)) !important;
}
```

**Why**: Prosilver applies `margin-right: -500px` to `.dropdown` (a layout
hack to allow inner content to be wider than the trigger). Several earlier
ForgeBoard rules tried to neutralise it but with varying specificity. The
dropdown was appearing at unpredictable positions depending on the page
(sometimes 200px to the right, sometimes off-screen).

`!important` here **locks** positioning deterministically. This is a
critical component (visible everywhere, on every page) — predictability
takes priority over cascade "purity".

---

## 5. Notification dropdown contents flow — 5× (lines 7437-7441)

```css
.forgeboard #notification_list .dropdown-contents {
  width: 100% !important;
  left: auto !important;
  margin: 0 !important;
  position: relative !important;
  right: auto !important;
}
```

**Why**: Prosilver `common.css:1120` enforces
`position: absolute; width: 340px` on `.dropdown-extended .dropdown-contents`.
ForgeBoard wants the contents to **flow** inside their wrapper (which is itself
absolutely positioned, anchored right). Without `!important`, Prosilver wins
on `position` by specificity.

Same for `width`, `left`, `right`, `margin` — all forced by Prosilver.

---

## 6. Phone navbar flex layout — 2× (lines 7519-7521)

```css
@media (max-width: 510px) {
  .forgeboard .forge-nav-main-card #nav-main,
  .forgeboard #nav-main.linklist {
    display: flex !important;
    justify-content: flex-start !important;
  }
}
```

**Why**: `#nav-main` receives its `display` (flex) from other ForgeBoard rules
that are NOT inside `@media`. At the mobile breakpoint, we want to enforce a
specific flex layout with `justify-content: flex-start`. Without `!important`,
the non-media rules (later source-order) take over and the hamburger doesn't
align correctly.

---

## 7. Theme toggle button right alignment — 1× (line 7960)

```css
.forgeboard .forge-nav-theme-toggle {
  margin-left: auto !important;
}
```

**Why**: `.linklist > li` has `margin: 0` or `margin-left: 5px` depending on
the Prosilver context. To push the theme-toggle button to the far right of
its flex `<ul>`, `margin-left: auto` is needed. The `!important` beats
linklist-item-specific margin rules that are more specific.

---

## Strategy for reducing later

Of these 7 groups, **3 are unavoidable** (Prosilver itself uses `!important`
or `position: absolute`):
- Group 1 (reported hover)
- Group 4 (notification positioning)
- Group 5 (notification contents flow)

The other 4 could be eliminated by:
- Reorganising the file so ForgeBoard rules are consolidated by component
  (all `.forge-topbar` rules in one block, etc.)
- Increasing specificity with `:where(.forgeboard)` so we don't break
  external overrides

This is one of the **technical debt** items identified (refactor by
component) — non-blocking for phpBB submission, deferred to v2.
