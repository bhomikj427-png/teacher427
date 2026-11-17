"""Unit 3 schematics (latches): sequential-circuit block, two-inverter ring, NAND latch, gated SR / D latch.

Reuses the helpers of figs1 (schemdraw drawing helpers and matplotlib block-diagram helpers).
"""
import figs1
from figs1 import ACC, G2, INK, MUTED, TINT, _arrow, _box, _canvas, _d, _line, _nat, _sd, elm, lg


def u3_seq_block():
    fig, ax = _canvas(7.4, 2.63, (-1.6, 12.2), (-2.0, 2.9))
    _box(ax, 1.5, 0, 3.2, 2.0, "Combinational\nlogic", fc=TINT, ec=ACC, fs=9.5)
    _box(ax, 7.2, 0, 3.2, 2.0, "Memory\nelements", fc="#eaf6ef", ec=G2, fs=9.5)
    _arrow(ax, (0.2, 1.0), (1.5, 1.0))
    ax.text(0.1, 1.0, "inputs", ha="right", va="center", fontsize=9)
    _arrow(ax, (3.1, 2.0), (3.1, 2.6))
    ax.text(3.3, 2.3, "outputs", ha="left", va="center", fontsize=9)
    _arrow(ax, (4.7, 1.0), (7.2, 1.0))
    ax.text(5.95, 1.15, "next state", ha="center", va="bottom", fontsize=9)
    _arrow(ax, (8.8, 2.6), (8.8, 2.0), color=MUTED)
    ax.text(9.0, 2.3, "CLK", ha="left", va="center", fontsize=8.5, color=MUTED)
    _line(ax, [10.4, 11.4, 11.4, 3.1], [1.0, 1.0, -1.2, -1.2])
    _arrow(ax, (3.1, -1.2), (3.1, 0.0))
    ax.text(7.25, -1.38, "present state (feedback)", ha="center", va="top", fontsize=9)
    return _nat(fig)


def u3_two_inv():
    d = _d()
    a = d.add(lg.Not().right().at((0, 1.2)))
    b = d.add(lg.Not().left().at((a.end[0], -1.2)))
    xr = a.out[0] + 1.0
    xl = a.start[0] - 1.0
    d += elm.Line().endpoints(a.out, (xr, a.out[1])).label("Q", loc="top")
    d += elm.Line().endpoints((xr, a.out[1]), (xr, b.start[1]))
    d += elm.Line().endpoints((xr, b.start[1]), b.start)
    d += elm.Line().endpoints(b.out, (xl, b.out[1])).label("Q'", loc="bottom")
    d += elm.Line().endpoints((xl, b.out[1]), (xl, a.start[1]))
    d += elm.Line().endpoints((xl, a.start[1]), a.start)
    return _sd(d, 60)


def _latch(d, ox, top, bot, labels=True):
    """Cross-coupled NAND pair, outputs at x = ox. Returns (g3, g4)."""
    g1 = d.add(lg.Nand().right().at((ox, top)).anchor("out"))
    g2 = d.add(lg.Nand().right().at((ox, bot)).anchor("out"))
    d += elm.Line().endpoints(g1.out, (ox + 1.6, top)).label("Q", loc="right")
    d += elm.Line().endpoints(g2.out, (ox + 1.6, bot)).label("Q'", loc="right")
    vx = min(g1.in1[0], g2.in1[0]) - 0.6
    for (x0, y0), pin in (((ox + 0.7, top), g2.in1), ((ox + 0.7, bot), g1.in2)):
        s = 1 if y0 > 0 else -1
        d += lg.Dot().at((x0, y0))
        ym = s * 0.55
        for p, q in (((x0, y0), (x0, ym)), ((x0, ym), (vx, -ym * 0.55)), ((vx, -ym * 0.55), (vx, pin[1])),
                     ((vx, pin[1]), pin)):
            d += elm.Line().endpoints(p, q)
    return g1, g2


def u3_nand_latch():
    d = _d()
    g1, g2 = _latch(d, 3, 1.3, -1.3)
    d += elm.Line().endpoints((0.2, g1.in1[1]), g1.in1).label("S'", loc="left")
    d += elm.Line().endpoints((0.2, g2.in2[1]), g2.in2).label("R'", loc="left")
    return _sd(d, 70)


def _gated(is_d):
    d = _d()
    ox = 8.2 if not is_d else 9.0
    g3, g4 = _latch(d, ox, 1.3, -1.3)
    # drive NANDs: outputs land on the latch's free inputs
    g1 = d.add(lg.Nand().right().at((ox - 3.0, g3.in1[1])).anchor("out"))
    g2 = d.add(lg.Nand().right().at((ox - 3.0, g4.in2[1])).anchor("out"))
    d += elm.Line().endpoints(g1.out, g3.in1).label("S'", loc="top")
    d += elm.Line().endpoints(g2.out, g4.in2).label("R'", loc="top")
    xb = g1.in1[0] - 0.6          # EN bus
    d += elm.Line().endpoints((xb, g1.in2[1]), g1.in2)
    d += elm.Line().endpoints((xb, g2.in1[1]), g2.in1)
    d += elm.Line().endpoints((xb, g1.in2[1]), (xb, g2.in1[1]))
    ym = (g1.in2[1] + g2.in1[1]) / 2
    d += lg.Dot().at((xb, ym))
    d += elm.Line().endpoints((xb - 0.7, ym), (xb, ym)).label("EN", loc="left")
    if not is_d:
        d += elm.Line().endpoints((xb - 0.7, g1.in1[1]), g1.in1).label("S", loc="left")
        d += elm.Line().endpoints((xb - 0.7, g2.in2[1]), g2.in2).label("R", loc="left")
    else:
        xd = xb - 1.6
        d += elm.Line().endpoints((xd - 0.9, g1.in1[1]), g1.in1).label("D", loc="left")
        d += lg.Dot().at((xd, g1.in1[1]))
        inv = d.add(lg.Not().right().at((xd, g2.in2[1])))
        d += elm.Line().endpoints((xd, g1.in1[1]), (xd, g2.in2[1]))
        d += elm.Line().endpoints(inv.out, g2.in2).label("D'", loc="bottom")
    return _sd(d, 85)


def u3_gated_sr():
    return _gated(False)


def u3_gated_d():
    return _gated(True)


FIGS = {
    "u3_seq_block": u3_seq_block,
    "u3_two_inv": u3_two_inv,
    "u3_nand_latch": u3_nand_latch,
    "u3_gated_sr": u3_gated_sr,
    "u3_gated_d": u3_gated_d,
}
