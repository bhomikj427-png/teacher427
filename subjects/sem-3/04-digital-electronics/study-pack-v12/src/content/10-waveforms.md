# 10 — Drawing latch and flip-flop waveforms

<div class="sub">Deck 08 (slides 22–24, 42–44) · syllabus Unit 3 (flip-flop operation, timing) · 3 real questions: MTE 2025 Q7 (4 marks), practice set 2 Q2, practice set 2 Q3 (a, b) · needs 09 steps 5 (D latch), 7 (latch vs flip-flop), 9 (JK table), 11 (race-around)</div>

## Map

[[map:1 Reading a timing diagram > 2 Which value counts at an edge > 3 Positive edge: MTE Q7 > 4 Negative edge > 5 D latch: transparent > 6 JK latch: race-around > 7 Asynchronous clear and preset|here=1]]

File 09 gave each memory element a table: what Q becomes for each input. An exam asks for the same thing drawn against time: the inputs are given as waveforms and Q must be drawn underneath. This file turns the tables into one procedure for edge-triggered flip-flops (steps 1–4), a second one for level-triggered latches (steps 5–6), and adds the inputs that act without the clock (step 7). Files 12–13 draw counter waveforms with the same procedure.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| CLK | the clock waveform | square wave |
| ↑n, ↓n | the n-th rising / falling clock edge, numbered from the left | n = 1 … 7 |
| EN | enable of a latch; the latch listens while EN = 1 | 0 or 1 |
| J, K, D | flip-flop or latch inputs, drawn as waveforms | 0 or 1 |
| Q₀ | Q before the first edge ("initially at logic zero / one") | given |
| CLR', PR' | asynchronous clear and preset, active-low: a 0 forces Q at once | idle at 1 |
| t_su | setup time: how long an input must be steady **before** the edge for the flip-flop to read it | a few ns |

## Running example

**MTE 2025 Q7's clock and inputs**: 7 clock pulses; J high from ↑1 to ↓1, from ↑3 to ↓3, from the middle of pulse 4's high time to ↓5, and from ↓6 to ↓7; K high for short pieces in periods 1–2 and from the middle of pulse 5 onward. Step 3 draws Q for a positive-edge JK, step 4 the same inputs for a negative-edge JK (practice set 2 Q3a), step 7 adds clear and preset (practice set 2 Q3b).

## The questions this file answers

- <span class="tag">MTE 2025 Q7 · 4 marks</span> Draw the output waveform for the following input waveform, assuming the flip-flop to be positive edge triggered and the output Q is initially at logic zero.
- <span class="tag">Practice set 2 Q3</span> Input waveforms for JK flip-flops are shown in given figures. Draw the output waveform for each case. Assume the flip-flops to be negative edge triggered for both cases and the output Q is initially at logic zero.
- <span class="tag">Practice set 2 Q2</span> Complete the timing diagrams for D Latch and JK Latch. Assume the latch to be high level triggered for both cases and the output Q is initially at logic one.
- <span class="tag">Deck 08 slides 42–44 (EX 8.42–8.44)</span> The same three tasks as unsolved slide exercises (D and JK latch; JK flip-flop on ↑; on ↓).

---

## Build

### 1 · Reading a timing diagram

A flip-flop changes only at an edge (file 09 step 7). So a waveform answer is a list of edges, the inputs at each, and file 09's table applied once per edge.

:::guess Predict
A positive-edge D flip-flop's D has two short pulses that start in the middle of a clock high time and end before the next ↑. Do they appear at Q?
:::

:::note Terms
**Timing diagram:** one row per signal, time running left to right, high = 1, low = 0. **Active edge:** the edge the flip-flop acts on: ↑ for positive-edge (plain ▷), ↓ for negative-edge (bubble before ▷).
:::

[[fig:u3_dff|What this graph plots: time across; rows CLK, D, Q of a positive-edge D flip-flop (high = 1). Dotted lines mark the six ↑ edges, where Q takes the D just before the line.|w=78]]

| Edge | ↑1 | ↑2 | ↑3 | ↑4 | ↑5 | ↑6 |
|---|---|---|---|---|---|---|
| D just before | 0 | 0 | 1 | 0 | 0 | 0 |
| Q after | 0 | 0 | 1 | 0 | 0 | 0 |

**The procedure** (every edge-triggered question):

1. Draw a dotted vertical line at every **active** edge; number them.
2. Start Q at the given initial value.
3. At each line read the inputs **just before** it (step 2 says why) and apply the table of file 09.
4. Draw Q **flat between lines**, whatever the inputs do there.
5. Write the edge table beside the drawing: it carries the marks even if a line is slightly off.

**Answer to the Predict.** **No.** The first D pulse (inside high time 1) is back to 0 by ↑2, and the last one (inside high time 5) is back to 0 by ↑6: Q never sees them. Q is high only from ↑3 to ↑4.

:::check Check 1
(a) Same D, but the flip-flop is negative-edge: read D just before ↓1 … ↓6 from the figure. (b) Between two active edges D changes three times. How many times can Q change there?
:::

### 2 · Which value counts when an input changes at the edge

In MTE Q7 some inputs change at the **same instant** as a clock edge. The rule of step 1 ("just before") decides them, and here is why.

:::q <span class="tag">MTE 2025 Q7 · 4 marks (inputs)</span>
Draw the output waveform for the following input waveform, assuming the flip-flop to be positive edge triggered and the output Q is initially at logic zero.
:::

[[fig:u3_mte7_noq|MTE 2025 Q7's inputs, redrawn from the paper. What this graph plots: time across; rows CLK, J, K (high = 1). The seven ↑ edges are numbered. J rises exactly at ↑1 and ↑3; K falls exactly at ↑2.|w=80]]

:::guess Guess first
At ↑1, J goes from 0 to 1 at the same instant. Does the flip-flop see J = 0 or J = 1?
:::

:::note Terms
**Setup time t_su:** an input must be steady for at least t_su **before** the active edge to be read correctly (KB 03 §6). **Hold time:** it must also stay steady for a short time after the edge.
:::

1. A flip-flop reads an input correctly only if it has been steady for t_su before the edge.
2. An input that changes **at** the edge was steady, before the edge, at its **old** value.
3. So the flip-flop reads the old value: J = 0 at ↑1 and ↑3, K = 1 at ↑2.

:::note Two readings of MTE Q7
Edges ↑1, ↑2, ↑3 have an input changing at the same instant. This pack uses the setup-time rule above (value just before the edge), the rule of real flip-flops. Some answer keys read the level drawn just **after** the edge instead, which gives Q = 1, 1, 1, 1, 1, 0, 1 after ↑1–↑7 (step 3 gives 0, 0, 0, 0, 1, 0, 1). In the exam, **write the rule you use in one line above the drawing**: either answer is then consistent.
:::

**Answer to the guess.** **J = 0**: J was 0 for the whole setup time before ↑1; its rise comes too late for that edge.

:::check Check 2
(a) At ↑2, K falls 1 → 0 at the edge. Which K does the flip-flop read? (b) Which input changes exactly at ↑3, and which value is read?
:::

### 3 · Positive edge: MTE 2025 Q7 worked

Steps 1 and 2 give everything the question needs: seven edges, the inputs just before each, the JK table of file 09 step 9.

:::q <span class="tag">MTE 2025 Q7 · 4 marks</span>
Draw the output waveform for the following input waveform, assuming the flip-flop to be positive edge triggered and the output Q is initially at logic zero.
:::

:::guess Guess first
At how many of the seven edges does Q change? Count before reading the table.
:::

:::note Terms
**Set / reset / hold / toggle:** the four JK rows (10, 01, 00, 11) of file 09 step 9.
:::

| Edge | ↑1 | ↑2 | ↑3 | ↑4 | ↑5 | ↑6 | ↑7 |
|---|---|---|---|---|---|---|---|
| J K just before | 0 0 | 0 1 | 0 0 | 0 0 | 1 0 | 0 1 | 1 1 |
| action | hold | reset | hold | hold | set | reset | toggle |
| Q after (Q₀ = 0) | 0 | 0 | 0 | 0 | 1 | 0 | 1 |

[[fig:u3_mte7|The answer. What this graph plots: time across; rows CLK, J, K, Q (high = 1). Q changes only on the numbered ↑ lines: up at ↑5, down at ↑6, up at ↑7.|w=80]]

**Answer.** Q stays **0 through ↑1–↑4**, goes **1 at ↑5** (set), **0 at ↑6** (reset), **1 at ↑7** (toggle), and stays 1 to the end. Q changes at **3** of the 7 edges. (With the after-the-edge reading of step 2's note: 1, 1, 1, 1, 1, 0, 1.)

:::check Check 3
(a) Redo ↑4 if J had risen just before ↑4 instead of in the middle of pulse 4. (b) If Q had started at 1, what would Q be after ↑1, ↑2 and ↑3?
:::

### 4 · Negative edge: the same inputs, read at ↓

A bubble before the clock ▷ moves every sampling line to the falling edges. Nothing else in the procedure changes.

:::q <span class="tag">Practice set 2 Q3 (a)</span>
Input waveforms for JK flip-flops are shown in given figures. Draw the output waveform for each case. Assume the flip-flops to be negative edge triggered for both cases and the output Q is initially at logic zero.
:::

:::guess Guess first
Practice set 2 Q3(a) uses the same CLK, J and K as MTE Q7. Will Q change at more or fewer edges than in step 3?
:::

:::note Terms
**Negative-edge triggered:** acts at ↓ (1 → 0) only.
:::

| Edge | ↓1 | ↓2 | ↓3 | ↓4 | ↓5 | ↓6 | ↓7 |
|---|---|---|---|---|---|---|---|
| J K just before | 1 0 | 0 1 | 1 0 | 1 0 | 1 1 | 0 1 | 1 1 |
| action | set | reset | set | set | toggle | reset | toggle |
| Q after (Q₀ = 0) | 1 | 0 | 1 | 1 | 0 | 0 | 1 |

[[fig:u3_ps2q3a|The answer for practice set 2 Q3(a). What this graph plots: time across; rows CLK, J, K, Q (high = 1). Dotted lines mark the falling edges ↓1–↓7; Q changes only on them.|w=80]]

Here too inputs change at edges (J falls at ↓1, ↓3, ↓5 and ↓7; K at ↓5 and ↓7; J rises at ↓6): by step 2's rule the value **before** the fall is read. For these falling edges that is the level drawn during the high half, the natural reading of the picture.

**Answer.** **Q = 1, 0, 1, 1, 0, 0, 1** after ↓1–↓7: Q changes at **5** edges, more than the 3 of step 3.

:::check Check 4
(a) At ↓6, J rises exactly at the edge. Which J is read, and what would Q be after ↓6 with the other value? (b) Where does Q stand between ↓4 and ↓5, whatever J and K do?
:::

### 5 · The D latch: transparent while enabled

A latch has no sampling lines. While EN = 1 it follows its table **continuously**; while EN = 0 it holds (file 09 step 5).

:::q <span class="tag">Practice set 2 Q2 (D latch)</span>
Complete the timing diagrams for D Latch and JK Latch. Assume the latch to be high level triggered for both cases and the output Q is initially at logic one.
:::

:::guess Guess first
The first enable window opens while D = 0. What happens to Q (which starts at 1) at that instant?
:::

:::note Terms
**Enable window:** a stretch of time with EN = 1. **High-level triggered:** transparent while EN = 1 (a low-level latch is transparent while EN = 0).
:::

**The latch procedure:**

1. Shade every enable window.
2. Inside a window, Q = D at every instant (D latch), including the instant the window opens.
3. Outside, Q holds the value it had when the window closed.

[[fig:u3_ps2q2d|The answer for the D latch. What this graph plots: time across (one grid square = one unit of the question's grid, 26 squares); rows EN, D, Q (high = 1). Shaded = EN high: inside, Q copies D; outside, Q is flat.|w=82]]

| Window (grid squares) | D inside | Q inside | Q held after |
|---|---|---|---|
| before the first window | — | 1 (initial) | — |
| 1–6 | 0, 1, 0, 1 | 0, 1, 0, 1 | 1 |
| 9–10 | 0 | 0 | 0 |
| 13–17 | 0, then 1 in square 17 | 0, then 1 | 1 |
| 23–26 | 1 | 1 | 1 |

**Answer.** Q drops **1 → 0** the moment the first window opens (it copies D = 0). Over the whole diagram: Q = 0 in squares 1–2, 1 in 3–4, 0 in 5, 1 in 6–8, 0 in 9–16, 1 from square 17 to the end. D's fall in square 8 and its rise in square 21 come while EN = 0, so Q ignores them (it holds 1, then 1 again).

:::check Check 5
(a) A positive-edge D flip-flop clocked by the same EN (its ↑ at squares 1, 9, 13, 23): Q after each ↑? (b) Why does the D latch answer change inside window 1 but the flip-flop's cannot?
:::

### 6 · The JK latch: transparent, and the race-around window

The JK latch obeys the JK table the whole time EN = 1. That works for set, reset and hold; J = K = 1 inside a window is file 09 step 11's race-around.

:::q <span class="tag">Practice set 2 Q2 (JK latch)</span>
Complete the timing diagrams for D Latch and JK Latch. Assume the latch to be high level triggered for both cases and the output Q is initially at logic one.
:::

:::guess Guess first
In the last window J and K are both 1 for two squares. What should you draw for Q there?
:::

:::note Terms
**Race-around (recalled from 09 step 11):** with J = K = 1 and the enable held high for longer than the loop delay, Q toggles repeatedly; its value when the window closes cannot be predicted.
:::

[[fig:u3_ps2q2jk|The answer for the JK latch. What this graph plots: time across (26 grid squares); rows EN, J, K, Q (high = 1). Green = EN high; red = the race-around stretch, where Q oscillates.|w=82]]

| Window (squares) | J K inside | Q |
|---|---|---|
| 1–6 | 10 (squares 1–2), 00, 01 (square 4), 00, 01 | 1 → **0 at square 4**, stays 0 |
| 7–12 (closed) | — | holds 0 |
| 13–16 | 00, then 10 (squares 15–16) | 0 → **1 at square 15** |
| 17–22 (closed) | — | holds 1 |
| 23–26 | 01 (squares 23–24), then 11 (squares 25–26) | **0 at square 23**, then **oscillates** in 25–26 |

**Answer.** Q = 1 in squares 1–3, 0 in 4–14, 1 in 15–22, 0 in 23–24; in squares 25–26 (J = K = 1 with EN = 1) Q **toggles repeatedly** (race-around), and its value after EN falls at square 26 is **unpredictable**. Draw it as rapid toggling and label it "race-around".

:::check Check 6
(a) In window 1, why does Q not go back to 1 in square 5? (b) What would a positive-edge JK flip-flop clocked by EN give at the ↑ of the last window (J K = 01 just before it)?
:::

### 7 · Asynchronous clear and preset

Some flip-flops have two extra inputs that act **without** the clock, to force a known state (at power-up, or a counter reset in file 12).

:::q <span class="tag">Practice set 2 Q3 (b)</span>
Input waveforms for JK flip-flops are shown in given figures. Draw the output waveform for each case. Assume the flip-flops to be negative edge triggered for both cases and the output Q is initially at logic zero. (Figure b adds active-low CLR and PR.)
:::

:::guess Guess first
PR' drops to 0 for a moment in the middle of pulse 4's high time. What happens to Q at that instant, and does it wait for the next ↓?
:::

:::note Terms
**Asynchronous (direct) input:** acts the instant it is asserted, not at a clock edge. **CLR' (clear):** 0 forces Q = 0. **PR' (preset):** 0 forces Q = 1. Both are idle at 1 and override J, K and the clock while asserted (KB 03 §3).
:::

[[fig:u3_ps2q3b|The answer for practice set 2 Q3(b). What this graph plots: time across; rows CLK, J, K, CLR', PR', Q (high = 1). CLR' and PR' are active-low pulses; dotted lines mark ↓1–↓7.|w=82]]

| Event | Inputs | Q after |
|---|---|---|
| CLR' pulse before pulse 1 | forces 0 | 0 |
| ↓1, ↓2, ↓3 | J K = 10, 01, 10 | 1, 0, 1 |
| PR' pulse inside pulse 4 | forces 1 | 1 (already 1) |
| ↓4 | 10 | 1 |
| ↓5 | 11 (toggle) | 0 |
| CLR' pulse across ↑6 | forces 0 | 0 (already 0) |
| ↓6, ↓7 | 01, 11 | 0, 1 |

The J, K and CLK waveforms are those of Q3(a), so the edge actions match step 4; the two later pulses arrive when Q already has the value they force, so they leave no mark on Q.

**Answer to the guess.** Q is forced to 1 **at that instant**, not at the next ↓. Here Q is already 1 (set at ↓3), so nothing visible happens. Q after ↓1–↓7 = **1, 0, 1, 1, 0, 0, 1**.

:::check Check 7
(a) If the PR' pulse came just after ↓2 instead (Q = 0 then), sketch what Q does until ↓3. (b) CLR' is held at 0 across a ↓ with J K = 10. Q after that edge?
:::

---

## Exam form

**Edge-triggered (flip-flop).**
1. State the edge type and Q₀.
2. Dotted line at every active edge (↑ for ▷, ↓ for a bubble), numbered.
3. Table: inputs just before each edge (an input changing at the edge counts at its old value: setup time; write this rule on the sheet) → action → Q after.
4. Draw Q flat between lines.

**Level-triggered (latch).**
1. Shade the enable windows.
2. Inside: Q follows the table continuously (D latch: Q = D; JK latch: set, reset, hold; J = K = 1 → race-around, draw oscillation, value at closing unknown).
3. Outside: Q holds.

**Asynchronous inputs.** CLR' = 0 forces Q = 0, PR' = 0 forces Q = 1, at once and for as long as asserted; edges resume afterwards.

**MTE 2025 Q7 (positive-edge JK, Q₀ = 0):** Q after ↑1–↑7 = 0, 0, 0, 0, 1, 0, 1.

## Traps

- Reading the inputs after the edge instead of just before it (or switching rules halfway through a diagram).
- Letting a flip-flop's Q change between edges: only a latch does that.
- Using rising edges when the clock pin has a bubble.
- Drawing a latch as if edge-sampled: inside a window Q follows every input change, including at the instant the window opens.
- Drawing a clean toggle for a JK latch with J = K = 1: it races.
- Waiting for the next edge after CLR' or PR' goes active.

## Self-test

1. Positive-edge D flip-flop, D just before four edges = 1, 0, 0, 1. Q after each?
2. Negative-edge T flip-flop, Q₀ = 1, T just before four ↓ = 1, 1, 0, 1. Q after each?
3. Positive-edge SR flip-flop, Q₀ = 0, S R just before four ↑ = 10, 00, 01, 00. Q after each?
4. A D latch and a D flip-flop get the same D and the same clock. In one line, how do their Q waveforms differ?
5. A JK flip-flop with J = K = 1 is clocked at 8 kHz. Frequency of Q?
6. MTE Q7 again, but Q₀ = 1. Q after ↑1–↑7?

<!--ANSWERS-->

## Answers

**Check 1.** (a) Before ↓1 … ↓6, D = **1, 0, 1, 0, 1, 0**: three of the four D pulses span a falling edge, so the negative-edge flip-flop catches them; the short one inside high time 3 ends before ↓3 and is missed. (b) **None**: Q can change only at an active edge.

**Check 2.** (a) **K = 1** (its old value). (b) **J** rises at ↑3; **J = 0** is read.

**Check 3.** (a) J K = 10 at ↑4 → set: Q = **1 from ↑4** (and still 1 after ↑5, since ↑5 is also a set). (b) ↑1: hold → **1**; ↑2: reset → **0**; ↑3: hold → **0**.

**Check 4.** (a) **J = 0** is read (with K = 1: reset, Q = 0). With J = 1, J K = 11 would toggle Q from 0 to **1**. (b) **Flat at 1** (the value set at ↓4).

**Check 5.** (a) EN's ↑ at squares 1, 9, 13, 23 (D just before = 0, 0, 0, 1): Q = **0, 0, 0, 1**. (b) The latch is transparent for the whole window; the flip-flop reads D only once, at the ↑.

**Check 6.** (a) In square 5 J K = 00 (hold), and in square 6 J K = 01 (reset): **nothing sets it**. (b) J K = 01 → **Q = 0** (reset), a clean single change.

**Check 7.** (a) Q jumps to **1 at the PR' pulse** and stays 1; at ↓3 J K = 10 sets it, so it is still 1. (b) **Q = 0**: CLR' overrides the set.

**Self-test.**

1. **1, 0, 0, 1.**
2. **0, 1, 1, 0.**
3. **1, 1, 0, 0.**
4. The latch's Q follows D during the whole high time; the flip-flop's Q changes only at the edges, to the D just before each.
5. **4 kHz** (Q toggles at each active edge: half the clock frequency).
6. ↑1: hold → **1**; ↑2: reset → **0**; then as in step 3: **0, 0, 1, 0, 1**. Full list: **1, 0, 0, 0, 1, 0, 1**.

<!--/ANSWERS-->
