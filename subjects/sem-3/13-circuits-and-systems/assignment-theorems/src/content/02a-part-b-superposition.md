# Part B · Sadiku (unsolved problems)

<div class="sub">Alexander & Sadiku, <i>Fundamentals of Electric Circuits</i> 5e, ch. 4 "Circuit Theorems": practice problems, then end-of-chapter problems</div>

[[map:Part A: every method, solved (done) > Part B: same theorems, your turn > Superposition §4.3 > Source transformation §4.4 > Thevenin / Norton §4.5–4.6 > Max power §4.8|here=3]]

**Where this sits.** Part A taught every method on solved problems. Sadiku's problems are unsolved, so they are practice: the solutions here are compact, and an orange hint appears only when a problem adds something Part A did not show.

**Answers.** Practice problems print their answer beside the question ("= book"). End-of-chapter problems have answers only for odd numbers, in Appendix D ("= App. D"). Every answer here, odd or even, was checked by solving the full circuit with all sources on, and every superposition part was checked to add up to it.

## A · Superposition (§4.3)

<div class="qhead"><span class="qn">B1 · Practice Problem 4.3</span><span class="qt">Superposition · DC <span class="lvl plain">practice</span></span></div>

:::q
Using the superposition theorem, find v_{o} in the circuit of Fig. 4.8.
:::

[[img:sd_pp4_3|Fig. 4.8|w=56]]

**5 A alone** (12 V shorted). From the middle node the 5 A sees 3 + 2 = 5 Ω and 5 Ω, so it splits 2.5 A each way:

$$v_{o}′ = 2.5 × 2 = 5 V$$

**12 V alone** (5 A opened). 5 Ω, 3 Ω and 2 Ω in series:

$$i = \frac{12}{5 + 3 + 2} = 1.2 A  ⇒  v_{o}″ = 1.2 × 2 = 2.4 V$$

:::ans
**v_{o} = 5 + 2.4 = 7.4 V** (= book)
:::

<div class="qhead"><span class="qn">B2 · Practice Problem 4.4</span><span class="qt">Superposition · dependent current source <span class="lvl plain">practice</span></span></div>

:::q
Use superposition to find v_{x} in the circuit of Fig. 4.11.
:::

[[img:sd_pp4_4|Fig. 4.11; 0.1v_{x} is a voltage-controlled current source.|w=56]]

:::try
The dependent source stays in both cases. One KCL at the v_{x} node per case.
:::

**25 V alone** (5 A opened):

$$\frac{25 − v_{x}′}{20} + 0.1v_{x}′ = \frac{v_{x}′}{4}  ⇒  1.25 = 0.2v_{x}′  ⇒  v_{x}′ = 6.25 V$$

**5 A alone** (25 V shorted):

$$5 + 0.1v_{x}″ = \frac{v_{x}″}{4} + \frac{v_{x}″}{20}  ⇒  5 = 0.2v_{x}″  ⇒  v_{x}″ = 25 V$$

:::ans
**v_{x} = 6.25 + 25 = 31.25 V** (= book)
:::

<div class="qhead"><span class="qn">B3 · Practice Problem 4.5</span><span class="qt">Superposition · three sources <span class="lvl plain">practice</span></span></div>

:::q
Find I in the circuit of Fig. 4.14 using the superposition principle.
:::

[[img:sd_pp4_5|Fig. 4.14|w=62]]

With the other sources off, the loop is always 6 + 2 + 8 = 16 Ω.

$$8 V alone:  I′ = \frac{8}{16} = 0.5 A        6 V alone (it opposes I):  I″ = −\frac{6}{16} = −0.375 A$$

$$2 A alone (2 A ∥ 2 Ω → 4 V in series with 2 Ω, pushing to the right):  I‴ = \frac{4}{16} = 0.25 A$$

:::ans
**I = 0.5 − 0.375 + 0.25 = 0.375 A = 375 mA** (= book)
:::

<div class="qhead"><span class="qn">B4 · Problem 4.8</span><span class="qt">Superposition · one-node circuit <span class="lvl light">new idea</span></span></div>

:::q
Using superposition, find V_{o} in the circuit of Fig. 4.76. Check with PSpice or MultiSim.
:::

[[img:sd4_8|Fig. 4.76|w=52]]

:::new Hint: what's new
- **One-node shortcut.** When every branch meets at one node, write one KCL at that node in each case instead of chaining dividers. Here the branches from V_{o} are 4 + 5 = 9 Ω, 3 Ω (+ 9 V) and 1 Ω (+ 3 V).
:::

**9 V alone** (3 V shorted):

$$\frac{V_{o}′}{9} + \frac{V_{o}′ − 9}{3} + \frac{V_{o}′}{1} = 0  ⇒  \frac{13}{9}V_{o}′ = 3  ⇒  V_{o}′ = \frac{27}{13} V$$

**3 V alone** (9 V shorted):

$$\frac{V_{o}″}{9} + \frac{V_{o}″}{3} + \frac{V_{o}″ − 3}{1} = 0  ⇒  \frac{13}{9}V_{o}″ = 3  ⇒  V_{o}″ = \frac{27}{13} V$$

:::ans
**V_{o} = \frac{54}{13} = 4.154 V** (even problem; full node solve agrees. The book's PSpice/MultiSim check is replaced by that solve.)
:::

<div class="qhead"><span class="qn">B5 · Problem 4.9</span><span class="qt">Superposition + linearity <span class="lvl light">new idea</span></span></div>

:::q
Given that I = 4 amps when V_{s} = 40 volts and I_{s} = 4 amps and I = 1 amp when V_{s} = 20 volts and I_{s} = 0, use superposition and linearity to determine the value of I when V_{s} = 60 volts and I_{s} = −2 amps.
:::

[[img:sd4_9|Fig. 4.77 (no resistor values given)|w=52]]

:::new Hint: what's new
- **Superposition without the circuit values.** In a linear circuit any response is a weighted sum of the sources, I = aV_{s} + bI_{s}. The two measurements give two equations for a and b.
:::

$$I_{s} = 0:  1 = 20a  ⇒  a = 0.05$$

$$4 = 40(0.05) + 4b  ⇒  b = 0.5$$

$$I = 0.05 × 60 + 0.5 × (−2) = 3 − 1 = 2 A$$

:::ans
**I = 2 A** (= App. D)
:::

<div class="qhead"><span class="qn">B6 · Problem 4.10</span><span class="qt">Superposition · design problem <span class="lvl light">new idea</span></span></div>

:::q
Using Fig. 4.78, design a problem to help other students better understand superposition. Note, the letter k is a gain you can specify to make the problem easier to solve but must not be zero.
:::

:::new Hint: what's new
- **Design problem:** there is no single answer. Choose values, then solve your own problem. Below is one complete design; any other non-zero choice is equally valid.
:::

[[img:sd4_10|Fig. 4.78|w=40]]

**One design.** In Fig. 4.78 (V in series with R and the dependent source kV_{ab}, current source I across a–b), take **V = 12 V, R = 4 Ω, I = 3 A, k = 2**, and ask: *use superposition to find V_{ab}.*

**Solution.** Terminals a–b are open, so the current I must return through R and the source V: the series current from V towards a is −I. KVL around the loop: V − R(−I) − kV_{ab} = V_{ab}, so in general V_{ab} = \frac{V + RI}{1 + k}.

$$12 V alone (I = 0):  V_{ab}′ = \frac{12}{1 + 2} = 4 V        3 A alone (V = 0):  V_{ab}″ = \frac{4 × 3}{1 + 2} = 4 V$$

:::ans
**(this design) V_{ab} = 4 + 4 = 8 V** (design problem; the book lists "multiple answers")
:::

<div class="qhead"><span class="qn">B7 · Problem 4.11</span><span class="qt">Superposition · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Use the superposition principle to find i_{o} and v_{o} in the circuit of Fig. 4.79.
:::

[[img:sd4_11|Fig. 4.79; 4i_{o} is a current-controlled current source.|w=65]]

Let the middle node be M and the left node A. KCL at M in either case: 5i_{o} flows on through the 20 Ω.

**6 A alone** (30 V shorted): 5i_{o} = V_{M}/20 ⇒ V_{M} = 100i_{o}, V_{A} = V_{M} + 10i_{o} = 110i_{o}.

$$KCL at A:  6 = \frac{110i_{o}}{40} + i_{o} = 3.75i_{o}  ⇒  i_{o}′ = 1.6 A,   v_{o}′ = 16 V$$

**30 V alone** (6 A opened; the right end of the 20 Ω is at −30 V): V_{M} = 100i_{o} − 30, V_{A} = 110i_{o} − 30.

$$0 = \frac{110i_{o} − 30}{40} + i_{o}  ⇒  3.75i_{o} = 0.75  ⇒  i_{o}″ = 0.2 A,   v_{o}″ = 2 V$$

:::ans
**i_{o} = 1.8 A, v_{o} = 18 V** (= App. D to rounding: 1.799 A, 17.99 V)
:::

<div class="qhead"><span class="qn">B8 · Problem 4.12</span><span class="qt">Superposition · three sources <span class="lvl plain">practice</span></span></div>

:::q
Determine v_{o} in the circuit of Fig. 4.80 using the superposition principle.
:::

[[img:sd4_12|Fig. 4.80; the 2 A pushes current from the right node B into the left node A.|w=60]]

**12 V alone.** B sees 12 ∥ 4 = 3 Ω; A sees 3 ∥ (5 + 3) = \frac{24}{11} Ω.

$$V_{A} = 12 × \frac{24/11}{6 + 24/11} = 3.2 V,   V_{B} = 3.2 × \frac{3}{8} = 1.2 V,   v_{o}′ = 2 V$$

**19 V alone.** A sees 6 ∥ 3 = 2 Ω; B sees 12 ∥ (5 + 2) = \frac{84}{19} Ω.

$$V_{B} = 19 × \frac{84/19}{4 + 84/19} = 9.975 V,   V_{A} = 9.975 × \frac{2}{7} = 2.85 V,   v_{o}″ = −7.125 V$$

**2 A alone.** A has 2 Ω to ground, B has 3 Ω; the 2 A splits equally between the 5 Ω and the 2 + 3 = 5 Ω path, so 1 A flows A → B in the 5 Ω:

$$v_{o}‴ = 5 × 1 = 5 V$$

:::ans
**v_{o} = 2 − 7.125 + 5 = −0.125 V** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B9 · Problem 4.13</span><span class="qt">Superposition · three sources <span class="lvl plain">practice</span></span></div>

:::q
Use superposition to find v_{o} in the circuit of Fig. 4.81.
:::

[[img:sd4_13|Fig. 4.81|w=60]]

**2 A alone.** It splits between 10 Ω and 8 + 5 = 13 Ω:

$$i_{5Ω} = 2 × \frac{10}{23} = \frac{20}{23} A,   v_{o}′ = 5 × \frac{20}{23} = \frac{100}{23} V$$

**12 V alone.** One loop of 10 + 8 + 5 = 23 Ω; clockwise current (L → 8 Ω → source → 5 Ω):

$$i = −\frac{12}{23} A,   v_{o}″ = 5i = −\frac{60}{23} V$$

**4 A alone.** It enters the right node and returns to the left node through 8 Ω or through 5 + 10 = 15 Ω:

$$i_{5Ω} = 4 × \frac{8}{23} = \frac{32}{23} A,   v_{o}‴ = \frac{160}{23} V$$

:::ans
**v_{o} = \frac{100 − 60 + 160}{23} = \frac{200}{23} = 8.696 V** (= App. D)
:::

<div class="qhead"><span class="qn">B10 · Problem 4.14</span><span class="qt">Superposition · three sources <span class="lvl plain">practice</span></span></div>

:::q
Apply the superposition principle to find v_{o} in the circuit of Fig. 4.82.
:::

[[img:sd4_14|Fig. 4.82; the left rail is the top of the 20 V source, the right rail is the top of the 3 Ω.|w=50]]

**20 V alone.** Between the rails: 6 Ω ∥ (4 + 2) Ω = 3 Ω, then 3 Ω to ground: v_{o}′ = 20 × \frac{3}{6} = 10 V.

**2 A alone** (it pulls 2 A out of the right rail). The right rail sees 3 ∥ 6 ∥ 6 = 1.5 Ω: v_{o}″ = −2 × 1.5 = −3 V.

**1 A alone.** From the middle node: 4 Ω to ground, or 2 Ω + (3 ∥ 6 = 2 Ω). Current towards the right rail = 1 × \frac{4}{4 + 4} = 0.5 A: v_{o}‴ = 0.5 × 2 = 1 V.

:::ans
**v_{o} = 10 − 3 + 1 = 8 V** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B11 · Problem 4.15</span><span class="qt">Superposition · power <span class="lvl plain">practice</span></span></div>

:::q
For the circuit in Fig. 4.83, use superposition to find i. Calculate the power delivered to the 3-Ω resistor.
:::

[[img:sd4_15|Fig. 4.83; the 16 V has its + at the bottom.|w=55]]

**20 V alone.** The top node sees 4 Ω (1 + 3) and 4 Ω (right): 2 Ω. V_{T} = 20 × \frac{2}{2 + 2} = 10 V, i′ = \frac{10}{4} = 2.5 A.

**2 A alone.** The 2 A enters the 3 Ω node and returns to the top node either through 1 Ω or through 3 Ω + (2 ∥ 4 = \frac{4}{3} Ω): i″ = 2 × \frac{1}{1 + 13/3} = 0.375 A.

**16 V alone.** The bottom of the right 4 Ω sits at −16 V; the top node sees 2 ∥ 4 = \frac{4}{3} Ω: V_{T} = −16 × \frac{4/3}{4/3 + 4} = −4 V, i‴ = −1 A.

$$i = 2.5 + 0.375 − 1 = 1.875 A,   P_{3Ω} = i^{2} × 3 = 10.55 W$$

:::ans
**i = 1.875 A, P = 10.55 W** (= App. D)
:::

:::trap Power does not superpose
Adding the three partial powers (18.75 + 0.42 + 3 W) gives a wrong answer. Add the currents first, then square.
:::

<div class="qhead"><span class="qn">B12 · Problem 4.16</span><span class="qt">Superposition · three sources <span class="lvl plain">practice</span></span></div>

:::q
Given the circuit in Fig. 4.84, use superposition to obtain i_{0}.
:::

[[img:sd4_16|Fig. 4.84; the 4 A pushes current from the node between 3 Ω and 2 Ω into the node above the 10 Ω.|w=60]]

**12 V alone.** Seen from the 4 Ω: 10 ∥ (3 + 2 + 5) = 5 Ω, so i_{0}′ = \frac{12}{4 + 5} = \frac{4}{3} A.

**2 A alone.** From its node: 5 Ω to ground, or 2 + 3 + (4 ∥ 10 = \frac{20}{7}) Ω. Current towards the 10 Ω node = 2 × \frac{5}{5 + 5 + 20/7} = \frac{7}{9} A, so V_{A} = \frac{7}{9} × \frac{20}{7} = \frac{20}{9} V and i_{0}″ = −\frac{V_{A}}{4} = −\frac{5}{9} A.

**4 A alone.** It returns from A to B through 3 Ω, or through \frac{20}{7} + 5 + 2 = \frac{69}{7} Ω. Current down the ground path = 4 × \frac{3}{3 + 69/7} = \frac{14}{15} A, so V_{A} = \frac{14}{15} × \frac{20}{7} = \frac{8}{3} V and i_{0}‴ = −\frac{2}{3} A.

:::ans
**i_{0} = \frac{4}{3} − \frac{5}{9} − \frac{2}{3} = \frac{1}{9} = 0.111 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B13 · Problem 4.17</span><span class="qt">Superposition · three sources <span class="lvl plain">practice</span></span></div>

:::q
Use superposition to obtain v_{x} in the circuit of Fig. 4.85. Check your result using PSpice or MultiSim.
:::

[[img:sd4_17|Fig. 4.85; A is the node after the 30 Ω, B the node after the 10 Ω.|w=70]]

**90 V alone.** B sees 30 ∥ 20 = 12 Ω; A sees 60 ∥ (10 + 12) = 16.10 Ω.

$$V_{A} = 90 × \frac{16.10}{30 + 16.10} = 31.43 V,   v_{x}′ = V_{A} × \frac{10}{22} = 14.29 V$$

**6 A alone.** B sees 12 Ω ∥ (10 + 30 ∥ 60) = 12 ∥ 30 = \frac{60}{7} Ω.

$$V_{B} = 6 × \frac{60}{7} = 51.43 V,   V_{A} = V_{B} × \frac{20}{30} = 34.29 V,   v_{x}″ = −17.14 V$$

**40 V alone.** B sees 30 ∥ (10 + 20) = 15 Ω.

$$V_{B} = 40 × \frac{15}{20 + 15} = 17.14 V,   V_{A} = V_{B} × \frac{20}{30} = 11.43 V,   v_{x}‴ = −5.71 V$$

:::ans
**v_{x} = 14.29 − 17.14 − 5.71 = −8.571 V** (= App. D)
:::

<div class="qhead"><span class="qn">B14 · Problem 4.18</span><span class="qt">Superposition · dependent current source <span class="lvl plain">practice</span></span></div>

:::q
Use superposition to find V_{o} in the circuit of Fig. 4.86.
:::

[[img:sd4_18|Fig. 4.86; 0.5V_{o} is a voltage-controlled current source from node A to the output node.|w=52]]

KCL at the output node (true in every case): (V_{A} − V_{o}) + 0.5V_{o} = \frac{V_{o}}{4} ⇒ V_{A} = 0.75V_{o}.

**10 V alone** (2 A opened), KCL at A:

$$\frac{10 − V_{A}}{2} = (V_{A} − V_{o}) + 0.5V_{o}  ⇒  5 = 1.5V_{A} − 0.5V_{o}$$

$$5 = 1.125V_{o} − 0.5V_{o} = 0.625V_{o}  ⇒  V_{o}′ = 8 V$$

**2 A alone** (10 V shorted), KCL at A:

$$2 − \frac{V_{A}}{2} = V_{A} − 0.5V_{o}  ⇒  2 = 0.625V_{o}  ⇒  V_{o}″ = 3.2 V$$

:::ans
**V_{o} = 8 + 3.2 = 11.2 V** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B15 · Problem 4.19</span><span class="qt">Superposition · floating dependent source <span class="lvl light">new idea</span></span></div>

:::q
Use superposition to solve for v_{x} in the circuit of Fig. 4.87.
:::

[[img:sd4_19|Fig. 4.87; 4i_{x} sits in the bottom wire, + on the right.|w=55]]

:::new Hint: what's new
- **A dependent source in the return wire.** The bottom wire is split into two nodes that differ by 4i_{x}. Take the left bottom node as ground; then the right bottom node is at 4i_{x}, and v_{x} = V_{top} − 4i_{x}.
:::

With i_{x} = V_{top}/2: v_{x} = V_{top} − 2V_{top} = −V_{top}. KCL at the top node (sources entering = currents leaving):

$$I_{in} = \frac{V_{top}}{2} + \frac{v_{x}}{8} = \frac{V_{top}}{2} − \frac{V_{top}}{8} = \frac{3}{8}V_{top}$$

$$6 A alone:  6 = \frac{3}{8}V_{top}  ⇒  V_{top} = 16 V,   v_{x}′ = −16 V$$

$$4 A alone:  4 = \frac{3}{8}V_{top}  ⇒  V_{top} = 10.67 V,   v_{x}″ = −10.67 V$$

:::ans
**v_{x} = −16 − 10.67 = −26.67 V** (= App. D)
:::
