# Foundations

> **Layer:** [05 Algorithms and Data Structures](../README.md) › Foundations
> **Children:** [Models of Computation](models-of-computation.md) · [Correctness and Invariants](correctness-and-invariants.md) · [Amortized Analysis](amortized-analysis.md)

## What this area is about

Before you can say an algorithm is "good" you need two things: a proof that it is right and a way to count what it costs. This area supplies both. It fixes a *cost model* (which operations count as one step, and what counts as memory), a *proof method* (invariants and induction), and a refinement of worst-case counting (*amortized* analysis) that matches how data structures are actually used: as long sequences of operations, not single calls.

The unifying idea is that an algorithmic claim is always relative to a model. "Sorting takes Θ(n log n)" is true for comparison sorts on a Random Access Machine (RAM). It is false for integer keys with radix sort, and incomplete on a machine where memory transfers, not instructions, dominate. Naming the model is what turns a claim into a theorem.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Models of Computation](models-of-computation.md) | Defines what a "step" and a "memory cell" cost; RAM, word RAM, comparison model, I/O model | [Turing machines](../../02-theory-of-computation/03-computability/turing-machines.md), [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/README.md) |
| [Correctness and Invariants](correctness-and-invariants.md) | Proves an algorithm meets its specification on every input | [Induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md) |
| [Amortized Analysis](amortized-analysis.md) | Bounds the total cost of a sequence of operations, not each one alone | Models of computation, invariants (the potential is an invariant on stored credit) |

Read them in order. The model tells you what to count. Correctness tells you the count is of a procedure worth running. Amortization tells you how to count when costs are uneven over time, which is the normal case for dynamic arrays, hash tables, union-find and self-adjusting trees.

```
  specification ──► algorithm ──► invariant proof ──► correct
                         │
                         └──► cost in model M ──► worst / expected / amortized bound
```

## Connections to sibling areas

- **[Fundamental Data Structures](../02-fundamental-data-structures/README.md):** every structure is a representation invariant plus operations that preserve it; amortized analysis justifies dynamic arrays and resizing hash tables.
- **[Design Paradigms](../03-design-paradigms/README.md):** each paradigm comes with a characteristic correctness argument (exchange argument for greedy, optimal substructure for dynamic programming) and a characteristic cost analysis (recurrences for divide and conquer).
- **[Sorting and Searching](../04-sorting-and-searching/README.md):** the comparison model defined here is exactly what makes the Ω(n log n) sorting lower bound provable.
- **[Graph Algorithms](../05-graph-algorithms/README.md):** Dijkstra and union-find are the classic examples where invariants and amortized bounds do the heavy lifting.
- **[String Algorithms](../06-string-algorithms/README.md):** Knuth–Morris–Pratt's linear time is an amortized argument on a pointer that never moves backwards.
- **[Advanced Topics](../07-advanced-topics/README.md):** external-memory and cache-oblivious algorithms replace the RAM model with the I/O model; streaming algorithms change the resource from time to space.

## Connections across layers

From below it takes logic and induction ([01](../../01-mathematical-foundations/README.md)), asymptotic notation ([02](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md)) and the facts about real machines ([04](../../04-computer-architecture/README.md)) that the RAM model idealises. Above, the same invariant-based reasoning becomes [Hoare logic](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) and [model checking](../../06-programming-languages/05-formal-methods/model-checking.md); amortized cost reasoning reappears in [garbage collection](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) and [log-structured storage](../../09-data-management/02-storage-and-indexing/lsm-trees.md).

## Cross-cutting threads

- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): loop and representation invariants are the main proof tool.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): the RAM model is an abstraction of hardware, and its leaks are where practice diverges.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): rare expensive operations paid for by many cheap ones.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): lower bounds are statements about every algorithm in a model.
