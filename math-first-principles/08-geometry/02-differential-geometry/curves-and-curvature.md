# Curves and Curvature

> **Layer:** [08 Geometry](../README.md) › [Differential Geometry](README.md)
> **Builds on:** [The derivative as a linear map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md), [Inner products and orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md)
> **Enables:** [Surfaces and Gaussian curvature](surfaces-and-gaussian-curvature.md), [The Gauss–Bonnet theorem](the-gauss-bonnet-theorem.md), [Existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), [Knot theory](../../07-topology/03-manifolds/knot-theory.md)

## Essence

Differential geometry begins by asking how a curve bends. Parametrised by arc length, a curve has a unit tangent, and the rate at which that tangent turns is the curvature, the reciprocal of the radius of the best-fitting circle. In space a second number, the torsion, measures how the curve twists out of its plane. The Frenet–Serret equations show that curvature and torsion are all there is: they determine the curve up to a rigid motion. Integrating curvature around a closed curve already gives a global, topological answer, the first instance of local geometry controlling global shape.

## Core tenets

1. **A regular curve can be reparametrised by arc length.** A curve γ: [a, b] → ℝⁿ is regular when its velocity γ′ is never zero. Then arc length s(t) = ∫ ‖γ′‖ is strictly increasing, so it can be inverted and used as the parameter, making the speed exactly 1. Without regularity this fails: t ↦ (t³, t²) is smooth but has a cusp at t = 0, where no tangent direction exists. Arc length is what makes curvature a property of the shape rather than of the parametrisation.

2. **Curvature is the rate of turning of the unit tangent.** With T = γ′ of unit length, differentiating ⟨T, T⟩ = 1 gives ⟨T′, T⟩ = 0, so T′ is perpendicular to T. Its length κ = ‖T′‖ is the curvature, and when κ > 0 the unit normal is N = T′/κ. The [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md) γ(s) = γ(0) + sT + ½s²κN + … shows the curve hugs the circle of radius 1/κ in direction N, the osculating circle. A straight line has κ = 0 and a circle of radius r has κ = 1/r.

3. **Torsion measures twisting out of the osculating plane.** In ℝ³ set B = T × N. Differentiating the orthonormal relations shows B′ is parallel to N, so B′ = −τN defines the torsion τ. A curve with κ > 0 is planar if and only if τ is identically 0: then B is constant and ⟨γ − γ(0), B⟩ has zero derivative.

4. **The Frenet–Serret equations describe the moving frame, and their matrix is skew.** Because (T, N, B) stays orthonormal, the matrix expressing its derivative in itself is antisymmetric, which is why only two functions κ and τ appear.

   ```
   T′ =       κN
   N′ = −κT        + τB
   B′ =      −τN
   ```

5. **Curvature and torsion determine the curve up to rigid motion.** Given smooth functions κ > 0 and τ, the Frenet–Serret equations are a linear system of ordinary differential equations for the frame, so by [existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md) there is exactly one solution with a given starting frame, and integrating T gives γ. Different starting points and frames differ by a rigid motion. A helix (a cos t, a sin t, bt) has constant κ = a/(a² + b²) and τ = b/(a² + b²), so constant curvature and torsion characterise helices. The hypothesis κ > 0 matters: where κ = 0 the normal is undefined, and two arcs can be glued with a twist.

6. **For plane curves curvature has a sign, and its integral is topological.** In the plane, N can be chosen as T rotated by a right angle, giving a signed curvature k with T turning at rate k. The total ∫ k ds measures the net turning of the tangent, so for a closed curve it is 2π times an integer, the turning number. Hopf's Umlaufsatz says a simple closed curve has turning number ±1, so ∫ k ds = ±2π. This is the one-dimensional ancestor of [the Gauss–Bonnet theorem](the-gauss-bonnet-theorem.md).

7. **Total curvature bounds the topology of space curves.** Fenchel's theorem says every closed space curve has ∫ κ ds ≥ 2π, with equality only for planar convex curves. The Fáry–Milnor theorem says a knotted curve has total curvature greater than 4π, so a [knot](../../07-topology/03-manifolds/knot-theory.md) must bend at least twice as much as a circle. Both follow from averaging over directions: a curve with small total curvature has a height function with only one maximum and one minimum.

## Key concepts

| Term | Meaning |
|---|---|
| Regular curve | A differentiable curve whose velocity never vanishes |
| Arc length | s = ∫ ‖γ′‖ dt; the natural parameter, with unit speed |
| Curvature κ | ‖T′‖ in arc length; the reciprocal of the osculating radius |
| Torsion τ | Rate at which the curve leaves its osculating plane, B′ = −τN |
| Frenet frame | The orthonormal triple (T, N, B) moving along the curve |
| Osculating circle | The circle of radius 1/κ in the plane of T and N that best fits the curve |
| Turning number | Net turning of the tangent of a closed plane curve, divided by 2π |
| Total curvature | ∫ κ ds over a closed curve |

## How it fits

- **Below:** [The derivative as a linear map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md) and [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md) give velocity and the osculating circle; [inner products](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md) give length and orthogonality.
- **Above:** Ordinary differential equations reconstruct a curve from its curvature, and total curvature constrains [knots](../../07-topology/03-manifolds/knot-theory.md).
- **Siblings:** Curves on a surface give the normal curvatures of [surfaces and Gaussian curvature](surfaces-and-gaussian-curvature.md) and the boundary term of [Gauss–Bonnet](the-gauss-bonnet-theorem.md); in [Riemannian manifolds](riemannian-manifolds.md) curves of zero geodesic curvature are geodesics.

## Common misconceptions

- **"Curvature is the second derivative"**: Only for unit speed; with another parametrisation γ″ also contains the change of speed, and κ = ‖γ′ × γ″‖/‖γ′‖³ in ℝ³.
- **"A smooth curve has a well-defined tangent everywhere"**: Smooth maps can have cusps where γ′ = 0; regularity is needed.
- **"Curvature is intrinsic to a curve"**: Every curve is locally isometric to a line; curvature describes how it sits in space, unlike the Gaussian curvature of a surface.

## Go deeper

- do Carmo, *Differential Geometry of Curves and Surfaces* (1976): the standard course, with Frenet–Serret and the global theorems.
- Pressley, *Elementary Differential Geometry* (2001): a gentler, example-led introduction.
- Needham, *Visual Differential Geometry and Forms* (2021): geometric intuition for curvature, drawn rather than computed.
