# U1 — Combinational Logic Design (Stage 1, MUJ level)

> Scope (verbatim syllabus block): *Boolean algebra & K-map overview; half & full adders;
> subtractors; serial & parallel adders; BCD adder.* Number systems/codes folded in as prereq.
> Tier-1: Anand Kumar 2e, Jain 4e, Brown & Vranesic 3e; load-bearing forms triangulated vs IIT-R
> Virtual Labs + manufacturer/standard references (`sources.md`). Confidence per claim inline.

---

## 0. The frame (deep structure first)

A **combinational** circuit = output is a pure function of present inputs (no memory, no feedback).
Design always factors into: **(1) capture the function** (truth table / Boolean expression) →
**(2) minimize it** (algebra / K-map / Q–McCluskey) → **(3) realize it** (gates, or an MSI block).
Every block in this unit and the next is this same pipeline. `settled`.

---

## 1. Boolean algebra — the algebra of {0,1}

**Operators:** AND (·, conjunction), OR (+, disjunction), NOT (′/overbar). XOR (⊕) and XNOR are
derived. A Boolean function of *n* variables is fixed by its **truth table** (2ⁿ rows). `settled`.

**Axioms / key theorems** (all `settled` — triangulated, standard across all three texts):
- Identity: A+0=A, A·1=A. Null: A+1=1, A·0=0. Idempotent: A+A=A, A·A=A.
- Complement: A+A′=1, A·A′=0. Involution: (A′)′=A.
- Commutative, Associative, Distributive (both ways: A+BC=(A+B)(A+C) — the OR-over-AND distributive
  law is the one novices forget). `settled`.
- **De Morgan (the workhorse):** (A+B)′ = A′·B′ and (A·B)′ = A′+B′. Generalizes to *n* vars.
  Mechanism: complementing a function = complement every literal **and** swap AND↔OR. This is *why*
  any AND-OR circuit converts to NAND-only (bubble-pushing). `settled`.
- **Consensus:** AB + A′C + BC = AB + A′C (the BC term is redundant). Useful for hazard removal (U4).
  `settled`.
- **Absorption:** A+AB=A, A(A+B)=A; A+A′B=A+B. `settled`.

**Canonical forms.** Any function has two canonical (fully-expanded) forms:
- **SOP / sum of minterms** — OR of minterms (each minterm = AND term where the function = 1, every
  variable present true-or-complemented). Notation f = Σm(…). 
- **POS / product of maxterms** — AND of maxterms (each maxterm = OR term where function = 0).
  f = ΠM(…). The maxterm list is the complement of the minterm list. `settled`.
- A minterm has a 1 in exactly one truth-table row; minterm mᵢ and maxterm Mᵢ are complements
  (Mᵢ = mᵢ′). `settled`.

**Functional completeness (threshold — big idea 3).** {AND,OR,NOT} is complete. **NAND alone is
complete; NOR alone is complete** (each can build NOT, AND, OR). Proof sketch (NAND): NOT = NAND(A,A);
AND = NOT(NAND(A,B)); OR = NAND(A′,B′) = NAND(NAND(A,A),NAND(B,B)). `settled` (standard; Brown &
Vranesic). This is why hardware is built from one repeated cell.

---

## 2. Minimization — K-maps and Quine–McCluskey

**Why minimize:** the same function has many gate realizations; fewer literals/gates → less area,
power, delay. Minimization ≠ changing the function (misconception **M1**). `settled`.

**Karnaugh map (K-map).** A 2ⁿ-cell grid whose rows/cols are **gray-coded** so physically adjacent
cells differ in exactly one variable. *That* adjacency = the Boolean adjacency XY+XY′=X — so grouping
adjacent 1-cells **eliminates** the variable that changes across the group (threshold concept). `settled`.
- **Grouping rules** (`settled`): groups must be rectangles of **2ᵏ** cells (1,2,4,8,16); a group of
  2ᵏ cells removes **k** variables; groups may **wrap around** edges (and corners on a 4-var map) —
  the map is a torus; use the **fewest, largest** groups that cover all 1s; overlap is allowed; each
  group ⇒ one product term (SOP) using the variables constant across it.
- **POS via K-map:** group the **0s** to get f′ in SOP, then complement (De Morgan) → POS. `settled`.
- **Don't-cares (×):** input combinations that can't occur or whose output is irrelevant; assign each
  × as **0 or 1 — whichever enlarges a group** (misconception **M3**). `settled`.
- **Prime implicant** = a group that can't be enlarged; **essential PI** = the only PI covering some
  minterm (must be in the cover). Minimal SOP = all essential PIs + a minimum set of others to cover
  the rest. `settled`.
- Practical limit: K-maps are clean to **4 variables**, workable to **5–6** (stacked maps); beyond
  that → Quine–McCluskey / CAD. `settled`.

**Quine–McCluskey (tabular method).** Algorithmic, exam-tested for 4–5 vars; the systematic version
of K-mapping. `settled`:
1. List minterms (+ don't-cares) in binary, group by number of 1s.
2. Combine pairs differing in one bit (mark the differing bit with –), repeat across columns until no
   more combine. Terms never combined = **prime implicants**.
3. Build a **PI chart** (PIs × minterms); select essential PIs, then cover the rest minimally
   (Petrick's method for the final selection if ambiguous).
- Don't-cares are *used* to form larger PIs but **need not be covered** in the final chart. `settled`.

**Worked-pattern (exam staple):** "Minimize f(A,B,C,D)=Σm(…)+Σd(…) using a K-map." Method: plot 1s
and ×s on the 4×4 map (rows AB in gray order 00,01,11,10; cols CD likewise) → ring largest 2ᵏ groups,
using ×s freely, wrapping edges → read each group as a product term → OR them. *Always state the
gray-code ordering and which variable each group drops.* 

---

## 3. Adders

**Half adder (HA)** — adds two bits, no carry-in. `settled` (triangulated, universal):
- Sum **S = A ⊕ B**; Carry **C = A·B**. (Sum = parity; carry = AND.)

**Full adder (FA)** — adds A, B, and carry-in Cin. `settled`:
- **S = A ⊕ B ⊕ Cin** (parity of the three inputs).
- **Cout = AB + Cin(A⊕B)** = AB + ACin + BCin (majority function — 1 when ≥2 inputs are 1).
- Build from two HAs + one OR: HA1(A,B)→(s1,c1); HA2(s1,Cin)→(S,c2); Cout=c1+c2. `settled`.

**Half subtractor (HS)** — A−B. `settled` (triangulated IIT-R Virtual Labs + tutorialspoint):
- Difference **D = A ⊕ B**; Borrow **Bout = A′·B**. (Borrow when A=0,B=1.)

**Full subtractor (FS)** — A − B − Bin. **Verified this session** (triangulated: IIT-R Virtual Labs,
tutorialspoint, GeeksforGeeks) `settled`:
- **D = A ⊕ B ⊕ Bin.**
- **Bout = A′B + Bin(A⊕B)′ = A′B + A′Bin + B·Bin.** (Both forms equivalent; the second is the
  3-term SOP from the K-map. Note the structural parallel to FA's Cout, with A complemented.)
- Subtraction in practice is usually done by **2's-complement addition** (A − B = A + B̄ + 1), so
  dedicated subtractor logic is mostly pedagogical — but the FS is exam-tested. `settled`.

---

## 4. Multi-bit adders — serial, parallel (ripple), and carry-lookahead

**Parallel / ripple-carry adder (RCA).** n full adders chained, Cout of stage i → Cin of stage i+1.
Simple, but the **carry ripples** → worst-case delay ∝ n (each stage waits for the previous carry).
For n bits, delay ≈ n·(FA carry delay). `settled`. This delay is *the* motivation for lookahead.

**Serial adder.** One full adder + a clocked carry flip-flop; bits fed LSB-first one per clock, sum
shifted into a register. Trades hardware (1 FA) for time (n clocks). It's actually a tiny **sequential**
circuit (the carry FF holds state) — a bridge to U3. `settled` (standard; confirm exact register
arrangement vs Jain in deep pass). 

**Carry-lookahead adder (CLA).** Removes the ripple by computing carries in parallel. Define per bit:
- **Generate Gᵢ = AᵢBᵢ** (this stage makes a carry regardless), **Propagate Pᵢ = Aᵢ ⊕ Bᵢ** (this
  stage passes an incoming carry). Then **Cᵢ₊₁ = Gᵢ + Pᵢ·Cᵢ**. `settled`.
- Unrolling: C₁=G₀+P₀C₀; C₂=G₁+P₁G₀+P₁P₀C₀; … each carry is a 2-level (SOP) function of the inputs →
  **constant delay** (≈ independent of n), at the cost of more gates / fan-in. Sum Sᵢ = Pᵢ ⊕ Cᵢ.
  `settled`. (Some texts define Pᵢ = Aᵢ+Bᵢ for the carry equation; Aᵢ⊕Bᵢ for the sum. Both give the
  same carry because when Aᵢ⊕Bᵢ=0 but Aᵢ+Bᵢ=1 we have Gᵢ=1 anyway. Note this in teaching. `settled`.)

**Exam pattern:** "Design a 4-bit CLA / show ripple delay vs lookahead." Method: write Gᵢ, Pᵢ; expand
C₁…C₄ as SOP; count gate levels (2 for carries) vs n for ripple.

---

## 4½. Codes & code converters (combinational design problems)

Binary codes are an assumed prereq, but **code converters** are canonical combinational design
exercises (NPTEL-standard) — each is "truth table → K-map → gates." `settled`:
- **Binary ↔ Gray:** Gray is **unit-distance** (successive codes differ in 1 bit → no decoding glitch;
  why K-maps use it, §2). Bin→Gray: gᵢ = bᵢ ⊕ bᵢ₊₁ (MSB unchanged). Gray→Bin: bᵢ = gᵢ ⊕ bᵢ₊₁
  (prefix-XOR from MSB). `settled`.
- **BCD ↔ Excess-3:** Excess-3 = BCD + 3; it is **self-complementing** (9's complement = bit-complement)
  → eases BCD subtraction (deepened in `stage-2/01`). `settled`.
- **Parity generator/checker:** an XOR tree appends/checks a parity bit (single-error *detection*) —
  the entry point to error-control coding (Hamming SEC/SEC-DED, → `stage-2/01` §F enrichment). `settled`.

---

## 5. BCD adder

**Problem:** BCD encodes each decimal digit in 4 bits (0000–1001). A plain 4-bit binary adder on two
BCD digits gives a *binary* sum 0–19, but **0–9 only** are valid BCD. **Verified this session**
(triangulated: GeeksforGeeks, eeeguide, Anand Kumar treatment) `settled`:
- **Correction:** if the 4-bit sum **> 9** OR a **carry-out** was produced, **add 0110 (6)** to skip
  the six unused codes 1010–1111 and generate the correct decimal carry.
- **Correction-trigger logic:** **Y = Cout + S₃S₂ + S₃S₁**, where S₃S₂S₁S₀ is the first adder's sum.
  (S₃S₂ catches sums 12–15; S₃S₁ catches 10–11; Cout catches 16–19.) Y also becomes the **carry to
  the next decimal digit.** `settled`.
- **Structure:** top 4-bit adder forms the raw sum; the detect logic computes Y; a **second 4-bit
  adder** adds `0Y Y0`=0110 (when Y=1) or 0000 (when Y=0) to the lower sum. `settled`.

**Exam pattern:** "Design a 1-digit BCD adder / add two BCD numbers showing correction." Always show
the >9-or-carry test and the +6 step.

---

## 6. Worked-problem patterns this unit must cover (Stage-1 exit targets)
1. Minimize a 4-var SOP with don't-cares by K-map; give minimal SOP **and** POS. 
2. Derive FA from two HAs; write S, Cout; extend to a 4-bit RCA and state its delay.
3. Full subtractor D, Bout from the truth table via K-map (get the verified forms above).
4. CLA: write Gᵢ, Pᵢ, expand carries, compare gate-delay with ripple.
5. BCD adder: add 0111+0110, show the >9 detect and +6 correction → 0001 0011.
6. Quine–McCluskey on a 4-var function with don't-cares; identify essential PIs.

## Stage-1 exit test (this unit)
Representative (no PYQ yet → textbook-level, exam-targeting `uncertain`): **(a)** Minimize
f(A,B,C,D)=Σm(1,3,7,11,15)+d(0,2,5) and realize NAND-only. **(b)** Add BCD 1001+0101 with correction.
**(c)** Give full-subtractor Bout in minimal SOP. → All answerable from §1–§5 mechanism with the
verified forms. **PASS** (mechanism shown; targeting unconfirmed pending PYQs).

---

→ **Stage 2** (`stage-2/01-...md`, when built) will add: the lattice/ring-theoretic view of Boolean
algebra; Q–McCluskey complexity + Petrick's method proof; carry-lookahead as a parallel-prefix
(Kogge-Stone/Brent-Kung) problem and its log-depth optimality; carry-save/carry-select adders;
why subtraction = 2's-complement addition derived from modular arithmetic; threshold/multi-valued logic.
