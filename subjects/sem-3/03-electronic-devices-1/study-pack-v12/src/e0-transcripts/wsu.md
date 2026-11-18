# wsu - source: exam-pack/slides-U4-logic-design-with-mosfets-WSU.pdf (53 pages, Dae Hyun Kim, EECS, Washington State University); method: pymupdf text extraction, images not viewed (overbars lost in extraction are restored as x' / ~x only where the logic makes it certain, marked (bar)); date 2026-11-19

Every page carries a figure (circuit or truth table); the text below is what the text layer holds.

## page 1
Logic Design with MOSFETs. Dae Hyun Kim, EECS, Washington State University.
## page 2
References: John P. Uyemura, "Introduction to VLSI Circuits and Systems", 2002, Chapter 2. Neil H. Weste and David M. Harris, "CMOS VLSI Design: A Circuits and Systems Perspective", 2011, Chapter 1.
## page 3
Goal: design logic gates using MOSFETs (NMOS and PMOS).
## page 4
Signals and Wires. Signals: 0 = VSS = Ground = GND = Low = 0V. 1 = VDD = Power = PWR = High = 5V, 3.3V, 1.5V, 1.2V, 1.0V, etc. Wires: wire 1 / wire 2 "No connection"; "Connection". [picture: wire diagrams]
## page 5
Ideal Switches. Switch; assert-high switch (A = 1: closed, y = x; A = 0: open, y undefined); assert-low switch (A = 0: closed, y = x; A = 1: open). Control input. [picture: switch symbols]
## page 6
Series/Parallel Connections of Switches. Series: y = x.a.b = x.(a.b), AND operation (y defined only when a = 1 and b = 1; undefined if a = 0 or b = 0). Parallel: x.a + x.b = x.(a+b), OR operation (y defined only when a = 1 or b = 1; undefined if a = 0 and b = 0). Truth tables a,b -> y: 00 undefined; 01 -> 1 x; 10 -> 1; 11 -> 1 (parallel); series 00, 01, 10 undefined, 11 -> x. [picture: switch networks]
## page 7
Inverter Design with Switches. The output is defined both when a = 0 and when a = 1. y = 1.(a bar) + 0.a = (a bar). Truth table a=0 -> 1; a=1 -> 0. [picture: two-switch inverter]
## page 8
Inverter Design with Switches. Two inverter designs ([picture]: the 1 and 0 rails swapped, switches controlled by a and a bar). "Why?"
## page 9
MOSFETs as Switches. n-channel MOSFET = nFET = NMOS; p-channel = pFET = PMOS; Complementary MOS: CMOS. Symbols: nFET (VD >= VS), pFET (VS >= VD), each equated to a switch with VG, VS, VD labels.
## page 10
MOSFETs as Switches. Threshold voltage: nFET VTn > 0; pFET VTp < 0.
- nFET: OFF: VGSn <= VTn; ON: VGSn > VTn.
- pFET: OFF: VSGp <= |VTp|; ON: VSGp > |VTp|.
- Logic translation: nFET Mn, input VA from 0 to VDD: A = 0 (Mn OFF) for 0..VTn; A = 1 (Mn ON) for VTn..VDD. pFET Mp: A = 0 (Mp ON) for 0..VDD-|VTp|; A = 1 (Mp OFF) for VDD-|VTp|..VDD.
## page 11
MOSFETs as Switches, examples:
- PTM High-Performance 45nm High-K Metal Gate: VDD 1.0V; VTn 0.46893V; VTp -0.49158V.
- PTM High-Performance 32nm High-K Metal Gate: VDD 0.9V; VTn 0.49396V; VTp -0.49155V.
- PTM High-Performance 22nm High-K Metal Gate: VDD 0.8V; VTn 0.50308V; VTp -0.4606V.
## page 12
Pass Characteristics. nFET (VG = VDD, VS = Vout, VD = Vin): Vin up, VGS down, Vout up; Vin 0 -> 0; Vin 0.1 -> 0.1; ... Vin VDD-VTn -> VDD-VTn; Vin VDD -> VDD-VTn (output stops at VDD - VTn). "Logic 0 transfer: strong logic 0. Logic 1 transfer: weak logic 1."
pFET (VG = 0, VS = Vin, VD = Vout): Vin down, VSG down, Vout down; Vin VDD -> VDD; VDD-epsilon -> VDD-epsilon; ... Vin |VTp| -> |VTp|; Vin 0 -> |VTp| (output stops at |VTp|). "Logic 0 transfer: weak logic 0. Logic 1 transfer: strong logic 1."
## page 13
Pass Characteristics: SPICE simulation (45nm technology), nFET. [picture: Vin, Vout waveform vs VDD]
## page 14
Pass Characteristics: SPICE simulation (45nm technology), pFET. [picture: Vin, Vout waveform, 0 marked]
## page 15
Pass Characteristics. nFET: strong logic 0 transfer, weak logic 1 transfer. pFET: strong logic 1 transfer, weak logic 0 transfer. CMOS: use pFETs to pass logic 1; use nFETs to pass logic 0.
## page 16
Basic Logic Gates in CMOS. Principles: construct the nFET network using only nFETs and the pFET network using only pFETs. If the output is 1, the pFET network connects VDD to the output and the nFET network disconnects VSS and the output. If the output is 0, the nFET network connects VSS to the output and the pFET network disconnects VDD and the output. [picture: block diagram, pFET network on top, nFET network below, inputs a, b, c, ..., output f]
## page 17
Inverter: f = (x bar). x = 0: f = 1; x = 1: f = 0 (other FET off). f = (x bar).1 + x.0 = (x bar). # TRs: 2 (nFET: 1, pFET: 1).
## page 18
Basic Logic Gates in CMOS: SPICE simulation. [picture only: inverter waveforms]
## page 19
Two-input NAND (NAND2). f = (a bar).(b bar).1 + (a bar).b.1 + a.(b bar).1 + a.b.0 = (a bar) + (b bar) = NOT(a.b). Cases shown: a=0,b=0 -> f=1; a=0,b=1 -> f=1; a=1,b=1 -> f=0. # TRs: 4 (nFETs 2, pFETs 2).
## page 20
SPICE simulation (NAND2). [picture only]
## page 21
Two-input NOR (NOR2). f = NOT(a+b). f = (a bar).(b bar).1 + (a bar).b.0 + a.(b bar).0 + a.b.0 = (a bar).(b bar) = NOT(a+b). Cases: 00 -> f=1; 01 -> f=0; 11 -> f=0. # TRs: 4 (nFETs 2, pFETs 2).
## page 22
SPICE simulation (NOR2). [picture only]
## page 23
Complex Logic Gates in CMOS. Example f = NOT(a.(b+c)). Using logic gates (two versions) vs using TRs: # TRs: 14 (nFETs 7, pFETs 7); # TRs: 10 (nFETs 5, pFETs 5); using TRs: # TRs: 6 (nFETs 3, pFETs 3). [pictures: gate-level diagrams]
## page 24
How to design. Inverter: f = (x bar) = (x bar).1 + x.0; nFET network connects 0 and the output; pFET network connects 1 and the output. NAND2: f = NOT(a.b) = (a.b bar).1 + a.b.0 = ((a bar)+(b bar)).1 + a.b.0; nFET network expressed by a and b: (a.b); pFET network expressed by a bar and b bar: ((a bar)+(b bar)).
## page 25
How to design f: express f = A.1 + B.0 = F(x1..xn).1 + (F bar)(x1..xn).0. Design a pFET network using A = F (pFETs are ON when inputs are 0). Design an nFET network using B = F bar (nFETs are ON when inputs are 1). Example f = NOT(a.(b+c)).1 + a.(b+c).0 = ((a bar) + (b bar).(c bar)).1 + a.(b+c).0. [picture: pFET and nFET networks]
## page 26
Example f = NOT(a.(b+c)); # TRs: 6 (nFETs 3, pFETs 3). [picture: full gate]
## page 27
Structured logic design: design a given Boolean equation using nFETs and pFETs. Assume only non-inverted input signals are given (a, b, c, ...); (a bar), (b bar), (c bar) are not given, generate them if needed.
## page 28
Design methodology 1: when f = NOT(S(x1..xn)) (S a function of non-inverted variables): f = (S bar) = (S bar).1 + S.0. Design an nFET network for S using x1..xn. Design a pFET network for (S bar) using x1..xn. Connect to VDD, VSS, f. Example f = NOT(a.(b+c)): nFET network for a.(b+c); pFET network for NOT(a.(b+c)) = (a bar) + (b bar).(c bar).
## page 29
Design methodology 2: f = NOT(S). Design an nFET network for S. Design a pFET network with a dual logic of the nFET network. Dual of f(x1..xn, 0, 1, AND, OR) = f(x1..xn, 1, 0, OR, AND). Example f = NOT(a.(b+c)): nFET network for a.(b+c); dual of a.(b+c) = a + b.c.
## page 30
Dual logic. f^D(x1..xn, 0, 1, AND, OR) = f(x1..xn, 1, 0, OR, AND). Examples: (A.B)^D = A + B; (A+B)^D = A.B; (1.A)^D = 0 + A = A; (1+A)^D = 0.A = 0; (0.A)^D = 1 + A = 1; (0+A)^D = 1.A = A. Principles: the nFET and pFET networks work complementarily; if the nFET network is ON (connects VSS to the output), the pFET network is OFF (disconnects the output from VDD) and vice versa. If two networks are dual, they work complementarily. "Prove!"
## page 31
Principles of the dual logic: f = S(x1..xn) = S.1 + (S bar).0 [as printed]. S bar(x1..xn) = S(x bar...) = S(x1..xn, 1, 0, OR, AND) = S^D (De Morgan's law). A pFET is ON when its control variable (xi) is 0. Thus the pFET network is the dual of the nFET network.
## page 32
Design methodology 3: f = S (S a function of non-inverted variables): f = NOT(NOT S). Design (S bar) and add an inverter at the output. Example f = a.(b+c): f = NOT(NOT(a.(b+c))). Design NOT(a.(b+c)), add an inverter at the output. [picture]
## page 33
Design methodology 4: f = S(x bar...) (S a function of inverted variables): generate inverted inputs from the given inputs; design S using the inverted inputs. Example f = (a bar).((b bar)+(c bar)). Inverters not shown for brevity. [picture]
## page 34
Design methodology 5: f = S(x...): f = S = (S bar)^D ... [printed: f = S(x1..xn) = S(x bar..)^D = S(x bar..)^D]; design S(...)^D using the given inputs; add an inverter at the output. Example f = (a bar) + ((b bar).(c bar)): f = NOT(a.(b+c)) = a.(b+c) bar. [picture]
## page 35
Design methodology 6: f = S(x bar...): f = NOT(NOT S); generate inverted inputs, design S bar using the inverted inputs and add an inverter at the output.
Design methodology 7: f = S(x bar...): f = S(x bar..) = S(x..)^D; design S^D using the given non-inverted inputs.
Design methodology 8: when f = S(x1, x1 bar, ..., xn) or similar: convert the given function into an appropriate form to simplify the logic; design it.
## page 36
Examples (assuming only non-inverted inputs are available): f = a.b (AND2): design f = NOT(a.b) and add an inverter at the output (# TRs: 6); or design f = a.b = (a bar)+(b bar) with two inverters to generate a bar and b bar (# TRs: 8). f = (a bar).b + (c bar).d: add two inverters to generate a bar and c bar, then design f (# TRs: 12). f = (s bar).a + s.b (2:1 MUX) [no count given].
## page 37
Bubble pushing (how to construct a pFET network): f = A.1 + B.0 = F.1 + (F bar)^D.0 [as printed]. NOR-type: f = (a.b).0 / f = (a+b).0; (a bar).(b bar).1 / f = ((a bar)+(b bar)).1. [pictures: five networks]
## page 38
Bubble pushing example, f from inputs a, b, c, d, e (four network pictures with "="). [picture only]
## page 39
XOR: a xor b = a.(b bar) + (a bar).b = NOT(a.b + (a bar).(b bar)) [overbar lost in extraction] (#TRs: 8+4 (for the two inverters)). XNOR: a xnor b = a.b + (a bar).(b bar) = ... (#TRs: 8+4 (for the two inverters)). [pictures: schematics]
## page 40
Structured logic analysis: derive a Boolean equation for a given transistor-level schematic. Analysis methodology 1: convert the nFET network into a Boolean equation (only when the pFET network is the dual of the nFET network); notice the nFET network passes logic 0. Example f = [whole-expression overbar lost in extraction] a.b + (a bar).(b bar) = ((a bar)+(b bar)).(a+b) = a.(b bar) + (a bar).b (i.e. f = NOT(XNOR) = XOR, consistent with the a xor b label on the schematic). [picture]
## page 41
Analysis methodology 2: identify all the paths from VSS to the output (only when the pFET network is the dual of the nFET network); merge them into a single Boolean equation; negate the output. Example: Path 1: b.a. Path 2: c.a. Merge: b.a + c.a = a.(b+c). Negate: NOT(a.(b+c)). f = NOT(a.(b+c)). [picture]
## page 42
Pass Transistors. nFET: g = 0: OFF; g = 1: ON. a = 0: b = strong 0; a = 1: b = weak 1. pFET: g = 1: OFF; g = 0: ON. a = 0: b = weak 0; a = 1: b = strong 1.
## page 43
Transmission Gate Circuits. Behaviours: when s = 0 both nFET and pFET are OFF; when s = 1 both are ON. If x = 0, the nFET perfectly transmits it to y (nFET is good at transferring 0). If x = 1, the pFET perfectly transmits it to y (pFET is good at transferring 1). Disadvantage: needs s bar; does not restore the input signals. [pictures: transistor circuit and symbol]
## page 44
Logic design using transmission gates: MUX: f = (s bar).x0 + s.x1. XNOR: f = a xnor b (the text layer prints the xor/xnor symbol with its overbar lost; inputs a, b, b bar, s, s bar). [pictures]
## page 45
Pass Transistors vs. Transmission Gates (table). Signal strength: pass TR strong 0 / weak 1 (nFET) or weak 0 / strong 1 (pFET); transmission gate strong 0, strong 1. Area: pass TR A, r.A (r > 1); transmission gate 1 + r.A [as extracted "A, rA (r>1), 1+rA"; read as A + rA]. Control signal: g (pass); g, g bar (transmission gate).
## page 46
Buffer: Y = A. Buffers are used for signal restoration; interconnect optimization. [pictures: symbol and two-inverter schematic]
## page 47
Tristate Inverter. Truth table: EN = 0 -> Y = Z; EN = 1 -> Y = (A bar). Symbol and schematic [pictures].
## page 48
Tristate Buffer: symbol and gate-level schematic [pictures only].
## page 49
Sequential Circuit - D Latch. Positive-level-sensitive D latch: CLK = 0: Q holds; CLK = 1: Q follows D (transparent). Waveforms CLK, D, Q vs t with VDD axis; regions marked Transparent, Capture, Hold.
## page 50
D Latch schematic (Q, Q bar, D, CLK, CLK bar labels) [picture].
## page 51
Sequential Circuit - D Flip-Flop. Positive-edge-triggered D flip-flop: CLK = 0 or 1: Q holds; CLK rising edge: catch D. Waveforms with Capture / Hold regions.
## page 52
D Flip-Flop schematic [picture].
## page 53
Sequential Circuit example. Inputs: D, AND/RST (as extracted "D, ..., CLK, CLK bar"), CLK, CLK bar; outputs Q, Q bar. [pictures: three images]

## Notes
- Extraction garbled the over-bars; bars are written "(a bar)" above. Whole-expression overbars are mostly lost, so some lines (pages 31, 34, 37, 39, 40, 44) are only approximate. No [?] used; uncertain items are described in brackets where they occur (pages 31, 34, 37, 40, 44, 45).
