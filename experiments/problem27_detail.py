"""
Detailed exploration of Problem 27: compute g(p) and structure of extremal
sets for small primes.  Exact integer arithmetic; finite-domain computation.
"""

from __future__ import annotations

import itertools
import sys

from problem27 import is_prime, primes_upto, ok, g, extremal_sets


def primes_upto2(limit):
    return [n for n in range(2, limit + 1) if is_prime(n)]


def gaps(A):
    """Sorted circular gaps of subset A of Z/pZ (need p passed)."""
    return None


def main() -> None:
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 19
    print("p  g(p)  num_extremal(showing first few)  examples")
    print("-" * 70)
    for p in primes_upto2(limit):
        if p == 2:
            continue
        val = g(p)
        ex = extremal_sets(p, val, limit=6)
        print(f"{p:2d}  {val:2d}   {len(ex)} shown   {ex[:4]}")


if __name__ == "__main__":
    main()
