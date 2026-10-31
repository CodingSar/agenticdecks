# Ordinal Numbers and Transfinite Induction

> **Layer:** [01 Sets and Foundations](../README.md) › [Infinity and Cardinality](README.md)
> **Builds on:** [Relations and orders](../01-sets-relations-and-functions/relations-and-orders.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [Countable sets](countable-sets.md), [Cardinal numbers](cardinal-numbers.md)
> **Enables:** [Zermelo–Fraenkel set theory](../03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md), [The axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md), [Natural numbers and the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [Proof theory and reverse mathematics](../../13-structure-and-metamathematics/02-computability-and-incompleteness/proof-theory-and-reverse-mathematics.md)

## Essence

Cardinals measure how many; ordinals measure how long. An ordinal is the shape of a well-order, and the ordinals continue counting past the natural numbers: 0, 1, 2, …, ω, ω + 1, ω + 2, …, ω · 2, …, ω², …, ω^ω, … Each ordinal is the set of all smaller ones, so every well-ordered set is isomorphic to exactly one of them. Because every non-empty set of ordinals has a least element, induction and recursion extend along them past every finite stage, with a new case at limit stages. This is the engine for building the hierarchy of sets, for iterating constructions until they stabilise, and for measuring the strength of theories.

## Core tenets

1. **Well-orders are rigid.** If f: W → W is strictly increasing on a well-order, then f(x) ≥ x for every x: otherwise take the least x with f(x) < x, and then f(f(x)) < f(x) contradicts the minimality of x. Hence no well-order is isomorphic to a proper initial segment of itself, an isomorphism between two well-orders is unique, and of any two well-orders one is isomorphic to an initial segment of the other.

2. **von Neumann ordinals: each ordinal is the set of its predecessors.** An ordinal is a transitive set (every element is a subset) that is well-ordered by ∈. Then 0 = ∅, α + 1 = α ∪ {α}, and a limit ordinal such as ω = {0, 1, 2, …} is the union of the ordinals below it. α < β means α ∈ β. Every well-order is isomorphic to exactly one ordinal; the proof needs the replacement axiom of [Zermelo–Fraenkel set theory](../03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md). The ordinals form no set: such a set would itself be an ordinal, hence a member of itself (Burali-Forti, 1897).

3. **Transfinite induction has three cases.** To prove P(α) for every ordinal α, prove P(0), prove P(α) ⇒ P(α + 1), and prove that P(β) for all β < λ implies P(λ) at each limit λ. It works for the same reason as ordinary induction: a least counterexample would have to be 0, a successor or a limit, and each case is excluded. Dropping the limit case fails at once, since nothing then reaches ω.

4. **Transfinite recursion defines a function on all ordinals.** If G says how to produce the next value from all earlier ones, there is a unique F with F(α) = G(F restricted to α). It builds the cumulative hierarchy of sets V_α, Cantor's process of repeatedly deleting isolated points from a closed set of reals until it stabilises, and the Borel sets, which close up after ω₁ steps of taking countable unions and complements (using countable choice).

5. **Ordinal arithmetic is not commutative.** α + β is α followed by a copy of β, and α · β is β copies of α laid end to end. So 1 + ω = ω, since one point in front of ω leaves the shape unchanged, but ω + 1 ≠ ω, since ω + 1 has a largest element. Likewise 2 · ω = ω while ω · 2 = ω + ω. Addition and multiplication are associative and continuous in the right argument. Every ordinal α > 0 has a unique Cantor normal form ω^β₁ · c₁ + … + ω^βₖ · cₖ with β₁ > … > βₖ and positive natural numbers cᵢ.

6. **Countable ordinals go very far, and ω₁ is the first that is not.** ω², ω^ω and ε₀ = ω^(ω^(ω^…)), the least ε with ω^ε = ε, are all countable: each is a well-order on ℕ. The set of all countable ordinals is itself an ordinal, ω₁, the first uncountable one, and its existence needs no choice. Initial ordinals, those not equinumerous with any smaller ordinal, serve as [cardinals](cardinal-numbers.md): ω = ℵ₀ and ω₁ = ℵ₁, while ω + 1 is countable and is not a cardinal.

7. **Goodstein's theorem needs ε₀.** Write n in hereditary base 2, replace every 2 by 3, subtract 1, rewrite in hereditary base 3, replace every 3 by 4, subtract 1, and so on. Starting from 3 the sequence runs 3, 3, 3, 2, 1, 0; starting from 4 it grows for an astronomically long time. Goodstein (1944) proved that every such sequence reaches 0, by replacing each base with ω to get a strictly decreasing sequence of ordinals below ε₀. Kirby and Paris (1982) showed that the theorem cannot be proved in Peano arithmetic (PA), the first-order axioms for ℕ; its proof uses ε₀, the ordinal Gentzen (1936) needed to prove PA consistent. See [proof theory and reverse mathematics](../../13-structure-and-metamathematics/02-computability-and-incompleteness/proof-theory-and-reverse-mathematics.md).

## Key concepts

| Term | Meaning |
|---|---|
| Ordinal | a transitive set well-ordered by ∈; the shape of a well-order |
| Successor ordinal | α + 1 = α ∪ {α} |
| Limit ordinal | a non-zero ordinal that is not a successor, such as ω |
| ω | the set of natural numbers, the least infinite ordinal |
| Transfinite induction | induction with zero, successor and limit cases |
| Transfinite recursion | definition of F(α) from all earlier values |
| Cantor normal form | a finite sum of terms ω^β · c with decreasing exponents |
| ε₀ | the least ordinal ε with ω^ε = ε |
| ω₁ | the set of all countable ordinals, the first uncountable ordinal |

## How it fits

- **Below:** an ordinal is a well-order from [relations and orders](../01-sets-relations-and-functions/relations-and-orders.md); transfinite induction generalises [mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md); [countable sets](countable-sets.md) and [cardinal numbers](cardinal-numbers.md) supply the sizes that initial ordinals represent.
- **Above:** the cumulative hierarchy of [Zermelo–Fraenkel set theory](../03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md) is indexed by ordinals; the well-ordering theorem in [the axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md) is a transfinite recursion; ω is the set-theoretic [natural numbers](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md); [proof theory](../../13-structure-and-metamathematics/02-computability-and-incompleteness/proof-theory-and-reverse-mathematics.md) measures theories by ordinals. The thread is [induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion).
- **Siblings:** [cardinal numbers](cardinal-numbers.md) forget the order that ordinals keep; the Burali-Forti paradox is a cousin of [Cantor's diagonal argument](cantors-diagonal-argument.md).

## Common misconceptions

- **"ω + 1 and 1 + ω are the same"**: 1 + ω = ω, but ω + 1 has a last element and ω does not.
- **"Ordinals and cardinals are the same numbers"**: ω, ω + 1 and ω · 2 are different ordinals of the same cardinality ℵ₀.
- **"Transfinite induction needs the axiom of choice"**: it needs only a well-order. Choice is used to well-order an arbitrary set in the first place.

## Go deeper

- John von Neumann, "Zur Einführung der transfiniten Zahlen" (1923): the definition of ordinals as sets of predecessors.
- Karel Hrbacek and Thomas Jech, *Introduction to Set Theory* (3rd edition, 1999): ordinals, their arithmetic and transfinite recursion with full proofs.
- Thomas Jech, *Set Theory* (3rd millennium edition, 2003): ordinals throughout set theory.
