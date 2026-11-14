# 01 — Semiconductors and carriers

<div class="sub">Unit 1–2 deck, slides 19–38 · syllabus Unit 1 · no prerequisite: this is the start</div>

## Map

[[map:1 Bands, electrons, holes > 2 Doping, n·p = n_{i}^{2} > 3 The Fermi level|here=1]]

Every device in this course is made of doped silicon. This file answers two questions: what carries current in silicon, and how many carriers there are. 02 answers the third: what makes them move.

| Constant | Value | Constant | Value |
|---|---|---|---|
| q | 1.6 × 10^{−19} C | V_{T} = kT/q | 25.9 mV ≈ 26 mV at 300 K |
| k | 8.62 × 10^{−5} eV/K | E_{g} | Si 1.12 · Ge 0.67 · GaAs 1.42 eV |
| Si atoms | 5 × 10^{22} cm^{−3} | n_{i} (Si, 300 K) | 10^{10} cm^{−3} (slides); 1.5 × 10^{10} in many books |

## The questions this file answers

- <span class="tag">Deck slides 19–24</span> Using energy bands, explain why heating lowers a semiconductor's resistance but raises a metal's.
- <span class="tag">practice</span> Si doped with N_{D} = 10^{16} cm^{−3}: find n and p.
- <span class="tag">Deck slide 38</span> Show that the Fermi level of an intrinsic semiconductor lies at mid-gap.

---

## Build

### 1 · Energy bands, electrons and holes

:::q <span class="tag">Deck slides 19–24</span>
Using energy bands, explain why heating lowers the resistance of a semiconductor but raises the resistance of a metal.
:::

:::guess Guess first
Write one line for each material before reading on.
:::

:::note Terms
**Valence electron:** an outer electron that forms bonds; Si has 4. **Covalent bond:** two atoms share a pair of electrons. **eV:** the energy one electron gains crossing 1 V, 1.6 × 10^{−19} J.
:::

[[fig:bands|Energy bands of an insulator, a semiconductor and a metal.|w=75]]

- In a crystal the allowed energies form **bands**. The **valence band** holds electrons locked in bonds; the **conduction band** holds free electrons. Between them is the **band gap E_{g}**, with no states.
- At 0 K every bond is full: silicon is an insulator. At room temperature heat breaks a few bonds. Each gives one **free electron** and one **hole**, a missing electron that moves as a charge of +q. So pure silicon has **n = p = n_{i}**.
- n_{i} ≈ 10^{10} cm^{−3} against 5 × 10^{22} atoms: one bond in 10^{12}. n_{i}^{2} ∝ T^{3}e^{−E_{g}/kT}: in Si it roughly doubles every 10 °C. A smaller gap gives a larger n_{i}, so Ge leaks more than Si.

**Answer.** Semiconductor: heating breaks more bonds, so the carrier count rises exponentially; that outweighs the extra scattering, and resistance **falls** (negative temperature coefficient). Metal: the bands overlap, so the number of free electrons is fixed; heat only adds scattering, and resistance **rises**.

:::check Check 1
(a) What are the two carriers, and what is each physically? (b) Why is n = p in pure silicon? (c) Which has the larger n_{i}, Si or Ge, and why?
:::

### 2 · Doping and the mass-action law

:::q <span class="tag">practice</span>
Silicon is doped with N_{D} = 10^{16} donor atoms per cm^{3}. At 300 K, find the electron and hole concentrations.
:::

:::guess Guess first
More holes or fewer holes than in pure silicon?
:::

:::note Terms
**Donor:** 5 valence electrons (P, As, Sb); the fifth is set free. **Acceptor:** 3 valence electrons (B, Al, Ga); the missing bond is a hole.
:::

[[fig:doping_bands|Donor levels just below E_{C}; acceptor levels just above E_{V}.|w=70]]

Donors make **n-type** silicon (electrons majority, holes minority); acceptors make **p-type**. At room temperature every dopant is ionised: **n ≈ N_{D}** (n-type), **p ≈ N_{A}** (p-type). In equilibrium the product is fixed by temperature alone:

$$n · p = n_{i}^{2}$$

Extra electrons make holes rarer, because a hole meets an electron and recombines sooner. The crystal stays neutral: each free electron left a fixed + donor ion (n + N_{A} = p + N_{D}). With both dopants, the larger wins: n ≈ N_{D} − N_{A} (compensated).

**Answer.** n ≈ **10^{16} cm^{−3}**. p = 10^{20}/10^{16} = **10^{4} cm^{−3}**: holes fell from 10^{10} to 10^{4}. (With n_{i} = 1.5 × 10^{10}, p = 2.25 × 10^{4}.)

:::check Check 2
(a) Si has N_{A} = 5 × 10^{17} cm^{−3} of boron. Type, p and n? (b) A doped bar has billions of extra free electrons. Why is it still neutral?
:::

### 3 · The Fermi level

:::q <span class="tag">Deck slide 38</span>
Show that the Fermi level of an intrinsic semiconductor lies at the middle of the forbidden gap.
:::

:::guess Guess first
Which way does E_{F} move when donors are added?
:::

:::note Terms
**f(E):** the probability that a state at energy E is occupied. **N_{C}, N_{V}:** effective number of states at the band edges.
:::

[[fig:fermi_plot|Fermi–Dirac function at two temperatures; f = ½ at E_{F}.|w=60]]

$$f(E) = 1/(1 + e^{(E − E_{F})/kT})$$

E_{F} is where f = ½. Counting filled conduction states and empty valence states:

$$n = N_{C}e^{−(E_{C} − E_{F})/kT}      p = N_{V}e^{−(E_{F} − E_{V})/kT}$$

E_{F} near E_{C} means many electrons (n-type); near E_{V}, many holes. For n-type, **E_{F} − E_{i} = kT ln(N_{D}/n_{i})**. At very high temperature n_{i} catches up with the doping and E_{F} returns to mid-gap.

**Answer.** Intrinsic: n = p, so N_{C}e^{−(E_{C} − E_{F})/kT} = N_{V}e^{−(E_{F} − E_{V})/kT}. With N_{C} = N_{V} the exponents are equal: E_{C} − E_{F} = E_{F} − E_{V}, so **E_{F} = (E_{C} + E_{V})/2**. Without that assumption, E_{F} = (E_{C} + E_{V})/2 + (kT/2)ln(N_{V}/N_{C}), off by only a few meV.

:::check Check 3
(a) f(E_{F}) at 300 K and 600 K? (b) N_{D} = 10^{16}, n_{i} = 10^{10}: how far is E_{F} above mid-gap? (c) f(E) for a state 0.1 eV above E_{F} at 300 K?
:::

---

## Exam form

**Bands.** Sketch insulator / semiconductor / metal; E_{g} values; electron–hole pair generation; n = p = n_{i}; temperature dependence; the semiconductor-vs-metal argument.

**Doping.** Donor and acceptor with examples; n ≈ N_{D}, p ≈ N_{A}; n·p = n_{i}^{2}; neutrality; compensation.

**Fermi level.** f(E); n and p expressions; derivation of E_{F} at mid-gap; E_{F} − E_{i} = kT ln(N_{D}/n_{i}).

## Traps

- Taking p = N_{D} − n or similar: use n·p = n_{i}^{2} for the minority.
- Saying a doped bar is charged: it is neutral.
- Using kT in joules with energies in eV: use 0.0259 eV at 300 K.
- Mixing n_{i} = 10^{10} and 1.5 × 10^{10}: state which you use.

## Self-test

1. Why does GaAs (1.42 eV) have a smaller n_{i} than Si?
2. N_{D} = 10^{15} cm^{−3}, n_{i} = 10^{10}. Find n and p.
3. N_{A} = 10^{16} and N_{D} = 4 × 10^{15} cm^{−3} together. Type, p and n?
4. Probability that a state 0.2 eV below E_{F} is occupied at 300 K?
5. For p-type with N_{A} = 10^{17}, how far is E_{F} below mid-gap?
6. Derive E_{F} = (E_{C} + E_{V})/2 from memory.

<!--ANSWERS-->

## Answers

**Check 1.** (a) Free electrons in the conduction band; holes, missing bond electrons that act as +q charges. (b) Each broken bond makes exactly one of each. (c) **Ge**: its smaller gap (0.67 eV) lets heat break more bonds.

**Check 2.** (a) **p-type**. p ≈ **5 × 10^{17}**, n = 10^{20}/(5 × 10^{17}) = **200 cm^{−3}**. (b) Every free electron left behind a fixed donor ion of charge +q.

**Check 3.** (a) **½** at both. (b) 0.0259 × ln(10^{6}) = **0.357 eV**. (c) 1/(1 + e^{3.86}) = 1/48.7 ≈ **0.0205**.

**Self-test.**

1. A larger gap means fewer bonds broken by heat: n_{i} ∝ e^{−E_{g}/2kT}.
2. n = **10^{15}**, p = **10^{5} cm^{−3}**.
3. **p-type**: p ≈ 6 × 10^{15}; n = 10^{20}/(6 × 10^{15}) = **1.67 × 10^{4} cm^{−3}**.
4. f = 1/(1 + e^{−7.72}) = **0.9996**.
5. 0.0259 × ln(10^{7}) = **0.417 eV**.
6. See step 3.

<!--/ANSWERS-->
