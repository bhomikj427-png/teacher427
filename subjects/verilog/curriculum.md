# Verilog — Curriculum (derived from knowledge-base/00-map.md)

> Ordered objectives, **prerequisites first** (cognitive-load order, `research/01 §2`). Strictly
> downstream of the map's prerequisite graph (§2). **The full deep pass is already done** (learner
> requested the exhaustive build): every unit has a deep note in `knowledge-base/01`–`12`. Still
> re-confirm/refresh each unit's note on a moving-field recheck before teaching it. Mastery-gated:
> a unit opens only when the prior one is demonstrated, not merely seen. Threshold units (★) get
> extra time + productive-failure setups. **Unit → deep note:** U1→01, U2→02, U3→03, U4→04, U5→05,
> U6→06, U7→07, U8→08, U9→09, U10→10, U11→11, U12→12.
>
> Learner entry point: **U2/U3 boundary** — has built combinational adders (structural/dataflow),
> sequential foundations undiagnosed. Confirm placement in session 1 before advancing.

---

## Syllabus anchor & career framing (added 2026-06-29)

Scope/sequence anchored to **IIT Kharagpur NPTEL *Hardware Modeling using Verilog*** (Sengupta) +
**UC Berkeley EECS151**; truth-authority stays **Harris & Harris**. The career goal (internship/job
edge — `learner-profile.md`) sets *emphasis*, not new truth. Verilog is **step #1 of a track**
(`../_career-roadmap/roadmap.md`).

**Existing units → anchor mapping** (the built base already covers both courses' Verilog scope):

| This curriculum | NPTEL week (Sengupta) | EECS151 theme |
|---|---|---|
| U1 framing | W1 digital circuit design flow | intro / abstraction |
| U2 modules & datatypes | W2 variables, operators, constructs | Verilog basics |
| U3 combinational (struct/dataflow) | W3 combinational modeling | comb. logic, adders |
| U4 behavioral combinational | W3 (behavioral) | — |
| U5 behavioral sequential | W4 sequential modeling | seq. elements |
| U6 blocking/nonblocking ★★ | W4 (clocked-logic correctness) | — |
| U7 FSMs | W4/W6 | FSMs in Verilog |
| U8 verification/testbenches | W5 test benches & simulation | verification tools |
| U9 scaling (params/generate) | W6 behavioral vs structural | datapath building blocks |
| U10 RTL & synthesis discipline | W1/W7 | synthesis, FPGA/ASIC flow |
| U11 timing | (implicit) | timing analysis |
| U12 SystemVerilog migration | → next track step | (SV) |

**Job-relevant scope extensions** (NPTEL W7–W8 + EECS151 capstone; *not yet built* — see
`00-map.md` §6, research to `stage-2✓` before teaching): **design-flow framing**, a **synthesizable
processor capstone** (NPTEL W8 / EECS151 RISC-V — the portfolio centerpiece), and **hands-on FPGA
toolflow**. Slotted as U10+ / U13-capstone / cross-cutting respectively.

---

## Phase I — Foundations & combinational (where the learner is)

**U1. Digital-logic & HDL framing** *(prereq audit + the master reframe)*
- Verify foundations: binary, gates, combinational vs sequential, flip-flop, clock.
- Threshold **T1**: Verilog = hardware description, concurrent, not a running program.
- Outcome: can state *why* code ≠ sequential program, in their own words.

**U2. Modules & data fundamentals**
- module / ports / instantiation / hierarchy (M8: instantiation ≠ function call).
- `wire` vs `reg` as *assignment context* (T4, M2); 4-state values 0/1/x/z; vectors/buses.
- Outcome: can read/declare a module and explain wire-vs-reg correctly.

**U3. Combinational modeling — structural & dataflow** *(consolidate + extend current skill)*
- Gate-level/structural (primitives, wiring); dataflow (`assign`, operators, `assign` is
  continuous & always live).
- **Live project: 4-bit ripple-carry adder** from full adders (the learner's stated next step) →
  then parameterize / compare to dataflow `+`.
- Outcome: builds multi-module combinational hardware; explains the structure as parallel.

## Phase II — Behavioral & the core thresholds

**U4. Behavioral combinational** ★(T3)
- `always @*`, `if`/`case`, **blocking `=`** (Cummings #3); **latch avoidance** (M6, M7):
  assign every output in every branch; complete sensitivity lists.
- Outcome: writes combinational `always` blocks with **zero** inferred latches; can spot one.

**U5. Behavioral sequential** ★(T4)
- `always @(posedge clk)`, flip-flops, reset (sync vs async — taught as judgment), `reg`→register
  inference. Counters, shift registers.
- Outcome: builds a working register/counter; explains when storage is actually inferred.

**U6. Blocking vs nonblocking & event scheduling** ★★(T2 — the keystone)
- **Nonblocking `<=` for sequential** (Cummings #1); the stratified event queue / RHS-eval then
  LHS-update mechanism; races (M3, M4, M5). *(Deep pass reads IEEE 1364 §5 first.)*
- Outcome: predicts shift-register behavior under `=` vs `<=`; states the scheduling rule and why
  it mirrors real flip-flops.

## Phase III — Design at scale & verification

**U7. Finite state machines** — encoding, Moore vs Mealy, 2-/3-block idiom (style as judgment).
**U8. Verification & testbenches** — stimulus, self-checking, `$display`/`$monitor`, waveforms;
why simulation is the verification loop.
**U9. Scaling** — parameters, `generate`, parameterized/reusable hierarchy.

## Phase IV — Professional (far horizon)

**U10. RTL & synthesis discipline** ★(T3, T5) — synthesizable subset, sim/synth mismatch, the RTL
mindset (registers + combinational clouds per cycle).
**U11. Timing** — setup/hold, clocking, intro clock-domain crossing.
**U12. SystemVerilog migration & verification** — `logic`, `always_comb/_ff`, assertions, intro to
UVM. *(Decision point from map §6: possibly pivot to SystemVerilog earlier given the pro goal.)*

---

### Notes
- **Block before interleave** (`research/02 §6`): each unit is practiced solid before U-level
  mixing (e.g. interleaving comb/seq design choices) begins — earliest at U6+.
- Threshold units (★/★★) use *productive failure first* where the goal is concept/transfer
  (`research/03 §5`), worked-examples-first where it's procedure.
- The SystemVerilog-vs-Verilog decision (map §6) is revisited before Phase IV.
