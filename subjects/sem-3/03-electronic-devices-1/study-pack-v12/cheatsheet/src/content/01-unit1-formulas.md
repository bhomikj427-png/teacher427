# Unit 1 — Formula cheat sheet: semiconductors and current flow

<div class="sub">One card per formula from v1.2 files 01a, 01b, 02a, 02b · each card: a question → the formula → every symbol defined → a figure → where it holds · answers at the end · every number recomputed in verify.py</div>

## Map

[[map:Count carriers (F1–F6) > Push them: drift (F7–F11) > Spread them: diffusion (F12–F15) > Lose them: recombination (F16–F19) > Charge → field (F20)]]

**Constants used on every card.** q = 1.6 × 10^{−19} C (charge of one electron, magnitude). kT = 0.0259 eV at 300 K (a typical thermal energy). V_{T} = kT/q = 0.0259 V ≈ 26 mV (the same energy in volts). Silicon at 300 K: E_{g} = 1.12 eV, n_{i} = 1.5 × 10^{10} cm^{−3} (some decks use 10^{10}), ε = 1.04 × 10^{−12} F/cm.

---

## Part 1 · Counting carriers

### F1 · Mass-action law: n · p = n_{i}^{2}

:::q <span class="tag">01a step 8</span>
Si doped with N_{D} = 10^{16} cm^{−3}, n_{i} = 1.5 × 10^{10} cm^{−3}, 300 K. Find n and p.
:::

$$n · p = n_{i}^{2}      n-type: n ≈ N_{D}, p = n_{i}^{2}/N_{D}      p-type: p ≈ N_{A}, n = n_{i}^{2}/N_{A}$$

:::note Terms
**n:** free electrons per cm^{3}. **p:** holes (empty bond places, charge +q) per cm^{3}. **n_{i}:** the electron count in pure (intrinsic) silicon, where n = p = n_{i}. **N_{D}:** donor atoms per cm^{3} (P, As: 5 valence electrons, each gives one electron). **N_{A}:** acceptor atoms per cm^{3} (B, Ga: 3 valence electrons, each makes one hole). **Thermal equilibrium:** steady temperature, no voltage, no light.
:::

[[fig:lattice_dopants|Left: a donor gives a free electron. Right: an acceptor leaves a hole.|w=70]]

- Doping raises one carrier and pushes the other down by the same factor: their product stays n_{i}^{2}.
- **Majority carrier:** the one doping supplies (electrons in n-type). **Minority:** the other.
- Holds only in equilibrium.

### F2 · Intrinsic density: n_{i} = √(N_{C}N_{V}) e^{−E_{g}/2kT}

:::q <span class="tag">01b step 8</span>
(a) N_{C} = 2.8 × 10^{19}, N_{V} = 1.04 × 10^{19} cm^{−3}, E_{g} = 1.12 eV, kT = 0.0259 eV. Find n_{i}. (b) n_{i} roughly doubles every 10 °C. By what factor does it grow from 25 °C to 45 °C?
:::

$$n_{i} = √(N_{C}N_{V}) e^{−E_{g}/2kT}$$

:::note Terms
**E_{g} (band gap):** the energy needed to break one bond and free an electron; 1.12 eV in Si. **N_{C}, N_{V}:** effective numbers of electron "seats" in the conduction band and of hole seats in the valence band, per cm^{3} (F4). **e^{−E_{g}/2kT}:** how rare a bond-breaking kick is; tiny, and very sensitive to E_{g} and T.
:::

[[fig:ni_vs_T|n_{i} against temperature (log axis: each grid step ×10). Smaller gap → more carriers; hotter → more carriers.|w=62]]

- Ge (E_{g} 0.66 eV) ≈ 2.4 × 10^{13}, Si ≈ 1.5 × 10^{10}, GaAs (1.42 eV) ≈ 1.8 × 10^{6} cm^{−3}.
- Why semiconductor resistance **falls** when heated: more carriers.

### F3 · Fermi–Dirac function f(E)

:::q <span class="tag">01b steps 2–3</span>
(a) What is f(E) at E = E_{F}? (b) At E − E_{F} = 3kT? (c) In pure Si, E_{C} is 0.56 eV above E_{F}. Find f(E_{C}).
:::

$$f(E) = \frac{1}{1 + e^{(E − E_{F})/kT}}      hole chance = 1 − f(E)$$

:::note Terms
**State ("seat"):** one allowed place for one electron at one energy. **f(E):** the probability that a seat at energy E is filled. **E_{F} (Fermi level):** the energy where that probability is exactly ½. **E_{C}:** bottom of the conduction band (lowest free-electron energy). **E_{V}:** top of the valence band (highest bonded-electron energy).
:::

[[fig:fermi_rotated|Bands with E_{F} at mid-gap, and f(E) turned so energy points up. Only the tail of f reaches the conduction band.|w=80]]

- Far below E_{F}: f ≈ 1 (full). Far above: f ≈ 0 (empty). The change from 1 to 0 takes a few kT.

### F4 · Carrier counts: n = N_{C}e^{−(E_{C} − E_{F})/kT}

:::q <span class="tag">01b step 7</span>
(a) E_{F} is 0.25 eV below E_{C} at 300 K. Find n. (b) E_{F} − E_{V} = 0.20 eV. Find p.
:::

$$n = N_{C} e^{−(E_{C} − E_{F})/kT}      p = N_{V} e^{−(E_{F} − E_{V})/kT}$$

:::note Terms
**N_{C}:** the number of seats per cm^{3} that, if all placed exactly at E_{C}, would hold the same electrons as the real band; 2.8 × 10^{19} cm^{−3} in Si, ∝ T^{3/2}. **N_{V}:** the same for holes at E_{V}; 1.04 × 10^{19}. **Exponential:** the chance a seat at the band edge is filled (the Boltzmann shortcut of f, valid when E_{F} is more than 3kT from the edge, "non-degenerate").
:::

[[fig:nc_equivalent|The real band (spread-out seats) replaced by N_{C} seats placed at E_{C}.|w=70]]

- **Read it:** the closer E_{F} is to E_{C}, the more electrons. Every 60 mV (0.06 eV) closer multiplies n by about 10.
- Multiply n by p: E_{F} cancels and n · p = N_{C}N_{V}e^{−E_{g}/kT} = n_{i}^{2}. That is F1 proved.

### F5 · Intrinsic Fermi level: E_{F} at mid-gap

:::q <span class="tag">Deck slide 38</span>
Show that the Fermi level in an intrinsic semiconductor lies at the middle of the forbidden gap.
:::

$$E_{Fi} = \frac{E_{C} + E_{V}}{2} + \frac{kT}{2} ln\frac{N_{V}}{N_{C}} ≈ \frac{E_{C} + E_{V}}{2}$$

:::note Terms
**Intrinsic:** undoped, so n = p. **E_{Fi} (also E_{i}):** the Fermi level of intrinsic silicon. **Mid-gap:** (E_{C} + E_{V})/2, halfway between the band edges.
:::

[[fig:ef_positions|E_{F} in intrinsic (middle), n-type (up toward E_{C}) and p-type (down toward E_{V}) silicon.|w=72]]

- The ln term is kT/2 × ln(1.04/2.8) = −13 mV: under 2 % of the 0.56 eV half-gap, so E_{F} ≈ mid-gap.

### F6 · Doping moves E_{F}: n = n_{i}e^{(E_{F} − E_{i})/kT}

:::q <span class="tag">01b step 10</span>
Si with N_{D} = 10^{16} cm^{−3}, n_{i} = 10^{10} cm^{−3}, 300 K. How far above mid-gap is E_{F}? How far below E_{C}?
:::

$$n = n_{i} e^{(E_{F} − E_{i})/kT}      p = n_{i} e^{(E_{i} − E_{F})/kT}      ⇒  E_{F} − E_{i} = kT ln(N_{D}/n_{i})$$

:::note Terms
**E_{i}:** the intrinsic Fermi level (≈ mid-gap), used as the reference. **E_{F} − E_{i} &gt; 0:** n-type (E_{F} above mid-gap). **&lt; 0:** p-type, with E_{i} − E_{F} = kT ln(N_{A}/n_{i}).
:::

[[fig:ef_vs_doping|E_{F} against doping: each ×10 in doping moves E_{F} by 60 mV toward a band edge.|w=62]]

---

## Part 2 · Drift: current pushed by a field

### F7 · Drift velocity: v_{d} = μE

:::q <span class="tag">02a step 2</span>
1 V across 100 μm of lightly doped Si gives E = 100 V/cm. μ_{n} = 1350 cm^{2}/V·s. Find the electron drift velocity and compare with the thermal speed 1.17 × 10^{7} cm/s.
:::

$$v_{d} = μE      (low field)      v_{d} = \frac{μE}{1 + μE/v_{sat}}      (any field)$$

:::note Terms
**E (field):** V/cm; the push per unit charge. **v_{d} (drift velocity):** the average velocity along the field after the random motion cancels. **μ (mobility):** cm^{2}/V·s; drift velocity per unit field; Si: μ_{n} ≈ 1350, μ_{p} ≈ 480. **v_{sat}:** the speed limit, ≈ 10^{7} cm/s in Si. **Thermal speed v_{th}:** random speed from heat; gives no current because the directions cancel.
:::

<div class="two">

[[fig:drift_walk|Random path plus a small steady creep: the drift. Holes along E, electrons against E.]]

[[fig:vsat_plot|v_{d} against E (log–log): straight (v_{d} = μE), then flat at v_{sat}.]]

</div>

- μ = qτ/m\*: longer time between collisions (τ) or lighter effective mass (m\*) → more mobile.
- μ falls with doping (ions scatter) and with temperature (vibrating atoms scatter).

### F8 · Drift current and conductivity: J = σE

:::q <span class="tag">Deck slide 51</span>
(a) Conductivity and resistivity of intrinsic Si at 300 K, n_{i} = 10^{10} cm^{−3}, μ_{n} = 1500, μ_{p} = 450 cm^{2}/V·s. (b) Effect of a 10 °C rise.
:::

$$J_{drift} = q(nμ_{n} + pμ_{p})E = σE      σ = q(nμ_{n} + pμ_{p})      ρ = 1/σ$$

:::note Terms
**J (current density):** A/cm^{2}; current through one cm^{2}. **σ (conductivity):** (Ω·cm)^{−1}; how much J one V/cm drives = how many carriers × how mobile. **ρ (resistivity):** Ω·cm; the material's resistance, independent of shape. Electrons and holes move opposite ways but both carry current along E, so the terms **add**.
:::

[[fig:ni_T_sigma|σ of pure Si follows n_{i}(T): μ changes by a few per cent, n_{i} doubles per 10 °C.|w=62]]

### F9 · Doped silicon: σ ≈ qN_{D}μ_{n}

:::q <span class="tag">Deck slide 52</span>
Si with N_{D} = 5 × 10^{17} cm^{−3} has σ = 32 (Ω·cm)^{−1}. (a) Find p. (b) What electron mobility does σ imply? (c) How many times more conductive than intrinsic Si (3.12 × 10^{−6})?
:::

$$n-type: σ ≈ qN_{D}μ_{n}      p-type: σ ≈ qN_{A}μ_{p}$$

:::note Terms
Once doped, the **minority** term is billions of times smaller than the majority term, so it is dropped. μ here is the mobility **at that doping**, lower than in pure Si.
:::

[[fig:mobility_doping|μ against doping: flat up to about 10^{15}, then falls as ions scatter.|w=60]]

### F10 · Resistance of a bar: R = ρL/A

:::q <span class="tag">02a step 8</span>
An n-type Si bar has ρ = 0.5 Ω·cm, length 1 mm, cross-section 100 μm × 100 μm. Find R and the current at 5 V.
:::

$$R = \frac{ρL}{A}      A = W × t$$

:::note Terms
**L:** length along the current, cm. **A:** cross-section area, cm^{2}; **W** width, **t** thickness. Convert μm to cm: 1 μm = 10^{−4} cm.
:::

[[fig:bar_resistor|Current flows along L through the cross-section A = W × t.|w=60]]

### F11 · Sheet resistance: R = R_{s} × L/W

:::q <span class="tag">02a step 9</span>
A doped layer is 1 μm thick, ρ = 0.01 Ω·cm. Find R_{s}. A resistor in it is 200 μm long, 10 μm wide. Find R.
:::

$$R_{s} = ρ/t   (Ω/□)      R = R_{s} × \frac{L}{W}$$

:::note Terms
**R_{s} (sheet resistance):** the resistance of one square of the layer, any size; units Ω, said "ohms per square". **L/W:** the number of squares end to end along the resistor. Used in IC layout, where every layer has a fixed t.
:::

[[fig:sheet_squares|A big square and a small square of the same layer have the same R: longer path, but wider.|w=62]]

---

## Part 3 · Diffusion: current from a crowd spreading out

### F12 · Fick's law: F = −D dn/dx

:::q <span class="tag">02b step 2</span>
Electron density falls in a straight line from 10^{17} to 10^{16} cm^{−3} over 1 μm. D_{n} = 35 cm^{2}/s. Find the gradient and the electron diffusion flux.
:::

$$F_{n} = −D_{n} \frac{dn}{dx}      F_{p} = −D_{p} \frac{dp}{dx}$$

:::note Terms
**Flux F:** carriers crossing one cm^{2} per second. **Gradient dn/dx:** slope of n(x), cm^{−4}. **D (diffusion coefficient):** cm^{2}/s; how fast a carrier spreads; Si: D_{n} ≈ 35, D_{p} ≈ 12.4. **Minus sign:** carriers flow **downhill**, from more to fewer.
:::

[[fig:fick_slopes|Steeper slope → bigger flux. Flat → no diffusion.|w=66]]

### F13 · Diffusion current: J_{n} = +qD_{n}dn/dx, J_{p} = −qD_{p}dp/dx

:::q <span class="tag">02b step 3</span>
dn/dx = −10^{18} cm^{−4}, D_{n} = 35 cm^{2}/s. Find the electron diffusion current density and its direction.
:::

$$J_{n,diff} = +qD_{n} \frac{dn}{dx}      J_{p,diff} = −qD_{p} \frac{dp}{dx}$$

:::note Terms
J = charge × flux. Electron charge is −q, so the minus sign of Fick flips to **+** for electrons. Holes (+q) keep the minus.
:::

[[fig:diff_signs|Both carriers flow downhill. Holes: current with the flow. Electrons: current against it.|w=74]]

### F14 · Total current: drift + diffusion

:::q <span class="tag">02b step 4</span>
In n-type Si: n = 10^{16} cm^{−3}, E = 10 V/cm along +x, dn/dx = −10^{18} cm^{−4}, μ_{n} = 1350, D_{n} = 35. Find the drift, diffusion and total electron current densities.
:::

$$J_{n} = qnμ_{n}E + qD_{n}\frac{dn}{dx}      J_{p} = qpμ_{p}E − qD_{p}\frac{dp}{dx}      J = J_{n} + J_{p}$$

:::note Terms
**J_{n}, J_{p}:** total electron and hole current densities. **J:** what an ammeter sees, per cm^{2}. In **equilibrium** the drift and diffusion parts cancel exactly: J = 0 (this is how the pn junction's built-in field forms, Unit 2 F21).
:::

[[fig:equilibrium_balance|Equilibrium: diffusion one way, the built-in field's drift back, net zero.|w=66]]

### F15 · Einstein relation: D/μ = kT/q

:::q <span class="tag">Deck slide 57</span>
(a) μ_{n} = 1350, μ_{p} = 480 cm^{2}/V·s at 300 K. Find D_{n}, D_{p}. (b) Derive the relation from J_{n} = 0 in equilibrium.
:::

$$\frac{D_{n}}{μ_{n}} = \frac{D_{p}}{μ_{p}} = \frac{kT}{q} = V_{T}$$

:::note Terms
**V_{T} (thermal voltage):** kT in volts, 0.0259 V at 300 K. D and μ are tied because the **same collisions** limit both spreading and drifting.
:::

---

## Part 4 · Generation, recombination, continuity

### F16 · SRH recombination → Δp/τ_{p}

:::q <span class="tag">Deck slide 61</span>
State the Shockley–Read–Hall net recombination rate. Show that in n-type Si with a small hole excess Δp it becomes R − G ≈ Δp/τ_{p}.
:::

$$R − G = \frac{np − n_{i}^{2}}{τ_{p}(n + n_{1}) + τ_{n}(p + p_{1})}      ⇒   R − G ≈ \frac{Δp}{τ_{p}}$$

:::note Terms
**EHP:** electron–hole pair. **G:** pairs created per cm^{3} per s (heat, light). **R:** pairs destroyed per cm^{3} per s. **Trap (G–R centre):** a defect with an energy level E_{T} inside the gap; in Si almost all recombination goes through traps. **τ_{n}, τ_{p}:** lifetimes, set by how many traps. **n_{1}, p_{1}:** n and p if E_{F} sat at E_{T} (= n_{i} for a mid-gap trap). **np − n_{i}^{2}:** how far from equilibrium; zero in equilibrium.
:::

[[fig:direct_vs_trap|Direct recombination (GaAs, gives light) against recombination through a trap (Si, gives heat).|w=72]]

### F17 · Lifetime decay: Δp(t) = Δp(0)e^{−t/τ_{p}}

:::q <span class="tag">02b step 10</span>
Light makes Δp = 10^{14} cm^{−3} extra holes in n-type Si, τ_{p} = 1 μs. Light off at t = 0. Δp after 1 μs and 3 μs?
:::

$$\frac{dΔp}{dt} = −\frac{Δp}{τ_{p}}   ⇒   Δp(t) = Δp(0) e^{−t/τ_{p}}$$

:::note Terms
**Δp (excess):** holes above the equilibrium value p_{0}. **τ_{p} (minority-carrier lifetime):** average survival time of an extra hole. After one τ, 37 % remain; after 3τ, 5 %.
:::

[[fig:lifetime_decay|Excess holes after the light goes off.|w=60]]

### F18 · Continuity equation

:::q <span class="tag">Deck slides 62–64</span>
Write the hole continuity equation. Reduce it to the steady-state, no-field form.
:::

$$\frac{∂n}{∂t} = +\frac{1}{q}\frac{∂J_{n}}{∂x} − (R − G)      \frac{∂p}{∂t} = −\frac{1}{q}\frac{∂J_{p}}{∂x} − (R − G)$$

:::note Terms
Bookkeeping for a thin box: **change in time = (in − out) − net loss**. **∂J/∂x:** how current changes across the box. **Steady state:** ∂/∂t = 0.
:::

[[fig:continuity_box|Carriers in, carriers out, carriers lost inside the box.|w=62]]

### F19 · Diffusion length: L = √(Dτ)

:::q <span class="tag">02b step 12</span>
Δp(0) = 10^{14} cm^{−3} held at x = 0 of a long n-region, no field. D_{p} = 12.4 cm^{2}/s, τ_{p} = 1 μs. Find L_{p} and Δp at 50 μm.
:::

$$L_{p} = √(D_{p}τ_{p})      Δp(x) = Δp(0) e^{−x/L_{p}}$$

:::note Terms
**L_{p} (diffusion length):** the average distance an injected hole spreads before it recombines; the excess falls to 1/e (37 %) over each L.
:::

[[fig:diff_length|Injected holes die away over a few diffusion lengths.|w=60]]

---

## Part 5 · Charge makes field

### F20 · Poisson's equation: dE/dx = ρ/ε

:::q <span class="tag">Deck slide 65</span>
(a) Write Poisson's equation for a semiconductor and explain each term. (b) A region holds only ionised donors, N_{D} = 10^{16} cm^{−3}. How fast does E grow with x, and by how much over 0.1 μm?
:::

$$\frac{dE}{dx} = \frac{ρ}{ε} = \frac{q}{ε}(p − n + N_{D}^{+} − N_{A}^{−})      E = −\frac{dV}{dx}$$

:::note Terms
**ρ(x):** net charge per cm^{3} (here ρ is charge, not resistivity). **N_{D}^{+}:** donors that gave away their electron (fixed, +). **N_{A}^{−}:** acceptors that took an electron (fixed, −). **ε:** permittivity, Si 11.7ε_{0} = 1.04 × 10^{−12} F/cm. **V:** potential; the field is its downhill slope.
:::

[[fig:poisson_stack|Charge → (integrate) → field → (integrate) → potential.|w=60]]

<!--ANSWERS-->

## Answers

**F1.** n ≈ N_{D} = **10^{16}**; p = (1.5 × 10^{10})^{2}/10^{16} = **2.25 × 10^{4} cm^{−3}**.

**F2.** (a) √(2.8 × 10^{19} × 1.04 × 10^{19}) = 1.71 × 10^{19}; e^{−1.12/0.0518} = 4.06 × 10^{−10}; n_{i} = **6.9 × 10^{9} cm^{−3}** (textbooks quote 1–1.5 × 10^{10}: the result is very sensitive to E_{g} and N_{V}). (b) Two doublings: **× 4**.

**F3.** (a) **½**. (b) 1/(1 + e^{3}) = **0.047**. (c) 1/(1 + e^{21.6}) ≈ **4 × 10^{−10}**.

**F4.** (a) 2.8 × 10^{19} × e^{−9.65} = **1.8 × 10^{15} cm^{−3}**. (b) 1.04 × 10^{19} × e^{−7.72} = **4.6 × 10^{15} cm^{−3}**.

**F5.** Intrinsic: n = p. N_{C}e^{−(E_{C} − E_{F})/kT} = N_{V}e^{−(E_{F} − E_{V})/kT}. Take ln: −(E_{C} − E_{F}) = ln(N_{V}/N_{C})kT − (E_{F} − E_{V}). So 2E_{F} = E_{C} + E_{V} + kT ln(N_{V}/N_{C}), giving E_{F} = (E_{C} + E_{V})/2 + (kT/2)ln(N_{V}/N_{C}). The second term is −13 mV, so **E_{F} ≈ mid-gap**.

**F6.** E_{F} − E_{i} = 0.0259 × ln(10^{6}) = **0.358 eV** above mid-gap. E_{C} − E_{F} = 0.0259 × ln(2.8 × 10^{19}/10^{16}) = **0.206 eV**. Check: 0.358 + 0.206 ≈ 0.56 eV, half the gap.

**F7.** v_{d} = 1350 × 100 = **1.35 × 10^{5} cm/s**, about **87 times slower** than v_{th}.

**F8.** (a) σ = 1.6 × 10^{−19} × 10^{10} × 1950 = **3.12 × 10^{−6} (Ω·cm)^{−1}**; ρ = **3.2 × 10^{5} Ω·cm**. (b) n_{i} doubles, μ barely changes: σ **doubles**.

**F9.** (a) p = 10^{20}/(5 × 10^{17}) = **200 cm^{−3}**. (b) μ_{n} = 32/(1.6 × 10^{−19} × 5 × 10^{17}) = **400 cm^{2}/V·s** (down from about 1400 in pure Si: ion scattering). (c) 32/3.12 × 10^{−6} ≈ **10^{7} times**.

**F10.** L = 0.1 cm, A = 10^{−4} cm^{2}. R = 0.5 × 0.1/10^{−4} = **500 Ω**; I = **10 mA**.

**F11.** R_{s} = 0.01/10^{−4} = **100 Ω/□**; 20 squares; R = **2 kΩ**.

**F12.** dn/dx = (10^{16} − 10^{17})/10^{−4} = **−9 × 10^{20} cm^{−4}**. F_{n} = **3.15 × 10^{22} cm^{−2}s^{−1}**, toward +x.

**F13.** J_{n} = 1.6 × 10^{−19} × 35 × (−10^{18}) = **−5.6 A/cm^{2}**: electrons move to +x, current flows to −x.

**F14.** Drift **21.6 A/cm^{2}**; diffusion **−5.6 A/cm^{2}**; total **16.0 A/cm^{2}** along +x.

**F15.** (a) D_{n} = 1350 × 0.0259 = **35 cm^{2}/s**; D_{p} = 480 × 0.0259 = **12.4 cm^{2}/s**. (b) In equilibrium E_{F} is flat and n = N_{C}e^{−(E_{C} − E_{F})/kT}, so dn/dx = −(n/kT) dE_{C}/dx. The band slope is the field: dE_{C}/dx = qE. So dn/dx = −nqE/kT. Set J_{n} = qnμ_{n}E + qD_{n}(−nqE/kT) = 0 → μ_{n} = D_{n}q/kT → D_{n}/μ_{n} = **kT/q**.

**F16.** n-type, low injection: n ≈ n_{0} ≫ p, n_{1}, p_{1}, so the denominator ≈ τ_{p}n_{0}. Numerator: n_{0}(p_{0} + Δp) − n_{i}^{2} = n_{0}Δp (because n_{0}p_{0} = n_{i}^{2}). R − G = n_{0}Δp/(τ_{p}n_{0}) = **Δp/τ_{p}**.

**F17.** 10^{14} × e^{−1} = **3.68 × 10^{13}**; 10^{14} × e^{−3} = **4.98 × 10^{12} cm^{−3}**.

**F18.** No field: J_{p} = −qD_{p}dp/dx, so −(1/q)∂J_{p}/∂x = D_{p}∂^{2}p/∂x^{2}. Steady state, R − G = Δp/τ_{p}: **D_{p} d^{2}Δp/dx^{2} = Δp/τ_{p}**, solved by F19.

**F19.** L_{p} = √(12.4 × 10^{−6}) = **35.2 μm**. Δp(50 μm) = 10^{14} × e^{−1.42} = **2.42 × 10^{13} cm^{−3}**.

**F20.** (a) As in the card. (b) dE/dx = qN_{D}/ε = **1.54 × 10^{9} V/cm^{2}**; over 10^{−5} cm, E grows by **1.54 × 10^{4} V/cm**.

<!--/ANSWERS-->
