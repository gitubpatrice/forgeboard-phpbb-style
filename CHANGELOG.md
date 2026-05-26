# Changelog

All notable changes to ForgeBoard are documented here.

## [1.5.1] — 2026-05-26

### Added
- Template override `template/memberlist_view.html` introducing a `.forge-viewprofile-head` wrapper that drives the avatar/details layout via CSS Grid (200px + 1fr) instead of the legacy prosilver float stack
- Spacing under the avatar (`margin: 0 0 14px`) and between rank lines (`margin: 0 0 10px`); rank title and rank image now left-aligned under the avatar
- `max-width: 100%` clamp on rank images so an oversized rank graphic no longer overflows the avatar column

### Fixed
- Profile-details `<dt>` labels (Username, Groups, …) rendered one character per line on narrow panels. Root cause: prosilver's `dl.details dt { width: 30% }` was still applied inside the grid container. The `.forgeboard.section-memberlist #viewprofile .left-box.details.profile-details` rule now resets `width: auto` and `max-width: 100%` on dt/dd, plus a dedicated dt rule with `text-align: left` and `white-space: nowrap` to keep labels on a single line

### Changed
- `style_version` bumped to 1.0.2
- `theme/stylesheet.css` bumped `forgeboard.css?hash=…` to force browser cache refresh

## [1.5.0] — 2026-05-02

### Added
- **Theme toggle** (light / dark / auto) with cookie + localStorage persistence
- Inline `<head>` bootstrap to prevent flash-of-unstyled-content (FOUC)
- **Empty states** with illustration + soft surface (NO_TOPICS, NO_FORUMS, NO_NOTIFICATIONS, etc.)
- **18 BBCode toolbar SVG icons** (bold, italic, underline, strike, quote, code, url, img, list, color, size, smiley, attach, eraser, preview, undo, redo)
- **23 SVG smileys** (clean, monochrome on yellow base, original designs)
- `print.css` — paper-friendly stylesheet (hides chrome, black/white text, page-break rules)
- `LICENSE` (GPL-2.0-or-later)
- `CHANGELOG.md`

### Changed
- Removed Open Sans Google Font loader (saved ~590 KB on first paint, theme uses system fonts via `--gb-font-sans`)
- Added `<link rel="preconnect">` for FontAwesome CDN
- Dark theme triggers via `[data-theme="dark"]` attribute (set by toggle JS) AND falls back to `@media (prefers-color-scheme: dark)` when no preference is stored

### Removed
- The Open Sans web-font dependency (replaced by system stack)

## [1.4.0] — 2026-05-02

### Added
- 39 custom SVG icons for the Prosilver-equivalent imageset (forum / topic / sticky / announce + variants)
- Dedup script (`theme/_dedup.py`) for forgeboard.css
- Stylelint config + VS Code workspace settings + recommended extensions

### Changed
- Imageset CSS overrides scoped strictly to `dl.row-item` (legacy Prosilver markup) so ForgeBoard's custom cards aren't affected
- 4161 / 3798 lines reformatted by Stylelint --fix (consistent indentation, color-hex case, value-keyword case)
- 5 real CSS bugs fixed (border/padding shorthand-after-longhand, empty block)
- 18 dedup merges (15 @media block consolidations + 1 top-level + 2 inside @media)

### Fixed
- Notification dropdown positioning (`.dropdown-contents` was absolutely-positioned by Prosilver, now anchored to bell trigger right edge)
- MCP topic_view: `.postbody` collapsed grid to single column (no more wasted profile column)
- viewforum: replies/views/lastpost columns aligned with category labels
- Topbar stacking at narrow widths (single column ≤ 1100 px)
- Various responsive issues (jumpbox, hero action, breadcrumbs, cp-menu)

## [1.3.0] — 2026-05-02

### Added
- 3-level button system: default / `.is-primary` (sky blue) / `.is-danger` (red)
- GitHub-style form inputs (subtle inset shadow + 3 px blue focus ring + accent-color)
- BBCode `[quote]` styled with left border accent (no fill)
- BBCode `[code]` styled with header bar + monospace body, inline code chip
- UCP/MCP sidebar as rail nav with filled active state + 3 px blue stripe
- Override of `mcp_topic.html` with custom `.forge-mcp-*` class hooks
- ForgeBoard layout fixes for floats lost when bulk-removing `!important`

### Changed
- Primary button color from green to sky blue
- Header user nav (avatar / PM / notifications): no chip hover, color shift only
- Breadcrumbs in nav card: plain text style, no shift on hover

### Removed
- `forge_dropdown_reset.js` (was force-closing all dropdowns aggressively, broke standard phpBB UX)

## [1.2.0] — 2026-05-02

### Added
- Typography tokens (`--gb-font-*`, `--gb-leading-*`, `--gb-weight-*`)
- Spacing tokens on a 4 px grid (`--gb-space-1..12`)
- Radius tokens (`--gb-radius-sm/md/lg`, max 9 px on buttons — never pill)
- Counter badges as subtle rounded chips (gray muted at 0, danger red when unread)

### Changed
- Base font size 11 px → 14 px (much more readable)
- All `border-radius` values normalized to 0 / 6 / 12 px
- Avatars: rounded squares (6 px), not circles

## [1.1.0] — 2026-05-02

### Added
- 11 missing `<!-- EVENT -->` placeholders restored in `forumlist_body.html`, `viewforum_body.html`, `overall_header.html` (extension compatibility)

### Changed
- Bulk-removed all 721 `!important` from `forgeboard.css`
- Deduplicated 108 occurrences of 62 selectors
- 53 commented-out CSS blocks removed (dead code)

### Removed
- `theme/colours.css` (4 useful lines, merged into `forgeboard.css`)
- `template/forge_viewforum_bottom_patch.js` (redundant with the template that already has the link)

## [1.0.0] — 2026-04 (initial)

- First release. Modern code-forge inspired phpBB style based on Prosilver.
