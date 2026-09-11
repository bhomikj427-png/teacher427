# ECE2102 Digital Electronics — Curriculum (derived from knowledge-base/00-map.md)

> Ordered objectives, **prerequisites first** (cognitive-load order). Strictly downstream of the
> map's prerequisite graph. Base is **`stage-2✓`** — Stage-1 files are the exam set; `stage-2/`
> holds depth to open after exam mastery (scoring-over-depth governs teaching order). Mastery-
> gated: a unit opens only when the prior is *demonstrated*. ★ marks threshold units.
> Cross-links: U5 shares substrate with `../03-electronic-devices-1` (MOSFET→CMOS) and the whole
> subject with `../../verilog` (HDL models of exactly these blocks) — re-use, don't re-derive.

## U0 (folded into U1 opening) — Number systems & codes (assumed prereq, verify by retrieval)
- Binary/hex, 2's-complement, BCD, Gray, ASCII. Probe, don't lecture; teach only exposed gaps.

## U1 — Combinational Logic Design ★★ (K-map fluency is the recurring tool)
- Boolean algebra (axioms, De Morgan); gates; **NAND/NOR functional completeness** (★).
- SOP/POS, minterms/maxterms; **K-map as visual Boolean adjacency** (★ — grouping = XY+XY′=X),
  don't-cares; Quine–McCluskey.
- Half/full adders, subtractors (FS-borrow verified); serial vs parallel adders, ripple vs CLA;
  BCD adder (+6 correction verified); code converters (Gray/excess-3).
- Outcome: minimizes via K-map incl. don't-cares and POS; converts AOI→NAND-only using De Morgan
  *in use*; designs an adder/subtractor from truth table to gates.

## U2 — MSI Combinational Blocks
- Comparators (verified eqns); MUX/DEMUX (MUX as function generator — loop back to minimization);
  encoders/decoders; display drivers + multiplexed display; barrel shifter; ALU.
- Outcome: implements an arbitrary function on a MUX/decoder; picks the right MSI block and
  justifies it from structure.

## U3 — Sequential Elements ★★ (the memory line: feedback + a clock)
- **Combinational vs sequential — the memory boundary** (★, the subject's deepest split).
- Latch → flip-flop: SR, D, JK, T; characteristic + excitation tables (verified);
  **master–slave / edge-triggering** (★ — why a latch races, how the edge fixes it).
- Ripple vs synchronous counters; shift registers; **timing: setup/hold, t_pd, f_max** (★ —
  f_max = 1/(t_pd,FF + t_comb + t_setup)).
- Outcome: derives a counter from excitation tables; computes f_max; explains level-vs-edge and
  why synchronous design tames feedback.

## U4 — State Machines ★ (the synthesis-pipeline threshold — U1 + U3 fuse here)
- FSM model: state register + next-state logic + output logic; Moore vs Mealy.
- **The pipeline** (★): state diagram → table → reduction → assignment → excitation → K-map the
  FF inputs/outputs. Gate: cannot open before U1 *and* U3 are solid.
- ASM charts; PRBS/LFSR (2ⁿ−1, all-zeros lockout — verified); pulse-train + clock generation
  (555/ring/crystal/Schmitt — added in cross-check pass); async circuits, hazards/races.
- Outcome: designs a sequence detector end-to-end through the pipeline unaided.

## U5 — Logic Families & Memories (the physics tax, deliberately last)
- Universal yardsticks: V_OH/V_OL/V_IH/V_IL, noise margin, fan-out, t_pd, power-delay product.
- Standard TTL NAND (verified DC table → fan-out 10, NM 0.4 V); tristate; ECL; CMOS + interfacing
  (per-series numbers `uncertain` — teach standard-TTL anchor + the datasheet caveat).
- SRAM/DRAM/ROM; PLDs: PROM/PLA/PAL (verified array structures) — implement earlier logic on them.
- Outcome: computes NM/fan-out from a DC table; chooses a family from trade-offs; maps a
  minimized function onto a PLA/PAL.

## Teaching notes carried from the map
- The two hardest edges: **minimization → combinational design** and **combinational → sequential**
  (the "feedback + clock = memory" jump). Budget productive-failure setups there.
- Confidence flags survive into teaching: MUJ unit/MTE-ETE split + examined textbook `uncertain`
  (no PYQ — rebuild exam-map when papers land); short-circuit-%/DRAM-ΔV/essential-hazard/74181 rows
  `likely` (mechanisms settled, exact numbers to primary); frontier claims `evolving` (recheck on
  re-entry).
- Stage-2 depth (`knowledge-base/stage-2/01–05`) opens per unit only after exam-level mastery.
