# 07 — Flip-Flops and Waveforms

Where combinational logic ends. Everything from here on has **memory**: the output depends on the
past, not only on the present inputs.

---

## Map

```
   SR latch (NOR / NAND)        <-- level sensitive, has a forbidden state
        |
        +--> gated SR latch     <-- add enable
              |
              +--> D latch      <-- kill the forbidden state
                    |
                    +--> EDGE-TRIGGERED flip-flops   <-- add a clock edge
                          |
                          +--> D FF     Q+ = D
                          +--> JK FF    Q+ = JQ' + K'Q      (fixes SR's forbidden state)
                          +--> T FF     Q+ = T (+) Q        (toggle)
                          +--> master-slave JK             (fixes race-around)
                                |
                                v
                          characteristic table  (given inputs -> next state)
                          excitation table      (given state change -> needed inputs)
                                |
                                v
                          waveform drawing  ·  FF conversion  ·  counters (file 08)
```

**Characteristic and excitation tables are two readings of the same truth table.** Confusing them
is trap T7 and it wrecks counter design.

---

## Attempt first

1. What is the difference between a latch and a flip-flop, in one sentence?
2. Why is `S = R = 1` forbidden on an SR latch?
3. Write the characteristic equation of a JK flip-flop.
4. What excitation input makes a T flip-flop toggle?
5. A JK flip-flop with `J = K = 1` is clocked by a level-sensitive (not edge-triggered) clock.
   What goes wrong?
6. Q is currently 0 and must become 1. What `J` and `K` are required? What `S` and `R`?

---

## Method

### Latch versus flip-flop

```
  LATCH        : level sensitive. Output follows input the whole time the enable is high.
  FLIP-FLOP    : edge triggered. Output can change only at the clock edge.
```

An exam answer that says "a flip-flop is clocked" is incomplete — **latches can be clocked too**.
The distinction is *level* versus *edge*.

### SR latch

Cross-coupled NOR gates:

```
   R ---+--[NOR]---+--- Q
        |          |
        +----------|----+
                   |    |
   S ---+--[NOR]---+--- Q'
```

| S | R | Q+ | Meaning |
|---|---|---|---|
| 0 | 0 | Q | hold |
| 0 | 1 | 0 | reset |
| 1 | 0 | 1 | set |
| 1 | 1 | — | **forbidden** |

**Why `S = R = 1` is forbidden:** it drives both `Q` and `Q'` to 0, so the two outputs are no longer
complements. Worse, when both inputs return to 0 simultaneously the final state depends on which
gate switches first — a **race**, and the result is unpredictable.

The NAND version (`S'R'` latch) is the same circuit with the forbidden combination at `0, 0`.

### D latch — the forbidden state removed

Feed `S = D` and `R = D'`. The two inputs can never be equal, so the forbidden combination cannot
be reached.

```
  Q+ = D       while the enable is high
```

### The four flip-flops

**Characteristic tables** — given the inputs, what is the next state `Q+`:

| D | Q+ |
|---|---|
| 0 | 0 |
| 1 | 1 |

| J | K | Q+ |
|---|---|---|
| 0 | 0 | Q (hold) |
| 0 | 1 | 0 (reset) |
| 1 | 0 | 1 (set) |
| 1 | 1 | Q' (**toggle**) |

| T | Q+ |
|---|---|
| 0 | Q (hold) |
| 1 | Q' (toggle) |

**Characteristic equations:**

```
  D FF :  Q+ = D
  SR FF:  Q+ = S + R'·Q          (with S·R = 0)
  JK FF:  Q+ = J·Q' + K'·Q
  T FF :  Q+ = T (+) Q  =  T·Q' + T'·Q
```

**The JK equation is the one to memorise cold.** Read it: J sets when Q is low, K' holds when Q is
high. Setting `J = K = 1` gives `Q+ = Q' + 0 = Q'`, the toggle.

### Excitation tables — the inverse reading

Given the transition you **want**, what inputs do you **apply**? This is what counter design uses.

| Q | Q+ | D | T | J K | S R |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 X | 0 X |
| 0 | 1 | 1 | 1 | 1 X | 1 0 |
| 1 | 0 | 0 | 1 | X 1 | 0 1 |
| 1 | 1 | 1 | 0 | X 0 | X 0 |

**Learn this table.** It is the engine of every synchronous counter question.

Read the `T` column as one rule:

```
  T = Q (+) Q+           T is 1 exactly when the state must CHANGE
```

Read the `J K` column as: each transition constrains only **one** of J and K; the other is a
don't-care. Those X's are what make the counter K-maps collapse.

### Race-around, and the master-slave fix

With a **level-triggered** JK and `J = K = 1`, the output toggles. But while the clock is still
high, the new output feeds back and toggles again — and again — for as long as the clock pulse
lasts.

```
  Race-around occurs when:   clock pulse width  >  flip-flop propagation delay
```

The output ends in an unpredictable state. Two fixes:

1. **Master-slave**: two latches in series on opposite clock phases. The master accepts input while
   the clock is high; the slave copies the master when the clock goes low. Input and output are
   never open at the same time, so feedback cannot race.
2. **Edge triggering**: the flip-flop samples only at the instant of the edge, so the window is
   effectively zero.

### Edge triggering and timing

```
  Positive edge-triggered : acts on the LOW-to-HIGH transition.  Symbol: >
  Negative edge-triggered : acts on the HIGH-to-LOW transition.  Symbol: > with a bubble
```

```
  Setup time (t_su)  : input must be STABLE BEFORE the edge
  Hold time  (t_h)   : input must stay STABLE AFTER the edge
  Propagation delay  : edge to valid output
```

Violating setup or hold can push the flip-flop into a **metastable** state — an output stuck between
valid levels for an unbounded time.

### Drawing a waveform — the procedure

This is MTE Q7's question form. Work it mechanically:

1. **Mark every active edge** on the clock with a vertical line. Positive edge = each rising edge;
   negative = each falling edge. Ignore every other point in time.
2. **Write the stated initial value of Q** at the far left.
3. At **each marked edge only**, read the input(s) *at that instant* and apply the characteristic
   table.
4. Hold the output flat between edges. **The output never changes between edges.**
5. Draw the output as a square wave transitioning only at the marked lines.

Worked shape, a D flip-flop, positive edge, Q initially 0:

```
  CLK   _|‾|_|‾|_|‾|_|‾|_|‾|_
         ^   ^   ^   ^   ^        <- active edges marked
  D     ___|‾‾‾‾‾‾‾|___|‾‾‾‾‾
  Q     _______|‾‾‾‾‾‾‾|___|‾‾
```

Q picks up D's value at each rising edge and holds it flat until the next one. Note Q's change
**lags** D — that lag is the answer to "why is this a memory element."

### Flip-flop conversion

To convert flip-flop X into flip-flop Y:

1. Write the **desired** (Y) characteristic table: `Q, Y-inputs -> Q+`.
2. For each row, use **X's excitation table** to find the X inputs needed for that `Q -> Q+`.
3. K-map the X inputs as functions of `Q` and the Y inputs.

**JK to T:** tie `J = K = T`.
Check: `T = 0` gives `J = K = 0` -> hold. `T = 1` gives `J = K = 1` -> toggle. Correct.

**JK to D:** `J = D`, `K = D'`.
Check: `D = 1` gives `J = 1, K = 0` -> set. `D = 0` gives `J = 0, K = 1` -> reset. Correct.

**D to T:** `D = T (+) Q`.
This is the characteristic equation of a T flip-flop fed straight into a D input — one XOR gate.

---

## Worked — MTE 2025 Q3 (2 marks)

> What excitation input should be applied to a T-FF to make output toggle?

```
  T = 1
```

From the characteristic equation `Q+ = T (+) Q`: with `T = 1`, `Q+ = 1 (+) Q = Q'`, which is the
toggle. With `T = 0`, `Q+ = Q`, a hold.

The general rule behind it — worth writing as the second line of the answer:

```
  T = Q (+) Q+     ->  T = 1 whenever the state must change
```

---

## Worked — MTE 2025 Q7 (4 marks), the method

> Draw the output waveform for the given input waveform, assuming the flip-flop to be positive edge
> triggered and the output Q is initially at logic zero.

The paper supplies the input waveform, so the marks are entirely in the procedure. Apply it:

```
  Step 1  Mark every RISING clock edge. Nothing else matters.
  Step 2  Write Q = 0 at t = 0, as stated.
  Step 3  At each marked edge read the input value AT that instant.
  Step 4  Apply the characteristic table of the flip-flop shown.
  Step 5  Hold Q flat between edges.
```

Example with a **JK** flip-flop, positive edge, Q initially 0:

```
  CLK   _|‾|_|‾|_|‾|_|‾|_
         1   2   3   4        <- rising edges

  edge 1:  J=1 K=0  -> set     -> Q = 1
  edge 2:  J=0 K=0  -> hold    -> Q = 1
  edge 3:  J=1 K=1  -> toggle  -> Q = 0
  edge 4:  J=0 K=1  -> reset   -> Q = 0
```

**Write the edge-by-edge reasoning next to the drawing.** If the waveform is slightly off, the
stated reasoning still earns marks; a bare waveform with an error earns none.

---

## Traps

**T6 — ignoring edge polarity or initial state.** The same input waveform gives a different output
for positive versus negative edge. The question states both; use them.

**T7 — characteristic versus excitation.** Characteristic: inputs -> next state. Excitation: desired
next state -> inputs. Counter design needs the **excitation** table. Reaching for the wrong one is
the most expensive habit in this unit.

**Changes between edges.** A common error is drawing Q following the input in the middle of a clock
period. An edge-triggered output changes **only at edges**, full stop.

**Race-around is a level-triggering problem.** It affects level-triggered JK with `J = K = 1`. An
edge-triggered JK does not suffer from it — saying otherwise is wrong.

**Don't-cares in the JK excitation table are a feature.** They shrink the K-maps in file 08. Do not
"fill them in" with 0s.

---

## Self-test

1. Write the characteristic equation of the JK flip-flop and derive the T flip-flop's from it.
2. Give the complete excitation table for all four flip-flops.
3. Convert a D flip-flop into a JK flip-flop. Give the input equation.
4. A JK flip-flop has `J = K = 1`, clock period 20 ns, propagation delay 8 ns, and is level
   triggered with a 15 ns high pulse. What happens?
5. A negative edge-triggered T flip-flop starts at `Q = 1` with `T` held at 1. Sketch Q over four
   clock cycles.
6. Why does a master-slave flip-flop not suffer from race-around?
7. A D flip-flop has `t_su = 3 ns`, `t_h = 2 ns`. The data changes 1 ns before the clock edge. Is
   this legal, and what may result?

---
---
---

## Answers

**1.**

```
  JK:  Q+ = J·Q' + K'·Q
```

Set `J = K = T`:

```
  Q+ = T·Q' + T'·Q  =  T (+) Q
```

which is the T flip-flop's characteristic equation. That substitution *is* the JK-to-T conversion.

**2.**

| Q | Q+ | D | T | J | K | S | R |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | X | 0 | X |
| 0 | 1 | 1 | 1 | 1 | X | 1 | 0 |
| 1 | 0 | 0 | 1 | X | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 | X | 0 | X | 0 |

**3.** D to JK. The D input must equal the JK's next state:

```
  D = Q+ = J·Q' + K'·Q
```

One AND-OR network (or two ANDs and an OR) plus inverters for `Q'` and `K'`. The feedback of `Q`
into the input logic is what makes the conversion work.

**4.** The clock pulse is **15 ns high** and the propagation delay is **8 ns**.

```
  pulse width (15 ns)  >  propagation delay (8 ns)
```

So after the first toggle at 8 ns, the clock is still high for another 7 ns and the new output feeds
back to toggle again. **Race-around occurs** — the output oscillates during the pulse and its final
state is unpredictable. Fix with a master-slave or an edge-triggered flip-flop, or shorten the pulse
below 8 ns.

**5.** Negative edge-triggered, `T = 1` (toggle at every falling edge), starting at `Q = 1`:

```
  CLK   ‾|_|‾|_|‾|_|‾|_|‾
          v   v   v   v        <- falling edges
  Q     ‾‾‾|___|‾‾‾|___|‾‾
```

Q goes 1 -> 0 -> 1 -> 0 -> 1, changing only on falling edges. Note Q's period is **twice** the
clock's: a toggle flip-flop divides frequency by 2, which is the basis of the ripple counter.

**6.** The master and slave latches are enabled on **opposite clock phases**.

```
  clock HIGH : master open (accepts J, K), slave CLOSED (output frozen)
  clock LOW  : master closed, slave open (copies master to output)
```

The input stage and the output stage are never transparent simultaneously, so the new output cannot
propagate back to the input while the input is still being sampled. The feedback loop that causes
race-around is broken in time.

**7.** Not legal. The data changed 1 ns before the edge but setup time requires **3 ns** of
stability before it.

```
  1 ns  <  t_su = 3 ns     -> setup violation
```

The flip-flop may capture the old value, the new value, or enter a **metastable** state — an output
hovering between logic levels for an unbounded settling time. The resolution time is probabilistic;
there is no guaranteed upper bound, only a mean time between failures.
