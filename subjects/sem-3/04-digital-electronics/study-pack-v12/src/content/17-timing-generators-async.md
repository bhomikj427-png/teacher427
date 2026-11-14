# 17 — Timing issues, generators, asynchronous circuits

<div class="sub">Syllabus Unit 4 items with no deck coverage: practice questions only (one from Anna University EC6302) · needs 14 (setup and hold) and 11 (shift registers)</div>

## Map

[[map:1 Skew, glitches, metastability > 2 LFSR, pulse trains, clocks > 3 Races and hazards|here=1]]

Three syllabus lines the decks skip: what goes wrong with real clocks and inputs, circuits that generate sequences and clocks, and circuits with no clock at all.

## The questions this file answers

- <span class="tag">practice</span> A push-button goes straight into a 100 MHz system. What can go wrong, and how is it fixed?
- <span class="tag">practice</span> A 3-bit LFSR with D_{1} = Q_{2} ⊕ Q_{3} starts at 100. List its states.
- <span class="tag">EC6302 Nov 2021 · 13 marks</span> Objective of state assignment in an asynchronous circuit; hazard-free realisation of f = ΠM(0, 2, 6, 7, 8, 10, 12).

---

## Build

### 1 · Skew, glitches and metastability

:::q <span class="tag">practice</span>
A push-button signal is connected straight into a 100 MHz synchronous system. What can go wrong, and how is it fixed?
:::

:::guess Guess first
The button is pressed at a random moment. What does 14 say about a D input that changes right at a clock edge?
:::

- **Clock skew:** the clock reaches flip-flops at slightly different times. A late receiving clock eats the **hold** margin (a slower clock cannot fix it); the other way eats setup. Fix: balanced clock routing.
- **Output glitches:** a Mealy output, or one decoded from several state bits, can pulse falsely while inputs or bits change. Fix: take the output from a flip-flop (Moore style).
- **Asynchronous inputs, metastability:** an unclocked input sometimes changes inside the setup/hold window and the flip-flop hangs between 0 and 1. Fix: a **synchronizer**, two D flip-flops in series on the system clock; the second gives the first a whole period to settle.

**Answer.** The button can change inside a setup/hold window, so a flip-flop goes metastable and different flip-flops may read different values. It also **bounces** (several pulses per press). Fix: debounce (SR latch on a two-way switch, or RC + Schmitt trigger), then a two-flip-flop synchronizer.

:::check Check 1
(a) Which violation can a lower clock frequency cure: setup or hold? (b) Why are Moore outputs glitch-free when Mealy outputs are not?
:::

### 2 · LFSR, pulse trains and clocks

:::q <span class="tag">practice</span>
A 3-bit shift register has its input fed by D_{1} = Q_{2} ⊕ Q_{3} and starts at Q_{1}Q_{2}Q_{3} = 100. List its states and find the sequence length.
:::

:::guess Guess first
3 flip-flops have 8 states. Can it reach 000 from 100? What if it starts at 000?
:::

[[fig:lfsr3|3-bit linear-feedback shift register.|w=60]]

An **LFSR** (pseudo-random binary sequence generator) feeds back the XOR of chosen taps. With the right taps it visits all **2^{n} − 1** non-zero states (maximal length). **000 is a lock-out** (0 ⊕ 0 = 0 forever). Uses: test patterns, scrambling, spread-spectrum codes.

**Pulse-train generator:** a fixed bit pattern, one bit per clock: a ring-connected shift register loaded with the pattern (11), or a MOD-N counter plus output logic.

**Clocks.** Divide with a MOD-N counter (f/N) or k toggle flip-flops (f/2^{k}). Make one with an oscillator:

| Multivibrator | Stable states | Output |
|---|---|---|
| Astable | none | free-running square wave (a clock) |
| Monostable | one | one fixed-width pulse per trigger; width 1.1RC (555) |
| Bistable | two | a latch or flip-flop |

<div class="two">

[[fig:astable_555|555 astable.]]

[[fig:ring_osc|Ring oscillator: an odd number of inverters.]]

</div>

**555 astable:** f = 1.44/((R_{1} + 2R_{2})C), duty = (R_{1} + R_{2})/(R_{1} + 2R_{2}). R_{1} = 1 kΩ, R_{2} = 10 kΩ, C = 10 nF: 6.86 kHz, 52%. **Ring oscillator:** N (odd) inverters give f = 1/(2N·t_{pd}): five of 2 ns give 50 MHz; it drifts with temperature and supply, so system clocks use crystals.

**Answer.** 100 → 010 → 101 → 110 → 111 → 011 → 001 → 100: **seven states = 2^{3} − 1**, maximal. Output at Q_{3}: 0 0 1 0 1 1 1, repeating.

:::check Check 2
(a) Sequence length of a maximal 5-bit LFSR? (b) Why must a ring oscillator have an odd number of inverters? (c) Which counter gives 1 Hz from a 50 Hz clock?
:::

### 3 · Asynchronous circuits: races and hazards

:::q <span class="tag">EC6302 Nov/Dec 2021 Q15(b) · 13 marks</span>
What is the objective of state assignment in a asynchronous circuit? Give the hazard free realization for the Boolean function f(A, B, C, D) = ΠM(0, 2, 6, 7, 8, 10, 12).
:::

:::guess Guess first
With no clock, two state bits are told to change "at the same time". What decides which changes first?
:::

:::note Terms
**Asynchronous circuit:** no clock; state held in feedback loops; reacts at once. **Stable state:** next = present. **Fundamental mode:** one input changes at a time, only after the circuit settles.
:::

Design outline: word description → primitive flow table → merge rows → state assignment → excitation equations → circuit.

- **Race:** a transition needs two state variables to change; gate delays decide the order. **Non-critical:** every order ends in the same stable state. **Critical:** the end state depends on the order: wrong some of the time.
- **Hazard:** a momentary wrong output from unequal delays. **Static-1:** should stay 1 but dips (one product term turns off before the next turns on). Static-0 is the opposite; **dynamic:** should change once but bounces. In an asynchronous circuit a glitch can look like a real input.
- **Cure:** on the K-map, every pair of adjacent 1s must share a group; add the redundant consensus group where they don't.

[[fig:hazard|Left: the K-map with the extra group AD. Right: a static-1 glitch.]]

**Answer.** **State assignment:** give states that have a transition between them codes differing in one bit, so only one variable changes at a time and no critical race occurs. **Hazard-free:** the 1s are Σm(1, 3, 4, 5, 9, 11, 13, 14, 15). Minimal cover B'D + C'D + A'BC' + ABC leaves pairs 11–15 and 13–15 in no common group; **AD** (9, 11, 13, 15) covers both:

$$f = B'D + C'D + A'BC' + ABC + AD$$

:::check Check 3
(a) F = AB + A'C. Which input change can cause a static-1 hazard, and which term removes it? (b) Critical vs non-critical race? (c) State the fundamental-mode rule.
:::

---

## Exam form

**Timing issues.** Skew (hold), glitches (Moore outputs), metastability and the two-flip-flop synchronizer; debouncing.

**Generators.** LFSR states, 2^{n} − 1, lock-out; pulse train (ring or counter + logic); clock division; multivibrator table, 555 formulas, ring oscillator.

**Asynchronous.** Flow table; races (critical, non-critical) and the state-assignment rule; hazards (static-1, static-0, dynamic) and the consensus cure.

## Traps

- Saying a synchronizer makes failure impossible: only very rare.
- Starting an LFSR at all zeros.
- A ring oscillator with an even number of inverters.
- Removing a "redundant" consensus term from a hazard-free design.

## Self-test

1. Sequence length of a maximal 4-bit LFSR?
2. 555 astable with R_{1} = 2 kΩ, R_{2} = 4 kΩ, C = 0.1 μF: f and duty cycle?
3. A ring oscillator of 3 inverters, t_{pd} = 1 ns: f?
4. F = A'B + AC: find the hazard and remove it.
5. 555 monostable with R = 10 kΩ, C = 1 μF: pulse width?
6. Draw a two-flip-flop synchronizer and explain it.

<!--ANSWERS-->

## Answers

**Check 1.** (a) **Setup**: a longer period gives data more time; hold does not involve the period. (b) Moore outputs come only from flip-flops, which change once per edge; Mealy outputs also follow the input, which changes any time.

**Check 2.** (a) **31**. (b) An even number forms a consistent loop (like a latch) and settles. (c) **MOD-50**.

**Check 3.** (a) With B = C = 1, changing A hands the output from AB to A'C; it can dip. Add **BC**. (b) Critical: the final state depends on which variable changes first; non-critical: every order ends in the same state. (c) Only one input changes at a time, and only after the circuit is stable.

**Self-test.**

1. **15**.
2. f = 1.44/(10 kΩ × 0.1 μF) = **1.44 kHz**; duty = 6/10 = **60%**.
3. 1/(2 × 3 × 1 ns) = **167 MHz**.
4. B = C = 1, A changing: static-1 hazard. Add **BC**: F = A'B + AC + BC.
5. 1.1 × 10 kΩ × 1 μF = **11 ms**.
6. Two D flip-flops in series on the system clock; the asynchronous input goes into the first. If the first goes metastable, it has a whole clock period to settle before the second samples it.

<!--/ANSWERS-->
