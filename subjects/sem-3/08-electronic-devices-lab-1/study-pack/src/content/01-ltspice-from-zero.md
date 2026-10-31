# 01 · LTspice from zero

<div class="sub">Needed for Exps 2, 4, 5, 8, 9, 10, 11, 12 and the extra experiment · LTspice is free (Analog Devices) and already installed on your laptop</div>

## Where this sits

[[map:LTspice basics > the 4 analyses > drawing a circuit > reading the result > exporting data|here=1]]

**What you already have:** circuits from C&S (KVL, KCL, sources, R, C), and the idea that a graph of one quantity against another describes a device.

**Three terms first:**

- **Simulator:** a program that solves the circuit's KVL/KCL equations for you, using a mathematical **model** of each part.
- **Model:** the set of numbers that describes a real part. For example, "BC547B" tells LTspice the β, the junction capacitances, and so on.
- **Directive:** a text command starting with a dot (`.dc`, `.ac`, `.tran`, `.op`, `.step`). It tells LTspice *which* analysis to run.

:::q <span class="tag">Manual Exp 2, Fig 2.1</span>
The circuit has `.dc V1 0 20 1` written under it. What does that line make LTspice do?
:::

:::guess Guess first
Guess what each of the four words means: `.dc`, `V1`, `0 20`, `1`.
:::

## The four analyses (every software experiment uses one or more)

| Directive | What it does | Gives you | Used in |
|---|---|---|---|
| `.op` | finds the DC operating point (all capacitors open) | one number per node | Exp 2 (load), checking a Q-point |
| `.dc V1 0 20 1` | sweeps source V1 from 0 to 20 V in 1 V steps, solving at each step | a curve: anything against V1 | Exps 2, 5, 9 |
| `.ac dec 10 200 1Meg` | small-signal sine at each frequency, 10 points per decade, 200 Hz to 1 MHz | gain (dB) and phase against frequency | Exps 7, 8, 10, extra |
| `.tran 10m` | runs time forward for 10 ms | waveforms against time | Exps 4, 7, 10, 11, 12 |
| `.step param R 100 1100 100` | reruns the analysis for R = 100, 200, … 1100 | a family of curves | Exp 2 (load) |

So `.dc V1 0 20 1` = "DC sweep of V1, start 0, stop 20, step 1". A **nested** sweep has a second source at the end: `.dc Vce 0 12 0.05 Ib 0 60u 20u` sweeps V_{ce} for each of I_{b} = 0, 20, 40, 60 µA, which gives one curve per I_{b}.

## Units: the trap that costs marks

SPICE ignores case, so **`M` means milli, not mega.**

| You want | Type | Not |
|---|---|---|
| 1 MΩ | `1Meg` | ~~`1M`~~ (that is 1 mΩ) |
| 10 µF | `10u` | |
| 0.5 nF | `0.5n` or `500p` | |
| 2.2 kΩ | `2.2k` | |

## Drawing a circuit

:::do Do it: draw, set, run
1. **File → New Schematic.**
2. Place parts using the keyboard: **R** resistor, **C** capacitor, **D** diode, **G** ground. **F2** opens the full component list (`voltage`, `npn`, `njf`, `nmos`, `zener`).
3. **F3** draws a wire: click at the start, click at each corner, right-click to stop. **Ctrl+R** rotates a part before you place it.
4. **Every circuit needs a ground (G).** Without one, the run fails with a "singular matrix" or "floating node" error.
5. **Right-click a part** to set its value (e.g. `2.2k`).
6. To choose a **model** (BC547B, 2N3819, 1N914, BZX84C6V2L, FDR6580, 2N2222, 2N5434), right-click the diode or transistor and click **Pick New …**. All the manual's parts are in LTspice's library.
7. To set up a **source**, right-click it and click **Advanced**:
   - **SINE**: DC offset, amplitude, frequency. `SINE(0 5 1k)` = 0 V offset, 5 V peak, 1 kHz.
   - **Small signal AC amplitude**: type `1` (or `0.5`) here for an `.ac` run.
   - **PULSE**: V1, V2, delay, rise, fall, on-time, period, cycles.
8. To add a directive, press **S** (or **Edit → SPICE Directive**), type it, and place the text anywhere on the sheet. Alternatively, **Simulate → Edit Simulation Cmd** fills the directive in for you.
9. **F4** puts a label on a wire. Name the output `Vo` so it is easy to plot.
10. Click **Run** (the running-man icon).
:::

## Reading the result

| You want | Do this |
|---|---|
| a node voltage | after the run, click on the wire (the probe turns into a red voltage probe) |
| a current | click on the part's body (the probe turns into a current clamp) |
| a different x-axis (e.g. V(base) instead of V_{be}) | right-click the x-axis, then set **Quantity plotted** to `V(base)` |
| an exact value | click the trace's name above the plot. A cursor appears, and its readout box shows x and y. A second click adds cursor 2; the box then also shows the difference. |
| gain in plain ratio, not dB | right-click the y-axis and choose **Linear** |
| y-axis limits | right-click the y-axis and set **Manual limits** |

In an `.ac` plot, the **solid line is the gain in dB** and the **dashed line is the phase**.

:::write Observation tables from a simulation
The manual says: "Paste data points from simulations". With the plot window active, use **File → Export data as text**. The file has one row per point. Copy only the rows the table asks for (5–10 points), and mark on the graph the points used in calculations.
:::

:::trap Trap: the default time step
`.tran 20m` lets LTspice pick its own step, which can be coarse. Edges then look slanted, or tall false spikes appear. Write `.tran 0 20m 0 1u` instead: the fourth number caps the step at 1 µs.
:::

:::check Check 1
(a) Write the directive that sweeps V_{gs} from −5 V to 0 V in 10 mV steps. (b) Your 1 MΩ resistor shows `1M`. What value is LTspice actually using? (c) Which analysis gives a frequency response?
:::

<!--ANSWERS-->

## Answers

**Check 1.** (a) `.dc Vgs -5 0 0.01` (or `10m`). (b) 1 milliohm, a short circuit. Write `1Meg`. (c) `.ac`, with the source's AC amplitude set.

**Opening question.** `.dc` = DC sweep, `V1` = the source being swept, `0 20` = from 0 V to 20 V, `1` = in 1 V steps. LTspice solves the circuit 21 times and plots any node against V1.

<!--/ANSWERS-->
