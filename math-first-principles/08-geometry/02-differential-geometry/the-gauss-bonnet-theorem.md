# The Gauss–Bonnet Theorem

> **Layer:** [08 Geometry](../README.md) › [Differential Geometry](README.md)
> **Builds on:** [Surfaces and Gaussian curvature](surfaces-and-gaussian-curvature.md), [Curves and curvature](curves-and-curvature.md), [The Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md), [Classification of surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md), [Vector calculus and the integral theorems](../../06-real-analysis/03-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md)
> **Enables:** [Differential forms and de Rham cohomology](differential-forms-and-de-rham-cohomology.md), [Riemannian manifolds](riemannian-manifolds.md), [Algebraic curves and Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md), [Fixed-point theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md)

## Essence

Gaussian curvature changes when a surface is dented, but the Gauss–Bonnet theorem says its total over a closed surface never does: it always equals 2π times the Euler characteristic. A sphere, however lumpy, has total curvature 4π; a torus, however twisted, has total curvature 0. The theorem is the model of a local-to-global principle, in which a quantity computed point by point from the metric adds up to a topological invariant that counts holes. Its proof is short, its counterexamples show exactly which hypotheses matter, and its generalisations run through modern geometry.

## Core tenets

1. **Statement: for a compact surface without boundary, ∫ K dA = 2πχ.** Let M be a compact smooth surface without boundary, with a Riemannian metric (for instance, sitting in ℝ³), Gaussian curvature K and area element dA. Then the integral of K equals 2π times the [Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md) χ(M). Orientation is not needed if K dA is read as a density: the round projective plane has K = 1, area 2π and χ = 1. For an orientable surface of genus g, χ = 2 − 2g.

   ```
   ∫∫_M K dA = 2π χ(M)          sphere: 4π     torus: 0     genus g: 2π(2 − 2g)
   ```

2. **The local version is the angle formula for geodesic triangles.** For a triangle T bounded by geodesics with interior angles α, β, γ, the integral of K over T is α + β + γ − π. Curvature is exactly what makes the angle sum differ from π, as on the sphere (excess) and the [hyperbolic plane](../01-classical-geometry/non-euclidean-geometry.md) (deficit). With curved edges the boundary adds the integral of the geodesic curvature k_g, the curvature of the edges as seen from inside the surface; for a disc in the plane, ∫ k_g ds = 2π recovers the turning number of [curves and curvature](curves-and-curvature.md). The proof of the local version is Green's theorem from [vector calculus](../../06-real-analysis/03-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md) applied to the rotation of a moving frame.

3. **Triangulating turns the local version into the global one.** Cut M into F geodesic triangles with E edges and V vertices. Summing the local formula, the total of K is the sum of all angles minus πF. The angles around each vertex add to 2π, giving 2πV; each triangle has three edges and each edge borders two triangles, so 3F = 2E. Then 2πV − πF = 2π(V − E + F) = 2πχ. The left side does not depend on the triangulation, which incidentally proves that χ does not either.

4. **Each hypothesis is needed.** Without compactness the theorem fails: the flat plane has ∫ K = 0 but χ = 1. Without the boundary term it fails for surfaces with boundary: a flat disc has ∫ K = 0 but χ = 1, and the missing 2π is ∫ k_g ds around the edge. Without smoothness it survives in a discrete form: for a convex polyhedron, curvature concentrates at vertices as the angle defect, 2π minus the face angles there, and Descartes's theorem says the defects total 4π, as with a cube's eight vertices of defect π/2.

5. **Topology constrains curvature.** A torus in ℝ³ must have points of positive and negative curvature, since the total is 0 and the outermost points have K > 0. A closed surface with K > 0 everywhere has χ > 0, so is a sphere or a projective plane. A surface of genus at least 2 has negative total curvature, so any metric on it has K < 0 somewhere; with constant curvature −1 its area is fixed at 4π(g − 1). Conversely, by the [classification of surfaces](../../07-topology/03-manifolds/classification-of-surfaces.md) the curvature total determines an orientable closed surface.

6. **The same number counts the zeros of vector fields.** The Poincaré–Hopf theorem says the indices of the zeros of a vector field with isolated zeros on a compact manifold sum to χ. On the sphere χ = 2 ≠ 0, so every continuous tangent vector field vanishes somewhere: the hairy ball theorem, related to the [fixed-point theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md). One proof compares the turning of a vector field with the turning of a frame and lands on Gauss–Bonnet.

7. **Gauss–Bonnet is the first index theorem.** Chern (1944) gave an intrinsic proof in all even dimensions, integrating a polynomial in the curvature to get χ; in [de Rham cohomology](differential-forms-and-de-rham-cohomology.md) the integrand is a closed form whose class is topological. The Atiyah–Singer index theorem (1963) generalises the pattern: an analytic count of solutions equals a topological integral. [Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) is another case.

## Key concepts

| Term | Meaning |
|---|---|
| Total curvature | ∫ K dA over a surface |
| Euler characteristic | χ = V − E + F for any triangulation; 2 − 2g for an orientable surface of genus g |
| Geodesic curvature | The curvature of a curve as seen within the surface; zero for geodesics |
| Angle excess | α + β + γ − π for a geodesic triangle; equals ∫ K |
| Angle defect | 2π minus the angles at a polyhedron vertex; concentrated curvature |
| Index of a zero | The winding number of a vector field around an isolated zero |
| Local-to-global theorem | A theorem whose integrand is local and whose answer is global |

## How it fits

- **Below:** [Surfaces and Gaussian curvature](surfaces-and-gaussian-curvature.md) define K; [the Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md) and the classification of surfaces supply the topology; Green's theorem does the local work.
- **Above:** Index theory and characteristic classes generalise it; [Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md) for curves relates degree and genus in the same spirit.
- **Siblings:** [Differential forms](differential-forms-and-de-rham-cohomology.md) give the language of Chern's proof; [Riemannian manifolds](riemannian-manifolds.md) extend curvature to higher dimensions; [polytopes](../03-convex-and-discrete-geometry/polytopes.md) carry the discrete version through Euler's formula.

## Common misconceptions

- **"Deforming a surface changes its total curvature"**: Curvature moves around, but its integral is fixed by χ for every metric.
- **"Gauss–Bonnet is about surfaces in ℝ³"**: It is intrinsic and holds for any metric on a compact surface, embedded or not.
- **"It holds for any surface"**: Non-compact surfaces and surfaces with boundary need hypotheses or a boundary term, as the plane and the disc show.

## Go deeper

- do Carmo, *Differential Geometry of Curves and Surfaces* (1976): the local and global theorem with full proofs.
- Stillwell, *Geometry of Surfaces* (1992): curvature, angle sums and topology for the three constant-curvature geometries.
- Needham, *Visual Differential Geometry and Forms* (2021): several geometric proofs, including via holonomy.
