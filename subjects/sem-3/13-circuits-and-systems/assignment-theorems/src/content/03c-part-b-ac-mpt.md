## G · AC maximum average power (ch. 11 §11.3)

[[map:AC Thevenin (done) > Average power P = ½|V||I|cos θ > Max power: Z_{L} = Z_{th}^{*}, P_{max} = |V_{th}|^{2}/8R_{th}|here=3]]

**Where this sits.** Part A's section C gave the rule (Z_{L} = Z_{th}^{*}; R_{L} = |Z_{th}| when the load must be a pure resistance). Sadiku's chapter 11 figures give **peak** (amplitude) phasors, so the average power carries a ½:

$$P = \frac{1}{2}Re(VI^{*}) = \frac{1}{2}|I|^{2}R,   P_{max} = \frac{|V_{th}|^{2}}{8R_{th}}$$

(Part A used rms values, which drops the ½: |V|^{2}/4R.) Every answer below was also checked by sweeping the load on the full circuit.

<div class="qhead"><span class="qn">B116 · Practice Problem 11.4</span><span class="qt">Average power per element <span class="lvl light">new idea</span></span></div>

:::q
Calculate the average power absorbed by each of the five elements in the circuit of Fig. 11.6.
:::

[[img:sd_pp11_4|Fig. 11.6|w=50]]

:::new Hint: what's new
- **Average power of each element:** P = ½Re(VI^{*}) with I entering the + terminal. Inductors and capacitors absorb 0; a negative value for a source means it delivers power. The total over all elements is 0 (conservation).
:::

Node M (top of −j2): \frac{40 − V}{8} = \frac{V}{−j2} + \frac{V − j20}{j4} ⇒ V = 16 − j32 V.

$$I_{8} = \frac{40 − V}{8} = 3 + j4 A,   I_{j4} = \frac{V − j20}{j4} = −13 − j4 A$$

$$P_{8Ω} = \frac{1}{2}|3 + j4|^{2}(8) = 100 W,   P_{40V} = \frac{1}{2}Re[40(−I_{8})^{*}] = −60 W,   P_{j20V} = \frac{1}{2}Re[j20 · I_{j4}^{*}] = −40 W$$

:::ans
**40 V source: −60 W; j20 V source: −40 W; resistor: 100 W; inductor and capacitor: 0 W** (= book; total = 0)
:::

<div class="qhead"><span class="qn">B117 · Practice Problem 11.5</span><span class="qt">AC max power <span class="lvl plain">practice</span></span></div>

:::q
For the circuit shown in Fig. 11.10, find the load impedance Z_{L} that absorbs the maximum average power. Calculate that maximum average power.
:::

[[img:sd_pp11_5|Fig. 11.10|w=42]]

$$Z_{th} = (8 − j4 + j10) ∥ 5 = (8 + j6) ∥ 5 = 3.415 + j0.732 Ω$$

$$V_{th} = 12 × \frac{8 − j4}{8 − j4 + j10 + 5} × 5 = 37.48∠−51.34° V,   P_{max} = \frac{37.48^{2}}{8 × 3.415}$$

:::ans
**Z_{L} = 3.415 − j0.7317 Ω, P_{max} = 51.43 W** (= book to rounding; it prints 51.47 W)
:::

<div class="qhead"><span class="qn">B118 · Problem 11.12</span><span class="qt">AC max power <span class="lvl plain">practice</span></span></div>

:::q
For the circuit shown in Fig. 11.44, determine the load impedance Z for maximum power transfer (to Z). Calculate the maximum power absorbed by the load.
:::

[[img:sd11_12|Fig. 11.44|w=46]]

$$Z_{th} = 4 ∥ [(j2 ∥ 5) − j3] = 4 ∥ (0.690 − j1.276) = 0.823 − j0.864 Ω   (source shorted)$$

Node solve with Z removed: V_{th} = 159.22 − j50.10 = 166.9∠−17.47° V.

:::ans
**Z = 0.823 + j0.864 Ω, P_{max} = \frac{166.9^{2}}{8 × 0.823} = 4.230 kW** (even problem; sweep agrees)
:::

<div class="qhead"><span class="qn">B119 · Problem 11.13</span><span class="qt">AC max power · given the equivalent <span class="lvl plain">practice</span></span></div>

:::q
The Thevenin impedance of a source is Z_{Th} = 120 + j60 Ω, while the peak Thevenin voltage is V_{Th} = 165 + j0 V. Determine the maximum available average power from the source.
:::

$$P_{max} = \frac{|V_{th}|^{2}}{8R_{th}} = \frac{165^{2}}{8 × 120} = 28.36 W   (at Z_{L} = 120 − j60 Ω)$$

:::ans
**P_{max} = 28.36 W** (= App. D)
:::

<div class="qhead"><span class="qn">B120 · Problem 11.14</span><span class="qt">AC max power · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 11.45, design a problem to help other students better understand maximum average power transfer.
:::

[[img:sd11_14|Fig. 11.45; the box on the right is the load Z.|w=40]]

**One design.** i_{s} = 10 cos ωt A with jωL = j10 Ω, R_{1} = 10 Ω, C → −j5 Ω, R_{2} = 5 Ω: *find Z for maximum average power and that power.*

$$j10 ∥ 10 = 5 + j5;   Z_{th} = 5 + j5 − j5 + 5 = 10 Ω,   V_{th} = 10(5 + j5) = 70.71∠45° V,   P_{max} = \frac{70.71^{2}}{80} = 62.5 W$$

:::ans
**(this design) Z = 10 Ω, P_{max} = 62.5 W** (design problem)
:::

<div class="qhead"><span class="qn">B121 · Problem 11.15</span><span class="qt">AC max power · dependent source <span class="lvl plain">practice</span></span></div>

:::q
In the circuit of Fig. 11.46, find the value of Z_{L} that will absorb the maximum power and the value of the maximum power.
:::

[[img:sd11_15|Fig. 11.46|w=48]]

**V_{oc}.** The 2V_{o} entering the right node can only return through −j1, so the current from V_{o}'s node to the right node is −2V_{o}. KCL at V_{o}:

$$12 − V_{o} = \frac{V_{o}}{j1} − 2V_{o}  ⇒  12 = V_{o}(−1 − j1)  ⇒  V_{o} = −6 + j6 V$$

$$V_{th} = V_{o} − (−j1)(−2V_{o}) = V_{o}(1 − j2) = 6 + j18 V$$

**I_{sc}.** Right node grounded: the −j1 carries \frac{V_{o}}{−j1} = jV_{o}, and KCL at V_{o} gives 12 − V_{o} = −jV_{o} + jV_{o} = 0, so V_{o} = 12 V:

$$I_{sc} = jV_{o} + 2V_{o} = 24 + j12 A,   Z_{th} = \frac{6 + j18}{24 + j12} = 0.5 + j0.5 Ω$$

:::ans
**Z_{L} = 0.5 − j0.5 Ω, P_{max} = \frac{|6 + j18|^{2}}{8 × 0.5} = 90 W** (= App. D)
:::

<div class="qhead"><span class="qn">B122 · Problem 11.16</span><span class="qt">AC max power · dependent source <span class="lvl plain">practice</span></span></div>

:::q
For the circuit in Fig. 11.47, find the value of Z_{L} that will receive the maximum power from the circuit. Then calculate the power delivered to the load Z_{L}.
:::

[[img:sd11_16|Fig. 11.47 (ω = 4: \frac{1}{20} F → −j5, 1 H → j4)|w=52]]

Node solves at ω = 4 (v_{o} at the capacitor node, the 0.5v_{o} source carrying current from that node to the inductor node): V_{th} = 11.89∠56.31° V, Z_{th} = 1.670 + j3.648 Ω.

:::ans
**Z_{L} = 1.670 − j3.648 Ω, P = \frac{11.89^{2}}{8 × 1.670} = 10.57 W** (even problem; sweep agrees)
:::

<div class="qhead"><span class="qn">B123 · Problem 11.17</span><span class="qt">AC max power · bridge <span class="lvl plain">practice</span></span></div>

:::q
Calculate the value of Z_{L} in the circuit of Fig. 11.48 in order for Z_{L} to receive maximum average power. What is the maximum average power received by Z_{L}?
:::

[[img:sd11_17|Fig. 11.48|w=44]]

The 5∠90° A enters the top corner and leaves the bottom one, splitting between (−j10 + 40) on the left and (30 + j20) on the right:

$$I_{left} = j5 × \frac{30 + j20}{70 + j10} = −1.1 + j2.3 A,   I_{right} = j5 × \frac{40 − j10}{70 + j10} = 1.1 + j2.7 A$$

$$V_{th} = 40I_{left} − j20I_{right} = (−44 + j92) − (−54 + j22) = 10 + j70 V$$

$$Z_{th} = (30 − j10) ∥ (40 + j20) = \frac{1400 + j200}{70 + j10} = 20 Ω$$

:::ans
**Z_{L} = 20 Ω, P_{max} = \frac{|10 + j70|^{2}}{8 × 20} = 31.25 W** (= App. D)
:::

<div class="qhead"><span class="qn">B124 · Problem 11.18</span><span class="qt">AC max power <span class="lvl plain">practice</span></span></div>

:::q
Find the value of Z_{L} in the circuit of Fig. 11.49 for maximum power transfer.
:::

[[img:sd11_18|Fig. 11.49|w=46]]

With the 60 V shorted the top rail and the middle node merge; with the 5 A opened:

$$Z_{th} = (−j10 ∥ 80) + (40 ∥ 40) + j30 = (1.231 − j9.846) + 20 + j30 = 21.23 + j20.15 Ω$$

:::ans
**Z_{L} = 21.23 − j20.15 Ω** (even problem; then V_{th} = 159.3∠63.56° V and P_{max} = 149.4 W)
:::

<div class="qhead"><span class="qn">B125 · Problem 11.19</span><span class="qt">AC max power · resistive load <span class="lvl plain">practice</span></span></div>

:::q
The variable resistor R in the circuit of Fig. 11.50 is adjusted until it absorbs the maximum average power. Find R and the maximum average power absorbed.
:::

[[img:sd11_19|Fig. 11.50|w=44]]

$$(3 + j1) ∥ 6 = 2.049 + j0.439 Ω,   V_{th} = 33 × (2.049 + j0.439) = 69.14∠12.09° V,   Z_{th} = 2.049 − j1.561 Ω$$

$$R = |Z_{th}| = 2.576 Ω,   P = \frac{1}{2}\frac{|V_{th}|^{2}}{|Z_{th} + R|^{2}}R = \frac{1}{2} × \frac{4781}{4.625^{2} + 1.561^{2}} × 2.576$$

:::ans
**R = 2.576 Ω, P_{max} = 258.5 W** (= App. D)
:::

<div class="qhead"><span class="qn">B126 · Problem 11.20</span><span class="qt">AC max power · resistive load, dependent source <span class="lvl plain">practice</span></span></div>

:::q
The load resistance R_{L} in Fig. 11.51 is adjusted until it absorbs the maximum average power. Calculate the value of R_{L} and the maximum average power.
:::

[[img:sd11_20|Fig. 11.51|w=52]]

Node solves (4I_{o} is a CCVS between the two capacitor nodes): V_{th} = 25.98∠−92.43° V, Z_{th} = 1.049 − j6.711 Ω.

$$R_{L} = |Z_{th}| = 6.793 Ω,   P = \frac{1}{2}\frac{25.98^{2}}{|1.049 + 6.793 − j6.711|^{2}} × 6.793$$

:::ans
**R_{L} = 6.793 Ω, P_{max} = 21.51 W** (even problem; sweep agrees)
:::

<div class="qhead"><span class="qn">B127 · Problem 11.21</span><span class="qt">AC max power · resistive load <span class="lvl plain">practice</span></span></div>

:::q
Assuming that the load impedance is to be purely resistive, what load should be connected to terminals a-b of the circuits in Fig. 11.52 so that the maximum power is transferred to the load?
:::

[[img:sd11_21|Fig. 11.52|w=52]]

$$100 ∥ (40 + j30) = 31.71 + j14.63 Ω;   − j10 ⇒ 31.71 + j4.63;   ∥ 50 ⇒ Z_{th} = 19.50 + j1.73 Ω$$

:::ans
**R_{L} = |Z_{th}| = 19.58 Ω** (= App. D; with it the load takes 26.47 W)
:::
