# External Memory and Cache-Oblivious Algorithms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Advanced Topics](README.md)
> **Builds on:** [Models of Computation](../01-foundations/models-of-computation.md), [Locality and Caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [DRAM and Storage Devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md), [Divide and Conquer](../03-design-paradigms/divide-and-conquer.md)
> **Enables:** [B-Trees](../../09-data-management/02-storage-and-indexing/b-trees.md), [LSM-Trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), [Join Algorithms](../../09-data-management/03-query-processing/join-algorithms.md), [File System Implementation](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md), [Training at Scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md)

## Essence

The Random Access Machine (RAM) model charges one unit for any memory access, but real memory is a hierarchy in which each level is larger and slower than the one above and moves data in blocks: ~1 ns for an L1 cache hit, ~100 ns for Dynamic Random-Access Memory (DRAM), ~10–100 µs for a Solid-State Drive (SSD) read, ~5–10 ms for a disk seek (circa 2020s hardware). When data exceeds a level, the number of block transfers, not the number of instructions, decides running time. The external-memory (I/O) model makes this explicit: fast memory of M words, slow memory read and written in blocks of B words, cost = number of block transfers. Cache-oblivious algorithms go further: they achieve optimal transfer counts for *every* level of the hierarchy at once, without knowing M or B, typically by recursive divide and conquer.

## Core tenets

1. **Cost is block transfers, so contiguity is worth a factor of B.** Scanning n contiguous items costs Θ(n/B) transfers, written scan(n). Visiting n items scattered randomly costs up to n transfers. With B = 8 words per 64-byte cache line, or thousands per disk page, this separates algorithms that run at memory bandwidth from ones a hundred times slower.

2. **Searching costs Θ(log_B n), which is why B-trees exist.** A binary search tree of n keys has height log₂ n, and each level may be a separate transfer. A B-tree with fan-out Θ(B) has height log_B n: for a billion keys with fan-out 500, about 4 levels instead of 30, and the top levels stay cached, so a lookup costs one or two disk reads. This is optimal for comparison-based search in the I/O model, hence B-trees in every database.

3. **Sorting costs Θ((n/B) log_{M/B}(n/B)), and multiway merge sort achieves it.** Form sorted runs of size M in memory, then merge M/B runs at a time, keeping one block of each run in memory. Each merge pass reads and writes everything once (2n/B transfers), and there are log_{M/B}(n/M) passes. With realistic M/B in the thousands, a terabyte sorts in two or three passes. Aggarwal and Vitter (1988) proved this bound is optimal, and many problems (permuting, list ranking, graph problems) are bounded by the sorting cost rather than by scanning.

4. **Permuting is as hard as sorting in external memory.** In RAM, rearranging items into a given order is O(n): just copy each item to its destination. In the I/O model, scattered writes cost a transfer each, so permuting costs Θ(min(n, sort(n))). This is a clean example of where the RAM model's intuition is wrong.

5. **Buffering trades latency for throughput on updates.** A B-tree insert costs O(log_B n) transfers, far more than the O(1/B) amortized cost of appending to a log. Buffer trees and Log-Structured Merge (LSM) trees batch updates in memory and push them down in large sorted chunks, achieving roughly O((1/B) log_{M/B}(n/B)) amortized transfers per insert, at the cost of slower or more complex reads. The Bε-tree interpolates between the two designs with a tunable parameter.

6. **Cache-oblivious algorithms are optimal at every level without tuning.** In the ideal-cache model (Frigo, Leiserson, Prokop and Ramachandran, 1999), an algorithm is analysed as if it had a cache of size M with blocks of size B, but it may not use M or B in its code. Recursive divide and conquer achieves this naturally: subproblems shrink until one fits in cache, and from then on all its work is cache-resident. Because the analysis holds for every (M, B), it holds simultaneously for L1, L2, L3, DRAM pages and disk. Examples: recursive matrix multiplication and transposition, funnelsort (optimal sorting), and the van Emde Boas layout for static search trees (O(log_B n) search).

7. **Real code exploits the hierarchy explicitly, with large constant-factor gains.** Tiling a matrix multiply so each tile fits in cache turns memory-bound work into compute-bound work; it is why tuned Basic Linear Algebra Subprograms (BLAS) libraries are ten or more times faster than the naive triple loop. Graphics Processing Unit (GPU) attention kernels such as FlashAttention compute in tiles held in on-chip memory for the same reason.

8. **Theory and practice diverge on prefetching, parallelism and device quirks.** The I/O model ignores hardware prefetching of sequential access, SSD internal parallelism, flash writes costing more than reads, and Translation Lookaside Buffer (TLB) misses. Cache-oblivious algorithms often lose to well-tuned cache-aware ones by a constant factor. The model gets the dominant term right; engineering supplies the rest.

## Key concepts

| Term | Meaning |
|---|---|
| I/O (external-memory) model | Cost = block transfers between fast memory of size M and slow memory in blocks of size B |
| scan(n) | Θ(n/B): cost of reading n contiguous items |
| sort(n) | Θ((n/B) log_{M/B}(n/B)): I/O cost of sorting |
| B-tree | Search tree with fan-out Θ(B); O(log_B n) I/Os per search |
| Buffer tree / LSM-tree | Structures that batch updates to amortize block transfers |
| Ideal-cache model | I/O model with optimal replacement where the algorithm does not know M or B |
| Cache-oblivious | Asymptotically optimal I/O cost for all M and B without tuning |

## How it fits

- **Below:** the model abstracts the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [cache design](../../04-computer-architecture/03-memory-hierarchy/cache-design.md) and [storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md); it refines the RAM in [models of computation](../01-foundations/models-of-computation.md).
- **Above:** [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md), [LSM-trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), [columnar layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md) and external sort-merge and hash [joins](../../09-data-management/03-query-processing/join-algorithms.md) in databases; [file-system](../../07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) layout; [compiler loop tiling](../../06-programming-languages/03-compilers/optimization.md); [batch-processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) shuffles; memory-aware kernels in [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md).
- **Siblings:** online [paging](streaming-and-online-algorithms.md) justifies assuming a near-optimal cache (Least Recently Used (LRU) replacement with twice the memory is within a factor 2 of optimal); [streaming algorithms](streaming-and-online-algorithms.md) are the extreme case of one sequential pass with tiny memory.

## Common misconceptions

- **"An O(n) algorithm is linear-time on big data."** If it makes random accesses it can cost n block transfers, slower than an O(n log n) algorithm that scans.
- **"Cache-oblivious means cache-unaware."** It means the code does not *mention* cache parameters, yet it is designed so its locality is optimal at every level.
- **"SSDs made the I/O model obsolete."** SSDs shrink the gap from ~10⁵ to ~10³ relative to DRAM, but block granularity and the cost of random writes remain.

## Go deeper

- Alok Aggarwal and Jeffrey S. Vitter, "The Input/Output Complexity of Sorting and Related Problems" (1988): the model and its sorting bound.
- Jeffrey S. Vitter, *Algorithms and Data Structures for External Memory* (2008): survey of the field.
- Matteo Frigo, Charles E. Leiserson, Harald Prokop, Sridhar Ramachandran, "Cache-Oblivious Algorithms" (1999).
