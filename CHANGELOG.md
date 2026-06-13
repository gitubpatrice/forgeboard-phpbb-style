# Changelog

All notable changes to ForgeBoard are documented here.
Versions match `style.cfg` `style_version`.

## [1.1.6] — 2026-06-13

### Fixed
- User navbar (logged in): the responsive overflow toggle ("...") no longer appears on portrait phones. Every user-nav item (profile / private messages / notifications) is now flagged `data-skip-responsive`, so `forum_fn.js` has nothing to collapse — but it still rendered the toggle empty once the row wrapped (~461px). The empty toggle is now hidden, scoped to `#nav-user > .responsive-menu` so the `#nav-main` quick-links hamburger is untouched.

### Changed
- `template/navbar_header.html`: `data-skip-responsive="true"` added to the private-messages `<li>` (consistent with profile and notifications)
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.1.6

## [1.1.5] — 2026-06-12

### Fixed
- Mobile navbar: the quick-links responsive toggle (the "three bars" hamburger) now appears on phones again — removed an erroneous `display:none` on `li.responsive-menu.dropdown-container` below 480px
- viewforum top toolbar (`bar-top`): below 760px the forum-search no longer drops onto its own line — it stays inline to the right of the "New Topic" button, with only the pagination wrapping underneath (bottom bar untouched)
- viewforum top toolbar: on portrait phones (≤480px) the inline forum-search is capped to 165px and right-aligned so it no longer stretches across the row

### Changed
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.1.5

## [1.1.4] — 2026-06-11

### Changed
- Extended the topic-tools accent-stripe hover to the quickmod dropdown links (same stripe, no fill, rounded 5px)
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.1.4

## [1.1.3] — 2026-06-11

### Added
- Topic-tools dropdown links hover: the same quick-links accent stripe (rounded 5px corners), with no background fill on the link or its icon

### Changed
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.1.3

## [1.1.2] — 2026-06-11

### Added
- Jumpbox links hover: a 3px left accent stripe mirroring the quick-links hover — blue (`--gb-link`) with a subtle inset outline for forum/sub links, red (`--gb-danger`) stripe only for category headers

### Changed
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.1.2

## [1.1.1] — 2026-06-11

### Changed
- Localised the remaining ARIA landmark labels (primary navigation, footer, MCP quick actions, MCP sections) through `theme/<lang>/style_lang.twig` instead of hardcoded English — added `NAV_PRIMARY_LABEL`, `NAV_FOOTER_LABEL`, `MCP_QUICK_ACTIONS_LABEL`, `MCP_SECTIONS_LABEL` (EN + FR)
- `style_version` bumped to 1.1.1

## [1.1.0] — 2026-06-11

### Fixed
- viewtopic top action bar now matches the bottom bar: reply + topic-tools are wrapped in a `.forge-bottom-left` group so they sit together on the left. Previously the bar's `space-between` spread the reply, the topic-tools dropdown and the pagination apart. Pagination stays a sibling, pushed to the right
- `.cp-main` width set to 80% with a 10px left margin
- Responsive menu trigger hidden below 480px

### Changed
- `LICENSE` renamed to `licence`
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.1.0

## [1.0.0] — 2026-04

First public release — a modern, code-forge inspired phpBB style based on Prosilver.

### Highlights
- Light / dark / auto theme toggle with cookie + localStorage persistence and a FOUC-preventing `<head>` bootstrap
- System-font typography (no web-font dependency), a 4px spacing scale and radius/colour design tokens
- Three-level button system, GitHub-style form inputs, styled `[quote]` / `[code]` BBCode and rail-style UCP/MCP navigation
- Custom SVG imageset (forum / topic icons), 18 BBCode toolbar icons and 23 SVG smileys
- `print.css`, illustrated empty states, responsive layout and restored `<!-- EVENT -->` placeholders for extension compatibility
