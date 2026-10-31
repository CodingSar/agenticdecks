# Multiple Integrals and Change of Variables

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of Several Variables](README.md)
> **Builds on:** [The Riemann integral](../02-calculus-of-one-variable/the-riemann-integral.md), [The fundamental theorem of calculus](../02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md), [The derivative as a linear map](the-derivative-as-a-linear-map.md), [Inverse and implicit function theorems](inverse-and-implicit-function-theorems.md), [Determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md)
> **Enables:** [Vector calculus and the integral theorems](vector-calculus-and-the-integral-theorems.md), [Measure and sigma-algebras](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md), [The Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md), [Random variables and distributions](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md), [Ray tracing and global illumination (CS)](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md)

## Essence

The integral of a function over a region of ℝⁿ is defined exactly as in one variable, by squeezing between upper and lower sums, now over grids of small boxes. Two theorems make it computable. Fubini's theorem reduces a multiple integral to repeated one-variable integrals, each handled by the fundamental theorem of calculus. The change of variables formula lets the region be reparametrised, at the cost of a factor |det Dφ| that measures how the substitution stretches volume. That factor is where linear algebra enters: a determinant is the volume scaling of a linear map, and a smooth map is locally linear.

## Core tenets

1. **The integral over a box is a squeeze of sums over sub-boxes.** Partition a box B = [a₁, b₁] × ⋯ × [aₙ, bₙ] into a grid of sub-boxes. Upper and lower sums use the sup and inf of f on each sub-box times its volume, and f is integrable when the two can be squeezed together. Continuous functions on B are integrable, by uniform continuity. To integrate over a bounded region E, integrate f·1_E over a box containing E. This works when the boundary of E has content zero, meaning it can be covered by finitely many boxes of arbitrarily small total volume. The graph of a continuous function has content zero, so regions bounded by such graphs are fine.

2. **Fubini's theorem: for continuous f on a rectangle [a, b] × [s, t], the double integral equals either iterated integral.**
   ```
   ∬ f = ∫ₐᵇ ( ∫ₛᵗ f(x, y) dy ) dx = ∫ₛᵗ ( ∫ₐᵇ f(x, y) dx ) dy
   ```
   Proof idea: a Riemann sum over a grid can be added up row by row or column by column, and each inner sum approximates an inner integral. In n variables the same argument reduces everything to n one-variable integrals.

3. **Without integrability, the order of integration can matter.** On [0, 1]², let f(x, y) = (x² − y²)/(x² + y²)². Since f is the y-derivative of y/(x² + y²), the inner integral over y is 1/(1 + x²), and integrating over x gives π/4. By the symmetry f(y, x) = −f(x, y), the other order gives −π/4. The function is unbounded near the origin and the integral of |f| is infinite, so Fubini does not apply.

4. **Change of variables: volume scales by the absolute value of the Jacobian determinant.** Let φ be a C¹ bijection from an open set U onto an open set V, with Dφ invertible everywhere, so that φ⁻¹ is C¹ by the [inverse function theorem](inverse-and-implicit-function-theorems.md). For f integrable on V,
   ```
   ∫_V f(x) dx = ∫_U f(φ(u)) · |det Dφ(u)| du
   ```
   Why: a linear map A sends the unit cube to a parallelepiped of volume |det A|, which is the geometric meaning of the [determinant](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md). Near each point φ is close to its derivative, so a tiny box around u is sent to a near-parallelepiped of volume about |det Dφ(u)| times its own. The absolute value appears because volume has no sign. In one variable the formula carries no absolute value because ∫ₐᵇ is oriented: swapping the limits changes the sign.

5. **Polar coordinates evaluate an integral that has no elementary antiderivative.** For x = r cos θ, y = r sin θ the Jacobian determinant is r, so dx dy becomes r dr dθ. Let I be the integral of e^(−x²) over ℝ. Then
   ```
   I² = ∬ e^(−(x² + y²)) dx dy = ∫₀^2π ∫₀^∞ e^(−r²) r dr dθ = 2π · ½ = π
   ```
   so I = √π, the constant in the normal distribution. The integrals are improper, and are justified as limits over growing discs and squares.

6. **High-dimensional volume behaves unexpectedly.** The same method gives the volume of the unit ball in ℝⁿ as π^(n/2)/Γ(n/2 + 1), where Γ is the gamma function: π for n = 2 and 4π/3 for n = 3, and tending to 0 as n grows. Since volume scales as rⁿ, the fraction of the ball within distance ε of its surface is 1 − (1 − ε)ⁿ, which tends to 1. In high dimensions almost all the volume of a ball is near its boundary, a fact behind many surprises in data analysis.

7. **Probability densities transform by the same rule.** If a random vector X has density p and Y = φ(X), the density of Y at y is p(φ⁻¹(y)) times |det Dφ⁻¹(y)|. The Box–Muller method uses polar coordinates to turn two independent uniform random numbers into two independent normal ones. [Random variables](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md) make this rigorous with measure theory, and Monte Carlo methods in [ray tracing (CS)](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md) estimate multiple integrals by random sampling.

## Key concepts

| Term | Meaning |
|---|---|
| Box | A product of closed intervals [a₁, b₁] × ⋯ × [aₙ, bₙ] |
| Content zero | Coverable by finitely many boxes of arbitrarily small total volume |
| Jordan measurable region | A bounded region whose boundary has content zero |
| Iterated integral | An integral of an integral, one variable at a time |
| Fubini's theorem | The multiple integral equals the iterated integrals, for integrable f |
| Diffeomorphism | A C¹ bijection with C¹ inverse |
| Jacobian determinant | det Dφ, the local volume scaling of φ |
| Polar coordinates | x = r cos θ, y = r sin θ, with dx dy = r dr dθ |

## How it fits

- **Below:** The squeeze generalises [the Riemann integral](../02-calculus-of-one-variable/the-riemann-integral.md); each iterated integral is computed by [the fundamental theorem of calculus](../02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md); [determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md) give the scaling factor.
- **Above:** [Measure](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) and [the Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) extend Fubini to the Fubini–Tonelli theorem, with clean hypotheses. Densities and expectations in [probability](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md) are multiple integrals.
- **Siblings:** [Vector calculus](vector-calculus-and-the-integral-theorems.md) integrates over curves and surfaces using the same parametrisation idea. [The derivative as a linear map](the-derivative-as-a-linear-map.md) supplies Dφ.

## Common misconceptions

- **"The order of integration never matters."** It does when f is not absolutely integrable (tenet 3).
- **"In polar coordinates, dx dy = dr dθ."** The Jacobian factor r is essential; without it the area of a disc of radius R would come out as 2πR.
- **"The change of variables factor is det Dφ."** For volumes it is |det Dφ|; the signed version belongs to oriented integrals and [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md).

## Go deeper

- James R. Munkres, *Analysis on Manifolds* (1991): the Riemann integral in ℝⁿ and a complete proof of the change of variables theorem.
- Michael Spivak, *Calculus on Manifolds* (1965): chapter 3 treats integration, Fubini and change of variables concisely.
- Jerrold E. Marsden and Anthony Tromba, *Vector Calculus* (6th edition, 2012): computational practice with many coordinate systems.
