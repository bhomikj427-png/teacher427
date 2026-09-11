# U12 — SystemVerilog Migration & the Strategic Decision (deep notes) [PROFESSIONAL]

> Deep pass 2026-06-15. Resolves the standing open question: Verilog vs SystemVerilog for a
> professional goal. Sources: Pong Chu (SV-vs-Verilog-in-RTL), Wikipedia SystemVerilog, industry
> commentary; triangulated.

## A. The relationship
- **Verilog is a subset of SystemVerilog.** SystemVerilog (IEEE 1800) absorbed Verilog (IEEE 1364)
  in 2009; all Verilog-2005 is valid SystemVerilog. So learning Verilog is **never wasted** — it's
  the foundation SV is built on. `[settled — Wikipedia; Pong Chu; corroborated]`

## B. SystemVerilog's RTL-design improvements (fix real Verilog pain points)
- **`logic` type** — replaces the `wire`/`reg` confusion (T4/M2): one type for both contexts (tool
  infers; multiple-driver still flagged). `[settled]`
- **`always_comb` / `always_ff` / `always_latch`** — declare *intent*; the tool **errors** if the
  code doesn't match (e.g. `always_comb` that would infer a latch, or an incomplete sensitivity
  list). Directly kills the U4 latch trap (M6/M7) at compile time. `[settled — Pong Chu; corrob.]`
- **`enum`** for state machines (readable, type-checked states); **`struct`/packed arrays** for
  clean buses; **`typedef`**. `[settled]`
- Net effect: "more descriptive and less error-prone" RTL — catches at compile time what Verilog
  catches only in sim or silicon. `[settled — Pong Chu]`

## C. SystemVerilog's verification side
A much larger leap: classes, constrained-random, functional coverage, assertions (SVA), and the
**UVM** methodology — the industrial verification standard. This is a substantial separate domain.
`[settled — industry-standard; Wikipedia]`

## D. The decision (resolved)
- **Industry reality:** SystemVerilog is the default for new RTL and the standard for verification;
  much legacy IP is plain Verilog, so professionals **read both**. `[settled — industry commentary;
  marked `evolving` — recheck on subject re-entry]`
- **Recommended path for this learner (professional goal):** learn the **fundamentals in Verilog**
  (U1–U9) — simpler surface, forces understanding of wire/reg, sensitivity lists, latches *before*
  the SV conveniences hide them — **then migrate to SystemVerilog** for RTL (`logic`,
  `always_comb/_ff`, `enum`) around U10/U12, and treat verification/UVM as a later dedicated track.
  Rationale: the SV safety features are best appreciated *after* feeling the Verilog problems they
  solve (desirable difficulty; avoids cargo-culting `always_comb`). **Confirm with the learner
  before Phase IV.** `[reasoned recommendation — flagged for learner sign-off]`

## What the engine teaches from this
Decision point, not a drill. Present the tradeoff honestly and let the learner choose (autonomy,
SDT). Near-term units (U1–U9) are taught Verilog-first regardless, so nothing blocks on this.

## Confidence / gaps
Relationship & feature facts `settled`. Industry-default status `evolving` (recheck on re-entry).
The learn-Verilog-then-SV recommendation is **reasoned**, not sourced as fact — flagged as a
judgment call for learner sign-off before Phase IV.
