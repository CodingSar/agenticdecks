# Groups

> **Layer:** [05 Abstract Algebra](../README.md) › Groups
> **Children:** [Groups and Subgroups](groups-and-subgroups.md) · [Homomorphisms and Quotient Groups](homomorphisms-and-quotient-groups.md) · [Group Actions](group-actions.md) · [The Sylow Theorems](the-sylow-theorems.md) · [Composition Series and Simple Groups](composition-series-and-simple-groups.md) · [Free Groups and Presentations](free-groups-and-presentations.md)

## What this area is about

A group is the algebra of reversible operations: one associative operation, an identity and inverses. That is exactly what the symmetries of any object satisfy, so groups are symmetry made exact, whether the object is a polygon, a crystal, a polynomial's roots or a differential equation. This area asks what those three axioms alone imply, and the answers are surprisingly strong. Subgroup sizes divide the group's size; the structure of a group is constrained by the arithmetic of its order; every finite group breaks into simple pieces in an essentially unique way; and the simple pieces have all been found.

The area also marks where the subject stops being tame. Composition factors do not determine a group, the number of groups of a given order can be astronomically large, and for groups given by generators and relations even the question "is this word the identity?" has no algorithmic answer.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Groups and Subgroups](groups-and-subgroups.md) | The axioms, cyclic groups, Lagrange's theorem and its failed converse | Equivalence relations, modular arithmetic |
| [Homomorphisms and Quotient Groups](homomorphisms-and-quotient-groups.md) | Comparing groups; kernels, normal subgroups, quotients, the isomorphism theorems | Groups and subgroups |
| [Group Actions](group-actions.md) | Groups moving sets: orbit–stabiliser, Burnside's lemma, the class equation | Homomorphisms |
| [The Sylow Theorems](the-sylow-theorems.md) | Prime-power subgroups exist, are conjugate and are counted | Group actions |
| [Composition Series and Simple Groups](composition-series-and-simple-groups.md) | Breaking groups into simple factors; solvability; the classification | Quotients, Sylow |
| [Free Groups and Presentations](free-groups-and-presentations.md) | Describing groups by generators and relations, and the limits of doing so | Homomorphisms |

The first two leaves are the grammar: subgroups and cosets give divisibility, and normal subgroups give quotients. Group actions are the main technique, because the cleanest way to learn about a group is to let it move something and count. The Sylow theorems are the payoff of that technique for finite groups, and composition series turn the payoff into a programme: factor every group into simple groups, then classify the simple ones. Free groups go the other way, building groups from nothing and finding where computation breaks down.

```
groups and subgroups ──> homomorphisms and quotients ──> free groups and presentations
                                   │
                                   v
                             group actions ──> Sylow theorems ──> composition series
```

## Connections to sibling areas

- [Rings and Fields](../02-rings-and-fields/README.md): a ring is an abelian group with a second operation; ideals are the kernels of ring homomorphisms, exactly as normal subgroups are kernels here; the multiplicative group of a finite field is cyclic.
- [Galois Theory](../03-galois-theory/README.md): the Galois group of a polynomial acts on its roots, and the quintic is unsolvable because S₅ is not a solvable group.
- [Modules and Representations](../04-modules-and-representations/README.md): finitely generated abelian groups are classified as modules over ℤ, and representations study groups through their actions on vector spaces.

## Connections across layers

- Below: cosets come from [equivalence relations](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), and ℤ/n from [modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md); Burnside's lemma is [double counting](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md).
- Above: [fundamental groups](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) are given by presentations; [symmetry groups](../../08-geometry/01-classical-geometry/symmetry-groups-and-tilings.md) and the [Erlangen programme](../../08-geometry/01-classical-geometry/the-erlangen-programme.md) use groups to define geometry; [Lie groups](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md) add smoothness; the word problem is a classic [undecidable problem](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md); [cryptography](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) works in large cyclic groups.

## Cross-cutting threads

- [Symmetry](../../CROSS-CUTTING.md#symmetry): groups are the exact language of symmetry.
- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): cosets and quotient groups.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): Jordan–Hölder and the classification of finite simple groups.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the failed converse of Lagrange and the undecidable word problem.
