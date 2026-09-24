# Circuits & Systems — handwritten class notes, transcribed + verified

**Source:** `NOTES-handwritten-2026-09.pdf` (23 pages, the learner's own notebook, scanned 12-Sep-2026).
**Transcribed:** 2026-09-25. Every formula re-derived by hand, every worked answer recomputed.
Checked against the textbook-sourced KB in `../../06-circuits-and-network-theory/knowledge-base/`
(`01-network-theorems.md`, `02-transient-analysis.md`), Alexander & Sadiku ch. 1, and 7809 datasheets.

**Honesty rule:** these are class notes. They show **what the professor covers and how** (scope and
emphasis). They are **not** the authority on facts; the textbook is.

**Legend:**
- ✅ correct as written
- ⚠ **slip, gap or caution**, with the fix
- ❓ couldn't read it with certainty, or the question is ambiguous. My best reading is given.
- *(my addition)* = not in the notes; added so the page is complete.

---

## Summary (read this first). Re-checked 2026-09-25

**Bottom line: none of the teacher's methods or concepts is wrong.** Every procedure (VDR, CDR, source
transformation, superposition, Thévenin, Norton, MPT derivation, the 0⁻/0⁺/∞ transient method, the
first-order formula) matches the textbook. Every numeric answer checks out once units are read consistently.
I re-read each flagged spot at high resolution and **simulated every circuit** with a nodal solver
(results in `../progress-log.md`). My first pass called 5 things "errors"; after this re-check, the list is:

**Slips of the pen / copying (the concept is right; just read them correctly):**

| # | Page | Written | Read it as |
|---|------|---------|------------|
| S1 | 3 | d/dt(**C**I) = **C** dI/dt for the inductor | **L** di/dt. The side box on the same page correctly has ψ = Li, so this is a pen slip |
| S2 | 7–8 | resistors labelled "4k", "2k"; answer **3 A** | The teacher's working (10×2/6 = 10/3 V → 5/3 A) treats them as **4 Ω and 2 Ω**. With ohms, a full-circuit simulation gives **exactly 3 A** ✅. Only the "k" labels clash |
| S3 | 5 | "I₂ + I₃ = 6×4/10 = 2.4" | the **resistance** 6‖4 = 2.4 (a label slip; the arithmetic is fine) |
| S4 | 16 | "0 5 mW" | ❓ no decimal point is visible. The correct value is **5 mW** (10 V × 0.5 mA); the 50 % efficiency is right either way |

**Wording to tighten (not a calculation issue):**
- p.2 "active element doesn't require any external energy source": taken literally, this conflicts with the next
  line (an amplifier needs a DC supply). The safer textbook wording (Alexander & Sadiku): an active element
  **can generate/deliver energy**; a passive one cannot.

**Question to clarify with the teacher (your notes stop partway):**
- p.22–23 RL question: I_R(0⁺) = 0 and I_L(0⁺) = 10 mA can't both hold in one **series** loop. The teacher's
  point (inductor current can't jump → 10 mA) is right. What's missing is where that current goes after
  the switch opens. Most likely the full board question had a discharge path.

**Textbook points worth adding (the teacher may cover them later; not errors):**
- G1 superposition does **not** apply to **power** (find the currents, add them, *then* P = I²R)
- G2 when switching sources off, **dependent sources stay on**
- G3 **P_max = V_Th² / (4R_Th)**

---

## p. 1 — Title, books, first question, element taxonomy

**Circuits & Systems**

Books:
1. Alexander & N.O. Sadiku (theory + practice)
2. Van Valkenburg (theory)
3. A.K. Chakraborty (numerical practice)

❓ The words in brackets are faint pencil. I read them as "(Theory + Practice)", "(Theory)" and "(Numerical Practice)".

**Question: infinite ladder, find R_eq.**
Shunt 3k → series 5k → shunt 7k → series 11k → shunt 13k → … ∞

*(No solution in the notes.)* *(My addition:)* R_eq = 3k ‖ (5k + 7k ‖ (11k + 13k ‖ (…))).
The values are the primes 3, 5, 7, 11, 13, … Assuming that pattern continues, the value converges
numerically to **R_eq ≈ 2.318 kΩ**. Truncations: 3 resistors give 2.400 kΩ, 5 give 2.329 kΩ, 9 give 2.318 kΩ.
❓ This is my calculation under an assumed pattern. Confirm the intended continuation with the
professor. The usual "the ladder looks the same after one section" trick does **not** work here,
because the values change from section to section.

**Basic circuit elements** ✅
```
Basic Circuit Element
├── Active
│   ├── Independent:  Voltage Source (V.S), Current Source (C.S)
│   └── Dependent:    VCVS, VCCS, CCCS, CCVS
└── Passive:  R, L, C
```
⚠ The notes write "V.D.V.C"; it should be **V.D.V.S** (voltage-dependent voltage source). Textbooks call these
*voltage-controlled* / *current-controlled* sources: VCVS, VCCS, CCVS, CCCS.

## p. 2 — Active elements, dependent sources

**Active element:**
- Delivers energy / power ✅
- "Doesn't require any external force or energy source": loose wording. Taken literally, it conflicts with the
  next line (an amplifier needs a DC supply). Alexander & Sadiku: *"An active element is capable of generating
  energy while a passive element is not."*
- Amplifier is also an active element ✅ (but it takes its energy from a DC supply)

**Dependent sources:** active elements whose value depends on another circuit variable (not constant) ✅
1. Voltage-dependent voltage source (VCVS)
2. Voltage-dependent current source (VCCS)
3. Current-dependent voltage source (CCVS)
4. Current-dependent current source (CCCS)

**Symbols** ✅ A **diamond** is a dependent source; a **circle** is an independent source. `+/−` inside means a voltage source; an **arrow** inside means a current source.
Drawn examples: diamond(+/−) V₁ = VCVS · diamond(+/−) 3I₁ = CCVS · diamond(↑) 2V₁ = VCCS · diamond(↑) 3I₁ = CCCS ·
circle(+/−) 2 V, battery 8 V, circle(↑) 2 A = independent.
Side scribbles "741" next to the VCVS and "BC547" next to the CCCS ✅: an op-amp is modelled as a VCVS, and a BJT
as a CCCS (I_C = β·I_B).

## p. 3 — Passive elements

1. **R**: dissipates heat (ohmic losses); Ohm's law V ∝ I ⇒ **V = IR** ✅
2. **L**: stores energy in a **magnetic field** ✅. The note "the current is stored" is loose wording: it stores **energy**,
   W = ½Li².
   Side box: ψ = Nφ, ψ ∝ i, ψ = Li ✅
   v = dψ/dt = d(Nφ)/dt = d(Li)/dt = **L di/dt** ✅ (S1: the notes write "C" here, a pen slip; the side box has ψ = Li)
   ★ **Inductor doesn't allow a sudden change in current** ✅ (a jump would need infinite voltage)
3. **C**: stores energy in an **electric field** ✅ ("stores voltage" is loose; W = ½Cv²)
   Q ∝ V ⇒ Q = CV → differentiate: dQ/dt = d(CV)/dt ⇒ *(completing the line)* **i = C dv/dt** ✅
   ★ **Capacitor doesn't allow a sudden change in voltage** ✅

## p. 4 — Source transformation, voltage and current division

**Notation** (✅ standard convention): uppercase I, V = DC (constant); lowercase i, v = AC, or more generally time-varying / instantaneous.

**Source transformation** ✅: voltage source V in series with R ⇔ current source **I = V/R** in parallel with the same R.

**Voltage division rule** ✅ (R₁, R₂ in series across V):
V₁ = V·R₁/(R₁+R₂), V₂ = V·R₂/(R₁+R₂)

Q: 15 V across 3 kΩ + 6 kΩ in series → V₁ = 15×3/9 = **5 V**, V₂ = 15×6/9 = **10 V** ✅

**Current division rule** ✅ (I into R₁ ∥ R₂): I₁ = I·R₂/(R₁+R₂), I₂ = I·R₁/(R₁+R₂). Each branch gets the *other* resistor on top.

## p. 5 — Current division with three branches; AC voltage division

**Q:** a 12 A source feeding 3k ∥ 6k ∥ 4k.
- I₁ (3k) = 12 × 2.4/(2.4+3) = **5.33 A** ✅ (2.4k = 6k‖4k)
- I₂ (6k) = 12 × (12/7)/(6 + 12/7) = **2.67 A** ✅ (12/7 k = 3k‖4k)
- I₃ (4k) = 12 × (18/9)/(2+4) = **4 A** ✅ (2k = 3k‖6k)
- Check: 5.33 + 2.67 + 4 = 12 ✅ (also V = 12 × 4/3 k, and I = V/R per branch gives the same numbers)
- (S3) the side-note "I₂ + I₃ = 6×4/10 = 2.4" is the **resistance** 6k‖4k = 2.4 kΩ, not a current.
- The first attempt, struck through in the notes, is correctly discarded.

**Q:** v = 10 sin(2kt + 30°) across 3k + 7k in series. Let x be the source voltage.
- v₁ = 0.3x = **3 sin(2kt + 30°)**, v₂ = 0.7x = **7 sin(2kt + 30°)** ✅
- Division works on AC too, because resistors don't shift phase. ❓ "2kt" most likely means 2000t, i.e. ω = 2000 rad/s.

## p. 6–7 — Superposition theorem

**Statement** ✅: when a circuit contains several active sources, the response across any element is the
**algebraic sum** of the responses produced by each source acting alone.

**Key features:**
1. Applicable to **linear** bidirectional/bilateral circuits. ✅ Strictly, the requirement is **linearity**;
   "bilateral" is the traditional add-on in Indian textbooks.
2. Makes a complex circuit easier to solve ✅

**Limitations:**
1. Doesn't work for non-linear circuits ✅
2. Doesn't work for unidirectional / unilateral circuits (e.g. diodes) ✅
3. "Sometimes gives false results in the case of ideal circuits" ❓. *My reading:* this is the case of **ideal
   sources that can't be switched off one at a time**, e.g. two ideal voltage sources in parallel. Shorting one
   shorts the other (see the p. 9 question).
- ⚠ **(G1) textbook addition:** superposition does **not** apply to **power**. Find each current by superposition, add them,
  *then* compute P = I²R. Summing the individual powers gives the wrong answer.

**NOTE** (faint pencil, ❓ partly guessed; the meaning is clear): when a single source is active, the remaining
sources are replaced by their **internal resistance**:
- ideal voltage source: internal R = 0 → **short circuit** ✅
- ideal current source: internal R = ∞ → **open circuit** ✅
- ⚠ **(G2)** this applies to **independent** sources only. **Dependent sources stay active in every sub-circuit.**

## p. 7–8 — Superposition worked example

**Q:** find I (through the 2k) by superposition. 10 V source → series 4k → node A. From A: 2k down to ground (I),
and a 2 A current source (arrow up, feeding A).

- **Case 1**: 10 V only (current source → open):
  V₂ₖ = 10 × 2/6 = **10/3 V** ✅ → I₁ = (10/3)/2 = **5/3 A** ✅ (with 2 Ω; see S2)
- **Case 2**: 2 A only (10 V → short): the 4k and 2k are now in parallel.
  I₂ = 2 × 4/6 = **4/3** (in the source's units) ✅
- **Step 3**: I = I₁ + I₂ = 5/3 + 4/3 = **3 A** ✅ (verified by simulating the whole circuit with both sources on).
  - (S2) This holds when the resistors are **4 Ω and 2 Ω**, which is how the working treats them. With literal
    "4k/2k" and a 2 A source, the answer would be 1.335 A; with 2 mA it would be 3 mA. Just keep the units consistent.

## p. 9 — Superposition question (unfinished)

**Q:** find I₁ by superposition. Left 5 V source, right 5 V source, 1 kΩ between the top and bottom rails.
Step 1 in the notes draws only the left 5 V with the 1k; the right source is simply *removed*.

*(My reading. The notes stop after Step 1.)* Both sources (+ at the top, confirmed at high zoom) connect
**directly across the 1k**, so they are ideal voltage sources in parallel. This is almost certainly the teacher's
**example of limitation 3** ("gives false results for ideal circuits"):
- by superposition: 5 V alone → 5 mA, and the other 5 V alone → 5 mA, so the "sum" is **10 mA** ✗
- actual: the 1k simply sees 5 V → **I₁ = 5 mA** ✅
- (and strictly, "switching off" one source means **shorting** it, which would short the other one. So superposition can't even be applied properly here.)

## p. 10–11 — Thévenin's theorem

- Applies to **linear**, bidirectional/bilateral circuits ✅
- **Process:**
  1. Remove the load (R_L or Z_L) ✅
  2. Calculate **V_Th** across the load terminals (the open-circuit voltage) ✅
  3. Calculate **R_Th / Z_Th** across the load terminals ✅
  4. Redraw: V_Th in series with R_Th (Z_Th), feeding R_L (Z_L) → **I_L = V_Th/(R_Th + R_L)** ✅
- **Note: with dependent sources**, find the equivalent resistance with a test source: apply V_dc at the terminals,
  measure I_dc, then **R_Th = V_dc/I_dc** (Z_Th for AC) ✅. ("average equivalence resistance" in the notes = *equivalent* resistance.)
  ⚠ The notes' figure still shows the input source V_in. Before applying the test source, **switch off the independent
  sources** (V_in → short) and keep the dependent ones. Alternative that always works: **R_Th = V_oc / I_sc**.

**Cloud box** ✅: V = 0 or R = 0 ⇒ short circuit; I = 0 or R = ∞ ⇒ open circuit.

**Q (p. 11):** find the load current using Thévenin. 10 V → 2k (current I →) → node A. From A: 2k in series with a
dependent source **2I** (+ on top) to ground. From A: 2k → node B. R_L = 1k from B to ground.
The notes stop at Step 1 (setting up V_Th). *(Completed by me; units V, mA, kΩ, so "2I" = 2 kΩ × I. ❓ confirm that is the intended unit.)*
- **V_Th** (R_L removed; no current in the right 2k, so V_Th = V_A):
  KCL at A: (10 − V_A)/2 = (V_A − 2I)/2 with I = (10 − V_A)/2 → V_A = 4I, I = 5/3 mA → **V_Th = 20/3 ≈ 6.67 V**
- **I_sc** (B shorted to ground): V_A = 2I, I = 2.5 mA → V_A = 5 V → **I_sc = 2.5 mA**
- **R_Th = V_oc/I_sc = 8/3 ≈ 2.67 kΩ**. The test-source method gives the same value: 2k + (2k ‖ 1k-equivalent) = 2 + 2/3 kΩ.
- **I_L = 6.67/(2.67 + 1) = 20/11 ≈ 1.82 mA**. Cross-checked by solving the full circuit directly: same answer.

## p. 12 — Projects (lab / PBL, not theory)

- **Project 1:** website → Tinkercad → Arduino; pin 3 → LED (+) (red); GND → LED (−).
  ⚠ *(My addition, safety)* put a **series resistor** (220–330 Ω) in line with the LED. Otherwise the pin/LED current isn't limited.
- **Project 2:** components: 1N4007 × 4 · 10 µF, 1 µF × 1 each · 7809 × 1 · red/black leads → "C type" (USB-C?) · probe ·
  jumper wires (M-M) · breadboard. ❓ "C type" reading.

## p. 13–14 — Maximum power transfer theorem

**Statement:** the theorem gives the maximum power that can be delivered to the load.
- Step 1: apply Thévenin. Step 2: V_Th, R_Th feeding R_L.
- I_L = V_Th/(R_Th + R_L) ✅
- ⚠ The first attempt, P_L = V_Th²/(R_Th+R_L) with its derivative, is **wrong**; the notes rightly cross it out and restart.
- ★★ **P_L = I_L² R_L = V_Th² R_L / (R_Th + R_L)²** ✅
- dP_L/dR_L = V_Th² · [(R_Th+R_L)² − R_L·2(R_Th+R_L)] / (R_Th+R_L)⁴ = 0 ✅
- (R_Th+R_L)² − 2R_L(R_Th+R_L) = 0 → R_Th² + R_L² + 2R_Th·R_L − 2R_Th·R_L − 2R_L² = 0 → R_Th² − R_L² = 0 ✅
- ⇒ **R_L = R_Th** ✅
- ⚠ **(G3)** *(my addition)*: substituting back gives **P_max = V_Th² / (4 R_Th)**

## p. 15 — Norton's theorem ✅

1. Applies to linear circuits. 2. Valid for bidirectional/bilateral circuits. 3. Analogous to Thévenin's theorem.
4. Procedure: (i) remove the load R_L/Z_L; (ii) find the equivalent resistance/impedance across the load terminals
   (exactly as for Thévenin); (iii) replace the load by a short circuit and find the short-circuit current **I_N**;
   (iv) Norton equivalent: I_N in parallel with R_Th (Z_Th), feeding R_L (Z_L).
- *(my addition)* link to Thévenin: **I_N = V_Th / R_Th**, R_N = R_Th (it is just a source transformation).

## p. 16–17 — Maximum power for impedances, and questions

- **Condition: Z_L = Z_Th\*** (the complex conjugate: j → −j) ✅ i.e. R_L = R_Th and X_L = −X_Th.

**Circuit:** 10 V, 10 kΩ series, variable R_L.
- Q1 value of R_L for maximum power: **R_L = R_Th = 10 kΩ** ✅
- Q2 total power delivered by the source: I = 10/20k = **0.5 mA** ✅ → P = V·I = 10 × 0.5 mA = **5 mW** (S4: the notes read "0 5 mW" ❓)
- Power in the load: P_L = I²R_L = (0.5 mA)² × 10k = **2.5 mW** (= V_Th²/4R_Th ✅)
- Q3 power consumed by R_Th: **2.5 mW**
- Q efficiency: η = P_L/P_total × 100 = 2.5/5 × 100 = **50 %** ✅ (the notes' 0.25/0.5 has the same ratio)
- Voltage across the load = **5 V** ✅
- Relation between load voltage and source voltage: **V_L = V_s/2** ✅
- **NOTE** (resistive network at P_max) ✅: V_L = V_s/2, P_L = P_s/2 (half the supplied power reaches the load, the other half is lost in R_Th).
  *(Caveat from the KB: the 50 % applies to the Thévenin equivalent. It is not necessarily the efficiency of the original, full circuit.)*

**Q:** 10 V, 5 kΩ series, find R for maximum power, P_max, and η.
*(No solution in the notes.)* *(Mine:)* **R = 5 kΩ**, P_max = 10²/(4×5k) = **5 mW**, **η = 50 %**.

## p. 18 — Lab circuit (Project 2)

Function generator (sine, **20 Vpp**, 50 Hz) → bridge rectifier (4 × 1N4007) → capacitor C → **7809** → connector ("C type" → "Mob…", ❓ probably *mobile*).

⚠ *(My addition, `likely`, please check with the lab instructor):*
- 20 Vpp = **10 V peak**. The bridge drops about 2 × 0.7 V, leaving **≈ 8.6 V peak**. A 7809 needs **about 11 V minimum input**
  (2 V dropout). So it **cannot regulate to 9 V** from this input.
- If the output really goes to a **phone through USB-C**: plain USB is **5 V**. A 7809 puts out **9 V**; don't plug that
  into a phone. A 5 V charger would use a **7805**.

## p. 19–20 — Transient analysis

Timeline: t = −∞ … 0⁻ (**steady state**) → 0⁻, 0, 0⁺ (**transient state**) → t ≈ 5τ → ∞ (**steady state**) ✅
(after 5τ the response is ~99 % settled).
- t = 0: the switching instant ("present time")
- t = 0⁻: just **before** the switch operates ✅
- t = 0⁺: just **after** the switch operates ✅

**Example:** V, switch (closes at t = 0), R.
- Step 1, t = 0⁻: switch open, steady state → **I(0⁻) = 0** ✅
- Step 2, t = 0⁺: switch closed → **I(0⁺) = V/R** ✅
- Step 3, t = ∞: switch closed, steady state → **I(∞) = V/R** ✅
- **Note: a resistor allows sudden changes in voltage and current** ✅. *(my addition:)* so a purely resistive circuit
  has **no** transient; it jumps straight to its final value.

## p. 21 — RL circuit, switch closes

V, switch (closes at t = 0), R in series with L.
- t = 0⁻: switch open → I_R(0⁻) = 0, I_L(0⁻) = 0 ✅
- t = 0⁺: switch closed; the inductor current can't jump → **I_L(0⁺) = 0**, so the inductor acts as an **open circuit** at 0⁺ ✅ → I_R(0⁺) = 0 ✅
- t = ∞: steady state; the inductor acts as a **short circuit** → **I(∞) = V/R** ✅
- *(my addition)* in between: i(t) = (V/R)(1 − e^(−t/τ)), with τ = L/R.

## p. 22–23 — General first-order solution + RL question

★ **x(t) = [x(0⁺) − x(∞)] · e^(−t/τ) + x(∞)** ✅, where τ is the circuit's time constant.
Valid for: RL ✅, RC ✅; **not** for RLC ✗ or LC ✗ (those are second order) ✅.
- **τ = RC** (RC circuit) ✅ · **τ = L/R** (RL circuit) ✅ (R = the Thévenin resistance seen by the L or C)

**Q:** 10 V, switch (**opens** at t = 0), 1 kΩ, 1 mH, all in **series**.
- Step 1, t = 0⁻: switch closed, steady state, inductor = short → **I_L(0⁻) = 10 V/1 kΩ = 10 mA** ✅
- Step 2, t = 0⁺: switch open → **I_L(0⁺) = 10 mA** ✅ (continuity), and the notes write I_R(0⁺) = 0.
- ❓ **To clarify:** in a single series loop, R and L carry the **same** current, so I_R ≠ I_L is impossible. Opening a switch in series
  with a current-carrying inductor has **no ideal solution**: di/dt → ∞ and the voltage spikes (in real life, an arc at the
  switch). The original question most likely has **another path** (e.g. the switch moves the R-L onto a discharge
  path, or there is a resistor in parallel). ❓ Check the board/textbook version.
  *If* the RL loop discharges through its own 1 kΩ: τ = L/R = 1 mH/1 kΩ = **1 µs**, i(t) = **10 e^(−t/1µs) mA**.

---

## Sources used for the cross-check

- `../../06-circuits-and-network-theory/knowledge-base/01-network-theorems.md`: superposition (not for power; dependent sources never
  deactivated), Thévenin/Norton (test-source method, V_oc/I_sc), MPT (R_L = R_Th, conjugate match, 50 % caveat). That KB is textbook-sourced; see its `sources.md`.
- `../../06-circuits-and-network-theory/knowledge-base/02-transient-analysis.md`: continuity at 0⁺, τ = RC and L/R, ~99 % settled in 5τ.
- Alexander & Sadiku, *Fundamentals of Electric Circuits*, ch. 1 (active/passive definition):
  <http://doctord.dyndns.org/courses/textbooks/alexander-sadiku/AlexanderCh01finalR1.pdf>
- 7809 minimum input about 11 V, 2 V dropout: <https://components101.com/regulators/7809-voltage-regulator-pinout-datasheet-specifications>,
  <https://www.watelectronics.com/lm7809-voltage-regulator/> (vendor summaries, `likely`; confirm against the part's own datasheet).
- All numeric answers were recomputed independently (Python check of the ladder, the superposition sums and the Thévenin load current).
