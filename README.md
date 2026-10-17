# Union-Closed Sets Conjecture — Research Repository

**Subject:** Extremal set theory / combinatorics  
**Problem:** Frankl's Union-Closed Sets Conjecture (1979)  
**Account:** `rajveersinh-is-dev`  
**Default branch:** `main`

---

## The problem

A family $\mathcal F$ of finite sets is **union-closed** if $A,B\in\mathcal F \Rightarrow A\cup B\in\mathcal F$.

> **Conjecture (P. Frankl, 1979).** For every finite union-closed family $\mathcal F\neq\{\varnothing\}$ there is an element $x$ contained in at least half of the member-sets:
> $$\max_{x}\frac{|\{A\in\mathcal F:x\in A\}|}{|\mathcal F|}\;\ge\;\frac12.$$

Equivalently, some element has frequency (degree) at least $1/2$. The only exception is the family consisting solely of the empty set.

This is one of the best-known open problems in extremal set theory. Its statement is elementary, yet it has resisted standard combinatorial techniques for over 40 years.

---

## What was established here

**Target:** Frankl's Union-Closed Sets Conjecture (1979) — **CONFIRMED OPEN** (best general bound $c\approx 0.3823455$; full conjecture unresolved).

| Item | Status |
|------|--------|
| Problem statement formalized | `mathematics/definitions.md` |
| Literature review / known results | `research/literature_review.md` |
| Strongest proved result | $M\ge m/(k+1)$ (Corollary), singleton case $\Rightarrow$ popular (Lemma 1) |
| Computational verification | Exact enumeration for $n\le 5$ (`src/enumerate.py`) |
| Formal (proof-assistant) verification | none |

### Rigorous results (PROVED HERE)

1. **Singleton case:** if $\{x\}\in\cF$ then $x$ is popular ($d(x)\ge m/2$).
2. **Injection bound:** for every $S\in\cF$, $|\{A:S\subseteq A\}|\ge|\{A:A\cap S=\varnothing\}|$.
3. **2-element case:** if $\cF$ contains $\{a,b\}$ of size 2, then $\max\{d(a),d(b)\}\ge m/2$ — Frankl's conjecture holds for such families.
4. **Degree bound:** $M=\max_x d(x)\ge m/(k+1)$ where $k$ is the smallest non-empty member-set size.

**Structural reduction:** Results 1 and 3 show that any counterexample must have $k\ge3$ (all non-empty member-sets have size at least 3). For $k\ge3$, Result 4 gives $M\ge m/(k+1)\le m/4<m/2$ — this is the precise open gap.

**No theorem resolving Frankl's conjecture is claimed.** The full conjecture ($M\ge m/2$ for all union-closed families) remains open; the gap from $m/(k+1)$ (which is $\le m/4$ whenever $k\ge3$) to $m/2$ is precisely the open difficulty. The entropy-based literature is provably sharp at $c\approx 0.3823455$ (Cambie 2025), so a new method is needed.

Any result labelled `PROVED HERE` is accompanied by a complete proof in `mathematics/proofs.md`. Conjectures and computations are never presented as theorems.

---

## Why the problem matters

* It is a natural extremal statement about finite set systems with a simple union-closure axiom.
* It has a precise quantitative gap: the conjecture asserts frequency $\ge 1/2$, while the best unconditional general lower bound is a constant $c\approx 0.382$ (Sawin 2022; refinements Liu 2023; Lu–Raz 2024).
* It is verified for families on at most 12 ground elements (Zivković–Vučković), but the general case remains open.
* Progress requires structural insight rather than large-scale computation, which matches this project's methodology.

---

## Existing results (strongest known)

* **Gilmer (2022):** first *constant* lower bound via an information-theoretic (entropy) approach.
* **Sawin (2022, arXiv:2212.12500):** improved the bound to $c=(3-\sqrt5)/2\approx 0.381966$ using dependent sampling + entropy.
* **Liu (2023, arXiv:2306.08824):** further refinement via conditionally-IID coupling.
* **Lu–Raz (2024, arXiv:2405.10639):** connection to Reimer's average-set-size theorem.
* **Zivković–Vučković:** conjecture verified for all union-closed families on $\le 12$ elements.
* The conjecture is known for several restricted classes (families with a set of size $\le 2$, separating families, etc.).

The **gap**: close $c\approx 0.382$ up to $1/2$, or prove the conjecture for a new broad class of families.

---

## Repository map

```
README.md            this file
LICENSE              MIT license
.gitignore           ignore rules
research/
  problem_selection.md   why this problem, open-status check, candidate pool
  literature_review.md   verified sources and strongest known results
  known_results.md       statements of established theorems with citations
  proof_attempts.md      documented attack strategies and audits
  research_log.md        dated log of decisions, dead ends, strategy changes
mathematics/
  definitions.md       formal definitions and notation
  main_results.md      theorem statements (labelled PROVED HERE / CONJECTURED / ...)
  proofs.md            complete proofs
paper/
  main.tex             LaTeX paper
  references.bib       bibliography
src/                 small exact-arithmetic helper scripts
tests/               automated tests for definitions/invariants
experiments/         finite-domain computational checks
results/             experiment outputs
docs/
  reproducibility.md   versions, seeds, commands, how to reproduce
CHANGELOG.md         project milestones
```

---

## Dependencies

* Python 3.14+ (standard library only) for the exact-enumeration helpers.
* No proprietary software required. All computations use exact integer arithmetic.

---

## Reproducibility

Run the exact-enumeration helpers in `src/` (see `docs/reproducibility.md`). Every experiment states its finite domain explicitly; finite enumeration is never claimed to prove a universal statement.

---

## Limitations

This is an independent research project. The results herein are **not** peer-reviewed and are not claimed to be published. A conjecture is never advertised as a theorem, and a finite computation is never advertised as a general solution.

---

## Citations

See `paper/references.bib` and `research/literature_review.md`.

---

## License

MIT License. See `LICENSE`.