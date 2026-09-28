# After Effects — sources (tiered, dated, confidence-marked)

> Per `../../../../subject-research-protocol.md` §2. For a software subject the vendor's documentation
> is tier 1 (the textbook's role). There is no tier 0 (no instructor material). Page numbers `UG p.N` are
> PDF page indices of the user guide below (the guide's own TOC uses the same numbers).

## Tier 1 — vendor documentation (sets truth)
- **[UG] Adobe, *Adobe After Effects User Guide* (PDF, 667 pp).** Original URL
  `https://helpx.adobe.com/pdf/after_effects_reference.pdf` (returns 403 to scripts); retrieved
  2026-09-28 from the Wayback Machine capture of **2025-06-13**:
  `https://web.archive.org/web/20250613033014id_/https://helpx.adobe.com/pdf/after_effects_reference.pdf`.
  Sections used: keyboard shortcuts (p.9–29), workspaces and panels (p.41–55), projects and compositions
  (p.78–102), previewing (p.155–168), layers, properties, blending (p.177–215), animation basics and
  Graph Editor (p.232–236), keyframes, interpolation, speed (p.292–329), shapes and masks (p.404–445),
  text and text animation (p.445–490), mattes (p.490–505), performance (p.527–537), rendering (p.541–560),
  expressions (p.576–640). `settled` for fundamentals. **Caveat:** most chapters are footed "Last updated
  11/4/2019" (AE 17.0); anything that changed after that is checked against the tier-2 items below.
- **[AE23] Adobe Community, "After Effects 23.0 and MAX 2022: H.264 export, selectable track matte layers
  and more"** (Adobe staff announcement), community.adobe.com/t5/after-effects-discussions/…/td-p/13275804,
  read 2026-09-28. Sets: H.264 in the Render Queue (three presets, hardware and software encoding) and
  track mattes selectable from any layer. `settled` [version: 23.0+].
- **[LEARN] Adobe Learn, "Render a video composition"**, adobe.com/hk_en/learn/after-effects/web/render-video-composition,
  read 2026-09-28. Sets: Render Queue click path (Best Settings → Output Module "Lossless" default →
  Output To → Render). `settled`.

## Tier 2 — reference for version facts
- **Wikipedia, "Adobe After Effects"**, read 2026-09-28: current release **2026 (26.5), 2026-09-10**.
  Used only for the version number. `likely`.
- **Adobe helpx feature summaries** (titles and search snippets only, pages 403 to fetch): Properties
  panel for layer transforms in the June 2024 release (24.5); Properties panel 3D-model options in the April
  2025 release (25.2). `likely` [version].

## Tier 3 — third-party (cross-check only, never sets a fact alone)
- **KeyCombiner, "After Effects keyboard shortcuts"**, keycombiner.com/collections/after-effects/, read
  2026-09-28. A copy of Adobe's table; agreed with UG on every row spot-checked.
- **Academy Class, "After Effects Keyboard Shortcuts: The Complete Cheat Sheet 2026"**, read 2026-09-28.
  Agreed with UG on work area, property keys, J/K, F9, precompose, split, render queue. **Disagreed** on
  frame stepping (it says → steps a frame). Adobe's table wins; see `misconceptions.md` T3.
- **ShortcutKings / Shotkit** (search results, 2026-09-28): Ctrl+M = Composition > Add to Render Queue.
  Two independent tier-3 sources plus the Composition menu itself; UG's table lists Ctrl+Shift+/ for the
  same command. Both are taught. `likely`.

## Not usable
- Adobe helpx HTML pages (keyboard-shortcut reference, what's-new) return HTTP 403 to automated fetches
  from this machine, so the live 2026 versions of those pages were not read. Open question Q1 in `00-map.md`.
