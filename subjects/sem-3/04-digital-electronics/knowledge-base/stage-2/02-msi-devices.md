# U2 — MSI Devices (Stage 2: deep structure + frontier)

> Extends `../02-msi-devices.md`. The deep idea: **every MSI block is an instance of one of a few
> universal decompositions** (Shannon expansion, residue/prefix). Primary: Brown & Vranesic, De
> Micheli, Weste-Harris.

---

## A. The MUX is Shannon's Expansion Theorem in hardware (the unifying result)

**Shannon expansion:** for any Boolean f, **f(x₁,…,xₙ) = xᵢ·f|ₓᵢ₌₁ + xᵢ′·f|ₓᵢ₌₀** (cofactors).
That identity *is* a 2:1 MUX (select xᵢ, data = the two cofactors). `settled (standard)` (Brown &
Vranesic §6; standard). Consequences — all one theorem:
- Recursively expanding on k variables → a **tree of 2:1 MUXes** = a 2ᵏ:1 MUX whose data inputs are
  the residue cofactors. So "implement an n-var function with a 2ⁿ⁻¹:1 MUX, data ∈ {0,1,xₙ,xₙ′}" is
  *literally* one expansion step done by hand. The Stage-1 trick is a theorem, not a recipe. `settled`.
- A **decoder** generates *all* minterms = the full cofactor basis; OR-ing them = reassembling f.
  A **PROM** (→ U5) is this frozen in silicon; an **FPGA LUT** is a small MUX-tree truth table
  (→ `../../../verilog`). One root: complete basis + programmable combination. `settled`.
- **BDD (Binary Decision Diagram):** Shannon expansion applied recursively, with sharing + reduction,
  gives the **ROBDD** — the canonical, compact function representation modern tools actually use for
  equivalence checking and synthesis. The MUX you learn in week 3 is the data structure EDA runs on.
  `settled (standard)` (Bryant 1986; De Micheli).

---

## B. Comparators, adders, priority — as prefix / iterative structures

- **Magnitude comparator is a prefix computation** like the adder: scanning MSB→LSB, "decided-greater/
  equal/less so far" is an associative accumulation → a ripple comparator is O(n), a tree comparator
  O(log n). The Stage-1 cascaded-7485 equation is the serial (ripple) form. `settled (standard)`.
- **Subtraction = comparison:** A−B's borrow-out *is* the (A<B) signal — comparison and subtraction
  are the same datapath (→ U1 §C). `settled`.
- **Priority encoder = a "find-first-one" prefix:** the valid/priority logic is a leading-zero-count
  primitive, used in floating-point normalization and arbiters. `settled (standard)`.

---

## C. Barrel shifter — log-depth, and the delay model

- An n-bit barrel shifter = log₂n stages of 2:1 MUXes (stage k shifts by 2ᵏ) → **O(log n) MUX delay,
  O(n log n) MUXes**; a *funnel* shifter handles shift+rotate+field-extract uniformly. This is why a
  CPU shifts any distance in one cycle while a shift register (U3) needs n clocks — **combinational
  log-depth vs sequential linear-time**, the same area↔time trade as adders. `settled (standard)`
  (Weste-Harris datapath). Logical-effort analysis gives the real per-stage delay.

---

## D. The ALU and the 74181 — the actual algebra

The 74181's "16 arithmetic + 16 logic functions" aren't ad hoc: it generalizes the (g,p) carry
network so the **same carry chain** serves add/subtract/increment and the logic ops, selected by
S₃–S₀ and mode M. It exposes group-generate/propagate (Ḡ, P̄) outputs precisely so a **74182
lookahead-carry generator** can build a fast wide ALU — i.e. the chip is engineered around the
prefix-carry structure of U1 §C. `settled (standard)` (function-table rows read from datasheet, not
recalled — `uncertain` for exact bit patterns).

---

## E. Cross-topic unification & where the textbook simplifies
- **MUX/decoder/PROM/LUT are one idea** (§A) — the single most important unification of this unit.
- **"MSI blocks are fixed functions" is a UG simplification:** in real design they're *generated* by
  the synthesizer from behavioral HDL (a `case` → MUX, a `+` → prefix adder); you rarely instantiate
  a 74xx. The blocks are mental models for what synthesis emits (→ `../../../verilog`). `settled`.
- **Glitches:** a MUX/decoder output can glitch on select transitions (function hazards) — fine when
  registered, dangerous if it gates a clock or async reset (→ U3/U4 timing). `settled`.

## F. Harder problems (§0 surplus test)
1. Derive the "2ⁿ⁻¹:1 MUX implements an n-var function" rule from Shannon expansion. ✓ (§A).
2. Show a MUX tree = a (reduced) BDD; when does the BDD blow up (e.g. multiplier middle bit)? ✓ (§A).
3. Recast an n-bit comparator as an O(log n) prefix network. ✓ (§B).
4. Compare barrel-shifter (combinational, log-depth) vs shift-register (sequential, n clocks) area/delay. ✓ (§C).
5. Explain how the 74181+74182 reuse the U1 prefix-carry structure for a fast wide ALU. ✓ (§D).

**§0 surplus exit (U2 Stage 2): PASS** — Shannon-expansion unification + prefix recasts answered from
mechanism; BDD/synthesis cited to Bryant/De Micheli; 74181 exact rows flagged `uncertain` (datasheet).

→ Frontier/open: LUT-based FPGA architecture & technology mapping (→ Verilog subject); approximate/
reconfigurable datapaths. Logged to register.
