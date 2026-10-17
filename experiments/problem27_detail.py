"""
Detailed exploration of Problem 27: compute g(p) and structure of extremal
sets for small primes.  Exact integer arithmetic; finite-domain computation.
"""

from __future__ import annotations

import sys
from typing import List

from problem27 import is_prime, primes_upto, ok, g, extremal_sets


def primes_upto2(limit: int) -> List[int]:
    """Return a list of all prime numbers <= limit using trial division.

    This function mirrors the behavior of the original implementation
    and is kept for compatibility with the existing script.
    """
    return [n for n in range(2, limit + 1) if is_prime(n)]


def main() -> None:
    """Entry point for the script.

    Reads an optional integer limit from the command line (default 19)
    and prints a table of primes p, g(p), the number of extremal sets
    (showing only the count), and the first few extremal set examples.
    """
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
