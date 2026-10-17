## C · Maximum power transfer theorem

[[map:Thevenin / Norton (done) > Load sees only V_{th} and Z_{th} > Maximum power: choose the load to match Z_{th}|here=3]]

**Where this sits.** Thevenin's theorem reduced any network to V_{th} in series with Z_{th}. The load current is then V_{th} / (Z_{th} + Z_{L}), so the only question left is which load draws the most power from that one source.

**Three terms first.**

- **Load:** the element connected at the terminals, R_{L} (DC) or Z_{L} = R_{L} + jX_{L} (AC).
- **Average power in the load:** P = |I|^{2}R_{L}. Only the resistive part of the load absorbs power.
- **Complex conjugate:** for Z_{th} = R_{th} + jX_{th}, the conjugate is Z_{th}^{*} = R_{th} − jX_{th} (same resistance, opposite reactance).

**Statement.**

| Load allowed to vary | Maximum power when | P_{max} |
|---|---|---|
| R_{L} only, DC | R_{L} = R_{th} | \frac{V_{th}^{2}}{4R_{th}} |
| Z_{L} = R_{L} + jX_{L}, both free (AC) | Z_{L} = Z_{th}^{*} (reactances cancel) | \frac{\|V_{th}\|^{2}}{4R_{th}} |
| Pure resistance R_{L}, AC source | R_{L} = \|Z_{th}\| | \|I\|^{2}R_{L} (calculate) |

The recipe is always: **find V_{th} and Z_{th}, then match.** At maximum power the load gets exactly half the power, so efficiency is only 50%.

**Phasor size convention.** The book takes phasor magnitudes as rms values, so P = |V_{th}|^{2} / (4R_{th}). If a source is given as a peak value, the power is half of that.

<div class="qhead"><span class="qn">A35 · Problem 5.35</span><span class="qt">Power and superposition <span class="lvl light">new idea</span></span></div>

:::q
In the network shown, the power dissipated in R when E_{1}, E_{2} or E_{3} acting alone is (a) 20 W, 80 W and 5 W respectively; (b) 30 W, 270 W and 120 W respectively. Calculate the maximum power that R can dissipate due to the simultaneous action of all the sources. Calculate both for (a) and (b). What will be the minimum power dissipated in R when all the sources are acting simultaneously?
:::

[[img:ck5_35||w=36]]

:::try
Power does not add. What does add? Turn each power back into a current, and remember you don't know each current's sign.
:::

:::new Hint: what's new
- **Superposition adds currents, not powers.** Each source alone gives |i_{k}| = \sqrt{P_{k}/R}; the directions are unknown, so the total is ±i_{1} ± i_{2} ± i_{3}.
- P = i^{2}R = (±\sqrt{P_{1}} ± \sqrt{P_{2}} ± \sqrt{P_{3}})^{2}. Largest: all signs the same. Smallest: the sign choice that makes the sum closest to zero.
:::

$$i = ±\sqrt{\frac{P_{1}}{R}} ± \sqrt{\frac{P_{2}}{R}} ± \sqrt{\frac{P_{3}}{R}}  ⇒  P = i^{2}R = (±\sqrt{P_{1}} ± \sqrt{P_{2}} ± \sqrt{P_{3}})^{2}$$

**(a)** \sqrt{20} = 2\sqrt{5}, \sqrt{80} = 4\sqrt{5}, \sqrt{5}:

$$P_{max} = (2 + 4 + 1)^{2} × 5 = 49 × 5 = 245 W,   P_{min} = (4 − 2 − 1)^{2} × 5 = 5 W$$

**(b)** \sqrt{30}, \sqrt{270} = 3\sqrt{30}, \sqrt{120} = 2\sqrt{30}:

$$P_{max} = (1 + 3 + 2)^{2} × 30 = 36 × 30 = 1080 W,   P_{min} = (3 − 1 − 2)^{2} × 30 = 0 W$$

:::ans
**(a) P_{max} = 245 W, P_{min} = 5 W.  (b) P_{max} = 1080 W, P_{min} = 0 W** (= book)
:::

:::note Side note
Adding the powers would give 105 W and 420 W, which is wrong in both cases. The book's working line for (b) P_{max} misprints the bracket as [4\sqrt{5} − 3\sqrt{5}]; its answer 1080 W is right.
:::

<div class="qhead"><span class="qn">A36 · Problem 5.36</span><span class="qt">Maximum power · DC <span class="lvl heavy">teach</span></span></div>

:::q
Find the value of R in the circuit of the figure such that maximum power transfer takes place. What is the amount of this power?
:::

:::try
For each circuit: remove R, find V_{th} across its terminals and R_{th} looking back in. Then R = R_{th} and P_{max} = V_{th}^{2}/(4R_{th}). In (b), look for an element that changes nothing. In (c), R is not connected to ground.
:::

:::new Hint: what's new
- **Maximum power transfer (DC):** R = R_{th}, P_{max} = \frac{V_{th}^{2}}{4R_{th}}. All the work is in finding V_{th} and R_{th}.
- **(b)** the 2 Ω directly across the 5 V source changes no other current (5.1's shortcut); then source transformations reduce the rest.
- **(c)** R sits between two non-ground nodes, so V_{th} = V_{P} − V_{Q}.
:::

**(a)**

[[img:ck5_36a||w=46]]

[[img:ck5_36as|R removed; the 6 V source (+ at the bottom) is in the path to the terminal|w=46]]

**V_{th}.** Mesh currents with R removed: 3i_{1} − 2i_{2} = 4, −2i_{1} + 8i_{2} = 0 ⇒ i_{1} = 4i_{2}, so 10i_{2} = 4:

$$i_{2} = \frac{2}{5} A,   V_{th} = 1 × i_{2} + 6 = \frac{32}{5} = 6.4 V$$

[[img:ck5_36as2|Sources shorted, looking back from R|w=40]]

$$R_{th} = [(1 ∥ 2) + 5] ∥ 1 = \frac{17}{3} ∥ 1 = \frac{17}{20} = 0.85 Ω$$

$$P_{max} = \frac{V_{th}^{2}}{4R_{th}} = \frac{6.4^{2}}{4 × 0.85} = \frac{40.96}{3.4} = 12.05 W$$

:::ans
**(a) R = 0.85 Ω, P_{max} = 12.05 W** (= book, which rounds to 12 W)
:::

**(b)**

[[img:ck5_36b||w=50]]

[[img:ck5_36bs1|The 2 Ω across the 5 V is dropped; 5 V with 3 Ω → \frac{5}{3} A ∥ 3 Ω|w=86]]

Combine the two current sources and the two resistors, then transform back:

$$\frac{5}{3} + 2 = \frac{11}{3} A,   3 ∥ 1 = \frac{3}{4} Ω  ⇒  \frac{11}{3} × \frac{3}{4} = \frac{11}{4} V in series with \frac{3}{4} Ω$$

[[img:ck5_36bs2|Successive source transformations|w=86]]

$$V_{th} = \frac{11}{4} V,   R_{th} = \frac{3}{4} + 1 = \frac{7}{4} Ω,   P_{max} = \frac{(11/4)^{2}}{4 × 7/4} = \frac{121}{112} = 1.08 W$$

:::ans
**(b) R = 7/4 = 1.75 Ω, P_{max} = 1.08 W** (= book)
:::

**(c)**

[[img:ck5_36c||w=50]]

[[img:ck5_36cs1|R_{th}: 5 A opened, 24 V shorted|w=40]]

$$R_{th} = 2 + (10 ∥ 5) = 2 + \frac{10}{3} = 5.33 Ω$$

[[img:ck5_36cs2|V_{oc}: 5 A ∥ 2 Ω → 10 V in series with 2 Ω|w=50]]

**V_{th}.** With R removed, no current flows in the 2 Ω, so V_{P} = 10 V. The right loop gives V_{Q} = 24 × \frac{5}{15} = 8 V (the book writes this as i = −24/15 = −1.6 A, V_{oc} = 5i + 10).

$$V_{th} = V_{P} − V_{Q} = 10 − 8 = 2 V,   P_{max} = \frac{2^{2}}{4 × 16/3} = \frac{3}{16} = 0.1875 W$$

:::ans
**(c) R = 5.33 Ω, P_{max} = 0.1875 W** (= book, 0.188 W)
:::

:::note Check
For each part, the full circuit was solved with R swept from 0 to 50 Ω; the power peaks at the R and P_{max} above.
:::

<div class="qhead"><span class="qn">A37 · Problem 5.37</span><span class="qt">Maximum power · AC conjugate match <span class="lvl light">new idea</span></span></div>

:::q
In the network shown, find the value of Z_{L} to which the maximum power can be delivered. Hence, find the value of the maximum power.
:::

[[img:ck5_37||w=56]]

:::try
Find V_{th} and Z_{th} at A–B as in any AC Thevenin problem. Then choose Z_{L} so that the total impedance in the loop is purely resistive.
:::

:::new Hint: what's new
- **AC load free in R and X:** Z_{L} = Z_{th}^{*}. The reactances cancel (X_{L} = −X_{th}), leaving the DC case R_{L} = R_{th}, so P_{max} = \frac{|V_{th}|^{2}}{4R_{th}}.
:::

**V_{th}.** Impedance seen by the source: 3 + j3 ∥ (3 − j3) = 3 + (3 + j3) = 6 + j3 Ω.

$$I = \frac{5}{6 + j3},   I_{right} = I × \frac{j3}{j3 + 3 − j3} = jI$$

$$V_{th} = I_{right}(−j3) = 3I = \frac{15}{6 + j3} = 2 − j1 = 2.236∠−26.57° V$$

**Z_{th}** (source shorted):

$$3 ∥ j3 = 1.5 + j1.5,   (1.5 + j1.5 + 3) ∥ (−j3) = \frac{(4.5 + j1.5)(−j3)}{4.5 − j1.5} = 1.8 − j2.4 Ω$$

$$Z_{L} = Z_{th}^{*} = 1.8 + j2.4 Ω,   I = \frac{V_{th}}{2 × 1.8} = 0.621∠−26.57° A$$

$$P_{max} = \frac{2.236^{2}}{4 × 1.8} = 0.694 W$$

:::ans
**Z_{L} = 1.8 + j2.4 Ω, P_{max} = 0.694 W** (= book)
:::

<div class="qhead"><span class="qn">A38 · Problem 5.38</span><span class="qt">Maximum power · AC load impedance <span class="lvl plain">practice</span></span></div>

:::q
A loudspeaker is connected across terminals A and B of the network. What should be its impedance to obtain maximum power dissipation in it?
:::

:::try
Only Z_{th} is needed: switch the sources off and look back from A–B.
:::

**(a)**

[[img:ck5_38a||w=46]]

$$Z_{th} = \frac{(3 + j4)(−j5)}{3 + j4 − j5} = \frac{20 − j15}{3 − j1} = 7.5 − j2.5 = 7.91∠−18.43° Ω$$

:::ans
**(a) Z_{L} = Z_{th}^{*} = 7.5 + j2.5 Ω** (the book prints 7.5 + j2.4, a typo; its own Z_{th} is 7.5 − j2.5)
:::

**(b)**

[[img:ck5_38b|Voltage source shorted and current source opened for Z_{th}.|w=60]]

$$(10 + j8) ∥ j5 = \frac{−40 + j50}{10 + j13} = 0.929 + j3.792 Ω$$

$$+ (4 + j6) = 4.929 + j9.792 Ω,   ∥ 10 Ω  ⇒  Z_{th} = 5.316 + j3.072 = 6.14∠30° Ω$$

:::ans
**(b) Z_{L} = Z_{th}^{*} = 5.316 − j3.072 = 6.14∠−30° Ω** (= book)
:::

<div class="qhead"><span class="qn">A39 · Problem 5.39</span><span class="qt">Maximum power · resistive load on an AC source <span class="lvl light">new idea</span></span></div>

:::q
Two inductors each of 1 Ω reactance and negligible resistance are connected in series across a 2 V a.c. source. Find the value of resistance which should be connected across one of the inductors for maximum power dissipation. Also, find the maximum power.
:::

:::try
Draw it: 2 V source, j1, then j1 ∥ R. Write the power in R as a function of R and maximise it, or find the Thevenin equivalent seen by R first.
:::

:::new Hint: what's new
- **Only a resistance is allowed**, so the reactance cannot be cancelled and Z_{L} = Z_{th}^{*} is impossible. For a purely resistive load the best value is R = |Z_{th}|.
:::

**Route 1: calculus** (as the book):

$$Z = \frac{jR}{R + j1} + j1 = \frac{−1 + j2R}{R + j1},   I_{R} = \frac{2(R + j1)}{−1 + j2R} × \frac{j1}{R + j1} = \frac{j2}{−1 + j2R}$$

$$P = |I_{R}|^{2}R = \frac{4R}{1 + 4R^{2}},   \frac{dP}{dR} = \frac{4(1 + 4R^{2}) − 4R(8R)}{(1 + 4R^{2})^{2}} = 0  ⇒  4 − 16R^{2} = 0  ⇒  R = 0.5 Ω$$

$$P_{max} = \frac{4 × 0.5}{1 + 4 × 0.25} = 1 W$$

**Route 2: Thevenin.** Seen by R: V_{th} = 2 × \frac{j1}{j1 + j1} = 1 V, Z_{th} = j1 ∥ j1 = j0.5 Ω. Pure resistance ⇒ R = |Z_{th}| = 0.5 Ω, and |I|^{2} = \frac{1}{|0.5 + j0.5|^{2}} = 2, so P = 2 × 0.5 = 1 W ✓.

:::ans
**R = 0.5 Ω, P_{max} = 1 W** (= book; its last line prints 4 × 0.4, a typo for 4 × 0.5)
:::

<div class="qhead"><span class="qn">A40 · Problem 5.40</span><span class="qt">Maximum power · dependent source <span class="lvl plain">practice</span></span></div>

:::q
In the network shown, calculate the maximum power that may be dissipated in the external resistor R.
:::

[[img:ck5_40|2i_{1} is a current-controlled voltage source; i_{1} flows down the 6 Ω.|w=52]]

:::try
The dependent source rules out "switch off and combine", so find V_{oc} and I_{sc}. Start by turning 10 A ∥ 4 Ω into a voltage source.
:::

[[img:ck5_40s1|10 A ∥ 4 Ω → 40 V in series with 4 Ω; terminals open|w=46]]

**V_{oc}** (no current in the 3 Ω, so the loop current is i_{1}):

$$−40 + 4i_{1} − 2i_{1} + 6i_{1} = 0  ⇒  i_{1} = 5 A,   V_{oc} = 6i_{1} = 30 V$$

[[img:ck5_40s2|Terminals shorted|w=46]]

**I_{sc}.** Let V_{M} be the node above the 6 Ω: i_{1} = V_{M}/6, I_{sc} = V_{M}/3, source current = V_{M}/6 + V_{M}/3 = V_{M}/2. Left loop:

$$40 − 4 × \frac{V_{M}}{2} + 2 × \frac{V_{M}}{6} − V_{M} = 0  ⇒  \frac{8}{3}V_{M} = 40$$

$$V_{M} = 15 V,   I_{sc} = \frac{15}{3} = 5 A$$

$$R_{th} = \frac{30}{5} = 6 Ω,   P_{max} = \frac{30^{2}}{4 × 6} = 37.5 W$$

:::ans
**R = 6 Ω, P_{max} = 37.5 W** (= book)
:::

<div class="qhead"><span class="qn">A41 · Problem 5.41</span><span class="qt">Maximum power · AC <span class="lvl plain">practice</span></span></div>

:::q
Find the Thevenin's equivalent between the points a and b for the circuit given in the figure. What should be the value of impedance connected between a and b for maximum power to be transferred from the sources? Obtain the amount of the maximum power.
:::

[[img:ck5_41||w=46]]

$$I = \frac{100}{2 + 3 + j5} = 10 − j10 A,   V_{th} = I(3 + j5) = 80 + j20 = 82.46∠14.04° V$$

$$Z_{th} = j6 + \frac{2(3 + j5)}{5 + j5} = j6 + 1.6 + j0.4 = 1.6 + j6.4 Ω$$

[[img:ck5_41s|Thevenin equivalent|w=40]]

$$Z_{L} = Z_{th}^{*} = 1.6 − j6.4 Ω,   P_{max} = \frac{|V_{th}|^{2}}{4R_{th}} = \frac{6800}{4 × 1.6} = 1062.5 W$$

:::ans
**V_{th} = 82.46∠14.04° V, Z_{th} = 1.6 + j6.4 Ω; Z_{L} = 1.6 − j6.4 Ω, P_{max} = 1062.5 W** (= book)
:::

<div class="qhead"><span class="qn">A42 · Problem 5.42</span><span class="qt">Maximum power · AC, two sources <span class="lvl plain">practice</span></span></div>

:::q
In the network in the figure, two voltage sources act on the load impedance connected to the terminal A and B. If the load is variable in both reactance and resistance, for what load Z_{L} will receive maximum power? What is the value of maximum power?
:::

[[img:ck5_42||w=56]]

**V_{th}** (Z_{L} removed; one loop current from the 50 V towards the j25 V):

$$I = \frac{50 − j25}{(5 + j5) + (3 − j4)} = \frac{50 − j25}{8 + j1}$$

$$V_{th} = 50 − I(5 + j5) = \frac{25 − j75}{8 + j1} = 1.923 − j9.615 = 9.806∠−78.69° V$$

$$Z_{th} = \frac{(5 + j5)(3 − j4)}{8 + j1} = \frac{35 − j5}{8 + j1} = 4.231 − j1.154 Ω$$

$$Z_{L} = Z_{th}^{*} = 4.231 + j1.154 Ω,   P_{max} = \frac{9.806^{2}}{4 × 4.231} = \frac{96.15}{16.92} = 5.68 W$$

:::ans
**Z_{L} = 4.23 + j1.154 Ω, P_{max} = 5.68 W** (= book to rounding: it squares 9.8 and prints 5.676 W)
:::

<div class="qhead"><span class="qn">A43 · Problem 5.43</span><span class="qt">Maximum power · equivalent from measurements <span class="lvl light">new idea</span></span></div>

:::q
A network has two output terminals. The open circuit voltage at these terminals is 260 V. The current flowing through the terminals is 20 A when the terminals are short circuited. Also, the current is 13 A when a coil of 11 ohm reactance and negligible resistance is connected across the terminals. Find the impedance components of the equivalent circuit feeding the terminals. What value of load impedance will give maximum power transfer and what is the value of this power?
:::

:::try
Let Z_{th} = R + jX. The two current readings give two equations for the magnitudes |R + jX| and |R + j(X + 11)|.
:::

:::new Hint: what's new
- **Z_{th} from terminal measurements:** |Z_{th}| = V_{oc}/I_{sc} gives R^{2} + X^{2}; a known reactance added in series gives a second equation. Subtracting them isolates X.
:::

$$|Z_{th}| = \frac{260}{20} = 13 Ω  ⇒  R^{2} + X^{2} = 169   …(i)$$

$$\frac{260}{|R + j(X + 11)|} = 13  ⇒  R^{2} + (X + 11)^{2} = 400   …(ii)$$

$$(ii) − (i):  22X + 121 = 231  ⇒  X = 5 Ω,   R = \sqrt{169 − 25} = 12 Ω$$

$$Z_{L} = Z_{th}^{*} = 12 − j5 Ω,   P_{max} = \frac{260^{2}}{4 × 12} = 1408.3 W$$

:::ans
**Z_{th} = 12 + j5 Ω; Z_{L} = 12 − j5 Ω, P_{max} = 1408.3 W** (= book)
:::

:::note Check
260/|12 + j5| = 260/13 = 20 A ✓;  260/|12 + j16| = 260/20 = 13 A ✓.
:::

<div class="qhead"><span class="qn">A44 · Problem 5.44</span><span class="qt">Maximum power · AC, two sources <span class="lvl plain">practice</span></span></div>

:::q
What should be the value of Z_{L} for maximum power to be delivered in the circuit shown in the figure?
:::

[[img:ck5_44|Impedances are given in ohms; both sources have the same ω.|w=58]]

$$Z_{th} = (3 + j2) ∥ (4 − j3) = \frac{(3 + j2)(4 − j3)}{7 − j1} = \frac{18 − j1}{7 − j1} = \frac{127 + j11}{50} = 2.54 + j0.22 Ω$$

:::ans
**Z_{L} = Z_{th}^{*} = 2.54 − j0.22 = 2.55∠−4.95° Ω** (= book)
:::

:::note Side note
The source values do not affect Z_{L}; they only set V_{th} and hence P_{max}. Thevenin's equivalent works here because both sources share one frequency ω.
:::
