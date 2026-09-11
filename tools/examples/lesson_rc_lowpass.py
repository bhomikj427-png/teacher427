#!/usr/bin/env python3
"""
Acceptance Test A — STRUCTURAL-REGISTRY path (subject: ece).

Concept: the RC low-pass filter. Exercises the primitive-6 registry (schemdraw via the shipped
"ece" entry) plus the universal primitives, end to end:
  concept map (2) -> schemdraw schematic (6, registry) -> matplotlib Bode (4)
  -> MathJax transfer function (1) -> one CHECK.

This is the *lesson surface* only (the browser tab). In a real session the dialogue + the CHECK
exchange happen in the terminal in plain ASCII; this file is what the terminal points at.

Run:  python tools/examples/lesson_rc_lowpass.py        # writes rc-lowpass.html beside this file
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # tools/ on path
from render_lesson import render


# --- primitive 4 data: compute the Bode magnitude in Python, pass arrays in (handlers stay pure) ---
R, C = 1_000.0, 1e-6                       # 1 kohm, 1 uF  ->  fc = 1/(2*pi*R*C) ~ 159 Hz
fc = 1.0 / (2 * np.pi * R * C)
f = np.logspace(0, 5, 400)                 # 1 Hz .. 100 kHz
w = 2 * np.pi * f
mag_db = 20 * np.log10(1.0 / np.sqrt(1.0 + (w * R * C) ** 2))


SPEC = {
    "title": "The RC Low-Pass Filter",
    "subject": "ece",
    "intro": "A resistor in series, a capacitor to ground, output across the capacitor. "
             "The capacitor shorts high frequencies to ground, so highs are attenuated and "
             "lows pass — a **first-order low-pass** with a single corner at `f_c`.",
    "sections": [
        # -- primitive 2: concept-map-first (non-negotiable, opens every concept) --
        {"heading": "The shape of it (open here)", "blocks": [
            {"type": "map", "caption": "How the pieces relate",
             "mermaid": (
                "graph LR\n"
                "  Vin[Input Vin] --> R[Resistor R]\n"
                "  R --> N((output node))\n"
                "  N --> C[Capacitor C to ground]\n"
                "  N --> Vout[Output Vout]\n"
                "  C -. shorts highs .-> GND[Ground]\n"
                "  N -- 'fc = 1 / 2*pi*R*C' --> FC{{Corner frequency}}"
             )},
        ]},
        # -- primitive 6: structural diagram through the REGISTRY (ece -> schemdraw) --
        {"heading": "The circuit", "blocks": [
            {"type": "structural", "caption": "RC low-pass: R in series, C shunt to ground, "
                                              "Vout across C",
             "figure": {"kind": "structural", "subject": "ece", "elements": [
                 {"e": "Ground"},
                 {"e": "SourceV", "d": "up", "label": "Vin"},
                 {"e": "Line", "d": "right"},
                 {"e": "Resistor", "d": "right", "label": "R"},
                 {"e": "Dot", "push": True},
                 {"e": "Capacitor", "d": "down", "label": "C"},
                 {"e": "Ground"},
                 {"pop": True},
                 {"e": "Line", "d": "right"},
                 {"e": "Dot", "label": "Vout"},
             ]},
             # if the ece renderer were ever absent, degrade to the concept map instead of breaking:
             "fallback": {"type": "map", "mermaid": "graph LR\n Vin-->R-->Vout\n R-->C-->GND[Ground]"}},
        ]},
        # -- primitive 4: matplotlib quantitative plot -> inline SVG --
        {"heading": "What it does to a signal", "blocks": [
            {"type": "plot", "caption": "Magnitude response (Bode). Flat below the corner, "
                                        "rolls off at -20 dB/decade above it.",
             "figure": {"kind": "matplotlib",
                        "series": [{"x": f.tolist(), "y": mag_db.tolist(), "label": "|H(jw)|"}],
                        "xlabel": "frequency  f  (Hz)", "ylabel": "gain  (dB)",
                        "xscale": "log",
                        "vlines": [{"x": fc, "label": "fc ~ 159 Hz"}],
                        "hlines": [{"y": -3.0, "label": "-3 dB"}]}},
        ]},
        # -- primitive 1: MathJax math --
        {"heading": "Why (the transfer function)", "blocks": [
            {"type": "math",
             "tex": r"H(s)=\frac{1}{1+sRC}\qquad |H(j\omega)|=\frac{1}{\sqrt{1+(\omega RC)^2}}"
                    r"\qquad f_c=\frac{1}{2\pi RC}"},
            {"type": "prose", "md": "At `w = 1/RC` the denominator is `sqrt(2)`, so the magnitude is "
                                    "`1/sqrt(2)` — that is the **-3 dB** point, and the phase is **-45°**."},
        ]},
        # -- the CHECK lands here carrying the figure; the retrieval still happens in the terminal --
        {"heading": "Check", "blocks": [
            {"type": "check",
             "q": "At the cutoff frequency `f_c`: (a) by how many **dB** is the output down, and "
                  "(b) what is the **phase shift** from input to output?",
             "answer": "(a) **-3 dB** (output amplitude is `1/sqrt(2)` ~ 0.707 of input).\n\n"
                       "(b) **-45°** (output lags input by 45 degrees)."},
        ]},
    ],
}


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rc-lowpass.html")
    render(SPEC, out, open_browser="--open" in sys.argv)
