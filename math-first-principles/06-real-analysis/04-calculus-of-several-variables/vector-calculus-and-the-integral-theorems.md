# Vector Calculus and the Integral Theorems

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of Several Variables](README.md)
> **Builds on:** [Multiple integrals and change of variables](multiple-integrals-and-change-of-variables.md), [The derivative as a linear map](the-derivative-as-a-linear-map.md), [The fundamental theorem of calculus](../02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md)
> **Enables:** [Differential forms and de Rham cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), [Laplace's equation and harmonic functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md), [The heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), [Cauchy's theorem and its consequences](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md), [Fluids, pressure and flow (medicine)](../../../medicine-first-principles/00-physical-and-chemical-foundations/01-physics-of-the-body/fluids-pressure-and-flow.md)

## Essence

The fundamental theorem of calculus says that integrating a derivative over an interval gives the values at its two endpoints. Vector calculus finds the same pattern one dimension up, twice more. Green's theorem trades the integral of a rotation density over a plane region for a line integral round its edge. Stokes' theorem does this for a surface in space, and the divergence theorem trades the total outflow density in a solid for the flux through its boundary surface. All of them are cases of one statement, ∫_M dω = ∫_∂M ω, made precise by differential forms.

## Core tenets

1. **Line and surface integrals are defined through parametrisations.** For a curve γ: [a, b] → ℝ³ and a vector field F, the work integral is
   ```
   ∫_γ F · dr = ∫ₐᵇ ⟨F(γ(t)), γ′(t)⟩ dt
   ```
   which does not change under reparametrisations that keep the direction. For a surface r(u, v), the flux of F is the integral of ⟨F, n⟩, where n is the unit normal, over the area element ∥r_u × r_v∥ du dv. These definitions rest on the [change of variables formula](multiple-integrals-and-change-of-variables.md).

2. **grad, div and curl measure change, outflow and rotation.** For a function f and a field F = (F₁, F₂, F₃):
   - grad f = ∇f, the direction and rate of steepest increase;
   - div F = ∂F₁/∂x + ∂F₂/∂y + ∂F₃/∂z, the net outflow per unit volume at a point;
   - curl F = ∇ × F, whose component along a unit vector n is the circulation per unit area in the plane perpendicular to n.
   
   For C² functions and fields, curl grad f = 0 and div curl F = 0, because mixed partial derivatives commute.

3. **Line integrals of gradients depend only on the endpoints.** If F = ∇f on an open set, then ∫_γ F · dr = f(γ(b)) − f(γ(a)): this is the fundamental theorem of calculus applied to t ↦ f(γ(t)). So the integral round every closed loop is 0. Conversely, if every closed loop gives 0, then f(x), defined as the integral from a fixed point to x along any path, is a potential with ∇f = F. Such fields are called conservative.

4. **Zero curl does not make a field a gradient: holes in the domain obstruct it.** On the plane with the origin removed, let
   ```
   F(x, y) = (−y, x)/(x² + y²)
   ```
   Its curl is 0 everywhere in the domain, yet its integral once anticlockwise round the unit circle is 2π, not 0. So F is not a gradient. Locally it is the gradient of the polar angle θ, which cannot be defined continuously round the origin. On a star-shaped domain, curl-free fields are gradients (the Poincaré lemma). The general obstruction is measured by [de Rham cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), and the 2π counts how many times the loop winds round the hole.

5. **Green's theorem.** Let D be a bounded region in the plane whose boundary ∂D is a piecewise C¹ curve traversed anticlockwise, and let P and Q be C¹ on a neighbourhood of D. Then
   ```
   ∮_∂D (P dx + Q dy) = ∬_D (∂Q/∂x − ∂P/∂y) dA
   ```
   Proof idea: for a rectangle, integrate ∂Q/∂x in x first; the fundamental theorem of calculus leaves Q on the two vertical edges, with opposite signs, and the same happens for P on the horizontal edges. For a region made of many rectangles, each interior edge is traversed twice in opposite directions and cancels, leaving only the outer boundary. With P = −y/2 and Q = x/2 it gives area(D) = ½∮(x dy − y dx). Green published the theorem in 1828.

6. **Stokes' theorem and the divergence theorem.** For an oriented surface S with boundary curve ∂S, traversed consistently with the normal, and a C¹ field F,
   ```
   ∬_S ⟨curl F, n⟩ dA = ∮_∂S F · dr
   ∭_V div F dV = ∬_∂V ⟨F, n⟩ dA      (n pointing outward)
   ```
   The orientation hypothesis matters: the Möbius band has no continuous choice of unit normal, so the left side of Stokes' theorem is not even defined on it. All three theorems, and the fundamental theorem of calculus, are cases of ∫_M dω = ∫_∂M ω for [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md).

7. **The divergence theorem turns conservation laws into differential equations.** If ρ is the density of a substance moving with velocity v, the amount in any small region changes only by flux through its boundary. Applying the divergence theorem to arbitrarily small regions gives the continuity equation ∂ρ/∂t + div(ρv) = 0, the basis of [fluid flow (medicine)](../../../medicine-first-principles/00-physical-and-chemical-foundations/01-physics-of-the-body/fluids-pressure-and-flow.md). If heat flows down the temperature gradient, the same reasoning gives [the heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) ∂u/∂t = kΔu, where the Laplacian Δ = div grad.

## Key concepts

| Term | Meaning |
|---|---|
| Line integral | ∫⟨F(γ(t)), γ′(t)⟩ dt, the work done by F along a curve |
| Flux | The integral of ⟨F, n⟩ over a surface, the rate of flow through it |
| Divergence | Outflow per unit volume |
| Curl | Circulation per unit area, as a vector |
| Conservative field | A gradient field; its loop integrals are all 0 |
| Laplacian Δ | div grad, the sum of the unmixed second partial derivatives |
| Orientation | A consistent choice of direction on a curve or of normal on a surface |
| Star-shaped domain | Contains the segment from one fixed point to each of its points |

## How it fits

- **Below:** [The fundamental theorem of calculus](../02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md) is the one-dimensional case and is used inside every proof; [multiple integrals](multiple-integrals-and-change-of-variables.md) give the double and triple integrals; [the derivative as a linear map](the-derivative-as-a-linear-map.md) gives grad, div and curl.
- **Above:** [Differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md) unify the theorems in any dimension. [Cauchy's theorem](../../09-advanced-analysis/02-complex-analysis/cauchys-theorem-and-its-consequences.md) is Green's theorem combined with the Cauchy–Riemann equations. Harmonic functions, with Δu = 0, are the subject of [Laplace's equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md).
- **Siblings:** [Change of variables](multiple-integrals-and-change-of-variables.md) makes the integrals independent of parametrisation.

## Common misconceptions

- **"A field with zero curl is a gradient."** Only on domains without holes; (−y, x)/(x² + y²) is the counterexample (tenet 4).
- **"Green, Stokes and Gauss are three unrelated theorems."** They are one theorem about boundaries, in dimensions 2, 2 and 3 (tenet 6).
- **"Divergence and curl are just formulas."** They are densities: of outflow and of circulation. The integral theorems say exactly this.

## Go deeper

- H. M. Schey, *Div, Grad, Curl, and All That* (4th edition, 2005): an informal, physically motivated introduction.
- Jerrold E. Marsden and Anthony Tromba, *Vector Calculus* (6th edition, 2012): the three theorems with proofs and applications to physics.
- Michael Spivak, *Calculus on Manifolds* (1965): chapter 5 proves the general Stokes theorem and recovers the classical ones.
