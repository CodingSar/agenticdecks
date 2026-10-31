# Algebraic Topology

> **Layer:** [07 Topology](../README.md) › Algebraic Topology
> **Children:** [Homotopy and the Fundamental Group](homotopy-and-the-fundamental-group.md) · [Covering Spaces](covering-spaces.md) · [Homology](homology.md) · [The Euler Characteristic](the-euler-characteristic.md) · [Fixed-Point Theorems](fixed-point-theorems.md)

## What this area is about

How do you prove that two spaces are not homeomorphic, or that a map with some property cannot exist? Point-set invariants such as compactness and connectedness are too coarse: they cannot tell a sphere from a torus. Algebraic topology attaches algebraic objects, groups and their homomorphisms, to spaces and continuous maps, in a way that is unchanged by continuous deformation. If the groups differ, the spaces differ; if a map would force an impossible homomorphism, the map does not exist.

Two constructions do most of the work. The fundamental group π₁ records loops up to deformation; it is computed from path lifting in covering spaces and from the Seifert–van Kampen theorem, and its subgroups classify connected covers in exact parallel with the Galois correspondence of field theory. Homology replaces loops by formal sums of simplices and holes by cycles that are not boundaries; the identity ∂∂ = 0 makes it computable, and it gives the homology of spheres in every dimension. Their dividends are numerical and geometric: the Euler characteristic, which turns V − E + F into an invariant, and fixed-point theorems such as Brouwer's, which prove existence without construction.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Homotopy and the fundamental group](homotopy-and-the-fundamental-group.md) | Deformation, π₁, π₁(S¹) ≅ ℤ, Seifert–van Kampen | Connectedness, quotients, 05 groups |
| [Covering spaces](covering-spaces.md) | Path lifting; covers classified by subgroups of π₁; the Galois analogy | Fundamental group, 05 Galois correspondence |
| [Homology](homology.md) | Chains, ∂∂ = 0, homology of spheres, functoriality | Fundamental group, 05 quotient groups, 04 linear algebra |
| [The Euler characteristic](the-euler-characteristic.md) | χ = V − E + F as an alternating sum of Betti numbers | Homology, 03 planar graphs |
| [Fixed-point theorems](fixed-point-theorems.md) | Brouwer via no retraction, Lefschetz, Borsuk–Ulam, Nash equilibria | Homology, compactness |

The fundamental group comes first because it is the most concrete invariant and the one that needs the least machinery: one computation, π₁(S¹) ≅ ℤ, already proves the fundamental theorem of algebra and the two-dimensional Brouwer theorem. Covering spaces are both the tool that computes π₁ and the geometric meaning of its subgroups. Homology trades π₁'s non-abelian subtlety for linear algebra, and so reaches every dimension. The last two leaves cash in: the Euler characteristic is homology's simplest number, and fixed-point theorems are its most famous applications.

```
   fundamental group  <──────>  covering spaces
          │   (path lifting computes π₁; subgroups classify covers)
          ▼
       homology  (abelianised π₁ in degree 1; every dimension)
       │      │
       ▼      ▼
   Euler    fixed-point theorems
   characteristic ──┘ (L(identity) = χ)
```

## Connections to sibling areas

- [Point-set topology](../01-point-set-topology/README.md): compactness of [0, 1] underlies path lifting and the Lebesgue number argument; quotients build cell complexes.
- [Manifolds](../03-manifolds/README.md): π₁ and χ classify surfaces; knot groups and the Alexander polynomial come from π₁ and covers; the Poincaré conjecture is a statement about π₁.

## Connections across layers

- [05 Abstract algebra](../../05-abstract-algebra/README.md): groups, presentations, quotient groups and the Galois correspondence are the language and the model.
- [04 Linear algebra](../../04-linear-algebra/README.md): rank–nullity makes the Euler characteristic an invariant.
- [08 Geometry](../../08-geometry/README.md): de Rham cohomology recovers homology from calculus, and Gauss–Bonnet equates total curvature with 2πχ.
- [13 Structure and metamathematics](../../13-structure-and-metamathematics/README.md): homological algebra generalises chain complexes, and homotopy type theory reads types as spaces.
- [14 Applied and computational mathematics](../../14-applied-and-computational-mathematics/README.md): Kakutani's fixed-point theorem gives Nash equilibria.

## Cross-cutting threads

- [Invariants](../../CROSS-CUTTING.md#invariants): π₁, homology and χ are unchanged by homeomorphism and homotopy.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): no retraction of a disc onto its boundary; ℝⁿ is not homeomorphic to ℝᵐ for n ≠ m.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): covering spaces and field extensions share one correspondence.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): homology turns spaces into vector spaces and abelian groups.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Brouwer proves a fixed point exists without locating it.
