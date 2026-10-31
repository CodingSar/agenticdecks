# Interpolation and Approximation

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Numerical Analysis](README.md)
> **Builds on:** [Polynomial Rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md), [Taylor Expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md), [Uniform Convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md), [Fourier Series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [Floating Point, Conditioning and Stability](floating-point-conditioning-and-stability.md)
> **Enables:** [Numerical Methods for Differential Equations](numerical-methods-for-differential-equations.md), [Error-Correcting Codes](../03-information-codes-and-cryptography/error-correcting-codes.md), [Sampling and Compressed Sensing](../06-data-and-learning/sampling-and-compressed-sensing.md), [The Mathematics of Deep Learning](../06-data-and-learning/the-mathematics-of-deep-learning.md)

## Essence

To compute with a function you must replace it by something finite, usually a polynomial or piecewise polynomial. Interpolation matches the function exactly at chosen nodes; approximation asks only to be uniformly close. Through n + 1 points passes exactly one polynomial of degree at most n, but where the points lie decides everything: equally spaced nodes can make interpolants diverge, while Chebyshev nodes give convergence as fast as the smoothness of the function allows. Splines give up a single formula for robust low-degree pieces.

## Core tenets

1. **Through n + 1 points with distinct nodes passes exactly one polynomial of degree at most n.** Two such polynomials differ by one of degree at most n with n + 1 roots, which must be zero. For existence, the Lagrange basis polynomial ℓₖ(x) = ∏_(j≠k) (x − xⱼ)/(xₖ − xⱼ) is 1 at xₖ and 0 at the other nodes, so p = ∑ yₖℓₖ. Only field operations are used, so this works over finite fields, giving Reed–Solomon codes and Adi Shamir's secret sharing (1979).

2. **The error is a high derivative times the node polynomial.** If f has n + 1 continuous derivatives on an interval I containing x and the nodes, then for some ξ in I

   ```
   f(x) − p(x) = f⁽ⁿ⁺¹⁾(ξ) / (n + 1)! · ω(x),     ω(x) = (x − x₀)(x − x₁)⋯(x − xₙ)
   ```

   Choose c so that g = f − p − cω vanishes at x as well as at the nodes; Rolle's theorem applied n + 1 times gives a zero ξ of g⁽ⁿ⁺¹⁾ = f⁽ⁿ⁺¹⁾ − c(n + 1)!. When the nodes coalesce, this is Taylor's remainder. The derivative belongs to f; ω is ours to choose.

3. **Equally spaced nodes can make interpolation diverge.** Carl Runge (1901) interpolated f(x) = 1/(1 + 25x²) on [−1, 1] at equally spaced nodes: the maximum error is about 1.9 for n = 10, 60 for n = 20 and 10⁵ for n = 40. The culprits are the complex poles of f at ±i/5, close to the interval, and a node polynomial that for n = 40 is about 3 × 10¹⁰ times larger near the ends than near the centre. This is Runge's phenomenon.

4. **Chebyshev nodes minimise the node polynomial and converge geometrically for analytic functions.** With x = cos θ, the Chebyshev polynomial T_m(x) = cos(mθ) has leading coefficient 2^(m−1) and takes the values ±1 alternately at m + 1 points, so T_m/2^(m−1) is the monic polynomial of degree m with the smallest maximum on [−1, 1]: a monic competitor with a smaller maximum would differ from it by a polynomial of degree below m with m sign changes. Taking as nodes the zeros of T_(n+1), which crowd towards the ends, makes ω = T_(n+1)/2ⁿ. If f is analytic inside the ellipse with foci ±1 and semi-axis sum ρ > 1, the error falls like ρ⁻ⁿ: Runge's poles give ρ = (1 + √26)/5 ≈ 1.22, and errors 0.11, 0.015 and 2.9 × 10⁻⁴ for n = 10, 20 and 40.

5. **At good nodes, interpolation is nearly as good as the best approximation.** Interpolation reproduces polynomials, so if p* is the best approximation of degree n and I is the interpolation operator, then f − p = (f − p*) − I(f − p*), and the error of p is at most 1 + Λₙ times that of p*. The Lebesgue constant Λₙ grows like (2/π) log n at Chebyshev nodes but exponentially at equally spaced ones.

6. **Every continuous function is a uniform limit of polynomials, but no fixed nodes interpolate them all.** Karl Weierstrass proved the first claim in 1885. Sergei Bernstein's 1912 proof is probabilistic: on [0, 1], Bₙf(x) = ∑ₖ f(k/n) C(n, k) xᵏ(1 − x)ⁿ⁻ᵏ is the expected value of f(Sₙ/n) for Sₙ binomial(n, x); Sₙ/n has variance at most 1/(4n), so it concentrates near x uniformly in x, and uniform continuity of f does the rest. But Georg Faber (1914) proved that for every choice of nodes, one set for each n, some continuous function has interpolants that do not converge uniformly.

7. **Splines trade one high-degree polynomial for many cubic pieces.** A cubic spline is a twice continuously differentiable function that is cubic between consecutive knots; interpolating needs only a tridiagonal solve. The natural spline, with zero second derivative at the ends, minimises the bending energy ∫ s″(x)² dx among all twice continuously differentiable interpolants. With suitable end conditions the error for smooth f is O(h⁴), where h is the knot spacing, and no Runge instability, because each piece depends mostly on nearby data. Isaac Schoenberg founded the theory in 1946; B-splines, bell-shaped basis splines each nonzero on a few intervals, define the curves of computer-aided design.

## Key concepts

| Term | Meaning |
|---|---|
| Lagrange basis ℓₖ | The polynomial of degree n equal to 1 at node xₖ and 0 at the others |
| Node polynomial ω | (x − x₀)⋯(x − xₙ), the factor of the error that the nodes control |
| Lebesgue constant Λₙ | The maximum over x of ∑ ∣ℓₖ(x)∣: how much interpolation can amplify errors |
| Best approximation p* | The degree-n polynomial with smallest maximum error, characterised by its error attaining the maximum with alternating signs at n + 2 points |
| Cubic spline | A twice continuously differentiable piecewise cubic |

## How it fits

- **Below:** uniqueness is the root bound for [polynomials over a field](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md); the error formula generalises [Taylor's theorem](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md); Weierstrass's theorem concerns [uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md); Chebyshev series are [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) of f(cos θ); Faber's theorem follows from the uniform boundedness principle of [Baire category](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md).
- **Above:** [time-stepping methods](numerical-methods-for-differential-equations.md) and quadrature integrate interpolants, and Gauss's n-point rule is exact up to degree 2n − 1; [Reed–Solomon codes](../03-information-codes-and-cryptography/error-correcting-codes.md) are decoded by interpolation over a finite field; [sampling theory](../06-data-and-learning/sampling-and-compressed-sensing.md) interpolates band-limited signals exactly; universal approximation in [deep learning](../06-data-and-learning/the-mathematics-of-deep-learning.md) is a Weierstrass theorem for neural networks.
- **Siblings:** the spline system is a banded problem of [numerical linear algebra](numerical-linear-algebra.md); the secant method of [root-finding](root-finding-and-newtons-method.md) is linear interpolation; grids in d dimensions need nᵈ points, which is why [Monte Carlo methods](monte-carlo-methods.md) win in high dimension; Chebyshev series are computed by the [fast Fourier transform](the-fast-fourier-transform-and-spectral-methods.md).

## Common misconceptions

- **"More nodes always give a better interpolant"**: at equally spaced nodes the error can grow without bound, even in exact arithmetic.
- **"High-degree polynomial interpolation is numerically hopeless"**: only in the monomial basis or at badly placed nodes; at Chebyshev nodes, with the barycentric formula, degrees in the thousands are routine.

## Go deeper

- Lloyd N. Trefethen, *Approximation Theory and Approximation Practice* (2013): Chebyshev technology, with code.
- Carl de Boor, *A Practical Guide to Splines* (1978; revised edition 2001): the standard reference.
- Philip J. Davis, *Interpolation and Approximation* (1963): the classical theory.
