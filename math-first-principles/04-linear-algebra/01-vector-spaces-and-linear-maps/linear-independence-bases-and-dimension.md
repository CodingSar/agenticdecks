# Linear Independence, Bases and Dimension

> **Layer:** [04 Linear Algebra](../README.md) › [Vector Spaces and Linear Maps](README.md)
> **Builds on:** [Fields and vector spaces](fields-and-vector-spaces.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [The axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md), [Counting principles and binomial coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md)
> **Enables:** [Linear maps and matrices](linear-maps-and-matrices.md), [Field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md), [Finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md), [Ruler and compass constructions](../../05-abstract-algebra/03-galois-theory/ruler-and-compass-constructions.md), [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md)

## Essence
A basis is a set of vectors from which every vector can be built in exactly one way. Choosing one turns abstract vectors into lists of numbers, their coordinates. The central theorem is that all bases of a space have the same size, so the dimension is a genuine invariant of the space, and two spaces over the same field are isomorphic exactly when their dimensions agree. Dimension is the first and coarsest classification in linear algebra, and it is complete: up to isomorphism, a finite-dimensional vector space is nothing but Fⁿ.

## Core tenets
1. **A basis gives unique coordinates.** Vectors v₁, …, vₙ are linearly independent if a₁v₁ + ⋯ + aₙvₙ = 0 forces every aᵢ = 0, and they span V if every vector is such a combination. A basis does both, and then each v has exactly one expression v = a₁v₁ + ⋯ + aₙvₙ, since two expressions would differ by a non-trivial relation. In ℝ², (1, 0) and (1, 1) form a basis; adding (0, 1) spoils independence through the relation (1, 1) − (1, 0) − (0, 1) = 0.

2. **The Steinitz exchange lemma: independent lists are never longer than spanning lists.** If u₁, …, uₘ are independent and w₁, …, wₙ span, then m ≤ n. Induct on i: after replacing i of the w's by u₁, …, uᵢ the list still spans, so uᵢ₊₁ is a combination of it; independence of the u's forces a non-zero coefficient on some remaining w, which can be swapped out for uᵢ₊₁. If m > n, the w's run out first, and some u would lie in the span of the others.

3. **Dimension is well defined.** Two bases are each independent and spanning, so the lemma applied both ways gives equal sizes. Hence Fᵐ and Fⁿ are isomorphic if and only if m = n, and a homogeneous system of m linear equations in n > m unknowns always has a non-zero solution, because n vectors in Fᵐ must be dependent.

4. **Every independent set extends to a basis and every spanning set shrinks to one.** Discard vectors lying in the span of the earlier ones, or adjoin vectors outside the current span, until the list is both independent and spanning. An isomorphism Fⁿ → V is then the same thing as an ordered basis: there is one for every choice, and none is preferred.

5. **Dimension counts like a size.** For subspaces U and W of a finite-dimensional space, dim(U + W) = dim U + dim W − dim(U ∩ W), proved by extending a basis of U ∩ W separately to bases of U and of W. Two distinct planes through the origin in ℝ³ meet in a line, since 2 + 2 − 3 = 1. Dimension counting of this kind drives later results such as [Sylvester's law](../03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md) and the [Eckart–Young theorem](../03-inner-product-spaces/singular-value-decomposition.md).

6. **Over a finite field, dimension counts elements.** A space of dimension n over ℤ/p has pⁿ elements, one for each coordinate list. Counting ordered bases (the first vector any non-zero one, each later one outside the span so far) gives the order of the general linear group GL(n, p) of invertible n × n matrices over ℤ/p:

   ```
   |GL(n, p)| = (pⁿ − 1)(pⁿ − p)(pⁿ − p²) ⋯ (pⁿ − pⁿ⁻¹)
   ```

   A finite field containing ℤ/p is a vector space over it, so its size is a prime power, and there is no field with 6 elements.

7. **Infinite-dimensional spaces have bases only by choice.** Zorn's lemma gives a maximal independent set, which must span, so every vector space has a basis; over Zermelo–Fraenkel set theory (ZF) this statement is in fact equivalent to [the axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) (Andreas Blass, 1984). A basis of ℝ over ℚ, a Hamel basis after Georg Hamel (1905), exists but cannot be written down. Analysts therefore replace finite combinations by convergent series, as with orthonormal bases in [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md).

## Key concepts
| Term | Meaning |
|---|---|
| Linear independence | Only the trivial combination gives 0 |
| Spanning set | Every vector is a linear combination of its members |
| Basis | Independent spanning set; gives unique coordinates |
| Coordinates | The coefficients of v in a fixed ordered basis |
| Dimension | The common size of all bases |
| Exchange lemma | Independent lists are no longer than spanning lists |
| Hamel basis | Basis in the purely algebraic sense, using finite combinations only |

## How it fits
- **Below:** [induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md) runs the exchange argument, [counting](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md) handles finite fields, and [choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) handles infinite dimension.
- **Above:** the degree of a [field extension](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md) is a dimension, which settles the classical [ruler and compass](../../05-abstract-algebra/03-galois-theory/ruler-and-compass-constructions.md) problems and the sizes of [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md).
- **Siblings:** [linear maps](linear-maps-and-matrices.md) are matrices once bases are chosen; [rank–nullity](linear-systems-and-rank-nullity.md) is a dimension count; a basis determines a [dual basis](dual-spaces.md).

## Common misconceptions
- **"Every space has a natural basis."**: Fⁿ does, but the plane x + y + z = 0 in ℝ³ or the solution space of a differential equation has none preferred; much of linear algebra is about statements that do not depend on the choice.
- **"Dimension obeys inclusion–exclusion for three subspaces."**: three distinct lines through the origin in ℝ² have pairwise and triple intersections 0, yet their sum has dimension 2, not 3.
- **"ℝ^∞ is like ℝⁿ with n large."**: the space of all real sequences has uncountable dimension; the sequences with finitely many non-zero terms are the countable-dimensional space.

## Go deeper
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): the exchange lemma and dimension done carefully.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (2nd edition, 1971): thorough, including infinite-dimensional remarks.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (2nd edition, 1958): bases, dimension and their invariance.
