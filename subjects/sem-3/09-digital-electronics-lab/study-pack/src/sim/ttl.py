"""Exp 14: standard TTL NAND (7400 internal circuit) and TTL NOR (7402-style) in LTspice. DC truth tables + VTC."""
import json
import numpy as np
from ltsim import run, OUT

INC = ".lib standard.bjt\n.lib standard.dio\n"
NAND = """VCC vcc 0 5
VA a 0 {va}
VB b 0 {vb}
R1 vcc b1 4k
Q1a c1 b1 a 2N2222
Q1b c1 b1 b 2N2222
R2 vcc c2 1.6k
Q2 c2 c1 e2 2N2222
R3 e2 0 1k
R4 vcc c4 130
Q4 c4 c2 e4 2N2222
D1 e4 out 1N4148
Q3 out e2 0 2N2222
RL out 0 100k
"""
NOR = """VCC vcc 0 5
VA a 0 {va}
VB b 0 {vb}
R1a vcc b1a 4k
R1b vcc b1b 4k
Q1a c1a b1a a 2N2222
Q1b c1b b1b b 2N2222
R2 vcc c2 1.6k
Q2a c2 c1a e2 2N2222
Q2b c2 c1b e2 2N2222
R3 e2 0 1k
R4 vcc c4 130
Q4 c4 c2 e4 2N2222
D1 e4 out 1N4148
Q3 out e2 0 2N2222
RL out 0 100k
"""
R = {}
for name, net in [("nand", NAND), ("nor", NOR)]:
    rows = []
    for va in (0, 5):
        for vb in (0, 5):
            d, _ = run(f"{name}_op", INC + net.format(va=va, vb=vb) + ".op\n.end\n")
            rows.append([int(va > 0), int(vb > 0), round(float(d[0]["v(out)"][0]), 3)])
    R[name] = rows
    d, _ = run(f"{name}_vtc", INC + net.format(va=0, vb=5 if name == "nand" else 0).replace("VA a 0 0", "VA a 0 0") + ".dc VA 0 5 0.01\n.end\n")
    s = d[0]; x = s[list(s)[0]]; y = s["v(out)"]
    np.savez(OUT / f"{name}_vtc.npz", vin=x, vout=y)
    k = int(np.argmin(abs(y - x)))
    R[name + "_vtc"] = {"VOH": float(y[0]) if name == "nand" else float(y[0]), "VOL": float(y[-1]), "VM": float(x[k])}
(OUT / "ttl.json").write_text(json.dumps(R, indent=1))
print(json.dumps(R, indent=1))
