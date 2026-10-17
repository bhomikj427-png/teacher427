<div class="qhead"><span class="qn">B52 · Problem 4.49</span><span class="qt">Norton · DC <span class="lvl plain">practice</span></span></div>

:::q
Find the Norton equivalent looking into terminals a-b of the circuit in Fig. 4.102. Let V = 40 V, I = 3 A, R_{1} = 10 Ω, R_{2} = 40 Ω, and R_{3} = 20 Ω.
:::

[[img:sd4_34|Fig. 4.102|w=38]]

$$R_{N} = R_{3} + R_{1} ∥ R_{2} = 20 + 8 = 28 Ω$$

Short a–b. V, R_{1}, R_{2} → 32 V behind 8 Ω. At the node above R_{2} (V_{N}), the short draws V_{N}/20 through R_{3} plus the 3 A:

$$\frac{32 − V_{N}}{8} = \frac{V_{N}}{20} + 3  ⇒  1 = 0.175V_{N}  ⇒  V_{N} = 5.714 V,   I_{N} = \frac{5.714}{20} + 3 = 3.286 A$$

:::ans
**R_{N} = 28 Ω, I_{N} = 3.286 A** (= App. D)
:::

<div class="qhead"><span class="qn">B53 · Problem 4.50</span><span class="qt">Norton · then use it <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Norton equivalent of the circuit in Fig. 4.116 to the left of terminals a-b. Use the result to find current i.
:::

[[img:sd4_50|Fig. 4.116; the 12 V has + on the left.|w=48]]

$$2 A ∥ 4 Ω ⇒ 8 V behind 4 Ω;  + 6 Ω, − 12 V  ⇒  V_{th} = 8 − 12 = −4 V,   R_{N} = 10 Ω,   I_{N} = −0.4 A$$

Right side: the Norton source and the 4 A both feed 10 ∥ 5 = \frac{10}{3} Ω:

$$V_{ab} = (−0.4 + 4) × \frac{10}{3} = 12 V,   i = \frac{12}{5} = 2.4 A$$

:::ans
**I_{N} = −0.4 A, R_{N} = 10 Ω; i = 2.4 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B54 · Problem 4.51</span><span class="qt">Norton · two terminal pairs <span class="lvl plain">practice</span></span></div>

:::q
Given the circuit in Fig. 4.117, obtain the Norton equivalent as viewed from terminals: (a) a-b (b) c-d
:::

[[img:sd4_51|Fig. 4.117|w=48]]

Node voltages with everything open (b and c are the same node):

$$\frac{120 − V_{a}}{6} = \frac{V_{a}}{3} + \frac{V_{a} − V_{b}}{4},   \frac{V_{a} − V_{b}}{4} + 6 = \frac{V_{b}}{2}  ⇒  V_{a} = 33 V,  V_{b} = 19 V$$

$$(a)  R_{N} = 4 ∥ (6 ∥ 3 + 2) = 4 ∥ 4 = 2 Ω,   I_{N} = \frac{33 − 19}{2} = 7 A$$

$$(b)  R_{N} = 2 ∥ (4 + 2) = 1.5 Ω,   I_{N} = \frac{19}{1.5} = 12.667 A$$

:::ans
**(a) 2 Ω, 7 A;  (b) 1.5 Ω, 12.667 A** (= App. D)
:::

<div class="qhead"><span class="qn">B55 · Problem 4.52</span><span class="qt">Thevenin · transistor model <span class="lvl plain">practice</span></span></div>

:::q
For the transistor model in Fig. 4.118, obtain the Thevenin equivalent at terminals a-b.
:::

[[img:sd4_52|Fig. 4.118; i_{o} flows down a plain wire.|w=44]]

The wire carrying i_{o} shorts the input to ground, so i_{o} = \frac{6}{3k} = 2 mA whatever happens on the right. The 20i_{o} = 40 mA flows down out of node a:

$$V_{oc} = −40 mA × 2 kΩ = −80 V,   I_{sc} = −40 mA,   R_{th} = 2 kΩ$$

:::ans
**V_{th} = −80 V, R_{th} = 2 kΩ** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B56 · Problem 4.53</span><span class="qt">Norton · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Find the Norton equivalent at terminals a-b of the circuit in Fig. 4.119.
:::

[[img:sd4_53|Fig. 4.119; 0.25v_{o} pushes current from a into the middle node.|w=40]]

**V_{oc}.** a is open, so the 2 Ω carries exactly the 0.25v_{o} that circulates back: V_{a} = v_{o} − 0.5v_{o}. At the middle node the two 0.25v_{o} currents cancel:

$$\frac{18 − v_{o}}{6} = \frac{v_{o}}{3}  ⇒  v_{o} = 6 V,   V_{oc} = 3 V$$

**I_{sc}.** a shorted:

$$\frac{18 − v_{o}}{6} = \frac{v_{o}}{3} + \frac{v_{o}}{2} − 0.25v_{o}  ⇒  v_{o} = 4 V,   I_{sc} = \frac{4}{2} − 0.25 × 4 = 1 A,   R_{N} = 3 Ω$$

:::ans
**R_{N} = 3 Ω, I_{N} = 1 A** (= App. D)
:::

<div class="qhead"><span class="qn">B57 · Problem 4.54</span><span class="qt">Thevenin · negative R_{th} <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent between terminals a-b of the circuit in Fig. 4.120.
:::

[[img:sd4_54|Fig. 4.120|w=50]]

This is Part A's Problem 5.27 with 50 Ω (A27).

$$V_{oc}:  I_{o} = \frac{3 − 2V_{x}}{1000},  V_{x} = −40I_{o} × 50 = −2(3 − 2V_{x})  ⇒  V_{oc} = 2 V$$

$$I_{sc}:  V_{x} = 0 ⇒ I_{o} = 3 mA,  I_{sc} = −40I_{o} = −0.12 A,   R_{th} = \frac{2}{−0.12} = −16.67 Ω$$

:::ans
**V_{th} = 2 V, R_{th} = −16.67 Ω** (even problem; test-source solve agrees)
:::

<div class="qhead"><span class="qn">B58 · Problem 4.55</span><span class="qt">Norton · transistor model <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Norton equivalent at terminals a-b of the circuit in Fig. 4.121.
:::

[[img:sd4_55|Fig. 4.121|w=50]]

$$I_{sc}:  V_{ab} = 0 ⇒ I = \frac{2}{8k} = 0.25 mA,  I_{N} = −80I = −20 mA$$

$$V_{oc}:  V_{ab} = −80I × 50k = −4 × 10^{6}I,  I = \frac{2 − 0.001V_{ab}}{8k} = \frac{2 + 4000I}{8000} ⇒ I = 0.5 mA,  V_{oc} = −2000 V$$

:::ans
**R_{N} = \frac{−2000}{−0.02} = 100 kΩ, I_{N} = −20 mA** (= App. D)
:::

<div class="qhead"><span class="qn">B59 · Problem 4.56</span><span class="qt">Norton · use it <span class="lvl plain">practice</span></span></div>

:::q
Use Norton's theorem to find V_{o} in the circuit of Fig. 4.122.
:::

[[img:sd4_56|Fig. 4.122|w=50]]

Norton seen by the 1 kΩ. 36 V, 12 kΩ, 24 kΩ → 24 V behind 8 kΩ.

$$R_{N} = 8k + 2k + 10k = 20 kΩ;   short:  \frac{24 − V_{B}}{10k} = 3 mA + \frac{V_{B}}{10k}  ⇒  V_{B} = −3 V,   I_{N} = −0.3 mA$$

$$V_{o} = I_{N} × (20k ∥ 1k) = −0.3 mA × 952.4 Ω$$

:::ans
**V_{o} = −0.2857 V** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B60 · Problem 4.57</span><span class="qt">Thevenin + Norton · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Thevenin and Norton equivalent circuits at terminals a-b for the circuit in Fig. 4.123.
:::

[[img:sd4_57|Fig. 4.123|w=50]]

$$I_{sc}:  \frac{50 − v_{x}}{3} = \frac{v_{x}}{6} + \frac{v_{x}}{2}  ⇒  v_{x} = 16.67 V,   I_{sc} = \frac{v_{x}}{2} + 0.5v_{x} = 16.67 A$$

$$V_{oc}:  KCL at a gives v_{x} = 0.6V_{a};   \frac{50 − 0.6V_{a}}{3} = −0.1V_{a}  ⇒  V_{a} = 166.67 V$$

:::ans
**V_{th} = 166.67 V, R_{th} = R_{N} = 10 Ω, I_{N} = 16.667 A** (= App. D)
:::

<div class="qhead"><span class="qn">B61 · Problem 4.58</span><span class="qt">Thevenin · current-source output <span class="lvl light">new idea</span></span></div>

:::q
The network in Fig. 4.124 models a bipolar transistor common-emitter amplifier connected to a load. Find the Thevenin resistance seen by the load.
:::

[[img:sd4_58|Fig. 4.124|w=44]]

:::new Hint: what's new
- **A current source alone at the output.** The only thing connecting the load's top terminal to the rest of the circuit is the dependent source bi_{b}. A current source in series fixes the terminal current, so no voltage you apply can change it.
:::

Switch off v_{s} and push a test current I_{t} into the output terminal. It can only flow through the dependent source, so I_{t} = bi_{b}. KCL at the middle node with v_{s} = 0 (i_{b} = −V/R_{1}): (1 + b)i_{b} = V/R_{2} gives V = 0 and i_{b} = 0, so I_{t} = 0 for any applied voltage.

:::ans
**R_{th} → ∞** (an ideal current-source output; even problem. The full solve with a test source is singular, as it must be.)
:::

<div class="qhead"><span class="qn">B62 · Problem 4.59</span><span class="qt">Thevenin + Norton · bridge <span class="lvl plain">practice</span></span></div>

:::q
Determine the Thevenin and Norton equivalents at terminals a-b of the circuit in Fig. 4.125.
:::

[[img:sd4_59|Fig. 4.125|w=42]]

Both branches are 60 Ω, so the 8 A splits 4 A each: V_{a} = 4 × 50 = 200 V, V_{b} = 4 × 40 = 160 V.

$$V_{th} = 40 V,   R_{th} = (10 + 20) ∥ (50 + 40) = 22.5 Ω,   I_{N} = \frac{40}{22.5} = 1.778 A$$

:::ans
**V_{th} = 40 V, R_{th} = 22.5 Ω, I_{N} = 1.7778 A** (= App. D)
:::

<div class="qhead"><span class="qn">B63 · Problem 4.60</span><span class="qt">Thevenin + Norton · challenging <span class="lvl plain">practice</span></span></div>

:::q
For the circuit in Fig. 4.126, find the Thevenin and Norton equivalent circuits at terminals a-b.
:::

[[img:sd4_60|Fig. 4.126|w=40]]

$$R_{th} = [(4 + 6) via the middle] ∥ [5 via the bottom] = 10 ∥ 5 = 3.333 Ω   (2 A and 3 A open, 18 V and 10 V shorted)$$

**V_{oc}** (b = 0). The middle branch current i flows a → 18 V → 4 Ω (with the 3 A added in) → 6 Ω → b: 6i = V_{Q} and (V_{a} − 18) − V_{Q} = 4(i + 3), so i = \frac{V_{a} − 30}{10}. KCL at a:

$$2 + \frac{V_{a} − 30}{10} + \frac{V_{a} − 10}{5} = 0  ⇒  3V_{a} = 30$$

:::ans
**V_{th} = 10 V, R_{th} = 3.333 Ω, I_{N} = 3 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B64 · Problem 4.61</span><span class="qt">Thevenin + Norton · symmetry <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Thevenin and Norton equivalent circuits at terminals a-b of the circuit in Fig. 4.127.
:::

[[img:sd4_61|Fig. 4.127|w=48]]

**V_{oc}.** The circuit is left–right symmetric, so both top nodes sit at the same V and no current flows in the 2 Ω between them. KCL at a top node and at the middle node M (bottom of its 6 Ω at −12 V):

$$\frac{V − 12}{2} + \frac{V − V_{M}}{6} = 0 ⇒ V_{M} = 4V − 36;   \frac{2(V_{M} − V)}{6} + \frac{V_{M} + 12}{6} = 0 ⇒ V = 9.6 V$$

**I_{sc}** (a grounded): solving the left and middle nodes gives V_{TL} = 4.8 V, V_{M} = −2.4 V, so

$$I_{sc} = \frac{12}{2} + \frac{4.8}{2} + \frac{−2.4}{6} = 6 + 2.4 − 0.4 = 8 A,   R_{th} = \frac{9.6}{8} = 1.2 Ω$$

:::ans
**V_{th} = 9.6 V, R_{th} = 1.2 Ω, I_{N} = 8 A** (= App. D)
:::

<div class="qhead"><span class="qn">B65 · Problem 4.62</span><span class="qt">Thevenin · no independent source <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent of the circuit in Fig. 4.128.
:::

[[img:sd4_62|Fig. 4.128; the left vertical wire joins the top-left and the middle node.|w=36]]

V_{th} = 0. Push 1 A into a (b grounded). With i_{o} = V_{M}/20 and v_{o} = V_{a} − V_{M}:

$$KCL at a:  1 + 0.1i_{o} = \frac{v_{o}}{10} ⇒ v_{o} = 10 + i_{o};   KCL at M:  1 = i_{o} + \frac{V_{M} − 2v_{o}}{40}$$

$$1 = i_{o} + \frac{18i_{o} − 20}{40}  ⇒  i_{o} = \frac{60}{58} A,  V_{M} = 20.69 V,  V_{a} = V_{M} + v_{o} = 31.72 V$$

:::ans
**V_{th} = 0, R_{th} = 31.72 Ω** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B66 · Problem 4.63</span><span class="qt">Norton · no independent source <span class="lvl plain">practice</span></span></div>

:::q
Find the Norton equivalent for the circuit in Fig. 4.129.
:::

[[img:sd4_63|Fig. 4.129|w=34]]

This is Part A's Problem 5.34 (A34): test source gives V = −\frac{10}{3}I.

:::ans
**R_{N} = −3.333 Ω, I_{N} = 0** (= App. D)
:::

<div class="qhead"><span class="qn">B67 · Problem 4.64</span><span class="qt">Thevenin · no independent source <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Thevenin equivalent seen at terminals a-b of the circuit in Fig. 4.130.
:::

[[img:sd4_64|Fig. 4.130|w=34]]

V_{th} = 0. Push I_{t} into a; i_{x} = V_{N}/2 and the source is 10i_{x} = 5V_{N}:

$$I_{t} = \frac{V_{N}}{2} + \frac{V_{N} − 5V_{N}}{4} = −\frac{V_{N}}{2}  ⇒  V_{N} = −2I_{t},   V_{a} = V_{N} + 1·I_{t} = −I_{t}$$

:::ans
**V_{th} = 0, R_{th} = −1 Ω** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B68 · Problem 4.65</span><span class="qt">Thevenin · terminal equation <span class="lvl plain">practice</span></span></div>

:::q
For the circuit shown in Fig. 4.131, determine the relationship between V_{o} and I_{o}.
:::

[[img:sd4_65|Fig. 4.131|w=46]]

$$V_{th} = 32 × \frac{12}{16} = 24 V,   R_{th} = 4 ∥ 12 + 2 = 5 Ω,   V_{o} = V_{th} − R_{th}I_{o}$$

:::ans
**V_{o} = 24 − 5I_{o}** (= App. D)
:::
