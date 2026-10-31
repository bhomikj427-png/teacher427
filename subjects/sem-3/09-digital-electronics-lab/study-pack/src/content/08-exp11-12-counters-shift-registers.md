# Exps 11–12 · Synchronous counter (7473), ring and Johnson counters, shift registers (7474)

<div class="sub">Manual pp. 9–14 (second numbering) · ICs 7473 ×2, 7408, 7474 ×2, 7400 · every sequence below was simulated clock by clock</div>

[[map:9–10 Flip-flops > 11 Counters > 12 Shift registers > 13 FSM|here=2]]

:::q <span class="tag">Manual Exp 11, aim</span>
Design and test a 4-bit synchronous up counter using the 7473, and test ring and Johnson counters. Viva form: "Derive J and K for each flip-flop of the synchronous counter, and say why the ring counter needs a preset."
:::

:::guess Guess first
In a binary count, when does bit QC toggle?
:::

## 4-bit synchronous up counter

From the JK excitation table (0→0: 0x, 0→1: 1x, 1→0: x1, 1→1: x0), the manual's state table reduces to:

$$J_{A} = K_{A} = 1    J_{B} = K_{B} = Q_{A}    J_{C} = K_{C} = Q_{A}Q_{B}    J_{D} = K_{D} = Q_{A}Q_{B}Q_{C}$$

So each bit toggles exactly when all lower bits are 1. All clocks are common: that is what makes it **synchronous**.

| Flip-flop | Pins (7473: FF1 = J 14, K 3, CLK 1, CLR' 2, Q 12; FF2 = J 7, K 10, CLK 5, CLR' 6, Q 9) |
|---|---|
| A = 7473 #1 FF1 | J 14, K 3 → +5 V; **QA = 12** |
| B = 7473 #1 FF2 | J 7, K 10 ← QA; **QB = 9** |
| C = 7473 #2 FF1 | J 14, K 3 ← 7408-3 (QA → 1, QB → 2); **QC = 12** |
| D = 7473 #2 FF2 | J 7, K 10 ← 7408-6 (7408-3 → 4, QC → 5); **QD = 9** |
| all four | CLK (pins 1, 5 on both ICs) ← clock; CLR' (pins 2, 6) ← clear switch; **VCC pin 4, GND pin 11** |

**Procedure:**

1. Clear: CLR' = 0, then 1. The count shows DCBA = 0000.
2. Apply clock pulses. The 7473 changes on the **falling** edge.
3. The count goes 0000 → 0001 → … → 1111, and on the 16th pulse back to **0000**.

[[fig:counter_timing|Expected waveforms: QA toggles every falling edge, QB every 2nd, QC every 4th, QD every 8th (divide-by-2, 4, 8, 16).|w=100]]

## Ring and Johnson counters (two 7474s)

Name the four flip-flops Q3, Q2, Q1, Q0: IC1 FF1, IC1 FF2, IC2 FF1, IC2 FF2.

7474 pins: FF1 = CLR' 1, D 2, CLK 3, PR' 4, Q 5, Q' 6; FF2 = Q' 8, Q 9, PR' 10, CLK 11, D 12, CLR' 13.

| | Ring counter | Johnson (twisted-ring) counter |
|---|---|---|
| shift chain | Q3 (IC1-5) → D (IC1-12); Q2 (IC1-9) → IC2-2; Q1 (IC2-5) → IC2-12 | same |
| feedback | **Q0 (IC2-9) → D3 (IC1-2)** | **Q0' (IC2-8) → D3 (IC1-2)** |
| clear line goes to | **PR' of Q3 (IC1-4)** and CLR' of Q2, Q1, Q0 (IC1-13, IC2-1, IC2-13) | CLR' of all four (IC1-1, IC1-13, IC2-1, IC2-13) |
| tie HIGH | CLR' of Q3 (IC1-1), unused PR's | all PR's |
| start state | 1000 | 0000 |
| sequence | 1000 → 0100 → 0010 → 0001 → 1000 | 0000 → 1000 → 1100 → 1110 → 1111 → 0111 → 0011 → 0001 → 0000 |
| states (n FFs) | n = 4 | 2n = 8 |

:::trap Trap: a ring counter cleared to 0000
The manual clears all four flip-flops. A ring counter at 0000 just circulates zeros forever. One flip-flop must be **preset** to 1, so the clear line goes to Q3's PR' instead of its CLR'. The Johnson counter starts fine from 0000.
:::

## Exp 12 · Shift registers (7474 ×2)

**SISO / SIPO (Fig 12.2):**

- Same chain as the ring counter, without feedback. Serial in → D3 (IC1-2); serial out = Q0 (IC2-9).
- All CLR' go to the clear line; all PR' are tied HIGH.

Enter 1, 1, 0, 1 (one bit per clock):

| After clock | serial in | Q3 Q2 Q1 Q0 |
|---|---|---|
| 1 | 1 | 1 0 0 0 |
| 2 | 1 | 1 1 0 0 |
| 3 | 0 | 0 1 1 0 |
| 4 | 1 | **1 0 1 1** (parallel out = 1011, the word entered) |
| 5 | 0 | 0 1 0 1 |
| 6 | 0 | 0 0 1 0 |
| 7 | 0 | 0 0 0 1 |

Serial out (Q0) after clocks 4, 5, 6, 7 = **1, 1, 0, 1**: the first bit in comes out first.

**PISO / PIPO (Fig 12.3):** parallel load through the **preset** inputs.

- Each PR' is driven by NAND(PE, data bit) on a 7400:
  - PE → 1, D → 2 → 3 → IC1-4;
  - PE → 4, C → 5 → 6 → IC1-10;
  - PE → 9, B → 10 → 8 → IC2-4;
  - PE → 12, A → 13 → 11 → IC2-10.
- Parallel outputs go through a 7408 (each Q AND output-enable).

**Procedure:**

1. Clear (CLR = 0, PE = 0), then set CLR = 1.
2. Set D C B A on the switches.
3. PE = 1 presets the 1-bits, so the register holds DCBA. Then set PE = 0.
4. **PIPO:** output enable = 1, read W X Y Z.
5. **PISO:** clock with serial in = 0. The bits leave at Q0 one per clock.

:::write Write in your record
**Result:** the 4-bit synchronous counter counted 0000–1111 and returned to 0000 on the 16th pulse. The ring counter (preset 1000) cycled through 4 states and the Johnson counter through 8. SISO/SIPO: 1011 entered serially, read in parallel after 4 clocks and serially after 4–7 clocks. PISO/PIPO: parallel data loaded through preset and read out in parallel and serially.

**Theory for the record:** in a synchronous counter all flip-flops share the clock, and logic on J/K decides which toggle: each bit toggles when all lower bits are 1 (J = K = product of the lower Q's). This avoids the cumulative delay of ripple counters. A ring counter circulates a single 1 (n states, must be preset). A Johnson counter feeds back Q' (2n states). Shift registers move data one position per clock: SISO, SIPO, PISO and PIPO, according to how data enters and leaves.
:::

:::check Check 1
(a) Why is J_{D} = K_{D} = Q_{A}Q_{B}Q_{C}? (b) How many flip-flops does a mod-10 Johnson counter need? (c) After loading 1011 into the SIPO register, how many clocks until the register reads 0000?
:::

<!--ANSWERS-->

## Answers

**Opening question.** QC toggles whenever QA = QB = 1, i.e. after every 4th count. So J_{C} = K_{C} = Q_{A}Q_{B}. The ring counter needs a preset because a cleared ring (0000) has no 1 to circulate.

**Check 1.** (a) In binary counting, a bit flips exactly when every lower bit is 1 (…0111 → …1000). So D toggles only when A, B and C are all 1. (b) 2n = 10, so **5**. (c) Four more clocks with serial in = 0 (it reads 0000 after clock 8).

<!--/ANSWERS-->
