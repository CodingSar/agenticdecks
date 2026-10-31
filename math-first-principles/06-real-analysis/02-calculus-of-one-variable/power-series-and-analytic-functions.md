# Power Series and Analytic Functions

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of One Variable](README.md)
> **Builds on:** [Series](../01-limits-and-convergence/series.md), [Uniform convergence](../01-limits-and-convergence/uniform-convergence.md), [The derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md), [Taylor expansion](taylor-expansion.md)
> **Enables:** [The exponential and trigonometric functions](the-exponential-and-trigonometric-functions.md), [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Analytic continuation and Riemann surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md)

## Essence

A power series ∑cₙ(x − a)ⁿ is a polynomial of infinite degree, and inside its radius of convergence it behaves like one: it can be added, multiplied and differentiated term by term, and its coefficients are its derivatives at a divided by n!. Functions given near every point by such a series are called analytic. They form a small, rigid class inside the smooth functions: an analytic function on an interval is determined by its values on any tiny piece of it, and how far its series converges is decided by singularities that may lie off the real line. That rigidity is the doorway to complex analysis.

## Core tenets

1. **Inside its radius, a power series is infinitely differentiable, and it is the Taylor series of its own sum.** Let f(x) = ∑cₙ(x − a)ⁿ with radius R > 0, given by the Cauchy–Hadamard formula in [series](../01-limits-and-convergence/series.md). The differentiated series has the same radius, because n^(1/n) → 1, and on each interval |x − a| ≤ r < R both converge uniformly by the M-test. So f′ is the differentiated series. Repeating, f is smooth, and setting x = a in the k-th derivative gives cₖ = f⁽ᵏ⁾(a)/k!. Hence two power series with the same sum near a have the same coefficients.

2. **Power series are closed under arithmetic and composition.** Sums and Cauchy products converge within the smaller radius; composites, and 1/f where f(a) ≠ 0, are again power series with positive radius, by rearranging absolutely convergent double sums. So sums, products, quotients and composites of analytic functions are analytic wherever they are defined.

3. **A power series is analytic at every point of its interval of convergence.** f is analytic on an open interval I if near each point b of I it equals a power series in (x − b) with positive radius. Given a series about a with radius R and |b − a| < R, write (x − a)ⁿ = ((x − b) + (b − a))ⁿ, expand by the binomial theorem and collect powers of (x − b). The double series converges absolutely when |x − b| + |b − a| < R, so the new series has radius at least R − |b − a|. For 1/(1 − x) = ∑xⁿ about 0, re-expanding about b in (−1, 1) gives ∑(x − b)ⁿ/(1 − b)ⁿ⁺¹, with radius exactly 1 − b.

4. **The identity theorem: an analytic function vanishing on a set with a limit point in I vanishes on all of I.** Suppose the zeros of f accumulate at a in I. If some coefficient at a were non-zero, with cₖ the first, then f(x) = (x − a)ᵏ(cₖ + cₖ₊₁(x − a) + ⋯) with the bracket non-zero near a, so a would be an isolated zero. So every derivative vanishes at a. The set where all derivatives vanish is closed by continuity and open because the series there is 0, so, I being connected, it is all of I. Hence two analytic functions that agree on a tiny interval agree on all of I, and there is no analytic bump function.

5. **Smooth functions are analytic exactly when their derivatives grow no faster than C·Mⁿ·n!.** If |f⁽ⁿ⁾(x)| ≤ C·Mⁿ·n! for all n and all x near a, the Lagrange remainder is at most C·(M|x − a|)ⁿ⁺¹, which tends to 0 when |x − a| < 1/M, so the Taylor series converges to f near a. Conversely, every analytic function obeys such bounds on each closed bounded subinterval. The derivatives of e^(−1/x²) from [Taylor expansion](taylor-expansion.md) break every such bound near 0, which is why it is smooth but not analytic there.

6. **The radius is fixed by the nearest complex singularity.** Tenet 1 works verbatim for complex x, so a real power series converges on a disc in ℂ, and an analytic function on I extends to a holomorphic function near I. So 1/(1 + x²), analytic on all of ℝ, has radius 1 about 0, because 1/(1 + z²) blows up at z = ±i; about b its radius is √(1 + b²), the distance to ±i. [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) explain why.

7. **Abel's theorem: if ∑cₙ converges, then ∑cₙxⁿ → ∑cₙ as x increases to 1.** Proof idea: summing by parts, ∑cₙxⁿ = (1 − x)·∑sₙxⁿ, where sₙ are the partial sums, a weighted average of the sₙ whose weight moves to large n as x → 1. Applied to log(1 + x) = x − x²/2 + x³/3 − ⋯ it gives log 2 = 1 − 1/2 + 1/3 − ⋯. The converse fails: ∑(−1)ⁿxⁿ = 1/(1 + x) → ½, yet ∑(−1)ⁿ diverges. Tauber's theorem restores the converse when ncₙ → 0.

## Key concepts

| Term | Meaning |
|---|---|
| Power series | ∑cₙ(x − a)ⁿ, a series of powers centred at a |
| Radius of convergence R | The series converges absolutely for ∣x − a∣ < R and diverges for ∣x − a∣ > R |
| Analytic function | Equal near each point to a power series with positive radius |
| Identity theorem | Zeros of a non-zero analytic function on an interval are isolated |
| Bump function | A smooth function that is non-zero only on a bounded interval; never analytic |
| Abel's theorem | Continuity of a power series up to an endpoint where it converges |
| Abel sum | The limit of ∑cₙxⁿ as x → 1, which can exist when ∑cₙ diverges |

## How it fits

- **Below:** [Series](../01-limits-and-convergence/series.md) gives the radius, and the M-test from [uniform convergence](../01-limits-and-convergence/uniform-convergence.md) licenses termwise differentiation. [Generating functions](../../03-combinatorics-and-graph-theory/01-enumeration/generating-functions.md) use the same series formally.
- **Above:** [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) are the functions analytic in ℂ, where tenet 6 becomes a theorem, and [analytic continuation](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) pushes tenet 3 as far as it will go.
- **Siblings:** [Taylor expansion](taylor-expansion.md) asks which smooth functions equal their series and supplies the remainder of tenet 5; this leaf studies those that do. [The exponential and trigonometric functions](the-exponential-and-trigonometric-functions.md) are built from power series by tenet 1, and [the mean value theorem](the-derivative-and-the-mean-value-theorem.md) underlies the remainder bounds.

## Common misconceptions

- **"A function analytic on all of ℝ has a Taylor series converging on all of ℝ."** 1/(1 + x²) is analytic everywhere on ℝ, yet its series about 0 has radius 1 (tenet 6).
- **"Smooth functions that agree on an interval agree everywhere."** True for analytic functions (tenet 4), false for smooth bump functions.
- **"If ∑cₙxⁿ has a limit as x → 1, then ∑cₙ converges."** ∑(−1)ⁿ has Abel sum ½ but diverges (tenet 7).

## Go deeper

- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 8 opens with power series and Abel's theorem.
- Steven G. Krantz and Harold R. Parks, *A Primer of Real Analytic Functions* (2nd edition, 2002): the real theory in full, including tenet 5.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): power series at an undergraduate pace.
