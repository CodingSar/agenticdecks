# Natural Transformations and the Yoneda Lemma

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Category theory](README.md)
> **Builds on:** [Categories and functors](categories-and-functors.md), [Dual spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md), [Group actions](../../05-abstract-algebra/01-groups/group-actions.md), [Representations of finite groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md)
> **Enables:** [Universal properties and adjunctions](universal-properties-and-adjunctions.md), [Higher categories and homotopy type theory](higher-categories-and-homotopy-type-theory.md), [Polymorphism and type inference](../../../cs-first-principles/06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md)

## Essence

A natural transformation is a map between two functors that is compatible with every arrow. It makes precise the old intuition that some isomorphisms are canonical while others depend on a choice, and with natural transformations as arrows, functors themselves form categories. The Yoneda lemma says that a natural transformation out of the functor Hom(−, A) is fixed by a single element, and its corollary is that an object is determined up to isomorphism by the maps into it from all other objects. Every construction defined by a universal property is, through this lemma, a statement that some functor is representable.

## Core tenets

1. **A natural transformation is a family of arrows that commutes with every arrow.** For functors F, G: C → D, a natural transformation α: F ⇒ G assigns to each object X an arrow α_X: F(X) → G(X) such that the square below commutes for every f: X → Y. It is a natural isomorphism if every α_X is an isomorphism.

   ```
   F(X) ──α_X──→ G(X)
    │              │
   F(f)          G(f)          G(f)∘α_X = α_Y∘F(f)
    ↓              ↓
   F(Y) ──α_Y──→ G(Y)
   ```

2. **The isomorphism V ≅ V\*\* is natural and V ≅ V\* is not.** The evaluation map V → V\*\*, v ↦ (φ ↦ φ(v)), commutes with every linear map and is an isomorphism for finite-dimensional V, with no basis chosen. No family α_V: V → V\* is natural, even for invertible maps alone: naturality for f: V → W requires (f⁻¹)\*∘α_V = α_W∘f, and over ℝ the choice f = 2·id gives ½·α_V = 2·α_V, so α_V = 0. Every isomorphism V ≅ V\* uses a basis or an inner product.

3. **Functors and natural transformations form a category.** The functors C → D, with natural transformations composed componentwise, form a functor category [C, D]. For a group G, [BG, Vect] is the category of linear representations of G, and its arrows are exactly the intertwining maps, so Schur's lemma is a statement about this category. An equivalence of categories is then a pair of functors whose two composites are naturally isomorphic to the identities.

4. **Many familiar functors are representable.** A functor F: Cᵒᵖ → Set is representable if F ≅ Hom(−, A) for some object A. The power set, made contravariant by taking preimages, is represented by {0, 1}, since a subset of X is a map X → {0, 1}. Covariantly, the underlying set of a group is Hom(ℤ, −), because a homomorphism out of ℤ is fixed by the image of 1, and the solutions of x² + y² = 1 in a commutative ring R are the homomorphisms ℤ[x, y]/(x² + y² − 1) → R.

5. **The Yoneda lemma: a natural transformation out of a representable functor is one element.** For a locally small category C, a functor F: Cᵒᵖ → Set and an object A, there is a bijection, natural in A and F:

   ```
   Nat(Hom(−, A), F)  ≅  F(A)
          α           ↦  α_A(id_A)
     (f ↦ F(f)(u))    ↤  u
   ```

   For f: X → A, naturality applied to f gives α_X(f) = α_X(id_A∘f) = F(f)(α_A(id_A)), so α is fixed by u = α_A(id_A), and the formula f ↦ F(f)(u) is natural for every u.

6. **An object is determined by the maps into it.** Taking F = Hom(−, B) gives Nat(Hom(−, A), Hom(−, B)) ≅ Hom(A, B): the Yoneda embedding A ↦ Hom(−, A), from C into the presheaf category [Cᵒᵖ, Set], is full and faithful. Hence Hom(−, A) ≅ Hom(−, B) if and only if A ≅ B. Grothendieck's functor of points rests on this: a [scheme](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/schemes.md) is determined by its sets of points over all commutative rings.

7. **Cayley's theorem is the Yoneda lemma for a one-object category.** In BG the functor Hom(−, ∗) is the set G with G acting by right multiplication. The Yoneda embedding says that the maps of this set commuting with every right multiplication are exactly the left multiplications x ↦ g·x, one for each g, so G embeds in the group of permutations of its own elements. The general lemma is the same argument with many objects.

## Key concepts

| Term | Meaning |
|---|---|
| Natural transformation | A family α_X: F(X) → G(X) with G(f)∘α_X = α_Y∘F(f) for every f |
| Natural isomorphism | A natural transformation whose components are all isomorphisms |
| Functor category [C, D] | Functors C → D as objects, natural transformations as arrows |
| Presheaf | A functor Cᵒᵖ → Set |
| Representable functor | A functor naturally isomorphic to Hom(−, A) or Hom(A, −) |
| Universal element | The element α_A(id_A) of F(A) that determines α |
| Yoneda embedding | A ↦ Hom(−, A), a full and faithful functor C → [Cᵒᵖ, Set] |

## How it fits

- **Below:** It makes precise why the double-dual map of [dual spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md) is canonical, and its one-object case recovers [group actions](../../05-abstract-algebra/01-groups/group-actions.md) and [representations](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md) as functors.
- **Above:** A polymorphic program such as list reversal is a natural transformation from the list functor to itself, a fact used in [type inference and polymorphism](../../../cs-first-principles/06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md); the [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) reads Yoneda as a structuralist slogan.
- **Siblings:** [Categories and functors](categories-and-functors.md) supplies the objects, [universal properties](universal-properties-and-adjunctions.md) are representability statements, and [higher categories](higher-categories-and-homotopy-type-theory.md) relax the naturality equation to a homotopy.

## Common misconceptions

- **"Isomorphic at every object means naturally isomorphic."**: Every finite-dimensional V is isomorphic to V\*, yet no natural isomorphism exists; the components must also commute with the arrows.
- **"Natural is an informal word for canonical."**: It is a definition, and giving it was the stated purpose of the 1945 paper that introduced categories.
- **"The Yoneda lemma is a deep theorem."**: Its proof is one line; its force lies in how often a problem becomes easier after replacing an object by the functor it represents.

## Go deeper

- Samuel Eilenberg and Saunders Mac Lane, "General Theory of Natural Equivalences", *Transactions of the American Mathematical Society* (1945): the founding paper.
- Emily Riehl, *Category Theory in Context* (2016): representability and the Yoneda lemma treated at length.
- Tom Leinster, *Basic Category Theory* (2014): a careful chapter on representables and Yoneda.
