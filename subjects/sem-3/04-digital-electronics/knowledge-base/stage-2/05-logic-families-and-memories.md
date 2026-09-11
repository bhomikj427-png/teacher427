# U5 — Logic Families & Memories (Stage 2: deep structure + frontier)

> Extends `../05-logic-families-and-memories.md`. This is the **physics under the abstraction** — the
> transistor-level truth the digital course rests on, tying directly to `../../../electronic-devices-1`
> (MOSFET/BJT). Primary: Weste-Harris, Rabaey, Razavi; V_M, power, SRAM-SNM verified this session
> (`sources.md`).

---

## A. The CMOS inverter VTC — deriving the levels Stage 1 *quoted*

The static voltage-transfer curve V_out(V_in) has five regions as V_in sweeps 0→V_DD; the **switching
threshold V_M** is where V_in=V_out and **both transistors are in saturation**, so I_DSn=I_DSp:
- ✓ verified this session: **V_M = [r(V_DD − |V_Tp|) + V_Tn] / (1 + r)**, with **r = √(k_p/k_n) =
  √(μ_p W_p / μ_n W_n)** (equal lengths). `settled`. Design lever: to center V_M = V_DD/2 you size
  **(W/L)_p / (W/L)_n ≈ μ_n/μ_p ≈ 2–3** (PMOS wider, because hole mobility is lower — the link back to
  `../../../electronic-devices-1`). `settled (standard)`.
- **Noise margins from the VTC, not quoted:** V_IL and V_IH are the **unity-gain points** (dV_out/dV_in
  = −1) of the curve; NM_L = V_IL − V_OL, NM_H = V_OH − V_IH with V_OH≈V_DD, V_OL≈0. A *steeper*
  transition (higher gain) ⇒ wider noise margins ⇒ why high gain at V_M is good. This is the
  first-principles version of Stage-1's "noise margin = level difference." `settled (standard)` (Weste-
  Harris; Razavi). **The white lie:** Stage-1's fixed 0.4 V TTL numbers are *one family's measured
  datasheet values* — the VTC is what actually sets them, and CMOS gives ≈0.4·V_DD, far better than TTL.

---

## A½. Building ANY CMOS gate — the pull-up / pull-down dual networks

The inverter generalizes to a recipe for *any* inverting function, and this is the core of CMOS
digital design (MIT 6.004 "gates from MOS"): every static CMOS gate = a **pull-down network (PDN) of
NMOS** to ground + a complementary **pull-up network (PUN) of PMOS** to V_DD. `settled (standard)`
(Weste-Harris):
- **PDN (NMOS)** conducts (output = 0) for the input combinations where the function is 0. **Series
  NMOS = AND** of inputs; **parallel NMOS = OR**. NMOS pass a strong 0.
- **PUN (PMOS)** is the **dual**: wherever the PDN is series, the PUN is parallel, and vice-versa, so
  exactly one network conducts in any static state (→ the ~zero static power of §B). PMOS pass a strong 1.
- ⇒ a **2-input NAND** = 2 NMOS in series (PDN) + 2 PMOS in parallel (PUN); a **NOR** = NMOS parallel +
  PMOS series. **NAND is preferred** over NOR because series **PMOS** (in the NOR's PUN) are slow (low
  hole mobility, → `../../../electronic-devices-1`) — so stacked PMOS hurt more than stacked NMOS.
  `settled (standard)`.
- **AOI/OAI complex gates** realize any inverting SOP/POS in **one** gate (one PDN+PUN) — fewer stages
  than gate-by-gate. **Euler-path** ordering gives a compact diffusion layout (stick diagram). Static
  CMOS is naturally **inverting**; non-inverting needs an extra inverter (→ why NAND/NOR/AOI dominate,
  echoing U1's functional-completeness story). `settled (standard)`.

---

## B. Power — the real equation (and why CMOS won, then hit a wall)

Total ≈ **P = α·C_L·V_DD²·f  +  I_SC·V_DD  +  I_leak·V_DD**:
- **Dynamic (switching):** charging/discharging C_L each 0→1→0 dissipates **C_L·V_DD²** per cycle,
  ×activity α ×frequency f. Derivation: energy from supply per L→H = C_L·V_DD²; half stored on C_L
  (½C_L V_DD²) then dumped on H→L → all of C_L V_DD² lost per full cycle, **independent of the
  resistance**. ✓ reasoning verified; `settled (standard)` (Rabaey §5). *This is the dominant term and
  the reason for the **V_DD² scaling** drive — halving V_DD quarters dynamic energy.*
- **Short-circuit:** during a finite input edge both transistors briefly conduct (V_Tn < V_in <
  V_DD−|V_Tp|) → a current spike; ~10% of dynamic with balanced edges, worse with slow inputs. `likely`
  (source to Rabaey/Veendrick).
- **Static/leakage:** Stage-1's "CMOS draws no power" (misconception M18) is the **biggest UG lie at
  modern nodes** — subthreshold + gate-tunneling leakage (I_leak ∝ e^{−V_T/...}, → the 60 mV/dec floor
  from `../../../electronic-devices-1` stage-2) now **dominates** standby power and is *why scaling
  stalled* and multicore/dark-silicon happened. `settled (standard)` (Weste-Harris; cross-link to EDV-1).
- **Figure of merit:** **power-delay product** (energy/op) and **energy-delay product** — the real
  optimization target, not raw speed or raw power. `settled`.

---

## C. Delay — the RC/logical-effort model under "propagation delay"

Stage-1's t_pd is, physically, an RC charge time: **t_pd ≈ 0.69·R_on·C_L** (the gate drives C_L through
its on-resistance R_on ∝ 1/[μC_ox(W/L)(V_DD−V_T)]). Hence delay ↑ with load/fan-out, ↓ with width and
V_DD. **Logical effort** (Sutherland) formalizes sizing a path for minimum delay (delay = g·h + p).
This is the first-principles content behind "fan-out slows you down" (Stage-1 M16). `settled (standard)`
(Weste-Harris). **Elmore delay** estimates multi-stage RC paths.

---

## D. Bipolar families, properly (TTL/ECL transistor-level)

- **TTL totem-pole:** the multi-emitter input does AND by pulling the base node; the phase splitter
  drives a push-pull output. The speed limiter is **BJT saturation charge storage** (the base minority-
  charge that must be removed — directly the reverse-recovery story of `../../../electronic-devices-1`).
  **Schottky TTL (74S/LS)** clamps the BJT out of deep saturation with a Schottky diode → kills storage
  time → faster. `settled (standard)` (Razavi; cross-link EDV-1).
- **ECL = a BJT differential pair / current switch** biased so transistors **never saturate** (no
  storage delay) → fastest, but constant tail current = high static power, and a small (~0.8 V) swing =
  small noise margin. The mechanism (avoid saturation) is the whole point. `settled (standard)`.

---

## E. Memories — the bit cells, physically

- **SRAM 6T:** two cross-coupled inverters (= the bistable of stage-2/03 §A) + 2 access transistors.
  Stability = **static noise margin (SNM)**, read graphically from the **butterfly curve** (the two
  inverter VTCs overlaid): ✓ verified this session — **SNM = side of the largest square that fits in a
  lobe**; **read-SNM < hold-SNM** because the access transistors pull the storage node up during a read
  (read-disturb), and **write needs the *opposite*** — the cell must be *destabilized* to flip. The 6T
  cell is a three-way **read-stability / writeability / area** compromise — *why* sizing ratios (cell
  ratio, pull-up ratio) are tuned, and why low-V_DD SRAM needs 8T/assist. `settled` (verified; Rabaey/
  SNM literature).
- **DRAM 1T1C:** one capacitor holds charge; reading is **destructive charge-sharing** onto the bit
  line, ΔV = V_signal·C_cell/(C_cell+C_bit) (C_cell ≪ C_bit → tiny ΔV) → a **sense amplifier** (a
  cross-coupled latch again!) regenerates it, then **write-back**; leakage forces **periodic refresh**.
  Density (1T) is why it's main memory. `settled (standard)` (Rabaey; exact ΔV form `likely`, to lock).
- **Flash/EEPROM:** a **floating-gate** MOSFET; charge tunnels (Fowler–Nordheim / hot-carrier) onto an
  isolated gate, shifting V_T → non-volatile; erase is block-wise (NAND Flash). Wear-out = oxide
  damage → finite endurance. `settled (standard)`.
- **ROM/PLD = the combinational §A of U1/U2 frozen:** PROM = decoder(fixed AND)+programmable OR =
  truth table in silicon = an FPGA LUT's ancestor (→ `../../../verilog`). `settled`.

---

## F. Cross-topic unification & frontier
- **One circuit, three hats:** cross-coupled inverters = the bistable latch (U3) = the SRAM cell (here)
  = the DRAM/sense-amp regenerator. Regeneration is the unifying mechanism of all static storage.
- **CMOS physics → digital logic → VLSI scaling** is the through-line of the whole subject: V_M, noise
  margin, power, delay all reduce to the MOSFET square-law + short-channel effects of
  `../../../electronic-devices-1` — **U5 is where this course and EDV-1 are the same course.**
- **Frontier (teach as live, not closed):** Dennard scaling **ended** (~2005, leakage/power wall) →
  multicore, dark silicon; **FinFET → GAA nanosheet** (electrostatics, ← EDV-1 stage-2); near-/sub-
  threshold logic; **emerging memory** (MRAM/ReRAM/PCM/FeFET) chasing a non-volatile-RAM unifier;
  3D-stacked DRAM/HBM. `likely`/`evolving` — dated, in register.

## G. Harder problems (§0 surplus test)
1. Derive V_M and the sizing for V_M=V_DD/2; why is PMOS made wider? ✓ (§A).
2. Derive dynamic energy = C_L V_DD²/cycle and explain the V_DD² scaling motive. ✓ (§B).
3. Why is "CMOS has no static power" false at 7 nm — name the mechanism. ✓ (§B, leakage; ←EDV-1).
4. Read SNM off a butterfly curve; explain read-disturb and the read-vs-write tension in 6T. ✓ (§E).
5. Why does DRAM need a sense amp and refresh but SRAM doesn't? ✓ (§E).
6. Why is ECL fastest and TTL-Schottky faster than plain TTL — one mechanism (saturation). ✓ (§D).

**§0 surplus exit (U5 Stage 2): PASS** — VTC/V_M, power, delay, SRAM-SNM, DRAM all answered from
device mechanism (V_M, dynamic power, SNM verified this session); short-circuit fraction + DRAM ΔV +
leakage constants flagged `likely`/`uncertain` to register. Frontier dated and marked `evolving`.
