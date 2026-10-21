# Sets

> **Layer:** [01 Mathematical Foundations](../README.md) › [Sets, Relations and Functions](README.md)
> **Builds on:** [Predicate Logic](../01-logic/predicate-logic.md)
> **Enables:** [Relations and Orders](relations-and-orders.md), [Finite Automata and Regular Languages](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md), [The Relational Model](../../09-data-management/01-data-models/the-relational-model.md), [Probability](../06-probability-and-statistics/probability.md), [Type Systems](../../06-programming-languages/02-semantics-and-types/type-systems.md)

## Essence

A set is a collection of distinct objects with no order and no repetition, determined entirely by which things are members. Almost every mathematical object a computer scientist uses is built from sets: a relation is a set of pairs, a function is a special relation, a language is a set of strings, a type can be read as a set of values, a database table is a set of tuples, and an event in probability is a set of outcomes. Set operations (union, intersection, difference, complement, product, power set) are the basic ways to build new collections from old ones. The single idea that makes sets work is *extensionality*: two sets are equal exactly when they have the same members, regardless of how they were described.

## Core tenets

1. **A set is defined by membership alone (extensionality).** `{1, 2, 2, 3}` and `{3, 1, 2}` are the same set. Order and multiplicity are not part of the object, which is why lists, multisets (bags) and sets are different data types. Relational databases are defined on sets of tuples, while Structured Query Language (SQL) actually returns bags unless you write `DISTINCT`, a gap between theory and practice that causes real bugs.

2. **Sets are described by listing or by a predicate.** `{x ∈ ℕ | x mod 2 = 0}` uses a predicate to select members of an existing set. This set-builder notation is the ancestor of list comprehensions (`[x for x in xs if x % 2 == 0]`) and of SQL's `SELECT … WHERE`. Selecting from an *existing* set is essential, as the next tenet shows.

3. **Unrestricted comprehension is inconsistent (Russell's paradox).** If any predicate defined a set, then `R = {x | x ∉ x}` would exist, and `R ∈ R` holds exactly when `R ∉ R`. Zermelo–Fraenkel set theory (ZF) avoids this by allowing comprehension only inside an already-existing set. The paradox is self-reference, the same force behind the [halting problem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) and behind type systems that forbid a type from containing itself.

4. **Set operations mirror logical connectives.** Union is OR on membership, intersection is AND, complement is NOT, and subset is implication: `A ⊆ B` means `x ∈ A → x ∈ B`. Hence De Morgan's laws hold for sets exactly as for propositions, and both are instances of [Boolean algebra](../04-algebra/boolean-algebra.md). A bitset makes this literal: a set over a small universe is a machine word, and `&`, `|`, `~` are intersection, union and complement in one instruction.

5. **The Cartesian product builds tuples, and the power set builds all subsets.** `A × B` is the set of ordered pairs `(a, b)`; it is the mathematical meaning of a record or struct type, and |A × B| = |A|·|B|. The power set `P(A)` of all subsets has 2^|A| elements, which is why a subset of *n* items is an *n*-bit vector, and why the [subset construction](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) that turns a nondeterministic automaton with *n* states into a deterministic one can need 2^n states.

6. **Inclusion–exclusion counts overlapping sets correctly.** |A ∪ B| = |A| + |B| − |A ∩ B|, and the pattern extends to more sets with alternating signs. It is the basis of counting arguments in [combinatorics](../03-discrete-mathematics/combinatorics.md), of the union bound in [probability](../06-probability-and-statistics/probability.md), and of reasoning about Bloom filter false positives.

7. **Strings and languages are sets too.** An alphabet Σ is a finite set; Σ* is the set of all finite strings over it; a *language* is any subset of Σ*. Because Σ* is countably infinite but its power set is uncountable, most languages have no program that recognises them. This one counting fact, developed in [functions and cardinality](functions-and-cardinality.md), is the root of uncomputability.

## Key concepts

| Term | Meaning |
|---|---|
| Membership (∈) | `x ∈ A` says object `x` belongs to set `A` |
| Subset (⊆) | Every member of `A` is a member of `B` |
| Union / intersection / difference | Members of either / both / the first but not the second |
| Complement | Members of the universe not in `A` |
| Cartesian product (×) | Set of ordered pairs (tuples) drawn from each set |
| Power set P(A) | The set of all subsets of `A`; size 2^|A| for finite `A` |
| Empty set (∅) | The unique set with no members |
| Partition | A split of a set into non-empty, disjoint pieces that cover it |
| Multiset (bag) | Like a set but members can repeat |

## How it fits

- **Below:** Sets are described using [predicate logic](../01-logic/predicate-logic.md); membership is a predicate.
- **Above:** Formal languages and automata ([02](../../02-theory-of-computation/README.md)) are sets of strings. The [relational model](../../09-data-management/01-data-models/the-relational-model.md) is set theory applied to data. [Type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md) read types as sets of values, with product types as Cartesian products and sum types as disjoint unions. Hash sets and [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) implement the set interface.
- **Siblings:** [Relations](relations-and-orders.md) are subsets of products; [functions](functions-and-cardinality.md) are special relations and give the notion of size for infinite sets.

## Common misconceptions

- **"A set has an order."** Any order you see (a sorted printout) is a property of the representation, not the set.
- **"Any description defines a set."** Russell's paradox shows it does not; definitions must select from something that already exists.
- **"∅ and {∅} are the same."** The first has no elements, the second has one (the empty set). The distinction matters like the one between an empty list and a list containing an empty list.

## Go deeper

- Paul Halmos, *Naive Set Theory* (1960): short, classic, enough set theory for all of computer science.
- Eric Lehman, F. Thomson Leighton and Albert Meyer, *Mathematics for Computer Science* (2017 revision, free online): sets and counting with computer-science examples.
- Kenneth Rosen, *Discrete Mathematics and Its Applications* (8th ed., 2019): broad reference with many exercises.
