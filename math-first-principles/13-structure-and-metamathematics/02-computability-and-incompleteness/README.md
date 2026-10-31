# Computability and Incompleteness

> **Layer:** [13 Structure and Metamathematics](../README.md) › Computability and Incompleteness
> **Children:** [Computable functions and the Church–Turing thesis](computable-functions-and-the-church-turing-thesis.md) · [Undecidable problems](undecidable-problems.md) · [Gödel's incompleteness theorems](godels-incompleteness-theorems.md) · [Proof theory and reverse mathematics](proof-theory-and-reverse-mathematics.md)

## What this area is about

In 1900 Hilbert asked for an algorithm to decide whether a Diophantine equation has integer solutions, and in the 1920s he hoped to show that mathematics is complete, consistent and decidable by finitary means. This area records how those hopes were answered, mostly in the negative, and what was learnt from the answers. It first makes "algorithm" a mathematical notion, then proves that some precisely stated problems have no algorithmic solution, then turns the same method on formal theories themselves: any consistent, effectively axiomatised theory that contains enough arithmetic leaves true statements unproved and cannot prove its own consistency. Proof theory then measures what a theory can prove instead of only noting that it falls short.

The unifying idea is that *programs, formulas and proofs can all be coded as natural numbers*. Once they are, a theory can talk about its own proofs, a program can run on its own code, and Cantor's diagonal argument becomes a limit on what any program or any theory can do.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Computable functions and the Church–Turing thesis](computable-functions-and-the-church-turing-thesis.md) | defines computability; shows the definitions agree | 00 induction, 01 countable sets, 02 Peano axioms |
| [Undecidable problems](undecidable-problems.md) | the halting problem and its reductions to logic, number theory and group theory | computable functions, 01 diagonal argument |
| [Gödel's incompleteness theorems](godels-incompleteness-theorems.md) | true but unprovable sentences; consistency is unprovable from within | both of the above, 00 completeness |
| [Proof theory and reverse mathematics](proof-theory-and-reverse-mathematics.md) | ordinals measure the strength of theories; which axioms theorems need | Gödel, 01 ordinals, 03 Ramsey theory |

The order is forced. Turing's machines, Church's λ-calculus and Kleene's recursive functions give the same class of functions, and that agreement supports the thesis that the class captures effective computation. A diagonal argument over the list of all programs then gives the undecidable halting problem, and reductions carry it to the Entscheidungsproblem, to Hilbert's tenth problem and to the word problem for groups. Gödel's theorems follow because the theorems of an effectively axiomatised theory are listed by a program, so a complete theory would decide what cannot be decided. The last leaf replaces "provable or not" by a scale: the strength of Peano arithmetic (PA) is the ordinal ε₀, and natural theorems such as the Paris–Harrington theorem and Goodstein's theorem are true but unprovable in PA.

```
 coding: programs, formulas and proofs are natural numbers
              |
 computable functions (Turing, Church 1936)
              |  diagonalise
 undecidable problems: halting, Entscheidungsproblem, Hilbert's tenth, word problem
              |  the theorems of T are listed by a program
 Gödel: consistent + effectively axiomatised + enough arithmetic => incomplete
              |  measure strength instead
 proof theory: ε₀ for PA; reverse mathematics; Paris–Harrington, Goodstein
```

## Connections to sibling areas

- **[Category theory](../01-category-theory/README.md)** shares the Curry–Howard correspondence, under which proofs are programs and propositions are types, and F. William Lawvere's fixed-point theorem (1969), which puts the halting problem and Gödel's diagonal lemma in a single categorical form.
- **[Model theory and independence](../03-model-theory-and-independence/README.md)** takes Gödel's incompleteness as its starting point for independence; its decidable theories, such as the real field and Presburger arithmetic, are the positive side of the boundary drawn here, and large cardinals continue the scale of consistency strength upward from ε₀.

## Connections across layers

- **Below:** It formalises the [proof systems](../../00-logic-and-proof/01-formal-logic/formal-proof-systems.md) and [completeness theorem](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md) of layer 00 and answers its question of [consistency](../../00-logic-and-proof/03-the-axiomatic-method/consistency-and-independence.md); it reuses [Cantor's diagonal argument](../../01-sets-and-foundations/02-infinity-and-cardinality/cantors-diagonal-argument.md) and [ordinals](../../01-sets-and-foundations/02-infinity-and-cardinality/ordinal-numbers-and-transfinite-induction.md), the [Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md) and [Diophantine equations](../../02-number-systems/02-elementary-number-theory/diophantine-equations.md), and [group presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md).
- **Above:** The [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) weighs what incompleteness means for formalism and mechanism, and [computer-checked proof](../../15-mathematics-in-context/computers-and-proof.md) rests on proofs being finite, checkable objects.
- **Sideways:** The computer science tree treats the same theory from the machine side, in [computability](../../../cs-first-principles/02-theory-of-computation/03-computability/README.md), including [Turing machines](../../../cs-first-principles/02-theory-of-computation/03-computability/turing-machines.md) and the [halting problem](../../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), and continues it into [complexity](../../../cs-first-principles/02-theory-of-computation/04-complexity/README.md), which asks what can be computed efficiently.

## Cross-cutting threads

- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the halting problem and Gödel's theorems are the model impossibility proofs.
- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): computable functions are built by recursion, and theories are measured by how much transfinite induction they prove.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): countably many programs against uncountably many functions; ordinals as measures of strength.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): coding turns statements about proofs and programs into statements about numbers and equations.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): what can be proved to exist need not be computable, and reverse mathematics measures the gap.
