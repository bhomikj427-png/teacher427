# Special Diodes: LED, Tunnel Diode, and Photodiode

## slide 1

### What is an LED?
- Light-emitting diode
- Semiconductor
- Has polarity

**Circuit / Component Diagram:**
- Diagram of a 5 mm plastic indicator LED showing translucent dome lens, flat notch on base rim labeled "flat", shorter lead labeled "cathode (-)", and longer lead labeled "anode (+)".

---

## slide 2

### What is a Light-Emitting Diode (LED)?
- A device that converts electrical energy into Light
- A p-n junction diode that emits monochromatic light when forward biased.
- Requires 1.5 ~ 4 V and 10 mA to turn ON
- One needs to use a resistor to prevent overloading

**Circuit / Component Diagram:**
- Schematic symbol of an LED: Standard diode triangle-and-bar symbol with two outgoing diagonal arrows pointing upward-right indicating light emission.
- LED package cutaway: Depicts plastic body with internal anvil/post leads labeled "ANODE" (+) on the longer lead and "CATHODE" (-) on the shorter lead.
- DC limiting circuit: A 10 V DC supply rail connected in series with a current-limiting resistor labeled "resistor limits current" to the anode of an LED, with the LED cathode connected to the 0 V reference rail.

---

## slide 3

### Light Emitting Diodes (LEDs)
### Advantages of Light Emitting Diodes (LEDs)
- **Longevity:** The light emitting element in a diode is a small conductor chip rather than a filament which greatly extends the diode’s life in comparison to an incandescent bulb (10 000 hours life time compared to ~1000 hours for incandescence light bulb)
- **Efficiency:** Diodes emit almost no heat and run at very low amperes.
- **Greater Light Intensity:** Since each diode emits its own light
- **Cost:** Not too bad
- **Robustness:** Solid state component, not as fragile as incandescence light bulb

**Circuit / Component Diagram:**
- Structural cutaway diagram of a through-hole LED: Labeled parts include "Lens" with dimension "~ 50 mm" (⚠ looks wrong: dimension labeled ~ 50 mm, standard indicator LED diameter is ~ 5 mm), "Semiconductor (LED chip) (.25 mm^2, chip not drawn to scale)", shorter "Cathode lead (to negative pole of battery)", and longer "Anode lead (to positive pole of battery)".
- Photographic inset: Illuminated white LED emitter glowing in darkness.

---

## slide 4

### How does it work?
- P-n junction
- Electrical Contacts
- A typical LED needs a p-n junction
- Junction is biased to produce even more e-h and to inject electrons from n to p for recombination to happen
- There are a lot of electrons and holes at the junction due to excitations
- Electrons from n need to be injected to p to promote recombination
- Recombination produces light!!

**Circuit / Component Diagram:**
- Forward-biased pn junction cross-section: Upper p-layer contacted by ohmic contacts with positive terminal (+) delivering forward current I; lower n-layer contacted by ohmic contact connected to negative terminal (-) in series with resistor R; electrons (solid black circles) in n-type inject across the metallurgical junction into the p-type region to recombine with holes (open white circles), emitting light directed upward labeled "Light emission" with red undulating wavy arrows.
- Photographic inset: Illuminated white LED emitter glowing in darkness.

---

## slide 5

### Small Band Gap: Low Energy Red Light
- p-type
- n-type
- hole
- electron
- e-
- e- Conduction Band
- Valence Band
- Small Band Gap

**Circuit / Component Diagram:**
- Top device schematic: Forward-biased semiconductor bar with p-type region (open circles representing holes drifting right) and n-type region (red circles representing electrons drifting left) connected across an external DC voltage source (+ on p-side, - on n-side) with an LED schematic symbol drawn above the junction.
- Bottom energy band diagram: Conduction band (e- Conduction Band) and Valence Band sloped downward under forward bias, separated by a bandgap labeled "Small Band Gap" with a double-headed arrow; electron transition across the bandgap produces a low-frequency, long-wavelength red wavy photon ray.

---

## slide 6

### Large Band Gap: High Energy Blue Light
- p-type
- n-type
- hole
- electron
- e-
- e- Conduction Band
- Valence Band
- Large Band Gap

**Circuit / Component Diagram:**
- Top device schematic: Identical forward-biased semiconductor structure as slide 5 with external DC source (+ on p-side, - on n-side), LED schematic symbol above, showing holes drifting right and electrons drifting left toward the junction.
- Bottom energy band diagram: Conduction band (e- Conduction Band) and Valence Band separated by a significantly wider bandgap labeled "Large Band Gap" with a double-headed arrow; electron transition across the wide bandgap produces a high-frequency, short-wavelength blue wavy photon ray.

---

## slide 7

### LED chip is the part that we shall deal with in this course
- (a) Lead-type
- (b) SMD-type

**Circuit / Component Diagram:**
- Diagram (a) Lead-type LED: Cutaway view showing LED chip mounted in a reflective cup of the Cathode lead using Conductive Silver paste, connected via an Au wire bond to the Anode lead, enclosed in molded epoxy Resin sealing.
- Diagram (b) SMD-type LED: Cross-section and top view of surface-mount device showing PCB substrate with Cathode electrode and Anode electrode, Cathode index notch, LED chip bonded with Conductive Silver paste, Au wire bond, encapsulated under domed Resin sealing.

---

## slide 8

### Structures of LED (Important ones) - I:
- Dome and planar LED are used in most display devices where the interest is in extracting the maximum amount of light from the device.
  =>Light is emitting in all directions and using a lens arrangement to focus the light
- Burrus and edge-emitting LED are used mainly in optical fiber communication systems

**Circuit / Component Diagram:**
- Diagram 1 (Dome LED): Hemispherical n-type dome with a central "Diffused p-type" region located at the bottom center between green "Ohmic contacts"; red arrows indicate radial "Light Output" exiting in all directions through the hemispherical surface.
- Diagram 2 (Planar LED): Planar rectangular structure showing top "p - type epitaxial layer" with perimeter green "Ohmic contacts" and lower "n - type substrate" with bottom full-surface green "Ohmic contacts"; red arrows indicate "Light Output" radiating upward and laterally from the edges.

---

## slide 9

### LED Material Properties:
- For efficient light emission, direct band-gap semiconductors are preferred (e.g. GaAs). As carriers recombine across the active region of the P-N junction device, the active region cannot be either n- or p-type as there are a lot of electron as well as a lot of holes.
- The Fermi energy, therefore, has to split and have separate quasi-Fermi energy for electrons (E_Fn) and quasi-Fermi energy for holes (E_fp).
- The wavelength of the light emitted is then proportional to this band-gap (E_g = h\nu). (⚠ looks wrong: band-gap energy E_g = h\nu is directly proportional to frequency \nu, but inversely proportional to wavelength \lambda = hc / E_g).

**Circuit / Component Diagram:**
- Graph: Energy vs crystal wavevector K showing conduction band valley profile with central direct \Gamma valley (direct energy gap E_gd), satellite X valley (indirect gap E_gi1), and satellite L valley (indirect gap E_gi2); lower valence band curves below the dashed reference line indicate Light Hole, Heavy Hole, and Split-off Band (Split Band).

---

## slide 10

### Direct and Indirect transition in Semiconductors
- LED's

**Equations:**
- E_g - \hbar\omega = 0
- \hbar k_{elec.} - \hbar k_{hole} = 0
- E_{ph} = \hbar\omega
- \hbar \equiv Reduced Plank's Constant (⚠ looks wrong: misspelled "Plank's" instead of "Planck's")
- \omega \equiv Frequency of the Photon
- E_{ph} = E_g - E_p

**Circuit / Component Diagram:**
- Top-left diagram: Discrete energy levels in LED active region showing electron and hole transitions with wavy horizontal emission arrows labeled "Spontaneous Emission".
- Top-right graph (Direct Band Gap): E vs k plot centered at k = 0 showing aligned conduction band minimum E_c and valence band maximum E_v separated by energy gap E_g; process 1 (orange arrow, "Absorption") excites carrier from E(k') to E(k'') absorbing photon E_ph = \hbar\omega; process 2 (blue arrow, "Recombination Emission") drops electron from E_c to E_v emitting photon E_ph = \hbar\omega without wavevector change (\Delta k = 0).
- Bottom-right graph (Indirect Band Gap): E vs k plot with valence band peak at k = 0 (E_v) and conduction band minimum shifted along k-axis by \Delta h (or \Delta k) at energy E_c; blue step-like arrow indicates "Recombination emission" involving phonon exchange of energy E_p to satisfy momentum conservation, emitting photon E_ph = E_g - E_p.
- Bottom-left graph: Phonon dispersion relation plotting phonon energy \hbar\omega_k versus wavevector \hbar\vec{a}_k with upper branch labeled "OP" (optical phonon) and lower branch labeled "AP" (acoustic phonon).

---

## slide 11

### TUNNEL DIODE (Esaki Diode)
- It was introduced by Leo Esaki in 1958.
- Heavily-doped p-n junction
- Impurity concentration is 1 part in 10^3 as compared to 1 part in 10^8 in p-n junction diode
- Width of the depletion layer is very small(about 100 A).
- It is generally made up of Ge and GaAs.
- It shows tunneling phenomenon.
- EV
- (a) Normally Doped P and N-Type Materials
- (b) Very Heavily Doped P-Type Material
- (c) Very Heavily Doped N-Type Material

**Circuit / Component Diagram:**
- Schematic symbol of Tunnel Diode: Anode lead on left connecting to diode triangle pointing right, with cathode bar having inward brackets at the ends, leading to Cathode lead on right.
- Band diagram (a) Normally Doped P and N-Type Materials: Conduction Band (EMPTY), Forbidden Gap E_G, Valence Band (FILLED).
- Band diagram (b) Very Heavily Doped P-Type Material: Conduction Band (EMPTY), Forbidden Gap E_G, Valence Band showing Fermi level penetrating into valence band, leaving top strip of valence band as EMPTY ENERGY LEVELS above lower FILLED ENERGY LEVELS.
- Band diagram (c) Very Heavily Doped N-Type Material: Conduction Band showing Fermi level penetrating into conduction band, creating lower strip of FILLED ENERGY LEVELS below upper EMPTY ENERGY LEVELS, Forbidden Gap E_G, Valence Band (FILLED).

---

## slide 12

### WHAT IS TUNNELING
- Classically, carrier must have energy at least equal to potential-barrier height to cross the junction .
- But according to Quantum mechanics there is finite probability that it can penetrate through the barrier for a thin width.
- This phenomenon is called tunneling and hence the Esaki Diode is know as Tunnel Diode. (⚠ looks wrong: original text has grammatical error "is know as")
- Triangular potential barrier approximation of the potential barrier in the tunnel diode.

**Circuit / Component Diagram:**
- Graph: Potential energy V(x) on vertical axis versus position x on horizontal axis, plotting a right-triangular potential barrier ramping linearly upward across the width of the "Space charge region".

---

## slide 13

### P-TYPE MATERIAL / N-TYPE MATERIAL (Isolated Bands)
- P-TYPE MATERIAL
  - CONDUCTION BAND: EMPTY
  - FORBIDDEN GAP: E_G
  - VALENCE BAND: top strip EMPTY, lower region FILLED
- DEPLETION REGION
- N-TYPE MATERIAL
  - CONDUCTION BAND: lower strip FILLED, upper region EMPTY
  - FORBIDDEN GAP: E_G
  - VALENCE BAND: FILLED

**Circuit / Component Diagram:**
- Band structure alignment diagram showing isolated degenerate P-type material and N-type material separated by the Depletion Region: P-type has conduction band empty, forbidden gap E_G, and valence band top states empty due to heavy acceptor doping; N-type has conduction band bottom states filled due to heavy donor doping, forbidden gap E_G, and valence band completely filled.

---

## slide 14

### CHARACTERISTIC OF TUNNEL DIODE
- - Ve Resistance Region
- Vf
- Vp
- Ip
- Vv
- Forward Voltage
- Reverse voltage
- Iv
- Reverse Current
- Forward Current
- Ip:- Peak Current
- Iv :- Valley Current
- Vp:- Peak Voltage
- Vv:- Valley Voltage
- Vf:- Peak Forward Voltage

**Circuit / Component Diagram:**
- Graph: Complete I-V characteristic curve of a tunnel diode showing Forward Current vs Forward Voltage in quadrant 1 and Reverse Current vs Reverse Voltage in quadrant 3; forward curve rises sharply from origin to Peak Current (Ip) at Peak Voltage (Vp), descends through the negative dynamic resistance region ("- Ve Resistance Region") to Valley Current (Iv) at Valley Voltage (Vv), then turns upward exponentially past Peak Forward Voltage (Vf, where current again equals Ip) under normal diode injection; reverse curve increases monotonically and steeply from the origin with increasing reverse bias.

---

## slide 15

### TUNNEL DIODE — ENERGY BANDS <-> I-V CHARACTERISTIC
- Tunnel Diode I-V Characteristic
- Energy Bands of Heavily Doped p+ - n+ Junction
- EQUILIBRIUM
- V = 0.00 V
- I = 0.07 (normalized)
- No net tunneling current
- Very thin depletion layer; no favorable net state overlap.
- PEAK
- NEGATIVE RESISTANCE
- VALLEY
- THIN DEPLETION REGION

**Circuit / Component Diagram:**
- Left graph: Tunnel Diode I-V Characteristic plotting normalized Current (0.0 to 1.0) vs Forward bias voltage V (0.0 to 0.75 V) with operating point at V = 0.00 V, I = 0.07 (green dot), rising to PEAK at ~0.2 V, dropping through NEGATIVE RESISTANCE region (shaded blue between 0.2 V and 0.43 V) to VALLEY at ~0.43 V (I = 0.36), and rising into diffusion conduction.
- Right graph: Energy Bands of heavily doped p+ - n+ junction at equilibrium (V = 0.00 V) showing thin depletion region (shaded blue), conduction band edge E_C (blue line), valence band edge E_V (orange line), and constant dashed Fermi level E_F (green dashed line) cutting through valence band on p+ side and conduction band on n+ side with zero net carrier transfer.

---

## slide 16

### ENERGY BAND DIAGRAM
- Energy-band diagram of pn junction in thermal equilibrium in which both the n and p region are degenerately doped.
- Energy-band diagram f a pn junction in thermal equilibrium in which both the n and p region are degenerately doped. (⚠ looks wrong: caption in slide has typo "diagram f a")
- n
- p
- E_C
- E_V
- E_F
- Space charge region

**Circuit / Component Diagram:**
- Diagram: Detailed equilibrium energy-band diagram of a degenerately doped pn junction showing constant horizontal dashed purple Fermi level E_F across the narrow "Space charge region" (demarcated by vertical dashed lines); on the n-side (left), E_F is above conduction band edge E_C with filled states shaded grey; on the p-side (right), E_F is below valence band edge E_V with filled states shaded grey up to E_F.

---

## slide 17

### AT ZERO BIAS
- -Zero current on the I-V diagram;
- All energy states are filled below EF on both sides of the junction;
- Simplified energy-band diagram and I-V characteristics of the tunnel diode at zero bias.
- Simplified energy-band diagram and I-V characteristics of he tunnel diode at zero bias. (⚠ looks wrong: caption has typo "of he tunnel diode")
- I
- V

**Circuit / Component Diagram:**
- Left diagram: Simplified energy-band diagram at zero bias showing horizontal dashed Fermi line with grey-shaded filled states aligned on both sides, such that electrons in the n-side conduction band face filled states in the p-side valence band, resulting in zero net tunneling current.
- Right graph: I vs V Cartesian coordinate axes with an operating point dot located at the origin (0, 0).

---

## slide 18

### AT SMALL FORWARD VOLTAGE
- Electrons in the conduction band of the n region are directly opposite to the empty states in the valence band of the p region.
- So a finite probability that some electrons tunnel directly into the empty states resulting in forward-bias tunneling current.
- Simplified energy-band diagram and I-V characteristics of the tunnel diode at a slight forward bias.
- Simplified energy-band diagram and I-V characteristics of he tunnel diode at a slight forward bias. (⚠ looks wrong: caption has typo "of he tunnel diode")
- e-
- I
- V

**Circuit / Component Diagram:**
- Left diagram: Simplified energy-band diagram at small forward bias showing n-side energy levels raised relative to p-side; electrons in the filled n-side conduction band are directly opposite available empty states in the p-side valence band, tunneling horizontally across the thin junction (indicated by purple arrow labeled "e-").
- Right graph: I vs V plot showing forward characteristic rising from the origin with an operating point dot positioned on the initial upward slope in the first quadrant.

---

## slide 19

### AT MAXIMUM TUNNELING CURENT (⚠ looks wrong: misspelled "CURENT" in slide title)
- The maximum number of electrons in the n region are opposite to the maximum number of empty states in the p region.
- Hence tunneling current is maximum.
- Simplified energy-band diagraam and I-V characteristics of the tunnel diode at a forward bias producing maximum tunneling current. (⚠ looks wrong: misspelled "diagraam" in slide text, and caption has typo "of he tunnel diode")
- e-
- I
- V

**Circuit / Component Diagram:**
- Left diagram: Simplified energy-band diagram at peak bias where forward bias raises the n-side conduction band to maximize the overlap between filled n-side electron states and unoccupied p-side valence states, indicated by two horizontal tunneling arrows labeled "e-".
- Right graph: I vs V plot showing the tunneling current curve reaching its crest, with an operating point dot located at the peak of the curve.

---

## slide 20

### AT DECREASING CURRENT REGION
- The forward-bias voltage increases so the number of electrons on the n side, directly opposite forbidden states on the p side decreases. (⚠ looks wrong: awkwardly phrased; as forward bias increases, filled n-side states move opposite the forbidden energy bandgap of the p-side, decreasing available empty states for tunneling)
- Hence the tunneling current decreases.
- Simplified energy-band diagram and I-V characteristics of the tunnel diode at a higher forward bias producing less tunneling current.
- Simplified energy-band diagram and I-V characteristics of he tunnel diode at a higher forward bias showing less tunneling current. (⚠ looks wrong: caption has typo "of he tunnel diode")
- e-
- I
- V

**Circuit / Component Diagram:**
- Left diagram: Simplified energy-band diagram at higher forward voltage where n-side bands are raised further, leaving only a small portion of filled n-side conduction states facing empty p-side valence states while the rest face the forbidden gap, with a single tunneling arrow labeled "e-".
- Right graph: I vs V plot illustrating the negative differential resistance region, with an operating point dot placed on the downward slope past the peak.

---

## slide 21

### AT HIGHER FORWARD VOLTAGE
- No electrons on the n side are directly opposite to the empty states on the p side.
- The tunneling current is zero.
- The normal ideal diffusion current exists in the device.
- Simplified energy-band diagram and I-V characteristics of the tunnel diode at a forward bias for which the diffusion current dominates.
- Simplified energy-band diagram and I-V characteristics of he tunnel diode at a forward bias for which the diffusion current dominates. (⚠ looks wrong: caption has typo "of he tunnel diode")
- e-
- I
- V

**Circuit / Component Diagram:**
- Left diagram: Simplified energy-band diagram at large forward bias where the n-side conduction band edge is raised entirely above the p-side valence band top edge (zero band overlap for tunneling); electrons cross the junction via conventional thermal diffusion over the barrier (illustrated by a curved purple arrow labeled "e-").
- Right graph: I vs V plot showing the current passing the valley minimum and rising exponentially like an ordinary diode, with an operating point dot on the steep exponential branch and a dashed green reference curve along the valley.

---

## slide 22

### AT REVERSE BIAS VOLTAGE
- Electrons in the valence band on the p side are directly opposite to empty states in the conduction band on the n side.
- Electrons tunnel directly from the p region into the n region.
- The reverse-bias current increases monotonically and rapidly with reverse-bias voltage.
- A simplified energy-band diagram of a tunnel diode with a reverse bias voltage
- I-V characteristic of a tunnel diode with a reverse-bias voltage.
- e-
- I
- V

**Circuit / Component Diagram:**
- Left diagram: Simplified energy-band diagram under reverse bias showing p-side bands raised relative to n-side; filled states in the p-side valence band align directly opposite empty states in the n-side conduction band, allowing electrons to tunnel directly from p to n (horizontal arrow pointing left labeled "e-").
- Right graph: I vs V characteristic showing forward characteristic as a dashed purple curve in quadrant 1, and a solid purple reverse tunneling curve in quadrant 3 dropping steeply and monotonically from the origin to a dot.

---

## slide 23

### TUNNEL DIODE EQUIVALENT CIRCUIT
- This is the equivalent circuit of tunnel diode when biased in negative resistance region.
- At higher frequencies the series R and L can be ignored. (⚠ looks wrong: in practical high-frequency equivalent circuits, parasitic series resistance rs and series inductance Ls become more prominent and degrade performance, rather than being negligible)
- Hence equivalent circuit can be reduced to parallel combination of junction capacitance and negative resistance.
- Cj
- -R
- rs
- Ls

**Circuit / Component Diagram:**
- Small-signal equivalent circuit schematic: A parallel combination of junction capacitance Cj and negative resistance -R, connected in series with series lead resistance rs in the upper conductor and series lead inductance Ls in the lower conductor, terminating at two open circular output terminals.

---

## slide 24

### Tunnel Diode Applications
- A tunnel diode is a heavily doped semiconductor device that uses quantum tunneling to create a region of negative differential resistance. Its primary applications include ultra-high-speed switching, microwave oscillators, and high-frequency amplifiers due to its near-instantaneous response time.
- **High-Frequency and Microwave Uses**
  - **Microwave Oscillators:** Acts as a negative resistance oscillator to generate stable high frequencies up to gigahertz ranges.
  - **Microwave Amplifiers:** Used in reflection-type amplifiers and satellite communication front-ends.
  - **Frequency Converters and Mixers:** Utilized in radar and communication receivers to process high-frequency signals

---

## slide 25

### THE BASIC PRINCIPLE OF OPTOELECTRONIC DETECTION
- When a photon of energy greater than the band gap of the semiconductor material (i.e., h\nu \ge E_g) is incident on or near the depletion region of the device, it excites an electron from the valence band into the conduction band. The vacancy of an electron creates a hole in the valence band.
- Electrons and holes so generated experience a strong electric field and drift rapidly towards the n and p sides, respectively.
- The resulting flow of current is proportional to the number of incident photons. Such a reverse-biased p-njunction, therefore, acts as a photodetector and is normally referred to as a p-n photodiode.
- Light rays
- Electron emission

**Circuit / Component Diagram:**
- Diagram (a) Top: Reverse-biased pn photodiode with negative lead (-) on p-side and positive lead (+) on n-side; within the central "Depletion region", an electron-hole pair separates under the electric field: hole (open circle) drifts left toward p, electron (solid circle) drifts right toward n.
- Diagram (a) Bottom: Energy band diagram under reverse bias showing conduction band E_c, valence band E_v, and Fermi level E_F; incident photon h\nu generates an electron-hole pair in the depletion region, sweeping the electron down the conduction band slope to the n-side and the hole up the valence band slope to the p-side.
- Inset diagram: Photoelectric emission schematic showing incoming yellow undulating "Light rays" striking a material slab and ejecting electrons (blue circles with minus sign) along red diagonal vectors labeled "Electron emission".

---

## slide 26

### Types of Photodiode
- EHP created close to the depletion layer can diffuse and subsequently be swept across the junction by the large electric field due to applied reverse biased voltage. An external current is produced but it is delayed with respect to variations in the incident optical power
- It is desirable that photon be absorbed in the depletion layer so that it can contribute maximum in generation of photocurrent.
- Typical pn photodiodes have a rise time of the order of microseconds making them unsuitable for high speed optical systems.
- The existence of electric field across the junction facilitate the rise of photocurrent
- The primary operating wavelength regions for FO communication systems are 850nm, 1310nm and 1550 nm. The photodetectors which are used in these systems are :
  - PN junction photodiodes
  - PIN photodiodes
  - Avalanche photodiode

---

## slide 27

### Types of Photodiode
### P-N junction photodiode
- The simplest structure is that of a p-nphotodiode, shown in Fig. (a).
- Incident photons of energy, say hn, are absorbed not only inside the depletion region but also outside it, as shown in Fig. (b).
- the photons absorbed within the depletion region generate electron–hole pairs. Because of the built-in strong electric field [shown in Fig. (c)],
- The resulting flow of photocurrent constitutes the response of the photodiode to the incident optical power. The response time is governed by the transit time tdrift , which is given by

**Equations:**
- \tau_{drift} = w / v_{drift}
- In order to minimize tdrift, both w and vdrift can be tailored. The depletion layer width w is given
- w = [ (2 * \epsilon / e) * (V_{bi} + V_0) * (1 / N_a + 1 / N_d) ]^{1/2}

**Circuit / Component Diagram:**
- Multi-part diagram:
  - (a) Cross-section of a reverse-biased pn junction connected to reverse bias voltage source V_0 and series load resistor Load, with light h\nu incident on the p-surface, showing central depletion layer width w (shaded).
  - (b) Plot of Optical power versus depth z showing exponential absorption decay through the device with the portion absorbed in the depletion width w shaded.
  - (c) Plot of Electric field versus depth z showing a high electric field peak confined strictly within the "Depletion region".

---

## slide 28

### Types of Photodiode
### P-N junction photodiode
- As incident photons are absorbed outside the depletion region also. The electrons generated in the p-side have to diffuse to the depletion-region boundary before they can drift (under the built in electric field) to the n-side.
- In a similar fashion, the holes generated in the n-side have to diffuse to the depletion region boundary for their drift towards the p-side.
- The diffusion process is inherently slow and hence the presence of a diffusive component may distort the temporal response of a photodiode, as shown in Fig.
- Input optical pulse
- Output electrical pulse

**Circuit / Component Diagram:**
- Dual-pane waveform plot:
  - (a) "Incident optical power" vs "Time" depicting an ideal square-wave pulse labeled "Input optical pulse".
  - (b) "Photocurrent" vs "Time" depicting the distorted "Output electrical pulse" characterized by a sharp initial drift-induced step, a slow curved rise due to carrier diffusion until pulse termination, an immediate drift cutoff drop, and an extended exponentially decaying "diffusion tail".

---

## slide 29

### Types of Photodiode
### PIN Photodiode
- The P-Intrinsic-N structure increases the distance between the P and N conductive layers, decreasing capacitance, increasing speed. The volume of the photo sensitive region also increases, enhancing conversion efficiency. The bandwidth can extend to 10's of GHz. PIN photodiodes are the preferred for high sensitivity, and high speed at moderate cost.
- PIN photodiode.

**Circuit / Component Diagram:**
- Left schematic: Reverse-biased p-i-n junction with battery (+ to n+ layer, - to p+ layer) across wide intrinsic layer "i (n-)"; incoming photons with E = h\nu generate electron-hole pairs that drift across the intrinsic region, while longer-wavelength light with E < E_g passes through without absorption.
- Top-right 3D model: PIN photodiode mesa structure showing "top metal contact" (+), "p diffusion" layer, "intrinsic region (larger depletion region)", "n type" layer, "n+ contact region", and "bottom metal contact" (-), with yellow light arrows entering the circular top window.
- Inset photograph: Two packaged fiber-pigtailed/leaded PIN photodiode modules.

---

## slide 30

### Types of Photodiode
### P-i-N PHOTODIODE
- A typical P-i-N photodiode consists of a highly-doped transparent p-type contact layer on top of an undoped absorbing layer (i) and an n-type highly doped contact layer on the bottom.
- This diode is evolved mainly from one basic requirement: light should be absorbed in the depletion region of the diode to ensure that the electrons and holes are separated in the electric field and contribute to the photocurrent, while the transit time must be minimal.
- This implies that a depletion region larger than the absorption length must exist in the detector. This is easily assured by making the absorbing layer undoped. Only a very small voltage is required to deplete the undoped region.
- An added advantage is that the recombination/generation time constant is longest for undoped material, which provides a minimal thermal generation current.

---

## slide 31

### Types of Photodiode
- A double heterostructure, improves the performance of the p-i-n photodiodes.
- Herein, the middle i-region of a material with lower band gap is sandwiched between p- and n-type materials of higher band gap, so that incident light is absorbed only within the i-region.
- Such a configuration is shown in Fig. The band gap of InP is 1.35 eV and hence it is transparent for light of wavelength greater than 0.92 µm, whereas the band gap of lattice-matched InGaAs is about 0.75 eV, which corresponds to a ʎc of 1.65 µm
- Thus the intrinsic layer of InGaAs absorbs strongly in the wavelength range 1.3–1.6 µm.
- The diffusive component of the photocurrent is completely eliminated in such a heterostructure simply because the incident photons are absorbed only within the depletion region.
- Such photodiodes are very useful for fiber-optic systems operating in the range 1.3–1.6 µm.
- (a) Structure of a p-i-n photodiode. (b) Electric-field distribution inside the device under reverse bias.
- A double heterostructure design of a p-i-n photodiode using InGaAs/InP

**Circuit / Component Diagram:**
- Top figure: (a) Cross-section of a reverse-biased PIN photodiode with incident light h\nu on p-layer, bias voltage, series Load resistor, and intrinsic region width w; (b) Electric-field distribution vs depth z showing strong electric field spanning across the intrinsic region w under reverse bias.
- Bottom diagram: Mesa cross-section of an InGaAs/InP double heterostructure p-i-n photodiode showing top Au/Au-Sn metal contact, P-InP layer, i-InGaAs absorbing layer, N-InP layer, N^+-InP substrate, and bottom annular ohmic contacts allowing light h\nu to enter through the substrate.

---

## slide 32

### Types of Photodiode
### Avalanche Photodiodes (APD) – Photodetector with Internal gain
- Avalanche photodiode showing high electric field region
- Photodiode with Internal gain: Internally multiply the primary signal photocurrent before it enters the input circuitry of the amplifier.
- Increases receiver sensitivity: the photocurrent is multiplied before encountering the thermal noise associated with the receiver circuit.
- For carrier multiplication, the photogenerated carriers must traverse a region where a very high electric field is present.

**Circuit / Component Diagram:**
- Device cross-section and electric field distribution: Left diagram depicts reverse-biased reach-through APD circuit with DC supply and Load resistor across layers ordered n, p, i, p^+ from top to bottom, with optical input hf incident on the top n-layer; right graph plots Electric field vs depth x showing an intense high-field peak in the "Gain region" (n-p junction) and a lower flat electric field in the wide "Absorption region" (i layer).

---

## slide 33

### Types of Photodiode
- In the high field region, a photogenerated electron or hole can gain enough energy so that it ionizes bonds in the valence band upon colliding with them. This is known as Impact Ionization
- The newly created carriers are also accelerated by the high electric field, gaining enough energy to cause further impact ionization. This phenomenon is the Avalanche Effect
- Create an extremely high electric field region (approximately 3 x 10^5 V/cm)
- Requires high reverse bias voltages (100 to 400 V) in order that the new carriers created by impact ionization (⚠ looks wrong: sentence is cut off and incomplete in original slide)
- Carrier multiplication factors as great as 10^4 may be obtained

---

## slide 34

### Types of Photodiode
- When carriers are generated in undepleted material, they are collected somewhat slowly by the diffusion process. This has the effect of producing a long 'diffusion tail' on a short optical pulse.
- When the APD is fully depleted by employing high electric fields, all the carriers drift at saturation-limited velocities.
- The response time for the device is limited by three factors:
  - the transit time of the carriers across the absorption region (i.e. the depletion width)
  - the time taken by the carriers to perform the avalanche multiplication process
  - the RC time constant incurred by the junction capacitance of the diode and its load
- At low gain the transit time and RC effects dominate giving a definitive response time and hence constant bandwidth for the device
- At high gain the avalanche build-up time dominates and therefore the device bandwidth decreases proportionately with increasing gain

---

## slide 35

### Types of Photodiode
- The rise time between 150-200ps and fall time of 1ns or more are quite common and this limits the overall response of the device
- Multiplication factor M is a measure of the internal gain provided by the APD and is defined as
  M = I_M / I_p
  where I_M is the average value of the total multiplied output current and I_p is the primary photocurrent.
- The avalanche mechanism is a statistical process, and not every carrier pair generated in the APD experiences the same multiplication. Thus, the measured value of M is expressed as an average quantity which is as great as 10^4 .
- Analogous to p-n and p-i-n photodiodes, the performance of an APD is described by its responsivity \mathcal{R}_{APD}, given by
  \mathcal{R}_{APD} = ((\eta * e) / (h * \nu)) * M = M * \mathcal{R}

---

## slide 36

### Quantum Efficiency (Q.E.)
- Quantum efficiency is defined as the fraction of the incident photons that contribute to photocurrent.

**Equations:**
- \eta = (number of emitted electrons) / (number of incident photons)
- One of the major factor which determine the quantum efficiency is the absorption coefficient of the semiconductor material used within photodetector. \eta < 1 quoted as a percentage say 85% i.e. 85 electrons collected per 100 incident photons
- It is related to responsivity by
  Q.E. = R_\lambda * ((h * c) / (\lambda * q))

---

## slide 37

### Responsivity
- The responsivity of a silicon photodiode is a measure of the sensitivity to light, and is defined as the ratio of the photocurrent I_p to the incident light power P at a given wavelength.
- R_\lambda = I_p / P
- It varies with the wavelength of the incident light as well as applied reverse bias and temperature. It is a measure of the effectiveness of the conversion of the light power into electrical current.
- Temperature Coefficient of Responsivity Vs. Wavelength For Silicon Photodiode
- The responsivity variations due to change in temperature is due to decrease or increase of the band gap, because of increase or decrease in the temperature respectively

**Circuit / Component Diagram:**
- Graph 1 (Left): Responsivity (A/W) vs Wavelength (nm) (range 200 to 1100 nm, y-axis 0.0 to 0.7 A/W) for Silicon photodiodes showing three curves: "Photovoltaic" (dotted line, peak ~0.62 A/W at ~920 nm), "Blue Enhanced" (thin solid line, peak ~0.48 A/W at ~950 nm), and "UV Enhanced" (thick solid line, peak ~0.54 A/W at ~850 nm).
- Graph 2 (Right): Temperature Coefficient of Responsivity (%/°C) vs Wavelength (nm) (range 300 to 1100 nm, y-axis -1.5 to 1.5 %/°C) for Silicon photodiode; curve begins at -0.4 %/°C at 300 nm, crosses 0 at ~500 nm, stays near +0.1 %/°C between 600-800 nm, dips toward 0 at 850 nm, and rises steeply to +1.5 %/°C at 1000 nm.

---

## slide 38

### Responsivity & Quantum efficiency
- Comparison of the responsivity and QE as a function of wavelength for photodiodes constructed of different materials.
- Quantum Efficiency is not constant at all wavelengths-varies according to photon energy.
- For a given material, as the wavelength of the incident photon becomes larger, the photon energy becomes less than that required to excite an electron from the valence band to the conduction band.
- Responsivity falls off rapidly beyond cutoff wavelength.

**Circuit / Component Diagram:**
- Graph: Responsivity (A/W) (vertical axis 0 to 1.0) versus Wavelength (\mu m) (horizontal axis 0.7 to 1.7 \mu m) for photodiodes made of different semiconductor materials: Silicon (Si, response 0.7–1.1 \mu m, peak ~0.62 A/W at 0.9 \mu m), Germanium (Ge, response 1.0–1.65 \mu m, peak ~0.55 A/W at 1.4 \mu m), and InGaAs (response 0.95–1.7 \mu m, peak ~0.95 A/W at 1.55 \mu m), overlaid with dashed constant Quantum Efficiency contour lines (10%, 30%, 50%, 70%, 90%).

---

## slide 39

### Types of Photodiode
### Advantages & Drawbacks of APDs
- **Advantages**
  - Provides an increase in sensitivity of between 5 dB to 15dB over p-i-n photodiodes i.e. detection of very low level light signals.
  - Wider dynamic range as a result of their gain variation with response time and reverse bias
- **Drawbacks**
  - Fabrication difficulties due to their more complex structure and hence increased cost.
  - The random nature of the gain mechanism which gives an additional noise contribution.
  - Often high bias voltages required (50 to 400 V)
  - The variation of the gain (multiplication factor) with temperature i.e. temperature compensation is necessary to stabilize the operation of the device.

---

## slide 40

### Types of Photodiode
### APD vs p-i-n diode
### Typical Performance Characteristics of Photodetectors

| Parameter | Silicon PIN | Silicon APD | Germanium PIN | Germanium APD | InGaAs PIN | InGaAs APD |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Wavelength range (nm) | 400–1100 | [spans Silicon] | 800–1800 | [spans Germanium] | 900–1700 | [spans InGaAs] |
| Peak (nm) | 900 | 830 | 1550 | 1300 | 1300 (1550) | 1300 (1550) |
| Responsivity R (A/W) | 0.6 | 77–130 | 0.65–0.7 | 3–28 | 0.63–0.8 <br> (0.75–0.97) | [blank] |
| Quantum efficiency (%) | 65–90 | 77 | 50–55 | 55–75 | 60–70 | 60–70 |
| Gain | 1 | 150–250 | 1 | 5–40 | 1 | 10–30 |
| Excess noise factor | — | 0.3–0.5 | — | 0.95–1 | — | 0.7 |
| Bias voltage (V) | 45–100 | 220 | 6–10 | 20–35 | 5 | <30 |
| Dark current (nA) | 1–10 | 0.1–1.0 | 50–500 | 10–500 | 1–20 | 1–5 |
| Capacitance (pF) | 1.2–3 | 1.3–2 | 2–5 | 2–5 | 0.5–2 | 0.5 |
| Rise time (ns) | 0.5–1 | 0.1–2 | 0.1–0.5 | 0.5–0.8 | 0.06–0.5 | 0.1–0.5 |

---

## Done report

- **Files written:**
  - `C:/Users/bhomi/AppData/Local/Temp/claude/6e81c002d1e3bfcd/bd6f37ef-47e2-42fc-83d1-906fe62e205d/scratchpad/edc-e0/out/spd.md`
- **Sections:**
  - 40 slide sections (`## slide 1` through `## slide 40`)
  - 1 `## Done report` section
- **Counts:**
  - Slides transcribed: 40 (slides 1 to 40)
  - Tables transcribed: 1 markdown table (slide 40: Typical Performance Characteristics of Photodetectors, 10 parameter rows x 6 detector columns)
  - Equations transcribed: 8 mathematical formulas (slides 9, 10, 25, 27, 35, 36, 37)
  - Circuit / graph / band diagrams described: 31 detailed component- and label-level descriptions across the slide deck
  - Worked examples / numerical questions: 0 present in this slide set
- **What could not be read:**
  - None; all slide texts, labels, equations, and images were clear and fully legible.
- **Every `[?]`:**
  - None; no ambiguous or uncertain digits, symbols, or text encountered.
- **Flagged issues (`⚠ looks wrong`):**
  - Slide 3: LED lens diameter labeled `~ 50 mm` in structural diagram `s003-image4.jpeg` (typical indicator LED diameter is ~ 5 mm).
  - Slide 9: Slide text states "The wavelength of the light emitted is then proportional to this band-gap (Eg = hν)", whereas photon energy is directly proportional to frequency and inversely proportional to wavelength ($\lambda = hc / E_g$).
  - Slide 10: Text misspells "Reduced Plank's Constant" (missing 'c' in Planck's).
  - Slide 12: Grammatical error in original slide text: "is know as Tunnel Diode" (instead of "is known as").
  - Slide 16: Caption in original figure contains typo: "Energy-band diagram f a pn junction" (instead of "diagram of a").
  - Slides 17, 18, 19, 20, 21: Captions in original figures contain typo: "characteristics of he tunnel diode" (instead of "of the tunnel diode").
  - Slide 19: Slide title misspells "MAXIMUM TUNNELING CURENT" and text contains "diagraam".
  - Slide 20: Bullet text awkwardly phrased ("directly opposite forbidden states on the p side decreases" describing alignment opposite the forbidden bandgap).
  - Slide 23: Text states "At higher frequencies the series R and L can be ignored", whereas series lead inductance $L_s$ and series resistance $r_s$ become dominant parasitic limits at high RF/microwave frequencies.
  - Slide 33: Fourth bullet point is cut off mid-sentence: "Requires high reverse bias voltages (100 to 400 V) in order that the new carriers created by impact ionization".
