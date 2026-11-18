# 14 — Timing analysis

<div class="sub">Syllabus Unit 3 (timing analysis of sequential circuits) · no deck covers it: built from KB 03 §6 and its sources · no real question in the papers: Predict prompts · needs 09 (the D flip-flop and its edge), 12 step on ripple delay, 13 step 1 (synchronous counter)</div>

## Map

[[map:1 Clock-to-Q delay > 2 Setup time > 3 Hold time > 4 Metastability > 5 Longest path and f_max > 6 Shortest path and hold > 7 Clock skew > 8 Counters compared|here=1]]

Files 09–13 treated a flip-flop as perfect: it copies D at the edge, instantly. File 12 already met one real delay (a ripple counter's stages settle one after another). This file gives every flip-flop three timing numbers and every logic path two, and turns them into the two rules a synchronous circuit must obey: the clock may not be too fast (setup), and the fastest path may not be too fast (hold). Files 15–17 build machines that obey them.

## Symbols

| Symbol | What it means in this file | Typical value |
|---|---|---|
| t_{pd} | clock-to-Q delay: time from the clock edge until Q shows its new value; set by the flip-flop's transistors | 8 ns |
| t_{su} | setup time: how long D must be steady before the edge for the flip-flop to read it reliably | 3 ns |
| t_{h} | hold time: how long D must stay steady after the edge | 2 ns |
| t_{comb,max}, t_{comb,min} | delay of the slowest and of the fastest gate path between two flip-flops: sum of the gate delays along it | 12 ns, 1 ns |
| T, f | clock period and frequency, f = 1/T | 25 ns, 40 MHz |
| T_{min}, f_{max} | smallest period (largest frequency) the circuit works at | 23 ns, 43.5 MHz |
| δ | clock skew: how much later the clock edge reaches the capturing flip-flop than the launching one (negative = earlier) | 0 – 3 ns |

## Running example

**One flip-flop → logic → flip-flop path** with t_{pd} = 8 ns, t_{su} = 3 ns, t_{h} = 2 ns, t_{comb,max} = 12 ns, t_{comb,min} = 1 ns (KB 03 §6). Steps 1–7 all use it; step 8 applies the same sums to the counters of files 12 and 13.

## The questions this file answers

- <span class="tag">Predict (exam pattern, KB 03 §6)</span> Given t_{pd}, t_{su}, t_{h} and the longest and shortest logic delays, find f_{max} and check the hold time.
- <span class="tag">Predict</span> How does clock skew change f_{max} and the hold check?
- <span class="tag">Predict</span> Compare the maximum clock of a ripple counter (file 12) and a synchronous counter (file 13).

---

## Build

### 1 · Clock-to-Q delay: the output is late

A flip-flop is a camera pointed at its D input: at the clock edge it takes a picture, and Q shows the picture. Like a real camera, it needs a moment before the picture is ready.

:::guess Predict
A D flip-flop with t_{pd} = 8 ns is clocked at 50 MHz. D went to 1 long before the edge at 10 ns. When does Q go to 1, and what fraction of a clock period has passed by then?
:::

:::note Terms
**Propagation delay t_{pd} (clock-to-Q):** the time from the active clock edge until Q shows the new value; the transistors inside need it to switch, so it is fixed by the chip (data-sheet number). **Clock period T:** the time from one rising edge to the next, T = 1/f.
:::

[[fig:u3r_tpd|What this graph plots: time across (ns), one row per signal, high = 1. The clock rises at 10 ns and 30 ns (period 20 ns, 50 MHz). D is already 1; Q follows only 8 ns after the edge.|w=70]]

| Time (ns) | CLK | D | Q |
|---|---|---|---|
| 5 | 0 | 1 | 0 (old value) |
| 10 | rising edge | 1 | 0: the picture is taken, not yet shown |
| 18 | 1 | 1 | **1** (10 + t_{pd}) |
| 25 | 0 | 1 | 1 |

Every signal that comes from a flip-flop is therefore t_{pd} late, and anything that uses Q (the logic of step 5, the next stage of a ripple counter) starts only then.

**Answer to the Predict.** T = 1/50 MHz = 20 ns. Q goes to 1 at 10 + 8 = **18 ns**, **40 %** of the period after the edge.

:::check Check 1
(a) The same flip-flop is clocked at 100 MHz. What fraction of the period does t_{pd} take now? (b) Why does the next flip-flop in a chain not see the new Q at the same edge?
:::

### 2 · Setup time: D must be steady before the edge

Step 1 said the camera takes the picture at the edge. A picture of something moving is blurred; the flip-flop's "picture" needs D to stand still for a moment first.

:::guess Predict
D changes 1 ns before the edge, and the flip-flop's data sheet says t_{su} = 3 ns. Is the new D reliably stored?
:::

:::note Terms
**Setup time t_{su}:** the time before the clock edge during which D must not change; inside the flip-flop the new value needs this long to reach the part that stores it.
:::

[[fig:setup_hold|What this graph plots: time across, rows CLK and D. The shaded window around the rising edge is where D must not change: it starts t_{su} before the edge and ends t_{h} after it.|w=60]]

The rule reads: **the last change of D must happen at least t_{su} before the edge**. With t_{su} = 3 ns and an edge at 20 ns, D may change up to 17 ns and not later. Setup is broken when the data arrives late: when the path feeding D is slow, or the clock is fast (step 5).

**Answer to the Predict.** **No.** 1 ns before the edge is inside the 3 ns setup window: the flip-flop may store the old value, the new one, or neither (step 4).

:::check Check 2
The edge is at 40 ns and t_{su} = 3 ns. Which of these D changes are safe: at 30 ns, 37 ns, 38.5 ns?
:::

### 3 · Hold time: D must stay steady after the edge

The camera's shutter does not close at the exact instant of the edge either: D must stay still a little after it.

:::guess Predict
D changes 1 ns after the edge, and t_{h} = 2 ns. Is the value present at the edge stored safely?
:::

:::note Terms
**Hold time t_{h}:** the time after the clock edge during which D must not change; the flip-flop's input is still being closed off during it.
:::

Same figure as step 2: the hold part of the window runs from the edge to t_{h} after it. The rule reads: **the first change of D after an edge must come at least t_{h} after that edge**. Hold is broken when new data arrives too *early*: in step 6 this happens when the path from the previous flip-flop is very short.

| D changes at (edge at 20 ns, t_{su} = 3, t_{h} = 2) | inside the window 17–22 ns? |
|---|---|
| 15 ns | no: safe |
| 18 ns | yes: setup broken |
| 21 ns | yes: hold broken |
| 23 ns | no: safe (it is read at the next edge) |

**Answer to the Predict.** **No.** 1 ns after the edge is inside the 2 ns hold window.

:::check Check 3
Edge at 20 ns, t_{su} = 3 ns, t_{h} = 2 ns. How long is the window in which D must not change, and from when to when?
:::

### 4 · Metastability: what happens when the window is broken

Steps 2 and 3 said "not reliably stored". Here is what the flip-flop actually does then.

:::guess Predict
D changes exactly at the edge. Name three things Q could do.
:::

:::note Terms
**Metastability:** the state of a flip-flop whose setup or hold was broken: Q sits at a level between 0 and 1 for a time that cannot be predicted, then falls to 0 or 1 at random.
:::

[[fig:u3r_meta|What this graph plots: time across (ns). Top: CLK rising at 10 ns with the setup + hold window shaded. Bottom: Q when D changed inside the window: it rises only to the middle (shaded: neither 0 nor 1), stays there, and later resolves to 1 (solid) or 0 (dotted).|w=70]]

A flip-flop stores a bit in two cross-coupled gates (file 09's latch), which settle in one of two stable states. Between them is a balance point, like a ball on top of a hill: a D change caught by the edge can leave the gates near that point, and they take an unbounded time to roll off to one side. Logic reading Q meanwhile may see 0, 1 or a level that some gates read as 1 and others as 0.

The cure is never "hope": obey setup and hold everywhere (steps 5–6), and pass a signal from outside the clock's control through a synchronizer first (file 17).

**Answer to the Predict.** Q may (1) take the new value, (2) keep the old one, or (3) go **metastable**: hang between 0 and 1 for an unknown time before resolving to either.

:::check Check 4
Why is metastability worse than simply storing the wrong bit?
:::

### 5 · The longest path sets f_{max}

Steps 1–2 gave two pieces: data leaves a flip-flop t_{pd} after an edge, and must arrive at the next flip-flop t_{su} before the following edge. Between them sits the logic.

:::guess Predict
Running example: t_{pd} = 8 ns, slowest logic path 12 ns, t_{su} = 3 ns. What is the shortest clock period that works? Will it run at 40 MHz? At 50 MHz?
:::

:::note Terms
**Launching / capturing flip-flop:** the flip-flop whose Q starts a path, and the one whose D ends it; both are clocked by the same edge train. **Longest (critical) path:** the slowest chain of gates between them, delay t_{comb,max}.
:::

[[fig:timing_path|Flip-flop → logic → flip-flop on one clock: the launching flip-flop's Q goes through the logic into the capturing flip-flop's D.|w=70]]

[[fig:u3r_budget|What this graph plots: time after the launching edge (ns). The bars are the delays the data meets in turn: t_{pd} (8), the slowest logic (12), and the setup time the capturing flip-flop needs (3). A vertical line is the next clock edge: at 40 MHz (25 ns) the bars fit with 2 ns spare; at 50 MHz (20 ns) the edge comes too early.|w=80]]

Put the pieces together, line by line:

1. At the edge at time 0 the launching flip-flop's Q changes at t_{pd} (step 1).
2. The change passes the slowest logic: it reaches the capturing D at t_{pd} + t_{comb,max}.
3. The capturing flip-flop needs it t_{su} before *its* next edge, at T (step 2): t_{pd} + t_{comb,max} ≤ T − t_{su}.
4. So **T ≥ t_{pd} + t_{comb,max} + t_{su}**, and **f_{max} = 1 / (t_{pd} + t_{comb,max} + t_{su})**.

Read in words: *one clock period must cover the flip-flop's delay, the slowest logic, and the next flip-flop's setup time.* If the circuit fails setup, slowing the clock fixes it.

| Clock | T (ns) | data ready (ns) = T_{min} | spare |
|---|---|---|---|
| 40 MHz | 25 | 23 | 2 ns: works |
| 43.5 MHz | 23 | 23 | 0: the limit |
| 50 MHz | 20 | 23 | −3 ns: fails |

**Answer to the Predict.** T_{min} = 8 + 12 + 3 = **23 ns**, f_{max} = 1 / 23 ns = **43.5 MHz**. 40 MHz works (2 ns spare); 50 MHz fails (3 ns short).

:::check Check 5
The longest path gains 4 ns (another gate). New T_{min} and f_{max}?
:::

### 6 · The shortest path and the hold check

Step 5 asked whether data arrives soon enough. Step 3 raises the opposite worry: at the same edge that the capturing flip-flop reads its D, the launching flip-flop starts sending the *next* value. It must not arrive before the hold window closes.

:::guess Predict
Running example: the fastest path from launching Q to capturing D has 1 ns of logic. t_{pd} = 8 ns, t_{h} = 2 ns. Is hold met? Would slowing the clock help if it were not?
:::

:::note Terms
**Shortest path:** the fastest chain of gates between the two flip-flops, delay t_{comb,min}; it may be a plain wire (0 ns).
:::

[[fig:u3r_hold0|What this graph plots: time after one clock edge (ns). Shaded: the hold window 0–2 ns in which the capturing flip-flop still reads its old D. Bars: the new value's trip, t_{pd} (8) then the fastest logic (1). It arrives at 9 ns, after the window.|w=70]]

1. At the edge (time 0) the capturing flip-flop reads D; it needs D unchanged until t_{h} (step 3).
2. At the same edge the launching flip-flop's new Q appears at t_{pd}, and through the fastest logic reaches D at t_{pd} + t_{comb,min}.
3. Safe if it arrives after the window: **t_{pd} + t_{comb,min} ≥ t_{h}**.

Read in words: *the fastest new data must not overtake the hold time.* Both sides are measured from the **same** edge, so **T does not appear**: slowing the clock cannot fix a hold violation. The fix is to add delay (buffers) in the short path.

**Answer to the Predict.** 8 + 1 = **9 ns ≥ 2 ns: hold met**, with 7 ns spare. No: the clock period is not in the inequality, so slowing the clock would not help.

:::check Check 6
t_{pd} = 2 ns, shortest logic 0.5 ns, t_{h} = 3 ns. Is hold met? If not, what is the fix and how much?
:::

### 7 · Clock skew: the two edges do not arrive together

Steps 5 and 6 assumed both flip-flops see the edge at the same instant. On a real board the clock wire is longer to some flip-flops than to others.

:::guess Predict
The capturing flip-flop's clock arrives 3 ns after the launching one's. Does that help setup or hurt it? Does it help hold or hurt it?
:::

:::note Terms
**Clock skew δ:** how much later the clock edge reaches the capturing flip-flop than the launching one; set by wire lengths and buffers in the clock path. Positive = capture late, negative = capture early.
:::

[[fig:u3r_skew3|What this graph plots: time across (ns). CLK1 clocks the launching flip-flop (edges at 0, 20); CLK2 is the capturing flip-flop's clock, 3 ns late (edges at 3, 23). The bar is the data path from CLK1's edge: t_{pd}, the slowest logic, and t_{su} before CLK2's edge. With T = 20 ns it just fits.|w=80]]

Redo steps 5 and 6 with the capturing edges moved δ later:

1. Setup: the data must be ready t_{su} before the capturing edge, now at T + δ: t_{pd} + t_{comb,max} + t_{su} ≤ T + δ, so **T ≥ t_{pd} + t_{comb,max} + t_{su} − δ**.
2. Hold: the capturing flip-flop's hold window now ends at δ + t_{h}: **t_{pd} + t_{comb,min} ≥ t_{h} + δ**.

*A late capture clock gives the slow data more time but keeps the hold window open longer for the fast data.* An early capture clock (δ &lt; 0) does the reverse. When the sign is unknown, designers assume the worst for each: + |δ| on the setup side and + |δ| on the hold side (UCSD CSE140 and Cornell ECE4740 timing notes, KB 03 §6).

[[fig:u3r_hold8|What this graph plots: time after the launching edge (ns). The capturing edge is 8 ns late, so its hold window is 8–10 ns. The fastest new data still arrives at 9 ns: inside the window, hold violated.|w=70]]

| Skew δ | T_{min} = 23 − δ | f_{max} | hold: 9 ≥ 2 + δ? |
|---|---|---|---|
| −3 ns | 26 ns | 38.5 MHz | 9 ≥ −1: met |
| 0 | 23 ns | 43.5 MHz | 9 ≥ 2: met |
| +3 ns | 20 ns | 50 MHz | 9 ≥ 5: met |
| +8 ns | 15 ns | 66.7 MHz | 9 ≥ 10: **violated by 1 ns** |

At δ = +8 ns, again the clock cannot fix it: add at least 1 ns to the short path. A 2 ns buffer gives 8 + 3 = 11 ≥ 10 and leaves the slow path untouched.

**Answer to the Predict.** A late capture clock **helps setup** (T_{min} falls from 23 to 20 ns, f_{max} rises to 50 MHz) and **hurts hold** (the 9 ns arrival must now beat 2 + 3 = 5 ns; it still does).

:::check Check 7
Running example with δ = +7 ns. Is hold met? What are T_{min} and f_{max}?
:::

### 8 · Counters compared: ripple against synchronous

Files 12 and 13 built the same counts two ways. Step 5's sum now says which one can be clocked faster.

:::guess Predict
4-bit counters with t_{pd} = 10 ns: a ripple counter (file 12), and a synchronous counter with one 5 ns AND gate before each T input and t_{su} = 5 ns (file 13). Which has the higher f_{max}, and what happens to each at 8 bits?
:::

:::note Terms
**Settling time of a ripple counter:** the time for a change to pass through all n stages, n · t_{pd}, since each stage is clocked by the one before (file 12).
:::

| Counter | What one clock period must cover | 4 bits | 8 bits |
|---|---|---|---|
| ripple | every stage in turn: n · t_{pd} | 40 ns, **25 MHz** | 80 ns, **12.5 MHz** |
| synchronous | one flip-flop, one gate level, setup: t_{pd} + t_{AND} + t_{su} | 20 ns, **50 MHz** | 20 ns, **50 MHz** (if the enables stay one gate deep) |

The ripple counter's period grows with every stage, because the stages wait for each other. The synchronous counter's flip-flops all switch t_{pd} after the same edge, so its period is step 5's single path, whatever n is (as long as the AND gates feeding the T inputs stay one level deep, file 13).

**Answer to the Predict.** The **synchronous** counter: **50 MHz** against 25 MHz at 4 bits; at 8 bits the ripple counter drops to **12.5 MHz** while the synchronous one stays at 50 MHz.

:::check Check 8
A 3-bit ripple counter uses flip-flops with t_{pd} = 20 ns. What is its f_{max}, and what would a synchronous version with a 5 ns AND and t_{su} = 5 ns reach?
:::

---

## Exam form

**Definitions (with one timing sketch: CLK, D with the shaded window, Q late by t_{pd}).** t_{pd}: edge to valid Q. t_{su}: D steady before the edge. t_{h}: D steady after the edge. Metastability: setup or hold broken → Q between 0 and 1 for an unknown time, then random.

**f_{max} (setup, longest path).**
1. T ≥ t_{pd} + t_{comb,max} + t_{su}.
2. f_{max} = 1 / (t_{pd} + t_{comb,max} + t_{su}).

**Hold check (shortest path).** t_{pd} + t_{comb,min} ≥ t_{h}; T is not in it, so the fix is delay in the short path, never a slower clock.

**With skew δ (capture late = positive).** T ≥ t_{pd} + t_{comb,max} + t_{su} − δ; t_{pd} + t_{comb,min} ≥ t_{h} + δ.

**Counters.** Ripple f_{max} = 1 / (n · t_{pd}); synchronous f_{max} = 1 / (t_{pd} + t_{gate} + t_{su}).

## Traps

- Leaving t_{pd} or t_{su} out of the period.
- Using the longest path for the hold check (it needs the shortest).
- Trying to fix a hold violation by slowing the clock.
- Getting the skew sign backwards: a late capture clock helps setup and hurts hold.
- Using one t_{pd} for a ripple counter: it is n · t_{pd}.

## Self-test

1. t_{pd} = 5 ns, longest logic 10 ns, t_{su} = 2 ns. f_{max}?
2. t_{pd} = 2 ns, shortest logic 0.5 ns, t_{h} = 3 ns. Is hold met?
3. Why can't a slower clock fix a hold violation?
4. t_{pd} = 6 ns, longest logic 9 ns, shortest 1 ns, t_{su} = 2 ns, t_{h} = 1 ns, capture clock 2 ns late. Find T_{min}, f_{max}, and check hold.
5. A design must run at 100 MHz with t_{pd} = 4 ns and t_{su} = 2 ns. What is the most logic delay allowed between two flip-flops?
6. Name the three things a flip-flop's Q can do when D changes inside the setup–hold window.

<!--ANSWERS-->

## Answers

**Check 1.** (a) T = 10 ns: 8/10 = **80 %**. (b) It reads D at the edge, and the new Q appears only t_{pd} later; it is read at the following edge.

**Check 2.** Window 37–40 ns before the edge: **30 ns safe**; 37 ns is exactly at the limit (safe, just); **38.5 ns breaks setup**.

**Check 3.** t_{su} + t_{h} = **5 ns**, from **17 ns to 22 ns**.

**Check 4.** A wrong bit is at least a valid 0 or 1 that every gate reads the same way. A metastable Q may be read as 1 by one gate and 0 by another, and it settles at an unknown time, possibly after the next edge.

**Check 5.** 8 + 16 + 3 = **27 ns**, f_{max} = **37.0 MHz**. The hold check does not change: it uses the shortest path.

**Check 6.** 2 + 0.5 = 2.5 ns &lt; 3 ns: **violated**. Add at least **0.5 ns** of delay to the short path.

**Check 7.** Hold: 9 ≥ 2 + 7 = 9: **met, with no margin**. T_{min} = 23 − 7 = **16 ns**, f_{max} = **62.5 MHz**.

**Check 8.** Ripple: 3 × 20 = 60 ns, **16.7 MHz**. Synchronous: 20 + 5 + 5 = 30 ns, **33.3 MHz**.

**Self-test.**

1. 5 + 10 + 2 = 17 ns: **58.8 MHz**.
2. 2 + 0.5 = 2.5 &lt; 3: **no**, violated by 0.5 ns.
3. Hold compares two delays measured from the same edge; the period does not appear in t_{pd} + t_{comb,min} ≥ t_{h}.
4. T_{min} = 6 + 9 + 2 − 2 = **15 ns**, f_{max} = **66.7 MHz**. Hold: 6 + 1 = 7 ≥ 1 + 2 = 3: **met**.
5. T = 10 ns: 4 + t_{comb} + 2 ≤ 10, so **t_{comb,max} ≤ 4 ns**.
6. Take the new value, keep the old one, or go **metastable** (hang between 0 and 1, then resolve at random).

<!--/ANSWERS-->
