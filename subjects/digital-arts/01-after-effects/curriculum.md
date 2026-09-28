# After Effects — curriculum (derived from `knowledge-base/00-map.md`)

> Ordered for the learner's goal: **one night → a finished (or nearly finished) .mp4**. Order follows the
> prerequisite graph; each chapter ends in something done *in the software*, because for a tool the
> retrieval that counts is doing it again without looking (principle 1). The study site is ordered the
> same way (`study-pack/web/`, chapters 1–8).

## The one-night plan (≈ 6 h; the build starts by hour 3 at the latest)

| # | Chapter | Time | Done when you can, without looking |
|---|---|---|---|
| 1 | Interface & project | 30 min | name every default panel's job; make a 1920×1080 30 fps 15 s comp; import a file; save |
| 2 | Layers & transforms | 40 min | make solid/shape/text/null; show A P S R T by key; move the anchor with Y; parent to a null |
| 3 | Keyframes & motion | 50 min | animate position with 2 keyframes; F9 it; see the speed graph (Shift+F3); fix a boomerang |
| 4 | Shapes, text, mattes | 50 min | Trim Paths line draw-on; text animator + range selector; footage/gradient inside text via track matte |
| 5 | Effects, precomps, expressions | 30 min | adjustment-layer glow; precompose with the right option; wiggle / time / loopOut |
| 6 | Preview & export | 20 min | preview at Half; Render Queue → H.264 → .mp4 on disk |
| 7 | Shortcuts | ongoing | Tier-1 list (24 keys) used, not memorised from the page |
| 8 | **The build** | 2–3 h | the piece below exported |

**Order rule:** if time is short, skip to chapter 8 after chapter 3 and pull chapters 4–6 in as each build
step needs them. The build *is* the curriculum's check.

## The build — "Title sting" (10–15 s, 1920×1080, 30 fps)
A short animated title (the learner's name or a word they choose) that uses every core skill once:
1. **Background:** solid + Gradient Ramp (or two shapes) → comp look.
2. **Line draw-on:** shape-layer line, Trim Paths End 0 → 100 %, eased.
3. **Title reveal:** text layer; animator (Opacity 0 %, Position y +60) with Range Selector swept 0 → 100 %.
4. **Shape accents:** 2–3 shapes (circles/rects) popping in with Scale keyframes + F9, one with a Repeater.
5. **Control rig:** parent everything to a null; animate the null for a slow push (Scale 100 → 105 %).
6. **Texture:** footage or gradient shown inside the text with a track matte (stretch goal).
7. **Polish:** adjustment layer with Glow; `wiggle(1, 8)` on one accent; motion blur on.
8. **Out:** Render Queue → H.264 → `title-sting-v1.mp4`.

"Done" = step 8 happened. Steps 6–7 are optional; the file matters more than the polish.

## After tonight (spaced relearning)
- Day +1: rebuild steps 2–3 from nothing, no notes (the delayed retrieval test). Log time taken + blocks.
- Day +3: Tier-1 shortcuts quiz from the site + a 5-minute "animate a logo in" drill.
- Day +7: a second, different piece (e.g. lower third or logo sting) → transfer check.
