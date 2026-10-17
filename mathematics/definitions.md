# Formal Definitions and Notation

## Ground set and families

Let $[n] = \{1,2,\dots,n\}$. Let $\mathcal P([n])$ be the power set.

A **family** (set system) is $\mathcal F\subseteq\mathcal P([n])$, a finite collection of subsets of $[n]$. We write $m := |\mathcal F|$ for the number of member-sets.

## Union-closed

$\mathcal F$ is **union-closed** if
$$A,B\in\mathcal F \;\Longrightarrow\; A\cup B\in\mathcal F.$$

The empty family $\mathcal F=\varnothing$ and $\mathcal F=\{\varnothing\}$ are trivially union-closed; Frankl's conjecture excludes $\mathcal F=\{\varnothing\}$ (the empty set is in every member-set vacuously, but there is no element with frequency $\ge 1/2$ since there are no elements). We assume $\mathcal F\neq\{\varnothing\}$.

## Frequency / degree

For $x\in[n]$, the **frequency** (degree) of $x$ is
$$d(x) := |\{A\in\mathcal F : x\in A\}|,\qquad
\tilde d(x) := \frac{d(x)}{m}\in[0,1].$$

An element is **popular** (or **abundant**) if $\tilde d(x)\ge 1/2$.

## Frankl's Union-Closed Sets Conjecture (1979)

> Every finite union-closed family $\mathcal F\neq\{\varnothing\}$ has a popular element:
> $$\max_{x\in[n]}\tilde d(x)\;\ge\;\frac12.$$

Equivalently: $\max_x d(x)\ge m/2$.

## Equivalent reformulations used in the literature

**Average-set-size form.** Since
$$\sum_{x\in[n]} d(x) = \sum_{A\in\mathcal F}|A|,$$
the average frequency is $\bar d = \frac{1}{n}\cdot\frac{1}{m}\sum_{A\in\mathcal F}|A| = \frac{\bar s}{n}$ where $\bar s$ is the average member-set size. Hence:
- If $\bar s\ge n/2$ then $\bar d\ge 1/2$, so some $x$ has $d(x)\ge m/2$. **Done.**
- The hard case is $\bar s < n/2$: member-sets are on average small, yet some element must still appear in at least half the sets.

**Complement/density form.** Let $\mathcal F_{\ge k}=\{A\in\mathcal F:|A|\ge k\}$. Various papers bound $|\mathcal F_{\ge k}|$ in terms of frequencies.

## Subfamilies $\mathcal F_x$

For each $x$, $\mathcal F_x := \{A\in\mathcal F:x\in A\}$ is itself union-closed: if $A,B\in\mathcal F_x$ then $A\cup B\in\mathcal F$ and $x\in A\cup B$, so $A\cup B\in\mathcal F_x$. This self-similarity is used in inductive arguments.

## Minimal sets

Let $\operatorname{Min}(\mathcal F)$ be the inclusion-minimal non-empty member-sets. Every member-set is a union of minimal sets, so $\mathcal F$ is determined (up to duplicate unions) by its minimal sets. If $|\operatorname{Min}(\mathcal F)|=k$ then $m\le 2^k$ (counting $\varnothing$).

## Known special cases (conjecture verified)

* Families containing a singleton $\{a\}$: then $a$ is popular (standard result).
* Families containing a 2-element set: verified (standard).
* Families on $\le 12$ ground elements: verified (Zivković–Vučković), via local-configuration reduction + computation.

## Best known unconditional bound

The conjecture asserts $\max_x\tilde d(x)\ge 1/2$. The best general lower bound is a constant
$$c \approx 0.382 \quad\text{(Sawin 2022, arXiv:2212.12500; refinements Liu 2023; Lu–Raz 2024).}$$
Gilmer (2022) obtained the first constant bound via an entropy argument.

**The gap:** raise $c\approx 0.382$ to $1/2$, or prove the conjecture for a new broad class of families.

## Evidence labels used in this project

Every claim carries one of: `PROVED HERE`, `ESTABLISHED IN PRIOR WORK`, `COMPUTATIONALLY VERIFIED`, `CONDITIONAL`, `CONJECTURED`, `HEURISTIC`, `UNRESOLVED`. No conjecture is ever presented as a theorem.
