# 02a — Drift: current pushed by a field

<div class="sub">Unit 1–2 deck, slides 44–52 · syllabus Unit 1 (carrier transport: drift, mobility, conductivity, resistivity, sheet resistance) · needs 01a (n, p, n_{i}, doping, majority/minority) · two deck questions (slides 49–50 derivation, slide 51 example) and slide 52; other openers are Predict prompts or practice problems</div>

## Map

[[map:1 Thermal motion, no current > 2 Drift velocity, mobility > 3 Velocity saturation > 4 What sets μ > 5 Drift current J > 6 σ and ρ of pure Si > 7 Doping sets σ > 8 Resistance of a bar > 9 Sheet resistance|here=1]]

01a and 01b counted the carriers: n electrons and p holes per cm^{3}. Counting is not current. A current needs carriers to **move** in one direction on average. Two things make that happen (deck slide 45): a **field** pushes them (**drift**, this file), and a **crowd** spreads out (**diffusion**, 02b). 03a joins the two at the pn junction.

## The questions this file answers

- <span class="tag">Deck slides 49–50</span> Show that the drift current density is J = q(pμ_{p} + nμ_{n})E.
- <span class="tag">Deck slide 51</span> (a) Conductivity and resistivity of intrinsic Si at 300 K. (b) The effect of a 10 °C rise. μ_{n} = 1500, μ_{p} = 450 cm^{2}/V·s.
- <span class="tag">Deck slide 52</span> Si with N_{D} = 5 × 10^{17} cm^{−3} has σ = 32 (Ω·cm)^{−1}: compare with intrinsic Si.
- <span class="tag">practice</span> Resistance of a doped bar; sheet resistance of an IC resistor.

---

## Build

### 1 · Carriers already move, with no current

:::guess Predict
At room temperature a free electron in silicon moves at about 10 million cm/s. A silicon bar sits on the desk with nothing connected. Is a current flowing through it? Why or why not?
:::

:::note Terms
**Thermal velocity v_{th}:** the typical speed a carrier has just from heat. **Scattering:** a carrier hitting something that changes its direction: a vibrating atom or a charged dopant ion. **Mean free time τ:** the average time between two scatterings.
:::

[[fig:thermal_walk|One electron's path with no field (deck slide 46), 14 free flights. Each straight piece is free flight at v_{th}; each corner is a scattering that sends it off in a random direction.|w=60]]

- Heat gives each carrier kinetic energy: ½m v_{th}^{2} = (3/2)kT. With the free-electron mass, v_{th} = √(3kT/m) ≈ **1.2 × 10^{7} cm/s** at 300 K.
- It does not fly far: it scatters every **0.01–1 ps** (deck slide 47). At 10^{7} cm/s for 0.2 ps it covers only about **20 nm** before turning.
- Every direction after a scattering is equally likely, so after many scatterings the **average displacement is zero** (deck slide 46).

**Answer to the Predict.** No current. As many electrons cross any plane going left as going right, so the charge carried each way cancels.

:::check Check 1
(a) Name the two things a carrier scatters off. (b) Why does fast motion not mean current? (c) The scattering time doubles. How far does the electron fly between collisions at 10^{7} cm/s, if τ was 0.2 ps?
:::

### 2 · A field adds a drift: v_{d} = μE

A battery puts a field across the bar. The random motion stays; a small steady shift is added on top.

:::q <span class="tag">practice</span>
1 V is applied across a 100 μm long piece of lightly doped Si. The field is 1 V / 0.01 cm = 100 V/cm. With μ_{n} = 1350 cm^{2}/V·s, how fast do the electrons drift? Compare with v_{th} ≈ 1.17 × 10^{7} cm/s.
:::

:::guess Guess first
Faster or slower than the thermal speed, and by roughly how much?
:::

:::note Terms
**Electric field E:** volts per cm; the push per unit charge. **Drift velocity v_{d}:** the average velocity of the carriers along the field, after averaging out the random part. **Mobility μ:** drift velocity per unit field, in cm^{2}/V·s; how easily a carrier is pushed.
:::

[[fig:drift_walk|The same kind of random path with a field to the right (deck slides 46–47). Each free flight bends slightly with the field, so the path creeps: holes along E, electrons against E. The thick arrow is the net shift, the drift.|w=88]]

- Between scatterings the field accelerates the carrier; each scattering throws away the direction it gained. The result is a steady average velocity proportional to the field (deck slide 47):

$$v_{d} = μE$$

- **Holes** drift **along** E (charge +q). **Electrons** drift **against** E (charge −q).
- **What sets μ** (deck slide 47): μ = qτ/m\*. Longer time between scatterings (τ) → more speed gained → higher μ. Heavier effective mass m\* → less speed gained → lower μ. Holes in Si are heavier: μ_{p} ≈ 480 against μ_{n} ≈ 1350.
- **Units:** (cm/s)/(V/cm) = cm^{2}/V·s.

**Answer.** v_{d} = 1350 × 100 = **1.35 × 10^{5} cm/s**. That is about **87 times slower** than v_{th}: the drift is a slow creep on top of fast random motion.

:::check Check 2
(a) Hole drift velocity in the same field, μ_{p} = 480? (b) Given m\* = 0.26 m_{0} for Si electrons, find τ from μ_{n} = 1350 cm^{2}/V·s (convert μ to m^{2}/V·s first). (c) In which direction do electrons drift relative to E, and why?
:::

### 3 · At high field the drift velocity saturates

:::guess Predict
v_{d} = μE gave 1.35 × 10^{5} cm/s at 100 V/cm. Raise the field 1000 times, to 10^{5} V/cm. Does v_{d} become 1.35 × 10^{8} cm/s?
:::

:::note Terms
**Saturation velocity v_{sat}:** the speed v_{d} cannot exceed, about 10^{7} cm/s in Si (deck slides 47–48). It is close to v_{th}.
:::

[[fig:vsat_plot|What this graph plots: for each field strength (horizontal) the drift velocity it produces (vertical), both on log scales. A point on the blue curve = "at this field, electrons drift this fast". Straight 45° part: v_{d} = μE. Flat part: saturated.|w=72]]

**Reading the figure.**

- **Low field (up to a few kV/cm):** a straight line of slope 1 on the log–log plot. 10× the field gives 10× the drift (deck slide 47). This is where μ is a constant.
- **High field:** the curve bends over and flattens at v_{sat} ≈ 10^{7} cm/s. Carriers now gain so much energy between scatterings that they lose it at once by shaking the lattice.
- **Where it bends:** μE reaches v_{sat} at E = v_{sat}/μ = 10^{7}/1350 = **7.4 kV/cm** for electrons. A simple model of the curve: v_{d} = μE/(1 + μE/v_{sat}).
- GaAs electrons (deck slide 47) rise faster, overshoot to a peak, then fall back to saturation. Not needed for Si sums.

**Answer to the Predict.** No. 1350 × 10^{5} = 1.35 × 10^{8} cm/s would be 13× v_{sat}. The model gives 1.35 × 10^{8}/(1 + 13.5) = **9.3 × 10^{6} cm/s**, just under v_{sat}.

:::check Check 3
(a) At what field does μ_{p}E reach 10^{7} cm/s for holes, μ_{p} = 480? (b) A transistor channel is 100 nm long with 1 V across it. Find E. Is the electron drift linear or saturated? (c) In the saturated region, is "μ" still the slope v_{d}/E?
:::

### 4 · What sets the mobility: doping and temperature

Step 2 said μ = qτ/m\*. The mass is fixed by the material, so mobility changes only through τ: how often the carrier scatters.

:::guess Predict
Add 5 × 10^{17} donor atoms per cm^{3} to silicon. Each one becomes a fixed + ion. Does the electron mobility go up, down, or stay?
:::

:::note Terms
**Lattice scattering:** collisions with atoms vibrating from heat. More heat → more vibration → more collisions. **Impurity scattering:** a carrier's path bent by a charged dopant ion. More dopants → more collisions.
:::

[[fig:mobility_doping|What this graph plots: for each doping level (horizontal, log scale) the mobility at 300 K (vertical, log scale). A point = "in Si doped this heavily, carriers have this mobility". Curves from the Caughey–Thomas fit; the same shape as deck slide 48.|w=72]]

- **Both scatterings act at once.** Their rates add, so 1/μ = 1/μ_{lattice} + 1/μ_{impurity} (Matthiessen's rule). The worse one dominates.
- **Doping:** light doping (below about 10^{15}) changes almost nothing; above about 10^{16} the ions take over and μ falls steeply.

| Doping (cm^{−3}) | 10^{14} | 10^{16} | 10^{17} | 5 × 10^{17} | 10^{18} |
|---|---|---|---|---|---|
| μ_{n} (cm^{2}/V·s) | 1420 | 1230 | 780 | 420 | 310 |
| μ_{p} (cm^{2}/V·s) | 460 | 420 | 310 | — | 150 |

- **Temperature** (deck slide 48): lattice scattering grows with heat, μ_{lattice} ∝ T^{−3/2}, so **μ falls as T rises** in lightly doped Si. Impurity scattering weakens with heat (faster carriers are bent less), so heavily doped Si changes less.

**Answer to the Predict.** Down: 5 × 10^{17} ions cut μ_{n} from about 1430 to about **420**.

:::note Mobility values in questions
Questions give μ. Books quote 1350 or 1500 for "μ_{n}" in lightly doped Si; both are inside the spread. Use the value the question gives.
:::

:::check Check 4
(a) From the table, μ_{n} at N_{D} = 10^{17}? (b) Lightly doped Si is heated from 300 K to 400 K. By what factor does μ change (lattice scattering only)? (c) Why is μ_{p} below μ_{n} at every doping?
:::

### 5 · Drift current density: counting carriers through a slice

The carriers drift at v_{d}. Current is charge per second, so count how many cross a surface each second.

:::q <span class="tag">Deck slides 49–50</span>
Show that the drift current density in a semiconductor is J = q(pμ_{p} + nμ_{n})E.
:::

:::guess Guess first
The holes inside a slice of width Δx all cross its right face within some time. What time?
:::

:::note Terms
**Flux F:** the number of carriers crossing one cm^{2} per second (deck slide 49). **Current density J:** the current through one cm^{2}, in A/cm^{2}; J = (charge of each carrier) × flux.
:::

[[fig:flux_box|A bar with a field along +x (deck slide 49). The shaded slice has face area A and width Δx and holds p·A·Δx holes.|w=82]]

**Answer** (each line follows from the one before):

1. Holes in the slice: **pAΔx**. Moving at v_{d}^{p}, all of them cross the right face within **Δx/v_{d}^{p}** seconds.
2. Hole flux = (number) / (time) / (area) = pAΔx / (Δx/v_{d}^{p}) / A = **p v_{d}^{p}**.
3. Electrons move the other way: electron flux = **−n v_{d}^{n}** (v_{d}^{n} is the electron speed).
4. Current = charge × flux: J = (+q)(p v_{d}^{p}) + (−q)(−n v_{d}^{n}) = **q(p v_{d}^{p} + n v_{d}^{n})**.
5. Low field: v_{d}^{p} = μ_{p}E, v_{d}^{n} = μ_{n}E. So

$$J_{drift} = q(pμ_{p} + nμ_{n})E = σE$$

- Line 4 is the key: electrons move **against** E, but they carry **negative** charge, so their **current** points **along** E. The two currents **add**.
- **Units** (deck slide 50): C × cm^{2}/V·s × 1/cm^{3} × V/cm = A/cm^{2}. ✓
- J = σE is **Ohm's law** written per cm^{2}: σ is the conductivity.

:::check Check 5
(a) Electrons and holes move in opposite directions. Why do their currents not cancel? (b) n = 10^{16} cm^{−3}, μ_{n} = 1350, E = 10 V/cm, holes negligible. Find J. (c) What are the units of σ?
:::

### 6 · Conductivity and resistivity of pure silicon

:::q <span class="tag">Deck slide 51</span>
(a) Calculate the conductivity and resistivity of intrinsic silicon at T = 300 K. (b) How would σ change if the temperature increased by 10 °C? Given: μ_{n} = 1500, μ_{p} = 450 cm^{2}/V·s for undoped silicon.
:::

:::guess Guess first
Is pure silicon closer to a copper wire (ρ ≈ 2 × 10^{−6} Ω·cm) or to glass (ρ ≈ 10^{12} Ω·cm)?
:::

:::note Terms
**Conductivity σ = q(nμ_{n} + pμ_{p}):** how much current density one V/cm drives; in (Ω·cm)^{−1}. Set by **how many** carriers (n, p) times **how mobile** (μ). **Resistivity ρ = 1/σ:** in Ω·cm; the material's resistance, independent of the shape.
:::

[[fig:ni_T_sigma|What this graph plots: for each temperature (horizontal, °C) the intrinsic carrier count n_{i} (vertical, log scale), from the table on deck slide 51. A point = "pure Si this hot has this many electrons per cm^{3}".|w=60]]

**Answer.** (a) Intrinsic: n = p = n_{i} ≈ 10^{10} cm^{−3} (deck's value).
σ = q n_{i}(μ_{n} + μ_{p}) = 1.6 × 10^{−19} × 10^{10} × (1500 + 450) = **3.12 × 10^{−6} (Ω·cm)^{−1}**.
ρ = 1/σ = **3.2 × 10^{5} Ω·cm**: about a third of a megohm for a 1 cm cube.

(b) n_{i} roughly **doubles** for every 10 °C near room temperature (01a step 5; the table: 8.1 × 10^{9} → 1.7 × 10^{10} from 25 to 35 °C). μ changes only a few per cent over 10 °C. So σ **doubles**.

- So pure silicon sits between metal and glass, and its σ is set almost entirely by n_{i}(T). The fall of μ with heat (step 4) is far smaller than the rise of n_{i}.

:::check Check 6
(a) Redo (a) with n_{i} = 1.5 × 10^{10} cm^{−3}. (b) From the table, by what factor does σ grow from 25 °C to 45 °C? (c) μ falls with temperature, yet σ of pure Si rises. Why?
:::

### 7 · Doping sets σ: one term is enough

:::q <span class="tag">Deck slide 52</span>
Compare (a) silicon with N_{D} = 5 × 10^{17} cm^{−3}, T = 300 K: σ = 32 (Ω·cm)^{−1}; (b) intrinsic silicon, T = 300 K: σ = 3.12 × 10^{−6} (Ω·cm)^{−1}.
:::

:::guess Guess first
How many silicon atoms per donor is 5 × 10^{17} donors in 5 × 10^{22} atoms? And how many times does σ grow?
:::

[[fig:sigma_doping|What this graph plots: for each doping (horizontal, log scale) the conductivity it gives (vertical, log scale). Dotted: pure Si. A point on a curve = "Si doped this much conducts this well". Built from σ = qNμ with μ(N) of step 4.|w=72]]

**Answer.** n ≈ N_{D} = 5 × 10^{17}; p = n_{i}^{2}/n = 10^{20}/(5 × 10^{17}) = **200 cm^{−3}**. The hole term pμ_{p} is 10^{−16} of the electron term: drop it: **σ ≈ qN_{D}μ_{n}.**

- Slide 52's σ = 32 means μ_{n} = 32/(1.6 × 10^{−19} × 5 × 10^{17}) = **400 cm^{2}/V·s**, not 1500: the heavy doping lowered μ (step 4's table gives 420). With 1500 you would get 120.
- One donor per 5 × 10^{22}/5 × 10^{17} = **10^{5} atoms** raises σ by 32/3.12 × 10^{−6} = **10^{7} times**.

- For doped material: **n-type σ ≈ qN_{D}μ_{n}; p-type σ ≈ qN_{A}μ_{p}.** Use μ at that doping.

:::check Check 7
(a) p-type Si, N_{A} = 10^{16}, μ_{p} = 420. Find σ and ρ. (b) Why can the minority term be dropped? (c) n-type, N_{D} = 10^{16}, μ_{n} = 1230. Find ρ.
:::

### 8 · Resistance of a bar: R = ρL/A

ρ belongs to the material. A real resistor also has a shape.

:::q <span class="tag">practice</span>
An n-type Si bar has ρ = 0.5 Ω·cm, length 1 mm, and a 100 μm × 100 μm cross-section. Find R and the current at 5 V.
:::

:::guess Guess first
Longer bar: more or less resistance? Fatter bar?
:::

[[fig:bar_resistor|A doped bar used as a resistor. Current flows along L; it squeezes through the cross-section A = W × t.|w=70]]

- **R = ρL/A.** Longer → more resistance (more scattering on the way). Bigger A → less (more paths side by side).
- Convert everything to cm: ρ is in Ω·cm.

**Answer.** L = 0.1 cm, A = 0.01 × 0.01 = 10^{−4} cm^{2}.
R = 0.5 × 0.1 / 10^{−4} = **500 Ω**; I = 5/500 = **10 mA**.

**Same answer from step 5** (independent route): E = 5 V/0.1 cm = 50 V/cm; σ = 1/ρ = 2 (Ω·cm)^{−1}; J = σE = 100 A/cm^{2}; I = J × A = 100 × 10^{−4} = **10 mA**. ✓

:::check Check 8
(a) Double the length: new R? (b) Halve both W and t: new R? (c) J in the original bar at 5 V?
:::

### 9 · Sheet resistance: counting squares

In an IC a resistor is a thin doped layer at the chip surface. The depth t is fixed by the process; the designer only draws the top view: L and W.

:::q <span class="tag">practice</span>
A doped layer is 1 μm thick with ρ = 0.01 Ω·cm. Find its sheet resistance. A resistor in this layer is 200 μm long and 10 μm wide. Find R.
:::

:::guess Guess first
A 10 μm × 10 μm square and a 100 μm × 100 μm square of the same layer: which has more resistance end to end?
:::

:::note Terms
**Sheet resistance R_{s} = ρ/t:** the resistance of one square of the layer, of any size; units Ω, said "ohms per square" (Ω/□). **Number of squares L/W:** how many such squares fit end to end along the resistor.
:::

[[fig:sheet_squares|Left: two squares of one layer have the same resistance: the bigger one is longer (more R) and wider (less R) by the same factor. Right: a resistor's top view cut into L/W squares in series.|w=88]]

- Rewrite step 8 with A = W × t:

$$R = \frac{ρL}{Wt} = \frac{ρ}{t} × \frac{L}{W} = R_{s} × (number of squares)$$

- Only the shape ratio L/W matters, so the designer just counts squares.

**Answer.** R_{s} = 0.01 / (1 × 10^{−4} cm) = **100 Ω/□**. L/W = 200/10 = 20 squares. R = 20 × 100 = **2 kΩ**.

:::check Check 9
(a) The ρ = 0.5 Ω·cm material of step 8, as a 1 μm layer: R_{s}? (b) R_{s} = 200 Ω/□, W = 5 μm. How long must the resistor be for 10 kΩ? (c) Answer the Guess-first question.
:::

---

## Exam form

**Drift (deck slides 46–48).** Random thermal motion gives no net displacement. A field adds a drift velocity v_{d} = μE: holes along E, electrons against. μ = qτ/m\*, units cm^{2}/V·s. At high field v_{d} saturates at v_{sat} ≈ 10^{7} cm/s (Si). μ falls with doping (impurity scattering) and with temperature (lattice scattering, ∝ T^{−3/2}).

**Drift current (deck slides 49–50).**

1. Holes in a slice: pAΔx; crossing time Δx/v_{d}^{p}; hole flux F_{p} = pv_{d}^{p}; electron flux F_{n} = −nv_{d}^{n}.
2. J = (+q)F_{p} + (−q)F_{n} = q(pv_{d}^{p} + nv_{d}^{n}).
3. v_{d} = μE → **J = q(pμ_{p} + nμ_{n})E = σE**.

**Formulas.** σ = q(nμ_{n} + pμ_{p}); ρ = 1/σ; intrinsic σ = qn_{i}(μ_{n} + μ_{p}); n-type σ ≈ qN_{D}μ_{n}; p-type σ ≈ qN_{A}μ_{p}. R = ρL/A. R_{s} = ρ/t (Ω/□); R = R_{s} × L/W.

**Temperature.** Intrinsic σ roughly doubles per 10 °C (n_{i} doubles; μ barely changes).

## Traps

- Dropping one carrier in **intrinsic** σ: both n_{i}μ_{n} and n_{i}μ_{p} count.
- Thinking electron and hole drift currents cancel: they **add**.
- Using μ = 1500 for heavily doped Si: μ falls with doping (slide 52 needs 400).
- Mixing units: ρ in Ω·cm needs L and A in cm (1 μm = 10^{−4} cm).
- Writing R_{s} in Ω·cm: it is in **Ω** (per square).
- Using v_{d} = μE at fields above a few kV/cm: it saturates.

## Self-test

1. p-type Si, N_{A} = 10^{17}, μ_{p} = 310. Find σ and ρ.
2. Hole drift velocity at 500 V/cm, μ_{p} = 480?
3. R_{s} = 50 Ω/□; a resistor 300 μm long, 6 μm wide. Find R.
4. A bar with ρ = 1.5 Ω·cm, 2 mm long, cross-section 0.5 mm × 0.5 mm. Find R.
5. Derive J = q(pμ_{p} + nμ_{n})E from the slice picture.
6. A 2 μm layer with ρ = 0.02 Ω·cm: R_{s}?
7. Explain in two sentences why μ falls with doping and why it falls with temperature.
8. Why does the conductivity of pure Si rise steeply with temperature?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **Vibrating lattice atoms** and **charged dopant ions**. (b) The directions are random, so the **average displacement is zero**: equal numbers cross each way. (c) τ = 0.4 ps: 10^{7} × 0.4 × 10^{−12} = 4 × 10^{−6} cm = **40 nm**.

**Check 2.** (a) 480 × 100 = **4.8 × 10^{4} cm/s**. (b) μ = 0.135 m^{2}/V·s; τ = μm\*/q = 0.135 × 0.26 × 9.11 × 10^{−31} / 1.6 × 10^{−19} = **2.0 × 10^{−13} s = 0.2 ps**. (c) **Against** E: the force on charge −q is −qE.

**Check 3.** (a) 10^{7}/480 = **2.1 × 10^{4} V/cm**. (b) E = 1 V / 10^{−5} cm = **10^{5} V/cm**, far above 7.4 kV/cm: **saturated**. (c) **No**: v_{d} no longer grows with E, so μ is no longer a constant.

**Check 4.** (a) **780 cm^{2}/V·s**. (b) (400/300)^{−3/2} = **0.65**: μ falls to 65 %. (c) Holes have a **heavier effective mass**, and μ = qτ/m\*.

**Check 5.** (a) Electrons carry **negative** charge moving the opposite way: negative × opposite = same direction of current. (b) J = 1.6 × 10^{−19} × 10^{16} × 1350 × 10 = **21.6 A/cm^{2}**. (c) **(Ω·cm)^{−1}** (also written S/cm).

**Check 6.** (a) σ = 1.6 × 10^{−19} × 1.5 × 10^{10} × 1950 = **4.68 × 10^{−6} (Ω·cm)^{−1}**; ρ = **2.14 × 10^{5} Ω·cm**. (b) n_{i}: 8.1 × 10^{9} → 3.5 × 10^{10}: **4.3 ×**. (c) n_{i} grows **exponentially** with T (doubling per 10 °C); μ falls only slowly (T^{−3/2}). The carrier count wins.

**Check 7.** (a) σ = 1.6 × 10^{−19} × 10^{16} × 420 = **0.672 (Ω·cm)^{−1}**; ρ = **1.49 Ω·cm**. (b) The minority concentration is n_{i}^{2}/N, many orders of magnitude below the majority, so its term is negligible. (c) σ = 1.6 × 10^{−19} × 10^{16} × 1230 = 1.97; ρ = **0.508 Ω·cm**.

**Check 8.** (a) **1000 Ω**. (b) A falls to ¼: **2000 Ω**. (c) J = σE = 2 × 50 = **100 A/cm^{2}**.

**Check 9.** (a) 0.5 / 10^{−4} = **5000 Ω/□**. (b) 10 000/200 = 50 squares; L = 50 × 5 = **250 μm**. (c) **Equal**: both are one square, R = R_{s}.

**Self-test.**

1. σ = 1.6 × 10^{−19} × 10^{17} × 310 = **4.96 (Ω·cm)^{−1}**; ρ = **0.202 Ω·cm**.
2. 480 × 500 = **2.4 × 10^{5} cm/s**.
3. 300/6 = 50 squares; R = **2.5 kΩ**.
4. R = 1.5 × 0.2 / (0.05 × 0.05) = **120 Ω**.
5. Step 5, lines 1–5.
6. 0.02 / (2 × 10^{−4}) = **100 Ω/□**.
7. More dopant ions mean more impurity scattering, so a shorter τ. More heat means more lattice vibration, so more lattice scattering and again a shorter τ; μ = qτ/m\*.
8. σ = qn_{i}(μ_{n} + μ_{p}), and n_{i} ∝ T^{3/2}e^{−E_{g}/2kT} doubles about every 10 °C; the mobility change is small.

<!--/ANSWERS-->
