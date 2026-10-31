# Fourier Series

> **Layer:** [09 Advanced Analysis](../README.md) › [Harmonic Analysis](README.md)
> **Builds on:** [Hilbert Spaces](../03-functional-analysis/hilbert-spaces.md), [Lᵖ Spaces](../01-measure-and-integration/lp-spaces.md), [Uniform Convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md), [The Exponential and Trigonometric Functions](../../06-real-analysis/02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md), [Hahn–Banach and Baire Category](../03-functional-analysis/hahn-banach-and-baire-category.md)
> **Enables:** [The Fourier Transform](the-fourier-transform.md), [Fourier Analysis on Groups](fourier-analysis-on-groups.md), [The Heat Equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), [Fourier Analysis (computer science)](../../../cs-first-principles/01-mathematical-foundations/05-continuous-mathematics/fourier-analysis.md)

## Essence

A Fourier series writes a periodic function as a sum of pure oscillations, f(x) ~ ∑ f̂(n)·e^(inx), with coefficients f̂(n) = (1/2π)·∫ f(x)·e^(−inx) dx over one period. Joseph Fourier claimed in 1822 that every function can be so expanded and used the claim to solve the heat equation. The claim is true in the sense of L², where the exponentials form an orthonormal basis, and subtly false in the sense of pointwise convergence. Sorting out exactly when the series converges occupied mathematicians for 150 years and forced the creation of set theory, the Lebesgue integral and much of functional analysis.

## Core tenets

1. **In L² the series always converges, and energy is conserved.** The functions e^(inx), n ∈ ℤ, are orthonormal in L²(𝕋) with inner product (1/2π)·∫ f·ḡ, and their span is dense, since trigonometric polynomials uniformly approximate continuous functions (tenet 3). So by [Hilbert-space](../03-functional-analysis/hilbert-spaces.md) theory, the partial sums Sₙf converge to f in L² for every f ∈ L², and Parseval's identity holds: (1/2π)·∫ ∣f∣² = ∑ ∣f̂(n)∣². Applied to f(x) = x on (−π, π), where ∣f̂(n)∣ = 1/∣n∣ for n ≠ 0, it gives ∑ 1/n² = π²/6.

2. **Partial sums are convolutions with the Dirichlet kernel.** Sₙf = f ∗ Dₙ, where Dₙ(x) = ∑ e^(ikx) over ∣k∣ ≤ n, which sums to sin((n + ½)x)/sin(x/2). The kernel has integral 1, but it oscillates and changes sign, and its L¹ norm grows like (4/π²)·log n. That growth is the source of every pathology. Dirichlet proved in 1829 that for a piecewise smooth f the series converges at every point to the average of the left and right limits, the midpoint of any jump. Near a jump the partial sums overshoot by about 9% of the jump size however many terms are taken, the Gibbs phenomenon.

3. **Averaging the partial sums fixes convergence for continuous functions.** Lipót Fejér showed in 1900 that the averages σₙ = (S₀ + ⋯ + Sₙ)/(n + 1) converge uniformly to every continuous periodic f. The reason is that σₙf = f ∗ Fₙ, where the Fejér kernel Fₙ(x) = (1/(n + 1))·(sin((n + 1)x/2)/sin(x/2))² is non-negative with integral 1 and concentrates at 0, so σₙf is a weighted average of nearby values. Positivity is the hypothesis that matters: the Dirichlet kernel has the same integral and the same concentration of mass but is not positive, and it fails. A corollary is the Weierstrass approximation theorem for trigonometric polynomials.

4. **Continuity alone does not give convergence.** Paul du Bois-Reymond constructed in 1873 a continuous function whose Fourier series diverges at a point. The modern proof is soft: the functionals f ↦ Sₙf(0) on C(𝕋) have norms ‖Dₙ‖₁, which are unbounded, so the [uniform boundedness principle](../03-functional-analysis/hahn-banach-and-baire-category.md) says that for a generic continuous f the partial sums at 0 are unbounded. Uniform convergence does hold under slightly more regularity, for example Hölder continuity, by the Dini–Lipschitz test.

5. **The almost-everywhere story ends with Carleson.** Andrey Kolmogorov constructed an L¹ function whose Fourier series diverges almost everywhere (1923), and then one diverging everywhere (1926). Whether this could happen for L² remained open until Lennart Carleson proved in 1966 that the Fourier series of every L² function converges almost everywhere, settling a question posed by Luzin. Richard Hunt extended this to Lᵖ for every p > 1 in 1968. So the dividing line lies between L¹ and Lᵖ for p > 1. Carleson's proof is a famously delicate decomposition of the maximal partial-sum operator. Kahane and Katznelson showed that for any set of measure zero there is a continuous function whose series diverges on it, so "almost everywhere" cannot be improved.

6. **Smoothness and decay of coefficients are two sides of one coin.** Integration by parts shows that the coefficients of f′ are in·f̂(n), so if f has k integrable derivatives then f̂(n) = o(1/∣n∣ᵏ). The Riemann–Lebesgue lemma says f̂(n) → 0 for every integrable f, by approximating with step functions. Conversely, rapid decay of the coefficients makes the series converge to a smooth function. Analytic functions have exponentially decaying coefficients. This dictionary is why Fourier methods solve the [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md): the solution ∑ f̂(n)·e^(−n²t)·e^(inx) damps high frequencies instantly, so the temperature becomes smooth for every t > 0.

7. **Fourier series reach into number theory and dynamics.** Hermann Weyl's equidistribution criterion of 1916 says a sequence xₖ is equidistributed modulo 1 if and only if its exponential averages (1/N)·∑ e^(2πinxₖ) tend to 0 for each n ≠ 0. For xₖ = kα with α irrational these are geometric sums bounded by 2/∣1 − e^(2πinα)∣, divided by N, so the multiples of an irrational number fill [0, 1) evenly. The same idea of testing against characters drives [Fourier analysis on groups](fourier-analysis-on-groups.md).

## Key concepts

| Term | Meaning |
|---|---|
| Fourier coefficient | f̂(n) = (1/2π)·∫ f(x)·e^(−inx) dx |
| Partial sum Sₙf | ∑ f̂(k)·e^(ikx) over ∣k∣ ≤ n |
| Dirichlet kernel | sin((n + ½)x)/sin(x/2); its convolution gives Sₙf |
| Fejér kernel | The average of Dirichlet kernels; non-negative |
| Parseval's identity | (1/2π)·∫ ∣f∣² = ∑ ∣f̂(n)∣² |
| Gibbs phenomenon | The persistent overshoot of about 9% at a jump |
| Riemann–Lebesgue lemma | f̂(n) → 0 for integrable f |
| Carleson's theorem | Fourier series of L² functions converge almost everywhere |

## How it fits

- **Below:** [Hilbert spaces](../03-functional-analysis/hilbert-spaces.md) and [L²](../01-measure-and-integration/lp-spaces.md) give the right notion of convergence; [uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md) and the [exponential function](../../06-real-analysis/02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md) come from 06; [uniform boundedness](../03-functional-analysis/hahn-banach-and-baire-category.md) explains divergence.
- **Above:** separation of variables for the [heat](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) and [wave](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-wave-equation.md) equations in 10; [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md); signal processing, as in the computer-science treatment of [Fourier analysis](../../../cs-first-principles/01-mathematical-foundations/05-continuous-mathematics/fourier-analysis.md).
- **Siblings:** the [Fourier transform](the-fourier-transform.md) replaces the circle by the line; [Fourier analysis on groups](fourier-analysis-on-groups.md) replaces it by any locally compact abelian group; a Fourier series is the boundary value of a [Laurent series](../02-complex-analysis/singularities-and-residues.md).

## Common misconceptions

- **"The Fourier series of a continuous function converges to it"**: it can diverge at a point; only averages such as Fejér's are guaranteed to converge.
- **"The Gibbs overshoot disappears with more terms"**: it narrows but keeps its height of about 9% of the jump.
- **"Convergence in L² means convergence at points"**: it does not, and for L² the pointwise statement needed Carleson's deep theorem.

## Go deeper

- Thomas W. Körner, *Fourier Analysis* (1988): a wide-ranging, historical and lively account.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction* (2003): a clear first course with applications.
- Yitzhak Katznelson, *An Introduction to Harmonic Analysis* (1968): the convergence theory in depth.
