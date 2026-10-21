# Query Processing

> **Layer:** [09 Data Management](../README.md) › Query Processing
> **Children:** [Join Algorithms](join-algorithms.md) · [Query Optimization](query-optimization.md)

## What this area is about

A declarative query says what result is wanted. Query processing turns it into a program that computes that result efficiently over the actual storage. The gap is large: the same SQL (Structured Query Language) query can run in milliseconds or in days depending on the order of joins, the algorithms chosen and the indexes used. Closing that gap automatically, without the user's help, is the central achievement of database systems and the reason declarative querying is practical.

The unifying idea is *plans as trees of physical operators, chosen by estimated cost*. A query is parsed into a relational algebra tree, rewritten using algebraic equivalences, and then mapped to physical operators (index scan, hash join, sort) whose costs depend on input sizes. The optimizer searches the space of equivalent plans and picks the one with the lowest estimated cost. The executor then runs it, usually by pulling tuples (or batches of tuples) through the operator tree.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Join Algorithms](join-algorithms.md) | The physical operators for the most expensive and most common operation: nested-loop, sort-merge and hash joins, and their costs | Storage layouts, sorting, hashing |
| [Query Optimization](query-optimization.md) | Rewrites queries, estimates sizes, enumerates join orders and picks a plan | Relational algebra, join costs, statistics |

```
 SQL text --parse--> logical plan (algebra tree)
          --rewrite (push selections, unnest)--> better logical plan
          --enumerate + cost (join order, access paths, algorithms)--> physical plan
          --execute (iterators / vectorised batches)--> result rows
```

Read join algorithms first: the optimizer's choices only make sense once you know what each operator costs and when it wins. Query optimization then shows how those costs, combined with cardinality estimates and a search over join orders, produce a plan.

## Connections to sibling areas

- **[Data Models](../01-data-models/README.md):** relational algebra's equivalence laws are the optimizer's rewrite rules; the declarative model is what gives the optimizer freedom.
- **[Storage and Indexing](../02-storage-and-indexing/README.md):** access paths (full scans, B-tree range scans, index lookups) are the leaves of every plan; buffer pool size decides whether a join fits in memory; column stores change which operators are cheap.
- **[Transactions](../04-transactions/README.md):** a running plan reads under some isolation level; long analytical queries and short transactions compete for locks or versions, which motivates multiversion concurrency control.

## Connections across layers

Join algorithms are [sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md) and [hashing](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) under the [external-memory model](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md); join-order search uses [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md); query compilation borrows from [compiler optimisation](../../06-programming-languages/03-compilers/optimization.md) and [JIT compilation](../../06-programming-languages/04-runtime-systems/jit-compilation.md). Above, distributed engines for [batch and stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) use the same operators plus data shuffling, and [partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) determines which joins can run locally.

## Cross-cutting threads

- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): one declarative query, many physical plans.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): memory vs I/O in joins; optimisation time vs plan quality.
- [Composition](../../CROSS-CUTTING.md#composition): operators compose as iterators into pipelines.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): tuples stream between operators without materialisation; partitions run in parallel.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): vectorised execution amortises per-tuple overhead.
