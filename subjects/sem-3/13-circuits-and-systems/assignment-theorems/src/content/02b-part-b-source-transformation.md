## B · Source transformation (§4.4)

[[map:Superposition (done) > Source transformation: swap V + series R ↔ I ∥ R > Thevenin / Norton (next)|here=2]]

**Where this sits.** Part A used source transformation inside superposition cases (5.9, 5.10). Here it is the whole method: keep swapping sources until the circuit is one loop or one node.

**The rule.** A voltage source V_{s} **in series** with R is equivalent to a current source i_{s} = V_{s}/R **in parallel** with the same R, and back again. The current source's arrow points towards the voltage source's + terminal.

- It works for dependent sources too, as long as the controlling voltage or current is not hidden inside the swap.
- A source with **no** series R (voltage) or **no** parallel R (current) cannot be transformed.
- Parallel current sources add; series voltage sources add; resistors combine as usual between swaps.

<div class="qhead"><span class="qn">B16 · Practice Problem 4.6</span><span class="qt">Source transformation <span class="lvl plain">practice</span></span></div>

:::q
Find i_{o} in the circuit of Fig. 4.19 using source transformation.
:::

[[img:sd_pp4_6|Fig. 4.19; the 5 V has + on the right.|w=66]]

:::try
Merge everything left of the 5 V into one source with one resistor, then add the 5 V.
:::

$$6 ∥ 3 = 2 Ω  with 5 A  ⇒  10 V behind 2 Ω;   + 5 V in series  ⇒  15 V behind 2 Ω$$

At the 7 Ω node (call it M), the 3 A enters and 1 + 4 = 5 Ω goes to ground:

$$\frac{15 − V_{M}}{2} + 3 = \frac{V_{M}}{7} + \frac{V_{M}}{5}  ⇒  10.5 = 0.8429V_{M}  ⇒  V_{M} = 12.46 V$$

:::ans
**i_{o} = \frac{12.46}{7} = 1.78 A** (= book)
:::

<div class="qhead"><span class="qn">B17 · Practice Problem 4.7</span><span class="qt">Source transformation · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation to find i_{x} in the circuit shown in Fig. 4.22.
:::

[[img:sd_pp4_7|Fig. 4.22; 2i_{x} has − at the top.|w=44]]

:::try
Transform the dependent source with its 5 Ω, but keep the 10 Ω (it carries i_{x}).
:::

The 2i_{x} source (− at top) in series with 5 Ω becomes a current source \frac{2i_{x}}{5} = 0.4i_{x} pulling current **out of** the top node, in parallel with 5 Ω. With V_{top} = 10i_{x}:

$$0.024 − 0.4i_{x} = \frac{10i_{x}}{10} + \frac{10i_{x}}{5} = 3i_{x}  ⇒  3.4i_{x} = 0.024$$

:::ans
**i_{x} = 7.059 mA** (= book)
:::

<div class="qhead"><span class="qn">B18 · Problem 4.20</span><span class="qt">Source transformation · reduce to one source <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation to reduce the circuit in Fig. 4.88 to a single voltage source in series with a single resistor.
:::

[[img:sd4_20|Fig. 4.88|w=50]]

Every branch runs between the two rails, so turn the voltage branches into current sources and add:

$$\frac{12}{20} = 0.6 A,   \frac{16}{40} = 0.4 A,   3 + 0.6 + 0.4 = 4 A  in parallel with  10 ∥ 20 ∥ 40 = \frac{40}{7} Ω$$

:::ans
**V = 4 × \frac{40}{7} = \frac{160}{7} = 22.86 V (+ at the top rail) in series with \frac{40}{7} = 5.714 Ω** (even problem; open-circuit and short-circuit solves agree)
:::

<div class="qhead"><span class="qn">B19 · Problem 4.21</span><span class="qt">Source transformation · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 4.89, design a problem to help other students better understand source transformation.
:::

[[img:sd4_21|Fig. 4.89|w=36]]

**One design.** Take **V = 20 V, R_{1} = 5 Ω, R_{2} = 20 Ω, I = 2 A** and ask: *use source transformation to find v_{o} and i_{o}.*

$$20 V behind 5 Ω  ⇒  4 A ∥ 5 Ω;   4 + 2 = 6 A  into  5 ∥ 20 = 4 Ω  ⇒  v_{o} = 24 V$$

$$i_{o} = \frac{V − v_{o}}{R_{1}} = \frac{20 − 24}{5} = −0.8 A$$

:::ans
**(this design) v_{o} = 24 V, i_{o} = −0.8 A** (design problem; the book lists "multiple answers")
:::

<div class="qhead"><span class="qn">B20 · Problem 4.22</span><span class="qt">Source transformation <span class="lvl plain">practice</span></span></div>

:::q
For the circuit in Fig. 4.90, use source transformation to find i.
:::

[[img:sd4_22|Fig. 4.90; the 2 A points down.|w=44]]

$$2 A (down) ∥ 5 Ω  ⇒  −10 V behind 5 Ω;   + 5 Ω  ⇒  −10 V behind 10 Ω$$

At the middle node M, with 20 V behind 10 Ω on the right:

$$\frac{−10 − V_{M}}{10} + \frac{20 − V_{M}}{10} = \frac{V_{M}}{4}  ⇒  1 = 0.45V_{M}  ⇒  V_{M} = 2.222 V$$

:::ans
**i = \frac{V_{M}}{4} = \frac{5}{9} = 0.556 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B21 · Problem 4.23</span><span class="qt">Source transformation · power <span class="lvl plain">practice</span></span></div>

:::q
Referring to Fig. 4.91, use source transformation to determine the current and power absorbed by the 8-Ω resistor.
:::

[[img:sd4_23|Fig. 4.91|w=52]]

$$Left:  3 A ∥ 10 Ω  ⇒  30 V behind 10 Ω        Right:  15 V behind 3 Ω  ⇒  5 A ∥ 3 Ω;  ∥ 6 Ω  ⇒  5 A ∥ 2 Ω  ⇒  10 V behind 2 Ω$$

$$i_{8Ω} = \frac{30 − 10}{10 + 8 + 2} = 1 A,   P = 1^{2} × 8 = 8 W$$

:::ans
**i = 1 A, P = 8 W** (= App. D)
:::

<div class="qhead"><span class="qn">B22 · Problem 4.24</span><span class="qt">Source transformation · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation to find the voltage V_{x} in the circuit of Fig. 4.92.
:::

[[img:sd4_24|Fig. 4.92; 2V_{x} is a voltage-controlled current source.|w=48]]

:::try
Both current sources have a resistor in parallel. Turn the circuit into a single loop, keeping the 8 Ω (it carries V_{x}).
:::

- 3 A ∥ 10 Ω (top) → 30 V in series with 10 Ω, + on the right.
- 2V_{x} ∥ 10 Ω (right) → 20V_{x} in series with 10 Ω, + at the top.

One loop, clockwise current i, with V_{x} = 8i:

$$40 = 8i + 10i − 30 + 10i + 20V_{x} = 28i − 30 + 160i  ⇒  188i = 70  ⇒  i = 0.3723 A$$

:::ans
**V_{x} = 8i = 2.979 V** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B23 · Problem 4.25</span><span class="qt">Source transformation · three current sources <span class="lvl light">new idea</span></span></div>

:::q
Obtain v_{o} in the circuit of Fig. 4.93 using source transformation. Check your result using PSpice or MultiSim.
:::

[[img:sd4_25|Fig. 4.93|w=48]]

:::new Hint: what's new
- **Every current source here has a resistor in parallel**, so all three transform: the whole circuit collapses into **one loop**. Keep track of each new + sign: it sits where the arrow pointed.
:::

- 3 A (down) ∥ 4 Ω → 12 V in series with 4 Ω, + at the bottom.
- 2 A (left → right) ∥ 9 Ω → 18 V in series with 9 Ω, + on the right.
- 6 A (down) ∥ 5 Ω → 30 V in series with 5 Ω, + at the bottom.

Clockwise loop current i (top: left → right; bottom: right → left through the 30 V and the 2 Ω):

$$18 + 30 + 30 − 12 = (9 + 5 + 2 + 4)i  ⇒  66 = 20i  ⇒  i = 3.3 A$$

The current runs right → left in the 2 Ω, against the + of v_{o}:

:::ans
**v_{o} = −2 × 3.3 = −6.6 V** (= App. D)
:::

<div class="qhead"><span class="qn">B24 · Problem 4.26</span><span class="qt">Source transformation <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation to find i_{o} in the circuit of Fig. 4.94.
:::

[[img:sd4_26|Fig. 4.94|w=46]]

$$6 A ∥ 2 Ω ⇒ 12 V behind 2 Ω;   3 A ∥ 5 Ω ⇒ 15 V behind 5 Ω (+ on the right)$$

$$i_{o} = \frac{12 + 15 − 20}{2 + 5 + 4} = \frac{7}{11} A$$

:::ans
**i_{o} = 0.636 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B25 · Problem 4.27</span><span class="qt">Source transformation <span class="lvl plain">practice</span></span></div>

:::q
Apply source transformation to find v_{x} in the circuit of Fig. 4.95.
:::

[[img:sd4_27|Fig. 4.95|w=52]]

$$Left:  50 V/10 Ω ⇒ 5 A ∥ 10 Ω;  ∥ 40 Ω ⇒ 5 A ∥ 8 Ω ⇒ 40 V behind 8 Ω$$

$$Right:  40 V/20 Ω ⇒ 2 A ∥ 20 Ω;  + 8 A ⇒ 10 A ∥ 20 Ω ⇒ 200 V behind 20 Ω$$

$$i_{a→b} = \frac{40 − 200}{8 + 12 + 20} = −4 A$$

:::ans
**v_{x} = 12 × (−4) = −48 V** (= App. D)
:::

<div class="qhead"><span class="qn">B26 · Problem 4.28</span><span class="qt">Source transformation · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation to find I_{o} in Fig. 4.96.
:::

[[img:sd4_28|Fig. 4.96; \frac{1}{3}V_{o} points down.|w=50]]

\frac{1}{3}V_{o} (down) ∥ 3 Ω → a voltage V_{o} in series with 3 Ω, + at the bottom. One loop, with V_{o} = 4I_{o}:

$$8 = 1·I_{o} + 4I_{o} + 3I_{o} − V_{o} = 8I_{o} − 4I_{o} = 4I_{o}$$

:::ans
**I_{o} = 2 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B27 · Problem 4.29</span><span class="qt">Source transformation · dependent source <span class="lvl light">new idea</span></span></div>

:::q
Use source transformation to find v_{o} in the circuit of Fig. 4.97.
:::

[[img:sd4_29|Fig. 4.97|w=40]]

:::new Hint: what's new
- **Look for the only return path first.** Every path out of the 3 mA source ends in the 1 kΩ, so all 3 mA flows through it, whatever the 4 kΩ, 2 kΩ and 3v_{o} do.
:::

$$v_{o} = 3 mA × 1 kΩ = 3 V$$

:::ans
**v_{o} = 3 V** (= App. D)
:::

:::note Check
With v_{o} = 3 V the dependent source is 9 V, and the 3 mA splits between the 4 kΩ and the 2 kΩ + 3v_{o} branches; a full node solve confirms v_{o} = 3 V.
:::

<div class="qhead"><span class="qn">B28 · Problem 4.30</span><span class="qt">Source transformation · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation on the circuit shown in Fig. 4.98 to find i_{x}.
:::

[[img:sd4_30|Fig. 4.98|w=52]]

0.7i_{x} ∥ 10 Ω → 7i_{x} in series with 10 Ω, + at the top. From node A (after the 24 Ω) the right side is then 60 + 10 = 70 Ω in series with 7i_{x}. With V_{A} = 12 − 24i_{x}, KCL at A:

$$i_{x} = \frac{V_{A}}{30} + \frac{V_{A} − 7i_{x}}{70}  ⇒  210i_{x} = 7(12 − 24i_{x}) + 3(12 − 31i_{x})  ⇒  471i_{x} = 120$$

:::ans
**i_{x} = 0.2548 A** (even problem; full node solve agrees)
:::

<div class="qhead"><span class="qn">B29 · Problem 4.31</span><span class="qt">Source transformation · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Determine v_{x} in the circuit of Fig. 4.99 using source transformation.
:::

[[img:sd4_31|Fig. 4.99|w=38]]

Both voltage sources have a series resistor: 12 V/3 Ω → 4 A ∥ 3 Ω, 2v_{x}/6 Ω → \frac{v_{x}}{3} ∥ 6 Ω. At the middle node (V_{M} = 12 − v_{x}):

$$4 + \frac{v_{x}}{3} = V_{M}(\frac{1}{3} + \frac{1}{8} + \frac{1}{6}) = 0.625(12 − v_{x})  ⇒  \frac{23}{24}v_{x} = 3.5$$

:::ans
**v_{x} = \frac{84}{23} = 3.652 V** (= App. D)
:::

<div class="qhead"><span class="qn">B30 · Problem 4.32</span><span class="qt">Source transformation · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation to find i_{x} in the circuit of Fig. 4.100.
:::

[[img:sd4_32|Fig. 4.100|w=44]]

0.5i_{x} ∥ 10 Ω (between A and B) → 5i_{x} in series with 10 Ω, + at B. The A–B branch now meets only the 40 Ω, so it carries \frac{V_{A} + 5i_{x}}{50}. With V_{A} = 60 − 15i_{x}, KCL at A:

$$i_{x} = \frac{V_{A}}{50} + \frac{V_{A} + 5i_{x}}{50}  ⇒  50i_{x} = 2(60 − 15i_{x}) + 5i_{x}  ⇒  75i_{x} = 120$$

:::ans
**i_{x} = 1.6 A** (even problem; full node solve agrees)
:::
