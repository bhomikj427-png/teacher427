#!/usr/bin/env python3
"""Reproducible source for the Verilog orientation lesson.
Per learner-preferences.md §3 (2026-07-03 rule): NOT one big map -- deliver a clean learning-FLOW
map first (the ordered path + current position), then several small CONNECTED sub-maps, one per
area, digestible. Distant areas stay single nodes on the flow map until we reach them.
Primitive 2 -> Mermaid. Re-render anytime: `python <thisfile>`."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
from render_lesson import save_lesson

# --- Map 1: the FLOW. The ordered journey + where the learner stands. The single orientation map.
FLOW = """
flowchart TD
    S0["Stage 0 - The reframe<br/>hardware, not software; all concurrent"]
    S1["Stage 1 - Building blocks<br/>modules, ports, wire/reg, 4-state, vectors"]
    S2["Stage 2 - Describing a circuit<br/>structural / dataflow / behavioral"]
    S3["Stage 3 - Combinational logic<br/>assign, always@*, latch traps"]
    S4["Stage 4 - Sequential logic<br/>flip-flops, clock, reset"]
    S5["Stage 5 - The core mechanism<br/>blocking vs nonblocking + event queue"]
    S6["Stage 6 - RTL model + FSMs<br/>registers &amp; clouds per clock; Moore/Mealy"]
    S7["Stage 7 - Synthesis discipline<br/>synth subset, sim/synth mismatch"]
    S8["Stage 8 - Verification<br/>testbenches, self-checking, waveforms"]
    S9["Stage 9 - Scaling + pro horizon<br/>parameters/generate; timing; SystemVerilog"]
    S0 --> S1 --> S2 --> S3 --> S4 --> S5 --> S6 --> S7 --> S8 --> S9
    classDef here fill:#2d5a2d,stroke:#8fdd8f,color:#fff,stroke-width:2px;
    classDef next fill:#5a4a1e,stroke:#e0c060,color:#fff,stroke-width:2px;
    class S3 here;
    class S4 next;
"""

# --- Sub-maps: one per NEAR area. Small and connected to the flow by stage number.
SUB_S0 = """
mindmap
  root((Stage 0<br/>The reframe))
    Hardware, not a program
      code maps to gates, wires, registers
      it does not run on a CPU, line by line
    Concurrency is the default
      every assign and always block runs in parallel
      statement order does not set execution order
    Why beginners trip here
      C-like syntax suggests sequential execution
      that wrong intuition causes most early bugs
"""

SUB_S1 = """
mindmap
  root((Stage 1<br/>Building blocks))
    module
      a hardware block with input and output ports
      instantiate and wire modules into a hierarchy
    signals and values
      wire vs reg is assignment context, not hardware
      four-state values - 0, 1, x, z
      vectors and buses carry many bits at once
"""

SUB_S34 = """
mindmap
  root((Stages 3 and 4<br/>Comb then Seq))
    Combinational - YOU ARE HERE
      output depends only on the current inputs
      written with assign or always at star
      a missing branch makes an accidental latch
    Sequential - NEXT
      output depends on stored state
      flip-flop stores a bit, updates on a clock edge
      clock advances state; reset makes it start known
"""

spec = {
    "title": "Verilog - The Learning Path",
    "subject": "verilog",
    "unit": "00-orientation",
    "intro": (
        "**Verilog is a Hardware Description Language (HDL)** - a formal notation for describing "
        "digital hardware (gates, wires, registers), standardized as IEEE 1364. It is **not** a "
        "software language; the C-like syntax is a trap.\n\n"
        "Read the **flow map first** (Figure 1): it is the ordered path we take and where you stand "
        "now. The smaller sub-maps zoom into the first few stops. Later stages stay single nodes on "
        "the flow map until we reach them."
    ),
    "sections": [
        {
            "heading": "The path (start here)",
            "blocks": [
                {"type": "map", "mermaid": FLOW,
                 "caption": "The route, in order. Green = where you are (Stage 3). "
                            "Gold = what's next (Stage 4). Follow the arrows top to bottom."},
            ],
        },
        {
            "heading": "Zoom: the first stops",
            "blocks": [
                {"type": "map", "mermaid": SUB_S0,
                 "caption": "Stage 0 detail - the one idea that reorganizes everything else."},
                {"type": "map", "mermaid": SUB_S1,
                 "caption": "Stage 1 detail - the vocabulary you build designs out of."},
                {"type": "map", "mermaid": SUB_S34,
                 "caption": "Stages 3-4 detail - your current ground, and the next climb."},
            ],
        },
    ],
}

if __name__ == "__main__":
    save_lesson(spec)
