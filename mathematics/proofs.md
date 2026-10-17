# Proofs

All arithmetic is exact integer arithmetic. Notation and definitions are in
`mathematics/definitions.md`.

---

## Notation recap

* $\mathcal F\subseteq\mathcal P([n])$, union-closed, $m=|\mathcal F|$.
* $d(x)=|\{A\in\mathcal F:x\in A\}|$, $M=\max_x d(x)$.
* $\mathcal F_x=\{A\in\mathcal F:x\in A\}$, $\mathcal F_{\bar x}=\{A\in\mathcal F:x\notin A\}$.
* For $S\subseteq[n]$:
  * $g(S)=|\{A\in\mathcal F:S\subseteq A\}|$ (sets containing $S$),
  * $h(S)=|\{A\in\mathcal F:A\cap S=\varnothing\}|$ (sets disjoint from $S$).

---

## Lemma 1 — Singleton case

> If $\{x\}\in\mathcal F$ then $d(x)\ge m/2$.

**Proof.** Define
$$\phi:\mathcal F_{\bar x}\longrightarrow\mathcal F_x,\qquad
\phi(B)=B\cup\{x\}.$$
Well-defined: for $B\in\mathcal F_{\bar x}$ we have $B\in\mathcal F$ and
$\{x\}\in\mathcal F$; since $\mathcal F$ is union-closed, $B\cup\{x\}\in\mathcal F$,
and $x\in B\cup\{x\}$, so $\phi(B)\in\mathcal F_x$.

Injective: if $\phi(B_1)=\phi(B_2)$ then $B_1\cup\{x\}=B_2\cup\{x\}$; since
$x\notin B_1,B_2$ (both are in $\mathcal F_{\bar x}$), removing $x$ gives
$B_1=B_2$.

Hence $|\mathcal F_x|\ge|\mathcal F_{\bar x}|$. But
$d(x)=|\mathcal F_x|$ and $m=|\mathcal F|=|\mathcal F_x|+|\mathcal F_{\bar x}|$
(the two subfamilies partition $\mathcal F$). Therefore
$$d(x)\ge m-d(x)\quad\Longleftrightarrow\quad 2d(x)\ge m
\quad\Longleftrightarrow\quad d(x)\ge \frac m2.$$
$\square$

**Consequence.** Any counterexample to Frankl's conjecture contains no
singleton member-set: if $\{x\}\in\mathcal F$ then $x$ is popular.

---

## Lemma 2 — Injection bound

> For every $S\in\mathcal F$,
> $$g(S)\ge h(S),$$
> i.e. $\bigl|\{A\in\mathcal F:S\subseteq A\}\bigr|
> \ge\bigl|\{A\in\mathcal F:A\cap S=\varnothing\}\bigr|.$

**Proof.** Define
$$\phi:\{B\in\mathcal F:B\cap S=\varnothing\}\longrightarrow
\{A\in\mathcal F:S\subseteq A\},\qquad
\phi(B)=B\cup S.$$
Well-defined: $B\in\mathcal F$ and $S\in\mathcal F$, union-closed gives
$B\cup S\in\mathcal F$, and $S\subseteq B\cup S$. Injective: if
$B_1\cup S=B_2\cup S$ then, since $B_1\cap S=B_2\cap S=\varnothing$,
intersecting with $[n]\setminus S$ recovers $B_1=B_2$. $\square$

---

## Corollary — Degree bound via the smallest member-set

> Let $k=\min\{|S|:\varnothing\ne S\in\mathcal F\}$ and $M=\max_x d(x)$.
> Then $M\ge m/(k+1)$.

**Proof.** Pick $S\in\mathcal F$ with $|S|=k$ (a smallest non-empty
member-set).
* Upper bound on $g(S)$: every set containing $S$ contains some $x\in S$, so
  $\{A:S\subseteq A\}\subseteq\bigcup_{x\in S}\{A:x\in A\}$, hence
  $g(S)\le\sum_{x\in S}d(x)\le kM$ (and also $g(S)\le d(x)$ for each
  $x\in S$, so $g(S)\le M$; we use the sharper $g(S)\le kM$ below).
* Lower bound on $h(S)$: the sets meeting $S$ are
  $\bigcup_{x\in S}\{A:x\in A\}$, whose size is at most
  $\sum_{x\in S}d(x)\le kM$. Therefore
  $$h(S)=m-\bigl|\{A:A\cap S\ne\varnothing\}\bigr|
       \ge m-kM.$$
* By Lemma 2, $g(S)\ge h(S)$. Using $g(S)\le kM$ is the wrong direction;
  instead use $g(S)\le \min_{x\in S}d(x)\le M$:
  $$M\ge g(S)\ge h(S)\ge m-kM,$$
  so $(k+1)M\ge m$, i.e. $M\ge m/(k+1)$. $\square$

**Consequences.**
* A counterexample has $k\ge2$ (no singletons by Lemma 1).
* If a counterexample has a 2-element member-set ($k=2$), then $M\ge m/3$.
* Average-set-size argument: $\sum_x d(x)=\sum_{A\in\mathcal F}|A|=m\bar s$,
  so $\max_x d(x)\ge m\bar s/n$. Hence if $\bar s\ge n/2$ then $M\ge m/2$.
  Thus a counterexample must also satisfy $\bar s<n/2$.

---

## Remarks on novelty

Lemma 1 and Lemma 2 are short, elementary arguments. They are very likely
present in some form in the existing literature on Frankl's conjecture; this
project presents them as self-contained, verified proofs rather than claiming
novelty for them. The genuine open difficulty is the jump from
$M\ge m/(k+1)$ (which is $<m/2$ whenever $k\ge2$) to the conjectured
$M\ge m/2$; the entropy-based literature reaches $c\approx0.3823455$ and is
provably sharp at that constant (Cambie 2025), so a genuinely new idea is
required to close the gap.
