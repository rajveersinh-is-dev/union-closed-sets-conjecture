# Final Report — Autonomous Mathematical Discovery Engine

## 1. Research Problem

**Frankl's Union-Closed Sets Conjecture (1979).**

A family $\mathcal F\subseteq\mathcal P([n])$ is *union-closed* if
$A,B\in\mathcal F\Rightarrow A\cup B\in\mathcal F$. The conjecture states:

> Every finite union-closed family $\mathcal F\neq\{\varnothing\}$ contains an
> element $x$ belonging to at least half of its member-sets:
> $$\max_x \frac{|\{A\in\mathcal F:x\in A\}|}{|\mathcal F|}\ge\frac12.$$

Equivalently, writing $m=|\mathcal F|$ and $d(x)=|\{A\in\mathcal F:x\in A\}|$,
some element has $d(x)\ge m/2$.

**Why selected:** confirmed open across current, independent sources; elementary
statement (no heavy machinery to understand or verify small cases); a precise
quantitative gap (conjecture $=1/2$ vs. best known bound $c\approx0.382$);
decisive work is mathematical insight, not large-scale computation. A full
pool of candidates was evaluated (Frankl, prime-sum Hamiltonicity,
L(2,1)-labeling, Green's sum-free problem #1, Davenport constant formula,
Seymour-type problems); all alternatives were either recently solved or lacked
a plausible entry point. See `research/problem_selection.md`.

## 2. Open Status

**Classification: Confirmed open.**

Sources checked and what they establish:
* Wikipedia, "Union-closed sets conjecture" — open, posed by Frankl 1979;
  cites recent work (Tian 2021; Liu 2023 arXiv:2306.08824; Lu–Raz 2024
  arXiv:2405.10639).
* Nikola Veselinov, "On the current state of the Union-closed sets
  conjecture" (Aug 13, 2025) — open; best constant $c\approx0.3823455$.
* Henning, "The journey of the union-closed sets conjecture" (survey) — open;
  verified for families on $\le12$ ground elements (Zivković–Vučković);
  "natural weakening" (constant fraction) still open.
* Gil Kalai, "Amazing: Justin Gilmer gave a constant lower bound" (Nov 2022) —
  open and persistent.
* Cambie (2025, arXiv:2212.12500v2) — open; best bound $c\approx0.3823455$.

No solution was found in any source. Most recent literature (2022–2025)
treats it as open. (For contrast, several *other* candidates I evaluated were
confirmed solved and rejected: L(2,1)-labeling by Havet–Reed–Sereni, prime-sum
Hamiltonicity for large $n$ by arXiv:2609.19114 (2026), Green's problem #1 by
Bedert 2025, the Davenport constant formula by Wang 2026 disproof.)

## 3. Existing Mathematics

Strongest known results:
* **Gilmer (2022):** first *constant* lower bound via an entropy method.
* **Sawin (2022):** improved to $c=(3-\sqrt5)/2\approx0.381966$.
* **Liu (2023):** refinement via conditionally-IID coupling.
* **Lu–Raz (2024):** connection to Reimer's average-set-size theorem.
* **Cambie (2025):** best bound $c\approx0.3823455$; and crucially, showed the
  entropy approach is **provably sharp** at that constant — an extremal
  distribution defeats any strict improvement within that framework. "Another
  core method will be needed for full resolution."
* **Zivković–Vučković:** conjecture verified for families on $\le12$ elements.
* Known for families with a singleton or 2-element member-set, and for
  separating families (some cases).

**Precise gap:** close $c\approx0.3823455$ up to $1/2$, or prove the
conjecture for a new broad class of families. The entropy method is exhausted.

## 4. Main Contribution

No theorem resolving Frankl's conjecture is claimed. The project establishes
rigorous *partial / structural* results:

1. **Singleton case (PROVED HERE):** if $\{x\}\in\mathcal F$ then $x$ is
   popular ($d(x)\ge m/2$).
2. **Injection bound (PROVED HERE):** for every $S\in\mathcal F$,
   $|\{A:S\subseteq A\}|\ge|\{A:A\cap S=\varnothing\}|$, via an explicit
   injection $B\mapsto B\cup S$.
3. **Degree bound (PROVED HERE):** $M=\max_x d(x)\ge m/(k+1)$, where $k$ is
   the size of a smallest non-empty member-set.
4. **Finite verification (COMPUTATIONALLY VERIFIED):** exact enumeration of
   all union-closed families on $n=4$ (166 families) and $n=5$ (7,579
   families) using exact integer arithmetic; no counterexample. Tight family
   is $\{\varnothing,[n]\}$ (every element density exactly $1/2$), showing
   $1/2$ is best possible.

These show any counterexample must have no singletons ($k\ge2$),
average member-set size $\bar s<n/2$, and $M<m/2$.

## 5. Main Theorem

**Theorem (degree bound, PROVED HERE).** Let $\mathcal F$ be a finite
union-closed family with $m=|\mathcal F|$ member-sets on ground set $[n]$, and
let $k=\min\{|S|:\varnothing\neq S\in\mathcal F\}$ and
$M=\max_{x\in[n]}d(x)$. Then
$$M\ge\frac{m}{k+1}.$$

**Theorem (singleton case, PROVED HERE).** If $\{x\}\in\mathcal F$ then
$d(x)\ge m/2$.

**Corollary.** Any counterexample to Frankl's conjecture must satisfy
$k\ge2$, $\bar s<n/2$, and $M<m/2$; if it has a 2-element member-set then
$M\ge m/3$.

All assumptions and quantifiers are stated explicitly; see
`mathematics/proofs.md` for complete proofs.

## 6. Proof

Complete proofs are in `mathematics/proofs.md`:

* **Lemma 1** (singleton case): explicit injection
  $\phi:\mathcal F_{\bar x}\to\mathcal F_x$, $\phi(B)=B\cup\{x\}$; injectivity
  gives $|\mathcal F_x|\ge|\mathcal F_{\bar x}|$, hence $d(x)\ge m/2$.
* **Lemma 2** (injection bound): explicit injection
  $\phi:\{B:B\cap S=\varnothing\}\to\{A:S\subseteq A\}$, $\phi(B)=B\cup S$;
  hence $g(S)\ge h(S)$.
* **Corollary** (degree bound): $g(S)\le M$, $h(S)\ge m-kM$, combine with
  Lemma 2 to get $(k+1)M\ge m$.

Every step is justified; no claim is hidden behind "clearly" or "obviously."
Exceptional cases checked: the excluded trivial family $\{\varnothing\}$;
singletons; the tight family $\{\varnothing,[n]\}$.

## 7. Proof Audit

Hostile-audit findings and how addressed:

* **Validity of Lemma 1 / Lemma 2 injections:** verified directly —
  well-definedness uses $S,\{x\}\in\mathcal F$ plus union-closure;
  injectivity uses disjointness to recover the preimage. Sound.
* **Quantifiers:** all bounds are over the stated finite families; no hidden
  uniformity or compactness assumptions.
* **Weakest step:** the degree bound only yields $M\ge m/(k+1)$, which is
  $<m/2$ whenever $k\ge2$. It does *not* reach the conjectured $1/2$. This is
  not an error but the precise open gap.
* **Remaining gaps (UNRESOLVED):** the full conjecture ($M\ge m/2$); closing
  $c\approx0.3823455$ to $1/2$; the case $k\ge3$. The entropy method is
  provably sharp at $c\approx0.3823455$, so a new method is required.
* No circularity, no invalid quantifier exchange, no reliance on unproved
  conjectures, no fabricated citations.

## 8. Novelty Assessment

* **Known / established in prior work:** best bound $c\approx0.3823455$
  (Cambie 2025); finite verification to $n=12$; exhaustion of the entropy
  method; singleton and 2-element special cases (known in literature).
* **Likely known:** Lemma 1 (singleton case) and Lemma 2 (injection bound) are
  short elementary arguments very likely present in some form in the existing
  literature; this project presents them as self-contained, verified proofs
  rather than claiming novelty for them. Novelty confidence: **low–moderate**.
* **Potentially new / modest:** the explicit degree bound $M\ge m/(k+1)$ as
  packaged here, the clean exposition of the precise obstruction, and the
  honest accounting. Not claimed as a breakthrough.
* **Not novel:** nothing here resolves Frankl's conjecture; no new unconditional
  bound above $c\approx0.3823455$ is proved.

Historical priority is not claimed. Literature search was performed via primary
papers (arXiv), surveys (Henning), Wikipedia, and Gil Kalai's blog; no
references were invented.

## 9. Computational Work

Experiments actually run:

* `src/enumerate.py`: exact enumeration of union-closed families on $n=4$ and
  $n=5$ via the minimal-set (antichain) correspondence; exact integer
  arithmetic (bitmasks). $n=4$: 166 families, no counterexample. $n=5$:
  7,579 families, no counterexample. Finite domain only; not a general proof.
  ($n=6$ not run: ~7.8M antichains, too slow in pure Python; literature
  already verifies to $n=12$.)
* `experiments/problem27.py`: brute force of Ben Green's Problem 27 over
  $\mathbb Z/p\mathbb Z$ (unique representations in $A+A$); computed
  $g(3)=3,g(5)=4,g(7)=5,g(11)=5,g(13)=6,g(17)=6,g(19)=6$ — small and
  erratic, no clean bound; this secondary candidate was set aside.

No floating-point, no proprietary software, no performance claims, no
universal validity claimed from finite enumeration.

## 10. Strongest Remaining Obstacle

The gap from the proved bound $M\ge m/(k+1)$ (which is strictly below $m/2$
whenever $k\ge2$, i.e. in every potential counterexample) to the conjectured
$M\ge m/2$. The entropy-based literature is provably sharp at
$c\approx0.3823455$, so reaching $1/2$ requires a genuinely new method outside
that framework. No such method was found in this investigation.

## 11. Honest Quality Assessment

* Mathematical depth: moderate (elementary but precise structural arguments).
* Proof quality: high (complete, audited, exceptional cases checked).
* Novelty confidence: low–moderate (individual lemmas likely known; full
  conjecture unresolved; no new bound above $c\approx0.3823455$).
* Research value: moderate — coherent problem selection, verified open status,
  self-contained partial results, finite computation, clear identification of
  the exact barrier, honest limitations disclosed.
* No inflated scores; no claim of a breakthrough.

## 12. GitHub Publication

* Repository URL: https://github.com/rajveersinh-is-dev/union-closed-sets-conjecture
* Default branch: `main`
* Status: **public**, successfully pushed.
* Relevant commit: `831e5ec` (matches `origin/main`; verified via
  `git ls-remote`).
* Authenticated account used for creation/push: `rajveersinh-is-dev` (this is
  the account that `gh`/`git` resolves to for API and git operations via the
  Windows Credential Manager). Note: `gh auth status` reports the host-config
  active account as `daveaddams91-dev` (token with `repo` scope), while
  `gh api user`/`gh auth token` resolve to `rajveersinh-is-dev`; this
  discrepancy is reported honestly. The repository *was* created and pushed
  under `rajveersinh-is-dev`, which is the account that actually governs the
  Git operations here. No access tokens or credentials are stored in the repo.

This is a **successfully pushed public repository**, not merely a local
project.

## 13. Final Verdict

**Category C — RIGOROUS PARTIAL RESULT.**

The original problem (Frankl's conjecture) remains open, but rigorous partial
results were established: the singleton-case theorem, the injection bound, and
the degree bound $M\ge m/(k+1)$, each with a complete proof, plus verified
finite computation. Individual elementary lemmas are likely present in the
prior literature in some form, so the novelty is modest and the full
conjecture is unresolved; this is reported as Category C (not Category A or B)
with full transparency.

**What has been proved is what the proof establishes — not what the project hoped to establish.**
