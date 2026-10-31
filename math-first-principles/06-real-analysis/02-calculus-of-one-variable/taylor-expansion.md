# Taylor Expansion

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of One Variable](README.md)
> **Builds on:** [The derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md), [Series](../01-limits-and-convergence/series.md), [Estimates and inequalities](../01-limits-and-convergence/estimates-and-inequalities.md)
> **Enables:** [The exponential and trigonometric functions](the-exponential-and-trigonometric-functions.md), [Extrema and Lagrange multipliers](../03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md), [Interpolation and approximation](../../14-applied-and-computational-mathematics/01-numerical-analysis/interpolation-and-approximation.md), [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md)

## Essence

The derivative gives the best linear approximation to a function; Taylor expansion gives the best polynomial approximation of each degree. The Taylor polynomial of degree n at a matches the value of f and its first n derivatives at a, and the theorem that matters is the bound on what is left over, the remainder. With a remainder bound, a function such as exp or sin can be computed to any accuracy from additions and multiplications. Without one, the expansion can mislead: a function may have derivatives of every order and still differ from its Taylor series everywhere except at a.

## Core tenets

1. **The Taylor polynomial is the unique polynomial that agrees with f to order n.** It is
   ```
   Pₙ(x) = f(a) + f′(a)(x − a) + f″(a)(x − a)²/2! + ⋯ + f⁽ⁿ⁾(a)(x − a)ⁿ/n!
   ```
   where f⁽ᵏ⁾ is the k-th derivative. The factor 1/k! appears because the k-th derivative of (x − a)ᵏ is k!. If f is n times differentiable at a, then f(x) = Pₙ(x) + o((x − a)ⁿ) (the Peano form), and no other polynomial of degree at most n has so small an error. So sin x = x − x³/6 + O(x⁵), which settles limits such as (x − sin x)/x³ → 1/6 at once.

2. **The Lagrange remainder: f(x) − Pₙ(x) = f⁽ⁿ⁺¹⁾(ξ)(x − a)ⁿ⁺¹/(n + 1)! for some ξ between a and x.** This needs f to be n + 1 times differentiable on the interval. Proof idea: choose K so that g(t) = f(t) − Pₙ(t) − K(t − a)ⁿ⁺¹ vanishes at t = x. Then g and its first n derivatives vanish at a, and g vanishes at x, so Rolle's theorem applied n + 1 times produces a ξ where g⁽ⁿ⁺¹⁾(ξ) = 0, which says K = f⁽ⁿ⁺¹⁾(ξ)/(n + 1)!. For eˣ on [0, 1] every derivative is at most 3, so 1 + 1 + 1/2! + ⋯ + 1/n! is within 3/(n + 1)! of e.

3. **The integral form of the remainder comes from the fundamental theorem of calculus.** If f⁽ⁿ⁺¹⁾ is continuous, f(x) − Pₙ(x) equals the integral from a to x of f⁽ⁿ⁺¹⁾(t)(x − t)ⁿ/n! dt. Start from f(x) = f(a) + ∫f′ and integrate by parts n times; each step produces the next Taylor term. This form needs no unknown point ξ, so it is the one used for vector-valued functions and in proofs.

4. **Smooth does not mean analytic.** Define f(x) = e^(−1/x²) for x ≠ 0 and f(0) = 0. Every derivative at 0 is 0, because e^(−1/x²) tends to 0 faster than any power of x. Its Taylor series at 0 is therefore the zero series: it converges everywhere, but to f only at x = 0. A function is analytic when it equals its Taylor series near every point; smooth functions (with derivatives of all orders) need not be. Borel's theorem goes further: any sequence of numbers is the sequence of derivatives at 0 of some smooth function, so a Taylor series may even have radius of convergence 0.

5. **Real analysis cannot see why a Taylor series stops converging; complex analysis can.** f(x) = 1/(1 + x²) is smooth on all of ℝ, yet its series 1 − x² + x⁴ − ⋯ converges only for |x| < 1. The reason lies off the real line: 1/(1 + z²) blows up at z = ±i, at distance 1 from 0. For [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) the radius of convergence is the distance to the nearest singularity, and differentiable once in ℂ already means analytic.

6. **The second derivative classifies critical points.** If f′(a) = 0, then f(a + h) = f(a) + ½f″(a)h² + o(h²). If f″(a) > 0, the quadratic term beats the error for small h and a is a strict local minimum; if f″(a) < 0 it is a strict local maximum. If f″(a) = 0 the test is silent: x³, x⁴ and −x⁴ all have f′(0) = f″(0) = 0 and behave in three different ways. In several variables f″ becomes the Hessian, a quadratic form.

7. **Taylor's theorem explains why Newton's method doubles the digits.** Newton's method solves f(x) = 0 by xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ). Expanding f to second order about xₙ at a simple root r, where f′(r) ≠ 0, gives eₙ₊₁ ≈ (f″(r)/(2f′(r)))·eₙ², where eₙ = xₙ − r is the error. Squaring the error roughly doubles the number of correct digits at each step, once the iterate is close enough.

## Key concepts

| Term | Meaning |
|---|---|
| Taylor polynomial Pₙ | The degree-n polynomial matching f and its first n derivatives at a |
| Remainder | f − Pₙ, the error of the approximation |
| Peano form | f − Pₙ = o((x − a)ⁿ); local, with no explicit bound |
| Lagrange form | f − Pₙ = f⁽ⁿ⁺¹⁾(ξ)(x − a)ⁿ⁺¹/(n + 1)! for some ξ between a and x |
| Taylor series | The power series ∑ f⁽ᵏ⁾(a)(x − a)ᵏ/k! |
| Smooth (C^∞) | Having derivatives of every order |
| Analytic | Equal to its Taylor series on a neighbourhood of each point |
| Quadratic convergence | Error at the next step bounded by a constant times the square of the current error |

## How it fits

- **Below:** The proof iterates Rolle's theorem from [the derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md). Taylor series are power series, whose radius comes from [series](../01-limits-and-convergence/series.md), and O and o come from [estimates and inequalities](../01-limits-and-convergence/estimates-and-inequalities.md).
- **Above:** The second-order expansion with the Hessian decides [extrema](../03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md). Numerical [interpolation and approximation](../../14-applied-and-computational-mathematics/01-numerical-analysis/interpolation-and-approximation.md) and [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) live on remainder bounds. In [complex analysis](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) every differentiable function is analytic.
- **Siblings:** [exp, sin and cos](the-exponential-and-trigonometric-functions.md) are defined by their Taylor series. The integral remainder uses [the fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md).

## Common misconceptions

- **"If f has derivatives of all orders, its Taylor series converges to f."** e^(−1/x²) is the counterexample (tenet 4).
- **"Adding more terms always improves the approximation."** Only inside the radius of convergence. For log(1 + x) at x = 2 the partial sums of x − x²/2 + x³/3 − ⋯ swing ever more wildly.
- **"The Taylor polynomial is the best polynomial approximation on an interval."** It is best near the single point a. Over a whole interval, other polynomials, such as those from Chebyshev interpolation, have smaller maximum error.

## Go deeper

- Michael Spivak, *Calculus* (4th edition, 2008): Taylor's theorem with every form of remainder, carefully proved.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): a gentle treatment of power series and Taylor's formula.
- E. Hairer and G. Wanner, *Analysis by Its History* (1996): how Newton, Taylor and Lagrange used series before analysis was rigorous.
