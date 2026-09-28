# Stage 2 exit test (the §0 surplus test) — 2026-09-28

> `two-stage-depth.md`: generate expert-level / edge-case / "why, not what" questions and confirm the base
> answers each **from mechanism, with sources**. No PYQs exist for this subject; the questions are the
> problems a working motion designer hits. Result at the bottom.

1. **Why does a drop shadow spin when its layer rotates, and name two fixes.**
   Effects render before transforms inside a layer, so the shadow is baked into the layer's pixels and then
   rotated with them. Fixes: apply the shadow on an adjustment layer (or precomp) above, so it is computed
   after the rotation; or add the Transform effect *above* Drop Shadow and rotate with it instead.
   → `stage-2/01` §1 [UG p.100–101]. **Pass.**
2. **A logo precomp looks soft when scaled to 300 % in the main comp. Why, and what fixes it?**
   The precomp is rendered to pixels at its own size first, then scaled up. Collapse Transformations defers
   the nested transforms so vector content is drawn at the final size. → `stage-2/01` §2 [UG p.101]. **Pass.**
3. **One glow should light 12 text layers evenly. Per-layer effect, adjustment layer, or precomp — which is
   cheaper and why?** Adjustment layer (or one effect on a precomp): it runs once on the composite below
   instead of 12 times; Adobe states the performance gain. → `stage-2/01` §1 [UG p.180]. **Pass.**
4. **Two Position keyframes with identical values, yet the layer drifts between them. Mechanism?**
   Auto Bezier spatial interpolation fits a smooth curve through neighbouring keyframes, so the path bulges
   out and back even when the endpoints match. Hold or Linear removes the curve. → unit 03 [UG p.310]. **Pass.**
5. **In the speed graph, you raise the outgoing speed of the first keyframe. Why does the middle of the
   move slow down?** The distance covered between keyframes is fixed (area under the speed curve); more
   speed early must be paid back later. → `stage-2/02` §1 (derived from UG p.318). **Pass (derived).**
6. **Motion blur is on for the layer but nothing blurs.** Comp-level Enable Motion Blur is off; both
   switches are required. With it on, 180° at 30 fps exposes 1/60 s per frame. → `stage-2/02` §3
   [UG p.91, 193]. **Pass.**
7. **Footage inside letters: which layer is the matte and which the fill, and what changed in 23.0?**
   Text = matte (alpha), footage = fill; since 23.0 the matte is picked in the Track Matte column and need
   not sit directly above. → unit 04 [UG p.499; AE23]. **Pass.**
8. **The render is 4 GB for 12 seconds. Why?** Default output module = Lossless. Use H.264 (Render Queue
   23.0+) or AME. Render settings and output module are separate stages, so only the output module changes.
   → unit 06, `stage-2/01` §5 [LEARN; AE23; UG p.541–543]. **Pass.**
9. **A gradient background shows visible bands. What setting, and why does it help?** Raise project bit
   depth to 16 bpc: more levels per channel (0–32 768 vs 0–255) → smaller steps. → `stage-2/01` §6
   [UG p.360]. **Pass.**
10. **Why does Easy Ease on every keyframe start to look samey, and what does the animation literature say?**
    Thomas & Johnston warn that overused slow-in/slow-out gives "a mechanical feel"; tune ease per move in
    the speed graph (asymmetric influence). → `stage-2/02` §2 [WLV06 quoting TJ81]. **Pass.**

**Result:** 10 / 10 answered from mechanism with sources (2 by derivation from sourced mechanism, marked).
Open register items Q1–Q3 in `00-map.md` are version checks, not gaps in mechanism.
**Status → `stage-2✓` for the scope in `../../course-info.md`.**
