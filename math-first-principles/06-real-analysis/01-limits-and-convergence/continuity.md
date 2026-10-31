# Continuity

> **Layer:** [06 Real Analysis](../README.md) › [Limits and Convergence](README.md)
> **Builds on:** [Sequences and limits](sequences-and-limits.md), [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md)
> **Enables:** [The derivative and the mean value theorem](../02-calculus-of-one-variable/the-derivative-and-the-mean-value-theorem.md), [The Riemann integral](../02-calculus-of-one-variable/the-riemann-integral.md), [Metric spaces and continuity](../03-metric-spaces/metric-spaces-and-continuity.md), [Compactness in metric spaces](../03-metric-spaces/compactness-in-metric-spaces.md), [Topological spaces and continuous maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md)

## Essence

A function f from a set D ⊆ ℝ to ℝ is continuous at a point a when small changes of input give small changes of output: for every ε > 0 there is δ > 0 such that |x − a| < δ implies |f(x) − f(a)| < ε. Equivalently, f preserves limits: xₙ → a implies f(xₙ) → f(a). This replaces "a curve drawn without lifting the pen" with a condition that can be checked and negated. The great theorems about continuous functions do not follow from continuity alone. Each also needs the domain to be an interval, often a closed bounded one, and the completeness of ℝ.

## Core tenets

1. **Continuity is a "∀ε ∃δ" statement, and δ may depend on the point.** For f(x) = x², the bound |x² − a²| = |x − a|·|x + a| ≤ |x − a|·(2|a| + 1), valid when |x − a| < 1, shows that δ = min(1, ε/(2|a| + 1)) works. This δ shrinks as |a| grows. When one δ serves every point, f is uniformly continuous, a stronger property that x² on ℝ lacks. Sums, products, quotients with nonzero denominator, and composites of continuous functions are continuous, by the limit laws.

2. **The ε–δ and sequential definitions are equivalent.** If f satisfies the ε–δ condition at a and xₙ → a, then eventually |xₙ − a| < δ, so |f(xₙ) − f(a)| < ε. Conversely, if the condition fails for some ε, then for each n there is an xₙ within 1/n of a with |f(xₙ) − f(a)| ≥ ε. This sequence tends to a while f(xₙ) stays away from f(a). One sequence is usually the quickest proof of discontinuity.

3. **Continuity can fail in strange patterns.** The Dirichlet function, 1 on ℚ and 0 elsewhere, is continuous nowhere, since every interval holds rationals and irrationals. Thomae's function, f(p/q) = 1/q in lowest terms and f = 0 at irrationals, is continuous exactly at the irrationals. Near an irrational only finitely many fractions with small denominators lie close, so f is small there. No function is continuous exactly at the rationals: the set of continuity points is always a countable intersection of open sets, and ℚ is not one, by the [Baire category theorem](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md).

4. **Intermediate value theorem (IVT): a continuous f on [a, b] takes every value between f(a) and f(b).** Bolzano proved it in 1817. Say f(a) < 0 < f(b) and let c = sup{x ∈ [a, b] : f(x) < 0}. If f(c) < 0, continuity keeps f negative a little to the right of c, so c is not an upper bound. If f(c) > 0, f is positive on an interval just left of c, so a smaller upper bound exists. Hence f(c) = 0. Both hypotheses matter: on ℚ ∩ [1, 2], x² − 2 changes sign without vanishing, and a function with a jump can skip values. The IVT gives every odd-degree real polynomial a real root and justifies bisection.

5. **Extreme value theorem (EVT): a continuous f on a closed bounded interval [a, b] is bounded and attains its maximum and minimum.** If f were unbounded, pick xₙ with f(xₙ) > n. By Bolzano–Weierstrass a subsequence converges to some c, which lies in [a, b] because the interval is closed, and continuity forces those values towards f(c), a contradiction. So M = sup f is finite; pick xₙ with f(xₙ) → M, extract a convergent subsequence, and its limit c has f(c) = M. Every hypothesis is needed: 1/x on (0, 1] is unbounded, x on [0, ∞) has no maximum, and −(x² − 2)² on ℚ ∩ [1, 2] never reaches its supremum 0.

6. **On a closed bounded interval, continuity is automatically uniform (the Heine–Cantor theorem).** Otherwise, for some ε there are points xₙ, yₙ with |xₙ − yₙ| < 1/n but |f(xₙ) − f(yₙ)| ≥ ε. A subsequence of the xₙ converges to some c, the matching yₙ converge to c as well, and continuity at c gives a contradiction. This is what makes continuous functions Riemann integrable. It fails on (0, 1] for sin(1/x) and on ℝ for x².

## Key concepts

| Term | Meaning |
|---|---|
| Continuity at a | ∀ε > 0 ∃δ > 0: ∣x − a∣ < δ ⇒ ∣f(x) − f(a)∣ < ε |
| Sequential continuity | xₙ → a implies f(xₙ) → f(a); equivalent to continuity at a |
| Limit of a function | lim f(x) = L as x → a: values at points near a, excluding a, are near L |
| Uniform continuity | For each ε, one δ serves every point of the domain |
| Lipschitz function | ∣f(x) − f(y)∣ ≤ K∣x − y∣ for a constant K; such f is uniformly continuous |
| Kinds of discontinuity | Removable (the limit exists but differs from f(a)), jump (the one-sided limits differ), essential (a one-sided limit fails to exist) |
| Intermediate value property | Every value between two values of f is attained |

## How it fits

- **Below:** The definition is a limit, from [sequences and limits](sequences-and-limits.md). The big theorems use the supremum and Bolzano–Weierstrass, both forms of the completeness of [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md). A function here is any rule in the sense of [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), not only a formula.
- **Above:** Continuity is a hypothesis of [the mean value theorem](../02-calculus-of-one-variable/the-derivative-and-the-mean-value-theorem.md) and of [integrability](../02-calculus-of-one-variable/the-riemann-integral.md). [Metric spaces](../03-metric-spaces/metric-spaces-and-continuity.md) restate it with a general distance, and [topology](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) restates it as "preimages of open sets are open", dropping distance altogether. Tenets 5 and 6 are special cases of [compactness](../03-metric-spaces/compactness-in-metric-spaces.md).
- **Siblings:** [Uniform convergence](uniform-convergence.md) asks when a limit of continuous functions is continuous. [Estimates and inequalities](estimates-and-inequalities.md) supplies the bounds used to find δ.

## Common misconceptions

- **"Continuous means the graph can be drawn without lifting the pen."** The picture misleads. x sin(1/x), set to 0 at 0, is continuous, yet its graph near 0 has infinite length. Weierstrass's function is continuous everywhere and differentiable nowhere.
- **"The intermediate value property implies continuity."** sin(1/x), given any value in [−1, 1] at 0, has the property but is discontinuous at 0. Every derivative has the property too, even a discontinuous one (Darboux's theorem).
- **"Continuous at every point means one δ works for each ε."** That is uniform continuity, which needs more, such as a closed bounded domain (tenet 6).

## Go deeper

- Michael Spivak, *Calculus* (4th edition, 2008): its chapter "Three Hard Theorems" isolates exactly where completeness enters.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): a gentle treatment of functional limits and continuity.
- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 4 treats continuity in metric spaces from the start.
