# Vector Bundles, Connections and Characteristic Classes

> **Layer:** [08 Geometry](../README.md) › [Differential Geometry](README.md)
> **Builds on:** [Differential forms and de Rham cohomology](differential-forms-and-de-rham-cohomology.md), [Riemannian manifolds](riemannian-manifolds.md), [Cohomology and Poincaré duality](../../07-topology/02-algebraic-topology/cohomology-and-poincare-duality.md), [Lie groups and Lie algebras](../04-lie-theory/lie-groups-and-lie-algebras.md)
> **Enables:** [Symplectic geometry](symplectic-geometry.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md), [Algebraic curves and Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md)

## Essence

A vector bundle attaches a vector space to each point of a manifold, varying smoothly and looking like a product over small regions, but possibly twisted globally, as the Möbius band twists a line around a circle. The tangent bundle is the first example, and vector fields are its sections. Comparing vectors in different fibres needs extra data, a connection, whose failure to be flat is its curvature, generalising the Levi-Civita connection and Riemann curvature. Characteristic classes are cohomology classes that measure the global twisting; Chern–Weil theory computes them by integrating polynomials in the curvature, which makes Gauss–Bonnet one instance of a general principle. In physics connections are gauge fields, the language of the Standard Model.

## Core tenets

1. **A vector bundle is locally a product, glued by linear maps.** A rank-k bundle E → M has a vector space Eₓ over each point and, over small open sets U, an identification of E with U × ℝᵏ. On overlaps two identifications differ by transition functions with values in GL(k, ℝ). The tangent bundle TM, normal bundles and the trivial bundle M × ℝᵏ are examples. The Möbius line bundle over the circle is not trivial: removing its zero section leaves one piece, not two as for S¹ × ℝ.

2. **Sections detect twisting.** A section picks a vector in each fibre smoothly; vector fields are sections of TM. A rank-k bundle is trivial if and only if it has k sections that are independent at every point. The hairy ball theorem says TS² has no non-vanishing section, so it is not trivial. Among spheres, only S¹, S³ and S⁷ have trivial tangent bundles.

3. **A connection differentiates sections, and is locally d plus a matrix of 1-forms.** Fibres at different points are not canonically identified, so differentiating a section needs a connection ∇, an operator obeying ∇_X(fs) = (Xf)s + f∇_X s. In a local trivialisation ∇ = d + A, where A is a matrix of [1-forms](differential-forms-and-de-rham-cohomology.md); changing the trivialisation by g: U → GL(k) changes A to g⁻¹Ag + g⁻¹dg. Connections exist on every bundle, by gluing local ones with a partition of unity, and any two differ by a matrix-valued 1-form. The [Levi-Civita connection](riemannian-manifolds.md) is the special connection on TM fixed by a metric.

4. **Curvature is the obstruction to flatness, seen as holonomy.** The curvature F = dA + A∧A is a matrix-valued 2-form, and under a change of trivialisation it is conjugated, F ↦ g⁻¹Fg, so its trace and determinant are well defined. Parallel transport along a curve carries fibres to fibres; around a small loop it differs from the identity by approximately F applied to the enclosed area. F = 0 exactly when transport depends only on the homotopy class of the path, and then the bundle is described by a representation of the fundamental group.

5. **Chern–Weil: polynomials in the curvature give topological invariants.** For a polynomial P invariant under conjugation, P(F) is a closed form, and its de Rham class does not depend on the connection: along a path of connections, the derivative of P(F) is exact. Chern classes of complex bundles come from det(I + iF/2π), Pontryagin classes of real bundles similarly, and the Euler class of an oriented bundle of even rank from the Pfaffian, a square root of the determinant. The Chern–Gauss–Bonnet theorem says the Euler class of TM, integrated over a closed oriented even-dimensional manifold, is the Euler characteristic; for surfaces this is [Gauss–Bonnet](the-gauss-bonnet-theorem.md). Stiefel–Whitney classes, with ℤ/2 coefficients, detect orientability and do not come from curvature.

6. **Characteristic classes obstruct and classify.** The Euler class vanishes when there is a nowhere-zero section, and the top Stiefel–Whitney class of TM is χ mod 2. Complex line bundles are classified by their first Chern class c₁ in H²(M; ℤ), via [cohomology](../../07-topology/02-algebraic-topology/cohomology-and-poincare-duality.md); over the sphere S², c₁ is an integer, the degree. Dirac's argument that magnetic charge is quantised is this integrality: the field of a monopole is the curvature of a line bundle over a sphere surrounding it.

7. **Gauge theory is the geometry of connections.** In physics a gauge field is a connection on a bundle with structure group a [Lie group](../04-lie-theory/lie-groups-and-lie-algebras.md), and the field strength is its curvature. For electromagnetism the group is U(1), the potential is A and F = dA; Maxwell's equation dF = 0 is the Bianchi identity, and the Aharonov–Bohm effect measures holonomy where F = 0. Yang and Mills (1954) proposed non-abelian groups, and the Standard Model uses SU(3) × SU(2) × U(1). Donaldson used moduli spaces of solutions of the Yang–Mills equations on 4-manifolds to distinguish smooth structures. Whether quantum Yang–Mills theory exists with a mass gap is a Millennium Prize problem, open as of 2026.

## Key concepts

| Term | Meaning |
|---|---|
| Vector bundle | A family of vector spaces over a manifold, locally a product |
| Section | A smooth choice of vector in each fibre |
| Connection | A rule ∇ for differentiating sections; locally d + A |
| Curvature | F = dA + A∧A; the matrix-valued 2-form measuring non-flatness |
| Holonomy | The linear map obtained by parallel transport around a loop |
| Characteristic class | A cohomology class of the base measuring the twisting of a bundle |
| Chern–Weil theory | Building characteristic classes from invariant polynomials in F |

## How it fits

- **Below:** [Differential forms](differential-forms-and-de-rham-cohomology.md) carry A and F; [Riemannian manifolds](riemannian-manifolds.md) give the motivating connection; [cohomology](../../07-topology/02-algebraic-topology/cohomology-and-poincare-duality.md) holds the classes; [Lie groups](../04-lie-theory/lie-groups-and-lie-algebras.md) are the structure groups.
- **Above:** Gauge fields and spinors in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md); the Christoffel connection of [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md); line bundles and their degrees in [Riemann–Roch](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md).
- **Siblings:** [Gauss–Bonnet](the-gauss-bonnet-theorem.md) is the first Chern–Weil formula; in [symplectic geometry](symplectic-geometry.md) the cotangent bundle is phase space and prequantisation uses a line bundle whose curvature is the symplectic form.

## Common misconceptions

- **"Locally trivial means trivial"**: The Möbius band and the tangent bundle of S² are locally products but globally twisted.
- **"A bundle has one natural connection"**: Connections form an affine space; only the characteristic classes are independent of the choice.
- **"Bundle curvature is the curvature of the base"**: The two are independent: the monopole bundle over ℝ³ minus a point, a flat base, is curved, and a trivial bundle with the trivial connection is flat over any base.

## Go deeper

- Milnor and Stasheff, *Characteristic Classes* (1974): the classic on Stiefel–Whitney, Chern, Pontryagin and Euler classes.
- Baez and Muniain, *Gauge Fields, Knots and Gravity* (1994): bundles and connections from the physics end.
- Taubes, *Differential Geometry: Bundles, Connections, Metrics and Curvature* (2011): a full modern treatment.
