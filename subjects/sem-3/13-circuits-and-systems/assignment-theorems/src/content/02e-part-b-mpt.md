## D · Maximum power transfer (§4.8)

[[map:Thevenin / Norton (done) > Max power: R_{L} = R_{th}, P_{max} = V_{th}^{2}/4R_{th} > Chapter 10 AC versions (later)|here=2]]

**Where this sits.** Part A, section C covered the theorem. Every problem below is: find V_{th} and R_{th} at the load's terminals, then R_{L} = R_{th}. Each answer was also checked by sweeping the load resistance on the full circuit and finding the peak.

<div class="qhead"><span class="qn">B69 · Practice Problem 4.13</span><span class="qt">Max power · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Determine the value of R_{L} that will draw the maximum power from the rest of the circuit in Fig. 4.52. Calculate the maximum power.
:::

[[img:sd_pp4_13|Fig. 4.52|w=40]]

**V_{oc}.** No current in the 4 Ω, so V_{th} = V_{M}; v_{x} = 9 − V_{M}:

$$\frac{9 − V_{M}}{2} = V_{M} − 3(9 − V_{M})  ⇒  9V_{M} = 63  ⇒  V_{th} = 7 V$$

**I_{sc}.**

$$\frac{9 − V_{M}}{2} = V_{M} − 3(9 − V_{M}) + \frac{V_{M}}{4}  ⇒  V_{M} = 6.632 V,   I_{sc} = \frac{V_{M}}{4} = 1.658 A$$

$$R_{L} = R_{th} = \frac{7}{1.658} = 4.222 Ω,   P_{max} = \frac{49}{4 × 4.222} = 2.901 W$$

:::ans
**R_{L} = 4.222 Ω, P_{max} = 2.901 W** (= book)
:::

<div class="qhead"><span class="qn">B70 · Problem 4.66</span><span class="qt">Max power · R between two nodes <span class="lvl plain">practice</span></span></div>

:::q
Find the maximum power that can be delivered to the resistor R in the circuit of Fig. 4.132.
:::

[[img:sd4_66|Fig. 4.132|w=46]]

$$R_{th} = 2 ∥ (3 + 5) = 1.6 Ω   (looking in across R, sources off)$$

**V_{th}.** With R removed, one loop current i through 3 Ω and 2 Ω; the 5 Ω carries i − 6:

$$20 = 3i + 2i − 10 + 5(i − 6)  ⇒  i = 6 A  ⇒  V_{B} = 0,  V_{A} = 20 − 18 = 2 V$$

:::ans
**P_{max} = \frac{2^{2}}{4 × 1.6} = 0.625 W** (at R = 1.6 Ω; even problem, sweep agrees)
:::

<div class="qhead"><span class="qn">B71 · Problem 4.67</span><span class="qt">Max power · bridge <span class="lvl plain">practice</span></span></div>

:::q
The variable resistor R in Fig. 4.133 is adjusted until it absorbs the maximum power from the circuit. (a) Calculate the value of R for maximum power. (b) Determine the maximum power absorbed by R.
:::

[[img:sd4_67|Fig. 4.133|w=44]]

The 40 V sits across the left and right corners. Shorted, those corners merge:

$$R_{th} = (80 ∥ 20) + (10 ∥ 90) = 16 + 9 = 25 Ω$$

$$V_{top} − V_{right} = 40 × \frac{20}{100} = 8 V,   V_{bottom} − V_{right} = 40 × \frac{90}{100} = 36 V,   V_{th} = −28 V$$

:::ans
**(a) R = 25 Ω  (b) P_{max} = \frac{28^{2}}{100} = 7.84 W** (= App. D)
:::

<div class="qhead"><span class="qn">B72 · Problem 4.68</span><span class="qt">Max power · the trap <span class="lvl light">new idea</span></span></div>

:::q
Compute the value of R that results in maximum power transfer to the 10-Ω resistor in Fig. 4.134. Find the maximum power.
:::

[[img:sd4_68|Fig. 4.134|w=40]]

:::new Hint: what's new
- **The theorem picks the load, not the source.** Here the fixed element (10 Ω) is the load and R is part of the source side. Matching R_{L} = R_{th} does not apply; instead ask how the 10 Ω's current changes as R grows.
:::

Node above the 10 Ω: \frac{12 − V}{R} = \frac{V − 8}{10} + \frac{V}{20}. As R grows from 0, V falls from 12 V towards 5.33 V, so the 10 Ω current (V − 8)/10 falls from 0.4 A through zero to −0.267 A. Its magnitude is largest at R = 0:

$$R = 0:  V = 12 V,   i_{10} = 0.4 A,   P = 0.4^{2} × 10 = 1.6 W$$

:::ans
**R = 0 Ω, P_{max} = 1.6 W** (even problem; a sweep of R confirms)
:::

<div class="qhead"><span class="qn">B73 · Problem 4.69</span><span class="qt">Max power · negative R_{th} <span class="lvl light">new idea</span></span></div>

:::q
Find the maximum power transferred to resistor R in the circuit of Fig. 4.135.
:::

[[img:sd4_69|Fig. 4.135|w=52]]

:::new Hint: what's new
- **Negative R_{th}.** If R_{th} < 0, the load current V_{th}/(R_{th} + R) has no finite maximum: it blows up as R → |R_{th}|. That is the book's "∞ (theoretically)". A real circuit would leave its linear range first.
:::

$$I_{sc}:  \frac{100 − v_{o}}{10k} = \frac{v_{o}}{40k} + \frac{v_{o}}{22k}  ⇒  v_{o} = 58.67 V,   I_{sc} = \frac{v_{o}}{22k} + 0.003v_{o} = 0.1787 A$$

$$V_{oc} = −243.6 V (two node equations),   R_{th} = \frac{−243.6}{0.1787} = −1363.6 Ω$$

:::ans
**P → ∞ as R → 1363.6 Ω** (= App. D, "∞ (theoretically)")
:::

<div class="qhead"><span class="qn">B74 · Problem 4.70</span><span class="qt">Max power · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Determine the maximum power delivered to the variable resistor R shown in the circuit of Fig. 4.136.
:::

[[img:sd4_70|Fig. 4.136|w=40]]

**V_{th}.** With R removed, nothing flows in the 6 Ω, so V_{x} = 0 and the dependent source is off. Then the right 5 Ω carries nothing either: V_{th} = V_{A} = 4 × \frac{15}{20} = 3 V.

**R_{th}** (4 V shorted, test current I_{t} in at the top of R, out at the bottom). The 6 Ω carries I_{t}, so V_{x} = 6I_{t} and the source is 18I_{t}:

$$5 Ω carries I_{t} + 18I_{t} = 19I_{t};   A sits on 5 ∥ 15 = 3.75 Ω carrying I_{t}$$

$$V = 95I_{t} + 3.75I_{t} + 6I_{t} = 104.75I_{t}  ⇒  R_{th} = 104.75 Ω$$

:::ans
**R = 104.75 Ω, P_{max} = \frac{3^{2}}{4 × 104.75} = 21.5 mW** (even problem; sweep agrees)
:::

<div class="qhead"><span class="qn">B75 · Problem 4.71</span><span class="qt">Max power · amplifier model <span class="lvl plain">practice</span></span></div>

:::q
For the circuit in Fig. 4.137, what resistor connected across terminals a-b will absorb maximum power from the circuit? What is that power?
:::

[[img:sd4_71|Fig. 4.137|w=50]]

$$v_{o} = 8 × \frac{1}{4} = 2 V,   source = −120v_{o} = −240 V (+ at the bottom)$$

$$V_{th} = −240 × \frac{40}{50} = −192 V,   R_{th} = 10k ∥ 40k = 8 kΩ,   P_{max} = \frac{192^{2}}{32000}$$

:::ans
**R = 8 kΩ, P_{max} = 1.152 W** (= App. D)
:::

<div class="qhead"><span class="qn">B76 · Problem 4.72</span><span class="qt">Thevenin + max power <span class="lvl plain">practice</span></span></div>

:::q
(a) For the circuit in Fig. 4.138, obtain the Thevenin equivalent at terminals a-b. (b) Calculate the current in R_{L} = 8 Ω. (c) Find R_{L} for maximum power deliverable to R_{L}. (d) Determine that maximum power.
:::

[[img:sd4_72|Fig. 4.138|w=46]]

$$R_{th} = 6 + (4 + 2) = 12 Ω$$

With a–b open, the 4 A sets the middle node at 4 × 2 = 8 V; the 2 A circulates through the 6 Ω, so V_{a} = 8 + 12 = 20 V; b sits at −20 V.

$$V_{th} = 40 V,   i_{8Ω} = \frac{40}{12 + 8} = 2 A,   P_{max} = \frac{40^{2}}{4 × 12} = 33.33 W$$

:::ans
**(a) 40 V, 12 Ω  (b) 2 A  (c) R_{L} = 12 Ω  (d) 33.33 W** (even problem; full solves agree)
:::

<div class="qhead"><span class="qn">B77 · Problem 4.73</span><span class="qt">Max power · bridge <span class="lvl plain">practice</span></span></div>

:::q
Determine the maximum power that can be delivered to the variable resistor R in the circuit of Fig. 4.139.
:::

[[img:sd4_73|Fig. 4.139|w=44]]

$$V_{left} = 60 × \frac{20}{30} = 40 V,   V_{right} = 60 × \frac{5}{30} = 10 V,   V_{th} = 30 V$$

$$R_{th} = 10 ∥ 20 + 25 ∥ 5 = 6.667 + 4.167 = 10.83 Ω$$

:::ans
**P_{max} = \frac{30^{2}}{4 × 10.83} = 20.77 W** (= App. D)
:::

<div class="qhead"><span class="qn">B78 · Problem 4.74</span><span class="qt">Max power · symbolic bridge <span class="lvl plain">practice</span></span></div>

:::q
For the bridge circuit shown in Fig. 4.140, find the load R_{L} for maximum power transfer and the maximum power absorbed by the load.
:::

[[img:sd4_74|Fig. 4.140|w=36]]

With v_{s} shorted the top and bottom rails merge:

$$R_{L} = R_{th} = \frac{R_{1}R_{2}}{R_{1} + R_{2}} + \frac{R_{3}R_{4}}{R_{3} + R_{4}},   V_{th} = v_{s}(\frac{R_{2}}{R_{1} + R_{2}} − \frac{R_{4}}{R_{3} + R_{4}})$$

:::ans
**R_{L} = R_{1} ∥ R_{2} + R_{3} ∥ R_{4},  P_{max} = \frac{V_{th}^{2}}{4R_{th}}** with V_{th} as above (even problem; checked numerically for sample values)
:::

<div class="qhead"><span class="qn">B79 · Problem 4.75</span><span class="qt">Max power · design R <span class="lvl plain">practice</span></span></div>

:::q
For the circuit in Fig. 4.141, determine the value of R such that the maximum power delivered to the load is 3 mW.
:::

[[img:sd4_75|Fig. 4.141; the three R's all meet at the top terminal.|w=48]]

$$V_{th} = \frac{1 + 2 + 3}{3} = 2 V,   R_{th} = \frac{R}{3},   P_{max} = \frac{4}{4R/3} = \frac{3}{R} = 3 × 10^{−3}$$

:::ans
**R = 1 kΩ** (= App. D; the load is then R_{L} = R/3 = 333.3 Ω)
:::

:::note Reading the figure
The wire from the top R crosses the middle R's wire with no dot. The book's answer (1 kΩ) requires all three R's to meet at the output node; if only the middle R reached it, R would be 333 Ω.
:::
