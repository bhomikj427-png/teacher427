# 12 — Asynchronous (ripple) counters

<div class="sub">Deck 10 (slides 4–17) · syllabus Unit 3 · needs 09 (T and JK flip-flops toggling)</div>

## Map

[[map:1 Ripple up and down > 2 MOD-N by reset, cascading|here=1]]

The cheapest counter: chain toggling flip-flops so each clocks the next. It costs no gates, but its outputs settle one after another. 13 removes that delay.

## The questions this file answers

- <span class="tag">Deck 10 slides 4–11</span> How does a ripple counter count, and what is its flaw?
- <span class="tag">Deck 10 slides 12–13</span> Design an asynchronous decade counter.

---

## Build

### 1 · Ripple up and down counters

:::guess Predict
FF0 toggles on every falling clock edge. FF1 toggles whenever Q_{0} falls. What sequence does Q_{1}Q_{0} go through?
:::

:::note Terms
**Counter:** steps through a fixed sequence, one step per clock pulse. **Asynchronous (ripple):** only the first flip-flop gets the clock; each other is clocked by the one before.
:::

[[fig:ripple_counter|3-bit ripple up counter and its waveforms; the shaded region shows the false states during 011 → 100.]]

- Every flip-flop toggles (T = 1 or J = K = 1). Reading Q_{2}Q_{1}Q_{0}: 0, 1, 2, … 7, 0: an **up counter**. Each Q is half the frequency of the one before: a **frequency divider**.
- Clock each stage from **Q'** instead and it counts **down** (with positive-edge flip-flops the rule swaps).
- **The flaw, ripple delay:** each stage waits for the one before. 011 → 100 passes through 010 and 000. Worst settling time **n·t_{pd}**; the clock period must exceed it, and anything reading the outputs sees false states.

**Answer.** 00, 01, 10, 11, 00: it counts up, and Q_{1} runs at a quarter of the clock frequency.

:::check Check 1
A 4-bit ripple counter uses flip-flops with t_{pd} = 25 ns. Worst settling time and highest usable clock frequency?
:::

### 2 · MOD-N by reset, and cascading

:::q <span class="tag">Deck 10 slides 12–13</span>
Design an asynchronous decade counter.
:::

:::guess Guess first
A decade counter has 10 states. How many flip-flops, and how do you stop it going on to 10, 11, … 15?
:::

**MOD less than 2^{n}.** Smallest n with 2^{n} ≥ MOD. Let it count normally, detect the **first unwanted state** with a NAND, and drive every flip-flop's active-low **CLEAR**. **Cascading** (deck 10 slides 16–17): clock a second counter from the last output of the first: MOD-M then MOD-N gives MOD-(M × N).

**Answer.** 8 &lt; 10 ≤ 16: **4 flip-flops**, all toggling, each clocked by the Q before it. The first unwanted state is 10 = **1010**, the first with Q_{3} and Q_{1} both 1: a **2-input NAND on Q_{3}, Q_{1}** drives all CLEARs. The count goes 0000 … 1001, shows 1010 for a few nanoseconds, and clears to 0000.

:::check Check 2
(a) <span class="tag">Deck 10 slide 14</span> Which outputs go to the NAND for MOD-7? For MOD-12? (b) Flip-flops for MOD-60? (c) A 10 kHz clock drives a MOD-10 counter: frequency of its last output?
:::

---

## Exam form

**Ripple counter.** Circuit, waveforms, up vs down connection, divide-by-2 per stage, ripple delay n·t_{pd} and the false states.

**MOD-N.** Number of flip-flops; first unwanted state; NAND → CLEAR; cascading.

## Traps

- Detecting state N − 1 instead of N.
- Including outputs that are 0 in state N in the NAND (only the 1s go in).
- Forgetting the momentary false state before clear.

## Self-test

1. Design a MOD-5 ripple counter: flip-flops and NAND inputs.
2. A 1 MHz clock drives a ripple counter. Frequency at Q_{0}? At Q_{3}?
3. A 3-bit ripple counter with t_{pd} = 20 ns: f_{max}?
4. How do you make a ripple counter count down?
5. MOD-6 by reset: NAND inputs?
6. How would you build MOD-24 from smaller counters?

<!--ANSWERS-->

## Answers

**Check 1.** 4 × 25 = **100 ns**; f_{max} = **10 MHz**.

**Check 2.** (a) MOD-7: clear at 111, **Q_{2}, Q_{1}, Q_{0}**. MOD-12: clear at 1100, **Q_{3}, Q_{2}**. (b) 32 &lt; 60 ≤ 64: **6**. (c) **1 kHz**.

**Self-test.**

1. **3 flip-flops**; clear at 101: NAND on **Q_{2}, Q_{0}**.
2. **500 kHz**; **62.5 kHz**.
3. 60 ns: **16.7 MHz**.
4. Clock each stage from the previous Q' (negative-edge flip-flops).
5. Clear at 110: **Q_{2}, Q_{1}**.
6. Cascade MOD-3 and MOD-8 (or MOD-4 and MOD-6): 3 × 8 = 24.

<!--/ANSWERS-->
