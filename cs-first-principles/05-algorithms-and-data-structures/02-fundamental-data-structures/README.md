# Fundamental Data Structures

> **Layer:** [05 Algorithms and Data Structures](../README.md) › Fundamental Data Structures
> **Children:** [Arrays and Linked Lists](arrays-and-linked-lists.md) · [Stacks and Queues](stacks-and-queues.md) · [Hash Tables](hash-tables.md) · [Search Trees](search-trees.md) · [Heaps and Priority Queues](heaps-and-priority-queues.md) · [Union–Find](union-find.md)

## What this area is about

A data structure is a representation of a collection plus a set of operations, chosen so that the operations a program needs most are cheap. The question this area answers is: *given the operations I need (insert, delete, look up by key, find the minimum, iterate in order), which layout makes them fastest, and what does it cost in memory?*

The unifying idea is that every structure trades **order** for **speed**. An unsorted array keeps no order and inserts in O(1) but searches in O(n). A hash table throws order away entirely to get O(1) expected lookup by exact key. A balanced search tree keeps full sorted order and pays O(log n) for every operation. A heap keeps only *partial* order (the minimum is at the top) and gets O(log n) insert and extract-min with an array and no pointers. Union–find keeps no order at all, only which group each element belongs to, and answers "same group?" in nearly constant amortized time. Knowing how much order you need is most of the choice.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Arrays and Linked Lists](arrays-and-linked-lists.md) | The two physical primitives: contiguous memory vs pointers | [Models of computation](../01-foundations/models-of-computation.md), [amortized analysis](../01-foundations/amortized-analysis.md) |
| [Stacks and Queues](stacks-and-queues.md) | Restricted access orders (LIFO, FIFO) that most algorithms use as work lists | Arrays and lists |
| [Hash Tables](hash-tables.md) | Unordered dictionary with O(1) expected operations | Arrays, [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) |
| [Search Trees](search-trees.md) | Ordered dictionary with O(log n) operations and range queries | Linked structure, [invariants](../01-foundations/correctness-and-invariants.md) |
| [Heaps and Priority Queues](heaps-and-priority-queues.md) | Partial order: fast repeated access to the minimum | Arrays (implicit tree) |
| [Union–Find](union-find.md) | Dynamic partition: merge groups and test membership in O(α(n)) amortized | Arrays (parent forest), [amortized analysis](../01-foundations/amortized-analysis.md) |

```
                     operations needed
     exact-key lookup only ─────────► hash table          O(1) expected
     ordered / range queries ───────► balanced search tree O(log n)
     repeated min / max ────────────► binary heap          O(log n), O(1) peek
     last-in or first-in only ──────► stack / queue        O(1)
     index by position ─────────────► array                O(1)
     same group? / merge groups ────► union–find           O(α(n)) amortized
```

Read arrays and linked lists first: every other structure is built from one or both. Stacks and queues restrict the interface to get O(1) everything. Hash tables, search trees and heaps are three different answers to "how do I find things by key quickly?", differing in how much order they keep. Union–find answers a different question, "which group is this in?", and is read last because it combines the heap's array-stored tree with the amortized analysis that dynamic arrays introduced; its inverse-Ackermann bound is the most striking amortized result in the area.

## Connections to sibling areas

- **[Foundations](../01-foundations/README.md):** each structure is a representation invariant; dynamic arrays, hash tables and union–find need amortized analysis.
- **[Design Paradigms](../03-design-paradigms/README.md):** memoization tables in dynamic programming are hash tables or arrays; randomization gives universal hashing and treaps.
- **[Sorting and Searching](../04-sorting-and-searching/README.md):** heapsort is a heap; binary search is the static form of a search tree; sorting is equivalent to n inserts into a search tree.
- **[Graph Algorithms](../05-graph-algorithms/README.md):** Breadth-First Search (BFS) uses a queue, Depth-First Search (DFS) a stack, Dijkstra and Prim a priority queue, Kruskal a union–find structure, and graphs themselves are stored as arrays of lists.
- **[String Algorithms](../06-string-algorithms/README.md):** tries are search trees keyed by characters; Rabin–Karp is hashing applied to substrings.
- **[Advanced Topics](../07-advanced-topics/README.md):** B-trees and buffer trees are search trees redesigned for the I/O model; Bloom filters and sketches are lossy hash tables.

## Connections across layers

These structures assume [flat memory](../01-foundations/models-of-computation.md), but their real speed depends on the [cache hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md): arrays are fast because of spatial locality, pointer-based structures are slow because each hop risks a cache miss. Higher layers use them everywhere: [call stacks](../../06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) and [symbol tables](../../06-programming-languages/03-compilers/semantic-analysis.md) in compilers, [run queues](../../07-operating-systems/02-process-management/scheduling.md) and [page tables](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md) in kernels, [B-tree indexes](../../09-data-management/02-storage-and-indexing/b-trees.md) and hash joins in databases, [packet queues](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) in routers.

## Cross-cutting threads

- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): the layout decides which operations are cheap.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): order vs speed, worst case vs expected, memory vs time.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): heap order, search-tree order and balance rules.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): pointers and hashing both map names to locations.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): why arrays beat linked structures in practice.
