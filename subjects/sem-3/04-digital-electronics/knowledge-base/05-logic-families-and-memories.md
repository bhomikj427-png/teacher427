# U5 — Logic Families & Semiconductor Memories (Stage 1, MUJ level)

> Scope (verbatim): *TTL NAND gate — specs, noise margin, propagation delay, fan-in/fan-out;
> tristate TTL; ECL; CMOS families & interfacing; memory elements; programmable logic devices; logic
> implementation using programmable devices.* This is the **device-physics floor** under the whole
> abstraction (big idea 7). Cross-links to `../../../electronic-devices-1` (MOSFET/BJT). Tier-1:
> Jain 4e, Anand Kumar; **standard-TTL DC table verified this session** vs Nuts&Volts + Cornell P360
> + Macnica + EduRev; PLD structure vs testbook + elprocus.

---

## 0. Frame — the universal yardsticks

The 0/1 abstraction is paid for in real transistors. Every family is measured by the same metrics
(`settled`):
- **Voltage levels:** V_OH/V_OL (output high/low *guaranteed*), V_IH/V_IL (input thresholds).
- **Noise margin** NM_H = V_OH − V_IH, NM_L = V_IL − V_OL (the noise a signal can absorb and still
  be read correctly — misconception M15: levels are *bands*, not exact voltages).
- **Fan-out** = max gate inputs one output drives within spec (misconception M16).
- **Propagation delay** t_pd; **power** P; **power–delay product** (energy/switch, the figure of merit).
- **Fan-in** = number of inputs to a gate.

---

## 1. TTL — the standard NAND gate

Transistor-Transistor Logic; bipolar; V_CC = +5 V. The canonical gate is the **7400 NAND**:
**multi-emitter input transistor** (does the ANDing) → **phase-splitter** → **totem-pole output**
(an active pull-up transistor stacked over a pull-down, giving low output impedance both ways → fast
edges). `settled` (Jain; structure standard).

**Standard-TTL DC parameters (VERIFIED this session, triangulated)** `settled`:
| Param | Value | | Param | Value |
|-------|-------|-|-------|-------|
| V_OH (min) | **2.4 V** | | I_OH (max) | **400 µA** |
| V_OL (max) | **0.4 V** | | I_OL (max) | **16 mA** |
| V_IH (min) | **2.0 V** | | I_IH (max) | **40 µA** |
| V_IL (max) | **0.8 V** | | I_IL (max) | **1.6 mA** |

- **Noise margin:** NM_H = 2.4 − 2.0 = **0.4 V**; NM_L = 0.8 − 0.4 = **0.4 V**. `settled`.
- **Fan-out** = min( I_OL/I_IL , I_OH/I_IH ) = min(16 mA/1.6 mA, 400 µA/40 µA) = **10**. `settled`.
  *(Mechanism: the LOW output must sink every driven input's I_IL; the HIGH output must source every
  I_IH — whichever limit binds first sets fan-out.)*
- **Propagation delay** ≈ **10 ns** (standard 74; t_pLH ≈ 11 ns, t_pHL ≈ 7 ns typ), power ≈ 10 mW/gate.
  `likely` (series-dependent; ranges agree across datasheets).

**TTL sub-series** (speed/power trade — exam-relevant, `settled` qualitatively): 74 (standard),
**74L** (low-power, slow), **74H** (high-speed), **74S** (Schottky — Schottky clamp prevents
saturation → faster), **74LS** (low-power Schottky — the workhorse: ~10 ns, ~2 mW), 74AS/74ALS/74F.
Exact per-series numbers vary — read the datasheet, don't recall (`uncertain` for specific series).

**Totem-pole caveat:** outputs **cannot be wired together** (a HIGH-over-LOW fight → large current).
Solutions: **open-collector** (external pull-up; allows *wired-AND* and bus sharing) and tristate (§2).
`settled`.

---

## 2. Tristate (three-state) TTL

A gate with a third output state — **high-impedance (Hi-Z)**, controlled by an **enable**: when
disabled the output is *electrically disconnected* (neither 0 nor 1). `settled`.
- Lets many outputs share a **bus** — only one drives at a time (enable arbitration); the rest float
  Hi-Z. This is the basis of microprocessor data/address buses. `settled`.
- Distinct from open-collector: tristate keeps the fast active pull-up *when enabled*. `settled`.

---

## 3. ECL — Emitter-Coupled Logic

A **non-saturating** bipolar family (a differential pair / current-steering switch). Because the
transistors never saturate (no stored-charge recovery delay), ECL is the **fastest** logic family
(sub-ns). `settled`.
- Trade-offs: **highest power** (always drawing the steering current), **small voltage swing** (~0.8 V
  → smaller noise margin), negative supply convention, **differential outputs** (true + complement).
  Used in high-speed/RF instrumentation. `settled`.
- The mechanism contrast — *avoid saturation = avoid the charge-storage delay* — is the exam point
  (links to BJT switching in `../../../electronic-devices-1`). `settled`.

---

## 4. CMOS families & interfacing

Complementary MOS: each gate = a **PMOS pull-up network + NMOS pull-down network**, complementary so
**exactly one network conducts** in a static state → **~zero static power**, rail-to-rail output
(V_OH≈V_DD, V_OL≈0). `settled`.
- **Why CMOS won:** near-zero static power, large noise margin (~0.45 V_DD), high density, scalable,
  wide supply range. Basis of all modern VLSI, memory, PLDs (big idea 7). `settled`.
- **Power (misconception M18):** static ≈ 0, but **dynamic power P = α·C·V_DD²·f** (charging load
  capacitance each switch) + short-circuit current during the transition → power grows with frequency
  and dominates at speed. `settled`.
- **Families:** 4000 series (slow, wide V), **74HC** (CMOS, HC = high-speed), **74HCT** (TTL-input-
  compatible thresholds), 74AC/ACT, modern LVC/AUC at lower V_DD. `settled` qualitatively.
- **Floating inputs (misconception M19):** a high-impedance CMOS input left unconnected is
  indeterminate/noise-driven (and can cause both transistors to conduct) → **always tie unused inputs**.
  `settled`.
- **Interfacing TTL↔CMOS (misconception M17):** **TTL→CMOS** problem: TTL V_OH(min)=2.4 V may be below
  CMOS V_IH(≈3.5 V at 5 V) → add a **pull-up resistor** (or use 74HCT, which has TTL-level inputs).
  **CMOS→TTL** problem: CMOS sources/sinks little current → must meet TTL's I_IL=1.6 mA sink (74HC can;
  4000-series needs a buffer). Always compare V_OH/V_OL vs V_IH/V_IL **and** current drive. `settled`.

---

## 5. Semiconductor memories

A memory = an array of cells addressed by an **address bus**, accessed via a **data bus**. Capacity =
2^(address lines) words × (data-bus width) bits. `settled`.

**Taxonomy** (`settled`):
- **RAM (read/write, volatile):**
  - **SRAM** — cell = cross-coupled inverters (a latch, 6 transistors); fast, no refresh, low density;
    cache. `settled`.
  - **DRAM** — cell = **1 transistor + 1 capacitor**; charge leaks → needs **periodic refresh**;
    high density, cheaper/bit; main memory. `settled`.
- **ROM (read-mostly, non-volatile):** MROM (mask), **PROM** (one-time, fusible), **EPROM**
  (UV-erasable), **EEPROM/Flash** (electrically erasable, block-wise for Flash). "Read-only" is a
  literalism — most are writable, just slowly/specially. `settled`.
- **Organization:** word lines (row, from the address decoder) × bit lines (column, to sense amps);
  a decoder selects the addressed word. **Exam pattern:** "How many address lines for a 1K×8 memory?"
  → 1K = 2¹⁰ → **10 address lines, 8 data lines**, 8192 bits. `settled`.

---

## 6. Programmable Logic Devices (PLDs)

Implement arbitrary SOP logic in a **programmable AND-array / OR-array** structure. The three classic
PLDs differ in **which array is programmable** (**verified this session**, triangulated testbook +
elprocus + intl-university) `settled`:

| Device | AND array | OR array | Note |
|--------|-----------|----------|------|
| **PROM** | **fixed** (full decoder — all minterms) | **programmable** | implements any function as Σ minterms; = a ROM/LUT |
| **PLA** | **programmable** | **programmable** | most flexible; share product terms; slowest |
| **PAL** | **programmable** | **fixed** | each OR sums a fixed set of products; faster, cheaper, most popular |

- **Mechanism:** SOP = (AND plane making product terms) → (OR plane summing them). What you can program
  decides flexibility vs speed (a fixed array is faster than a programmable one). `settled`.
- **Implementing logic on a PLD:** minimize each function to SOP, share product terms (PLA), map to the
  programmable connections. **Exam pattern:** "Implement F1, F2 (given Σm) on a PLA — give the
  programming/connection table." `settled`.
- Beyond classic PLDs: **GAL** (reprogrammable PAL), **CPLD**, **FPGA** (LUT-based — the "MUX as
  universal function" of U2 taken to scale; bridges to `../../../verilog`). `settled` (orientation).

---

## 7. Worked-problem patterns (Stage-1 exit targets)
1. Compute fan-out from I_OL/I_IL and I_OH/I_IH; compute NM_H, NM_L from a DC table.
2. Explain the totem-pole output and why outputs can't be tied (→ open-collector/tristate).
3. ECL: why non-saturating = fastest; CMOS: derive dynamic power CV²f and why static≈0.
4. TTL↔CMOS interface: identify the failing parameter and the fix (pull-up / 74HCT / buffer).
5. Memory sizing: address/data lines for an N×m memory; SRAM vs DRAM cell + refresh.
6. PROM vs PLA vs PAL array table; implement given functions on a PLA.

## Stage-1 exit test (this unit)
Representative (no PYQ → `uncertain` targeting): **(a)** Standard TTL: I_OL=16 mA, I_IL=1.6 mA,
I_OH=400 µA, I_IH=40 µA — find fan-out and both noise margins (=10; 0.4 V, 0.4 V). **(b)** Why does a
floating CMOS input misbehave, and how do you interface a standard-TTL output to a 4000-series CMOS
input? **(c)** PROM vs PLA vs PAL — which arrays are programmable, and which is fastest? → all
answerable from §1–§6 with the verified DC table + PLD structure. **PASS** (mechanism shown; targeting
unconfirmed).

---

→ **Stage 2** (`stage-2/05-...md`) will add: full transistor-level TTL/ECL/CMOS gate analysis (transfer
curve, V_M, noise-margin derivation from the VTC); short-circuit + leakage power, the power-delay/
energy-delay product optimization; DRAM sense-amp + charge-sharing physics; Flash floating-gate
tunneling; SRAM stability (static noise margin, butterfly curve); FPGA architecture; the CMOS scaling
story (→ `../../../electronic-devices-1` MOSFET physics). 
