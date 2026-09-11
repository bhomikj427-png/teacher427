# U3 — Sequential Logic Design (Stage 2: deep structure + frontier)

> Extends `../03-sequential-logic-design.md`. The deep idea: **a flip-flop is a continuous-time
> positive-feedback dynamical system**; "stores a bit" is an approximation that *fails* in the
> metastable window. Primary: Razavi, Weste-Harris, Rabaey, NXP AN219; metastability verified this
> session (`sources.md`).

---

## A. The bistable as a dynamical system (why two states exist)

Cross-couple two inverters: V_out = f(f(V_in)). Fixed points solve V = f(f(V)). The loop gain at a
fixed point is the product of the two inverter gains:
- **|loop gain| > 1** at the two outer fixed points → **stable** (any perturbation is restored): the
  logic 0 and logic 1. These are **energy minima** (potential wells). `settled (standard)` (Razavi).
- **|loop gain| > 1 through the middle** forces a **third, unstable** fixed point at V_M (the inverter
  switching threshold, → U5) — a hilltop. A latch parked exactly there is **metastable**. `settled`.

So "two stable states" is a *regenerative* property (positive feedback), not a structural given. The
SR latch's "forbidden→race" and the JK's "race-around" are this same dynamics seen at the gate level.

---

## B. Metastability — the white lie that "a FF always resolves in t_pd"

Near V_M, linearize: the differential voltage grows as **ΔV(t) = ΔV₀·e^{t/τ}**, τ = C/g_m the
regeneration time-constant (~20–50 ps in modern CMOS). The FF is metastable until |ΔV| reaches a
valid level. Because resolution is **exponential**, the probability of *still* being metastable after
time t_r falls like e^{−t_r/τ} → never exactly zero. Hence the **MTBF** (✓ verified this session):

  **MTBF = e^{t_r/τ} / (T_W · f_clk · f_data)**

t_r = slack available for resolution, T_W = metastability "aperture" window, f_clk·f_data = rate of
dangerous input/clock coincidences. `settled` (NXP AN219; Trilobyte/Golson; ecrionix).
- **Design consequence:** you *cannot* eliminate metastability, only push MTBF to centuries by buying
  resolution time → the **two-FF synchronizer** (the second FF gives the first a full clock of slack).
  More stages or higher f_clk margin ⇒ exponentially better MTBF. `settled`.
- **Where the UG textbook lies:** "setup/hold guarantee correct capture" — they only bound the *input*
  timing; violating them doesn't give a wrong-but-defined value, it gives an **unbounded resolution
  time**. Every clock-domain crossing is a probabilistic device. `settled`.

---

## C. Setup/hold, derived; master-slave pathologies

- **Setup/hold are the metastability aperture, not arbitrary specs.** They are the input-stability
  window around the edge outside which capture risks landing on the V_M hilltop. t_su+t_h ≈ the
  aperture T_W projected to the data input. `settled (standard)` (Weste-Harris).
- **Master-slave 1's-catching / 0's-catching:** because the master latch is *transparent* for a full
  half-period, a narrow glitch on J (or K) while CLK=1 can be **caught** and passed to the slave even
  though it was gone by the edge — a real pulse-triggered-FF hazard that **edge-triggered** FFs avoid
  (their aperture is the narrow edge window, not a half period). *This is the concrete reason modern
  design uses edge-triggered, not master-slave JK.* `settled (standard)` (Wakerly).
- **CMOS implementation:** the real edge-triggered D-FF is two **transmission-gate latches** in
  master-slave with clock/clock-bar — the JK/T you K-map are behavioral abstractions over this one
  physical cell (D-FF + input logic). `settled (standard)` (Weste-Harris).

---

## D. Timing analysis, the real inequalities (incl. skew & jitter)

For a launch FF → combinational path → capture FF with clock skew δ (capture clock later by δ):
- **Setup (max-delay / long path):** t_pd,FF + t_comb,max + t_su ≤ T_clk + δ ⇒
  **f_max = 1/(t_pd,FF + t_comb,max + t_su − δ)** — positive skew toward capture *helps* setup.
- **Hold (min-delay / short path):** t_pd,FF + t_comb,min ≥ t_h + δ — the same positive skew *hurts*
  hold, and **hold violations can't be fixed by slowing the clock** (no T_clk term). This asymmetry is
  the crux of real timing closure. Jitter eats further into both margins. `settled (standard)`
  (Weste-Harris/Rabaey; extends Stage-1 §6).

---

## E. Cross-topic unification & frontier
- **Latch = U5's cross-coupled inverter = SRAM cell (→ stage-2/05):** the bistable, the SR latch, and
  the 6T SRAM bit are the *same* circuit analyzed for different things (logic / storage / SNM).
- **The FF is the only "memory" primitive** the whole sequential half (counters/registers/FSMs/U4)
  reduces to; everything else is combinational logic around it.
- **These are the Verilog `always @(posedge clk)` inferences** — synthesis maps a non-blocking
  assignment to exactly this cell (→ `../../../verilog`).
- **Frontier:** low-power **clock gating** + retention FFs; **pulsed/transparent latches** for time
  borrowing; near-threshold operation (τ grows → MTBF degrades). Logged to register. `likely`.

## F. Harder problems (§0 surplus test)
1. From loop gain, show why exactly three fixed points exist and which are stable. ✓ (§A).
2. Derive MTBF's exponential form from ΔV(t)=ΔV₀e^{t/τ}; show why a 2-FF synchronizer wins. ✓ (§B).
3. Explain 1's-catching in master-slave JK and why edge-triggered avoids it. ✓ (§C).
4. Show a positive clock skew that *fixes* a setup failure but *creates* a hold failure. ✓ (§D).
5. Why can't slowing the clock fix a hold violation? ✓ (§D, no T_clk term).

**§0 surplus exit (U3 Stage 2): PASS** — bistable dynamics + metastability MTBF + skew inequalities
answered from mechanism, metastability verified this session; CMOS-cell/1's-catching cited to Weste-
Harris/Wakerly.
