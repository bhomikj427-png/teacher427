# 03 — The pn junction and the diode

<div class="sub">Unit 1–2 deck, slides 77–100 (examples slides 77–78) · syllabus Unit 2 · needs 02a (drift, σ) and 02b (drift–diffusion balance, Einstein relation, lifetime τ, diffusion length L, Poisson)</div>

## Map

[[map:1 Junction, built-in voltage > 2 The diode equation > 3 Resistances, models, capacitances|here=1]]

Put p-type and n-type silicon in contact and you get a one-way valve for current. This file explains the device; 04 and 05 use it in circuits; 07 squeezes a channel with its depletion region.

## The questions this file answers

- <span class="tag">Deck slides 77–78</span> Abrupt Si junction, V_{bi} = 0.85 V. Find W_{1}/W_{0} for V_{a} = 0.6 V; repeat for 2 V reverse.
- <span class="tag">practice · slides 79–83</span> I_{s} = 1 pA: current at 0.6 V, and the effect of 60 mV more.
- <span class="tag">practice · slides 84–100</span> Static and dynamic resistance; transition and diffusion capacitance; reverse recovery.

---

## Build

### 1 · Junction formation and the built-in voltage

:::q <span class="tag">Deck slides 77–78</span>
For an abrupt silicon pn junction, V_{bi} = 0.85 V. Let W_{0} and W_{1} be the depletion widths for V_{a} = 0 V and V_{a} = 0.6 V. What is W_{1}/W_{0}? Repeat for a reverse bias of 2 V.
:::

:::guess Guess first
Does forward bias make the depletion region wider or narrower?
:::

:::note Terms
**Abrupt junction:** doping switches from p to n in one step. **Ion:** a dopant atom that lost its carrier: charged, fixed. **Bias:** a DC voltage across the device.
:::

[[fig:junction|pn junction: depletion region of fixed ions, built-in field from n to p.|w=75]]

At contact, holes diffuse p → n and electrons n → p (02b) and recombine, leaving fixed ions: − on the p side, + on the n side. This carrier-free strip is the **depletion region**. Its field (n → p) pushes carriers back; diffusion stops when drift cancels it. The voltage across it then is

$$V_{bi} = V_{T} ln(N_{A}N_{D}/n_{i}^{2})$$

about 0.6–0.9 V in Si. (A voltmeter reads zero across a loose diode: the metal contacts cancel it.) Solving Poisson (02b step 13) gives a triangular field and

$$W = √[(2ε/q)(1/N_{A} + 1/N_{D})(V_{bi} − V_{a})]      N_{A}x_{p} = N_{D}x_{n}$$

V_{a} is positive for forward bias. The region reaches further into the **lightly doped** side. **Forward** bias lowers the barrier to V_{bi} − V_{a}: the region narrows and majority carriers pour across. **Reverse** bias widens it; only a tiny current of minority carriers flows.

**Answer.** W ∝ √(V_{bi} − V_{a}). Forward 0.6 V: √(0.25/0.85) = **0.54**, it shrinks. Reverse 2 V: √(2.85/0.85) = **1.83**, it expands.

:::check Check 1
(a) Find V_{bi} for N_{A} = 10^{17}, N_{D} = 10^{16} cm^{−3}, n_{i} = 10^{10}, V_{T} = 25.9 mV. (b) Which side holds more of the depletion region? (c) What two currents balance at equilibrium?
:::

### 2 · The diode I–V equation

:::q <span class="tag">practice · slides 79–83</span>
A diode has I_{s} = 1 pA and η = 1 at 300 K. Find its current at V_{D} = 0.6 V. What happens if V_{D} rises by 60 mV?
:::

:::guess Guess first
Will 60 mV make a small change or a big one?
:::

[[fig:diode_iv|Diode I–V: forward knee near 0.7 V (Si), flat reverse current, breakdown.|w=60]]

Lowering the barrier lets exponentially more carriers cross:

$$I_{D} = I_{s}(e^{V_{D}/ηV_{T}} − 1)      V_{T} = kT/q = T/11 600 ≈ 26 mV$$

| Symbol | Meaning |
|---|---|
| I_{s} | reverse saturation current: minority carriers; nA in Si, μA in Ge; ∝ n_{i}^{2} |
| η | ideality factor, 1 to 2 (slides: 1 for Ge, 2 for Si); take 1 unless told |
| Knee voltage | Si 0.7 V, Ge 0.3 V, GaAs 1.2 V |

Forward (V_{D} ≫ V_{T}): I_{D} ≈ I_{s}e^{V_{D}/ηV_{T}}. Reverse: I_{D} ≈ −I_{s}, flat. Breakdown at large reverse voltage (05). **Temperature:** I_{s} doubles every 10 °C, I_{s2} = I_{s1} × 2^{(T_{2} − T_{1})/10} (slide 81); at fixed current V_{D} falls about 2 mV/°C.

**Answer.** I_{D} = 10^{−12} × e^{0.6/0.0259} = **12 mA**. +60 mV multiplies it by e^{0.06/0.0259} ≈ **10**: every 60 mV is a factor of ten, which is why the curve looks like a wall at 0.7 V.

:::check Check 2
(a) I_{s} = 10 nA at 25 °C. Find I_{s} at 55 °C. (b) Why is the reverse current almost independent of reverse voltage? (c) Which leaks more, Si or Ge, and why?
:::

### 3 · Resistances, models, capacitances, switching

:::q <span class="tag">practice · slides 84–100</span>
A diode carries 2 mA at 0.7 V. Find its static and dynamic resistance (η = 1).
:::

:::guess Guess first
Which of the two is larger?
:::

**Static:** R_{D} = V_{D}/I_{D}. **Dynamic** (slope for a small AC signal), from differentiating the diode equation: **r_{d} = ηV_{T}/I_{D} ≈ 26 mV/I_{D}**. Average AC resistance r_{av} = ΔV_{D}/ΔI_{D} for large swings.

[[fig:diode_models|Ideal, simplified (0.7 V) and piecewise-linear models. Use the simplified model unless told "ideal".|w=75]]

| Capacitance | When | Formula | Cause |
|---|---|---|---|
| Transition C_{T} | reverse | εA/W | the depletion region is a dielectric; more reverse V → wider W → smaller C_{T} (varactor) |
| Diffusion C_{D} | forward | τI_{D}/ηV_{T} | stored minority carriers; much larger than C_{T} |

**Switching.** When the voltage reverses, stored minority carriers keep a large reverse current flowing for the **storage time t_{s}**, then it decays over the **transition time t_{t}**: **t_{rr} = t_{s} + t_{t}**, ns to μs. It limits the usable frequency.

**Answer.** R_{D} = 0.7/2 mA = **350 Ω**. r_{d} = 26/2 = **13 Ω**: the curve is steep there.

:::check Check 3
(a) r_{d} at 0.5 mA and 5 mA? (b) Which capacitance matters in reverse bias, and how does it change as reverse voltage grows? (c) What causes the reverse recovery time?
:::

---

## Exam form

**Junction.** Diffusion → ions → depletion region → field → equilibrium; sketch charge, field, potential. V_{bi} = V_{T}ln(N_{A}N_{D}/n_{i}^{2}); W formula; forward/reverse effect.

**Diode equation.** I_{D} = I_{s}(e^{V_{D}/ηV_{T}} − 1); terms; regions; temperature rules.

**Resistances, capacitances.** R_{D}, r_{d} = 26 mV/I_{D}; models; C_{T} vs C_{D} table; t_{rr} = t_{s} + t_{t}.

## Traps

- W depends on √(V_{bi} − V_{a}), not on V_{a} alone.
- Using η = 2 without being told; state your choice.
- Confusing C_{T} (reverse) with C_{D} (forward).
- r_{d} uses mV over mA, giving ohms: 26/2 = 13 Ω, not 0.013.

## Self-test

1. V_{bi} for N_{A} = N_{D} = 10^{16} cm^{−3}, n_{i} = 10^{10}.
2. I_{s} = 1 pA: find I_{D} at 0.65 V (η = 1, V_{T} = 25.9 mV).
3. r_{d} at 10 mA?
4. V_{bi} = 0.85 V. By what factor do W and C_{T} change from 0 V to 5 V reverse?
5. I_{s} = 5 nA at 25 °C. Find it at 45 °C.
6. Explain t_{rr} in two lines.

<!--ANSWERS-->

## Answers

**Check 1.** (a) 0.0259 × ln(10^{33}/10^{20}) = 0.0259 × 29.9 = **0.774 V**. (b) The **n side**: lighter doping needs more width to hold equal charge. (c) Diffusion of majority carriers across, and drift of minority carriers back, driven by the built-in field.

**Check 2.** (a) Three doublings: **80 nA**. (b) It is made of thermally generated minority carriers; their supply depends on temperature, not voltage. (c) **Ge**: smaller gap, far larger n_{i}, and I_{s} ∝ n_{i}^{2}.

**Check 3.** (a) **52 Ω** and **5.2 Ω**. (b) C_{T} = εA/W; it **falls** as W widens. (c) Minority carriers stored near the junction must be removed before the diode can block.

**Self-test.**

1. 0.0259 × ln(10^{12}) = **0.716 V**.
2. 10^{−12} × e^{25.1} = **79 mA**.
3. **2.6 Ω**.
4. W × √(5.85/0.85) = **× 2.62**; C_{T} **× 0.38**.
5. Two doublings: **20 nA**.
6. Charge stored during forward conduction keeps a reverse current flowing (t_{s}) until it is cleared, then the current decays (t_{t}); t_{rr} = t_{s} + t_{t}.

<!--/ANSWERS-->
