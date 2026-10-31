# Topological and Smooth Manifolds

> **Layer:** [07 Topology](../README.md) › [Manifolds](README.md)
> **Builds on:** [Separation Axioms and Metrisability](../01-point-set-topology/separation-axioms-and-metrisability.md), [Subspaces, Products and Quotients](../01-point-set-topology/subspaces-products-and-quotients.md), [Homology](../02-algebraic-topology/homology.md), [The Derivative as a Linear Map](../../06-real-analysis/04-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Inverse and Implicit Function Theorems](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md)
> **Enables:** [Differential Forms and de Rham Cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), [Riemannian Manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md), [Lie Groups and Lie Algebras](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md), [Hamiltonian Systems and Integrability](../../10-differential-equations-and-dynamics/04-dynamical-systems/hamiltonian-systems-and-integrability.md), [The Geometry of General Relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md)

## Essence

A manifold is a space that looks like ordinary ℝⁿ near each of its points, however twisted it is globally. The Earth's surface is the model: every atlas page is a flat map of a small region, and the pages overlap consistently, yet no single flat page shows the whole sphere. Topological manifolds ask only that the overlaps be continuous; smooth manifolds ask that they be differentiable, so that calculus can be done on curved spaces. This is the stage for most of geometry and physics: configuration spaces of mechanical systems, spacetime, Lie groups and solution sets of equations. The surprise is that the step from "continuous" to "smooth" is not innocent. Milnor showed in 1956 that the 7-sphere carries smooth structures that are not equivalent to the standard one, and ℝ⁴, alone among the spaces ℝⁿ, carries uncountably many.

## Core tenets

1. **A topological n-manifold is Hausdorff, second countable and locally homeomorphic to ℝⁿ.** Each point has an open neighbourhood homeomorphic to an open subset of ℝⁿ. The two global conditions exclude pathologies that are locally fine. The line with two origins (two copies of ℝ glued everywhere except at 0) is locally Euclidean and second countable but not Hausdorff, so sequences have two limits. The long line (uncountably many copies of [0, 1) laid end to end) is Hausdorff and locally Euclidean but not second countable, and it does not embed in any ℝᴺ.

2. **Dimension is well defined, and that needs topology.** A non-empty open subset of ℝⁿ is not homeomorphic to one of ℝᵐ for n ≠ m. This is invariance of dimension, proved with [homology](../02-algebraic-topology/homology.md): for a point x of an open set U ⊂ ℝⁿ, the local homology Hₖ(U, U − {x}) is ℤ for k = n and zero otherwise, so n is read off from the topology. Without it, "n-manifold" would be ambiguous, since there are continuous surjections from [0, 1] onto a square (space-filling curves).

3. **A smooth structure is a maximal atlas with smooth transition maps.** A chart is a homeomorphism φ: U → φ(U) ⊂ ℝⁿ. Where two charts overlap, the transition map ψ ∘ φ⁻¹ goes from an open set of ℝⁿ to another; the atlas is smooth if every transition map is infinitely differentiable. A function on the manifold is smooth if it is smooth in every chart, which is consistent because transitions are smooth. Maximality means including every chart compatible with the atlas, so the structure does not depend on which charts were listed first.

4. **Equations cut out manifolds when the derivative has full rank.** If f: ℝᵐ → ℝᵏ is smooth and the derivative is surjective at every point of f⁻¹(c), then f⁻¹(c) is a smooth manifold of dimension m − k (the regular value theorem). The proof is the [implicit function theorem](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), which supplies the charts. The sphere Sⁿ is f⁻¹(1) for f(x) = ∣x∣²; the orthogonal group O(n) is the set of matrices with AᵀA = I, a manifold of dimension n(n − 1)/2. Where the rank drops, as for xy = 0 at the origin, the solution set can have a crossing and fail to be a manifold.

5. **Smoothness gives calculus and partitions of unity.** Each point has a tangent space, an n-dimensional vector space, and a smooth map has a [derivative](../../06-real-analysis/04-calculus-of-several-variables/the-derivative-as-a-linear-map.md) between tangent spaces. Second countability and the Hausdorff property guarantee smooth partitions of unity: smooth functions, each supported in one chart, summing to 1. They glue local constructions into global ones, which gives every smooth manifold a Riemannian metric and, by Whitney's theorem, an embedding into ℝ²ⁿ.

6. **"Different atlases" is not "different structures".** On ℝ, the charts x ↦ x and x ↦ x³ give incompatible atlases, since x^(1/3) is not differentiable at 0. Yet the map x ↦ x^(1/3) is a diffeomorphism from one structure to the other, so they are the same up to diffeomorphism. The real question is whether two smooth structures on a manifold are diffeomorphic.

7. **Exotic spheres and exotic ℝ⁴ show that smoothness carries real information.** Milnor (1956) built smooth 7-manifolds homeomorphic to S⁷ but not diffeomorphic to it. Kervaire and Milnor then showed that S⁷ has 28 smooth structures up to orientation-preserving diffeomorphism. In dimensions 1, 2 and 3 every topological manifold has exactly one smooth structure up to diffeomorphism. ℝⁿ has exactly one for every n ≠ 4, but work combining Freedman's topological and Donaldson's gauge-theoretic results in the early 1980s produced exotic ℝ⁴s, and Taubes showed there are uncountably many. Some topological 4-manifolds have no smooth structure at all. Whether S⁴ has an exotic smooth structure (the smooth four-dimensional Poincaré conjecture) is open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Chart | A homeomorphism from an open set of the manifold onto an open set of ℝⁿ |
| Atlas | A collection of charts covering the manifold |
| Transition map | ψ ∘ φ⁻¹ on the overlap of two charts, a map between open sets of ℝⁿ |
| Smooth structure | A maximal atlas whose transition maps are all infinitely differentiable |
| Diffeomorphism | A smooth bijection with a smooth inverse |
| Regular value | A value c at which the derivative of f is surjective at every point of f⁻¹(c) |
| Partition of unity | Smooth functions subordinate to a cover, summing to 1 |
| Exotic structure | A smooth structure homeomorphic but not diffeomorphic to the standard one |

## How it fits

- **Below:** the global conditions come from [separation axioms](../01-point-set-topology/separation-axioms-and-metrisability.md) (a manifold is metrisable); gluing uses [quotients](../01-point-set-topology/subspaces-products-and-quotients.md); smoothness and charts from equations come from [several-variable calculus](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md).
- **Above:** [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md) and [Riemannian metrics](../../08-geometry/02-differential-geometry/riemannian-manifolds.md) live on smooth manifolds; [Lie groups](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md) are manifolds with a smooth group law; phase spaces in [Hamiltonian mechanics](../../10-differential-equations-and-dynamics/04-dynamical-systems/hamiltonian-systems-and-integrability.md) and spacetime in [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) are manifolds.
- **Siblings:** two-dimensional manifolds are [classified completely](classification-of-surfaces.md); [knots](knot-theory.md) are embedded circles in a 3-manifold; [three-manifolds](three-manifolds-and-the-poincare-conjecture.md) yield to geometry.

## Common misconceptions

- **"A manifold is a subset of some ℝᴺ."**: The definition is intrinsic. Whitney's theorem shows that every smooth manifold can be embedded, but the embedding is a theorem, not part of the definition.
- **"Homeomorphic smooth manifolds are diffeomorphic."**: False: S⁷ carries exotic smooth structures, and so does ℝ⁴.

## Go deeper

- John M. Lee, *Introduction to Smooth Manifolds* (2nd edition, 2013): the standard modern text.
- John Milnor, *Topology from the Differentiable Viewpoint* (1965): regular values and degree in under a hundred pages.
- Victor Guillemin and Alan Pollack, *Differential Topology* (1974): manifolds in ℝᴺ, with intuition first.
