## E · AC: superposition and source transformation (ch. 10 §10.4–10.5)

[[map:Ch. 4 theorems, DC (done) > Same theorems with phasors and impedances > Sources at different ω: one circuit per ω, add in time > Thevenin / Norton AC (next)|here=2]]

**Where this sits.** Every theorem from chapter 4 works unchanged in AC once R becomes Z = R + jX (Part A did this in 5.2, 5.4, 5.5, 5.6). The one new rule is the one Part A's 5.5(b) and 5.6 showed: **sources at different frequencies need separate circuits** (X_{L} = ωL and X_{C} = 1/ωC change with ω), and their answers are added **in the time domain**. A DC source is ω = 0: inductor → short, capacitor → open.

Phasor magnitudes here are amplitudes (Sadiku's convention in ch. 10). A sin source is handled as a sin reference throughout its own circuit and written back as sin.

<div class="qhead"><span class="qn">B80 · Practice Problem 10.4</span><span class="qt">AC · bridge with a current source <span class="lvl plain">practice</span></span></div>

:::q
Calculate current I_{o} in the circuit of Fig. 10.11.
:::

[[img:sd_pp10_4|Fig. 10.11 (a §10.3 problem; solved here by superposition)|w=46]]

**60 V alone** (2.4 A opened). The diamond is (5 − j4) ∥ (j8 − j6) between its top and bottom:

$$Z_{d} = (5 − j4) ∥ j2 = 0.690 + j2.276 Ω,   I_{o}′ = \frac{60}{10 + Z_{d}} = 5.490∠−12.02° A$$

**2.4 A alone** (60 V shorted, so the 10 Ω runs from the top corner to the bottom). Node solve of the three corners gives V_{top} = −6.873 − j17.737 V:

$$I_{o}″ = \frac{0 − V_{top}}{10} = 0.687 + j1.774 = 1.902∠68.82° A$$

:::ans
**I_{o} = 6.057 + j0.631 = 6.089∠5.94° A** (= book)
:::

<div class="qhead"><span class="qn">B81 · Practice Problem 10.5</span><span class="qt">AC superposition <span class="lvl plain">practice</span></span></div>

:::q
Find current I_{o} in the circuit of Fig. 10.8 using the superposition theorem.
:::

[[img:sd_pp10_5|Fig. 10.8|w=40]]

This is Part A's Chakraborty 5.5(c) with 10 A and 50∠30° V. The correct method there (current divider uses the **other** branch) gives the book's answer here, confirming the book error flagged in 5.5(c).

$$50∠30° alone:  I_{o}′ = 2.808∠81.84° A        10 A alone:  I_{o}″ = 10 × \frac{Z}{(8 − j2) + Z},  Z = j4 ∥ 6  ⇒  3.370∠51.84° A$$

:::ans
**I_{o} = 2.481 + j5.430 = 5.97∠65.45° A** (= book)
:::

<div class="qhead"><span class="qn">B82 · Practice Problem 10.6</span><span class="qt">AC superposition · two frequencies <span class="lvl plain">practice</span></span></div>

:::q
Calculate v_{o} in the circuit of Fig. 10.15 using the superposition theorem.
:::

[[img:sd_pp10_6|Fig. 10.15|w=50]]

Part A's 5.6 with 75 V and 6 A (same reactances: ω = 5 gives −j1 and j5; ω = 10 gives −j0.5 and j10).

$$ω = 5:  v′ = \frac{75}{8(0.125 + j0.8)} = 11.578∠−81.12° V        ω = 10:  v″ = \frac{6}{0.125 + j1.9} = 3.151∠−86.24° V$$

:::ans
**v_{o} = 11.578 sin(5t − 81.12°) + 3.151 cos(10t − 86.24°) V** (= book; it prints 3.154, a rounding difference)
:::

<div class="qhead"><span class="qn">B83 · Practice Problem 10.7</span><span class="qt">AC source transformation <span class="lvl plain">practice</span></span></div>

:::q
Find I_{o} in the circuit of Fig. 10.19 using the concept of source transformation.
:::

[[img:sd_pp10_7|Fig. 10.19|w=46]]

$$12∠90° ∥ (4 − j3)  ⇒  V = j12(4 − j3) = 36 + j48 V behind 4 − j3;   + (2 + j1)  ⇒  behind 6 − j2 Ω$$

$$⇒  I = \frac{36 + j48}{6 − j2} = 3 + j9 A ∥ (6 − j2);   ∥ j5 Ω  ⇒  Z_{p} = 3.333 + j3.333 Ω$$

$$I_{o} = (3 + j9) × \frac{Z_{p}}{Z_{p} + 1 − j2}$$

:::ans
**I_{o} = −1.622 + j9.730 = 9.863∠99.46° A** (= book)
:::

<div class="qhead"><span class="qn">B84 · Problem 10.40</span><span class="qt">AC superposition · DC + AC <span class="lvl plain">practice</span></span></div>

:::q
Find i_{o} in the circuit shown in Fig. 10.85 using superposition.
:::

[[img:sd10_40|Fig. 10.85|w=46]]

Same circuit as Part A's 5.5(b); here the textbook answer confirms the correction made there.

$$8 V (ω = 0, L short):  i_{o}′ = \frac{8}{2} = 4 A        10 cos 4t (L = j4):  I = \frac{10}{4 + j4 ∥ 2} = 1.768∠−8.13° A,  i_{o}″ = I × \frac{2}{2 + j4} = 0.791∠−71.57° A$$

:::ans
**i_{o} = 4 + 0.791 cos(4t − 71.57°) A** (even problem; per-frequency node solves agree)
:::

<div class="qhead"><span class="qn">B85 · Problem 10.41</span><span class="qt">AC superposition · one source, two frequencies <span class="lvl light">new idea</span></span></div>

:::q
Find v_{o} for the circuit in Fig. 10.86, assuming that v_{s} = 6 cos 2t + 4 sin 4t V.
:::

[[img:sd10_41|Fig. 10.86|w=30]]

:::new Hint: what's new
- **One source holding two frequencies** is two sources in series. Treat each term as its own source.
:::

$$ω = 2:  Z_{C} = \frac{1}{j2 × 0.25} = −j2,   V′ = 6 × \frac{2}{2 − j2} = 4.243∠45° V$$

$$ω = 4:  Z_{C} = −j1,   V″ = 4 × \frac{2}{2 − j1} = 3.578∠26.57° V$$

:::ans
**v_{o} = 4.243 cos(2t + 45°) + 3.578 sin(4t + 26.57°) V** (App. D prints 25.56°; tan^{−1}(1/2) = 26.57°, so that is a typo)
:::

<div class="qhead"><span class="qn">B86 · Problem 10.42</span><span class="qt">AC superposition · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 10.87, design a problem to help other students better understand the superposition theorem.
:::

[[img:sd10_42|Fig. 10.87|w=46]]

**One design.** V_{1} = 10∠0° V, V_{2} = 5∠0° V, X_{L} = 2 Ω, R_{1} = 4 Ω, X_{C} = 4 Ω, R_{2} = 2 Ω: *find I_{o}* (current from the R_{1} node into the −jX_{C} / R_{2} side).

$$V_{1} alone:  4 ∥ (−j4) ∥ 2 = 1.2 − j0.4 Ω,  V′ = 2 − j6 V,  I_{o}′ = \frac{V′}{−j4} + \frac{V′}{2} = 2.5 − j2.5 A$$

$$V_{2} alone:  V″ = 3 + j1 V,  I_{o}″ = \frac{V″}{−j4} + \frac{V″ − 5}{2} = −1.25 + j1.25 A$$

:::ans
**(this design) I_{o} = 1.25 − j1.25 = 1.768∠−45° A** (design problem)
:::

<div class="qhead"><span class="qn">B87 · Problem 10.43</span><span class="qt">AC superposition <span class="lvl plain">practice</span></span></div>

:::q
Using the superposition principle, find i_{x} in the circuit of Fig. 10.88.
:::

[[img:sd10_43|Fig. 10.88 (ω = 2: 4 H → j8, \frac{1}{8} F → −j4)|w=56]]

$$Current source alone:  i_{x}′ = 8.000∠−133.13° A        Voltage source alone:  i_{x}″ = \frac{10∠−60°}{3 − j4 + j8} = 2∠−113.13° A$$

:::ans
**i_{x} = 9.903 cos(2t − 129.17°) A** (= App. D)
:::

<div class="qhead"><span class="qn">B88 · Problem 10.44</span><span class="qt">AC superposition · two frequencies <span class="lvl plain">practice</span></span></div>

:::q
Use the superposition principle to obtain v_{x} in the circuit of Fig. 10.89. Let v_{s} = 50 sin 2t V and i_{s} = 12 cos(6t + 10°) A.
:::

[[img:sd10_44|Fig. 10.89|w=46]]

$$ω = 2 (5 H → j10):  V′ = 50 × \frac{16}{16 + 20 + j10} = 21.41∠−15.52° V$$

$$ω = 6 (5 H → j30):  V″ = 12∠10° × [16 ∥ (20 + j30)] = 147.7∠26.50° V$$

:::ans
**v_{x} = 21.41 sin(2t − 15.52°) + 147.7 cos(6t + 26.50°) V** (even problem; node solves agree)
:::

<div class="qhead"><span class="qn">B89 · Problem 10.45</span><span class="qt">AC superposition · series loop <span class="lvl plain">practice</span></span></div>

:::q
Use superposition to find i(t) in the circuit of Fig. 10.90.
:::

[[img:sd10_45|Fig. 10.90|w=44]]

$$ω = 10:  I′ = \frac{16∠30°}{20 + j3} = 0.7911∠21.47° A        ω = 4 (opposes i):  I″ = \frac{−6}{20 + j1.2} = 0.2995∠176.57° A$$

:::ans
**i(t) = 791.1 cos(10t + 21.47°) + 299.5 sin(4t + 176.57°) mA** (= App. D)
:::

<div class="qhead"><span class="qn">B90 · Problem 10.46</span><span class="qt">AC superposition · three frequencies <span class="lvl plain">practice</span></span></div>

:::q
Solve for v_{o}(t) in the circuit of Fig. 10.91 using the superposition principle.
:::

[[img:sd10_46|Fig. 10.91|w=58]]

$$10 V (ω = 0: C open, L short):  v_{o}′ = 10 V$$

$$12 cos 3t (C → −j4, L → j6):  −j4 ∥ j6 = −j12,  V″ = 12 × \frac{−j12}{6 − j12} = 10.73∠−26.57° V$$

$$4 sin 2t (C → −j6, L → j4):  6 ∥ (−j6) ∥ j4 = 4.8 + j2.4 Ω,  V‴ = 4(4.8 + j2.4) = 21.47∠26.57° V$$

:::ans
**v_{o}(t) = 10 + 10.73 cos(3t − 26.57°) + 21.47 sin(2t + 26.57°) V** (even problem; node solves agree)
:::

<div class="qhead"><span class="qn">B91 · Problem 10.47</span><span class="qt">AC superposition · three frequencies <span class="lvl plain">practice</span></span></div>

:::q
Determine i_{o} in the circuit of Fig. 10.92, using the superposition principle.
:::

[[img:sd10_47|Fig. 10.92|w=58]]

$$24 V (DC: C open, L short):  the loop 2 Ω → 24 V → 4 Ω gives 6i = 24,  i_{o}′ = 4 A$$

$$10 sin(t − 30°) (ω = 1: C → −j6, L → j2):  Z_{A} = 2 ∥ (4 + j2) = 1.4 + j0.2,  I = \frac{10∠−30°}{1 − j6 + Z_{A}} = 1.593∠37.52°,  i_{o}″ = I × \frac{2}{6 + j2} = 0.504∠19.09° A$$

$$2 cos 3t (ω = 3: C → −j2, L → j6):  2 ∥ (1 − j2) = 1.077 − j0.615,  i_{o}‴ = 2 × \frac{1.077 − j0.615}{1.077 − j0.615 + 4 + j6} = 0.3352∠−76.43° A$$

:::ans
**i_{o} = 4 + 0.504 sin(t + 19.09°) + 0.3352 cos(3t − 76.43°) A** (= App. D)
:::

<div class="qhead"><span class="qn">B92 · Problem 10.48</span><span class="qt">AC superposition · three frequencies <span class="lvl plain">practice</span></span></div>

:::q
Find i_{o} in the circuit of Fig. 10.93 using superposition.
:::

[[img:sd10_48|Fig. 10.93|w=50]]

$$24 V (DC):  C open, L short ⇒ one path 100 + 80 + 60 Ω:  i_{o}′ = \frac{24}{240} = 0.1 A$$

$$50 cos 2000t (C → −j25, L → j80):  node solve,  i_{o}″ = 0.2175∠134.12° A$$

$$2 sin 4000t (C → −j12.5, L → j160):  node solve,  i_{o}‴ = 1.178∠−172.62° A$$

:::ans
**i_{o} = 0.1 + 0.2175 cos(2000t + 134.12°) + 1.178 sin(4000t − 172.62°) A** (even problem)
:::

<div class="qhead"><span class="qn">B93 · Problem 10.49</span><span class="qt">AC source transformation <span class="lvl plain">practice</span></span></div>

:::q
Using source transformation, find i in the circuit of Fig. 10.94.
:::

[[img:sd10_49|Fig. 10.94 (ω = 200: 5 mH → j1, 1 mF → −j5)|w=44]]

$$8∠30° ∥ 5 Ω  ⇒  40∠30° V behind 5 Ω;   i = \frac{40∠30°}{5 + 3 + j1 − j5} = \frac{40∠30°}{8.944∠−26.57°}$$

:::ans
**i = 4.472 sin(200t + 56.57°) A** (= App. D)
:::

<div class="qhead"><span class="qn">B94 · Problem 10.50</span><span class="qt">AC source transformation · design problem <span class="lvl plain">practice</span></span></div>

:::q
Using Fig. 10.95, design a problem to help other students understand source transformation.
:::

[[img:sd10_50|Fig. 10.95|w=40]]

**One design.** v_{s} = 10 cos 2t V, R_{1} = 2 Ω, C = 0.25 F (→ −j2), L = 1 H (→ j2), R_{2} = 2 Ω: *find v_{o}*.

$$10 V behind 2 Ω ⇒ 5 A ∥ 2 Ω;  ∥ −j2 ⇒ 5 A ∥ (1 − j1) ⇒ 5(1 − j1) V behind 1 − j1$$

$$v_{o} = 5(1 − j1) × \frac{2}{1 − j1 + j2 + 2} = \frac{10 − j10}{3 + j1} = 2 − j4 = 4.472∠−63.43° V$$

:::ans
**(this design) v_{o} = 4.472 cos(2t − 63.43°) V** (design problem)
:::

<div class="qhead"><span class="qn">B95 · Problem 10.51</span><span class="qt">AC source transformation <span class="lvl plain">practice</span></span></div>

:::q
Use source transformation to find I_{o} in the circuit of Prob. 10.42.
:::

With B86's design values: V_{1}/jX_{L} = \frac{10}{j2} = −j5 A ∥ j2, and V_{2}/R_{2} = 2.5 A ∥ 2 Ω. At the single node (everything in parallel):

$$V(\frac{1}{j2} + \frac{1}{4} + \frac{1}{−j4} + \frac{1}{2}) = −j5 + 2.5  ⇒  V = \frac{2.5 − j5}{0.75 − j0.25} = 5 − j5 V$$

$$I_{o} = \frac{V}{−j4} + \frac{V − 5}{2} = 1.25 − j1.25 A$$

:::ans
**(B86 design) I_{o} = 1.768∠−45° A**, the same as by superposition. (App. D prints 109.3∠30° mA. That value depends on design values the book never states, so it cannot be checked against this design.)
:::

<div class="qhead"><span class="qn">B96 · Problem 10.52</span><span class="qt">AC source transformation <span class="lvl plain">practice</span></span></div>

:::q
Use the method of source transformation to find I_{x} in the circuit of Fig. 10.96.
:::

[[img:sd10_52|Fig. 10.96|w=48]]

$$\frac{60}{2 + j4} = 6 − j12 A ∥ (2 + j4);  ∥ 6 Ω ⇒ Z_{1} = 2.4 + j1.8,  V_{1} = 36 − j18 V$$

$$+ (−j2) ⇒ Z_{2} = 2.4 − j0.2;  \frac{V_{1}}{Z_{2}} = 15.517 − j6.207 A;  + j5 ⇒ 15.517 − j1.207 A ∥ Z_{2}$$

$$I_{x} = (15.517 − j1.207) × \frac{Z_{2}}{Z_{2} + 4 − j3}$$

:::ans
**I_{x} = 5 + j1.5625 = 5.239∠17.35° A** (even problem; node solve agrees)
:::

<div class="qhead"><span class="qn">B97 · Problem 10.53</span><span class="qt">AC source transformation · ladder <span class="lvl plain">practice</span></span></div>

:::q
Use the concept of source transformation to find V_{o} in the circuit of Fig. 10.97.
:::

[[img:sd10_53|Fig. 10.97|w=52]]

$$5 A ∥ (4 ∥ j2 = 0.8 + j1.6) ⇒ V_{1} = 4 + j8 V;  + (−j3) ⇒ Z_{2} = 0.8 − j1.4;  ∥ 2 Ω ⇒ Z_{3} = 0.857 − j0.571,  V_{3} = j5.714 V$$

$$V_{o} = V_{3} × \frac{−j2}{Z_{3} + j4 − j2}$$

:::ans
**V_{o} = 3.529 − j5.882 = 6.860∠−59.04° V** (= App. D)
:::

<div class="qhead"><span class="qn">B98 · Problem 10.54</span><span class="qt">AC source transformation <span class="lvl plain">practice</span></span></div>

:::q
Rework Prob. 10.7 using source transformation.
:::

Prob. 10.7 (§10.2): *Use nodal analysis to find V in the circuit of Fig. 10.56.*

[[img:sd10_7|Fig. 10.56; the 6∠30° A points down, out of node V.|w=50]]

$$I_{1} = \frac{120∠−15°}{40 + j20} = 2.683∠−41.57° A  in parallel with  40 + j20 Ω$$

$$Net current into V:  I_{1} − 6∠30° = −3.189 − j4.780 A$$

$$Y = \frac{1}{40 + j20} + \frac{1}{−j30} + \frac{1}{50} = 0.04 + j0.02333 S,   V = \frac{−3.189 − j4.780}{0.04 + j0.02333}$$

:::ans
**V = 124.08∠−153.96° V** (the App. D answer to Prob. 10.7, 124.08∠−154° V; node solve agrees)
:::
