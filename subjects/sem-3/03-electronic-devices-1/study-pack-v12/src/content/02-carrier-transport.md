# 02 — Drift, diffusion and continuity

<div class="sub">Unit 1–2 deck, slides 40–60 (example slide 51) · syllabus Unit 1 · needs 01 (n, p, n_{i})</div>

## Map

[[map:1 Drift, conductivity > 2 Diffusion, Einstein > 3 Generation, continuity, Poisson|here=1]]

01 counted the carriers. Two things make them move: a field (drift) and a crowd (diffusion). The pn junction in 03 is the place where the two balance.

## The questions this file answers

- <span class="tag">Deck slide 51</span> Conductivity and resistivity of intrinsic Si at 300 K; the effect of a 10 °C rise.
- <span class="tag">practice</span> Diffusion coefficient and diffusion current density for a given gradient.
- <span class="tag">Syllabus Unit 1</span> Write the continuity equation and the Poisson equation and explain each term.

---

## Build

### 1 · Drift, mobility, conductivity

:::q <span class="tag">Deck slide 51</span>
(a) Calculate the conductivity and resistivity of intrinsic silicon at 300 K. (b) How would σ change if the temperature rose by 10 °C? Given μ_{n} = 1500, μ_{p} = 450 cm^{2}/V·s.
:::

:::guess Guess first
Bigger or smaller than 1 Ω·cm?
:::

:::note Terms
**Field E:** volts per cm. **Current density J:** current per unit area, A/cm^{2}. **Scattering:** a carrier colliding with a vibrating atom or an ion.
:::

[[fig:drift_diff|Drift (driven by a field) and diffusion (driven by a gradient).|w=75]]

A field accelerates carriers and scattering keeps stopping them, so they settle at **v_{d} = μE**. Electrons are faster than holes (Si: μ_{n} ≈ 1350–1500, μ_{p} ≈ 450–480). Mobility falls as temperature or doping rise. At very high fields v_{d} saturates near 10^{7} cm/s. Both carriers add:

$$J_{drift} = q(nμ_{n} + pμ_{p})E = σE      ρ = 1/σ$$

[[fig:sheet_res|Sheet resistance: R = R_{s} × L/W, counted in squares.|w=55]]

**Sheet resistance.** IC resistors are thin doped layers of thickness t: **R_{s} = ρ/t** (Ω/□), and **R = R_{s} × L/W**. A square of any size has resistance R_{s}.

**Answer.** (a) σ = 1.6 × 10^{−19} × 10^{10} × 1950 = **3.12 × 10^{−6} (Ω·cm)^{−1}**; ρ = **3.2 × 10^{5} Ω·cm**. (b) n_{i} doubles while the mobilities barely change: σ **doubles**. (Slide 52 dopes it with N_{D} = 5 × 10^{17}: σ = 32 (Ω·cm)^{−1}, ten million times larger.)

:::check Check 1
n-type Si, N_{D} = 10^{16}, μ_{n} = 1350. Find (a) σ and ρ; (b) v_{d} at 100 V/cm; (c) R_{s} of a 1 μm layer; (d) R of a strip with L/W = 10.
:::

### 2 · Diffusion and the Einstein relation

:::q <span class="tag">practice</span>
In a silicon bar the electron concentration falls by 10^{18} cm^{−3} per cm. μ_{n} = 1350 cm^{2}/V·s at 300 K. Find D_{n} and the electron diffusion current density.
:::

:::guess Guess first
No voltage is applied. Can a current still flow?
:::

Random thermal motion gives a net flow from crowded to sparse, proportional to the gradient:

$$J_{n,diff} = +qD_{n} dn/dx      J_{p,diff} = −qD_{p} dp/dx$$

The signs differ because electrons carry −q. Drift and diffusion are limited by the same scattering, so:

$$D_{n}/μ_{n} = D_{p}/μ_{p} = kT/q = V_{T}$$

**Total current:** J_{n} = qnμ_{n}E + qD_{n}dn/dx; J_{p} = qpμ_{p}E − qD_{p}dp/dx. In equilibrium J_{n} = 0 and J_{p} = 0 separately: wherever a gradient exists, a built-in field makes a drift that cancels it. That is the pn junction (03).

**Answer.** Yes. D_{n} = 1350 × 0.0259 = **34.9 cm^{2}/s**. |J| = 1.6 × 10^{−19} × 34.9 × 10^{18} = **5.59 A/cm^{2}**.

:::check Check 2
(a) D_{p} for μ_{p} = 480? (b) Name the cause of drift and of diffusion in one phrase each. (c) Write the total hole current density.
:::

### 3 · Generation, recombination, continuity, Poisson

:::q <span class="tag">Syllabus Unit 1</span>
Write the continuity equation for electrons and state what each term means.
:::

:::guess Guess first
List every way the number of electrons in a small box can change.
:::

[[fig:gr_fig|Direct recombination (GaAs, gives light) and trap-assisted recombination (Si, gives heat).|w=65]]

- **Generation (G)** creates a pair (heat or light); **recombination (R)** destroys one. In equilibrium G = R, which holds n·p at n_{i}^{2}.
- Direct (band-to-band) recombination gives light and dominates in GaAs. In Si the electron drops through a mid-gap **trap** in two steps (Shockley–Read–Hall), and the energy becomes heat.
- Excess minority carriers decay as Δp(t) = Δp(0)e^{−t/τ}; **τ** is the lifetime. It sets how fast a diode switches off (03).

$$∂n/∂t = (1/q)∂J_{n}/∂x − (R − G)      ∂p/∂t = −(1/q)∂J_{p}/∂x − (R − G)$$

**Poisson** links charge to field: dE/dx = ρ/ε = (q/ε)(p − n + N_{D} − N_{A}), with E = −dV/dx and ε = 11.7ε_{0} for Si. In neutral material ρ = 0 and the field is constant; in a depletion region it ramps (03).

**Answer.** Left: the rate of change of electron concentration at a point. First term: net flow into the slice (current in minus out). Second: net loss by recombination over generation. For holes the flow term changes sign (+q).

:::check Check 3
(a) Why does recombination in Si mostly go through traps? (b) τ = 1 μs: what fraction of excess holes is left after 3 μs? (c) Where in a device is ρ not zero?
:::

---

## Exam form

**Drift.** v_{d} = μE; σ = q(nμ_{n} + pμ_{p}); ρ = 1/σ; sheet resistance R_{s} = ρ/t, R = R_{s}L/W.

**Diffusion.** J expressions with signs; Einstein D/μ = V_{T}; total current for each carrier; equilibrium balance.

**Continuity and Poisson.** Both equations with every term named; G–R mechanisms; lifetime.

## Traps

- Forgetting the hole term (or the electron term) in σ for intrinsic material.
- Sign of the diffusion current for electrons.
- Using V_{T} = 26 V instead of 26 mV.
- Thinking current needs a field: diffusion flows with none.

## Self-test

1. p-type Si, N_{A} = 10^{16}, μ_{p} = 450. Find σ and ρ.
2. Find D_{n} for μ_{n} = 1500 at 300 K.
3. R_{s} = 100 Ω/□. A resistor is 200 μm long and 10 μm wide. Find R.
4. τ = 2 μs. What fraction of an excess is left after 2 μs?
5. Write the continuity equation for holes.
6. Why must J_{n} and J_{p} each be zero in equilibrium?

<!--ANSWERS-->

## Answers

**Check 1.** (a) σ = 1.6 × 10^{−19} × 10^{16} × 1350 = **2.16 (Ω·cm)^{−1}**; ρ = **0.462 Ω·cm**. (b) **1.35 × 10^{5} cm/s**. (c) 0.462/10^{−4} = **4620 Ω/□**. (d) **46.2 kΩ**.

**Check 2.** (a) 480 × 0.0259 = **12.4 cm^{2}/s**. (b) Drift: an electric field. Diffusion: a concentration gradient. (c) J_{p} = qpμ_{p}E − qD_{p}dp/dx.

**Check 3.** (a) Si has an indirect gap, so a direct drop is unlikely; a mid-gap trap lets it fall in two easy steps. (b) e^{−3} ≈ **5%**. (c) The depletion (space-charge) region.

**Self-test.**

1. σ = 1.6 × 10^{−19} × 10^{16} × 450 = **0.72 (Ω·cm)^{−1}**; ρ = **1.39 Ω·cm**.
2. 1500 × 0.0259 = **38.9 cm^{2}/s**.
3. 20 squares: **2 kΩ**.
4. e^{−1} = **0.368**.
5. ∂p/∂t = −(1/q)∂J_{p}/∂x − (R − G).
6. With no applied bias, any net flow of either carrier would build up charge somewhere forever; the built-in field adjusts until drift exactly cancels diffusion for each carrier.

<!--/ANSWERS-->
