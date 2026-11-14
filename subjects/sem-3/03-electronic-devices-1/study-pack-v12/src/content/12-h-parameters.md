# 12 — h-parameters, multistage amplifiers, Darlington

<div class="sub">h-parameter problem pages (book pp. 131–145, Problems 3–16) · deck "Multi-Stage Amplifier" · syllabus Unit 5 · needs 10 (the CE connection) and 11 (a biased transistor)</div>

## Map

[[map:1 The h-parameter model > 2 CE analysis: Ai, Ri, Av, Yo > 3 Cascading > 4 Darlington pair|here=1]]

11 fixed the DC operating point. Now a small signal rides on top of it. For that signal the transistor is a box with two input and two output wires, described by four numbers.

## The questions this file answers

- <span class="tag">Book P9</span> CE amplifier, R_{s} = 800 Ω, R_{L} = 2 kΩ, h_{ie} = 1.1 k, h_{fe} = 50, h_{oe} = 25 μmho, h_{re} = 2.5 × 10^{−4}. Find A_{i}, R_{i}, A_{v}, R_{o}, R_{ot}, A_{p}, exact and approximate, and the % error in A_{i}.
- <span class="tag">Deck</span> Two stages with gains 40 and 60 are cascaded. Overall gain, as a number and in dB.
- <span class="tag">Deck</span> Derive β of a Darlington pair.

---

## Build

### 1 · The h-parameter model

:::guess Predict
A two-port has four quantities: v_{in}, i_{in}, v_{out}, i_{out}. If you pick two as inputs to the equations, how many coefficients describe the box?
:::

:::note Terms
**Two-port:** a box with an input pair and an output pair of terminals. **Small-signal quantities** (lower case: i_{b}, v_{ce}): the AC parts only. **mho (℧)** = siemens, 1/Ω.
:::

[[fig:h_model|The CE h-parameter model: h_{ie} with a voltage source h_{re}v_{ce} at the input; a current source h_{fe}i_{b} with 1/h_{oe} at the output.|w=70]]

$$v_{be} = h_{ie}i_{b} + h_{re}v_{ce}        i_{c} = h_{fe}i_{b} + h_{oe}v_{ce}$$

| Parameter | Name | Measured with | Unit | Typical (CE) |
|---|---|---|---|---|
| h_{ie} = v_{be}/i_{b} | input resistance | output shorted (v_{ce} = 0) | Ω | 1.1 kΩ |
| h_{re} = v_{be}/v_{ce} | reverse voltage ratio | input open (i_{b} = 0) | none | 2.5 × 10^{−4} |
| h_{fe} = i_{c}/i_{b} | forward current gain (≈ β) | output shorted | none | 50 |
| h_{oe} = i_{c}/v_{ce} | output admittance | input open | S | 25 μS |

The second subscript names the connection: e, b or c (h_{ib}, h_{fc}, …).

**Answer.** Four: two per equation. Their units are mixed (an impedance, an admittance, two ratios), so they are **hybrid** parameters.

:::check Check 1
(a) Which h-parameter is closest to β? (b) Why is h_{ie} measured with the output shorted?
:::

### 2 · CE amplifier analysis

:::q <span class="tag">Book P9</span>
A CE amplifier is driven by a source of internal resistance R_{s} = 800 Ω. The load is 2 kΩ. h_{ie} = 1.1 k, h_{fe} = 50, h_{oe} = 25 μmho, h_{re} = 2.5 × 10^{−4}. Compute A_{i}, R_{i}, A_{v}, R_{o}, R_{ot} and A_{p}, by (a) exact and (b) approximate analysis. Compute the % error in A_{i}.
:::

:::guess Guess first
h_{fe} is 50. Will the current gain into a real load be exactly 50, more, or less?
:::

| Quantity | Exact | Approximate (h_{oe}R_{L} &lt; 0.1) |
|---|---|---|
| A_{i} = i_{L}/i_{b} | −h_{fe}/(1 + h_{oe}R_{L}) | −h_{fe} |
| R_{i} | h_{ie} + h_{re}A_{i}R_{L} | h_{ie} |
| A_{v} | A_{i}R_{L}/R_{i} | −h_{fe}R_{L}/h_{ie} |
| Y_{o} (R_{o} = 1/Y_{o}) | h_{oe} − h_{fe}h_{re}/(h_{ie} + R_{s}) | 0, R_{o} → ∞ |
| Also | A_{vs} = A_{v}R_{i}/(R_{i} + R_{s}) · A_{p} = A_{i}A_{v} · R_{ot} = R_{o} ∥ R_{L} | |

Always in the order **A_{i} → R_{i} → A_{v} → Y_{o}**: each uses the one before. The minus signs are the CE phase reversal. The same formulas serve CB and CC with that connection's parameter set.

**Answer (a), exact.** A_{i} = −50/(1 + 0.05) = **−47.6**. R_{i} = 1100 + (2.5 × 10^{−4})(−47.6)(2000) = **1076.2 Ω**. A_{v} = (−47.6)(2000)/1076.2 = **−88.5**. A_{vs} = −88.5 × 1076.2/1876.2 = −50.75. Y_{o} = 25 μS − (50)(2.5 × 10^{−4})/1900 = 18.42 μS, **R_{o} = 54.28 kΩ**. **R_{ot}** = 54.28 k ∥ 2 k = **1.93 kΩ**. **A_{p}** = (−47.6)(−88.5) = **4214** (the book rounds earlier: 4210.6).

**(b), approximate** (h_{oe}R_{L} = 0.05 ✓). A_{i} = −50, R_{i} = 1100 Ω, A_{v} = −50 × 2000/1100 = −90.9. **Error in A_{i}** = (50 − 47.6)/47.6 = **5%**.

:::check Check 2
(a) h_{ie} = 1 kΩ, h_{fe} = 100, R_{L} = 1 kΩ: approximate A_{i}, R_{i}, A_{v}. (b) What condition allows the approximate model?
:::

### 3 · Cascading stages

:::q <span class="tag">Deck</span>
Two amplifier stages with voltage gains 40 and 60 are cascaded. Find the overall gain as a number and in dB.
:::

:::guess Guess first
Do the gains add or multiply?
:::

[[fig:two_stage|Two RC-coupled CE stages.|w=75]]

The overall gain is the **product** of the stage gains, where each stage's gain is found with the next stage connected as its load (R_{i} of stage 2 loads stage 1). In decibels, A_{v}(dB) = 20 log_{10}|A_{v}|, and the stage values **add**.

| Coupling | How | For · against |
|---|---|---|
| RC | a capacitor between stages | cheap, small, good at audio; blocks DC so each stage biases separately; gain falls at low f |
| Transformer | a transformer | matches impedances for maximum power; bulky, costly, poor frequency response |
| Direct | a wire | amplifies down to DC; bias of one stage disturbs the next; drift is amplified |

**Answer.** A_{v} = 40 × 60 = **2400**. 20 log 40 + 20 log 60 = 32.0 + 35.6 = **67.6 dB**.

:::check Check 3
(a) Why is the gain of stage 1 lower once stage 2 is connected? (b) Which coupling can amplify a DC signal?
:::

### 4 · The Darlington pair

:::q <span class="tag">Deck</span>
Derive the current gain of a Darlington pair.
:::

:::guess Guess first
Q1's emitter current is Q2's base current. Roughly what is the overall β?
:::

[[fig:darlington|Darlington pair: the emitter of Q1 drives the base of Q2; collectors joined.|w=40]]

I_{E1} = (1 + β_{1})I_{B}, and I_{E2} = (1 + β_{2})I_{E1} = (1 + β_{1})(1 + β_{2})I_{B}. The collector current is I_{E2} − I_{B} = (β_{1}β_{2} + β_{1} + β_{2})I_{B}:

$$β_{D} = β_{1}β_{2} + β_{1} + β_{2} ≈ β_{1}β_{2}$$

Two base–emitter drops in series: V_{BE} ≈ 1.4 V. Very high input resistance. Used as an emitter follower to drive heavy loads. DC bias with R_{B} and R_{E}: I_{B} = (V_{CC} − V_{BE})/(R_{B} + β_{D}R_{E}).

**Answer.** β_{D} = β_{1}β_{2} + β_{1} + β_{2}, about β_{1}β_{2}: a "super-β" transistor.

:::check Check 4
Two transistors with β = 100 each form a Darlington pair. Find β_{D} exactly.
:::

---

## Exam form

**h-parameters.** Two equations; the table of four with name, test condition and unit; why "hybrid"; draw the model.

**CE analysis.** A_{i} = −h_{fe}/(1 + h_{oe}R_{L}) → R_{i} = h_{ie} + h_{re}A_{i}R_{L} → A_{v} = A_{i}R_{L}/R_{i} → Y_{o} = h_{oe} − h_{fe}h_{re}/(h_{ie} + R_{s}); A_{vs}, A_{p}, R_{ot}. Approximate when h_{oe}R_{L} &lt; 0.1. Percentage error.

**Multistage.** Product of gains (loaded), dB add; RC, transformer, direct coupling compared.

**Darlington.** Derivation of β_{D}; V_{BE} ≈ 1.4 V; high R_{i}.

## Traps

- Computing R_{i} before A_{i}: R_{i} needs A_{i}.
- Dropping the minus sign on A_{i} and A_{v}.
- Using μmho as mho: 25 μmho = 25 × 10^{−6} S.
- Multiplying unloaded stage gains.
- Forgetting R_{s} in Y_{o}.

## Self-test

1. Define the four CE h-parameters with their test conditions.
2. h_{ie} = 2 kΩ, h_{fe} = 80, h_{oe} = 10 μS, R_{L} = 4 kΩ. Is the approximate model allowed? Find approximate A_{i}, R_{i}, A_{v}.
3. For Q2, find the exact A_{i}.
4. Three stages have gains 10, 20 and 30. Overall gain, and in dB?
5. A Darlington pair has β_{1} = 50, β_{2} = 80. Find β_{D}.
6. Compare RC and direct coupling in three points.

<!--ANSWERS-->

## Answers

**Check 1.** (a) h_{fe}. (b) Shorting the output sets v_{ce} = 0, so the h_{re}v_{ce} term vanishes and v_{be}/i_{b} is h_{ie} alone.

**Check 2.** (a) A_{i} = **−100**, R_{i} = **1 kΩ**, A_{v} = −100 × 1/1 = **−100**. (b) h_{oe}R_{L} &lt; 0.1.

**Check 3.** (a) Stage 2's input resistance is in parallel with stage 1's collector resistor, lowering its effective load. (b) Direct coupling.

**Check 4.** 100 × 100 + 100 + 100 = **10 200**.

**Self-test.**

1. See step 1's table.
2. h_{oe}R_{L} = 0.04 &lt; 0.1 ✓. A_{i} = **−80**, R_{i} = **2 kΩ**, A_{v} = −80 × 4/2 = **−160**.
3. A_{i} = −80/1.04 = **−76.9**.
4. 10 × 20 × 30 = **6000**; 20 log 6000 = **75.6 dB**.
5. 4000 + 50 + 80 = **4130**.
6. RC blocks DC (separate biasing, no drift passed on), cheap, low-frequency roll-off. Direct passes DC (amplifies DC signals), stages' biases interact, drift is amplified.

<!--/ANSWERS-->
