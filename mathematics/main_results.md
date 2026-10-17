# Main Results

This project studies Frankl's Union-Closed Sets Conjecture (1979), which remains
**open** (confirmed via multiple current sources; best unconditional general
bound $c\approx 0.3823455$, Cambie 2025, and the entropy approach is provably
exhausted at that constant).

Below are the rigorous results established in this project.

---

## Result 1 — Singleton case (PROVED HERE)

If a union-closed family $\mathcal F$ contains a singleton $\{x\}$, then $x$ is
popular:
$$\{x\}\in\mathcal F \;\Longrightarrow\; d(x)\ge \frac{|\mathcal F|}{2}.$$

Proof: `mathematics/proofs.md`, Lemma 1.

---

## Result 2 — Injection bound (PROVED HERE)

For every member-set $S\in\mathcal F$,
$$\bigl|\{A\in\mathcal F:S\subseteq A\}\bigr|
\;\ge\;
\bigl|\{A\in\mathcal F:A\cap S=\varnothing\}\bigr|.$$

Proof: `mathematics/proofs.md`, Lemma 2 (an explicit injection
$B\mapsto B\cup S$).

---

## Result 3 — The 2-element case (PROVED HERE)

If $\mathcal F$ is union-closed and contains a member-set $\{a,b\}$ of size
exactly 2, then $\max\{d(a),d(b)\}\ge m/2$ where $m=|\mathcal F|$. Equivalently,
Frankl's conjecture holds for every union-closed family with a 2-element
member-set.

Proof: `mathematics/proofs.md`, Theorem (2-element case). The proof partitions
$\mathcal F$ by which elements of $\{a,b\}$ each set contains and applies
Lemma 2.

---

## Result 4 — Degree bound in terms of the smallest member-set (PROVED HERE)

Let $k=\min\{|S|:\varnothing\ne S\in\mathcal F\}$ and $M=\max_x d(x)$. Then
$$M\;\ge\;\frac{m}{k+1},\qquad m:=|\mathcal F|.$$

Proof: `mathematics/proofs.md`, Corollary.

---

## Consequences (PROVED HERE)

1. **Reduction to $k\ge3$.** Any counterexample to Frankl's conjecture must
   have no singletons (Result 1) and no 2-element member-sets (Result 3), so
   $k\ge3$: every non-empty member-set has size at least $3$. The conjecture is
   thereby reduced to this case.
2. For $k\ge3$, Result 4 gives $M\ge m/(k+1)\le m/4<m/2$ — well short of the
   conjectured $m/2$. This is the precise open gap.
3. Average-set-size argument: if the average member-set size $\bar s\ge n/2$
   then some element is popular. So a counterexample must satisfy
   $\bar s<n/2$ **and** $M<m/2$ **and** $k\ge3$.

---

## What remains open (UNRESOLVED)

* The full conjecture ($M\ge m/2$ for all union-closed $\mathcal F\ne\{\varnothing\}$).
* Closing the gap between the best general bound $c\approx 0.3823455$ and $1/2$.
* The conjecture for families whose smallest non-empty member-set has size
  $k\ge3$ (Result 4 only gives $M\ge m/(k+1)\le m/4$ there).

---

## Evidence labels

* `PROVED HERE` = complete proof included in `mathematics/proofs.md`.
* `ESTABLISHED IN PRIOR WORK` = cited from the literature (best bound,
  finite verification to $n=12$, entropy-exhaustion sharpness).
* `COMPUTATIONALLY VERIFIED` = exact enumeration for $n\le 5$
  (`src/enumerate.py`); finite domain only, not a general proof.
* `UNRESOLVED` = the full conjecture and the gap to $1/2$.
