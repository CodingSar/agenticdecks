# Non-Euclidean Geometry

> **Layer:** [08 Geometry](../README.md) › [Classical Geometry](README.md)
> **Builds on:** [Euclidean geometry](euclidean-geometry.md), [Consistency and independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md), [The complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md), [Group actions](../../05-abstract-algebra/01-groups/group-actions.md)
> **Enables:** [Surfaces and Gaussian curvature](../02-differential-geometry/surfaces-and-gaussian-curvature.md), [Riemannian manifolds](../02-differential-geometry/riemannian-manifolds.md), [Conformal maps and the Riemann mapping theorem](../../09-advanced-analysis/02-complex-analysis/conformal-maps-and-the-riemann-mapping-theorem.md), [Three-manifolds and the Poincaré conjecture](../../07-topology/03-manifolds/three-manifolds-and-the-poincare-conjecture.md)

## Essence

For centuries geometers assumed the negation of the parallel postulate and hunted for a contradiction. Around 1830 Gauss (privately), Bolyai and Lobachevsky took the opposite view: the negation gives a coherent geometry, now called hyperbolic, with infinitely many parallels through a point and triangles whose angles sum to less than π. Models built from Euclidean objects, by Beltrami, Klein and Poincaré, showed that hyperbolic geometry is consistent if Euclidean geometry is, so the parallel postulate is independent of the other axioms. It turned out to be the natural geometry of most surfaces.

## Core tenets

1. **Denying the parallel postulate in neutral geometry forces infinitely many parallels.** Saccheri (1733) derived many consequences of the negation and declared a contradiction on weak grounds; Gauss, Bolyai and Lobachevsky read the same consequences as a geometry. Neutral geometry already proves that parallels exist (Euclid I.27), so the negation of uniqueness means more than one parallel; then every line through P between two limiting parallels misses ℓ, giving infinitely many.

2. **A triangle's angle deficit is its area.** In the hyperbolic plane of curvature −1, a triangle with angles α, β, γ has area π − (α + β + γ). The deficit is additive when a triangle is cut in two, which is why it behaves like area; [Gauss–Bonnet](../02-differential-geometry/the-gauss-bonnet-theorem.md) makes this exact. So no triangle has area above π (ideal triangles, with vertices at infinity, reach it), similar triangles are congruent, and angles fix lengths, giving a natural unit of length. On the unit sphere the same argument gives area (α + β + γ) − π: curvature +1 instead of −1.

3. **The upper half-plane model turns hyperbolic geometry into complex arithmetic.** Its points are z = x + iy with y > 0, and lengths are measured by the metric below. Geodesics are vertical half-lines and semicircles centred on the real axis, which plays the role of the circle at infinity. The orientation-preserving isometries are the Möbius maps z ↦ (az + b)/(cz + d) with a, b, c, d real and ad − bc = 1, forming PSL(2, ℝ) = SL(2, ℝ)/{±I}; scaling z ↦ λz with λ > 0 visibly preserves the metric, since it multiplies dx, dy and y alike.

   ```
   half-plane:  ds² = (dx² + dy²) / y²
   disc:        ds² = 4(dx² + dy²) / (1 − x² − y²)²
   ```

4. **The Poincaré disc and the Beltrami–Klein disc are other pictures of the same plane.** The Cayley map z ↦ (z − i)/(z + i) carries the half-plane onto the unit disc with the second metric above; geodesics become diameters and arcs meeting the boundary at right angles, and angles are still Euclidean angles. The Beltrami–Klein model uses the same disc with straight chords as lines; it distorts angles, but its distance is ½∣log∣ of a cross-ratio, and its isometries are the [projective maps](projective-geometry.md) preserving the circle. A fourth model is the sheet x² + y² − z² = −1, z > 0, in Minkowski space, a sphere of imaginary radius. All four are isometric.

5. **The models prove relative consistency, so the parallel postulate is independent.** Each model is assembled from Euclidean objects, and each hyperbolic axiom becomes a Euclidean theorem about them. A contradiction derived in hyperbolic geometry would therefore translate into one in Euclidean geometry. Since ℝ² models the parallel postulate and the disc models its negation, neither follows from the other axioms: the first great example of [consistency and independence](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md), and the pattern later followed by [forcing](../../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md).

6. **No complete hyperbolic plane sits smoothly in ordinary space.** The pseudosphere, swept out by rotating a tractrix and used by Beltrami in 1868, has curvature −1 and carries pieces of hyperbolic geometry, but it has a sharp rim and is not complete. Hilbert (1901) proved that no complete surface of constant negative curvature can be smoothly immersed in ℝ³. So the models must be metrics on a disc, the intrinsic view of [surfaces and Gaussian curvature](../02-differential-geometry/surfaces-and-gaussian-curvature.md).

7. **Hyperbolic geometry is the typical case.** A circle of hyperbolic radius r has circumference 2π sinh r, so space grows exponentially. By uniformisation every closed orientable surface of genus g ≥ 2 has a metric of curvature −1, which presents it as the hyperbolic plane divided by a discrete group of isometries; its area is then 4π(g − 1). In dimension three, Thurston showed that every knot is a torus knot, a satellite knot or has a hyperbolic complement, and hyperbolic geometry is one of the eight geometries in his geometrisation programme, completed by Perelman (see [three-manifolds](../../07-topology/03-manifolds/three-manifolds-and-the-poincare-conjecture.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Hyperbolic plane | The complete, simply connected surface of constant curvature −1 |
| Angle deficit | π minus the angle sum of a triangle; equal to its area at curvature −1 |
| Ideal point | A point on the circle at infinity; not itself in the plane |
| Upper half-plane | {x + iy : y > 0} with metric (dx² + dy²)/y² |
| Poincaré disc | The unit disc with a conformal metric; lines are arcs orthogonal to the boundary |
| Beltrami–Klein model | The unit disc with chords as lines and a cross-ratio distance |
| Möbius map | z ↦ (az + b)/(cz + d); with real coefficients and ad − bc = 1, an isometry of the half-plane |
| Relative consistency | If one theory is consistent, so is another, because the second has a model inside the first |

## How it fits

- **Below:** [Euclidean geometry](euclidean-geometry.md) supplies neutral geometry, [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) the Möbius maps, and [group actions](../../05-abstract-algebra/01-groups/group-actions.md) the isometry groups.
- **Above:** Curvature −1 is the constant-curvature case of [Riemannian manifolds](../02-differential-geometry/riemannian-manifolds.md); disc automorphisms reappear in [conformal maps](../../09-advanced-analysis/02-complex-analysis/conformal-maps-and-the-riemann-mapping-theorem.md).
- **Siblings:** [Projective geometry](projective-geometry.md) supplies the Klein model; [the Erlangen programme](the-erlangen-programme.md) reads hyperbolic geometry as the invariants of PSL(2, ℝ); [symmetry groups and tilings](symmetry-groups-and-tilings.md) has hyperbolic analogues with infinitely many tiling groups.

## Common misconceptions

- **"The sphere already shows the parallel postulate is independent"**: Great circles meet twice and betweenness fails, so the sphere violates neutral axioms that hyperbolic geometry keeps; neutral geometry even proves parallels exist.
- **"Hyperbolic geometry was proved consistent outright"**: Only relative to Euclidean geometry, which is in turn consistent if the real numbers are.
- **"A saddle or a pseudosphere is the hyperbolic plane"**: They carry only pieces of it; Hilbert's theorem rules out a complete smooth copy in ℝ³.

## Go deeper

- Greenberg, *Euclidean and Non-Euclidean Geometries* (1974): the axiomatic story from Saccheri to the models.
- Anderson, *Hyperbolic Geometry* (1999): the half-plane and disc models worked out with Möbius maps.
- Stillwell, *Geometry of Surfaces* (1992): hyperbolic surfaces as quotients of the plane by discrete groups.
- Thurston, *Three-Dimensional Geometry and Topology* (1997): hyperbolic geometry as the heart of three-dimensional topology.
