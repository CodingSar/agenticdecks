# Design Paradigms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › Design Paradigms
> **Children:** [Divide and Conquer](divide-and-conquer.md) · [Greedy Algorithms](greedy-algorithms.md) · [Dynamic Programming](dynamic-programming.md) · [Backtracking and Branch and Bound](backtracking-and-branch-and-bound.md) · [Randomized Algorithms](randomized-algorithms.md)

## What this area is about

Most algorithms are not invented from nothing. They are instances of a handful of strategies, each of which exploits a particular structure in the problem. This area answers: *what structure does my problem have, and which strategy turns that structure into an efficient algorithm?* Knowing the paradigms turns algorithm design from inspiration into a checklist.

The unifying idea is **how the problem decomposes into subproblems**. If subproblems are independent and you can combine their answers, use divide and conquer. If they overlap, so the same subproblem recurs many times, store answers and use dynamic programming. If one locally best choice is always safe, so you never need to reconsider, use a greedy algorithm. If no such structure exists and you must explore choices, use backtracking and prune what cannot win. Randomization is orthogonal: it can be added to any of these to defeat bad inputs or to simplify.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Divide and Conquer](divide-and-conquer.md) | Split into independent subproblems, solve recursively, combine | [Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) |
| [Greedy Algorithms](greedy-algorithms.md) | Commit to the locally best choice; prove it is never wrong | [Invariants](../01-foundations/correctness-and-invariants.md), exchange arguments |
| [Dynamic Programming](dynamic-programming.md) | Solve overlapping subproblems once each, in dependency order | Divide and conquer (same recursion, plus memory) |
| [Backtracking and Branch and Bound](backtracking-and-branch-and-bound.md) | Systematic search with pruning for problems lacking the structures above | [NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) |
| [Randomized Algorithms](randomized-algorithms.md) | Use coin flips to get simplicity or speed with probabilistic guarantees | [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) |

```
  Does the problem split into subproblems?
     │
     ├─ independent subproblems ─────────────► divide and conquer
     ├─ overlapping subproblems + optimal ───► dynamic programming
     │    substructure
     ├─ ... and a greedy choice is safe ─────► greedy (one branch suffices)
     └─ no exploitable structure ────────────► backtracking / branch and bound
  Orthogonal: add randomness to any of these ► randomized algorithms
```

Greedy and dynamic programming are close relatives: both need *optimal substructure* (an optimal solution contains optimal solutions to subproblems). Dynamic programming tries every choice and keeps the best; greedy proves only one choice needs trying. Backtracking is what you fall back to when neither works, and is exponential in the worst case. That is expected, because those problems are typically NP-hard.

## Connections to sibling areas

- **[Foundations](../01-foundations/README.md):** each paradigm has a signature proof (recurrence solving, exchange argument, subproblem induction) and cost analysis (Master Theorem, table size × work per cell).
- **[Fundamental Data Structures](../02-fundamental-data-structures/README.md):** greedy algorithms need priority queues; dynamic programming needs tables (arrays or hash maps); backtracking needs a stack.
- **[Sorting and Searching](../04-sorting-and-searching/README.md):** merge sort and quicksort are the archetypal divide-and-conquer algorithms; randomized quickselect finds medians in expected linear time.
- **[Graph Algorithms](../05-graph-algorithms/README.md):** Dijkstra, Prim and Kruskal are greedy; Bellman–Ford and Floyd–Warshall are dynamic programming.
- **[String Algorithms](../06-string-algorithms/README.md):** edit distance is dynamic programming; Rabin–Karp is randomized.
- **[Advanced Topics](../07-advanced-topics/README.md):** approximation algorithms are often greedy or rounded linear programs; streaming algorithms are randomized.

## Connections across layers

These paradigms rest on [induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) and [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), and their limits come from [complexity theory](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md). Higher layers apply them: [register allocation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md) uses greedy graph colouring, [query optimizers](../../09-data-management/03-query-processing/query-optimization.md) use dynamic programming over join orders, [constraint solvers](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md) use backtracking, [reinforcement learning](../../13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) generalises dynamic programming (Bellman equations), and [MapReduce](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) is divide and conquer across machines.

## Cross-cutting threads

- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): every paradigm except pure greedy is defined recursively.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): memoization is caching applied to subproblem answers.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): greedy proofs are invariants of the form "partial solution extends to an optimum".
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): space for time in dynamic programming; certainty for speed in randomization.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): independent subproblems in divide and conquer run in parallel.
