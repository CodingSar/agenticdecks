# The Exponential and Trigonometric Functions

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of One Variable](README.md)
> **Builds on:** [Series](../01-limits-and-convergence/series.md), [Uniform convergence](../01-limits-and-convergence/uniform-convergence.md), [The derivative and the mean value theorem](the-derivative-and-the-mean-value-theorem.md), [Taylor expansion](taylor-expansion.md), [The complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md)
> **Enables:** [Linear systems and the matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md), [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [Lie groups and Lie algebras](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md), [Compartment models and exponential processes (medicine)](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md)

## Essence

School mathematics defines powers by roots and sin and cos by triangles, then assumes their derivatives. Analysis reverses the order. It defines one function, exp, by a power series that converges for every complex number, and derives everything else from it: the law exp(a + b) = exp(a)·exp(b), the logarithm, real powers, cos and sin, and even the number π. Geometry then becomes a theorem rather than an assumption. The payoff is Euler's formula, exp(ix) = cos x + i sin x, which shows that growth and rotation are the same function seen along two different directions in ℂ.

## Core tenets

1. **exp is defined by a power series that converges everywhere.** For every complex z,
   ```
   exp(z) = ∑ zⁿ/n! = 1 + z + z²/2! + z³/3! + ⋯
   ```
   The ratio of successive terms is |z|/(n + 1) → 0, so the ratio test gives an infinite radius of convergence, and the Weierstrass M-test gives uniform convergence on every bounded set. Hence exp is continuous, and differentiating term by term gives exp′ = exp with exp(0) = 1. Equivalently, exp is the unique solution of y′ = y with y(0) = 1.

2. **The functional equation exp(a + b) = exp(a)·exp(b) follows from the binomial theorem.** Both series converge absolutely, so their Cauchy product converges to the product:
   ```
   exp(a)·exp(b) = ∑ₙ ∑ₖ aᵏ bⁿ⁻ᵏ/(k!·(n − k)!) = ∑ₙ (a + b)ⁿ/n! = exp(a + b)
   ```
   The middle step is the binomial theorem divided by n!. A second proof uses only the differential equation: for fixed c, g(x) = exp(x)·exp(c − x) has derivative 0, so it is constant by the mean value theorem (MVT), equal to g(0) = exp(c). So exp(x)·exp(−x) = 1, and exp never vanishes.

3. **On ℝ, exp is an increasing bijection onto (0, ∞), and its inverse is the logarithm.** exp(x) = exp(x/2)² > 0, so exp′ > 0 and exp is strictly increasing. For x ≥ 0, exp(x) ≥ 1 + x → ∞, and exp(−x) = 1/exp(x) → 0, so the intermediate value theorem (IVT) makes it onto (0, ∞). Its inverse log has log′(y) = 1/y, recovering the integral definition of ln. Real powers are then defined by aˣ = exp(x·log a), and e = exp(1) = lim(1 + 1/n)ⁿ, because n·log(1 + 1/n) → log′(1) = 1.

4. **cos and sin are defined from exp, and Euler's formula is their definition.** Set cos x and sin x to be the real and imaginary parts of exp(ix) for real x. Splitting the series into even and odd terms gives cos x = 1 − x²/2! + x⁴/4! − ⋯ and sin x = x − x³/3! + ⋯, so exp(ix) = cos x + i sin x. The conjugate of exp(ix) is exp(−ix), so |exp(ix)|² = exp(ix)·exp(−ix) = 1, which is cos² x + sin² x = 1. Differentiating gives cos′ = −sin and sin′ = cos, and tenet 2 with a = ix, b = iy gives the addition formulas.

5. **π is defined analytically, as twice the first positive zero of cos.** cos 0 = 1. The series for cos 2 alternates with decreasing terms after the second, so
   ```
   cos 2 < 1 − 2 + 16/24 = −1/3 < 0
   ```
   By the IVT, cos has a zero in (0, 2), and the zero set is closed and avoids a neighbourhood of 0, so there is a least positive zero. Call it π/2. On (0, π/2), sin′ = cos > 0, so sin rises from 0 to 1, giving exp(iπ/2) = i. Hence exp(iπ) = −1, exp(2πi) = 1, and exp(z) = 1 if and only if z is an integer multiple of 2πi. No triangle or circle was used.

6. **The geometric π agrees with the analytic one.** The curve t ↦ exp(it) has velocity i·exp(it), of length 1, so it runs round the unit circle at unit speed. By tenet 5 it first returns to 1 at t = 2π and covers the circle once on [0, 2π). So the circumference is 2π, and the angle t is genuinely arc length. Multiplying by exp(iθ) rotates ℂ through θ, which gives every complex number a polar form r·exp(iθ).

7. **exp is the only continuous solution of the functional equation, but continuity is essential.** If f: ℝ → ℝ is continuous and f(a + b) = f(a)·f(b), then f is 0 or f(x) = exp(cx) for some c: f is non-negative, vanishes everywhere if anywhere, and otherwise log f is a continuous additive function, hence linear. Without continuity there are wild solutions, built from a basis of ℝ as a vector space over ℚ, needing the axiom of choice.

## Key concepts

| Term | Meaning |
|---|---|
| Exponential function | exp(z) = ∑zⁿ/n!, defined for every complex z |
| Functional equation | exp(a + b) = exp(a)·exp(b) |
| Logarithm | The inverse of exp: (0, ∞) → ℝ, with log′(y) = 1/y |
| Real power aˣ | exp(x·log a), for a > 0 |
| Euler's formula | exp(ix) = cos x + i sin x |
| π | Twice the least positive zero of cos |
| Period | exp(z + 2πi) = exp(z), and 2πi generates all periods |
| Polar form | z = r·exp(iθ), with r = ∣z∣ |

## How it fits

- **Below:** [Series](../01-limits-and-convergence/series.md) gives the radius and the Cauchy product; [uniform convergence](../01-limits-and-convergence/uniform-convergence.md) licenses termwise differentiation; [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) supply the field in which exp(ix) lives.
- **Above:** The same series defines the [matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md) that solves y′ = Ay, and the exponential map of a [Lie group](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md). [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) study exp and its many-valued inverse on ℂ, and [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) expand functions in exp(inx). In pharmacology, first-order elimination is exponential decay: see [compartment models (medicine)](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/03-systems-and-models/compartment-models-and-exponential-processes.md).
- **Siblings:** [Taylor expansion](taylor-expansion.md) explains why the series is the right one. [The fundamental theorem of calculus](the-fundamental-theorem-of-calculus.md) gives the alternative route through ln as an integral.

## Common misconceptions

- **"exp(A + B) = exp(A)·exp(B) for matrices too."** The binomial step in tenet 2 needs ab = ba. For matrices it holds when AB = BA and fails in general.
- **"π is defined by circles, so analysis cannot reach it."** Tenet 5 defines π from a power series, and tenet 6 proves it is the circle constant. That analytic handle is what proves π irrational and, by Lindemann in 1882, transcendental (Hermite proved e transcendental in 1873). Whether π + e is irrational is open as of 2026.
- **"The complex logarithm is just the inverse of exp."** exp is not injective on ℂ, since exp(z + 2πi) = exp(z), so log z is defined only up to multiples of 2πi.

## Go deeper

- Walter Rudin, *Real and Complex Analysis* (3rd edition, 1987): the prologue builds exp, π and the circle exactly as here.
- Michael Spivak, *Calculus* (4th edition, 2008): constructs the trigonometric functions rigorously and proves π irrational.
- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): power series and termwise differentiation in detail.
