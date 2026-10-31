# 05 Abstract Algebra

> **Layer:** 05 Abstract Algebra
> **Children:** [Groups](01-groups/README.md) · [Rings and Fields](02-rings-and-fields/README.md) · [Galois Theory](03-galois-theory/README.md) · [Modules and Representations](04-modules-and-representations/README.md)

## What this area is about

Abstract algebra asks what structure alone implies. It takes the operations that appear across mathematics, such as composing symmetries, adding and multiplying numbers or polynomials, and applying linear maps. It strips them down to a few axioms and studies every system that satisfies those axioms at once. A theorem about groups is then a theorem about the symmetries of a crystal, the permutations of a deck of cards, the roots of a polynomial and the rotations of space, all proved together.

The payoff is a set of results that no amount of calculation in a single example could reach. Lagrange's theorem forces the order of a subgroup to divide the order of the group. Finite fields exist exactly in prime-power sizes. Unique factorisation, true in ℤ, fails in ℤ[√−5], and ideals repair it. Most famously, the general quintic equation has no formula in radicals, because the symmetric group S₅ is not solvable; the Greek problems of doubling the cube and trisecting the angle fall to the same method. The layer also finishes major classifications: finitely generated abelian groups, finite fields and the finite simple groups, the last a proof of thousands of pages.

## Why this layer sits here

From below, the layer needs four things:
- logic and set theory, for equivalence relations, quotients and, occasionally, Zorn's lemma, from [01 Sets and Foundations](../01-sets-and-foundations/README.md);
- the arithmetic of ℤ, ℤ/n and polynomials, from [02 Number Systems](../02-number-systems/README.md), which supplies the motivating examples;
- the counting arguments of [03 Combinatorics and Graph Theory](../03-combinatorics-and-graph-theory/README.md);
- vector spaces and dimension from [04 Linear Algebra](../04-linear-algebra/README.md). Degree of a field extension is a dimension, and Artin's lemma, at the heart of Galois theory, is a statement about linear equations.

Above it, [07 Topology](../07-topology/README.md) attaches groups and modules to spaces, [08 Geometry](../08-geometry/README.md) is organised by symmetry groups, and [12 Number Theory and Algebraic Geometry](../12-number-theory-and-algebraic-geometry/README.md) is built on rings, ideals and Galois groups. [13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md) abstracts the patterns found here into categories, and [14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md) computes in finite fields for codes and cryptography.

The one idea this layer contributes is that a structure is defined by its operations and their axioms, and is studied through the maps that preserve them: homomorphisms, their kernels and the quotients they produce. That idea, with symmetry made exact as a group, is used by nearly every layer above.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Groups](01-groups/README.md) | One operation: symmetry, quotients, actions, Sylow theory, simple groups and presentations | Sets, number theory |
| [Rings and Fields](02-rings-and-fields/README.md) | Two operations: ideals, factorisation, polynomials, extensions, finite fields, and localisation and the prime spectrum | Groups |
| [Galois Theory](03-galois-theory/README.md) | Fields studied through their symmetry groups; the quintic and the Greek construction problems | Groups, rings and fields |
| [Modules and Representations](04-modules-and-representations/README.md) | Linear algebra over rings, and groups acting by matrices | Groups, rings and fields, linear algebra |

Groups come first because they have the fewest axioms and the most examples, and because their basic constructions, the normal subgroup and the quotient, are reused in every later area as the ideal and the quotient ring, or the submodule and the quotient module. Rings and fields add a second operation; the area reaches field extensions measured by linear algebra, and ends with localisation and the prime spectrum, which hand rings on to algebraic geometry. Galois theory then joins the first two areas: it studies a field extension through a finite group, and solves classical problems by that translation. Modules and representations bring linear algebra back as the main tool, with the structure theorem for modules over a principal ideal domain and character theory for finite groups.

```
          groups ─────────────────────────────┐
            │                                 │
            v                                 v
     rings and fields ──> Galois theory   modules and representations
            │                                 ^
            └─────────────────────────────────┘
```

## Connections to neighbouring layers

- [02 Number Systems](../02-number-systems/README.md): ℤ/n, primitive roots and the Euclidean algorithm become rings, cyclic groups and Euclidean domains; algebraic and transcendental numbers become field theory.
- [03 Combinatorics and Graph Theory](../03-combinatorics-and-graph-theory/README.md): Burnside's lemma counts objects up to symmetry; Cayley graphs draw groups.
- [04 Linear Algebra](../04-linear-algebra/README.md): degrees are dimensions, the Jordan normal form is a corollary of the structure theorem for modules, and matrix groups are the first examples of non-abelian groups.
- [07 Topology](../07-topology/README.md): the fundamental group and homology are algebraic invariants of spaces, and covering spaces obey a correspondence parallel to Galois's.
- [08 Geometry](../08-geometry/README.md): the Erlangen programme defines a geometry by its symmetry group; Lie groups, studied there, are groups that are also smooth manifolds.
- [12 Number Theory and Algebraic Geometry](../12-number-theory-and-algebraic-geometry/README.md): ideals and class groups, varieties defined by polynomial ideals, and class field theory, which describes abelian Galois extensions.
- [13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md): categories generalise structures and morphisms, homological algebra studies modules through resolutions, and the word problem for groups is undecidable.
- [14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md): finite fields power error-correcting codes and cryptography.

## Connections across layers

- Below: [modular arithmetic](../02-number-systems/02-elementary-number-theory/modular-arithmetic.md) is the first quotient ring; [linear independence and dimension](../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md) measures field extensions; [the axiom of choice](../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) gives maximal ideals and algebraic closures.
- Above: [homology](../07-topology/02-algebraic-topology/homology.md), [the Langlands programme](../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md) and [undecidable problems](../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md) all use this layer's objects directly.
- In computer science: [abstract algebra for computing](../../cs-first-principles/01-mathematical-foundations/04-algebra/abstract-algebra.md), [public-key cryptography](../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md) and [error correction](../../cs-first-principles/02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) apply groups and finite fields.

## Cross-cutting threads

- [Symmetry](../CROSS-CUTTING.md#symmetry): groups make symmetry exact, and Galois groups are the symmetries of roots.
- [Structure and morphism](../CROSS-CUTTING.md#structure-and-morphism): homomorphisms, kernels and the isomorphism theorems.
- [Equivalence and quotients](../CROSS-CUTTING.md#equivalence-and-quotients): quotient groups, quotient rings and fields built as F[x]/(f).
- [Decomposition and classification](../CROSS-CUTTING.md#decomposition-and-classification): composition series, finite simple groups, finite fields and the structure theorem.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): the quintic, the three Greek problems and the word problem.
- [Invariants](../CROSS-CUTTING.md#invariants): orders, degrees, invariant factors and characters.
- [Dictionaries between fields](../CROSS-CUTTING.md#dictionaries-between-fields): the Galois correspondence between subgroups and fields.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): one set of axioms covers every example at once.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): splitting fields, algebraic closures and Sylow subgroups.
