# U3 — Sequential Logic Design (Stage 1, MUJ level)

> Scope (verbatim): *latch; flip-flops — S-R, D, JK, T, master-slave JK, edge-triggered; ripple &
> synchronous counters; shift registers; timing analysis of sequential circuits.* This is the
> **memory** half of the subject (big idea 1 & 4). Tier-1: Anand Kumar, Jain, Brown & Vranesic; FF
> characteristic eqns triangulated vs Wikipedia(Excitation table)+GfG+edurev. **Highest threshold
> density — budget the most teaching time here.**

---

## 0. Frame — what makes a circuit *sequential*

Add **feedback** to combinational logic and output now depends on output before → the circuit
**stores state** (big idea 4). The storage element is the **flip-flop** (1 bit). A clock disciplines
*when* state updates. Two sub-families:
- **Asynchronous / level-sensitive** (latches): respond whenever inputs/enable change. Simple but
  race-prone.
- **Synchronous / edge-triggered** (flip-flops): update only at a clock **edge**. The basis of all
  reliable design. `settled`.

---

## 1. Latches (level-sensitive)

**SR latch** — cross-coupled NOR (or NAND) gates. `settled`:
- NOR version (active-high S,R): S=1,R=0 → Set (Q=1); S=0,R=1 → Reset (Q=0); S=R=0 → **hold**;
  S=R=1 → **forbidden** (both outputs 0, then a race on release). NAND version is active-low (S̄R̄).
- This is the irreducible memory cell: the feedback latches one of two stable states (bistable). `settled`.

**Gated (clocked) latch** — add an enable/clock: the latch follows S,R (or D) only while EN=1,
holds while EN=0. **Transparent** when enabled (output tracks input) — this transparency is the
problem edge-triggering solves. `settled`.

**D latch** — gated latch with D and D′ on the inputs → eliminates the forbidden state. Q follows D
while EN=1. Q⁺ = D (while enabled). `settled`.

---

## 2. Flip-flops (edge-triggered) — characteristic & excitation tables

A **flip-flop** samples its inputs only at the active **clock edge** (↑ or ↓), holding otherwise
(misconception **M9**: not "whenever clock is high"). The four types (**verified this session**,
triangulated):

| FF | Inputs | **Characteristic eqn** Q⁺ | Behaviour |
|----|--------|---------------------------|-----------|
| **SR** | S,R | **Q⁺ = S + R′Q**, with constraint **SR=0** | set/reset/hold; SR=1 forbidden |
| **D**  | D   | **Q⁺ = D** | transparent-free load; "delay" |
| **JK** | J,K | **Q⁺ = JQ′ + K′Q** | like SR but J=K=1 **toggles** (no forbidden state) |
| **T**  | T   | **Q⁺ = T⊕Q = TQ′ + T′Q** | T=1 toggle, T=0 hold |

All `settled` (Wikipedia Excitation-table, GfG, Anand Kumar agree).

**Excitation tables** (inverse: given present Q→desired Q⁺, what inputs?) — *the* tool for counter
design (§4). **Verified this session** `settled`:

| Q→Q⁺ | S R | J K | D | T |
|------|-----|-----|---|---|
| 0→0  | 0 × | 0 × | 0 | 0 |
| 0→1  | 1 0 | 1 × | 1 | 1 |
| 1→0  | 0 1 | × 1 | 0 | 1 |
| 1→1  | × 0 | × 0 | 1 | 0 |

(× = don't-care — JK's abundance of don't-cares is why JK gives the cheapest next-state logic.) `settled`.

**FF conversion** (exam staple): to convert FF-X→FF-Y, put Y's excitation needs through X's
excitation table and K-map the result. E.g. JK→D: J=D, K=D′. D→JK: D = JQ′+K′Q. `settled`.

---

## 3. The race problem, master-slave, and edge-triggering (★ threshold)

**Race-around (level-triggered JK at J=K=1):** while the clock is high *and* the gate delay <<
pulse width, the JK toggles repeatedly → output is indeterminate at clock-fall. `settled`
(misconception **M8**; verified — allaboutelectronics, GfG).

**Two standard fixes** (`settled`):
- **Master–slave JK:** two latches in series, clocked on opposite phases. Master loads while CLK=1,
  slave (output) loads while CLK=0 → output changes once per clock period, toggling at most once.
  (Classic "pulse-triggered"; has the **1's-catching** subtlety — master can catch a transient high.)
- **Edge-triggered (e.g. positive-edge D/JK):** captures inputs in a narrow window at the *edge* only.
  Cleaner; the modern standard. The level→edge distinction is the gateway to reliable sequential
  design (misconception **M7**: latch ≠ FF). `settled`.

**Asynchronous (direct) inputs:** PRESET/CLEAR override the clock to force Q=1/0 — used for
initialization, independent of the clock. `settled`.

---

## 4. Counters

A counter = FFs cycling through a state sequence on clock pulses. Two architectures (the contrast is
exam-central, misconception **M10**):

**Ripple / asynchronous counter.** FF0 clocked by the system clock; each next FF clocked by the
previous FF's output. Counts up/down by toggling (T=1 or JK=11). `settled`.
- Simple (n FFs → mod-2ⁿ), but carries **ripple delay**: stage delays accumulate, so the count is
  briefly *wrong* during propagation (decoding spikes / glitches), and **f_max falls as n grows**
  (worst path = n·t_pd,FF). `settled`.
- **Mod-N (non-2ⁿ):** detect the terminal count with a gate and asynchronously CLEAR (e.g. mod-10 =
  clear at 1010). Has a transient-state glitch hazard. `settled`.

**Synchronous counter.** **All FFs share one clock** → all update simultaneously, no ripple, higher
f_max. Next-state logic feeds each FF's inputs. **Design procedure** (the load-bearing method,
`settled`):
1. State diagram → **state table** (present → next).
2. Pick FF type; use its **excitation table** (§2) to find each FF's required inputs per transition.
3. **K-map each FF input** (and any output) as a function of present-state bits → minimal equations.
4. Draw the logic. (JK minimizes gates via its don't-cares.) `settled`.
- Up/down/mod-N by changing the next-state spec. Unused states should be checked for **self-start**
  (do they lead back into the main cycle?). `settled`.

**Exam pattern:** "Design a mod-6 synchronous counter using JK FFs" — full excitation-table → K-map
→ equations pipeline. Highest-value counter problem.

---

## 5. Shift registers

Cascade of FFs (usually D) sharing a clock; each clock shifts the stored word one position. `settled`.
- **Four data modes:** SISO (serial-in serial-out), SIPO (serial-in parallel-out), PISO
  (parallel-in serial-out), PIPO (parallel load). A **universal shift register** (74194) does all +
  left/right via a mode-select MUX on each FF input. `settled`.
- **Applications:** serial↔parallel conversion, delay lines, serial adder (U1), sequence generation.
- **Ring counter:** feed last output back to first → a single 1 circulates; n FFs → mod-n, one-hot,
  self-decoding (no decode gates) but inefficient (n states from n FFs). `settled`.
- **Johnson / twisted-ring counter:** feed *complemented* last output back → n FFs → **mod-2n**,
  with simple 2-input decode per state. `settled`.

**Exam pattern:** draw waveforms for a 4-bit SIPO loading 1011; design a mod-8 Johnson counter; ring
vs Johnson state-count comparison.

---

## 6. Timing analysis of sequential circuits (★ threshold)

Real FFs/gates have finite timing — logical correctness ≠ hardware correctness (misconception M11).
`settled`:
- **Propagation delay t_pd (clk→Q):** time from active edge to output valid.
- **Setup time t_su:** input must be stable *before* the edge. **Hold time t_h:** input must stay
  stable *after* the edge. Violating either → **metastability** (output hangs between 0/1 for an
  unbounded time, eventually resolving randomly). `settled`.
- **Maximum clock frequency** of a synchronous machine (FF → comb logic → FF path):
  **T_clk,min = t_pd,FF + t_comb,max + t_su**, so **f_max = 1 / (t_pd,FF + t_comb,max + t_su).**
  `settled` (this is the load-bearing exam formula). 
- **Hold check** uses the *shortest* path: t_pd,FF + t_comb,min ≥ t_h. `settled`.
- **Clock skew** (clock arriving at FFs at different times) eats into setup or hold margin → a real
  failure mode introduced in U4's "timing issues." `settled`.

**Exam pattern:** given t_pd, t_su, t_h and a logic-delay range, compute f_max; check for hold
violations.

---

## 7. Worked-problem patterns (Stage-1 exit targets)
1. Build/analyze an SR-from-NAND latch; explain the forbidden state and the D-latch fix.
2. Convert JK→T, JK→D, D→JK via excitation tables.
3. Design a mod-6 (or mod-10) **synchronous** counter with JK FFs (full pipeline).
4. Design a mod-10 **ripple** counter; contrast its glitch/f_max with the synchronous version.
5. Draw output waveforms of a universal shift register through a sequence of mode/data inputs.
6. Compute f_max and check hold time from given FF/gate timing.

## Stage-1 exit test (this unit)
Representative (no PYQ → `uncertain` targeting): **(a)** Design a mod-5 synchronous counter (JK),
showing the excitation table, K-maps, and self-start check. **(b)** Why does a level-triggered JK
race, and how do master-slave/edge-trig fix it? **(c)** Given t_pd,FF=8 ns, t_comb=12 ns, t_su=3 ns,
find f_max. (=1/23 ns ≈ 43.5 MHz.) → all answerable from §2–§6 with verified eqns/tables. **PASS**
(mechanism shown; targeting unconfirmed).

---

→ **Stage 2** (`stage-2/03-...md`) will add: the bistable as a positive-feedback / energy-well
system + metastability MTBF derivation (τ, resolution-time exponential); setup/hold as aperture of a
sense-amp; master-slave 0's/1's-catching analysis; CMOS transmission-gate FF internals; low-power
clock-gating; the SR latch's continuous-time dynamics. Cross-link: these FFs are the `../../../verilog`
`always @(posedge clk)` blocks.
