# Sorting and Searching

> **Layer:** [05 Algorithms and Data Structures](../README.md) › Sorting and Searching
> **Children:** [Comparison Sorting](comparison-sorting.md) · [Non-Comparison Sorting](non-comparison-sorting.md) · [Searching and Selection](searching-and-selection.md)

## What this area is about

Sorting puts n items in order; searching finds an item or a rank in a collection. They are the most studied problems in algorithms because nearly everything else uses them: sorted data makes search logarithmic, duplicates adjacent, merges linear and ranges contiguous. Knuth reported that computer manufacturers in the 1960s estimated over a quarter of all computer time went to sorting. This area is also where theory first gives *tight* answers: we know matching upper and lower bounds, so we know exactly how hard these problems are in each model.

The unifying idea is **information**. A comparison yields at most one bit about the input. Sorting must identify one of n! orderings, which needs log₂(n!) ≈ n log₂ n bits, hence Ω(n log n) comparisons. Searching a sorted list must identify one of n + 1 positions, hence Ω(log n). Algorithms that beat these bounds do so by extracting more than one bit per step, by looking at key digits (radix sort) or computing addresses (hashing), which is a change of model, not a refutation.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Comparison Sorting](comparison-sorting.md) | Merge sort, quicksort, heapsort; the Ω(n log n) lower bound | [Divide and conquer](../03-design-paradigms/divide-and-conquer.md), [heaps](../02-fundamental-data-structures/heaps-and-priority-queues.md), [randomization](../03-design-paradigms/randomized-algorithms.md) |
| [Non-Comparison Sorting](non-comparison-sorting.md) | Counting, radix and bucket sort: linear time by using key structure | Comparison sorting (to see what it escapes), [word Random Access Machine (RAM)](../01-foundations/models-of-computation.md) |
| [Searching and Selection](searching-and-selection.md) | Binary search, interpolation search, selection of the k-th smallest in linear time | Sorting, [search trees](../02-fundamental-data-structures/search-trees.md), randomization |

```
          information lower bound: log2(n!) ~ n log n comparisons
                         |
      comparison sorting ---- matches it (merge, heap, quick)
                         |
   non-comparison sorting ---- escapes it by reading key digits: O(n + k), O(d(n + b))
                         |
   searching / selection ---- log n for search; linear time for the k-th element
```

Read comparison sorting first: it introduces the decision-tree argument that the other two children reuse or escape. Non-comparison sorting shows what changes when keys are small integers or strings. Searching and selection show that some problems that seem to need sorting (finding the median) do not.

## Connections to sibling areas

- **[Foundations](../01-foundations/README.md):** the comparison model and decision-tree lower bounds are defined there; invariants prove partition and binary search correct.
- **[Fundamental Data Structures](../02-fundamental-data-structures/README.md):** heapsort uses a heap; binary search on a sorted array is a static search tree; hash tables replace search when order is not needed.
- **[Design Paradigms](../03-design-paradigms/README.md):** merge sort and quicksort are the textbook examples of divide and conquer; randomized pivots make quicksort and quickselect robust.
- **[Graph Algorithms](../05-graph-algorithms/README.md):** Kruskal's algorithm starts by sorting edges; topological sort orders vertices of a Directed Acyclic Graph (DAG).
- **[String Algorithms](../06-string-algorithms/README.md):** suffix arrays are built by sorting suffixes, often with radix sort.
- **[Advanced Topics](../07-advanced-topics/README.md):** external merge sort is the canonical I/O-model algorithm; sorting is the first step of many geometric algorithms (convex hull, sweep line).

## Connections across layers

Sorting is shaped by hardware: [cache behaviour](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) favours quicksort's sequential partitioning over heapsort's jumps, [branch mispredictions](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) make branchless partitioning faster, and [Single Instruction, Multiple Data (SIMD)](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) sorting networks speed small sorts. Above, databases use [sort-merge joins](../../09-data-management/03-query-processing/join-algorithms.md) and sorted [indexes](../../09-data-management/02-storage-and-indexing/b-trees.md), [MapReduce](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) is built around a distributed sort ("shuffle"), and [Log-Structured Merge (LSM) trees](../../09-data-management/02-storage-and-indexing/lsm-trees.md) are sorted runs merged in the background.

## Cross-cutting threads

- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): the Ω(n log n) comparison bound and the Ω(log n) search bound.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): radix sort wins by exploiting how keys are encoded.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): partition invariants and binary search's bracket invariant.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): why quicksort usually beats heapsort despite equal bounds.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): stability, in-place operation and worst-case guarantees cannot all be had cheaply.
