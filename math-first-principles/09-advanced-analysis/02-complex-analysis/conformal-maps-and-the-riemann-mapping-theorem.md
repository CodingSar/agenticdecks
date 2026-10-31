# Conformal Maps and the Riemann Mapping Theorem

> **Layer:** [09 Advanced Analysis](../README.md) › [Complex Analysis](README.md)
> **Builds on:** [Holomorphic Functions](holomorphic-functions.md), [Cauchy's Theorem and Its Consequences](cauchys-theorem-and-its-consequences.md), [Compactness in Metric Spaces](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md), [Non-Euclidean Geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md)
> **Enables:** [Analytic Continuation and Riemann Surfaces](analytic-continuation-and-riemann-surfaces.md), [Laplace's Equation and Harmonic Functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md), [Modular Forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md), [Complex Dynamics](../../10-differential-equations-and-dynamics/04-dynamical-systems/complex-dynamics.md)

## Essence

A holomorphic function with non-zero derivative preserves angles, so it is a conformal map: it distorts sizes but keeps the shape of infinitesimal figures. Conformal maps between plane regions are surprisingly plentiful and surprisingly rigid at once. The Riemann mapping theorem says that every simply connected open region of the plane other than the plane itself can be mapped conformally and bijectively onto the unit disc, so a jagged coastline and a perfect circle are indistinguishable to complex analysis. Yet the maps of the disc to itself form only a three-dimensional family, the isometries of the hyperbolic plane.

## Core tenets

1. **Holomorphic with f′ ≠ 0 means angle-preserving.** At a point where f′(z₀) = re^(iθ) ≠ 0, the derivative multiplies tangent vectors by r and rotates them by θ, so two curves crossing at z₀ cross at the same angle, with the same orientation, after mapping. Where f′(z₀) = 0, as for z² at 0, angles are multiplied by the order of the zero. A holomorphic bijection automatically has f′ ≠ 0 and a holomorphic inverse.

2. **Möbius transformations are the conformal symmetries of the sphere.** Maps z ↦ (az + b)/(cz + d) with ad − bc ≠ 0 act on the Riemann sphere ℂ ∪ {∞}, compose like 2 × 2 matrices, and form the group PSL(2, ℂ). They send circles and lines to circles and lines, and there is exactly one taking any three distinct points to any other three. The Cayley transform z ↦ (z − i)/(z + i) maps the upper half-plane onto the unit disc, since points nearer i than −i are exactly those with positive imaginary part.

3. **The Schwarz lemma pins down the disc's self-maps.** If f maps the unit disc 𝔻 into itself with f(0) = 0, then ∣f(z)∣ ≤ ∣z∣ and ∣f′(0)∣ ≤ 1, with equality only for a rotation. Proof idea: f(z)/z has a removable singularity at 0, and the maximum modulus principle on circles of radius r close to 1 bounds it by 1/r. Composing with the maps z ↦ (z − a)/(1 − āz), which swap a and 0, shows that every biholomorphism of 𝔻 is e^(iθ)·(z − a)/(1 − āz). These are exactly the orientation-preserving isometries of the Poincaré disc model of the [hyperbolic plane](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md), and every holomorphic self-map of 𝔻 is a contraction of the hyperbolic metric.

4. **The Riemann mapping theorem.** Let U ⊊ ℂ be a non-empty, simply connected open set and z₀ ∈ U. Then there is exactly one biholomorphism f from U onto 𝔻 with f(z₀) = 0 and f′(z₀) real and positive. Riemann stated it in 1851 with a proof resting on the Dirichlet principle, which was not then justified; complete proofs came at the turn of the twentieth century. Uniqueness follows from tenet 3: two such maps differ by a disc automorphism fixing 0 with positive derivative, which is the identity.

5. **The proof is an extremal problem solved by compactness.** Consider all injective holomorphic maps g from U into 𝔻 with g(z₀) = 0, and maximise ∣g′(z₀)∣.
   - The family is non-empty. Pick a point a ∉ U. Since U is simply connected and z − a never vanishes there, z − a has a holomorphic square root on U, which is injective and misses a whole disc. A Möbius map then sends its image into 𝔻.
   - A maximiser exists. Montel's theorem says that a locally bounded family of holomorphic functions has locally uniformly convergent subsequences. It follows from Cauchy's estimates, which give equicontinuity, and the Arzelà–Ascoli theorem. Hurwitz's theorem keeps the limit injective, since a limit of zero-free functions is zero-free or identically zero.
   - The maximiser is onto. If it missed a point, a square root followed by Möbius maps would produce a map with larger derivative, by the Schwarz lemma.

6. **Each hypothesis is needed.** If U = ℂ, a biholomorphism onto 𝔻 would be a bounded entire function, constant by Liouville's theorem. If U is not simply connected, say an annulus r < ∣z∣ < 1, its loops cannot be contracted while the disc's can, and a homeomorphism preserves that. Even two annuli are conformally equivalent only if they have the same ratio of radii, the modulus, so topology alone does not decide conformal type for multiply connected regions.

7. **Higher dimensions are rigid.** In ℂ² the open ball and the bidisc 𝔻 × 𝔻 are both simply connected, bounded and smoothly equivalent, yet no biholomorphism joins them; Poincaré proved this by comparing their automorphism groups. In real dimension n ≥ 3, Liouville's theorem on conformal maps says that the only smooth conformal maps are Möbius transformations.

8. **Conformal maps transplant problems.** Harmonic functions stay harmonic under conformal change of variable, so the Dirichlet problem for [Laplace's equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) on any simply connected region reduces to the disc, where the Poisson integral solves it. Carathéodory's theorem says that if the boundary is a Jordan curve, the Riemann map extends to a homeomorphism of the closures, so boundary data can be carried across.

## Key concepts

| Term | Meaning |
|---|---|
| Conformal map | A map preserving angles and orientation; holomorphic with f′ ≠ 0 |
| Biholomorphism | A holomorphic bijection with holomorphic inverse |
| Möbius transformation | z ↦ (az + b)/(cz + d) with ad − bc ≠ 0 |
| Riemann sphere | ℂ ∪ {∞}, on which Möbius maps act |
| Schwarz lemma | A self-map of 𝔻 fixing 0 satisfies ∣f(z)∣ ≤ ∣z∣ |
| Normal family | A family in which every sequence has a locally uniformly convergent subsequence |
| Montel's theorem | Locally bounded families of holomorphic functions are normal |
| Riemann mapping theorem | Every simply connected U ⊊ ℂ is biholomorphic to 𝔻 |

## How it fits

- **Below:** the [derivative as rotation and scaling](holomorphic-functions.md) explains angle preservation; [Cauchy's estimates](cauchys-theorem-and-its-consequences.md) and [compactness](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md) drive the proof; the [hyperbolic plane](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md) explains the disc's symmetries.
- **Above:** potential theory and the [Dirichlet problem](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) in 10; [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md) in 12 live on the upper half-plane modulo a Möbius group; normal families define the Julia sets of [complex dynamics](../../10-differential-equations-and-dynamics/04-dynamical-systems/complex-dynamics.md).
- **Siblings:** [Riemann surfaces](analytic-continuation-and-riemann-surfaces.md) extend the theorem to uniformisation; [singularities](singularities-and-residues.md) govern how conformal maps behave at boundary corners.

## Common misconceptions

- **"Conformal means preserving distances"**: only angles are preserved; lengths are scaled by ∣f′∣, which varies from point to point.
- **"The Riemann map is explicit"**: the theorem is existential; explicit formulas exist for polygons (Schwarz–Christoffel) and a few other shapes, and otherwise the map is computed numerically.

## Go deeper

- Lars V. Ahlfors, *Complex Analysis* (3rd edition, 1979): normal families and a clean proof of the mapping theorem.
- Tristan Needham, *Visual Complex Analysis* (1997): Möbius maps and hyperbolic geometry drawn.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (2003): conformal maps, Montel and Schwarz–Christoffel.
