# 05 — Decoders, Encoders, 7-Segment Display

---

## Map

```
   DECODER: n inputs -> 2^n outputs, exactly ONE active
        |
        +--> each output line IS one minterm
        |         |
        |         +--> active-HIGH outputs + OR gate  -> implement Sigma-m
        |         +--> active-HIGH outputs + NOR gate -> implement Pi-M
        |         +--> active-LOW  outputs + NAND gate -> implement Sigma-m
        |
        +--> with an enable = DEMUX (file 04)

   ENCODER: 2^n inputs -> n outputs (the inverse)
        |
        +--> priority encoder fixes the multiple-input ambiguity

   BCD to 7-SEGMENT: a code converter, not a plain decoder
        |
        +--> common cathode -> active HIGH
        +--> common anode   -> active LOW
```

---

## Attempt first

1. A 3-to-8 decoder is given `A=1, B=0, C=1`. Which output is active?
2. Why can any Sum-of-Products function be built from a decoder and one OR gate?
3. `Sum` of a full adder is `Sigma-m(1,2,4,7)`. Which decoder outputs feed the OR gate?
4. `Y = Pi-M(0,3,5,6,7)`. Realize it with a decoder and **one NOR** gate.
5. What goes wrong in a plain 8-to-3 encoder if two inputs are high at once?
6. A common-anode display is driven by a BCD decoder. Is segment `a` driven high or low to light it?

---

## Method

### Decoder

An n-to-2^n decoder activates exactly one output line for each input combination.

3-to-8 decoder, active-high outputs:

```
           +-----------+
   A ----->|           |---> D0 = A'B'C'
   B ----->|  3-to-8   |---> D1 = A'B'C
   C ----->|  decoder  |---> D2 = A'BC'
           |           |---> D3 = A'BC
   EN ---->|           |---> D4 = AB'C'
           +-----------+---> D5 = AB'C
                       +---> D6 = ABC'
                       +---> D7 = ABC
```

**Each output line is one minterm.** That single fact is the whole topic.

### Implementing functions with a decoder

| Decoder output type | Function form wanted | Collecting gate |
|---|---|---|
| Active **high** | `Sigma-m` (SOP) | **OR** |
| Active **high** | `Pi-M` (POS) | **NOR** |
| Active **low** | `Sigma-m` (SOP) | **NAND** |
| Active **low** | `Pi-M` (POS) | **AND** |

**Active-high + OR:** `F = Sigma-m(a,b,c)` means `F = D_a + D_b + D_c`. Wire those lines to an OR.

**Active-high + NOR:** `F = Pi-M(a,b,c)` means F is **0** at those indices. So
`F = (D_a + D_b + D_c)'` — a NOR over the maxterm lines. This is practice Q7.

**Active-low + NAND:** with active-low outputs each line is `(minterm)'`, so
`NAND` of the selected lines gives back `Sigma-m`. De Morgan again.

**Cost note:** one decoder serves **several functions at once** — that is its advantage over a MUX.
A full adder needs one 3-to-8 decoder and two gates for both Sum and Cout.

### Decoder expansion

Build a 4-to-16 from two 3-to-8 decoders using the enable:

```
  MSB = 0  ->  enable decoder A (outputs 0..7)
  MSB = 1  ->  enable decoder B (outputs 8..15)
```

Feed the MSB to one enable directly and through an inverter to the other.

### Encoder

An encoder is the inverse: `2^n` inputs, n outputs, output = the binary index of the active input.

8-to-3 encoder:

```
  Y2 = D4 + D5 + D6 + D7
  Y1 = D2 + D3 + D6 + D7
  Y0 = D1 + D3 + D5 + D7
```

Three OR gates. Read them as: `Y2` is high for indices 4-7, `Y1` for 2,3,6,7, `Y0` for odd indices —
each output bit ORs the inputs whose index has that bit set.

**Two problems with the plain encoder:**

1. **Ambiguity.** If `D3` and `D5` are both high, the output is `011 + 101 = 111` = 7, which is
   neither input. Garbage.
2. **Zero ambiguity.** Output `000` means either `D0` is active or *nothing* is active. A separate
   "valid" output fixes this.

### Priority encoder

Resolves the ambiguity: when several inputs are active, the **highest-index** input wins.

4-to-2 priority encoder, `D3` highest:

```
  Y1 = D3 + D2
  Y0 = D3 + D2'·D1
  V  = D3 + D2 + D1 + D0          valid output
```

Read `Y0`: `D3` forces it high; otherwise `D1` only counts when `D2` is inactive. The general shape
is "this input, OR this input with all higher ones inactive."

### BCD to 7-segment

A code converter: 4 BCD inputs `A B C D` (A = MSB), 7 outputs `a` to `g`.

```
        a
      -----
   f |     | b
     |  g  |
      -----
   e |     | c
     |     |
      -----
        d
```

Digits 1010 through 1111 never occur in BCD -> **six don't-cares**, which is what makes the
minimized equations short.

Segment on/off per digit (1 = lit):

| Digit | a | b | c | d | e | f | g |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 3 | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 4 | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 5 | 1 | 0 | 1 | 1 | 0 | 1 | 1 |
| 6 | 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| 7 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 8 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 9 | 1 | 1 | 1 | 1 | 0 | 1 | 1 |

Minimized with the six don't-cares (these are the **active-high / common-cathode** equations):

```
  a = A + C + B·D + B'·D'
  b = B' + C·D + C'·D'
  c = B + C' + D
  d = A + B'·D' + C·D' + B'·C + B·C'·D
  e = B'·D' + C·D'
  f = A + C'·D' + B·C' + B·D'
  g = A + B·C' + B'·C + C·D'
```

### Common cathode versus common anode

```
  COMMON CATHODE : all cathodes tied to ground.
                   Segment lights when its driver output is HIGH.
                   -> use the equations above directly (ACTIVE HIGH).

  COMMON ANODE   : all anodes tied to Vcc.
                   Current flows when the driver pulls the pin LOW.
                   -> segment lights when the driver output is LOW (ACTIVE LOW).
                   -> COMPLEMENT every equation above.
```

For a common-anode display:

```
  a_drive = ( A + C + B·D + B'·D' )'
```

and so on for all seven. In practice you either invert the outputs or re-minimize by grouping the
**0s** of each segment map. **Stating which convention you used is part of the answer.**

---

## Worked — MTE 2025 Q6 (4 marks)

> Design a Full Adder using a suitable decoder.

**Step 1 — pick the decoder.** Three inputs `A, B, Cin` -> a **3-to-8 decoder**.

**Step 2 — write the function as minterms** (from file 03):

```
  Sum  = Sigma-m(1, 2, 4, 7)
  Cout = Sigma-m(3, 5, 6, 7)
```

**Step 3 — collect with OR gates** (assuming active-high outputs):

```
  Sum  = D1 + D2 + D4 + D7
  Cout = D3 + D5 + D6 + D7
```

**Step 4 — draw.**

```
           +-----------+
   A ----->|           |--- D0
   B ----->|  3-to-8   |--- D1 ---+
   Cin --->|  decoder  |--- D2 ---+
           |           |--- D3 --------+       +--[OR]--- Sum
           |           |--- D4 ---+    |       |   (D1,D2,D4,D7)
           |           |--- D5 --------+       |
           |           |--- D6 --------+       |
           |           |--- D7 ---+----+--[OR]--- Cout
           +-----------+                   (D3,D5,D6,D7)
```

One 3-to-8 decoder, two 4-input OR gates. `D7` feeds **both** gates — the decoder's advantage is
exactly this sharing.

**If the decoder has active-low outputs**, swap both OR gates for **NAND** gates. Say which
convention you assumed.

---

## Worked — practice Q7

> Realize `Y = Pi-M(0,3,5,6,7)` with a Decoder and one NOR gate.

Three variables (indices up to 7) -> a **3-to-8 decoder**.

`Pi-M` means Y is **0** at 0, 3, 5, 6, 7 and **1** everywhere else. Equivalently
`Y = Sigma-m(1,2,4)`.

With a **NOR** gate, wire the **maxterm** lines directly:

```
  Y = ( D0 + D3 + D5 + D6 + D7 )'
```

```
   A ---->|          |--- D0 --+
   B ---->| 3-to-8   |--- D3 --+
   C ---->| decoder  |--- D5 --+---[NOR]--- Y
          |          |--- D6 --+
          |          |--- D7 --+
```

One 5-input NOR. Whenever the input hits one of those five indices the NOR sees a 1 and outputs 0;
for 1, 2 and 4 all five lines are low, so Y = 1.

**Do not convert to Σm and use an OR** — the question specified a NOR, and the maxterm lines feed it
directly. This is the point of the question.

---

## Traps

**ΠM is not Σm.** `Pi-M(0,3,5,6,7)` lists where the function is **zero**. Wiring those five lines
into an OR gives you the complement of the answer.

**Active-high versus active-low outputs.** The collecting gate changes: OR becomes NAND for
active-low outputs. If the question does not say, state your assumption.

**Common anode inverts everything.** Trap T10. Common cathode = active high; common anode = active
low. Getting this backwards lights the complement of every digit.

**The plain encoder is broken by design.** If a question asks "what happens with two inputs active,"
the answer is a meaningless output, and the fix is a **priority** encoder — not more OR gates.

**Use the decoder's sharing.** When one question asks for two functions, one decoder serves both.
Drawing two decoders wastes the insight the question is testing.

---

## Self-test

1. Implement `F(a,b,c,d) = Sigma-m(0,1,2,5,6,8,9,15)` using a suitable decoder.
2. Write the outputs of a 3-to-8 decoder with active-**low** outputs for input `ABC = 110`.
3. Build a 4-to-16 decoder from two 3-to-8 decoders with enables.
4. Design a 4-to-2 priority encoder with a valid flag. Give all three equations.
5. Design a BCD to 7-segment decoder for a **common anode** display. Give the driver equation for
   segments `c` and `e`.
6. Implement a full **subtractor** using a 3-to-8 decoder and OR gates.

---
---
---

## Answers

**1.** Four variables -> **4-to-16 decoder**. With active-high outputs and one OR gate:

```
  F = D0 + D1 + D2 + D5 + D6 + D8 + D9 + D15
```

An 8-input OR gate. With active-low outputs, use an 8-input NAND instead.

**2.** Active-low means the selected line goes **0** and all others stay **1**.

`ABC = 110` = index 6, so:

```
  D6 = 0 ;  D0 = D1 = D2 = D3 = D4 = D5 = D7 = 1
```

**3.**

```
   A (MSB) --+--------------------> EN of decoder B   (outputs 8..15)
             |
             +--[NOT]-------------> EN of decoder A   (outputs 0..7)

   B, C, D ----------------------> address inputs of BOTH decoders
```

When `A = 0`, decoder A is enabled and produces outputs 0-7 from `BCD`. When `A = 1`, decoder B is
enabled and its eight outputs are relabelled 8-15. Exactly one of the sixteen lines is ever active.

**4.** `D3` highest priority.

```
  Y1 = D3 + D2
  Y0 = D3 + D2'·D1
  V  = D3 + D2 + D1 + D0
```

Check `D3 = 0, D2 = 1, D1 = 1`: `Y1 = 1`, `Y0 = 0 + 0·1 = 0` -> output `10` = 2. `D2` wins over
`D1`, as required.

**5.** Take the active-high equations and complement them.

```
  c (common cathode, active high) = B + C' + D
  c_drive (common anode)          = ( B + C' + D )'  =  B'·C·D'
```

Sanity check: segment `c` is off only for digit 2 (`ABCD = 0010`). `B'·C·D' = 1·1·1 = 1`, so the
driver goes high, which on a common-anode display means **off**. Correct.

```
  e (common cathode) = B'·D' + C·D'
  e_drive (common anode) = ( B'·D' + C·D' )'  =  (B + D)·(C' + D)  =  B·C' + D
```

Expand to check: `(B + D)(C' + D) = B·C' + B·D + C'·D + D = B·C' + D` (absorption).
Segment `e` is lit for digits 0, 2, 6, 8. Test digit 0 (`0000`): `B·C' + D = 0·1 + 0 = 0` -> driver
low -> lit. Correct. Test digit 1 (`0001`): `0 + 1 = 1` -> driver high -> off. Correct.

**6.** Full subtractor (file 03): `Difference = Sigma-m(1,2,4,7)`, `Bout = Sigma-m(1,2,3,7)`.

```
  Difference = D1 + D2 + D4 + D7
  Bout       = D1 + D2 + D3 + D7
```

One 3-to-8 decoder with inputs `A, B, Bin`, two 4-input OR gates.

Note `Difference` has the **same** minterm set as a full adder's `Sum` — subtraction and addition
share the XOR structure, and only the borrow/carry term differs. Verify `Bout` against the table in
file 03: Bout = 1 for `(A,B,Bin)` = 001, 010, 011, 111 -> indices 1, 2, 3, 7. Correct.
