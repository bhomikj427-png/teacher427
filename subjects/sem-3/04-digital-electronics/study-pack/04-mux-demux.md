# 04 — Multiplexers and Demultiplexers

The single highest-value topic on the MTE. It appeared as a 4-mark question on the paper and three
more times in the practice set.

---

## Map

```
   MUX = many inputs -> one output, chosen by select lines
        |
        +--> 2ⁿ : 1 MUX has n select lines
        |
        +--> USE 1: data routing
        +--> USE 2: implement any Boolean function   <-- this is what gets examined
                      |
                      +--> exact fit:  n vars on a 2⁽ⁿ⁻¹⁾:1 MUX, last var as data
                      +--> undersized: n vars on a smaller MUX, data = f(leftovers)
                      +--> cascading:  build a big MUX from small ones

   DEMUX = one input -> many outputs (a decoder with an enable)
```

---

## Attempt first

1. How many select lines does a 16:1 MUX have? How many data inputs does a MUX with 5 select lines
   have?
2. Write the output equation of a 4:1 MUX in terms of `S1, S0, I0..I3`.
3. You must implement a 4-variable function on an 8:1 MUX. Which variables become selects, and what
   are the four possible values a data input can take?
4. `F(P,Q,R,S) = Σm(0,1,3,4,8,9,10,11,13,15)` on one 8:1 MUX. Give `D0` through `D7`.
5. What changes if you are given only a **4:1** MUX for a 4-variable function?

---

## Method

### Structure

A `2ⁿ : 1` MUX has **n select lines** and `2ⁿ` data inputs. The select word is a binary number
that picks one data input and copies it to the output.

4:1 MUX:

```
   I0 --|\
   I1 --| \
   I2 --| / --- Y
   I3 --|/
         ||
        S1 S0
```

```
  Y = S1'·S0'·I0 + S1'·S0·I1 + S1·S0'·I2 + S1·S0·I3
```

**That equation is the key to everything below.** Read it as: the MUX is a hardware sum of minterms
of the select variables, with each minterm weighted by its data input.

### Implementing a function — the exact-fit method

To put an **n-variable** function on a **2⁽ⁿ⁻¹⁾ : 1** MUX:

1. Use the **n-1 most significant variables as the select lines**, in order.
2. The **least significant variable** becomes the data variable.
3. Write the truth table in **consecutive pairs of minterms**. Each pair shares one select value.
4. For each pair, compare the two output values and read off the data input:

| F at even minterm (last var = 0) | F at odd minterm (last var = 1) | Data input |
|---|---|---|
| 0 | 0 | `0` |
| 0 | 1 | `D` (the last variable) |
| 1 | 0 | `D'` |
| 1 | 1 | `1` |

That four-row table is the entire method. **Only four values are ever possible: 0, 1, D, D'.**

Practical shortcut: list the minterm indices in rows of two.

```
  select 000  ->  m0, m1
  select 001  ->  m2, m3
  select 010  ->  m4, m5
  select 011  ->  m6, m7
  select 100  ->  m8, m9
  select 101  ->  m10, m11
  select 110  ->  m12, m13
  select 111  ->  m14, m15
```

Tick the minterms present in F, then read each row against the table above.

### The undersized MUX

When the MUX is smaller than the exact fit — a **4:1 for a 4-variable function** — two variables
become selects and **two** are left over. Each data input is then a function of those two leftovers,
built with a few extra gates.

Method: group the truth table in **blocks of four** (one block per select value), and express each
block as a function of the two remaining variables.

Possible data-input values are now any function of two variables: `0`, `1`, `C`, `C'`, `D`, `D'`,
`CD`, `C+D`, `C ⊕ D`, `C'+D`, and so on.

### Cascading

Build a bigger MUX from smaller ones. An 8:1 from two 4:1 plus one 2:1:

```
   I0..I3 --> [4:1 A] --+
                        +--> [2:1] --- Y
   I4..I7 --> [4:1 B] --+
                  ||         |
                 S1 S0       S2
```

The low select bits drive the small MUXes; the high bit picks between their outputs.
Alternatively use the **enable** pins: drive enables from the MSB and OR the outputs.

### Demultiplexer

One input, `2ⁿ` outputs, n selects. The data goes to the selected output; the rest sit at 0.

```
  Y_i = D  when select = i,  else 0
```

**A demux and a decoder are the same circuit.** A decoder with an enable input *is* a demux: feed
data into the enable, and the decoder outputs become the demux outputs. Examiners ask for this
equivalence.

---

## Worked — MTE 2025 Q5 (4 marks)

> Implement the following function using a single 8:1 Multiplexer.
> `F(P,Q,R,S) = Σm(0, 1, 3, 4, 8, 9, 10, 11, 13, 15)`

**Step 1 — assign.** 8:1 MUX has 3 selects. Four variables, so:

```
  Selects: S2 = P,  S1 = Q,  S0 = R          Data variable: S
```

**Step 2 — pair the minterms.** Present minterms: 0, 1, 3, 4, 8, 9, 10, 11, 13, 15.

| PQR | minterm pair | F at each | Data input |
|---|---|---|---|
| 000 | m0, m1 | 1, 1 | `D0 = 1` |
| 001 | m2, m3 | 0, 1 | `D1 = S` |
| 010 | m4, m5 | 1, 0 | `D2 = S'` |
| 011 | m6, m7 | 0, 0 | `D3 = 0` |
| 100 | m8, m9 | 1, 1 | `D4 = 1` |
| 101 | m10, m11 | 1, 1 | `D5 = 1` |
| 110 | m12, m13 | 0, 1 | `D6 = S` |
| 111 | m14, m15 | 0, 1 | `D7 = S` |

**Step 3 — draw.**

```
        1  --|D0\
        S  --|D1 \
        S' --|D2  \
        0  --|D3   |--- F
        1  --|D4  /
        1  --|D5 /
        S  --|D6/
        S  --|D7
              |||
              P Q R
```

One 8:1 MUX plus one inverter for `S'`. **Answer: D0 = 1, D1 = S, D2 = S', D3 = 0, D4 = 1,
D5 = 1, D6 = S, D7 = S.**

**Check one row.** m10 means PQRS = 1010, so select PQR = 101 picks `D5 = 1` -> F = 1. And 10 is in
the minterm list. Correct.

---

## Worked — practice Q5: the undersized 4:1

> Implement `F(A,B,C,D) = Σm(0,2,7,8,9,11,13,14,15)` using **only a 4:1 Multiplexer**.

Two selects, so `A` and `B` become selects and **both C and D are left over**.

**Group in blocks of four:**

| AB | block | minterms present | F as a function of C, D |
|---|---|---|---|
| 00 | m0..m3 | 0, 2 | CD = 00 -> 1, 01 -> 0, 10 -> 1, 11 -> 0 |
| 01 | m4..m7 | 7 | only CD = 11 -> 1 |
| 10 | m8..m11 | 8, 9, 11 | CD = 00,01,11 -> 1; 10 -> 0 |
| 11 | m12..m15 | 13, 14, 15 | CD = 01,10,11 -> 1; 00 -> 0 |

Read each block:

```
  I0 = D'            (1 when D = 0, regardless of C)
  I1 = C·D
  I2 = C' + D
  I3 = C + D
```

```
        D'      --|I0\
        C·D     --|I1 \ --- F
        C' + D  --|I2 /
        C + D   --|I3/
                    ||
                   A  B
```

One 4:1 MUX plus one AND, two ORs and two inverters. **The extra gates are expected** — an
undersized MUX cannot avoid them.

**Check.** m14 = 1110: AB = 11 selects `I3 = C + D` with CD = 10, giving 1. And 14 is a minterm.
Correct. m12 = 1100: AB = 11 selects `I3 = C + D` with CD = 00, giving 0. And 12 is absent. Correct.

---

## Traps

**Variable order.** The MSB of the function must be the MSB select. Swapping `P` and `R` produces a
different, wrong assignment. Write the order down before you start.

**Only four values on an exact fit.** If you find yourself writing `D0 = PQ`, you have mis-assigned
something. On an exact fit, every data input is `0`, `1`, `D` or `D'`.

**`D` versus `D'` inverted.** `F = 0` at the even minterm and `1` at the odd one means `D`, not
`D'`. The even minterm has the data variable at 0.

**Missing minterms count too.** A pair with neither minterm present is `0` — write it, do not leave
the pin blank.

**Draw the MUX.** A table of data inputs with no diagram is a partial answer.

---

## Self-test

1. Implement `F(a,b,c,d) = Σm(0,1,3,5,7,9,15)` on an 8:1 MUX.
2. Implement `F(P,Q,R,S) = Σm(0,2,5,9,11,12,14,15)` on an 8:1 MUX.
3. Implement `F(a,b,c) = Σm(1,3,5,6)` on a 4:1 MUX with `a`, `b` as selects.
4. Build an 8:1 MUX from 4:1 MUXes and any additional gates. How many 4:1 MUXes?
5. Implement a **full adder** using two 8:1 MUXes.
6. Show how a 3-to-8 decoder with an active-high enable behaves as a 1-to-8 demultiplexer.

---
---
---

## Answers

**1.** `F(a,b,c,d) = Σm(0,1,3,5,7,9,15)`. Selects `a, b, c`; data variable `d`.

| abc | pair | F, F | Data |
|---|---|---|---|
| 000 | m0, m1 | 1, 1 | `D0 = 1` |
| 001 | m2, m3 | 0, 1 | `D1 = d` |
| 010 | m4, m5 | 0, 1 | `D2 = d` |
| 011 | m6, m7 | 0, 1 | `D3 = d` |
| 100 | m8, m9 | 0, 1 | `D4 = d` |
| 101 | m10, m11 | 0, 0 | `D5 = 0` |
| 110 | m12, m13 | 0, 0 | `D6 = 0` |
| 111 | m14, m15 | 0, 1 | `D7 = d` |

**2.** `F(P,Q,R,S) = Σm(0,2,5,9,11,12,14,15)`. Selects `P, Q, R`; data variable `S`.

| PQR | pair | F, F | Data |
|---|---|---|---|
| 000 | m0, m1 | 1, 0 | `D0 = S'` |
| 001 | m2, m3 | 1, 0 | `D1 = S'` |
| 010 | m4, m5 | 0, 1 | `D2 = S` |
| 011 | m6, m7 | 0, 0 | `D3 = 0` |
| 100 | m8, m9 | 0, 1 | `D4 = S` |
| 101 | m10, m11 | 0, 1 | `D5 = S` |
| 110 | m12, m13 | 1, 0 | `D6 = S'` |
| 111 | m14, m15 | 1, 1 | `D7 = 1` |

**3.** `F(a,b,c) = Σm(1,3,5,6)`, selects `a, b`, data variable `c`.

| ab | pair | F, F | Data |
|---|---|---|---|
| 00 | m0, m1 | 0, 1 | `I0 = c` |
| 01 | m2, m3 | 0, 1 | `I1 = c` |
| 10 | m4, m5 | 0, 1 | `I2 = c` |
| 11 | m6, m7 | 1, 0 | `I3 = c'` |

**4.** Two 4:1 MUXes plus one 2:1 MUX (which is itself buildable from gates).

```
  I0..I3 -> MUX A, selects S1 S0
  I4..I7 -> MUX B, selects S1 S0
  Y = S2' · A_out + S2 · B_out        <- the 2:1 stage
```

**Two 4:1 MUXes.** The enable-based alternative: drive MUX A's enable with `S2'` and MUX B's with
`S2`, then OR the two outputs — no third MUX, one OR gate.

**5.** Full adder: `Sum = Σm(1,2,4,7)`, `Cout = Σm(3,5,6,7)`, variables `A, B, Cin`.

An 8:1 MUX with all three variables as selects needs no data variable at all — tie each data input
to the truth-table value:

```
  Sum MUX:   D0=0  D1=1  D2=1  D3=0  D4=1  D5=0  D6=0  D7=1     selects A, B, Cin
  Cout MUX:  D0=0  D1=0  D2=0  D3=1  D4=0  D5=1  D6=1  D7=1     selects A, B, Cin
```

This is the brute-force use of a MUX as a lookup table — always correct, never minimal.

**6.** A decoder asserts output line `i` when the select word equals `i` **and the enable is
active**; all outputs are inactive when the enable is off.

Feed the data stream into the **enable** pin and use the decoder's address lines as the demux
selects:

```
  Y_i = (select == i) · EN  =  (select == i) · D
```

When `D = 1` the addressed line goes high; when `D = 0` every line stays low. That is exactly
demultiplexer behaviour — the same silicon, relabelled.
