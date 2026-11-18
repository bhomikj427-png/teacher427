# finfet1 - source: exam-pack/slides-U4-finfet-structure-vs-mosfet.pptx (13 slides); method: text extraction with deck_extract.py, images not viewed; date 2026-11-19

## slide 1
Introduction to FinFETs Structure (page no. 474)

## slide 2
Outline (475): Why Multigate FinFET; FinFET Structure; Technology Scaling nodes (FinFET); FinFET Fabrication Steps

## slide 3
Why Multigate FinFET (476)
- At some point of scaling MOSFET, short channel effects show up: shift of Vth; sub-threshold slope degradation; off current (IOFF) increases. So overall performance (Figure of Merit) decreases.
- Multigate FinFET is a way to overcome this problem, and scaling continues.
- Citation: T. Dutta et al, "Impact of quantum effects on the short channel effects of III-V nMOSFETs in weak and strong inversion regimes", SSE.
- [picture: s003-image3.png, graph/figure of short-channel effects, not viewed]

## slide 4
FinFET Structure (478)
- FINFET stands for Fin Field Effect Transistor; it belongs to the FET family and is a type of Multi gate MOSFET used in place of a common MOSFET.
- Unlike regular FETs which are planar in shape, FINFET is non-planar having a 3D structure.

## slide 5
FinFET Structure
- FINFET is built on the silicon substrate and the gate is surrounded by the channel forming drain and source.
- Name derived from the fin of fish as the top view of FINFET drain and source appears like a fin. Fin can also be defined as the channel between the drain and the source.
- Like MOSFET, FINFET is also built on silicon on an insulator (SOI). It is also a three-terminal device forming gate, drain, and source.

## slide 6
FinFET Structure
- FinFET overcomes the short channel effect because of its fins and gate surrounded by channel from three sides; the fins increase the area covered by gate and increase the control of gate over the channel, which reduces the leakage current and helps to reduce the channel length and size of transistor.

## slide 7
Basic Structure of FinFET
- Fin: name derived from this 3D vertical fin-like structure that acts as channel. Made of semiconductor material or silicon.
- Gate: role similar to common MOSFET. Fin surrounds the gate and gate forms 3D structure, there can be more than one gate. Gate is made of metal. Controls current flow in channel.
- Drain and Source: similar role as in MOSFET. Carriers enter through source and exit from drain. Drain is at high potential and source at low potential.
- Substrate: base for the whole structure; helps to isolate device in chips.

## slide 8
Basic Structure of FinFET
- [picture: s008-image4.png, labelled FinFET structure diagram, whole slide is a picture, not viewed]

## slide 9 (479)
- The current flows on three facets of the fin.
- The equivalent channel width is therefore equal to the sum of the fin's width, WF, and twice its height (HF). [text as printed: "sum of the fin's width WF and twice its height HF"; formula W = WF + 2HF follows from line "WF+2HF yields the desired transistor width"]
- Suppose WF ~ 6 nm and HF ~ 50 nm.
- Since HF is not under the circuit designer's control, it appears that WF can be chosen so that WF+2HF yields the desired transistor width.
- WF affects device imperfections such as source and drain series resistance, channel-length modulation, and subthreshold conduction.
- Wider transistors can be obtained only by increasing the number of fins.
- Source: Behzad Razavi, "Design of Analog CMOS Integrated Circuit", 2nd edition.
- [pictures: s009-image5.jpg, s009-image6.jpg, not viewed]

## slide 10 (480)
Why is fin spacing important:
- If fins are too close: electric fields from neighbouring fins interact; parasitic capacitance increases; gate loses independent control of each fin.
- If fins are too far apart: area efficiency becomes poor; fewer fins fit in a given layout width.
- So [spacing] is chosen by the technology to balance electrical performance and layout density. (sic, symbol missing in text)
- The spacing between the fins, SF, also plays a significant role in the performance and is typically fixed.
- [pictures: s010-image7.png, s010-image8.png, not viewed]

## slide 11 (480)
- Due to the small dimensions of the intrinsic FinFET, the gate and S/D contacts must be placed away from the core of the device.
- Layout of single- and double-fin transistors. (Behzad Razavi, Design of Analog CMOS Integrated Circuit, 2nd edition)
- [pictures: s011-image9.png, s011-image10.png, not viewed]

## slide 12
Difference Between FinFET and MOSFET (table, MOSFET | FinFET)
- It is single gate device. | It is multi gate device.
- MOSFET is planar in shape. | FinFET is non planar in shape having 3d structure fins.
- It consume more power as compared to FinFET. | It consume less power as compared to MOSFET.
- Switching speed is comparatively slower than FinFET. | Switching Speed faster than MOSFET.
- More Leakage current. | Less leakage current than MOFSET.
- Less parasitic capacitance and resistance. | More parasitic capacitance and resistance due to non-planar shape.
- Less voltage gain. | More voltage gain.
- Easy to fabricate and less costly. | Complex to fabricate and costly.

## slide 13
- Better gate control in FinFET reduces leakage current, which directly reduces power loss.
- The channel turns ON/OFF sharply due to stronger electrostatic control.
- In MOSFETs, the gate cannot fully control the channel at small dimensions. FinFETs solve this by controlling the channel from multiple sides.
- FinFET improves control and power efficiency, but fabrication introduces extra parasitics.
- Better channel control -> higher transconductance -> improved gain.
- Parasitic capacitance is the unwanted capacitance that exists between different parts of an electronic device or circuit due to their physical proximity, even though no capacitor is intentionally placed there.

## Notes
- Mostly-picture slides per deck_extract: [8]. No [?] marks. Slide 2 outline lists "Technology Scaling nodes (FinFET)" but no slide covers it.
