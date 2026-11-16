"""Check a pack's figures for overlapping labels (study-pack-format.md v1.3, §7.3).

Usage:  python tools/fig_overlap_check.py <pack src/build.py> [figure-name-prefix ...]

Imports the pack's build.py (which defines ALL = {name: fn}), draws every figure, and lists
labels that overlap. Exit 1 if any are found. The shared builder runs the same check on every
figure it renders, so this script is for checking figures before a build.
"""
import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import figlib  # noqa: E402


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv:
        print(__doc__)
        return 2
    path = Path(argv[0]).resolve()
    sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location("pack_build", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    figs = mod.ALL
    if argv[1:]:
        figs = {k: v for k, v in figs.items() if k.startswith(tuple(argv[1:]))}
    rep = figlib.run_all(figs)
    for name, prob in rep:
        print(f"{name}: {prob}")
    print(f"{len(figs)} figures checked, {len(rep)} problems")
    return 1 if rep else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
