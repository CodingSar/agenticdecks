# Models and the Löwenheim–Skolem Theorems

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Model theory and independence](README.md)
> **Builds on:** [Soundness, completeness and compactness](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md), [Cardinal numbers](../../01-sets-and-foundations/02-infinity-and-cardinality/cardinal-numbers.md), [Zermelo–Fraenkel set theory](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md), [Natural numbers and the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md)
> **Enables:** [Quantifier elimination and decidable theories](quantifier-elimination-and-decidable-theories.md), [Forcing and independence](forcing-and-independence.md), [Large cardinals](large-cardinals.md), [Philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md)

## Essence

Layer 00 proved that first-order logic is complete and compact. Model theory studies the structures that satisfy a theory, and its first lesson is that first-order theories cannot control the size of their models. The Löwenheim–Skolem theorems say that a theory with an infinite model has models of every infinite size at least that of its language, so no first-order axioms pin down ℕ, ℝ or the universe of sets up to isomorphism. This produces Skolem's paradox, non-standard models of arithmetic and infinitesimals made rigorous, and it turns the question "which theories do determine their models?" into a classification problem.

## Core tenets

1. **Downward: every structure has a small elementary substructure.** If A is a structure for a language L and X ⊆ A, there is an elementary substructure N with X ⊆ N ⊆ A, satisfying exactly the same sentences with parameters from N, and |N| ≤ |X| + |L| + ℵ₀. Choose for each formula ∃y φ(x, y) a Skolem function picking a witness y, and close X under these functions; the Tarski–Vaught test confirms that N is elementary. The choice of witnesses uses the axiom of choice.

2. **Skolem's paradox: set theory has countable models.** If Zermelo–Fraenkel set theory with choice (ZFC) is consistent, it has a model, hence a countable one, even though ZFC proves that uncountable sets exist. There is no contradiction: a set that the model calls uncountable has countably many elements from outside, but the bijection with ℕ that would witness this is not a member of the model. "Uncountable" is relative to the model.

3. **Upward: models of every larger size exist, so categoricity fails.** Add κ new constants and the sentences cᵢ ≠ cⱼ to the theory of an infinite structure A; every finite subset is satisfiable in A, so by compactness the whole set has a model of size at least κ, and the downward theorem trims it to size exactly κ. Hence no first-order theory with an infinite model is categorical, having only one model up to isomorphism. Second-order Peano arithmetic is categorical, but second-order logic has no complete proof system, and Per Lindström (1969) showed that first-order logic is the strongest logic with both compactness and the downward theorem.

4. **Arithmetic has non-standard models.** Adding a constant c with axioms c > 0, c > 1, c > 2, … gives, by compactness, a model of true arithmetic with an element larger than every standard number. Every countable non-standard model of Peano arithmetic (PA) has order type ω + (ω* + ω)·η: the standard numbers followed by a dense, endless sequence of copies of the integers. Stanley Tennenbaum (1959) proved that in no countable non-standard model of PA are addition and multiplication computable.

5. **Non-standard analysis makes infinitesimals rigorous.** Take sequences of reals and identify two when they agree on a set in a non-principal ultrafilter U on ℕ. By Łoś's theorem a first-order statement holds in this ultrapower if and only if it holds coordinatewise on a set in U, so the result is an ordered field with the same first-order properties as ℝ, the transfer principle, but containing the infinitesimal represented by (1, 1/2, 1/3, …). Abraham Robinson founded the subject in 1961 and set it out in a book in 1966.

6. **Some theories are categorical in some sizes, and Morley classified when.** Dense linear orders without endpoints are ℵ₀-categorical, by Cantor's back-and-forth argument, but not categorical in size continuum: ℝ and ℝ ∖ {0} differ, since only the first is complete. Algebraically closed fields of characteristic 0 are categorical in every uncountable size, because transcendence degree determines them, but not in size ℵ₀. Michael Morley (1965) proved that a countable theory categorical in one uncountable cardinality is categorical in all of them. By the Łoś–Vaught test a theory with no finite models that is categorical in some infinite size is complete.

7. **Independence is proved by building models.** To show T does not prove φ, exhibit a model of T + ¬φ. Hyperbolic models showed that the parallel postulate is independent of the other axioms of [plane geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md); [forcing](forcing-and-independence.md) applies the same principle to set theory.

## Key concepts

| Term | Meaning |
|---|---|
| Structure, model | A set with interpretations of the symbols; a model of T satisfies every sentence of T |
| Elementary substructure | A substructure satisfying the same sentences with its own parameters |
| Skolem function | A function choosing a witness for each existential formula |
| Categorical | Having exactly one model up to isomorphism, possibly in a given size |
| Non-standard model | A model of arithmetic not isomorphic to ℕ |
| Ultrapower | A product of copies of a structure modulo an ultrafilter |
| Łoś's theorem | A sentence holds in an ultrapower if and only if it holds on a large set of factors |

## How it fits

- **Below:** It builds on [compactness and completeness](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md) and [cardinal arithmetic](../../01-sets-and-foundations/02-infinity-and-cardinality/cardinal-numbers.md), and shows that [Peano's axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [the axioms for ℝ](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) and [ZFC](../../01-sets-and-foundations/03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md) characterise their intended structures only in second-order form.
- **Above:** The [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) debates what Skolem's paradox means for the determinacy of mathematical concepts.
- **Siblings:** [Quantifier elimination](quantifier-elimination-and-decidable-theories.md) analyses particular theories completely, while [forcing](forcing-and-independence.md) and [large cardinals](large-cardinals.md) build models of set theory.

## Common misconceptions

- **"Skolem's paradox shows set theory is inconsistent."**: It shows only that countability, a statement about which bijections exist, depends on the model in which it is evaluated.
- **"Second-order axioms solve the problem."**: They make ℕ and ℝ categorical, but at the cost of completeness and compactness: the consequences of second-order axioms are not captured by any proof system.

## Go deeper

- Wilfrid Hodges, *A Shorter Model Theory* (1997): the standard introduction.
- David Marker, *Model Theory: An Introduction* (2002): from Löwenheim–Skolem to Morley's theorem.
- Abraham Robinson, *Non-standard Analysis* (1966): the founding book.
