# 10 — Mock paper (MTE syllabus)

<div class="sub">Covers the professor's MTE syllabus (10/9/26), Parts I–III · all 14 of the professor's board questions + textbook problems for syllabus items the class has not yet worked · marks unknown (no hand-out or past paper yet) · attempt closed-book, then mark with the answers</div>

:::note How to use this
Do it in one sitting without opening 01–09. Write every step: the working earns marks, not just the final number.
Mark each item clean / with struggle / wrong, and schedule it as in 00. Items tagged <span class="tag">textbook</span> are not the professor's; everything else is quoted from the board.
:::

## Section A — Theory

Prompts on the syllabus topics. No past paper has been seen yet, so the *wording* of these is not the professor's.

1. Classify circuit elements. Distinguish active and passive elements, with examples. Draw the symbols of the four dependent sources and name a device for each.
2. Distinguish lumped and distributed parameters.
3. Derive v = L di/dt from ψ = Nφ. Explain why an inductor does not allow a sudden change of current.
4. State KCL and KVL. State the passive sign convention for power.
5. Write the procedures for nodal and mesh analysis. When is each preferred?
6. State the superposition theorem. List its limitations. How is it applied when sources have different frequencies?
7. Write the procedure for Thévenin's theorem. How is R_{Th} found when the network contains dependent sources?
8. State Norton's theorem. Give its procedure and draw the equivalent model.
9. Derive the condition for maximum power transfer to a resistive load. State the condition for a complex load.
10. Explain t = 0⁻, 0⁺ and ∞. Write the general first-order response and the time constants of RL and RC circuits.
11. Define the unit impulse, step and ramp signals, with their Laplace transforms and one example each.
12. For a series RLC circuit, write the characteristic equation and classify the response by damping.

## Section B — Numericals

### Part I · elements, laws, analysis

**B1** <span class="tag">Class p.4</span> 15 V is applied across 3 kΩ and 6 kΩ in series. Find V_{1} and V_{2}.

**B2** <span class="tag">Class p.5</span> A 12 A current source feeds 3 kΩ, 6 kΩ and 4 kΩ in parallel. Find I_{1}, I_{2}, I_{3}.

**B3** <span class="tag">Class p.5</span> v = 10 sin(2000t + 30°) V across 3 kΩ and 7 kΩ in series. Find v_{1}, v_{2}.

**B4** <span class="tag">Class p.1</span> Find R_{eq} of the infinite ladder 3 kΩ shunt, 5 kΩ series, 7 kΩ shunt, 11 kΩ series, 13 kΩ shunt, …

[[fig:ladder||w=65]]

**B5** <span class="tag">textbook</span> Find the loop current and the power of every element. Show that the powers balance.

[[fig:kvl_loop||w=45]]

**B6** <span class="tag">textbook</span> Find V_{1} by nodal analysis and the mesh currents i_{1}, i_{2} by mesh analysis. Check that they agree.

[[fig:mesh2||w=55]]

### Part II · theorems (DC and AC)

**B7** <span class="tag">Class p.7 · set 2 p.8</span> Calculate the current I using superposition. Verify by nodal analysis.

[[fig:sp_q||w=45]]

**B8** <span class="tag">Class p.9 · set 2 p.9</span> Calculate the current I_{1} using superposition. Comment on the result.

[[fig:sp_5v||w=45]]

**B9** <span class="tag">textbook</span> A 10 V DC source and a 10 cos(1000t) V source in series drive 1 kΩ and 1 H. Find i(t) in steady state.

**B10** <span class="tag">Class p.11 · set 2 p.11</span> Determine the load current using Thévenin's theorem (take 2I as 2 kΩ × I, I in mA). Verify with Norton's theorem.

[[fig:th_q||w=58]]

**B11** <span class="tag">textbook</span> 10∠0° V at ω = 1000 rad/s, 1 kΩ in series, 1 µF across the output. Find the Thévenin and Norton equivalents, the load for maximum power, and that power.

**B12–B13** <span class="tag">Class p.16–17 · set 2 p.14</span> For the circuit below: (a) the value of R_{L} for maximum power; (b) the total power delivered by the source; (c) the power consumed by R_{Th}; (d) the efficiency; (e) the voltage across the load; (f) the relation between load power and total power, and between load voltage and source voltage.

[[fig:mpt_q||w=40]]

**B14** <span class="tag">Class p.17</span> 10 V source with 5 kΩ: determine R for maximum power, the maximum power, and the efficiency.

### Part III · transients

**B15** <span class="tag">Class p.19–20</span> V, switch closing at t = 0, R. Find I(0⁻), I(0⁺), I(∞).

**B16** <span class="tag">Class p.21</span> V, switch closing at t = 0, R and L in series. Find I_{R}, I_{L} at 0⁻, 0⁺, ∞. Then find i(t) for V = 10 V, R = 1 kΩ, L = 1 mH, **by Laplace transform**.

**B17** <span class="tag">Set 2 p.20–21</span> V, switch closing at t = 0, R and C in series (C uncharged). Find v_{C}, v_{R}, I at 0⁻, 0⁺, ∞.

**B18** <span class="tag">Class p.22</span> 10 V, a switch opening at t = 0, 1 kΩ and 1 mH in series. Find I_{L}(0⁻) and I_{L}(0⁺). What happens to the inductor's current after the switch opens?

**B19** <span class="tag">textbook</span> An RC circuit (R = 1 kΩ, C = 1 µF, output v_{C}) is driven by a unit step, then by a unit ramp. Find v_{C}(t) for each by Laplace transform.

**B20** <span class="tag">textbook</span> 10 V is switched onto a series R, 1 H, 1 µF circuit (at rest). Classify the response for R = 2.5 kΩ, 2 kΩ, 1.2 kΩ, 0, and find v_{C}(t) for R = 2.5 kΩ.

<!--ANSWERS-->
## Answers

**Section A**: model answers are the **Exam form** sections: 01 (A1–A3), 02–03 (A4), 04 (A5), 05 (A6), 06 (A7, A8), 07 (A9), 08 (A10, A11), 09 (A12).

| | Answer | Where it's taught |
|---|---|---|
| **B1** | V_{1} = 5 V, V_{2} = 10 V | 02 §1 |
| **B2** | 5.33 A, 2.67 A, 4 A | 02 §2 |
| **B3** | v_{1} = 3 sin(2000t + 30°) V, v_{2} = 7 sin(2000t + 30°) V | 02 §3 |
| **B4** | ≈ 2.318 kΩ (if the values continue as primes) | 02 §5 |
| **B5** | i = 4/3 mA; 12 V source −16 mW (delivers), 4 V source +5.33 mW, 2 kΩ +3.56 mW, 4 kΩ +7.11 mW; sum 0 | 03 §2–3 |
| **B6** | V_{1} = 5.6 V; i_{1} = 2.2 mA, i_{2} = 0.8 mA; 4 kΩ carries 1.4 mA = 5.6 V/4 kΩ ✓ | 04 §1, §3 |
| **B7** | I_{1} = 5/3 A, I_{2} = 4/3 A, **I = 3 A** (resistors in Ω); nodal V_{A} = 6 V | 05 §1–3, 04 §2 |
| **B8** | By the rule each case gives 0 (the shorted idle source also shorts the 1 kΩ), so I = **0 A**; true value **5 mA**. Limitation: superposition fails for parallel ideal voltage sources | 05 §5 |
| **B9** | i(t) = 10 + 7.07 cos(1000t − 45°) mA | 05 §6 |
| **B10** | V_{Th} = 20/3 V, R_{Th} = 8/3 kΩ, **I_{L} = 20/11 ≈ 1.82 mA**; Norton I_{N} = 2.5 mA, same I_{L}. (With 2I read as 2 Ω: 5.0025 V, 3.0 kΩ, 1.25 mA; see 06 §2 Note) | 06 §2–5 |
| **B11** | V_{Th} = 7.07∠−45° V, Z_{Th} = 500 − j500 Ω, I_{N} = 10∠0° mA; Z_{L} = 500 + j500 Ω, P_{max} = 12.5 mW | 06 §6, 07 §4 |
| **B12–B13** | (a) 10 kΩ (b) 5 mW (c) 2.5 mW (d) 50 % (e) 5 V (f) P_{L} = P_{s}/2, V_{L} = V_{s}/2 | 07 §2–3 |
| **B14** | R = 5 kΩ, P_{max} = 5 mW, η = 50 % | 07 Check 1 |
| **B15** | 0, V/R, V/R | 08 §1 |
| **B16** | 0, 0, V/R for both; I(s) = 10^{4}/(s(s + 10^{6})) ⇒ i(t) = 10(1 − e^{−t/1 µs}) mA | 08 §2, §6 |
| **B17** | 0⁻: all 0. 0⁺: v_{C} = 0, v_{R} = V, I = V/R. ∞: v_{C} = V, v_{R} = 0, I = 0 | 08 §2 |
| **B18** | I_{L}(0⁻) = I_{L}(0⁺) = 10 mA. With no path, the ideal circuit has no solution (voltage spike, arc). If the R–L loop closes on itself: i(t) = 10e^{−t/1 µs} mA | 08 §5 |
| **B19** | τ = 1 ms. Step: 1 − e^{−t/τ} V. Ramp: t − τ + τe^{−t/τ} (lags the input by τ) | 08 §7 |
| **B20** | ω_{0} = 1000 rad/s, R_{c} = 2 kΩ: over, critical, under, undamped. R = 2.5 kΩ: v_{C} = 10 − (40/3)e^{−500t} + (10/3)e^{−2000t} V | 09 §4–5 |
<!--/ANSWERS-->
