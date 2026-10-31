# Series

> **Layer:** [06 Real Analysis](../README.md) › [Limits and Convergence](README.md)
> **Builds on:** [Sequences and limits](sequences-and-limits.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md)
> **Enables:** [Uniform convergence](uniform-convergence.md), [Taylor expansion](../02-calculus-of-one-variable/taylor-expansion.md), [The exponential and trigonometric functions](../02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md), [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [The Riemann zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md)

## Essence

A series a₁ + a₂ + a₃ + ⋯ is not an infinite addition. It is the limit of its partial sums sₙ = a₁ + ⋯ + aₙ, and it converges when that limit exists. Exact sums are rarely computable, so the theory is mostly a set of tests that decide convergence by comparison with a series one understands, usually the geometric series. The main surprise is that infinite sums obey the laws of finite sums only under absolute convergence: a conditionally convergent series can be reordered to sum to any number at all. Power series turn the theory into a supply of functions, among them exp, sin and cos.

## Core tenets

1. **If a series converges, its terms tend to 0; the converse is false.** If sₙ → s then aₙ = sₙ − sₙ₋₁ → s − s = 0. The harmonic series 1 + 1/2 + 1/3 + ⋯ shows the converse fails. Group its terms as 1 + 1/2 + (1/3 + 1/4) + (1/5 + ⋯ + 1/8) + ⋯: each bracket is at least 1/2, so the partial sums are unbounded. This grouping argument goes back to Nicole Oresme in the 14th century.

2. **The geometric series is the yardstick.** For |r| < 1, the identity 1 + r + ⋯ + rⁿ = (1 − r^(n+1))/(1 − r) gives the sum 1/(1 − r); for |r| ≥ 1 the terms do not tend to 0. The ratio test compares with it: if |aₙ₊₁/aₙ| → L < 1, the terms eventually shrink faster than a geometric series with ratio between L and 1, so the series converges, and if L > 1 the terms grow. The root test does the same with limsup |aₙ|^(1/n). When L = 1 both tests are silent: ∑1/n diverges and ∑1/n² converges, and both have L = 1.

3. **A series of non-negative terms converges exactly when its partial sums are bounded.** Its partial sums increase, so the monotone convergence of bounded sequences applies. This yields the comparison test (0 ≤ aₙ ≤ bₙ and ∑bₙ converges, so ∑aₙ converges) and the integral test: ∑1/nᵖ converges if and only if p > 1, by comparison with the integral of x^(−p) from 1 to ∞. The same idea shows that 1 + 1/2 + ⋯ + 1/n − log n decreases to a limit γ ≈ 0.5772, the Euler–Mascheroni constant. Whether γ is irrational is open as of 2026.

4. **Absolute convergence implies convergence, by the Cauchy criterion.** If ∑|aₙ| converges, then |aₘ₊₁ + ⋯ + aₙ| ≤ |aₘ₊₁| + ⋯ + |aₙ|, which is small for large m, so the partial sums of ∑aₙ are Cauchy and completeness supplies a sum. The converse fails: 1 − 1/2 + 1/3 − ⋯ converges (to log 2) while ∑1/n diverges. The alternating series test explains why: if aₙ decreases to 0, the partial sums of ∑(−1)ⁿaₙ swing back and forth inside nested intervals of length aₙ, and the error is at most the first omitted term.

5. **Only absolutely convergent series may be reordered freely (Riemann's rearrangement theorem).** If ∑|aₙ| converges, every rearrangement has the same sum, because the terms outside a large finite set contribute almost nothing. If the convergence is only conditional, the positive terms alone sum to ∞, and so do the negative terms alone, while all terms tend to 0. To reach any target c, add positive terms until the sum exceeds c, then negative terms until it falls below, and repeat: the overshoots shrink with the terms, so the new series converges to c.

6. **Multiplying series needs absolute convergence.** The Cauchy product of ∑aₙ and ∑bₙ (indexed from 0) is ∑cₙ with cₙ = a₀bₙ + a₁bₙ₋₁ + ⋯ + aₙb₀, the rule for multiplying power series. If one factor converges absolutely and the other converges, ∑cₙ converges to the product of the sums (Mertens's theorem). With two conditionally convergent factors it can fail: in the square of ∑(−1)ⁿ/√(n + 1), the arithmetic mean–geometric mean (AM–GM) inequality shows that cₙ has size at least 2(n + 1)/(n + 2), so the terms do not tend to 0. This theorem is the step behind exp(a + b) = exp(a) exp(b).

7. **A power series converges inside a radius and diverges outside it.** For ∑cₙxⁿ there is an R in [0, ∞] with absolute convergence for |x| < R and divergence for |x| > R, where 1/R = limsup |cₙ|^(1/n) (the Cauchy–Hadamard formula). The reason: if the series converges at x₀, its terms are bounded there, so at any |x| < |x₀| it is dominated by a geometric series with ratio |x/x₀|. On the circle |x| = R anything can happen: ∑xⁿ/n converges at x = −1 and diverges at x = 1.

## Key concepts

| Term | Meaning |
|---|---|
| Partial sum | sₙ = a₁ + ⋯ + aₙ; the series converges when sₙ does |
| Geometric series | ∑rⁿ = 1/(1 − r) for ∣r∣ < 1 |
| Harmonic series | ∑1/n: its terms tend to 0 but its partial sums are unbounded |
| Absolute convergence | ∑∣aₙ∣ converges |
| Conditional convergence | ∑aₙ converges but ∑∣aₙ∣ does not |
| Rearrangement | The same terms summed in a different order |
| Cauchy product | The series ∑cₙ with cₙ = a₀bₙ + ⋯ + aₙb₀ |
| Radius of convergence | The R with 1/R = limsup ∣cₙ∣^(1/n), separating convergence from divergence |

## How it fits

- **Below:** A series is a sequence of partial sums, so everything rests on [sequences and limits](sequences-and-limits.md) and on the completeness of [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), which supplies sums through the Cauchy criterion. [Generating functions](../../03-combinatorics-and-graph-theory/01-enumeration/generating-functions.md) use power series as formal objects, where convergence is not needed.
- **Above:** [Taylor expansion](../02-calculus-of-one-variable/taylor-expansion.md) asks which functions are sums of power series, and [exp](../02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md) is defined as one. [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) expand in sines and cosines, where convergence is delicate. The [Riemann zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md) ζ(s) = ∑1/nˢ starts life as a series.
- **Siblings:** [Uniform convergence](uniform-convergence.md) treats series of functions, whose sums must also be continuous or differentiable. [Estimates and inequalities](estimates-and-inequalities.md) supplies the bounds that comparison tests need.

## Common misconceptions

- **"If the terms tend to 0, the series converges."** The harmonic series is the counterexample, and ∑1/(n log n) diverges even more slowly.
- **"1 + 2 + 3 + ⋯ = −1/12."** The series diverges. The value −1/12 is ζ(−1), the analytic continuation of ∑1/nˢ from the region where it converges, a different object that agrees with the series only where the series converges.
- **"The order of the terms never matters."** It matters for every conditionally convergent series, by tenet 5.

## Go deeper

- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 3 proves the tests, the product theorem and the rearrangement theorem.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): a gentler path through convergence tests and rearrangements.
- Konrad Knopp, *Theory and Application of Infinite Series*: the classic, encyclopaedic reference.
