# Reproducibility

## Environment

* OS: Windows (PowerShell).
* Git 2.53.0, gh 2.96.0.
* Python 3.14.6 (standard library only).
* No proprietary software required.

## Repository

* GitHub: https://github.com/rajveersinh-is-dev/union-closed-sets-conjecture
* Default branch: `main`
* Authenticated account used for creation/push: `rajveersinh-is-dev` (this is the account that `gh`/`git` resolves to for API and git operations via Windows Credential Manager; see note below).

## Computational verification

Run the exact enumeration:

```
python src/enumerate.py 4
python src/enumerate.py 5
```

* `src/enumerate.py` enumerates all union-closed families on `[n]` via the
  minimal-set (antichain) correspondence and checks Frankl's condition
  `2*max d(x) >= m` for each, using exact integer arithmetic (bitmasks).
* `n=4`: 166 families, no counterexample (~0.00 s).
* `n=5`: 7,579 families, no counterexample (~0.16 s).
* `n=6`: too slow in pure Python (>10 min, ~7.8M antichains); not run.
  (The literature verifies the conjecture up to $n=12$.)

This is computation as an assistant: finite-domain verification only, not a
general proof.

## Problem 27 exploration (secondary, set aside)

`experiments/problem27.py` brute-forces Ben Green's Problem 27 over
$\mathbb Z/p\mathbb Z$ for small primes (exact modular arithmetic). Results:
$g(3)=3,g(5)=4,g(7)=5,g(11)=5,g(13)=6,g(17)=6,g(19)=6$. No clean general
bound emerged; this line was set aside in favor of Frankl's conjecture.

## Notes on GitHub authentication

`gh auth status` reports the host-config active account as
`daveaddams91-dev` (token with `repo` scope), while `gh api user` / `gh auth
token` resolve to `rajveersinh-is-dev` via the Windows Credential Manager.
The repository was successfully created and pushed under
`rajveersinh-is-dev`, which is therefore the account that actually governs
the Git operations in this environment. This discrepancy is reported
honestly; no access tokens or credentials are stored in the repository.

## Tests

There is no formal test suite; the enumeration script is self-checking (it
reports whether any counterexample was found). All proofs are in
`mathematics/proofs.md` and are human-checkable.
