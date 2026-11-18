# finfet2 - source: exam-pack/slides-U4-finfet-types-and-fabrication.pptx (9 slides); method: text extraction with deck_extract.py, images not viewed; date 2026-11-19

## slide 1
FinFET - Introduction

## slide 2
Why FinFET. FinFETs are an improvement on MOSFETs:
- better channel control: 3D fin-shaped structure gives better electrostatic control over the channel; regulates current flow and reduces short-channel effects. FinFETs have a wrap-around gate over the thin body, which makes channel doping optional.
- lower leakage current: lower than planar MOSFETs because the vertical fin structure and better gate control reduce leakage. Lower leakage in the off state reduces standby power consumption.
- faster switching speeds: faster than planar MOSFETs because of their 3D architecture and better channel control.

## slide 3
FinFET
- Unlike planar MOSFETs, built on a flat silicon substrate, FinFETs have a gate that surrounds multiple sides of the channel, forming a multigate structure.
- FinFETs can be created on either a bulk silicon wafer or Silicon-on-Insulator (SOI).
- The name "FinFET" comes from the design's resemblance to a fish's back fin.
- The channel is a three-dimensional structure called a "fin", as opposed to the flat channel in traditional MOSFETs.
- [pictures: s003-image1.png, s003-image2.png, s003-image3.png, not viewed]

## slide 4
FinFET gate
- By enveloping the channel, the gate offers better control, leading to improved performance and lower power consumption.
- In traditional MOSFETs, dopants are introduced into the channel to reduce short-channel effects (SCEs) and ensure a high threshold voltage. FinFETs naturally mitigate SCEs with their thin body and wrap-around gate, making channel doping optional.
- This reduces sensitivity to dopant-induced variations and enhances carrier mobility in the channel. As a result, FinFETs can operate at lower threshold voltages, offering better performance and lower power dissipation than planar MOSFETs.
- Channel of FinFET is vertical.
- [picture: s004-image4.png, not viewed]

## slide 5
FinFET
- [picture: s005-image5.png, whole slide is a picture, not viewed]

## slide 6
Types of FinFET: shorted-gate (SG) and independent-gate (IG).
- SG FinFETs are also known as three-terminal (3T) FinFETs and IG FinFETs as four-terminal (4T) FinFETs.
- In SG FinFETs, both gates are jointly used to control the electrostatics of the channel. Hence, SG FinFETs show higher on-current (Ion) and also higher off-current (Ioff or the subthreshold current) compared to those of IG FinFETs.
- IG FinFETs offer the flexibility of applying different signals or voltages to their two gates. This enables the use of the back-gate bias to modulate the Vth of the front gate linearly. However, IG FinFETs incur a high area penalty due to the need for placing two separate gate contacts.
- [picture: s006-image6.png, not viewed]

## slide 7
FinFET Fabrication steps
1. Substrate: basis is a lightly p-doped substrate with a hard mask on top (e.g. silicon nitride) as well as a patterned resist layer.
2. Fin etch: fins are formed in a highly anisotropic etch process. Since there is no stop layer on a bulk wafer as there is in SOI, the etch process has to be time based. In a 22 nm process the width of the fins might be 10 to 15 nm, the height would ideally be twice that or more.
3. Oxide deposition: to isolate the fins from each other, an oxide deposition with a high aspect ratio filling behaviour is needed.
4. Planarization: the oxide is planarized by chemical mechanical polishing. The hard mask acts as a stop layer.
- [pictures: s007-image7..image10.png, four process-step images, not viewed]

## slide 8
5. Recess etch: another etch process is needed to recess the oxide film to form a lateral isolation of the fins.
6. Gate oxide: on top of the fins the gate oxide is deposited via thermal oxidation to isolate the channel from the gate electrode. Since the fins are still connected underneath the oxide, a high-dose angled implant at the base of the fin creates a dopant junction and completes the isolation (not illustrated).
7. Deposition of the gate: finally a highly n+-doped poly silicon layer is deposited on top of the fins, thus up to three gates are wrapped around the channel: one on each side of the fin, and - depending on the thickness of the gate oxide on top - a third gate above.
- [pictures: s008-image11..image13.png, not viewed]

## slide 9
FinFET advantages and disadvantages
- Disadvantages: self-heating effect; quantized device-width; higher parasitics due to 3-D profile; very high capacitances; "Cornet effect" (sic, probably corner effect); high fabrication cost.
- Advantages: better control over the channel; suppressed short-channel effects; lower static leakage current; faster switching speed; higher drain current; lower switching voltage; low power consumption.

## Notes
- Mostly-picture slides per deck_extract: [5]. No [?] marks. No slide notes were produced by deck_extract.
