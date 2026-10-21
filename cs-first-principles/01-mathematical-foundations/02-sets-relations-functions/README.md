# Sets, Relations and Functions

> **Layer:** [01 Mathematical Foundations](../README.md) › Sets, Relations and Functions
> **Children:** [Sets](sets.md) · [Relations and Orders](relations-and-orders.md) · [Functions and Cardinality](functions-and-cardinality.md)

## What this area is about

This area supplies the raw material from which almost every other mathematical object in computer science is built. A set is a collection; a relation is a set of pairs; a function is a relation with one output per input. With these three ideas you can define strings and languages, graphs, database tables, types, data structures, state machines and probability spaces. The unifying idea is that *structure is defined by membership*: a relation *is* the set of pairs it relates, and a function *is* its input-output table, nothing more.

The area also answers a question that turns out to shape all of computing: how big is a set, and can one set be matched up with another? Comparing sizes by bijection shows that programs are countable while problems are not, so most problems cannot be solved by any program. That result, which comes before any machine is built, is the first hard limit in the stack.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Sets](sets.md) | Collections, set operations, products and power sets; strings and languages as sets | Predicate logic |
| [Relations and Orders](relations-and-orders.md) | Sets of pairs; equivalences (sameness) and partial orders (precedence); closure and lattices | Sets |
| [Functions and Cardinality](functions-and-cardinality.md) | Deterministic maps; injective, surjective, bijective; countable versus uncountable | Sets, relations |

Read in order: each child is defined as a special case of the previous one.

```
sets ──► relations (subsets of A × B) ──► functions (relations with one output per input)
                 │                                   │
                 ├─ equivalences → partitions        ├─ bijections → same size
                 └─ partial orders → schedules       └─ diagonal argument → uncountable
```

The two branches of relations matter differently in Computer Science (CS). Equivalence relations justify every "treat these as the same" step: hashing to buckets, connected components, canonical forms. Partial orders justify every "this must come before that" step: dependency resolution, happens-before in distributed systems, and the well-founded orders that make induction and termination proofs work. Functions then add determinism and, through bijections, a precise notion of size.

## Connections to sibling areas

- **[Logic](../01-logic/README.md):** Sets are written with predicates, and set algebra mirrors logical connectives. Logic needs sets to interpret quantifiers.
- **[Discrete Mathematics](../03-discrete-mathematics/README.md):** [Combinatorics](../03-discrete-mathematics/combinatorics.md) is cardinality for finite sets; [graphs](../03-discrete-mathematics/graph-theory.md) are relations; congruence in [number theory](../03-discrete-mathematics/number-theory.md) is an equivalence relation.
- **[Algebra](../04-algebra/README.md):** Algebraic structures are sets with functions (operations) obeying laws; Boolean algebra is the algebra of subsets.
- **[Continuous Mathematics](../05-continuous-mathematics/README.md):** Calculus studies functions on the real numbers, an uncountable set.
- **[Probability and Statistics](../06-probability-and-statistics/README.md):** Events are subsets of a sample space; random variables are functions on it.

## Connections across layers

The [automata and formal languages](../../02-theory-of-computation/02-automata-and-formal-languages/README.md) of layer 02 are sets of strings, and [computability](../../02-theory-of-computation/03-computability/README.md) rests on the countability argument. The [relational model](../../09-data-management/01-data-models/the-relational-model.md) is relation theory applied to data. [Type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md) read types as sets and function types as sets of functions. [Time, clocks and ordering](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md) is partial-order theory, and [CRDTs (Conflict-free Replicated Data Types)](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md) are lattices.

## Cross-cutting threads

- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): bijections are exactly lossless re-encodings; a set over a small universe is a bit vector.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): uncountably many problems, countably many programs.
- [State and time](../../CROSS-CUTTING.md#state-and-time): happens-before is a partial order, not a total one.
- [Composition](../../CROSS-CUTTING.md#composition): function composition is associative, which lets pipelines be built in pieces.
- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): Russell's paradox and Cantor's diagonal argument.
