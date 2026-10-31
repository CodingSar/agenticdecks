# Universal Properties and Adjunctions

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Category theory](README.md)
> **Builds on:** [Natural transformations and the Yoneda lemma](natural-transformations-and-the-yoneda-lemma.md), [Equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [Tensor products](../../04-linear-algebra/04-multilinear-algebra/tensor-products.md), [Free groups and presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md), [Subspaces, products and quotients](../../07-topology/01-point-set-topology/subspaces-products-and-quotients.md)
> **Enables:** [Homological algebra](homological-algebra.md), [Higher categories and homotopy type theory](higher-categories-and-homotopy-type-theory.md), [Functional programming](../../../cs-first-principles/06-programming-languages/01-paradigms/functional.md)

## Essence

Products, quotients, free groups and tensor products were each built by hand in earlier layers, from pairs, equivalence classes, words and formal sums. Each is better defined by what it does: it is the object through which every map of a certain kind factors uniquely. Such a universal property fixes the object up to unique isomorphism, says what the construction is for, and works in any category. An adjunction packages a whole family of universal properties into a pair of functors, and it is the most common way that two kinds of structure are related.

## Core tenets

1. **A universal property fixes an object up to unique isomorphism.** A product of A and B is an object P with arrows p: P → A and q: P → B such that every pair f: X → A, g: X → B factors as f = p∘h, g = q∘h for exactly one h: X → P. If P′ is another, the factorisations give arrows P → P′ → P whose composite must be the identity, by uniqueness. In Yoneda's terms, P represents the functor X ↦ Hom(X, A) × Hom(X, B).

2. **One definition gives the right product in each category.** It yields the Cartesian product of sets, the direct product of groups, and the product topology, not the box topology: under the box topology the diagonal map ℝ → ℝ^ℕ is not continuous, since the preimage of the open box ∏(−1/n, 1/n) is {0}. Reversing arrows gives coproducts: disjoint union, free product of groups, direct sum of modules. In an ordered set products are greatest lower bounds and coproducts least upper bounds.

3. **Quotients are maps out of which certain maps factor.** The quotient G → G/N is universal among homomorphisms killing N, which is the first isomorphism theorem; G → G/[G, G] is universal among homomorphisms to abelian groups; the quotient topology is universal among continuous maps constant on the classes. Each is a coequaliser, the dual of the solution set of an equation.

4. **Free objects and tensor products are universal too.** The free group F(S) has a map S → F(S) such that every function from S to a group extends uniquely to a homomorphism. The polynomial ring ℤ[x] is free on one generator among commutative rings, the extension being evaluation at the image of x. The tensor product V ⊗ W is universal among bilinear maps out of V × W, which is why its elements are not just pairs.

5. **An adjunction is a natural bijection of arrows.** Functors F: C → D and G: D → C are adjoint, F ⊣ G, if Hom_D(F(X), Y) ≅ Hom_C(X, G(Y)) naturally in X and Y. Free ⊣ forgetful is the pattern above. Currying is − × A ⊣ (−)^A in Set: maps X × A → Y are maps X → Y^A. Even floor is an adjoint: n ≤ ⌊x⌋ if and only if n ≤ x for integers n, so ⌊−⌋ is right adjoint to ℤ → ℝ, while ⌈−⌉ is left adjoint. Stone–Čech compactification is left adjoint to the inclusion of compact Hausdorff spaces into spaces.

6. **Left adjoints preserve colimits, right adjoints preserve limits.** Colimits are universal cocones over a diagram; coproducts, cokernels and pushouts are examples. Since Hom(F(colim Xᵢ), Y) ≅ Hom(colim Xᵢ, G(Y)) ≅ lim Hom(Xᵢ, G(Y)), F preserves colimits; so F(S ⊔ T) ≅ F(S) ∗ F(T) for free groups. For modules − ⊗ M is left adjoint to Hom(M, −), so tensoring is right exact but not exact; measuring the failure gives Tor.

7. **Limits and colimits organise the earlier constructions.** The p-adic integers ℤ_p are the limit of the reduction maps … → ℤ/p³ → ℤ/p² → ℤ/p, so a p-adic integer is a compatible sequence of residues. The Seifert–van Kampen theorem says that π₁ sends a union of two path-connected open sets with path-connected intersection to a pushout of groups: π₁ preserves this particular colimit, which is how the fundamental group of a space glued from pieces is computed.

## Key concepts

| Term | Meaning |
|---|---|
| Universal property | Every arrow of a given kind factors uniquely through a fixed one |
| Product, coproduct | Universal pair of arrows out of, into, a single object |
| Equaliser, coequaliser | Universal solution of f∘h = g∘h, of h∘f = h∘g |
| Limit, colimit | Universal cone over, under, a diagram |
| Free object | The value of a left adjoint to a forgetful functor |
| Adjunction F ⊣ G | Hom(F(X), Y) ≅ Hom(X, G(Y)), naturally in X and Y |
| Unit, counit | The arrows X → G(F(X)) and F(G(Y)) → Y given by identities |
| Monad | The composite G∘F with the structure an adjunction gives it |

## How it fits

- **Below:** It recasts [quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [free groups](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md), [tensor products](../../04-linear-algebra/04-multilinear-algebra/tensor-products.md) and [product topologies](../../07-topology/01-point-set-topology/subspaces-products-and-quotients.md) as instances of one idea, proved unique by [Yoneda](natural-transformations-and-the-yoneda-lemma.md).
- **Above:** Currying and monads are working tools of [functional programming](../../../cs-first-principles/06-programming-languages/01-paradigms/functional.md).
- **Siblings:** [Homological algebra](homological-algebra.md) studies how far tensor and Hom fail to be exact, and [higher categories](higher-categories-and-homotopy-type-theory.md) weaken uniqueness to a contractible space of choices.

## Common misconceptions

- **"Every pair of objects has a product."**: Among fields there is no product of 𝔽₂ and 𝔽₃, since a field with homomorphisms to both would have characteristic 2 and 3.
- **"A universal property is a construction."**: It characterises an object without proving that one exists; existence needs a construction or an adjoint functor theorem.
- **"Adjoint functors are inverse to each other."**: Free and forgetful are adjoint, but forgetting the group structure of F(S) gives a set much larger than S.

## Go deeper

- Saunders Mac Lane, *Categories for the Working Mathematician* (1971; 2nd edition 1998): the standard account of limits and adjoints.
- Daniel Kan, "Adjoint Functors", *Transactions of the American Mathematical Society* (1958): the paper that introduced adjunctions.
- Emily Riehl, *Category Theory in Context* (2016): limits, colimits and adjunctions, with examples from across mathematics.
