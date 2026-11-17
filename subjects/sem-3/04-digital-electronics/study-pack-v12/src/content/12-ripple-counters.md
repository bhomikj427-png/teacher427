# 12 — Asynchronous (ripple) counters

<div class="sub">Deck 10 (slides 2–17) · syllabus Unit 3 (asynchronous counters, MOD-N counters) · 1 real question set: deck 10 slide 14's four design exercises (no MTE or practice-set question) · needs 09 step 10 (T flip-flop: T = 1 toggles), 09 step 6 (clock edges), 10 step 7 (asynchronous clear)</div>

## Map

[[map:1 A toggling flip-flop halves the clock > 2 Two flip-flops count to 3 > 3 3-bit up counter > 4 Counting down > 5 Ripple delay > 6 MOD-6 by reset > 7 Decade counter > 8 Cascading|here=1]]

File 09 ended with the T flip-flop: with T = 1 it toggles at every active clock edge. This file chains toggling flip-flops so that each one's output is the next one's clock. The chain counts clock pulses in binary, divides the clock frequency by 2 at every stage, and costs no gates at all; its one flaw is that the stages change one after another, not together. File 13 removes that flaw by giving every flip-flop the same clock.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| CLK | the pulses being counted; drives only the first flip-flop | 1 kHz – 10 MHz |
| ↓, ↑ | a falling (1 → 0) and a rising (0 → 1) edge of a signal | — |
| FF0, FF1, … | the flip-flops, FF0 first in the chain | — |
| Q0, Q1, … | their outputs; Q0 is the least significant bit, the count is read Q2 Q1 Q0 | 0 or 1 |
| Q' | the complement output of a flip-flop | 1 − Q |
| n | number of flip-flops in the chain | 2 – 4 |
| MOD-N (modulus) | the number of different states the counter steps through before repeating | 2^{n} for a plain chain; 5, 6, 10, 12 with a reset |
| f | frequency: how many cycles per second a signal completes | kHz – MHz |
| t_{pd} | propagation delay of one flip-flop: time from its clock edge to its output changing | 10 – 25 ns |
| CLR' | active-low asynchronous clear: a 0 here forces Q = 0 at once, without a clock edge (10 step 7) | idle at 1 |

## Running example

**A 3-bit ripple up counter: three negative-edge T flip-flops with T = 1, FF0 clocked by CLK, FF1 by Q0, FF2 by Q1, starting at 000.** Step 3 counts it through 000 … 111 and back; step 4 rewires it to count down; step 5 times its 011 → 100 transition with t_{pd} = 10 ns; step 6 cuts it to MOD-6 with one NAND gate.

## The questions this file answers

- <span class="tag">Deck 10 slide 14 · Q1</span> Design 3-bit asynchronous up counter.
- <span class="tag">Deck 10 slide 14 · Q2</span> Design 3-bit asynchronous down counter negative edge triggering.
- <span class="tag">Deck 10 slide 14 · Q3</span> Design Mod-7 asynchronous up counter.
- <span class="tag">Deck 10 slide 14 · Q4</span> Design MOD-5 asynchronous down counter with positive edge triggering.
- <span class="tag">Deck 10 slides 10–13</span> Determine the counting sequence of the MOD-6 circuit; design an asynchronous decade counter.

---

## Build

### 1 · A toggling flip-flop halves the clock

**Anchor.** A light switch that flips at every press: press it 8 times and the lamp goes on 4 times. The lamp completes one on-off cycle for every two presses. A T flip-flop with T = 1 is that switch, and the presses are clock edges.

:::guess Predict
A negative-edge T flip-flop with T = 1 receives an 8 kHz clock. How many times per second does its output Q complete a full 0 → 1 → 0 cycle?
:::

:::note Terms
**Toggle:** Q changes to its complement (09 step 10: T = 1 gives Q⁺ = Q'). **Negative-edge triggered:** the flip-flop acts only at ↓ of its clock input (the bubble on the clock pin). **Frequency divider:** a circuit whose output frequency is the input frequency divided by a whole number.
:::

[[fig:u3_tdiv|What this graph plots: time across; rows CLK, Q_A, Q_B (high = 1). Q_A toggles at each clock edge, so it completes one cycle for every two clock cycles; Q_B, clocked by Q_A, completes one for every two of Q_A's.|w=78]]

Q changes once per clock cycle. It needs two changes (0 → 1, then 1 → 0) to complete one cycle of its own, so it completes one cycle per **two** clock cycles:

$$f_{Q} = f_{CLK} / 2$$

Read it as: *the output runs at half the speed of whatever clocks it.* Feed Q into a second toggling flip-flop and that one runs at a quarter of the clock; a third, an eighth.

| Stage | Clocked by | Frequency with an 8 kHz clock |
|---|---|---|
| FF0 | CLK | 8 / 2 = 4 kHz |
| FF1 | Q0 | 4 / 2 = 2 kHz |
| FF2 | Q1 | 2 / 2 = 1 kHz |

**Answer to the Predict.** **4000 times per second** (4 kHz): one output cycle per two clock cycles.

:::check Check 1
A 1 MHz clock drives a chain of two toggling flip-flops, each clocked by the one before. Frequency at Q0? At Q1?
:::

### 2 · Two flip-flops count to 3

Step 1 read the chain as a frequency divider. Read the same outputs together, as one binary number, and the chain counts.

:::q <span class="tag">Deck 10 slide 4 (EX 10.4)</span>
2-bit ripple binary counter: the output of one flip-flop is connected to the clock input of the next more-significant flip-flop.
:::

:::guess Guess first
FF0 toggles at every ↓ of CLK; FF1 toggles at every ↓ of Q0. Starting from Q1 Q0 = 00, write the four values after the first four clock pulses.
:::

:::note Terms
**Counter:** a circuit that steps through a fixed sequence of states, one step per clock pulse (deck 10 slide 2). **Asynchronous (ripple) counter:** only FF0 receives the clock; every other flip-flop is clocked by an output of the one before, so they do not change at the same instant (deck 10 slide 3).
:::

[[fig:u3c_ripple2_waves|What this graph plots: time across; rows CLK, Q0, Q1 (high = 1). The number above each clock ↓ is the count Q1 Q0 just after it. Q1 changes only where Q0 falls.|w=72]]

Work edge by edge. FF0 toggles at every ↓ of CLK. FF1 toggles only when Q0 goes 1 → 0.

| CLK ↓ | Q0 | Did Q0 fall? | Q1 | Q1 Q0 (count) |
|---|---|---|---|---|
| start | 0 | — | 0 | 00 (0) |
| 1 | 0 → 1 | no | 0 | 01 (1) |
| 2 | 1 → 0 | yes → FF1 toggles | 1 | 10 (2) |
| 3 | 0 → 1 | no | 1 | 11 (3) |
| 4 | 1 → 0 | yes → FF1 toggles | 0 | 00 (0) |

Q0 falls exactly when the count passes from an odd number to the next even one, which is when the twos bit must change. That is why "clock the next bit from the falling Q" counts up.

**Answer.** 01, 10, 11, 00: the chain counts **0, 1, 2, 3, 0**: a 2-bit binary up counter, 4 states (MOD-4).

:::check Check 2
(a) The same counter starts at 00. What does it show after 6 clock pulses? (b) FF1 is clocked by Q0' instead of Q0 (still negative-edge). Starting at 00, write the next four states.
:::

### 3 · The 3-bit up counter

Step 2's rule extends to any length: each flip-flop is clocked by the Q of the one before.

:::q <span class="tag">Deck 10 slide 14 · Q1</span>
Design 3-bit asynchronous up counter.
:::

:::guess Guess first
How many states does a 3-flip-flop chain step through, and which flip-flop changes least often?
:::

:::note Terms
**MOD-N:** a counter that steps through N different states and then repeats (deck 10 slide 3: "# of states = # of MOD"). **n flip-flops → MOD-2^{n}:** n bits can hold 2^{n} different numbers, and the chain visits every one.
:::

[[fig:u3c_ripple3|The running example: 3-bit ripple up counter (deck 10 slides 5, 15). Every T is tied to 1; CLK drives FF0 only; FF1's clock is Q0, FF2's clock is Q1. The bubble on each clock pin marks negative-edge triggering.|w=82]]

[[fig:u3c_ripple3_waves|What this graph plots: time across; rows CLK, Q0, Q1, Q2 (high = 1). The number above each clock ↓ is the count Q2 Q1 Q0 after it. Each row toggles where the row above it falls.|w=82]]

1. FF0 toggles at every clock ↓: Q0 = 0, 1, 0, 1, …
2. FF1 toggles at every ↓ of Q0, i.e. every 2nd clock: Q1 = 0, 0, 1, 1, 0, 0, …
3. FF2 toggles at every ↓ of Q1, i.e. every 4th clock: Q2 = 0, 0, 0, 0, 1, 1, 1, 1, …
4. Read Q2 Q1 Q0 down the columns: 000, 001, 010, … 111, then 000.

The design is fixed by two choices only: how many flip-flops (n = 3 for 8 states), and which output clocks the next stage (Q, for negative-edge flip-flops counting up).

**Answer.** Three negative-edge T flip-flops (or JK with J = K = 1), T = 1, CLK → FF0, Q0 → FF1's clock, Q1 → FF2's clock. It counts **0, 1, 2, 3, 4, 5, 6, 7, 0**: MOD-8. Q2 changes least often: once per 4 clock pulses, so it runs at f_{CLK}/8.

:::check Check 3
A 4-bit ripple up counter starts at 0000. (a) Its MOD number and its highest count? (b) The count after 21 clock pulses, in binary? (c) With a 16 kHz clock, the frequency at Q3?
:::

### 4 · Counting down

An up counter clocks each stage when the previous Q **falls**. A down counter needs the opposite moment.

:::q <span class="tag">Deck 10 slide 14 · Q2</span>
Design 3-bit asynchronous down counter negative edge triggering.
:::

:::guess Guess first
Counting down from 000 the next state is 111: every bit changes. In 000 → 111, does Q0 rise or fall? So when must FF1 toggle?
:::

:::note Terms
**Down counter:** steps through its states from the maximum to 0 and repeats (deck 10 slide 15). **Borrow:** in subtraction, a bit must change when the bit below it goes 0 → 1, i.e. when Q rises, which is when Q' falls.
:::

[[fig:u3c_ripple3_down|3-bit ripple down counter (deck 10 slide 15, lower circuit): the only change from step 3 is that each clock comes from the previous Q' instead of Q.|w=82]]

[[fig:u3c_ripple3_down_waves|What this graph plots: time across; rows CLK, Q0, Q1, Q2 (high = 1). The number above each clock ↓ is the count after it. Each row toggles where the row above it rises.|w=82]]

A negative-edge flip-flop acts when its clock input falls. Q' falls exactly when Q rises, so clocking from Q' makes each stage toggle when the stage before goes 0 → 1: the borrow moment.

| Flip-flops | Clock the next stage from | Counts |
|---|---|---|
| negative-edge (bubble) | Q | up |
| negative-edge (bubble) | Q' | down |
| positive-edge | Q' | up (deck 10 slides 4–5) |
| positive-edge | Q | down |

The last two rows follow from the first two: a positive-edge flip-flop acts at ↑ of its clock input, and ↑ of Q' is ↓ of Q.

:::note Slip in deck 10 slide 6
Slide 6 is titled "3-bit binary (MOD-8) down counter" and its state diagram and waveforms count down, but its circuit clocks the negative-edge flip-flops from Q0 and Q1 (not Q0', Q1'). That circuit counts **up**. Slide 15's lower circuit (clocks from Q') is the correct down counter; the pack uses it.
:::

**Answer.** Three negative-edge T flip-flops, T = 1, CLK → FF0, **Q0' → FF1's clock, Q1' → FF2's clock**. From 000 it counts **0, 7, 6, 5, 4, 3, 2, 1, 0**.

:::check Check 4
(a) A 3-bit counter uses positive-edge flip-flops and clocks each stage from the previous Q. Up or down? (b) Deck 10 slide 4's 2-bit counter uses positive-edge JK flip-flops clocked from Q0'. Up or down?
:::

### 5 · Ripple delay: the flaw

Steps 2–4 drew every output changing exactly on its edge. A real flip-flop needs time to respond, and in a ripple chain those times add.

:::q <span class="tag">Deck 10 slide 7</span>
Propagation delays in an asynchronous (ripple-clocked) binary counter: if the accumulated delay is greater than the clock pulse, some counter states may be misrepresented.
:::

:::guess Guess first
The running example sits at 011, each flip-flop has t_{pd} = 10 ns, and a clock ↓ arrives. Which values do the outputs show, and when, before they settle at 100?
:::

:::note Terms
**t_{pd} (propagation delay):** the time from an edge at a flip-flop's clock pin to its Q changing; set by the chip's transistors, 10–25 ns for common TTL/CMOS parts. **Settling time:** time from the clock edge until the last output has changed. **Transient (false) state:** a value the outputs show for a few nanoseconds that is not a real count.
:::

[[fig:u3c_delay|What this graph plots: time across in ns (the clock ↓ at 0); rows CLK, Q0, Q1, Q2 (high = 1). Each output changes 10 ns after the one before it; the shaded stretches are the false states 010 and 000.|w=82]]

Each stage can start only after the stage before it has changed, because that change **is** its clock:

| Time after CLK ↓ | What happens | Q2 Q1 Q0 |
|---|---|---|
| 0 ns | CLK falls | 011 (3) |
| 10 ns | FF0 toggles: Q0 1 → 0, a ↓ for FF1 | 010 (2) false |
| 20 ns | FF1 toggles: Q1 1 → 0, a ↓ for FF2 | 000 (0) false |
| 30 ns | FF2 toggles: Q2 0 → 1 | 100 (4) settled |

The worst case is the edge where every stage must change in turn (011 → 100 here, 111 → 000 too). Then:

$$t_{settle} = n · t_{pd}$$

*n stages, each waiting one t_{pd} for the one before.* The count must settle before the next edge arrives, so the clock period must be at least n · t_{pd}, which sets the highest clock frequency f_{max} = 1 / (n · t_{pd}). For the running example: 3 × 10 = 30 ns, f_{max} = 1 / 30 ns = 33.3 MHz. Every stage added lowers f_{max}.

**Answer to the Predict.** **010 at 10 ns, 000 at 20 ns, 100 at 30 ns.** A decoder watching for "count = 2" or "count = 0" would fire for 10 ns at a count that never happened: a **decoding glitch**.

:::check Check 5
A 4-bit ripple counter uses flip-flops with t_{pd} = 25 ns. (a) Its worst settling time and f_{max}? (b) Name the two clock edges (present → next count) on which all four stages change.
:::

### 6 · MOD-6 by reset

A chain of n flip-flops always gives MOD-2^{n}. A count of 6 (or 10, or 12) needs the chain to restart early.

:::q <span class="tag">Deck 10 slides 9–11 (EX 10.10–10.11)</span>
Given the following circuit, determine the counting sequence (and hence the modulus no.): a 3-bit negative-edge ripple counter with a 2-input NAND on B and C (Q1 and Q2) driving the CLR inputs of all three flip-flops.
:::

:::guess Guess first
The NAND's output goes to 0 only when Q2 = Q1 = 1. Which count is the first one with both 1? What happens the instant it appears?
:::

:::note Terms
**Truncated sequence:** a count that skips the states above some value by forcing the counter to recycle early (deck 10 slide 10). **Momentary (temporary) state:** the state that appears for a few nanoseconds and fires the reset before anyone could read it (deck 10 slide 9).
:::

[[fig:u3c_mod6|The circuit of deck 10 slide 10 in the pack's naming (A = Q0, B = Q1, C = Q2): the running example plus one NAND on Q2, Q1 driving every CLR'.|w=82]]

[[fig:u3c_mod6_waves|What this graph plots: time across; rows CLK, Q0, Q1, Q2 and the NAND output (high = 1). The number above each clock ↓ is the settled count after it. In the shaded slivers the counter shows 110 for a few ns, the NAND drops to 0, and CLR' forces 000.|w=86]]

1. From 000 the chain counts normally: 001, 010, 011, 100, 101. In none of these are Q2 and Q1 both 1, so the NAND output stays 1 and CLR' is idle.
2. The 6th clock ↓ moves 101 → 110. Now Q2 = Q1 = 1, the NAND output falls to 0.
3. CLR' = 0 forces every Q to 0 at once, without waiting for a clock (10 step 7). The outputs become 000, the NAND output returns to 1.
4. 110 lasted only a NAND delay plus a clear delay (a few ns): it is a momentary state, not a count.

The general rule (deck 10 slide 11): **to build MOD-N, clear when the count reaches N**, and feed the NAND only the outputs that are 1 in N's binary code. Every smaller count has at least one of those bits at 0, so the NAND cannot fire early.

**Answer.** The settled sequence is **000, 001, 010, 011, 100, 101, 000, …**: six states, **MOD-6**. 110 appears for an instant at every 6th pulse and fires the clear; 111 is never reached.

:::check Check 6
Which outputs feed the NAND for (a) <span class="tag">Deck 10 slide 14 · Q3</span> a MOD-7 ripple up counter? (b) a MOD-5 ripple up counter? How many flip-flops does each need?
:::

### 7 · The decade counter

Step 6's rule, applied to the count everyone uses: ten.

:::q <span class="tag">Deck 10 slides 12–13 (EX 10.12–10.13)</span>
Design an asynchronous decade counter.
:::

:::guess Guess first
A decade counter has 10 states. How many flip-flops does it need, and which outputs go to the NAND?
:::

:::note Terms
**Decade (BCD) counter:** a MOD-10 counter, counting 0000 … 1001 (0–9) and recycling; used in meters and clocks where each digit counts 0–9 (deck 10 slide 12). **Smallest n with 2^{n} ≥ N:** the number of flip-flops a MOD-N counter needs.
:::

[[fig:u3c_decade|Asynchronous decade counter (deck 10 slides 12–13, flip-flops renamed Q0–Q3 with Q0 = LSB): four toggling stages and a NAND on Q3, Q1 driving every CLR'.|w=88]]

1. Flip-flops: 2^{3} = 8 is too few for 10 states, 2^{4} = 16 is enough, so **n = 4**.
2. Clear at N = 10 = **1010**: Q3 = 1 and Q1 = 1. NAND inputs: **Q3, Q1** only.
3. Check nothing fires early: below 10, Q3 = 1 only in 1000 (8) and 1001 (9), and both have Q1 = 0. So the NAND first sees Q3 = Q1 = 1 at 1010.
4. Sequence: 0000 … 1001, then 1010 for an instant, cleared to 0000.

A useful by-product: Q3 is high only for counts 8 and 9, so it is high for 2 of every 10 clock periods and completes one cycle per 10 clocks. With a 10 kHz clock, Q3 is a **1 kHz** signal that is high **20 %** of the time.

:::note Slip in deck 10 slides 12–13
The slides name the flip-flops D, C, B, A from left to right with the clock entering D, so D is the least significant bit and A the most, the reverse of the usual order; the NAND is fed by A and C (the MSB and the 2s bit), which is the same circuit as the pack's NAND on Q3, Q1. On slide 12 the NAND's top input wire is also drawn running over stage D; slide 13 draws it correctly from C.
:::

**Answer.** **4 flip-flops**, all toggling, each clocked by the previous Q; a **2-input NAND on Q3 and Q1** drives every CLR'. It counts 0000 → 1001 and recycles to 0000 (1010 appears for a few ns).

:::check Check 7
(a) A MOD-12 ripple counter: flip-flops and NAND inputs? (b) How many flip-flops for MOD-60? For MOD-100?
:::

### 8 · Cascading counters

Steps 6–7 build any MOD-N from one chain. Large moduli are easier from two smaller counters in a row.

:::q <span class="tag">Deck 10 slides 16–17 (EX 10.16–10.17)</span>
A modulus-32 ripple counter constructed from a modulus-4 counter and a modulus-8 counter.
:::

:::guess Guess first
The MOD-4 counter's last output completes one cycle per 4 input pulses, and it clocks the MOD-8 counter. How many input pulses for one cycle of the MOD-8 counter's last output?
:::

:::note Terms
**Cascading:** connecting the last-stage output of one counter to the clock input of the next (deck 10 slide 16). **Overall modulus:** the number of input pulses before both counters are back to 0 together.
:::

[[fig:u3c_cascade|Cascading (deck 10 slide 16): the MOD-4 counter's last output is the MOD-8 counter's clock.|w=80]]

The second counter advances once per full cycle of the first, so the moduli multiply:

$$MOD_{total} = M × N$$

*M pulses move the second counter one step; it needs N steps to recycle.* With a 32 kHz input: the MOD-4 counter's last output runs at 32 / 4 = 8 kHz, and the MOD-8 counter's last output at 8 / 8 = **1 kHz**: one cycle per 32 input pulses. Deck 10 slide 17 does the same with two 3-bit counters: 2^{3} × 2^{3} = 64 states, a 6-bit counter that counts 0 to 63.

**Answer.** **4 × 8 = 32 pulses**: the cascade is a MOD-32 counter.

:::check Check 8
(a) A 1 MHz clock drives a MOD-4 counter cascaded into a MOD-8 counter. Frequency at the MOD-4 counter's last output, and at the MOD-8 counter's last output? (b) Build a MOD-24 and a MOD-60 counter from two smaller counters (give the two moduli).
:::

---

## Exam form

**Ripple up counter (n bits).**
1. n flip-flops, each toggling (T = 1, or J = K = 1).
2. CLK → FF0. Each next stage clocked from: negative-edge flip-flops → Q (up) or Q' (down); positive-edge → Q' (up) or Q (down).
3. Draw the waveforms: each row toggles where the row above falls (up, negative-edge); read Q_{n−1} … Q0 as the count.
4. MOD-2^{n}; stage k runs at f_{CLK} / 2^{k+1}.

**MOD-N by reset.**
1. Flip-flops: smallest n with 2^{n} ≥ N.
2. Write N in binary. NAND inputs = the outputs that are 1 in N.
3. NAND output → CLR' of every flip-flop (for a down counter, decode the state after 0 and preset/clear back to N − 1).
4. State that N appears momentarily (a glitch) and the counter shows 0 … N − 1.

**Formulas.** f_{Q} = f_{CLK}/2 per stage · t_{settle} = n · t_{pd}, f_{max} = 1/(n · t_{pd}) · cascaded MOD = M × N.

## Traps

- Clearing at N − 1 instead of N: the counter then never shows N − 1.
- Putting outputs that are 0 in N into the NAND: it then never fires.
- Clocking from Q with negative-edge flip-flops and calling it a down counter (deck 10 slide 6's slip).
- Forgetting the momentary state N, and the false states during ripple, when asked about glitches.
- Using t_{pd} instead of n · t_{pd} for a ripple counter's f_{max}.
- Reading the count with Q0 as the most significant bit.

## Self-test

1. <span class="tag">Deck 10 slide 14 · Q3</span> Design a MOD-7 ripple up counter: flip-flops, clock connections, NAND inputs.
2. A 1 MHz clock drives a 4-bit ripple counter. Frequency at Q0? At Q3?
3. A 3-bit ripple counter uses flip-flops with t_{pd} = 20 ns. Settling time and f_{max}?
4. <span class="tag">Deck 10 slide 14 · Q4</span> Design a MOD-5 ripple down counter with positive-edge flip-flops (count 4, 3, 2, 1, 0, 4, …).
5. A MOD-6 ripple counter: which state appears momentarily, and which state is never reached?
6. How many flip-flops for MOD-5, MOD-10, MOD-12, MOD-100?
7. A decade counter's Q3 drives a second decade counter. Overall modulus, and the output frequency with a 1 MHz clock?

<!--ANSWERS-->

## Answers

**Check 1.** Q0: 1 MHz / 2 = **500 kHz**. Q1: 500 / 2 = **250 kHz**.

**Check 2.** (a) 6 pulses = one full cycle (4) + 2: **10**. (b) FF1 now toggles when Q0 rises: **11, 10, 01, 00**: it counts down.

**Check 3.** (a) **MOD-16**, highest count **15** (1111). (b) 21 = 16 + 5, so one full cycle and 5 more: **0101**. (c) 16 kHz / 2^{4} = **1 kHz**.

**Check 4.** (a) **Down**: a positive-edge stage clocked from Q toggles when the previous Q rises. (b) **Up**: it toggles when Q0' rises, i.e. when Q0 falls (00, 01, 10, 11).

**Check 5.** (a) 4 × 25 = **100 ns**; f_{max} = 1 / 100 ns = **10 MHz**. (b) **0111 → 1000** and **1111 → 0000**.

**Check 6.** (a) MOD-7: clear at 7 = 111: **Q2, Q1, Q0**; 3 flip-flops. (b) MOD-5: clear at 5 = 101: **Q2, Q0**; 3 flip-flops.

**Check 7.** (a) 12 = 1100: **4 flip-flops**, NAND on **Q3, Q2**. (b) MOD-60: 2^{6} = 64 ≥ 60, **6**; MOD-100: 2^{7} = 128 ≥ 100, **7**.

**Check 8.** (a) 1 MHz / 4 = **250 kHz**; 250 kHz / 8 = **31.25 kHz**. (b) MOD-24 = **3 × 8** (or 4 × 6, 2 × 12); MOD-60 = **6 × 10** (or 4 × 15, 5 × 12).

**Self-test.**

1. 3 flip-flops (2^{3} = 8 ≥ 7), negative-edge, T = 1, CLK → FF0, Q0 → FF1, Q1 → FF2; clear at 7 = 111: NAND on **Q2, Q1, Q0** → all CLR'. Counts 0 … 6.
2. Q0: **500 kHz**; Q3: 1 MHz / 16 = **62.5 kHz**.
3. 3 × 20 = **60 ns**; f_{max} = 1 / 60 ns = **16.7 MHz**.
4. 3 flip-flops, positive-edge, T = 1, each clocked from the previous **Q** (down). From 000 the next state would be 111 (7); decode it with a NAND on **Q2, Q1, Q0** and drive the **CLR' of FF1 and FF0** only, so 111 is forced to 100 (4) at once. Sequence **4, 3, 2, 1, 0, 4, …**; 111 appears momentarily.
5. **110** appears momentarily; **111** is never reached.
6. MOD-5: **3**; MOD-10: **4**; MOD-12: **4**; MOD-100: **7**.
7. 10 × 10 = **MOD-100**; the second counter's Q3 runs at 1 MHz / 100 = **10 kHz**.

<!--/ANSWERS-->
