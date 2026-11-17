## slide 1

Crystal oscillators

Crystal oscillators operate on the principle of the inverse piezoelectric effect. When alternating voltage is applied to the crystal, it vibrates at its natural frequency. Thes[e?] vibrations are then converted into oscillations.

These oscillators are usually made of Quartz crystal. In crystal oscillators, the crysta[l is?] suitably cut and mounted between two metallic plates as shown by Figure 1a whose electrical equivalent is shown by Figure 1b. In reality, the crystal behaves like a series RLC circuit, formed by the components.
* A low-valued resistor Rs
* A large-valued inductor Ls
* A small-valued capacitor Cs

which will be in parallel with the capacitance of its electrodes Cp.

Figure 1: (a) Quartz crystal slab mounted between two parallel metallic plates with horizontal connection leads; (b) Equivalent electrical circuit consisting of a series branch with capacitor Cs, inductor Ls, and resistor Rs connected in parallel with electrode capacitance Cp across two terminal leads.

Figure 1 (a) Quartz Crystal (b) Equivalent Electric Circuit

## slide 2

Due to the presence of Cp, the crystal will resonate at two different frequencies viz.,

Series Resonant Frequency, fs which occurs when the series capacitance Cs resonates with the series inductance LS. At this stage, the crystal impedance will be the least and hence the amount of feedback will be the largest. Mathematic[al?] expression for the same is given as

fs = 1 / (2 * pi * sqrt(Ls * Cs))

Parallel Resonant frequency, fp which is exhibited when the reactance of the LSCS leg equals the reactance of the parallel capacitor Cp i.e. LS and CS resonate with Cp. At this instant, the crystal impedance will be the highest and thus the feedback will be the least. Mathematically it can be given as

fp = 1 / (2 * pi * sqrt(Ls * (Cp * Cs) / (Cp + Cs)))

## slide 3

[Note: slide contains two picture objects: s003-image3.png (an exact duplicate of slide 2 image s002-image2.png layered underneath) and s003-image4.png (visible slide content layered over it).]

Crystal oscillators can be designed by connecting the crystal into the circuit such t[hat?] it offers low impedance when operated in series-resonant mode (Figure 2a) and [high?] impedance when operated in anti-resonant or parallel resonant mode (Figure 2b).

Figure 2(a): Transistor crystal oscillator operating in series resonance consisting of an NPN BJT with base bias resistors R1 (to VCC) and R2 (to ground), emitter resistor RE with parallel bypass capacitor CE to ground, collector connected through radio frequency choke RFC to VCC and to Output terminal, with a series feedback branch of Crystal and capacitor CC connected between collector and base.

Figure 2(b): Transistor crystal oscillator operating in parallel resonance consisting of an NPN BJT with base bias voltage divider R1 (to VCC) and R2 (to ground), base bypass capacitor C to ground, emitter resistor RE to ground, collector choke RFC to VCC and to Output terminal, a capacitive divider with C1 between collector and emitter and C2 between emitter and ground, and Crystal connected between collector and ground in parallel across the capacitive divider.

Graph (right): Output Impedance vs. frequency f showing a curve that drops through a Capacitive region (f < fs) to minimum impedance RS at series resonance fs (labeled Series Resonance and Crystal Frequency), rises sharply through an Inductive region (fs < f < fp) to a peak impedance ZP at parallel resonance fp (labeled Parallel Resonance), and falls off into a Capacitive region (f > fp).

Figure 2 Crystal Oscillator Operating in (a) Series Resonance (b) Parallel Resonance

## Done report

* Files written:
  - `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/xtal.md`
* Sections written:
  - `## slide 1`
  - `## slide 2`
  - `## slide 3`
  - `## Done report`
* Counts:
  - Slides transcribed: 3 (slides 1, 2, 3)
  - Circuit and graph descriptions: 5 (Figure 1(a), Figure 1(b), Figure 2(a), Figure 2(b), Output Impedance vs. frequency graph)
  - Equations: 2 (series resonant frequency fs, parallel resonant frequency fp)
  - Worked examples / questions: 0
  - Tables: 0
* What could not be read / every `[?]`:
  - Slide 1 (`s001-image1.png`):
    - `Thes[e?]`: final 'e' partially obscured at right edge by a screen overlay widget.
    - `the crysta[l is?]`: 'l' and subsequent word 'is' clipped at right margin by image edge/overlay widget.
  - Slide 2 (`s002-image2.png`):
    - `Mathematic[al?]`: 'al' cut off at right margin by circular sparkle overlay button.
  - Slide 3 (`s003-image4.png`):
    - `such t[hat?]`: 'hat' occluded at right edge by overlay button.
    - `and [high?]`: word preceding 'impedance' at end of line 2 occluded by overlay button.
  - Slide 3 (`s003-image3.png`):
    - Duplicate image object identical to `s002-image2.png` positioned underneath `s003-image4.png`.
