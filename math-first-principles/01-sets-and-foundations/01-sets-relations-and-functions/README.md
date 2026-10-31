# Sets, Relations and Functions

> **Layer:** [01 Sets and Foundations](../README.md) › Sets, Relations and Functions
> **Children:** [Sets and set operations](sets-and-set-operations.md) · [Relations and orders](relations-and-orders.md) · [Functions](functions.md) · [Equivalence relations and quotients](equivalence-relations-and-quotients.md)

## What this area is about

This area supplies the vocabulary that the rest of mathematics is written in. It starts from one primitive, membership, and builds four things from it: sets and their Boolean operations, relations as sets of pairs, functions as relations with one output per input, and quotients, which turn "equivalent" into "equal". Nothing here is a hard theorem; what is remarkable is that these four notions suffice. A group, a metric space, a probability space and a manifold are each a set with extra data, and that data (an operation, a distance, a family of events, an atlas of charts) is itself a set, a relation or a function.

The unifying idea is that *structure is data on a set, and the data is itself a set*. Two habits follow, and they recur in every layer above: compare objects by the maps between them, and identify objects by passing to a quotient.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Sets and set operations](sets-and-set-operations.md) | membership, Boolean operations, ordered pairs, Cartesian products, power sets | 00 logic only |
| [Relations and orders](relations-and-orders.md) | relations as sets of pairs; partial orders, suprema, well-orders and induction | sets |
| [Functions](functions.md) | relations with one output per input; injections, surjections, images, preimages | sets, relations |
| [Equivalence relations and quotients](equivalence-relations-and-quotients.md) | partitions, quotient sets, and when a definition on classes is well defined | relations, functions |

Read them in order. The ordered pair from the first leaf is the hinge: once (a, b) is a set, the Cartesian product A × B exists, and relations and functions become subsets of it. The second and fourth leaves are two halves of one story about relations: orders say when one thing comes before another, equivalences say when two things are alike. Functions tie the two together, because every function defines an equivalence (its kernel) and every equivalence comes from a function (its quotient map).

```
 sets ──► ordered pairs, A × B ──► relations R ⊆ A × B
                                     │
            ┌────────────────────────┼─────────────────────────┐
            ▼                        ▼                         ▼
   orders (≤, ⊆, divides)   functions (one output    equivalences (~)
   well-orders → induction    per input)             = partitions
                                     │                         │
                                     └──► quotient map q: X → X/~
                                          well defined ⇔ constant on classes
```

Sets are used naively here: they are formed whenever needed. That is safe, because this area only forms subsets, products and power sets of sets already given. The one dangerous move, forming {x : P(x)} with no ambient set, is shown to be contradictory in the first leaf and repaired in [axiomatic set theory](../03-axiomatic-set-theory/README.md).

## Connections to sibling areas

- **[Infinity and Cardinality](../02-infinity-and-cardinality/README.md)** takes the bijection as the definition of "same size" and the well-order as the backbone of the ordinals; the power set from the first leaf is what Cantor's theorem shows is always larger than the set itself.
- **[Axiomatic Set Theory](../03-axiomatic-set-theory/README.md)** justifies every set formed here by an axiom (pairing, union, power set, separation) and isolates the one principle used in passing that needs an axiom of its own: picking a right inverse for an arbitrary surjection, or a representative from every equivalence class, is the axiom of choice.

## Connections across layers

- **Below:** set operations are [propositional connectives](../../00-logic-and-proof/01-formal-logic/propositional-logic.md), inclusion and indexed unions are [quantifiers](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), and the proofs are the [methods of proof](../../00-logic-and-proof/02-methods-of-proof/what-a-proof-is.md) applied to membership. In return, 00's [soundness and completeness](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md) uses these leaves to say what a model is.
- **Above:** [02 Number Systems](../../02-number-systems/README.md) builds ℤ and ℚ as quotients; [combinatorics](../../03-combinatorics-and-graph-theory/README.md) counts sets, functions and partitions; [abstract algebra](../../05-abstract-algebra/README.md) and [topology](../../07-topology/README.md) study sets with structure through structure-preserving maps and quotients; [measure theory](../../09-advanced-analysis/README.md) works with families of subsets; [category theory](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md) makes objects and maps the starting point.
- **Sideways:** the computer science tree covers the same ground for programmers in [sets, relations and functions](../../../cs-first-principles/01-mathematical-foundations/02-sets-relations-functions/README.md).

## Cross-cutting threads

- [Equivalence and quotients](../../CROSS-CUTTING.md#equivalence-and-quotients): the quotient set, and the rule that well defined means constant on classes.
- [Structure and morphism](../../CROSS-CUTTING.md#structure-and-morphism): sets are compared by injections, surjections and bijections.
- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): a function is any set of pairs, not a formula.
- [Induction and recursion](../../CROSS-CUTTING.md#induction-and-recursion): a well-order is exactly what makes induction by least counterexample work.
- [Invariants](../../CROSS-CUTTING.md#invariants): an invariant is a function on a quotient.
