# The Riemann Integral

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of One Variable](README.md)
> **Builds on:** [Continuity](../01-limits-and-convergence/continuity.md), [Sequences and limits](../01-limits-and-convergence/sequences-and-limits.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md)
> **Enables:** [The fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md), [Multiple integrals and change of variables](../03-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md), [The Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md), [Measure and sigma-algebras](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md)

## Essence

The integral of f over [a, b] is meant to be the signed area under its graph. Riemann defined it, in work on Fourier series in 1854, by trapping that area between sums of rectangles: chop [a, b] into pieces, build rectangles over each piece using the largest and the smallest value of f there, and ask whether the upper and lower totals can be squeezed together. When they can, the common value is the integral. Continuous and monotone functions pass this test. Some simple functions fail it, and the failures show that the Riemann integral is not closed under limits. That defect is the motive for the Lebesgue integral.

## Core tenets

1. **The integral is squeezed between upper and lower sums.** A partition P of [a, b] is a list a = x₀ < x₁ < ⋯ < xₙ = b. For bounded f, let Mᵢ and mᵢ be the sup and inf of f on [xᵢ₋₁, xᵢ], and Δxᵢ = xᵢ − xᵢ₋₁. The Darboux sums are
   ```
   U(f, P) = ∑ Mᵢ·Δxᵢ        L(f, P) = ∑ mᵢ·Δxᵢ
   ```
   Adding a point to P lowers U or leaves it, and raises L or leaves it. So any lower sum is at most any upper sum: compare both with their common refinement. f is integrable when sup over P of L equals inf over P of U, and that number is ∫ₐᵇ f. Completeness supplies the sup and the inf.

2. **Riemann's criterion: f is integrable if and only if, for every ε > 0, some partition has U(f, P) − L(f, P) < ε.** The gap U − L is the total area of the strips where f oscillates, so integrability means the oscillation can be confined to a region of small total area. Equivalently, the Riemann sums ∑f(tᵢ)Δxᵢ, with any choice of tᵢ in each piece, converge as the longest piece shrinks to 0. Linearity, monotonicity and the bound |∫f| ≤ ∫|f| pass from the sums to the integral.

3. **Continuous functions on [a, b] are integrable, because continuity there is uniform.** By the Heine–Cantor theorem, for ε > 0 there is δ such that f varies by less than ε/(b − a) on any piece shorter than δ. On such a partition, Mᵢ − mᵢ < ε/(b − a), so U − L < ε. Pointwise continuity alone would not supply one δ for all pieces; the closed bounded interval does.

4. **Monotone functions are integrable, even with infinitely many jumps.** If f increases, split [a, b] into n equal pieces. On each piece Mᵢ − mᵢ = f(xᵢ) − f(xᵢ₋₁), and these differences telescope:
   ```
   U − L = (f(b) − f(a))·(b − a)/n  →  0
   ```
   An increasing function can even jump at every rational point and still be integrable.

5. **The definition needs a bounded function on a bounded interval; anything else is an improper integral.** If f is unbounded, some Mᵢ is infinite and no upper sum is finite. So the integral of 1/√x over [0, 1] is defined as a limit: the integral over [c, 1] equals 2 − 2√c, which tends to 2 as c → 0. Integrals over [0, ∞) are likewise limits of integrals over [0, R].

6. **Lebesgue's criterion: a bounded f on [a, b] is Riemann integrable if and only if its set of discontinuities has measure zero.** A set has measure zero when, for every ε > 0, countably many intervals of total length below ε cover it. Thomae's function, 1/q at p/q in lowest terms and 0 at irrationals, is discontinuous exactly at the rationals, a countable set and so of measure zero. Hence it is integrable, with integral 0. Integrability is about how small the set of bad points is, not whether it is empty.

7. **The indicator of the rationals is not integrable, and this failure motivates Lebesgue.** Let f = 1 on ℚ ∩ [0, 1] and 0 elsewhere. Every piece of every partition contains rationals and irrationals, so U = 1 and L = 0 always. Yet list the rationals as q₁, q₂, …, and let fₙ be 1 at q₁, …, qₙ and 0 elsewhere. Each fₙ is integrable with integral 0, and fₙ increases to f at every point. A monotone limit of integrable functions with integral 0 has escaped the class. Equivalently, the Riemann integrable functions are not complete under the distance ∫|f − g|. [The Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) assigns ℚ measure 0, gives this f integral 0, and makes such limits safe.

## Key concepts

| Term | Meaning |
|---|---|
| Partition | Points a = x₀ < x₁ < ⋯ < xₙ = b |
| Mesh | The length of the longest piece of a partition |
| Upper and lower Darboux sums | ∑Mᵢ·Δxᵢ and ∑mᵢ·Δxᵢ, using sup and inf of f on each piece |
| Riemann sum | ∑f(tᵢ)·Δxᵢ with a chosen point tᵢ in each piece |
| Refinement | A partition containing all the points of another |
| Riemann integrable | sup of lower sums equals inf of upper sums |
| Measure zero | Coverable by countably many intervals of total length below any ε > 0 |
| Improper integral | A limit of integrals over bounded intervals, or of bounded pieces of f |

## How it fits

- **Below:** The sup and inf in every sum come from the completeness of [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md). Integrability of continuous functions uses uniform continuity from [continuity](../01-limits-and-convergence/continuity.md), and the integral is a limit in the sense of [sequences and limits](../01-limits-and-convergence/sequences-and-limits.md).
- **Above:** The same squeeze over boxes gives [multiple integrals](../03-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md). Tenet 7 is the starting point of [measure](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) and [the Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md), which integrate far more functions and allow limits under mild conditions.
- **Siblings:** [The fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md) connects this definition with antiderivatives, which is how integrals are actually computed. [Uniform convergence](../01-limits-and-convergence/uniform-convergence.md) gives one safe way to pass limits through the integral.

## Common misconceptions

- **"The integral is defined as an antiderivative evaluated at the ends."** That is a theorem, and it needs hypotheses. The integral is defined by sums, and some integrable functions have no antiderivative at all, such as a step function.
- **"Integrable functions must be continuous."** Monotone functions with infinitely many jumps, and Thomae's function, are integrable (tenets 4 and 6).
- **"If fₙ → f at every point, then ∫fₙ → ∫f."** f may not even be integrable (tenet 7), and when it is, the integrals can still converge to the wrong value.

## Go deeper

- Michael Spivak, *Calculus* (4th edition, 2008): a careful development through upper and lower sums.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): proves Lebesgue's criterion and motivates what comes next.
- Elias M. Stein and Rami Shakarchi, *Real Analysis* (2005): motivates Lebesgue's integral by the limits that Riemann's cannot handle.
