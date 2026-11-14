# 11 — Registers, ring and Johnson counters

<div class="sub">Deck 09 (slides 6–26) · syllabus Unit 3 · needs 09 (D flip-flops)</div>

## Map

[[map:1 Shift registers > 2 Ring and Johnson counters|here=1]]

One flip-flop stores a bit; a row of them sharing a clock stores a word. Connect each Q to the next D and the word moves one place per clock. Feed the end back to the start and it becomes a counter.

## The questions this file answers

- <span class="tag">Deck 09 slide 24</span> A 4-bit SIPO right-shift register with XOR feedback holds 0110. Find its contents for three clocks.
- <span class="tag">Deck 09 slides 16–23</span> Draw a 4-bit Johnson counter; give its sequence and modulus; compare it with a ring counter.

---

## Build

### 1 · Shift registers

:::q <span class="tag">Deck 09 slide 24 (figure redrawn)</span>
The initial contents of the 4-bit serial-in-parallel-out right-shift register shown in the figure is 0 1 1 0. Find out the contents of the shift register for upcoming three clock cycles.
:::

[[fig:sipo_xor|The register: serial input = Q_{2} ⊕ Q_{3}.|w=65]]

:::guess Guess first
Which bit is lost at each clock, and what replaces it at the left?
:::

:::note Terms
**Register:** n flip-flops on one clock, storing an n-bit word. **Shift register:** each Q feeds the next D, so the word moves one place per clock.
:::

[[fig:shift4|4-bit shift register.|w=70]]

| Type | In | Out | Use |
|---|---|---|---|
| SISO | serial | serial | delay line: n clocks |
| SIPO | serial | parallel | serial → parallel (receiver) |
| PISO | parallel load | serial | parallel → serial (transmitter) |
| PIPO | parallel | parallel | storage |

Serial loading takes n clocks (SIPO loading 1011, rightmost bit first, from 0000: 1000, 1100, 0110, 1011). A **universal shift register** (74194) has a 4:1 MUX before each D: hold, shift right, shift left, parallel load. Shifting toward the MSB multiplies by 2.

**Answer.** The serial input is Q_{2} ⊕ Q_{3}, read before the edge:

| Clock | Q_{2} ⊕ Q_{3} before | Q_{0} Q_{1} Q_{2} Q_{3} after |
|---|---|---|
| start | | 0 1 1 0 |
| 1 | 1 ⊕ 0 = 1 | **1 0 1 1** |
| 2 | 1 ⊕ 1 = 0 | **0 1 0 1** |
| 3 | 0 ⊕ 1 = 1 | **1 0 1 0** |

XOR feedback like this makes a pseudo-random sequence generator (17).

:::check Check 1
(a) Continue for two more clocks. (b) A 4-bit SISO holds 0000; bits 1, 1, 0, 1 enter on clocks 1–4. On which clock does the first 1 reach the output? (c) Which type does a serial transmitter need?
:::

### 2 · Ring and Johnson counters

:::q <span class="tag">Deck 09 slides 16–23</span>
Draw a 4-bit Johnson counter. Give its count sequence and modulus, and compare it with a ring counter.
:::

:::guess Guess first
4 flip-flops have 16 states. How many does this counter visit?
:::

:::note Terms
**Modulus (MOD):** the number of states before the count repeats. **Shift-register counter:** a shift register fed back to its own input.
:::

[[fig:johnson4|Johnson counter: Q_{3}' fed back to D_{0}.|w=70]]

| clk | Q_{0} Q_{1} Q_{2} Q_{3} | Decode | clk | Q_{0} Q_{1} Q_{2} Q_{3} | Decode |
|---|---|---|---|---|---|
| 0 | 0 0 0 0 | Q_{0}'Q_{3}' | 4 | 1 1 1 1 | Q_{0}Q_{3} |
| 1 | 1 0 0 0 | Q_{0}Q_{1}' | 5 | 0 1 1 1 | Q_{0}'Q_{1} |
| 2 | 1 1 0 0 | Q_{1}Q_{2}' | 6 | 0 0 1 1 | Q_{1}'Q_{2} |
| 3 | 1 1 1 0 | Q_{2}Q_{3}' | 7 | 0 0 0 1 | Q_{2}'Q_{3} |

- **Ring:** Q_{3} straight back to D_{0}, preset to 1000: the single 1 circulates. n flip-flops → MOD-n; each Q is one state, no decoder.
- **Johnson (twisted ring):** Q_{3}' fed back: fills with 1s, then empties. n flip-flops → **MOD-2n**; each state decoded by one 2-input AND.
- **Lock-out:** Johnson uses 8 of 16 states; from an unused one (e.g. 0100) it cycles among the others for ever. Start with a reset, or add self-correcting logic.

[[fig:johnson_waves|Johnson outputs: square waves at f/8, each shifted one clock.|w=70]]

**Answer.** 8 states, **MOD-8**, sequence in the table. Ring: n states, no decoding. Johnson: 2n states, 2-input decoding. Both waste states against a binary counter (2^{n}).

:::check Check 2
(a) Flip-flops for MOD-10 as Johnson, ring and binary? (b) Decode term for state 0011? (c) A ring counter starts at 0000 by mistake. What happens?
:::

---

## Exam form

**Shift registers.** Circuit; the four types; trace table for a given input; universal register modes.

**Ring, Johnson.** Circuits; sequence tables; MOD-n vs MOD-2n; decoding; lock-out and the cure; comparison with binary.

## Traps

- Computing the feedback from the new values instead of the values before the edge.
- Johnson MOD = 2n, not n or 2^{n}.
- Forgetting that a ring counter must be preset to one 1.

## Self-test

1. Give the sequence and modulus of a 3-bit Johnson counter.
2. MOD of a 5-bit ring counter?
3. A PISO register holds 8 bits. How many clocks to send them after loading?
4. A 4-bit SISO register is clocked at 1 MHz. What delay does it give?
5. Decode term for Johnson state 1110 (Q_{0}Q_{1}Q_{2}Q_{3})?

<!--ANSWERS-->

## Answers

**Check 1.** (a) From 1010: 1 ⊕ 0 → **1101**; then 0 ⊕ 1 → **1110**. (b) **Clock 4**. (c) **PISO**.

**Check 2.** (a) **5, 10, 4**. (b) **Q_{1}'Q_{2}**. (c) It **stays at 0000**: nothing to circulate (its lock-out).

**Self-test.**

1. 000, 100, 110, 111, 011, 001: **MOD-6**.
2. **MOD-5**.
3. **8**.
4. 4 clocks = **4 μs**.
5. **Q_{2}Q_{3}'**.

<!--/ANSWERS-->
