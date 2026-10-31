"""Every ED-lab circuit from the manual, run in LTspice.

Writes out/results.json (numbers quoted in the pack) + out/<exp>.npz (curves for the figures).
Run: python sims.py
"""
import json
import numpy as np
from ltsim import run, OUT

R = {}
INC = ".lib standard.dio\n.lib standard.bjt\n.lib standard.jft\n.lib standard.mos\n"


def save(name, **arrs):
    np.savez(OUT / f"{name}.npz", **arrs)


def first(sw):
    return sw[list(sw)[0]]


def cross(x, y, level):
    """x where y first crosses level."""
    for k in range(1, len(y)):
        if (y[k - 1] - level) * (y[k] - level) <= 0 and y[k] != y[k - 1]:
            return float(x[k - 1] + (level - y[k - 1]) * (x[k] - x[k - 1]) / (y[k] - y[k - 1]))
    return None


def bw(f, g):
    """g = |gain|. Returns (Amax, fL, fH) at Amax/sqrt(2)."""
    k = int(np.argmax(g))
    a = float(g[k])
    lv = a / np.sqrt(2)
    fL = cross(f[:k + 1][::-1], g[:k + 1][::-1], lv)
    fH = cross(f[k:], g[k:], lv)
    return a, fL, fH


def at(x, y, pts):
    return [(float(p), float(np.interp(p, x, y))) for p in pts]


# ---------------- Exp 1: zener reverse characteristic
d, _ = run("exp01", INC + """* zener reverse bias, 1k series
Vs in 0 0
R1 in k 1k
D1 0 k BZX84C6V2L
.dc Vs 0 15 0.05
.end
""")
s = d[0]; x = first(s); vz = s["v(k)"]; iz = s["i(r1)"] * 1e3
save("exp01", vs=x, vz=vz, iz=iz)
v2, v8 = float(np.interp(2, iz, vz)), float(np.interp(8, iz, vz))
R["exp01"] = {"table": [(v, float(np.interp(v, x, vz)), float(np.interp(v, x, iz))) for v in range(0, 16)],
              "Vz_at_1mA": float(np.interp(1, iz, vz)), "Vz_at_5mA": float(np.interp(5, iz, vz)),
              "v2": v2, "v8": v8, "rz_2_8mA": (v8 - v2) / 6e-3}

# ---------------- Exp 2: zener regulator
d, _ = run("exp02a", INC + """* line regulation
V1 in 0 0
R1 in vo 1k
D1 0 vo BZX84C6V2L
R2 vo 0 1k
.dc V1 0 20 1
.end
""")
s = d[0]; x = first(s); vo = s["v(vo)"]
save("exp02a", vin=x, vo=vo)
R["exp02_line"] = {"table": [(float(a), float(b)) for a, b in zip(x, vo)],
                   "vo14": float(np.interp(14, x, vo)), "vo17": float(np.interp(17, x, vo)),
                   "line_reg_pct_14_17": float((np.interp(17, x, vo) - np.interp(14, x, vo)) / 3 * 100)}
rs = list(range(100, 1200, 100))
vals = []
for r in rs:
    d, _ = run("exp02b", INC + f"""* load regulation R={r}
V1 in 0 20
R1 in vo 1k
D1 0 vo BZX84C6V2L
R2 vo 0 {r}
.op
.end
""")
    vals.append(float(d[0]["v(vo)"][0]))
d, _ = run("exp02c", INC + """* no load
V1 in 0 20
R1 in vo 1k
D1 0 vo BZX84C6V2L
.op
.end
""")
vnl = float(d[0]["v(vo)"][0])
R["exp02_load"] = {"R": rs, "vo": vals, "VNL": vnl,
                   "loadreg_pct_1k": (vnl - vals[rs.index(1000)]) / vals[rs.index(1000)] * 100,
                   "loadreg_pct_600": (vnl - vals[rs.index(600)]) / vals[rs.index(600)] * 100}

# ---------------- Exp 3: clippers
for tag, net in [("a", "D1 out b 1N4007\nVb b 0 2"), ("b", "D1 b out 1N4007\nVb 0 b 2")]:
    d, _ = run(f"exp03{tag}", INC + f"""* clipper {tag}
V1 in 0 SINE(0 10 1k)
R1 in out 1k
{net}
.tran 0 3m 0 2u
.end
""")
    s = d[0]
    save(f"exp03{tag}", t=s["time"], vin=s["v(in)"], vo=s["v(out)"])
    R[f"exp03{tag}"] = {"max": float(s["v(out)"].max()), "min": float(s["v(out)"].min())}

# ---------------- Exp 4: clamper
d, _ = run("exp04", INC + """* clamper
V1 in 0 SINE(0 5 1k)
C1 in out 0.01u
D1 out 0 1N914
R1 out 0 1Meg
.tran 0 5m 0 2u
.end
""")
s = d[0]; t = s["time"]; m = t > 3e-3; vo = s["v(out)"]
save("exp04", t=t, vin=s["v(in)"], vo=vo)
R["exp04"] = {"max": float(vo[m].max()), "min": float(vo[m].min()), "vpp": float(vo[m].max() - vo[m].min()),
              "dc": float(np.mean(vo[m]))}

# ---------------- Exp 5: BJT CE characteristics
d, _ = run("exp05in", INC + """* input characteristics (manual directive)
Vbe vb 0 0
R1 vb base 2k
Q1 coll base 0 BC547B
R2 vcc coll 62k
Vce vcc 0 10
.dc Vbe 0 1 0.001 Vce 0 10 10
.end
""")
ins = [{"vce": vce, "vbase": sw["v(base)"], "ib": sw["ib(q1)"] * 1e6} for sw, vce in zip(d, [0, 10])]
save("exp05in", vb0=ins[0]["vbase"], ib0=ins[0]["ib"], vb1=ins[1]["vbase"], ib1=ins[1]["ib"])
c = ins[1]
vb10, vb30 = float(np.interp(10, c["ib"], c["vbase"])), float(np.interp(30, c["ib"], c["vbase"]))
R["exp05_in"] = {"n_sweeps": len(d), "vb10": vb10, "vb30": vb30, "hie": (vb30 - vb10) / 20e-6,
                 "vb_at_20uA_vce0": float(np.interp(20, ins[0]["ib"], ins[0]["vbase"])),
                 "vb_at_20uA_vce10": float(np.interp(20, ins[1]["ib"], ins[1]["vbase"])),
                 "table_vce0": at(ins[0]["vbase"], ins[0]["ib"], [0.5, 0.55, 0.6, 0.62, 0.64, 0.66, 0.68]),
                 "table_vce10": at(ins[1]["vbase"], ins[1]["ib"], [0.5, 0.55, 0.6, 0.62, 0.64, 0.66, 0.68])}
d, _ = run("exp05out", INC + """* output characteristics, IB stepped
Ib 0 base 0
Q1 coll base 0 BC547B
Vce coll 0 0
.dc Vce 0 12 0.05 Ib 0 60u 20u
.end
""")
outs = [{"ib": ib, "vce": first(sw), "ic": sw["ic(q1)"] * 1e3} for sw, ib in zip(d, [0, 20, 40, 60])]
save("exp05out", **{f"vce{k}": o["vce"] for k, o in enumerate(outs)}, **{f"ic{k}": o["ic"] for k, o in enumerate(outs)})
o20, o40 = outs[1], outs[2]
ic20_5, ic40_5 = float(np.interp(5, o20["vce"], o20["ic"])), float(np.interp(5, o40["vce"], o40["ic"]))
ic20_4, ic20_10 = float(np.interp(4, o20["vce"], o20["ic"])), float(np.interp(10, o20["vce"], o20["ic"]))
R["exp05_out"] = {"n_sweeps": len(d), "vce_pts": [0.2, 0.5, 1, 2, 4, 6, 8, 10, 12],
                  "table": [[float(np.interp(v, o["vce"], o["ic"])) for o in outs] for v in [0.2, 0.5, 1, 2, 4, 6, 8, 10, 12]],
                  "ic20_5": ic20_5, "ic40_5": ic40_5, "hfe": (ic40_5 - ic20_5) * 1e-3 / 20e-6,
                  "ic20_4": ic20_4, "ic20_10": ic20_10, "hoe": (ic20_10 - ic20_4) * 1e-3 / 6}
vals = {}
for vce in (2, 10):
    d, _ = run(f"exp05hre{vce}", INC + f"""* hre point
Ib 0 base 20u
Q1 coll base 0 BC547B
Vce coll 0 {vce}
.op
.end
""")
    vals[vce] = float(d[0]["v(base)"][0])
R["exp05_hre"] = {"vbe2": vals[2], "vbe10": vals[10], "hre": (vals[10] - vals[2]) / 8}
d, _ = run("exp05man", INC + """* manual output directive
Vbe vb 0 0
R1 vb base 2k
Q1 coll base 0 BC547B
R2 vcc coll 62k
Vce vcc 0 10
.dc Vce 0 20 1 Vbe 500m 600m 20m
.end
""")
R["exp05_manual_out_ic_max_uA"] = [float(np.max(sw["ic(q1)"]) * 1e6) for sw in d]
R["exp05_manual_out_ib_uA"] = [float(np.max(sw["ib(q1)"]) * 1e6) for sw in d]

# ---------------- Exp 6: CE amplifier (hands-on; expected values)
CE = """V1 vcc 0 15
Rs vs b1in 2.2k
Cin b1in b1 10u
R1 vcc b1 25k
R2 b1 0 8.2k
Rc vcc c1 560
Re e1 0 560
Ce e1 0 47u
Q1 c1 b1 e1 BC547B
Cc c1 out 10u
Rcro out 0 1Meg
"""
d, _ = run("exp06ac", INC + "* CE amp\nVs vs 0 AC 1\n" + CE + ".ac dec 50 10 100Meg\n.end\n")
s = d[0]; f = s["frequency"]; g = np.abs(s["v(out)"])
save("exp06ac", f=f, g=g)
a, fL, fH = bw(f, g)
R["exp06"] = {"Amax": a, "AmaxdB": 20 * np.log10(a), "fL": fL, "fH": fH,
              "table": at(f, g, [100, 500, 800, 1e3, 5e3, 10e3, 50e3, 100e3, 500e3, 800e3, 1e6])}
d, _ = run("exp06op", INC + "* op\nVs vs 0 0\n" + CE + ".op\n.end\n")
o = d[0]
R["exp06_op"] = {"vb": float(o["v(b1)"][0]), "ve": float(o["v(e1)"][0]), "vc": float(o["v(c1)"][0]),
                 "ic_mA": float(o["ic(q1)"][0] * 1e3)}
for amp in (0.5, 0.1, 0.02):
    d, _ = run(f"exp06tr", INC + f"* CE amp transient\nVs vs 0 SINE(0 {amp} 1k)\n" + CE + ".tran 0 30m 0 5u\n.end\n")
    s = d[0]; m = s["time"] > 22e-3
    save(f"exp06tr{int(amp * 1000)}", t=s["time"][m], vo=s["v(out)"][m], vs=s["v(vs)"][m])
    R[f"exp06_tran_{int(amp * 1000)}mV"] = {"vomax": float(s["v(out)"][m].max()), "vomin": float(s["v(out)"][m].min())}

# ---------------- Exp 7: emitter follower
EF = """V1 vcc 0 15
R2 vcc b 33k
R3 b 0 3.3k
Q1 vcc b e BC547B
R4 e 0 2k
C2 in b 10u
C1 e out 10u
Rp out 0 1Meg
"""
d, _ = run("exp07ac", INC + "* EF\nV2 in 0 AC 0.5\n" + EF + ".ac dec 50 10 1G\n.end\n")
s = d[0]; f = s["frequency"]; g = np.abs(s["v(out)"]) / 0.5
save("exp07ac", f=f, g=g)
a, fL, fH = bw(f, g)
R["exp07"] = {"Amax": a, "fL": fL, "fH": fH, "table": at(f, g, [200, 500, 1e3, 10e3, 100e3, 1e6])}
d, _ = run("exp07tr", INC + "* EF tran\nV2 in 0 SINE(0 0.5 1k)\n" + EF + ".tran 0 10m 0 5u\n.end\n")
s = d[0]; m = s["time"] > 6e-3
save("exp07tr", t=s["time"], vin=s["v(in)"], vo=s["v(out)"])
R["exp07_tran"] = {"vo_pp": float(s["v(out)"][m].max() - s["v(out)"][m].min())}
d, _ = run("exp07op", INC + "* op\nV2 in 0 0\n" + EF + ".op\n.end\n")
R["exp07_op"] = {"vb": float(d[0]["v(b)"][0]), "ve": float(d[0]["v(e)"][0]), "ie_mA": float(d[0]["v(e)"][0] / 2)}

# ---------------- Exp 8: negative feedback (bypass capacitor in / out)
FB = """V1 vcc 0 15
R6 in a 2.2k
C2 a b 6u
R2 vcc b 68k
R3 b 0 22k
R1 vcc c 4.7k
R4 e 0 2.2k
Q1 c b e 2N2222
C3 c out 0.33u
R5 out 0 47k
"""
res8 = {}
for tag, extra in [("with_Ce", "C1 e 0 47u\n"), ("no_Ce", "")]:
    d, _ = run(f"exp08{tag}", INC + "* fb\nV2 in 0 AC 1\n" + FB + extra + ".ac dec 50 1 1G\n.end\n")
    s = d[0]; f = s["frequency"]; g = np.abs(s["v(out)"])
    save(f"exp08{tag}", f=f, g=g)
    a, fL, fH = bw(f, g)
    res8[tag] = {"Amax": a, "AmaxdB": 20 * np.log10(a), "fL": fL, "fH": fH,
                 "table": at(f, g, [100, 500, 1e3, 5e3, 10e3, 50e3, 100e3, 500e3, 1e6])}
d, _ = run("exp08op", INC + "* op\nV2 in 0 0\n" + FB + ".op\n.end\n")
res8["op"] = {"vb": float(d[0]["v(b)"][0]), "ve": float(d[0]["v(e)"][0]), "vc": float(d[0]["v(c)"][0])}
R["exp08"] = res8

# ---------------- Exp 9: JFET characteristics
d, _ = run("exp09out", INC + """* JFET drain characteristics
Vgs g 0 0
Vds d 0 0
J1 d g 0 2N3819
.dc Vds 0 16 0.1 Vgs 0 -3 -1
.end
""")
o9 = [{"vgs": vgs, "vds": first(sw), "id": sw["id(j1)"] * 1e3} for sw, vgs in zip(d, [0, -1, -2, -3])]
save("exp09out", **{f"vds{k}": o["vds"] for k, o in enumerate(o9)}, **{f"id{k}": o["id"] for k, o in enumerate(o9)})
d, _ = run("exp09tr", INC + """* JFET transfer
Vgs g 0 0
Vds d 0 8
J1 d g 0 2N3819
.dc Vgs -5 0 0.01
.end
""")
s = d[0]; vg = first(s); idt = s["id(j1)"] * 1e3
save("exp09tr", vgs=vg, id=idt)
o0, o1 = o9[0], o9[1]
id6, id7 = float(np.interp(6, o0["vds"], o0["id"])), float(np.interp(7, o0["vds"], o0["id"]))
id4_0, id4_1 = float(np.interp(4, o0["vds"], o0["id"])), float(np.interp(4, o1["vds"], o1["id"]))
R["exp09"] = {"n_sweeps": len(o9), "table": [[float(np.interp(v, o["vds"], o["id"])) for o in o9] for v in range(0, 9)],
              "IDSS_Vds8": float(np.interp(0, vg, idt)), "VP": float(vg[np.argmax(idt > 1e-3)]),
              "id6": id6, "id7": id7, "rd": 1 / ((id7 - id6) * 1e-3),
              "id4_0": id4_0, "id4_m1": id4_1, "gm_mS": id4_0 - id4_1}

# ---------------- Exp 10: CS amplifier
CS = """VDD vdd 0 12
RA vdd g 6.8Meg
RB g 0 1Meg
C1 in g 1u
R1 vdd d 3.3k
Rs s 0 2.2k
Cs s 0 100u
J1 d g s 2N5434
C2 d out 0.5u
R2 out 0 10k
"""
d, _ = run("exp10ac", INC + "* CS\nVin in 0 AC 1\n" + CS + ".ac dec 50 1 1G\n.end\n")
s = d[0]; f = s["frequency"]; g = np.abs(s["v(out)"])
save("exp10ac", f=f, g=g)
a, fL, fH = bw(f, g)
R["exp10"] = {"Amax": a, "AmaxdB": 20 * np.log10(a), "fL": fL, "fH": fH,
              "table": at(f, g, [100, 1e3, 5e3, 10e3, 50e3, 100e3, 500e3, 1e6, 5e6, 10e6, 100e6])}
d, _ = run("exp10tr", INC + "* CS tran\nVin in 0 SINE(0 0.1 1k)\n" + CS + ".tran 0 10m 0 2u\n.end\n")
s = d[0]; m = s["time"] > 6e-3
save("exp10tr", t=s["time"], vin=s["v(in)"], vo=s["v(out)"])
R["exp10_tran"] = {"vo_pp": float(s["v(out)"][m].max() - s["v(out)"][m].min()), "vin_pp": 0.2}
d, _ = run("exp10op", INC + "* op\nVin in 0 0\n" + CS + ".op\n.end\n")
R["exp10_op"] = {"vg": float(d[0]["v(g)"][0]), "vs": float(d[0]["v(s)"][0]), "vd": float(d[0]["v(d)"][0]),
                 "id_mA": float(d[0]["v(s)"][0] / 2.2)}

# ---------------- Exp 11: RC phase-shift oscillator
res11 = {}
for C in ("0.5n", "1n"):
    d, _ = run("exp11", INC + f"""* phase shift oscillator
V1 vcc 0 10
R4 vcc b 57k
R3 b 0 10k
R1 vcc c 6.8k
R2 e 0 1.5k
C1 e 0 100n
Q1 c b e BC547B
C2 c n1 {C}
R5 n1 0 10k
C3 n1 n2 {C}
R6 n2 0 10k
C4 n2 b {C}
C6 c out 10u
Ro out 0 1Meg
.tran 0 10m 0 0.2u startup
.end
""")
    s = d[0]; t = s["time"]; v = s["v(c)"]
    m = t > 7e-3
    tt, vv = t[m], v[m] - np.mean(v[m])
    zc = [tt[k - 1] - vv[k - 1] * (tt[k] - tt[k - 1]) / (vv[k] - vv[k - 1])
          for k in range(1, len(vv)) if vv[k - 1] < 0 <= vv[k]]
    fobs = (len(zc) - 1) / (zc[-1] - zc[0]) if len(zc) > 2 else None
    Cv = 0.5e-9 if C == "0.5n" else 1e-9
    fth = 1 / (2 * np.pi * 10e3 * Cv * np.sqrt(6))
    save(f"exp11_{C}", t=t, vo=v)
    res11[C] = {"f_obs": fobs, "f_theory": float(fth), "vpp": float(vv.max() - vv.min()),
                "err_pct": (float(fth) - fobs) / float(fth) * 100 if fobs else None}
R["exp11"] = res11

# ---------------- Exp 12: MOSFET resistive-load inverter
d, _ = run("exp12tr", INC + """* inverter transient
V1 vdd 0 5
R1 vdd out 1k
M1 out in 0 FDR6580
V2 in 0 PULSE(0 5 0 0 0 1m 2m 10)
.tran 0 20m 0 1u
.end
""")
s = d[0]
save("exp12tr", t=s["time"], vin=s["v(in)"], vo=s["v(out)"])
R["exp12_tran"] = {"vout_max": float(s["v(out)"].max()), "vout_min": float(s["v(out)"].min())}
d, _ = run("exp12vtc", INC + """* inverter VTC
V1 vdd 0 5
R1 vdd out 1k
M1 out in 0 FDR6580
V2 in 0 0
.dc V2 0 5 0.001
.end
""")
s = d[0]; vi = first(s); vo = s["v(out)"]
save("exp12vtc", vin=vi, vo=vo)
slope = np.gradient(vo, vi)
idx = np.where(slope < -1)[0]
R["exp12_vtc"] = {"VOH": float(vo[0]), "VOL": float(vo[-1]), "VIL": float(vi[idx[0]]), "VIH": float(vi[idx[-1]]),
                  "VM": cross(vi, vo - vi, 0), "VOUT_at_VIL": float(vo[idx[0]]), "VOUT_at_VIH": float(vo[idx[-1]])}

# ---------------- Additional: two-stage RC-coupled amplifier
ST1 = """V1 vcc 0 15
R6 in a 2.2k
C2 a b1 10u
R2 vcc b1 25k
R3 b1 0 8.2k
R1 vcc c1 560
R4 e1 0 560
C1 e1 0 47u
Q1 c1 b1 e1 BC547B
"""
d, _ = run("expAs", INC + "* single stage, 1k load\nV2 in 0 AC 1\n" + ST1 + "C3 c1 out 10u\nR5 out 0 1k\n.ac dec 50 10 100Meg\n.end\n")
s = d[0]; f1 = s["frequency"]; g1 = np.abs(s["v(out)"])
d, _ = run("expAt", INC + "* two stage\nV2 in 0 AC 1\n" + ST1 + """C3 c1 b2 10u
R8 vcc b2 25k
R9 b2 0 8.2k
R7 vcc c2 560
R10 e2 0 560
C4 e2 0 47u
Q2 c2 b2 e2 BC547B
C6 c2 out 10u
R11 out 0 1k
.ac dec 50 10 100Meg
.end
""")
s = d[0]; f2 = s["frequency"]; g2 = np.abs(s["v(out)"]); g21 = np.abs(s["v(b2)"])
save("expA", f1=f1, g1=g1, f2=f2, g2=g2, g21=g21)
a1, l1, h1 = bw(f1, g1)
a2, l2, h2 = bw(f2, g2)
R["expA"] = {"one": {"Amax": a1, "dB": 20 * np.log10(a1), "fL": l1, "fH": h1},
             "two": {"Amax": a2, "dB": 20 * np.log10(a2), "fL": l2, "fH": h2},
             "table": [(p, float(np.interp(p, f1, g1)), float(np.interp(p, f2, g2)))
                       for p in [100, 500, 800, 1e3, 5e3, 10e3, 50e3, 100e3, 500e3, 800e3, 1e6, 2e6, 3e6]]}

# ---------------- Exp 5 corrected input sweep: collector driven directly (R2 shorted), VCE = 0 V and 5 V
d, _ = run("exp05in2", INC + """* input characteristics, collector held at VCE
Vbe vb 0 0
R1 vb base 2k
Q1 coll base 0 BC547B
Vce coll 0 0
.dc Vbe 0 1 0.001 Vce 0 5 5
.end
""")
c0 = {"vb": d[0]["v(base)"], "ib": d[0]["ib(q1)"] * 1e6}
c5 = {"vb": d[1]["v(base)"], "ib": d[1]["ib(q1)"] * 1e6}
save("exp05in2", vb0=c0["vb"], ib0=c0["ib"], vb5=c5["vb"], ib5=c5["ib"])
v10, v30 = float(np.interp(10, c5["ib"], c5["vb"])), float(np.interp(30, c5["ib"], c5["vb"]))
R["exp05_in2"] = {"vb10_5V": v10, "vb30_5V": v30, "hie": (v30 - v10) / 20e-6,
                  "table_vce0": at(c0["vb"], c0["ib"], [0.5, 0.55, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7]),
                  "table_vce5": at(c5["vb"], c5["ib"], [0.5, 0.55, 0.6, 0.62, 0.64, 0.66, 0.68, 0.7])}

# ---------------- Exp 7 wide sweep for the lower cut-off
d, _ = run("exp07wide", INC + "* EF wide\nV2 in 0 AC 0.5\n" + EF + ".ac dec 50 0.01 10Meg\n.end\n")
s = d[0]; f = s["frequency"]; g = np.abs(s["v(out)"]) / 0.5
gm_ = float(np.interp(1e3, f, g))
R["exp07_wide"] = {"A1k": gm_, "fL": cross(f, g, gm_ / np.sqrt(2))}

(OUT / "results.json").write_text(json.dumps(R, indent=1, default=float))
print("done")
