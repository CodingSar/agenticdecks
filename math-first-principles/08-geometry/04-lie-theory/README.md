# Lie Theory

> **Layer:** [08 Geometry](../README.md) › Lie Theory
> **Children:** [Lie Groups and Lie Algebras](lie-groups-and-lie-algebras.md) · [The Classification of Simple Lie Algebras](the-classification-of-simple-lie-algebras.md) · [Representations of Lie Groups](representations-of-lie-groups.md)

## What this area is about

Lie theory studies continuous symmetry. The rotations of space, the unitary transformations of quantum states and the Lorentz transformations of relativity are not finite groups but smooth families, groups that are also manifolds. Sophus Lie's idea, in the 1870s, was to study such a group through its infinitesimal elements, which form a vector space with a bracket. That linearisation turns geometry into algebra, and the algebra turns out to be rigid enough to classify: the simple Lie algebras over ℂ form four infinite families and five exceptions, found by Killing and made rigorous by Cartan. Representation theory then asks how these groups act linearly, and answers with highest weights, characters and the Peter–Weyl theorem.

The area is where Klein's [Erlangen programme](../01-classical-geometry/the-erlangen-programme.md) becomes a working tool. If a geometry is a space with a group of symmetries, Lie theory supplies the groups and their structure.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Lie groups and Lie algebras](lie-groups-and-lie-algebras.md) | Groups that are manifolds; tangent algebra, exponential map, coverings; SU(2) and SO(3) | Group actions, smooth manifolds, covering spaces |
| [The classification of simple Lie algebras](the-classification-of-simple-lie-algebras.md) | Killing form, roots, Dynkin diagrams; Aₙ, Bₙ, Cₙ, Dₙ and the five exceptions | Lie algebras, diagonalisation, quadratic forms |
| [Representations of Lie groups](representations-of-lie-groups.md) | Linear actions; complete reducibility, highest weights, spin, Peter–Weyl | Lie groups, the classification, finite-group representations |

The first child sets up the dictionary between groups and algebras and shows its limit: the algebra sees a group only up to coverings, so SU(2) and SO(3) look the same infinitesimally. The second child uses that dictionary to reduce structure to combinatorics, passing from an algebra to a root system to a Dynkin diagram. The third child returns to groups: representations of sl(2) explain spin, and the root geometry of the classification labels the irreducible representations of every semisimple group. The SU(2) double cover runs through all three.

```
Lie group ──differentiate──> Lie algebra ──roots──> Dynkin diagram
    ▲                             │                      │
    └── exponentiate ─────────────┘                      ▼
                                              highest weights label
                                              irreducible representations
```

## Connections to sibling areas

- [Classical geometry](../01-classical-geometry/README.md): the isometry groups of Euclidean, spherical and hyperbolic space are Lie groups, and the Erlangen programme reads each geometry from its group.
- [Differential geometry](../02-differential-geometry/README.md): Lie groups are manifolds, isometry groups of Riemannian manifolds are Lie groups, and symmetric spaces are quotients of Lie groups.
- [Convex and discrete geometry](../03-convex-and-discrete-geometry/README.md): root systems are finite configurations of vectors, the E₈ roots are the minimal vectors of the E₈ lattice, and Weyl groups are symmetry groups of polytopes.

## Connections across layers

- [04 Linear algebra](../../04-linear-algebra/README.md): eigenvalues, inner products and quadratic forms drive the classification.
- [05 Abstract algebra](../../05-abstract-algebra/README.md): group actions and the representations of finite groups are the discrete models.
- [07 Topology](../../07-topology/README.md): manifolds, covering spaces and the fundamental group ℤ/2 of SO(3).
- [09 Advanced analysis](../../09-advanced-analysis/README.md): the Peter–Weyl theorem is Fourier analysis on compact groups.
- [10 Differential equations and dynamics](../../10-differential-equations-and-dynamics/README.md): [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md) turns one-parameter symmetry groups into conservation laws.
- [12 Number theory and algebraic geometry](../../12-number-theory-and-algebraic-geometry/README.md): the Langlands programme is organised by reductive groups and their representations.
- [14 Applied and computational mathematics](../../14-applied-and-computational-mathematics/README.md): spin in quantum mechanics, and the Lorentz group in [the geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md).

## Cross-cutting threads

- [Symmetry](../../CROSS-CUTTING.md#symmetry): continuous symmetry groups and their actions.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): replacing a curved group by its tangent algebra.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): simple algebras by Dynkin diagrams, representations by highest weights.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): the algebra fixes the group only up to coverings.
