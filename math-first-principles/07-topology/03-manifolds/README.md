# Manifolds

> **Layer:** [07 Topology](../README.md) › Manifolds
> **Children:** [Topological and Smooth Manifolds](topological-and-smooth-manifolds.md) · [Classification of Surfaces](classification-of-surfaces.md) · [Knot Theory](knot-theory.md) · [Three-Manifolds and the Poincaré Conjecture](three-manifolds-and-the-poincare-conjecture.md)

## What this area is about

Manifolds are the spaces that look like ordinary ℝⁿ near every point: curves, surfaces, the 3-dimensional universe, configuration spaces of machines, groups of rotations. They are the natural meeting place of point-set and algebraic topology, because their local simplicity makes global invariants computable, and they are the stage on which geometry, mechanics and relativity are played. This area defines them, with charts and atlases and, when transition maps are differentiable, smooth structures, and then asks the classification question dimension by dimension.

The answers form a striking pattern. In dimension 2 the classification is complete and simple: orientability and the Euler characteristic decide everything. In dimension 3 the answer is geometric: Thurston's geometrisation, proved by Perelman through Hamilton's Ricci flow, cuts every closed 3-manifold into pieces modelled on eight geometries, and the Poincaré conjecture falls out as a special case. Knots, circles embedded in 3-space, are both a subject in their own right and a source of 3-manifolds. In dimension 4 and above no complete list is possible, since every finitely presented group occurs as a fundamental group, and smoothness becomes a subtle extra layer: Milnor's exotic 7-spheres and the exotic structures on ℝ⁴ show that a topological manifold can carry several inequivalent smooth structures.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Topological and smooth manifolds](topological-and-smooth-manifolds.md) | Definitions, charts and atlases, regular values, exotic spheres and exotic ℝ⁴ | Separation axioms, homology, 06 several-variable calculus |
| [Classification of surfaces](classification-of-surfaces.md) | Every closed surface is a sphere with handles or cross-caps | Manifolds, Euler characteristic, π₁ |
| [Knot theory](knot-theory.md) | Circles in 3-space; tricolourability, linking number, Alexander and Jones polynomials | Manifolds, π₁, covering spaces |
| [Three-manifolds and the Poincaré conjecture](three-manifolds-and-the-poincare-conjecture.md) | Decomposition, Thurston's eight geometries, Ricci flow with surgery | Surfaces, knots, π₁ |

The first leaf supplies the definitions and shows why "smooth" is more than "continuous". The other three climb in dimension. Surfaces are the solved case and the template: decompose by connected sum, then read off invariants. Knots are 1-dimensional objects whose interest lies entirely in how they sit in a 3-dimensional space, and their complements are the basic examples of 3-manifolds. The three-manifold leaf uses both: the decomposition imitates surfaces, and hyperbolic knot complements show that hyperbolic geometry is the typical case.

```
       topological and smooth manifolds
          │            │             │
          ▼            ▼             ▼
      surfaces       knots     (dimension ≥ 4:
     (dimension 2)  (in dim 3)  no classification;
          │            │         exotic smoothings)
          └─────┬──────┘
                ▼
     three-manifolds, geometrisation, Poincaré
```

## Connections to sibling areas

- [Point-set topology](../01-point-set-topology/README.md): the Hausdorff and second-countability conditions in the definition, Urysohn's metrisation theorem, and quotients for building surfaces from polygons.
- [Algebraic topology](../02-algebraic-topology/README.md): π₁ and χ distinguish surfaces; knot groups and the Alexander polynomial come from π₁ and covering spaces; homology proves invariance of dimension.

## Connections across layers

- [06 Real analysis](../../06-real-analysis/README.md): the inverse and implicit function theorems supply charts for solution sets of equations.
- [08 Geometry](../../08-geometry/README.md): Riemannian metrics, curvature, de Rham cohomology and Lie groups all live on smooth manifolds; Gauss–Bonnet ties curvature to χ.
- [09 Advanced analysis](../../09-advanced-analysis/README.md): compact Riemann surfaces are orientable surfaces with a complex structure.
- [10 Differential equations and dynamics](../../10-differential-equations-and-dynamics/README.md): Ricci flow is a nonlinear PDE; phase spaces are manifolds.
- [14 Applied and computational mathematics](../../14-applied-and-computational-mathematics/README.md): spacetime in general relativity; knot invariants from quantum field theory.
- [15 Mathematics in context](../../15-mathematics-in-context/README.md): the Poincaré conjecture as a solved Millennium problem; the smooth 4-dimensional Poincaré conjecture, open as of 2026.

## Cross-cutting threads

- [Local to global](../../CROSS-CUTTING.md#local-to-global): manifolds are locally trivial, and all their interest is global.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): connected sums of surfaces; prime and torus decompositions of 3-manifolds.
- [Invariants](../../CROSS-CUTTING.md#invariants): knot polynomials, Euler characteristic, orientability.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): no algorithm classifies 4-manifolds; some topological 4-manifolds have no smooth structure.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): Ricci flow deforms a metric towards a uniform geometry.
