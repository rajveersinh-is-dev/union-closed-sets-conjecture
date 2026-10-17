"""
Explore restricted classes of union-closed families to look for provable
special cases or structural patterns.  Computation as assistant only.

For each ground size n and each restriction, enumerate all union-closed
families, filter by the restriction, and report the minimum of
max_x d(x)/m (the "Frankl ratio").  If the minimum is >= 1/2 for a class,
that supports (but does not prove) a special-case theorem.

Restrictions tested:
  all            : every non-trivial union-closed family
  no_empty       : empty set not a member
  no_singletons  : no member-set of size 1
  min_size_2     : every member-set has size >= 2  (=> no empty, no singleton)
  full_in_F      : [n] is a member
  no_isolated    : every element appears in at least one member-set
  min_sets_size2 : every minimal (generator) set has size exactly 2
"""

from __future__ import annotations

import sys
from time import time

from enumerate import antichains, union_closure, frequencies


def set_size(a: int) -> int:
    return a.bit_count()


def full_mask(n: int) -> int:
    return (1 << n) - 1


def restriction_ok(family, antichain, n, kind):
    full = full_mask(n)
    if kind == "no_empty":
        return 0 not in family
    if kind == "no_singletons":
        return all(set_size(A) != 1 for A in family)
    if kind == "min_size_2":
        return all(set_size(A) >= 2 for A in family)
    if kind == "full_in_F":
        return full in family
    if kind == "no_isolated":
        d = frequencies(family, n)
        return all(v > 0 for v in d)
    if kind == "min_sets_size2":
        return all(set_size(M) == 2 for M in antichain)
    return True


def main() -> None:
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    kinds = ["all", "no_empty", "no_singletons", "min_size_2",
             "full_in_F", "no_isolated", "min_sets_size2"]
    t0 = time()
    for kind in kinds:
        total = 0
        best_ratio = 1.0
        best_example = None
        count_ok = 0
        for antichain in antichains(n):
            if not antichain:
                continue
            family = union_closure(antichain, n)
            if not restriction_ok(family, antichain, n, kind):
                continue
            total += 1
            m = len(family)
            d = frequencies(family, n)
            maxd = max(d)
            ratio = maxd / m
            if 2 * maxd >= m:
                count_ok += 1
            if ratio < best_ratio:
                best_ratio = ratio
                best_example = (antichain, family, d, m)
        dt = time() - t0
        print(f"n={n} restriction={kind:14s} families={total:5d} "
              f"all_ok={count_ok} min_ratio={best_ratio:.4f}")
        if best_example:
            ant, fam, d, m = best_example
            print(f"    extremal minSets={[format(a,f'0{n}b') for a in ant]} "
                  f"m={m} d(x)={d} max/m={max(d)/m:.4f}")
    print(f"Elapsed {time()-t0:.2f}s")


if __name__ == "__main__":
    main()
