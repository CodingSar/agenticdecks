# Higher Categories and Homotopy Type Theory

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Category theory](README.md)
> **Builds on:** [Homotopy and the fundamental group](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md), [Constructive and intuitionistic logic](../../00-logic-and-proof/03-the-axiomatic-method/constructive-and-intuitionistic-logic.md), [Type theory and alternative foundations](../../01-sets-and-foundations/03-axiomatic-set-theory/type-theory-and-alternative-foundations.md), [Universal properties and adjunctions](universal-properties-and-adjunctions.md), [Homological algebra](homological-algebra.md)
> **Enables:** [Proof assistants and dependent types](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md), [Type systems](../../../cs-first-principles/06-programming-languages/02-semantics-and-types/type-systems.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md)

## Essence

In topology two paths are rarely equal, only homotopic, and two homotopies are themselves related by higher homotopies. A higher category keeps all of this: arrows between objects, 2-arrows between arrows, and so on, with composition associative only up to a coherent choice of higher arrows. ∞-categories now carry much of algebraic topology and derived algebraic geometry. Homotopy type theory runs the same idea through logic: under the Curry–Howard correspondence propositions are types and proofs are programs, and if an equality proof is read as a path, types behave like spaces. Vladimir Voevodsky's univalence axiom then makes equivalent structures equal.

## Core tenets

1. **Strict equality loses information that homotopy keeps.** Gluing two discs along their boundary circle gives the sphere S². Each disc is homotopy equivalent to a point, yet gluing two points along a circle in the ordinary sense gives a point, not something equivalent to S²: the ordinary pushout does not respect homotopy equivalence. The repair, the homotopy pushout, remembers the homotopies used in the gluing, and an ordinary category, whose arrows are only equal or not, cannot express it.

2. **∞-groupoids are spaces.** In an ∞-groupoid every arrow at every level is invertible up to higher arrows. Alexander Grothendieck's *Pursuing Stacks* (1983) proposed the homotopy hypothesis: ∞-groupoids and homotopy types are the same thing. When ∞-groupoids are modelled by Kan complexes, this is the classical equivalence of homotopy theories between Kan complexes and spaces, due to Daniel Quillen (1967).

3. **Quasi-categories make ∞-categories workable.** A quasi-category is a simplicial set in which composable arrows have composites that exist and are unique up to a contractible space of choices. Introduced by Boardman and Vogt (1973) and developed by André Joyal and by Jacob Lurie, whose *Higher Topos Theory* (2009) rebuilt topos theory in this setting, they allow limits, adjunctions and Yoneda in a homotopy-coherent form. Stable ∞-categories repair the derived categories of homological algebra, where cones of maps are not functorial.

4. **Propositions are types and proofs are programs.** Haskell Curry noticed in the 1930s that the axioms of implicational logic are the types of basic combinators; William Howard's notes of 1969, published in 1980, extended this to a full correspondence, and Joachim Lambek matched it with cartesian closed categories.

   | Logic | Type theory | Category |
   |---|---|---|
   | proposition A ⇒ B | function type A → B | exponential object |
   | A ∧ B | product type A × B | product |
   | proof | program (term) | arrow |
   | cut elimination | evaluation | composition |

   The correspondence is intuitionistic; classical logic needs control operators, as Timothy Griffin observed in 1990 for call-with-current-continuation.

5. **Identity proofs behave like paths.** In Martin-Löf type theory a proof of a = b is an element of an identity type, and path induction says that to prove something for all such proofs it suffices to prove it for reflexivity. Martin Hofmann and Thomas Streicher's groupoid model (1994) showed that two proofs of a = b need not be equal. In the 2000s Steve Awodey and Michael Warren, and independently Voevodsky, interpreted types as spaces and identity proofs as paths.

6. **Univalence identifies equivalent types.** The univalence axiom says that the canonical map (A = B) → (A ≃ B) is an equivalence, so isomorphic structures can be substituted in every context. It contradicts uniqueness of identity proofs: Bool ≃ Bool has two elements, the identity and negation, so Bool = Bool has two. It is consistent relative to ZFC, Zermelo–Fraenkel set theory with choice, plus inaccessible cardinals, through a model in simplicial sets, and cubical type theory, due to Cohen, Coquand, Huber and Mörtberg, gives it computational meaning.

7. **Higher inductive types build spaces synthetically.** The circle is the type generated by a point and a loop from it to itself. Daniel Licata and Michael Shulman proved in type theory (2013) that its loop space is equivalent to ℤ, so π₁(S¹) ≅ ℤ, and the proof was checked by computer. The book *Homotopy Type Theory: Univalent Foundations of Mathematics* (2013), written collaboratively during a special year at the Institute for Advanced Study, set out the programme; as of 2026 it remains a research programme alongside set-theoretic foundations.

## Key concepts

| Term | Meaning |
|---|---|
| ∞-groupoid | Arrows at all levels, each invertible up to higher arrows |
| Homotopy hypothesis | ∞-groupoids and homotopy types are equivalent |
| Quasi-category | A simplicial set modelling an ∞-category |
| Curry–Howard correspondence | Propositions as types, proofs as programs |
| Identity type | The type of proofs that a = b, read as paths |
| Univalence | Equivalent types are equal, in a way compatible with all constructions |
| Higher inductive type | A type generated by points and by paths between them |

## How it fits

- **Below:** It treats the [homotopies](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) of topology as basic, and develops the [type theories](../../01-sets-and-foundations/03-axiomatic-set-theory/type-theory-and-alternative-foundations.md) and [constructive logic](../../00-logic-and-proof/03-the-axiomatic-method/constructive-and-intuitionistic-logic.md) of earlier layers.
- **Above:** Dependent type theory runs [proof assistants](../../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) and [type systems](../../../cs-first-principles/06-programming-languages/02-semantics-and-types/type-systems.md); its role in [computer-checked mathematics](../../15-mathematics-in-context/computers-and-proof.md) is discussed in layer 15.
- **Siblings:** It weakens [universal properties](universal-properties-and-adjunctions.md) to contractible spaces of choices and gives [homological algebra](homological-algebra.md) stable ∞-categories; its consistency relies on the [large cardinals](../03-model-theory-and-independence/large-cardinals.md) of model theory.

## Common misconceptions

- **"Homotopy type theory is what proof assistants use."**: Lean's mathlib, the largest library, assumes uniqueness of identity proofs for propositions and is not univalent; univalent libraries are a smaller, separate effort.
- **"Univalence says isomorphic things are identical."**: It says that the type of identifications is equivalent to the type of equivalences, which is why Bool = Bool has two elements rather than one.

## Go deeper

- The Univalent Foundations Program, *Homotopy Type Theory: Univalent Foundations of Mathematics* (2013): the book, freely available.
- Jacob Lurie, *Higher Topos Theory* (2009): the foundational treatise on quasi-categories.
- Emily Riehl and Dominic Verity, *Elements of ∞-Category Theory* (2022): ∞-categories developed independently of a model.
- Morten Heine Sørensen and Paweł Urzyczyn, *Lectures on the Curry–Howard Isomorphism* (2006): the logic–computation correspondence in detail.
