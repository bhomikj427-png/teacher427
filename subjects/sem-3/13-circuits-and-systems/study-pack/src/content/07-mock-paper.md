# 07 — Mock paper

<div class="sub">All 13 of the professor's board questions, plus theory prompts on the lectured topics · marks unknown (no hand-out or past paper yet) · attempt closed-book, then mark with the answers</div>

:::note How to use this
Do it in one sitting without opening 01–06. Write every step: the working earns marks, not just the final number.
Mark each item clean / with struggle / wrong, and schedule it as in 00.
:::

## Section A — Theory

Prompts on the topics the professor lectured. No past paper has been seen yet, so the *wording* of these is not the professor's.

1. Classify circuit elements. Distinguish active and passive elements, with examples. Draw the symbols of the four dependent sources.
2. Derive v = L di/dt from ψ = Nφ. Explain why an inductor does not allow a sudden change of current.
3. State the superposition theorem. List its limitations.
4. Write the procedure for Thévenin's theorem. How is R_{Th} found when the network contains dependent sources?
5. State Norton's theorem. Give its procedure and draw the equivalent model.
6. Derive the condition for maximum power transfer to a resistive load. State the condition for a complex load.
7. Explain t = 0⁻, 0⁺ and ∞. Write the general first-order response and the time constants of RL and RC circuits.

## Section B — Numericals (the professor's board questions)

**B1** <span class="tag">Class p.4</span> 15 V is applied across 3 kΩ and 6 kΩ in series. Find V_{1} and V_{2}.

**B2** <span class="tag">Class p.5</span> A 12 A current source feeds 3 kΩ, 6 kΩ and 4 kΩ in parallel. Find I_{1}, I_{2}, I_{3}.

**B3** <span class="tag">Class p.5</span> v = 10 sin(2000t + 30°) V across 3 kΩ and 7 kΩ in series. Find v_{1}, v_{2}.

**B4** <span class="tag">Class p.1</span> Find R_{eq} of the infinite ladder 3 kΩ shunt, 5 kΩ series, 7 kΩ shunt, 11 kΩ series, 13 kΩ shunt, …

[[fig:ladder||w=65]]

**B5** <span class="tag">Class p.7</span> Calculate the current I using superposition.

[[fig:sp_q||w=45]]

**B6** <span class="tag">Class p.9</span> Calculate the current I_{1} using superposition. Comment on the result.

[[fig:sp_5v||w=45]]

**B7** <span class="tag">Class p.11</span> Determine the load current using Thévenin's theorem. Verify with Norton's theorem.

[[fig:th_q||w=58]]

**B8–B9** <span class="tag">Class p.16–17</span> For the circuit below: (a) the value of R_{L} for maximum power; (b) the total power delivered by the source; (c) the power consumed by R_{Th}; (d) the efficiency; (e) the voltage across the load; (f) the relation between load power and total power, and between load voltage and source voltage.

[[fig:mpt_q||w=40]]

**B10** <span class="tag">Class p.17</span> 10 V source with 5 kΩ: determine R for maximum power, the maximum power, and the efficiency.

**B11** <span class="tag">Class p.19–20</span> V, switch closing at t = 0, R. Find I(0⁻), I(0⁺), I(∞).

**B12** <span class="tag">Class p.21</span> V, switch closing at t = 0, R and L in series. Find I_{R}, I_{L} at 0⁻, 0⁺, ∞. Then write i(t) for V = 10 V, R = 1 kΩ, L = 1 mH.

**B13** <span class="tag">Class p.22</span> 10 V, a switch opening at t = 0, 1 kΩ and 1 mH in series. Find I_{L}(0⁻) and I_{L}(0⁺). What happens to the inductor's current after the switch opens?

<!--ANSWERS-->
## Answers

**Section A**: model answers are the **Exam form** sections: 01 (A1, A2), 03 (A3), 04 (A4, A5), 05 (A6), 06 (A7).

| | Answer | Where it's taught |
|---|---|---|
| **B1** | V_{1} = 5 V, V_{2} = 10 V | 02 §1 |
| **B2** | 5.33 A, 2.67 A, 4 A | 02 §2 |
| **B3** | v_{1} = 3 sin(2000t + 30°) V, v_{2} = 7 sin(2000t + 30°) V | 02 §3 |
| **B4** | ≈ 2.318 kΩ (if the values continue as primes) | 02 §5 |
| **B5** | I_{1} = 5/3 A, I_{2} = 4/3 A, **I = 3 A** (resistors in Ω) | 03 §1–3 |
| **B6** | Mechanical superposition gives 10 mA; the true value is **5 mA**. Superposition fails for parallel ideal voltage sources | 03 §5 |
| **B7** | V_{Th} = 20/3 V, R_{Th} = 8/3 kΩ, **I_{L} = 20/11 ≈ 1.82 mA**; Norton: I_{N} = 2.5 mA, same I_{L} | 04 |
| **B8–B9** | (a) 10 kΩ (b) 5 mW (c) 2.5 mW (d) 50 % (e) 5 V (f) P_{L} = P_{s}/2, V_{L} = V_{s}/2 | 05 §2–3 |
| **B10** | R = 5 kΩ, P_{max} = 5 mW, η = 50 % | 05 Check 1 |
| **B11** | 0, V/R, V/R | 06 §1 |
| **B12** | 0, 0, V/R for both; i(t) = 10(1 − e^{−t/1 µs}) mA | 06 §2–4 |
| **B13** | I_{L}(0⁻) = I_{L}(0⁺) = 10 mA. With no path, the ideal circuit has no solution (voltage spike, arc). If the R–L loop closes on itself: i(t) = 10e^{−t/1 µs} mA | 06 §5 |
<!--/ANSWERS-->
