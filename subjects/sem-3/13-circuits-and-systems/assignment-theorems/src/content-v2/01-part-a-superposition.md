# Part A · Superposition (v2 demo)

<div class="sub">Ghosh & A K Chakraborty, <i>Circuit Theory and Networks</i> 4e, ch. 5, Solved Problems 5.1–5.14 · new How / What / Why format</div>

<div class="howto" markdown="1">
<div class="bh">How to read this version</div>

- **How:** the literal working, so you can follow the solution line by line.
- **What:** one line saying what we did and where: "KCL at node X", "switch off the 2 A".
- **Why:** the reasoning behind the move. This is the part that carries over to questions you haven't seen.

**Fading:** A1–A3 label every step. From A4 on, only the steps that use an idea from the **What's new** box get What / Why; routine working is left bare. Practice questions are bare: by then the moves are yours.
</div>

[[map:KVL, KCL, Ohm's law (you have these) > Nodal / mesh: all sources at once > Superposition: one source at a time > Thevenin / Norton (next)|here=3]]

**Where this sits.** You can already solve any circuit with nodal or mesh analysis, taking every source at once. Superposition breaks the same job into smaller circuits, **one source at a time**, which is often quicker by hand. It is also the reason Thevenin's theorem works, which comes next.

**Three terms first.**

- **Linear circuit:** made of R, L, C, linear dependent sources and independent sources. Doubling every source doubles every current and voltage.
- **Independent source:** a fixed voltage or current (a battery, a 2 A source, 10 cos 4t).
- **Dependent source** (diamond symbol): its value follows some other voltage or current in the circuit, for example 2V_{x}.

**Statement.** In a linear circuit with several independent sources, any current or voltage is the **algebraic sum** of the values caused by **each independent source acting alone**.

**Switching a source off** means setting its value to zero:

| Source | Switched off it becomes | Why |
|---|---|---|
| Ideal voltage source | **short circuit** | 0 V across it |
| Ideal current source | **open circuit** | 0 A through it |
| Dependent source | **never switched off** | it is not a source on its own; it follows the circuit |

Superposition adds currents and voltages only, **not power** (P goes as I², and (I′ + I″)² ≠ I′² + I″²).

<div class="qhead"><span class="qn">A1 · Problem 5.1</span><span class="qt">Superposition · DC <span class="lvl heavy">teach · every step labelled</span></span></div>

:::q
Find the current I in the circuit shown, using the superposition theorem.
:::

[[img:ck5_1|I flows left to right through the 2 Ω resistor.|w=70]]

:::try
Cover everything below. Draw two circuits, 1 V alone and 1 A alone, find the current in the 2 Ω in each, and decide each one's sign before adding.
:::

:::new Hint: what's new
- **The whole method:** two sources, so solve **two small circuits** and add.
- **Switching off:** the 1 V source becomes a short; the 1 A source becomes an open.
- **Signs:** measure each part against the arrow drawn for I. A part flowing the other way is negative.
:::

[[img:ck5_1s|(i) 1 V acting alone (1 A opened) · (ii) 1 A acting alone (1 V shorted)|w=88]]

**Given:** 1 A source, 1 V source; 1 Ω (series), 1 Ω (shunt), 2 Ω, 3 Ω. **To find:** I through the 2 Ω (left → right).

:::step
@how
$$I = I′ (1 V alone) + I″ (1 A alone),  both measured left → right through the 2 Ω$$
@what Split the circuit into two single-source circuits; agree one reference arrow for both parts.
@why Two sources at once would need simultaneous equations. One source at a time, each circuit is plain series/parallel. The parts only add correctly if both are measured along the **same** arrow, so fix that arrow (I's) before starting.
:::

**Case (i): 1 V alone**

:::step
@how
Replace the 1 A source with an open circuit. The left 1 Ω now ends at an open gap, so it carries 0 A.
@what Switch off the 1 A (current source → open).
@why "Off" means value = 0. A source forcing 0 A behaves exactly like a broken wire. Anything **in series** with that gap carries nothing, so the left 1 Ω drops out.
:::

:::step
@how
The 3 Ω is directly across the 1 V, so ignore it. What is left is one loop, 1 V → 2 Ω → 1 Ω (shunt) → back:
$$current = \frac{1}{2 + 1} = \frac{1}{3} A,  flowing right → left in the 2 Ω$$
@what Drop the 3 Ω, then Ohm's law on the single series loop.
@why An element **in parallel with an ideal voltage source** cannot change anything else: the source fixes its voltage, and it fixes it whether the 3 Ω is there or not. Removing it leaves one series loop, where I = V ÷ (total R).
:::

:::step
@how
$$I′ = −\frac{1}{3} A$$
@what Give the part its sign by comparing with I's arrow.
@why The 1 V pushes current out of its + terminal (top right) leftwards through the 2 Ω, opposite to I's arrow. A part flowing against the reference arrow enters the sum as negative.
:::

**Case (ii): 1 A alone**

:::step
@how
Replace the 1 V with a short. The 3 Ω now has a wire across it, so it has 0 V and carries 0 A.
@what Switch off the 1 V (voltage source → short); the 3 Ω is shorted out.
@why A source forcing 0 V is a plain wire. Current always takes a 0 Ω path over a resistor beside it, so a resistor with a wire across it drops out.
:::

:::step
@how
$$I″ = 1 × \frac{1}{1 + 2} = \frac{1}{3} A  (left → right, along I)$$
@what Current divider at the middle node, between the 1 Ω shunt and the 2 Ω.
@why The 1 A arrives at the middle node and has two ways back down: the 1 Ω, or the 2 Ω then the short. Two parallel paths sharing a **known** current call for a divider: share in one branch = I × (other branch) ÷ (sum). The series 1 Ω on the left doesn't matter: the source delivers 1 A through it whatever its value.
:::

:::step
@how
$$I = I′ + I″ = −\frac{1}{3} + \frac{1}{3} = 0$$
@what Add the signed parts.
@why This is the superposition statement: the full response is the algebraic sum of the single-source responses.
:::

:::ans
**I = 0 A** (= book)
:::

:::note Why zero, and two shortcuts
- Node check: 1 = \frac{V_{A}}{1} + \frac{V_{A} − 1}{2} gives V_{A} = 1 V, the same as the right-hand node, so no current flows in the 2 Ω.
- An element **in series with an ideal current source** never changes any other current (the left 1 Ω here).
- An element **in parallel with an ideal voltage source** never changes any other current (the 3 Ω here).
:::

<div class="qhead"><span class="qn">A2 · Problem 5.2</span><span class="qt">Superposition · AC <span class="lvl heavy">teach · every step labelled</span></span></div>

:::q
Calculate the voltage V across the resistor R by using the superposition theorem.
:::

[[img:ck5_2|The book draws +/− signs inside the current source. Read it by its arrow: 1 A pushed up into the top node.|w=62]]

:::try
Which elements drop out in each case? Aim for V′ and V″ in the form \frac{something}{1 + j}.
:::

:::new Hint: what's new
- **AC (phasor) circuit.** j1 Ω is an inductor, −j5 Ω a capacitor. Superposition is unchanged; the arithmetic uses complex numbers.
- **Complex dividers:** the same formulas as for resistors, with Z in place of R.
- The −j5 + j4 branch is **across the 1 V source** (5.1's shortcut), so it never matters.
:::

[[img:ck5_2s|(i) 1 A acting alone · (ii) 1 V acting alone|w=80]]

**Given:** 1 A, 1 V; R = 1 Ω, j1 Ω, −j5 Ω, j4 Ω. **To find:** V across R (+ at top).

:::step
@how
$$V = V′ (1 A alone) + V″ (1 V alone),  both + at the top of R$$
@what Two single-source circuits; one reference polarity (+ at top of R).
@why Same plan as 5.1. Being AC changes only the arithmetic: every impedance is a complex number, and every rule (Ohm, KCL, dividers, superposition) works on it unchanged.
:::

**Case (i): 1 A alone**

:::step
@how
Short the 1 V. The right top node is now joined to the bottom, so the −j5 + j4 branch has both ends on the bottom wire: it carries nothing. The j1 now runs from the top node straight to the bottom.
@what Switch off the 1 V, then redraw to see what is left: R and j1, both from the top node to the bottom.
@why A branch whose two ends land on the same node has 0 V across it and drops out. After any switch-off, look for elements that now sit between the same two nodes; that is how a messy circuit turns into a simple one.
:::

:::step
@how
$$V′ = 1 × (R ∥ j1) = 1 × \frac{1 × j1}{1 + j1} = \frac{j}{1 + j} V$$
@what Ohm's law on the parallel pair: V = I × Z_{parallel}.
@why The 1 A can only go through R or j1, and both join the same two nodes, so they are in parallel. A known current into a known impedance gives the voltage directly; no divider is needed, because we want the voltage, not a branch current.
:::

**Case (ii): 1 V alone**

:::step
@how
Open the 1 A. Drop the −j5 + j4 branch (it sits across the 1 V). One loop remains: 1 V → j1 → R → back.
$$I″ = \frac{1}{1 + j}  ⇒  V″ = 1 × I″ = \frac{1}{1 + j} V$$
@what Switch off the 1 A, drop the branch across the source, then Ohm's law on the series loop and on R.
@why These are 5.1's two shortcuts again (series with a current source, parallel with a voltage source). I″ flows down through R, top to bottom, so the top of R is +, which matches the reference: no sign flip.
:::

:::step
@how
$$V = \frac{j}{1 + j} + \frac{1}{1 + j} = \frac{1 + j}{1 + j} = 1 V$$
@what Add over the common denominator.
@why Leaving each part as a fraction over the same (1 + j) makes the sum one line. Converting to decimals first would hide the clean answer.
:::

:::ans
**V = 1∠0° V** (= book)
:::

:::note Check
Node equation at the top node: 1 = \frac{V}{1} + \frac{V − 1}{j1} gives V(1 + j) = 1 + j, so V = 1 V ✓.
:::

<div class="qhead"><span class="qn">A3 · Problem 5.3</span><span class="qt">Superposition · dependent source <span class="lvl heavy">teach · every step labelled</span></span></div>

:::q
Use the superposition theorem on the circuit shown to find I.
:::

[[img:ck5_3|2V_{x} is a voltage-controlled voltage source. V_{x} is across the 2 Ω with + at the bottom.|w=58]]

:::try
Write V_{x}′ in terms of the loop current in case (i). For case (ii), write one KCL at the top of the 2 Ω and one equation for the left branch. Expect elevenths.
:::

:::new Hint: what's new
- **Dependent source:** it **stays in every case**. Only the 10 V and the 2 A take turns.
- **Its value changes per case:** 2V_{x}′ in case (i), 2V_{x}″ in case (ii). Re-find V_{x} in each sub-circuit.
- **Polarity of V_{x}:** + is at the **bottom** of the 2 Ω. Most wrong answers to this question come from this sign.
:::

[[img:ck5_3s|(i) 10 V alone (2 A opened) · (ii) 2 A alone (10 V shorted); the dependent source stays in both|w=88]]

**Given:** 10 V, 2 A, 5 Ω, 2 Ω, VCVS 2V_{x}. **To find:** I (out of the 10 V source, through the 5 Ω).

:::step
@how
$$I = I′ (10 V alone) + I″ (2 A alone)$$
The diamond stays in both circuits, as 2V_{x}′ in case (i) and 2V_{x}″ in case (ii).
@what Two single-source circuits; the dependent source is kept in both.
@why Superposition switches off **independent** sources only. The diamond has no value of its own; it is "2 × whatever V_{x} is right now". Each case has its own V_{x}, so the diamond is the same element with a different value. Shorting it would delete a part of the circuit, not a source.
:::

**Case (i): 10 V alone**

:::step
@how
Open the 2 A. One loop is left: 10 V → 5 Ω → diamond → 2 Ω → back. Call its current i′, clockwise.
@what Switch off the 2 A; name one loop current, clockwise.
@why One loop needs one unknown current. Clockwise matches I's arrow (out of the 10 V's +, rightwards through the 5 Ω), so I′ = i′ with no sign to fix at the end.
:::

:::step
@how
$$V_{x}′ = −2i′$$
@what Write the controlling voltage V_{x}′ in terms of the loop current.
@why The diamond brings a second unknown, V_{x}′. **Every dependent source needs this one extra line:** its controlling quantity in terms of your unknowns. i′ flows down the 2 Ω, which makes the top of the 2 Ω +. V_{x} is defined with + at the bottom, so V_{x}′ = −(2i′).
:::

:::step
@how
$$10 + 2V_{x}′ = 5i′ + 2i′$$
@what KVL around the loop, going clockwise.
@why One loop gives one equation. Going clockwise you **rise** 10 V (− to + through the source), **drop** 5i′, **rise** 2V_{x}′ (the diamond is crossed − to +), and **drop** 2i′. Total rise = total drop.
:::

:::step
@how
$$10 + 2(−2i′) = 7i′  ⇒  10 = 11i′  ⇒  I′ = i′ = \frac{10}{11} A$$
@what Substitute V_{x}′ = −2i′ into the KVL and solve.
@why Now there is one equation in one unknown.
:::

**Case (ii): 2 A alone**

:::step
@how
Short the 10 V, so the left end of the 5 Ω is on the bottom wire. Take the bottom wire as 0 V. Then the top of the 2 Ω (node X) is at V_{X} = −V_{x}″.
@what Switch off the 10 V; choose the bottom wire as reference (0 V).
@why With a reference node, every point has a single voltage and each branch current is just (voltage difference) ÷ R. X is the − end of V_{x} and the + end is at 0 V, so X sits at −V_{x}″.
:::

:::step
@how
Unknowns: V_{x}″, and i″ = the current leaving X to the left (through the diamond and the 5 Ω). The current down the 2 Ω is \frac{V_{X}}{2} = −\frac{V_{x}″}{2}.
@what Label the two ways the 2 A can leave node X.
@why The 2 A arrives at X and has exactly two exits: down the 2 Ω, or left through the diamond and 5 Ω. The diamond needs V_{x}″ anyway, and the 2 Ω current is already written in V_{x}″, so two unknowns cover the whole circuit.
:::

:::step
@how
$$KCL at X:  2 = −\frac{V_{x}″}{2} + i″   …(1)$$
@what KCL at node X (top of the 2 Ω).
@why X is the one node where the **known** 2 A meets **both** unknowns, so in = out gives a single equation containing exactly our two unknowns. General habit: write KCL at the node where the known current source enters.
:::

:::step
@how
Walk the left branch from X to ground. X is at −V_{x}″. Crossing the diamond from + to − drops another 2V_{x}″, so the right end of the 5 Ω is at −3V_{x}″; its left end is at 0 V.
$$i″ = \frac{−3V_{x}″ − 0}{5} = −\frac{3}{5}V_{x}″   …(2)$$
@what Follow the voltage along the left branch (KVL), then Ohm's law on the 5 Ω.
@why Two unknowns need a second equation. The left branch is a single path, so its current is set by Ohm's law on the 5 Ω once you know the voltage at both ends. Walking from a known voltage and adding each element's rise or drop gives that end voltage.
:::

:::step
@how
$$(2) in (1):  2 = −\frac{V_{x}″}{2} − \frac{3V_{x}″}{5} = −\frac{11}{10}V_{x}″  ⇒  V_{x}″ = −\frac{20}{11} V,  i″ = \frac{12}{11} A$$
@what Substitute and solve.
@why (2) gives i″ in terms of V_{x}″, so (1) becomes one equation in one unknown.
:::

:::step
@how
$$I″ = −\frac{12}{11} A$$
@what Sign against I's arrow.
@why i″ flows **leftwards** through the 5 Ω; I's arrow points right. Opposite direction, so the part is negative.
:::

:::step
@how
$$I = I′ + I″ = \frac{10}{11} − \frac{12}{11} = −\frac{2}{11} A$$
@what Add the signed parts.
@why Superposition: the sum of the single-source responses, all measured along I's arrow.
:::

:::ans
**I = −2/11 A ≈ −0.182 A** (= book). The minus sign means the current actually flows into the + of the 10 V source.
:::

:::trap Never switch off a dependent source
Shorting 2V_{x} as if it were independent gives a wrong answer. It stays in; only its value changes from case to case.
:::

<div class="qhead"><span class="qn">A4 · Problem 5.4</span><span class="qt">Superposition · AC <span class="lvl light">new idea · labels on new steps only</span></span></div>

:::q
Determine the current in the capacitor branch by the superposition theorem.
:::

[[img:ck5_4|Z_{1} = 3 + j4 Ω (left branch); Z_{2} = 3 − j4 Ω (capacitor branch); current source 2∠90° A.|w=40]]

:::try
Which way does each source see Z_{1} and Z_{2}: in series, or in parallel?
:::

:::new Hint: what's new
- **Source with an angle:** 2∠90° A = j2 A. Convert to rectangular form before multiplying.
- **Polar form with a negative real part:** a calculator's tan⁻¹ lands in the wrong quadrant; add 180°.
:::

[[img:ck5_4s|(i) 4∠0° V alone · (ii) 2∠90° A alone|w=62]]

**Given:** 4∠0° V, 2∠90° A, Z_{1} = 3 + j4 Ω, Z_{2} = 3 − j4 Ω. **To find:** I in the capacitor branch (left → right).

**Case (i): 4∠0° V alone** (current source opened). Z_{1}, Z_{2} in series:

$$I′ = \frac{4∠0°}{(3 + j4) + (3 − j4)} = \frac{2}{3}∠0° A$$

**Case (ii): 2∠90° A alone** (voltage source shorted). Z_{1} ∥ Z_{2} across the source:

:::step
@how
$$2∠90° = j2,   I″ = j2 × \frac{3 + j4}{6} = \frac{j6 − 8}{6} = −\frac{4}{3} + j1 A$$
@what Convert the source to rectangular form, then use the current divider.
@why Multiplying j2 × (3 + j4) is one line in rectangular form; mixing polar and rectangular in one product is where slips happen. (A number at ∠90° is purely imaginary: 2∠90° = 0 + j2.)
:::

$$I = \frac{2}{3} − \frac{4}{3} + j1 = −\frac{2}{3} + j1 A$$

:::step
@how
$$|I| = \sqrt{(2/3)^{2} + 1} = 1.20 A,   θ = 180° − tan^{−1}(1.5) = 123.7°$$
@what Convert to polar, fixing the quadrant.
@why Real part negative, imaginary part positive, so the point is in the **2nd quadrant** (90° to 180°). A calculator's tan⁻¹(1 ÷ (−2/3)) returns −56.3°, a 4th-quadrant angle, because tan alone can't tell (−, +) from (+, −). Always read the signs first, then pick the angle.
:::

:::ans
**I = 1.2∠123.7° A** (= book)
:::

:::note Side note
Z_{1} + Z_{2} = 6 Ω is purely real (+j4 and −j4 cancel), which is why both cases are clean. Equal and opposite reactances in series act like a short: **series resonance**, met later.
:::

<div class="qhead"><span class="qn">A5 · Problem 5.5</span><span class="qt">Superposition · AC, DC + AC <span class="lvl light">new idea · labels on new steps only</span></span></div>

:::q
Find the current i_{0} using the superposition theorem, in each of circuits (a), (b) and (c).
:::

[[img:ck5_5||w=62]]

:::try
(a) is quick practice. In (b), stop and ask: what does an inductor look like to the 8 V **DC** source? In (c), redraw the circuit after switching off each source before you calculate anything.
:::

:::new Hint: what's new
- **(b) Two different frequencies (DC and 10 cos 4t).** Each case is solved **at its own frequency**: at DC (ω = 0), X_{L} = ωL = 0, so the **inductor is a short**; at ω = 4, it is j4 Ω. The two answers are added **in the time domain**, never as phasors, because phasors only add when they share one frequency.
- **(c) Redraw after switching off.** Once the voltage source is shorted, the 6 Ω and the current source both run to ground and everything becomes parallel.
:::

**(a) Given:** 5∠0° V, 2∠0° A, 4 Ω, −j2 Ω, j5 Ω. **To find:** i_{0} (down the capacitor).

[[img:ck5_5as|(i) voltage source alone · (ii) current source alone|w=78]]

$$5∠0° alone:  i_{0}′ = \frac{5}{4 − j2} = 1 + j0.5 A$$

$$2∠0° alone (j5 is in series with the source, so irrelevant):  i_{0}″ = 2 × \frac{4}{4 − j2} = 1.6 + j0.8 A$$

:::ans
**(a) i_{0} = 2.6 + j1.3 = 2.91∠26.57° A** (= book, 2.9∠26.56° A)
:::

**(b) Given:** 10 cos 4t V, 8 V DC, 4 Ω, 1 H, 2 Ω. **To find:** i_{0}(t) (down the inductor).

[[img:ck5_5bs|The book's sub-circuits (a) DC alone, (b) AC alone. In (a) the inductor must be read as a short circuit.|w=78]]

:::step
@how
8 V DC alone (AC source shorted): ω = 0, so X_{L} = ωL = 0 and the inductor is a wire.
$$i_{0}′ = \frac{8}{2} = 4 A  (the 4 Ω has 0 V across it)$$
@what Solve the DC case with the inductor replaced by a short.
@why An impedance belongs to one frequency. Each case is solved at **its own source's** ω, and for DC, ω = 0. With the inductor a wire, the middle node is at 0 V; the 4 Ω's other end is the shorted AC source, also 0 V, so it carries nothing. The 8 V drives the 2 Ω alone.
:::

**10 cos 4t alone** (8 V shorted; ω = 4 rad/s, Z_{L} = j4 Ω):

$$Z = 4 + \frac{j4 × 2}{2 + j4} = 5.6 + j0.8 Ω,   I = \frac{10∠0°}{Z} = 1.75 − j0.25 A$$

$$i_{0}″ = I × \frac{2}{2 + j4} = 0.25 − j0.75 = 0.791∠−71.57° A$$

:::step
@how
$$i_{0}(t) = 4 + 0.791 cos(4t − 71.57°) A$$
@what Turn each part into a time function, then add.
@why A phasor stands for a cosine at **one fixed ω**. The DC part doesn't rotate at all; the AC part rotates at 4 rad/s. Adding them as complex numbers would treat both as the same frequency, which they are not. In the time domain they add with no problem.
:::

:::ans
**(b) i_{0}(t) = 4 + 0.791 cos(4t − 71.57°) A**
:::

:::trap Book error in 5.5(b)
The book treats the inductor as j4 Ω for the **DC** source too, and then adds the DC and AC results as if both were phasors, printing 2.63∠−63.58° A. Both steps are wrong: at DC an inductor is a short, and quantities at different frequencies cannot be added as phasors. The answer above was confirmed by a node solve of each case.
:::

**(c) Given:** 10∠30° V, 2∠0° A, 8 Ω, −j2 Ω, j4 Ω, 6 Ω. **To find:** i_{0} (down the 8 Ω).

[[img:ck5_5cs1|(i) voltage source alone|w=48]]

**10∠30° V alone** (current source opened):

$$Z = 6 + j4 ∥ (8 − j2) = 6 + (1.882 + j3.529) = 7.882 + j3.529 Ω,   I = \frac{10∠30°}{Z} = 1.158∠5.88° A$$

$$i_{0}′ = I × \frac{j4}{(8 − j2) + j4} = I × \frac{j4}{8 + j2} = 0.562∠81.84° A$$

[[img:ck5_5cs2|(ii) current source alone, redrawn: the 6 Ω and the source now both go to ground|w=72]]

:::step
@how
2∠0° A alone (voltage source shorted). Redrawn: the source, the 6 Ω, the j4 and the (8 − j2) branch all join the same top node to ground. Z = j4 ∥ 6 = 1.846 + j2.769 Ω:
$$i_{0}″ = 2 × \frac{Z}{(8 − j2) + Z} = \frac{j24}{28 + j22} = 0.674∠51.84° A$$
@what Redraw after shorting the voltage source, merge j4 ∥ 6 into Z, then a current divider between Z and the (8 − j2) branch.
@why The shorted source turns the 6 Ω's right end into ground, which the original drawing hides. Once redrawn it is "a current source feeding parallel branches", a known current shared between paths, which is exactly a divider. Merging two branches first leaves a two-way split.
:::

$$i_{0} = (0.080 + j0.556) + (0.416 + j0.530) = 0.496 + j1.086 A$$

:::ans
**(c) i_{0} = 1.19∠65.45° A**
:::

:::trap Book error in 5.5(c)
The book prints 0.81∠39.38° A. Two slips: in case (i) it divides the current with (8 − j2)/(8 + j2) instead of j4/(8 + j2) (the current into a branch is set by the **other** branch's impedance); in case (ii) it expands (8 − j2)(3 + j2) + j12 as 12 + j11 instead of 28 + j22. The answer above was confirmed by a full node solve.
:::

<div class="qhead"><span class="qn">A6 · Problem 5.6</span><span class="qt">Superposition · two frequencies <span class="lvl light">new idea · labels on new steps only</span></span></div>

:::q
Find v_{0} using the superposition theorem.
:::

[[img:ck5_6||w=62]]

:::try
Work out X_{C} and X_{L} separately for ω = 5 and ω = 10 before drawing anything.
:::

:::new Hint: what's new
- **Reactances change with frequency.** X_{C} = \frac{1}{ωC} and X_{L} = ωL must be recomputed for each source's own ω.
- **Mixed sin and cos:** keep each term in the function it started with (sin for the voltage source, cos for the current source).
:::

[[img:ck5_6s|(i) voltage source alone, ω = 5 · (ii) current source alone, ω = 10|w=82]]

**Given:** 30 sin 5t V with 8 Ω; 0.2 F, 1 H, 20 cos 10t A. **To find:** v_{0}(t).

:::step
@how
30 sin 5t alone (ω = 5): X_{C} = \frac{1}{5 × 0.2} = 1 Ω → −j1 Ω;  X_{L} = 5 × 1 = 5 Ω → j5 Ω.
20 cos 10t alone (ω = 10): X_{C} = \frac{1}{10 × 0.2} = 0.5 Ω → −j0.5 Ω;  X_{L} = 10 Ω → j10 Ω.
@what Compute each reactance twice, once per source frequency.
@why The figure gives L and C, not impedances. An impedance only exists at a given ω, and here each case has a different ω, so each case gets its own impedances. Using one set for both cases is the common mistake.
:::

**30 sin 5t alone** (current source opened), node equation at the top:

$$\frac{30 − v′}{8} = \frac{v′}{−j1} + \frac{v′}{j5}  ⇒  v′ = \frac{30}{8(0.125 + j0.8)} = 4.631∠−81.12° V$$

**20 cos 10t alone** (voltage source shorted):

$$20 = v″(\frac{1}{8} + \frac{1}{−j0.5} + \frac{1}{j10}) = v″(0.125 + j1.9)  ⇒  v″ = 10.50∠−86.24° V$$

:::step
@how
$$v_{0}(t) = 4.631 sin(5t − 81.12°) + 10.50 cos(10t − 86.24°) V$$
@what Write each phasor back as a time function in its own original form (sin or cos), then add.
@why A phasor only records size and angle; the sin or cos it came from is up to you to remember. The first source was a sine, so its answer is a sine; the second was a cosine. Different ω, so add in time, as in 5.5(b).
:::

:::ans
**v_{0}(t) = 4.631 sin(5t − 81.12°) + 10.50 cos(10t − 86.24°) V**
:::

:::trap Book inconsistency in 5.6
The figure gives the current source as **20** cos 10t A, but the book's solution uses **2**∠0° A and prints 1.051 cos(10t − 86.24°) for the second term. The answer above follows the figure. If your source is 2 A, the second term is 1.051 cos(10t − 86.24°) V; the first term is unchanged.
:::

<div class="qhead"><span class="qn">A7 · Problem 5.7</span><span class="qt">Superposition · current-controlled source <span class="lvl light">new idea · labels on new steps only</span></span></div>

:::q
Find i_{0} and i from the circuit of the figure using the superposition theorem.
:::

[[img:ck5_7|2i_{0} is a current-controlled voltage source.|w=45]]

:::try
In each case, the dependent source's value is 2 × (that case's i_{0}). Write KCL at the middle node and one KVL around the outer loop.
:::

:::new Hint: what's new
- **Controlled by a current, not a voltage** (5.3 was voltage-controlled). The rule is the same: keep the source, and re-find its controlling current i_{0} in each case.
:::

[[img:ck5_7s|(i) 6 V alone · (ii) 1 A alone|w=82]]

**Given:** 6 V, 1 A, 1 Ω, 5 Ω, CCVS 2i_{0}. **To find:** i_{0}, i.

**6 V alone** (1 A opened): one loop, so i_{0}′ = i′.

$$6 = 1·i′ + 5·i′ + 2i_{0}′ = 8i′  ⇒  i′ = i_{0}′ = 0.75 A$$

**1 A alone** (6 V shorted):

:::step
@how
$$KCL at the middle node:  i″ = 1 + i_{0}″        outer KVL:  1·i_{0}″ + 5i″ + 2i_{0}″ = 0$$
@what KCL at the middle node (where the 1 A enters), then KVL around the outer loop, with the diamond worth 2i_{0}″.
@why Same two moves as 5.3. KCL where the known source current enters ties the two unknown currents together. For the second equation, take the loop that **avoids the 1 A source**: the voltage across a current source is unknown, so a loop through it would add a third unknown. The diamond is valued with **this case's** controlling current, i_{0}″.
:::

$$3i_{0}″ + 5(1 + i_{0}″) = 0  ⇒  8i_{0}″ = −5  ⇒  i_{0}″ = −0.625 A,   i″ = 0.375 A$$

:::ans
**i = 0.75 + 0.375 = 1.125 A,  i_{0} = 0.75 − 0.625 = 0.125 A**
:::

:::trap Book error in 5.7
The book sets up the same equation, then solves 8i_{0}″ = −5 as i_{0}″ = −5/4 = −1.25 A, and prints i = 0.5 A, i_{0} = −0.5 A. The correct value is −5/8 = −0.625 A. Direct check: KCL i = i_{0} + 1 and KVL 6 − i_{0} − 5i = 2i_{0} give i_{0} = 1/8 A ✓.
:::

<div class="qhead"><span class="qn">A8 · Problem 5.8</span><span class="qt">Superposition · AC <span class="lvl plain">practice · How only</span></span></div>

:::q
Using the superposition theorem, calculate the current through the (2 + j3) Ω impedance branch.
:::

[[img:ck5_8||w=62]]

:::try
Series-parallel reduction, twice. Watch which way the branch current flows in case II.
:::

[[img:ck5_8s1|Case I: 30 V alone|w=62]]

**Case I: 30 V alone** (20 V shorted). Branch: Z_{b} = (2 + j3) + (6 ∥ 4) = 4.4 + j3 Ω.

$$Z = 5 + \frac{Z_{b} × j5}{Z_{b} + j5} = 6.32 + j2.60 Ω,   I′ = \frac{30}{Z} = 4.06 − j1.67 A,   i′ = I′ × \frac{j5}{Z_{b} + j5} = 2.389 + j0.270 A$$

[[img:ck5_8s2|Case II: 20 V alone|w=62]]

**Case II: 20 V alone** (30 V shorted). Branch: Z_{a} = (5 ∥ j5) + 2 + j3 = 4.5 + j5.5 Ω.

$$Z = 4 + \frac{6Z_{a}}{Z_{a} + 6} = 7.31 + j1.41 Ω,   I″ = \frac{20}{Z} = 2.638 − j0.509 A$$

$$i″ = −I″ × \frac{6}{Z_{a} + 6} = −1.063 + j0.848 A  (it flows right → left, against i)$$

:::ans
**i = i′ + i″ = 1.326 + j1.117 = 1.73∠40.13° A** (= book)
:::

<div class="qhead"><span class="qn">A9 · Problem 5.9</span><span class="qt">Superposition · three sources, open terminals <span class="lvl light">new idea · labels on new steps only</span></span></div>

:::q
Using the superposition theorem, find V_{AB}.
:::

[[img:ck5_9||w=52]]

:::try
Three sources, so three cases. Nothing is connected across A–B, so no current leaves at A or B.
:::

:::new Hint: what's new
- **Three sources:** same method, one more case.
- **Open terminals:** V_{AB} is the voltage across a gap. With no load, the only path is the loop 4 Ω + 2 Ω + 6 Ω, and V_{AB} can be read along either side of that loop.
- **Source transformation inside a case:** 2 A in parallel with 4 Ω equals an 8 V source in series with 4 Ω, which makes case III a single loop.
:::

[[img:ck5_9s1|Case I: 2 V alone|w=52]]

:::step
@how
$$Case I (2 V):  I′ = \frac{2}{4 + 2 + 6} = \frac{1}{6} A,   V_{AB}′ = 6I′ = 1 V$$
@what One loop current, then V_{AB} read across the top 6 Ω (its 4 V is switched off).
@why Nothing is connected at A or B, so no current leaves there: the circuit is a single loop. V_{AB} is the voltage between two points, and it is the same along any path from A to B. Pick the path you know best: in this case the top path is just the 6 Ω. The current runs through it from A's side to B's side, so A is higher and the sign is +.
:::

[[img:ck5_9s2|Case II: 4 V alone|w=52]]

$$Case II (4 V):  I″ = \frac{4}{12} = \frac{1}{3} A,   V_{AB}″ = −(4 + 2)I″ = −2 V  (bottom path; current flows B → A along it)$$

[[img:ck5_9s3|Case III: 2 A alone|w=50]]

[[img:ck5_9s4|Case III after source transformation: 2 A ∥ 4 Ω → 8 V in series with 4 Ω|w=52]]

:::step
@how
2 A ∥ 4 Ω → 8 V in series with 4 Ω, then one loop:
$$Case III (2 A):  I‴ = \frac{8}{12} = \frac{2}{3} A,   V_{AB}‴ = −6I‴ = −4 V$$
@what Source-transform the 2 A and its 4 Ω, then Ohm's law on the single loop.
@why A current source in parallel with a resistor acts on the rest of the circuit exactly like V = IR in series with the same R. Converting it removes the only node where current splits, so the case becomes one loop (one equation, no KCL needed). Current now runs through the 6 Ω from B's side to A's side, hence the minus.
:::

:::ans
**V_{AB} = 1 − 2 − 4 = −5 V** (= book)
:::

<div class="qhead"><span class="qn">A10 · Problem 5.10</span><span class="qt">Superposition · dependent source, three sources <span class="lvl light">new idea · labels on new steps only</span></span></div>

:::q
Find the current i in the circuit shown using the superposition theorem.
:::

[[img:ck5_10|4i is a current-controlled voltage source; i flows down the 3 Ω.|w=48]]

:::try
Case I is one loop. In case II, look for a resistor in series with the dependent source.
:::

:::new Hint: what's new
- **Source transformation works on dependent sources too.** In case II, the 4i source in series with the 2 Ω becomes a dependent current source 4i/2 = **2i** in parallel with 2 Ω.
- **A current source inside a mesh fixes that mesh current** (case III: the 8 A source sets the mesh difference I − 8).
:::

[[img:ck5_10s1|Case I: 10 V alone|w=36]]

**Case I: 10 V alone** (2 A and 8 A opened). Loop current i′ clockwise:

$$−4i′ + 3i′ − 10 + 2i′ = 0  ⇒  i′ = 10 A$$

[[img:ck5_10s2|Case II: 2 A alone|w=34]]

[[img:ck5_10s3|Case II after converting 4i″ + 2 Ω into 2i″ ∥ 2 Ω|w=48]]

:::step
@how
4i″ in series with 2 Ω → 2i″ in parallel with 2 Ω. Now a total of (2 + 2i″) splits between 2 Ω and 3 Ω:
$$i″ = \frac{2}{2 + 3}(2 + 2i″)  ⇒  5i″ = 4 + 4i″  ⇒  i″ = 4 A$$
@what Source-transform the dependent source with its series 2 Ω, then a current divider between 2 Ω and 3 Ω.
@why With the 8 A opened, the left node has only two elements, the 2 Ω and the diamond, so they are in series and can be transformed (V ÷ R = 4i″ ÷ 2). Everything then hangs between the same two nodes, so the whole case is one divider. The value stays written in i″, the **controlling** current; it is solved for at the end.
:::

[[img:ck5_10s4|Case III: 8 A alone|w=44]]

:::step
@how
Mesh current I clockwise in the inner loop; the 8 A is the outer mesh's current, so the shared 3 Ω carries i‴ = I − 8:
$$−4i‴ + 3(I − 8) + 2I = 0,  I = i‴ + 8  ⇒  −4i‴ + 3i‴ + 2i‴ + 16 = 0  ⇒  i‴ = −16 A$$
@what Mesh analysis with one unknown mesh current; the 8 A fixes the other.
@why A current source sitting alone on the outside edge of a mesh **is** that mesh's current: 8 A, known, so no equation is needed for it. In an element shared by two meshes, the current is the difference of the two mesh currents. That leaves one KVL for one unknown.
:::

:::ans
**i = 10 + 4 − 16 = −2 A** (= book)
:::

<div class="qhead"><span class="qn">A11 · Problem 5.11</span><span class="qt">Superposition · dependent source, three sources <span class="lvl plain">practice · How only</span></span></div>

:::q
Using the superposition theorem, determine V_{1}, the voltage across the 3 Ω resistor.
:::

[[img:ck5_11|The figure prints no value on the bottom-middle voltage source; the book's solution uses 10 V.|w=36]]

:::try
Three cases again; the dependent source 4i stays in all three. Case I has a supermesh around the 8 A source.
:::

[[img:ck5_11s1|Case I: 8 A alone · Case II: 2 A alone|w=80]]

**Case I: 8 A alone.** Supermesh KVL and KCL at node x:

$$3i′ + 2i_{1} − 4i′ = 0 ⇒ i_{1} = \frac{i′}{2};   i_{1} = 8 + i′ ⇒ \frac{i′}{2} = 8 + i′ ⇒ i′ = −16 A,  V_{1}′ = 3i′ = −48 V$$

**Case II: 2 A alone.** Mesh current i_{2} on the left; the 3 Ω carries i″ = i_{2} + 2:

$$3(i_{2} + 2) + 2i_{2} − 4i″ = 0 ⇒ 5i_{2} + 6 − 4(i_{2} + 2) = 0 ⇒ i_{2} = 2 A,  i″ = 4 A,  V_{1}″ = 12 V$$

[[img:ck5_11s2|Case III: 10 V alone|w=28]]

**Case III: 10 V alone.** One loop:

$$3i‴ − 10 + 2i‴ − 4i‴ = 0 ⇒ i‴ = 10 A,  V_{1}‴ = 30 V$$

:::ans
**V_{1} = −48 + 12 + 30 = −6 V** (= book)
:::

<div class="qhead"><span class="qn">A12 · Problem 5.12</span><span class="qt">Superposition · AC <span class="lvl light">new idea · labels on new steps only</span></span></div>

:::q
Calculate the current through the impedance (3 + j4) Ω using the superposition theorem.
:::

[[img:ck5_12||w=56]]

:::try
Two voltage sources, same frequency. Get each case's current as a fraction before simplifying.
:::

:::new Hint: what's new
- **The two contributions can cancel.** Here they come out equal and opposite, so the branch current is zero. A zero answer is not an error; check it with one node equation.
:::

[[img:ck5_12s1|10∠90° V alone|w=50]]

$$10∠90° alone:  I = \frac{j10}{5 + \frac{(3 + j4)j5}{3 + j9}} = \frac{j10(3 + j9)}{−5 + j60},   I′ = I × \frac{j5}{3 + j9} = \frac{−10}{−1 + j12} = 0.069 + j0.828 A$$

[[img:ck5_12s2|10∠0° V alone|w=50]]

$$10∠0° alone:  I = \frac{10}{j5 + \frac{5(3 + j4)}{8 + j4}} = \frac{10(8 + j4)}{−5 + j60},   I″ = I × \frac{5}{8 + j4} = \frac{10}{−1 + j12} = −0.069 − j0.828 A$$

:::step
@how
$$I = I′ + I″ = 0$$
Check, node equation at the top node: V(\frac{1}{5} + \frac{1}{3 + j4} + \frac{1}{j5}) = \frac{j10}{5} + \frac{10}{j5} = j2 − j2 = 0, so V = 0 ✓.
@what Add, then confirm the zero with one node equation.
@why A zero can come from a real cancellation or from a sign slip, and the sum alone can't tell which. One independent check (nodal, all sources on) settles it in a line. Here each source pushes exactly j2 A into the node, from opposite sides.
:::

:::ans
**I = 0 A** (= book)
:::

<div class="qhead"><span class="qn">A13 · Problem 5.13</span><span class="qt">Superposition · AC <span class="lvl plain">practice · How only</span></span></div>

:::q
Using the superposition theorem, determine the current in the 4 Ω resistor.
:::

[[img:ck5_13|The book labels the current source "20∠0° V"; it is a current source (arrow), 20∠0° A.|w=62]]

:::try
Combine the parallel pairs first: 5 Ω ∥ j2 Ω and 2 Ω ∥ −j2 Ω.
:::

[[img:ck5_13s1|Case I: 20∠0° A alone|w=58]]

**Case I: 20∠0° A alone** (voltage source shorted). Z_{1} = 5 ∥ j2 = 0.690 + j1.724 Ω; Z_{2} = 2 ∥ (−j2) = 1 − j1 Ω.

$$I_{1} = 20 × \frac{Z_{1}}{Z_{1} + 4 + Z_{2}} = 3.145 + j5.660 A  (left → right)$$

[[img:ck5_13s2|Case II: 100∠90° V alone|w=58]]

**Case II: 100∠90° V alone** (current source opened). (Z_{1} + 4) ∥ (−j2) = 0.850 − j1.950 Ω:

$$I_{s} = \frac{j100}{2 + (0.850 − j1.950)} = −16.35 + j23.90 A,   V_{B} = I_{s}(0.850 − j1.950) = 32.70 + j52.20 V$$

$$I_{2} = \frac{V_{B}}{Z_{1} + 4} = 9.748 + j7.547 A  (right → left)$$

:::ans
**I = I_{1} − I_{2} = −6.604 − j1.887 = 6.87∠−164.05° A (left → right)**, i.e. 6.87 A flowing right → left (= book, 6.89∠−163.67° A, to rounding)
:::

<div class="qhead"><span class="qn">A14 · Problem 5.14</span><span class="qt">Superposition · dependent source <span class="lvl plain">practice · How only</span></span></div>

:::q
Find I in the figure using the superposition theorem.
:::

[[img:ck5_14|5V_{x} is a voltage-controlled voltage source; V_{x} is across the 2 Ω (+ at top).|w=40]]

:::try
Same idea as 5.3. In case II, the 4 V short joins the two top-left nodes; write one KCL there.
:::

[[img:ck5_14s1|Case I: 4 V alone|w=46]]

**Case I: 4 V alone** (2 A opened). One loop; I′ flows up the 2 Ω, so V_{x}′ = −2I′:

$$−4 + 3I′ + 5V_{x}′ − V_{x}′ = 0 ⇒ 3I′ + 4(−2I′) = 4 ⇒ I′ = −0.8 A$$

[[img:ck5_14s2|Case II: 2 A alone|w=40]]

**Case II: 2 A alone** (4 V shorted). KCL at the top node (voltage V_{x}″):

$$2 = \frac{V_{x}″}{2} + \frac{V_{x}″ − 5V_{x}″}{3} ⇒ V_{x}″ = −2.4 V,   I″ = \frac{V_{x}″ − 5V_{x}″}{3} = 3.2 A$$

:::ans
**I = −0.8 + 3.2 = 2.4 A** (= book)
:::
