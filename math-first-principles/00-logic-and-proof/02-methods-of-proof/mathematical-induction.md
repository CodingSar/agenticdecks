# Mathematical Induction

> **Layer:** [00 Logic and Proof](../README.md) › [Methods of Proof](README.md)
> **Builds on:** [What a Proof Is](what-a-proof-is.md), [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md), [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md)
> **Enables:** [Natural Numbers and the Peano Axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md), [Ordinal Numbers and Transfinite Induction](../../01-sets-and-foundations/02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), [Recurrence Relations](../../03-combinatorics-and-graph-theory/01-enumeration/recurrence-relations.md), [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md), [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md)

## Essence

Mathematical induction proves a statement P(n) for every natural number n from two finite pieces: the base case P(0) and the inductive step, that P(n) implies P(n + 1) for every n. It works because the natural numbers are exactly what is reached from 0 by repeatedly adding 1, so no number escapes the chain. Strong induction, the well-ordering principle and infinite descent are equivalent forms of the idea, and structural induction extends it to anything built by rules, such as formulas, trees and derivations. Induction verifies a statement; it does not find it.

## Core tenets

1. **Base case and step together reach every number.** To prove 1 + 3 + … + (2n − 1) = n²: for n = 1 both sides are 1, and if the formula holds for n, adding 2n + 1 gives n² + 2n + 1 = (n + 1)². Neither part suffices alone: "n > n + 1" has a valid step (if n > n + 1 then n + 1 > n + 2) but no base case. The argument that all horses have the same colour, by overlapping groups of n out of n + 1 horses, fails because its step breaks from 1 to 2, where the groups do not overlap.

2. **Strong induction assumes all smaller cases.** To prove P(n), one may assume P(k) for every k < n. Every integer n ≥ 2 is a product of primes: if n is not prime, then n = ab with 2 ≤ a, b < n, and a and b are products of primes. Strong induction is no stronger than ordinary induction: it is ordinary induction applied to Q(n), "P(k) holds for every k ≤ n".

3. **Well-ordering: every non-empty set of natural numbers has a least element.** It is equivalent to induction. If P failed somewhere, there would be a least counterexample m, and showing that P(m) follows from P at smaller numbers is the contradiction. The property is special to ℕ and its relatives: ℤ has no least element, nor does the set of positive real numbers.

4. **Infinite descent: no strictly decreasing infinite sequence of natural numbers exists.** Fermat used it to show that x⁴ + y⁴ = z² has no solution in positive integers, by building a smaller solution from any given one. It also proves √2 irrational: if √2 = a/b with b the least possible positive denominator, then b < a < 2b and

```
(2b − a)² = 4b² − 4ab + a² = 6b² − 4ab = 2(a − b)²,     with 0 < a − b < b
```

so √2 = (2b − a)/(a − b), with a smaller denominator.

5. **A stronger hypothesis can make the step go through.** The bound ∑ 1/k² ≤ 2, summed for k from 1 to n, resists induction, since the bound 2 leaves no room for the next term. The stronger ∑ 1/k² ≤ 2 − 1/n succeeds: its step needs 1/(n + 1)² ≤ 1/n − 1/(n + 1), true because 1/(n + 1)² ≤ 1/(n(n + 1)) = 1/n − 1/(n + 1). Finding an invariant strong enough to be preserved is also how loops are proved correct ([Correctness and Invariants](../../../cs-first-principles/05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)).

6. **Structural induction proves properties of everything built by rules.** If a property holds for the basic objects and survives each construction rule, it holds for all objects so built: every formula has as many left as right brackets, and the soundness theorem is proved by induction on derivations. Well-founded induction, along any relation with no infinite descending chain, covers all these cases, and transfinite induction extends it along the ordinals ([Ordinal Numbers and Transfinite Induction](../../01-sets-and-foundations/02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md)).

7. **Recursion is induction's twin.** Giving f(0) and f(n + 1) in terms of f(n) defines f on all of ℕ, by the recursion theorem, itself proved by induction: 0! = 1 and (n + 1)! = (n + 1) · n!. The Peano axioms make induction an axiom of arithmetic ([Natural Numbers and the Peano Axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md)), and the pairing runs through mathematics and computing ([induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion)).

8. **Induction verifies; it does not discover.** To prove ∑ k² = n(n + 1)(2n + 1)/6 by induction, the formula must already be known, guessed for instance by fitting a cubic to the first few values. Induction then checks it, and the algebra of the step often shows why it holds.

## Key concepts

| Term | Meaning |
|---|---|
| Base case | P at the starting value |
| Inductive step | P(n) ⇒ P(n + 1) for every n |
| Inductive hypothesis | The assumption P(n), or every P(k) with k < n, used in the step |
| Strong induction | Induction that assumes all smaller cases |
| Well-ordering principle | Every non-empty set of natural numbers has a least element |
| Infinite descent | No strictly decreasing infinite sequence of natural numbers exists |
| Structural induction | Induction over objects generated by rules |
| Well-founded relation | A relation with no infinite descending chain |
| Recursive definition | Defining f(n + 1) from f(n), justified by the recursion theorem |

## How it fits

- **Below:** [Predicate Logic and Quantifiers](../01-formal-logic/predicate-logic-and-quantifiers.md) gives the form ∀n P(n); [What a Proof Is](what-a-proof-is.md) and [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md) supply the steps and the least-counterexample argument.
- **Above:** [Natural Numbers and the Peano Axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md) makes induction an axiom; [Recurrence Relations](../../03-combinatorics-and-graph-theory/01-enumeration/recurrence-relations.md) and [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md) use it constantly; [Soundness, Completeness and Compactness](../01-formal-logic/soundness-completeness-and-compactness.md) is proved by structural induction; computing uses it for recursive programs ([Induction and Recurrences](../../../cs-first-principles/01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md)).
- **Siblings:** [Direct Proof, Contraposition and Contradiction](direct-proof-contraposition-and-contradiction.md) proves the step; [Cases, Constructions and Counterexamples](cases-constructions-and-counterexamples.md) checks finitely many cases where induction covers infinitely many.

## Common misconceptions

- **"Induction assumes what it is trying to prove"**: the step assumes P(n) for one n in order to prove P(n + 1); it never assumes ∀n P(n).
- **"Spotting a pattern is induction"**: that is the inductive reasoning of the empirical sciences; mathematical induction is deduction and needs a proved step.
- **"Induction works on any infinite set"**: it needs a well-founded order; on ℤ or ℝ with the usual order there is no base from which every element is reached.

## Go deeper

- Ronald L. Graham, Donald E. Knuth and Oren Patashnik, *Concrete Mathematics* (2nd edition, 1994): induction and recurrences in practice.
- Daniel J. Velleman, *How to Prove It: A Structured Approach* (3rd edition, 2019), chapter 6: induction, strong induction and recursion.
- George Pólya, *Induction and Analogy in Mathematics* (1954): how formulas are guessed before they are proved.
