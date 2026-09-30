# phpBB.com validation response — ForgeBoard 1.2.1

Comment to post on the phpBB.com Customisations topic when re-submitting,
addressing the Styles Team (_Vinny_) review. Excluded from the release ZIP
(docs/ is not shipped).

---

Hello,

Thank you for the detailed review of ForgeBoard. I've addressed **every point** you raised, and — after a full self-audit — added a few further improvements. The updated package is **ForgeBoard 1.2.1**.

**The nine denial reasons — all fixed:**

1. **Block headers lacked contrast in light mode** — Forum and table headers now use dedicated high-contrast tokens (`--gb-block-header-bg` / `--gb-block-header-fg`), so the header band clearly separates from the block body and the row stripes.
2. **Placeholder that didn't make sense** — The decorative "site name" filler cards have been removed entirely. The forum grid now flows naturally with `repeat(auto-fit, minmax(280px, 1fr))`.
3. **Locked forum had no icon** — Locked forums now display a lock icon.
4. **Topic icons were not supported** — Admin-defined topic icons (`TOPIC_ICON_IMG`, under `S_TOPIC_ICONS`) are now rendered in the topic list.
5. **Locked topics had no icon** — Locked topics now display a lock icon.
6. **PM icons used prosilver images** — The private-message folder list now uses the style's own SVG status icons instead of inheriting prosilver's GIFs.
7. **No contact icons in the mini-profile** — Contact icons are now rendered with the style's own FontAwesome glyphs, legible in both light and dark themes, with no dependency on prosilver's `icons_contact.png` sprite.
8. **Stylesheet header referenced 3.3.16** — Corrected to 3.3.17, matching `style.cfg`.
9. **No `prefers-color-scheme` fallback for dark mode** — Added an `@media (prefers-color-scheme: dark)` block so dark mode works with JavaScript disabled, while still respecting an explicit light-mode choice.

**Additional improvements made during my own review:**

- **Light-mode contrast hardening** — Red text (kickers, flags, labels) and small secondary labels were darkened so they meet WCAG AA (>=4.5:1) on the light canvas.
- **Prosilver parity** — Restored `{LAST_VISIT_DATE}` on the index for logged-in users (the only content variable missing after the redesign). I also re-verified that all overridden templates keep every prosilver template **event** and all original functionality (polls, attachments, signatures, post/moderation buttons, posting options, etc.).
- **Full RTL support** — The style previously shipped no `bidi.css`, so RTL boards had no mirroring at all. I added a `theme/bidi.css` (loaded only for RTL languages, zero impact on LTR): it imports prosilver's `bidi.css` for the inherited base and mirrors the physical properties of the custom card layout. Verified by rendering the index, viewforum and viewtopic in RTL.
- **Locked-topic cues** — The reply button and the topic-list icon now turn red on a locked topic, to make the closed state obvious.

Download: **https://github.com/gitubpatrice/forgeboard-phpbb-style/releases/tag/v1.2.1**

Thanks again for taking the time to review ForgeBoard.
