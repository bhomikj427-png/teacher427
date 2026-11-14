# 14 — Timing analysis

<div class="sub">Syllabus Unit 3 item with no deck coverage: practice questions only · needs 09 (flip-flops) and 13 (synchronous circuits)</div>

## Map

[[map:1 Setup, hold, propagation delay > 2 f_{max} and the hold check|here=1]]

Every synchronous circuit is flip-flops with logic between them. How fast can its clock run? Three numbers per flip-flop and two per logic path answer it.

## The questions this file answers

- <span class="tag">practice</span> t_{pd} = 8 ns, t_{su} = 3 ns, t_{h} = 2 ns, logic 12 ns longest and 1 ns shortest. Find f_{max} and check hold.
- <span class="tag">practice</span> Compare the maximum clock of a ripple counter (12) and a synchronous counter (13).

---

## Build

### 1 · Setup, hold and propagation delay

:::guess Predict
A D flip-flop samples at the edge. What do you think happens if D is changing at exactly that instant?
:::

[[fig:setup_hold|D must be steady from t_{su} before the edge to t_{h} after it.|w=60]]

:::note Terms
**Setup time t_{su}:** D must be steady this long before the edge. **Hold time t_{h}:** and this long after. **Propagation delay t_{pd}:** edge to valid Q. **Metastability:** if setup or hold is broken, Q can hang between 0 and 1 for an unpredictable time.
:::

**Answer.** The flip-flop may go **metastable**: an in-between output that resolves to 0 or 1 after an unknown time (17 shows the synchronizer that guards against it).

:::check Check 1
Define t_{su}, t_{h} and t_{pd} in one line each, with a sketch.
:::

### 2 · f_{max} and the hold check

:::q <span class="tag">practice</span>
A synchronous circuit has t_{pd} = 8 ns, t_{su} = 3 ns, t_{h} = 2 ns, and combinational delays of 12 ns (longest path) and 1 ns (shortest). Find the maximum clock frequency and check the hold time.
:::

:::guess Guess first
Data leaves one flip-flop at an edge. By when must it reach the next one?
:::

[[fig:timing_path|Flip-flop → logic → flip-flop on one clock.|w=70]]

**Setup (longest path):** launched at one edge, the data must pass the flip-flop and the slowest logic and arrive t_{su} before the next edge:

$$T_{clk} ≥ t_{pd} + t_{comb,max} + t_{su}      f_{max} = 1/T_{clk,min}$$

**Hold (shortest path):** the new data must not arrive while the next flip-flop is still holding: **t_{pd} + t_{comb,min} ≥ t_{h}**. The period is not in this inequality, so **slowing the clock cannot fix a hold violation**: add delay to the short path.

**Answer.** T_{min} = 8 + 12 + 3 = **23 ns**, **f_{max} = 43.5 MHz**. Hold: 8 + 1 = 9 ns ≥ 2 ns ✓.

:::check Check 2
(a) The longest path gains 4 ns. New f_{max}? Does the hold check change? (b) A synchronous counter has t_{pd} = 10 ns, one 5 ns AND gate between flip-flops, t_{su} = 5 ns. f_{max}?
:::

---

## Exam form

Define t_{su}, t_{h}, t_{pd}, metastability with a timing sketch. Setup inequality → f_{max}. Hold inequality and why the clock does not appear. Ripple counter f_{max} = 1/(n·t_{pd}) for comparison.

## Traps

- Leaving out t_{pd} or t_{su} from the period.
- Using the longest path for the hold check.
- Trying to fix hold by slowing the clock.

## Self-test

1. t_{pd} = 5 ns, longest logic 10 ns, t_{su} = 2 ns. f_{max}?
2. t_{pd} = 2 ns, shortest logic 0.5 ns, t_{h} = 3 ns. Is hold met? If not, what is the fix?
3. Why can't a slower clock fix a hold violation?
4. Compare f_{max} of a 4-bit ripple counter (t_{pd} = 10 ns) and the synchronous counter of Check 2(b).

<!--ANSWERS-->

## Answers

**Check 1.** t_{su}: D steady before the edge; t_{h}: D steady after it; t_{pd}: edge to valid Q. Sketch as in step 1.

**Check 2.** (a) 8 + 16 + 3 = 27 ns: **37.0 MHz**. Hold unchanged: it uses the shortest path. (b) 10 + 5 + 5 = 20 ns: **50 MHz**.

**Self-test.**

1. 17 ns: **58.8 MHz**.
2. 2.5 &lt; 3: **violated**; add at least 0.5 ns of delay to the short path.
3. Hold compares two delays after the same edge; the period is not involved.
4. Ripple: 4 × 10 = 40 ns, **25 MHz**. Synchronous: **50 MHz**, and its period does not grow with the number of bits.

<!--/ANSWERS-->
