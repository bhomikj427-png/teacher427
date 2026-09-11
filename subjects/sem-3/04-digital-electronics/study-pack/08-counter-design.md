# 08 — Synchronous Counter Design (the 8-mark question)

**This is Section C.** One question, 8 marks, 27% of the paper, roughly 24 minutes. It is a
**procedure**, not a fact — and a procedure you can execute cold is worth more than any amount of
reading about counters.

No professor deck covers this material. It is built from the textbook-verified knowledge base.

---

## Map

```
   RIPPLE (asynchronous) counter        SYNCHRONOUS counter
     each FF clocks the next              ALL FFs share one clock
     simple, cumulative delay             inputs computed by logic
     glitches on decoded outputs          no cumulative skew
            |                                    |
            |                                    v
            |                        THE 5-STEP DESIGN PROCEDURE
            |                        1. count sequence -> state table
            |                        2. next state per FF
            |                        3. excitation table (T / JK / D)
            |                        4. K-map each FF input
            |                        5. draw + check unused states
            |
            +--> mod-N by clearing on N
```

---

## Attempt first

1. In a synchronous counter, what drives each flip-flop's clock pin?
2. How many flip-flops are needed to count 0 to 7? 0 to 9? 0 to 11?
3. For a straight binary up-counter with T flip-flops, when must bit 2 toggle?
4. A mod-5 counter has 3 flip-flops. How many unused states, and why do they matter?
5. Design a synchronous counter counting 0 to 7 using negative edge-triggered T flip-flops.

---

## Method

### Ripple versus synchronous

```
  RIPPLE:   CLK -> [FF0] -> clocks [FF1] -> clocks [FF2]
            Delay accumulates: total = n x t_pd.
            Intermediate states appear briefly -> decoding glitches.

  SYNCHRONOUS:  CLK -> all flip-flop clock pins, in parallel
                Every flip-flop changes at the SAME edge.
                Total delay = one t_pd + the input logic delay.
```

**Every question in this file is synchronous.** The clock goes to all flip-flops in parallel; the
design work is deciding what to feed each flip-flop's *data* inputs.

### Number of flip-flops

```
  n flip-flops count 2ⁿ states,  0 to 2ⁿ - 1

  For a mod-N counter:  choose the smallest n with  2ⁿ ≥ N
```

0 to 7 -> 8 states -> **3 flip-flops**.
0 to 9 -> 10 states -> **4 flip-flops** (6 unused).
0 to 11 -> 12 states -> **4 flip-flops** (4 unused).

### The 5-step procedure

**Step 1 — write the count sequence as a state table.** Present state, then next state.

**Step 2 — split the next state into one column per flip-flop.**

**Step 3 — convert each transition into flip-flop inputs using the excitation table** (file 07):

| Q | Q+ | D | T | J | K |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | X |
| 0 | 1 | 1 | 1 | 1 | X |
| 1 | 0 | 0 | 1 | X | 1 |
| 1 | 1 | 1 | 0 | X | 0 |

For T flip-flops there is a shortcut that skips the table entirely:

```
  T_i = Q_i ⊕ Q_i+          T is 1 exactly when that bit must CHANGE
```

**Step 4 — K-map each flip-flop input** as a function of the present state bits. Unused states are
**don't-cares** — use them to simplify.

**Step 5 — draw the circuit, then check the unused states.** Feed each unused state into your
equations and see where it goes. A counter that can enter an unused state and never return is
**not self-starting** — a real mark deduction (trap T9).

### The standard binary up-counter result

Worth knowing before you derive it, as a check on your own work:

```
  T0 = 1
  T1 = Q0
  T2 = Q1·Q0
  T3 = Q2·Q1·Q0
```

Read it as a rule: **a bit toggles when all lower bits are 1.** That is exactly how binary counting
carries. With JK flip-flops the same result appears as `J_i = K_i = (product of all lower Q)`.

For a **down** counter the rule inverts: a bit toggles when all lower bits are **0**, so
`T1 = Q0'`, `T2 = Q1'·Q0'`, and so on.

---

## Worked — MTE 2025 Q8 (8 marks)

> Design a synchronous counter that counts clock pulses from 0-7 using negative edge triggered T
> flipflop.

**Step 0 — size it.** 0 to 7 is 8 states, so `2ⁿ ≥ 8` gives **n = 3**. Flip-flops `Q2 Q1 Q0`,
`Q2` the MSB. All eight states are used — **no don't-cares, no unused-state problem.**

**Step 1 and 2 — state table.**

| Count | Q2 Q1 Q0 | Q2+ Q1+ Q0+ |
|---|---|---|
| 0 | 0 0 0 | 0 0 1 |
| 1 | 0 0 1 | 0 1 0 |
| 2 | 0 1 0 | 0 1 1 |
| 3 | 0 1 1 | 1 0 0 |
| 4 | 1 0 0 | 1 0 1 |
| 5 | 1 0 1 | 1 1 0 |
| 6 | 1 1 0 | 1 1 1 |
| 7 | 1 1 1 | 0 0 0 |

**Step 3 — excitation, using `T = Q ⊕ Q+`.**

| Q2 Q1 Q0 | T2 | T1 | T0 |
|---|---|---|---|
| 0 0 0 | 0 | 0 | 1 |
| 0 0 1 | 0 | 1 | 1 |
| 0 1 0 | 0 | 0 | 1 |
| 0 1 1 | 1 | 1 | 1 |
| 1 0 0 | 0 | 0 | 1 |
| 1 0 1 | 0 | 1 | 1 |
| 1 1 0 | 0 | 0 | 1 |
| 1 1 1 | 1 | 1 | 1 |

**Step 4 — K-map each column.**

`T0` is 1 in every row:

```
  T0 = 1
```

`T1` is 1 at states 001, 011, 101, 111 — exactly the rows with `Q0 = 1`:

```
  T1 = Q0
```

`T2` is 1 at states 011 and 111 — the rows with `Q1 = 1` and `Q0 = 1`:

```
  T2 = Q1·Q0
```

K-map for `T2` (rows `Q2`, columns `Q1 Q0`):

```
          Q1Q0=00   01    11    10
   Q2=0 |    0  |  0  |  1  |  0  |
   Q2=1 |    0  |  0  |  1  |  0  |
```

One group of two spanning both rows -> `Q1·Q0`, with `Q2` dropping out.

**Step 5 — circuit.**

```
            T0 = 1              T1 = Q0            T2 = Q1·Q0
               |                   |                   |
          +----v----+         +----v----+         +----v----+
          |  T   Q  |--+ Q0   |  T   Q  |--+ Q1   |  T   Q  |--- Q2
          |         |  |      |         |  |      |         |
          |  FF0    |  |      |  FF1    |  |      |  FF2    |
          |    o CLK|  |      |    o CLK|  |      |    o CLK|
          +----^----+  |      +----^----+  |      +----^----+
               |       |           |       |           |
   CLK --------+-------|-----------+-------|-----------+
                       |                   |
                       |   Q0              |   Q1
                       +-----------+       |
                                   |       |
                                 +-v-------v-+
                                 |    AND    |----> T2 = Q1·Q0
                                 +-----------+

   Q0 also feeds T1 directly.        o on CLK = negative edge triggered
```

Reading the diagram in words, which is what earns the marks:

- All three flip-flops take the **same clock**, on the **negative (falling) edge** — the bubble on
  each CLK pin.
- `T0` is tied to logic **1**, so `Q0` toggles on every falling edge.
- `T1` is driven by `Q0`.
- `T2` is driven by an AND of `Q1` and `Q0`.

**Verify the sequence.** Start at `000`:

```
  000 : T2=0 T1=0 T0=1  ->  001
  001 : T2=0 T1=1 T0=1  ->  010
  010 : T2=0 T1=0 T0=1  ->  011
  011 : T2=1 T1=1 T0=1  ->  100
  100 : T2=0 T1=0 T0=1  ->  101
  101 : T2=0 T1=1 T0=1  ->  110
  110 : T2=0 T1=0 T0=1  ->  111
  111 : T2=1 T1=1 T0=1  ->  000
```

Counts 0 through 7 and rolls over. **Write this trace into your answer** — it is the proof, and it
costs two minutes.

**On "negative edge triggered":** it changes only *when* the transitions happen, not the logic. The
equations for a positive-edge version are identical. Say this explicitly — it shows you know the
difference between the triggering mechanism and the design.

---

## Worked — mod-5 synchronous counter with JK flip-flops

The harder variant: **unused states appear**, and the JK don't-cares do real work.

Count `000 -> 001 -> 010 -> 011 -> 100 -> 000`. Three flip-flops, **three unused states**
(101, 110, 111).

**State and excitation table** (X = don't-care from the JK table; entire rows X for unused states):

| Q2 Q1 Q0 | next | J2 K2 | J1 K1 | J0 K0 |
|---|---|---|---|---|
| 0 0 0 | 0 0 1 | 0 X | 0 X | 1 X |
| 0 0 1 | 0 1 0 | 0 X | 1 X | X 1 |
| 0 1 0 | 0 1 1 | 0 X | X 0 | 1 X |
| 0 1 1 | 1 0 0 | 1 X | X 1 | X 1 |
| 1 0 0 | 0 0 0 | X 1 | 0 X | 0 X |
| 1 0 1 | — | X X | X X | X X |
| 1 1 0 | — | X X | X X | X X |
| 1 1 1 | — | X X | X X | X X |

**K-map each of the six inputs:**

```
  J2 : 1 only at 011; with the unused-state X at 111 it groups as  Q1·Q0
  K2 : 1 at 100, X elsewhere                                    ->  1
  J1 : 1 at 001, X at 011/101/111                               ->  Q0
  K1 : 1 at 011, 0 at 010, X at 111                             ->  Q0
  J0 : 1 at 000 and 010, 0 at 100                               ->  Q2'
  K0 : 1 at 001 and 011, X elsewhere                            ->  1
```

```
  J2 = Q1·Q0     K2 = 1
  J1 = Q0        K1 = Q0
  J0 = Q2'       K0 = 1
```

**Step 5 — the self-start check, which is the whole point of this variant.**

Feed each unused state into the equations:

```
  101 : J2=Q1Q0=0, K2=1 -> Q2 resets to 0
        J1=Q0=1, K1=Q0=1 -> Q1 toggles to 1
        J0=Q2'=0, K0=1   -> Q0 resets to 0
        next state = 010      VALID

  110 : J2=0, K2=1 -> Q2 -> 0
        J1=Q0=0, K1=Q0=0 -> Q1 holds at 1
        J0=Q2'=0, K0=1   -> Q0 -> 0
        next state = 010      VALID

  111 : J2=1, K2=1 -> Q2 toggles to 0
        J1=1, K1=1       -> Q1 toggles to 0
        J0=Q2'=0, K0=1   -> Q0 -> 0
        next state = 000      VALID
```

Every unused state returns to the count within one clock. **The counter is self-starting.** State
it in those words — examiners look for the check, not just the conclusion.

If an unused state had led into another unused state in a closed loop, the fix is to force a
don't-care to a definite value and re-minimize.

### Mod-N by clearing

The shortcut used in labs and in short-answer questions: build a full binary counter and reset it
the moment it reaches N.

```
  Mod-10 (0 to 9) from a 4-bit counter:
  detect 1010 (decimal 10) with an AND on Q3 and Q1, feed it to the asynchronous CLEAR
```

State 1010 exists for a few nanoseconds before the clear takes effect — a **glitch**. Acceptable in
practice, but a fully synchronous design (the 5-step procedure) has no such spike. Mention the
trade-off if a question asks you to compare.

---

## Traps

**T8 — wrong excitation table.** T flip-flops are not JK flip-flops. Use the table for the device
the question names.

**T9 — unused states unchecked.** Any mod-N counter with `2ⁿ > N` has unused states. Trace them.
Three lines of work, and it is where the last marks of Section C sit.

**Forgetting the `T = Q ⊕ Q+` shortcut.** For T flip-flops it turns step 3 into a column of XORs.

**Treating "negative edge" as a logic change.** It is not. The equations are identical; only the
active edge differs.

**No verification trace.** Walking the counter through its states proves your equations. It takes
two minutes of a 24-minute question and converts a plausible answer into a demonstrated one.

**Asynchronous clearing in a "synchronous" question.** If the question says synchronous, use the
5-step procedure, not a clear-on-N shortcut.

---

## Self-test

1. Design a synchronous 3-bit **down** counter (7 down to 0) using T flip-flops.
2. Design a mod-6 synchronous counter (0 to 5) using T flip-flops. Check self-starting.
3. Design a synchronous counter for the sequence `0 -> 2 -> 4 -> 6 -> 0` using JK flip-flops.
4. How many flip-flops for a mod-12 counter? How many unused states?
5. A 4-bit ripple counter uses flip-flops with 10 ns propagation delay. What is the maximum clock
   frequency for the output to be valid before the next edge?
6. Why does a ripple counter produce decoding glitches while a synchronous counter does not?

---
---
---

## Answers

**1.** Down counter `111 -> 110 -> ... -> 000 -> 111`. Using `T = Q ⊕ Q+`:

| Q2 Q1 Q0 | next | T2 T1 T0 |
|---|---|---|
| 1 1 1 | 1 1 0 | 0 0 1 |
| 1 1 0 | 1 0 1 | 0 1 1 |
| 1 0 1 | 1 0 0 | 0 0 1 |
| 1 0 0 | 0 1 1 | 1 1 1 |
| 0 1 1 | 0 1 0 | 0 0 1 |
| 0 1 0 | 0 0 1 | 0 1 1 |
| 0 0 1 | 0 0 0 | 0 0 1 |
| 0 0 0 | 1 1 1 | 1 1 1 |

```
  T0 = 1
  T1 = Q0'          (T1 = 1 at states 110, 100, 010, 000 -> Q0 = 0)
  T2 = Q1'·Q0'      (T2 = 1 at states 100 and 000)
```

The up-counter rule inverted: **a bit toggles when all lower bits are 0.**

**2.** Mod-6, states 0 to 5, unused 110 and 111.

| Q2 Q1 Q0 | next | T2 T1 T0 |
|---|---|---|
| 0 0 0 | 0 0 1 | 0 0 1 |
| 0 0 1 | 0 1 0 | 0 1 1 |
| 0 1 0 | 0 1 1 | 0 0 1 |
| 0 1 1 | 1 0 0 | 1 1 1 |
| 1 0 0 | 1 0 1 | 0 0 1 |
| 1 0 1 | 0 0 0 | 1 0 1 |
| 1 1 0 | — | X X X |
| 1 1 1 | — | X X X |

K-maps (don't-cares at 110, 111):

```
  T0 = 1
  T1 : 1 at 001 and 011, 0 at 000/010/100/101, X at 110/111  ->  T1 = Q2'·Q0
  T2 : 1 at 011 and 101, 0 at 000/001/010/100, X at 110/111  ->  T2 = Q1·Q0 + Q2·Q0 = Q0·(Q1 + Q2)
```

**Self-start check:**

```
  110 : T2 = Q0·(Q1+Q2) = 0·(1+1) = 0  -> Q2 holds 1
        T1 = Q2'·Q0      = 0·0     = 0  -> Q1 holds 1
        T0 = 1                          -> Q0 toggles 0 -> 1
        next state = 111

  111 : T2 = Q0·(Q1+Q2) = 1·(1+1) = 1  -> Q2 toggles 1 -> 0
        T1 = Q2'·Q0      = 0·1     = 0  -> Q1 holds 1
        T0 = 1                          -> Q0 toggles 1 -> 0
        next state = 010      VALID
```

`110` goes to `111`, and `111` returns to `010`, which is in the count. The counter recovers within
two clocks — **self-starting**, though not in a single clock. Say exactly that.

**3.** Sequence `000 -> 010 -> 100 -> 110 -> 000`. `Q0` is always 0, so it is a 2-flip-flop counter
on `Q2 Q1` with `Q0` tied low — but designed as asked with three:

| Q2 Q1 Q0 | next | J2 K2 | J1 K1 | J0 K0 |
|---|---|---|---|---|
| 0 0 0 | 0 1 0 | 0 X | 1 X | 0 X |
| 0 1 0 | 1 0 0 | 1 X | X 1 | 0 X |
| 1 0 0 | 1 1 0 | X 0 | 1 X | 0 X |
| 1 1 0 | 0 0 0 | X 1 | X 1 | 0 X |

```
  J2 = Q1     K2 = Q1
  J1 = 1      K1 = 1
  J0 = 0      K0 = 1        (Q0 held at 0)
```

`Q1` toggles every clock; `Q2` toggles when `Q1` is 1. This is a 2-bit up counter shifted one
position left — counting in steps of 2 is counting normally on the upper bits.

**4.** Mod-12 needs `2ⁿ ≥ 12` -> **n = 4** flip-flops (16 states).

```
  unused states = 16 - 12 = 4     (1100, 1101, 1110, 1111)
```

All four must be traced in the self-start check.

**5.** Ripple counter delays accumulate through all four stages:

```
  total settling time = 4 x 10 ns = 40 ns
  f_max = 1 / 40 ns = 25 MHz
```

A synchronous counter of the same width settles in one flip-flop delay plus the input gate delay —
roughly 10-15 ns, so well above 60 MHz. That gap is the reason synchronous design dominates.

**6.** In a ripple counter each flip-flop is clocked by the previous one, so the bits change at
**staggered times**, rippling from LSB to MSB.

During the ripple, the output word passes through **intermediate values that are not real counter
states**. Going from `0111` to `1000`, the bits settle one at a time: `0111 -> 0110 -> 0100 ->
0000 -> 1000`. A decoder watching those lines briefly sees 6, 4, and 0 — short false pulses, the
**decoding glitches**.

In a synchronous counter all flip-flops change at the same edge, so the word steps directly from one
valid state to the next and no intermediate value is ever presented.
