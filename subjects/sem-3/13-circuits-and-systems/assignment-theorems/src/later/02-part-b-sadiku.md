# Part B · Sadiku (unsolved problems)

<div class="sub">Alexander & Sadiku, <i>Fundamentals of Electric Circuits</i> 5e · ch. 4 §4.3 Superposition · practice problems first, then end-of-chapter problems</div>

Part A already covered the method, so most Sadiku questions are plain practice. An orange box appears only when a question adds something new.

<div class="qhead"><span class="qn">B1 · Practice Problem 4.3</span><span class="qt">Superposition · DC <span class="lvl plain">practice</span></span></div>

:::q
Using the superposition theorem, find v_{o} in the circuit of Fig. 4.8.
:::

[[img:sd_pp4_3||w=45]]

**Given:** 5 A current source, 12 V voltage source, 2 Ω, 3 Ω, 5 Ω.

**To find:** v_{o} across the 2 Ω (+ at the top).

**Case (i): 5 A acting alone** (12 V shorted). From the middle node, the 5 A has two paths to ground: 3 Ω + 2 Ω = 5 Ω on the left, and 5 Ω on the right. The two paths are equal, so the current splits evenly, 2.5 A each:

$$v_{o}′ = 2.5 × 2 = 5 V$$

**Case (ii): 12 V acting alone** (5 A opened). The 5 Ω, 3 Ω and 2 Ω are in series:

$$i = \frac{12}{5 + 3 + 2} = 1.2 A  ⇒  v_{o}″ = 1.2 × 2 = 2.4 V$$

**By superposition:** v_{o} = v_{o}′ + v_{o}″ = 5 + 2.4 = 7.4 V

:::ans
**v_{o} = 7.4 V** (= book answer, 7.4 V)
:::

<div class="qhead"><span class="qn">B2 · Problem 4.8</span><span class="qt">Superposition · DC <span class="lvl light">new idea</span></span></div>

:::q
Using superposition, find V_{o} in the circuit of Fig. 4.76. (The book adds "check with PSpice or MultiSim". The check below uses a direct node equation instead.)
:::

[[img:sd4_8|Fig. 4.76|w=42]]

:::new
- **One-node shortcut.** When every branch meets at a single node, don't reach for dividers. Write one KCL at that node in each case. Here the node is V_{o}, with three branches to ground: 4 + 5 = 9 Ω, 3 Ω (+ 9 V source), 1 Ω (+ 3 V source).
:::

**Given:** 9 V and 3 V sources; branches from V_{o}: 4 Ω + 5 Ω, 3 Ω, 1 Ω.

**To find:** V_{o}.

**Case (i): 9 V alone** (3 V shorted). KCL at V_{o}:

$$\frac{V_{o}′}{9} + \frac{V_{o}′ − 9}{3} + \frac{V_{o}′}{1} = 0  ⇒  V_{o}′(13/9) = 3  ⇒  V_{o}′ = \frac{27}{13} V$$

**Case (ii): 3 V alone** (9 V shorted). KCL at V_{o}:

$$\frac{V_{o}″}{9} + \frac{V_{o}″}{3} + \frac{V_{o}″ − 3}{1} = 0  ⇒  V_{o}″(13/9) = 3  ⇒  V_{o}″ = \frac{27}{13} V$$

**By superposition:** V_{o} = \frac{27}{13} + \frac{27}{13} = \frac{54}{13} V

:::ans
**V_{o} = 54/13 ≈ 4.154 V** (even-numbered problem, so the book prints no answer)
:::

:::note Check
Both sources at once: \frac{V_{o}}{9} + \frac{V_{o} − 9}{3} + (V_{o} − 3) = 0 gives \frac{13}{9}V_{o} = 6, so V_{o} = 54/13 V ✓.
:::

<div class="qhead"><span class="qn">B3 · Problem 4.9</span><span class="qt">Superposition + linearity <span class="lvl light">new idea</span></span></div>

:::q
Given that I = 4 A when V_{s} = 40 V and I_{s} = 4 A, and I = 1 A when V_{s} = 20 V and I_{s} = 0, use superposition and linearity to determine the value of I when V_{s} = 60 V and I_{s} = −2 A.
:::

[[img:sd4_9|Fig. 4.77 (no resistor values given)|w=45]]

:::new
- **Superposition without the circuit values.** In a linear circuit, any response is a weighted sum of the sources: **I = aV_{s} + bI_{s}**. The constants a and b come from the circuit, but you can find them from the data instead. Two measurements give two equations for a and b.
:::

**Given:** (V_{s}, I_{s}, I) = (40 V, 4 A, 4 A) and (20 V, 0, 1 A).

**To find:** I for V_{s} = 60 V, I_{s} = −2 A.

By superposition and linearity, I = aV_{s} + bI_{s}.

From the second measurement (I_{s} = 0): 1 = 20a, so **a = 0.05 A/V**.

From the first measurement: 4 = 40(0.05) + 4b = 2 + 4b, so **b = 0.5**.

Now: I = 0.05 × 60 + 0.5 × (−2) = 3 − 1 = 2 A

:::ans
**I = 2 A** (= Appendix D answer, 2 A)
:::

:::note Side note
The resistors are fixed, so a and b are fixed numbers. Exam questions sometimes give a "black box" table like this one and call it the *linearity property*. It is solved the same way.
:::
