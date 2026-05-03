# ForgeBoard Stylebook

A reference of all `.forge-*` classes shipped by the theme, grouped by feature.
Use this when:

- Modifying a section without breaking another
- Writing a phpBB extension that wants to look "ForgeBoard-native"
- Auditing markup before submitting changes

> ForgeBoard inherits from Prosilver. Classes prefixed `forge-` are **custom**
> and exclusive to ForgeBoard. Other classes (`.button`, `.dropdown-container`,
> `.topiclist`, `.row`, etc.) come from Prosilver and follow phpBB conventions.

---

## Design tokens (CSS custom properties)

All ForgeBoard tokens live on `:root` (light theme) and are overridden by
`:root[data-theme="dark"]`. The toggle script `forge_theme_toggle.js` flips the
attribute based on user preference (cookie + localStorage).

### Color
```
--gb-canvas, --gb-surface, --gb-surface-subtle, --gb-surface-muted
--gb-border, --gb-border-muted
--gb-text, --gb-text-muted
--gb-link, --gb-link-hover
--gb-accent, --gb-accent-hover
--gb-danger
--gb-header, --gb-header-muted
--gb-focus
--gb-blue-soft, --gb-red-soft, --gb-white-soft
```

### Typography (14 px base, 1.5 leading)
```
--gb-font-sans  --gb-font-mono
--gb-font-xs (12)  --gb-font-sm (13)  --gb-font-md (14)  --gb-font-lg (16)
--gb-font-h1 (32)  --gb-font-h2 (24)  --gb-font-h3 (20)
--gb-leading-tight (1.25)  --gb-leading-normal (1.5)
--gb-weight-normal (400)  --gb-weight-medium (500)
--gb-weight-semibold (600)  --gb-weight-bold (700)
```

### Radius (max 9 px on buttons; 999 px never used)
```
--gb-radius-sm (4)  --gb-radius-md (6)  --gb-radius-lg (12)  --gb-radius-pill (999)
--gb-radius (12, legacy)  --gb-radius-small (6, legacy)
```

### Spacing (4 px grid)
```
--gb-space-1 (4)  -2 (8)  -3 (12)  -4 (16)  -6 (24)  -8 (32)  -12 (48)
```

### Buttons
```
--gb-btn-primary-bg / -hover / -active / -fg / -border   (sky-blue CTA)
--gb-btn-danger-bg  / -hover / -active / -fg / -border   (red destructive)
--gb-btn-default-bg / -hover / -active / -fg / -border   (neutral surface)
```

### Inputs
```
--gb-input-bg, --gb-input-border, --gb-input-focus-ring, --gb-input-shadow-inset
```

---

## Header & navigation

| Class | Where | What it does |
|---|---|---|
| `.forge-shell` | `overall_header.html` | Outer wrapper around the page (replaces `.wrap`) |
| `.forge-page-header` | `overall_header.html` | `<header>` containing topbar + navbar |
| `.forge-topbar` | `overall_header.html` | Logo + search-box row at the very top |
| `.forge-brand` | `overall_header.html` | The clickable site logo + name combo |
| `.forge-brand-copy` | `overall_header.html` | The text container (site name + tagline) inside `.forge-brand` |
| `.forge-search` | `overall_header.html` | Top-right search-box wrapper (variant of phpBB `.search-box`) |
| `.forge-nav-wrap` / `.forge-nav-card` | `overall_header.html` | Card holding the main navbar |
| `.forge-nav-layout` | `navbar_header.html` | Flex/grid container inside `.forge-nav-card` |
| `.forge-nav-top` | `navbar_header.html` | Top row (main links + user actions) |
| `.forge-nav-main-card` | `navbar_header.html` | `<ul#nav-main>` parent — FAQ / ACP / MCP + theme toggle |
| `.forge-nav-user-card` | `navbar_header.html` | `<ul#nav-user>` parent — avatar / PM / notifications |
| `.forge-nav-user-item` | `navbar_header.html` | `<li>` modifier for user-card items |
| `.forge-nav-user-profile` | `navbar_header.html` | Avatar dropdown trigger |
| `.forge-nav-user-pm` | `navbar_header.html` | PM bell trigger |
| `.forge-nav-user-notify` | `navbar_header.html` | Notifications bell trigger |
| `.forge-nav-user-login` / `.forge-nav-user-register` | `navbar_header.html` | Guest entry points |
| `.forge-nav-breadcrumbs-card` | `navbar_header.html` | Bottom row (breadcrumb + responsive search) |
| `.forge-nav-theme-toggle` | `navbar_header.html` | `<li>` wrapping the theme toggle, pushed right |
| `.forge-theme-toggle` | `navbar_header.html` | The button itself (light/dark/auto cycle) |
| `.forge-theme-icon`, `.forge-theme-icon-light/-dark/-auto` | `navbar_header.html` | One SVG icon per state — visibility driven by `[data-theme-pref]` |

---

## Hero / kicker

| Class | Where | Purpose |
|---|---|---|
| `.forge-hero` | `index_body.html` | Welcome card on the index page (clock + site name + Mark forums read) |
| `.forge-hero-action` | `index_body.html` | The "Mark forums read" button placement |
| `.forge-forum-hero` | `viewforum_body.html` | Per-forum hero (title + description + MCP/Mark read) |
| `.forge-forum-hero-actions` | `viewforum_body.html` | Buttons row inside the forum hero |
| `.forge-forum-hero-desc` | `viewforum_body.html` | Forum description paragraph |
| `.forge-hero-mark-read` | `viewforum_body.html` | Variant of the action button |
| `.forge-kicker` | `index_body.html`, `viewforum_body.html`, `forumlist_body.html`, `faq_body.html` | Small uppercase label above an h1/h2 ("FORUM", "TOPICS", etc.) |

---

## Forum list (index)

| Class | Where | Purpose |
|---|---|---|
| `.forge-category` | `forumlist_body.html` | A category section (header + grid of forums) |
| `.forge-category-head` | both | Header row: title (h2) + column labels |
| `.forge-category-labels` | both | Right-side labels: Topics / Posts / Last post |
| `.forge-forum-grid` | `forumlist_body.html` | Grid of forum cards (responsive cols) |
| `.forge-forum-card` | `forumlist_body.html` | One forum item (icon + title + numbers + lastpost) |
| `.forge-forum-unread` (modifier) | `forumlist_body.html` | Forum has unread posts |
| `.forge-forum-link` (modifier) | `forumlist_body.html` | Forum is an external link |
| `.forge-forum-main` | `forumlist_body.html` | Left half of card (icon + title + desc) |
| `.forge-forum-icon` | `forumlist_body.html` | Folder/link icon container |
| `.forge-forum-copy` | `forumlist_body.html` | Title + description column |
| `.forge-forum-desc` | `forumlist_body.html` | Forum description |
| `.forge-forum-meta` | `forumlist_body.html` | Moderators / subforums line |
| `.forge-forum-numbers` | `forumlist_body.html` | Topics / Posts counters |
| `.forge-lastpost` | `forumlist_body.html`, `viewforum_body.html` | Last-post column |
| `.forge-lastpost-label` | `forumlist_body.html` | "Last post" label (responsive only) |
| `.forge-lastpost-jump` | `forumlist_body.html`, `viewforum_body.html` | Arrow → jump to last post |

---

## Forum view (topic list)

| Class | Where | Purpose |
|---|---|---|
| `.forge-toolbar` | `viewforum_body.html` | New Topic / search / pagination bar (top + bottom) |
| `.forge-action-strip` | `viewforum_body.html` | Variant of toolbar without the bar background |
| `.forge-toolbar-actions` | `viewforum_body.html` | Buttons row inside `.forge-toolbar` |
| `.forge-inline-search` | `viewforum_body.html` | Inline forum-search (no header search) |
| `.forge-primary-button` | `viewforum_body.html` | Promotes a button to the sky-blue CTA |
| `.forge-bottom-row` (and -top, -bottom) | viewforum, viewtopic | Multiple rows inside the bottom toolbar |
| `.forge-bottom-left` / `.forge-bottom-right` | viewforum, viewtopic | Halves inside a bottom row |
| `.forge-topic-section` | `viewforum_body.html` | Each section (Announcements / Topics) |
| `.forge-topic-grid` | `viewforum_body.html` | Grid of topic cards |
| `.forge-topic-card` | `viewforum_body.html` | One topic row (4-col grid) |
| `.forge-topic-card-viewforum` | `viewforum_body.html` | Variant for viewforum context |
| `.forge-topic-main` (and -viewforum) | `viewforum_body.html` | Title + byline column |
| `.forge-topic-icon` | `viewforum_body.html` | File/sticky/announce icon |
| `.forge-topic-copy` | `viewforum_body.html` | Title + meta wrapper |
| `.forge-topic-byline` | `viewforum_body.html` | "by Author / 12 Dec 2021" line |
| `.forge-topic-flag` | `viewforum_body.html` | Reported / unapproved / deleted badge |
| `.forge-topic-stats` | `viewforum_body.html` | Wrapper around replies + views (transparent grid) |
| `.forge-topic-stat`, `-stat-replies`, `-stat-views` | `viewforum_body.html` | Individual stat boxes |
| `.forge-topic-lastpost` | `viewforum_body.html` | Last-post column in viewforum cards |
| `.forge-topic-pagination` | `viewforum_body.html` | "X topics · page Y of Z" |

---

## Topic view (viewtopic)

| Class | Where | Purpose |
|---|---|---|
| `.forge-topic-title` | `viewtopic_body.html` | The H2 topic title (with optional first-unread chip on the right) |
| `.forge-first-unread` | `viewtopic_body.html` | Right-aligned chip linking to first unread post |
| `.forge-topic-search` | `viewtopic_body.html` | Inline search inside topic |
| `.forge-topic-search-row` | `viewtopic_body.html` | Search container row |
| `.forge-topic-bottom-bar` | `viewtopic_body.html` | Bottom action bar (jumpbox, return, etc.) |
| `.forge-quickmod`, `-menu`, `-item`, `-link` | `viewtopic_body.html` | Quickmod dropdown for moderators |

---

## Posting (preview / edit / topic review)

| Class | Where | Purpose |
|---|---|---|
| `.forge-posting-submit-buttons` | `posting_editor.html` | Submit / Preview / Cancel row |
| `.forge-topic-review-bar` | `posting_topic_review.html` | Header bar (title + Expand-view toggle) |
| `.forge-topic-review-head` | `posting_topic_review.html` | The H3 inside the bar |
| `.forge-topic-review-toggle` | `posting_topic_review.html` | Expand view link (right side) |
| `.forge-topic-review-list` | `posting_topic_review.html` | List of preview posts |
| `.forge-topic-review-back` | `posting_topic_review.html` | Bottom "back to top" link |

---

## Jumpbox

| Class | Where | Purpose |
|---|---|---|
| `.forge-jumpbox` | jumpbox, viewforum, viewtopic | Wrapper for the dropdown |
| `.forge-jumpbox-inline` | viewforum, viewtopic | Inline variant (in the bottom bar) |
| `.forge-jumpbox-trigger` | all | The clickable label |
| `.forge-jumpbox-dropdown` | all | The dropdown panel |
| `.forge-jumpbox-menu` | all | The `<ul>` of forums |
| `.forge-jumpbox-item` | all | One `<li>` |
| `.forge-jumpbox-link` | all | Forum link inside item |
| `.forge-jumpbox-return` | all | "Return to Board Index" line |
| `.forge-jumpbar` | `jumpbox.html` | Container for the legacy markup |

---

## MCP custom (mcp_topic override)

| Class | Where | Purpose |
|---|---|---|
| `.forge-tabs-container` | `mcp_topic.html` | Tab+title container with flex layout |
| `.forge-mcp-form` | `mcp_topic.html` | Form wrapper |
| `.forge-mcp-panel` (-options, -review) | `mcp_topic.html` | Panel section |
| `.forge-mcp-fieldset` | `mcp_topic.html` | A single fieldset |
| `.forge-mcp-review-head` | `mcp_topic.html` | Title bar of the review panel |
| `.forge-mcp-review-title` | `mcp_topic.html` | "Topic review: ..." text |
| `.forge-mcp-review-toggle` | `mcp_topic.html` | Expand view link |
| `.forge-mcp-topicreview` | `mcp_topic.html` | List of posts |
| `.forge-mcp-post` | `mcp_topic.html` | One post |
| `.forge-mcp-postbody` | `mcp_topic.html` | Post body (full width, no profile column) |
| `.forge-mcp-post-actions` | `mcp_topic.html` | Info + Select checkbox cluster |
| `.forge-mcp-post-author` | `mcp_topic.html` | Author meta line |
| `.forge-mcp-post-content` | `mcp_topic.html` | Post text |
| `.forge-mcp-actionbar` | `mcp_topic.html` | Bottom pagination bar |
| `.forge-mcp-pagination` | `mcp_topic.html` | Pagination links |
| `.forge-mcp-display-actions` | `mcp_topic.html` | Bottom select-action row |
| `.forge-mcp-mark-actions` | `mcp_topic.html` | "Mark all / Unmark all" links |
| `.forge-mcp-select-cell` | `mcp_topic.html` | Select checkbox container |
| `.forge-mcp-empty` | `mcp_topic.html` | Empty state when no posts |

---

## UCP custom

| Class | Where | Purpose |
|---|---|---|
| `.forge-ucp-groups` | `ucp_groups_membership.html` | Form wrapper |
| `.forge-groups-list` | `ucp_groups_membership.html` | Group list `<ul>` |
| `.forge-groups-mark` | `ucp_groups_membership.html` | Select-radio cell |
| `.forge-ucp-subscribed` | `ucp_main_subscribed.html` | Subscribed forums/topics page |
| `.forge-watch-head`, `-head-forums`, `-head-topics` | `ucp_main_subscribed.html` | Section headers |
| `.forge-watch-list`, `-list-forums`, `-list-topics` | `ucp_main_subscribed.html` | Item lists |
| `.forge-watch-mark`, `.forge-watch-mark-head` | `ucp_main_subscribed.html` | Checkbox cells |

---

## FAQ

| Class | Where | Purpose |
|---|---|---|
| `.forge-faq-top` | `faq_body.html` | Hero section (title + index of questions) |
| `.forge-faq-header` | `faq_body.html` | Header inside hero |
| `.forge-faq-grid` | `faq_body.html` | Grid of question cards |
| `.forge-faq-section`, `-section-head` | `faq_body.html` | One section |
| `.forge-faq-item` | `faq_body.html` | A single Q&A |
| `.forge-faq-answer` | `faq_body.html` | The answer text |
| `.forge-faq-index`, `-index-card` | `faq_body.html` | Sticky index of FAQ sections |

---

## Footer

| Class | Where | Purpose |
|---|---|---|
| `.forge-footer` | `overall_footer.html` | Outer footer container |
| `.forge-footer-nav` | `overall_footer.html` | Top row (links) |
| `.forge-footer-meta` | `overall_footer.html` | Bottom row (copyright, version) |
| `.forge-footer-breadcrumbs` | `navbar_footer.html` | Breadcrumbs in the footer nav |
| `.forge-footer-crumb`, `-crumb-link` | `navbar_footer.html` | Single crumb |

---

## Stats blocks

| Class | Where | Purpose |
|---|---|---|
| `.forge-stats-grid` | `index_body.html` | Three-up cards (Who is online / Birthdays / Statistics) |
| `.forge-check` | `index_body.html`, `viewforum_body.html` | Custom checkbox styled chip |

---

## Buttons & toolbars

| Class | Where | Purpose |
|---|---|---|
| `.forge-primary-button` | `viewforum_body.html` | Sky-blue CTA modifier on `.button` |
| `.button.is-primary` | (any) | Same as above (preferred — design system) |
| `.button.is-danger` / `.forge-danger-button` | (any) | Red destructive modifier |
| `.button.is-small` / `.button.button-small` | (any) | Compact button |
| `.button.button-icon-only` | (any) | Square button, only icon |

---

## Empty states

| Class | Where | Purpose |
|---|---|---|
| `.forge-empty` | `forumlist_body.html`, `viewforum_body.html` | Modifier on `.panel` for "no forums / no topics" |
| `.forge-empty-state` | (any) | Generic empty state with illustration |

The `::before` and `::after` pseudo-elements render a soft circle + an SVG icon
(`empty_inbox.svg`, `empty_search.svg`, `empty_check.svg`, `empty_bell.svg`).
Variant via `.forgeboard.section-search`, `.forgeboard.section-mcp`,
`.forgeboard #notification_list .no_notifications`.

---

## Theme toggle (JavaScript API)

The script `forge_theme_toggle.js` exposes:

```js
ForgeTheme.set('dark' | 'light' | 'auto')
ForgeTheme.get()        // returns current preference
ForgeTheme.resolved()   // returns 'dark' or 'light' after auto-resolution
```

Stored as `forgeboard_theme` cookie (1 year) AND `localStorage` key.

---

## Conventions

- **Naming**: `forge-{feature}-{element}-{modifier?}` (kebab-case).
- **No `!important`**: avoided unless overriding a Prosilver `!important` (rare).
- **Specificity ceiling**: target ≤ (0,5,2). Rules above that emit a Stylelint warning.
- **Theme switching**: never hardcode hex; always use `var(--gb-...)`.
- **Spacing**: prefer `var(--gb-space-N)` over raw px on a 4 px grid.
- **Radius**: `--gb-radius-sm` (4) / `-md` (6) / `-lg` (12). No 999px on buttons.
- **No emojis** in CSS `content`; use inline SVG via `mask-image` with `currentColor`.

---

_Generated 2026-05-02 (style version 1.5.0). Run `python theme/_inventory_forge.py`
to regenerate the raw inventory if templates change._
