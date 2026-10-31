# Convex and Discrete Geometry

> **Layer:** [08 Geometry](../README.md) › Convex and Discrete Geometry
> **Children:** [Convex Sets and Separation](convex-sets-and-separation.md) · [Polytopes](polytopes.md) · [Lattices and Sphere Packing](lattices-and-sphere-packing.md)

## What this area is about

Convex and discrete geometry studies shapes defined by finitely many pieces of linear data: half-spaces, vertices, lattice points. Convexity is the single condition that makes such shapes tractable, because a convex set can always be separated from an outside point by a hyperplane. That one fact gives duality in optimisation, the minimax theorem and, in infinite dimensions, the Hahn–Banach theorem. Discreteness adds counting: how many faces a polytope has, which regular polytopes exist, how many balls can touch one ball.

The area mixes very old and very new mathematics. Euler's formula and the Platonic solids are classical; the proof of Kepler's conjecture needed computers and a formal verification completed in 2014, and the sphere-packing problem in dimensions 8 and 24 was solved only in 2016.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Convex sets and separation](convex-sets-and-separation.md) | Nearest points, separating hyperplanes, Carathéodory, Helly and Farkas | Inner products, compactness |
| [Polytopes](polytopes.md) | Finite convex hulls; Euler's formula; regular polytopes in every dimension | Convex sets, Euler characteristic |
| [Lattices and sphere packing](lattices-and-sphere-packing.md) | Discrete subgroups of ℝⁿ; Minkowski; Kepler, E₈ and Leech | Convex sets, polytopes, quadratic forms |

Separation comes first because both other children use it: a polytope's two descriptions, by vertices and by inequalities, are equivalent by a separation argument, and Minkowski's lattice-point theorem is a statement about symmetric convex bodies. Polytopes come next because lattices produce them, as Voronoi cells and fundamental domains, and because the regular polytopes and the exceptional lattices share symmetry groups. Sphere packing closes the area by combining all three: convex bodies, lattices and, in Viazovska's proofs, Fourier analysis.

```
convex sets ── separation, Farkas ──> duality in optimisation
     │
     ├──> polytopes ── Euler, regular solids, simplex method
     │        │
     └────────┴──> lattices ── Minkowski, packing, E₈, Leech
```

## Connections to sibling areas

- [Classical geometry](../01-classical-geometry/README.md): crystallographic lattices and the Platonic symmetry groups come from symmetry groups and tilings.
- [Differential geometry](../02-differential-geometry/README.md): the angle defect of a polyhedron is the discrete Gaussian curvature, and Descartes's 4π is Gauss–Bonnet.
- [Lie theory](../04-lie-theory/README.md): the E₈ lattice is a root lattice, and root systems are finite configurations of vectors classified by convex-geometric arguments.

## Connections across layers

- [04 Linear algebra](../../04-linear-algebra/README.md): inner products, determinants and quadratic forms are the basic tools.
- [09 Advanced analysis](../../09-advanced-analysis/README.md): Hahn–Banach is separation in infinite dimensions, and the Fourier transform drives the packing bounds.
- [12 Number theory and algebraic geometry](../../12-number-theory-and-algebraic-geometry/README.md): Minkowski's theorem proves finiteness of class numbers; modular forms built the magic functions.
- [14 Applied and computational mathematics](../../14-applied-and-computational-mathematics/README.md): linear and convex optimisation, codes and lattice cryptography.
- [15 Mathematics in context](../../15-mathematics-in-context/README.md): Flyspeck is a landmark of computer-verified proof.

## Cross-cutting threads

- [Duality](../../CROSS-CUTTING.md#duality): points versus half-spaces; Farkas's lemma and linear programming duality.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): nearest points, densest packings, best vertices.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): the regular polytopes in every dimension.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): codes, lattices and modular forms in dimensions 8 and 24.
