# 01b — The Fermi level: counting electrons and holes

<div class="sub">Unit 1–2 deck, slides 25–38 · syllabus Unit 1 (energy bands in intrinsic and extrinsic silicon) · needs 01a (bands, E_{C}, E_{V}, E_{g}, n, p, n_{i}, doping) · one deck derivation (slide 38); other openers are Predict prompts</div>

## Map

[[map:1 States = seats > 2 f(E), read point by point > 3 f(E) on the band diagram > 4 Seats per energy g(E) > 5 n = seats × chance > 6 The exponential shortcut > 7 N_{C} and N_{V} > 8 n·p = n_{i}^{2} proved > 9 E_{F} at mid-gap > 10 E_{F} moves with doping|here=1]]

01a counted carriers with rules of thumb: n ≈ N_{D}, p = n_{i}^{2}/n. This file explains where those rules come from, using one idea: **number of carriers = number of places an electron could sit × the chance each place is taken.** The Fermi level E_{F} is the single number that sets that chance. 03 uses it to explain the pn junction.

---

## Build

### 1 · States: the seats electrons sit in

:::guess Predict
A cinema has 500 seats; 80 % are taken. How many people are inside? Now: what two numbers would you need to know how many electrons sit in the conduction band?
:::

:::note Terms
**State:** one allowed place for one electron at one energy, a "seat". At most one electron per state (Pauli exclusion principle). **Occupied / empty:** a seat with or without an electron.
:::

[[fig:seats|The band diagram as rows of seats. Each short line is one state. Dots are electrons. The gap has no seats.|w=82]]

- In the conduction band almost every seat is **empty**; a filled one is a **free electron**.
- In the valence band almost every seat is **filled**; an empty one is a **hole**.
- So, exactly as in the cinema:

$$electrons in a band = (number of seats) × (chance a seat is filled)$$

Steps 2–3 give the chance. Steps 4–7 give the seats.

:::check Check 1
(a) In seat language, what is a hole? (b) Why can no electron be found in the gap?
:::

### 2 · The Fermi–Dirac function f(E), read point by point

:::guess Predict
At 0 K electrons fill the lowest seats first, up to some energy, and nothing above. Sketch "chance a seat is filled" against energy at 0 K. Then guess how heat changes the sketch.
:::

:::note Terms
**f(E):** the probability that a seat at energy E is filled, in thermal equilibrium (deck slide 28). **Fermi level E_{F}:** the energy where that probability is exactly ½ (deck slide 30). **kT:** the size of a typical thermal "kick", 0.0259 eV at 300 K.
:::

[[fig:fermi_read|What this graph plots: pick any seat. Its horizontal position is how far its energy is above E_{F} (left = below). Its height is the chance it holds an electron.|w=74]]

$$f(E) = \frac{1}{1 + e^{(E − E_{F})/kT}}$$

**Read it at four seats (300 K):**

| Seat energy | (E − E_{F})/kT | f(E) | Meaning |
|---|---|---|---|
| exactly E_{F} | 0 | 1/(1 + 1) = **0.5** | half the time filled |
| 1 kT above | 1 | 1/(1 + 2.72) = **0.27** | usually empty |
| 3 kT above (0.078 eV) | 3 | 1/(1 + 20.1) = **0.047** | rarely filled |
| 3 kT below | −3 | 1/(1 + 0.05) = **0.953** | almost always filled |

- **At 0 K** (dashed): a step. Every seat below E_{F} filled, every seat above empty.
- **At 300 K**: heat rounds the step over a width of a few kT. Far below E_{F}: f → 1. Far above: f → 0, falling **exponentially** (deck slide 30).
- E_{F} itself is just a **reference energy**. It does not need a seat at it; in silicon it usually lies inside the gap.

:::check Check 2
(a) f(E_{F}) at 300 K? At 600 K? (b) f for a seat 0.1 eV above E_{F} at 300 K? (c) A seat 0.2 eV **below** E_{F}: what is f, and what is the chance it is **empty**?
:::

### 3 · f(E) placed on the band diagram

The graph in step 2 has energy on the horizontal axis. Turn it so energy points up, and lay it beside the bands: now it shows which seats in each band are filled.

:::guess Predict
In pure silicon E_{F} sits in the middle of the gap, 0.56 eV from each band edge. Is the chance a conduction-band seat is filled large or tiny?
:::

[[fig:fermi_rotated|Left: bands, with E_{F} at mid-gap. Right: the same f(E) with energy vertical. Blue: the part of f inside the conduction band (electrons). Red: the part of 1 − f inside the valence band (holes). kT is drawn 3.5× wider than real so the tails show.|w=86]]

**Reading the figure.**

- **In the gap** f(E) has values, but there are no seats there, so nothing is filled.
- **Conduction band:** only the tail of f reaches it. At E_{C}, 0.56 eV above E_{F}, f = 1/(1 + e^{21.6}) ≈ **4 × 10^{−10}**. Tiny, but there are very many seats, so the electron count is n_{i}.
- **Valence band:** f is almost 1. The chance a seat is **empty** is **1 − f(E)**: the hole probability. By symmetry it is also ≈ 4 × 10^{−10} at E_{V}.

**Answer to the Predict.** Tiny: about 4 in 10 billion. That is why pure silicon has so few carriers.

:::check Check 3
(a) Which function gives the chance a valence-band seat holds a hole? (b) If E_{F} moved up towards E_{C}, which tail grows and which shrinks?
:::

### 4 · How many seats: the density of states g(E)

The chance per seat is known. The other factor is how many seats there are at each energy.

:::guess Predict
Are seats spread evenly up the conduction band, or packed more densely at its bottom edge, or more densely higher up?
:::

:::note Terms
**Density of states g(E):** number of seats per unit energy per cm^{3} at energy E (the deck's N(E), slide 26). **Effective mass m\*:** the mass an electron (or hole) appears to have when moving in the crystal; for Si electrons, 1.08 × the free-electron mass.
:::

[[fig:dos_plot|What this graph plots: at each energy (vertical), how many seats exist there (horizontal). Zero in the gap; growing like a square root into each band.|w=52]]

- At the very band edge there are **no** seats; moving into the band, the count grows as a square root (deck slide 26: N(E) = γE^{1/2}, with E measured from the band edge):

$$g_{c}(E) ∝ √(E − E_{C})      g_{v}(E) ∝ √(E_{V} − E)$$

- The constant in front depends on the effective mass: heavier carriers → more seats.
- So seats get **more numerous** going up into the conduction band, while f(E) gets **smaller**. The electrons end up where both are reasonable: just above E_{C}.

:::check Check 4
(a) What is g(E) inside the gap? (b) In words: what does g(E) = 0 at exactly E = E_{C} mean?
:::

### 5 · Electrons per energy: multiply seats by chance

:::guess Predict
Multiply a curve that rises from zero (seats) by one that falls fast (chance). Sketch the shape of the product.
:::

[[fig:gf_product|① seats g(E); ② chance filled f(E); ③ their product: electrons per energy (blue) and holes per energy (red). The area of each shaded hump is the carrier concentration. kT widened so the humps show.|w=95]]

- **Electrons:** at each energy in the conduction band, electrons there = g_{c}(E) × f(E). Adding up over the whole band (an integral):

$$n = ∫ g_{c}(E) f(E) dE   (over the conduction band)$$

- **Holes:** the same with the chance of being empty:

$$p = ∫ g_{v}(E) [1 − f(E)] dE   (over the valence band)$$

- The humps are narrow: almost all electrons sit within a few kT of E_{C}, almost all holes within a few kT of E_{V}. That is why "the electrons are at E_{C}" is a good picture.

:::check Check 5
(a) Why is the electron hump zero exactly at E_{C}? (b) Why does it die off a few kT above E_{C}?
:::

### 6 · The exponential shortcut (Boltzmann approximation)

The integral in step 5 is awkward because of the "1 +" in f(E). In silicon it can almost always be dropped.

:::guess Predict
For x = 5, compare 1/(1 + e^{x}) with e^{−x}. How close are they?
:::

[[fig:boltz_compare|What this graph plots: the chance a seat is filled (log scale) against how many kT the seat is above E_{F}. Solid: exact f. Dashed: e^{−x}. Shaded: where they agree within 5 %.|w=68]]

- When a seat is more than about **3 kT** above E_{F}, e^{(E − E_{F})/kT} > 20, so the "1 +" barely matters (deck slide 31):

$$f(E) ≈ e^{−(E − E_{F})/kT}      (E − E_{F} ≥ 3kT)$$

- For holes, the chance of being empty, 1 − f, becomes (deck slide 33):

$$1 − f(E) ≈ e^{−(E_{F} − E)/kT}      (E_{F} − E ≥ 3kT)$$

- In silicon E_{F} normally sits in the gap, more than 3 kT (0.078 eV) from both band edges, so both shortcuts hold. Such silicon is called **non-degenerate**. (Very heavy doping, above about 10^{19} cm^{−3}, breaks this; not needed in this course.)

**Answer to the Predict.** x = 5: exact 0.00669, shortcut 0.00674. They differ by under 1 %.

:::check Check 6
(a) At x = 3, the exact f is 0.0474 and the shortcut gives 0.0498. Percentage error? (b) E_{F} is 0.02 eV below E_{C}. Can you use the shortcut? Why?
:::

### 7 · N_{C} and N_{V}: the effective number of seats

With the shortcut, the integral of step 5 can be done once and for all. The result has one new number in it, and this is the step that defines it.

:::guess Predict
Electrons in the conduction band are spread over a few kT above E_{C}. Could you replace the whole band by a single block of seats sitting exactly at E_{C} and still get the right electron count? What would that block's size have to be?
:::

:::note Terms
**N_{C}:** effective density of states of the conduction band: the number of seats per cm^{3} that, **if all placed exactly at E_{C}**, would hold the same number of electrons as the real band. **N_{V}:** the same for the valence band, placed at E_{V}, counting holes.
:::

[[fig:nc_equivalent|Left: the real band. Seats spread upward (dashed) and the filled part (blue) lies within a few kT of E_{C}. Right: the bookkeeping. One block of N_{C} seats placed at E_{C} holds the same number of electrons.|w=85]]

- Doing the integral with the shortcut (deck slide 32) gives:

$$n = N_{C} e^{−(E_{C} − E_{F})/kT}      p = N_{V} e^{−(E_{F} − E_{V})/kT}$$

- **Read each formula as seats × chance.** N_{C} = how many seats count; e^{−(E_{C} − E_{F})/kT} = the chance a seat at E_{C} is filled (step 6). Only the gap between E_{F} and the band edge matters.
- **What sets N_{C}:** the effective mass and temperature: N_{C} = 2(2πm_{n}\*kT/h^{2})^{3/2}, so **N_{C} ∝ T^{3/2}**.

| Si, 300 K | Value | Compare |
|---|---|---|
| N_{C} | **2.8 × 10^{19} cm^{−3}** (m_{n}\* = 1.08 m_{0}) | about 1 seat per 1800 atoms |
| N_{V} | **1.04 × 10^{19} cm^{−3}** (m_{p}\* = 0.56 m_{0}) | some books: 1.8 × 10^{19} |

**Worked use.** E_{F} is 0.25 eV below E_{C} (300 K). n = 2.8 × 10^{19} × e^{−0.25/0.0259} = 2.8 × 10^{19} × 6.45 × 10^{−5} = **1.8 × 10^{15} cm^{−3}**.

:::check Check 7
(a) In one sentence each, without symbols: what is N_{C}, and what is the exponential next to it? (b) E_{F} − E_{V} = 0.20 eV. Find p. (c) By what factor does N_{C} grow from 300 K to 600 K?
:::

### 8 · Multiply n and p: the mass-action law, proved

01a stated n · p = n_{i}^{2} from a rate argument. The two formulas of step 7 prove it directly.

:::guess Predict
Multiply n and p from step 7. Does E_{F} survive in the product?
:::

$$n · p = N_{C}N_{V} e^{−(E_{C} − E_{F})/kT} e^{−(E_{F} − E_{V})/kT} = N_{C}N_{V} e^{−(E_{C} − E_{V})/kT} = N_{C}N_{V} e^{−E_{g}/kT}$$

- **E_{F} cancels.** The product depends only on the material (N_{C}, N_{V}, E_{g}) and T. Doping moves E_{F}, so it changes n and p, but **never their product**.
- Pure silicon has n = p = n_{i}, so that product is n_{i}^{2}:

$$n_{i} = √(N_{C}N_{V}) e^{−E_{g}/2kT}$$

- This is the e^{−E_{g}/2kT} that made n_{i} so temperature-sensitive in 01a step 5.

:::note Deck slide 36
The slide writes the product as N_{V}N_{C}e^{−2E_{F}/kT}. That is a slip: the two exponents use different energies (E_{V} and E_{C}), and they combine to **e^{−E_{g}/kT}**, with no E_{F}. The slide's own conclusion (the product is a constant n_{i}^{2}(T)) needs the corrected form.
:::

:::note Why books disagree on n_{i}
With N_{C} = 2.8 × 10^{19}, N_{V} = 1.04 × 10^{19}, E_{g} = 1.12 eV: n_{i} = 1.71 × 10^{19} × e^{−21.6} ≈ **6.9 × 10^{9}**, not 1.5 × 10^{10}. The effective masses and E_{g} are known only to a few per cent, and n_{i} depends on E_{g} exponentially. Use the n_{i} the question gives.
:::

:::check Check 8
(a) Why can doping not change n · p? (b) Recompute √(N_{C}N_{V}) from the table in step 7.
:::

### 9 · E_{F} in intrinsic silicon lies at mid-gap

:::q <span class="tag">Deck slide 38</span>
Show that the Fermi level in an intrinsic semiconductor lies at the middle of the forbidden gap.
:::

:::guess Guess first
Which condition, true only for pure silicon, do you set up first?
:::

**Answer** (each line follows from the one before):

1. Intrinsic: **n = p**.
2. Substitute step 7: N_{C}e^{−(E_{C} − E_{F})/kT} = N_{V}e^{−(E_{F} − E_{V})/kT}.
3. Approximation: **take N_{C} ≈ N_{V}**. They cancel: e^{−(E_{C} − E_{F})/kT} = e^{−(E_{F} − E_{V})/kT}.
4. Equal exponentials have equal exponents: E_{C} − E_{F} = E_{F} − E_{V}.
5. So 2E_{F} = E_{C} + E_{V}, and

$$E_{F} = E_{i} = \frac{E_{C} + E_{V}}{2}$$

**E_{i}** (the **intrinsic level**) is the name for E_{F} in pure material.

- Without step 3, the same algebra gives E_{i} = (E_{C} + E_{V})/2 + (kT/2) ln(N_{V}/N_{C}). For Si: 0.01295 × ln(1.04/2.8) = **−12.8 meV**, about 1 % of the gap below the middle. "Mid-gap" is accurate to that.

:::note Deck slide 38
The slide labels N_{C} = N_{V} "at equilibrium". Equilibrium does not make them equal: N_{C} = N_{V} is an **approximation** (for Si they differ by about 2.7×). Write "assuming N_{C} ≈ N_{V}" in the exam.
:::

:::check Check 9
(a) Where in the derivation did "intrinsic" enter? (b) If holes were heavier than electrons (N_{V} > N_{C}), would E_{i} sit slightly above or below mid-gap?
:::

### 10 · E_{F} moves with doping

:::q <span class="tag">practice</span>
Si doped with N_{D} = 10^{16} cm^{−3}, n_{i} = 10^{10} cm^{−3}, 300 K. How far above mid-gap is E_{F}? How far below E_{C}?
:::

:::guess Guess first
Up or down from mid-gap, and roughly how much of the 0.56 eV half-gap?
:::

[[fig:ef_positions|Where E_{F} sits. Blue dots: free electrons; red rings: holes. More electrons ↔ E_{F} closer to E_{C}.|w=86]]

- Measuring from E_{i} instead of the band edges, step 7 becomes (divide by the intrinsic case):

$$n = n_{i} e^{(E_{F} − E_{i})/kT}      p = n_{i} e^{(E_{i} − E_{F})/kT}$$

- Each kT that E_{F} rises multiplies n by e (2.72) and divides p by e: n · p stays n_{i}^{2}.
- n-type, n ≈ N_{D}: **E_{F} − E_{i} = kT ln(N_{D}/n_{i})**. p-type, p ≈ N_{A}: **E_{i} − E_{F} = kT ln(N_{A}/n_{i})**.

[[fig:ef_vs_doping|What this graph plots: for each doping level (horizontal, log scale), where E_{F} sits relative to mid-gap (vertical). Blue: donors push E_{F} up. Red: acceptors push it down. Ten times more doping moves E_{F} by only 0.06 eV.|w=72]]

**Answer.** E_{F} − E_{i} = 0.0259 × ln(10^{16}/10^{10}) = 0.0259 × 13.8 = **0.358 eV above mid-gap**. From the band edge directly: E_{C} − E_{F} = kT ln(N_{C}/n) = 0.0259 × ln(2.8 × 10^{19}/10^{16}) = **0.206 eV**. Check: 0.358 + 0.206 = 0.564 eV ≈ half the gap.

**Why this matters next.** In equilibrium E_{F} is **the same everywhere** in a connected piece of material (deck slide 36). Join p-type (E_{F} low) to n-type (E_{F} high) and the bands must bend until the two E_{F} line up. That bending is the pn junction, in 03.

:::check Check 10
(a) p-type, N_{A} = 10^{17}, n_{i} = 10^{10}: how far is E_{F} below mid-gap? (b) An n-type sample has E_{F} 0.3 eV above E_{i}, n_{i} = 1.5 × 10^{10}. Find n. (c) Heat a doped sample until n_{i} becomes larger than N_{D}. Where does E_{F} go?
:::

---

## Exam form

**Fermi–Dirac function.** f(E) = 1/(1 + e^{(E − E_{F})/kT}) is the probability a state at energy E is occupied. f(E_{F}) = ½ at every T. Sketch at 0 K (step) and T > 0 (rounded over a few kT).

**Fermi level.** The energy at which the occupation probability is ½; in equilibrium it is constant throughout the material.

**Carrier concentrations.**

1. n = ∫ g_{c}(E) f(E) dE over the conduction band; p = ∫ g_{v}(E)[1 − f(E)] dE over the valence band; g ∝ √(energy from band edge).
2. Boltzmann approximation (E_{F} more than 3kT from the band edges): f ≈ e^{−(E − E_{F})/kT}.
3. Result: n = N_{C}e^{−(E_{C} − E_{F})/kT}, p = N_{V}e^{−(E_{F} − E_{V})/kT}, with N_{C}, N_{V} the effective densities of states (Si: 2.8 × 10^{19}, 1.04 × 10^{19} cm^{−3}).

**Mass action.** np = N_{C}N_{V}e^{−E_{g}/kT} = n_{i}^{2}, independent of E_{F}; n_{i} = √(N_{C}N_{V})e^{−E_{g}/2kT}.

**E_{F} at mid-gap (deck slide 38).** n = p → N_{C}e^{−(E_{C} − E_{F})/kT} = N_{V}e^{−(E_{F} − E_{V})/kT} → assume N_{C} ≈ N_{V} → E_{C} − E_{F} = E_{F} − E_{V} → E_{F} = (E_{C} + E_{V})/2. Exact: + (kT/2)ln(N_{V}/N_{C}).

**Doped.** n = n_{i}e^{(E_{F} − E_{i})/kT}; n-type E_{F} − E_{i} = kT ln(N_{D}/n_{i}); p-type E_{i} − E_{F} = kT ln(N_{A}/n_{i}). Sketch the three band diagrams.

## Traps

- Saying f(E) is "the number of electrons at E": it is a **probability**. Electrons = seats × probability.
- Saying "N_{C} = N_{V} at equilibrium": it is an **approximation**, not a law.
- Writing np with E_{F} left in the exponent (the slide 36 slip): it **cancels**.
- Using kT in joules with energies in eV: at 300 K use **0.0259 eV**.
- Using the Boltzmann shortcut when E_{F} is within 3kT of a band edge.
- Putting E_{F} for n-type below mid-gap: more electrons ↔ E_{F} **closer to E_{C}**.

## Self-test

1. Sketch f(E) at 0 K and 300 K and mark the value at E_{F}.
2. Probability that a state 0.2 eV **below** E_{F} is empty, at 300 K?
3. Explain in two sentences what N_{C} is, using the words "seats" and "E_{C}".
4. Derive E_{F} = (E_{C} + E_{V})/2 for intrinsic silicon from memory, stating the approximation.
5. Show from the n and p formulas that np does not depend on E_{F}.
6. N_{D} = 10^{15} cm^{−3}, n_{i} = 1.5 × 10^{10}: E_{F} − E_{i}?
7. Si with E_{C} − E_{F} = 0.206 eV: find n and say what N_{D} that corresponds to.
8. Why does a p-type sample's E_{F} move back toward mid-gap when heated strongly?

<!--ANSWERS-->

## Answers

**Check 1.** (a) An **empty seat in the valence band**. (b) The gap has **no seats** (no allowed states).

**Check 2.** (a) **½** at both: e^{0} = 1 for any T. (b) 1/(1 + e^{0.1/0.0259}) = 1/(1 + 47.5) = **0.0206**. (c) f = 1/(1 + e^{−7.72}) = **0.99956**; empty chance 1 − f = **4.4 × 10^{−4}**.

**Check 3.** (a) **1 − f(E)**. (b) The **conduction-band tail grows** (more electrons); the valence-band hole tail shrinks (fewer holes).

**Check 4.** (a) **Zero**: no seats. (b) Exactly at the edge there are **no seats yet**; they start and grow as you go into the band.

**Check 5.** (a) g_{c}(E_{C}) = 0: **no seats** at the edge. (b) f(E) falls by e for every kT; it **outruns** the √ growth of seats.

**Check 6.** (a) (0.0498 − 0.0474)/0.0474 ≈ **5 %**. (b) **No**: 0.02 eV < 3kT = 0.078 eV; the "1 +" matters there.

**Check 7.** (a) N_{C}: **the number of seats that, all placed at E_{C}, hold the band's electrons**. The exponential: **the chance one seat at E_{C} is filled**. (b) p = 1.04 × 10^{19} × e^{−0.20/0.0259} = **4.6 × 10^{15} cm^{−3}**. (c) (600/300)^{3/2} = **2.83×**.

**Check 8.** (a) E_{F} **cancels** in the product; only N_{C}, N_{V}, E_{g}, T remain. (b) √(2.8 × 10^{19} × 1.04 × 10^{19}) = √(2.91 × 10^{38}) = **1.71 × 10^{19} cm^{−3}**.

**Check 9.** (a) Line 1: **n = p**. (b) ln(N_{V}/N_{C}) > 0, so E_{i} sits slightly **above** mid-gap.

**Check 10.** (a) 0.0259 × ln(10^{7}) = **0.417 eV below**. (b) n = 1.5 × 10^{10} × e^{0.3/0.0259} = **1.6 × 10^{15} cm^{−3}**. (c) n → n_{i}: E_{F} returns to **mid-gap**; the sample behaves as intrinsic.

**Self-test.**

1. 0 K: a step from 1 to 0 at E_{F}. 300 K: rounded over a few kT. Both pass through **½ at E_{F}**.
2. 1 − f = 1 − 1/(1 + e^{−7.72}) = **4.4 × 10^{−4}**.
3. N_{C} is the number of seats per cm^{3} that, all placed at E_{C}, would hold as many electrons as the whole conduction band. It lets n be written as seats × the chance a seat at E_{C} is filled.
4. Step 9, lines 1–5; approximation **N_{C} ≈ N_{V}**.
5. Step 8: the exponents add to −(E_{C} − E_{V})/kT = −E_{g}/kT.
6. 0.0259 × ln(10^{15}/1.5 × 10^{10}) = 0.0259 × 11.1 = **0.288 eV**.
7. n = 2.8 × 10^{19} × e^{−0.206/0.0259} = **10^{16} cm^{−3}**, so N_{D} ≈ **10^{16}** (step 10).
8. n_{i} rises steeply with T; once n_{i} ≫ N_{A}, p ≈ n ≈ n_{i}, the sample behaves as intrinsic and E_{F} → E_{i}.

<!--/ANSWERS-->
