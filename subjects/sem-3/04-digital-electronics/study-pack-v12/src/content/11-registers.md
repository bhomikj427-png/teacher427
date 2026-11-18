# 11 — Registers, ring and Johnson counters

<div class="sub">Deck 09 (slides 1–26) · syllabus Unit 3 (registers, shift registers, ring and Johnson counters) · 4 worked questions from the deck (EX 9.20, 9.22, 9.24, 9.26) · needs 09 steps on the D flip-flop and its edge, 04 step 2 (full adder), 12 step 1 (counter, MOD)</div>

## Map

[[map:1 Register > 2 SISO > 3 SIPO > 4 PISO > 5 Universal > 6 Ring counter > 7 Johnson counter > 8 Lock-out > 9 XOR feedback > 10 Serial adder|here=1]]

File 09 built the D flip-flop: one bit, copied from D to Q at the clock edge. This file puts several of them on one clock. Side by side they store a whole word (a **register**); wired Q to D they pass the word along one place per clock (a **shift register**), which turns serial data into parallel and back. Fed back from the last stage to the first, a shift register becomes a **counter** with a fixed loop of states. File 14 then asks how fast any of these may be clocked.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| n | number of flip-flops (stages) in the register | 4 |
| Q_{0} … Q_{3} | stage outputs; Q_{0} is the stage the serial input enters, Q_{3} the last one. Words are written Q_{0}Q_{1}Q_{2}Q_{3} | 0 or 1 |
| D_{0} … D_{3} | parallel data inputs, one per stage | 0 or 1 |
| CLK | the clock: every stage copies its D input at the same rising edge | 1 Hz – 100 MHz |
| SHIFT/LOAD' | PISO control: 0 = load the D inputs, 1 = shift | 0 or 1 |
| S_{1} S_{0} | mode select of the universal register 74194: hold, shift right, shift left, load | 00 – 11 |
| DSR, DSL | 74194 serial inputs: DSR enters Q_{0} on a right shift, DSL enters Q_{3} on a left shift | 0 or 1 |
| MOD | number of different states a counter passes before it repeats | n or 2n here |

## Running example

**The word 1011 (eleven).** Step 1 stores it in one clock, step 3 loads it one bit per clock, step 4 sends it out one bit per clock, step 5 shifts it both ways in a 74194, and step 10's serial adder produces it as 0100 + 0111.

## The questions this file answers

- <span class="tag">Deck 09 slide 20 (EX 9.20)</span> A 6-bit (MOD-6) ring counter: circuit and state sequence.
- <span class="tag">Deck 09 slide 22 (EX 9.22)</span> A 4-bit (MOD-8) Johnson counter: circuit and state sequence.
- <span class="tag">Deck 09 slide 24 (EX 9.24)</span> The initial contents of the 4-bit serial-in parallel-out right-shift register shown in the figure are 0 1 1 0. Find the contents of the shift register for the next three clock cycles.
- <span class="tag">Deck 09 slide 26 (EX 9.26)</span> Serial addition: A = 0100, B = 0111. Show that A + B = 1011 is stored in A after 4 clock pulses.

---

## Build

### 1 · A register: n flip-flops on one clock

A calculator keeps the number you typed while you press "+". Something must hold all its bits at once, and change them all together when the next number arrives.

:::guess Predict
One D flip-flop holds one bit. Four of them share one clock line, and their D inputs carry 1, 0, 1, 1 just before a rising edge. What do the four outputs show just after it, and how many clock edges did that take?
:::

:::note Terms
**Register:** n flip-flops whose clock pins are joined, so they all copy their D inputs at the same edge; it stores one n-bit word. **Parallel load:** all n bits enter at the same edge, one wire per bit.
:::

[[fig:u3r_reg4|A 4-bit register (deck 09 slides 3–4): four D flip-flops, D₀–D₃ in on the left, Q₀–Q₃ out on the right, one clock line to all four.|w=45]]

Each flip-flop obeys file 09's rule Q(t+1) = D(t): *the output after the edge equals what the input was just before it*. Four of them on one clock apply the rule to four bits at once, so the register's rule is the same equation read for a whole word (deck 09 slide 4). Between edges, D can change freely; the register keeps showing the last word it took.

Deck 09 slide 13 calls this circuit "parallel in / parallel out". It is the same register: no wire runs from one stage to the next.

:::note Slide slips
Slide 2 (titled "Simple registers") says "a new 4-bit data is loaded every clock cycle" under a drawing of a shift register, which takes 4 clocks to load 4 bits (step 2). Slide 13 files this register under "shift registers" although nothing shifts. The pack uses this step's reading.
:::

**Answer to the Predict.** Q_{0}Q_{1}Q_{2}Q_{3} = **1011** after **one** edge: all four bits load together.

:::check Check 1
(a) The D inputs change from 1011 to 0110 halfway between two edges. What do the outputs show before and after the next edge? (b) How many flip-flops does a register for one byte need?
:::

### 2 · Each Q feeds the next D: serial in, serial out

Step 1 loaded four bits through four wires. A cable between two machines often has one data wire, so the bits must arrive one after another.

:::q <span class="tag">Deck 09 slides 8–10</span>
A 4-bit serial-in serial-out shift register holds 0000. The bits 1, 1, 0, 1 are applied to its serial input, one per clock, on clocks 1–4 (then 0s). On which clock does the first bit reach the serial output, and what does the output show after clocks 1–8?
:::

:::guess Guess first
How many stages must a bit pass through before it shows at Q_{3}?
:::

:::note Terms
**Shift register:** a register whose stage i takes its D from the stage before (D_{i} = Q_{i−1}), so at each edge every bit moves one stage on. **Serial input / output:** the one wire into the first stage (D_{0}) and out of the last (Q_{3}).
:::

[[fig:shift4|A 4-bit shift register (SISO, deck 09 slide 8): the serial input feeds D of the first stage, each Q feeds the next D, the last Q is the serial output.|w=70]]

At an edge every stage copies the stage before it *as it was just before the edge*, so a bit advances exactly one stage per clock, never two. A bit entering at clock k sits in Q_{0} after clock k, Q_{1} after k+1, and reaches Q_{3} after clock k+3.

| After clock | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| bit entering | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| Q_{0}Q_{1}Q_{2}Q_{3} | 1000 | 1100 | 0110 | 1011 | 0101 | 0010 | 0001 | 0000 |
| serial out Q_{3} | 0 | 0 | 0 | **1** | **1** | **0** | **1** | 0 |

Read across: the input pattern 1 1 0 1 reappears at the output unchanged, 3 clocks late. Used as a **delay line**, an n-stage SISO delays a bit by n clock periods from input wire to output: 4 stages at 1 MHz (1 µs per clock) give **4 µs**.

**Answer.** The first bit reaches the output after **clock 4**; the output after clocks 1–8 is **0 0 0 1 1 0 1 0**.

:::check Check 2
(a) An 8-stage SISO is clocked at 2 MHz. What delay does it give? (b) Why can a bit never skip a stage, even though all stages share one edge?
:::

### 3 · Serial in, parallel out: collecting a word

Step 2's table already showed the whole word sitting inside the register after clock 4. Bring every Q out on its own wire and the register converts serial data into a parallel word.

:::q <span class="tag">Deck 09 slides 11–12</span>
The binary number 1011 is loaded sequentially into a 4-bit serial-in parallel-out register (initially 0000), one bit at each clock pulse. Show the contents after each clock; when is the number available at the parallel output?
:::

:::guess Guess first
Which bit of 1011 must be sent first so that it ends up in Q_{3}?
:::

:::note Terms
**SIPO (serial in, parallel out):** the shift register of step 2 with all n outputs brought out, read together once n bits have entered. **LSB first:** the bit worth 1 is sent first.
:::

[[fig:u3r_sipo_waves|What this graph plots: time across, one row per signal (high = 1). CLK rises at edges 1–4; the serial input carries 1, 1, 0, 1 (the LSB of 1011 first); each row Q₀–Q₃ changes only at a rising edge. The word under each edge is Q₀Q₁Q₂Q₃ just after it.|w=75]]

The first bit sent travels furthest: after 4 clocks it has reached Q_{3}, and the last bit sent sits in Q_{0}. To read 1011 at the outputs with Q_{0} as the MSB, send the LSB first:

| After clock | bit entering | Q_{0}Q_{1}Q_{2}Q_{3} |
|---|---|---|
| 1 | 1 (LSB) | 1000 |
| 2 | 1 | 1100 |
| 3 | 0 | 0110 |
| 4 | 1 (MSB) | **1011** |

Between clocks 1 and 3 the outputs show part-filled words; the receiver reads them only after the n-th clock. A serial receiver (a UART, deck 09 slide 7) does exactly this, one byte at a time.

**Answer.** Contents 1000, 1100, 0110, **1011**: the number is available after **clock 4** (n clocks for n bits).

:::check Check 3
The sender sends 1011 MSB first (1, 0, 1, 1). What does Q_{0}Q_{1}Q_{2}Q_{3} read after 4 clocks, and how must the receiver read it?
:::

### 4 · Parallel in, serial out: sending a word

The sender has the opposite job: it holds a word on n wires and must put it on one wire, a bit per clock. Each stage now needs two possible D inputs: its own D_{i} (to load) or the stage before (to shift).

:::q <span class="tag">Deck 09 slides 14–15</span>
In the parallel-in serial-out register, bits are entered simultaneously but output is serial. Explain the SHIFT/LOAD' control. The word D_{0}D_{1}D_{2}D_{3} = 1011 is loaded; list the serial output after the load and after each of the next three shift clocks.
:::

:::guess Guess first
Which of the four bits appears on the output first?
:::

:::note Terms
**PISO (parallel in, serial out):** a shift register in which each stage's D is chosen by a 2-to-1 selector. **SHIFT/LOAD':** the one control line choosing it: 0 = every stage takes its D_{i} (load), 1 = every stage takes the stage before (shift). The prime on LOAD says load is the 0 state.
:::

[[fig:u3r_piso|A 4-bit PISO (deck 09 slide 15): an inverter makes SHIFT'; each later stage's D is SHIFT·Q of the stage before OR SHIFT'·its own Dᵢ (two ANDs and an OR, a 2-to-1 MUX); the first stage has only the load AND. Q₃ is the serial output.|w=80]]

The AND–OR pair in front of stage 2 computes D = SHIFT·Q_{1} + SHIFT'·D_{2} (file 05's 2-to-1 MUX with SHIFT as the select): *with SHIFT = 1 the first AND passes Q_{1} and the second is closed; with SHIFT = 0 the second passes D_{2}.* The first stage has nothing before it; during a shift its AND is closed and it takes 0.

1. SHIFT/LOAD' = 0, one clock: Q_{0}Q_{1}Q_{2}Q_{3} = 1011. The output Q_{3} already shows **d_{3} = 1**.
2. SHIFT/LOAD' = 1, shift 1: 0101, output **d_{2} = 1**.
3. Shift 2: 0010, output **d_{1} = 0**.
4. Shift 3: 0001, output **d_{0} = 1**.

Each bit stays on the output wire for one clock period, so an n-bit word occupies the line for n clock periods.

:::note Slide slip
Slide 15's callout "SHIFT·Q₀ + SHIFT'·D₁" is the stage-1 expression, but its arrow points at stage 2, whose input is SHIFT·Q₁ + SHIFT'·D₂.
:::

**Answer.** SHIFT/LOAD' = 0 loads all four bits in one clock; = 1 shifts. The output reads **1, 1, 0, 1** (d_{3}, d_{2}, d_{1}, d_{0}): the bit loaded into the last stage leaves first.

:::check Check 4
(a) SHIFT/LOAD' = 0 at an edge: what does stage 2 take? (b) Load D_{0}D_{1}D_{2}D_{3} = 1100. List the output after the load and after shifts 1–3.
:::

### 5 · Both directions and every mode: the universal register

Steps 2–4 each wired one behaviour. Put a 4-to-1 MUX (file 05) in front of every D and one chip can hold, shift either way, or load, chosen by two select bits.

:::q <span class="tag">Deck 09 slide 5</span>
The deck lists register types up to the "bidirectional shift register" and the "universal shift register". The 74194 holds Q_{0}Q_{1}Q_{2}Q_{3} = 1011. Give the contents after one clock with S_{1}S_{0} = 00, 01 (DSR = 0), 10 (DSL = 0) and 11 (D = 0110).
:::

:::guess Guess first
In which mode does the MUX feed each flip-flop its own output back?
:::

:::note Terms
**Bidirectional shift register:** it shifts toward Q_{3} (right) or toward Q_{0} (left), chosen by a control input. **Universal shift register:** bidirectional, plus parallel load and hold. The 74194 is the 4-bit chip; its mode select inputs are S_{1} S_{0}.
:::

[[fig:u3r_univ_stage|One stage i of a universal register: the 4-to-1 MUX picks the stage's next D from its own Qᵢ (hold), the stage to its left (shift right), the stage to its right (shift left) or Dᵢ (load); S₁S₀ is the MUX select.|w=65]]

| S_{1} S_{0} | Mode | Each stage takes | 1011 becomes |
|---|---|---|---|
| 0 0 | hold | its own Q | 1011 |
| 0 1 | shift right | the stage before; DSR enters Q_{0} | **0101** (DSR = 0) |
| 1 0 | shift left | the stage after; DSL enters Q_{3} | **0110** (DSL = 0) |
| 1 1 | parallel load | D_{0} … D_{3} | **0110** (D = 0110) |

Source: Nexperia 74HC194 data sheet, function table; the clock is the rising edge, and an active-low master reset MR' clears all four outputs at once without waiting for an edge. **Hold** works by feeding each flip-flop its own Q: it is clocked, but copies itself.

**Answer.** **1011, 0101, 0110, 0110** for 00, 01, 10, 11.

:::check Check 5
Start at 1011. Apply in turn: shift right with DSR = 1, shift right with DSR = 0, shift left with DSL = 1, hold. Give the word after each.
:::

### 6 · The ring counter: one 1 going round

Step 2's register loses its last bit at every clock. Wire the last output back to the first input and nothing is lost: the word circulates for ever, and the register becomes a counter.

:::q <span class="tag">Deck 09 slides 16–20 (EX 9.20)</span>
A 6-bit (MOD-6) ring counter: draw the circuit and give its state sequence.
:::

:::guess Guess first
A ring counter is started with a single 1 in Q_{0}. How many different states does a 6-bit one pass through before it repeats?
:::

:::note Terms
**Shift-register counter:** a shift register with its serial output fed back to its serial input; it is a counter because its states follow a fixed loop (slide 16). **Ring counter:** the feedback is Q_{n−1} straight into D_{0}. **One-hot:** exactly one output is 1 in each state.
:::

[[fig:u3r_ring4|A 4-bit ring counter (deck 09 slides 18–19): Q₃ goes back to D₀. START' presets the first flip-flop to 1 and clears the others, so the count starts at 1000.|w=75]]

[[fig:u3r_ring_states|What this graph plots: one circle per state Q₀Q₁Q₂Q₃, one arrow per clock edge. The single 1 moves one place per clock and wraps from Q₃ to Q₀.|w=40]]

At each clock the 1 moves one stage on, and from Q_{3} the feedback wire carries it back to Q_{0}. With n stages it is back home after n clocks: **an n-bit ring counter has n states (MOD-n)**. Each state has its own output that is 1 only in that state, so **no decoding gates are needed** (slide 19). Each output is high for one clock in every n: it is the clock frequency divided by n.

The preset matters: a ring counter started at 0000 has nothing to circulate and stays at 0000.

**Answer.** Six D flip-flops, Q_{5} → D_{0}, PRE' on the first and CLR' on the others (slide 20). Sequence **100000 → 010000 → 001000 → 000100 → 000010 → 000001 → 100000**: 6 states, **MOD-6**.

:::note Slide slip
Slide 17 draws the loop 0001 → 0010 → 0100 → 1000 but its timing diagram shifts the 1 from Q_{A} to Q_{D}. Both describe the same counter written in opposite bit orders. This file writes Q_{0} first, so the 1 moves left to right (slide 18's "1000 → 0100 → 0010 → 0001").
:::

:::check Check 6
(a) A 4-bit ring counter is wrongly started at 1100. List its states. (b) A 6-bit ring counter is clocked at 600 kHz. What is the frequency at each output?
:::

### 7 · The Johnson counter: twice the states from the same flip-flops

A ring counter uses n flip-flops for only n states. Invert the feedback and the same n flip-flops give twice as many.

:::q <span class="tag">Deck 09 slides 21–23 (EX 9.22)</span>
A 4-bit (MOD-8) Johnson counter: draw the circuit and give its state sequence.
:::

:::guess Guess first
Start at 0000 and feed Q_{3}' (which is 1) into D_{0}. What does the register look like after 4 clocks, and after 8?
:::

:::note Terms
**Johnson (twisted-ring) counter:** a shift-register counter whose feedback is the *complement* of the last stage, Q_{n−1}' → D_{0} (slide 21). **Decode term:** the AND of outputs that is 1 in one state only, used to detect that state.
:::

[[fig:johnson4|A 4-bit Johnson counter (deck 09 slide 22): Q₃' is fed back to D₀. A common CLR' starts it at 0000.|w=70]]

From 0000 the inverted feedback pushes in 1s until the register is full (1111); then Q_{3}' = 0 pushes in 0s until it is empty again. Filling takes n clocks and emptying n more: **an n-bit Johnson counter has 2n states (MOD-2n)**.

| clock | Q_{0}Q_{1}Q_{2}Q_{3} | decode | clock | Q_{0}Q_{1}Q_{2}Q_{3} | decode |
|---|---|---|---|---|---|
| 0 | 0000 | Q_{0}'Q_{3}' | 4 | 1111 | Q_{0}Q_{3} |
| 1 | 1000 | Q_{0}Q_{1}' | 5 | 0111 | Q_{0}'Q_{1} |
| 2 | 1100 | Q_{1}Q_{2}' | 6 | 0011 | Q_{1}'Q_{2} |
| 3 | 1110 | Q_{2}Q_{3}' | 7 | 0001 | Q_{2}'Q_{3} |

Each state has exactly one place where the 1s and 0s meet (or, for 0000 and 1111, the two ends), so **one 2-input AND decodes each state**: more gates than the ring counter, fewer flip-flops (slide 21). Slide 23's left-shift version (0000 → 0001 → 0011 → 0111 …) is the same counter written Q_{3}Q_{2}Q_{1}Q_{0}.

[[fig:johnson_waves|What this graph plots: time across, one row per output of the 4-bit Johnson counter. Each output is high for 4 clocks and low for 4: a square wave at f/8, each one clock later than the one above.|w=70]]

**Answer.** Four D flip-flops, Q_{3}' → D_{0}, common CLR'. Sequence **0000, 1000, 1100, 1110, 1111, 0111, 0011, 0001**, back to 0000: **MOD-8**.

:::check Check 7
(a) How many flip-flops does a MOD-10 counter need as a Johnson, a ring and a binary counter? (b) Give the decode term for state 0011. (c) List the states of a 3-bit Johnson counter.
:::

### 8 · The other states: lock-out

Four flip-flops have 2^{4} = 16 states, but the Johnson loop uses 8. A power-up glitch can leave the register in one of the other 8.

:::guess Predict
The 4-bit Johnson counter powers up at 0100. Does it find its way back to 0000?
:::

:::note Terms
**Unused state:** a register state outside the counter's loop. **Lock-out:** the counter, once in an unused state, cycles among unused states and never returns to its loop.
:::

[[fig:u3r_johnson_lockout|What this graph plots: one circle per state Q₀Q₁Q₂Q₃, one arrow per clock. Left: the 8 states of the Johnson loop. Right: the other 8 states, which form a second closed loop of their own.|w=85]]

Apply the same rule (shift, Q_{3}' into Q_{0}) starting from 0100:

0100 → 1010 → 1101 → 0110 → 1011 → 0101 → 0010 → 1001 → 0100

It is another closed loop of 8: the 16 states split into two loops with no arrow between them. The counter, once in the wrong loop, stays there; its decode ANDs then fire in the wrong pattern.

The cure is the one the deck's circuits already carry: a common **CLR'** that forces 0000 at start-up (slide 22), so the counter always starts in its own loop. A ring counter has the same problem (0000 or 1100 are outside its loop), cured by START' presetting 1000.

**Answer to the Predict.** **No.** From 0100 it runs 1010, 1101, 0110, 1011, 0101, 0010, 1001 and back to 0100: it never reaches 0000.

:::check Check 8
(a) List the three states after 1101 in the unused loop. (b) Why does clearing to 0000 at power-up remove the problem?
:::

### 9 · Feedback through an XOR

Steps 6–8 fed back one output. Feed back a combination of outputs and the register produces a longer, scrambled-looking sequence.

:::q <span class="tag">Deck 09 slide 24 (EX 9.24)</span>
The initial contents of the 4-bit serial-in parallel-out right-shift register shown in the figure are 0 1 1 0. Find the contents of the shift register for the next three clock cycles.
:::

:::guess Guess first
Which bit is lost at each clock, and what replaces it at the left?
:::

:::note Terms
**Feedback function:** the logic that computes the next serial input from the present outputs; here Q_{2} ⊕ Q_{3}, the XOR of the last two stages (1 when they differ).
:::

[[fig:sipo_xor|The register of EX 9.24 (deck 09 slide 24, redrawn): stages Q₀ to Q₃ from the left, holding 0 1 1 0; an XOR of the last two stages feeds the serial input.|w=65]]

At each edge the register shifts right (Q_{3} is lost) and Q_{0} takes the XOR, computed from the values **just before** the edge:

| Clock | Q_{2} ⊕ Q_{3} before the edge | Q_{0}Q_{1}Q_{2}Q_{3} after |
|---|---|---|
| start | | 0110 |
| 1 | 1 ⊕ 0 = 1 | **1011** |
| 2 | 1 ⊕ 1 = 0 | **0101** |
| 3 | 0 ⊕ 1 = 1 | **1010** |

Run on, this register visits all 15 non-zero 4-bit words before 0110 returns, in an order that looks random; such registers are used as pseudo-random sequence generators (file 17). From 0000 the XOR gives 0 for ever, so 0000 is its one locked state.

**Answer.** **1011, 0101, 1010.**

:::check Check 9
(a) Continue for two more clocks. (b) Why must this register not start at 0000?
:::

### 10 · Serial addition: one full adder, many bits

The ripple adder of file 04 uses one full adder per bit. Shift registers can feed the bits of two numbers past a single full adder, one pair per clock, and keep the carry in a flip-flop until the next pair arrives.

:::q <span class="tag">Deck 09 slides 25–26 (EX 9.26)</span>
In the serial adder, A ← A + B. A = 0100, B = 0111. Show that A + B = 1011 is stored in A after 4 clock pulses.
:::

:::guess Guess first
Which bits does the full adder see at the first clock, and where does the carry wait?
:::

:::note Terms
**Serial adder:** two right-shift registers A and B whose serial outputs (their LSBs) feed one full adder; the sum bit S enters A's serial input, the carry C is stored in a D flip-flop and fed back as the adder's third input. **Carry flip-flop:** holds the carry from one bit position to the next, cleared to 0 at the start.
:::

[[fig:u3r_serial_adder|The serial adder (deck 09 slide 25): A's and B's serial outputs and the carry flip-flop feed the full adder; S shifts into A, C into the carry flip-flop; one AND of Shift-right and CP clocks all three.|w=80]]

Each clock: the adder adds A's LSB x, B's LSB y and the stored carry z (file 04: S = x ⊕ y ⊕ z, C = 1 when two or more are 1); at the edge, S enters A's MSB end as A shifts right, B shifts right, and C is stored for the next bit.

| Clock | x + y + z | S, C | A after | carry after |
|---|---|---|---|---|
| 1 | 0 + 1 + 0 | 1, 0 | 1010 | 0 |
| 2 | 0 + 1 + 0 | 1, 0 | 1101 | 0 |
| 3 | 1 + 1 + 0 | 0, 1 | 0110 | 1 |
| 4 | 0 + 0 + 1 | 1, 0 | **1011** | 0 |

After 4 clocks the four sum bits have replaced A's bits, LSB first: A = 1011 = 4 + 7 = 11. The serial adder needs n clocks where the ripple adder needs one, but one full adder instead of n: slower, less hardware (slide 25).

**Answer.** Sum and carry per clock as in the table; after the 4th clock **A = 1011**, carry flip-flop 0.

:::check Check 10
Add A = 0110 and B = 0011 serially. Give S and C at each of the 4 clocks and the final A.
:::

---

## Exam form

**Shift-register types (deck 09 slides 6–15).**
1. Draw the circuit: n D flip-flops, common clock, Q_{i−1} → D_{i}.
2. Name the type by its input and output: SISO (delay line, n clocks), SIPO (serial → parallel), PISO (parallel → serial, SHIFT/LOAD' and a 2-to-1 MUX per stage), PIPO (register).
3. Trace table: one row per clock, Q_{0}…Q_{3} after the edge, each new value computed from the values before the edge.

**Universal register.** 4-to-1 MUX before each D; S_{1}S_{0} = 00 hold, 01 shift right (DSR in), 10 shift left (DSL in), 11 load.

**Ring and Johnson counters (slides 16–23).**
1. Ring: Q_{n−1} → D_{0}, preset one 1: MOD-n, one-hot, no decoder, f/n per output.
2. Johnson: Q_{n−1}' → D_{0}, clear to 0: MOD-2n, one 2-input AND per state, f/2n square waves.
3. Unused states: 2^{n} − n (ring) or 2^{n} − 2n (Johnson); start with a preset/clear to avoid lock-out.

**Serial adder (slides 25–26).** Block diagram; trace S, C and A per clock; n clocks for n bits.

## Traps

- Computing the feedback or the next stage from the new values instead of the values before the edge.
- Johnson MOD = 2n, not n or 2^{n}; ring MOD = n.
- Starting a ring counter at 0000 (it stays there) or a Johnson counter in an unused state (lock-out).
- Reading a SIPO the wrong way round: the first bit sent ends in the last stage.
- Leaving out the carry flip-flop's clear in the serial adder: a leftover 1 adds one to the sum.

## Self-test

1. Give the MOD of a 5-bit ring counter and of a 5-bit Johnson counter.
2. A Johnson counter has 8 flip-flops. How many states does it use, and how many are unused?
3. Give the decode term for Johnson state 1110 (Q_{0}Q_{1}Q_{2}Q_{3}).
4. A receiver collects bytes in an 8-bit SIPO clocked at 9600 bits per second. How long does one byte take to arrive?
5. A 74194 holds 1011. What does it hold after one clock with S_{1}S_{0} = 10 and DSL = 0?
6. Why does a ring counter need no decoding gates while a Johnson counter needs one AND per state?

<!--ANSWERS-->

## Answers

**Check 1.** (a) **1011** before the edge (the change between edges is ignored), **0110** after it. (b) **8**.

**Check 2.** (a) 8 clocks × 0.5 µs = **4 µs**. (b) Every stage copies the stage before *as it was just before the edge*; the new value appears only after the edge, too late to be copied again at the same edge.

**Check 3.** **1101**: the first bit sent (the MSB, 1) is now in Q_{3}. The receiver reads Q_{3}Q_{2}Q_{1}Q_{0} = 1011, or the sender sends the LSB first.

**Check 4.** (a) **D_{2}** (the load AND is open, the shift AND closed). (b) After the load Q_{0}Q_{1}Q_{2}Q_{3} = 1100, output d_{3} = **0**; shifts 1–3 give **0, 1, 1**. Output sequence 0, 0, 1, 1.

**Check 5.** **1101** (DSR 1 in, 1 lost), **0110**, **1101** (DSL 1 into Q_{3}), **1101**.

**Check 6.** (a) **1100, 0110, 0011, 1001**, then 1100 again: two 1s circulate, a 4-state loop outside the intended one. (b) 600 kHz / 6 = **100 kHz**.

**Check 7.** (a) Johnson **5**, ring **10**, binary **4**. (b) **Q_{1}'Q_{2}**. (c) **000, 100, 110, 111, 011, 001** (MOD-6).

**Check 8.** (a) **0110, 1011, 0101**. (b) 0000 is in the counter's own loop, and from there the shift rule only ever reaches the 8 good states.

**Check 9.** (a) From 1010: 1 ⊕ 0 = 1 → **1101**; 0 ⊕ 1 = 1 → **1110**. (b) 0 ⊕ 0 = 0, so 0000 → 0000 for ever.

**Check 10.** Clock 1: 0 + 1 + 0, S = 1, C = 0 (A = 1011). Clock 2: 1 + 1 + 0, S = 0, C = 1 (A = 0101). Clock 3: 1 + 0 + 1, S = 0, C = 1 (A = 0010). Clock 4: 0 + 0 + 1, S = 1, C = 0. Final **A = 1001** (6 + 3 = 9).

**Self-test.**

1. Ring **MOD-5**, Johnson **MOD-10**.
2. 2 × 8 = **16** used; 2^{8} − 16 = **240** unused.
3. **Q_{2}Q_{3}'**.
4. 8 bits / 9600 bits per second = **0.833 ms**.
5. Shift left, 0 into Q_{3}: **0110**.
6. A ring counter is one-hot: each state already has its own output that is 1 only then. A Johnson state is identified by where its 1s and 0s meet, which takes two outputs, so one 2-input AND.

<!--/ANSWERS-->
