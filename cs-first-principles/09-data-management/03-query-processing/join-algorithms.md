# Join Algorithms

> **Layer:** [09 Data Management](../README.md) › [Query Processing](README.md)
> **Builds on:** [Relational Algebra and SQL](../01-data-models/relational-algebra-and-sql.md), [Storage Layouts](../02-storage-and-indexing/storage-layouts.md), [Hash Tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), [Comparison Sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md), [External Memory and Cache-Oblivious Algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md)
> **Enables:** [Query Optimization](query-optimization.md), [Batch and Stream Processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md), [Partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md)

## Essence

A join combines two relations by matching tuples on a condition, usually equality of keys. Defined as a Cartesian product followed by a selection, a join of two million-row tables would examine 10^12 pairs. Practical join algorithms avoid this by organising the inputs so that only tuples that can match meet each other. There are three families: *nested-loop* (for each outer tuple, find matches in the inner, ideally through an index), *sort-merge* (sort both inputs on the join key, then merge), and *hash* (build a hash table on the smaller input, probe it with the larger). Each wins in different conditions of input size, memory, available indexes and sortedness, which is why the optimizer must choose.

## Core tenets

1. **Cost is dominated by Input/Output (I/O) and by how often each input is read.** For relations R and S of M and N pages with B buffer pages available, the question is how many times each page must be read from storage. Naive nested-loop join reads S once per tuple of R; good algorithms read each input a small constant number of times. Central Processing Unit (CPU) cost matters too once data fits in memory.

2. **Nested-loop join is general but quadratic unless helped.** Simple tuple-at-a-time nested loops cost about M + (tuples in R) × N page reads. *Block* nested loops read a chunk of R that fills memory and scan S once per chunk: M + ⌈M/(B−2)⌉ × N. It alone handles arbitrary join conditions (inequalities, functions), and is fine when one side is tiny.

3. **Index nested-loop join turns the inner scan into lookups.** If S has an index on the join key, each outer tuple does a B-tree or hash lookup instead of scanning S. Cost ≈ M + (tuples in R) × (cost of one lookup). This is ideal when R is small or highly filtered, as in typical transactional queries ("this customer's orders"), and poor when R is large and lookups are random reads.

4. **Sort-merge join exploits order.** Sort both inputs on the join key (external merge sort takes about 2 passes over each input when memory is at least the square root of the input size), then scan both in step, emitting matches. Cost ≈ 3(M + N) I/Os if each sort needs one merge pass, less if inputs are already sorted (from an index or an earlier operator). Its output is sorted, which can satisfy a later ORDER BY or GROUP BY for free.

5. **Hash join partitions so that matches meet in memory.** In the simple case, build an in-memory hash table on the smaller input R and probe it with each tuple of S: cost M + N. If R does not fit in memory, *Grace hash join* first partitions both inputs with the same hash function into buckets written to disk; matching tuples must land in the same bucket pair, so each pair is then joined in memory. Cost ≈ 3(M + N). Hash join is usually the best choice for large equi-joins without useful order.

6. **Skew and memory estimates make or break hash joins.** If many tuples share one key, one partition is too big for memory and must be repartitioned recursively. If the optimizer underestimates the build side, the join spills unexpectedly. Hybrid hash join keeps one partition in memory to save I/O when memory is between the two extremes.

7. **Execution pipelines tuples between operators.** In the iterator (Volcano) model, each operator implements open/next/close and pulls tuples from its children, so a chain of selections, projections and probe-side hash joins streams data without writing intermediate results. Sorts and hash-table builds are *pipeline breakers*: they must consume all input before producing output. Modern engines pull batches of tuples (vectorisation) or compile pipelines into tight machine code to cut per-tuple overhead.

8. **Distributed joins add data movement.** When relations are partitioned across machines, a join requires matching keys to be co-located. Either both sides are repartitioned (shuffled) by join key, or the small side is broadcast to every machine. Network transfer then often dominates, which is why partitioning by commonly joined keys matters.

## Key concepts

| Term | Meaning |
|---|---|
| Equi-join | Join on equality of attributes; the common case |
| Outer / inner input | Driving relation / relation probed for matches |
| Block nested-loop join | Scan inner once per memory-sized block of outer |
| Index nested-loop join | Look up matches for each outer tuple via an index on inner |
| Sort-merge join | Sort both inputs on the key, then merge |
| Hash join | Build hash table on one input, probe with the other |
| Grace hash join | Partition both inputs by hash to disk, then join partition pairs |
| Pipeline breaker | Operator that must see all input before emitting output |
| Iterator model | Operators expose next() and pull tuples from children |
| Shuffle / broadcast join | Distributed join by repartitioning both sides / replicating the small side |

## How it fits

- **Below:** joins are the product-plus-select of [relational algebra](../01-data-models/relational-algebra-and-sql.md), implemented with [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) and [sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md) under the [external-memory model](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md); memory available comes from the buffer pool in [storage layouts](../02-storage-and-indexing/storage-layouts.md).
- **Above:** [query optimization](query-optimization.md) chooses among these algorithms; MapReduce-style and Structured Query Language (SQL)-on-cluster engines for [batch and stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) are distributed sort-merge and hash joins; [partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) decides how much data must be shuffled.
- **Siblings:** [query optimization](query-optimization.md) needs these cost formulas to compare plans.

## Common misconceptions

- **"Hash join is always fastest."** Index nested-loop wins when the outer side is small; sort-merge wins when inputs are already sorted or output order is needed.
- **"Joins require loading both tables into memory."** Grace hash join and external sort-merge work with memory far smaller than the inputs.
- **"The join order does not matter if the algorithm is good."** Intermediate result sizes can differ by many orders of magnitude between orders; that choice usually dominates.

## Go deeper

- L. D. Shapiro, *Join Processing in Database Systems with Large Main Memories* (ACM TODS, 1986): hybrid hash join and cost analysis.
- G. Graefe, *Query Evaluation Techniques for Large Databases* (ACM Computing Surveys, 1993): the comprehensive survey of operators.
- G. Graefe, *Volcano: An Extensible and Parallel Query Evaluation System* (1994): the iterator model.
