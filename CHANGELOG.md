# Changelog

All notable changes to ForgeBoard are documented here.
Versions match `style.cfg` `style_version`.

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
