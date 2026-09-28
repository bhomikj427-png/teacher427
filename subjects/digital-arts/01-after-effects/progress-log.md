# Progress log — After Effects (digital-arts/01)

## Session resume
- Last session: 2026-09-28 (build session, no teaching yet)
- Where we stopped: KB + study pack built. No learner retrieval has happened yet.
- Recap (what happened):
  - Subject created on learner request: "digital arts" group, After Effects first.
  - KB built from Adobe's official After Effects user guide (tier 1), cross-checked for 2026 changes.
  - Site-v1 study pack written: 8 chapters, the last one being tonight's build project.
- Next up: the learner's one-night sprint. The study pack is ordered for it (ch 1 → 8). Next session opens
  with delayed recall of the interface map + the 20 must-know shortcuts, **before** any recap.
- Due for review today: nothing (no items mastered yet).

## Mastery ledger
*(empty: nothing has passed a retrieval CHECK yet)*

## Spaced-review / relearning queue
*(empty. The first items enter here when the learner passes a check; suggested first return = the day
after the sprint, then +3 days, +7 days.)*

## Live log — 2026-09-28
- Learner request: new `digital-arts` group, first subject After Effects; wants layout, how to operate,
  shortcut list, "whatever usefulness"; one night; wants an end product even if unfinished; site-v1 pack.
- Gate: subject created at `stage-0`; researched to `stage-2✓` for the scope in `course-info.md`
  before any study material was written (teaching gate).
- Sources pulled: Adobe *After Effects User Guide* PDF (Wayback copy, 2025-06-13, 667 pp) = tier 1; Adobe
  community announcement for AE 23.0 (H.264 in Render Queue, selectable track mattes); Wikipedia for the
  current version (26.5, 2026-09-10); two tier-3 shortcut lists for cross-checking. Adobe helpx pages
  returned 403 to automated fetches, so live help pages could not be read directly.
- Discrepancy logged: a 2026 third-party cheat sheet says → steps one frame; Adobe's table says
  Page Down / Ctrl+→ steps a frame and a plain arrow nudges the selected layer 1 px. Adobe wins;
  recorded as trap T3 in `misconceptions.md`.
- Correction logged: the guide says a track matte "only applies to the layer directly beneath it"; since
  AE 23.0 any layer can be picked as the matte. KB teaches the 23.0+ behaviour (CHANGELOG entry 1).
- KB written: `knowledge-base/` 00-map, units 01–06, shortcuts, misconceptions, sources, CHANGELOG;
  `stage-2/` 01–03 + sources. Stage-2 exit test answered in `stage-2/03-exit-test.md` → status `stage-2✓`
  (scope-bounded, see course-info).
- Study pack: `study-pack/web/` (meta.json, figures.py, verify.py, content 01–08) written; `site/build.py`
  given an optional `line` field (top-bar text for subjects with no exam) and now omits the ★ legend on
  pages with no exam questions; `SITE-V1.md` §4/§6 note both (format unchanged).
- `verify.py` first run: 1 failure — 8 keys shown on the site were not listed explicitly in
  `knowledge-base/shortcuts.md` (H, W, Alt+Shift+P/S/R/T, Ctrl+3, Ctrl+5; all on UG p.14–25). KB table made
  explicit; rerun: ALL CHECKS PASSED (37 figures valid, 78 shortcut rows ⊆ KB, easing/rotation/selector/
  expression maths).
- `site/build.py`: after-effects tree page, 69 concepts, 69 drawn. Screenshots checked at 1400 px (tree,
  Easy Ease card, keyboard card, track-matte card) and 390 px. At 390 px the card clipped on the right, and
  the existing Digital Electronics pack clips the same way in the same headless run → suspected headless
  Chrome minimum-width artefact, not confirmed on a real phone.
- After the ★-legend edit to `site/build.py`, the shell's safety check stopped responding: the final
  rebuild, the 390 px iframe re-check and the git commit/push were **not run** this session. They were
  handed to the learner as `!` commands. If the tree is dirty at next start, §0b applies.
- Learner's `!` rebuild failed twice: first a wrong working directory, then WinError 32, because the engine
  shell was still inside `site/public/after-effects`. Shell moved out; rebuild OK (69/69 drawn; ★ legend
  absent on after-effects, present on digital-electronics). 390 px check re-run inside iframes: card and
  tree fit with no clipping → the earlier clipping was the headless minimum-width artefact.
