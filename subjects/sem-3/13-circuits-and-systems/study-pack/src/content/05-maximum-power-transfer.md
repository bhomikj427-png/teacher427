# 05 — Maximum power transfer

<div class="sub">Class notes p.13–14, p.16–17 · 2 board question sets · needs 04</div>

## Map

[[map:1 Power in the load > 2 The condition R_{L} = R_{Th} > 3 P_{max} and the 50 % efficiency > 4 AC loads: conjugate match|here=1]]

## The questions this file answers

- <span class="tag">Class p.16–17</span> 10 V source, 10 kΩ, variable R_{L}: for what R_{L} is power maximum? Total power from the source? Power in R_{Th}? Efficiency? Voltage across the load? How do the load's voltage and power compare with the source's?
- <span class="tag">Class p.17</span> 10 V source, 5 kΩ: find R for maximum power, the maximum power, and the efficiency.

---

## Build

:::q <span class="tag">Class p.16</span>
For what value of load resistance will maximum power be delivered? Then: determine the total power delivered by the source.
:::

[[fig:mpt_q|The board circuit: a 10 V source with 10 kΩ in series, driving a variable load.|w=45]]

:::guess Guess first
Make R_{L} tiny, then huge. What happens to the load's power at each extreme? So where must the maximum be?
:::

### 1 · Power in the load

From 04, every linear source network is V_{Th} in series with R_{Th}, so this circuit is already in that form. The load current and power:

$$I_{L} = \frac{V_{Th}}{R_{Th} + R_{L}}      P_{L} = I_{L}^{2} R_{L} = \frac{V_{Th}^{2} R_{L}}{(R_{Th} + R_{L})^{2}}$$

:::note Class p.13
The first attempt on the board used P_{L} = V_{Th}^{2}/(R_{Th} + R_{L}), which is wrong; it was crossed out and redone with **P_{L} = I_{L}^{2}R_{L}** (starred). Use the starred one.
:::

The Guess answer: tiny R_{L} gives big current but almost no voltage, so P ≈ 0. Huge R_{L} gives big voltage but almost no current, so P ≈ 0. The power must peak somewhere in between:

[[fig:mpt_curve|Top: the load's power peaks exactly at R_{L} = R_{Th}. Bottom: efficiency keeps rising with R_{L}, and is only 50 % at that peak.|w=78]]

### 2 · The condition (class p.13–14 derivation)

Set \frac{dP_{L}}{dR_{L}} = 0. Quotient rule:

$$\frac{dP_{L}}{dR_{L}} = V_{Th}^{2}·\frac{(R_{Th} + R_{L})^{2} − R_{L}·2(R_{Th} + R_{L})}{(R_{Th} + R_{L})^{4}} = 0$$

The numerator must be zero:

$$(R_{Th} + R_{L})^{2} − 2R_{L}(R_{Th} + R_{L}) = 0 ⇒ R_{Th}^{2} + 2R_{Th}R_{L} + R_{L}^{2} − 2R_{Th}R_{L} − 2R_{L}^{2} = 0 ⇒ R_{Th}^{2} = R_{L}^{2}$$

$$R_{L} = R_{Th}$$

(The negative root is not a resistance. The curve above shows it is a maximum, not a minimum.)

**Answer, part 1:** R_{L} = R_{Th} = **10 kΩ**.

### 3 · P_{max}, source power, efficiency

Put R_{L} = R_{Th} into P_{L}:

$$P_{max} = \frac{V_{Th}^{2}}{4R_{Th}}$$

For the board circuit, at R_{L} = 10 kΩ:

| Quantity | Working | Value |
|---|---|---|
| Current | 10 V / 20 kΩ | **0.5 mA** |
| Total power from the source | V·I = 10 × 0.5 mA | **5 mW** |
| Power in the load | I^{2}R_{L} = (0.5 mA)^{2} × 10 kΩ = V_{Th}^{2}/4R_{Th} | **2.5 mW** |
| Power in R_{Th} | same current, same resistance | **2.5 mW** |
| Efficiency η | P_{load} / P_{total} = 2.5 / 5 | **50 %** |
| Voltage across the load | 0.5 mA × 10 kΩ | **5 V = V_{s}/2** |
| Load vs source | | **V_{L} = V_{s}/2, P_{L} = P_{s}/2** |

:::note Class p.16
The notes read "I × V = 0 5 mW" with no visible decimal point. The value is **5 mW**. The 50 % efficiency on p.17 is right either way.
:::

**Maximum power is not maximum efficiency.** η = \frac{R_{L}}{R_{Th} + R_{L}} keeps rising as R_{L} grows (bottom plot), while P_{L} falls. So:

- **communication / signal circuits** match R_{L} = R_{Th}: a weak signal needs every bit of power delivered, and 50 % loss is acceptable;
- **power systems** keep R_{L} ≫ R_{Th}: wasting half the generated power would be unacceptable.

The 50 % refers to the Thévenin equivalent. The power actually lost inside the original, full network can differ.

:::check Check 1
(a) Why is exactly half the power lost at the match? Use the fact that R_{Th} and R_{L} carry the same current. (b) The class p.17 question: 10 V with 5 kΩ. Find R, P_{max}, η.
:::

### 4 · AC loads: the conjugate match

:::guess Predict
A source has Z_{Th} = 3 + j4 Ω. Its reactance j4 Ω doesn't absorb power, but it does limit the current. What reactance should the load add?
:::

For impedances (class p.16):

$$Z_{L} = Z_{Th}^{*}   (the complex conjugate: j → −j)$$

- **R_{L} = R_{Th}**: the resistance match, as before.
- **X_{L} = −X_{Th}**: the load's reactance **cancels** the source's, so the loop is purely resistive and the current is as large as possible.

For the Predict: Z_{L} = 3 − j4 Ω. Then P_{max} = \frac{|V_{Th}|^{2}}{4R_{Th}}, with V_{Th} as an rms value.

---

## Exam form

**Statement.** A linear network delivers maximum power to a resistive load when R_{L} = R_{Th}. The maximum power is P_{max} = V_{Th}^{2}/(4R_{Th}). For an AC network with a complex load, the condition is Z_{L} = Z_{Th}^{*}.

**Derivation.** P_{L} = V_{Th}^{2}R_{L}/(R_{Th}+R_{L})^{2}; set dP_{L}/dR_{L} = 0 ⇒ R_{L} = R_{Th} (step 2).

**At the match.** η = 50 %, V_{L} = V_{Th}/2, P_{L} = P_{s}/2.

## Traps

- Using P = V_{Th}^{2}/(R_{Th} + R_{L}) (the crossed-out attempt on class p.13).
- Saying "maximum power means maximum efficiency".
- In the AC case, matching Z_{L} = Z_{Th} instead of the **conjugate**.
- Forgetting to find R_{Th} first when the source network is more than one resistor: use 04.

## Self-test

1. Derive R_{L} = R_{Th} (three lines).
2. V_{Th} = 12 V, R_{Th} = 3 kΩ. Find P_{max} and the source power at that point.
3. Why do power companies not operate at maximum power transfer?
4. Z_{Th} = 50 − j20 Ω. Load for maximum power?
5. In the 04 board circuit (V_{Th} = 20/3 V, R_{Th} = 8/3 kΩ), what R_{L} gets maximum power, and how much?

<!--ANSWERS-->
## Answers

**Check 1.** (a) At the match, R_{Th} = R_{L} and both carry the same current, so I^{2}R_{Th} = I^{2}R_{L}: equal power in each, i.e. half of the total. (b) R = **5 kΩ**; P_{max} = 10^{2}/(4 × 5 kΩ) = **5 mW**; η = **50 %** (the source supplies 10 V × 1 mA = 10 mW).

**Self-test.**

1. P_{L} = V_{Th}^{2}R_{L}/(R_{Th}+R_{L})^{2}; the numerator of the derivative is (R_{Th}+R_{L})^{2} − 2R_{L}(R_{Th}+R_{L}) = 0; this gives R_{Th}^{2} = R_{L}^{2}, so R_{L} = R_{Th}.
2. P_{max} = 144/12k = **12 mW**; I = 12/6k = 2 mA; P_{s} = 24 mW.
3. Efficiency would be only 50 %: half of the generated power lost in the source and lines.
4. Z_{L} = **50 + j20 Ω**.
5. R_{L} = **8/3 kΩ ≈ 2.67 kΩ**; P_{max} = (20/3)^{2} / (4 × 8/3) = **4.17 mW**.
<!--/ANSWERS-->
