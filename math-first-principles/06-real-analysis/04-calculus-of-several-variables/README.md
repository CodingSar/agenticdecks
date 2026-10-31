# Calculus of Several Variables

> **Layer:** [06 Real Analysis](../README.md) › Calculus of Several Variables
> **Children:** [The derivative as a linear map](the-derivative-as-a-linear-map.md) · [Inverse and implicit function theorems](inverse-and-implicit-function-theorems.md) · [Extrema and Lagrange multipliers](extrema-and-lagrange-multipliers.md) · [Multiple integrals and change of variables](multiple-integrals-and-change-of-variables.md) · [Vector calculus and the integral theorems](vector-calculus-and-the-integral-theorems.md)

## What this area is about

Most quantities depend on more than one variable, so calculus has to work in ℝⁿ. The step from one variable to several is not just more of the same. The derivative stops being a number and becomes a linear map, so linear algebra becomes part of calculus. Partial derivatives turn out to be weaker than differentiability. And integrals over regions bring in geometry: volume scaling, orientation, and boundaries.

The central idea is that a smooth map looks linear near each point, and that many of its local properties can be read off from that linear approximation. If the derivative is invertible, the map can be inverted nearby. If it has full rank, the solution set of an equation is a smooth surface. If it vanishes, the point is a candidate for an extremum, and the Hessian decides. On the integration side, the determinant of the derivative measures how a substitution stretches volume, and the theorems of Green, Stokes and Gauss relate integrals over a region to integrals over its boundary.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The derivative as a linear map](the-derivative-as-a-linear-map.md) | Defines Df(a), the Jacobian, the gradient and the Hessian; the chain rule as matrix product | One-variable derivative; linear maps (layer 04) |
| [Inverse and implicit function theorems](inverse-and-implicit-function-theorems.md) | An invertible or full-rank derivative gives local inverses and smooth level sets | The derivative; contraction mapping principle (area 03) |
| [Extrema and Lagrange multipliers](extrema-and-lagrange-multipliers.md) | Critical points, the Hessian test, and constrained optimisation | The derivative; implicit functions; compactness (area 03) |
| [Multiple integrals and change of variables](multiple-integrals-and-change-of-variables.md) | Integrals over regions, Fubini, and the Jacobian determinant | Riemann integral; the derivative; inverse functions |
| [Vector calculus and the integral theorems](vector-calculus-and-the-integral-theorems.md) | grad, div, curl; Green, Stokes and divergence theorems | Multiple integrals; the derivative; FTC |

```
             the derivative as a linear map
              ┌──────────┴──────────┐
  inverse and implicit fns     (Jacobian, Hessian)
      │           │                  │
   extrema    multiple integrals ────┘
                  │
           vector calculus
```

Start with [the derivative as a linear map](the-derivative-as-a-linear-map.md): every other child uses its definitions. The differential strand runs through the [inverse and implicit function theorems](inverse-and-implicit-function-theorems.md), whose proof uses the contraction mapping principle, to [extrema](extrema-and-lagrange-multipliers.md), where the implicit function theorem justifies Lagrange multipliers. The integral strand runs from [multiple integrals](multiple-integrals-and-change-of-variables.md), which needs a local inverse to change variables, to [vector calculus](vector-calculus-and-the-integral-theorems.md), the multivariable form of the fundamental theorem of calculus (FTC).

The two strands meet in one theme: the derivative controls the map locally. Its invertibility gives local inverses, its rank gives the dimension of level sets, its zeros give critical points, and its determinant gives the volume factor.

## Connections to sibling areas

- [Limits and convergence](../01-limits-and-convergence/README.md): limits and continuity in ℝⁿ use the norm in place of the absolute value, and Cauchy–Schwarz explains why the gradient gives the steepest ascent.
- [Calculus of one variable](../02-calculus-of-one-variable/README.md): every proof here reduces to one-variable facts along lines or coordinates: the mean value theorem, Taylor's theorem, the Riemann integral and the FTC.
- [Metric spaces](../03-metric-spaces/README.md): the contraction mapping principle proves the inverse function theorem, and compactness guarantees that extrema exist. The dependence runs one way, from this area to that one.

## Connections across layers

From below, this area uses [linear maps and matrices](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [determinants](../../04-linear-algebra/02-determinants-and-eigenvalues/determinants.md) and [quadratic forms](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md). Above, the implicit function theorem makes level sets into [smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), and the integral theorems become the general Stokes theorem for [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md). The divergence theorem turns conservation laws into [the heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md), and Lagrange multipliers grow into [convex optimisation and duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md). In computing, the chain rule is [backpropagation](../../../cs-first-principles/13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md) and the Jacobian drives [geometric transformations](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md).

## Cross-cutting threads

- [Linearisation](../../CROSS-CUTTING.md#linearisation): a smooth map is studied through its derivative, a linear map, at each point.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): the inverse function theorem is only local, and zero curl gives a global potential only on domains without holes.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): critical points, the Hessian test and Lagrange multipliers.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the field (−y, x)/(x² + y²) is curl-free but not a gradient, detecting the hole it circles.
