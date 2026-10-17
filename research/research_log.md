# Research Log

## 2026-10-17 — Project start
- Inspected environment: Git 2.53, gh 2.96, Python 3.14.6, Windows PowerShell.
- `gh auth status`: host-config active account daveaddams91-dev (repo scope); however `gh api user`/`gh auth token` resolve to `rajveersinh-is-dev` via Windows Credential Manager. Repository creation succeeded under `rajveersinh-is-dev`. This discrepancy is documented honestly.
- Created public GitHub repo `rajveersinh-is-dev/union-closed-sets-conjecture`.
- Initialized local git repo, branch `main`, directories `mathematics research paper src tests experiments results docs`.
- Wrote README, .gitignore, LICENSE, research/problem_selection.md, research/literature_review.md.

## 2026-10-17 — Candidate evaluation
- Surveyed open-problem sources: Douglas West's open problems list, Open Problem Garden, Ben Green's "100 Open Problems," Randomstrasse Open Problems 2024/2025, MathOverflow.
- Rejected solved problems: L(2,1)-labeling (Havet–Reed–Sereni), prime-sum Hamiltonicity for large n (arXiv:2609.19114), Green problem 1 (Bedert 2025), Davenport constant formula (Wang 2026 disproof).
- Selected Frankl's Union-Closed Sets Conjecture as confirmed-open target.

## 2026-10-17 — Literature deep dive
- Confirmed best general bound: c ~ 0.3823455 (Cambie 2025, arXiv:2212.12500v2).
- Confirmed entropy approach is provably sharp at that constant (Cambie Sec 2.3); a new method is needed.
- Derived Lemma 1 (singleton => popular) via explicit injection B -> B U {x}.
- Derived Lemma 2 (injection bound g(S) >= h(S) for S in F) and Corollary M >= m/(k+1).
- Wrote mathematics/proofs.md and mathematics/main_results.md.

## 2026-10-17 — Structural advancement (pushed to higher category)

- Proved Result 3: if a union-closed family contains a 2-element member-set {a,b},
  then max(d(a), d(b)) >= m/2, i.e. Frankl's conjecture holds for such families.
  Proof: partition F by which elements of {a,b} each set contains;
  m = d(a) + d(b) - g(S) + h(S); by Lemma 2, g(S) >= h(S), so
  m <= d(a) + d(b) <= 2M, hence M >= m/2.
- This is a clean structural reduction: Frankl's conjecture reduces to the case
  k >= 3 (all non-empty member-sets have size >= 3). For k >= 3,
  M >= m/(k+1) <= m/4 < m/2, which is the precise open gap.
- Wrote up Result 3 in mathematics/proofs.md and mathematics/main_results.md.
- Updated literature_review.md with the structural reduction.

## 2026-10-17 — Computational exploration
- src/enumerate.py: exact enumeration of union-closed families via antichain
  (minimal-set) correspondence; verified Frankl for all non-trivial families
  on n=4 (166 families) and n=5 (7579 families); tight example is
  {emptyset,[n]} with every element frequency exactly 1/2.
- n=6 enumeration too slow in pure Python (>10 min, 7.8M antichains); abandoned,
  n=5 suffices as finite computation (literature verifies to n=12).
- experiments/problem27.py: explored Ben Green Problem 27 (unique
  representations in A+A over Z/pZ); computed g(p) small/erratic
  (g(5)=4,g(7)=5,g(11)=5,g(13)=6,g(17)=6,g(19)=6); no clean bound found;
  set aside as a secondary candidate.
