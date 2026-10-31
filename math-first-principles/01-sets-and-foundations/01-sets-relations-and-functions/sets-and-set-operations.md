# Sets and Set Operations

> **Layer:** [01 Sets and Foundations](../README.md) › [Sets, Relations and Functions](README.md)
> **Builds on:** [Propositional logic](../../00-logic-and-proof/01-formal-logic/propositional-logic.md), [Predicate logic and quantifiers](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), [Direct proof, contraposition and contradiction](../../00-logic-and-proof/02-methods-of-proof/direct-proof-contraposition-and-contradiction.md)
> **Enables:** [Relations and orders](relations-and-orders.md), [Paradoxes and naive set theory](../03-axiomatic-set-theory/paradoxes-and-naive-set-theory.md), [Counting principles](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md), [Measure and σ-algebras](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md)

## Essence

A set is a collection treated as a single object, and it is determined entirely by its members: order, repetition and the way it was described carry no information. The one primitive is membership, x ∈ A, and every other notion in this layer (subset, union, ordered pair, relation, function) is defined from it. The operations on sets are the logical connectives in disguise: union is "or", intersection is "and", difference is "and not", and inclusion is "implies". So a claim about sets is proved by reducing it to a claim about an arbitrary element, and that is why sets can serve as the common language of mathematics. The one limit is that not every property defines a set, which is where axioms enter.

## Core tenets

1. **A set is determined by its elements (extensionality).** A = B means ∀x (x ∈ A ⇔ x ∈ B), so equality of sets is proved by double inclusion: show A ⊆ B and B ⊆ A, each by taking an arbitrary element. Hence {1, 2} = {2, 1} = {1, 1, 2}. It also makes the empty set ∅ unique: two sets with no elements have the same elements, vacuously.

2. **Membership is not inclusion.** a ∈ A says a is one of the elements; A ⊆ B says every element of A is an element of B. So 1 ∈ {1, 2} and {1} ⊆ {1, 2}, but {1} ∉ {1, 2}. Inclusion is transitive and membership is not: ∅ ∈ {∅} and {∅} ∈ {{∅}}, yet ∅ ∉ {{∅}}. Also ∅ ⊆ A for every A, because "x ∈ ∅ ⇒ x ∈ A" has a false hypothesis.

3. **The Boolean operations are the connectives.** A ∪ B = {x : x ∈ A ∨ x ∈ B}, A ∩ B = {x : x ∈ A ∧ x ∈ B} and A ∖ B = {x : x ∈ A ∧ x ∉ B}. Each identity is a tautology in disguise: x ∉ A ∪ B means ¬(x ∈ A ∨ x ∈ B), which is equivalent to x ∉ A ∧ x ∉ B, so U ∖ (A ∪ B) = (U ∖ A) ∩ (U ∖ B), one of De Morgan's laws. The subsets of a fixed set U form a Boolean algebra in which ⊆ plays the role of ⇒.

4. **Complements are relative, because there is no set of everything.** The complement of A means U ∖ A for a stated universe U, such as ℝ. An absolute complement would need a universal set, and naive comprehension ("every property P defines a set {x : P(x)}") is contradictory: for R = {x : x ∉ x}, R ∈ R ⇔ R ∉ R (Russell's paradox). The repair is to carve subsets out of a set already given, {x ∈ A : P(x)}, the separation axiom of [Zermelo–Fraenkel set theory](../03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md).

5. **Indexed unions and intersections are the quantifiers.** For sets Aᵢ indexed by i ∈ I, x ∈ ⋃ Aᵢ means ∃i (x ∈ Aᵢ) and x ∈ ⋂ Aᵢ means ∀i (x ∈ Aᵢ); De Morgan's laws extend because ¬∃ is ∀¬. Infinite operations behave unlike finite ones: the intervals (0, 1/n) for n = 1, 2, 3, … are nested and non-empty, yet their intersection is ∅, since every x > 0 exceeds some 1/n. Nested closed bounded intervals in ℝ always share a point; that difference is the completeness of ℝ.

6. **Order can be encoded in a set.** Sets are unordered, but the Kuratowski pair (a, b) = {{a}, {a, b}} satisfies (a, b) = (c, d) ⇔ a = c ∧ b = d: a is the element common to both members, and b is the other element of {a, b}, or a itself when that member is a singleton. So the Cartesian product A × B = {(a, b) : a ∈ A, b ∈ B} exists, and relations and functions become sets of pairs. The same habit gives the von Neumann numbers 0 = ∅, 1 = {∅}, 2 = {∅, {∅}}, used in [the natural numbers and the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md).

7. **A subset is a yes-or-no answer for each element.** The power set 𝒫(A) is the set of all subsets of A. If A has n elements, 𝒫(A) has 2ⁿ, because a subset is fixed by n independent in-or-out choices: {a, b} has the subsets ∅, {a}, {b}, {a, b}. The indicator function of S ⊆ A, equal to 1 on S and 0 off it, matches subsets of A one to one with functions A → {0, 1}. [Cantor's diagonal argument](../02-infinity-and-cardinality/cantors-diagonal-argument.md) uses that match to show 𝒫(A) is always larger than A.

## Key concepts

| Term | Meaning |
|---|---|
| Element, x ∈ A | x is one of the members of A; the one primitive relation |
| Subset, A ⊆ B | every element of A is an element of B |
| Extensionality | sets with the same elements are equal |
| Empty set ∅ | the unique set with no elements; a subset of every set |
| A ∪ B, A ∩ B, A ∖ B | membership combined by "or", "and", "and not" |
| Complement | U ∖ A, taken inside a stated universe U |
| Indexed family | a set Aᵢ for each index i ∈ I |
| Ordered pair | (a, b) = {{a}, {a, b}}; equal to (c, d) exactly when a = c and b = d |
| Cartesian product | A × B, all pairs (a, b) with a ∈ A and b ∈ B |
| Power set 𝒫(A) | the set of all subsets of A |
| Indicator function | 1 on S and 0 on A ∖ S |

## How it fits

- **Below:** [propositional logic](../../00-logic-and-proof/01-formal-logic/propositional-logic.md) supplies the connectives behind ∪, ∩ and ∖, and [predicate logic](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md) the quantifiers behind ⊆, ⋃ and ⋂. That the sets formed here exist is assumed naively and justified in [Zermelo–Fraenkel set theory](../03-axiomatic-set-theory/zermelo-fraenkel-set-theory.md).
- **Above:** [02 Number Systems](../../02-number-systems/README.md) builds every number as a set; events in [probability](../../03-combinatorics-and-graph-theory/03-discrete-probability/finite-probability-spaces.md) are subsets; [σ-algebras](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) and [topologies](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) are families of subsets closed under chosen operations.
- **Siblings:** [relations](relations-and-orders.md) and [functions](functions.md) are subsets of Cartesian products; [equivalence relations and quotients](equivalence-relations-and-quotients.md) turn a partition, a set of subsets, into a new set.

## Common misconceptions

- **"{a, b} and {b, a, a} are different sets"**: a set records only which objects belong to it, so they are equal; order and multiplicity need tuples or multisets, built from sets afterwards.
- **"a and {a} are the same thing"**: {a} has exactly one element, a. ∅ is empty but {∅} has an element, and the encoding 0 = ∅, 1 = {∅} depends on the difference.
- **"Any property defines a set"**: Russell's set {x : x ∉ x} shows this is contradictory, and with it the idea of a complement of "everything else"; see [paradoxes and naive set theory](../03-axiomatic-set-theory/paradoxes-and-naive-set-theory.md).

## Go deeper

- Paul R. Halmos, *Naive Set Theory* (1960): the classic short account, informal but faithful to the axioms.
- Daniel J. Velleman, *How to Prove It: A Structured Approach* (3rd edition, 2019): proofs about sets as exercises in logic.
- Herbert B. Enderton, *Elements of Set Theory* (1977): the same material developed carefully from the axioms.
