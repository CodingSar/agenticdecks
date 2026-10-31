# Categories and Functors

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Category theory](README.md)
> **Builds on:** [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [Linear maps and matrices](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [Homomorphisms and quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), [Topological spaces and continuous maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md), [Homotopy and the fundamental group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md)
> **Enables:** [Natural transformations and the Yoneda lemma](natural-transformations-and-the-yoneda-lemma.md), [Universal properties and adjunctions](universal-properties-and-adjunctions.md), [Homological algebra](homological-algebra.md), [Higher categories and homotopy type theory](higher-categories-and-homotopy-type-theory.md), [Functional programming](../../../cs-first-principles/06-programming-languages/01-paradigms/functional.md)

## Essence

Groups with homomorphisms, vector spaces with linear maps and spaces with continuous maps share one pattern: objects, structure-preserving maps and composition. A category is that pattern made into a definition, and a functor is a map between categories that preserves it. The change of viewpoint is to describe an object by the arrows into and out of it rather than by its elements, so that a definition phrased in arrows (isomorphism, product, kernel) works in every category at once. Samuel Eilenberg and Saunders Mac Lane introduced the language in 1945 to make the "natural" isomorphisms of algebraic topology precise.

## Core tenets

1. **A category needs only arrows that compose associatively and have identities.** A category has objects, a collection Hom(A, B) of arrows f: A → B for each pair, a composite g∘f: A → C for f: A → B and g: B → C, and an identity id_A on each A, subject only to h∘(g∘f) = (h∘g)∘f and f∘id_A = f = id_B∘f. Arrows need not be functions: in the category Mat the objects are 0, 1, 2, …, an arrow m → n is an n × m real matrix, and composition is matrix multiplication.

2. **Isomorphism is defined by arrows, so each category decides what "the same" means.** An arrow f: A → B is an isomorphism if some g: B → A has g∘f = id_A and f∘g = id_B. In Set, the category of sets and functions, this is a bijection; in Top, the category of spaces and continuous maps, it is a homeomorphism. The continuous bijection t ↦ (cos t, sin t) from [0, 2π) to the circle is not one, because its inverse tears the circle at (1, 0).

3. **A single group or ordered set is itself a category.** A group G gives a category BG with one object and one arrow for each element, composed by multiplication; an ordered set gives a category with one arrow x → y exactly when x ≤ y. A functor BG → BH is a homomorphism, a functor BG → Set is an action of G, and a functor from BG to vector spaces is a linear representation.

4. **Functors preserve isomorphisms, which is the logic of every invariant.** A functor F sends each f: A → B to F(f): F(A) → F(B), with F(g∘f) = F(g)∘F(f) and F(id_A) = id, so if g inverts f then F(g) inverts F(f), and F(A) ≇ F(B) proves A ≇ B. A retraction r of the disc D² onto its boundary S¹ would make the identity of π₁(S¹) = ℤ factor through π₁(D²) = 0, which is impossible; so none exists, and Brouwer's fixed-point theorem for the disc follows.

5. **Reversing every arrow gives the opposite category, so every theorem has a dual.** The category Cᵒᵖ has an arrow B → A for each arrow A → B of C, and a contravariant functor is a functor out of Cᵒᵖ: the dual space V ↦ V* sends f to precomposition with f, and (g∘f)* = f*∘g*. A proof from the axioms survives reversing all arrows, so an initial object (exactly one arrow to every object) dualises to a terminal one (exactly one arrow from every object): ∅ and a point in Set.

6. **Monomorphisms and epimorphisms are arrow-only versions of injective and surjective, and can differ from them.** An arrow f is a monomorphism if f∘g = f∘h forces g = h, and an epimorphism if g∘f = h∘f forces g = h; in Set these are the injections and surjections. Among rings, the inclusion ℤ → ℚ is an epimorphism, since a homomorphism out of ℚ must send 1/n to the inverse of the image of n. It is mono and epi yet not invertible.

7. **Equivalence, not isomorphism, is the right sameness for categories.** A functor is an equivalence if it is full and faithful (bijective on each Hom(A, B)) and every object of the target is isomorphic to an object in its image. The functor from Mat sending n to ℝⁿ and each matrix to its linear map is one, since every finite-dimensional real vector space is isomorphic to some ℝⁿ, though the categories are not isomorphic: one has countably many objects, the other a proper class. This is the precise sense in which linear algebra is matrix algebra.

8. **Large categories force a choice about size.** Set has a proper class of objects, so the category of all categories needs care. One requires each Hom(A, B) to be a set (local smallness) or works inside a Grothendieck universe, a set closed under the usual set-forming operations. A universe containing ℕ exists if and only if an [inaccessible cardinal](../03-model-theory-and-independence/large-cardinals.md) does, which Zermelo–Fraenkel set theory with the axiom of choice (ZFC) cannot prove if it is consistent.

## Key concepts

| Term | Meaning |
|---|---|
| Category | Objects and arrows, with associative composition and identities |
| Isomorphism | An arrow with a two-sided inverse |
| Functor | A map of categories preserving composition and identities |
| Contravariant functor | A functor out of Cᵒᵖ: it reverses arrows |
| Monomorphism, epimorphism | An arrow that cancels on the left, on the right |
| Full, faithful | Surjective, injective on each Hom(A, B) |
| Equivalence | A full and faithful functor reaching every object up to isomorphism |
| Locally small | Each Hom(A, B) is a set |

## How it fits

- **Below:** It keeps only composition from [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md) and treats [group homomorphisms](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), [linear maps](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md) and [continuous maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) as one notion; the [fundamental group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) is its first serious functor.
- **Above:** [Functional programming](../../../cs-first-principles/06-programming-languages/01-paradigms/functional.md) treats types and programs as a category, and the [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) asks whether categories could replace sets as a foundation.
- **Siblings:** [Natural transformations](natural-transformations-and-the-yoneda-lemma.md) compare functors, [universal properties](universal-properties-and-adjunctions.md) define constructions by arrows, and [homological algebra](homological-algebra.md) and [higher categories](higher-categories-and-homotopy-type-theory.md) extend the language.

## Common misconceptions

- **"Category theory is a language with no theorems of its own."**: The retraction argument is already a proof, and the Yoneda lemma, the adjoint functor theorems and derived functors have real content.
- **"Arrows are functions between sets of elements."**: In an ordered set or in Mat they are not, and some categories admit no faithful functor to Set at all; Peter Freyd proved this for the homotopy category of pointed spaces.

## Go deeper

- Saunders Mac Lane, *Categories for the Working Mathematician* (1971; 2nd edition 1998): the classic reference, by one of the founders.
- Emily Riehl, *Category Theory in Context* (2016): a modern course whose examples come from across mathematics.
- Tom Leinster, *Basic Category Theory* (2014): the shortest careful introduction.
