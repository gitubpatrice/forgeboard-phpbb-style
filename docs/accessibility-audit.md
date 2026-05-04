# ForgeBoard — Accessibility Audit

**Reference**: WCAG 2.1 AA / RGAA 4.1
**Date**: 2026-05-02
**Method**: Static code review (HTML templates + CSS + JS)
**Estimated score**: 68 / 100

This document tracks the issues identified during the audit and their resolution status.

---

## Blockers (must fix before phpBB submission)

| ID | Issue | File | Status |
|---|---|---|---|
| B1 | Skip link placed AFTER header — keyboard users tab through nav before reaching it | `overall_header.html:111-112` | ✅ Fixed |
| B2 | `outline: 0` on footer links without alternative — focus invisible | `forgeboard.css:5527, 5553, 5567` | ✅ Fixed |
| B3 | Input focus invisible in light mode (box-shadow contrast ~1.2:1, < 3:1 required) | `forgeboard.css:1911, 6621` | ✅ Fixed |
| B4 | AJAX modals lack `role="alertdialog"`, `aria-modal`, accessible close label | `overall_footer.html:50-61` | ✅ Fixed |
| B5 | `role="menubar"` / `role="menu"` / `role="menuitem"` misused on site nav (desktop-app pattern, breaks SR) | `navbar_header.html`, `overall_footer.html:25` | ✅ Fixed |

## Major issues

| ID | Issue | File | Status |
|---|---|---|---|
| M1 | `aria-expanded` missing on all `dropdown-trigger` | `navbar_header.html`, `jumpbox.html` | ✅ Fixed |
| M2 | Theme toggle button doesn't announce current state | `navbar_header.html`, `forge_theme_toggle.js` | ✅ Fixed |
| M3 | No `@media (prefers-reduced-motion)` — 12 transitions ignore user preference | `forgeboard.css` | ✅ Fixed |
| M4 | `role="banner"` duplicated on `<header>` AND `<div>` child | `overall_header.html:71-72` | ✅ Fixed |
| M5 | Forum column labels hidden with `aria-hidden="true"` — SR users lose context | `forumlist_body.html:17` | ✅ Fixed |
| M6 | Positive `tabindex` (`tabindex="1"` etc.) in posting + login forms | `posting_editor.html`, `index_body.html` | ✅ Fixed |
| M7 | Header search `<fieldset>` lacks `<legend>` | `overall_header.html:86-96` | ✅ Fixed |

## Minor

| ID | Issue | Notes |
|---|---|---|
| m1 | `lang="{S_USER_LANG}"` may produce invalid value (`fr_FR` instead of `fr-FR`) | To verify in production |
| m2 | Multiple `<nav role="navigation">` should be distinguished with `aria-label` | Header & footer both have them |
| m3 | `<header>` nested inside `<section>` (hero blocks) — semantically valid, just noted |
| m4 | Heading hierarchy jumps `<h1>` to `<h3>` in stat blocks | Verify per-page |
| m5 | Dark theme inaccessible without JS | Already handled via `prefers-color-scheme` fallback |
| m6 | `print.css` hides `.skiplink` — correct behavior for print |

## Browser-only tests still required

These cannot be done from static code review and must be performed manually:

1. **Real contrast measurement** — `--gb-text-muted` (`#607080`) on `--gb-canvas` (`#f3f5f7`) with Colour Contrast Analyser. Target ≥ 4.5:1 for body text.
2. **Full keyboard navigation** — Tab through every page (index, viewforum, viewtopic, posting, MCP, UCP) without using mouse.
3. **Screen reader test** — NVDA + Firefox / VoiceOver + Safari on:
   - Index page
   - Topic with quotes/code
   - Posting form with smileys / BBCode toolbar
   - Notifications dropdown
   - Theme toggle button (verify announced state changes)
4. **200% zoom** — viewport reflow check on all major templates.
5. **320px width** — narrow phone layout test.
6. **Focus visible contrast** — measure `--gb-input-focus-ring` (3px ring color) against the surrounding background. Target ≥ 3:1 (WCAG 2.4.11).
7. **Dropdown keyboard** — Enter/Space opens, Escape closes, Tab moves through items.
8. **Dark mode contrast** — All token combinations in dark mode against a contrast checker.
9. **No-JS dark mode** — Disable JavaScript, set OS preference to dark, verify auto fallback works.
10. **Real `lang` attribute** — Inspect `<html lang>` value with French installation.

## Continuous code review checklist

- Any new icon-only element must have `aria-hidden="true"` + `.sr-only` text
- Any new modal must have `role="dialog"` + `aria-modal="true"` + `aria-labelledby` + focus trap
- No `outline: 0` without a documented visible replacement
- No positive `tabindex` (> 0)
- Every dropdown trigger must have `aria-expanded` toggled by JS
- Every form `<fieldset>` must have a `<legend>` (visible or `.sr-only`)
- Color tokens must be tested in BOTH light and dark modes for contrast
