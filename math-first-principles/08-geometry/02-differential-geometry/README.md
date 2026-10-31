# Differential Geometry

> **Layer:** [08 Geometry](../README.md) › Differential Geometry
> **Children:** [Curves and Curvature](curves-and-curvature.md) · [Surfaces and Gaussian Curvature](surfaces-and-gaussian-curvature.md) · [The Gauss–Bonnet Theorem](the-gauss-bonnet-theorem.md) · [Differential Forms and de Rham Cohomology](differential-forms-and-de-rham-cohomology.md) · [Riemannian Manifolds](riemannian-manifolds.md)

## What this area is about

Differential geometry uses calculus to measure shape. Its central quantity is curvature: how a curve bends, how a surface departs from its tangent plane, how parallel transport around a loop fails to return a vector to itself. The decisive discovery, Gauss's Theorema Egregium, is that the curvature of a surface can be measured from inside it, without reference to the surrounding space. Riemann turned that into a definition of geometry in any dimension: a manifold with a metric.

The second theme is local-to-global. Curvature is defined point by point, yet its integral over a closed surface is a topological invariant (Gauss–Bonnet), and differential forms, built from purely local calculus, recover the global cohomology of a manifold (de Rham). This area is where geometry, analysis and topology meet.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Curves and curvature](curves-and-curvature.md) | Curvature and torsion; Frenet–Serret; total curvature of closed curves | Calculus, inner products |
| [Surfaces and Gaussian curvature](surfaces-and-gaussian-curvature.md) | Fundamental forms, principal curvatures, the Theorema Egregium | Curves, quadratic forms |
| [The Gauss–Bonnet theorem](the-gauss-bonnet-theorem.md) | Total curvature = 2πχ; local geometry gives global topology | Surfaces, Euler characteristic |
| [Differential forms and de Rham cohomology](differential-forms-and-de-rham-cohomology.md) | d, the general Stokes theorem, cohomology from calculus | Exterior algebra, manifolds, homology |
| [Riemannian manifolds](riemannian-manifolds.md) | Metric, geodesics, connection and curvature in any dimension | Surfaces, Gauss–Bonnet |

The order follows dimension and abstraction. Curves have curvature but no intrinsic geometry, since every curve is locally a line. Surfaces have intrinsic curvature, K, and the Theorema Egregium separates it from the bending visible only in space. Gauss–Bonnet integrates K, and its turning-number ancestor already appears for plane curves. Differential forms supply the coordinate-free calculus for integrating over manifolds, and Riemannian manifolds generalise the first fundamental form to every dimension, where curvature becomes a tensor.

```
curves ──> surfaces ──> Gauss–Bonnet ──> differential forms
  κ, τ       K intrinsic   ∫K = 2πχ          d, Stokes, de Rham
                 \                               /
                  └──────> Riemannian manifolds <┘
                           metric, ∇, R; relativity
```

## Connections to sibling areas

- [Classical geometry](../01-classical-geometry/README.md): the sphere, the Euclidean plane and the hyperbolic plane are the constant-curvature surfaces, and the Erlangen programme becomes Cartan's curved geometry.
- [Convex and discrete geometry](../03-convex-and-discrete-geometry/README.md): angle defects of polyhedra are the discrete Gauss–Bonnet, and Euler's formula is its combinatorial shadow.
- [Lie theory](../04-lie-theory/README.md): Lie groups are smooth manifolds, and their exponential map is the group-theoretic cousin of the Riemannian one.

## Connections across layers

- [06 Real analysis](../../06-real-analysis/README.md): derivatives as linear maps, the inverse function theorem and the classical integral theorems are the raw material.
- [07 Topology](../../07-topology/README.md): manifolds, the Euler characteristic and homology are what curvature and forms detect.
- [10 Differential equations and dynamics](../../10-differential-equations-and-dynamics/README.md): geodesics and Frenet–Serret are ordinary differential equations; geodesics are variational.
- [14 Applied and computational mathematics](../../14-applied-and-computational-mathematics/README.md): general relativity is Lorentzian geometry.

## Cross-cutting threads

- [Local to global](../../CROSS-CUTTING.md#local-to-global): Gauss–Bonnet and de Rham's theorem.
- [Invariants](../../CROSS-CUTTING.md#invariants): Gaussian curvature as an isometry invariant; cohomology as a topological one.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): tangent spaces, the shape operator and the exponential map.
- [Duality](../../CROSS-CUTTING.md#duality): integration pairs forms with chains; Poincaré duality.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): no isometric flat map of the sphere; closed forms that are not exact.
