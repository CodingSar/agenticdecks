# 05 Algorithms and Data Structures

> **Layer:** 05 Algorithms and Data Structures
> **Children:** [Foundations](01-foundations/README.md) · [Fundamental Data Structures](02-fundamental-data-structures/README.md) · [Design Paradigms](03-design-paradigms/README.md) · [Sorting and Searching](04-sorting-and-searching/README.md) · [Graph Algorithms](05-graph-algorithms/README.md) · [String Algorithms](06-string-algorithms/README.md) · [Advanced Topics](07-advanced-topics/README.md)

## What this area is about

An algorithm is a finite, precisely specified procedure that turns any valid input into the correct output. A data structure is a way of laying out information in memory so that the operations an algorithm needs are cheap. This layer asks two questions about every problem: *is the procedure correct for every input?* and *how do its costs (time, memory, memory transfers) grow as the input grows?*

The unifying idea is that **representation decides cost**. The same set of numbers stored as an unsorted array, a sorted array, a hash table, a balanced tree or a heap supports different operations at very different prices. Algorithm design is the art of choosing a representation and an invariant (a property that every step preserves) so that the work you must do is small and provably enough. Theory then tells you when you have hit a wall: some problems need Ω(n log n) comparisons, some need to look at every input bit, and some (the NP-hard ones) probably have no efficient exact algorithm at all.

## Why this layer sits here

Algorithms might look like pure mathematics, and much of their analysis is. But the cost model used to analyse them is a machine.

- **From [01 Mathematical Foundations](../01-mathematical-foundations/README.md):** proofs by [induction](../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) establish correctness and solve running-time recurrences; [graph theory](../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) supplies the objects most algorithms manipulate; [combinatorics](../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md) counts the possibilities that lower bounds rest on; [probability](../01-mathematical-foundations/06-probability-and-statistics/probability.md) underpins randomized algorithms and hashing.
- **From [02 Theory of Computation](../02-theory-of-computation/README.md):** [asymptotic analysis](../02-theory-of-computation/04-complexity/asymptotic-analysis.md) gives the O, Ω, Θ language; [P, NP and NP-completeness](../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) tells you when to stop looking for an exact fast algorithm; [computability](../02-theory-of-computation/03-computability/README.md) tells you some problems have no algorithm at all.
- **From [04 Computer Architecture](../04-computer-architecture/README.md):** the standard Random Access Machine (RAM) model is an idealised computer: unit-cost access to any memory word, unit-cost arithmetic on words of Θ(log n) bits. That is a deliberate abstraction of a real processor. It predicts well when data fits in cache and badly when it does not. A random memory access costs ~1 ns in Level 1 (L1) cache and ~100 ns in Dynamic Random-Access Memory (DRAM) (circa 2020s hardware), a factor of about 100 the RAM model ignores. Cache-aware, cache-oblivious and external-memory algorithms exist only because of the [memory hierarchy](../04-computer-architecture/03-memory-hierarchy/README.md); you cannot design or even state them without layer 04.

The layer contributes one abstraction to the stack: **the algorithmic contract**, a specification (input, output, pre- and postconditions) plus a cost bound in a named machine model. Everything above uses that contract to reason about what is feasible without measuring every program.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Foundations](01-foundations/README.md) | Cost models, correctness proofs, amortized analysis | 01, 02, 04 |
| [02 Fundamental Data Structures](02-fundamental-data-structures/README.md) | The containers: arrays, lists, stacks, queues, hash tables, trees, heaps, union–find | 01 Foundations |
| [03 Design Paradigms](03-design-paradigms/README.md) | Reusable strategies: divide and conquer, greedy, dynamic programming, search, randomization | Foundations, data structures |
| [04 Sorting and Searching](04-sorting-and-searching/README.md) | The canonical problems; first tight lower bounds | Paradigms, structures |
| [05 Graph Algorithms](05-graph-algorithms/README.md) | Traversal, shortest paths, spanning trees, flow | Queues, heaps, [union–find](02-fundamental-data-structures/union-find.md), paradigms |
| [06 String Algorithms](06-string-algorithms/README.md) | Pattern matching and text indexes | Automata, hashing, sorting |
| [07 Advanced Topics](07-advanced-topics/README.md) | Beyond exact, in-RAM, offline: approximation, streaming, external memory, geometry | Everything above |

```
             07 Advanced topics (relax the model: approximate, streaming, I/O, geometry)
          /          |             \
   05 Graphs   06 Strings   04 Sorting & searching      <- canonical problems
          \          |             /
             03 Design paradigms                         <- how to find an algorithm
                     |
             02 Data structures                          <- how to store state cheaply
                     |
             01 Foundations                              <- how to measure and prove
```

Read bottom-up. Foundations give you the yardstick. Data structures are the vocabulary. Paradigms are the grammar. Sorting, graphs and strings are the classic sentences, and advanced topics change the rules: they give up exactness, offline access or the flat-memory assumption to get something feasible.

## Connections to neighbouring layers

- **[02 Theory of Computation](../02-theory-of-computation/README.md):** theory says what is possible and how hard problems are in principle; this layer builds concrete procedures and matches upper bounds to lower bounds. [Finite automata](../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) reappear as string matchers.
- **[04 Computer Architecture](../04-computer-architecture/README.md):** [caches](../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [Single Instruction, Multiple Data (SIMD) units and Graphics Processing Units (GPUs)](../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [branch prediction](../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) explain why an O(n log n) algorithm can beat an O(n) one in practice.
- **[06 Programming Languages](../06-programming-languages/README.md):** compilers are algorithm-heavy: parsing uses automata and dynamic programming, [register allocation](../06-programming-languages/03-compilers/code-generation-and-register-allocation.md) is graph colouring, [garbage collection](../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) is graph traversal.
- **[07 Operating Systems](../07-operating-systems/README.md):** [schedulers](../07-operating-systems/02-process-management/scheduling.md) use priority queues, [page replacement](../07-operating-systems/04-memory-management/page-replacement.md) is an online caching problem, [memory allocators](../07-operating-systems/04-memory-management/memory-allocation.md) use free lists and buddy trees, and [deadlock detection](../07-operating-systems/03-concurrency/deadlock.md) is cycle detection.
- **[08 Networking](../08-networking/README.md):** [routing](../08-networking/03-network-layer/routing-algorithms.md) is shortest paths (Dijkstra in link-state, Bellman–Ford in distance-vector); [forwarding](../08-networking/03-network-layer/ip-addressing-and-forwarding.md) is longest-prefix match on tries.
- **[09 Data Management](../09-data-management/README.md):** [B-trees](../09-data-management/02-storage-and-indexing/b-trees.md) and [Log-Structured Merge (LSM) trees](../09-data-management/02-storage-and-indexing/lsm-trees.md) are external-memory search structures; [join algorithms](../09-data-management/03-query-processing/join-algorithms.md) are sorting and hashing; [query optimization](../09-data-management/03-query-processing/query-optimization.md) is dynamic programming.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md):** the [work–span model](../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) extends sequential cost analysis to many processors; [consistent hashing](../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) extends hash tables to many machines.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** [heuristic search](../13-artificial-intelligence/01-classical-ai/search-and-planning.md) is graph search with estimates, [constraint satisfaction](../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md) is backtracking, and [training](../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) is iterative numerical optimisation whose cost is dominated by matrix multiplication.

## Connections across layers

This layer takes discrete mathematics, probability and complexity theory from 01 and 02, and an idealised machine from 04. It gives every higher layer a catalogue of solved problems with known costs. Compilers, kernels, databases, routers and machine learning (ML) systems are, at their core, carefully chosen data structures plus algorithms whose costs match the hardware. When those systems are slow, the cause is usually one of three things this layer names: the wrong asymptotic class, a constant factor the model ignored, or a memory-access pattern the RAM model could not see.

## Cross-cutting threads

- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): the choice of data structure decides which operations are cheap.
- [Invariants and correctness](../CROSS-CUTTING.md#invariants-and-correctness): every algorithm here is justified by an invariant (loop invariant, heap order, balance condition, cut property).
- [Recursion and self-reference](../CROSS-CUTTING.md#recursion-and-self-reference): divide and conquer and dynamic programming define solutions by smaller instances.
- [Batching and amortization](../CROSS-CUTTING.md#batching-and-amortization): dynamic arrays, union–find and splay trees pay rare large costs that average out.
- [Caching and locality](../CROSS-CUTTING.md#caching-and-locality): memoization, and the gap between RAM-model and real performance.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): comparison-sort and search lower bounds, NP-hardness, streaming space bounds.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): time vs space, worst case vs expected, exact vs approximate.
