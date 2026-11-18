# 17 — Timing issues, generators, asynchronous circuits

<div class="sub">Syllabus Unit 4 items with no deck slides (built from the KB; one practice question from Anna University EC6302) · needs 14 (setup, hold, clock skew), 11 (shift registers), 12 and 13 (counters), 09 steps 2–3 (the NOR and NAND latches) and 02 (K-map groups)</div>

## Map

[[map:1 Decoding glitches > 2 Metastability > 3 Switch bounce > 4 The LFSR > 5 Maximal length, lock-out > 6 Pulse trains > 7 Dividing a clock > 8 The 555 > 9 Ring oscillator > 10 Asynchronous circuits > 11 Races > 12 Static hazards > 13 Hazard-free design|here=1]]

File 14 timed one path between two flip-flops on a clean clock. This file covers the rest of syllabus Unit 4, in three parts. **Timing issues** (steps 1–3): what goes wrong when outputs are decoded from several flip-flops, when an input is not tied to the clock, and when the input is a mechanical switch. (Clock skew is in 14 step 7.) **Generators** (steps 4–9): circuits that make sequences, pulse trains and clocks. **Asynchronous circuits** (steps 10–13): circuits with no clock at all, and the two faults that come with that: races and hazards.

## Symbols

| Symbol | What it means in this file |
|---|---|
| Q_{1} … Q_{n} | flip-flop outputs of a shift register; data shift Q_{1} → Q_{2} → … → Q_{n} |
| D_{1} | the input of the first flip-flop (the feedback in an LFSR) |
| ⊕ | XOR: 1 when its inputs differ |
| t_{pd} | propagation delay of one gate or one flip-flop (clock to Q) |
| t_{su}, t_{h} | setup and hold time of a flip-flop (file 14) |
| R_{1}, R_{2}, C | the 555's timing resistors and capacitor (TI's data sheet calls them R_{A}, R_{B}) |
| t_{H}, t_{L} | time the output is high, low, in one period |
| N | number of inverters in a ring oscillator; or the modulus of a counter |
| y | a state variable of an asynchronous circuit (the signal fed back) |
| Y | the value the logic is driving y towards (the next state) |

## Running example

The generator part carries one circuit: the **3-bit LFSR** with D_{1} = Q_{2} ⊕ Q_{3}, started at Q_{1}Q_{2}Q_{3} = 100. Step 4 traces it, step 5 asks why it never reaches 000, step 6 compares it with a ring that repeats a chosen pattern. The asynchronous part carries the EC6302 function f(A, B, C, D) = ΠM(0, 2, 6, 7, 8, 10, 12) to its hazard-free form in step 13.

## The questions this file answers

- <span class="tag">practice</span> A counter's output is decoded from two flip-flops and shows short false pulses. Why, and how is it cured?
- <span class="tag">practice</span> A push-button goes straight into a 100 MHz system. What can go wrong, and how is it fixed?
- <span class="tag">practice</span> A 3-bit LFSR with D_{1} = Q_{2} ⊕ Q_{3} starts at 100. List its states and its sequence length.
- <span class="tag">practice</span> A 555 astable with R_{1} = 1 kΩ, R_{2} = 10 kΩ, C = 10 nF: frequency and duty cycle.
- <span class="tag">EC6302 Nov/Dec 2021 Q15(b) · 13 marks</span> What is the objective of state assignment in an asynchronous circuit? Give the hazard-free realisation of f(A, B, C, D) = ΠM(0, 2, 6, 7, 8, 10, 12).

No deck covers these topics, so the steps open on Predict prompts.

---

## Build

### 1 · Glitches from decoded state bits

File 13 drew counters as if all flip-flops change at the same instant. They change at the same clock edge, but each one has its own clock-to-Q delay.

:::guess Predict
A 2-bit counter goes 00 → 01 → 10 → 11. An AND gate decodes state 00: Y = Q_{1}'Q_{0}'. On the edge from 01 to 10, Q_{0} happens to fall 2 ns before Q_{1} rises. What does Y do in those 2 ns?
:::

:::note Terms
**Glitch:** a short pulse on a signal that should not change at all (or should change once). **Decoded output:** an output formed by gates from several state bits, like Y = Q_{1}'Q_{0}'. **Registered output:** an output taken straight from a flip-flop.
:::

[[fig:u4b_decode_glitch|What this graph plots: time across (ns), one row per signal, high = 1. The clock edge at 10 ns moves the counter from 01 to 10; Q0 falls at 17 ns, Q1 rises at 19 ns, so for 2 ns the bits read 00 and the decoder output Y pulses.|w=78]]

When two bits change on one edge, the circuit passes through an in-between state for as long as the delays differ. From 01 to 10 there are two possible in-between states:

1. Q_{0} first: 01 → **00** → 10.
2. Q_{1} first: 01 → **11** → 10.

Any gate that decodes the in-between state gives a short false pulse. Glitches do not matter to logic that is only read at the next clock edge: by then everything has settled. They do matter when the output drives something that reacts at once: a clock input, an asynchronous clear, a counter in another clock domain.

**The cure: register the output.** Compute the output one state early and store it in a flip-flop on the same clock. Y must be 1 in state 00, and the state before 00 is 11, so the flip-flop's input is D_{Y} = Q_{1}Q_{0}. Y then comes from a flip-flop and changes once per edge. This is the Moore-style output of file 15: an output that depends only on the state, taken from a register, is glitch-free.

**Answer to the Predict.** For those 2 ns the bits read 00, so **Y gives a 2 ns false pulse** (shifted by the AND gate's delay). Q_{1} rising first would have given 11 instead, and no pulse on this Y.

:::check Check 1
(a) A 3-bit up counter has an output Y that decodes state 000. On which transitions can Y give a false pulse? (b) Write D_{Y} for the registered version of that Y.
:::

### 2 · Asynchronous inputs and metastability

Step 1's in-between states come from the circuit's own delays. An input from outside, with no link to the clock, makes a worse fault.

:::guess Predict
A push-button signal goes straight into a flip-flop clocked at 100 MHz. The button can be pressed at any moment. What does file 14 step 4 say about a D input that changes inside the setup/hold window?
:::

:::note Terms
**Asynchronous input:** a signal that can change at any time relative to the clock (a button, a sensor, data from a system on another clock). **Metastability:** when D changes inside the setup/hold window, the flip-flop's output can hang between 0 and 1 for an unpredictable time, then fall to either value. **Synchronizer:** two D flip-flops in series on the system clock; the asynchronous signal enters the first, the system reads only the second.
:::

[[fig:u4b_sync|Top: the two-flip-flop synchronizer. Bottom: what this graph plots: time across (ns), one row per signal. A changes at 19.6 ns, inside the window around the edge at 20 ns; FF1 hangs undecided until about 26 ns; FF2 samples Q1 at 30 ns, after it has settled.|w=80]]

A flip-flop is a latch pair (file 09): two gates feeding each other. Between "0" and "1" there is a balance point. If D changes just as the edge closes the latch, the loop can start at that balance point and take a long, unpredictable time to tip one way. Two faults follow:

1. The output sits at an invalid level, which other gates may read differently.
2. If the input fans out to several flip-flops, some may catch the new value and some the old one, so the circuit enters a state it was never designed for.

**The synchronizer.** FF1 takes the risk; FF2 reads FF1 one clock period later. In a 100 MHz system FF1 has 10 ns, minus FF2's setup time (say 2 ns), so 8 ns to settle. The chance that a flip-flop is still undecided falls off exponentially with the time it is given (KB 04 stage 2, NXP AN219), so a whole period makes a failure very rare. **It never makes it impossible.** The price is delay: the system sees the input one to two clock periods late.

**Answer to the Predict.** The button can change inside the setup/hold window, so the flip-flop can go **metastable**, and different flip-flops may read different values. Fix: pass it through a **two-flip-flop synchronizer** first (and debounce it, step 3).

:::check Check 2
(a) The synchronizer runs at 50 MHz and FF2 needs t_{su} = 2 ns. How long does FF1 get to settle? (b) Why is one flip-flop not enough? (c) What does the synchronizer cost?
:::

### 3 · Switch bounce and debouncing

Step 2 treated the button as one clean change at a random time. A real switch gives several.

:::guess Predict
A mechanical switch closes once. Its metal contacts are springy. What does the voltage on the contact look like for the first moments after it closes, and what would a counter connected to it count?
:::

:::note Terms
**Contact bounce:** the springy contacts strike, rebound and strike again several times before they stay closed, so one press gives a burst of pulses. **SPDT switch** (single pole, double throw): a common terminal that touches either contact A or contact B. **Debouncing:** turning the burst into one clean edge.
:::

[[fig:u4b_bounce|What this graph plots: time across, rows the raw switch contact and the latch output Q. The contact bounces after the press and after the release; Q changes once each time.|w=72]]

**The SR-latch debouncer** (Utah CS 5780 lecture 11; UNC Charlotte ECGR 2156 lab 2). Use an SPDT switch and the NAND latch of file 09 step 3 (inputs S' and R', active low):

1. The common terminal is grounded. Contact A goes to S', contact B to R'. Pull-up resistors hold each input at 1 when its contact is open.
2. Pressing the switch moves the common terminal to A: S' goes to 0, the latch sets, Q = 1.
3. Now A bounces: S' flips between 0 and 1. With R' = 1, S'R' = 01 sets and S'R' = 11 holds, so Q stays 1. The terminal never bounces back as far as B.
4. Releasing it moves the terminal to B: R' goes to 0, the latch resets, and bounce on B again only alternates reset and hold.

So the latch works because a bounce only ever repeats the same command or says "hold". The other cure in the KB is a monostable (step 8) or an RC filter followed by a Schmitt trigger, which ignores a signal until it has been steady long enough.

**Answer to the Predict.** A **burst of pulses** before the contact stays closed, so a counter counts several presses for one. A latch on a two-way switch turns the burst into **one edge**.

:::check Check 3
(a) Why does the debouncer need a two-way (SPDT) switch rather than a simple push-to-close one? (b) During a bounce on contact A, the latch sees S'R' = 11 for a moment. What does it do?
:::

### 4 · The LFSR: a shift register that feeds itself

File 11 ended with shift registers whose first input is a function of their own outputs (ring, Johnson, XOR feedback). The LFSR is the XOR version made into a sequence generator.

:::guess Predict
A 3-bit shift register shifts Q_{1} → Q_{2} → Q_{3} on each clock, and its input is D_{1} = Q_{2} ⊕ Q_{3}. It starts at 100. How many different states will you see before 100 comes back? (There are 8 states in all.)
:::

:::note Terms
**LFSR (linear-feedback shift register):** a shift register whose input is the XOR of chosen outputs. **Taps:** the outputs fed into the XOR. **Sequence length (period):** the number of states before the register repeats.
:::

[[fig:lfsr3|The running example: three D flip-flops in a shift register, Q1 to Q2 to Q3, with D1 = Q2 XOR Q3 fed back (the taps).|w=60]]

Trace it: at each edge the new Q_{1} is Q_{2} ⊕ Q_{3}, and the old Q_{1}, Q_{2} move right.

| Clock | Q_{1}Q_{2}Q_{3} | D_{1} = Q_{2} ⊕ Q_{3} |
|---|---|---|
| 0 | 100 | 0 ⊕ 0 = 0 |
| 1 | 010 | 1 ⊕ 0 = 1 |
| 2 | 101 | 0 ⊕ 1 = 1 |
| 3 | 110 | 1 ⊕ 0 = 1 |
| 4 | 111 | 1 ⊕ 1 = 0 |
| 5 | 011 | 1 ⊕ 1 = 0 |
| 6 | 001 | 0 ⊕ 1 = 1 |
| 7 | 100 | back to the start |

The output, read at Q_{3}, is **0 0 1 0 1 1 1**, then the same again. It looks random (four 1s, three 0s, no obvious pattern) but it is fixed and repeatable, which is why an LFSR is called a **pseudo-random binary sequence (PRBS) generator**. Uses: test patterns for chips, scrambling data, spread-spectrum codes (KB 04 §5).

**Answer to the Predict.** **7 states**: 100, 010, 101, 110, 111, 011, 001. That is every state except 000.

:::check Check 4
(a) Trace the running example from 011. Which state follows 001? (b) What is the output sequence at Q_{1} over one period?
:::

### 5 · Maximal length and the lock-out state

Step 4's register visited 7 of 8 states. Two questions: why not the 8th, and does every choice of taps visit that many?

:::guess Predict
Start the running example at 000. What is D_{1}, and what is the next state?
:::

:::note Terms
**Maximal-length LFSR:** an n-bit LFSR that visits all **2^{n} − 1** non-zero states before repeating. **Lock-out state:** a state the register cannot leave.
:::

**The lock-out.** With XOR feedback, 000 gives D_{1} = 0 ⊕ 0 = 0 and the next state is 000 again, forever. That is why 2^{n} − 1 is the most an XOR LFSR can reach: all-zeros is its own one-state cycle. The register must be started (seeded) at any non-zero value. (An LFSR built with XNOR instead locks at all-ones, because XNOR of 1 and 1 is 1.)

**The taps decide the length.** Only some tap choices are maximal; the rule (a "primitive feedback polynomial") is beyond this course, so exam questions give the taps and ask you to trace. Two 4-bit choices:

| Taps | Cycles found by tracing every start | Maximal? |
|---|---|---|
| D_{1} = Q_{3} ⊕ Q_{4} | 15 states + the lock-out 0000 | yes: 2^{4} − 1 = 15 |
| D_{1} = Q_{2} ⊕ Q_{4} | 6, 6 and 3 states + 0000 | no |

With Q_{2} ⊕ Q_{4}, starting at 1000 gives 1000 → 0100 → 1010 → 0101 → 0010 → 0001 → 1000: only 6 states. Which cycle you land in depends on the seed.

**Answer to the Predict.** D_{1} = 0, and the next state is **000 again**: the register is stuck. That is the one state the running example never visits.

:::check Check 5
(a) Sequence length of a maximal 5-bit LFSR? (b) A 4-bit LFSR, seeded at 1000, returns to 1000 after 6 clocks. Is it maximal? (c) Why must an LFSR's reset put a 1 somewhere?
:::

### 6 · Pulse-train generators

An LFSR makes a sequence you don't choose. Often you need a fixed pattern: say 1 1 0 1 0 0, one bit per clock, repeating.

:::guess Predict
You need the train 1 1 0 1 0 0 repeating. One way uses 6 flip-flops and no gates. Another uses 3 flip-flops and a few gates. What are they?
:::

:::note Terms
**Pulse-train (sequence) generator:** a synchronous circuit whose output repeats a fixed bit pattern, one bit per clock. Its period is the number of states it cycles through.
:::

**Way 1: a ring.** Load the 6 bits into a 6-flip-flop ring counter (file 11 step 6: the last output feeds the first input). Each clock rotates the pattern by one place, and any one output gives the train. Cost: one flip-flop per bit, no logic.

**Way 2: a counter plus output logic.** A MOD-6 counter (file 13) steps through 0–5. Z must be 1 at counts 0, 1 and 3:

| Count Q_{2}Q_{1}Q_{0} | 000 | 001 | 010 | 011 | 100 | 101 |
|---|---|---|---|---|---|---|
| Z | 1 | 1 | 0 | 1 | 0 | 0 |

Counts 6 and 7 never occur, so they are don't-cares. The K-map gives

$$Z = Q_{2}'Q_{1}' + Q_{2}'Q_{0}$$

(Q_{1}Q_{0}, using don't-care 7, is an equally small second term.) Cost: 3 flip-flops plus two ANDs and an OR. For long patterns the counter wins: n flip-flops count to 2^{n}. Z is decoded from several state bits, so step 1 applies: register Z if it drives anything edge-sensitive.

**Answer to the Predict.** A **6-flip-flop ring loaded with 110100**, or a **MOD-6 counter with Z = Q_{2}'Q_{1}' + Q_{2}'Q_{0}**.

:::check Check 6
(a) A ring counter is to repeat 1 0 0 1 1 1 0 0. How many flip-flops? (b) Design Z for the train 1 0 1 1 0 from a MOD-5 counter (don't-cares 5, 6, 7).
:::

### 7 · Dividing a clock

Step 6's MOD-6 counter repeats every 6 clocks. Any counter's output bit is a slower clock.

:::guess Predict
You have 50 Hz from the mains and need a 1 Hz clock. Which counter, how many flip-flops, and is its top bit a square wave?
:::

:::note Terms
**Frequency divider:** a counter used for its output frequency. **Duty cycle:** the fraction of each period the signal is high (a square wave is 50 %).
:::

**Binary division.** In a binary counter, Q_{0} toggles every clock, Q_{1} every 2, Q_{2} every 4: their frequencies are f/2, f/4, f/8. k toggle flip-flops in a chain divide by 2^{k} (file 12).

**Division by N.** A MOD-N counter returns to 0 every N clocks, so any of its bits repeats at f/N. But the top bit is not a square wave unless N is a power of 2. For MOD-50:

1. Flip-flops: 6, because 2^{5} = 32 < 50 ≤ 64 = 2^{6}.
2. The top bit Q_{5} (weight 32) is 1 for counts 32–49: 18 of every 50 counts.
3. Duty cycle = 18/50 = **36 %**.

For a 50 % square wave, divide by half the number first and finish with one toggle flip-flop: MOD-25 gives 2 Hz, the T flip-flop halves it to 1 Hz, high for exactly one 2 Hz period in two.

**Answer to the Predict.** A **MOD-50 counter** (6 flip-flops). Its top bit is 1 Hz but only **36 %** high; **MOD-25 then a T flip-flop** gives a 1 Hz square wave.

:::check Check 7
(a) Divide 1 MHz to 1 kHz with a counter: what modulus, and how many flip-flops at least? (b) A 3-bit binary counter is clocked at 8 MHz. What frequency is Q_{2}?
:::

### 8 · Making the clock: multivibrators and the 555

Step 7 divides a clock that already exists. Something has to make the first one.

:::guess Predict
A 555 timer is wired as a free-running oscillator with R_{1} = 1 kΩ, R_{2} = 10 kΩ, C = 10 nF. The capacitor charges through R_{1} + R_{2} and discharges through R_{2} alone. Will the output be high for more or less than half of each period?
:::

:::note Terms
**Multivibrator:** a two-state switching circuit, named by how many states it can rest in.
:::

| Multivibrator | Stable states | What it gives | Seen in |
|---|---|---|---|
| Astable | none | a free-running square wave: a clock | 555 astable, ring oscillator (step 9) |
| Monostable | one | one pulse of fixed width per trigger (a "one-shot") | 555 monostable, debouncing |
| Bistable | two | stays in either state until told: memory | the latch and flip-flop (file 09) |

[[fig:astable_555|The 555 wired as an astable: R1 from the supply to the discharge pin, R2 from there to the capacitor C; the output is the clock.|w=55]]

**The 555 astable** (TI NE555 data sheet SLFS022K, eq. 1–5). C charges through R_{1} + R_{2} from ⅓ to ⅔ of the supply (output high) and discharges through R_{2} alone (output low):

$$t_{H} = 0.693(R_{1} + R_{2})C    t_{L} = 0.693R_{2}C$$

$$f = \frac{1}{t_{H} + t_{L}} = \frac{1.44}{(R_{1} + 2R_{2})C}    duty = \frac{R_{1} + R_{2}}{R_{1} + 2R_{2}}$$

Read them: *each half-period is 0.693 times the RC it charges or discharges through*; 1.44 is 1/0.693. For the Predict's values:

1. t_{H} = 0.693 × 11 kΩ × 10 nF = 76.2 μs.
2. t_{L} = 0.693 × 10 kΩ × 10 nF = 69.3 μs.
3. f = 1.44 / (21 kΩ × 10 nF) = **6.86 kHz** (1/(t_{H} + t_{L}) gives 6.87 kHz; the gap is the rounding in 1.44).
4. Duty = 11/21 = **52.4 %**.

Since R_{1} + R_{2} > R_{2}, the duty is always above 50 % in this circuit; R_{2} ≫ R_{1} brings it close.

**The 555 monostable:** one trigger pulse gives one output pulse of width **T = 1.1RC** (data sheet §6). R = 47 kΩ, C = 10 μF: T = 1.1 × 47 kΩ × 10 μF = 517 ms.

**Answer to the Predict.** **More than half**: charging runs through R_{1} + R_{2} = 11 kΩ, discharging through 10 kΩ, so **52.4 %** high, at **6.86 kHz**.

:::check Check 8
(a) R_{1} = 2 kΩ, R_{2} = 4 kΩ, C = 0.1 μF: f and duty cycle? (b) Why can this circuit never give exactly 50 %?
:::

### 9 · Ring oscillator and crystal

The 555 needs a resistor and a capacitor. Inside a chip, a clock can be made from inverters alone.

:::guess Predict
Connect inverters in a loop, each output into the next input. With 2 inverters, what happens? With 3?
:::

:::note Terms
**Ring oscillator:** an odd number N of inverters connected in a loop. **Crystal oscillator:** an oscillator whose frequency is set by the mechanical resonance of a quartz crystal.
:::

[[fig:ring_osc|Ring oscillator: an odd number of inverters in a loop; the output of the last feeds the first.|w=55]]

With an **even** number of inverters the loop is consistent: 2 inverters is the latch of file 09, with two stable states, and it settles. With an **odd** number there is no consistent state: a 1 sent round the loop comes back as 0. An edge chases itself round the ring. It takes N·t_{pd} to go round once, and a full period needs two trips (one rising, one falling):

$$f = \frac{1}{2Nt_{pd}}$$

Five inverters of 2 ns: f = 1 / (2 × 5 × 2 ns) = 1/(20 ns) = **50 MHz**.

The ring is cheap but its t_{pd} drifts with temperature, supply voltage and manufacture, so its frequency does too. It is used to measure gate delay on a chip, not to clock a system. System clocks come from a **crystal oscillator**, accurate to parts per million (KB 04 §5).

**Answer to the Predict.** **2 inverters latch** (stable, no oscillation); **3 oscillate**, because an odd loop has no stable state.

:::check Check 9
(a) A ring of 3 inverters with t_{pd} = 1 ns: f? (b) 7 inverters of 1.5 ns: period and f?
:::

### 10 · Asynchronous circuits: the flow table

Every circuit so far changed state only at a clock edge. Take the clock away and the feedback loop itself is the memory.

:::guess Predict
The NOR latch of file 09 step 2 has no clock. Its Q is fed back into its own logic. With S = 0, R = 0 it holds Q. Make S = 1: Q becomes 1. Does it change anything if S then goes back to 0?
:::

:::note Terms
**Asynchronous (sequential) circuit:** no clock; the state is held in feedback loops and changes as soon as an input does. **State variable y:** the signal fed back. **Next state Y:** the value the logic drives y towards. **Stable state:** Y = y, nothing moves. **Fundamental mode:** only one input changes at a time, and only after the circuit has settled.
:::

Read the NOR latch as an asynchronous circuit. Its feedback gives

$$Y = R'(S + y)$$

Read it: *the latch is 1 next if R is 0 and either S is 1 or it was already 1*. The **flow table** lists Y for every present y and input SR; a stable entry (Y = y) is circled in books, here **bold**:

| y \ SR | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| 0 | **0** | **0** | **0** | 1 |
| 1 | **1** | 0 | 0 | **1** |

To follow the circuit: stay in the row of the present y, move along the row when an input changes, and if the entry is not stable, move down or up to the row it names (y becomes Y). Then look again.

1. Start y = 0, SR = 00: stable.
2. S rises, SR = 10: the entry is 1, unstable. y becomes 1; in row 1, column 10 is 1: stable. The latch has set.
3. S falls, SR = 00: row 1, column 00 is 1: stable. The latch remembers.

The fundamental-mode rule matters because with two inputs changing at once the circuit could pass through either in-between column, just as step 1's bits passed through either in-between state.

**Answer to the Predict.** **No**: after S returns to 0 the circuit sits in the stable entry y = 1, SR = 00. The feedback holds the 1.

:::check Check 10
(a) From y = 1, SR = 10, R rises (SR = 11). Follow the table: where does it settle? (b) In one sentence, what is a stable state?
:::

### 11 · Races and state assignment

In step 10 one state variable changed. With two or more, the order in which they change is decided by gate delays.

:::guess Predict
An asynchronous circuit has state variables y_{1}y_{2}. In state 00, an input change asks for state 11. Both variables are told to change "at once". What decides which changes first, and does it matter?
:::

:::note Terms
**Race:** a transition in which two or more state variables must change. **Non-critical race:** every order of change ends in the same stable state. **Critical race:** the end state depends on the order, so the circuit is sometimes wrong.
:::

One column of a flow table (input x = 1), present state y_{1}y_{2} → next:

| y_{1}y_{2} | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| table A (critical) | 11 | **01** | **11** | 11 |
| table B (non-critical) | 11 | 11 | **11** | 11 |
| table C (cycle) | 10 | **01** | **11** | 11 |

From 00 the circuit must reach 11:

1. Table A, y_{1} first: 00 → 10 → 11, stable. Correct.
2. Table A, y_{2} first: 00 → 01, and 01 is **stable**: it stops there. Wrong. **Critical race.**
3. Table B: whichever changes first, the in-between state leads on to 11. **Non-critical.**
4. Table C: 00 is sent to 10 first, then 10 → 11. Each move changes one variable, so there is no race at all (a **cycle** through an unstable state).

**State assignment** is the step where binary codes are given to the states. Its objective in an asynchronous circuit: **give states that have a transition between them codes that differ in one bit**, so every transition changes one variable and no critical race can occur. Where that is impossible, route the transition through an extra unstable state, as table C does.

**Answer to the Predict.** **Gate and wire delays** decide, and it matters when an in-between state is stable for that input: then the circuit stops in the wrong state (a critical race).

:::check Check 11
(a) Critical vs non-critical race, one line each. (b) <span class="tag">EC6302 part (a)</span> What is the objective of state assignment in an asynchronous circuit?
:::

### 12 · Static hazards and the consensus term

Step 11's fault came from two state variables. A single input change can also cause a wrong pulse, inside the combinational logic alone.

:::guess Predict
F = AB + A'C with B = C = 1. Then F = A + A' = 1 for either A. Now A falls from 1 to 0. The inverter that makes A' takes 2 ns. Can F dip to 0?
:::

:::note Terms
**Static-1 hazard:** the output should stay 1 but dips to 0 for a moment. **Static-0 hazard:** should stay 0 but pulses to 1. **Dynamic hazard:** should change once but changes three or more times. **Consensus term:** for XY + X'Z, the term YZ; adding it does not change the function (file 01: AB + A'C + BC = AB + A'C).
:::

[[fig:u4b_static1|What this graph plots: time across (ns), one row per signal, B = C = 1 throughout. NOT 2 ns, AND 3 ns, OR 3 ns. A falls at 10 ns; AB falls at 13 ns but A'C rises only at 15 ns, so F dips from 16 to 18 ns. With BC added, F stays 1.|w=78]]

Follow the delays (NOT 2 ns, AND 3 ns, OR 3 ns), A falling at 10 ns:

1. AB falls at 10 + 3 = 13 ns.
2. A' rises at 10 + 2 = 12 ns, so A'C rises at 12 + 3 = 15 ns.
3. From 13 to 15 ns both products are 0. F, 3 ns behind, is 0 from **16 to 18 ns**: a 2 ns dip, the inverter's delay.

**On the K-map:** cells A'BC (3) and ABC (7) are both 1 and are neighbours, but AB holds one and A'C the other. Moving between them hands F from one product to the other, and the hand-over can leave a gap. **The rule:** every pair of adjacent 1s must lie together in some group. Add the group that joins them: BC, the consensus term. With B = C = 1, BC = 1 whatever A does, so F stays 1.

$$F = AB + A'C + BC$$

The POS form has the mirror fault: (A + B)(A' + C) with B = C = 0 can pulse to 1 (static-0), cured by the consensus factor (B + C). Two-level SOP with every adjacent pair covered is free of static and dynamic hazards for single input changes.

**Answer to the Predict.** **Yes**: F dips to 0 for **2 ns** (16 to 18 ns). Adding **BC** removes it.

:::check Check 12
(a) F = A'B + AC: which input change can cause a static-1 hazard, and which term removes it? (b) For (A + B)(A' + C), when can a static-0 hazard occur, and what is added?
:::

### 13 · Hazard-free design (EC6302)

Step 12 found the hazard in a 3-variable function by eye. The same rule, applied cell by cell, solves the exam question.

:::q <span class="tag">EC6302 Nov/Dec 2021 Q15(b) · 13 marks</span>
What is the objective of state assignment in an asynchronous circuit? Give the hazard-free realisation for the Boolean function f(A, B, C, D) = ΠM(0, 2, 6, 7, 8, 10, 12).
:::

:::guess Predict
The minimal SOP of f has four terms. How many adjacent pairs of 1s do you expect to find that no single term covers: none, a few, or many?
:::

[[fig:hazard|Top: f's K-map, rows AB and columns CD, each cell's small number its minterm, with the four minimal groups and the added group AD (cells 9, 11, 13, 15). Bottom: what this graph plots: time across, rows the two product terms and F; when B falls in cell 15 the output passes from one term to the other and F dips.|w=80]]

1. **The 1s.** ΠM lists the 0s, so the 1s are the rest: **Σm(1, 3, 4, 5, 9, 11, 13, 14, 15)**.
2. **Minimal cover** (file 02): B'D (1, 3, 9, 11), C'D (1, 5, 9, 13), A'BC' (4, 5), ABC (14, 15).
3. **Check every adjacent pair of 1s.** All pairs share a group except two: 11 (1011) with 15 (1111), where B'D holds 11 and ABC holds 15; and 13 (1101) with 15 (1111), where C'D holds 13 and ABC holds 15.
4. **Add one group for both.** Cells 9, 11, 13, 15 are all 1s and form the quad **AD**; it holds 11 with 15 and 13 with 15.

$$f = B'D + C'D + A'BC' + ABC + AD$$

AD is redundant for the function (it covers no new 1) and essential for the timing. Leave it out and B falling at ABCD = 1111 (cell 15 → 11) can make f glitch.

One hazard this method cannot reach: an **essential hazard** lives in the asynchronous circuit's flow table itself, not in any one function's cover; it is cured by adding delay in the feedback path, not by consensus terms (KB 04 §6).

**Answer to the question.** **State assignment:** codes for states with a transition between them differ in one bit, so no critical race occurs (step 11). **Hazard-free f = B'D + C'D + A'BC' + ABC + AD.** **Answer to the Predict:** **a few**: exactly two pairs, (11, 15) and (13, 15), and one extra term covers both.

:::check Check 13
(a) F(A, B, C) = Σm(0, 1, 5, 7) has minimal SOP A'B' + AC. Find the uncovered adjacent pair and the term that fixes it. (b) Why can't a consensus term cure an essential hazard?
:::

---

## Exam form

**Timing issues (steps 1–3).**
1. Decoded-output glitch: list the in-between states of a multi-bit change; cure by registering the output (D = the decode of the state before).
2. Metastability: cause (D changes inside setup/hold), effects (invalid level; flip-flops disagree), two-flip-flop synchronizer (rare, not impossible; one or two clocks of delay).
3. Debounce: SPDT switch + SR latch; bounce only repeats "set" or says "hold".

**Generators (steps 4–9).**
4. LFSR trace table; length 2^{n} − 1 when maximal; all-zeros lock-out (XNOR: all-ones).
5. Pulse train: ring of n flip-flops loaded with the pattern, or MOD-n counter + output K-map.
6. Division: f/2^{k} from binary bits; MOD-N for f/N; MOD-N/2 then T flip-flop for 50 %.
7. Multivibrator table; 555: t_{H} = 0.693(R_{1} + R_{2})C, t_{L} = 0.693R_{2}C, f = 1.44/((R_{1} + 2R_{2})C), duty = (R_{1} + R_{2})/(R_{1} + 2R_{2}); monostable T = 1.1RC. Ring: f = 1/(2Nt_{pd}), N odd.

**Asynchronous (steps 10–13).**
8. Flow table: stable entries, moving along a row then to the named row; fundamental mode.
9. Races: critical vs non-critical; state assignment with one-bit transitions; cycles.
10. Hazards: static-1, static-0, dynamic, essential; every adjacent pair of 1s in a common group; consensus term.

## Traps

- Saying a synchronizer makes metastability impossible: it makes failure rare.
- Debouncing with a one-way switch and a latch: the latch needs both contacts.
- Seeding an LFSR with all zeros (or an XNOR LFSR with all ones).
- Taking 2^{n} − 1 for any taps: only maximal taps reach it; trace the given ones.
- Using a MOD-N counter's top bit as a square wave when N is not a power of 2.
- Writing 555 f = 1.44/((R_{1} + R_{2})C): the discharge resistor counts twice, (R_{1} + 2R_{2}).
- A ring oscillator with an even number of inverters: it latches.
- Removing a "redundant" consensus term from a hazard-free design.
- Forgetting that ΠM lists the 0s: the K-map's 1s are the missing numbers.

## Self-test

1. A 4-bit LFSR with D_{1} = Q_{3} ⊕ Q_{4} is seeded at 0001. How many clocks until 0001 returns?
2. 555 monostable with R = 10 kΩ, C = 1 μF: pulse width?
3. 555 astable with R_{1} = 4.7 kΩ, R_{2} = 47 kΩ, C = 1 nF: f and duty cycle?
4. Ring oscillator of 9 inverters, t_{pd} = 0.5 ns: f?
5. A 2-bit up counter has an output Y = Q_{1}Q_{0}. On which transition can it glitch, and with which bit changing first?
6. Divide 100 MHz to a 1 MHz square wave (50 % duty).
7. F = A'B + AC. Find the hazard and remove it.
8. Draw a two-flip-flop synchronizer and explain why the second flip-flop is there.

<!--ANSWERS-->

## Answers

**Check 1.** (a) 001 → 010 (Q_{0} falls first: 000) and 011 → 100 (Q_{1} and Q_{0} fall before Q_{2} rises: 000). 111 → 000 ends in 000, so a 1 there is correct. (b) The state before 000 is 111: **D_{Y} = Q_{2}Q_{1}Q_{0}**.

**Check 2.** (a) 1/50 MHz = 20 ns, minus 2 ns: **18 ns**. (b) One flip-flop's output can itself be metastable, and the system would read it; the second gives it a whole period to settle first. (c) **Delay**: the input reaches the system one to two clock periods late.

**Check 3.** (a) With one contact the latch has only a "set" input; the release must drive "reset" from the other contact. Each contact only ever sends one command, which is what makes bounce harmless. (b) **Holds**: S'R' = 11 is the NAND latch's no-change input.

**Check 4.** (a) 011 → 001 → **100** → 010 → 101 → 110 → 111 → 011. (b) Q_{1} over one period from 100: **1 0 1 1 1 0 0**.

**Check 5.** (a) 2^{5} − 1 = **31**. (b) **No**: maximal for 4 bits is 15. (c) All-zeros is a lock-out: from 0…0 it never moves.

**Check 6.** (a) **8** flip-flops, one per bit. (b) Z = 1 at counts 0, 2, 3: **Z = Q_{1} + Q_{2}'Q_{0}'** (Q_{1} groups 2, 3, 6, 7 with the don't-cares).

**Check 7.** (a) **MOD-1000**, at least **10** flip-flops (2^{10} = 1024 ≥ 1000). (b) 8 MHz / 8 = **1 MHz**.

**Check 8.** (a) f = 1.44 / ((2 + 8) kΩ × 0.1 μF) = **1.44 kHz**; duty = 6/10 = **60 %**. (b) The high time charges through R_{1} + R_{2}, the low time through R_{2} only; with R_{1} > 0 the high time is always longer.

**Check 9.** (a) 1/(2 × 3 × 1 ns) = **167 MHz**. (b) Period 2 × 7 × 1.5 ns = **21 ns**, f = **47.6 MHz**.

**Check 10.** (a) Row 1, column 11: Y = 0, unstable; move to row 0, column 11: 0, **stable at y = 0** (the NOR latch's S = R = 1 gives Q = 0). (b) A state where the next state equals the present one (Y = y), so nothing changes until an input does.

**Check 11.** (a) Critical: the end state depends on which variable changes first. Non-critical: every order ends in the same stable state. (b) To give states with a transition between them **codes differing in one bit**, so no transition races and no **critical race** can occur.

**Check 12.** (a) With **B = C = 1**, a change of **A** hands F from A'B to AC; add **BC**: F = A'B + AC + BC. (b) With **B = C = 0**, a change of A; add the factor **(B + C)**: (A + B)(A' + C)(B + C).

**Check 13.** (a) Cells 1 (001) and 5 (101) are adjacent 1s, held by A'B' and AC separately; add **B'C**: F = A'B' + AC + B'C. (b) An essential hazard comes from the flow table (an input change racing the feedback), not from a gap in one function's cover; it needs **delay** in the feedback path.

**Self-test.**

1. Maximal 4-bit taps: **15** clocks.
2. 1.1 × 10 kΩ × 1 μF = **11 ms**.
3. f = 1.44 / (98.7 kΩ × 1 nF) = **14.6 kHz**; duty = 51.7/98.7 = **52.4 %**.
4. 1/(2 × 9 × 0.5 ns) = 1/(9 ns) = **111 MHz**.
5. **01 → 10, with Q_{1} rising first**: the bits pass through 11.
6. **MOD-50 then a T flip-flop** (÷100, 50 % duty); a MOD-100 counter's top bit is not a square wave.
7. With B = C = 1, A changing: static-1 hazard. Add **BC**: F = A'B + AC + BC.
8. Two D flip-flops in series on the system clock; the asynchronous input enters the first. If the first goes metastable, the second samples it a whole period later, after it has (almost always) settled.

<!--/ANSWERS-->
