"""Render every zero-argument figure; write a preview sheet HTML -> PDF for visual checks. usage: figtest.py [module]"""
import importlib, inspect, sys, traceback
from pathlib import Path
import build
HERE = Path(__file__).resolve().parent
mods = sys.argv[1:] or sorted(p.stem for p in HERE.glob("figs*.py"))
out, bad = [], 0
for mn in mods:
    m = importlib.import_module(mn)
    for name, fn in inspect.getmembers(m, inspect.isfunction):
        if name.startswith("_") or fn.__module__ != mn: continue
        if any(p.default is p.empty for p in inspect.signature(fn).parameters.values()): continue
        try:
            r = fn()
            if not isinstance(r, str): continue
            out.append(f'<div style="break-inside:avoid;border:1px solid #ccc;margin:6px 0;padding:4px"><code>{mn}.{name}</code><div class="fig">{r}</div></div>')
        except Exception:
            bad += 1; print("FAIL", mn, name); traceback.print_exc(limit=3)
html = HERE / "figtest.html"
html.write_text(f'<!doctype html><meta charset="utf-8"><style>{build.CSS}</style>' + "\n".join(out), encoding="utf-8")
print(len(out), "figures ok,", bad, "failed ->", build.pdf(html))
