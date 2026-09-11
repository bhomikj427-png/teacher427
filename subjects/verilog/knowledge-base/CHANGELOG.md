# Verilog Knowledge Base — CHANGELOG (correction audit trail, protocol §10)

> Format: `[YYYY-MM-DD] <claim/topic> — <what changed> — <why> — <trigger> — <confidence old→new>`
> Never silently overwrite a claim; record the correction here.

- [2026-06-15] Knowledge base created — map pass completed (00-map, misconceptions, sources) —
  built from authoritative sources (IEEE 1364, Harris & Harris, Cummings SNUG) triangulated with
  secondary refs — trigger: subject creation — confidence: n/a → initial marks set per file.
- [2026-06-15] **Exhaustive deep pass** — at learner request, built per-unit deep notes `01`–`12`
  for the entire curriculum (not just next unit) — trigger: learner asked to clear backlog / no
  deferral — confidence: many `uncertain` → `settled` (see below).
- [2026-06-15] Event-queue scheduling (Big Idea #5 / U6) — added stratified-queue mechanism
  (active/inactive/NBA/monitor; RHS-active, LHS-NBA) — why: needed to teach blocking/nonblocking
  from mechanism — trigger: deep pass — source: Accellera IEEE-1364 §5 extract + chipverify —
  confidence: uncertain → settled.
- [2026-06-15] M9 (`x`/`z` synthesis treatment) — resolved: sim-unknown vs synth-don't-care
  ("X-optimism"), casex bug-masking — trigger: deep pass — source: sim/synth-mismatch + verilogpro
  — confidence: uncertain → settled.
- [2026-06-15] SV-vs-Verilog decision (U12) — resolved with a reasoned recommendation (Verilog
  first → migrate to SV at U10/U12, learner sign-off before Phase IV) — trigger: deep pass —
  source: Pong Chu + Wikipedia + industry commentary — confidence: open → settled (facts) /
  evolving (industry default) / reasoned-judgment (the recommendation).
- [2026-06-15] Added reset-strategy (U5) as `contested` (Cummings SNUG 2002), signed-arithmetic &
  bit-width gotchas (U2, Tumbush DVCon'05), CDC/metastability (U11) — trigger: deep pass.
- [2026-06-29] **Career re-frame + syllabus anchor** — goal re-stated as an internship/job edge and
  as **step #1 of a track** (new `../_career-roadmap/roadmap.md`); scope/sequence anchored to IIT-KGP
  NPTEL (Sengupta) + Berkeley EECS151 (sources added); existing units mapped to those weeks in
  `curriculum.md`. **No truth claims changed** — emphasis only. Opened 3 scope-extension items
  (design-flow framing, processor capstone, FPGA toolflow) in 00-map §6, queued for `stage-2✓`
  research before teaching — trigger: learner request — confidence: unchanged for all existing claims.
