# Riemannian Manifolds

> **Layer:** [08 Geometry](../README.md) › [Differential Geometry](README.md)
> **Builds on:** [Surfaces and Gaussian curvature](surfaces-and-gaussian-curvature.md), [The Gauss–Bonnet theorem](the-gauss-bonnet-theorem.md), [Topological and smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [Tensor products](../../04-linear-algebra/04-multilinear-algebra/tensor-products.md), [Metric spaces and continuity](../../06-real-analysis/04-metric-spaces/metric-spaces-and-continuity.md)
> **Enables:** [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md), [The Euler–Lagrange equation](../../10-differential-equations-and-dynamics/03-calculus-of-variations/the-euler-lagrange-equation.md), [Three-manifolds and the Poincaré conjecture](../../07-topology/03-manifolds/three-manifolds-and-the-poincare-conjecture.md), [Lie groups and Lie algebras](../04-lie-theory/lie-groups-and-lie-algebras.md)

## Essence

Riemann's 1854 lecture on the hypotheses underlying geometry took Gauss's intrinsic view of surfaces and made it the definition of geometry in any dimension: a smooth manifold with an inner product on each tangent space, varying smoothly. From this metric alone come lengths, distances, geodesics, a way to differentiate vector fields (the Levi-Civita connection), and curvature, which measures how far the space is from flat. Curvature, in turn, controls global shape: positive curvature closes space up, non-positive curvature opens it out. This is the setting of general relativity and of much of modern topology.

## Core tenets

1. **A Riemannian metric is a smoothly varying inner product, and every smooth manifold has one.** At each point p the metric g gives an inner product on the tangent space, written in coordinates as gᵢⱼ dxⁱ dxʲ, a symmetric [tensor](../../04-linear-algebra/04-multilinear-algebra/tensor-products.md). Existence: take the Euclidean metric in each chart and glue with a partition of unity; a convex combination of positive-definite forms is positive definite. The argument fails for indefinite metrics, because sums of indefinite forms can degenerate: a compact manifold carries a Lorentzian metric, the kind used in relativity, if and only if its Euler characteristic is 0.

2. **The metric gives lengths, a distance and geodesics.** A curve's length is ∫ √g(γ′, γ′) dt, and the infimum over curves joining two points is a distance making M a [metric space](../../06-real-analysis/04-metric-spaces/metric-spaces-and-continuity.md) with its original topology. Geodesics are curves that locally minimise length; as critical points of the energy, an [Euler–Lagrange](../../10-differential-equations-and-dynamics/03-calculus-of-variations/the-euler-lagrange-equation.md) problem, they solve the second-order equation below, so through each point in each direction there is exactly one. The exponential map sends a tangent vector v to the point reached at time 1 along the geodesic with velocity v.

   ```
   γ̈ᵏ + Γᵏᵢⱼ γ̇ⁱ γ̇ʲ = 0          Γᵏᵢⱼ = ½ gᵏˡ (∂ᵢ gⱼₗ + ∂ⱼ gᵢₗ − ∂ₗ gᵢⱼ)
   ```

3. **Hopf–Rinow: completeness as a metric space equals geodesic completeness.** For a connected Riemannian manifold, the metric space is complete if and only if every geodesic extends for all time, and then any two points are joined by a length-minimising geodesic (Hopf and Rinow, 1931). The punctured plane ℝ² ∖ {0} shows what fails otherwise: (−1, 0) and (1, 0) are distance 2 apart, but the straight segment passes through the missing origin, and no curve in the punctured plane achieves length 2.

4. **There is exactly one torsion-free connection compatible with the metric.** To differentiate a vector field along another one needs a connection ∇; on ℝⁿ it is the ordinary derivative, but on a curved space the tangent spaces at different points are not canonically identified. Requiring ∇ to preserve the metric and to be torsion-free (∇_X Y − ∇_Y X = [X, Y]) determines it uniquely, by the Koszul formula, which solves for ∇ in terms of g; in coordinates its Christoffel symbols are the Γᵏᵢⱼ above. This is the Levi-Civita connection. Parallel transport along a curve uses it to carry vectors without turning them.

5. **Curvature is the failure of second covariant derivatives to commute.** The Riemann curvature tensor is R(X, Y)Z = ∇_X∇_Y Z − ∇_Y∇_X Z − ∇_[X,Y] Z, which vanishes if and only if the metric is locally Euclidean. Geometrically, parallel transport around a small loop rotates vectors by an amount proportional to the enclosed curvature; on a surface the rotation angle is ∫ K dA, as in [Gauss–Bonnet](the-gauss-bonnet-theorem.md). R has n²(n² − 1)/12 independent components: 1 for surfaces (Gaussian curvature), 6 in dimension 3 and 20 in dimension 4. Contracting it gives Ricci curvature and then scalar curvature; sectional curvature is the Gaussian curvature of 2-dimensional slices.

6. **Curvature bounds control topology.** Bonnet–Myers: a complete manifold with Ricci curvature at least (n − 1)k > 0 is compact, with diameter at most π/√k and finite fundamental group, because geodesics focus as on a sphere. Cartan–Hadamard: a complete simply connected manifold with sectional curvature ≤ 0 is diffeomorphic to ℝⁿ via the exponential map, because geodesics spread out and never refocus. The model spaces of constant curvature 1, 0 and −1 are the sphere, Euclidean space and hyperbolic space, the homogeneous geometries of [the Erlangen programme](../01-classical-geometry/the-erlangen-programme.md).

7. **The abstract and embedded views agree, and the theory reaches physics and topology.** Nash's embedding theorem (1956) shows every Riemannian manifold is isometric to a submanifold of some ℝᴺ, so Riemann's intrinsic definition loses nothing. General relativity replaces the inner product by a Lorentzian metric and reads gravity as curvature through Einstein's equation ([the geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md)). Hamilton's Ricci flow, deforming a metric by its Ricci curvature, was the tool Perelman used in 2002–2003 to prove the Poincaré and geometrisation conjectures ([three-manifolds](../../07-topology/03-manifolds/three-manifolds-and-the-poincare-conjecture.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Riemannian metric | A smoothly varying inner product g on tangent spaces |
| Geodesic | A curve that locally minimises length; solves the geodesic equation |
| Exponential map | Tangent vector v ↦ endpoint at time 1 of the geodesic with velocity v |
| Levi-Civita connection | The unique torsion-free connection preserving g |
| Christoffel symbols | Γᵏᵢⱼ, the coefficients of the connection in coordinates |
| Parallel transport | Moving a vector along a curve with zero covariant derivative |
| Riemann tensor | R(X, Y)Z; the obstruction to being locally flat |
| Sectional, Ricci, scalar curvature | Curvature of 2-planes, its average over directions, and its full trace |
| Lorentzian metric | A metric of signature (−, +, +, +); the setting of relativity |

## How it fits

- **Below:** [Smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) carry the structure, tensors express the metric, and the intrinsic geometry of [surfaces](surfaces-and-gaussian-curvature.md) is the two-dimensional case.
- **Above:** Variational problems in [calculus of variations](../../10-differential-equations-and-dynamics/03-calculus-of-variations/the-euler-lagrange-equation.md), general relativity, and Ricci flow in three-manifold topology.
- **Siblings:** [Differential forms](differential-forms-and-de-rham-cohomology.md) gain the Hodge star from a metric; [Lie groups](../04-lie-theory/lie-groups-and-lie-algebras.md) carry invariant metrics, and compact ones have non-negative sectional curvature for a bi-invariant metric.

## Common misconceptions

- **"Curvature needs an ambient space to curve into"**: Riemann's curvature is intrinsic; Nash's theorem shows an ambient space exists but is never needed.
- **"Geodesics always minimise length"**: Only locally; on a sphere a great-circle arc longer than half the circle is a geodesic but not the shortest path.
- **"Ricci curvature is the whole curvature"**: In dimension 4 Ricci has 10 of the 20 components; the rest, the Weyl tensor, carries gravitational waves in vacuum.

## Go deeper

- do Carmo, *Riemannian Geometry* (1992): the standard first course, from connections to comparison theorems.
- Lee, *Introduction to Riemannian Manifolds* (2018): a modern and very clear account.
- Needham, *Visual Differential Geometry and Forms* (2021): parallel transport and curvature made visible.
