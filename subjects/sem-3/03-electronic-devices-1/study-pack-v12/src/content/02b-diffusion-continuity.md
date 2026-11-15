# 02b — Diffusion, recombination and continuity

<div class="sub">Unit 1–2 deck, slides 53–65 · syllabus Unit 1 (diffusion, Einstein relation, generation and recombination, continuity equation) · needs 01b (n = N_{C}e^{−(E_{C} − E_{F})/kT}, E_{F} flat) and 02a (drift, μ, flux, J) · three deck derivations (slide 57 Einstein, slides 62–64 continuity, slide 61 SRH); other openers are Predict prompts or practice problems</div>

## Map

[[map:1 Diffusion: crowds spread > 2 Fick's law > 3 Diffusion current and signs > 4 Total current > 5 Equilibrium: drift cancels diffusion > 6 Einstein relation > 7 Generation, recombination > 8 Direct G–R > 9 Trap G–R (SRH) > 10 Lifetime τ > 11 Continuity equation > 12 Diffusion length L > 13 Poisson's equation|here=1]]

02a moved carriers with a field. This file adds the second way: carriers spread from where they are crowded, with **no field at all**. Then it asks how carriers are **created and destroyed**, and puts flow and creation into one bookkeeping equation, the **continuity equation**. 03 uses every piece: the pn junction is diffusion balanced by drift, and the diode current is diffusion of carriers that recombine within a length L.

## The questions this file answers

- <span class="tag">Deck slide 57</span> Derive Einstein's relation D_{n}/μ_{n} = kT/q.
- <span class="tag">Deck slides 62–64</span> Derive the continuity equation for electrons and holes.
- <span class="tag">Deck slide 61</span> State the SRH net recombination rate and explain each symbol.
- <span class="tag">Deck slide 65</span> Write Poisson's equation for a semiconductor and explain each term.
- <span class="tag">practice</span> Diffusion current for a given gradient; decay of excess carriers; diffusion length.

---

## Build

### 1 · Diffusion: a crowd spreads out by itself

:::guess Predict
Put a drop of ink into still water. Nothing pushes the ink. A minute later, is it still a drop? What makes it move, and in which direction?
:::

[[fig:diffusion_spread|What this graph plots: for each position x (horizontal), how many carriers per cm^{3} sit there (vertical), at three moments (deck slide 53). A point on a curve = "at this time, this place holds this many". The peak falls and the curve widens.|w=70]]

- Each carrier does the random walk of 02a step 1. No carrier "knows" where the crowd is.
- But count crossings at a plane. If one side holds more carriers, more of them happen to cross from that side:

[[fig:crossing_count|Half the carriers on each side head toward the plane. 26 on the left send 13 across; 7 on the right send 3.5 back. Net: 9.5 cross left to right.|w=72]]

- So the crowd spreads, **from crowded to sparse**, until the concentration is the same everywhere. This net flow is **diffusion** (deck slide 53). No field and no force are needed.

**Answer to the Predict.** The ink spreads out; random motion of its molecules moves it from where it is concentrated to where it is not.

:::check Check 1
(a) Does any single carrier move toward the sparse side on purpose? (b) When does net diffusion stop? (c) Why does a uniform n-type bar have no diffusion?
:::

### 2 · Fick's law: flux is set by the slope

:::q <span class="tag">practice</span>
The electron concentration falls in a straight line from 10^{17} to 10^{16} cm^{−3} over 1 μm. D_{n} = 35 cm^{2}/s. Find the electron diffusion flux.
:::

:::guess Guess first
A gentle slope and a steep slope of n: which gives the larger flow? Which way does it go?
:::

:::note Terms
**Gradient dn/dx:** how fast n changes with position, in cm^{−3} per cm = cm^{−4}; the slope of the n(x) curve. **Diffusion coefficient D:** flux per unit gradient, in cm^{2}/s; how fast that carrier spreads. Set by the same scattering that sets μ (step 6).
:::

[[fig:fick_slopes|What these graphs plot: carrier concentration (vertical) against position (horizontal). Left: concentration falls with x, so the flow goes to +x. Right: it rises with x, so the flow goes to −x (deck slide 54).|w=82]]

- Twice the slope → twice the imbalance at each plane → twice the flux (deck slide 54):

$$F_{n} = −D_{n} \frac{dn}{dx}      F_{p} = −D_{p} \frac{dp}{dx}$$

- The **minus sign** says the flow runs **downhill**: where dn/dx < 0, F is positive (+x).
- **Units** (deck slide 54): F in cm^{−2}s^{−1}, dn/dx in cm^{−4}, so D in **cm^{2}/s**.

**Answer.** dn/dx = (10^{16} − 10^{17}) / 10^{−4} cm = **−9 × 10^{20} cm^{−4}**.
F_{n} = −35 × (−9 × 10^{20}) = **3.15 × 10^{22} electrons per cm^{2} per second**, toward +x (downhill).

:::check Check 2
(a) Holes with dp/dx > 0: which way do they flow? (b) The slope is halved. What happens to the flux? (c) Show that D has units cm^{2}/s.
:::

### 3 · Diffusion current, and why the signs differ

Flux counts particles. Current counts charge: multiply by the charge of each carrier.

:::q <span class="tag">practice</span>
In a silicon bar the electron concentration falls by 10^{18} cm^{−3} per cm (dn/dx = −10^{18} cm^{−4}). D_{n} = 35 cm^{2}/s. Find the electron diffusion current density and its direction.
:::

:::guess Guess first
Electrons diffuse toward +x. Which way does their current point?
:::

[[fig:diff_signs|The same falling profile for both carriers. Both diffuse toward +x. Electrons carry −q, so their current points to −x; holes carry +q, so their current points to +x (deck slide 55).|w=88]]

- Electrons: J_{n} = (−q) × F_{n} = (−q)(−D_{n} dn/dx):

$$J_{n,diff} = +qD_{n} \frac{dn}{dx}      J_{p,diff} = −qD_{p} \frac{dp}{dx}$$

- The hole formula keeps Fick's minus sign; the electron formula loses it, because of the electron's negative charge.

**Answer.** J_{n} = 1.6 × 10^{−19} × 35 × (−10^{18}) = **−5.6 A/cm^{2}**. The electrons move to +x; the current flows to **−x**.

:::check Check 3
(a) Holes with dp/dx = −10^{18} cm^{−4}, D_{p} = 12.4 cm^{2}/s: J_{p} and its direction? (b) In one sentence: why do electron and hole diffusion currents in the same falling profile point opposite ways?
:::

### 4 · Total current = drift + diffusion

A real device often has a field **and** a gradient at the same place. Each carrier type then has both currents.

:::q <span class="tag">practice</span>
At one point in n-type Si: n = 10^{16} cm^{−3}, E = 10 V/cm along +x, dn/dx = −10^{18} cm^{−4}, μ_{n} = 1350, D_{n} = 35. Find the drift, diffusion and total electron current densities.
:::

:::guess Guess first
Do the two parts add or partly cancel here?
:::

:::note Terms
**J_{n}, J_{p}:** total electron and hole current densities. **J:** the total current density, J_{n} + J_{p}; the one an ammeter sees (per cm^{2}).
:::

- Add 02a's drift to step 3's diffusion, for each carrier (deck slide 55):

$$J_{n} = qnμ_{n}E + qD_{n}\frac{dn}{dx}      J_{p} = qpμ_{p}E − qD_{p}\frac{dp}{dx}      J = J_{n} + J_{p}$$

| Device region | Which term carries the current |
|---|---|
| doped resistor (uniform) | drift only: no gradient |
| forward-biased diode, neutral sides | diffusion of minority carriers (03) |
| depletion region in equilibrium | huge drift and huge diffusion, cancelling (step 5) |

:::note Deck slide 65
The pasted web page writes J_{p} = qμ_{p}pE **+** qD_{p}dp/dx. The diffusion term for holes is **−qD_{p}dp/dx** (step 3; deck slide 55 has it right).
:::

**Answer.** Drift: 1.6 × 10^{−19} × 10^{16} × 1350 × 10 = **21.6 A/cm^{2}** (+x). Diffusion: 1.6 × 10^{−19} × 35 × (−10^{18}) = **−5.6 A/cm^{2}**. Total J_{n} = **16.0 A/cm^{2}** (+x). They partly cancel.

:::check Check 4
(a) Write the total hole current density with both terms. (b) In the question, what gradient dn/dx would make J_{n} = 0?
:::

### 5 · Equilibrium: drift and diffusion cancel exactly

:::guess Predict
A bar is doped unevenly: 10^{17} donors per cm^{3} at the left, falling to 10^{15} at the right. No battery. Electrons diffuse to the right. Does a current flow forever? If not, what stops it?
:::

:::note Terms
**Equilibrium:** nothing connected, no light, steady temperature. **Built-in field:** a field created inside the material by its own charges, with no battery.
:::

[[fig:equilibrium_balance|Same bar, three views against position x in μm (after deck slide 56). ① Energy above E_{F}: E_{F} is flat, E_{C} rises where n falls. ② n on a log scale. ③ The electron diffusion current and the electron drift current: mirror images, sum zero at every x.|w=98]]

1. Electrons diffuse right. They leave behind fixed **+ donor ions** on the left and pile up as **− charge** on the right.
2. That charge makes a **field pointing right** (+ to −). It pushes electrons **back to the left**: a drift current.
3. Diffusion builds the field until the drift exactly cancels it, at **every** point.

- **Each** carrier's current is zero separately: J_{n} = 0 and J_{p} = 0, so J_{n}^{drift} = −J_{n}^{diff} (deck slide 56, detailed balance). If only the sum were zero, electrons would pile up somewhere forever.
- On the band diagram: **E_{F} is flat** (01b); E_{C} − E_{F} = kT ln(N_{C}/n) grows where n falls, so **the bands tilt**. A tilt of the bands **is** the built-in field: E = (1/q) dE_{C}/dx.
- The potential step across the bar: kT/q × ln(10^{17}/10^{15}) = 0.0259 × 4.61 = **0.119 V**. 03 does the same for a pn junction.

**Answer to the Predict.** A current flows only for an instant. The charge it moves builds a field whose drift current cancels the diffusion current. Then J = 0 everywhere.

:::check Check 5
(a) Why must J_{n} and J_{p} each be zero, not just their sum? (b) Find E_{C} − E_{F} at the left end (n = 10^{17}) and right end (n = 10^{15}); use N_{C} = 2.8 × 10^{19}. Their difference? (c) Which way does the built-in field point, and why?
:::

### 6 · The Einstein relation: D and μ are tied together

:::q <span class="tag">Deck slide 57</span>
In a non-degenerate semiconductor in equilibrium, use J_{n}^{drift} = −J_{n}^{diff} to show that D_{n}/μ_{n} = kT/q.
:::

:::guess Guess first
Which two facts from earlier steps do you need: one about n, one about the field?
:::

:::note Terms
**Thermal voltage V_{T} = kT/q:** the energy kT expressed in volts. 0.0259 V at 300 K. **Non-degenerate:** E_{F} more than 3kT from the band edges, so n = N_{C}e^{−(E_{C} − E_{F})/kT} holds (01b step 6).
:::

**Answer** (deck slide 57; E_{F} constant, E_{C} varies with x):

1. n = N_{C}e^{−(E_{C} − E_{F})/kT}.
2. Drift, with the field from the band tilt E = (1/q)dE_{C}/dx: J_{n}^{drift} = qnμ_{n}E = **nμ_{n} dE_{C}/dx**.
3. Diffusion: differentiate line 1: dn/dx = n × (−1/kT) dE_{C}/dx. So J_{n}^{diff} = qD_{n}dn/dx = **−(q/kT) D_{n} n dE_{C}/dx**.
4. Set J_{n}^{drift} = −J_{n}^{diff}: nμ_{n} dE_{C}/dx = (q/kT) D_{n} n dE_{C}/dx.
5. Cancel n dE_{C}/dx:

$$\frac{D_{n}}{μ_{n}} = \frac{D_{p}}{μ_{p}} = \frac{kT}{q} = V_{T}$$

- **Why it makes sense:** a carrier that scatters rarely (long τ) both drifts easily (large μ) and spreads fast (large D). One scattering process sets both, so their ratio depends only on temperature.
- **Units** (deck slide 57): (cm^{2}/s)/(cm^{2}/V·s) = V. ✓
- **Numbers (300 K):** D_{n} = 1350 × 0.0259 = **35.0 cm^{2}/s**; D_{p} = 480 × 0.0259 = **12.4 cm^{2}/s**.

:::check Check 6
(a) At 400 K, V_{T} = ? If μ_{n} = 1000 there, D_{n} = ? (b) D_{n} for μ_{n} = 1500 at 300 K? (c) A data sheet gives μ and D for a sample that do not satisfy D/μ = kT/q at its temperature. What should you suspect?
:::

### 7 · Generation and recombination

Steps 1–6 moved carriers around. Now: carriers being **created** and **destroyed**.

:::guess Predict
In pure Si at 300 K, bonds break all the time, each one making an electron and a hole. Why does n_{i} not keep growing?
:::

:::note Terms
**EHP:** electron–hole pair. **Generation G:** pairs created per cm^{3} per second (energy in: heat or light). **Recombination R:** pairs destroyed per cm^{3} per second (an electron falls into a hole; energy out).
:::

[[fig:gr_events|Before and after on the band diagram (deck slide 58). Generation: an electron jumps from E_{V} to E_{C}, leaving a hole. Recombination: an electron in E_{C} drops into a hole in E_{V}; both vanish.|w=92]]

- The rates depend on (deck slide 58): the band structure, light of a suitable wavelength, defects and impurities, the carrier densities, the temperature.
- R grows with how many electrons **and** holes there are to meet: more of both → more recombination.
- **Equilibrium:** G = R. That balance is what holds n · p at n_{i}^{2} (01a step 8).
- **Disturbed** (light, or a diode in forward bias): extra carriers make R > G, so the excess dies away. Too few carriers (a reverse-biased junction): G > R, so pairs are made. **R − G** is the **net** rate that pulls n·p back toward n_{i}^{2}.

**Answer to the Predict.** Recombination: the more pairs exist, the faster they meet and vanish, until destruction matches creation.

:::check Check 7
(a) In equilibrium, what is R − G? (b) Shine light on a sample: sign of R − G just after the light goes off? (c) In which device region is n·p < n_{i}^{2}, so G > R?
:::

### 8 · Direct (band-to-band) generation and recombination

:::guess Predict
LEDs are made from GaAs, not silicon. Guess why.
:::

:::note Terms
**Photon:** a particle of light; carries energy, almost no momentum. **Phonon:** a quantum of lattice vibration (heat); carries momentum. **Direct / indirect gap:** in GaAs an electron at E_{C} can drop straight to E_{V}; in Si it also needs a momentum change, which only a phonon can supply.
:::

[[fig:direct_vs_trap|Left: direct recombination, one jump E_{C} → E_{V}, energy E_{g} leaves as a photon (deck slide 59). Right: recombination through a trap level E_{T} in two steps, ① and ②; the energy leaves as heat (deck slides 60–61).|w=92]]

- **Direct recombination** (deck slide 59): a conduction electron meets a valence hole in one jump. The energy E_{g} leaves as a **photon** (radiative) or as phonons (non-radiative).
- **Direct generation:** the reverse. A photon (photo-generation) or phonons (thermal generation) lift an electron E_{V} → E_{C}.
- Both bands take part, so these are called **band-to-band** G–R.
- **GaAs** (direct gap): band-to-band is fast and gives light. **Si** (indirect gap): it is rare, because a phonon must take part at the same moment.
- Photon wavelength λ (nm) = 1240/E_{g} (eV): GaAs, 1240/1.42 = **873 nm** (infrared); Si, 1240/1.12 = **1107 nm**.

**Answer to the Predict.** GaAs has a direct gap, so its electrons and holes recombine by giving off light. In Si they mostly recombine through traps and give off heat (step 9).

:::check Check 8
(a) Where does the energy go in radiative and in non-radiative recombination? (b) Why is band-to-band recombination rare in Si? (c) Which photon wavelength would a material with E_{g} = 1.97 eV emit?
:::

### 9 · Recombination through traps (SRH)

:::q <span class="tag">Deck slide 61</span>
State the Shockley–Read–Hall net recombination rate. Show that in n-type Si with a small excess of holes Δp it becomes R − G ≈ Δp/τ_{p}.
:::

:::guess Guess first
In n-type Si, which carrier is scarce? Which one would limit how fast pairs can meet at a trap?
:::

:::note Terms
**G–R centre (trap):** a defect or impurity atom with an allowed level E_{T} inside the gap (deck slide 60). **τ_{n}, τ_{p}:** electron and hole lifetimes, set by how many traps there are and how readily they capture. **n_{1}, p_{1}:** the n and p you would have if E_{F} sat at E_{T} (deck slide 61).
:::

- **Two steps** (figure in step 8, right): ① an electron drops from E_{C} into the trap; ② it drops from the trap into a hole in E_{V}. Each step needs only part of E_{g}, so each is easy. The energy leaves as heat. In Si this is the main route (deck slide 61).
- Traps work best near **mid-gap**, E_{T} ≈ E_{i}: neither half-step is too large (deck slide 60).
- The net rate (deck slide 61):

$$R − G = \frac{np − n_{i}^{2}}{τ_{p}(n + n_{1}) + τ_{n}(p + p_{1})}      n_{1} = n_{i}e^{(E_{T} − E_{i})/kT},  p_{1} = n_{i}e^{(E_{i} − E_{T})/kT}$$

- **Read the top:** np − n_{i}^{2} = how far from equilibrium. Zero in equilibrium; positive with excess carriers (R wins); negative with a shortage (G wins).

**Answer** (mid-gap trap, so n_{1} = p_{1} = n_{i}):

1. n-type: n ≈ N_{D}, much larger than p, n_{i}.
2. p = p_{0} + Δp, with N_{D}p_{0} = n_{i}^{2}. Top: N_{D}(p_{0} + Δp) − n_{i}^{2} = **N_{D}Δp**.
3. Bottom: τ_{p}(N_{D} + n_{i}) + τ_{n}(p + n_{i}) ≈ **τ_{p}N_{D}**.
4. So **R − G ≈ Δp/τ_{p}**: the rate is set by the **minority** carrier and its lifetime. (Checked numerically for N_{D} = 10^{16}, Δp = 10^{12}: within 1 %.)

:::check Check 9
(a) E_{T} = E_{i}: what are n_{1} and p_{1}? (b) Why does the minority carrier set the rate in doped Si? (c) Sign of R − G where np < n_{i}^{2}?
:::

### 10 · Lifetime: excess carriers die away exponentially

:::q <span class="tag">practice</span>
Light creates Δp = 10^{14} cm^{−3} extra holes in n-type Si with τ_{p} = 1 μs. The light goes off at t = 0. How many extra holes are left after 1 μs and after 3 μs?
:::

:::guess Guess first
After 1 μs, none, about half, or about a third?
:::

:::note Terms
**Excess Δp:** holes above the equilibrium value p_{0}. **Minority-carrier lifetime τ_{p}:** the average time an extra hole survives before it recombines.
:::

[[fig:lifetime_decay|What this graph plots: time after the light goes off, in lifetimes (horizontal), against the fraction of extra holes still left (vertical). A point = "after this many lifetimes, this fraction remains".|w=66]]

- From step 9: the loss rate is Δp/τ_{p}. A loss proportional to what is left gives an exponential:

$$\frac{dΔp}{dt} = −\frac{Δp}{τ_{p}}   ⇒   Δp(t) = Δp(0) e^{−t/τ_{p}}$$

- Each lifetime leaves 1/e = 0.368 of what there was.

**Answer.** t = 1 μs = τ: 10^{14} × 0.368 = **3.68 × 10^{13} cm^{−3}**. t = 3 μs: 10^{14} × e^{−3} = **4.98 × 10^{12} cm^{−3}** (5 %).

:::check Check 10
(a) How many lifetimes until only 1 % is left? (b) How many until half is left? (c) 03 says τ sets how fast a diode switches off. Longer τ: faster or slower switch-off?
:::

### 11 · The continuity equation: bookkeeping for a small box

Steps 2–6 gave flow; steps 7–10 gave creation and loss. One equation counts both.

:::q <span class="tag">Deck slides 62–64</span>
Derive the continuity equation for electrons, and write it for holes.
:::

:::guess Guess first
List every way the number of electrons in a small box can change.
:::

[[fig:continuity_box|A thin box, face area A, from x to x + Δx (deck slide 62). Electrons flow in through the left face, out through the right, and are lost inside by net recombination.|w=80]]

**Answer** (n, F vary only along x; deck slide 63):

1. Electrons in the box: nAΔx. Its rate of change: AΔx ∂n/∂t.
2. In per second through the left face: F_{n}(x)A. Out through the right: F_{n}(x + Δx)A.
3. Lost inside per second: (R − G)AΔx.
4. Balance: AΔx ∂n/∂t = F_{n}(x)A − F_{n}(x + Δx)A − (R − G)AΔx.
5. Divide by AΔx, let Δx → 0 (deck slide 64):

$$\frac{∂n}{∂t} = −\frac{∂F_{n}}{∂x} − (R − G)$$

6. Use J_{n} = −qF_{n} and J_{p} = +qF_{p}:

$$\frac{∂n}{∂t} = +\frac{1}{q}\frac{∂J_{n}}{∂x} − (R − G)      \frac{∂p}{∂t} = −\frac{1}{q}\frac{∂J_{p}}{∂x} − (R − G)$$

- **In words:** change in the box = (net flow in) − (net recombination). The sign before ∂J/∂x differs only because of the carrier's charge.

:::note Deck slide 64
The slide writes J_{p} = +qF_{n}. It should be **J_{p} = +qF_{p}** (holes' own flux). The final hole equation on the slide is right.
:::

:::check Check 11
(a) Steady state (∂n/∂t = 0) and no recombination: what does the equation say about J_{n} along x? (b) A uniform sample (no gradients, no flow): reduce the hole equation and compare with step 10. (c) Why the opposite sign of ∂J/∂x for holes?
:::

### 12 · Diffusion length: how far injected carriers get

The continuity equation's most-used result: holes are pushed into an n-type region at one end (as a diode does in 03). They diffuse in and recombine on the way.

:::q <span class="tag">practice</span>
Holes are held at Δp(0) = 10^{14} cm^{−3} at x = 0 of a long n-type Si region; no field. D_{p} = 12.4 cm^{2}/s, τ_{p} = 1 μs. Find the diffusion length L_{p} and Δp at x = 50 μm.
:::

:::guess Guess first
Will the holes reach 1 mm in? 50 μm?
:::

:::note Terms
**Steady state:** nothing changes with time (∂/∂t = 0). **Diffusion length L:** the distance over which the excess falls to 1/e; L = √(Dτ).
:::

[[fig:diff_length|What this graph plots: distance into the n-type side (horizontal, μm) against the fraction of the injected excess still there (vertical). A point = "this deep in, this fraction of Δp(0) remains". L_{p} = 35.2 μm.|w=70]]

1. No field: J_{p} = −qD_{p} dΔp/dx (step 3).
2. Steady state, hole equation of step 11, with R − G = Δp/τ_{p} (step 9): 0 = D_{p} d^{2}Δp/dx^{2} − Δp/τ_{p}.
3. So d^{2}Δp/dx^{2} = Δp/L_{p}^{2}, with **L_{p} = √(D_{p}τ_{p})**. The solution that dies away inside the region:

$$Δp(x) = Δp(0) e^{−x/L_{p}}$$

**Answer.** L_{p} = √(12.4 × 10^{−6}) = 3.52 × 10^{−3} cm = **35.2 μm**. Δp(50 μm) = 10^{14} × e^{−50/35.2} = 10^{14} × 0.242 = **2.42 × 10^{13} cm^{−3}**. Almost none reach 1 mm.

- The hole current at x = 0 is qD_{p}Δp(0)/L_{p}: steeper profile (short L) → more current. This is the diode current of 03.

:::check Check 12
(a) L_{n} for D_{n} = 35 cm^{2}/s, τ_{n} = 1 μs? (b) τ is made 4 times longer. What happens to L? (c) Find the hole current density at x = 0 in the question.
:::

### 13 · Poisson's equation: charge makes field

:::q <span class="tag">Deck slide 65</span>
Write Poisson's equation for a semiconductor and explain each term.
:::

:::guess Guess first
Where in a device is the net charge not zero?
:::

:::note Terms
**Charge density ρ(x):** net charge per cm^{3} (not resistivity; same letter). **Permittivity ε:** how strongly the material weakens a field; Si: ε = 11.7ε_{0} = 1.04 × 10^{−12} F/cm. **Potential V:** volts; the field is its downhill slope, E = −dV/dx.
:::

[[fig:poisson_stack|Three graphs against position x for a layer of − charge next to a layer of + charge (the shape of a pn junction's depletion region, 03). ① charge density; ② field: its slope is ρ/ε; ③ potential: its slope is −E.|w=92]]

$$\frac{dE}{dx} = \frac{ρ}{ε} = \frac{q}{ε}(p − n + N_{D}^{+} − N_{A}^{−})$$

- **Four charges** (deck slide 65): holes (+), electrons (−), ionised donors (+), ionised acceptors (−).
- **Neutral region:** they balance, ρ = 0, so the field is constant (a uniform resistor).
- **Depletion region (03):** carriers gone, ions left, ρ ≠ 0: the field ramps up, and the potential bends. That is the built-in voltage.

**Answer.** dE/dx = ρ/ε: the field changes in proportion to the net charge; ρ = q(p − n + N_{D}^{+} − N_{A}^{−}); ε = 11.7ε_{0} for Si; and E = −dV/dx links the field to the potential.

:::check Check 13
(a) 1 μm of Si with N_{D}^{+} = 10^{16} cm^{−3} and no electrons. By how much does E change across it? (b) What is ρ in a uniformly doped neutral region? (c) The letter ρ means two things in this unit. Which two?
:::

---

## Exam form

**Diffusion (deck slides 53–55).** Random motion + a concentration gradient → net flow from high to low. Fick: F = −D dn/dx. J_{n,diff} = +qD_{n}dn/dx; J_{p,diff} = −qD_{p}dp/dx. D in cm^{2}/s.

**Total current.** J_{n} = qnμ_{n}E + qD_{n}dn/dx; J_{p} = qpμ_{p}E − qD_{p}dp/dx; J = J_{n} + J_{p}. In equilibrium J_{n} = J_{p} = 0 separately: drift cancels diffusion.

**Einstein relation (deck slide 57).**

1. n = N_{C}e^{−(E_{C} − E_{F})/kT}, E_{F} constant.
2. J_{n}^{drift} = qnμ_{n}(1/q)dE_{C}/dx = nμ_{n}dE_{C}/dx.
3. J_{n}^{diff} = qD_{n}dn/dx = −(q/kT)D_{n}n dE_{C}/dx.
4. Equilibrium: J^{drift} = −J^{diff} → **D_{n}/μ_{n} = kT/q = V_{T}** (0.0259 V at 300 K). Same for holes.

**G–R (deck slides 58–61).** Generation = pair created, recombination = pair destroyed; equilibrium G = R. Direct (band-to-band): photon or phonon; GaAs. Indirect via a trap at E_{T} near mid-gap, two steps; Si. SRH: R − G = (np − n_{i}^{2})/[τ_{p}(n + n_{1}) + τ_{n}(p + p_{1})]. Low injection, n-type: R − G = Δp/τ_{p}; Δp(t) = Δp(0)e^{−t/τ_{p}}.

**Continuity (deck slides 62–64).** Box AΔx: AΔx ∂n/∂t = F_{n}(x)A − F_{n}(x + Δx)A − (R − G)AΔx → ∂n/∂t = (1/q)∂J_{n}/∂x − (R − G); ∂p/∂t = −(1/q)∂J_{p}/∂x − (R − G).

**Diffusion length.** Steady state, no field: D_{p}d^{2}Δp/dx^{2} = Δp/τ_{p} → Δp(x) = Δp(0)e^{−x/L_{p}}, L_{p} = √(D_{p}τ_{p}).

**Poisson (deck slide 65).** dE/dx = ρ/ε = (q/ε)(p − n + N_{D}^{+} − N_{A}^{−}); E = −dV/dx.

## Traps

- Sign of the electron diffusion current: **+qD_{n}dn/dx** (the minus of Fick's law cancels with −q).
- Copying the slide-65 hole equation with **+qD_{p}dp/dx**: it is **−**.
- V_{T} = 26 **mV**, not 26 V: D_{n} = 1350 × 0.0259, not × 26.
- Saying equilibrium means "no carrier motion": both currents can be large; they **cancel**.
- Thinking diffusion needs a field: it needs only a **gradient**.
- Using τ of the majority carrier: lifetime in doped material is the **minority** carrier's.
- Writing L = Dτ: it is **√(Dτ)**.

## Self-test

1. D_{p} for μ_{p} = 450 at 300 K?
2. Holes in n-type Si: dp/dx = +10^{19} cm^{−4}, D_{p} = 12 cm^{2}/s. J_{p,diff} and its direction?
3. D = 10 cm^{2}/s, τ = 0.1 μs. Find L.
4. What fraction of an excess survives 2 lifetimes?
5. Derive D_{n}/μ_{n} = kT/q from memory.
6. Derive the continuity equation for holes from a box.
7. Name the two kinds of recombination and the material each dominates in.
8. Why must a built-in field appear wherever doping varies?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **No**: each moves at random; the net flow comes only from there being more of them on one side. (b) When the concentration is **uniform**. (c) n is the same everywhere: **no gradient**.

**Check 2.** (a) dp/dx > 0 → F_{p} < 0: toward **−x** (downhill). (b) The flux **halves**. (c) D = F/(dn/dx) = (cm^{−2}s^{−1})/(cm^{−4}) = **cm^{2}/s**.

**Check 3.** (a) J_{p} = −1.6 × 10^{−19} × 12.4 × (−10^{18}) = **+1.98 A/cm^{2}**, toward **+x**. (b) Both diffuse the same way, but they carry **opposite charges**, so their currents point opposite ways.

**Check 4.** (a) J_{p} = qpμ_{p}E − qD_{p}dp/dx. (b) 0 = qnμ_{n}E + qD_{n}dn/dx → dn/dx = −nμ_{n}E/D_{n} = −10^{16} × 1350 × 10/35 = **−3.86 × 10^{18} cm^{−4}**.

**Check 5.** (a) If only the sum were zero, electrons would flow one way and holes the other forever, piling up charge; with nothing connected that cannot last. (b) Left: 0.0259 × ln(2.8 × 10^{19}/10^{17}) = **0.146 eV**; right: 0.0259 × ln(2.8 × 10^{19}/10^{15}) = **0.265 eV**; difference **0.119 eV**. (c) **To the right (+x)**, from the + donor ions left behind to the − electrons piled up; it pushes electrons back left.

**Check 6.** (a) V_{T} = 8.617 × 10^{−5} × 400 = **0.0345 V**; D_{n} = **34.5 cm^{2}/s**. (b) 1500 × 0.0259 = **38.9 cm^{2}/s**. (c) A wrong value, or a **degenerate** (very heavily doped) sample, where the Boltzmann form behind the relation fails.

**Check 7.** (a) **Zero**. (b) **Positive**: excess carriers, recombination wins. (c) A **reverse-biased junction** (its depletion region), where carriers are swept out.

**Check 8.** (a) Radiative: a **photon** (light). Non-radiative: **phonons** (heat). (b) Si has an **indirect gap**: the jump needs a phonon at the same time, which is unlikely. (c) 1240/1.97 = **629 nm** (red).

**Check 9.** (a) n_{1} = p_{1} = **n_{i}**. (b) A pair needs one of each to meet at a trap; the **scarce** carrier sets how often that happens. (c) **Negative**: net generation.

**Check 10.** (a) ln 100 = **4.6 lifetimes**. (b) ln 2 = **0.69 lifetimes**. (c) **Slower**: stored minority carriers take longer to recombine.

**Check 11.** (a) ∂J_{n}/∂x = 0: **J_{n} is the same at every x** (what flows in flows out). (b) dp/dt = −(R − G) = −Δp/τ_{p}: the decay of **step 10**. (c) J_{n} = −qF_{n} but J_{p} = +qF_{p}: the **charge sign** flips.

**Check 12.** (a) √(35 × 10^{−6}) = 5.92 × 10^{−3} cm = **59.2 μm**. (b) L ∝ √τ: L **doubles**. (c) J_{p} = 1.6 × 10^{−19} × 12.4 × 10^{14} / 3.52 × 10^{−3} = **0.0564 A/cm^{2}** (56 mA/cm^{2}).

**Check 13.** (a) ΔE = qN_{D}W/ε = 1.6 × 10^{−19} × 10^{16} × 10^{−4} / 1.04 × 10^{−12} = **1.54 × 10^{5} V/cm**. (b) **Zero**. (c) **Resistivity** (02a) and **charge density** (here).

**Self-test.**

1. 450 × 0.0259 = **11.7 cm^{2}/s**.
2. J_{p} = −1.6 × 10^{−19} × 12 × 10^{19} = **−19.2 A/cm^{2}**, toward **−x** (holes flow downhill, toward −x).
3. L = √(10 × 10^{−7}) = 10^{−3} cm = **10 μm**.
4. e^{−2} = **0.135**.
5. Step 6, lines 1–5.
6. Step 11 with p: AΔx ∂p/∂t = F_{p}(x)A − F_{p}(x + Δx)A − (R − G)AΔx → ∂p/∂t = −∂F_{p}/∂x − (R − G) = −(1/q)∂J_{p}/∂x − (R − G).
7. **Direct (band-to-band)**: GaAs. **Through traps (SRH)**: Si.
8. Varying doping gives a gradient in n (or p), so carriers diffuse; with nothing connected the current must be zero, so a field builds until drift cancels diffusion at every point.

<!--/ANSWERS-->
