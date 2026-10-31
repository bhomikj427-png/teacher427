# Exp 4 · Diode clamper circuit

<div class="sub">Manual pp. 15–16 · LTspice · CO3 · the manual's sample output minimum (−9.38 V) matches the simulation below</div>

[[map:0 Instruments > 1 Zener curve > 2 Regulator > 3 Clipper > 4 Clamper|here=5]]

**What you already have:** the clipper from Exp 3, which **cuts** a wave. From C&S, a capacitor keeps its charge unless current flows, and τ = RC sets how fast it discharges.

**Two terms first:**

- **Clamper (DC restorer):** a circuit that **shifts** the whole wave up or down without changing its shape. It adds a DC level.
- **Peak-to-peak preserved:** the wave keeps its full V_{pp}. Only its position moves.

:::q <span class="tag">Manual Exp 4, aim</span>
To implement a diode clamper circuit and observe its output waveform. Viva form: "Input is ±5 V. The output swings from about +0.5 V to −9.4 V. Explain where the −4.4 V shift comes from."
:::

:::guess Guess first
Which part could be storing a voltage that adds to the input?
:::

## How it works

[[fig:exp04_circuit|Fig 4.1: series C, diode to ground (anode at V_{o}), 1 MΩ load.|w=62]]

1. **First positive peak:** V_{in} rises, V_{o} tries to go positive, and the diode turns on, holding V_{o} ≈ +0.5 V. The capacitor charges to about **V_{p} − 0.5 ≈ 4.5 V**, positive on the input side.
2. **After that** the diode is off. The capacitor cannot discharge quickly, because its only path is the 1 MΩ: τ = RC = 1 MΩ × 0.01 µF = **10 ms**, which is 10× the 1 ms period. So it acts like a 4.5 V battery in series with the input:

$$V_{o} = V_{in} − V_{C} ≈ V_{in} − 4.5 V$$

So the output swings from +5 − 4.5 = **+0.5 V** to −5 − 4.5 = **−9.5 V**. Same 10 V p-p, but shifted down by the capacitor's voltage. This is a **negative clamper**: the positive peak is clamped at about 0 V, and the wave sits below it.

[[fig:exp04_wave|LTspice: V_{o} from +0.48 V to −9.39 V. The output is clamped in the very first cycle.|w=90]]

**Reverse the diode** (cathode at V_{o}): the negative peak clamps at about −0.5 V, and the wave sits above it, a **positive clamper**. **Add a battery** in series with the diode: the clamping level moves to that battery's voltage ± 0.7 V.

:::do Do it (LTspice)
1. V1: right-click, **Advanced → SINE**, DC offset 0, amplitude 5, frequency 1k (= `SINE(0 5 1k)`).
2. C1 = `0.01u`. Diode D1: Pick New Diode → **1N914**, with its anode on the output node and cathode to ground. R1 = `1Meg` (**not** `1M`!).
3. Directive: `.tran 0 5m 0 2u`. Run. Plot the input wire and V(vo).
4. Use cursors to read the maximum and minimum of V_{o}. Then V_{pp} = max − min, and the DC shift = (max + min)/2.
:::

| Quantity | LTspice value |
|---|---|
| V_{o} maximum (clamped level) | +0.48 V |
| V_{o} minimum | −9.39 V |
| V_{o} peak-to-peak | 9.87 V (input 10 V) |
| average of V_{o} (DC shift) | −4.41 V |

:::write Write in your record
**Result:** output clamped at about **+0.5 V** (positive peak); V_{o} swings +0.48 V to −9.39 V; peak-to-peak 9.87 V ≈ input 10 V; DC level shifted by about −4.4 V. Negative clamper.

**Theory for the record:** a clamper shifts a waveform's DC level without changing its shape or peak-to-peak value. A capacitor in series charges through the diode to (nearly) the input peak on the first half cycle. With the diode off, it discharges only through the load, so it must have RC ≫ T (here 10 ms ≫ 1 ms). The capacitor voltage then adds to the input, shifting the wave so that one peak sits at the diode's clamping level. Diode direction sets negative/positive clamping; a series battery sets the reference level.
:::

:::trap Traps
- `1M` in LTspice is 1 **milli**ohm. With R ≈ 0, the capacitor discharges every cycle and nothing clamps.
- If RC is comparable to T, the capacitor droops between peaks and the output tilts. The rule is RC ≥ 10T (some books use 5T).
:::

:::check Check 1
(a) Clipper vs clamper: one sentence each on what happens to V_{pp}. (b) Replace 0.01 µF with 100 pF. What goes wrong, and why? (c) Diode reversed: give V_{o}'s max and min.
:::

<!--ANSWERS-->

## Answers

**Opening question.** The capacitor charges to about 4.5 V on the first positive peak (through the diode). It then can't discharge (τ = 10 ms ≫ 1 ms), so it stays in series with the input as a −4.5 V offset.

**Check 1.** (a) A clipper **reduces** V_{pp} (part of the wave is cut). A clamper **keeps** V_{pp} and only shifts the DC level. (b) τ = 1 MΩ × 100 pF = 0.1 ms ≪ 1 ms: the capacitor discharges between peaks, so the shift is not held and the output distorts. (c) Positive clamper: min ≈ −0.5 V, max ≈ +9.5 V.

<!--/ANSWERS-->
