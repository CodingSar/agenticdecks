# Advanced Topics

> **Layer:** [05 Algorithms and Data Structures](../README.md) › Advanced Topics
> **Children:** [Approximation Algorithms](approximation-algorithms.md) · [Streaming and Online Algorithms](streaming-and-online-algorithms.md) · [External Memory and Cache-Oblivious Algorithms](external-memory-and-cache-oblivious.md) · [Computational Geometry](computational-geometry.md)

## What this area is about

The classical algorithms in this layer assume three things: the answer must be exact, the whole input is available up front, and memory is flat with unit-cost access. Real problems violate all three. Many important optimisation problems are NP-hard, so exact answers are out of reach at scale. Data often arrives as an unending stream, or requests must be served before the future is known. And data sets are larger than cache or Random-Access Memory (RAM), so the cost of moving data dominates the cost of computing on it. This area asks: *what can we still guarantee when we relax each assumption?* Geometry is here too, as the main family of algorithms over continuous space, where numeric precision becomes a correctness issue.

The unifying idea is **replacing an impossible guarantee with a measurable one**. Approximation algorithms prove "within a factor α of optimal." Online algorithms prove "within a factor c of the best offline algorithm" (competitive ratio). Streaming algorithms prove "within ε of the truth with probability 1 − δ, in polylogarithmic space." External-memory algorithms prove bounds in block transfers rather than instructions. Each child trades one ideal for a guarantee you can still state and prove.

## How the children fit together

| Child | Its role in the whole | Assumption relaxed |
|---|---|---|
| [Approximation Algorithms](approximation-algorithms.md) | Provably near-optimal answers to NP-hard problems in polynomial time | Exactness |
| [Streaming and Online Algorithms](streaming-and-online-algorithms.md) | Decide without seeing the future; summarise data in tiny space | Full input in advance; unlimited memory |
| [External Memory and Cache-Oblivious Algorithms](external-memory-and-cache-oblivious.md) | Minimise data movement between levels of the memory hierarchy | Flat, unit-cost memory |
| [Computational Geometry](computational-geometry.md) | Algorithms on points, lines and polygons; exactness under floating point | Discrete, exact data |

```
            classical algorithm: exact, offline, flat memory
             /                |                     \
    give up exactness   give up offline / space   give up flat memory
    approximation       online, streaming         external memory,
    ratio α             competitive ratio c,      cache-oblivious:
                        (ε, δ) sketches           count block transfers
```

The children are largely independent and can be read in any order. They share techniques: randomization appears in streaming sketches and in approximation by randomized rounding; online caching (paging) is the bridge between streaming/online and the memory hierarchy; geometric algorithms use sorting, sweep lines and divide and conquer, and their large-scale versions are external-memory problems.

## Connections to sibling areas

- **[Foundations](../01-foundations/README.md):** the I/O model and competitive analysis are new cost models alongside the RAM; amortized analysis proves the Least Recently Used (LRU) competitive ratio.
- **[Fundamental Data Structures](../02-fundamental-data-structures/README.md):** B-trees and buffer trees are search trees redesigned for blocks; Bloom filters and Count-Min sketches are lossy hash tables.
- **[Design Paradigms](../03-design-paradigms/README.md):** approximation uses greedy algorithms and Linear Programming (LP) rounding; streaming is randomized; cache-oblivious algorithms are divide and conquer.
- **[Sorting and Searching](../04-sorting-and-searching/README.md):** external merge sort is the canonical I/O algorithm; quantile sketches approximate selection in a stream.
- **[Graph Algorithms](../05-graph-algorithms/README.md):** vertex cover, Steiner tree and the travelling salesperson problem are classic approximation targets; massive graphs need semi-external and streaming algorithms.
- **[String Algorithms](../06-string-algorithms/README.md):** compressed indexes and suffix-array construction at scale are external-memory problems.

## Connections across layers

This area depends on [NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) (why approximation is needed), [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) (sketches), the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/README.md) and [storage devices](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) (I/O model), and [floating point](../../03-digital-logic/01-number-representation/floating-point.md) (geometric robustness). It feeds [page replacement](../../07-operating-systems/04-memory-management/page-replacement.md), [B-trees](../../09-data-management/02-storage-and-indexing/b-trees.md) and [Log-Structured Merge (LSM) trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md), [stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md), [Content Delivery Network (CDN) caching](../../08-networking/05-application-layer/content-delivery-and-caching.md), [graphics](../../14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) and [robotics planning](../../13-artificial-intelligence/01-classical-ai/search-and-planning.md).

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): inapproximability results, streaming space lower bounds, competitive-ratio lower bounds.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): online paging and I/O-efficient algorithms are the theory of caching.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): accuracy for space, optimality for time.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): moving whole blocks, buffering updates in buffer trees and LSM-trees.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): sketches are lossy encodings designed to answer specific queries.
