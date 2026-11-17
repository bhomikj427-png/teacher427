# 09 — Latches and flip-flops

<div class="sub">Deck 08 (slides 1–58) · syllabus Unit 3 (latch; S-R, D, JK, T, master–slave JK, edge-triggered flip-flops) · 2 real questions: MTE 2025 Q3 (2 marks), practice set 2 Q1 · needs 01 step 3 (NOT, NAND, NOR gates), 01 step 8 (XOR), 02 steps 1–5 (2- and 3-variable K-maps, don't-cares from 02 step 7)</div>

## Map

[[map:1 Memory needs feedback > 2 NOR SR latch > 3 NAND latch > 4 Gated SR latch > 5 D latch > 6 The clock > 7 Latch vs flip-flop > 8 D and SR flip-flops > 9 JK flip-flop > 10 T flip-flop > 11 Race-around, master–slave > 12 Excitation tables > 13 Conversion|here=1]]

Files 01–08 built **combinational** circuits: the output is fixed by the inputs present now, and the circuit forgets an input the moment it changes. This file builds the one-bit memory. It starts from two gates that feed each other (the latch), adds a control input that says when the latch may listen, and then a clock edge that says the exact instant (the flip-flop). It ends with the two tables every later design uses: the characteristic table (inputs → next state) and the excitation table (wanted change → inputs). File 10 draws flip-flop waveforms; files 12–13 chain flip-flops into counters.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| Q | the stored bit: the output of the latch or flip-flop now | 0 or 1 |
| Q' | the second output; the complement of Q in every allowed state | 1 − Q |
| Q⁺ (also Q(t+1)) | the value Q takes after the next clock edge (or, for a latch, after the inputs act) | 0 or 1 |
| Q₀ (also Q(t)) | the value Q had before the inputs acted ("present state") | 0 or 1 |
| S, R | Set and Reset inputs: S = 1 asks for Q = 1, R = 1 asks for Q = 0 | 0 or 1 |
| S', R' | active-low Set and Reset of the NAND latch: a **0** makes them act | 0 or 1 |
| EN (also C, E) | enable: while it is 1 the latch listens to its inputs; while 0 it holds | 0 or 1 |
| CLK | clock: a square wave that tells every flip-flop when to update | 1 kHz – 100 MHz |
| D, J, K, T | the data inputs of the D, JK and T flip-flops | 0 or 1 |
| X | don't-care: either value gives the required result | — |
| T (time) | clock period: time from one rising edge to the next | 10 ns – 1 ms |

## Running example

**One positive-edge JK flip-flop, Q = 0 at the start, with J K just before five clock edges = 10, 00, 01, 11, 11.** Step 9 finds Q after each edge (1, 1, 0, 1, 0); step 11 asks what goes wrong if the same JK is level-triggered; step 12 reads its excitation; step 13 turns a JK into a D flip-flop.

## The questions this file answers

- <span class="tag">Deck 08 slides 6–17</span> Draw an SR latch with NOR gates (and with NAND gates), give its table for every input, and say why one input pair is not allowed.
- <span class="tag">MTE 2025 Q3 · 2 marks</span> What excitation input should be applied to a T- FF to make output toggle?
- <span class="tag">Practice set 2 Q1</span> Design a D flip-flop, using SR, JK & T flip-flop and suitable logic gates.
- <span class="tag">Deck 08 slides 53–58 (EX 8.53–8.58)</span> Convert JK → D, SR → JK, D → SR, D → T, D → JK.

---

## Build

### 1 · Memory needs feedback

Every gate in 01–08 has an output fixed by its inputs now. To remember, a circuit must see its own past: its output has to come back to its input.

**Anchor.** A lift call button: press it once and let go, and the lamp stays lit until the lift arrives. The lamp remembers a press that is no longer happening. Nothing in an AND–OR circuit can do that.

:::guess Predict
Two inverters are joined in a ring: A's output drives B, B's output drives A. Suppose A's output is 1. What is B's output, and can the ring ever change on its own?
:::

:::note Terms
**Sequential circuit:** combinational logic plus memory elements, where the outputs depend on the present inputs **and** on the stored state (deck 08 slide 1). **Feedback:** a wire that carries an output back to an input of the same circuit. **Bistable:** has exactly two states it can rest in forever (deck 08 slide 3).
:::

[[fig:u3_seq_block|A sequential circuit (deck 08 slide 1). The memory holds the present state; the combinational logic computes the outputs and the next state from the inputs and the present state, and the next state is written back into memory.|w=70]]

[[fig:u3_two_inv|The simplest memory (deck 08 slide 4): two inverters in a ring. Q = 1 makes Q' = 0, and Q' = 0 makes Q = 1 again, so the ring holds 1; the same argument holds for Q = 0.|w=48]]

| Q (output of A) | B outputs | A then outputs | Settled? |
|---|---|---|---|
| 1 | Q' = 0 | 1 | yes: holds 1 |
| 0 | Q' = 1 | 0 | yes: holds 0 |

The ring has two resting states and no input, so it stores one bit but cannot be told to change. The latch in step 2 replaces each inverter with a NOR gate, whose second input is the "change" handle.

**Answer to the Predict.** B outputs **0**, and that 0 drives A back to 1: the ring **holds 1 for ever** and cannot change on its own. It is bistable, which is exactly a 1-bit memory with no way to write it.

:::check Check 1
(a) The ring has Q = 0. What is Q', and what is Q a minute later? (b) Can a 2-input AND gate with no feedback store a bit? One line why.
:::

### 2 · The NOR SR latch

Step 1's ring cannot be written. Swap each inverter for a NOR gate: a NOR with its other input at 0 is an inverter (file 03 step 2), so the ring still holds; a 1 on the other input forces that gate's output to 0, which writes the bit.

:::q <span class="tag">Deck 08 slides 6–15</span>
Draw an SR latch using NOR gates and give its output for every input combination. Why is S = R = 1 not allowed?
:::

:::guess Guess first
With S = R = 0 the latch can sit with Q = 0 or with Q = 1. What decides which one?
:::

:::note Terms
**Set:** make Q = 1. **Reset:** make Q = 0. **Hold (no change):** Q keeps its previous value Q₀.
:::

[[fig:sr_latch|NOR SR latch (deck 08 slide 6). R enters the gate that drives Q; S enters the gate that drives Q'. Each output is fed back to the other gate.|w=50]]

A NOR outputs 1 only when both its inputs are 0. Work each row from that one fact, starting from the input that is 1 (it forces its gate to 0):

| S | R | Q₀ | Q | Q' | Action |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | hold (Q = Q₀) |
| 0 | 0 | 1 | 1 | 0 | hold (Q = Q₀) |
| 0 | 1 | 0 | 0 | 1 | reset |
| 0 | 1 | 1 | 0 | 1 | reset |
| 1 | 0 | 0 | 1 | 0 | set |
| 1 | 0 | 1 | 1 | 0 | set |
| 1 | 1 | 0 | 0 | 0 | not allowed |
| 1 | 1 | 1 | 0 | 0 | not allowed |

1. S = 1 forces Q' = NOR(1, Q) = 0.
2. The Q gate then sees R = 0 and Q' = 0, so Q = NOR(0, 0) = 1: **set**.
3. S returns to 0: Q' = NOR(0, Q = 1) = 0 still, so Q stays 1: **the latch remembers**.

**Answer.** Circuit and table above (deck 08 slides 7–15 fill it row by row). With S = R = 0 the latch keeps whichever value it had: Q₀ decides. S = R = 1 is not allowed for two reasons: (1) it forces **Q = Q' = 0**, so the outputs are no longer complements; (2) if S and R then return to 0 together, both gates head for 1 at the same time and the state the latch settles in depends on which gate is faster: it cannot be predicted.

:::check Check 2
(a) Q = 0. S R = 10, then 00. Q after each? (b) S = R = 1: give Q and Q'. (c) From (b), S and R both drop to 0 at the same instant. What can you say about Q?
:::

### 3 · The NAND latch: active-low inputs

The same ring built from NAND gates is the latch inside most chips (and inside every flip-flop of steps 7–10). A NAND outputs 0 only when both inputs are 1, so its "forcing" input value is 0, not 1.

:::q <span class="tag">Deck 08 slides 15, 17</span>
Give the table of the active-LOW input S'-R' latch (NAND gate latch).
:::

:::guess Guess first
In the NOR latch, 1 on an input acts and 11 is forbidden. Which input value acts in the NAND latch, and which pair is forbidden?
:::

:::note Terms
**Active-low:** the input does its job when it is **0** and is idle at 1. The prime in S' and R' marks this.
:::

[[fig:u3_nand_latch|NAND latch (deck 08 slide 15). S' enters the gate that drives Q; R' enters the gate that drives Q'. Each output is fed back to the other gate.|w=50]]

| S' | R' | Q | Action |
|---|---|---|---|
| 1 | 1 | Q₀ | hold |
| 1 | 0 | 0 | reset |
| 0 | 1 | 1 | set |
| 0 | 0 | Q = Q' = 1 | not allowed |

1. S' = 0 forces Q = NAND(0, Q') = 1.
2. The other gate sees R' = 1 and Q = 1, so Q' = NAND(1, 1) = 0: set.
3. S' back to 1: Q = NAND(1, Q' = 0) = 1 still: hold.

**Answer.** **0 acts** (S' = 0 sets, R' = 0 resets), **11 holds**, and **00 is forbidden**: it forces Q = Q' = 1. The NOR latch's table read with every input inverted.

:::check Check 3
(a) S' = 1, R' = 0. Q? (b) Q = 1 and S'R' = 11. Q? (c) Which input pair is forbidden, and what are Q and Q' then?
:::

### 4 · The gated SR latch: an enable decides when to listen

A bare latch reacts the instant S or R changes. A circuit with many latches needs them to listen only at agreed times. One extra input does it.

:::q <span class="tag">Deck 08 slides 18–19</span>
NAND based SR latch with control input: give its function table.
:::

:::guess Guess first
Two NAND gates are put in front of the NAND latch, each also fed by EN. What does the latch see when EN = 0?
:::

:::note Terms
**Enable (EN):** a control input; EN = 1 lets S and R through to the latch, EN = 0 blocks them so the latch holds. **Gated (controlled) latch:** a latch with an enable.
:::

[[fig:u3_gated_sr|Gated SR latch from four NAND gates (deck 08 slide 18). The input NANDs turn S and R into the active-low S' and R' of step 3, but only while EN = 1.|w=80]]

| EN | S | R | Q | Action |
|---|---|---|---|---|
| 0 | X | X | Q₀ | hold |
| 1 | 0 | 0 | Q₀ | hold |
| 1 | 0 | 1 | 0 | reset |
| 1 | 1 | 0 | 1 | set |
| 1 | 1 | 1 | — | not allowed |

1. EN = 0: each input NAND has a 0 input, so it outputs 1 whatever S or R is. The latch sees S'R' = 11: hold (step 3).
2. EN = 1: the input NANDs output (S·1)' = S' and (R·1)' = R'. The latch sees the active-low versions, so S = 1 sets and R = 1 resets: the gated latch is **active-high**.

Deck 08 slide 19 builds the same table from two AND gates in front of a NOR latch.

**Answer.** With EN = 0 the latch sees **S'R' = 11** and holds; S and R can do anything. The forbidden case survives: EN = 1 with S = R = 1.

:::check Check 4
Q = 0. (a) EN = 0, S = 1, R = 0: Q? (b) EN rises to 1 with the same S, R: Q? (c) EN falls to 0, then S = 0, R = 1: Q?
:::

### 5 · The D latch: no forbidden input

Steps 2–4 all carry a forbidden pair. Deck 08 slide 20: make S and R come from one wire so they can never both be 1.

:::q <span class="tag">Deck 08 slides 20–21, 24</span>
Give the logic diagram, function table and characteristic equation of the gated D latch.
:::

:::guess Guess first
S = D and R = D'. While EN = 1, what does Q do when D changes?
:::

:::note Terms
**D (data):** the one data input. **Transparent:** while EN = 1, Q copies D, so a change on D appears at Q (after the gate delays) as if through a wire.
:::

[[fig:u3_gated_d|Gated D latch (deck 08 slide 20): step 4's circuit with S = D and R = D' made by one inverter.|w=80]]

| EN | D | Q⁺ | Action |
|---|---|---|---|
| 0 | X | Q₀ | hold |
| 1 | 0 | 0 | reset |
| 1 | 1 | 1 | set |

Characteristic equation (deck 08 slide 21): **when EN = 1, Q⁺ = D.** Read: "while enabled, the next Q is whatever D is." While EN = 0 the latch holds.

**Answer to the guess.** Q **follows D**: every change of D while EN = 1 reaches Q. The forbidden case is gone because S = D and R = D' are never both 1.

:::check Check 5
Q = 0. (a) EN = 1 while D goes 1 → 0 → 1. Q at each stage? (b) EN falls to 0, then D goes to 0. Q? (c) One line: why can a D latch never reach the forbidden state?
:::

### 6 · The clock

Step 5's latch listens whenever EN = 1. A system with hundreds of memory bits needs one shared signal that says when: the clock.

:::q <span class="tag">Deck 08 slide 25</span>
Define clock period, clock frequency and duty cycle.
:::

:::guess Guess first
A clock repeats every 8 µs and is high for 2 µs of each repeat. What fraction of the time is it high?
:::

:::note Terms
**Clock period T:** the time from one rising edge to the next; set by the oscillator that makes the clock. **Rising (positive) edge ↑:** the 0 → 1 transition; **falling (negative) edge ↓:** the 1 → 0 transition. **Duty cycle:** the fraction of each period the clock spends high.
:::

[[fig:u3_clock|What this graph plots: time across, the clock level up the page (high = 1, low = 0). Each ↑ line is a rising edge, each ↓ line a falling edge; one period runs from one ↑ to the next.|w=70]]

| Quantity | Formula | Read in words | Example (figure) |
|---|---|---|---|
| period | T | time for one full cycle | 2 units |
| frequency | f = 1/T | cycles per second | 1/2 per unit |
| duty cycle | t_H / T | high time ÷ period | 1/2 = 50 % |

A 1 kHz clock has T = 1/1000 s = 1 ms; at 50 % duty cycle it is high for 0.5 ms and low for 0.5 ms.

**Answer to the guess.** 2/8 = **25 %** (duty cycle); the frequency is 1/(8 µs) = 125 kHz.

:::check Check 6
(a) A clock runs at 50 MHz. Its period? (b) A clock has period 40 ns and is high for 30 ns. Frequency and duty cycle?
:::

### 7 · Latch vs flip-flop: level vs edge

A latch with its enable tied to the clock listens for the whole high half of each period. Deck 08 slide 27 says this makes latches unsuitable in synchronous circuits: a change on the input passes straight to the output while the clock is high.

:::q <span class="tag">Deck 08 slides 22, 26–29</span>
Distinguish a latch from a flip-flop.
:::

:::guess Predict
The same D and the same clock drive a D latch (EN = CLK) and a positive-edge D flip-flop. Which output changes more often?
:::

:::note Terms
**Level-triggered (level-sensitive):** acts during the whole time the control is at one level (a latch). **Edge-triggered:** samples its inputs only at the instant of one clock edge and ignores them the rest of the time (a flip-flop). **Synchronous:** all memory elements change at the same clock edge.
:::

[[fig:latch_vs_ff|What this graph plots: time across; rows CLK, D, the latch's Q, the flip-flop's Q (high = 1). Shaded = clock high (latch transparent); ↑ = the flip-flop's sampling instants.|w=78]]

| Reading the figure | D latch (EN = CLK) | Positive-edge D flip-flop |
|---|---|---|
| when it looks at D | the whole shaded time | only at each ↑ |
| number of times Q changes | 8 (the short pulse inside the 3rd high time appears) | 2 |
| D pulse that starts mid-way through a high time (1st, last) | appears at once | missed (D is 0 again by the next ↑) |

| | Latch | Flip-flop |
|---|---|---|
| triggered by | a level (EN = 1) | an edge (↑ or ↓) |
| inputs reach Q | at any time while enabled | only at the edge instant |
| use | simple storage | every synchronous circuit (registers, counters) |

[[fig:ff_symbols|Flip-flop symbols (deck 08 slide 32). The ▷ on the clock pin marks edge triggering; a bubble before ▷ means the falling edge.|w=78]]

**Answer to the Predict.** The **latch** (8 changes against 2): it passes every change of D during the high time, the flip-flop only the value at each ↑.

:::check Check 7
(a) Which one can change Q while CLK is held at 1: latch or flip-flop? (b) A positive-edge D flip-flop has D = 1 just before ↑; D drops to 0 halfway through the high time. Q just after ↑ and at the end of the high time? (c) What does a bubble in front of the ▷ mean?
:::

### 8 · The D and SR flip-flops

From here on every memory element is edge-triggered. Each type is defined by one table: what Q⁺ is for each input, at the active edge.

:::q <span class="tag">Deck 08 slides 30–31, 45–47</span>
Give the characteristic table and characteristic equation of the D flip-flop and of the SR flip-flop.
:::

:::guess Guess first
A D flip-flop: D = 1 at the edge. Does Q⁺ depend on the old Q?
:::

:::note Terms
**Characteristic table:** for each input combination at the active edge, the next state Q⁺ (in terms of Q). **Characteristic equation:** the same table as a Boolean expression for Q⁺, found with a K-map.
:::

| D | Q⁺ | | S | R | Q⁺ | Action |
|---|---|---|---|---|---|---|
| 0 | 0 | | 0 | 0 | Q | hold |
| 1 | 1 | | 0 | 1 | 0 | reset |
| | | | 1 | 0 | 1 | set |
| | | | 1 | 1 | ? | not allowed |

- **D:** Q⁺ = D. Read: "after the edge, Q is the D that was there at the edge." The D flip-flop is a one-clock delay.
- **SR:** Q⁺ = S + R'Q, valid only with **SR = 0** (S and R never both 1). Read: "Q is 1 next if set now, or if it was 1 and not reset."

:::note Slip in the slides
Deck 08 slides 30 and 31 are titled "D Flip-flop" and "SR Flip-flop" but draw the **gated latches** of steps 4–5 (level-triggered, no edge detector). The tables on those slides are correct for the latches; this pack draws the latch circuits in steps 4–5 and calls them latches.
:::

**Answer to the guess.** **No**: Q⁺ = D whatever Q was.

:::check Check 8
(a) Positive-edge SR flip-flop, Q = 1, S = 0 and R = 1 at the edge: Q⁺? (b) Put S = R = 0 into Q⁺ = S + R'Q and read the result. (c) D before four edges = 1, 1, 0, 1. Q after each?
:::

### 9 · The JK flip-flop: the SR with its forbidden row used

The SR flip-flop wastes its 11 input. The JK flip-flop gives that row a job: toggle.

:::q <span class="tag">Deck 08 slides 33–37</span>
Derive the characteristic equation of the JK flip-flop from its table.
:::

:::guess Guess first
J = K = 1 at an edge: Q⁺ must be different from Q. Which single expression of Q is that?
:::

:::note Terms
**J, K:** J plays S (set), K plays R (reset). **Toggle (complement):** Q⁺ = Q'; the output flips.
:::

| J | K | Q | Q⁺ | Action |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | hold |
| 0 | 0 | 1 | 1 | hold |
| 0 | 1 | 0 | 0 | reset |
| 0 | 1 | 1 | 0 | reset |
| 1 | 0 | 0 | 1 | set |
| 1 | 0 | 1 | 1 | set |
| 1 | 1 | 0 | 1 | toggle |
| 1 | 1 | 1 | 0 | toggle |

[[fig:u3_jk_kmap|Q⁺ of the JK flip-flop on a 3-variable K-map (file 02 step 4): row J, columns K Q in Gray order; a 1 marks an input row where Q⁺ = 1. Two pairs cover the 1s.|w=50]]

1. Q⁺ = 1 on rows JKQ = 001, 100, 101, 110, i.e. Σm(1, 4, 5, 6).
2. Pair m4, m6 (J = 1, Q = 0; the wrap-around pair of the J = 1 row): **JQ'**.
3. Pair m1, m5 (K = 0, Q = 1, both rows): **K'Q**.
4. **Q⁺ = JQ' + K'Q.** Read: "Q becomes 1 if it is 0 and J says set, or if it is 1 and K does not say reset."

**Running example.** Q = 0; J K before five edges = 10, 00, 01, 11, 11:

| Edge | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| J K | 1 0 | 0 0 | 0 1 | 1 1 | 1 1 |
| action | set | hold | reset | toggle | toggle |
| Q after | 1 | 1 | 0 | 1 | 0 |

**Answer.** **Q⁺ = JQ' + K'Q**; at J = K = 1 it gives Q⁺ = Q' + 0 = **Q'**, the expression the guess asked for.

:::check Check 9
(a) Use Q⁺ = JQ' + K'Q on the row J = 1, K = 1, Q = 1. (b) Q = 1, J K before four edges = 01, 10, 11, 00. Q after each?
:::

### 10 · The T flip-flop: toggle on command

Tie J and K of step 9 together and only two rows remain: hold (00) and toggle (11). That is the T flip-flop, the building block of counters (files 12–13).

:::q <span class="tag">MTE 2025 Q3 · 2 marks</span>
What excitation input should be applied to a T- FF to make output toggle?
:::

:::guess Guess first
Write your one-word answer before reading on.
:::

:::note Terms
**T (toggle input):** T = 1 at an edge flips Q; T = 0 holds it. **Frequency divider:** a circuit whose output has a lower frequency than its clock.
:::

| T | Q⁺ | Action |
|---|---|---|
| 0 | Q | hold |
| 1 | Q' | toggle |

1. Q⁺ = T'Q + TQ' (hold when T = 0, complement when T = 1).
2. T'Q + TQ' is the XOR of T and Q (file 01 step 8): **Q⁺ = T ⊕ Q** (deck 08 slide 46).
3. From the JK: put J = K = T into JQ' + K'Q to get TQ' + T'Q, the same expression.

[[fig:u3_tdiv|Frequency division (deck 08 slide 41). What this graph plots: time across; rows CLK, Q_A (a T = 1 flip-flop clocked by CLK), Q_B (a T = 1 flip-flop clocked by Q_A's rising edges). Q_A changes at every ↑, so it has half the clock frequency; Q_B has a quarter.|w=78]]

| Signal | Edges that change it | Frequency (1 kHz clock) |
|---|---|---|
| CLK | — | 1 kHz |
| Q_A | every ↑ of CLK | 500 Hz |
| Q_B | every ↑ of Q_A | 250 Hz |

**Answer (MTE Q3).** **T = 1.** From Q⁺ = T ⊕ Q: with T = 1, Q⁺ = 1 ⊕ Q = Q', so the output toggles at every active clock edge (T = 0 gives Q⁺ = Q, no change).

:::check Check 10
(a) T = 1, clock 10 kHz: frequency at Q? (b) Three T = 1 flip-flops in a chain (each clocked by the one before), 16 kHz clock: frequency at the last Q? (c) Q = 0, T before four edges = 1, 0, 1, 1: Q after each?
:::

### 11 · Race-around and the master–slave JK

Step 9 assumed the JK acts at one instant. Build it as a **level-triggered** JK latch (deck 08 slide 33's NAND circuit with CLK as a plain enable) and the toggle row breaks.

:::guess Predict
A level-triggered JK latch has J = K = 1 and its clock stays high for 1 µs, while one trip round its gates takes 20 ns. How many times can Q toggle before the clock falls?
:::

:::note Terms
**Propagation delay:** the time a gate takes to respond to an input change (ns). **Race-around:** with J = K = 1 and the clock high for longer than the loop delay, the new Q reaches the inputs, toggles Q again, and repeats until the clock falls. **Master–slave:** two latches in series, enabled on opposite clock levels.
:::

[[fig:u3_race|What this graph plots: time across; rows CLK, J = K (held at 1), Q of a level-triggered JK. Shaded = clock high: Q keeps toggling, so its value when the clock falls depends on the exact delays.|w=72]]

Race-around needs two things at once: **J = K = 1**, and a clock-high time **longer than the delay** round the loop. Two cures (KB 03 §3):

1. **Master–slave JK** (below): the master listens while CLK = 1, the slave copies the master while CLK = 0. They are never open together, so a new Q never reaches the inputs that are being read. Q changes once per period, when CLK falls.
2. **Edge triggering:** the flip-flop reads its inputs only in a short window at the edge, far shorter than the loop delay.

[[fig:ms_jk|Master–slave JK. The master (JK latch) is enabled by CLK, the slave (SR latch) by CLK'; Q and Q' feed back to the master's input gates.|w=70]]

**Answer to the Predict.** Up to 1000/20 = **about 50 toggles**: the final Q is unpredictable. A master–slave or edge-triggered JK toggles **exactly once** per clock period.

:::check Check 11
(a) Which two conditions together cause race-around? (b) In a master–slave JK with CLK = 1, can Q change? When does it change? (c) Running example: the 4th and 5th edges have J = K = 1. What would a level-triggered JK latch give there instead of 1 and 0?
:::

### 12 · Excitation tables: from the change you want to the inputs you need

Counters and state machines (files 13, 15) start from the change they want (Q: 0 → 1, say) and must find the inputs that cause it. That is the characteristic table read backwards.

:::q <span class="tag">Deck 08 slides 47–52</span>
Give the excitation tables of the SR, JK, D and T flip-flops.
:::

:::guess Guess first
A JK must go from Q = 0 to Q⁺ = 1. Which J K pairs do it? (Look at step 9's table.)
:::

:::note Terms
**Excitation table:** for each transition Q → Q⁺, the flip-flop inputs that produce it (deck 08 slide 47: "the excitation or moves required to take the flip-flop from the present state to the next state"). **X** = either value works.
:::

| Q → Q⁺ | S R | J K | D | T |
|---|---|---|---|---|
| 0 → 0 | 0 X | 0 X | 0 | 0 |
| 0 → 1 | 1 0 | 1 X | 1 | 1 |
| 1 → 0 | 0 1 | X 1 | 0 | 1 |
| 1 → 1 | X 0 | X 0 | 1 | 0 |

How each entry is read off the characteristic table (JK, 0 → 1): rows with Q = 0 and Q⁺ = 1 are J K = 10 (set) and 11 (toggle). J must be 1; K can be either: **1 X**.

- **D column = Q⁺:** D is just the next state.
- **T column = Q ⊕ Q⁺:** T = 1 exactly when Q must change.
- **JK has an X in every row:** each transition is reached by two input pairs. More X's mean bigger K-map groups, so JK designs usually need the least logic.

**Answer to the guess.** **J K = 10 (set) or 11 (toggle)**, written 1 X.

**Running example.** Edge 3 takes Q from 1 to 0: the excitation table says J K = X 1, and the example's 01 fits (J = 0, K = 1).

:::check Check 12
(a) JK inputs for 1 → 1? (b) T input for 1 → 1? (c) SR inputs for 0 → 0, and why R is X there.
:::

### 13 · Converting one flip-flop into another

The excitation table turns any flip-flop into any other: the wanted type supplies Q⁺, the available type's excitation table supplies the inputs, and a K-map gives the logic.

:::q <span class="tag">Practice set 2 Q1</span>
Design a D flip-flop, using SR, JK & T flip-flop and suitable logic gates.
:::

:::guess Guess first
A T flip-flop must act as a D. When exactly must T be 1?
:::

:::note Terms
**Conversion table:** one row per (new input, Q): the Q⁺ the new type needs, then the old type's inputs that produce it (from step 12).
:::

**The procedure** (deck 08 slide 53, EX 8.53 JK → D):

1. List the new flip-flop's inputs and Q; write Q⁺ from the **new** type's characteristic table.
2. For each row, write the **old** type's inputs from its excitation table (Q → Q⁺).
3. K-map each old input against (new inputs, Q); the X's are don't-cares.
4. Draw the old flip-flop with that logic in front of its inputs.

| D | Q | Q⁺ | S R | J K | T |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 X | 0 X | 0 |
| 0 | 1 | 0 | 0 1 | X 1 | 1 |
| 1 | 0 | 1 | 1 0 | 1 X | 1 |
| 1 | 1 | 1 | X 0 | X 0 | 0 |

[[fig:u3_conv_jk_d|K-maps for JK → D (deck 08 slide 53): rows D, columns Q; a cell holds the J (left) or K (right) the row needs, X = don't-care. J = D and K = D'.|w=60]]

[[fig:u3_conv_t_d|K-map for T → D: T = 1 on rows (D, Q) = (0, 1) and (1, 0), a diagonal with no pair: T = D'Q + DQ' = D ⊕ Q.|w=32]]

**Answer (practice set 2 Q1).**

| Have | Logic in front | Circuit |
|---|---|---|
| SR | **S = D, R = D'** (S map: 1 at D = 1, Q = 0, X at D = 1, Q = 1; R the mirror) | D to S, D through a NOT to R |
| JK | **J = D, K = D'** | D to J, D through a NOT to K |
| T | **T = D ⊕ Q** | one XOR fed by D and the flip-flop's own Q |

The other conversions on deck 08 (each checked row by row in the pack's verify script):

| Have → want | Logic | Slide |
|---|---|---|
| SR → JK | S = JQ', R = KQ | 54–55 |
| D → SR | D = S + R'Q | 56 |
| D → T | D = T ⊕ Q | 57 |
| D → JK | D = JQ' + K'Q | 58 |
| JK → T | J = K = T | 39 |

**Running example.** A JK made into a D (J = D, K = D') loads D at every edge: D = 1 gives J K = 10 (set), D = 0 gives 01 (reset); the hold and toggle rows are never used.

:::check Check 13
(a) Convert JK → T with the conversion-table method. (b) Check SR → JK on the row J = K = 1, Q = 1: what S, R does the logic give, and is Q⁺ correct? (c) Convert T → JK.
:::

---

## Exam form

**SR latch (NOR).** (1) Draw two cross-coupled NOR gates, R into the Q gate, S into the Q' gate. (2) Table: 00 hold, 01 reset, 10 set, 11 not allowed (Q = Q' = 0). (3) Why 11 is not allowed: outputs not complementary; releasing both together gives an unpredictable state.

**NAND latch.** Inputs active-low: 11 hold, 10 reset, 01 set, 00 not allowed (Q = Q' = 1).

**Gated / D latch.** EN = 0 holds; EN = 1 passes S, R (or D). D latch: S = D, R = D', Q⁺ = D while EN = 1 (transparent).

**Clock.** f = 1/T; duty cycle = t_H / T.

**Latch vs flip-flop.** Level-triggered (acts during EN = 1) vs edge-triggered (acts at ↑ or ↓ only).

**Characteristic equations.** D: Q⁺ = D · SR: Q⁺ = S + R'Q, SR = 0 · JK: Q⁺ = JQ' + K'Q · T: Q⁺ = T ⊕ Q. JK derivation: table → K-map Σm(1, 4, 5, 6) → JQ' + K'Q.

**Race-around.** Level-triggered JK, J = K = 1, clock high longer than the loop delay → Q toggles repeatedly. Cures: master–slave (master on CLK = 1, slave on CLK = 0) or edge triggering.

**Excitation table.** The four-row table of step 12 (memorise the JK and T columns).

**Conversion.** (1) New type's characteristic table → Q⁺. (2) Old type's excitation per row. (3) K-map each old input. (4) Draw. Results: D from SR: S = D, R = D'; from JK: J = D, K = D'; from T: T = D ⊕ Q.

## Traps

- NAND latch inputs are active-low: 00 is the forbidden pair, not 11.
- Calling a gated latch a flip-flop (deck 08 slides 30–31 do): a flip-flop has an edge-triggered clock (▷).
- Using the characteristic table where the excitation table is needed (design starts from Q → Q⁺).
- Writing T = D for T → D: T must be 1 only when Q has to change, T = D ⊕ Q.
- Forgetting SR = 0 when quoting Q⁺ = S + R'Q.
- Saying the latch "samples at the clock": it passes every input change during the enable level.

## Self-test

1. NOR SR latch, Q = 0. S R = 10, 00, 01, 00. Q after each?
2. A clock has period 40 ns and high time 10 ns. Frequency and duty cycle?
3. JK flip-flop, Q = 1. J K before four edges = 11, 00, 10, 01. Q after each?
4. Derive Q⁺ of the T flip-flop from its characteristic table.
5. Why does a master–slave JK not race around?
6. Convert a T flip-flop into a D flip-flop, and say what the gate is fed with.
7. In one line each: what makes a D latch different from a positive-edge D flip-flop, and which one has a forbidden input?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **Q' = 1; Q is still 0** a minute later (the ring holds). (b) **No**: its output is fixed by its present inputs; nothing carries the past back in.

**Check 2.** (a) **1, then 1** (set, then hold). (b) **Q = 0, Q' = 0.** (c) **Unpredictable**: both gates head for 1 at once and the faster one wins.

**Check 3.** (a) **Q = 0** (R' = 0 resets). (b) **Q = 1** (hold). (c) **S'R' = 00**, giving **Q = Q' = 1**.

**Check 4.** (a) **Q = 0** (EN = 0 holds). (b) **Q = 1** (set). (c) **Q = 1** (EN = 0 holds; the new R is ignored).

**Check 5.** (a) **1, 0, 1** (Q follows D). (b) **Q = 1** (EN = 0 holds the last value). (c) S = D and R = D' are **never both 1**.

**Check 6.** (a) T = 1/(50 × 10⁶) s = **20 ns**. (b) f = 1/(40 ns) = **25 MHz**; duty cycle = 30/40 = **75 %**.

**Check 7.** (a) **The latch.** (b) **1 and 1**: the flip-flop took D = 1 at ↑ and ignores the later change. (c) **Negative (falling) edge** triggering.

**Check 8.** (a) **Q⁺ = 0** (reset). (b) Q⁺ = 0 + 1·Q = **Q** (hold). (c) **1, 1, 0, 1** (Q⁺ = D).

**Check 9.** (a) 1·0 + 0·1 = **0** (toggle from 1). (b) 01 → **0**; 10 → **1**; 11 → **0**; 00 → **0**.

**Check 10.** (a) **5 kHz.** (b) 16 → 8 → 4 → **2 kHz.** (c) **1, 1, 0, 1.**

**Check 11.** (a) **J = K = 1** and the **clock high for longer than the loop delay**. (b) **No**: the slave is closed while CLK = 1. Q changes **when CLK falls** (the slave opens and copies the master). (c) An **unpredictable** value at each of those edges (Q toggles many times while the clock is high).

**Check 12.** (a) **X 0** (hold 00 or set 10). (b) **T = 0.** (c) **S R = 0 X**: S must not set; R = 0 (hold) and R = 1 (reset) both leave Q at 0.

**Check 13.** (a) Rows (T, Q) → Q⁺: 00 → 0: J K = 0 X; 01 → 1: X 0; 10 → 1: 1 X; 11 → 0: X 1. Maps: **J = T, K = T** (J = K = T). (b) S = JQ' = 1·0 = **0**, R = KQ = 1·1 = **1**: reset, **Q⁺ = 0 = Q'**, the toggle is correct. (c) T must be 1 when Q changes: Q = 0 and J = 1, or Q = 1 and K = 1: **T = JQ' + KQ**.

**Self-test.**

1. **1, 1, 0, 0.**
2. f = 1/(40 ns) = **25 MHz**; duty cycle = 10/40 = **25 %**.
3. 11 → **0**; 00 → **0**; 10 → **1**; 01 → **0**.
4. T = 0: Q⁺ = Q; T = 1: Q⁺ = Q'. So Q⁺ = T'Q + TQ' = **T ⊕ Q**.
5. Master and slave are **never enabled together**: the slave copies only after the master has closed, so the new Q cannot reach the inputs while they are being read; Q changes once per period.
6. **T = D ⊕ Q**: an XOR fed by D and the flip-flop's own output Q, driving T.
7. The **D latch** passes D to Q during the whole enable level; the **D flip-flop** takes D only at the clock edge. **Neither** has a forbidden input (S = D and R = D' are never both 1).

<!--/ANSWERS-->
