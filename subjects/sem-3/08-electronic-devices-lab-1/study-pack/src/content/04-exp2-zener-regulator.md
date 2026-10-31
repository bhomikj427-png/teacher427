# Exp 2 · Zener diode as a voltage regulator: line and load regulation

<div class="sub">Manual pp. 9–12 · LTspice / Virtual Lab · CO3 · the manual's printed data matches the simulation below digit-for-digit</div>

[[map:0 Instruments > 1 Zener curve > 2 Regulator > 3 Clipper > 4 Clamper|here=3]]

**What you already have:** from Exp 1, in breakdown V_{Z} stays ≈ 6.2 V while I_{Z} changes. From C&S, voltage dividers and KCL.

**Three terms first:**

- **Regulator:** a circuit that keeps V_{o} constant.
- **Line regulation:** how much V_{o} moves when the **input** V_{in} changes. The "line" is the supply line.
- **Load regulation:** how much V_{o} moves when the **load current** changes, i.e. when R_{L} changes.

:::q <span class="tag">Manual Exp 2, aim</span>
To use a zener diode for line and load regulation. Viva form: "Input rises from 14 V to 17 V and V_{o} rises by only 0.08 V. Where did the other 2.92 V go?"
:::

:::guess Guess first
Answer before reading on. Hint: there are only two other parts, R1 and the zener.
:::

## How a zener regulates

[[fig:exp02_line_circuit|Fig 2.1 (line regulation): V1 swept 0→20 V, with a fixed 1 kΩ load.|w=62]]

KCL at the output node: the current through R1 splits between the zener and the load.

$$I_{R1} = \frac{V_{in} − V_{Z}}{R_{1}} = I_{Z} + I_{L}$$

- **V_{in} rises:** the extra current all goes into the **zener**. V_{Z} barely moves (small r_{z}), so V_{o} stays put and **R1 absorbs the extra voltage**. That is the answer to the question.
- **R_{L} falls (more load current):** the zener gives up current to the load. V_{o} holds **as long as I_{Z} stays above I_{Z(min)}**.
- If the load demands more than R1 can supply, I_{Z} hits zero, the zener switches off, and V_{o} becomes an ordinary divider output that collapses.

Because the zener sits in parallel (shunt) with the load, this is called a **shunt regulator**.

## Line regulation (Fig 2.1)

:::do Do it (LTspice)
1. Draw V1, R1 = 1k, zener **BZX84C6V2L** (cathode to the output node), R2 = 1k load, and ground.
2. Label the output wire `vo` (F4).
3. Directive: `.dc V1 0 20 1`. Run.
4. Plot V(vo) against V1. Use cursors to read V_{o} at V_{in} = 14 V and 17 V.
:::

[[fig:exp02_line_plot|Two regions. Below about 12 V the zener is off and the output is half the input (1 kΩ:1 kΩ divider). Above it, V_{o} is pinned near 6.2–6.36 V.|w=78]]

**Why 12 V?** With the zener off, V_{o} = V_{in}/2. The zener turns on when V_{in}/2 reaches about 6.2 V, i.e. at V_{in} ≈ 12.4 V.

| V_{in} (V) | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|
| V_{o} (V) | 5.000 | 5.500 | 5.973 | 6.168 | **6.234** | 6.271 | 6.297 | **6.317** | 6.333 | 6.358 |

$$\% line regulation = \frac{ΔV_{o}}{ΔV_{in}} × 100 = \frac{6.317 − 6.234}{17 − 14} × 100 = \frac{0.083}{3} × 100 = 2.8 \%$$

## Load regulation (Fig 2.2)

[[fig:exp02_load_circuit|Fig 2.2 (load regulation): V1 fixed at 20 V, load stepped 100 Ω → 1100 Ω.|w=62]]

:::do Do it (LTspice)
1. Same circuit, but V1 = 20 V and the load value written as `{R}` (curly braces = a parameter).
2. Directives: `.step param R 100 1100 100` and `.op`. Run.
3. Plot V(vo). The x-axis is now R.
4. **No load:** delete R2, run `.op` again, and read V_{NL}.
5. Choose a full-load point (e.g. R = 1 kΩ) and read V_{FL}.
:::

[[fig:exp02_load_plot|Above about 450 Ω the output holds near 6.3 V. Below that, the load takes more current than R1 can supply.|w=78]]

| R_{L} (Ω) | 100 | 200 | 300 | 400 | 500 | 600 | 800 | 1000 | 1100 | no load |
|---|---|---|---|---|---|---|---|---|---|---|
| V_{o} (V) | 1.818 | 3.333 | 4.615 | 5.714 | 6.223 | 6.292 | 6.338 | **6.358** | 6.364 | **6.409** |

$$\% load regulation = \frac{V_{NL} − V_{FL}}{V_{FL}} × 100 = \frac{6.409 − 6.358}{6.358} × 100 = 0.81 \%$$

**Smallest load that still regulates:** R1 can pass at most (20 − 6.2)/1 kΩ = 13.8 mA. The load gets all of that only when I_{Z} → 0, so R_{L(min)} = 6.2 V / 13.8 mA ≈ **450 Ω**. This matches the knee in the plot. Below 450 Ω the zener is off, and V_{o} = 20 × R_{L}/(1000 + R_{L}): at 100 Ω that is 1.82 V ✓.

:::write Write in your record
**Result:** % line regulation = **2.8 %** (14–17 V, R_{L} = 1 kΩ); % load regulation = **0.81 %** (no load → 1 kΩ, V_{in} = 20 V). Lower % = better regulation.

**Theory for the record:** a zener shunt regulator places a reverse-biased zener across the load, fed through a series resistor R_{S}. In breakdown, the zener voltage is nearly constant, so changes in input voltage appear across R_{S}, and changes in load current are absorbed by a change in zener current. Regulation holds while I_{Z(min)} < I_{Z} < I_{Z(max)}. R_{S} is chosen so that I_{Z} ≥ I_{Z(min)} at minimum input and maximum load. Line regulation = ΔV_{o}/ΔV_{in} × 100 %; load regulation = (V_{NL} − V_{FL})/V_{FL} × 100 %.
:::

:::trap Trap: an "unregulated" line plot
If V_{o} keeps rising with slope ½ all the way to 20 V, the zener is in backwards (forward-biased, clamping at about 0.7 V) or is the wrong part. If V_{o} sticks at about 0.7 V, it is definitely reversed. The cathode (bar) must face the output node.
:::

:::check Check 1
(a) Why does V_{o} in the line plot still creep up slightly (6.23 → 6.36 V) instead of staying perfectly flat? (b) With V_{in} = 20 V and R_{L} = 1 kΩ, how much current does the zener carry? (c) What happens to I_{Z} when the load is removed, and why is that the worst case for zener power?
:::

<!--ANSWERS-->

## Answers

**Opening question.** Across R1. The extra input raises the current through R1 (it flows on into the zener), so R1's voltage drop rises by about 2.92 V.

**Check 1.** (a) The zener has a dynamic resistance r_{z} (Exp 1). More current through it means slightly more voltage: ΔV = r_{z}ΔI_{Z}. (b) I_{R1} = (20 − 6.358)/1000 = 13.64 mA, I_{L} = 6.358/1000 = 6.36 mA, so I_{Z} = 13.64 − 6.36 = **7.28 mA**. (c) All of R1's current then flows through the zener, its maximum, so I_{Z} and P_{Z} = V_{Z}I_{Z} peak. Design must keep this below I_{Z(max)}.

<!--/ANSWERS-->
