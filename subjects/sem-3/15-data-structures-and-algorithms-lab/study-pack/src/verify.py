"""Compile every program in code/ and run it on test inputs; must print ALL PASS.

Run:  python verify.py
- Compiles with g++ -std=c++17 -Wall -Wextra -pedantic-errors -Werror (VLAs and all warnings are errors).
- Runs each case with stdin piped in, checks the expected text appears, saves the screen output to
  out/<case>.txt (build.py embeds these, so the PDF always shows real output).
- Also compiles the manual's broken copies in code/manual_original/ and saves the compiler errors to
  out/err_<name>.txt (the PDF quotes them), checking that they really fail.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CODE = HERE / "code"
BIN = HERE / "bin"
OUT = HERE / "out"
GXX = shutil.which("g++") or str(Path.home() / "AppData/Local/Microsoft/WinGet/Packages/"
                                  "BrechtSanders.WinLibs.POSIX.UCRT_Microsoft.Winget.Source_8wekyb3d8bbwe/mingw64/bin/g++.exe")
FLAGS = ["-std=c++17", "-Wall", "-Wextra", "-pedantic-errors", "-Werror", "-O0", "-static"]

# (case name, program, stdin, [texts that must appear in the output])
CASES = [
    ("p01", "p01_hello", "", ["Hello, lab!"]),
    ("p02", "p02_input", "17 5\n", ["Sum = 22", "a / b = 3", "a % b = 2", "a is bigger"]),
    ("p03", "p03_loops_arrays", "4\n0\n", ["for loop: 10 20 30 40 50", "50 40 30 20 10"]),
    ("p04", "p04_functions", "", ["square(7) = 49", "2 4 6", "after tryToChange: 5", "after reallyChange: 99"]),
    ("e01", "e01_pointers", "", ["Value of number = 25", "Value using pointer = 25"]),
    ("e02", "e02_pointer_arithmetic", "", ["Value : 10", "Value : 20", "Value : 30"]),
    ("e03_begin", "e03_array_insert", "5\n10 20 30 40 50\n1\n5\n", ["5 10 20 30 40 50"]),
    ("e03_pos", "e03_array_insert", "5\n10 20 30 40 50\n2\n3\n25\n", ["10 20 25 30 40 50"]),
    ("e03_end", "e03_array_insert", "5\n10 20 30 40 50\n3\n60\n", ["10 20 30 40 50 60"]),
    ("e03_pos_last", "e03_array_insert", "3\n1 2 3\n2\n4\n9\n", ["1 2 3 9"]),
    ("e03_bad_pos", "e03_array_insert", "3\n1 2 3\n2\n7\n", ["Invalid position."]),
    ("e04_begin", "e04_array_delete", "5\n10 20 30 40 50\n1\n", ["20 30 40 50"]),
    ("e04_pos", "e04_array_delete", "5\n10 20 30 40 50\n2\n3\n", ["Deleted element: 30", "10 20 40 50"]),
    ("e04_end", "e04_array_delete", "5\n10 20 30 40 50\n3\n", ["10 20 30 40"]),
    ("e04_bad_pos", "e04_array_delete", "5\n10 20 30 40 50\n2\n6\n", ["Invalid position."]),
    ("e05", "e05_matrix_multiply", "2 2\n2 2\n1 2\n3 4\n5 6\n7 8\n", ["19 22", "43 50"]),
    ("e05_rect", "e05_matrix_multiply", "2 3\n3 2\n1 2 3\n4 5 6\n7 8\n9 10\n11 12\n", ["58 64", "139 154"]),
    ("e05_bad", "e05_matrix_multiply", "2 3\n2 3\n", ["Matrix multiplication not possible."]),
    ("e06", "e06_matrix_transpose", "2 3\n1 2 3\n4 5 6\n", ["1 4", "2 5", "3 6"]),
    ("e07", "e07_insertion_sort", "6\n5 2 4 6 1 3\n", ["Original Array: 5 2 4 6 1 3", "Sorted Array: 1 2 3 4 5 6"]),
    ("e07_dup", "e07_insertion_sort", "7\n3 -1 3 0 9 -1 2\n", ["Sorted Array: -1 -1 0 2 3 3 9"]),
    ("e08", "e08_quick_sort", "6\n10 7 8 9 1 5\n", ["Sorted Array using Quick Sort: 1 5 7 8 9 10"]),
    ("e08_dup", "e08_quick_sort", "8\n4 4 1 9 0 4 -3 7\n", ["-3 0 1 4 4 4 7 9"]),
    ("e08_compare", "e08_sort_compare", "6\n10 7 8 9 1 5\n",
     ["Quick Sort     : 1 5 7 8 9 10", "Bubble Sort    : 1 5 7 8 9 10",
      "Selection Sort : 1 5 7 8 9 10", "Insertion Sort : 1 5 7 8 9 10", " ms"]),
    ("e09", "e09_stack", "1\n10\n1\n20\n1\n30\n4\n3\n2\n4\n2\n2\n2\n5\n",
     ["30 20 10", "Top element is 30", "30 popped", "Stack Underflow!", "Program terminated."]),
    ("e09_over", "e09_stack", "1\n1\n1\n2\n1\n3\n1\n4\n1\n5\n1\n6\n5\n", ["Stack Overflow!"]),
    ("e10", "e10_queue", "1\n10\n1\n20\n1\n30\n3\n2\n3\n4\n",
     ["10 inserted into queue.", "10 20 30", "10 deleted from queue.", "20 30", "Program terminated."]),
    ("e10_limits", "e10_queue", "2\n1\n1\n1\n2\n1\n3\n1\n4\n1\n5\n1\n6\n2\n2\n1\n7\n3\n4\n",
     ["Queue Underflow!", "Queue Overflow!", "3 4 5"]),
    ("e11", "e11_singly_linked_list", "1\n10\n1\n20\n1\n30\n3\n2\n3\n4\n",
     ["Linked List: 10 20 30", "10 deleted from list.", "Linked List: 20 30", "Program terminated."]),
    ("e11_empty", "e11_singly_linked_list", "2\n3\n1\n5\n2\n3\n4\n", ["List is empty."]),
    ("e12", "e12_circular_linked_list", "1\n10\n1\n20\n1\n30\n3\n2\n3\n4\n",
     ["Circular Linked List: 10 20 30", "10 deleted from list.", "Circular Linked List: 20 30",
      "Program terminated."]),
    ("e12_one", "e12_circular_linked_list", "1\n7\n2\n3\n2\n4\n", ["7 deleted from list.", "List is empty."]),
    ("e04b", "e04b_array_menu", "1\n1 10\n1\n2 30\n1\n2 20\n3\n2\n1\n3\n2\n5\n4\n",
     ["Array: 10 20 30", "Deleted element: 10", "Array: 20 30", "Invalid position."]),
    ("e10b", "e10b_circular_queue", "1\n1\n1\n2\n1\n3\n1\n4\n1\n5\n1\n6\n2\n2\n1\n6\n1\n7\n3\n1\n8\n4\n",
     ["Queue Overflow!", "1 deleted", "2 deleted", "6 inserted", "7 inserted", "3 4 5 6 7", "Program terminated."]),
]

# Manual copies that must FAIL to compile (strict flags), stored for the PDF.
BROKEN = ["m07_vla", "m10_screenshot", "m12_listing"]


def compile_(src, exe, extra=()):
    r = subprocess.run([GXX, *FLAGS, *extra, str(src), "-o", str(exe)], capture_output=True, text=True)
    return r.returncode, r.stderr


def tidy(err, limit=6):
    """Keep the first `limit` distinct errors, each with its source line and caret."""
    err = err.replace(str(CODE / "manual_original") + "\\", "").replace(str(CODE) + "\\", "")
    lines = err.splitlines()
    blocks, seen = [], set()
    for k, ln in enumerate(lines):
        m = re.match(r"(\S+?):(\d+):\d+: error: (.*)", ln)
        if not m or m.group(3) in seen:
            continue
        seen.add(m.group(3))
        block = [ln]
        for nxt in lines[k + 1:k + 3]:
            if re.match(r"\s*\d*\s*\|", nxt):
                block.append(nxt.rstrip())
        blocks.append("\n".join(block))
        if len(blocks) == limit:
            break
    return "\n".join(blocks)


def main():
    BIN.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)
    fails = 0
    for src in sorted(CODE.glob("*.cpp")) + sorted((CODE / "variants").glob("*.cpp")):
        code, err = compile_(src, BIN / (src.stem + ".exe"))
        if code:
            print("COMPILE FAIL", src.name, "\n", err)
            fails += 1
        elif not src.stem.startswith("t_"):
            compile_(src, BIN / ("echo_" + src.stem + ".exe"), ["-include", str(HERE / "echo.h")])
    for name, prog, stdin, wants in CASES:
        exe = BIN / (prog + ".exe")
        if not exe.exists():
            print("MISSING", prog)
            fails += 1
            continue
        try:
            r = subprocess.run([str(exe)], input=stdin, capture_output=True, text=True, timeout=60)
            out = r.stdout
        except subprocess.TimeoutExpired:
            print("TIMEOUT", name)
            fails += 1
            continue
        shown = subprocess.run([str(BIN / f"echo_{prog}.exe")], input=stdin, capture_output=True,
                               text=True, timeout=60).stdout
        (OUT / f"{name}.txt").write_text(shown.rstrip() + "\n", encoding="utf-8")
        missing = [w for w in wants if w not in out]
        print(("ok  " if not missing else "FAIL") + f" {name}" + (f"  missing {missing}" if missing else ""))
        fails += bool(missing)
    for b in BROKEN:
        src = CODE / "manual_original" / f"{b}.cpp"
        code, err = compile_(src, BIN / f"{b}.exe")
        (OUT / f"err_{b}.txt").write_text(tidy(err), encoding="utf-8")
        print(("ok  " if code else "FAIL") + f" {b} fails to compile as expected")
        fails += not code
    # variant test drivers print PASS/FAIL lines themselves
    for exe in sorted(BIN.glob("t_*.exe")):
        r = subprocess.run([str(exe)], capture_output=True, text=True, timeout=60)
        bad = [ln for ln in r.stdout.splitlines() if ln.startswith("FAIL")]
        n = r.stdout.count("PASS")
        print(("ok  " if not bad and n else "FAIL") + f" {exe.stem}: {n} checks" + (f" {bad}" if bad else ""))
        fails += bool(bad) or not n
    print("ALL PASS" if not fails else f"{fails} FAILURE(S)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
