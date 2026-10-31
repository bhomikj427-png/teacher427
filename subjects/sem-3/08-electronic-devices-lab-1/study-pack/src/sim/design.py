"""Design problem: CE stage (partly bypassed emitter) + emitter follower, 9 V. Checks every spec in LTspice."""
import json
import numpy as np
from ltsim import run, OUT

INC = ".lib standard.bjt\n"
CORE = """V1 vcc 0 9
R1 vcc b1 220k
R2 b1 0 33k
Q1 c1 b1 e1 BC547B
RC vcc c1 8.2k
RE1 e1 x 82
RE2 x 0 820
CE x 0 100u
Q2 vcc c1 e2 BC547B
RE e2 0 1.8k
Cout e2 out 100u
RL out 0 10k
"""
R = {}
d, _ = run("des_ac", INC + "Vs in 0 AC 1\nCin in b1 10u\n" + CORE + ".ac dec 50 1 100Meg\n.end\n")
s = d[0]; f = s["frequency"]
R["gain_1k"] = float(np.interp(1e3, f, np.abs(s["v(out)"])))
R["rin_1k"] = float(np.interp(1e3, f, np.abs(1 / s["i(vs)"])))
g = np.abs(s["v(out)"]); a = np.interp(1e3, f, g)
R["fL"] = float(f[np.argmax(g > a / np.sqrt(2))]); R["fH"] = float(f[len(g) - 1 - np.argmax(g[::-1] > a / np.sqrt(2))])
d, _ = run("des_rout", INC + "Vs in 0 0\nCin in b1 10u\n" + CORE.replace("RL out 0 10k\n", "") + "Iout 0 out AC 1\n.ac list 1k\n.end\n")
R["rout_1k"] = float(abs(d[0]["v(out)"][0]))
d, _ = run("des_op", INC + "Vs in 0 0\nCin in b1 10u\n" + CORE + ".op\n.end\n")
o = d[0]
R["op"] = {k: float(o[k][0]) for k in ["v(b1)", "v(e1)", "v(c1)", "v(e2)"]}
R["supply_mA"] = float(-o["i(v1)"][0] * 1e3)
for amp in (0.018, 0.025):
    d, _ = run("des_tr", INC + f"Vs in 0 SINE(0 {amp} 1k)\nCin in b1 10u\n" + CORE + ".tran 0 300m 0 5u\n.end\n")
    s = d[0]; m = s["time"] > 290e-3; v = s["v(out)"][m]
    vv = v - v.mean()
    R[f"tran_{int(amp*1000)}mV"] = {"vpp": float(v.max() - v.min()), "pos": float(vv.max()), "neg": float(vv.min())}
(OUT / "design.json").write_text(json.dumps(R, indent=1))
print(json.dumps(R, indent=1))
