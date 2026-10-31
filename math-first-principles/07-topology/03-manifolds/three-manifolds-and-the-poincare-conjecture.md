# Three-Manifolds and the Poincaré Conjecture

> **Layer:** [07 Topology](../README.md) › [Manifolds](README.md)
> **Builds on:** [Classification of Surfaces](classification-of-surfaces.md), [Knot Theory](knot-theory.md), [Topological and Smooth Manifolds](topological-and-smooth-manifolds.md), [Homotopy and the Fundamental Group](../02-algebraic-topology/homotopy-and-the-fundamental-group.md), [Group Actions](../../05-abstract-algebra/01-groups/group-actions.md)
> **Enables:** [Riemannian Manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md), [Non-Euclidean Geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md), [Nonlinear PDEs](../../10-differential-equations-and-dynamics/02-partial-differential-equations/nonlinear-pdes.md), [Open Problems](../../15-mathematics-in-context/open-problems.md)

## Essence

Is a closed 3-dimensional space in which every loop can be shrunk to a point necessarily the 3-sphere? Poincaré asked this in 1904, and it became the most famous problem in topology. It was settled in every dimension above 3 first: by Smale for dimension 5 and higher, and by Freedman for dimension 4. Dimension 3 was too cramped for their methods yet too complicated for surface methods. The answer came from geometry. Thurston conjectured that every closed 3-manifold can be cut into pieces each carrying one of eight uniform geometries, which would contain the Poincaré conjecture as a special case. Perelman proved this geometrisation conjecture in preprints of 2002–2003, by following Hamilton's Ricci flow, a heat equation for the shape of space, and cutting out its singularities by surgery. He declined both the Fields Medal (2006) and the Millennium Prize (2010).

## Core tenets

1. **The conjecture, and why homology was not enough.** The Poincaré conjecture states: every closed, simply connected 3-manifold is homeomorphic to S³. Poincaré first suggested that having the homology of a sphere suffices, then refuted himself with the Poincaré homology sphere: it has the same homology as S³, but its fundamental group is a non-trivial group of order 120 (the binary icosahedral group). One concrete model is the quotient of S³, viewed as the unit quaternions, by that group acting by multiplication. So the hypothesis had to be π₁ = 1, not merely homology zero.

2. **Higher dimensions were easier.** The analogue in dimension n says that a closed n-manifold homotopy equivalent to Sⁿ is homeomorphic to it. Smale proved this for n ≥ 5 (1961), cancelling handles with the Whitney trick, which needs room to move 2-dimensional discs past each other. Freedman proved the n = 4 case (1982) with new infinite constructions. In dimension 3 neither the room nor the infinite constructions were available.

3. **Three-manifolds decompose canonically.** Every closed orientable 3-manifold is a connected sum of prime pieces, uniquely (Kneser and Milnor). Each prime piece can be cut further along a minimal collection of incompressible tori, tori that do not compress to circles, a decomposition due to Jaco–Shalen and Johannson. This mirrors the [classification of surfaces](classification-of-surfaces.md), where connected sum also organises everything, but the pieces are far more varied.

4. **Geometrisation: eight model geometries.** Thurston's conjecture (around 1982) says each piece of the decomposition carries a complete, locally homogeneous metric modelled on one of eight geometries: S³, Euclidean E³, hyperbolic H³, S² × ℝ, H² × ℝ, Nil, Sol, and the universal cover of SL(2, ℝ). Each manifold is a quotient of its model by a discrete [group action](../../05-abstract-algebra/01-groups/group-actions.md). Thurston proved it for a large class (Haken manifolds), and it implies the Poincaré conjecture: a simply connected closed 3-manifold is prime, contains no essential tori, and has finite π₁, so it is spherical, S³ divided by its trivial fundamental group, which is S³.

5. **Hyperbolic geometry is the generic case.** Most 3-manifolds and most [knot](knot-theory.md) complements are hyperbolic; the figure-eight knot's complement is the first example. Mostow rigidity says that a closed hyperbolic 3-manifold has only one hyperbolic metric, so geometric quantities such as volume become topological invariants. Thurston showed that every knot is a torus knot, a satellite knot or hyperbolic.

6. **Ricci flow evolves the metric to make it uniform.** Hamilton introduced (1982) the flow

   ```
   ∂g/∂t = −2 · Ric(g)
   ```

   where g is a Riemannian metric and Ric its Ricci curvature. It behaves like a heat equation for the metric: regions of high positive curvature shrink and the curvature spreads out. Hamilton showed that a closed 3-manifold with positive Ricci curvature flows to a round metric, hence is a quotient of S³. In general the flow develops singularities in finite time, such as necks that pinch off, and Hamilton proposed cutting them out and continuing, a programme he could not complete.

7. **Perelman completed the programme.** In three arXiv preprints (2002–2003) Perelman introduced an entropy-like quantity that is monotone under the flow, proved that the flow does not collapse locally, classified the possible singularity models, and showed that surgery can be performed with control, so that only finitely many surgeries happen in finite time. For a simply connected manifold the flow becomes extinct in finite time, leaving only spheres. Several teams checked and expanded the argument, with expositions by Kleiner and Lott, by Morgan and Tian, and by Cao and Zhu appearing around 2006. Perelman declined the Fields Medal (2006) and the Clay Millennium Prize (2010). As of 2026 the Poincaré conjecture remains the only Millennium Prize problem to have been solved.

## Key concepts

| Term | Meaning |
|---|---|
| Simply connected | Path-connected with trivial fundamental group |
| Homology sphere | A closed manifold with the homology of a sphere, not necessarily a sphere |
| Prime manifold | One that is not a connected sum of two manifolds neither of which is a sphere |
| Incompressible torus | An embedded torus whose loops stay non-trivial in the manifold |
| Model geometry | One of the eight homogeneous geometries of Thurston's list |
| Ricci flow | The evolution ∂g/∂t = −2·Ric(g) of a Riemannian metric |
| Surgery | Cutting out a nearly singular neck and capping the ends with balls |

## How it fits

- **Below:** the decomposition imitates [surfaces](classification-of-surfaces.md); [knots](knot-theory.md) supply examples, and surgery on links builds every closed orientable 3-manifold; [π₁](../02-algebraic-topology/homotopy-and-the-fundamental-group.md) is the hypothesis of the conjecture.
- **Above:** the flow is a [nonlinear PDE](../../10-differential-equations-and-dynamics/02-partial-differential-equations/nonlinear-pdes.md) on [Riemannian manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md); hyperbolic geometry from [non-Euclidean geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md) is the generic case; the problem's history belongs to [open problems](../../15-mathematics-in-context/open-problems.md).
- **Siblings:** the smooth 4-dimensional Poincaré conjecture, discussed in [topological and smooth manifolds](topological-and-smooth-manifolds.md), is open as of 2026.

## Common misconceptions

- **"Dimension 3 should follow from the proofs in higher dimensions."**: The higher-dimensional proofs use room that dimension 3 lacks; the 3-dimensional case needed an entirely different, geometric method.
- **"Perelman proved only the Poincaré conjecture."**: His argument proves Thurston's full geometrisation conjecture, which classifies all closed 3-manifolds in geometric terms.

## Go deeper

- William P. Thurston, *Three-Dimensional Geometry and Topology, Volume 1* (1997): the eight geometries from their originator.
- John Morgan and Gang Tian, *Ricci Flow and the Poincaré Conjecture* (2007): a complete, detailed account of Perelman's proof.
- Donal O'Shea, *The Poincaré Conjecture* (2007): the century-long story for a general reader.
