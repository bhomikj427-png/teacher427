"""Session 2 rework: concept kinds + L0 priming for Digital Electronics.

Stand-in for two automatic steps of v2 proper (SITE-V2-DRAFT §7), hand-written here from the KB and the graph so the
look can be judged on real content:

* KIND: what sort of thing each concept is. It tells the learner *how to study it* (the verb), and drives the "kind"
  colour mode. Five kinds, chosen by the engine (learner: "3 kinds or even more if u feel its going to be usefull"):
    logic    - can be worked out from what came before           -> work it out
    memorise - a fact, value, table or definition to hold         -> remember it
    method   - a recipe you carry out step by step                 -> do it
    circuit  - a hardware block to recognise and draw              -> draw it
    trap     - where marks are lost                                 -> avoid it
  Evidence for splitting study moves by material type: route by goal (procedure -> worked example first, concept ->
  attempt first; research/03 §5), retrieval practice for what must be held (research/02 §1).

* PRIME: what an L0 stop shows. A heading, a guess question, one sentence, and at most three key terms, each with a
  short gloss. This is the pretraining principle (names + characteristics of the key components before the lesson;
  Mayer) plus pretesting (research/02 §5). Glosses are drawn from the concept gists in de_graph.py.
"""

KINDS = [
    {"id": "logic", "label": "Logic", "verb": "work it out"},
    {"id": "memorise", "label": "Memorise", "verb": "remember it"},
    {"id": "method", "label": "Method", "verb": "do it"},
    {"id": "circuit", "label": "Circuit", "verb": "draw it"},
    {"id": "trap", "label": "Trap", "verb": "avoid it"},
]

_K = {
    "logic": """binary demorgan minterms sop-pos universal why-min kmap-layout kmap-adj group-size pi-epi cla
                memory-line hazards edge metastab skew fsm moore-mealy async-fsm state-assign memory-org rom""",
    "memorise": """bcd excess3 bool-laws consensus alu-74181 tpd ff-types char-eq async-in excitation setup-hold
                   ff-count asm yardsticks pdp ecl sram-dram""",
    "method": """gray twos-comp truth-table bubble nand-real nor-real group-rules kmap-pos five-var dont-cares qm
                 comb-pipeline code-conv mux-fn mux-cascade mux-under dec-fn dec-expand seven-seg waveform ff-conv
                 fmax hold-check mod-n-clear sync-counter self-start pulse-train state-diag state-red fsm-pipeline
                 seq-det noise-margin fanout interfacing pld-impl""",
    "circuit": """gates xor parity half-adder half-sub full-adder rca fa-from-ha full-sub add-sub bcd-adder mux demux
                  barrel decoder encoder prio-enc cmp-1 cmp-4 alu mux-display sr-latch gated-latch d-latch d-ff
                  master-slave shift-reg ring universal-sr johnson serial-adder ripple-counter clock-gen prbs
                  cmos-inv cmos-gates ttl-nand totem tristate pld""",
    "trap": "kmap-traps ca-cc race",
}
KIND = {cid: k for k, ids in _K.items() for cid in ids.split()}


def T(term, gloss):
    return {"t": term, "g": gloss}


# chapter priming, keyed by the auto-cut chapter id (autocut.py is deterministic on this graph)
CHAPTERS = {
    "ch1": dict(title="Bits, codes & gates",
                q="How can 0s and 1s stand for numbers, and what can you do with them?",
                line="Everything digital is patterns of bits, and three gates are enough to act on them.",
                terms=[T("Binary", "place values are powers of 2"), T("Gray code", "neighbours differ in one bit"),
                       T("Truth table", "every input, every output")]),
    "ch2": dict(title="Boolean algebra",
                q="Can two different-looking circuits be the same circuit?",
                line="Algebra on 0 and 1 rewrites a circuit without changing what it does.",
                terms=[T("De Morgan", "a complement swaps AND ↔ OR"), T("Minterm", "an AND term true on one row"),
                       T("NAND / NOR", "one gate type builds everything")]),
    "ch3": dict(title="K-maps",
                q="How do you find the smallest circuit for a truth table, by eye?",
                line="Fold the truth table into a grid where neighbours differ in one bit, then circle groups.",
                terms=[T("K-map", "a truth table as a Gray-ordered grid"), T("Group", "a power-of-2 block of 1s"),
                       T("Wrap-around", "the map's edges touch")]),
    "ch4": dict(title="Minimise, then design",
                q="Which groups are forced, and what do you do with a row you don't care about?",
                line="Take the forced groups, let don't-cares grow the rest, and design any block in three steps.",
                terms=[T("Essential implicant", "a group nothing else covers"), T("Don't-care (X)", "free to be 0 or 1"),
                       T("Capture → minimise → realise", "the design recipe")]),
    "ch5": dict(title="Adders & subtractors",
                q="How does a circuit add two numbers, and why does it slow down with more bits?",
                line="Adders are built one bit at a time, and the carry decides how fast they are.",
                terms=[T("Full adder", "adds A, B and a carry-in"), T("Ripple carry", "each bit waits for the last"),
                       T("Carry look-ahead", "all carries at once")]),
    "ch6": dict(title="Multiplexers",
                q="How do a few select wires pick one signal out of many?",
                line="A MUX is a switch steered by bits, and it can build any function.",
                terms=[T("Select lines", "choose which input passes"), T("DEMUX", "one input out to many"),
                       T("Barrel shifter", "any shift in one step")]),
    "ch7": dict(title="Decoders & encoders",
                q="How does a 3-bit number light exactly one of 8 wires, and back again?",
                line="A decoder puts every minterm on its own wire. An encoder does the reverse.",
                terms=[T("Decoder", "n bits in, one of 2ⁿ out"), T("Priority encoder", "the highest input wins"),
                       T("Expansion", "small decoders make big ones")]),
    "ch8": dict(title="Comparators, ALU & displays",
                q="How does a chip know that A > B, and how does a digit light up?",
                line="Real blocks made from earlier parts: compare, compute, show the result.",
                terms=[T("Magnitude comparator", "first differing bit decides"), T("ALU", "the opcode picks the operation"),
                       T("7-segment", "one K-map per segment")]),
    "ch9": dict(title="Latches: circuits that remember",
                q="How can a circuit keep a bit after its input has gone?",
                line="Loop an output back to an input and the circuit holds its state. A clock edge decides when it changes.",
                terms=[T("Feedback", "the output loops back in"), T("SR latch", "set, reset, hold"),
                       T("Edge-triggered", "changes only at the clock edge")]),
    "ch10": dict(title="Flip-flops",
                 q="Four kinds of flip-flop store the same single bit. Why four?",
                 line="SR, D, JK and T differ only in how their inputs command the stored bit.",
                 terms=[T("Characteristic equation", "next state from the inputs"),
                        T("Excitation table", "inputs needed for a change"), T("Race-around", "a JK toggling out of control")]),
    "ch11": dict(title="Timing",
                 q="How fast can a clocked circuit run before it breaks?",
                 line="Every path must settle before the next edge, and inputs must hold still around it.",
                 terms=[T("Setup / hold", "stay still before and after the edge"), T("f_max", "set by the slowest path"),
                        T("Metastability", "stuck between 0 and 1")]),
    "ch12": dict(title="Shift registers",
                 q="What happens when flip-flops are chained on one clock?",
                 line="Bits march one place per clock. Feed them back and you get counters.",
                 terms=[T("SISO · PIPO", "serial or parallel, in and out"), T("Ring counter", "a single 1 circulates"),
                        T("Johnson counter", "2n states from n flip-flops")]),
    "ch13": dict(title="Counters",
                 q="How do you build a circuit that counts 0 to 9 and starts again?",
                 line="Counters either ripple (simple, slow) or are designed as synchronous circuits from an excitation table.",
                 terms=[T("Ripple counter", "each flip-flop clocks the next"), T("Mod-N", "counts N states, then repeats"),
                        T("Self-starting", "stray states rejoin the cycle")]),
    "ch14": dict(title="State machines",
                 q="What do a counter, a vending machine and a traffic light have in common?",
                 line="Every sequential machine is a state register, next-state logic and output logic.",
                 terms=[T("FSM", "states, transitions, outputs"), T("Moore / Mealy", "output from state, or state + input"),
                        T("PRBS", "a shift register that looks random")]),
    "ch15": dict(title="Designing a state machine",
                 q="Given a word problem like “detect 1011”, how do you get to gates?",
                 line="Diagram, table, reduce, assign, excite, K-map: the whole design pipeline.",
                 terms=[T("State table", "present state → next state"), T("State reduction", "merge states that act alike"),
                        T("Sequence detector", "the classic exam FSM")]),
    "ch16": dict(title="Logic families",
                 q="What voltage really counts as a 1, and why can't every chip talk to every other?",
                 line="Gates are transistors. Their voltages, speed and power decide what can connect to what.",
                 terms=[T("Noise margin", "safety gap between levels"), T("Fan-out", "inputs one output can drive"),
                        T("CMOS · TTL", "the two main families")]),
    "ch17": dict(title="Memory & programmable logic",
                 q="How does a chip hold a million bits, or become any circuit you like?",
                 line="Memory is a decoder plus storage cells. Programmable logic is AND and OR planes you fill in.",
                 terms=[T("ROM", "a truth table in silicon"), T("SRAM · DRAM", "latch cell vs capacitor cell"),
                        T("PLA · PAL", "programmable AND–OR planes")]),
}

# the syllabus units, for the unit-first L0 variant (00-map.md: U1 → U5, number systems folded in before U1)
UNITS = [
    dict(id="u0", n="U0", title="Bits & gates", chapters=["ch1"],
         q="What are the raw materials of every digital circuit?",
         line="Number codes and the three gates. Assumed knowledge, folded into the start of unit 1.",
         terms=[T("Binary", "place values are powers of 2"), T("Gray code", "neighbours differ in one bit"),
                T("Truth table", "every input, every output")]),
    dict(id="u1", n="U1", title="Combinational logic", chapters=["ch2", "ch3", "ch4", "ch5"],
         q="How do you get from a word problem to the smallest circuit?",
         line="Boolean algebra and K-maps shrink a function. Adders are the first real design.",
         terms=[T("Boolean algebra", "rewrite without changing"), T("K-map", "minimise by circling groups"),
                T("Full adder", "one bit of addition")]),
    dict(id="u2", n="U2", title="MSI building blocks", chapters=["ch6", "ch7", "ch8"],
         q="What ready-made blocks do real designs reach for?",
         line="MSI (medium-scale integration) chips package logic as parts: MUXes, decoders, comparators, ALUs.",
         terms=[T("MUX", "bits choose the input"), T("Decoder", "one wire per minterm"), T("ALU", "the opcode picks the job")]),
    dict(id="u3", n="U3", title="Sequential logic", chapters=["ch9", "ch10", "ch11", "ch12", "ch13"],
         q="How does a circuit remember, and how does it count?",
         line="Feedback plus a clock gives memory: latches, flip-flops, registers, counters.",
         terms=[T("Flip-flop", "one clocked bit of memory"), T("Setup / hold", "the timing rules"),
                T("Counter", "flip-flops stepping through states")]),
    dict(id="u4", n="U4", title="State machines", chapters=["ch14", "ch15"],
         q="How do you design a circuit that behaves in steps?",
         line="State machines fuse everything before: flip-flops hold the state, K-maps give the logic.",
         terms=[T("FSM", "states, transitions, outputs"), T("Moore / Mealy", "two ways to make outputs"),
                T("State table", "the design's starting point")]),
    dict(id="u5", n="U5", title="Logic families & memory", chapters=["ch16", "ch17"],
         q="What is under the logic, down in the silicon?",
         line="Voltages, transistors and power, and how memories and programmable chips are built.",
         terms=[T("Noise margin", "safety gap between levels"), T("CMOS", "pMOS up, nMOS down"),
                T("ROM · RAM", "stored words, addressed")]),
]
