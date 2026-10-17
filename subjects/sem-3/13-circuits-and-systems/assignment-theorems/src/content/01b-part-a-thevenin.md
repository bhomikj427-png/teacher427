## B · Thevenin's and Norton's theorems

[[map:Superposition: one source at a time (done) > Thevenin: whole network → one source + one impedance > Norton: the same as a current source > Maximum power transfer (next)|here=2]]

**Where this sits.** Superposition showed that a linear circuit's response is a sum of simple parts. Thevenin's theorem uses that fact to shrink everything a load is connected to into **two numbers**, so changing the load never means re-solving the whole circuit.

**Three terms first.**

- **Terminals a–b:** the two points where the load connects. Everything on the other side of them is the **network**.
- **Open-circuit voltage V_{oc}:** the voltage across a–b with the load removed (nothing connected).
- **Short-circuit current I_{sc}:** the current through a wire placed across a–b, counted **from a to b through the wire** (out of the + terminal).

**Statement.** Seen from a–b, any linear network behaves exactly like **one voltage source V_{th} = V_{oc} in series with one impedance Z_{th}**. Norton's form is the same network as **one current source I_{N} = I_{sc} in parallel with Z_{N} = Z_{th}**. The two forms are a source transformation of each other: V_{th} = I_{N}Z_{th}.

**Finding Z_{th}: three cases.**

| The network contains | Z_{th} is found by |
|---|---|
| Independent sources only | switch every source off (V → short, I → open), then combine impedances seen from a–b |
| Independent **and** dependent sources | Z_{th} = V_{oc} / I_{sc}, or switch off the independent sources only and apply a test source |
| Dependent sources only | V_{th} = 0; apply a test source (1 A in, measure V): Z_{th} = V / I |

With dependent sources Z_{th} can come out **negative** (the network supplies energy). Keep the sign of I_{sc}: it decides the sign of Z_{th}.

<div class="qhead"><span class="qn">A15 · Problem 5.15</span><span class="qt">Thevenin · DC <span class="lvl heavy">teach</span></span></div>

:::q
Draw the Thevenin's equivalent of the circuit in the figure and find the load current i. All values are in ohm.
:::

[[img:ck5_15|i flows down through R = 2 Ω.|w=62]]

:::try
Remove R. Find the voltage across its terminals (two meshes), then short both sources and find the resistance seen from there. Last, put R back on the equivalent.
:::

:::new Hint: what's new
- **The Thevenin recipe:** (1) remove the load; (2) V_{th} = open-circuit voltage at its terminals; (3) R_{th} = resistance seen into the terminals with every independent source switched off; (4) load current = V_{th} / (R_{th} + R_{L}).
- **Switching off for R_{th}** uses the same rule as superposition: voltage sources become shorts.
:::

[[img:ck5_15s1|Load removed: two mesh currents, V_{oc} across the open terminals|w=58]]

**Given:** 10 V, 5 V; 1 Ω (series with 10 V), 1 Ω, 1 Ω, 2 Ω; R = 2 Ω. **To find:** V_{th}, R_{th}, i.

**Step 1: V_{th}** (R removed). Mesh currents clockwise:

$$Mesh 1:  3i_{1} − i_{2} = 10        Mesh 2:  −i_{1} + 4i_{2} = −5$$

$$⇒  i_{1} = \frac{35}{11} A,   i_{2} = −\frac{5}{11} A$$

$$V_{th} = V_{oc} = 5 + 2i_{2} = 5 − \frac{10}{11} = \frac{45}{11} = 4.091 V$$

[[img:ck5_15s2|Both sources shorted: R_{th} seen from the load terminals|w=80]]

**Step 2: R_{th}** (both sources shorted):

$$(1 + 1) ∥ 1 = \frac{2}{3} Ω,   \frac{2}{3} + 1 = \frac{5}{3} Ω,   R_{th} = \frac{5}{3} ∥ 2 = \frac{10}{11} = 0.909 Ω$$

**Step 3: load current:**

$$i = \frac{V_{th}}{R_{th} + R} = \frac{45/11}{10/11 + 2} = \frac{45}{32} A$$

:::ans
**Thevenin equivalent: 45/11 V in series with 10/11 Ω.  i = 1.406 A** (= book)
:::

:::note Side note
The book prints i_{1} = 5/11; it is 35/11 (only i_{2} is used, so the answer is unaffected). Full node solve with R in place: i = 1.40625 A ✓.
:::

<div class="qhead"><span class="qn">A16 · Problem 5.16</span><span class="qt">Thevenin · dependent source <span class="lvl heavy">teach</span></span></div>

:::q
Find I in the given figure, using Thevenin's theorem.
:::

[[img:ck5_16|3V_{0} is a voltage-controlled voltage source; V_{0} is across the 1 Ω (+ on the right).|w=45]]

:::try
The dependent source cannot be switched off, so R_{th} must come from V_{oc} / I_{sc}. Find both, and keep the sign of I_{sc}.
:::

:::new Hint: what's new
- **Dependent source ⇒ R_{th} = V_{oc} / I_{sc}** (or a test source). Shorting the independent sources and combining resistors would ignore the dependent source.
- **I_{sc} is measured from x to y through the short.** A negative I_{sc} gives a **negative R_{th}**, which is allowed: the dependent source can supply energy.
:::

[[img:ck5_16s|Top: terminals x–y open (V_{oc}). Bottom: x–y shorted (I_{sc}).|w=42]]

**Given:** 10 V, 1 A, 1 Ω, VCVS 3V_{0}, load 2 Ω. **To find:** I.

**V_{oc}** (2 Ω removed). Nothing leaves at x, so the 1 A must flow left through the 1 Ω: V_{0} = 1 × 1 = 1 V.

$$V_{a} = 10 + V_{0} = 11 V,   V_{oc} = V_{a} − 3V_{0} = 11 − 3 = 8 V$$

**I_{sc}** (x shorted to y, so V_{x} = 0):

$$0 = V_{a} − 3V_{0} = (10 + V_{0}) − 3V_{0}  ⇒  V_{0} = 5 V$$

$$KCL at a:  1 = \frac{V_{0}}{1} + I_{sc}  ⇒  I_{sc} = 1 − 5 = −4 A$$

$$R_{th} = \frac{V_{oc}}{I_{sc}} = \frac{8}{−4} = −2 Ω$$

**Load:** R_{th} + 2 Ω = −2 + 2 = 0, so

$$I = \frac{V_{th}}{R_{th} + 2} = \frac{8}{0}  ⇒  no finite solution$$

:::ans
**V_{th} = 8 V, R_{th} = −2 Ω. With the 2 Ω load, R_{th} + R_{L} = 0: the circuit as drawn has no solution.** (Book: 2 A.)
:::

:::trap Book error in 5.16
The book finds I_{sc} = −4 A, then writes R_{th} = 8/4 = 2 Ω, dropping the minus sign, and prints I = 2 A. Direct check with the 2 Ω in place: KCL at a gives V_{0} = 1 − I; the right-hand path gives V_{x} = 10 − 2V_{0} = 8 + 2I; but V_{x} = 2I, so 8 = 0, a contradiction. A test source (10 V shorted, 1 A opened, 1 A pushed into x) confirms R_{th} = −2 Ω. For any other load, I = \frac{8}{R_{L} − 2}.
:::

<div class="qhead"><span class="qn">A17 · Problem 5.17</span><span class="qt">Thevenin · repeated reduction <span class="lvl light">new idea</span></span></div>

:::q
By the iterative use of Thevenin's theorem, reduce the circuit shown in the figure to a single emf acting in series with a single resistor. Hence, calculate the current in the 10 Ω resistor connected across XY.
:::

[[img:ck5_17|Ladder network; the load is the 10 Ω across XY.|w=78]]

:::try
Cut the ladder just right of the first shunt resistor and replace the left part by its Thevenin equivalent. Repeat, one rung at a time.
:::

:::new Hint: what's new
- **Iterative Thevenin:** a ladder is reduced rung by rung. Each step is a voltage divider for V_{th} and a parallel combination for R_{th}: V_{new} = V_{old} × \frac{R_{sh}}{R_{old} + R_{series} + R_{sh}},  R_{new} = (R_{old} + R_{series}) ∥ R_{sh}.
:::

**Step 1** (left of AB: 100 V behind 90 + 10 = 100 Ω, shunt 1000 Ω):

$$V_{1} = 100 × \frac{1000}{1100} = \frac{1000}{11} V,   R_{1} = 100 ∥ 1000 = \frac{1000}{11} Ω$$

[[img:ck5_17s1|After step 1|w=66]]

**Step 2** (add 100 Ω series, shunt 10 Ω):

$$V_{2} = \frac{1000}{11} × \frac{10}{2100/11 + 10} = \frac{1000}{221} V,   R_{2} = \frac{2100}{11} ∥ 10 = \frac{2100}{221} Ω$$

[[img:ck5_17s2|After step 2|w=52]]

**Step 3** (add 100 Ω series, shunt 100 Ω):

$$V_{3} = \frac{1000}{221} × \frac{100}{24200/221 + 100} = \frac{1000}{463} V,   R_{3} = \frac{24200}{221} ∥ 100 = \frac{24200}{463} Ω$$

[[img:ck5_17s3|After step 3, with the 1000 Ω still in series|w=52]]

**Step 4** (add 1000 Ω series):

$$V_{th} = \frac{1000}{463} = 2.160 V,   R_{th} = \frac{24200}{463} + 1000 = \frac{487200}{463} = 1052.3 Ω$$

$$I = \frac{1000/463}{487200/463 + 10} = \frac{1000}{491830} A$$

:::ans
**Single emf 2.160 V in series with 1052.3 Ω;  I = 2.03 mA ≈ 0.002 A** (= book)
:::

<div class="qhead"><span class="qn">A18 · Problem 5.18</span><span class="qt">Thevenin · op-amp, test source <span class="lvl light">new idea</span></span></div>

:::q
In the operational-amplifier circuit shown in the figure, find I in the R = 4 kΩ resistor, using Thevenin's theorem.
:::

[[img:ck5_18|Ideal op-amp; the load is R = 4 kΩ from node e_{1} to ground.|w=60]]

:::try
With R removed, write KCL at e_{1} and at the inverting input. For R_{th}, short the 12 V and push 1 A into e_{1}.
:::

:::new Hint: what's new
- **Ideal op-amp rules:** no current into its inputs, and (with negative feedback) e_{2} = e_{+} = 0 V. The output can supply any current, so **no KCL is written at the output node**.
- **Test source for R_{th}:** the op-amp acts like a dependent source, so switch off the 12 V only, inject 1 A at the terminals and read the voltage: R_{th} = e_{1} / 1 A.
:::

**Given:** 12 V, 2 kΩ, 4 kΩ (feedback e_{1} → V_{0}), 8 kΩ, 12 kΩ, ideal op-amp. **To find:** I in R = 4 kΩ.

**V_{th}** (R removed; e_{2} = 0, e_{3} = V_{0}):

$$KCL at e_{2}:  \frac{0 − e_{1}}{8k} + \frac{0 − V_{0}}{12k} = 0  ⇒  V_{0} = −\frac{3}{2}e_{1}$$

$$KCL at e_{1}:  \frac{e_{1} − 12}{2k} + \frac{e_{1} − V_{0}}{4k} + \frac{e_{1}}{8k} = 0  ⇒  7e_{1} = 48 + 2V_{0}$$

$$7e_{1} = 48 − 3e_{1}  ⇒  V_{th} = e_{1} = 4.8 V$$

[[img:ck5_18s|12 V shorted, 1 A test source at the load terminals|w=60]]

**R_{th}** (12 V shorted, 1 A injected at e_{1}):

$$\frac{e_{1}}{2k} + \frac{e_{1} − V_{0}}{4k} + \frac{e_{1}}{8k} = 1  ⇒  7e_{1} − 2V_{0} = 8000$$

$$10e_{1} = 8000  ⇒  e_{1} = 800 V$$

$$R_{th} = \frac{800 V}{1 A} = 800 Ω,   I = \frac{4.8}{800 + 4000} = 1 × 10^{−3} A$$

:::ans
**V_{th} = 4.8 V, R_{th} = 800 Ω, I = 1 mA** (= book)
:::

<div class="qhead"><span class="qn">A19 · Problem 5.19</span><span class="qt">Thevenin · dependent current source <span class="lvl plain">practice</span></span></div>

:::q
Find Thevenin's equivalent about AB for the circuit shown in the figure.
:::

[[img:ck5_19|The 4 Ω across AB is the load (the book removes it).|w=48]]

:::try
V_{oc}: with AB open, what does KCL at the middle node say about V_{s}? Then short AB for I_{sc}.
:::

[[img:ck5_19s1|AB open|w=42]]

**V_{oc}** (AB open, so the series 4 Ω carries nothing; V_{s} = 10 − V_{M}). KCL at the middle node M:

$$\frac{V_{s}}{2} + 4V_{s} = 0  ⇒  V_{s} = 0  ⇒  V_{oc} = V_{M} = 10 V$$

[[img:ck5_19s2|AB shorted|w=42]]

**I_{sc}** (AB shorted; V_{1} = V_{M}, V_{s} = 10 − V_{1}):

$$\frac{V_{1} − 10}{2} + \frac{V_{1}}{4} = 4(10 − V_{1})  ⇒  19V_{1} = 180  ⇒  V_{1} = 9.474 V$$

$$I_{sc} = \frac{V_{1}}{4} = 2.368 A$$

$$R_{th} = \frac{10}{2.368} = 4.22 Ω$$

:::ans
**V_{th} = 10 V, R_{th} = 38/9 = 4.22 Ω** (= book)
:::

:::note Side note
The 2 Ω in series with the dependent current source never matters (5.1's shortcut). Test-source check (10 V shorted, 1 A into A): V_{A} = 4 + \frac{1}{4.5} = 4.22 V ⇒ R_{th} = 4.22 Ω ✓.
:::

<div class="qhead"><span class="qn">A20 · Problem 5.20</span><span class="qt">Thevenin · AC, floating terminals <span class="lvl light">new idea</span></span></div>

:::q
In the network, determine the steady current in the 8 Ω inductor using Thevenin's theorem.
:::

[[img:ck5_20|The load is the j8 Ω between a and b.|w=78]]

:::try
With j8 removed, the circuit splits into two separate halves. Find V_{a} and V_{b} with a divider each.
:::

:::new Hint: what's new
- **Neither terminal is ground.** V_{th} = V_{a} − V_{b}, each found from its own half.
- With the sources shorted, each half is a parallel pair, and the two pairs are **in series** between a and b.
:::

[[img:ck5_20s|j8 Ω removed: two independent halves|w=78]]

$$V_{a} = 100∠0° × \frac{−j8}{j4 − j8} = 200∠0° V,   V_{b} = 100∠60° × \frac{−j6}{j4 − j6} = 300∠60° V$$

$$V_{th} = V_{a} − V_{b} = 200 − (150 + j259.81) = 50 − j259.81 = 264.58∠−79.11° V$$

$$Z_{th} = \frac{(j4)(−j8)}{j4 − j8} + \frac{(j4)(−j6)}{j4 − j6} = j8 + j12 = j20 Ω$$

$$i = \frac{V_{th}}{Z_{th} + j8} = \frac{264.58∠−79.11°}{28∠90°}$$

:::ans
**i = 9.45∠−169.11° A (a → b)** (= book)
:::

<div class="qhead"><span class="qn">A21 · Problem 5.21</span><span class="qt">Thevenin / Norton · AC, s-domain, dependent source <span class="lvl light">new idea</span></span></div>

:::q
Obtain Thevenin's equivalent circuit with respect to terminals A–B in the networks shown below.
:::

:::try
(a)–(c) are practice. In (d), treat s like jω. In (e) the dependent source stays, so use V_{oc} / I_{sc}.
:::

:::new Hint: what's new
- **(d) s-domain:** impedances are R, sL and \frac{1}{sC}; the source becomes its Laplace transform, 2 cos 2t → \frac{2s}{s^{2} + 4}. Everything else is unchanged.
- **(e) AC with a dependent source:** find V_{th} and I_{N} separately; Z_{th} = V_{th} / I_{N}.
:::

**(a)**

[[img:ck5_21a||w=46]]

Source transformation: 10∠0° A ∥ j15 Ω → j150 V in series with j15 Ω. With AB open, one loop:

$$I = \frac{j150}{j15 + 2 − j5 + 3} = \frac{j150}{5 + j10} = 13.42∠26.57° A,   V_{th} = I × (−j5) = 30 − j60 V$$

$$Z_{th} = (−j5) ∥ (5 + j15) = \frac{−j5(5 + j15)}{5 + j10} = 1 − j7 Ω$$

:::ans
**(a) V_{th} = 67.08∠−63.43° V, Z_{th} = 7.07∠−81.87° Ω** (= book)
:::

**(b)**

[[img:ck5_21b||w=46]]

$$V_{th} = 20∠90° × \frac{3 − j4}{(5 + j10) + (3 − j4)} = \frac{j20(3 − j4)}{8 + j6} = \frac{100∠36.87°}{10∠36.87°} = 10∠0° V$$

$$Z_{th} = \frac{(5 + j10)(3 − j4)}{8 + j6} = \frac{55 + j10}{8 + j6} = 5 − j2.5 Ω$$

:::ans
**(b) V_{th} = 10∠0° V, Z_{th} = 5.59∠−26.57° Ω** (= book; its first line prints j120, a typo for j20)
:::

**(c)** The 4 Ω across AB is the load.

[[img:ck5_21c||w=52]]

$$Z = 10 + (−j5) ∥ (13 + j6) = 11.91 − j5.15 = 12.98∠−23.37° Ω$$

$$I = \frac{100}{Z} = 7.706∠23.37° A$$

$$I_{right} = I × \frac{−j5}{13 + j1} = 2.955∠−71.03° A,   V_{th} = I_{right}(8 + j6) = 29.55∠−34.16° V$$

$$Z_{th} = [(10 ∥ −j5) + 5] ∥ (8 + j6) = (7 − j4) ∥ (8 + j6) = 5.328 − j0.044 Ω$$

:::ans
**(c) V_{th} = 29.55∠−34.16° V, Z_{th} = 5.33∠−0.47° Ω** (= book)
:::

**(d)**

[[img:ck5_21d||w=52]]

The two \frac{1}{4} F capacitors both run from the same node to ground, so they add: \frac{1}{2} F → \frac{2}{s}. A is the node after the inductor; B is ground.

[[img:ck5_21ds|Redrawn in the s-domain|w=40]]

$$V_{th}(s) = \frac{2s}{s^{2} + 4} × \frac{1 + 2/s}{(1 + 2/s) + (1 + s/2)} = \frac{2s}{s^{2} + 4} × \frac{2}{s + 2} = \frac{4s}{(s^{2} + 4)(s + 2)}$$

(Simplify: 1 + 2/s = \frac{s + 2}{s} and 2 + s/2 + 2/s = \frac{(s + 2)^{2}}{2s}, so the ratio is \frac{2}{s + 2}.)

$$Z_{th}(s) = (1 + 2/s) ∥ (1 + s/2) = \frac{(s + 2)^{2}/(2s)}{(s + 2)^{2}/(2s)} = 1 Ω$$

:::ans
**(d) V_{th}(s) = \frac{4s}{(s^{2} + 4)(s + 2)} V, Z_{th} = 1 Ω** (= book)
:::

**(e)**

[[img:ck5_21e|I flows through the 100 Ω; the dependent source 5I points from A towards the middle node.|w=52]]

[[img:ck5_21es1|AB open|w=52]]

**V_{th}.** With AB open, the 5I circulates only through the −j5 Ω, so the source current is set by the left loop alone:

$$I = \frac{10∠0°}{100 + j10} = 0.0995∠−5.71° A$$

$$V_{th} = V_{AB} = I(j10) − 5I(−j5) = j35I = 3.483∠84.29° V$$

[[img:ck5_21es2|AB shorted, with 5I ∥ −j5 transformed to −j25I in series with −j5|w=52]]

**I_{N}.** AB shorted. Right loop: j10(I − I_{N}) + j25I + j5I_{N} = 0 ⇒ I_{N} = 7I. Left loop:

$$10 = (100 + j10)I − j10I_{N} = (100 − j60)I  ⇒  I = 0.0857∠30.96° A$$

$$I_{N} = 7I = 0.600∠30.96° A$$

$$Z_{th} = \frac{V_{th}}{I_{N}} = \frac{3.483∠84.29°}{0.600∠30.96°} = 5.80∠53.33° Ω$$

:::ans
**(e) V_{th} = 3.48∠84.3° V, I_{N} = 0.600∠31.0° A, Z_{th} = 5.80∠53.3° Ω** (= book)
:::

<div class="qhead"><span class="qn">A22 · Problem 5.22</span><span class="qt">Thevenin · AC, dependent source <span class="lvl plain">practice</span></span></div>

:::q
Find V_{0} using Thevenin's theorem.
:::

[[img:ck5_22|ω = 1 rad/s. The source's + is at the bottom; i_{0} flows right through the 4 Ω.|w=62]]

:::try
ω = 1: work out the three reactances first. Transform 3i_{0} ∥ j2 into a voltage source, then write two mesh equations for each of V_{th} and I_{N}.
:::

[[img:ck5_22s1|2 Ω removed; 3i_{0} ∥ j2 Ω → j6i_{0} in series with j2 Ω (+ on the right)|w=62]]

**Reactances (ω = 1):** 2 H → j2 Ω, \frac{1}{4} F → −j4 Ω, \frac{1}{8} F → −j8 Ω.

**V_{th}** (2 Ω removed; clockwise mesh currents, i_{0} = I_{1}):

$$Mesh 1:  (4 − j4)I_{1} + j4I_{2} = −12$$

$$Mesh 2:  −j4(I_{2} − I_{1}) + j2I_{2} − j6I_{1} − j8I_{2} = 0  ⇒  −j2I_{1} − j10I_{2} = 0  ⇒  I_{2} = −0.2I_{1}$$

$$(4 − j4.8)I_{1} = −12  ⇒  I_{1} = −1.230 − j1.475 A,   I_{2} = 0.246 + j0.295 A$$

$$V_{th} = I_{2}(−j8) = 2.361 − j1.967 = 3.073∠−39.81° V$$

[[img:ck5_22s2|Terminals shorted (the −j8 is shorted out)|w=62]]

**I_{N}** (terminals shorted):

$$Mesh 2:  −j4(I_{2} − I_{1}) + j2I_{2} − j6I_{1} = 0  ⇒  I_{2} = −I_{1};   (4 − j8)I_{1} = −12$$

$$I_{N} = I_{2} = \frac{12}{4 − j8} = 0.6 + j1.2 = 1.342∠63.43° A$$

$$Z_{th} = \frac{V_{th}}{I_{N}} = 2.290∠−103.24° = −0.525 − j2.230 Ω$$

$$V_{0} = V_{th} × \frac{2}{Z_{th} + 2} = \frac{3.073∠−39.81° × 2}{2.674∠−56.50°} = 2.299∠16.70° V$$

:::ans
**V_{0} = 2.30∠16.70° V, i.e. v_{0}(t) = 2.30 cos(t + 16.70°) V**
:::

:::trap Book error in 5.22
For V_{th}, the book writes mesh 2 as −j2I_{1} − j6I_{2} = 0: it keeps the shared −j4 in the I_{1} term but drops it from I_{2}'s own impedance (−j4 + j2 − j8 = −j10, not −j6). That gives V_{th} = 4.8∠−36.87° V, Z_{th} = 3.58∠−100.3° Ω and V_{0} = 1.27∠32° V. Its I_{N} = 1.342∠63.43° A is right. The answer above was confirmed by a full node solve with the 2 Ω in place (2.2988∠16.70° V).
:::

<div class="qhead"><span class="qn">A23 · Problem 5.23</span><span class="qt">Norton · DC <span class="lvl light">new idea</span></span></div>

:::q
Obtain the Norton's equivalent circuit with respect to the terminals AB for the network shown in the figure.
:::

[[img:ck5_23||w=40]]

:::try
Short A to B. What current does each source push through the short?
:::

:::new Hint: what's new
- **Norton's form:** I_{N} = I_{sc} (current through the A–B short), R_{N} = R_{th}, drawn as a current source in parallel with R_{N}, arrow pointing towards A.
- With A–B shorted, each source sees only its own resistor, so I_{sc} is a sum of two Ohm's-law currents.
:::

[[img:ck5_23s|Top: sources removed (R_{N}). Bottom: A–B shorted (I_{N}).|w=46]]

$$R_{N} = 5 ∥ 15 = \frac{75}{20} = 3.75 Ω$$

$$I_{N} = I_{sc} = \frac{10}{5} + \frac{20}{15} = 2 + 1.333 = 3.33 A$$

[[img:ck5_23s2|Norton equivalent (arrow towards A)|w=24]]

:::ans
**I_{N} = 3.33 A (towards A) in parallel with R_{N} = 3.75 Ω** (= book).  Check: V_{th} = I_{N}R_{N} = 12.5 V = node voltage at A ✓.
:::

<div class="qhead"><span class="qn">A24 · Problem 5.24</span><span class="qt">Norton · from a v–i characteristic <span class="lvl light">new idea</span></span></div>

:::q
For the one-port shown in the figure, determine the Norton's equivalent at the terminals AB, if the v–i characteristic is given by 16v = 80 − 2i.
:::

[[img:ck5_24||w=20]]

:::try
Which two points on the v–i line are V_{oc} and I_{sc}?
:::

:::new Hint: what's new
- **The equivalent is read off the terminal line.** i = 0 gives V_{oc}; v = 0 gives I_{sc}; R_{N} = V_{oc} / I_{sc} (the size of the line's slope, Δv/Δi).
:::

$$16v = 80 − 2i  ⇒  \frac{v}{5} + \frac{i}{40} = 1$$

$$i = 0:  V_{oc} = 5 V        v = 0:  I_{sc} = 40 A        R_{N} = \frac{5}{40} = \frac{1}{8} Ω$$

[[img:ck5_24s|The v–i line and the Norton equivalent|w=56]]

:::ans
**I_{N} = 40 A (towards A) in parallel with R_{N} = 1/8 Ω** (= book)
:::

:::note Sign convention
v = 5 − \frac{i}{8} describes an ordinary source only if i is the current **delivered out of A** (v falls as the load draws more). The figure's arrow points into N; read literally, that would make R_{N} = −1/8 Ω with the 40 A reversed. The intended answer is the book's.
:::

<div class="qhead"><span class="qn">A25 · Problem 5.25</span><span class="qt">Thevenin + Norton · superposition inside <span class="lvl plain">practice</span></span></div>

:::q
Find both Thevenin's and Norton's equivalent circuits for the network shown in the figure. All values are in ohm.
:::

[[img:ck5_25|Terminals at the right-hand end of the 1 Ω series resistor and the bottom rail.|w=62]]

:::try
Which resistors does the shorted 5 V source remove from R_{th}? Then find I_{sc} one source at a time.
:::

[[img:ck5_25s1|Sources switched off: the two 2 Ω across the 5 V are shorted out|w=80]]

$$R_{N} = R_{th} = (2 ∥ 1) + 1 = \frac{2}{3} + 1 = \frac{5}{3} Ω$$

[[img:ck5_25s3|5 V alone, terminals shorted|w=56]]

**I_{sc}, 5 V alone** (2 A opened): the middle node sees 2 Ω to the 5 V, and 1 Ω ∥ 1 Ω to ground:

$$\frac{V_{m} − 5}{2} + \frac{V_{m}}{1} + \frac{V_{m}}{1} = 0  ⇒  V_{m} = 1 V,   I_{sc}′ = \frac{1}{1} = 1 A$$

[[img:ck5_25s4|2 A alone, terminals shorted|w=80]]

**I_{sc}, 2 A alone** (5 V shorted): the 2 A divides between 2 Ω ∥ 1 Ω = 2/3 Ω and the 1 Ω to the short:

$$I_{sc}″ = 2 × \frac{2/3}{2/3 + 1} = \frac{4}{5} A$$

$$I_{N} = 1 + \frac{4}{5} = \frac{9}{5} A,   V_{th} = I_{N}R_{th} = \frac{9}{5} × \frac{5}{3} = 3 V$$

[[img:ck5_25s5|Norton and Thevenin forms|w=62]]

:::ans
**Norton: 1.8 A ∥ 5/3 Ω.  Thevenin: 3 V in series with 5/3 Ω** (= book)
:::

<div class="qhead"><span class="qn">A26 · Problem 5.26</span><span class="qt">Thevenin · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Replace the circuit in the figure with the Thevenin's equivalent circuit across A and B.
:::

[[img:ck5_26|The question's figure, as printed: it marks no terminals A and B.|w=56]]

:::trap Book error in 5.26: figure and solution belong to different circuits
The figure shows no A and B, so the question cannot be answered as printed. The book's solution solves a different circuit (a transistor model): 10 mV source, 1 kΩ carrying I, a controlled voltage 10^{−4}V_{0} in the input loop, and a controlled current source 75I in parallel with 30 kΩ across A–B. That solution is checked below. Ask your professor which circuit is meant before submitting.
:::

[[img:ck5_26s|The book's solution circuit, A–B shorted|w=62]]

**V_{oc}** (A–B open). The 75I pulls current down out of node A, and it can only return through the 30 kΩ, so V_{0} = 30k × (−75I) = −2.25 × 10^{6}I. Input loop:

$$10^{3}I + 10^{−4}V_{0} = 10 × 10^{−3}  ⇒  −4.444 × 10^{−4}V_{0} + 1 × 10^{−4}V_{0} = 10^{−2}  ⇒  V_{0} = −29.03 V$$

**I_{sc}.** A–B shorted ⇒ V_{0} = 0, so I = \frac{10 mV}{1 kΩ} = 10^{−5} A and I_{sc} = −75I = −7.5 × 10^{−4} A.

$$R_{th} = \frac{−29.03}{−7.5 × 10^{−4}} = 38.71 kΩ$$

:::ans
**(solution circuit) V_{th} = −29.0 V, R_{th} = 38.7 kΩ** (≈ book: it rounds V_{0} to −29 V and prints 38.67 kΩ)
:::

<div class="qhead"><span class="qn">A27 · Problem 5.27</span><span class="qt">Thevenin · dependent sources, negative R_{th} <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin's equivalent between terminals a and b of the circuit shown in the figure.
:::

[[img:ck5_27|The question figure gives 50 kΩ; the book's solution figure uses 50 Ω.|w=60]]

:::try
V_{x} = V_{oc} feeds back into the left loop. For I_{sc}, V_{x} = 0 removes the 2V_{x} source.
:::

**V_{oc}** (R = 50 kΩ, as in the question figure). Left loop and right node:

$$I_{0} = \frac{3 − 2V_{x}}{1000},   V_{oc} = V_{x} = −40I_{0} × 50000 = −2000(3 − 2V_{oc})$$

$$3999V_{oc} = 6000  ⇒  V_{oc} = 1.5004 V$$

[[img:ck5_27s|a–b shorted|w=56]]

**I_{sc}** (V_{x} = 0 ⇒ 2V_{x} = 0): I_{0} = \frac{3}{1000} = 3 mA. The 50 kΩ is shorted, and the dependent source pulls 40I_{0} from a down to b, so the short carries it from b to a:

$$I_{sc} (a → b) = −40I_{0} = −0.12 A,   R_{th} = \frac{1.5004}{−0.12} = −12.50 Ω$$

:::ans
**V_{th} = 1.500 V, R_{th} = −12.50 Ω** (figure value 50 kΩ)
:::

:::trap Book errors in 5.27
1. The solution uses **50 Ω** (V_{x} = −40I_{0} × 50 = −2000I_{0}), not the figure's 50 kΩ. With 50 Ω: V_{oc} = −2(3 − 2V_{oc}) ⇒ V_{oc} = 2 V.
2. It then writes R_{th} = 2/0.12 = 16.67 Ω, dropping the sign of I_{sc} = −0.12 A. With 50 Ω the correct value is **R_{th} = −16.67 Ω**.

Test-source check (3 V shorted, 1 V applied at a): I_{0} = −\frac{2}{1000} A, current drawn = \frac{1}{R} − 0.08, giving R_{th} = −12.50 Ω (50 kΩ) or −16.67 Ω (50 Ω) ✓.
:::

<div class="qhead"><span class="qn">A28 · Problem 5.28</span><span class="qt">Norton · s-domain transient <span class="lvl light">new idea</span></span></div>

:::q
In the network shown in the figure, the switch is closed at time t = 0. Assuming all the initial currents and voltages as zero, find the current through the inductor L_{2} by the use of Norton's theorem.
:::

[[img:ck5_28||w=60]]

:::try
Draw the s-domain circuit (zero initial conditions). Make (R_{2} + sL_{2}) the load and find the Norton equivalent of the rest.
:::

:::new Hint: what's new
- **Transient = theorem in the s-domain.** A DC source switched on at t = 0 becomes \frac{V}{s}; R → R, L → sL, C → \frac{1}{sC}. Find I_{L}(s) exactly as in AC, then invert with partial fractions.
- With A–B shorted the capacitor is shorted out, so I_{sc} is one Ohm's-law step.
:::

[[img:ck5_28s1|The book's s-domain network: note it draws the capacitor as 1/s|w=56]]

**s-domain:** source \frac{3}{s}; R_{1} + sL_{1} = s + 2; C = 2 F → \frac{1}{2s}; load R_{2} + sL_{2} = s + 2.

$$Z_{N} = (s + 2) ∥ \frac{1}{2s} = \frac{s + 2}{2s^{2} + 4s + 1},   I_{N} = I_{sc} = \frac{3/s}{s + 2} = \frac{3}{s(s + 2)}$$

$$I_{L}(s) = I_{N} × \frac{Z_{N}}{Z_{N} + (s + 2)} = \frac{3}{s(s + 2)} × \frac{1}{1 + (2s^{2} + 4s + 1)} = \frac{3}{2s(s + 2)(s + 1)^{2}}$$

$$Partial fractions:  I_{L}(s) = \frac{3/4}{s} − \frac{3/4}{s + 2} + \frac{0}{s + 1} − \frac{3/2}{(s + 1)^{2}}$$

(Coefficients: at s = 0, \frac{3}{2·2·1} = \frac{3}{4}; at s = −2, \frac{3}{2(−2)(1)} = −\frac{3}{4}; on (s + 1)^{2}, \frac{3}{2(−1)(1)} = −\frac{3}{2}; on 1/(s + 1), 0, because the s^{3} terms must cancel.)

:::ans
**i_{L2}(t) = \frac{3}{4} − \frac{3}{4}e^{−2t} − \frac{3}{2}te^{−t} A**  (t ≥ 0)
:::

:::trap Book error in 5.28
The figure gives C = 2 F, but the book's s-domain network uses \frac{1}{s} (that is C = 1 F) and prints i(t) = \frac{3}{4} − \frac{3}{4}e^{−2t} − \frac{3}{2}e^{−t} sin t A. That answer is right for a 1 F capacitor only. A direct simulation of the circuit equations with C = 2 F matches the answer above (e.g. i(1 s) = 0.0967 A; the book's formula gives 0.184 A). Checks: i(0) = 0 and i(∞) = \frac{3}{2 + 2} = 0.75 A.
:::

<div class="qhead"><span class="qn">A29 · Problem 5.29</span><span class="qt">Thevenin · dependent source <span class="lvl plain">practice</span></span></div>

:::q
The following circuit has a dependent current source and an independent voltage source. Find the Thevenin equivalent network of the circuit across the terminals a and b.
:::

[[img:ck5_29||w=42]]

[[img:ck5_29s|Left: a–b open (v_{1} = v_{oc}). Right: a–b shorted (v_{1} = 0, so the dependent source is zero).|w=80]]

**V_{oc}:** the top node sits at v_{1} + 100. KCL there:

$$\frac{v_{1}}{100} = \frac{v_{1} + 100}{20}  ⇒  v_{1} = 5v_{1} + 500  ⇒  V_{oc} = −125 V$$

**I_{sc}:** v_{1} = 0, so the dependent source is off; the top node is at 100 V and the 20 Ω draws 5 A from it, which must come from the short: I_{sc} (a → b) = −5 A.

$$R_{th} = \frac{−125}{−5} = 25 Ω$$

:::ans
**V_{th} = −125 V (i.e. 125 V with + at b), R_{th} = 25 Ω** (= book)
:::

<div class="qhead"><span class="qn">A30 · Problem 5.30</span><span class="qt">Thevenin · transient with initial conditions <span class="lvl light">new idea</span></span></div>

:::q
In the network of the figure, the switch K is closed at time t = 0, a steady state having previously existed. Obtain the current in the resistor R using Thevenin's theorem.
:::

[[img:ck5_30|Closing K shorts R_{1}.|w=62]]

:::try
Find both inductor currents just before t = 0 (inductors are shorts in DC steady state). Then build the s-domain circuit with those currents as sources.
:::

:::new Hint: what's new
- **Non-zero initial current:** an inductor carrying i(0) becomes sL **in series with a voltage source L·i(0)**, polarity aiding the current's direction.
:::

[[img:ck5_30s1|t = 0−: inductors as shorts|w=48]]

**t = 0−** (K open, R_{1} in):

$$30I_{1} − 10I_{2} = 100,   −10I_{1} + 20I_{2} = 0$$

$$i_{L1}(0) = I_{1} = 4 A,   i_{L2}(0) = I_{2} = 2 A$$

[[img:ck5_30s2|s-domain network for t > 0 (R_{1} shorted); the load Z_{L} = s + 10 is in the dashed box|w=80]]

**Thevenin at a–b** (load = sL_{2} + R = s + 10; the 2 V of L_{2} stays on the source side):

$$Z_{th} = (s + 10) ∥ 10 = \frac{10(s + 10)}{s + 20}$$

$$I(s) = \frac{100/s + 4}{s + 20} = \frac{4s + 100}{s(s + 20)},   V_{th} = 10I(s) + 2 = \frac{2s^{2} + 80s + 1000}{s(s + 20)}$$

$$I_{R}(s) = \frac{V_{th}}{Z_{th} + s + 10} = \frac{2s^{2} + 80s + 1000}{s(s + 10)(s + 30)} = \frac{10/3}{s} − \frac{2}{s + 10} + \frac{2/3}{s + 30}$$

:::ans
**i_{R}(t) = \frac{10}{3} − 2e^{−10t} + \frac{2}{3}e^{−30t} A = 3.33 − 2e^{−10t} + 0.67e^{−30t} A** (= book)
:::

:::note Check
i(0) = 10/3 − 2 + 2/3 = 2 A = i_{L2}(0) ✓.  i(∞) = \frac{100}{10 + 5} × \frac{1}{2} = 3.33 A ✓.  A direct simulation of the circuit equations agrees at every time tested.
:::

<div class="qhead"><span class="qn">A31 · Problem 5.31</span><span class="qt">Thevenin · symbolic, two dependent sources <span class="lvl light">new idea</span></span></div>

:::q
For the network shown in the figure, show that the Thevenin equivalent at the terminals a-b is represented by V_{Th} = \frac{V_{1}}{2}(1 + a + b − ab) and Z_{Th} = \frac{3 − b}{2}.
:::

[[img:ck5_31||w=50]]

:::try
Keep a, b and V_{1} as letters. Open circuit: no current in the right 1 Ω. Short circuit: two mesh equations.
:::

:::new Hint: what's new
- **Symbolic answer:** the method is unchanged; carry the letters and simplify at the end. Substituting numbers (e.g. a = b = 0) checks the algebra.
:::

**V_{th}** (no current in the right 1 Ω). Left mesh:

$$2I_{1} + aV_{1} = V_{1}  ⇒  I_{1} = \frac{V_{1}}{2}(1 − a)$$

$$V_{th} = aV_{1} + 1·I_{1} + bI_{1} = aV_{1} + (1 + b)\frac{V_{1}}{2}(1 − a) = \frac{V_{1}}{2}(1 + a + b − ab)$$

[[img:ck5_31s|a–b shorted|w=50]]

**I_{sc}.** Two meshes:

$$2I_{1} − I_{SC} = V_{1}(1 − a)   …(i)        −(1 + b)I_{1} + 2I_{SC} = aV_{1}   …(ii)$$

$$I_{SC} = \frac{2aV_{1} + (1 + b)V_{1}(1 − a)}{4 − (1 + b)} = \frac{V_{1}(1 + a + b − ab)}{3 − b}$$

$$Z_{th} = \frac{V_{th}}{I_{SC}} = \frac{3 − b}{2}   (proved)$$

:::note Check
Test source (V_{1} = 0): the top node sits on 1 ∥ 1 = 0.5 Ω, I_{1} = −0.5I_{t}, so V = I_{t} + 0.5I_{t} − 0.5bI_{t} = \frac{3 − b}{2}I_{t} ✓. Also confirmed numerically for two sets of (a, b, V_{1}).
:::

<div class="qhead"><span class="qn">A32 · Problem 5.32</span><span class="qt">Thevenin · AC, current source <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin equivalent circuit for the network shown in the figure at terminals A-B.
:::

[[img:ck5_32|The 5∠30° A is fed in at the left node and returns on the bottom rail.|w=50]]

$$I_{right} = 5∠30° × \frac{50 + j50}{(100 + 50 + j50) + (50 + j50)} = 5∠30° × \frac{1 + j}{4 + j2} = 1.581∠48.43° A$$

$$V_{th} = I_{right}(50 + j50) = 111.8∠93.43° V$$

$$Z_{th} = (150 + j50) ∥ (50 + j50) = \frac{5000 + j10000}{200 + j100} = 40 + j30 Ω$$

:::ans
**V_{th} = 111.8∠93.43° V, Z_{th} = 50∠36.87° = 40 + j30 Ω** (= book)
:::

<div class="qhead"><span class="qn">A33 · Problem 5.33</span><span class="qt">Thevenin · dependent source <span class="lvl plain">practice</span></span></div>

:::q
Find Thevenin's equivalent circuit across the terminals A and B for the network shown in the figure.
:::

[[img:ck5_33||w=48]]

[[img:ck5_33s1|A–B open|w=48]]

$$KVL:  10i_{0} + V_{th} = 12        KCL at A:  i_{0} + 2i_{0} = \frac{V_{th}}{5}  ⇒  V_{th} = 15i_{0}$$

$$25i_{0} = 12  ⇒  i_{0} = 0.48 A,   V_{th} = 7.2 V$$

[[img:ck5_33s2|A–B shorted (the 5 Ω is shorted out)|w=48]]

$$i_{0} = \frac{12}{10} = 1.2 A,   I_{sc} = i_{0} + 2i_{0} = 3.6 A,   R_{th} = \frac{7.2}{3.6} = 2 Ω$$

:::ans
**V_{th} = 7.2 V, R_{th} = 2 Ω** (= book)
:::

<div class="qhead"><span class="qn">A34 · Problem 5.34</span><span class="qt">Thevenin · no independent source <span class="lvl light">new idea</span></span></div>

:::q
Find Thevenin's equivalent circuit for the network shown in the figure.
:::

[[img:ck5_34||w=40]]

:::try
There is nothing to drive the circuit. What is V_{th}? For Z_{th}, connect a 1 A source and find the voltage it produces.
:::

:::new Hint: what's new
- **Only dependent sources:** V_{th} = 0 (no independent source, no response), and I_{sc} = 0 too, so V_{oc}/I_{sc} fails. Use a **test source**: Z_{th} = V / I.
:::

[[img:ck5_34s|Test current I applied; V measured|w=50]]

$$KCL at x:  \frac{V − v_{0}}{10} − 0.5v_{0} − I = 0  ⇒  V = 10I + 6v_{0}$$

$$Current down the 20 Ω = \frac{V − v_{0}}{10} = 0.5v_{0} + I$$

$$v_{0} = 20(0.5v_{0} + I)  ⇒  v_{0} = −\frac{20}{9}I$$

$$V = 10I − \frac{120}{9}I = −\frac{10}{3}I  ⇒  Z_{th} = −3.33 Ω$$

:::ans
**V_{th} = 0, Z_{th} = −10/3 = −3.33 Ω** (= book; its final sketch omits the minus sign)
:::
