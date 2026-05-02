# ForgeBoard

A modern code-forge inspired phpBB style based on Prosilver (phpBB 3.3.16).

## Installation

1. Copy the `ForgeBoard/` directory into your phpBB `styles/` directory.
2. Go to ACP → Customise → Styles → Install ForgeBoard.
3. Purge the phpBB cache.

## Requirements

- phpBB 3.3.x (tested on 3.3.16)
- Prosilver style installed (parent style)

## Structure

```
ForgeBoard/
├── style.cfg           # Style metadata (parent = prosilver)
├── template/           # Templates overriding Prosilver
│   ├── overall_header.html
│   ├── overall_footer.html
│   ├── index_body.html
│   ├── viewforum_body.html
│   ├── viewtopic_body.html
│   ├── posting_editor.html
│   ├── ...
│   ├── forge_dropdown_reset.js
│   └── forge_mcp_fix.js
└── theme/              # CSS theme
    ├── stylesheet.css  # Imports Prosilver + forgeboard.css
    └── forgeboard.css  # ForgeBoard overrides + variables
```

## CSS Variables

The theme exposes CSS custom properties (in `:root`) for colors, radii and shadows.
A dark variant is auto-applied via `prefers-color-scheme: dark`.

Key variables:

- `--gb-canvas`, `--gb-surface`, `--gb-surface-subtle`
- `--gb-text`, `--gb-text-muted`
- `--gb-link`, `--gb-link-hover`, `--gb-accent`
- `--gb-border`, `--gb-border-muted`
- `--gb-radius`, `--gb-radius-small`
- `--gb-shadow`, `--gb-shadow-soft`

## Versioning

See `style.cfg` for current `style_version`.

## License

(c) FanFanLaTuFlippe, 2026.
