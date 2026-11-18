# 20 — Mock end-term paper

<div class="sub">Closed book, on paper, 3 hours · do it after the rest · then mark it with the key on the last pages and redo anything you missed</div>

No Digital Electronics end-term paper or blueprint has been seen, so the format is a guess. This paper copies the layout of the one official blueprint in hand (MAS2001, July–Nov 2026): Part A 10 × 2, Part B 6 × 6, Part C 2 × 8, Part D 1 × 8, total 80. Questions with a source tag are the professor's own and are not used earlier in the pack.

## Part A · 10 × 2 = 20 marks

1. State De Morgan's two theorems.
2. Convert F(A, B, C) = Σm(1, 3, 6) to product-of-maxterms form.
3. Why is the NAND gate called a universal gate?
4. How many select lines does a 16:1 MUX have? How many 4:1 MUXes build it as a tree?
5. Find the odd parity bit for 1101001.
6. Give two differences between a latch and a flip-flop.
7. How many flip-flops does a MOD-12 counter need, and how many states are unused?
8. Give two differences between Mealy and Moore machines.
9. V_{OH(min)} = 2.7 V, V_{IH(min)} = 2.0 V, V_{IL(max)} = 0.8 V, V_{OL(max)} = 0.5 V. Find the noise margins.
10. Differentiate PAL and PLA.

## Part B · 6 × 6 = 36 marks

11. <span class="tag">Set 1 Q4</span> Design a combinational circuit having 4 inputs that will produce an output '1' when two consecutive input bits are 1 and produce '0' for other cases.
12. <span class="tag">Set 1 Q6</span> Implement F(P, Q, R, S) = Σm(0, 2, 5, 9, 11, 12, 14, 15) using an 8:1 multiplexer.
13. <span class="tag">Set 1 Q8</span> Implement F(a, b, c, d) = Σm(0, 1, 2, 5, 6, 8, 9, 15) using a suitable decoder.
14. <span class="tag">Set 2 Q4</span> Design a 2-bit synchronous up counter with JK flip-flops: state table, excitation table, equations.
15. <span class="tag">Deck 12 slide 18</span> Reduce by partitioning (next/z for x = 0; for x = 1): A D/0, D/0 · B C/1, D/0 · C C/1, D/0 · D D/0, B/0 · E C/1, F/0 · F D/0, D/0 · G G/0, G/0 · H B/1, D/0.
16. Draw a two-input TTL NAND with totem-pole output and explain it. I_{OL} = 8 mA, I_{IL} = 0.4 mA, I_{OH} = 0.4 mA, I_{IH} = 20 μA: find the fan-out.

## Part C · 2 × 8 = 16 marks

17. <span class="tag">Deck 11 slide 43 Q1</span> Design a Moore circuit to detect 1011 (overlap allowed) with D flip-flops: state diagram, state table, input equations.
18. <span class="tag">Deck 15 slide 28</span> Realise with a PAL of three product terms per output: F_{1}(A, B, C, D) = Σm(1, 4–7, 10–13), F_{2} = Σm(4–7, 10–11), F_{3} = Σm(4–7, 9–15). Give the minimal expressions and the programming table.

## Part D · 1 × 8 = 8 marks

19. (a) Design a MOD-6 synchronous up counter (0–5) with JK flip-flops and check whether it is self-starting. (b) For an asynchronous MOD-6 instead: flip-flops, reset-gate inputs, and one disadvantage.

---

## Formula recall

Cover the right column, write each line from the cue, then uncover. Any row you miss, go back to the file named.

| Cue | Recall |
|---|---|
| 01 Laws | X + X'Y = X + Y · X + YZ = (X + Y)(X + Z) · De Morgan · consensus XY + X'Z + YZ = XY + X'Z |
| 01 Canonical | Σm = 1-rows, ΠM = 0-rows · M_{j} = m_{j}' |
| 02 K-map | groups 1, 2, 4, 8; wrap; largest, fewest; X only to enlarge · POS: group 0s, read inverted |
| 03 Universal | SOP → NAND–NAND · POS → NOR–NOR · XOR = 4 NAND |
| 04 Adders | S = A ⊕ B ⊕ C_{in}, C_{out} = AB + C_{in}(A ⊕ B) · C_{i+1} = G_{i} + P_{i}C_{i} · ripple (2n + 1)T · BCD: + 0110 if K + Z_{3}Z_{2} + Z_{3}Z_{1} |
| 05 MUX | n variables on 2^{n−1}:1: inputs 0, 1, x, x' per row pair |
| 06 Decoder, encoder | output j = m_{j}; OR (NAND if active-low) · x = D_{2} + D_{3}, y = D_{3} + D_{1}D_{2}', V = D_{0} + D_{1} + D_{2} + D_{3} |
| 07 Display, comparator, parity | common anode lit by 0 · x_{i} = A_{i} ⊙ B_{i}, G = A_{1}B_{1}' + x_{1}A_{0}B_{0}' · P_{even} = XOR of data, checker E = XOR of data and P |
| 08 Shifts, ALU | arithmetic right copies sign · MUX gives Y = B, 0000, 1111, B' for S C_{in} = 00, 01, 10, 11; F = A + Y + C_{in} |
| 09 Flip-flops | Q⁺ = JQ' + K'Q · Q⁺ = D · Q⁺ = T ⊕ Q · excitation table |
| 11 Registers, shift counters | SIPO/SISO: n clocks for n bits · 74194 S_{1}S_{0} = 00 hold, 01 right, 10 left, 11 load · ring MOD-n · Johnson MOD-2n, 2-input decode |
| 12 Ripple | n·t_{pd} · clear at first unwanted state |
| 13 Synchronous | six steps; T = Q ⊕ Q⁺; unused states → self-start check |
| 14 Timing | T ≥ t_{pd} + t_{comb,max} + t_{su} · t_{pd} + t_{comb,min} ≥ t_{h} · skew δ (capture late): − δ on setup, + δ on hold |
| 15, 16 FSM | Moore output in circle, Mealy on arrow · partition by outputs, then by next-state blocks |
| 17 Timing, generators, async | register decoded outputs · 2-flip-flop synchronizer · LFSR 2^{n} − 1, all-zeros lock-out · MOD-N/2 + T flip-flop for 50 % · 555 f = 1.44/((R_{1} + 2R_{2})C), duty (R_{1} + R_{2})/(R_{1} + 2R_{2}), T = 1.1RC · ring f = 1/(2Nt_{pd}), N odd · one-bit state codes · every adjacent pair of 1s in one group |
| 18 Families | t_{pd} = larger of t_{PLH}, t_{PHL} (50 % points) · t_{r}, t_{f}: 10–90 % · NM_{H} = V_{OH} − V_{IH}, NM_{L} = V_{IL} − V_{OL} · fan-out = min(I_{OL}/I_{IL}, I_{OH}/I_{IH}) · P = CV^{2}f · PDP = t_{pd} × P |
| 19 Memory, PLD | 2^{k} × m: k address, m data lines · chips = (words ÷ words per chip) × (bits ÷ bits per chip) · PROM fixed AND · PAL fixed OR (feed an output back) · PLA both programmable (minimise F and F', share) |

<!--ANSWERS-->

## Key

**Part A.**

1. (X + Y)' = X'Y' and (XY)' = X' + Y'. (01)
2. **ΠM(0, 2, 4, 5, 7)**. (01)
3. NOT, AND and OR can each be built from NANDs alone, so any function can. (03)
4. **4** select lines; **five** 4:1 MUXes. (05 steps 2, 7)
5. Four 1s (even): odd parity bit **1**. (07 step 9)
6. Latch: level-triggered, transparent while enabled, passes glitches. Flip-flop: edge-triggered, samples once per clock. (09)
7. **4** flip-flops; **4** unused states. (12)
8. Mealy: output from state and input, on arrows, fewer states. Moore: from state only, in circles, one more state (any two). (15)
9. NM_{H} = **0.7 V**, NM_{L} = **0.3 V**. (18 step 4)
10. PAL: programmable AND, fixed OR, no sharing. PLA: both programmable, terms shared. (19 steps 5, 12)

**Part B.**

11. F = 1 for minterms 3, 6, 7, 11, 12, 13, 14, 15. K-map: three quads, **F = AB + BC + CD**: three 2-input ANDs and a 3-input OR (or NAND–NAND).
12. P, Q, R on the selects. I_{0} = **S'**, I_{1} = **S'**, I_{2} = **S**, I_{3} = **0**, I_{4} = **S**, I_{5} = **S**, I_{6} = **S'**, I_{7} = **1**. (05 step 5, Check 5)
13. A 4:16 decoder (two 3:8s, a enabling one directly and the other through an inverter); **OR outputs 0, 1, 2, 5, 6, 8, 9, 15** (8-input NAND if active-low). (06 steps 4, 8)
14. 00 → 01 → 10 → 11 → 00. Excitation (J_{1}K_{1}, J_{0}K_{0}): 00: 0X, 1X · 01: 1X, X1 · 10: X0, 1X · 11: X1, X1. **J_{0} = K_{0} = 1, J_{1} = K_{1} = Q_{0}**. (13)
15. P_{1}: (ADFG)(BCEH). P_{2}: on x = 1, D → B (other block): D separates → (AFG)(BCEH)(D). P_{3}: A, F → D but G → G: G separates; on x = 1, E → F but B, C, H → D: E separates → (AF)(BCH)(D)(E)(G). P_{4} = P_{3}. **A ≡ F, B ≡ C ≡ H**: 8 states become 5. (16)
16. Circuit and operation: 18 steps 9–10. Fan-out: 8/0.4 = 20 and 400/20 = 20: **20**.

**Part C.**

17. S0 nothing, S1 "1", S2 "10", S3 "101", S4 "1011" (z = 1). Next (x = 0, x = 1): S0 → S0, S1 · S1 → S2, S1 · S2 → S0, S3 · S3 → S2, S4 · S4 → S2, S1. Codes Y_{2}Y_{1}Y_{0}: 000, 001, 010, 011, 100; 101–111 don't-care. **D_{2} = Y_{1}Y_{0}X · D_{1} = Y_{0}X' + Y_{1}Y_{0}'X + Y_{2}X' · D_{0} = Y_{1}'X + Y_{0}'X · z = Y_{2}**. (15)
18. **F_{1} = A'B + BC' + AB'C + A'C'D** (four terms), **F_{2} = A'B + AB'C**, **F_{3} = B + AC + AD**. F_{1} does not fit in three terms, but two of its terms are F_{2}: feed F_{2} back, **F_{1} = F_{2} + BC' + A'C'D**. Table (A B C D F_{2}; 1 = true, 0 = complement, – = none): F_{2}: A'B = 0 1 – – –; AB'C = 1 0 1 – –. F_{1}: F_{2} = – – – – 1; BC' = – 1 0 – –; A'C'D = 0 – 0 1 –. F_{3}: B = – 1 – – –; AC = 1 – 1 – –; AD = 1 – – 1 –. (19 step 9)

**Part D.**

19. (a) 3 flip-flops; 6, 7 don't-care. **J_{0} = K_{0} = 1 · J_{1} = Q_{2}'Q_{0}, K_{1} = Q_{0} · J_{2} = Q_{1}Q_{0}, K_{2} = Q_{0}**. Self-start: 110 → 111 (only FF0 toggles); 111 → 000. Both return: **self-starting**. (13) (b) 3 flip-flops; clear at 110: **Q_{2}, Q_{1}** into the NAND. Disadvantage: ripple delay up to 3t_{pd} and false states (a brief 110) on the outputs. (12)

<!--/ANSWERS-->
