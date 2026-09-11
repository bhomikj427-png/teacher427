# 09 — Drill Set

The real paper and the real practice set. **Work these under time before you read any solution.**

Sources: `../exam-pack/PYQ-MTE-2025-09-25.pdf` and
`../exam-pack/practice-set-01-combinational.png`.

---

## Drill A — the 2025 MTE, timed

**Set a timer for 90 minutes. 30 marks. Closed book. Write full answers, including every circuit
diagram.**

Reproduced from the paper. Q7 depends on a waveform figure printed in the original — open the PDF
for that one, or substitute the variant supplied below it.

---

### SECTION A — Memory Based Questions (3 × 2 = 6 marks)

**A1.** Optimize the following expression and implement using 2-input NOR gate. **(2)**

```
  F = P'Q' + P'
```

**A2.** The four-bit binary sequence `1011` is applied to an even parity generator circuit. What
will be the output? **(2)**

**A3.** What excitation input should be applied to a T-FF to make output toggle? **(2)**

---

### SECTION B — Concept Based Questions (4 × 4 = 16 marks)

**B4.** Minimize the following Boolean function using K-Map method to obtain a simplified
expression. Also draw the logic circuit using basic gates. **(4)**

```
  F(a,b,c,d) = Sigma-m(0, 4, 5, 7, 8, 9, 15) + d(1, 3, 6, 14)
```

**B5.** Implement the following function using single 8:1 Multiplexer. **(4)**

```
  F(P,Q,R,S) = Sigma-m(0, 1, 3, 4, 8, 9, 10, 11, 13, 15)
```

**B6.** Design Full Adder using suitable decoder. **(4)**

**B7.** Draw the output waveform for the following input waveform, assuming the flip-flop to be
positive edge triggered and the output Q is initially at logic zero. **(4)**

*(Figure in the original paper. Substitute drill: a **JK** flip-flop, positive edge triggered,
Q initially 0, clocked six times, with inputs at the six rising edges:*

```
  edge:   1     2     3     4     5     6
  J:      1     0     1     1     0     1
  K:      0     0     1     1     1     1
```

*Draw the Q waveform and state Q after each edge.)*

---

### SECTION C — Analytical Based Questions (1 × 8 = 8 marks)

**C8.** Design a synchronous counter that counts clock pulses from 0-7 using negative edge
triggered T flipflop. **(8)**

---

## Drill B — practice set 1 (combinational)

Ten questions, all from the professor's practice sheet. **Untimed, but write full solutions.**

**P1.** Minimize using K-Map and implement the circuit using universal gate.

```
  F(v,w,x,y,z) = Sigma-m(0,2,5,8,10,13,15,17,19,21,26,28,29,30,31) + d(7,12,14,23,24)
```

**P2.** Minimize using K-Map and realize using NAND gates only.

```
  F(w,x,y,z) = Sigma-m(0,1,3,5,7,10,11) + d(2,6,13)
```

**P3.** Implement using 8:1 Multiplexer.

```
  F(a,b,c,d) = Sigma-m(0,1,3,5,7,9,15)
```

**P4.** Design a combinational circuit having 4 inputs that will produce an output `1` when two
consecutive input bits are 1, and `0` for other cases.

**P5.** Design a combinational circuit to implement the following Boolean function using only a
4:1 Multiplexer. Take `D` as input variable.

```
  F(A,B,C,D) = Sigma-m(0,2,7,8,9,11,13,14,15)
```

**P6.** Implement using 8:1 Multiplexer.

```
  F(P,Q,R,S) = Sigma-m(0,2,5,9,11,12,14,15)
```

**P7.** Realize the Boolean function `Y = Pi-M(0,3,5,6,7)` with a Decoder and one NOR gate.

**P8.** Implement the following function using suitable decoder.

```
  F(a,b,c,d) = Sigma-m(0,1,2,5,6,8,9,15)
```

**P9.** Draw the logic diagram of a 4-bit odd/even parity generator.

**P10.** Design a BCD to 7-segment decoder circuit for a common anode display.

---

## Exam-day tactics

**Read the whole paper first — 3 minutes.** Section C is the biggest single block; know what it is
asking before you spend 20 minutes elsewhere.

**Budget by marks, not by question order.**

```
  Section A   3 questions x 2 marks   ->   about 6 minutes total
  Section B   4 questions x 4 marks   ->   about 12 minutes each
  Section C   1 question x 8 marks    ->   about 24 minutes
  Reserve     for checking            ->   about 10 minutes
```

**Section A questions are one-liners.** If one takes more than three minutes you have misread it —
`F = P'Q' + P'` is an absorption, not a K-map.

**Always draw the circuit when asked.** "Also draw the logic circuit", "implement", "realize",
"design" — each is a diagram mark. An expression alone is a partial answer.

**State your assumptions.** Active-high or active-low decoder outputs; gate fan-in; common anode or
cathode. A stated assumption is accepted; a silent one is marked wrong when it differs from the
examiner's.

**Verify by substitution.** One minterm and one non-minterm through your final expression catches
most K-map errors in under a minute.

**In Section C, write the trace.** Walking the counter through its full sequence proves the design.
It is the cheapest mark on the paper.

---
---
---

## Answers — Drill A

**A1.** Absorption: `F = P'(Q' + 1) = P'`. Implement as `F = NOR(P, P)` — **one 2-input NOR** with
both inputs tied to P. Full working: file `01`, worked example 1, and file `02`.

**A2.** `1011` has **three** 1s, an odd count, so the even-parity bit is **1**:
`P = 1 (+) 0 (+) 1 (+) 1 = 1`. The transmitted word `10111` then has four 1s. Full working: file
`03`.

**A3.** `T = 1`. From `Q+ = T (+) Q`, setting `T = 1` gives `Q+ = Q'`. General rule:
`T = Q (+) Q+`. Full working: file `07`.

**B4.**

```
  F = b'c' + bc + a'b          (or  b'c' + bc + a'c'  -- both minimal, 6 literals)
```

Groups: `b'c'` (m0, m1X, m8, m9) and `bc` (m6X, m7, m14X, m15) are essential; m4 and m5 need one
more term. Full K-map, essential-group reasoning and the gate diagram: file `01`, worked example 2.

**B5.** Selects `P, Q, R`; data variable `S`.

```
  D0 = 1     D1 = S     D2 = S'    D3 = 0
  D4 = 1     D5 = 1     D6 = S     D7 = S
```

Full pairing table and diagram: file `04`, worked example 1.

**B6.** 3-to-8 decoder with inputs `A, B, Cin`, two OR gates:

```
  Sum  = D1 + D2 + D4 + D7        (Sum  = Sigma-m(1,2,4,7))
  Cout = D3 + D5 + D6 + D7        (Cout = Sigma-m(3,5,6,7))
```

`D7` feeds both gates. With active-low decoder outputs use NAND gates instead. Full diagram:
file `05`, worked example 1.

**B7 (substitute drill).** JK flip-flop, positive edge, Q starts at 0:

```
  edge 1:  J=1 K=0  -> SET     -> Q = 1
  edge 2:  J=0 K=0  -> HOLD    -> Q = 1
  edge 3:  J=1 K=1  -> TOGGLE  -> Q = 0
  edge 4:  J=1 K=1  -> TOGGLE  -> Q = 1
  edge 5:  J=0 K=1  -> RESET   -> Q = 0
  edge 6:  J=1 K=1  -> TOGGLE  -> Q = 1
```

```
  CLK   _|‾|_|‾|_|‾|_|‾|_|‾|_|‾|_
         1   2   3   4   5   6
  Q     ___|‾‾‾‾‾‾‾|___|‾‾‾|___|‾‾
```

Q changes **only at rising edges** and holds flat between them. Method: file `07`.

**C8.** Three T flip-flops, all on the same clock, negative edge:

```
  T0 = 1
  T1 = Q0
  T2 = Q1·Q0
```

State table, K-maps, circuit diagram and the full eight-state verification trace: file `08`,
worked example 1.

---

## Answers — Drill B

**P1.**

```
  F = x·z  +  w·z'  +  v·w'·z  +  v'·x'·z'
```

Two groups of 8 span both halves of the 5-variable map (`xz` and `wz'`); two groups of 4 stay on one
half (`vw'z`, `v'x'z'`). The group `wx` is legal but **entirely redundant** — that is the difficulty
of this question. Full derivation: file `01`, self-test 6. NAND realization (9 gates): file `02`,
worked example 3.

**P2.**

```
  F = w'x' + w'z + x'y
```

NAND realization, **6 gates** (2 inverters, 3 product NANDs, 1 collector). Full working: file `01`
self-test 3, file `02` self-test 3.

**P3.** Selects `a, b, c`; data variable `d`.

```
  D0 = 1    D1 = d    D2 = d    D3 = d
  D4 = d    D5 = 0    D6 = 0    D7 = d
```

File `04`, self-test 1.

**P4.** Inputs `A B C D` in order; consecutive pairs are `(A,B)`, `(B,C)`, `(C,D)`.

```
  F = A·B + B·C + C·D          = Sigma-m(3,6,7,11,12,13,14,15)
```

K-map confirmation (rows `AB`, columns `CD`):

```
          CD=00   01    11    10
  AB=00 |   0  |  0  |  1  |  0  |
  AB=01 |   0  |  0  |  1  |  1  |
  AB=11 |   1  |  1  |  1  |  1  |
  AB=10 |   0  |  0  |  1  |  0  |
```

Three groups of four: the `AB=11` row (`AB`), the `CD=11` column (`CD`), and m6/m7/m14/m15 (`BC`).
All three are essential — m12 sits only in `AB`, m3 only in `CD`, m6 only in `BC`. So the
by-inspection answer is already minimal. Circuit: three 2-input ANDs into one 3-input OR.

**P5.** 4:1 MUX with `A, B` as selects; `C` and `D` both left over.

```
  I0 = D'          I1 = C·D          I2 = C' + D          I3 = C + D
```

Extra gates required: one AND, two ORs, two inverters. Full block-of-four derivation: file `04`,
worked example 2.

**P6.** Selects `P, Q, R`; data variable `S`.

```
  D0 = S'   D1 = S'   D2 = S    D3 = 0
  D4 = S    D5 = S    D6 = S'   D7 = 1
```

File `04`, self-test 2.

**P7.** `Pi-M(0,3,5,6,7)` means Y is **0** at those five indices.

```
  Y = ( D0 + D3 + D5 + D6 + D7 )'
```

One 3-to-8 decoder, one 5-input NOR wired to the **maxterm** lines. Do not convert to Σm and use an
OR — the NOR takes the maxterm lines directly. File `05`, worked example 2.

**P8.** Four variables -> 4-to-16 decoder, active-high outputs, one 8-input OR:

```
  F = D0 + D1 + D2 + D5 + D6 + D8 + D9 + D15
```

With active-low outputs, use an 8-input NAND. File `05`, self-test 1.

**P9.**

```
  Even parity generator:  P = A (+) B (+) C (+) D
  Odd parity generator:   P = ( A (+) B (+) C (+) D )'
```

Three XOR gates in a tree; for odd parity the final stage is an XNOR (or add one inverter).

```
   A --+
       |XOR|--+
   B --+      |XOR|--+
   C --+      |      |XOR|--- P_even     (XNOR here for P_odd)
       |XOR|--+      |
   D --+             |
```

The even-parity output is 1 when the data has an **odd** number of 1s. File `03`.

**P10.** BCD to 7-segment, **common anode = active low**, so complement the standard active-high
equations. Active-high (common cathode) forms, minimized with the six don't-cares 1010-1111:

```
  a = A + C + B·D + B'·D'
  b = B' + C·D + C'·D'
  c = B + C' + D
  d = A + B'·D' + C·D' + B'·C + B·C'·D
  e = B'·D' + C·D'
  f = A + C'·D' + B·C' + B·D'
  g = A + B·C' + B'·C + C·D'
```

For the **common anode** display, every driver output is the complement:

```
  a_drive = ( A + C + B·D + B'·D' )'
  c_drive = ( B + C' + D )'          =  B'·C·D'
  e_drive = ( B'·D' + C·D' )'        =  B·C' + D
```

and likewise for `b`, `d`, `f`, `g`. **State the convention in your answer** — common anode sinks
current, so a segment lights when its driver is pulled **low**. Worked checks for `c` and `e`:
file `05`, self-test 5.
