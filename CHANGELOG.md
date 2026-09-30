# Changelog

All notable changes to ForgeBoard are documented here.
Versions match `style.cfg` `style_version`.

## [Unreleased]

For the next submission. None of this is in the 1.2.4 archive.

### Changed
- **X icon replaces the Twitter bird in the mini-profile contact dropdown**, following prosilver 3.3.18 (PHPBB-17623). The FontAwesome build phpBB ships (4.7) has no X glyph, so `\f099` could only ever draw the bird. The logo is now `theme/images/contact_x.svg` (Simple Icons path, CC0 1.0), applied as a CSS mask and painted with `--gb-link` / `--gb-link-hover` like the glyphs beside it. It therefore follows the light and dark themes with no extra token. Checked in both themes against the Facebook and YouTube glyphs: same colour, matching size.
- `theme/stylesheet.css`: `forgeboard.css` cache-buster hash refreshed.

### Added
- `@media (forced-colors: active)` rule for the X icon only. Forced colours repaint `background-color`, which would erase a mask-drawn icon, while the font glyphs are repainted as text and stay visible. The icon is drawn in `LinkText` there. Not yet checked in a real forced-colours session.

## [1.2.4] — 2026-09-25

Compatibility release for phpBB 3.3.19.

### Changed
- `phpbb_version` set to 3.3.19; footer credit updated to 1.2.4.

### Added
- `template/mcp_topic.html`: `{% EVENT mcp_topic_postrow_post_after %}`, new in prosilver 3.3.18.
- `theme/en/` and `theme/fr/icon_user_online.gif` (prosilver's GIF), and an empty `theme/images/index.htm`.

### Deliberately unchanged
- `message_body.html` is not overridden, so the 3.3.19 return link (`RETURN_LINK`) comes from prosilver.

## [1.2.3] — 2026-07-29

Found while testing a real attachment upload; 1.2.2 had already been submitted,
so this replaces it in the queue. CSS only — no template, event or asset
touched. See `docs/phpbb-validation-response-1.2.3.md`.

### Fixed
- **Literal colours inherited from prosilver's `colours.css`.** ForgeBoard `@import`s prosilver's whole stylesheet chain, so every hardcoded colour there shows through on any element the style does not restyle. Written for a light board, they break the dark theme — the symptom was `.attachbox { background-color: #FFFFFF }`, a glaring white panel on a dark post. An audit for that exact pattern (a literal colour on a selector ForgeBoard never restyles) found **28 leaking rules**; the **20** that actually break in dark mode are now expressed in tokens: the attachment box and its captions, thumbnails, the UCP avatar gallery, `ul.forums`, `.jumpbox-sub-link`, the dropdown caret, `.current` (which needs `!important` to beat prosilver's own `color: #000000 !important`) and the reported/disapproved notification labels.
- **Attachments tab label off-centre.** `posting_editor.html` puts `<strong class="file-total-progress">` inside the tab link. prosilver lays it out as a `display:block` element with negative margins calibrated for a `display:block` anchor padded `5px 9px`; ForgeBoard renders that anchor as an `inline-flex` row with a `gap`, so the bar became a second flex item beside the label and shoved the text sideways. It is now absolutely positioned along the bottom edge of the tab, inset by the corner radius. The anchor is already `position: relative` from prosilver's `cp.css`.
- Attachment box padding raised from prosilver's `6px` to `var(--gb-space-3)`: `6px` was written for square corners and let the label run under the corner arc once the radius was applied.

### Added
- Tokens `--gb-attachbox-bg` / `--gb-attachbox-border`, declared in all three token blocks (`:root`, `[data-theme="dark"]`, and the `prefers-color-scheme` fallback for visitors with JavaScript disabled): `#f7f9fb` / `#7d8ea6` light, `#181c23` / `#5d6d88` dark. The fill deliberately sits close to the post surface in both themes (1.06:1 light, 1.01:1 dark), so the border alone delimits the block — which makes it a meaningful UI boundary, hence both borders clear 3:1 under WCAG 1.4.11 (3.16:1 light, 3.26:1 dark).

### Changed
- Attachment box radius uses `var(--gb-radius-lg)` instead of a loose value.
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.2.3

### Deliberately unchanged
- Eight prosilver colour leaks remain: the five PM colour flags (semantic markers, and side borders rather than fills), `.darken` and `.loading_indicator` (black overlays intended to be black in both themes), and `.message-box textarea`, where ForgeBoard's own rule already wins on source order at equal specificity.

## [1.2.2] — 2026-07-29

Answers the phpBB.com Styles Team review (_Vinny_).

### Added
- **`theme/plupload.css` — attachment upload status.** `overall_header.html` links this file directly from `{T_THEME_PATH}`, so it is *not* inherited from prosilver: ForgeBoard never shipped one, the `<link>` 404'd, and the whole attachment panel lost its styling — including the STATUS column, which stayed blank. The file now carries the panel layout rules plus the three upload states, drawn with Font Awesome and ForgeBoard tokens instead of prosilver's fixed-colour GIFs, so they stay readable on both surfaces: working (spinner, `--gb-text-muted`), uploaded (check, `--gb-success-fg`), error (cross, `--gb-danger`). The spinner honours `prefers-reduced-motion`. Progress bars use `--gb-link` on a `--gb-surface-muted` track (4.08:1 light / 4.83:1 dark).

- **`theme/tweaks.css`.** Third and last file linked from `{T_THEME_PATH}` without a local copy (IE ≤ 9 conditional comment in both headers). Mirrors prosilver's, so every `{T_THEME_PATH}` link in the style now resolves.

### Fixed
- **MCP list header contrast.** The `li.header` band of the moderation queue and the reports list hardcoded `rgba(22, 27, 34, 0.72)` — a dark-theme value applied in both themes. In light mode the labels rendered dark-on-dark and only the red "Mark" was legible. Both rules now use the `--gb-block-header-bg` / `--gb-block-header-fg` pair already used by every other block header (11.28:1 light, 15.80:1 dark), and the `dt`/`dd`/`dd.mark` cells inherit that colour instead of pinning `--gb-text` / `--gb-danger` onto a surface that shifts under them.
- **Black checkboxes on the light theme.** `:root` declared `color-scheme: light dark` and never updated it, so the UA painted native widgets (checkboxes, radios, selects, scrollbars) from the OS preference. A visitor on an OS in dark mode who pinned ForgeBoard's light theme got black checkboxes on a light page — visible on the MCP moderation queue's Mark column. `color-scheme` now flips in step with the dark tokens, in all three blocks (`:root`, `[data-theme="dark"]`, and the `prefers-color-scheme` fallback).
- **Poll option captions invisible in light mode.** `fieldset.polls dl` set `color: #FAFAFA` unconditionally, so the option caption and the percentage — which sit on the panel surface, not on the bar — were near-white on white. The light foreground is now scoped to `dd.resultbar div`, the only element actually on the coloured bar.
- **Reported-row highlight.** `li.row.reported:hover` / `:focus-within` forced a fixed dark red `#9c4d48` in both themes; on the light theme the row's own text fell to 1.16:1. Now `--gb-red-soft` with the red identity carried by the `--gb-danger` border and stripe (6.19:1 for row text, 5.55:1 for the accent). Affects the reported rows in the MCP and in the topic lists.
- **UCP `dl.mini` labels.** `#7eafff` — a dark-theme blue — sat at 2.22:1 on the light surface. `dl.mini` comes from prosilver's `ucp_header.html`, which ForgeBoard does not override, so it renders in both themes; now `--gb-link` (4.63:1 / 6.85:1).
- **Poll row alignment.** Prosilver lays each poll option out with floats, so the caption and the percentage sat at the top of their boxes while the bar sat lower by its own padding. The row is now a centred flex line, so the three columns share one axis whatever the bar's height; `float` is neutralised on `dt`/`dd`, with the matching override in `bidi.css` (which loads after `stylesheet.css` and would otherwise re-float them under RTL).
- **Poll option hierarchy on tokens.** The inherited prosilver pair (`dl` `#666`, `dl.voted` `#000`) only works on a light surface — `#666` falls to 3.01:1 on ForgeBoard's dark panel. Non-voted options now use `--gb-text-muted` and the voted one `--gb-text`, keeping prosilver's "voted stands out" hierarchy in both themes (5.63:1 / 6.84:1 light, 8.61:1 / 17.30:1 dark).
- **Poll bars unified.** Only `.pollbar1` and `.pollbar5` had been recoloured, leaving bars 2–4 on prosilver's red ramp; white vote counts on `.pollbar4` / `.pollbar5` sat at 4.63:1 / 4.03:1. All five now form one flat blue ramp, every step ≥5:1 with the white count, with the matching RTL left-border overrides in `bidi.css`.

### Changed
- `license.txt` now contains the verbatim GPL-2.0 text instead of a pointer to it.
- Removed an empty `.forge-nav-user-card a` rule.
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.2.2

## [1.2.1] — 2026-07-10

### Changed
- **Locked-topic cues in red.** The reply button on a locked topic (viewtopic) now uses a solid red fill + red border (`.forge-button-locked`) so it is obvious the topic is closed. In the topic list (viewforum), a locked topic's icon tile now gets a red border and a red padlock (`.forge-topic-icon-locked`), matching the closed state.

### Changed
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.2.1

## [1.2.0] — 2026-07-10

### Added
- **Full RTL (right-to-left) support.** ForgeBoard previously shipped no `bidi.css`, so the conditional `<link href="{T_THEME_PATH}/bidi.css">` in the headers 404'd and RTL boards got no mirroring at all. Added `theme/bidi.css`, loaded only when the board language is RTL (zero impact on the default LTR rendering):
  - Part 1 imports prosilver's `bidi.css`, restoring the full inherited base (breadcrumbs, forms, dropdowns, mini-profile, pagination…).
  - Part 2 mirrors the physical (left/right) properties of ForgeBoard's own `.forge-*` cards: hero/card accent bars, last-post block + jump arrow, forum icon gutters, topbar brand/search, nav split cards, all `margin:auto` push helpers, hover accent stripes, MCP layouts, member-profile alignment, skip link, and the viewtopic mini-profile shape. Flex/grid axes flip natively under `dir="rtl"`.
- Verified by rendering the RTL forum index, viewforum and viewtopic (cards, hero bars, mini-profile split all mirror correctly).

### Changed
- `style_version` bumped to 1.2.0

## [1.1.9] — 2026-07-10

### Fixed
- Light-mode contrast hardening (follow-up to the Styles Team review): `--gb-danger` darkened `#c83e4d → #bd2130` so red text (kickers, flags, labels) meets WCAG AA (≥4.5:1) on the light canvas; `--gb-text-muted` darkened `#607080 → #5a6979` so small secondary labels also reach AA without losing hierarchy.
- Restored `{LAST_VISIT_DATE}` on the index hero for logged-in users (parity with prosilver; it was the only content variable missing after the redesign).

### Changed
- `theme/stylesheet.css` cache-buster hash refreshed
- `style_version` bumped to 1.1.9

## [1.1.8] — 2026-07-10

### Fixed — phpBB Styles Team validation feedback
- Block headers now contrast with the block body in light mode (dedicated `--gb-block-header-bg` / `--gb-block-header-fg` tokens on `.forumbg`/`.forabg` headers and table `thead th`).
- Removed the decorative "{SITENAME}" placeholder cards; the forum grid flows with `repeat(auto-fit, minmax(280px, 1fr))`.
- Locked forums now show a lock icon (`S_LOCKED_FORUM` branch in the forum card).
- Admin topic icons are rendered (`TOPIC_ICON_IMG` under `S_TOPIC_ICONS`) in the topic card.
- Locked topics now show a lock icon (`S_TOPIC_LOCKED` branch).
- PM folder icons use ForgeBoard's own SVGs instead of prosilver's GIFs (`dl.row-item.pm_read` / `.pm_unread`).
- Mini-profile contact icons rendered with the style's own FontAwesome glyphs instead of prosilver's `icons_contact.png` sprite (legible in light and dark).
- Stylesheet header comment corrected from 3.3.16 to 3.3.17.
- Added an `@media (prefers-color-scheme: dark)` fallback so dark mode works with JavaScript disabled (respects an explicit light choice).

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
