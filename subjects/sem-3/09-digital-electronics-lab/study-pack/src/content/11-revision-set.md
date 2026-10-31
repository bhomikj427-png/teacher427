# 11 · Revision set: one question per idea

<div class="sub">Answer from memory on paper, then check. A miss points back to its chapter, shown in brackets.</div>

1. VCC and GND pins of: a 14-pin gate IC, a 16-pin MSI chip, the 7483, the 7473. *(00)*
2. What does a floating TTL input read as, and where do you tie unused AND and NOR inputs? *(00)*
3. Build OR from NANDs only, and AND from NORs only. Give the gate counts. *(Exp 1)*
4. Full adder S and C_{out}. Full subtractor D and B_{o}. *(Exp 2)*
5. How does one 7483 subtract, and what does C_{out} = 0 mean afterwards? *(Exp 2)*
6. BCD adder correction condition. *(Exp 2)*
7. Which form (SOP/POS) for NAND-only, and which for NOR-only? *(Exp 3)*
8. Binary → Gray equations; Gray → binary equations. *(Exp 4)*
9. Excess-3 of 6, and why XS-3 is self-complementing. *(Exp 4)*
10. 7485 cascade inputs for a single chip. *(Exp 5)*
11. Odd-parity generator for XYZ; what checker output 1 means. *(Exp 5)*
12. f = Σm(0,3,5,7,8,10,14) on an 8:1 MUX: the eight data inputs. *(Exp 6)*
13. 74138 as a 1:8 DEMUX: where does the data go? *(Exp 7)*
14. Why does the selected LED go dark on the NAND decoder? *(Exp 8)*
15. Race-around: cause and cure. *(Exp 9)*
16. 7474 and 7473: which edge, and which asynchronous inputs? *(Exp 10)*
17. D = ? to make a T flip-flop; S, R = ? to make a D from an SR. *(Exp 10)*
18. J and K for each stage of a 4-bit synchronous up counter. *(Exp 11)*
19. Ring vs Johnson: feedback, number of states, start state. *(Exp 11)*
20. Load 1011 serially: the register contents after each of the 4 clocks. *(Exp 12)*
21. Mealy vs Moore; what "overlapping" means for 1010. *(Exp 13)*
22. The 101 detector equations with D flip-flops. *(Exp 13)*
23. TTL NAND: the output stage's name, and why the diode is there. Noise margin. *(Exp 14)*

<!--ANSWERS-->

## Answers

1. 14-pin: VCC 14, GND 7. 16-pin: 16, 8. **7483: VCC 5, GND 12. 7473: VCC 4, GND 11.**
2. HIGH. Unused AND/NAND inputs → +5 V or a used input; unused OR/NOR inputs → GND.
3. OR = NAND(NAND(A,A), NAND(B,B)), 3 gates. AND = NOR(NOR(A,A), NOR(B,B)), 3 gates.
4. S = A ⊕ B ⊕ C_{in}, C_{out} = AB + BC_{in} + AC_{in}. D = A ⊕ B ⊕ B_{i}, B_{o} = A'B + (A ⊕ B)'B_{i}.
5. XOR each B bit with M = 1 and set C_{in} = M = 1, giving A + B' + 1. C_{out} = 0 means A < B; the result is in 2's complement.
6. K = C_{4} + S_{3}S_{2} + S_{3}S_{1}. When K = 1, add 0110.
7. NAND-only: SOP. NOR-only: POS.
8. G3 = B3, G_{i} = B_{i+1} ⊕ B_{i}. B3 = G3, B_{i} = B_{i+1} ⊕ G_{i}.
9. 6 + 3 = 9 = **1001**. Inverting XS-3(d) gives XS-3(9 − d).
10. I(A=B) = 1, I(A>B) = I(A<B) = 0.
11. P = (X ⊕ Y ⊕ Z)'. C = 1 means an even number of 1s arrived: an error.
12. Select ABC: I0 = D', I1 = D, I2 = D, I3 = D, I4 = D', I5 = D', I6 = 0, I7 = D'.
13. Into E1' (active LOW), with E2' = 0 and E3 = 1. The selected output follows D.
14. The outputs are active-LOW: the selected one goes to 0.
15. A level-triggered JK with J = K = 1 toggles repeatedly while CLK = 1. Cure: edge triggering or master-slave.
16. 7474: positive edge, PR' and CLR'. 7473: negative edge, CLR' only.
17. D = T ⊕ Q. S = D, R = D'.
18. J_{A} = K_{A} = 1; J_{B} = K_{B} = Q_{A}; J_{C} = K_{C} = Q_{A}Q_{B}; J_{D} = K_{D} = Q_{A}Q_{B}Q_{C}.
19. Ring: Q0 → D3, n states, must be preset to 1000. Johnson: Q0' → D3, 2n states, starts from 0000.
20. 1000, 1100, 0110, 1011.
21. Mealy: output depends on state and input. Moore: output depends on state only. Overlapping: after a match, go to the state for "10", not the start.
22. D_{1} = Q_{0}X', D_{0} = X, Z = Q_{1}X.
23. Totem pole. The diode keeps Q4 off when the output is LOW. Noise margin 0.4 V.

<!--/ANSWERS-->
