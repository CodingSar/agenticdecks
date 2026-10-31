# Differential Forms and de Rham Cohomology

> **Layer:** [08 Geometry](../README.md) › [Differential Geometry](README.md)
> **Builds on:** [Exterior algebra](../../04-linear-algebra/04-multilinear-algebra/exterior-algebra.md), [Vector calculus and the integral theorems](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md), [Multiple integrals and change of variables](../../06-real-analysis/04-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md), [Topological and smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [Homology](../../07-topology/02-algebraic-topology/homology.md)
> **Enables:** [Riemannian manifolds](riemannian-manifolds.md), [Cauchy's theorem and its consequences](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md), [Homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md), [Hamiltonian systems and integrability](../../10-differential-equations-and-dynamics/04-dynamical-systems/hamiltonian-systems-and-integrability.md)

## Essence

Differential forms are the things that can be integrated over curves, surfaces and their higher-dimensional analogues, independently of coordinates. A single operator, the exterior derivative d, replaces gradient, curl and divergence, and a single theorem, Stokes's theorem ∫ dω = ∫ ω over the boundary, replaces the fundamental theorem of calculus, Green's, Stokes's and Gauss's theorems. Because d ∘ d = 0, every exact form is closed, and the closed forms that are not exact detect holes. De Rham's theorem (1931) shows that this calculus recovers exactly the real cohomology of the manifold, a bridge from analysis to topology.

## Core tenets

1. **A k-form is an alternating multilinear function of k tangent vectors, varying smoothly.** In coordinates a 2-form on ℝ³ is a dy∧dz + b dz∧dx + c dx∧dy, built from the [exterior algebra](../../04-linear-algebra/04-multilinear-algebra/exterior-algebra.md) of the dual space. Alternation gives dx∧dx = 0 and dx∧dy = −dy∧dx, so the form measures oriented area. Under a change of variables with Jacobian J, dx∧dy pulls back to det J du∧dv, which is exactly the [change-of-variables](../../06-real-analysis/04-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md) factor with sign. That is why forms, not functions, are what one integrates over oriented manifolds.

2. **The exterior derivative is unique, and d ∘ d = 0 because mixed partials commute.** There is exactly one linear operator d taking k-forms to (k+1)-forms that is the usual differential on functions, satisfies a graded Leibniz rule, and has d ∘ d = 0. For a function f, d(df) = Σ ∂²f/∂xⱼ∂xᵢ dxᵢ∧dxⱼ, and the symmetric coefficients cancel against the antisymmetric wedge. In ℝ³, d on 0-, 1- and 2-forms is grad, curl and div, so curl grad = 0 and div curl = 0 are both d ∘ d = 0.

3. **d commutes with pullback, so it is coordinate-free.** For a smooth map φ, the pullback of dω equals d of the pullback of ω. So d defined in any chart agrees on overlaps and makes sense on any [smooth manifold](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), with no metric needed.

4. **Stokes's theorem: ∫_M dω = ∫_∂M ω.** For a compact oriented n-manifold M with boundary ∂M (given the induced orientation) and an (n−1)-form ω, the integral of dω over M equals the integral of ω over ∂M. The proof uses a partition of unity to reduce to a form supported in one chart, where it is the fundamental theorem of calculus in one variable after Fubini. Compactness matters: on the open interval (0, 1), with no boundary, ∫ dx = 1 ≠ 0. The classical theorems of [vector calculus](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md) are the cases n = 1, 2, 3.

5. **Closed forms need not be exact, and the failure detects holes.** A form is closed if dω = 0 and exact if ω = dη; by d ∘ d = 0 exact forms are closed. The Poincaré lemma says that on a star-shaped region every closed form is exact. On ℝ² ∖ {0} the angle form dθ = (x dy − y dx)/(x² + y²) is closed, but its integral around the unit circle is 2π, while by Stokes an exact form integrates to 0 around any closed curve. So dθ is not exact, and the obstruction is the hole at the origin.

6. **De Rham cohomology measures closed forms modulo exact ones.** H^k_dR(M) is the vector space of closed k-forms divided by exact ones. H⁰ counts connected components (closed functions are locally constant), H¹(ℝ² ∖ {0}) is ℝ, spanned by dθ, and for a compact connected oriented n-manifold integration gives Hⁿ ≅ ℝ. The wedge product makes cohomology a ring, and pairing α with β by ∫ α∧β gives Poincaré duality.

7. **De Rham's theorem: H^k_dR(M) ≅ H^k(M; ℝ).** Integrating closed forms over smooth cycles defines a map from de Rham cohomology to the dual of real [homology](../../07-topology/02-algebraic-topology/homology.md). Stokes makes it well defined: an exact form integrates to 0 over a cycle, and a closed form integrates to 0 over a boundary. De Rham (1931) proved this map is an isomorphism, so calculus computes topology. The Hodge theorem adds that, given a metric on a compact manifold, each class contains exactly one harmonic form.

8. **Forms are the native language of physics and analysis.** Maxwell's equations become dF = 0 and d⋆F = J for the electromagnetic 2-form F. Cauchy's theorem in [complex analysis](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md) is Stokes applied to the closed form f(z) dz, and the symplectic form of [Hamiltonian mechanics](../../10-differential-equations-and-dynamics/04-dynamical-systems/hamiltonian-systems-and-integrability.md) is a closed non-degenerate 2-form.

## Key concepts

| Term | Meaning |
|---|---|
| k-form | A smoothly varying alternating multilinear function of k tangent vectors |
| Wedge product | The alternating product α∧β of forms |
| Exterior derivative | d: k-forms → (k+1)-forms; grad, curl and div in ℝ³ |
| Pullback | Transport of a form backwards along a smooth map |
| Closed form | dω = 0 |
| Exact form | ω = dη for some η |
| Poincaré lemma | On star-shaped regions closed forms are exact |
| De Rham cohomology | Closed forms modulo exact forms |
| Harmonic form | A form that is closed and co-closed for a given metric |

## How it fits

- **Below:** [Exterior algebra](../../04-linear-algebra/04-multilinear-algebra/exterior-algebra.md) supplies the wedge, multivariable calculus the change of variables and the classical integral theorems, and [homology](../../07-topology/02-algebraic-topology/homology.md) the topology that de Rham recovers.
- **Above:** Chain complexes with d ∘ d = 0 are the subject of [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md); symplectic forms underlie Hamiltonian systems.
- **Siblings:** Chern's proof of [Gauss–Bonnet](the-gauss-bonnet-theorem.md) writes the curvature as a form; [Riemannian manifolds](riemannian-manifolds.md) add a metric, which gives the Hodge star and harmonic forms.

## Common misconceptions

- **"dx is an infinitesimal number"**: It is a linear function on tangent vectors, the differential of the coordinate x.
- **"Closed and exact are the same"**: Only locally, by the Poincaré lemma; globally the difference is cohomology.
- **"Forms need a metric"**: d, wedge, pullback and Stokes's theorem are metric-free; only the Hodge star and harmonic forms need one.

## Go deeper

- Spivak, *Calculus on Manifolds* (1965): forms and the general Stokes theorem, in under 150 pages.
- Tu, *An Introduction to Manifolds* (2008): a careful first course ending with de Rham cohomology.
- Bott and Tu, *Differential Forms in Algebraic Topology* (1982): de Rham theory as a road into topology.
