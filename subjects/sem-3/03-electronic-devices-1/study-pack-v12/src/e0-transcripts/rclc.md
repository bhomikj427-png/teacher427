# Source: slides-U7-oscillators-RC-LC.ppt (old binary .ppt); method: deck_extract.py text runs in file order (no slide numbers; no olefile), images and OLE equation objects not viewed (image reads failed), 8 pictures saved; date 2026-11-19

Note: slide boundaries are not recoverable. Blocks below follow the text-run order of the file. Every equation is an embedded Equation/MathType object, so no equation text survived; the equations are reconstructed from the surrounding words only where the words state them (marked [eq missing]). No Hartley, Colpitts, crystal or relaxation-oscillator body text was found in the extractable runs; they appear only in the "Types of oscillators" list.

## Block 1: Oscillators / Introduction
Oscillators are circuits that produce a continuous signal of some type without the need of an input. These signals serve a variety of purposes. Communications systems, digital systems (including computers), and test equipment make use of oscillators.
Oscillator is an electronic circuit that generates a periodic waveform on its output without an external signal source. It is used to convert dc to ac. The waveform can be sine wave, square wave, triangular wave, and sawtooth wave.
An oscillator is a circuit that produces a repetitive signal from a dc voltage.
The feedback oscillator relies on a positive feedback of the output to maintain the oscillations.
The relaxation oscillator makes use of an RC timing circuit to generate a nonsinusoidal signal such as square wave.

## Block 2: Types of oscillators
1. RC oscillators: Wien Bridge, Phase Shift. 2. LC oscillators: Hartley, Colpitts. 3. Relaxation oscillators.

## Block 3: Basic principles for oscillation
An oscillator is an amplifier with positive feedback.
[picture/objects: feedback block diagram, not viewed]
The closed loop gain is: [eq missing; standard Af = A/(1 - A beta)].
In general A and beta are functions of frequency and thus may be written A(s), beta(s) [eq missing]. A(s)beta(s) is known as loop gain [eq missing]. Writing L(s) = A(s)beta(s), the loop gain becomes [eq missing]. Replacing s with j omega [eq missing]. At a specific frequency f0, L(j omega0) = 1 [eq missing]. At this frequency the closed loop gain will be infinite, i.e. the circuit will have finite output for zero input signal - oscillation.
Thus, the condition for sinusoidal oscillation of frequency f0 is [eq missing; L(j omega0) = A(j omega0) beta(j omega0) = 1]. This is known as Barkhausen criterion.
The feedback oscillator is widely used for generation of sine wave signals. The positive (in phase) feedback arrangement maintains the oscillations. The feedback gain must be kept to unity to keep the output from distorting.
If the feedback circuit returns the signal out of phase, an inverting amplifier produces positive feedback.

## Block 4: Design Criteria for Oscillators
1. The magnitude of the loop gain must be unity or slightly larger, i.e. [eq missing; |A beta| >= 1] (Barkhaussen criterion [sic]).
2. Total phase shift of the loop gain must be 0 deg or 360 deg.

## Block 5: Factors determining the frequency of oscillation
Oscillators can be classified into many types depending on the feedback components, amplifiers and circuit topologies used.
RC components generate a sinusoidal waveform at a few Hz to kHz range.
LC components generate a sine wave at frequencies of 100 kHz to 100 MHz.
Crystals generate a square or sine wave over a wide range, i.e. about 10 kHz to 30 MHz.

## Block 6: 1. RC Oscillators
RC feedback oscillators are generally limited to frequencies of 1 MHz or less. The types of RC oscillators discussed are the Wien-bridge and the phase-shift.

## Block 7: The Wien-Bridge Oscillator
RC feedback is used in various lower frequency sine-wave oscillators. The feedback circuit in a Wien-bridge uses a lead-lag circuit. When the Rs and Cs have equal values, the output will be [1/3 (eq missing)] of the input at only one frequency and the phase shift at this frequency will be 0 deg.
The lead-lag circuit of a Wien-bridge oscillator reduces the input signal by 1/3. The frequency of resonance can be determined by the formula below [eq missing; f0 = 1/(2 pi R C)].
Wien-bridge: it is a low frequency oscillator which ranges from a few kHz to 1 MHz. Structure of this oscillator is shown below [picture: Wien-bridge amplifier with lead-lag network and voltage divider R2/R1, not viewed].
From the previous equation, the magnitude condition is [eq missing; A beta = 1 with beta = 1/3 at f0]. To ensure oscillation, the ratio R2/R1 must be slightly greater than 2.
With the ratio [eq missing; K = 1 + R2/R1], then [eq missing]. K = 3 ensures the loop gain of unity oscillation.
- K > 3: growing oscillations
- K < 3: decreasing oscillations

## Block 8: Phase-shift
The three RC circuits combine to produce a phase shift of 180 deg. Fig. 3 shows a circuit containing three RC circuits in its feedback network called the phase-shift oscillator [picture, not viewed].
R-C Phase-shift: the phase shift oscillator utilizes three RC circuits to provide 180 deg phase shift that when coupled with the 180 deg of the amplifier itself provides the necessary feedback to sustain oscillations. The gain must be at least 29 to maintain the oscillations. The frequency of resonance for this type is similar to any RC circuit oscillator [eq missing; f0 = 1/(2 pi sqrt(6) R C)].
The transfer function of the RC network is [eq missing] (Phase-shift network). If the gain around the loop equals 1, the circuit oscillates at this frequency. Thus for the oscillations we want [eq missing]. Putting s = j omega and equating the real parts and imaginary parts to zero at omega0, we obtain: Imaginary part [eq missing]; Real part [eq missing].
Conditions for oscillation with the phase-shift oscillator: if all Rs are equal, the amplifier must have a gain of at least 29 to make up for the attenuation of the feedback circuit. This means that Rf/R3 [cut off by the extractor; eq missing: Rf/R3 >= 29].

## Block 9: Worked example (phase-shift design)
Design a phase-shift oscillator for a frequency of 800 Hz. The capacitors are to be 10 nF.
Start by solving for the resistors needed in the feedback circuit: R = [eq missing] = 8.12 kOhm (Use 8.2 kOhm.)
Calculate the feedback resistor needed: Rf = 29R = 238 kOhm.
[circuit labels: 10 nF, 8.2 kOhm, 238 kOhm]
