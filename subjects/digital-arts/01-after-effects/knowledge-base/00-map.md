# After Effects — 00 MAP

> Big ideas, prerequisite graph, threshold concepts, scope and the to-verify register. Built to
> `../../../../subject-research-protocol.md`. Scope = `../course-info.md`. Truth = Adobe's user guide [UG]
> (`sources.md`). Confidence: `settled` unless marked.
>
> **Status: `stage-2✓` (2026-09-28), scope-bounded.** Stage 1 = units 01–06 + shortcuts. Stage 2 =
> `stage-2/` (render pipeline, motion and time, exit test). The exit test is recorded in
> `stage-2/03-exit-test.md`. "Complete" means complete **for the scope in course-info**; the parked
> topics listed there are not researched.

## The big ideas (the schema an expert reasons from)

1. **Everything is a nesting of containers.** Project (.aep file) ⊃ compositions ⊃ layers ⊃ property
   groups ⊃ properties. A composition is a timeline plus a frame; it can itself be a layer in another
   composition (nesting / precomposing). Almost every "where is X?" question is answered by knowing which
   container owns X. [UG p.78, 86]
2. **Animation = a property changing over time, pinned by keyframes.** Any property with a stopwatch can
   be animated. You set values at key times; After Effects interpolates the frames between. How it
   interpolates (linear, Bezier family, hold; eased or not) is where motion gets its feel. [UG p.232, 309]
3. **A frame is computed bottom-up.** The bottom layer renders first. Inside each raster layer: masks →
   effects → transform → layer styles. This one order explains adjustment layers, why a drop shadow turns
   with its layer, why precomposing changes results, and why track mattes need care. [UG p.100]
4. **Transforms are relative.** Position lives in composition space; the anchor point lives in layer
   space and is the pivot for scale and rotation. A child layer's transforms are relative to its parent.
   Most "it rotates around the wrong point" / "it flies off" bugs are this idea. [UG p.183, 205]
5. **Nothing is real until it is rendered.** Preview is a cached approximation (RAM, resolution, skip).
   The file only exists after the Render Queue (or Media Encoder) encodes it. [UG p.155, 541]

## Prerequisite graph (what builds on what)

```
01 Interface & project ──► 02 Layers & transforms ──► 03 Keyframes & motion ──┐
                                   │                                          ├─► 05 Effects, precomps,
                                   └──► 04 Shapes, text, masks, mattes ───────┘       expressions
                                                                                        │
 Shortcuts (spans all units; learned by use, not by list)             06 Preview & export ◄─┘
                                                                        │
                                                                        ▼
                                                                     THE BUILD
```
- 03 needs 02: you animate transform properties first (A P S R T).
- 04 needs 02 (layers, stacking) and uses 03 (Trim Paths and range selectors are keyframed).
- 05 needs 02–04: precomposing and track mattes only make sense once layers and stacking are clear.
- 06 needs 01 (compositions) and anything to export.

## Threshold concepts (once crossed, the rest reorganizes)
- **T1 Anchor point vs position.** Until this clicks, every rotation and scale looks broken.
- **T2 Keyframes store values, interpolation makes motion.** Until this clicks, learners add many
  keyframes to fake smoothness instead of easing two.
- **T3 Render order (bottom-up; masks → effects → transform).** Unlocks adjustment layers, precomps,
  mattes and "why does my effect do that".
- **T4 Composition as a layer (nesting).** Unlocks precomposing, reusable pieces and project organisation.

## Unit files
- `01-interface-and-project.md` · `02-layers-and-transforms.md` · `03-keyframes-and-motion.md` ·
  `04-shapes-text-masks-mattes.md` · `05-effects-precomps-expressions.md` · `06-preview-and-export.md`
- `shortcuts.md` — the verified shortcut reference, ranked.
- `misconceptions.md` — predictable beginner errors (traps).
- `stage-2/` — depth: render pipeline, motion and time, exit test.

## Open questions / to-verify register
- **Q1 [version]** Adobe's live 2026 shortcut page could not be fetched (403). Shortcuts are from the
  archived guide (AE 17.0 era) cross-checked against two 2026 third-party lists. Re-check any shortcut
  that misbehaves in 26.5 in Edit > Keyboard Shortcuts (Ctrl+Alt+'), which shows the live bindings.
- **Q2 [version]** The Properties panel (2024+) changes the easiest place to edit transforms; the KB
  teaches the Timeline route, which still works. Confirm the panel's default presence in 26.5's
  Default workspace on first launch.
- **Q3** Default expression engine is JavaScript in current versions (the guide has a section on
  JavaScript vs Legacy ExtendScript). The three starter expressions taught work in both. `likely`.
