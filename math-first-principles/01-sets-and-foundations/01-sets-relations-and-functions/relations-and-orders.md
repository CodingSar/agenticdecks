# Relations and Orders

> **Layer:** [01 Sets and Foundations](../README.md) › [Sets, Relations and Functions](README.md)
> **Builds on:** [Sets and set operations](sets-and-set-operations.md), [Predicate logic and quantifiers](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md)
> **Enables:** [Equivalence relations and quotients](equivalence-relations-and-quotients.md), [Ordinal numbers and transfinite induction](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [Graphs and connectivity](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md), [Posets and extremal set theory](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/posets-and-extremal-set-theory.md)

## Essence

A relation from A to B is a set of ordered pairs, a subset R ⊆ A × B, and "a R b" means (a, b) ∈ R. This turns any comparison (less than, divides, happens before) into an object with properties of its own. Four properties (reflexive, symmetric, antisymmetric, transitive) pick out the two kinds mathematics uses everywhere: equivalences, which say when things are alike, and orders, which say when one comes before another. For orders, the lesson is that comparison need not be total and extremes need not exist. A well-order, in which every non-empty subset has a least element, is exactly what makes induction work.

## Core tenets

1. **A relation is its set of pairs.** Two descriptions with the same pairs define the same relation: on ℝ, "x² = y²" and "x = y or x = −y" are one relation. A relation on a finite set is a directed graph, with an arrow a → b for each pair; composing relations follows two arrows in a row, and the inverse R⁻¹ reverses every arrow.

2. **The four basic properties are universal sentences, checked one at a time.** R on A is reflexive if ∀a (a R a), symmetric if a R b ⇒ b R a, antisymmetric if a R b ∧ b R a ⇒ a = b, and transitive if a R b ∧ b R c ⇒ a R c. "Divides" on ℤ is reflexive and transitive but neither symmetric (2 ∣ 4 but 4 ∤ 2) nor antisymmetric (2 ∣ −2 and −2 ∣ 2, yet 2 ≠ −2). Symmetric and antisymmetric are not opposites: together they force a R b ⇒ a = b, which equality satisfies.

3. **Closures exist because these properties survive intersection.** An intersection of transitive relations is transitive, so the transitive closure of R is the intersection of all transitive relations containing R (A × A is one). From below, it is R ∪ R² ∪ R³ ∪ …, where Rⁿ is R composed with itself n times: a reaches b along a path of arrows. Unions are not safe: {(1, 2)} and {(2, 3)} are transitive, but their union lacks (1, 3). The same pattern gives generated subgroups and generated σ-algebras.

4. **A partial order is reflexive, antisymmetric and transitive; it need not compare everything.** ⊆ on 𝒫(X), ≤ on ℝ and divisibility on ℕ are partial orders. ≤ is total, meaning any two elements are comparable, but ⊆ is not: {1} and {2} are incomparable. A finite partial order is drawn as a Hasse diagram, with an edge from each element up to each element directly above it. The divisors of 12 under divisibility:

```
        12
       /  \
      4    6
       \  / \
        2    3
         \  /
          1
```

5. **Maximal is not maximum, and bounds need not have a best one.** A maximal element has nothing strictly above it; a maximum is above everything. In {2, 3} under divisibility both elements are maximal and neither is a maximum. The supremum of S is its least upper bound, if one exists: in ℚ the set {x ∈ ℚ : x² < 2} is bounded above with no least rational upper bound, because √2 is irrational, and [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) are what fills such gaps. In a lattice every pair has a supremum and an infimum: 𝒫(X) with ∪ and ∩, or ℕ under divisibility with the least common multiple (lcm) and greatest common divisor (gcd).

6. **A well-order is what makes induction work.** A well-order is a total order in which every non-empty subset has a least element. To prove P(n) for all n ∈ ℕ, suppose it fails and take the least counterexample m; the inductive step from the cases below m gives a contradiction. ℤ, ℚ and even (0, 1) are not well-ordered, since none has a least element. Induction works along any well-founded relation (every non-empty subset has a minimal element), such as the lexicographic order on ℕ × ℕ, which proves that nested recursions terminate. Such a relation has no infinite descending chain; the converse needs dependent choice, a weak form of [the axiom of choice](../03-axiomatic-set-theory/the-axiom-of-choice.md).

7. **Order isomorphism is finer than counting.** An order isomorphism is a bijection f with x ≤ y ⇔ f(x) ≤ f(y). ℕ and ℤ can be matched one to one (list ℤ as 0, 1, −1, 2, −2, …), but they are not order-isomorphic, because ℕ has a least element and ℤ does not. The isomorphism types of well-orders are the [ordinal numbers](../02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md). Chains, subsets on which the order is total, are the subject of Zorn's lemma, which uses the axiom of choice to build maximal objects.

## Key concepts

| Term | Meaning |
|---|---|
| Relation | a subset R ⊆ A × B; a R b means (a, b) ∈ R |
| Transitive | a R b and b R c imply a R c |
| Transitive closure | the smallest transitive relation containing R: reachability along paths |
| Partial order | a reflexive, antisymmetric, transitive relation |
| Total order | a partial order in which any two elements are comparable |
| Upper bound, supremum | an element above every member of S; the least such, if it exists |
| Maximal element | an element with nothing strictly above it |
| Lattice | a partial order in which every pair has a supremum and an infimum |
| Well-order | a total order in which every non-empty subset has a least element |
| Well-founded relation | every non-empty subset has a minimal element |
| Chain | a subset on which the order is total |

## How it fits

- **Below:** relations are sets of pairs from [sets and set operations](sets-and-set-operations.md); their properties are quantified sentences from [predicate logic](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md); well-ordering is the set form of [mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md).
- **Above:** suprema define [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md); [posets](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/posets-and-extremal-set-theory.md) and [graphs](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md) are objects of combinatorics; computing uses partial orders for the [happens-before relation](../../../cs-first-principles/10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md) of distributed systems.
- **Siblings:** a [function](functions.md) is a relation with exactly one output per input, and an [equivalence relation](equivalence-relations-and-quotients.md) is the symmetric counterpart of a partial order.

## Common misconceptions

- **"In a partial order any two elements can be compared"**: that is a total order; {1} and {2} under ⊆ are incomparable.
- **"A maximal element is the largest element"**: there can be many maximal elements and no largest, as in {2, 3} under divisibility.
- **"Every bounded set has a supremum"**: only in a complete order such as ℝ; in ℚ, {x : x² < 2} has none.

## Go deeper

- B. A. Davey and H. A. Priestley, *Introduction to Lattices and Order* (2nd edition, 2002): the standard gentle text on orders and lattices.
- Paul R. Halmos, *Naive Set Theory* (1960): relations, orders and well-ordering in a few short chapters.
