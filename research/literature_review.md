# Literature Review — Frankl's Union-Closed Sets Conjecture

## Problem (original formulation, Frankl 1979)

Let $\mathcal F\subseteq\mathcal P([n])$ be finite and union-closed ($A,B\in\mathcal F\Rightarrow A\cup B\in\mathcal F$), with $\mathcal F\neq\{\varnothing\}$. Conjecture: some $x\in[n]$ has frequency $\tilde d_x:=|\{A\in\mathcal F:x\in A\}|/|\mathcal F|\ge 1/2$.

## Strongest known results (verified from sources)

| Result | Source | Status |
|--------|--------|--------|
| Conjecture posed | Frankl (1979) | OPEN |
| First constant lower bound ($\ge 0.01$) | Gilmer (2022) | ESTABLISHED |
| Lower bound $c=(3-\sqrt5)/2\approx0.381966$ | Sawin (2022), arXiv:2212.12500 | ESTABLISHED |
| Refinement via conditionally-IID coupling | Liu (2023), arXiv:2306.08824 | ESTABLISHED |
| Connection to Reimer's average-set-size theorem | Lu–Raz (2024), arXiv:2405.10639 | ESTABLISHED |
| Verified for $n\le 12$ ground elements | Zivković–Vučković | ESTABLISHED (computation + local configurations) |
| Minimal counterexample must have $n\le 4m-1$ ($m=|\mathcal F|$) | Lo Faro | ESTABLISHED |
| Known for families with a member-set of size $\le 2$ | literature | ESTABLISHED |

Best general lower bound: $c\approx 0.3823455$ (Cambie 2025, arXiv:2212.12500v2, improving on $(3-\sqrt5)/2\approx0.381966$). Gap to $1/2$ remains.

Important: the entropy approach (Gilmer 2022; Sawin; Liu 2023; Cambie 2025) is provably sharp at $c\approx0.3823455$ — Cambie Section 2.3 exhibits a distribution showing no strict improvement is possible with the Sawin linear-combination idea. "Another core method will be needed for the full resolution" (Cambie 2025).

## Main techniques in the literature

* Entropy / information-theoretic method (Gilmer; Sawin's dependent sampling).
 * Reimer's average-set-size theorem.
* Local-configuration / reduction to small cases (Zivković–Vučković; Lo Faro).
* Induction on the number of sets / elements.

## Known special cases (conjecture verified)

* Families with a singleton member-set.
* Families with a 2-element member-set.
* Separating families (under conditions).
* Families on $\le 12$ elements.

## Unresolved cases

* General families on $n\ge 13$ elements.
* Improving the constant $c$ above $\approx0.382$ toward $1/2$.
* The "natural weakening": guarantee an element of constant positive frequency (already known) vs. $1/2$.

## What remains (the precise gap)

Close the gap between the best lower bound $c\approx 0.382$ and the conjectured $1/2$, or prove the conjecture for a new broad class of families. No approach has yet closed this gap.

## Sources consulted

* Wikipedia, "Union-closed sets conjecture."
* Nikola Veselinov, "On the current state of the Union-closed sets conjecture," Aug 2025.
* Henning, "The journey of the union-closed sets conjecture," survey (uni-ulm.de).
* Gil Kalai, "Amazing: Justin Gilmer gave a constant lower bound," Combinatorics and more, Nov 2022.
* Gilmer (2022); Sawin arXiv:2212.12500; Liu arXiv:2306.08824; Lu–Raz arXiv:2405.10639.
* Zivković–Vučković ($n\le 12$); Lo Faro (minimal counterexample bound).
