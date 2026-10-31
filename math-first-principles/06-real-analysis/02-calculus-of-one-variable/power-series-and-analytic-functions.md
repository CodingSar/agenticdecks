# Power Series and Analytic Functions

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of One Variable](README.md)
> **Builds on:** [Series](../01-limits-and-convergence/series.md), [Uniform convergence](../01-limits-and-convergence/uniform-convergence.md), [The derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md), [Taylor expansion](taylor-expansion.md)
> **Enables:** [The exponential and trigonometric functions](the-exponential-and-trigonometric-functions.md), [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Analytic continuation and Riemann surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md)

## Essence

A power series ∑cₙ(x − a)ⁿ is a polynomial of infinite degree, and inside its radius of convergence it behaves almost exactly like one: it can be added, multiplied, differentiated and integrated term by term, and its coefficients can be read off from its derivatives at a. Functions that are given near every point by such a series are called analytic. They form a small, rigid class inside the smooth functions. An analytic function on an interval is determined by its values on any tiny piece of it, and how far its series converges is decided by singularities that may lie off the real line. This rigidity is what makes polynomials, exp, sin, cos and most functions of physics so well behaved, and it is the doorway to complex analysis.

## Core tenets

1. **Inside its radius, a power series is infinitely differentiable, and it is the Taylor series of its own sum.** Let f(x) = ∑cₙ(x − a)ⁿ with radius R > 0, from the Cauchy–Hadamard formula in [series](../01-limits-and-convergence/series.md). The differentiated series ∑ncₙ(x − a)ⁿ⁻¹ has the same radius, because n^(1/n) → 1. On each smaller interval |x − a| ≤ r < R both series converge uniformly by the M-test, so f is differentiable with f′ equal to the differentiated series. Repeating, f is smooth, and setting x = a in the k-th derivative gives cₖ = f⁽ᵏ⁾(a)/k!. So two power series with the same sum near a have the same coefficients.

2. **Power series form an algebra closed under the usual operations.** Sums and products of convergent power series are power series, with products given by the Cauchy product, valid within the smaller of the two radii. Composition of power series, and the reciprocal 1/f where f(a) ≠ 0, are again power series with a positive radius. Each step rearranges absolutely convergent double sums, which is safe. So sums, products, quotients and composites of analytic functions are analytic wherever they are defined.

3. **A power series is analytic at every point of its interval of convergence.** f is analytic on an open interval I if near each point b of I it equals a power series in (x − b) with positive radius. Polynomials qualify by definition. For a power series about a with radius R and a point b with |b − a| < R, write (x − a)ⁿ = ((x − b) + (b − a))ⁿ, expand by the binomial theorem and collect powers of (x − b). The double series converges absolutely when |x − b| + |b − a| < R, so the rearrangement is valid and the new series has radius at least R − |b − a|. For 1/(1 − x) = ∑xⁿ about 0, re-expanding about b in (−1, 1) gives ∑(x − b)ⁿ/(1 − b)ⁿ⁺¹, with radius exactly 1 − b.

4. **The identity theorem: an analytic function vanishing on a set with a limit point in I vanishes on all of I.** Suppose f is analytic on I, and its zeros accumulate at a point a of I. If some coefficient of f at a were non-zero, with cₖ the first, then f(x) = (x − a)ᵏ(cₖ + cₖ₊₁(x − a) + ⋯), and the bracket is non-zero near a, so a would be an isolated zero. So every derivative of f vanishes at a. The set of points where all derivatives vanish is closed by continuity, and open because the series there is 0. An interval is connected, so that set is all of I. Two analytic functions that agree on a tiny interval agree everywhere on I. There is no analytic bump function: a non-zero analytic function cannot vanish on an interval.

5. **Smooth functions are analytic exactly when their derivatives grow no faster than C·Mⁿ·n!.** The function e^(−1/x²), extended by 0 at x = 0, from [Taylor expansion](taylor-expansion.md) is smooth but not analytic at 0. A sufficient condition: if |f⁽ⁿ⁾(x)| ≤ C·Mⁿ·n! for all n and all x near a, the Lagrange remainder is at most C·(M|x − a|)ⁿ⁺¹, which tends to 0 when |x − a| < 1/M. So the Taylor series converges to f near a. Conversely, every analytic function obeys bounds of this form on each closed bounded subinterval. For e^(−1/x²) the derivatives near 0 grow faster than any such bound.

6. **The radius is fixed by the nearest complex singularity.** The proof of tenet 1 works verbatim for complex x, so a real power series converges on a disc in ℂ, and an analytic function on I extends to a holomorphic function near I. So 1/(1 + x²), analytic on all of ℝ, has radius 1 about 0, because 1/(1 + z²) blows up at z = ±i. About the point b its radius is √(1 + b²), the distance to ±i. [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) explain this, and [analytic continuation](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) extends tenet 3 off the line.

7. **Abel's theorem: if ∑cₙ converges, then ∑cₙxⁿ → ∑cₙ as x increases to 1.** The sum is continuous up to an endpoint where the series converges. Proof idea: summing by parts, ∑cₙxⁿ = (1 − x)·∑sₙxⁿ, where sₙ are the partial sums, a weighted average of the sₙ whose weight moves to large n as x → 1. Applied to log(1 + x) = x − x²/2 + x³/3 − ⋯ it gives log 2 = 1 − 1/2 + 1/3 − ⋯, and applied to arctan it gives π/4 = 1 − 1/3 + 1/5 − ⋯. The converse fails: ∑(−1)ⁿxⁿ = 1/(1 + x) → ½, yet ∑(−1)ⁿ diverges. Tauber's theorem restores the converse when ncₙ → 0.

## Key concepts

| Term | Meaning |
|---|---|
| Power series | ∑cₙ(x − a)ⁿ, a series of powers centred at a |
| Radius of convergence R | The series converges absolutely for ∣x − a∣ < R and diverges for ∣x − a∣ > R |
| Analytic function | Equal near each point to a power series with positive radius |
| Re-expansion | Rewriting a power series about a new centre inside its radius |
| Identity theorem | Zeros of a non-zero analytic function on an interval are isolated |
| Bump function | A smooth function that is non-zero only on a bounded interval; never analytic |
| Abel's theorem | Continuity of a power series up to an endpoint where it converges |
| Abel sum | The limit of ∑cₙxⁿ as x → 1, which can exist when ∑cₙ diverges |

## How it fits

- **Below:** The radius comes from the Cauchy–Hadamard formula in [series](../01-limits-and-convergence/series.md), and the M-test in [uniform convergence](../01-limits-and-convergence/uniform-convergence.md) licenses termwise differentiation. [Taylor expansion](taylor-expansion.md) supplies the remainder estimates of tenet 5. [Generating functions](../../03-combinatorics-and-graph-theory/01-enumeration/generating-functions.md) use the same series formally, and convergence lets them be evaluated as functions.
- **Above:** [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) are exactly the functions analytic in ℂ, and there tenet 6 becomes a theorem. [Analytic continuation](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) pushes tenet 3 as far as it will go.
- **Siblings:** [The exponential and trigonometric functions](the-exponential-and-trigonometric-functions.md) are built from power series by tenet 1. [Taylor expansion](taylor-expansion.md) asks which smooth functions equal their series; this leaf studies those that do. [The mean value theorem](the-derivative-and-the-mean-value-theorem.md) underlies the remainder bounds.

## Common misconceptions

- **"A function analytic on all of ℝ has a Taylor series converging on all of ℝ."** 1/(1 + x²) is analytic everywhere on ℝ, yet its series about 0 has radius 1 (tenet 6).
- **"Smooth functions that agree on an interval agree everywhere."** True for analytic functions (tenet 4), false for smooth ones: a smooth bump function agrees with 0 outside its support.
- **"If ∑cₙxⁿ has a limit as x → 1, then ∑cₙ converges."** ∑(−1)ⁿ has Abel sum ½ but diverges (tenet 7).

## Go deeper

- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 8 opens with power series, re-expansion and Abel's theorem.
- Steven G. Krantz and Harold R. Parks, *A Primer of Real Analytic Functions* (2nd edition, 2002): the real theory in full, including the derivative bounds of tenet 5.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): power series and Abel's theorem at an undergraduate pace.
