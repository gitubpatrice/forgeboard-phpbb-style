# Presentation post for "Styles in Development" forum

This is the BBCode-formatted post to copy-paste at:
https://www.phpbb.com/community/viewforum.php?f=691

---

## Suggested thread title

```
[RC1] ForgeBoard 1.5.0 - modern code-forge style for phpBB 3.3
```

(phpBB conventions for the prefix: `[Dev]` for early in-development, `[Alpha]`, `[Beta]`, `[RC1]`/`[RC2]` for release candidates, then no prefix once the style is in the Customisations DB. RC1 fits because the style is feature-complete and being tested.)

---

## First post (BBCode)

```bbcode
[size=150][b]ForgeBoard 1.5.0 - Release Candidate 1[/b][/size]
A modern, code-forge inspired style for phpBB 3.3, built on top of Prosilver.

[size=120][b]Pitch[/b][/size]
ForgeBoard takes design cues from modern developer-tooling UIs: clean typography on a system-font stack, generous whitespace, sharp components, light AND dark themes with an explicit toggle, and a print-friendly stylesheet. It targets phpBB 3.3.x and inherits 100% of Prosilver's structure (no core changes, all extension events preserved).

[size=120][b]Key features[/b][/size]
[list]
[*][b]Light & dark themes[/b] with a 3-state toggle (light / dark / auto-from-OS) - persisted via cookie + localStorage, no flash-of-unstyled-content
[*][b]Custom SVG imageset[/b] - 39 status icons (forum, topic, sticky, announce, locked, mine, hot variants) in monochrome SVG using currentColor
[*][b]System font stack[/b] - no Google Fonts download, saving ~590 KB on first paint
[*][b]Print stylesheet[/b] - paper-friendly, hides chrome, page-break-aware
[*][b]Responsive[/b] - 5 breakpoints (1100 / 980 / 900 / 760 / 510 / 480 px)
[*][b]GitHub-inspired components[/b]: 3-level button system, focus rings, quote blocks with left accent, code blocks with mono header bar, UCP/MCP sidebar as a rail nav
[*][b]Theme tokens[/b] in :root - 80+ CSS custom properties for colors, spacing, radii, typography, weights
[*][b]Accessibility[/b] - skip link, aria-expanded sync on dropdowns, prefers-reduced-motion, modal focus trap, sr-only utility, no positive tabindex, ARIA-correct landmarks
[*][b]Original SVG smiley pack[/b] (23 expressions, optional)
[*][b]MCP topic_view template overridden[/b] with clean .forge-mcp-* class hooks
[/list]

[size=120][b]Screenshots[/b][/size]
[Light mode index]
[Light mode viewtopic]
[Dark mode index]
[Dark mode viewtopic]
[Mobile 375px]

(Replace with actual [img] tags pointing to imgur or your demo host. Save the screenshots first, host them, then paste the URLs.)

[size=120][b]Demo[/b][/size]
[url=YOUR_DEMO_URL]Live demo[/url] (anonymous / visitor mode)

(Add your demo URL here.)

[size=120][b]Source code[/b][/size]
[url=https://github.com/gitubpatrice/forgeboard-phpbb-style]github.com/gitubpatrice/forgeboard-phpbb-style[/url]

[size=120][b]Requirements[/b][/size]
[list]
[*]phpBB 3.3.x (tested on 3.3.16)
[*]Prosilver style installed (parent style)
[*]Modern browser - Chrome 90+, Firefox 81+, Safari 14+, Edge 90+
[*]CSS features used: :has(), color-mix(), container queries, clamp(), [data-theme] attribute
[/list]

[size=120][b]License[/b][/size]
GPL-2.0-or-later. Free to use, modify, redistribute under the terms of the GNU GPL v2 (or any later version).

[size=120][b]What I would like feedback on[/b][/size]
[list]
[*][b]Visual consistency[/b] across pages I haven't explicitly customised (memberlist, search results, login/register, UCP sections)
[*][b]Compatibility[/b] with popular extensions - if you have an extension installed, please report rendering issues
[*][b]Accessibility[/b] - the static audit found 0 blockers but the browser tests (NVDA, VoiceOver, Lighthouse a11y) need real users. Please report any keyboard or screen-reader friction
[*][b]Dark mode[/b] - color contrast, eye fatigue, anything that feels off
[*][b]Print[/b] - I added a print.css; let me know if a Ctrl+P preview looks broken on a specific page
[*][b]Browser fallback[/b] - the style uses some recent CSS (color-mix, :has) - if you're on an older browser and something looks wrong, please tell me which browser/version
[/list]

[size=120][b]Known limitations / not yet done[/b][/size]
[list]
[*]ACP appearance - not customised; admin panel uses inherited Prosilver
[*]SVG smiley set ships in /theme/images/smilies/ but is NOT auto-imported into the smiley table; use the default phpBB smileys for now
[*]Specificity warnings - the CSS still has high-specificity selectors (technical debt). Refactor planned for v2 (won't change visuals)
[*]CSS file size - ~8 KLOC; deduplicated and Stylelint-clean but a v2 component refactor would shrink it
[/list]

[size=120][b]Changelog (1.0 -> 1.5)[/b][/size]
See [url=https://github.com/gitubpatrice/forgeboard-phpbb-style/blob/main/CHANGELOG.md]CHANGELOG.md[/url] in the repo.

[size=120][b]How to install for testing[/b][/size]
[list=1]
[*]Download the ZIP from GitHub
[*]Extract /styles/ForgeBoard/ to your phpBB styles/ directory
[*]ACP -> Customise -> Styles -> install ForgeBoard
[*]Purge the phpBB cache (ACP -> General -> Server load -> purge cache)
[*]Set ForgeBoard as the default style
[/list]

Thanks in advance for any feedback!

[i]ForgeBoard is free software. Bug reports, suggestions and pull requests are welcome on GitHub.[/i]
```

---

## What you need to gather BEFORE posting

1. **5 screenshots** (PNG, ~1200x800 or similar):
   - Index light mode
   - Index dark mode
   - viewtopic with a post containing quote + code
   - viewforum
   - Mobile width (375px) - any of the above

   Host them on imgur, ImgBB, your own server, or as GitHub repo assets, then replace `[Light mode index]` etc. with `[img]URL_TO_IMAGE[/img]`.

2. **Demo URL** to your installed forum where visitors (logged out) can browse. Replace `YOUR_DEMO_URL` in the post.

3. **Final commit + push** of the latest local changes (notification dropdown empty state, See All hover, etc.) — let me know when you want me to do this.

---

## Forum etiquette tips for this submission

- **Do not bump** the thread unless you have a real update (new RC, fixed bug). Bumping just to ask for feedback is frowned upon.
- **Reply to feedback** politely, even if you disagree. Reviewers there are volunteers.
- **Update the OP** when you push a new RC; don't post a fresh thread.
- **Tag the version** in the title `[RC1]` -> `[RC2]` -> remove prefix once you submit to the Customisations DB.
- **License** must be visible (you have it) and the style must NOT modify phpBB core (you don't).
- **Original work** - your style must be your own creation. Don't lift assets from other styles. (You're clean on this.)
- **No spam links** in the post. Demo + repo + screenshots is fine.

---

## Suggested next steps before you post

1. Take the 5 screenshots
2. Host them
3. Replace placeholders in the BBCode above
4. Add demo URL
5. Final commit + push (the in-flight changes from today)
6. Bump style_version to 1.5.0-RC1 in style.cfg if you want to be explicit
7. Post on https://www.phpbb.com/community/viewforum.php?f=691
