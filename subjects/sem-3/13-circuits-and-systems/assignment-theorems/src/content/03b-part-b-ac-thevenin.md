## F · AC Thevenin and Norton (ch. 10 §10.6)

[[map:AC superposition + source transformation (done) > AC Thevenin / Norton: V_{th}, I_{N}, Z_{th} as phasors > AC max power (next)|here=2]]

**Where this sits.** Identical to chapter 4 with complex numbers: V_{th} = V_{oc}, I_{N} = I_{sc} (a → b), Z_{th} = Z_{N} = V_{oc}/I_{sc} or by test source. Sources at different frequencies would need one equivalent per frequency; every problem here has a single ω.

<div class="qhead"><span class="qn">B99 · Practice Problem 10.8</span><span class="qt">AC Thevenin <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent at terminals a-b of the circuit in Fig. 10.24.
:::

[[img:sd_pp10_8|Fig. 10.24; b is the top of the 10 Ω.|w=46]]

No current flows in the 10 Ω, so V_{b} = 0:

$$V_{th} = 100∠20° × \frac{−j4}{6 + j2 − j4} = 63.25∠−51.57° V,   Z_{th} = (6 + j2) ∥ (−j4) + 10 = 2.4 − j3.2 + 10$$

:::ans
**Z_{th} = 12.4 − j3.2 Ω, V_{th} = 63.24∠−51.57° V** (= book)
:::

<div class="qhead"><span class="qn">B100 · Practice Problem 10.9</span><span class="qt">AC Thevenin · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Determine the Thevenin equivalent of the circuit in Fig. 10.27 as seen from the terminals a-b.
:::

[[img:sd_pp10_9|Fig. 10.27; V_{o} is across 8 + j4 (+ on the left).|w=44]]

Let L be the left node; V_{o} = V_{L} − V_{a}. KCL at L and at a (terminals open):

$$\frac{V_{L}}{4 − j2} + 5 + \frac{V_{o}}{8 + j4} = 0,   5 + \frac{V_{o}}{8 + j4} + 0.2V_{o} = 0  ⇒  V_{o} = −16.22 − j2.70 V$$

$$V_{L} = −14.05 + j4.32 V,   V_{th} = V_{L} − V_{o} = 2.162 + j7.027 V$$

Z_{th} by test source (5 A opened): 1 A into a gives V_{a} = 4.432 − j0.595 V.

:::ans
**V_{th} = 7.35∠72.9° V, Z_{th} = 4.473∠−7.64° Ω** (= book)
:::

<div class="qhead"><span class="qn">B101 · Practice Problem 10.10</span><span class="qt">AC Norton · use it <span class="lvl plain">practice</span></span></div>

:::q
Determine the Norton equivalent of the circuit in Fig. 10.30 as seen from terminals a-b. Use the equivalent to find I_{o}.
:::

[[img:sd_pp10_10|Fig. 10.30; the load is 10 − j5 Ω.|w=48]]

$$Z_{N} = (4 + j2) ∥ (8 + 1 − j3) = 3.176 + j0.706 Ω   (20 V shorted, 4∠−90° A opened)$$

Short a–b. The 4 + j2 carries \frac{20}{4 + j2} = 4 − j2 A. Node M (above the current source):

$$\frac{20 − V_{M}}{8} − j4 = \frac{V_{M}}{1 − j3}  ⇒  V_{M} = −4.533 − j11.733 V,   \frac{V_{M}}{1 − j3} = 3.067 − j2.533 A$$

$$I_{N} = (4 − j2) + (3.067 − j2.533) = 8.396∠−32.68° A,   I_{o} = I_{N} × \frac{Z_{N}}{Z_{N} + 10 − j5}$$

:::ans
**Z_{N} = 3.176 + j0.706 Ω, I_{N} = 8.396∠−32.68° A, I_{o} = 1.971∠−2.10° A** (= book)
:::

<div class="qhead"><span class="qn">B102 · Problem 10.55</span><span class="qt">AC Thevenin + Norton <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin and Norton equivalent circuits at terminals a-b for each of the circuits in Fig. 10.98.
:::

**(a)**

[[img:sd10_55a||w=40]]

$$V_{th} = 50∠30° × \frac{−j10}{j20 − j10} = −50∠30° = 50∠−150° V,   Z_{th} = j20 ∥ (−j10) + 10 = 10 − j20 Ω$$

$$I_{N} = \frac{V_{th}}{Z_{th}} = \frac{50∠−150°}{22.36∠−63.43°} = 2.236∠−86.57° A$$

:::ans
**(a) Z_{th} = 10 − j20 = 22.36∠−63.43° Ω, V_{th} = 50∠−150° V, I_{N} = 2.236∠−86.57° A** (= App. D, which prints 22.63, a digit swap)
:::

**(b)**

[[img:sd10_55b||w=40]]

$$Z_{th} = (8 − j5) ∥ j10 = 8.989 + j4.382 = 10∠25.99° Ω,   I_{N} = 4 × \frac{8}{8 − j5} = 3.392∠32.01° A$$

:::ans
**(b) Z_{th} = 10∠26° Ω, V_{th} = I_{N}Z_{th} = 33.92∠58° V, I_{N} = 3.392∠32° A** (= App. D)
:::

<div class="qhead"><span class="qn">B103 · Problem 10.56</span><span class="qt">AC Thevenin + Norton <span class="lvl plain">practice</span></span></div>

:::q
For each of the circuits in Fig. 10.99, obtain Thevenin and Norton equivalent circuits at terminals a-b.
:::

**(a)**

[[img:sd10_56a||w=34]]

$$j4 ∥ (−j2) = −j4;   Z_{th} = 6 − j4 Ω (the source branch opened),   I_{N} = 2∠0° A,   V_{th} = 2(6 − j4) = 12 − j8 V$$

:::ans
**(a) Z_{th} = 6 − j4 = 7.211∠−33.69° Ω, V_{th} = 14.42∠−33.69° V, I_{N} = 2∠0° A** (even problem)
:::

**(b)**

[[img:sd10_56b||w=44]]

$$120∠45° behind 30 Ω, shunt 60 Ω  ⇒  80∠45° V behind 20 Ω;   V_{th} = 80∠45° × \frac{−j5}{20 + j10 − j5} = 19.40∠−59.04° V$$

$$Z_{th} = (20 + j10) ∥ (−j5) = 1.176 − j5.294 Ω,   I_{N} = \frac{V_{th}}{Z_{th}} = 3.578∠18.43° A$$

:::ans
**(b) Z_{th} = 5.423∠−77.47° Ω, V_{th} = 19.40∠−59.04° V, I_{N} = 3.578∠18.43° A** (even problem)
:::

<div class="qhead"><span class="qn">B104 · Problem 10.57</span><span class="qt">AC Thevenin · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 10.100, design a problem to help other students better understand Thevenin and Norton equivalent circuits.
:::

[[img:sd10_57|Fig. 10.100|w=40]]

**One design.** V_{s} = 10∠0° V, R_{1} = 2 Ω, X_{C} = 2 Ω, X_{L} = 2 Ω, R_{2} = 1 Ω: *find both equivalents.*

$$V_{th} = 10 × \frac{j2}{2 − j2 + j2} = j10 V,   Z_{th} = (2 − j2) ∥ j2 + 1 = 2 + j2 + 1 = 3 + j2 Ω,   I_{N} = \frac{j10}{3 + j2} = 2.774∠56.31° A$$

:::ans
**(this design) V_{th} = 10∠90° V, Z_{th} = 3 + j2 Ω, I_{N} = 2.774∠56.31° A** (design problem)
:::

<div class="qhead"><span class="qn">B105 · Problem 10.58</span><span class="qt">AC Thevenin <span class="lvl plain">practice</span></span></div>

:::q
For the circuit depicted in Fig. 10.101, find the Thevenin equivalent circuit at terminals a-b.
:::

[[img:sd10_58|Fig. 10.101|w=40]]

$$Z_{th} = (8 − j6) ∥ j10 = 10 + j5 Ω,   V_{th} = 5∠45° × (10 + j5) = 55.90∠71.57° V$$

:::ans
**V_{th} = 55.90∠71.57° V, Z_{th} = 10 + j5 Ω** (even problem)
:::

<div class="qhead"><span class="qn">B106 · Problem 10.59</span><span class="qt">AC output impedance · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Calculate the output impedance of the circuit shown in Fig. 10.102.
:::

[[img:sd10_59|Fig. 10.102|w=40]]

Push 1 A into the output. It flows through 10 Ω and then through −j2 towards T. With V_{o}'s + at T:

$$V_{o} = V_{T} − V_{X} = j2 × 1 = j2 V,   dependent source 0.2V_{o} = j0.4 A into T$$

$$j40 carries 1 + j0.4 A  ⇒  V_{T} = j40(1 + j0.4) = −16 + j40 V$$

$$V_{out} = V_{T} − j2 + 10 = −6 + j38 V  ⇒  Z_{out} = −6 + j38 Ω$$

:::ans
**Z_{out} = −6 + j38 Ω** (= App. D)
:::

<div class="qhead"><span class="qn">B107 · Problem 10.60</span><span class="qt">AC Thevenin · two terminal pairs <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent of the circuit in Fig. 10.103 as seen from: (a) terminals a-b (b) terminals c-d
:::

[[img:sd10_60|Fig. 10.103|w=50]]

20 V behind 10 Ω with j5 shunt ⇒ 4 + j8 V behind 10 ∥ j5 = 2 + j4 Ω. Add −j4 ⇒ (4 + j8) V behind 2 Ω ⇒ 2 + j4 A ∥ 2 Ω.

$$(a)  node d = a:  (2 + j4 + 4) × (2 ∥ 4) = (6 + j4) × \frac{4}{3} = 8 + j5.333 V,   Z_{th} = 2 ∥ 4 = 1.333 Ω$$

$$(b)  V_{c} = 13.33 + j13.33 V (node solve),  V_{th} = V_{c} − V_{d} = 5.333 + j8 V,   Z_{th} = (−j4) ∥ (2 + j4 + 4) = 2.667 − j4 Ω$$

:::ans
**(a) 9.615∠33.69° V, 1.333 Ω  (b) 9.615∠56.31° V, 2.667 − j4 Ω** (even problem; full solves agree)
:::

<div class="qhead"><span class="qn">B108 · Problem 10.61</span><span class="qt">AC Thevenin · dependent source, negative R <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent at terminals a-b of the circuit in Fig. 10.104.
:::

[[img:sd10_61|Fig. 10.104|w=44]]

**V_{oc}.** a open, so the 4 Ω carries the 1.5I_{x} backwards into L: KCL at L: 2 + 1.5I_{x} = I_{x} ⇒ I_{x} = −4 A, V_{L} = −j3(−4) = j12 V, V_{a} = V_{L} + 4 × 1.5I_{x} = j12 − 24.

**Z_{th}** (2 A opened, 1 A into a): I_{x} = 1 + 1.5I_{x} ⇒ I_{x} = −2 A, V_{L} = j6, V_{a} = j6 + 4(1 + 1.5I_{x}) = j6 − 8.

:::ans
**V_{th} = −24 + j12 V, Z_{th} = −8 + j6 Ω** (= App. D)
:::

<div class="qhead"><span class="qn">B109 · Problem 10.62</span><span class="qt">AC Thevenin · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Using Thevenin's theorem, find v_{o} in the circuit of Fig. 10.105.
:::

[[img:sd10_62|Fig. 10.105 (ω = 1)|w=46]]

This is Part A's Chakraborty 5.22 (A22) with the source's + at the top instead of the bottom, so every result flips sign:

$$V_{th} = −(2.361 − j1.967) = 3.073∠140.19° V,   Z_{th} = −0.525 − j2.230 Ω,   v_{o} = V_{th} × \frac{2}{Z_{th} + 2}$$

:::ans
**v_{o} = 2.299 cos(t − 163.30°) V** (even problem; full node solve agrees). This independent textbook circuit confirms the A22 correction: the book's 1.27∠32° V there is wrong.
:::

<div class="qhead"><span class="qn">B110 · Problem 10.63</span><span class="qt">AC Norton <span class="lvl plain">practice</span></span></div>

:::q
Obtain the Norton equivalent of the circuit depicted in Fig. 10.106 at terminals a-b.
:::

[[img:sd10_63|Fig. 10.106 (ω = 200: 10 H → j2000, 5 μF → −j1000)|w=50]]

$$j2000 ∥ 2000 = 1000 + j1000;   Z_{N} = 1000 + j1000 − j1000 = 1 kΩ,   I_{N} = 4∠30° × \frac{1000 + j1000}{1000} = 5.657∠75° A$$

:::ans
**Z_{N} = 1 kΩ, i_{N} = 5.657 cos(200t + 75°) A** (= App. D)
:::

<div class="qhead"><span class="qn">B111 · Problem 10.64</span><span class="qt">AC Norton · bridge <span class="lvl plain">practice</span></span></div>

:::q
For the circuit shown in Fig. 10.107, find the Norton equivalent circuit at terminals a-b.
:::

[[img:sd10_64|Fig. 10.107|w=42]]

$$Z_{N} = (60 + 40) ∥ (j80 − j30) = 100 ∥ j50 = 20 + j40 Ω   (source opened)$$

Short a–b. All 3∠60° A passes the top pair (60 ∥ 40) and then the bottom pair (j80 ∥ −j30):

$$I_{60} = 3∠60° × \frac{40}{100} = 1.2∠60° A (into a),   I_{j80} = 3∠60° × \frac{−j30}{j50} = −1.8∠60° A (out of a)$$

$$I_{N} = I_{60} − I_{j80} = 3∠60° A$$

:::ans
**Z_{N} = 20 + j40 Ω, I_{N} = 3∠60° A, V_{th} = 134.2∠123.43° V** (even problem; full solves agree)
:::

<div class="qhead"><span class="qn">B112 · Problem 10.65</span><span class="qt">AC Norton · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 10.108, design a problem to help other students better understand Norton's theorem.
:::

[[img:sd10_65|Fig. 10.108|w=34]]

**One design.** v_{s} = 10∠0° V (+ on the left), R = 5 Ω, C_{1} → −j10 Ω, L → j5 Ω, C_{2} → −j5 Ω: *use Norton's theorem (seen by L) to find i_{o}.*

$$Z_{N} = (−j10 + 5) ∥ (−j5) = 0.5 − j3.5 Ω;   short L:  I_{N} = \frac{10}{−j5} = j2 A$$

$$i_{o} = j2 × \frac{0.5 − j3.5}{0.5 − j3.5 + j5} = 4.472∠−63.43° A$$

:::ans
**(this design) i_{o} = 4.472∠−63.43° A** (design problem; full solve agrees)
:::

<div class="qhead"><span class="qn">B113 · Problem 10.66</span><span class="qt">AC Thevenin · mixed sin/cos, dependent source <span class="lvl plain">practice</span></span></div>

:::q
At terminals a-b, obtain Thevenin and Norton equivalent circuits for the network depicted in Fig. 10.109. Take ω = 10 rad/s.
:::

[[img:sd10_66|Fig. 10.109 (ω = 10: 10 mF → −j10, ½ H → j5)|w=50]]

Write both sources as cosines: 2 sin 10t = 2∠−90° A, 12 cos 10t = 12∠0° V. Node solve with a open: v_{o} = −0.198 − j2.076 V, V_{a} = 29.73 − j1.88 V. With a shorted: I_{sc} = −30.4 − j32.4 A.

$$Z_{th} = \frac{V_{oc}}{I_{sc}} = −0.427 + j0.517 Ω$$

:::ans
**V_{th} = 29.79∠−3.62° V, I_{N} = 44.43∠−133.18° A, Z_{th} = −0.427 + j0.517 Ω** (even problem; test-source solve agrees)
:::

<div class="qhead"><span class="qn">B114 · Problem 10.67</span><span class="qt">AC Thevenin + Norton · bridge <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin and Norton equivalent circuits at terminals a-b in the circuit of Fig. 10.110.
:::

[[img:sd10_67|Fig. 10.110|w=46]]

$$V_{a} = 60∠45° × \frac{10}{23 − j5} = 25.49∠57.26° V,   V_{b} = 60∠45° × \frac{8 + j6}{20 + j6} = 28.73∠65.17° V$$

$$V_{th} = V_{a} − V_{b} = 1.719 − j4.636 V,   Z_{th} = (13 − j5) ∥ 10 + 12 ∥ (8 + j6) = 11.243 + j1.079 Ω$$

:::ans
**V_{th} = 4.944∠−69.66° V, Z_{th} = 11.243 + j1.079 Ω, I_{N} = 0.4377∠−75.14° A** (= App. D to within 0.1°: it prints −69.76° and −75.24°)
:::

<div class="qhead"><span class="qn">B115 · Problem 10.68</span><span class="qt">AC Thevenin · dependent sources <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent at terminals a-b in the circuit of Fig. 10.111.
:::

[[img:sd10_68|Fig. 10.111 (ω = 10: \frac{1}{20} F → −j2, 1 H → j10)|w=50]]

The left node is held at v_{o}/3, so i_{o} = \frac{6 − v_{o}/3}{4}; the 4i_{o} drives −j2 ∥ j10 = −j2.5 Ω.

$$I_{sc}:  v_{o} = 0 ⇒ i_{o} = 1.5 A,  I_{N} = 6 A        V_{oc}:  v_{o} = 4 × \frac{6 − v_{o}/3}{4} × (−j2.5)  ⇒  v_{o} = \frac{−j15}{1 − j0.8333}$$

:::ans
**V_{th} = 11.52 sin(10t − 50.19°) V, Z_{th} = \frac{V_{th}}{I_{N}} = 1.230 − j1.475 Ω** (even problem; test-source solve agrees)
:::
