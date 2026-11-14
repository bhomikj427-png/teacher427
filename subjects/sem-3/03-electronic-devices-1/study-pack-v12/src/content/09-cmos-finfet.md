# 09 — The MOSFET as a switch, CMOS gates, FinFET

<div class="sub">Deck "MOSFET biasing and digital circuit" (slide 9: complex CMOS gate) · two FinFET decks · syllabus Unit 4 extra · needs 08 (regions of operation)</div>

## Map

[[map:1 Switch, CMOS inverter > 2 CMOS logic gates > 3 FinFET|here=1]]

08 used the MOSFET in saturation as an amplifier. Drive it fully off or fully on instead and it is a switch. Pair an n-switch with a p-switch and you have CMOS, the logic inside every chip. Shrinking that switch brings problems the FinFET solves.

## The questions this file answers

- <span class="tag">Deck slide 9</span> Implement f = (a·(b + c))′ as a single CMOS gate. How many transistors?
- <span class="tag">Deck</span> Explain the CMOS inverter and why it draws almost no static power.
- <span class="tag">FinFET decks</span> What problems appear when a planar MOSFET is scaled down, and how does a FinFET overcome them?

---

## Build

### 1 · The MOSFET switch and the CMOS inverter

:::guess Predict
An nMOS with V_{T} = 1 V has its gate at V_{DD} = 5 V and tries to pass a logic 1 (5 V) from drain to source. What voltage comes out?
:::

:::note Terms
**Logic 1 / 0:** V_{DD} / 0 V. **Pull-up network:** transistors between V_{DD} and the output. **Pull-down network:** between the output and ground.
:::

- **Switch:** cutoff = open; triode with large V_{GS} = closed, with r_{DS(on)} ≈ 1/[2K(V_{GS} − V_{T})]. No gate current is needed to hold it on.
- **nMOS** closes when its gate is 1; **pMOS** when its gate is 0. nMOS passes a strong 0 but a weak 1 (it stops at V_{DD} − V_{T}); pMOS passes a strong 1 but a weak 0. So CMOS **pulls up with pMOS and down with nMOS**.

<div class="two">

[[fig:cmos_inv|CMOS inverter.]]

[[fig:cmos_vtc|Inverter transfer characteristic.]]

</div>

**CMOS inverter.** Input 0: pMOS on, nMOS off, output V_{DD}. Input 1: nMOS on, pMOS off, output 0. In either steady state one transistor is off, so **no current flows from V_{DD} to ground**: static power ≈ 0. Power is used only while switching. The output swings the full 0 to V_{DD}.

**Answer.** V_{DD} − V_{T} = **4 V**, a weak 1: once the source rises to V_{G} − V_{T} the nMOS turns off.

:::check Check 1
(a) Why does a CMOS inverter draw almost no current when its input is steady? (b) Find r_{DS(on)} for K = 0.5 mA/V^{2}, V_{GS} = 10 V, V_{T} = 2 V.
:::

### 2 · CMOS logic gates

:::q <span class="tag">Deck slide 9 "Complex Logic Gates in CMOS: Example"</span>
Implement f = (a·(b + c))′ as a single CMOS gate. How many transistors does it need?
:::

:::guess Guess first
Sketch the nMOS network that must connect the output to ground when a·(b + c) = 1.
:::

[[fig:cmos_gates|CMOS NAND, NOR, and the gate for (a·(b + c))′.]]

1. The **pull-down** (nMOS) implements the function **before** the final inversion: series = AND, parallel = OR.
2. The **pull-up** (pMOS) is the **dual**: series ↔ parallel.
3. Each input drives one nMOS and one pMOS: **n inputs, 2n transistors**.
4. A CMOS gate always inverts: NAND and NOR are natural; AND needs a NAND plus an inverter.

**Answer.** Pull-down: a in series with (b ∥ c). Pull-up: a in parallel with (b series c). Three inputs: **6 transistors** (3 nMOS + 3 pMOS). For each of the 8 input combinations exactly one network conducts.

:::check Check 2
In a 2-input CMOS NOR, which transistors are in series and which in parallel?
:::

### 3 · FinFET

:::q <span class="tag">FinFET decks</span>
What problems appear when a planar MOSFET is scaled down, and how does a FinFET overcome them?
:::

:::guess Guess first
When the channel gets very short, what else besides the gate can influence it?
:::

[[fig:finfet_fig|Planar MOSFET (gate on top) and FinFET (gate wrapped round three sides of a fin).]]

**The problem: short-channel effects.** At tens of nanometres the drain is so close to the source that its field reaches into the channel and the gate loses control: the **threshold voltage shifts** (falls) with length and drain voltage; the **subthreshold slope degrades**, so it no longer turns off sharply; the **off-state leakage I_{OFF} rises**.

**The fix.** The channel becomes a thin vertical **fin**; the gate covers it on **three sides**. Current flows along both side walls and the top. The gate controls the whole thin body.

| | Planar MOSFET | FinFET |
|---|---|---|
| Gate | one side (top) | three sides of a fin |
| Channel control | weakens at short lengths | strong |
| Leakage | high at small size | low |
| Drive per area | lower | higher; lower supply voltage |
| Channel doping | needed | optional (thin body) |
| Width | any value | whole fins only |
| Fabrication | simpler, cheaper | complex, costly; more parasitic C; heat harder to remove |

Types: **shorted-gate** (both side gates joined) and **independent-gate** (driven separately, one can tune the threshold). Fin spacing matters: too close interferes, too far wastes area.

**Answer.** Scaling brings short-channel effects (threshold shift, poor subthreshold slope, high off current) because the drain starts to control the channel. Raising the channel into a fin and wrapping the gate round three sides restores control: lower leakage, faster switching, scaling continues.

:::check Check 3
(a) Name three short-channel effects. (b) On how many sides does the gate touch the channel in a planar MOSFET and in a FinFET? (c) Two disadvantages of FinFETs?
:::

---

## Exam form

**Switch.** Cutoff open, triode closed; r_{DS(on)}; nMOS strong 0, pMOS strong 1.

**CMOS inverter.** Circuit, operation table, VTC sketch, near-zero static power.

**CMOS gate design.** Pull-down = function before inversion (series AND, parallel OR); pull-up is the dual; 2n transistors. Draw NAND, NOR.

**FinFET.** Short-channel effects (three); structure; planar vs FinFET table; SG and IG types.

## Traps

- Drawing the pull-up with the same series/parallel as the pull-down.
- Forgetting the CMOS output is inverted: (a·(b + c))′, not a·(b + c).
- Using nMOS in the pull-up (weak 1).
- Saying FinFET gates surround the channel on four sides (that is gate-all-around).

## Self-test

1. Draw a 2-input CMOS NAND and give its truth table with the state of each transistor.
2. How many transistors does a CMOS gate for (ab + cd)′ need? Describe its pull-down.
3. Why is CMOS preferred over nMOS-only logic?
4. Explain the threshold-voltage shift in a short-channel MOSFET.
5. What is the difference between shorted-gate and independent-gate FinFETs?

<!--ANSWERS-->

## Answers

**Check 1.** (a) One of the two transistors is always off: no path from V_{DD} to ground. (b) 1/(2 × 0.5 mA/V^{2} × 8 V) = 1/(8 mS) = **125 Ω**.

**Check 2.** The two **pMOS in series** (pull-up); the two **nMOS in parallel** (pull-down).

**Check 3.** (a) Threshold-voltage shift, degraded subthreshold slope, increased off (leakage) current. (b) **One; three**. (c) Any two: complex and costly fabrication; width only in whole fins; higher parasitic capacitance; self-heating.

**Self-test.**

1. Two pMOS in parallel from V_{DD} to output; two nMOS in series from output to ground. 00, 01, 10 → at least one pMOS on, one nMOS off: output 1. 11 → both nMOS on, both pMOS off: output 0.
2. Four inputs: **8 transistors**. Pull-down: (a series b) in parallel with (c series d); pull-up: (a ∥ b) in series with (c ∥ d).
3. Near-zero static power, full rail-to-rail swing, strong 0 and strong 1.
4. The drain's field depletes part of the channel the gate would otherwise have to deplete, so less gate voltage is needed: V_{T} falls as length shrinks or V_{DS} rises.
5. Shorted-gate: the side gates are joined and act as one. Independent-gate: the two sides are driven separately; one can adjust the threshold.

<!--/ANSWERS-->
