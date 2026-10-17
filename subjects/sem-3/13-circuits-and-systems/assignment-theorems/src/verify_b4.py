"""Batch 4 check: Sadiku 5e section 4.3 superposition (PP 4.3-4.5, Probs. 4.8-4.19).

Each figure is entered as a netlist and solved with all sources on (no superposition). Then every
independent source is switched on alone (others zeroed: V -> 0 V, I -> 0 A; dependent sources kept)
to produce the partial answers used in the write-up; the partials must add up to the full answer.
Run: python verify_b4.py
"""
from verify import solve

INDEP = ("V", "I")


def is_indep(e):
    return (e[0] == "V" and not e[1].startswith(("am", "_"))) or e[0] == "I"


def zero(e):
    if e[0] == "V":
        return e[:4] + (0,)
    return e[:3] + (0,)


def run(name, n, elems, measure, ref=None):
    V, I = solve(n, elems)
    full = measure(V, I)
    parts = []
    for k, e in enumerate(elems):
        if not is_indep(e):
            continue
        alone = [x if (x is e or not is_indep(x)) else zero(x) for x in elems]
        Va, Ia = solve(n, alone)
        parts.append((e[1] if e[0] == "V" else f"I{k}", measure(Va, Ia)))
    s = sum(p for _, p in parts)
    ps = "  ".join(f"{lab}: {p.real:+.4f}" for lab, p in parts)
    print(f"{name:7s} full {full.real:+.5f}   sum of parts {s.real:+.5f}   [{ps}]" + (f"   book: {ref}" if ref else ""))
    return full


run("PP4.3", 3, [("Z", 1, 0, 2), ("Z", 1, 2, 3), ("I", 0, 2, 5), ("Z", 2, 3, 5), ("V", "s12", 3, 0, 12)],
    lambda V, I: V[1], "7.4 V")
run("PP4.4", 2, [("V", "s25", 1, 0, 25), ("Z", 1, 2, 20), ("I", 0, 2, 5), ("Z", 2, 0, 4), ("G", 0, 2, 2, 0, 0.1)],
    lambda V, I: V[2], "31.25 V")
run("PP4.5", 4, [("V", "s8", 1, 0, 8), ("Z", 1, 2, 6), ("Z", 2, 3, 2), ("I", 2, 3, 2), ("Z", 3, 4, 8),
                 ("V", "s6", 4, 0, 6)], lambda V, I: (V[3] - V[4]) / 8, "375 mA")
run("4.8", 4, [("Z", 1, 0, 5), ("Z", 1, 2, 4), ("Z", 2, 3, 3), ("V", "s9", 3, 0, 9), ("Z", 2, 4, 1),
               ("V", "s3", 4, 0, 3)], lambda V, I: V[2], "even (54/13 = 4.1538)")
run("4.11io", 4, [("I", 0, 1, 6), ("Z", 1, 0, 40), ("V", "am", 1, 4, 0), ("Z", 4, 2, 10), ("F", 0, 2, "am", 4),
                  ("Z", 2, 3, 20), ("V", "s30", 0, 3, 30)], lambda V, I: I["am"], "1.799 A")
run("4.11vo", 4, [("I", 0, 1, 6), ("Z", 1, 0, 40), ("V", "am", 1, 4, 0), ("Z", 4, 2, 10), ("F", 0, 2, "am", 4),
                  ("Z", 2, 3, 20), ("V", "s30", 0, 3, 30)], lambda V, I: V[1] - V[2], "17.99 V")
run("4.12", 4, [("V", "s12", 1, 0, 12), ("Z", 1, 2, 6), ("Z", 2, 0, 3), ("Z", 2, 3, 5), ("Z", 3, 0, 12),
                ("Z", 3, 4, 4), ("V", "s19", 4, 0, 19), ("I", 3, 2, 2)], lambda V, I: V[2] - V[3], "even")
run("4.13", 3, [("I", 0, 1, 2), ("Z", 1, 0, 10), ("Z", 1, 2, 8), ("V", "s12", 2, 3, 12), ("Z", 3, 0, 5),
                ("I", 1, 3, 4)], lambda V, I: V[3], "8.696 V")
run("4.14", 3, [("V", "s20", 1, 0, 20), ("Z", 1, 3, 6), ("I", 3, 1, 2), ("Z", 1, 2, 4), ("Z", 2, 3, 2),
                ("I", 0, 2, 1), ("Z", 3, 0, 3)], lambda V, I: V[3], "even")
run("4.15", 4, [("V", "s20", 1, 2, 20), ("Z", 2, 0, 2), ("Z", 1, 3, 1), ("I", 1, 3, 2), ("Z", 3, 0, 3),
                ("Z", 1, 4, 4), ("V", "s16", 0, 4, 16)], lambda V, I: V[3] / 3, "1.875 A")
run("4.16", 5, [("V", "s12", 1, 0, 12), ("V", "am", 1, 5, 0), ("Z", 5, 2, 4), ("Z", 2, 0, 10), ("Z", 2, 3, 3),
                ("Z", 3, 4, 2), ("Z", 4, 0, 5), ("I", 0, 4, 2), ("I", 3, 2, 4)], lambda V, I: I["am"], "even")
run("4.17", 4, [("V", "s90", 1, 0, 90), ("Z", 1, 2, 30), ("Z", 2, 0, 60), ("Z", 2, 3, 10), ("I", 0, 3, 6),
                ("Z", 3, 0, 30), ("Z", 3, 4, 20), ("V", "s40", 4, 0, 40)], lambda V, I: V[2] - V[3], "-8.571 V")
run("4.18", 3, [("V", "s10", 1, 0, 10), ("Z", 1, 2, 2), ("I", 0, 2, 2), ("Z", 2, 3, 1), ("G", 2, 3, 3, 0, 0.5),
                ("Z", 3, 0, 4)], lambda V, I: V[3], "even")
run("4.19", 2, [("Z", 1, 0, 2), ("E", "d", 2, 0, 1, 0, 2), ("I", 0, 1, 6), ("I", 2, 1, 4), ("Z", 1, 2, 8)],
    lambda V, I: V[1] - V[2], "-26.67 V")
# 4.10 sample design: V = 12 V, R = 4 Ω, I = 3 A, k = 2 ; nodes 1 = V+, 2 = after R, 3 = a
run("4.10", 3, [("V", "s12", 1, 0, 12), ("Z", 1, 2, 4), ("E", "k", 2, 3, 3, 0, 2), ("I", 0, 3, 3)],
    lambda V, I: V[3], "design (formula (V + RI)/(1 + k) = 8 V)")
