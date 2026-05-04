# ForgeBoard 1.0.0 [RC1] — final post for phpbb.com

## Thread title (copy/paste in the title field)

```
[RC1] ForgeBoard 1.0.0 - modern code-forge style for phpBB 3.3
```

---

## Forum: Styles in Development
URL: https://www.phpbb.com/community/viewforum.php?f=691

---

## First post BBCode (copy/paste — only thing left to fill: YOUR_DEMO_URL)

```bbcode
[size=150][b]ForgeBoard 1.0.0 - Release Candidate 1[/b][/size]
A modern, code-forge inspired style for phpBB 3.3, built on top of Prosilver.

[size=120][b]Pitch[/b][/size]
ForgeBoard takes design cues from modern developer-tooling UIs: clean typography on a system-font stack, generous whitespace, sharp components, light AND dark themes with an explicit toggle, and a print-friendly stylesheet. It targets phpBB 3.3.x and inherits 100% of Prosilver's structure (no core changes, all extension events preserved).

[size=120][b]Key features[/b][/size]
[list]
[*][b]Light & dark themes[/b] with a 3-state toggle (light / dark / auto-from-OS) - persisted via cookie + localStorage, no flash-of-unstyled-content
[*][b]Custom SVG imageset[/b] - 39 status icons (forum, topic, sticky, announce, locked, mine, hot variants) in monochrome SVG using currentColor
[*][b]System font stack[/b] - no Google Fonts download, saving ~590 KB on first paint
[*][b]Print stylesheet[/b] - paper-friendly, hides chrome, page-break-aware
[*][b]Responsive[/b] - 6 breakpoints (1100 / 980 / 900 / 760 / 510 / 480 px)
[*][b]GitHub-inspired components[/b]: 3-level button system, focus rings, quote blocks with left accent, code blocks with mono header bar, UCP/MCP sidebar as a rail nav
[*][b]Theme tokens[/b] in :root - 80+ CSS custom properties for colors, spacing, radii, typography, weights
[*][b]Accessibility[/b] - skip link, aria-expanded sync on dropdowns, prefers-reduced-motion, modal focus trap, sr-only utility, no positive tabindex, ARIA-correct landmarks
[*][b]Original SVG smiley pack[/b] (23 expressions, optional)
[*][b]MCP topic_view template overridden[/b] with clean .forge-mcp-* class hooks
[/list]

[size=120][b]Screenshots[/b][/size]

[b]Index - light[/b]
[img]https://zupimages.net/up/26/19/ppl9.jpg[/img]

[b]Index - dark[/b]
[img]https://zupimages.net/up/26/19/a4qx.jpg[/img]

[b]Forum view - light[/b]
[img]https://zupimages.net/up/26/19/f5j0.jpg[/img]

[b]Forum view - dark[/b]
[img]https://zupimages.net/up/26/19/5625.jpg[/img]

[b]Topic view - light[/b]
[img]https://zupimages.net/up/26/19/nedc.jpg[/img]

[b]Topic view - dark[/b]
[img]https://zupimages.net/up/26/19/9b99.jpg[/img]

[b]MCP - light[/b]
[img]https://zupimages.net/up/26/19/8c3f.jpg[/img]

[b]MCP - dark[/b]
[img]https://zupimages.net/up/26/19/d778.jpg[/img]

[b]FAQ - dark[/b]
[img]https://zupimages.net/up/26/19/5qz7.jpg[/img]

[size=120][b]Demo[/b][/size]
[url=YOUR_DEMO_URL]Live demo[/url] (anonymous / visitor mode - no account needed to browse)

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
[*]A v2 component refactor of the CSS is planned (no visual change, only internal organisation)
[/list]

[size=120][b]Changelog[/b][/size]
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

## Last thing to do before posting

**Replace `YOUR_DEMO_URL`** with the URL of your live demo (the forum where ForgeBoard is already deployed and visitors can browse anonymously).

Example replacement:
```
[url=https://forum.styles-design.fr]Live demo[/url]
```

---

## Reminder — phpBB forum etiquette

- Do NOT bump the thread without a real update
- Reply politely to feedback (reviewers are volunteers)
- When you push RC2 / final, edit the OP rather than starting a new thread
- Update the title prefix as you progress: `[RC1]` -> `[RC2]` -> remove prefix when submitted to the Customisations DB
