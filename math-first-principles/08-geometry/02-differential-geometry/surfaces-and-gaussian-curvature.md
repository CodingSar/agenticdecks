# Surfaces and Gaussian Curvature

> **Layer:** [08 Geometry](../README.md) › [Differential Geometry](README.md)
> **Builds on:** [Curves and curvature](curves-and-curvature.md), [Quadratic forms and positive definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md), [The spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md), [Inverse and implicit function theorems](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), [Topological and smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md)
> **Enables:** [The Gauss–Bonnet theorem](the-gauss-bonnet-theorem.md), [Riemannian manifolds](riemannian-manifolds.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md)

## Essence

A surface in space bends differently in different directions, and two quadratic forms record how: the first measures lengths on the surface, the second measures how the surface curves away from its tangent plane. The extreme bendings at a point are the principal curvatures, and their product is the Gaussian curvature K. Gauss's Theorema Egregium (1827) says K can be computed from lengths measured inside the surface alone, though it was defined using the surrounding space. That makes K an intrinsic property, which bending without stretching cannot change, and explains why no flat map of the Earth preserves all distances.

## Core tenets

1. **The first fundamental form measures length on the surface.** A parametrised surface x(u, v) is regular when x_u and x_v are independent, so by the [inverse function theorem](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md) it is locally a smooth graph. Restricting the inner product of ℝ³ to the tangent plane gives the [positive-definite quadratic form](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md) below, with E = ⟨x_u, x_u⟩, F = ⟨x_u, x_v⟩, G = ⟨x_v, x_v⟩. Every length, angle and area measured within the surface comes from E, F and G; this is the data an ant living on the surface could collect.

   ```
   I  = E du² + 2F du dv + G dv²       (first form: lengths)
   II = L du² + 2M du dv + N dv²       (second form: bending)
   K  = (LN − M²) / (EG − F²)
   ```

2. **The second fundamental form measures bending, and its eigenvalues are the principal curvatures.** With unit normal n, the coefficients L = ⟨x_uu, n⟩, M = ⟨x_uv, n⟩, N = ⟨x_vv, n⟩ record how fast the surface leaves its tangent plane. Equivalently, the shape operator −dn sends each tangent vector to the rate of change of the normal; it is self-adjoint with respect to the first form, so by the [spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) it has real eigenvalues k₁, k₂, the principal curvatures, with perpendicular principal directions. They are the extreme values of the normal curvature of curves through the point in each direction.

3. **Gaussian curvature is the product of the principal curvatures.** K = k₁k₂ is the determinant of the shape operator, given by the formula above; the mean curvature is H = (k₁ + k₂)/2. A sphere of radius r has K = 1/r², a cylinder K = 0 (one direction is straight), a saddle K < 0 (it curves up one way and down the other). Geometrically, K is the limiting ratio of the area swept by the unit normal (the Gauss map to the sphere) to the area of the patch.

4. **Theorema Egregium: K depends only on the first fundamental form.** Gauss (1827) showed that K can be written in terms of E, F, G and their first and second derivatives. The proof idea: the mixed third derivatives x_uuv and x_uvu are equal, and writing both in the frame (x_u, x_v, n) gives the Gauss equation, which expresses LN − M² through E, F, G. Mean curvature is not intrinsic: a flat sheet and a cylinder are isometric, with H = 0 and H = 1/(2r), yet both have K = 0.

5. **No map of the sphere onto the plane preserves distances.** An isometry would preserve the first fundamental form, hence K by the Theorema Egregium, but the sphere has K > 0 and the plane K = 0. So every world map distorts something: Mercator keeps angles, equal-area projections keep areas, and no map does both. Folding a pizza slice to stiffen it uses the same theorem: bending one way forces the other direction to stay straight, since K must remain 0.

6. **Curvature can be measured from inside by circles.** On a surface with curvature K at a point, a geodesic circle of radius r has circumference C(r) = 2πr − (π/3)Kr³ + o(r³). Positive curvature makes circles shorter than in the plane and negative curvature longer, matching the sphere and the [hyperbolic plane](../01-classical-geometry/non-euclidean-geometry.md). This is the definition Riemann generalised to higher dimensions.

7. **A surface is a two-dimensional manifold, and the definitions are local.** Global surfaces are covered by parametrised patches, as in [smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), and the formulas above do not depend on the patch. This is what lets K be integrated over a whole closed surface in [the Gauss–Bonnet theorem](the-gauss-bonnet-theorem.md).

## Key concepts

| Term | Meaning |
|---|---|
| Regular surface | Locally the image of a map with independent partial derivatives |
| First fundamental form | The inner product restricted to tangent planes: E, F, G |
| Second fundamental form | Normal component of second derivatives: L, M, N |
| Shape operator | −dn; a self-adjoint map of the tangent plane |
| Principal curvatures | Eigenvalues k₁, k₂ of the shape operator |
| Gaussian curvature | K = k₁k₂; intrinsic |
| Mean curvature | H = (k₁ + k₂)/2; not intrinsic; zero for soap films |
| Gauss map | p ↦ n(p), from the surface to the unit sphere |
| Local isometry | A map preserving the first fundamental form |

## How it fits

- **Below:** [Curves and curvature](curves-and-curvature.md) gives normal curvature; quadratic forms and the spectral theorem give principal curvatures; [smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) give the global setting.
- **Above:** Intrinsic curvature is the seed of [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md), where gravity is curvature measured from inside space-time.
- **Siblings:** [Gauss–Bonnet](the-gauss-bonnet-theorem.md) integrates K; [Riemannian manifolds](riemannian-manifolds.md) start from the first fundamental form alone and extend intrinsic curvature to every dimension.

## Common misconceptions

- **"A cylinder is curved, so its Gaussian curvature is non-zero"**: It is curved in space, but it unrolls flat without stretching, so K = 0.
- **"Curvature needs a surrounding space"**: Gaussian curvature can be measured by beings confined to the surface, using circles or triangles.
- **"A clever projection could make a perfect world map"**: The Theorema Egregium forbids preserving all distances, and no map is both conformal and equal-area.

## Go deeper

- do Carmo, *Differential Geometry of Curves and Surfaces* (1976): the fundamental forms and the Theorema Egregium in full.
- Pressley, *Elementary Differential Geometry* (2001): worked examples of curvature computations.
- Needham, *Visual Differential Geometry and Forms* (2021): a geometric proof of the Theorema Egregium and much intuition.
