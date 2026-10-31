# Root-Finding and Newton's Method

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Numerical Analysis](README.md)
> **Builds on:** [Continuity](../../06-real-analysis/01-limits-and-convergence/continuity.md), [Taylor Expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [Iterated Maps](../../10-differential-equations-and-dynamics/04-dynamical-systems/iterated-maps.md), [Floating Point, Conditioning and Stability](floating-point-conditioning-and-stability.md)
> **Enables:** [Numerical Methods for Differential Equations](numerical-methods-for-differential-equations.md), [Convex Optimisation and Duality](../02-optimisation/convex-optimisation-and-duality.md), [Mathematical Finance](../05-games-decisions-and-finance/mathematical-finance.md)

## Essence

Most equations f(x) = 0 have no formula for their solutions, so we guess and improve. Most methods are iterations x_(n+1) = g(xₙ) built so that the root is a fixed point of g, and the questions are always the same: does it converge, from where, and how fast? Bisection is slow and certain. Newton's method replaces f by its tangent line and, near a simple root, doubles the number of correct digits at every step; far from a root it can cycle, diverge or wander between fractal basins of attraction.

## Core tenets

1. **Bisection always converges, gaining one bit per step.** If f is continuous on [a, b] and f(a), f(b) have opposite signs, the intermediate value theorem gives a root; keeping the half-interval on which the sign still changes traps a root in an interval of length (b − a)/2ⁿ after n steps. From [1, 2], 52 steps reach the spacing of double-precision numbers. Continuity is essential: 1/x changes sign on [−1, 1], and bisection converges to the pole at 0.

2. **Fixed-point iteration converges where the map contracts.** Rewrite f(x) = 0 as x = g(x) and iterate. If g maps an interval into itself with ∣g′∣ ≤ L < 1 there, the contraction mapping principle gives a unique fixed point x* and errors shrinking by about ∣g′(x*)∣ per step: linear convergence. Iterating cos from any real start converges to 0.739085…, because after two steps the iterates lie in [cos 1, 1], where ∣sin x∣ ≤ sin 1 < 1. The choice of g is everything: for √2, the map x ↦ 2/x has g′ = −1 at the root and sends 1 to 2 and back forever, while x ↦ (x + 2/x)/2 converges.

3. **Newton's method converges quadratically near a simple root.** Replace f by its tangent at xₙ and solve: x_(n+1) = xₙ − f(xₙ)/f′(xₙ). Taylor's theorem with remainder gives, for the error eₙ = xₙ − x*,

   ```
   e_(n+1) = ( f″(ξ) / (2 f′(xₙ)) ) · eₙ²     for some ξ between xₙ and x*
   ```

   so if f′(x*) ≠ 0 and f″ is continuous, the number of correct digits roughly doubles once the error is small. For f(x) = x² − 2 from x₀ = 1 (Heron's method) the iterates are 1.5, 1.41667, 1.4142157 and 1.41421356237469, with errors 0.086, 0.0025, 2.1 × 10⁻⁶ and 1.6 × 10⁻¹².

4. **Each hypothesis has its own failure.** At a double root, where f′(x*) = 0, convergence drops to linear: for x², Newton halves the error each step, and at a root of multiplicity m the error ratio is (m − 1)/m. Far from a root the tangent can point anywhere: for x³ − 2x + 2, Newton from 0 goes to 1 and back to 0 forever, and nearby starts are drawn into this cycle. For x^(1/3), whose derivative is infinite at the root, the iteration is x_(n+1) = −2xₙ and diverges from every start except 0.

5. **Basins of attraction can be fractal.** In ℂ, Newton's method for z² − 1 sends every point with positive real part to 1 and every point with negative real part to −1. For z³ − 1 the three basins are interleaved, and every boundary point of one basin is a boundary point of all three: the common boundary is the Julia set of the Newton map. Arthur Cayley, who posed the problem in 1879, settled only the quadratic case. Even so, for each degree d an explicit finite set of starting points finds all roots of every polynomial of degree d whose roots lie in the unit disc (Hubbard, Schleicher and Sutherland, 2001).

6. **Newton's method works in n dimensions.** For F: ℝⁿ → ℝⁿ, each step solves the linear system J(xₙ)s = −F(xₙ), where J is the Jacobian matrix of partial derivatives, and sets x_(n+1) = xₙ + s. Convergence is again quadratic near a root where J is invertible, and Kantorovich's theorem certifies convergence from x₀ given bounds on F(x₀), J(x₀)⁻¹ and the variation of J. Quasi-Newton methods replace J by cheap low-rank updates and still converge superlinearly.

7. **Cost per evaluation matters, and conditioning limits every method.** The secant method replaces f′ by the slope through the last two iterates and has order φ = (1 + √5)/2 ≈ 1.618; since a Newton step costs two evaluations (f and f′), per evaluation the secant method is faster than Newton's order √2 ≈ 1.414. Brent's method adds the safety of a bracket and is the standard black box. No method beats conditioning: changing f by δ moves a simple root by about δ/∣f′(x*)∣ but a double root by about √δ, so a double root is found to only about 8 digits. In Wilkinson's polynomial (x − 1)(x − 2)⋯(x − 20), changing the coefficient −210 of x¹⁹ by 2⁻²³ ≈ 1.2 × 10⁻⁷ turns ten real roots into five complex pairs.

## Key concepts

| Term | Meaning |
|---|---|
| Order of convergence p | e_(n+1) ≈ C ∣eₙ∣ᵖ: p = 1 is linear, p = 2 quadratic |
| Simple root | A root x* with f′(x*) ≠ 0 |
| Multiplicity m | f and its first m − 1 derivatives vanish at x*, the m-th does not |
| Contraction | A map with ∣g(x) − g(y)∣ ≤ L∣x − y∣ for a fixed L < 1 |
| Basin of attraction | The set of starting points whose iterates converge to a given root |

## How it fits

- **Below:** bisection is the intermediate value theorem of [continuity](../../06-real-analysis/01-limits-and-convergence/continuity.md) as an algorithm; Newton's error formula is [Taylor's theorem](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md); fixed-point iteration is the [contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md); cycles and fractal basins are [iterated maps](../../10-differential-equations-and-dynamics/04-dynamical-systems/iterated-maps.md).
- **Above:** implicit [time-stepping](numerical-methods-for-differential-equations.md) solves a nonlinear system by Newton's method at every step; Newton's method on ∇f = 0 drives interior-point methods in [convex optimisation](../02-optimisation/convex-optimisation-and-duality.md); implied volatility in [mathematical finance](../05-games-decisions-and-finance/mathematical-finance.md) is a root found this way.
- **Siblings:** [numerical linear algebra](numerical-linear-algebra.md) supplies the linear solve inside each n-dimensional step; [floating point](floating-point-conditioning-and-stability.md) sets the accuracy any root can have; the secant method is linear [interpolation](interpolation-and-approximation.md) of f.

## Common misconceptions

- **"Quadratic convergence means few steps from anywhere"**: it is a local property. For x²⁰ − 1 from x₀ = 0.5, Newton first jumps to about 26 000, then shrinks by a factor of only 19/20 per step, taking about 200 steps to return.
- **"A tiny ∣f(x)∣ means x is close to the root"**: near a multiple or ill-conditioned root, ∣f(x)∣ can be tiny far from x*; the error is about ∣f(x)∣/∣f′(x*)∣.

## Go deeper

- Endre Süli and David Mayers, *An Introduction to Numerical Analysis* (2003): rigorous and readable.
- C. T. Kelley, *Solving Nonlinear Equations with Newton's Method* (2003): the practical n-dimensional story.
- Kendall E. Atkinson, *An Introduction to Numerical Analysis* (2nd edition, 1989): the classical treatment.
