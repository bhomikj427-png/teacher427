# After Effects KB — CHANGELOG (corrections audit trail)

> Protocol §10 format: date · claim · old → new · why · source.

1. **2026-09-28 · Track matte position.** UG p.499: "A track matte only applies to the layer directly
   beneath it." → Since **23.0** any layer can be selected as the matte (Track Matte column pick whip or
   menu). · Newer vendor source supersedes the 2019-era guide text. · [AE23]
2. **2026-09-28 · Export to .mp4.** UG (2019 text) routes H.264 through Adobe Media Encoder. → Since **23.0**
   H.264 is available directly in the Render Queue output module. · [AE23]
3. **2026-09-28 · Frame stepping.** Tier-3 cheat sheet (Academy Class, 2026): → steps one frame. → Rejected:
   Adobe's table maps arrows to layer nudge and Page Down / Ctrl+→ to frame step. · UG p.17, 23. Logged as
   trap T3.
4. **2026-09-28 · Removed an unsourced claim** from unit 05 ("the value turns red while an expression is
   active"): not found in UG; dropped rather than kept on recall.
5. **2026-09-28 · Page citations** in units 01–06 were checked one by one against the PDF text and
   corrected where the first draft was off by 1–5 pages.
6. **2026-09-28 · wiggle amplitude.** First draft: "up to amp units". → UG p.615: amp is the *average* size ("average size of about 20 pixels"). Also dropped an unsourced "wiggle is deterministic per layer" line from stage-2/02.
