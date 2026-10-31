# Holomorphic Functions

> **Layer:** [09 Advanced Analysis](../README.md) › [Complex Analysis](README.md)
> **Builds on:** [The Complex Numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md), [The Derivative as a Linear Map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Series](../../06-real-analysis/01-limits-and-convergence/series.md), [The Exponential and Trigonometric Functions](../../06-real-analysis/02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md)
> **Enables:** [Cauchy's Theorem and Its Consequences](cauchys-theorem-and-its-consequences.md), [Conformal Maps and the Riemann Mapping Theorem](conformal-maps-and-the-riemann-mapping-theorem.md), [Laplace's Equation and Harmonic Functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md)

## Essence

A function f of a complex variable is holomorphic on an open set if the limit f′(z) = lim (f(z + h) − f(z))/h exists at every point, with h → 0 through complex values. The definition looks like the real one, but it asks far more: the same limit must arise from every direction in the plane. Written in real coordinates this is the pair of Cauchy–Riemann equations, which say the derivative is a rotation followed by a scaling. That one condition has startling consequences: a function that is complex differentiable once is differentiable infinitely often and equals its Taylor series, its real and imaginary parts are harmonic, and its zeros are isolated. Nothing like this holds for real functions.

## Core tenets

1. **Complex differentiability is the Cauchy–Riemann equations.** Write f = u + iv with z = x + iy. Letting h → 0 along the real axis gives f′ = u_x + i·v_x; along the imaginary axis it gives f′ = v_y − i·u_y. Equating the two:

   ```
   u_x = v_y,      u_y = −v_x
   ```

   Conversely, if u and v are real-differentiable at a point and satisfy these equations there, f is complex differentiable there. So holomorphy is real differentiability plus two partial differential equations.

2. **The derivative is a rotation and a scaling.** As a real-linear map of ℝ², the derivative of f has Jacobian matrix [[u_x, u_y], [v_x, v_y]], which by Cauchy–Riemann is [[a, −b], [b, a]] with f′(z) = a + ib. That matrix is multiplication by the complex number f′(z): it scales by ∣f′(z)∣ and rotates by arg f′(z). So where f′ ≠ 0, f preserves angles and orientation; it is [conformal](conformal-maps-and-the-riemann-mapping-theorem.md). Complex conjugation z ↦ z̄ is real-linear but reverses orientation, has matrix [[1, 0], [0, −1]], and is complex differentiable nowhere, although it is as smooth as a real map can be.

3. **Power series are holomorphic inside their disc of convergence.** A series ∑ aₙ(z − z₀)ⁿ converges absolutely on an open disc of radius R = 1/limsup ∣aₙ∣^(1/n) and diverges outside it, and it can be differentiated term by term there. This defines exp, sin and cos on all of ℂ, with e^(iθ) = cos θ + i sin θ. The radius is the distance to the nearest point where the function cannot be continued holomorphically, which explains real puzzles: 1/(1 + x²) is smooth on all of ℝ, yet its Taylor series at 0 has radius 1, because of the poles at ±i.

4. **One complex derivative forces all of them, and a convergent Taylor series.** If f is holomorphic on an open set, then f is infinitely differentiable, and on every disc inside the set f equals its Taylor series. The proof goes through [Cauchy's integral formula](cauchys-theorem-and-its-consequences.md), which writes f as an integral of 1/(w − z) and expands that kernel in a geometric series. Goursat's lemma shows that no continuity of f′ needs to be assumed. The real contrast is total: e^(−1/x²), extended by 0 at x = 0, is infinitely differentiable on ℝ, yet every derivative vanishes at 0, so its Taylor series is 0 and represents the function only at that point.

5. **Real and imaginary parts are harmonic.** Differentiating the Cauchy–Riemann equations gives u_xx = v_yx = v_xy = −u_yy, so Δu = u_xx + u_yy = 0, and likewise Δv = 0. Conversely, on a simply connected domain every harmonic u is the real part of a holomorphic function. This is why two-dimensional potential theory, ideal fluid flow and electrostatics reduce to complex analysis, and why [Laplace's equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) in the plane is solved by conformal maps.

6. **Zeros are isolated, so a holomorphic function is determined by very little.** If f is holomorphic on a connected open set and not identically 0, then near a zero z₀ it factors as (z − z₀)ᵏ·g(z) with g(z₀) ≠ 0, so z₀ is the only zero nearby. Hence two holomorphic functions on a connected set that agree on a set with a limit point inside it agree everywhere (the identity theorem). Smooth real functions are not rigid: a bump function vanishes on an interval without vanishing everywhere. The identity theorem is the basis of [analytic continuation](analytic-continuation-and-riemann-surfaces.md).

7. **Non-constant holomorphic maps are open.** A non-constant holomorphic function on a connected open set maps open sets to open sets. Near a point where f(z) − f(z₀) has a zero of order k, f behaves like z ↦ zᵏ, which covers a small disc around f(z₀) k times. In particular ∣f∣ cannot have a local maximum at an interior point, the seed of the maximum modulus principle.

## Key concepts

| Term | Meaning |
|---|---|
| Holomorphic | Complex differentiable at every point of an open set |
| Analytic | Locally equal to a convergent power series; for complex functions the same as holomorphic |
| Entire | Holomorphic on all of ℂ, like exp, sin and polynomials |
| Cauchy–Riemann equations | u_x = v_y and u_y = −v_x for f = u + iv |
| Radius of convergence | R = 1/limsup ∣aₙ∣^(1/n); the series converges for ∣z − z₀∣ < R |
| Harmonic function | A real C² function with Δu = 0 |
| Identity theorem | Holomorphic functions agreeing on a set with a limit point agree on the connected domain |
| Open mapping theorem | Non-constant holomorphic functions map open sets to open sets |

## How it fits

- **Below:** [complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) supply the field; the [derivative as a linear map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md) explains Cauchy–Riemann; [series](../../06-real-analysis/01-limits-and-convergence/series.md) and the [exponential function](../../06-real-analysis/02-calculus-of-one-variable/the-exponential-and-trigonometric-functions.md) give the first examples.
- **Above:** [harmonic functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) in 10; the [Riemann zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md) and [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md) in 12 are holomorphic functions.
- **Siblings:** [Cauchy's theorem](cauchys-theorem-and-its-consequences.md) proves tenet 4; [conformal maps](conformal-maps-and-the-riemann-mapping-theorem.md) develop tenet 2; [analytic continuation](analytic-continuation-and-riemann-surfaces.md) develops tenet 6.

## Common misconceptions

- **"Complex differentiable is real differentiable in two variables"**: z ↦ z̄ is real-linear and nowhere complex differentiable; the Cauchy–Riemann equations are the extra demand.
- **"Smooth functions equal their Taylor series"**: e^(−1/x²) is smooth on ℝ and not analytic at 0; only in the complex setting does one derivative imply analyticity.
- **"Bounded on ℝ means bounded"**: sin is bounded on ℝ, but sin(iy) = i·sinh y grows exponentially.

## Go deeper

- Tristan Needham, *Visual Complex Analysis* (1997): the geometry of the derivative as an amplitwist, in pictures.
- Lars V. Ahlfors, *Complex Analysis* (3rd edition, 1979): the classic concise course.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (2003): a modern course with applications to number theory and Fourier analysis.
