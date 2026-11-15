# 01a — Silicon: bonds, bands, electrons and holes

<div class="sub">Unit 1–2 deck, slides 3–24 and 37–40 · syllabus Unit 1 (intrinsic and extrinsic semiconductors, energy bands) · no prerequisite: this is the start · no past-paper question yet: openers are Predict prompts</div>

## Map

[[map:1 Atoms and bonds > 2 Breaking a bond > 3 The hole > 4 Energy bands > 5 n_{i} and heat > 6 Donors > 7 Acceptors > 8 n·p = n_{i}^{2}|here=1]]

Every device in this course is a piece of silicon with a few chosen impurities. This file answers one question: **what carries current inside silicon, and how many of these carriers are there?** 01b then explains *why* the counts come out as they do (the Fermi level). 02 explains what makes the carriers move.

| Symbol | Meaning | Value used |
|---|---|---|
| q | charge of one electron (magnitude) | 1.6 × 10^{−19} C |
| eV | energy one electron gains crossing 1 V | 1.6 × 10^{−19} J |
| k | Boltzmann's constant | 8.62 × 10^{−5} eV/K |
| kT | typical heat energy per particle | 0.0259 eV at 300 K |
| cm^{−3} | "per cubic centimetre": every concentration in this file | — |

---

## Build

### 1 · Atoms and covalent bonds

:::guess Predict
Copper conducts; glass does not. Silicon sits in between. What do you think silicon's outer electrons are doing that a metal's are not?
:::

:::note Terms
**Valence electrons:** the electrons in an atom's outermost shell; they are the ones that bond. **Covalent bond:** two neighbouring atoms share one pair of electrons, one from each. **Crystal:** atoms arranged in one repeating pattern.
:::

[[fig:lattice_pure_broken|Silicon crystal drawn flat. Circles = atoms; each pair of dots on a line = one covalent bond (2 shared electrons). Left: at 0 K. Right: at room temperature one bond has broken.|w=92]]

- Silicon (14 electrons) and germanium (32) both have **4 valence electrons** (deck slide 5). Each Si atom bonds to 4 neighbours, sharing one electron with each. Every valence electron is then locked in a bond.
- An electron locked in a bond **cannot carry current**: it cannot leave its place.
- In a metal, the outer electrons are not locked in bonds at all: they roam the whole crystal. That is the difference the Predict asks for.

:::check Check 1
(a) How many bonds does each Si atom make, and how many electrons are in one bond? (b) Why does a perfect Si crystal at 0 K not conduct?
:::

### 2 · Breaking a bond: the free electron

Some bonds must break for silicon to conduct at all.

:::guess Predict
What could supply the energy to pull an electron out of a bond?
:::

:::note Terms
**Free electron:** an electron that has left its bond and can move through the crystal. **Intrinsic silicon:** silicon so pure that every free carrier comes from broken bonds, none from impurities (deck slide 13).
:::

- **Heat** (thermal energy) or **light** (a photon) can break a bond (deck slide 11). The released electron wanders through the crystal and can carry current.
- In pure silicon at 300 K the number of free electrons per cm^{3} is about **1.5 × 10^{10}** (deck slide 11). That sounds large, but Si has **5 × 10^{22} atoms** per cm^{3}: only about **1 bond in 3 × 10^{12}** is broken.
- So pure silicon conducts, but very weakly. Most of this course is about raising the carrier count on purpose (steps 6–7).

:::check Check 2
(a) Name the two energy sources that free electrons. (b) Pure Si has 5 × 10^{22} atoms/cm^{3} and 1.5 × 10^{10} free electrons/cm^{3}. Roughly how many atoms per free electron?
:::

### 3 · The hole: the second carrier

A broken bond leaves something behind, and it carries current too.

:::guess Predict
A bond is missing one electron. A neighbouring bond electron is next to the gap. What can it do, and what does the gap appear to do?
:::

:::note Terms
**Hole:** the empty place in a bond after its electron leaves. It behaves like a particle with charge **+q**. **Carrier:** anything mobile that carries charge; in a semiconductor, free electrons and holes.
:::

[[fig:hole_motion|One row of bonds, three moments. Black dot = bond electron; red ring = the hole. Each step, one bond electron hops left into the hole.|w=95]]

- A bond electron next to the hole can hop into it with very little energy: it stays a bond electron, just in a neighbouring bond. The hole is now where that electron came from.
- Repeat: electrons step **left** one at a time, so the hole travels **right**. A missing negative charge moving right is the same current as a **positive** charge moving right. So we track the hole as a +q particle.
- Every broken bond makes **one free electron and one hole**. In intrinsic silicon:

$$n = p = n_{i}$$

**n** = free electrons per cm^{3}; **p** = holes per cm^{3}; **n_{i}** = the intrinsic carrier concentration (each of them, not their sum).

:::check Check 3
(a) Is a hole an empty seat in a bond or a positive particle? Which description is the physics, and which is the bookkeeping? (b) Why must n equal p in pure silicon?
:::

### 4 · Energy bands

The bond picture tells *what* happens. To say *how much energy* it costs, we need the band picture, which every later file uses.

:::guess Predict
A single atom only allows electrons at certain sharp energies. Bring 10^{22} atoms close together. What do you guess happens to those sharp energies?
:::

:::note Terms
**Energy level:** an energy an electron is allowed to have. **Band:** a dense range of allowed energies formed from one level of many atoms. **Band gap E_{g}:** a range of energies no electron in the crystal can have.
:::

[[fig:levels_to_bands|How bands form. Horizontal axis: how close the atoms are (pushed together towards the right). Vertical axis: electron energy. Far apart (left), each level is one sharp line. Close together, each line spreads into a band.|w=78]]

**Reading the figure.** Each atom alone allows sharp energies (left edge). When atoms are pushed close, their electrons interact and each sharp level splits into as many levels as there are atoms, packed so tightly they form a continuous **band** (deck slides 21–24). At the actual spacing in silicon (dashed line), two bands matter:

| Band | Its electrons | Edge |
|---|---|---|
| **Valence band** | bond electrons (step 1) | top edge **E_{V}** |
| **Conduction band** | free electrons (step 2) | bottom edge **E_{C}** |

Between them is the **band gap, E_{g} = E_{C} − E_{V}**: no allowed energies. Breaking a bond = lifting an electron from the valence band to the conduction band, which costs at least E_{g}. The hole is the empty place left in the valence band.

[[fig:bands|The same idea for three materials. The gap size decides how many electrons heat can lift.|w=78]]

| Material | E_{g} at 300 K | Result |
|---|---|---|
| metal | bands overlap, no gap | electrons always free |
| Ge · Si · GaAs | 0.66 · 1.12 · 1.42 eV | heat frees a few |
| insulator (diamond, glass) | > 5 eV | almost none freed |

:::check Check 4
(a) In band language, what is a free electron and what is a hole? (b) Why can no electron in pure Si have an energy halfway between E_{V} and E_{C}?
:::

### 5 · How n_{i} depends on temperature and on E_{g}

:::guess Predict
Heat silicon from 25 °C to 35 °C. Does n_{i} rise by about 3 %, about 30 %, or about 100 %?
:::

[[fig:ni_vs_T|n_{i} against temperature for three materials. The vertical axis is logarithmic: each grid step is ×10.|w=72]]

**Reading the figure.** Each curve shows how many carriers heat frees (per cm^{3}) at each temperature. Three facts come straight off it:

- **Steep rise with T.** For Si near room temperature, n_{i} **roughly doubles every 10 °C** (deck slide 37: 8.1 × 10^{9} at 25 °C, 1.7 × 10^{10} at 35 °C).
- **Smaller gap, more carriers.** At 300 K: Ge ≈ 2.4 × 10^{13}, Si ≈ 1.5 × 10^{10}, GaAs ≈ 1.8 × 10^{6} cm^{−3}.
- **Why so steep:** the controlling factor is e^{−E_{g}/2kT} (derived in 01b). At 300 K: Ge 2.8 × 10^{−6}, Si 4.1 × 10^{−10}, GaAs 1.2 × 10^{−12}. A small change in E_{g}/kT changes the count by orders of magnitude.

**Answer to the Predict.** About **100 %**: it doubles. That is why semiconductor resistance **falls** when heated (negative temperature coefficient), while a metal's **rises**: a metal already has all its electrons free, so heat only adds collisions (deck slide 19).

:::note n_{i} differs between books
Si: 1.5 × 10^{10} (deck, Boylestad), 1.45 × 10^{10}, or 1.0 × 10^{10} (newer measurements). Use the value the question gives; if none is given, state the one you use.
:::

:::check Check 5
(a) Roughly how much does Si's n_{i} grow from 300 K to 330 K? (b) Why does Ge leak more current than Si at the same temperature?
:::

### 6 · Donors: n-type silicon

n_{i} is tiny and swings with temperature. Devices need carrier counts that are large and fixed. Doping supplies them.

:::guess Predict
Replace one Si atom with phosphorus, which has 5 valence electrons. Four go into bonds. What happens to the fifth?
:::

:::note Terms
**Doping:** adding chosen impurity atoms on purpose (deck slide 18). **Donor:** an impurity with 5 valence electrons (P, As, Sb) that gives away one electron. **N_{D}:** donor atoms per cm^{3}.
:::

[[fig:lattice_dopants|Left: a phosphorus atom (P) in the crystal; its 5th electron has no bond to join. Right: a boron atom (B); one bond is short of an electron.|w=92]]

[[fig:dopant_levels|The same two cases as energy levels. Freeing a donor's 5th electron costs only ≈ 45 meV (P), against 1120 meV to break a Si bond.|w=88]]

- The 5th electron is held only weakly: **≈ 45 meV for P, 54 meV for As** (deck slide 39). In the band picture it sits at a **donor level E_{D}** just below E_{C}.
- At 300 K, kT = 26 meV, so heat frees practically every donor electron: **every donor is ionised**. Each gives one free electron and leaves a fixed **+ ion** (the P atom, now one electron short) that cannot move.
- **No hole is made**: the bonds are all complete. So electrons outnumber holes.

**n-type silicon:** electrons are the **majority carriers**, holes the **minority carriers**, and **n ≈ N_{D}**.

How strong this is: 1 part per million of P gives N_{D} = 10^{−6} × 5 × 10^{22} = **5 × 10^{16} cm^{−3}**, about 3.3 million times n_{i} (deck slide 17: "1 part per million can transform a poor conductor into a good one").

:::check Check 6
(a) After a donor gives its electron, what is left behind, and can it move? (b) Why is n-type silicon still electrically neutral?
:::

### 7 · Acceptors: p-type silicon

:::guess Predict
Boron has 3 valence electrons. Which bond around it is incomplete, and what will a nearby bond electron do?
:::

:::note Terms
**Acceptor:** an impurity with 3 valence electrons (B, Al, Ga) that accepts one electron from a neighbouring bond. **N_{A}:** acceptor atoms per cm^{3}.
:::

- Boron fills only 3 of its 4 bonds (right panel of the lattice figure above). A neighbouring bond electron needs only **≈ 45 meV** to jump in (deck slide 39): the **acceptor level E_{A}** sits just above E_{V}.
- The jump completes boron's bonds, so boron becomes a fixed **− ion**, and leaves a **hole** in the valence band, free to move.
- At 300 K every acceptor is ionised: **p ≈ N_{A}**.

| | n-type | p-type |
|---|---|---|
| impurity | donor, 5 valence e⁻: P, As, Sb | acceptor, 3 valence e⁻: B, Al, Ga |
| fixed ion left | + | − |
| majority carrier | electrons, n ≈ N_{D} | holes, p ≈ N_{A} |
| minority carrier | holes | electrons |
| level | E_{D} just below E_{C} | E_{A} just above E_{V} |

:::check Check 7
(a) Gallium is in the same group as boron. Which type does it make? (b) In p-type Si, where do the free electrons come from?
:::

### 8 · The mass-action law: n · p = n_{i}^{2}

Doping fixes the majority count. The minority count needs one more rule.

:::q <span class="tag">practice</span>
Silicon is doped with N_{D} = 10^{16} cm^{−3}, n_{i} = 1.5 × 10^{10} cm^{−3}, 300 K. Find n and p.
:::

:::guess Guess first
Does adding electrons leave the hole count at n_{i}, raise it, or lower it?
:::

:::note Terms
**Thermal equilibrium:** steady temperature, no applied voltage or light: nothing drives the material. **Recombination:** a free electron falls into a hole; both carriers disappear.
:::

- Bonds keep breaking (generation, set by temperature only) and electrons keep falling into holes (recombination). In equilibrium the two rates are equal.
- Recombination needs an electron to *meet* a hole, so its rate grows with n × p. Generation depends only on T. Balance therefore fixes the **product**:

$$n · p = n_{i}^{2}      (thermal equilibrium, any doping)$$

- So extra electrons make holes **rarer**: a hole now meets an electron and vanishes sooner. 01b proves the law another way.
- **Charge neutrality:** total + charge = total − charge, so **n + N_{A} = p + N_{D}**. With both dopants, the larger wins: n ≈ N_{D} − N_{A} if N_{D} > N_{A} (called **compensated** silicon).

**Answer.** All donors ionised: n ≈ N_{D} = **10^{16} cm^{−3}**. p = n_{i}^{2}/n = (1.5 × 10^{10})^{2}/10^{16} = 2.25 × 10^{20}/10^{16} = **2.25 × 10^{4} cm^{−3}**. Holes fell from 1.5 × 10^{10} to about 2 × 10^{4}. (With n_{i} = 10^{10}: p = 10^{4}.)

:::note When n ≈ N_{D} fails
If N_{D} is not much larger than n_{i}, solve neutrality and mass action together: n = N_{D}/2 + √((N_{D}/2)^{2} + n_{i}^{2}). Example N_{D} = 10^{10}, n_{i} = 1.5 × 10^{10}: n = 5 × 10^{9} + √(2.5 × 10^{19} + 2.25 × 10^{20}) = **2.08 × 10^{10}**, p = 2.25 × 10^{20}/2.08 × 10^{10} = **1.08 × 10^{10} cm^{−3}**.
:::

:::check Check 8
(a) Si has N_{A} = 5 × 10^{17} cm^{−3} of boron, n_{i} = 1.5 × 10^{10}. Type, p and n? (b) N_{A} = 10^{16} and N_{D} = 4 × 10^{15} cm^{−3} together. Type, majority and minority concentrations?
:::

---

## Exam form

**Intrinsic semiconductor (definition + sketch).** Pure crystal; carriers only from bonds broken by heat or light; each broken bond gives one free electron and one hole, so n = p = n_{i}. Draw the flat lattice with one broken bond.

**Hole.** The vacancy left by a bond electron; neighbouring bond electrons move into it, so it moves opposite to them and acts as a +q carrier.

**Energy bands (sketch insulator / semiconductor / conductor).** Valence band (bond electrons, top E_{V}), conduction band (free electrons, bottom E_{C}), band gap E_{g} = E_{C} − E_{V}. E_{g}: Ge 0.66, Si 1.12, GaAs 1.42 eV; insulator > 5 eV; metal: bands overlap.

**Temperature coefficient.** Semiconductor: heat frees more carriers (n_{i} ∝ e^{−E_{g}/2kT}, Si doubles per ≈ 10 °C) → resistance falls (negative). Metal: carrier count fixed, more collisions → resistance rises (positive).

**Extrinsic semiconductor.** n-type: donors (P, As, Sb; 5 valence e⁻), E_{D} ≈ 45 meV below E_{C}, n ≈ N_{D}, holes minority. p-type: acceptors (B, Al, Ga; 3 valence e⁻), E_{A} ≈ 45 meV above E_{V}, p ≈ N_{A}, electrons minority. Draw both lattices and both band diagrams.

**Numerical procedure (carrier concentrations).**

1. Find the net doping: N_{D} − N_{A} (or N_{A} − N_{D}); the larger dopant sets the type.
2. Majority ≈ net doping (all dopants ionised at 300 K).
3. Minority = n_{i}^{2} / majority. State the n_{i} you used.
4. If net doping is not ≫ n_{i}, use n = N/2 + √((N/2)^{2} + n_{i}^{2}).

## Traps

- Writing p = N_{D} − n or p = n_{i} for doped material: the minority is always **n_{i}^{2}/majority**.
- Saying doped silicon is charged: each free carrier left a fixed ion of the opposite sign. It is **neutral**.
- Calling holes "positive electrons" or "missing atoms": a hole is a missing **bond electron**.
- Mixing n_{i} = 10^{10} and 1.5 × 10^{10} within one answer.
- Saying n = p = n_{i} counts both carriers together: n_{i} is the count of **each**.

## Self-test

1. Draw the flat Si lattice with one P atom and one B atom; label the fixed ions and the free carriers.
2. Explain with the band diagram why a semiconductor's resistance falls with temperature.
3. N_{D} = 10^{15} cm^{−3}, n_{i} = 10^{10}. Find n and p.
4. N_{D} = 2 × 10^{17} and N_{A} = 5 × 10^{16} cm^{−3}, n_{i} = 1.5 × 10^{10}. Type, n and p?
5. Why is GaAs's n_{i} about 10^{4} times smaller than Si's?
6. The P donor's binding energy is 45 meV. How many kT is that at 300 K, and why does it mean every donor is ionised?
7. Give two reasons silicon is doped rather than used pure.

<!--ANSWERS-->

## Answers

**Check 1.** (a) **4 bonds**, **2 electrons** per bond (one from each atom). (b) Every valence electron is locked in a bond; none can move.

**Check 2.** (a) **Heat** and **light**. (b) 5 × 10^{22}/1.5 × 10^{10} ≈ **3 × 10^{12}** atoms per free electron.

**Check 3.** (a) Physically it is an **empty place** in a bond; treating it as a **+q particle** is the bookkeeping that gives the right current. (b) Each broken bond makes exactly **one of each**.

**Check 4.** (a) Free electron = an electron in the **conduction band**; hole = an empty state in the **valence band**. (b) That energy lies in the **gap**: there are no allowed states there.

**Check 5.** (a) Three steps of 10 K, each about ×2: **≈ 8×** (formula: 8.3). (b) Ge's gap is smaller (0.66 vs 1.12 eV), so heat frees **about 1600× more** carriers (2.4 × 10^{13} vs 1.5 × 10^{10}).

**Check 6.** (a) A **fixed + ion** (P with one electron short); it is part of the crystal and **cannot move**. (b) For every free electron there is one + ion: total charge is **zero**.

**Check 7.** (a) **p-type** (3 valence electrons: acceptor). (b) From **bonds broken by heat**: n = n_{i}^{2}/p, a very small number.

**Check 8.** (a) **p-type**. p ≈ **5 × 10^{17}**; n = 2.25 × 10^{20}/5 × 10^{17} = **450 cm^{−3}**. (b) N_{A} > N_{D}: **p-type**. p ≈ 10^{16} − 4 × 10^{15} = **6 × 10^{15}**; n = 2.25 × 10^{20}/6 × 10^{15} = **3.75 × 10^{4} cm^{−3}** (n_{i} = 1.5 × 10^{10}).

**Self-test.**

1. P: fixed **+** ion, one free electron nearby. B: fixed **−** ion, one hole nearby. All other bonds complete.
2. Heat lifts electrons across E_{g}; n_{i} rises ∝ e^{−E_{g}/2kT}; more carriers → lower resistance. The extra collisions are outweighed.
3. n = **10^{15}**, p = 10^{20}/10^{15} = **10^{5} cm^{−3}**.
4. **n-type**. n ≈ 2 × 10^{17} − 5 × 10^{16} = **1.5 × 10^{17}**; p = 2.25 × 10^{20}/1.5 × 10^{17} = **1500 cm^{−3}**.
5. Larger gap (1.42 vs 1.12 eV) and n_{i} ∝ e^{−E_{g}/2kT}: e^{−0.30/0.0518} ≈ 1/330, and the effective-seat counts (01b) differ too; together ≈ 10^{4}.
6. 45/25.9 = **1.74 kT**: small enough that heat frees practically every donor electron at 300 K.
7. Pure Si has **too few** carriers (n_{i} ≈ 10^{10}), and n_{i} **changes rapidly with temperature**. Doping gives a large, temperature-steady count, and sets the carrier **type**.

<!--/ANSWERS-->
