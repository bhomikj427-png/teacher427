# exam-pack/: professor material for Electronic Devices (& Circuits)

**What this folder is:** the professor's decks, solved-numerical sheets and exam tips. These files set
**scope and emphasis** only. Facts come from the prescribed textbooks (honesty rule,
`../../research-engine/exam-resources.md`). Never teach a fact straight off a slide.

**Course actually taken:** **ECE2106 Electronic Devices & Circuits** (2025-26 scheme). The syllabus is printed on
slide 2 of `slides-U1-U2-…`. It is ECE2101's five units **plus U6 Feedback and U7 Oscillators**. The
folder name and `../course-info.md` still say ECE2101, the old scheme. See the 2026-11-13 entry in `../progress-log.md`.

Naming: `slides-U<unit>-[L<lecture>-]<topic>`. Sorting by name puts the files in syllabus order.
`NUMERICALS-` = solved problem sheets. `TIP-` = exam hints. Lecture numbers (L08, L20…) are the
professor's own where the original filename gave them.

## Index (filed 2026-11-13 from `_inbox`; original names in `../../_inbox/TRIAGE-LOG.md`)

| Unit | File | Slides / pp. | Covers |
|---|---|---|---|
| U1–U2 | `slides-U1-U2-semiconductor-physics-to-pn-junction.pptx` | 100 | **Syllabus slide (S2).** Semiconductor types, valence/bonding, intrinsic/extrinsic, doping, mobility, temperature, energy bands, Fermi–Dirac + Fermi level, intrinsic concentration, minority carriers, drift/diffusion transport, Poisson equation, diode static/dynamic resistance |
| U2 | `slides-U2-L08-diode-load-line-and-series-parallel.pptx` | 19 | Diode load-line analysis, Q-point; series, parallel, series-parallel diode circuits (worked examples) |
| U2 | `slides-U2-L09-diode-rectifiers.pptx` | 27 | Half-wave, full-wave (bridge + centre-tapped), V_DC = 0.318/0.636 V_m, PIV, efficiency, summary table |
| U2 | `slides-U2-L10-diode-clippers-clampers-multipliers.pptx` | 22 | Series/parallel clippers (biased), clampers, voltage multipliers |
| U2 | `slides-U2-special-diodes-LED-tunnel-photodiode.pptx` | 40 | LED working; tunnel (Esaki) diode: tunnelling, negative resistance, band diagrams, equivalent circuit; photodiode types (PN, p-i-n, double heterostructure; several type slides are image-only) |
| U3 | `slides-U3-jfet.pptx` | 44 | FET classification, n/p-channel JFET construction, pinch-off, output + transfer characteristics, Shockley equation, **the four parameters g_m, r_d, μ (+ μ = g_m·r_d derivation)**, CS + CD amplifiers |
| U3 | `TIP-JFET-parameters-8marks-2026-10-05.md` | — | Classmate's relay: JFET parameters "8 marks" |
| U3–U4 | `NUMERICALS-U3-U4-jfet-dmosfet-emosfet-solved.pdf` | 21 pp. (scan) | ~31 solved Qs: Shockley I_D, V_GS(off)/V_P, g_m vs V_GS, self/voltage-divider bias, d.c. load line, D-MOSFET I_D + zero-bias amplifier, E-MOSFET K from I_D(on), transconductance curves |
| U4 | `slides-U4-mosfet-types-and-characteristics.pptx` | 29 | Enhancement/depletion, n/p-channel structure, operation, V-I characteristics, region-wise equations, K constant |
| U4 | `slides-U4-mosfet-biasing-and-digital-circuits.pptx` | 16 | Gate bias, drain-to-gate (feedback) bias, voltage-divider bias, MOSFET digital circuits (slides 2–9 are images) |
| U4 | `slides-U4-logic-design-with-mosfets-WSU.pdf` | PDF | Third-party lecture (D. H. Kim, Washington State Univ.; refs Uyemura, Weste & Harris): ideal switches, NMOS/PMOS as switches, CMOS gates |
| U4 (extra) | `slides-U4-finfet-structure-vs-mosfet.pptx` | 13 | Why multigate, short-channel effects, fin structure, fin spacing, FinFET vs MOSFET |
| U4 (extra) | `slides-U4-finfet-types-and-fabrication.pptx` | 9 | Same topic, different deck: shorted vs independent gate, fabrication steps, pros/cons |
| U5 | `slides-U5-L20-bjt-construction.pptx` | 8 | npn/pnp, layers, junctions, naming |
| U5 | `slides-U5-L21-bjt-operation.pptx` | 6 | npn/pnp working, current components |
| U5 | `slides-U5-L22-common-base.pptx` | 8 | CB: α, I_C expression, input/output characteristics |
| U5 | `slides-U5-L23-25-common-emitter-and-load-line.pptx` | 17 | CE: β, α–β relation, characteristics, comparison of CB/CE/CC, d.c. load line, operating point |
| U5 | `slides-U5-L26-27-biasing-stability-h-parameters.pptx` | 53 | Stability factor; fixed, emitter-stabilised, voltage-divider bias (exact + approx.), Q-point movement, bias compensation (diode/transistor); CE amplifier, phase reversal, **h-parameter model: A_i, Z_i, A_v, Y_o** |
| U5 (extra) | `slides-U5-multistage-amplifier-and-darlington.pptx` | 13 | Cascaded BJT stages, overall gain, Darlington connection + d.c. bias |
| U5 | `NUMERICALS-U5-h-parameter-book-pp131-145.pdf` | 8 pp. (photos) | Book *Electronic Devices & Circuits* pp. 131–145, h-parameter Problems 3–16: CE/CC exact vs approximate analysis, R_i = h_i − h_r·A_v…, cascade/Darlington, bootstrap, Miller |
| U6 | `slides-U6-feedback-amplifiers.pptx` | 51 | Amplifier classification (V/I/G_m/R_m), +ve/−ve feedback, sampling + mixing, 4 topologies, gain/Z_in/Z_out with feedback, gain stabilisation, distortion/noise, bandwidth |
| U7 | `slides-U7-oscillators-RC-LC.ppt` | old .ppt | Barkhausen criterion, RC phase-shift (R_f = 29R), Wien bridge, LC (Hartley, Colpitts), relaxation oscillator |
| U7 | `slides-U7-crystal-oscillators.pptx` | 3 (images) | Inverse piezoelectric effect, quartz equivalent circuit (R_s, L_s, C_s ∥ C_p) |

"(extra)" = taught on the decks but not named in the syllabus text. Treat it as examinable until a PYQ says otherwise.

## Not yet here
No PYQs (MTE/ETE) and no course hand-out yet. When they arrive, rebuild `../knowledge-base/exam-map.md` from them.

## Duplicates removed
- 2026-11-13: `jfet numericals (1).pdf`, byte-identical (MD5) to the kept numericals sheet.
