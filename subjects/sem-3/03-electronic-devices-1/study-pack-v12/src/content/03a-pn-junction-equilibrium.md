# 03a — The pn junction: how it forms and what it holds

<div class="sub">Unit 1–2 deck, slides 66–78 · syllabus Unit 2 (pn junction, depletion region, built-in voltage, Poisson's equation) · needs 01a (doping, n_{i}, mass action), 01b (E_{F}, Boltzmann count), 02b (diffusion, drift–diffusion balance, Poisson) · two deck questions (slides 77, 78); other openers are Predict prompts or practice problems</div>

## Map

[[map:1 The diode > 2 How it is made > 3 Abrupt model > 4 Carriers cross > 5 Bare ions > 6 Field and balance > 7 Band picture > 8 V_bi > 9 Charge ρ(x) > 10 Field E(x) > 11 Potential, width W > 12 Bias|here=1]]

01a–02b dealt with one uniform piece of silicon. A device needs two kinds of silicon side by side. Put p-type next to n-type and three things you already have meet: a **crowd of holes** on one side and a **crowd of electrons** on the other (01a), the urge of a crowd to **spread** (02b, diffusion), and a **field** that pushes back (02a, drift). This file follows them until they settle. 03b then applies a voltage and gets the diode's current.

| Symbol | Meaning in this file | Typical value |
|---|---|---|
| N_{A} | acceptor atoms per cm^{3} on the p side (01a step 7) | 10^{17} |
| N_{D} | donor atoms per cm^{3} on the n side (01a step 6) | 10^{16} |
| n_{i} | electrons per cm^{3} in pure Si (01a step 3) | 10^{10} |
| V_{T} | thermal voltage kT/q, the energy kT in volts (02b step 6) | 25.9 mV at 300 K |
| ε | permittivity of Si (02b step 13) | 1.04 × 10^{−12} F/cm |

These are the **running example's** numbers: every graph in this file is drawn for them.

## The questions this file answers

- <span class="tag">Deck slide 77</span> For an abrupt silicon pn junction, V_{bi} = 0.85 V. W_{0} and W_{1} are the depletion widths for V_{a} = 0 V and V_{a} = 0.6 V. What is W_{1}/W_{0}?
- <span class="tag">Deck slide 78</span> The same junction with V_{a} = −2 V (a reverse bias of 2 V). What is W_{1}/W_{0}?
- <span class="tag">practice</span> For N_{A} = 10^{17}, N_{D} = 10^{16} cm^{−3}: V_{bi}, x_{n}, x_{p}, W and the peak field.

---

## Build

### 1 · The diode: p-type next to n-type

:::guess Predict
A piece of silicon is p-type on its left half and n-type on its right half. You connect a battery one way, then the other way. Will the current be the same both ways?
:::

:::note Terms
**pn junction:** the boundary where p-type silicon meets n-type silicon inside one crystal. **Diode:** a device made of one pn junction with a metal contact on each end. **Anode / cathode:** the p-side terminal / the n-side terminal.
:::

[[fig:diode_symbol|Left: a diode is one piece of silicon, p-type on one side and n-type on the other, with a metal contact at each end (deck slide 66). Right: its circuit symbol. The triangle points from anode to cathode, the direction current flows easily.|w=90]]

- The junction is **not** two pieces glued together. It is one crystal whose doping changes from acceptors to donors (step 2).
- A diode lets current through in one direction only: **from anode to cathode**. The other way it blocks. This is called **rectifying** (deck slide 75).
- Uses (deck slide 66): on its own as a diode; as a building block of every transistor (07–12); and to isolate devices from each other on a chip.

**Answer to the Predict.** No. One direction gives a large current, the other almost none. Steps 4–12 find out why.

:::check Check 1
(a) Which terminal of a diode is the anode, and which side of the junction is it on? (b) In the symbol, which way does the triangle point? (c) Is a pn junction two crystals pressed together?
:::

### 2 · How a junction is made

The deck shows the steps before the physics (slides 67–69). Each step only adds or removes material from one region.

:::guess Predict
You want boron (an acceptor) in one small patch of an n-type wafer and nowhere else. How could you keep it out of the rest of the surface?
:::

:::note Terms
**Epitaxial (epi) layer:** a thin, lightly doped layer of crystal grown on top of the wafer. **Oxide (SiO_{2}):** glass grown on the silicon; boron cannot get through it. **Photoresist and mask:** a light-sensitive coating; UV light through a patterned plate (the mask) marks where the oxide will be removed.
:::

[[fig:fab_steps|The six fabrication steps of deck slides 67–69, side view. ① heavily doped n⁺ wafer with a lightly doped n layer on top; ② oxide over everything; ③ photoresist, mask, UV light; ④ the exposed patch of oxide is etched away (in HF acid), leaving a window; ⑤ boron gas (BH₃) diffuses in through the window only and makes a p region; ⑥ metal contacts on top and bottom.|w=96]]

- The **oxide** is the stencil: boron enters only where the window is.
- The boron diffuses in from the surface, so its concentration fades with depth. Step 3 replaces this gradual profile with a sharp step.
- The **n⁺** wafer underneath (very heavily doped) is a good conductor that carries current to the bottom contact.

**Answer to the Predict.** Cover the surface with oxide, open a window only where you want the p region, and diffuse boron through the window.

:::check Check 2
(a) What does the oxide do during the boron step? (b) Which step decides the size of the p region? (c) Why is the bottom layer n⁺ and not lightly doped?
:::

### 3 · The abrupt-junction model

Real boron fades out with depth (step 2). To calculate anything, the deck replaces the real profile with a simpler one (slide 70).

:::guess Predict
Which is easier to calculate with: doping that changes smoothly over 0.1 μm, or doping that jumps at one point?
:::

:::note Terms
**Abrupt (step) junction:** doping N_{A} everywhere left of a plane and N_{D} everywhere right of it. **Junction plane x = 0 (deck: x_{j}):** where the doping switches. **One-sided junction:** one side much more heavily doped than the other, written p⁺n or n⁺p.
:::

[[fig:abrupt_profile|What these graphs plot: for each position x (horizontal, μm from the junction) the number of dopant atoms per cm^{3} (vertical, log scale). Red = acceptors, blue = donors. Left: what diffusion really gives. Right: the abrupt model used from here on (deck slide 70), drawn for the running example.|w=92]]

- **Left of x = 0:** p-type, N_{A} = 10^{17} acceptors per cm^{3}. **Right:** n-type, N_{D} = 10^{16} donors per cm^{3}.
- Far from the junction each side is just the uniform material of 01a: p ≈ N_{A} on the p side, n ≈ N_{D} on the n side.
- The model gives formulas you can use by hand; the real profile only changes the numbers a little.

**Answer to the Predict.** The jump. With a step, each side has one constant doping, so each side can be solved on its own and the two answers joined at x = 0.

:::check Check 3
(a) In the running example, which side is more heavily doped, and by what factor? (b) What do "p⁺n" and the ⁺ mean? (c) Far from the junction on the n side, about how many electrons per cm^{3} are there?
:::

### 4 · At contact, carriers cross

Now let the two sides meet. Use 01a's mass-action law (n·p = n_{i}^{2}) to count both carriers on each side first.

:::q <span class="tag">practice</span>
Before any carriers move: how many holes and how many electrons per cm^{3} are on each side of the running junction? By what factor do the hole counts on the two sides differ?
:::

:::guess Guess first
Holes are packed on one side and scarce on the other. Which way will they move, and what makes them move? (02b step 1)
:::

:::note Terms
**Majority carrier:** the carrier the doping provides (holes in p, electrons in n). **Minority carrier:** the other one, made only by heat (01a step 8).
:::

[[fig:carrier_profile|What this graph plots: for each position x (horizontal, μm; p side left, n side right) the number of holes (red) and electrons (blue) per cm^{3} (vertical, log scale), once things have settled. A point = "at this place there are this many carriers per cm^{3}". Dotted: the sharp step each side would have if carriers could not cross. Shaded: the strip where both counts collapse (step 5).|w=74]]

| Side | Majority | Minority = n_{i}^{2}/majority |
|---|---|---|
| p side (N_{A} = 10^{17}) | holes p = **10^{17}** | electrons n = 10^{20}/10^{17} = **10^{3}** |
| n side (N_{D} = 10^{16}) | electrons n = **10^{16}** | holes p = 10^{20}/10^{16} = **10^{4}** |

- Holes: 10^{17} on the left, 10^{4} on the right. A steep slope in a crowd means **diffusion** (02b steps 1–2): holes flow **p → n**.
- Electrons: 10^{16} on the right, 10^{3} on the left: electrons diffuse **n → p**.
- A hole that crosses lands among many electrons and soon **recombines** (02b step 7); so does an electron that crosses.

**Answer.** p side: 10^{17} holes, 10^{3} electrons. n side: 10^{16} electrons, 10^{4} holes. The hole counts differ by 10^{17}/10^{4} = **10^{13}**; so do the electron counts (10^{16}/10^{3}). That huge ratio drives the diffusion, and step 8 turns it into a voltage.

:::check Check 4
(a) Redo the table for N_{A} = 10^{16}, N_{D} = 10^{18}. (b) In which direction do electrons diffuse, and why? (c) What happens to a hole after it crosses into the n side?
:::

### 5 · The bare ions: the depletion region

:::guess Predict
A hole leaves the p side. The acceptor atom it came from stays fixed in the crystal. Is that region now neutral, positive or negative?
:::

:::note Terms
**Ion:** a dopant atom whose carrier has left: an acceptor ion is −, a donor ion is + (01a steps 6–7). Ions are part of the crystal and cannot move. **Depletion region (space-charge region):** the strip around the junction emptied of mobile carriers, holding only fixed ions. **Depletion approximation:** treat that strip as having **no** carriers at all and sharp edges; outside it, everything is neutral (deck slide 72).
:::

[[fig:depletion_ions|① At the moment of contact holes (○) cross to the right and electrons (●) to the left. ② Near the junction they are gone: the p side is left with fixed − acceptor ions, the n side with fixed + donor ions. That strip is the depletion region.|w=94]]

- Before contact each side was neutral: on the p side, each − acceptor ion had its + hole beside it.
- Holes leave the p side near the junction → the **− acceptor ions** there are uncovered. Electrons leave the n side → the **+ donor ions** are uncovered.
- So the depletion region has **negative charge on its p side and positive charge on its n side**. That is why the deck also calls it the **space-charge region** (slide 72).
- Outside the strip, carriers still match the ions: those **neutral regions** carry no charge.

**Answer to the Predict.** Negative. The acceptor ion keeps its extra electron and lost the hole that balanced it.

:::check Check 5
(a) What charge is left on the n side of the depletion region, and from which atoms? (b) Why can the ions not move away too? (c) State the depletion approximation in one line.
:::

### 6 · The built-in field stops the crossing

The uncovered charges of step 5 make a field, and a field pushes carriers (02a). This is what stops the crossing.

:::guess Predict
The n side holds + ions, the p side − ions. Which way does the field between them point? Which way does it push a hole?
:::

:::note Terms
**Built-in field:** the field set up by the ions of the depletion region, with no battery connected. **Equilibrium:** nothing connected and nothing changing; every current is zero (02b step 5).
:::

[[fig:balance_arrows|The four flows across the depletion region (deck slide 74). Solid arrows: diffusion, set by the crowding. Dashed arrows: drift, set by the field. Red = holes, blue = electrons. The purple arrow is the field.|w=80]]

- A field points from + charge to − charge: here **from the n side to the p side**.
- **Holes** drift along E: **n → p**, opposite to their diffusion (p → n).
- **Electrons** drift against E: **p → n**, opposite to their diffusion (n → p).
- Crossing continues, more ions are bared, the field grows, until for **each** carrier drift exactly cancels diffusion (deck slide 74):

$$J_{n}^{diff} = −J_{n}^{drift}      J_{p}^{diff} = −J_{p}^{drift}$$

- Both currents are **still flowing**; they just cancel. This is 02b step 5's balance, now at a junction.

**Answer to the Predict.** From n to p. It pushes holes from n back toward p, against their diffusion.

:::check Check 6
(a) Which way do electrons drift in the built-in field? (b) In equilibrium is the hole diffusion current zero? (c) Why does the crossing stop instead of continuing until both sides are mixed?
:::

### 7 · The band picture: one flat Fermi level

01b step 10 put E_{F} near E_{V} in p-type silicon and near E_{C} in n-type. Now both are in one crystal.

:::guess Predict
In equilibrium the Fermi level is the same everywhere (01b: E_{F} is a single level for the whole system). On the p side it sits near E_{V}, on the n side near E_{C}. What must the bands do?
:::

:::note Terms
**Band bending:** E_{C} and E_{V} shifting up or down with position because of a voltage there. An electron's energy changes by −q × (change in potential). **Barrier:** the energy step an electron must climb to go from n side to p side.
:::

[[fig:band_bending|What this graph plots: for each position x (horizontal, μm) the electron energy of the band edges E_{C}, E_{V} and of E_{F} (vertical, eV, with E_{F} = 0), for the running example (deck slides 71, 73). A point on E_{C} = "an electron at the bottom of the conduction band here has this energy".|w=74]]

- E_{F} is drawn **flat**: nothing flows, so the Fermi level is one value everywhere (deck slide 71).
- Far on the p side E_{F} is just above E_{V}; far on the n side it is just below E_{C}. To keep E_{F} flat the **bands on the p side sit higher**.
- The difference in height is **qV_{bi}**: the built-in voltage V_{bi} times the electron charge.
- For an electron on the n side, this is a hill: only those with enough energy can climb to the p side (03b step 2 uses this).

**Answer to the Predict.** They bend: E_{C} and E_{V} rise from the n side to the p side by the same amount, qV_{bi}, so that one flat E_{F} fits both sides.

:::check Check 7
(a) Which side's bands sit higher? (b) In which region do the bands bend, and why there? (c) Why is E_{F} flat in equilibrium?
:::

### 8 · The built-in voltage V_{bi}

Now combine three things you already have: the hole count on each side (step 4), the Boltzmann count (01b step 6), and the voltage step of step 7.

:::q <span class="tag">practice · deck slide 73</span>
Find V_{bi} for the running junction: N_{A} = 10^{17}, N_{D} = 10^{16} cm^{−3}, n_{i} = 10^{10} cm^{−3}, V_{T} = 25.9 mV.
:::

:::guess Guess first
More doping makes the crowds bigger. Does V_{bi} grow or shrink with doping?
:::

:::note Terms
**Built-in voltage V_{bi}:** the voltage across the depletion region in equilibrium, n side higher. Also called the contact potential or barrier voltage. **Thermal voltage V_{T} = kT/q:** k is Boltzmann's constant (1.38 × 10^{−23} J/K), T the temperature in kelvin, q = 1.6 × 10^{−19} C. V_{T} = 25.9 mV at 300 K.
:::

[[fig:vbi_ladder|What these graphs plot: top, the hole count per cm^{3} at each position (log scale); bottom, the potential ψ at each position (volts, p side taken as 0). The hole count falls by 10^{13} across the same strip where the potential rises by V_{bi} (deck slide 73).|w=72]]

**The pieces** (each line follows from the one before):

1. Holes on the p side: p_{p} = N_{A}. Holes on the n side: p_{n} = n_{i}^{2}/N_{D} (step 4).
2. Boltzmann (01b step 6): the number of holes at a place falls by **e^{−1}** for every V_{T} of potential they would have to climb. Across the junction they climb V_{bi}, so p_{n} = p_{p}·e^{−V_{bi}/V_{T}}.
3. Rearrange: e^{V_{bi}/V_{T}} = p_{p}/p_{n} = N_{A}N_{D}/n_{i}^{2}. Take the log:

$$V_{bi} = V_{T} ln\frac{N_{A}N_{D}}{n_{i}^{2}}$$

- **N_{A}, N_{D}** inside the log: more doping → bigger ratio → larger V_{bi}, but only logarithmically.
- **n_{i}^{2}** below: a wider-gap material (smaller n_{i}) gives a larger V_{bi}. Si: 0.6–0.9 V.

**Answer.** N_{A}N_{D}/n_{i}^{2} = 10^{33}/10^{20} = 10^{13}; ln(10^{13}) = 29.93. V_{bi} = 0.0259 × 29.93 = **0.775 V**.

:::note Why a voltmeter reads 0 V across a diode
The diode's metal contacts also have built-in voltages. Around the closed loop they cancel V_{bi} exactly (deck slide 76, equation (1)). V_{bi} does no work, so no meter can read it.
:::

:::check Check 8
(a) V_{bi} for N_{A} = 10^{18}, N_{D} = 10^{16}? (b) Both dopings are raised 10 times. By how much does V_{bi} rise? (c) Why can't you measure V_{bi} with a voltmeter?
:::

### 9 · The charge in the depletion region: ρ(x)

Steps 9–11 find how wide the depletion region is. They follow 02b step 13's chain: charge → field → potential.

:::guess Predict
The p side is 10 times more heavily doped than the n side. The two sides of the depletion region hold equal and opposite charge. Which side's part of the strip is wider?
:::

:::note Terms
**Charge density ρ(x):** net charge per cm^{3} at position x (02b step 13). **x_{p}, x_{n}:** how far the depletion region reaches into the p side and into the n side. **W = x_{p} + x_{n}:** the total width.
:::

[[fig:rho_plot|What this graph plots: for each position x (horizontal, μm) the net charge per cm^{3}, divided by q (vertical, in units of 10^{16}). Drawn to scale for the running example: −10^{17} over a thin strip on the p side, +10^{16} over a strip ten times wider on the n side (deck slide 73).|w=74]]

- Under the depletion approximation (step 5): **ρ = −qN_{A}** from −x_{p} to 0 (bare acceptors), **ρ = +qN_{D}** from 0 to x_{n} (bare donors), **ρ = 0** outside.
- The whole crystal stays neutral, so the − charge equals the + charge. For a cross-section of area A: qN_{A}x_{p}A = qN_{D}x_{n}A, so

$$N_{A}x_{p} = N_{D}x_{n}$$

- In words: the two shaded areas are equal. The **lightly doped side** needs a **wider** strip to bare the same charge.

**Answer to the Predict.** The n side (the lightly doped one). With N_{A} = 10 N_{D}, x_{n} = 10 x_{p}.

:::check Check 9
(a) N_{A} = 10^{18}, N_{D} = 10^{15}. Find x_{n}/x_{p}. (b) Why is ρ zero outside the depletion region? (c) For a p⁺n junction, where is almost all of W?
:::

### 10 · The field E(x): a triangle

:::guess Predict
02b step 13: the slope of E equals ρ/ε. On the p side ρ is a large negative constant; on the n side a small positive constant. What shape is E(x)?
:::

:::note Terms
**Peak field E_{max}:** the largest field strength, at the junction plane x = 0. **Slope of E = ρ/ε:** the rule from 02b step 13 (Poisson's equation).
:::

[[fig:field_plot|What this graph plots: for each position x (horizontal, μm) the electric field (vertical, kV/cm) for the running example. Negative = pointing to −x, from n to p. Zero outside the depletion region (deck slide 73).|w=74]]

- Start at −x_{p} with E = 0 (neutral region). Slope = −qN_{A}/ε: E falls in a **straight line** to its most negative value at x = 0.
- From 0 to x_{n} the slope is +qN_{D}/ε: E rises in a straight line back to **0** at x_{n}.
- So E(x) is a **triangle**; its tip is

$$|E_{max}| = \frac{qN_{D}x_{n}}{ε} = \frac{qN_{A}x_{p}}{ε}$$

- The two forms are equal because N_{A}x_{p} = N_{D}x_{n} (step 9).

**Answer to the Predict.** A triangle: zero at both edges, sloping straight down on the p side (steep) and straight back up on the n side (gentle), peak at the junction. For the running example (x_{n} from step 11): |E_{max}| = 1.6 × 10^{−19} × 10^{16} × 3.03 × 10^{−5} / 1.04 × 10^{−12} = **4.66 × 10^{4} V/cm**.

:::check Check 10
(a) Why is the p-side slope steeper? (b) Where is the field largest? (c) Find |E_{max}| from the p-side form, with x_{p} = 3.03 × 10^{−6} cm.
:::

### 11 · The potential, and the width W

Now combine steps 8, 9 and 10. The potential across the strip must add up to V_{bi}.

:::q <span class="tag">practice</span>
For the running junction (V_{bi} = 0.775 V) find W, x_{n} and x_{p}.
:::

:::guess Guess first
Is W closer to 1 nm, 0.3 μm or 1 mm?
:::

:::note Terms
**Potential ψ(x):** the voltage at position x, with the p side taken as 0. Its slope is −E (02b step 13), so the **area under the E(x) triangle is the total voltage** across it.
:::

[[fig:potential_plot|What this graph plots: for each position x (horizontal, μm) the potential ψ (vertical, volts), for the running example. Two joined parabolas; the total rise is V_{bi} (deck slide 73).|w=74]]

**Combining** (each line follows from the one before):

1. Area of the field triangle = ½ × base × height: **V_{bi} = ½|E_{max}|W** (step 10's triangle, base W).
2. Put in |E_{max}| = qN_{D}x_{n}/ε and x_{n} = W·N_{A}/(N_{A} + N_{D}) (from step 9).
3. Solve for W:

$$W = \sqrt{\frac{2ε}{q} (\frac{1}{N_{A}} + \frac{1}{N_{D}}) V_{bi}}$$

| Symbol | What it is | Its effect on W |
|---|---|---|
| ε | permittivity: a weaker-shielding material needs more width | W ∝ √ε |
| 1/N_{A} + 1/N_{D} | the lighter doping dominates the sum | lighter doping → wider |
| V_{bi} | the voltage the strip must hold | W ∝ √V_{bi} |

**Answer.** 2ε/q = 2 × 1.04 × 10^{−12}/1.6 × 10^{−19} = 1.30 × 10^{7}. (1/10^{17} + 1/10^{16}) = 1.1 × 10^{−16}. W = √(1.30 × 10^{7} × 1.1 × 10^{−16} × 0.775) = 3.33 × 10^{−5} cm = **0.333 μm**. x_{n} = W × 10/11 = **0.303 μm**; x_{p} = W × 1/11 = **0.030 μm**.

**Check by a second route:** ½ × 4.66 × 10^{4} × 3.33 × 10^{−5} = 0.776 V ≈ V_{bi}. ✓

:::check Check 11
(a) N_{A} = N_{D} = 10^{16} (V_{bi} = 0.716 V). Find W. (b) For a p⁺n junction (N_{A} ≫ N_{D}), simplify the W formula. (c) What share of V_{bi} is dropped on the n side in the running example? (Hint: x_{n}/W.)
:::

### 12 · Applying a voltage: V_{j} = V_{bi} − V_{a}

A battery V_{a} is connected, + to the p side for **forward bias**, + to the n side for **reverse bias** (V_{a} negative).

:::q <span class="tag">Deck slides 77–78</span>
For an abrupt silicon pn junction, V_{bi} = 0.85 V. Let W_{0} and W_{1} denote the depletion widths for V_{a} = 0 V and V_{a} = 0.6 V. What is W_{1}/W_{0}? Repeat for V_{a} = −2 V (a reverse bias of 2 V).
:::

:::guess Guess first
Forward bias: does the depletion region get wider or narrower?
:::

:::note Terms
**Applied voltage V_{a}:** the battery voltage, p side minus n side. **Junction voltage V_{j}:** the voltage across the depletion region alone (deck slide 76).
:::

[[fig:voltage_drops|Where the applied voltage goes (deck slide 76). The contacts and neutral regions conduct well, so almost none of V_{a} is lost there; it all appears across the depletion region.|w=92]]

- In equilibrium the junction holds V_{bi}. Forward bias **opposes** the built-in voltage (deck slide 76):

$$V_{j} = V_{bi} − V_{a}$$

- **Forward** (V_{a} > 0): smaller barrier, **narrower** W. Majority carriers can climb it: large current (03b).
- **Reverse** (V_{a} < 0): bigger barrier V_{bi} + |V_{a}|, **wider** W. Almost no current.
- Step 11's formula with V_{bi} replaced by V_{bi} − V_{a} gives W ∝ √(V_{bi} − V_{a}). The ratio method of the deck: V_{j} = kW^{2}, so W_{1}/W_{0} = √(V_{j1}/V_{j0}).

[[fig:bias_W|The depletion strip for the deck's junction (V_{bi} = 0.85 V) at three biases, drawn to scale relative to W_{0}.|w=86]]

**Answer.** Forward 0.6 V: W_{1}/W_{0} = √((0.85 − 0.6)/0.85) = √0.294 = **0.54**: the region **shrinks**. Reverse 2 V: √((0.85 + 2)/0.85) = √3.35 = **1.83**: it **expands**.

Running example: +0.5 V gives W = 0.198 μm; −5 V gives 0.909 μm (2.73 × W_{0}).

:::check Check 12
(a) V_{bi} = 0.7 V, forward 0.4 V: W_{1}/W_{0}? (b) Same junction: what reverse bias makes W 3.16 times W_{0}? (c) Why does almost all of V_{a} appear across the depletion region and not the neutral regions?
:::

---

## Exam form

**Junction formation** (deck slides 70–74). Abrupt junction: N_{A} for x < 0, N_{D} for x > 0. At contact, holes diffuse p → n and electrons n → p and recombine. Fixed ions are left: − acceptors on the p side, + donors on the n side: the **depletion (space-charge) region**. Their field points **n → p**. Equilibrium: for each carrier, drift = −diffusion; E_{F} flat; bands bend by qV_{bi}.

**Sketch** (deck slide 73): ρ(x) two rectangles (−qN_{A}, +qN_{D}, equal areas); E(x) a triangle with its peak at x = 0; ψ(x) two parabolas rising by V_{bi}.

**V_{bi} derivation.**

1. p_{p} = N_{A}, p_{n} = n_{i}^{2}/N_{D}.
2. Boltzmann: p_{n} = p_{p}e^{−V_{bi}/V_{T}}.
3. **V_{bi} = V_{T}ln(N_{A}N_{D}/n_{i}^{2})**.

**Width.** N_{A}x_{p} = N_{D}x_{n}; |E_{max}| = qN_{D}x_{n}/ε; V_{bi} = ½|E_{max}|W;
**W = √[(2ε/q)(1/N_{A} + 1/N_{D})(V_{bi} − V_{a})]**; x_{n} = W·N_{A}/(N_{A} + N_{D}).

**Bias.** V_{j} = V_{bi} − V_{a}; W ∝ √(V_{bi} − V_{a}); W_{1}/W_{0} = √[(V_{bi} − V_{a1})/(V_{bi} − V_{a0})].

## Traps

- W ∝ √(V_{bi} − V_{a}), not √V_{a}: forgetting V_{bi} gives W = 0 at zero bias.
- Reverse bias is a **negative** V_{a}: V_{bi} − (−2) = V_{bi} + 2.
- The depletion region reaches further into the **lightly** doped side, not the heavy one.
- The built-in field points **n → p** (from + ions to − ions).
- Units: ε in F/cm with N in cm^{−3} gives W in cm; 1 μm = 10^{−4} cm.
- V_{bi} cannot be read by a voltmeter.
- In equilibrium the currents are not zero one by one: each drift cancels a diffusion.

## Self-test

1. V_{bi} for N_{A} = 10^{16}, N_{D} = 10^{17} cm^{−3} (n_{i} = 10^{10}, V_{T} = 25.9 mV).
2. N_{A} = 10^{18}, N_{D} = 10^{15}: find x_{n}/x_{p}. Which side holds the depletion region?
3. N_{A} = N_{D} = 10^{17}: find V_{bi} and W.
4. V_{bi} = 0.8 V. By what factor does W grow at a reverse bias of 7.2 V?
5. Sketch ρ(x), E(x) and ψ(x) for a junction with N_{A} = 4N_{D}, marking x_{p}, x_{n} and V_{bi}.
6. Explain in three sentences why diffusion across a junction stops.
7. Derive V_{bi} = V_{T}ln(N_{A}N_{D}/n_{i}^{2}) from the hole counts.

<!--ANSWERS-->

## Answers

**Check 1.** (a) The anode is the **p-side** terminal. (b) From anode to cathode: the direction of easy current. (c) **No**: one crystal whose doping changes from p to n.

**Check 2.** (a) It **blocks** boron everywhere except the window. (b) The **mask/window** step (③–④). (c) n⁺ conducts well, so little voltage is lost getting current to the bottom contact.

**Check 3.** (a) The **p side**, 10 times (10^{17} vs 10^{16}). (b) p⁺n: the p side is far more heavily doped than the n side; ⁺ means "heavily doped". (c) n ≈ N_{D} = **10^{16}**.

**Check 4.** (a) p side: p = 10^{16}, n = 10^{4}; n side: n = 10^{18}, p = 10^{2}. (b) **n → p**: 10^{18} on the n side against 10^{4} on the p side, and a crowd spreads from where it is dense. (c) It meets many electrons and **recombines**.

**Check 5.** (a) **Positive**: donor ions whose electrons left. (b) They are atoms of the crystal, bonded in place. (c) The depletion region has no mobile carriers and sharp edges; outside it everything is neutral.

**Check 6.** (a) **p → n** (against the field, which points n → p). (b) **No**: it flows, cancelled by an equal hole drift current. (c) Each crossing bares more ions; the field grows until drift cancels diffusion.

**Check 7.** (a) The **p side**. (b) In the **depletion region**: the voltage V_{bi} is dropped there; the neutral regions have no field. (c) No current flows and nothing changes: one Fermi level describes the whole system.

**Check 8.** (a) 0.0259 × ln(10^{34}/10^{20}) = 0.0259 × 32.2 = **0.835 V**. (b) The ratio grows 100 ×: V_{T}ln(100) = **0.119 V** more. (c) The contact voltages at the metal contacts cancel it exactly around the loop.

**Check 9.** (a) x_{n}/x_{p} = N_{A}/N_{D} = **1000**. (b) There the carriers exactly cover the ions. (c) On the lightly doped **n side**.

**Check 10.** (a) The slope is qN/ε, and N_{A} > N_{D} on the p side. (b) At the junction plane **x = 0**. (c) 1.6 × 10^{−19} × 10^{17} × 3.03 × 10^{−6} / 1.04 × 10^{−12} = **4.66 × 10^{4} V/cm**, the same.

**Check 11.** (a) W = √(1.30 × 10^{7} × 2 × 10^{−16} × 0.716) = 4.31 × 10^{−5} cm = **0.431 μm**. (b) 1/N_{A} drops out: **W ≈ √[2εV_{bi}/(qN_{D})]**, all on the n side. (c) x_{n}/W = 10/11 = **91 %**; the p side drops only 9 %. (V on each side = ½E_{max}x, so the shares follow x_{n} and x_{p}.)

**Check 12.** (a) √(0.3/0.7) = **0.655**. (b) Need (0.7 + V_{R})/0.7 = 10 → **V_{R} = 6.3 V**. (c) The neutral regions and contacts are good conductors with almost no resistance; the depletion region has no carriers, so the voltage appears there.

**Self-test.**

1. Same product as the running example: **0.775 V**.
2. **1000**: almost all on the lightly doped **n side**.
3. V_{bi} = 0.0259 × ln(10^{14}) = **0.835 V**; W = √(1.30 × 10^{7} × 2 × 10^{−17} × 0.835) = **0.147 μm**.
4. √((0.8 + 7.2)/0.8) = √10 = **3.16**.
5. ρ: −qN_{A} over x_{p}, +qN_{D} over x_{n} = 4x_{p}; E: triangle, steep on p (4 times), peak at 0; ψ: parabolas rising V_{bi}, 80 % of it on the n side.
6. Holes and electrons diffuse across and leave fixed ions. The ions make a field from n to p that drifts carriers back. The field grows until drift cancels diffusion for each carrier.
7. Step 8, lines 1–3.

<!--/ANSWERS-->
