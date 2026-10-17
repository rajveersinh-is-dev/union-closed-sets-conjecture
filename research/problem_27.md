# Candidate: Ben Green's "100 Open Problems", Problem 27

## Statement

For a prime $p$ and $A\subseteq\mathbb Z/p\mathbb Z$, define the representation function
$$r_A(s) := |\{(a,b)\in A\times A : a+b = s\}| \qquad (s\in\mathbb Z/p\mathbb Z).$$
(Ordered pairs; doubles $(a,a)$ count once.)

Define
$$g(p) := \min\{\,|A| : A\subseteq\mathbb Z/p\mathbb Z,\ |A|\ge2,\ \forall s\in A+A,\ r_A(s)\ne 1\,\}.$$

That is: every representable sum $s\in A+A$ has either $0$ or at least $2$ representations — no sum is represented in exactly one way.

**Problem 27 (Ben Green, "100 Open Problems"):** Determine $g(p)$ (as a function of $p$, or at least bounds/asymptotics). Open; no "solved" update on Green's list.

## Immediate necessary condition

For $s=2a$ ($a\in A$), $(a,a)$ is always a representation. For $r_A(2a)\ne1$, we need another pair, necessarily $(b,c)$ with $b\ne c$ and $b+c=2a$ (doubles $(b,b)$ give $2b=2a\Rightarrow b=a$). Thus:

> Every $a\in A$ must be the midpoint of two distinct elements of $A$: $\exists b,c\in A,\ b\ne c,\ b+c=2a$.

Hence no element of $A$ is a "midpoint-extreme."

## Small cases (reasoning)

* $|A|=2$: $A=\{a,b\}$. $r(2a)=1$ (only $(a,a)$) since $2a=a+b\Rightarrow a=b$ and $2a=b+b\Rightarrow a=b$. Fails. So $g(p)\ge3$.
* $|A|=3$: $A=\{a,b,c\}$. Need $2a=b+c$, $2b=a+c$, $2c=a+b$ (each element midpoint of the other two). For $p>3$, subtracting gives $a=b=c$, contradiction. So $|A|=3$ impossible for $p>3$; $g(p)\ge4$ for $p>3$.

## Status to verify

Confirm Problem 27 is still open (no subsequent solution), and identify any known bounds on $g(p)$.

## Computational plan

Brute-force enumerate subsets of $\mathbb Z/p\mathbb Z$ by increasing size for small primes, compute $g(p)$, inspect extremal sets, conjecture a bound/formula, then attempt a proof.

**Evidence label:** computation is `COMPUTATIONALLY VERIFIED` on finite domains only; any general bound must be proved.
