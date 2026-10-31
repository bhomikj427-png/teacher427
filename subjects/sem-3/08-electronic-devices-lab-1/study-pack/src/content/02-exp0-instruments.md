# Exp 0 · Measuring DC and AC: power supply, function generator, DSO, multimeter

<div class="sub">Manual pp. 4–6 · hands-on · not assessed on its own, but every hands-on experiment (1, 3, 6, 7) depends on it</div>

[[map:0 Instruments > 1 Zener curve > 2 Regulator > 3 Clipper > 4 Clamper|here=1]]

**What you already have:** voltage, current, and a sine wave v(t) = V_{p} sin(2πft) from C&S.

**Three terms first:**

- **Peak V_{p}:** the sine's height above its centre line.
- **Peak-to-peak V_{pp}:** top to bottom, = 2V_{p}.
- **RMS:** the steady DC value that would heat a resistor equally. For a sine, V_{rms} = V_{p}/√2.

:::q <span class="tag">Manual Exp 0, aim</span>
Generation and measurement of the DC voltage and AC signals. Viva form: "The DSO shows 4 divisions peak-to-peak at 2 V/div, and one cycle spans 4 divisions at 0.25 ms/div. Give V_{pp}, V_{rms} and f."
:::

:::guess Guess first
Write your three numbers before reading on.
:::

## The four instruments

| Instrument | What it does | The knobs that matter |
|---|---|---|
| **DC power supply** | gives a steady voltage | voltage knob; **current-limit** knob (set it low to protect the circuit); + and − terminals |
| **Function generator** | gives a sine, square or triangle wave | waveform buttons, frequency range + fine knob, **amplitude**, **DC offset** (keep at 0 unless asked) |
| **DSO** (digital storage oscilloscope) | draws voltage against time | **VOLTS/DIV** (vertical scale), **TIME/DIV** (horizontal scale), **coupling DC/AC**, trigger, **Auto-set**, **Measure** menu |
| **DMM** (digital multimeter) | gives one number: V, A or Ω | knob position; black lead in **COM**; red lead in **VΩmA** (or **10A** for currents above 200 mA) |

[[fig:dso_screen|Reading a DSO screen: count divisions, then multiply by the knob setting.|w=70]]

## Reading the screen (the answer to the question)

- **Volts:** V_{pp} = (divisions top to bottom) × (VOLTS/DIV) = 4 × 2 = **8 V**. So V_{p} = 4 V.
- **RMS of a sine:** V_{rms} = V_{p}/√2 = 4/1.414 = **2.83 V**. This is what a DMM on AC volts should show.
- **Time:** T = (divisions per cycle) × (TIME/DIV) = 4 × 0.25 ms = 1 ms, so **f = 1/T = 1 kHz**.

| Wave | V_{rms} |
|---|---|
| sine | V_{p}/√2 = 0.707 V_{p} |
| triangle | V_{p}/√3 = 0.577 V_{p} |
| square | V_{p} |

:::trap Trap: the manual's RMS formula
The manual writes V_{rms} = V_{p}/√2 but has you read "V_{p}" as **peak-to-peak**. Divide **peak** by √2, or peak-to-peak by 2√2. Using V_{pp}/√2 gives an RMS twice too large.
:::

:::trap Trap: the meter and the wave shape
A basic DMM is calibrated for **sine waves**. On a square or triangle wave it can read wrong unless it says "True RMS". Basic meters also lose accuracy at higher frequencies, so keep the generator at about 1 kHz or lower for the meter comparison.
:::

:::do Do it (hands-on)
**DC:**

1. Set the supply to a value (e.g. 5 V), with the current limit low.
2. Connect the DSO probe tip to + and the probe's ground clip to −. Coupling **DC**.
3. Count the divisions the trace rises from the 0 V line, and multiply by VOLTS/DIV.
4. Read the same output with the DMM on DC volts.

**AC:**

1. Connect the generator output to the DSO (probe tip to signal, ground clip to ground).
2. Press Auto-set, or set VOLTS/DIV and TIME/DIV so that 1–2 cycles fill the screen.
3. Count V_{pp} divisions and the divisions in one period T. Calculate V_{rms} and f.
4. Measure the same output with the DMM on AC volts.
5. Repeat for the square and triangle waves.
:::

:::write Write in your record
**Observation table columns:** wave shape · divisions for V_{pp} · VOLTS/DIV · V_{pp} · divisions for T · TIME/DIV · T · f = 1/T · V_{rms} (calculated) · V_{rms} (DMM).

**Result:** average error of the DSO reading = (|DMM − DSO| / DMM) × 100 averaged over the readings.

**Theory for the record:** a function generator produces sine, square and triangle voltages of set amplitude and frequency. A DSO samples the input, stores it digitally and draws voltage against time on a grid. Amplitude = divisions × VOLTS/DIV, and period = divisions × TIME/DIV, with f = 1/T. A DMM measures DC/AC voltage, current and resistance. On AC it displays RMS, which for a sine equals V_{peak}/√2. A regulated DC supply holds its output constant against changes in load and line.
:::

:::check Check 1
(a) A triangle wave is 6 V peak-to-peak. What is its RMS? (b) The probe's ground clip is left unconnected. What does the trace typically look like? (c) Why must the DMM be on the mA port, and in series, to measure a current?
:::

<!--ANSWERS-->

## Answers

**Opening question.** V_{pp} = 8 V, V_{rms} = 2.83 V, f = 1 kHz.

**Check 1.** (a) V_{p} = 3 V, so V_{rms} = 3/√3 = **1.73 V**. (b) A noisy, fuzzy trace (often showing 50 Hz mains pickup), because the probe has no reference point. (c) An ammeter must carry the same current as the branch, so it goes in series. It has a very low resistance, so it must never be placed across a source: that is a short circuit, and it blows the meter's fuse.

<!--/ANSWERS-->
