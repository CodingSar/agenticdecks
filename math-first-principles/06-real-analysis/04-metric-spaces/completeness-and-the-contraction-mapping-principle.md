# Completeness and the Contraction Mapping Principle

> **Layer:** [06 Real Analysis](../README.md) › [Metric Spaces](README.md)
> **Builds on:** [Metric spaces and continuity](metric-spaces-and-continuity.md), [Sequences and limits](../01-limits-and-convergence/sequences-and-limits.md), [Uniform convergence](../01-limits-and-convergence/uniform-convergence.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md)
> **Enables:** [Inverse and implicit function theorems](../03-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), [Existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), [Hahn–Banach and Baire category](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md), [Root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md)

## Essence

A metric space is complete when every sequence whose terms bunch together, a Cauchy sequence, actually converges to a point of the space. ℝ is complete and ℚ is not, and the same contrast appears in every corner of analysis: completeness is what lets a proof say "the limit exists" without naming it. Its most useful consequence is Banach's contraction mapping principle. If a map on a complete space shrinks all distances by a fixed factor, iterating it from any starting point converges to its unique fixed point. That one theorem proves existence for differential equations, the inverse function theorem and the convergence of many algorithms, each time by setting up the right space and the right map.

## Core tenets

1. **A space is complete when every Cauchy sequence converges in it.** xₙ is Cauchy when d(xₘ, xₙ) → 0 as m and n both grow. Every convergent sequence is Cauchy, by the triangle inequality. The converse is the content of completeness. ℝ has it, by its construction; ℚ does not, since the decimal approximations of √2 are Cauchy with no rational limit; ℝⁿ has it, by working one coordinate at a time.

2. **Completeness belongs to the metric, not to the open sets.** (0, 1) and ℝ are homeomorphic, yet 1/n is a Cauchy sequence in (0, 1) with no limit there. So completeness is not preserved by homeomorphisms, unlike compactness. Two simple rules locate complete spaces: a closed subset of a complete space is complete, and a complete subset of any metric space is closed.

3. **The continuous functions are complete under the sup metric but not under the L¹ metric.** If fₙ is Cauchy in the sup metric on C[a, b], each fₙ(x) is a Cauchy sequence of reals, so it has a limit f(x); the convergence is uniform, so f is continuous by [uniform convergence](../01-limits-and-convergence/uniform-convergence.md). Under ∫|f − g|, ramps that rise ever more steeply from 0 to 1 near x = ½ form a Cauchy sequence whose only candidate limit is a step function, which is not continuous. Completing this space under ∫|f − g| produces the space L¹ of [Lebesgue integrable functions](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md).

4. **Every metric space has a completion, unique up to isometry.** Take Cauchy sequences, and identify two when the distance between them tends to 0. The resulting space is complete and contains the original as a dense subset. This is how Cantor built ℝ from ℚ. With the p-adic metric in place of |·|, the same recipe gives the [p-adic numbers](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md).

5. **Banach's contraction mapping principle (1922).** Let X be a non-empty complete metric space and T: X → X a map with d(Tx, Ty) ≤ q·d(x, y) for all x and y, where 0 ≤ q < 1 is fixed. Then T has exactly one fixed point x*, and for any x₀ the iterates xₙ₊₁ = Txₙ converge to it with
   ```
   d(xₙ, x*) ≤ qⁿ/(1 − q) · d(x₁, x₀)
   ```
   Proof idea: d(xₙ₊₁, xₙ) ≤ qⁿ·d(x₁, x₀), so the steps are dominated by a geometric series and the sequence is Cauchy. Its limit x* satisfies Tx* = x* because T is continuous. If y* were a second fixed point, d(x*, y*) ≤ q·d(x*, y*) would force d(x*, y*) = 0. The bound tells you in advance how many steps you need.

6. **Each hypothesis is needed.**
   - A fixed q < 1, not just shrinking distances: T(x) = x + 1/x on the complete space [1, ∞) satisfies d(Tx, Ty) < d(x, y) for x ≠ y, yet T(x) > x always, so there is no fixed point.
   - Completeness: T(x) = x/2 on (0, 1] contracts with q = ½, but its fixed point 0 is missing. On ℚ ∩ [1, 2], T(x) = x/2 + 1/x maps the set into itself and contracts with q = ½, but its fixed point is √2. This T is the Babylonian method for square roots, and on ℝ it converges to √2 from any start in [1, 2].

7. **The principle turns existence questions into choices of space and map.** Picard's method writes a differential equation y′ = f(t, y) as a fixed-point problem y = T(y) for an integral operator, which is a contraction in the sup metric on a short time interval, giving [existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md). The [inverse function theorem](../03-calculus-of-several-variables/inverse-and-implicit-function-theorems.md) solves f(x) = y by a contraction near a point. Google's PageRank vector is the fixed point of a damped random-walk map, a contraction in the ℓ¹ distance, linked to [Perron–Frobenius theory](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md). Completeness also gives the Baire category theorem, a foundation of [functional analysis](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md).

## Key concepts

| Term | Meaning |
|---|---|
| Cauchy sequence | d(xₘ, xₙ) → 0 as m and n both tend to infinity |
| Complete space | Every Cauchy sequence converges to a point of the space |
| Completion | The smallest complete space containing a given one as a dense subset |
| Isometry | A map preserving all distances |
| Contraction | A map with d(Tx, Ty) ≤ q·d(x, y) for a fixed q < 1 |
| Fixed point | A point x* with Tx* = x* |
| A priori bound | d(xₙ, x*) ≤ qⁿ/(1 − q)·d(x₁, x₀), known before iterating |
| Banach space | A complete normed vector space |

## How it fits

- **Below:** The completeness of [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) and the Cauchy criterion from [sequences and limits](../01-limits-and-convergence/sequences-and-limits.md) are the model; [metric spaces](metric-spaces-and-continuity.md) supply the setting.
- **Above:** Complete normed spaces are [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md). Fixed-point iterations drive [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md), and a contraction is the heart of the proof of the [inverse function theorem](../03-calculus-of-several-variables/inverse-and-implicit-function-theorems.md).
- **Siblings:** [Compactness](compactness-in-metric-spaces.md) is equivalent to completeness plus total boundedness, so the two properties together give the closed bounded interval its power.

## Common misconceptions

- **"A map that shrinks every distance has a fixed point."** x + 1/x on [1, ∞) shrinks every distance and has none (tenet 6); the factor must be uniform.
- **"Completeness is a property of the shape of a space."** (0, 1) and ℝ have the same shape in topology, and only ℝ is complete (tenet 2).
- **"A limit of continuous functions in any reasonable metric is continuous."** Only in the sup metric; in the L¹ metric limits can be step functions (tenet 3).

## Go deeper

- Erwin Kreyszig, *Introductory Functional Analysis with Applications* (1978): the contraction principle with applications to linear equations, differential equations and integral equations.
- Wilson A. Sutherland, *Introduction to Metric and Topological Spaces* (2nd edition, 2009): completeness and completions, carefully.
- Andrzej Granas and James Dugundji, *Fixed Point Theory* (2003): Banach's principle and its many relatives.
