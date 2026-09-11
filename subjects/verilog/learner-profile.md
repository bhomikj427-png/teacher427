# Verilog — Learner Profile

> Current level, goals, known/observed misconceptions, and subject-specific preference overrides.
> Maintained by the engine via the self-update protocol (`../../CLAUDE.md`).

## Goal
- **End goal: professional RTL design — explicitly framed as a *career* skill: an edge for VLSI/
  digital-design internships and jobs.** `[stated 2026-06-15; re-framed 2026-06-29]` → research
  deep (toward synthesis, timing, verification); teach gradually; hold a high correctness bar from
  early on. The career framing sets the *emphasis*: lead with what makes a hire-able RTL portfolio
  (a synthesizable design built end-to-end, a small processor capstone, clean RTL coding discipline,
  testbench/verification literacy), not just language syntax.
- **Verilog is goal #1 of a multi-step track, not the destination.** `[stated 2026-06-29]` The
  learner wants the sequence *after* Verilog mapped too (next language = SystemVerilog; then the
  Design-vs-Verification fork; UVM; scripting; FPGA/ASIC flow). The full sequenced plan lives in
  `../_career-roadmap/roadmap.md`. Teach Verilog with that horizon in view — name where each skill
  leads, so it never feels like isolated syntax.
- **Syllabus anchor (chosen 2026-06-29):** scope/sequence anchored to **IIT Kharagpur NPTEL
  *Hardware Modeling using Verilog*** (Prof. Indranil Sengupta — the strongest Verilog-dedicated
  top-tier course, IIT, freely accessible, and ingestible via `tools/fetch_transcripts.py`), cross-
  referenced with **UC Berkeley EECS151** (FPGA+ASIC flow, industrial EDA tools, RISC-V capstone —
  the job-grade framing). Textbook authority stays **Harris & Harris** (truth), per the source-split
  rule. Mapping of existing units → these courses is in `curriculum.md`.

## Current level — **developing** (re-diagnose each session)
- Has written combinational Verilog: **half adder**, **full adder**; **4-bit adder** is the
  intended-but-not-yet-built next step. `[stated 2026-06-15]`
- **Undiagnosed:** depth of digital-logic foundations (esp. sequential logic, flip-flops,
  clocking); whether prior adders were structural, dataflow, or behavioral; grasp of the
  hardware-not-software reframe (T1). → first session opens with retrieval to place them.
- Entry point: curriculum **U3** (combinational modeling), pending the U1 prereq audit.

## Known / suspected misconceptions to watch
*(from `knowledge-base/misconceptions.md` — confirm or rule out via retrieval, don't assume)*
- T1/M1 (hardware vs sequential program) — **unconfirmed**; high-priority probe.
- M2 (`reg` = flip-flop) and M8 (instantiation = function call) — likely untested so far (adders
  are combinational + small). Watch when modules/registers appear.
- M3–M7 (blocking/nonblocking, latches) — not yet reachable; will surface at U4–U6.

## Preferences (overrides)
*(Subject-specific only; these win over `../../learner-preferences.md` inside Verilog. None yet.)*
- [observed 2026-06-15] Insists the knowledge base be researched to standard **before** being
  taught — flagged that teaching from recall is not acceptable. → always complete the map/deep
  pass and cite sources before instructing; never teach from unverified recall. *(Also reflects a
  universal value — mirrored to `learner-preferences.md`.)*
- [stated 2026-07-03] **Do not drill gate-level circuit reproduction/recall** (e.g. reconstruct a
  full adder from gates) — learner can hold the block-level/conceptual model but not the gate
  diagram, and predicts they won't retain gate diagrams. → work at the **behavioral/RTL abstraction**
  (describe behavior, e.g. `assign {cout,s}=a+b+cin;`, let synthesis build gates); when gate
  structure is genuinely needed, **derive it from the truth table** (sum=parity, carry=majority),
  never require recall. Goal-aligned: RTL design never hand-codes gates, so this trades no principle
  — retrieval still happens, at the abstraction the goal actually uses. Diagnose T1/sequential via
  other probes, not the full-adder gates.

## Tensions to manage
- None yet.
