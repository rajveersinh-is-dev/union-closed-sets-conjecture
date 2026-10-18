"""
Brute-force computation of g(p) for Ben Green's Problem 27.

g(p) = min |A| such that A subset Z/pZ, |A|>=2, and every s in A+A
has r_A(s) != 1, where r_A(s) = #{(a,b) in A^2 : a+b = s} (ordered pairs,
doubles count once).

Computation is exact integer arithmetic over Z/pZ.  Results are
COMPUTATIONALLY VERIFIED on finite domains only; they suggest conjectures
but prove nothing for general p.
"""

from __future__ import annotations

import itertools
import sys



def is_prime(n: int) -> bool:
    """Is prime.
    
    Args:
        n:
    
    Returns:
        bool: Result of type bool
    
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primes_upto(limit: int) -> list[int]:
    """Primes upto.
    
    Args:
        limit:
    
    Returns:
        The computed result
    
    """
    return [n for n in range(2, limit + 1) if is_prime(n)]


def ok(A: tuple[int, ...], p: int) -> bool:
    """Return True iff every sum s in A+A has r_A(s) != 1."""
    S = set(A)
    # count representations of each sum
    counts: dict[int, int] = {}
    for a in S:
        for b in S:
            s = (a + b) % p
            counts[s] = counts.get(s, 0) + 1
    return all(v != 1 for v in counts.values())


def g(p: int, max_size: int | None = None) -> int | None:
    """Brute-force g(p): try subsets by increasing size."""
    if max_size is None:
        max_size = p
    elems = list(range(p))
    for k in range(2, max_size + 1):
        for A in itertools.combinations(elems, k):
            if ok(A, p):
                return k
    return None


def extremal_sets(p: int, k: int, limit: int = 10) -> list[tuple[int, ...]]:
    """Return up to `limit` extremal sets of size k satisfying the condition."""
    out = []
    for A in itertools.combinations(range(p), k):
        if ok(A, p):
            out.append(A)
            if len(out) >= limit:
                break
    return out


def main() -> None:
    """Entry point — parse arguments and run the main computation.
    
    """
    args = sys.argv[1:]
    limit = int(args[0]) if args else 13
    print("p   g(p)   example extremal set (size g(p))")
    print("-" * 55)
    for p in primes_upto(limit):
        if p == 2:
            print(f"{p}   N/A (p=2 trivial/degenerate)")
            continue
        val = g(p)
        ex = extremal_sets(p, val) if val else []
        print(f"{p}   {val}    {ex[0] if ex else '-'}")
        if val and len(ex) > 1:
            print(f"         (and {len(ex)-1} more)")


if __name__ == "__main__":
    main()
