# Cauchy's Theorem and Its Consequences

> **Layer:** [09 Advanced Analysis](../README.md) › [Complex Analysis](README.md)
> **Builds on:** [Holomorphic Functions](holomorphic-functions.md), [Vector Calculus and the Integral Theorems](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md), [Uniform Convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md), [Homotopy and the Fundamental Group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md)
> **Enables:** [Singularities and Residues](singularities-and-residues.md), [Spectral Theory](../03-functional-analysis/spectral-theory.md), [Laplace's Equation and Harmonic Functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md), [The Prime Number Theorem](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md)

## Essence

Cauchy's theorem says that the integral of a holomorphic function around a closed curve is 0, provided the curve can be shrunk to a point without leaving the domain. From it follows the integral formula, which recovers the values of f inside a circle from its values on the circle. That formula is the source of nearly everything special about holomorphic functions: infinite differentiability, power series, Liouville's theorem, the maximum modulus principle and a two-line proof of the fundamental theorem of algebra. The one place where the integral is not 0, ∮ dz/z = 2πi around the origin, measures how a curve winds around a hole, and it becomes the residue theorem.

## Core tenets

1. **Cauchy's theorem: holomorphic functions integrate to 0 around contractible loops.** Let f be holomorphic on an open set U and γ a closed piecewise smooth curve in U that is homotopic in U to a constant curve. Then ∮_γ f(z) dz = 0. For f with continuous derivative it is Green's theorem: ∮ (u + iv)(dx + i dy) becomes a double integral of (−v_x − u_y) + i(u_x − v_y), which vanishes by Cauchy–Riemann. Édouard Goursat removed the continuity assumption by subdividing a triangle: if the integral around it were large, one of four sub-triangles carries a quarter of it, and nesting down to a point where f is nearly linear gives a contradiction.

2. **The hypothesis on the curve cannot be dropped: ∮ dz/z = 2πi.** On the unit circle z = e^(iθ), dz = i·e^(iθ) dθ, so the integral of 1/z is ∫₀^(2π) i dθ = 2πi. The function 1/z is holomorphic on ℂ ∖ {0}, but the circle cannot be shrunk to a point there. So the theorem detects topology: the value of ∮ f dz depends only on the homotopy class of the curve, and its failure on ℂ ∖ {0} is the [fundamental group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) at work. The number (1/2πi)·∮_γ dz/(z − a) is the winding number of γ about a.

3. **Cauchy's integral formula: boundary values determine interior values.** If the closed disc of radius r about z₀ lies in U and ∣z − z₀∣ < r, then

   ```
   f(z) = (1/2πi) ∮_(∣w−z₀∣=r) f(w)/(w − z) dw
   ```

   Proof idea: shrink the circle to a tiny one about z, which Cauchy's theorem allows for f(w)/(w − z) on the region between them, and let it shrink; f(w) ≈ f(z) there and ∮ dw/(w − z) = 2πi. Expanding 1/(w − z) as a geometric series in (z − z₀)/(w − z₀) turns the formula into a power series for f, convergent on the whole disc. Differentiating under the integral gives every derivative.

4. **Cauchy's estimates bound derivatives by size alone.** If ∣f∣ ≤ M on the circle of radius r about z₀, then ∣f⁽ⁿ⁾(z₀)∣ ≤ n!·M/rⁿ. For real functions nothing like this holds: sin(nx) is bounded by 1 with derivative n. One consequence is Weierstrass's theorem: a locally uniform limit of holomorphic functions is holomorphic, with derivatives converging too. A uniform limit of smooth real functions can be nowhere differentiable.

5. **Liouville's theorem: a bounded entire function is constant.** If ∣f∣ ≤ M on ℂ, Cauchy's estimate with n = 1 gives ∣f′(z₀)∣ ≤ M/r for every r, so f′ = 0. Both hypotheses matter: sin is bounded on ℝ but not entire-and-bounded, since sin(iy) = i·sinh y; and 1/z is bounded far out but not entire. Liouville's theorem also shows that the spectrum of a bounded operator is non-empty, in [spectral theory](../03-functional-analysis/spectral-theory.md).

6. **The fundamental theorem of algebra follows in two lines.** Let p be a polynomial of degree n ≥ 1 with no root. Then 1/p is entire, and since ∣p(z)∣ → ∞ as ∣z∣ → ∞ it is bounded, so by Liouville it is constant, which is absurd. So every non-constant complex polynomial has a root, and by induction it factors into n linear factors.

7. **Maximum modulus: ∣f∣ has no interior maximum.** Taking z = z₀ in the integral formula gives the mean value property: f(z₀) is the average of f over any circle about z₀. If ∣f∣ had a local maximum at z₀, the average could reach ∣f(z₀)∣ only if ∣f∣ were constant on every small circle, which forces f to be constant nearby and, by the identity theorem, everywhere on a connected domain. On a bounded domain, ∣f∣ therefore attains its maximum on the boundary. The same averaging gives the maximum principle for [harmonic functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md).

8. **Morera's theorem is the converse.** If f is continuous on U and ∮ f dz = 0 around every triangle in U, then f is holomorphic. The integrals define a primitive F with F′ = f, and F, being holomorphic, has holomorphic derivatives. It is the practical way to prove that a limit or integral of holomorphic functions is holomorphic.

## Key concepts

| Term | Meaning |
|---|---|
| Contour integral | ∮_γ f(z) dz = ∫ f(γ(t))·γ′(t) dt along a piecewise smooth curve |
| Cauchy's theorem | ∮_γ f dz = 0 for f holomorphic on U and γ contractible in U |
| Winding number | (1/2πi)·∮_γ dz/(z − a), the number of turns of γ about a |
| Cauchy's integral formula | f(z) = (1/2πi)·∮ f(w)/(w − z) dw for z inside the circle |
| Cauchy's estimates | ∣f⁽ⁿ⁾(z₀)∣ ≤ n!·M/rⁿ when ∣f∣ ≤ M on the circle of radius r |
| Liouville's theorem | Bounded entire functions are constant |
| Maximum modulus principle | A non-constant holomorphic ∣f∣ has no local maximum in the domain |
| Morera's theorem | Continuous with vanishing triangle integrals implies holomorphic |

## How it fits

- **Below:** the [integral theorems of vector calculus](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md) give the first proof; [homotopy](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) gives the right hypothesis; [uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md) is what Weierstrass's theorem strengthens.
- **Above:** contour integrals relate the zeros of the [zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md) to primes in the [prime number theorem](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md); the mean value property drives potential theory in 10.
- **Siblings:** [residues](singularities-and-residues.md) handle the curves that wind around singularities; [conformal maps](conformal-maps-and-the-riemann-mapping-theorem.md) use the estimates to extract convergent subsequences; [spectral theory](../03-functional-analysis/spectral-theory.md) borrows Liouville.

## Common misconceptions

- **"Cauchy's theorem holds for any closed curve in the domain"**: only for curves that can be shrunk to a point there, as 1/z on the unit circle shows.
- **"The fundamental theorem of algebra is a theorem of algebra"**: every proof needs some analysis or topology, because ℝ is defined by completeness.
- **"Bounded on a line means bounded"**: Liouville's theorem needs boundedness on all of ℂ.

## Go deeper

- Lars V. Ahlfors, *Complex Analysis* (3rd edition, 1979): the general homology form of Cauchy's theorem, carefully proved.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (2003): Goursat's proof and its consequences, with many applications.
- Tristan Needham, *Visual Complex Analysis* (1997): ∮ dz/z = 2πi, seen geometrically.
