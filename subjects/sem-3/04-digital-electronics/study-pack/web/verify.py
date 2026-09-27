"""Check every minimized answer and every drawn K-map group in the web pack.

For each answer: the SOP must be 1 on every minterm and 0 on every non-don't-care maxterm.
For each drawn group: the group's cells must be exactly the cells of its term.
Run: python verify.py
"""
import itertools
import re

import figures as F


def term_cells(term, vars_):
    """'a'bc'' over vars 'abcd' -> set of minterm indices where the product term is 1."""
    lits = re.findall(r"([A-Za-z])('?)", term)
    n = len(vars_)
    out = set()
    for bits in itertools.product((0, 1), repeat=n):
        val = dict(zip(vars_, bits))
        if all(val[v] == (0 if neg else 1) for v, neg in lits):
            out.add(int("".join(map(str, bits)), 2))
    return out


def sop(expr, vars_):
    return set().union(*(term_cells(t.strip(), vars_) for t in expr.split("+")))


def check(name, expr, vars_, ones, dcs=()):
    n = len(vars_)
    cover = sop(expr, vars_)
    ones, dcs = set(ones), set(dcs)
    zeros = set(range(2 ** n)) - ones - dcs
    ok = ones <= cover and not (cover & zeros)
    print(f"{'OK ' if ok else 'BAD'} {name}: F = {expr}")
    assert ok, (ones - cover, cover & zeros)


def check_group(name, cells, term, vars_):
    ok = set(cells) == term_cells(term, vars_)
    print(f"{'OK ' if ok else 'BAD'}   group {term:8} = {sorted(cells)}  ({name})")
    assert ok


q4 = ([0, 4, 5, 7, 8, 9, 15], [1, 3, 6, 14])
check("MTE Q4", "b'c' + bc + a'b", "abcd", *q4)
check("MTE Q4 alt (self-test 5)", "b'c' + bc + a'c'", "abcd", *q4)
check_group("q4", [0, 1, 8, 9], "b'c'", "abcd")
check_group("q4", [6, 7, 14, 15], "bc", "abcd")
check_group("q4", [4, 5, 6, 7], "a'b", "abcd")
check_group("q4", [0, 1, 4, 5], "a'c'", "abcd")
check("self-test 2", "a'b'c + a'bc' + ab'c'", "abc", [1, 2, 4])
check("self-test 3", "w'x' + w'z + x'y", "wxyz", [0, 1, 3, 5, 7, 10, 11], [2, 6, 13])
check_group("ans3", [0, 1, 3, 2], "w'x'", "wxyz")
check_group("ans3", [1, 3, 5, 7], "w'z", "wxyz")
check_group("ans3", [3, 2, 11, 10], "x'y", "wxyz")
check("self-test 4", "B'D'", "ABCD", [0, 2, 8, 10])
check("self-test 6", "xz + wz' + vw'z + v'x'z'", "vwxyz", F.Q6_ONES, F.Q6_DC)
check_group("ans6", [5, 7, 13, 15, 21, 23, 29, 31], "xz", "vwxyz")
check_group("ans6", [8, 10, 12, 14, 24, 26, 28, 30], "wz'", "vwxyz")
check_group("ans6", [17, 19, 21, 23], "vw'z", "vwxyz")
check_group("ans6", [0, 2, 8, 10], "v'x'z'", "vwxyz")
# group-size strip
for cells, term in (([5], "a'bc'd"), ([5, 7], "a'bd"), ([5, 7, 13, 15], "bd"),
                    ([1, 3, 5, 7, 13, 15, 9, 11], "d")):
    check_group("sizes", cells, term, "abcd")
check_group("dontcare", [7, 15], "bcd", "abcd")
check_group("dontcare", [6, 7, 14, 15], "bc", "abcd")
check_group("corners", [0, 2, 8, 10], "b'd'", "abcd")
# POS example: F = Σm(0,1,2,3,7), groups of 0s give F' = ab' + ac'
check_group("pos", [4, 5], "ab'", "abc")
check_group("pos", [4, 6], "ac'", "abc")
check("POS example as SOP (a' + bc)", "a' + bc", "abc", [0, 1, 2, 3, 7])
fp = sop("ab' + ac'", "abc")
assert fp == {4, 5, 6}, fp
print("OK  POS example: F' = ab' + ac' is exactly the 0-cells, so F = (a' + b)(a' + c)")
print("all checks passed")
