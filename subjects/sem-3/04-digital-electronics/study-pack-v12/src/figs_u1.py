"""Unit 1 figures (files 01-03, v1.3, S1 2026-11-17).

The K-map, two-level circuit and gate drawers live in the v1 module figs1.py (SVG via schemdraw and
kfig); tools/figlib.py has no logic primitives (sprints.md assumption 5). This module only calls
them with the functions files 01-03 teach. Every function drawn here is checked in verify.py u1.
"""
import figs1
from figs1 import ACC, _d, _inputs, _sd, _wire, elm, lg

km, km5, two = figs1.km, figs1.km5, figs1.two_level

FIGS = {
    # 01 Boolean algebra: running example F(x,y,z) before and after simplification
    "u1_run_before": lambda: two([["x'", "y", "z"], ["x'", "y", "z'"], ["x", "z"]], width=70),
    "u1_run_after": lambda: two([["x'", "y"], ["x", "z"]], width=70),
    # 02 K-maps
    "u1_km2": lambda: km("AB", [2, 3], terms=["A"], cs=48),
    "u1_km3_idx": lambda: km("xyz", [], cs=48),
    "u1_km3_run": lambda: km("xyz", [2, 3, 5, 7], terms=["x'y", "xz"], cs=48),
    "u1_km3_wrong": lambda: km("abc", [2, 3, 6, 7], terms=["a'b", "ab"], cs=44),
    "u1_km3_right": lambda: km("abc", [2, 3, 6, 7], terms=["b"], cs=44),
    "u1_km3_pi": lambda: km("abc", [2, 3, 4, 5, 6], terms=["a'b", "ab'", "bc'", "ac'"], cs=48),
    "u1_km4_idx": lambda: km("abcd", [], cs=44),
    "u1_km4_nodc": lambda: km("abcd", [0, 4, 5, 7, 8, 9, 15], terms=["b'c'd'", "a'bc'", "bcd", "ab'c'"], cs=44),
    "u1_km4_dc": lambda: km("abcd", [0, 4, 5, 7, 8, 9, 15], [1, 3, 6, 14], terms=["b'c'", "bc", "a'c'"], cs=44),
    "u1_mte4_andor": lambda: two([["b'", "c'"], ["b", "c"], ["a'", "c'"]], width=60),
    "u1_km4_pos": lambda: km("WXYZ", [0, 1, 2, 5, 8, 9, 10], terms=["(W' + X')", "(Y' + Z')", "(X' + Z)"], pos=True, cs=44),
    "u1_km4_sop63": lambda: km("WXYZ", [0, 1, 2, 5, 8, 9, 10], terms=["X'Y'", "X'Z'", "W'Y'Z"], cs=44),
    "u1_km5_ce": lambda: km5("abcde", [5, 7, 13, 15, 21, 23, 29, 31], [], ["ce"]),
    "u1_km5_ps1q1": lambda: km5("vwxyz", [0, 2, 5, 8, 10, 13, 15, 17, 19, 21, 26, 28, 29, 30, 31],
                                [7, 12, 14, 23, 24], ["xz", "wz'", "v'x'z'", "vw'z"]),
    "u1_km4_ps1q4": lambda: km("ABCD", [3, 6, 7, 11, 12, 13, 14, 15], terms=["AB", "BC", "CD"], cs=44),
    "u1_ps1q4_andor": lambda: two([["A", "B"], ["B", "C"], ["C", "D"]], width=60),
    # 03 NAND/NOR
    "u1_nand_141": lambda: two([["X'", "Y'", "Z'"], ["X", "Y", "Z'"]], g1="Nand", g2="Nand", width=70),
    "u1_nor_145": lambda: two([["X'", "Y"], ["X", "Y'"]], g1="Nor", g2="Nor", single=["Z"], width=70),
    "u1_km4_ps1q2": lambda: km("wxyz", [0, 1, 3, 5, 7, 10, 11], [2, 6, 13], terms=["w'x'", "w'z", "x'y"], cs=44),
    "u1_nand_ps1q2": lambda: two([["w'", "x'"], ["w'", "z"], ["x'", "y"]], g1="Nand", g2="Nand", width=70),
    "u1_nand_ps1q1": lambda: two([["v'", "x'", "z'"], ["x", "z"], ["w", "z'"], ["v", "w'", "z"]],
                                 g1="Nand", g2="Nand", width=75),
    "u1_nand_mte4": lambda: two([["b'", "c'"], ["b", "c"], ["a'", "c'"]], g1="Nand", g2="Nand", width=60),
}


def universal_nor():
    """NOT, OR, AND built from NOR gates only (mirror of figs1.universal_nand)."""
    d = _d(fs=11)
    g = d.add(lg.Nor().right().at((0, 0)).anchor("out"))
    d += elm.Line().at(g.in1).left(0.4); d += elm.Line().down(g.in1[1] - g.in2[1]); d += elm.Line().right(0.4)
    d += elm.Line().at((g.in1[0] - 0.4, 0)).left(0.6).label("X", loc="left")
    d += elm.Line().at(g.out).right(0.5).label("X'", loc="right")
    a = d.add(lg.Nor().right().at((5.2, 0)).anchor("out")); _inputs(d, a, ["X", "Y"], 0.5)
    b = d.add(lg.Nor().right().at((7.6, 0)).anchor("out"))
    d += elm.Line().endpoints(a.out, (a.out[0] + 0.45, 0))
    d += elm.Line().endpoints((a.out[0] + 0.45, b.in1[1]), (a.out[0] + 0.45, b.in2[1]))
    d += elm.Line().endpoints((a.out[0] + 0.45, b.in1[1]), b.in1); d += elm.Line().endpoints((a.out[0] + 0.45, b.in2[1]), b.in2)
    d += elm.Line().at(b.out).right(0.5).label("X + Y", loc="right")
    x0 = 12.6
    for y, lab in ((0.9, "X"), (-0.9, "Y")):
        n = d.add(lg.Nor().right().at((x0, y)).anchor("out"))
        d += elm.Line().at(n.in1).left(0.4); d += elm.Line().down(n.in1[1] - n.in2[1]); d += elm.Line().right(0.4)
        d += elm.Line().at((n.in1[0] - 0.4, y)).left(0.6).label(lab, loc="left")
    o = d.add(lg.Nor().right().at((x0 + 2.6, 0)).anchor("out"))
    _wire(d, (x0, 0.9), o.in1, x0 + 0.4); _wire(d, (x0, -0.9), o.in2, x0 + 0.4)
    d += elm.Line().at(o.out).right(0.5).label("X·Y", loc="right")
    for x, t in ((-1.2, "NOT"), (5.4, "OR"), (12.6, "AND")):
        d += elm.Label().at((x, 2.0)).label(t, fontsize=11, color=ACC)
    return _sd(d, 172)


FIGS["u1_universal_nor"] = universal_nor
