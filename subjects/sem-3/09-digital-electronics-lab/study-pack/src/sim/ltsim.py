"""Run an LTspice netlist in batch mode and parse the ASCII .raw file.

run(name, netlist) -> (data, log_text)
data = list of sweeps; each sweep is a dict {trace_name_lower: numpy array}.
Stepped runs (.step / nested .dc) are split where the sweep variable restarts.
"""
import os
import re
import subprocess
from pathlib import Path

import numpy as np

LTSPICE = Path(os.path.expandvars(r"%LOCALAPPDATA%\Programs\ADI\LTspice\LTspice.exe"))
OUT = Path(__file__).resolve().parent / "out"


def run(name, netlist):
    OUT.mkdir(exist_ok=True)
    net = OUT / f"{name}.net"
    net.write_text(f"* {name}\n" + netlist, encoding="latin1")
    for ext in (".raw", ".log"):
        (OUT / f"{name}{ext}").unlink(missing_ok=True)
    r = subprocess.run([str(LTSPICE), "-b", "-ascii", str(net)], timeout=300)
    log = _read(OUT / f"{name}.log") if (OUT / f"{name}.log").exists() else ""
    if r.returncode or not (OUT / f"{name}.raw").exists():
        raise RuntimeError(f"{name} failed:\n{log}")
    return parse(OUT / f"{name}.raw"), log


def _read(p):
    b = p.read_bytes()
    if b[:2] in (b"\xff\xfe",) or (len(b) > 1 and b[1:2] == b"\x00"):
        return b.decode("utf-16-le", errors="replace").lstrip("﻿")
    return b.decode("latin1")


def parse(p):
    t = _read(p)
    head, body = t.split("Values:", 1)
    names = []
    complex_ = "complex" in head.lower().split("flags:")[1].splitlines()[0]
    nvars = int(re.search(r"No\. Variables:\s*(\d+)", head).group(1))
    vsec = head.split("Variables:")[-1].strip().splitlines()
    for line in vsec[:nvars]:
        parts = line.split()
        names.append(parts[1].lower())
    toks = body.split()
    rows = []
    i = 0
    while i < len(toks):
        i += 1  # point index
        row = []
        for _ in range(nvars):
            tk = toks[i]
            i += 1
            if complex_:
                re_, im_ = tk.split(",")
                row.append(complex(float(re_), float(im_)))
            else:
                row.append(float(tk))
        rows.append(row)
    arr = np.array(rows)
    x = np.real(arr[:, 0])
    # split stepped runs where the sweep variable restarts
    cuts = [0] + [k for k in range(1, len(x)) if (x[k] - x[k - 1]) * (x[1] - x[0] if len(x) > 1 else 1) < 0
                  and abs(x[k] - x[0]) < 1e-12 + 1e-9 * abs(x[0])] + [len(x)]
    sweeps = []
    for a, b in zip(cuts[:-1], cuts[1:]):
        d = {n: arr[a:b, j] for j, n in enumerate(names)}
        if not complex_:
            d = {n: np.real(v) for n, v in d.items()}
        else:
            d[names[0]] = np.real(d[names[0]])
        sweeps.append(d)
    return sweeps


def meas(log, key):
    m = re.search(rf"^{key}\S*[:=]\s*.*?=?\s*([-+0-9.eE]+)", log, flags=re.M | re.I)
    return float(m.group(1)) if m else None
