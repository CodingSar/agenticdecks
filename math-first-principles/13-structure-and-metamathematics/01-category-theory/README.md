# Category Theory

> **Layer:** [13 Structure and Metamathematics](../README.md) › Category Theory
> **Children:** [Categories and functors](categories-and-functors.md) · [Natural transformations and the Yoneda lemma](natural-transformations-and-the-yoneda-lemma.md) · [Universal properties and adjunctions](universal-properties-and-adjunctions.md) · [Homological algebra](homological-algebra.md) · [Higher categories and homotopy type theory](higher-categories-and-homotopy-type-theory.md)

## What this area is about

Every earlier layer studied some kind of structure together with the maps that preserve it: groups and homomorphisms, vector spaces and linear maps, spaces and continuous maps. Category theory takes that pattern as the object of study. It describes things by their relationships rather than their elements, so that a product, a quotient or a free object is defined once, by a universal property, and recognised in every field at the same time. Its theorems are often short, but they explain why constructions in distant subjects behave alike, and they let a problem be moved, by a functor, to a field where it is easier.

The unifying idea is that *an object is known by its maps*. The Yoneda lemma makes this precise, universal properties exploit it, homological algebra applies it to complexes of modules, and higher category theory relaxes "equal" to "homotopic" throughout.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Categories and functors](categories-and-functors.md) | the language: objects, arrows, functors, duality, equivalence | 01 functions, 05 groups, 07 topology |
| [Natural transformations and the Yoneda lemma](natural-transformations-and-the-yoneda-lemma.md) | maps between functors; an object is determined by the maps into it | categories and functors |
| [Universal properties and adjunctions](universal-properties-and-adjunctions.md) | products, quotients, free objects and tensor products as universal constructions; adjoint functors | Yoneda |
| [Homological algebra](homological-algebra.md) | chain complexes, exact sequences, the snake lemma, Tor and Ext | adjunctions, 05 modules, 07 homology |
| [Higher categories and homotopy type theory](higher-categories-and-homotopy-type-theory.md) | ∞-categories, Curry–Howard, univalence | all of the above, 00 constructive logic |

Read them in order. The first leaf gives the vocabulary and shows its first use, the fundamental group as a functor. The second shows that functors themselves form categories, and proves the lemma that every later leaf uses: a universal construction is the statement that some functor is representable, and Yoneda makes it unique up to unique isomorphism. The third collects the constructions of earlier layers under limits, colimits and adjunctions. The last two branch: homological algebra measures how far additive functors such as ⊗ and Hom fail to preserve exactness, and higher categories keep track of homotopies instead of equations.

```
 categories and functors
          ↓
 natural transformations, Yoneda
          ↓
 universal properties, adjunctions
          ↓                 ↘
 homological algebra  →  higher categories and HoTT
```

## Connections to sibling areas

- **[Computability and incompleteness](../02-computability-and-incompleteness/README.md)** meets this area in the Curry–Howard correspondence, where proofs are programs and, following Joachim Lambek, arrows of a cartesian closed category; F. William Lawvere's fixed-point theorem (1969) shows that Cantor's diagonal argument, the halting problem and Gödel's diagonal lemma share one categorical form.
- **[Model theory and independence](../03-model-theory-and-independence/README.md)** supplies the inaccessible cardinals behind Grothendieck universes, the size convention for large categories; in the other direction, Lawvere and Myles Tierney's topos theory recasts Cohen's forcing as passing to sheaves on the forcing poset.

## Connections across layers

- **Below:** It generalises [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [homomorphisms](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md), [tensor products](../../04-linear-algebra/04-multilinear-algebra/tensor-products.md) and the [homology](../../07-topology/02-algebraic-topology/homology.md) of layer 07, and it is the working language of [schemes](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/schemes.md) in layer 12.
- **Above:** The [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) weighs categories and univalent type theory as alternative foundations, and [computer-checked proof](../../15-mathematics-in-context/computers-and-proof.md) runs on dependent type theory.
- **Sideways:** In the computer science tree, [functional programming](../../../cs-first-principles/06-programming-languages/01-paradigms/functional.md) uses functors and monads directly, and [proof assistants](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) implement the type theories of the last leaf.

## Cross-cutting threads

- [Structure and morphism](../../CROSS-CUTTING.md#structure-and-morphism): the defining idea of the area, objects known by their arrows.
- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): one definition of product or quotient serves every field.
- [Duality](../../CROSS-CUTTING.md#duality): reversing arrows exchanges products and coproducts, limits and colimits, Tor and Ext.
- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): equivalence of categories and univalence refine what "the same" means.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): functors carry problems from topology to algebra, and Curry–Howard carries proofs to programs.
- [Invariants](../../CROSS-CUTTING.md#invariants): a functor sends isomorphic objects to isomorphic objects, which is why homology and π₁ are invariants.
