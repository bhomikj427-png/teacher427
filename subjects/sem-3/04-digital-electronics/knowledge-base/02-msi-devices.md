# U2 — MSI Devices (Stage 1, MUJ level)

> Scope (verbatim): *comparators; multiplexers; encoder; decoder; driver & multiplexed display;
> barrel shifter; ALU.* These are **combinational** building blocks (U1 pipeline applies). Tier-1:
> Anand Kumar, Jain, Brown & Vranesic; comparator eqns triangulated vs IIT-KGP Vlabs + UTA notes.

---

## 0. Frame

MSI ("medium-scale integration") blocks are *pre-packaged combinational functions* — each is just a
minimized truth table you'd otherwise build by hand. The deep skill of this unit: **(a)** know each
block's function and standard IC, and **(b)** use them as *universal building blocks* — especially
the MUX and decoder as **function generators** (any Boolean function, no minimization needed). `settled`.

---

## 1. Magnitude comparator

Compares two n-bit numbers → three outputs (A>B, A=B, A<B), mutually exclusive. `settled`.
- **Equality:** A=B iff every bit equal. Bit-equality **xᵢ = Aᵢ ⊙ Bᵢ = (Aᵢ⊕Bᵢ)′** (XNOR). Then
  **(A=B) = x₃x₂x₁x₀** (AND of all bit-equalities). `settled`.
- **Greater-than (verified this session, triangulated 7485 datasheet form + UTA notes + IIT-KGP
  Vlabs):** scan from MSB; A>B at the most-significant bit where they differ with Aᵢ=1,Bᵢ=0:
  **(A>B) = A₃B₃′ + x₃A₂B₂′ + x₃x₂A₁B₁′ + x₃x₂x₁A₀B₀′.** `settled`.
- **Less-than:** symmetric — **(A<B) = A₃′B₃ + x₃A₂′B₂ + x₃x₂A₁′B₁ + x₃x₂x₁A₀′B₀.** Or simply
  (A<B) = (A>B)′·(A=B)′. `settled`.
- **Standard IC: 7485** (4-bit). **Cascading** for wider words via three expander inputs (I_{A>B},
  I_{A=B}, I_{A<B}): chain lower-nibble outputs → higher-stage cascade inputs. The least-significant
  stage is seeded I_{A=B}=1, I_{A>B}=I_{A<B}=0. `settled` (7485 datasheet). 

**Exam pattern:** design a 2-bit comparator from the truth table via K-map; cascade two 7485s to 8-bit.

---

## 2. Multiplexer (MUX) — data selector

2ⁿ data inputs, n select lines, 1 output: **Y = the selected input.** For a 4:1: 
**Y = S₁′S₀′I₀ + S₁′S₀I₁ + S₁S₀′I₂ + S₁S₀I₃.** General: Y = Σ (mᵢ of selects)·Iᵢ. `settled`.
- Standard ICs: 74151 (8:1), 74153 (dual 4:1), 74157 (quad 2:1). Usually have an **active-low enable**
  (misconception **M5** — read the bubble). `settled`.
- **MUX as universal function generator (threshold/high-value):** a 2ⁿ:1 MUX implements *any* n-var
  function by wiring select=variables, data inputs = the truth-table output column. Better: a 2ⁿ⁻¹:1
  MUX implements an n-var function — put n−1 vars on selects, and each data input = {0, 1, the nth
  var, or its complement} per the **Shannon-expansion residue**. `settled` (IIT-KGP Vlabs). This
  needs **no minimization** — the standard exam trick.
- **DEMUX** = inverse: 1 input → 2ⁿ outputs, routed by selects. A decoder with an enable *is* a DEMUX.
  `settled`.

**Exam pattern:** "Implement f(A,B,C)=Σm(…) using an 8:1 then a 4:1 MUX." Method: 8:1 — data=truth
column; 4:1 — AB on selects, each data input solved as a function of C (0/1/C/C′).

---

## 3. Encoder & decoder

**Decoder** — n inputs → 2ⁿ outputs, exactly one active for each input code. Each output = one
minterm. A 3-to-8 (74138, active-low outputs + enables) gives all 8 minterms of 3 vars. `settled`.
- **Decoder as function generator:** OR the needed minterm outputs (for active-low outputs, use a NAND
  to combine) → any SOP function. One decoder feeds *several* functions of the same variables. `settled`.
- Enable input turns the decoder into a **DEMUX** and allows expansion (cascade two 3:8 → 4:16). `settled`.

**Encoder** — inverse: 2ⁿ (one-hot) inputs → n-bit code. Plain encoder = OR gates. **Problem
(misconception M6):** breaks if **two inputs are active** at once (outputs a meaningless OR) and can't
distinguish all-zero from input-0. `settled`.
- **Priority encoder** fixes this: on multiple active inputs, encodes the **highest-priority** one;
  adds a **valid (V)** output to flag "≥1 input active." Standard IC: 74147 (10→4, decimal-to-BCD),
  74148 (8→3). `settled`.

**Exam pattern:** design an 8-to-3 priority encoder truth table + equations (use don't-cares for
lower-priority inputs); BCD-to-7-segment is a decoder design.

---

## 4. Display driver & multiplexed display

**Seven-segment display** (a–g segments; common-anode or common-cathode). A **BCD-to-7-segment
decoder/driver** (e.g. 7447 common-anode active-low, 7448 common-cathode) maps a BCD digit → segment
pattern. The "driver" part sources/sinks enough current to light the LEDs (and may have ripple-blank
in/out for leading-zero suppression). `settled` (Jain; 7447 datasheet — verify exact blanking pins in
deep pass, `likely`).
- **Multiplexed (time-multiplexed) display:** to drive D digits without D separate decoders, **share
  one decoder** and a **digit-select** that scans digits fast (> ~50–100 Hz) so persistence of vision
  makes all appear lit. Saves wiring/pins at the cost of a scan clock + drivers. Mechanism: only one
  digit is energized at a time; the eye integrates. `settled` (standard; exact refresh threshold
  `likely`, perception-dependent).

---

## 5. Barrel shifter

A **combinational** shifter that shifts/rotates an n-bit word by any amount **0…n−1 in one step**
(unlike a sequential shift register, which takes one clock per position — big contrast with U3).
`settled`.
- Built from **log₂n stages of 2:1 MUXes**: stage k shifts by 2ᵏ or not, controlled by shift-amount
  bit k. So an n-bit barrel shifter = n·log₂n MUXes, **constant (log-depth) delay**. `settled`
  (standard; triangulate exact gate count in deep pass).
- Supports logical/arithmetic shift and rotate by choosing the fill (0, sign bit, or wrapped bit).
  Central to ALUs/CPUs (single-cycle shifts). `settled`.

**Exam pattern:** show a 4-bit barrel shifter as two MUX stages (shift by 1, shift by 2); contrast
with shift register (combinational vs sequential, 1 step vs n clocks).

---

## 6. Arithmetic Logic Unit (ALU)

A combinational block that performs a **selected** arithmetic OR logic operation on two n-bit
operands, chosen by **function-select** lines. `settled`.
- Core = a parallel adder/subtractor (2's-complement) with **operand-conditioning logic** on the B
  input (true / complement / 0 / all-1) + a **mux on the output** to pick arithmetic vs logic result.
  Carry-in + B-invert give add/subtract/increment/decrement; the logic side gives AND/OR/XOR/NOT. `settled`.
- **Standard IC: 74181** — 4-bit ALU, 16 arithmetic + 16 logic functions via S₃S₀ + mode M + carry;
  cascadable, often with a 74182 carry-lookahead generator. (Function table is the exam reference, not
  memorized.) `settled` (74181 is the canonical teaching ALU; exact function-table rows `likely` —
  read from datasheet, don't recall).

**Exam pattern:** given an ALU function table, trace the output for a select code; explain how
B-invert + Cin produces subtraction (A + B̄ + 1).

---

## 7. Worked-problem patterns (Stage-1 exit targets)
1. Implement an arbitrary 3- or 4-var function with an 8:1 / 4:1 MUX (Shannon residues). 
2. Implement multiple functions of the same vars from one 3:8 decoder.
3. Design an 8→3 priority encoder (truth table with don't-cares → equations + valid bit).
4. Cascade 7485s for an 8-bit comparison; write the bit-equality/greater-than equations.
5. BCD-to-7-segment: derive segment 'a' equation from the K-map (don't-cares 1010–1111).
6. Barrel-shift a 4-bit word by 3; show the two MUX-stage control.

## Stage-1 exit test (this unit)
Representative (no PYQ → `uncertain` targeting): **(a)** Implement f(A,B,C,D)=Σm(0,2,5,7,8,10,13,15)
with an 8:1 MUX. **(b)** Write (A>B) for 4-bit A,B and cascade two 7485s. **(c)** Explain why a plain
encoder needs priority + valid. → answerable from §1–§6 with verified comparator/MUX forms. **PASS**
(mechanism shown; targeting unconfirmed).

---

→ **Stage 2** (`stage-2/02-...md`) will add: MUX/decoder trees + the Shannon-expansion theorem proof;
comparator as a parallel-prefix problem; barrel shifter vs funnel/log shifter delay analysis; the
74181's actual function-generation algebra (G/P internal structure); LUT-based FPGA logic as "MUX as
universal function" taken to its conclusion (→ `../../../verilog`).
