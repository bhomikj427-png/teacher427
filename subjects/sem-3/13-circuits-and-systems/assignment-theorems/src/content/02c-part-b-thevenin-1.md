## C · Thevenin's and Norton's theorems (§4.5–4.6)

[[map:Source transformation (done) > Thevenin / Norton: V_{oc}, I_{sc}, R_{th} > Max power (next)|here=2]]

**Where this sits.** Part A, section B taught the method and its three R_{th} cases (switch off and combine; V_{oc}/I_{sc} or test source with dependent sources; test source only when there is no independent source). These are practice. I_{sc} is always counted **from a to b through the short**, so R_{th} = V_{oc}/I_{sc} keeps its sign.

<div class="qhead"><span class="qn">B31 · Practice Problem 4.8</span><span class="qt">Thevenin · DC <span class="lvl plain">practice</span></span></div>

:::q
Using Thevenin's theorem, find the equivalent circuit to the left of the terminals in the circuit of Fig. 4.30. Then find I.
:::

[[img:sd_pp4_8|Fig. 4.30; the 1 Ω is the load.|w=48]]

$$12 V/6 Ω + 2 A  ⇒  (2 + 2) A ∥ 6 Ω  ⇒  24 V behind 6 Ω;   + 6 Ω  ⇒  24 V behind 12 Ω$$

$$V_{th} = 24 × \frac{4}{12 + 4} = 6 V,   R_{th} = 12 ∥ 4 = 3 Ω,   I = \frac{6}{3 + 1} = 1.5 A$$

:::ans
**V_{th} = 6 V, R_{th} = 3 Ω, I = 1.5 A** (= book)
:::

<div class="qhead"><span class="qn">B32 · Practice Problem 4.9</span><span class="qt">Thevenin · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent circuit of the circuit in Fig. 4.34 to the left of the terminals.
:::

[[img:sd_pp4_9|Fig. 4.34; 1.5I_{x} is a current-controlled current source.|w=48]]

**V_{oc}.** I_{x} flows through 3 Ω and 4 Ω, so I_{x} = V_{a}/4 and V_{M} = V_{a} + 3I_{x} = 1.75V_{a}. KCL at M:

$$\frac{6 − 1.75V_{a}}{5} + 1.5I_{x} = I_{x}  ⇒  6 − 1.75V_{a} = −0.625V_{a}  ⇒  V_{oc} = 5.333 V$$

**I_{sc}.** V_{a} = 0, so I_{x} = V_{M}/3:

$$\frac{6 − V_{M}}{5} = −0.5 × \frac{V_{M}}{3}  ⇒  V_{M} = 36 V,   I_{sc} = I_{x} = 12 A,   R_{th} = \frac{5.333}{12} = 0.4444 Ω$$

:::ans
**V_{th} = 5.333 V, R_{th} = 444.4 mΩ** (= book)
:::

<div class="qhead"><span class="qn">B33 · Practice Problem 4.10</span><span class="qt">Thevenin · no independent source <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Thevenin equivalent of the circuit in Fig. 4.36.
:::

[[img:sd_pp4_10|Fig. 4.36|w=40]]

No independent source ⇒ V_{th} = 0. Push 1 A into a; let i flow from a into the left branch (through 4v_{x}, 10 Ω, 5 Ω):

$$v_{x} = 5i,   V_{a} = 15i − 4v_{x} = −5i,   1 = \frac{V_{a}}{15} + i = \frac{2}{3}i  ⇒  i = 1.5 A,   V_{a} = −7.5 V$$

:::ans
**V_{th} = 0, R_{th} = −7.5 Ω** (= book)
:::

<div class="qhead"><span class="qn">B34 · Practice Problem 4.11</span><span class="qt">Norton · DC <span class="lvl plain">practice</span></span></div>

:::q
Find the Norton equivalent circuit for the circuit in Fig. 4.42, at terminals a-b.
:::

[[img:sd_pp4_11|Fig. 4.42|w=44]]

$$R_{N} = (3 + 3) ∥ 6 = 3 Ω;   short a–b:  \frac{15 − V_{M}}{3} + 4 = \frac{V_{M}}{3}  ⇒  V_{M} = 13.5 V,   I_{N} = \frac{13.5}{3} = 4.5 A$$

:::ans
**R_{N} = 3 Ω, I_{N} = 4.5 A** (= book)
:::

<div class="qhead"><span class="qn">B35 · Practice Problem 4.12</span><span class="qt">Norton · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Find the Norton equivalent circuit of the circuit in Fig. 4.45 at terminals a-b.
:::

[[img:sd_pp4_12|Fig. 4.45|w=42]]

**I_{sc}:** a–b shorted ⇒ v_{x} = 0 ⇒ 2v_{x} = 0, so the left node is shorted to b and all 10 A flows through the short: I_{N} = 10 A.

**V_{oc}:** v_{x} = V_{a}, left node at V_{a} + 2v_{x} = 3V_{a}. KCL there: 10 = \frac{3V_{a}}{6} + \frac{V_{a}}{2} = V_{a} ⇒ V_{oc} = 10 V, R_{N} = \frac{10}{10} = 1 Ω.

:::ans
**R_{N} = 1 Ω, I_{N} = 10 A** (= book)
:::

<div class="qhead"><span class="qn">B36 · Problem 4.33</span><span class="qt">Thevenin · DC <span class="lvl plain">practice</span></span></div>

:::q
Determine the Thevenin equivalent circuit, shown in Fig. 4.101, as seen by the 5-ohm resistor. Then calculate the current flowing through the 5-ohm resistor.
:::

[[img:sd4_33|Fig. 4.101|w=36]]

$$V_{th} = 4 × 10 = 40 V (no current in the series 10 Ω),   R_{th} = 10 + 10 = 20 Ω,   I = \frac{40}{20 + 5} = 1.6 A$$

:::ans
**V_{th} = 40 V, R_{th} = 20 Ω, I = 1.6 A** (= App. D)
:::

<div class="qhead"><span class="qn">B37 · Problem 4.34</span><span class="qt">Thevenin · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 4.102, design a problem that will help other students better understand Thevenin equivalent circuits.
:::

[[img:sd4_34|Fig. 4.102|w=38]]

**One design.** V = 12 V, R_{1} = 6 Ω, R_{2} = 3 Ω, R_{3} = 2 Ω, I = 1 A: *find the Thevenin equivalent at a–b.*

With a open, I circulates through R_{3} only, so the node above R_{2} is a plain divider: V_{N} = 12 × \frac{3}{9} = 4 V, and V_{a} = V_{N} + IR_{3} = 4 + 2 = 6 V. Sources off: R_{th} = R_{3} + R_{1} ∥ R_{2} = 2 + 2 = 4 Ω.

:::ans
**(this design) V_{th} = 6 V, R_{th} = 4 Ω** (design problem)
:::

<div class="qhead"><span class="qn">B38 · Problem 4.35</span><span class="qt">Thevenin · reuse of Prob. 4.12 <span class="lvl plain">practice</span></span></div>

:::q
Use Thevenin's theorem to find v_{o} in Prob. 4.12.
:::

[[img:sd4_12|Fig. 4.80: remove the 5 Ω and find the Thevenin equivalent between its ends A (left) and B (right).|w=48]]

$$V_{A}:  \frac{12 − V_{A}}{6} + 2 = \frac{V_{A}}{3}  ⇒  V_{A} = 8 V        V_{B}:  \frac{19 − V_{B}}{4} − 2 = \frac{V_{B}}{12}  ⇒  V_{B} = 8.25 V$$

$$V_{th} = V_{A} − V_{B} = −0.25 V,   R_{th} = (6 ∥ 3) + (12 ∥ 4) = 2 + 3 = 5 Ω,   v_{o} = −0.25 × \frac{5}{5 + 5}$$

:::ans
**v_{o} = −0.125 V = −125 mV** (= App. D; matches the superposition answer in 4.12)
:::

<div class="qhead"><span class="qn">B39 · Problem 4.36</span><span class="qt">Thevenin · load with a source in series <span class="lvl plain">practice</span></span></div>

:::q
Solve for the current i in the circuit of Fig. 4.103 using Thevenin's theorem. (Hint: Find the Thevenin equivalent seen by the 12-Ω resistor.)
:::

[[img:sd4_36|Fig. 4.103|w=36]]

Remove the 12 Ω. The top node: 50 V behind 10 Ω with 40 Ω ⇒ 50 × \frac{40}{50} = 40 V, R = 10 ∥ 40 = 8 Ω. The lower end of the gap sits on the 30 V source.

$$V_{th} = 40 − 30 = 10 V,   R_{th} = 8 Ω,   i = \frac{10}{8 + 12} = 0.5 A$$

:::ans
**i = 0.5 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B40 · Problem 4.37</span><span class="qt">Norton · DC <span class="lvl plain">practice</span></span></div>

:::q
Find the Norton equivalent with respect to terminals a-b in the circuit shown in Fig. 4.104.
:::

[[img:sd4_37|Fig. 4.104|w=46]]

$$R_{N} = (20 + 40) ∥ 12 = 10 Ω$$

Short a–b (12 Ω out). 2 A ∥ 40 Ω → 80 V in series with 40 Ω, + on the left, opposing the 120 V:

$$I_{N} = \frac{120 − 80}{20 + 40} = 0.6667 A$$

:::ans
**R_{N} = 10 Ω, I_{N} = 666.7 mA** (= App. D)
:::

<div class="qhead"><span class="qn">B41 · Problem 4.38</span><span class="qt">Thevenin · DC <span class="lvl plain">practice</span></span></div>

:::q
Apply Thevenin's theorem to find V_{o} in the circuit of Fig. 4.105.
:::

[[img:sd4_38|Fig. 4.105|w=48]]

$$3 A ∥ 16 Ω ⇒ 48 V behind 16 Ω;  + 4 Ω ⇒ 48 V behind 20 Ω;  with 12 V behind 5 Ω:  V = \frac{48/20 + 12/5}{1/20 + 1/5} = 19.2 V,  R = 20 ∥ 5 = 4 Ω$$

$$V_{th} = 19.2 V,   R_{th} = 4 + 1 = 5 Ω,   V_{o} = 19.2 × \frac{10}{5 + 10}$$

:::ans
**V_{o} = 12.8 V** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B42 · Problem 4.39</span><span class="qt">Thevenin · current source between nodes <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Thevenin equivalent at terminals a-b of the circuit shown in Fig. 4.106.
:::

[[img:sd4_39|Fig. 4.106; the 3 A pushes current from a towards the top-left node.|w=40]]

$$R_{th} = 16 + (10 + 10) ∥ 5 = 16 + 4 = 20 Ω$$

**V_{oc}.** With a open, the 3 A leaving a must arrive through the 16 Ω, so V_{a} = V_{M} − 48. Let x = V_{TL} − V_{M}. KCL at the top-left node and at M:

$$3 + \frac{24 − V_{TL}}{10} = \frac{x}{10},   \frac{x}{10} = \frac{V_{M}}{5} + 3  ⇒  x = 27.6 V,   V_{M} = −1.2 V$$

:::ans
**V_{th} = −1.2 − 48 = −49.2 V, R_{th} = 20 Ω** (= App. D)
:::

<div class="qhead"><span class="qn">B43 · Problem 4.40</span><span class="qt">Thevenin · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent at terminals a-b of the circuit in Fig. 4.107.
:::

[[img:sd4_40|Fig. 4.107|w=48]]

**V_{oc}.** One loop, current i: V_{o} = 10k i and 70 = 10k i + 20k i + 4V_{o} = 70k i ⇒ i = 1 mA, V_{o} = 10 V, V_{a} = 70 − 10 = 60 V.

**I_{sc}.** a–b shorted ⇒ V_{o} = 70 V, dependent source 280 V:

$$I_{sc} = \frac{70}{10k} + \frac{280}{20k} = 7 + 14 = 21 mA,   R_{th} = \frac{60}{0.021} = 2.857 kΩ$$

:::ans
**V_{th} = 60 V, R_{th} = 2.857 kΩ** (even problem; test-source solve agrees)
:::

<div class="qhead"><span class="qn">B44 · Problem 4.41</span><span class="qt">Thevenin + Norton · DC <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin and Norton equivalents at terminals a-b of the circuit shown in Fig. 4.108.
:::

[[img:sd4_41|Fig. 4.108; the 14 V has + on the right.|w=50]]

$$1 A ∥ 6 Ω ⇒ 6 V behind 6 Ω;  + 14 V ⇒ 20 V behind 6 + 14 = 20 Ω$$

$$KCL at a:  \frac{20 − V}{20} − 3 = \frac{V}{5}  ⇒  −2 = 0.25V  ⇒  V_{th} = −8 V,   R_{th} = 20 ∥ 5 = 4 Ω,   I_{N} = −2 A$$

:::ans
**V_{th} = −8 V, R_{th} = R_{N} = 4 Ω, I_{N} = −2 A** (= App. D)
:::

<div class="qhead"><span class="qn">B45 · Problem 4.42</span><span class="qt">Thevenin · challenging, floating terminals <span class="lvl light">new idea</span></span></div>

:::q
For the circuit in Fig. 4.109, find the Thevenin equivalent between terminals a and b.
:::

[[img:sd4_42|Fig. 4.109; the 20 V has + at the bottom.|w=52]]

:::new Hint: what's new
- **Merge parallel branches with sources first.** Between M (above the 5 A) and b there are two branches: 20 Ω, and 20 Ω + 20 V. Together they are 10 Ω in series with 10 V (rising towards b). 5 A ∥ 10 Ω → 50 V behind 10 Ω.
- **Symmetry for R_{th}.** With sources off: a–ground 10 Ω, a–M 10 Ω, M–ground 10 Ω, M–b 10 Ω, b–ground 10 Ω. Push 1 A in at a and out at b: by symmetry V_{M} = 0 and V_{b} = −V_{a}.
:::

**V_{oc}.** a carries current only to M, so V_{a} = \frac{30 + V_{M}}{2}; b has only 10 Ω to ground, so V_{b} = \frac{V_{M} + 10}{2}. KCL at M:

$$\frac{30 − V_{M}}{20} + \frac{50 − V_{M}}{10} = \frac{V_{M} + 10}{20}  ⇒  4V_{M} = 120  ⇒  V_{M} = 30 V,  V_{a} = 30 V,  V_{b} = 20 V$$

**R_{th}.** KCL at a with V_{M} = 0: \frac{V_{a}}{10} + \frac{V_{a}}{10} = 1 ⇒ V_{a} = 5 V, V_{b} = −5 V ⇒ R_{th} = 10 Ω.

:::ans
**V_{th} = V_{a} − V_{b} = 10 V, R_{th} = 10 Ω** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B46 · Problem 4.43</span><span class="qt">Thevenin · zero result <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent looking into terminals a-b of the circuit in Fig. 4.110 and solve for i_{x}.
:::

[[img:sd4_43|Fig. 4.110; the 6 Ω between a and b is the load.|w=52]]

$$V_{a} = 20 × \frac{10}{20} = 10 V,   V_{b} = 2 × 5 = 10 V,   V_{th} = 0,   R_{th} = 10 ∥ 10 + 5 = 10 Ω$$

:::ans
**R_{th} = 10 Ω, V_{th} = 0 V, so i_{x} = 0** (= App. D)
:::

<div class="qhead"><span class="qn">B47 · Problem 4.44</span><span class="qt">Thevenin · two terminal pairs <span class="lvl plain">practice</span></span></div>

:::q
For the circuit in Fig. 4.111, obtain the Thevenin equivalent as seen from terminals: (a) a-b (b) b-c
:::

[[img:sd4_44|Fig. 4.111|w=40]]

With all terminals open, one loop current i flows through 2, 3 and 4 Ω, and i + 2 through the 5 Ω:

$$24 = 2i + 3i + 4i + 5(i + 2)  ⇒  14i = 14  ⇒  i = 1 A$$

$$(a)  V_{th} = 4i = 4 V,   R_{th} = 1 + 4 ∥ (3 + 2 + 5) = 1 + \frac{40}{14} = 3.857 Ω$$

$$(b)  V_{th} = 5(i + 2) = 15 V,   R_{th} = 5 ∥ (4 + 3 + 2) = \frac{45}{14} = 3.214 Ω$$

:::ans
**(a) 4 V, 3.857 Ω;  (b) 15 V, 3.214 Ω** (even problem; full node solves agree)
:::

<div class="qhead"><span class="qn">B48 · Problem 4.45</span><span class="qt">Thevenin · DC <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent of the circuit in Fig. 4.112 as seen by looking into terminals a and b.
:::

[[img:sd4_45|Fig. 4.112|w=40]]

$$4 A ∥ 6 Ω ⇒ 24 V behind 6 Ω;  + 6 Ω ⇒ 24 V behind 12 Ω;   V_{th} = 24 × \frac{4}{16} = 6 V,   R_{th} = 12 ∥ 4 = 3 Ω$$

:::ans
**V_{th} = 6 V, R_{th} = 3 Ω** (App. D prints "3 Ω, 2 A", the Norton form: I_{N} = 6/3 = 2 A)
:::

<div class="qhead"><span class="qn">B49 · Problem 4.46</span><span class="qt">Norton · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 4.113, design a problem to help other students better understand Norton equivalent circuits.
:::

[[img:sd4_46|Fig. 4.113|w=44]]

**One design.** I = 6 A, R_{1} = 4 Ω, R_{2} = 4 Ω, R_{3} = 8 Ω: *find the Norton equivalent at a–b.*

$$Short a–b (R_{3} out):  I_{N} = 6 × \frac{4}{4 + 4} = 3 A;   R_{N} = (4 + 4) ∥ 8 = 4 Ω$$

:::ans
**(this design) I_{N} = 3 A, R_{N} = 4 Ω** (design problem)
:::

<div class="qhead"><span class="qn">B50 · Problem 4.47</span><span class="qt">Thevenin + Norton · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Thevenin and Norton equivalent circuits of the circuit in Fig. 4.114 with respect to terminals a and b.
:::

[[img:sd4_47|Fig. 4.114|w=46]]

$$I_{sc}:  V_{x} = 0 ⇒ I_{N} = \frac{30}{12} = 2.5 A        V_{oc}:  \frac{30 − V}{12} = \frac{V}{60} + 2V  ⇒  2.5 = 2.1V  ⇒  V = 1.1905 V$$

:::ans
**V_{th} = 1.1905 V, R_{th} = R_{N} = 476.2 mΩ, I_{N} = 2.5 A** (= App. D)
:::

<div class="qhead"><span class="qn">B51 · Problem 4.48</span><span class="qt">Norton · negative R_{N} <span class="lvl plain">practice</span></span></div>

:::q
Determine the Norton equivalent at terminals a-b for the circuit in Fig. 4.115.
:::

[[img:sd4_48|Fig. 4.115; 10i_{o} is a current-controlled voltage source.|w=36]]

**V_{oc}:** no current in the 2 Ω, so i_{o} = 2 A, the node above the 4 Ω is at 8 V, and V_{a} = 8 − 10i_{o} = −12 V.

**I_{sc}:** current i flows to the short, i_{o} = 2 − i, and 4i_{o} − 10i_{o} − 2i = 0 ⇒ −6(2 − i) − 2i = 0 ⇒ i = 3 A.

$$R_{N} = \frac{V_{oc}}{I_{sc}} = \frac{−12}{3} = −4 Ω$$

:::ans
**I_{N} = 3 A, R_{N} = −4 Ω** (even problem; test-source solve agrees)
:::
