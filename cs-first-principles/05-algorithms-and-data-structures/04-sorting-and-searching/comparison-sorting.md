# Comparison Sorting

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Sorting and Searching](README.md)
> **Builds on:** [Divide and Conquer](../03-design-paradigms/divide-and-conquer.md), [Heaps and Priority Queues](../02-fundamental-data-structures/heaps-and-priority-queues.md), [Randomized Algorithms](../03-design-paradigms/randomized-algorithms.md), [Combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md)
> **Enables:** [Searching and Selection](searching-and-selection.md), [Join Algorithms](../../09-data-management/03-query-processing/join-algorithms.md), [External Memory and Cache-Oblivious Algorithms](../07-advanced-topics/external-memory-and-cache-oblivious.md), [Computational Geometry](../07-advanced-topics/computational-geometry.md)

## Essence

A comparison sort orders n items using only a "less than" test between pairs, so it works for any type with a total order: numbers, strings, dates, tuples. The fundamental fact is a lower bound: every comparison sort needs Ω(n log n) comparisons in the worst case, because it must distinguish all n! possible input orders and each comparison has only two outcomes. Merge sort, heapsort and (in expectation) quicksort meet this bound, so they are asymptotically optimal. The differences that matter in practice are constants, memory use, stability, adaptivity to presorted input, and cache behaviour, which is why real libraries use hybrids such as introsort, pdqsort and Timsort.

## Core tenets

1. **Any comparison sort needs at least log₂(n!) = Θ(n log n) comparisons in the worst case.** Model the algorithm as a binary decision tree: each internal node is a comparison, each leaf an output permutation. A correct sort needs at least n! reachable leaves, and a binary tree of height h has at most 2ʰ leaves, so h ≥ log₂(n!). By Stirling's approximation, log₂(n!) = n log₂ n − n log₂ e + O(log n) ≈ n log₂ n − 1.44n. The same bound holds for the *average* number of comparisons over random permutations.

2. **Merge sort is optimal, stable and predictable, at the cost of extra memory.** Split in half, sort each half recursively, merge in linear time: T(n) = 2T(n/2) + Θ(n) = Θ(n log n) in every case, with at most n⌈log₂ n⌉ comparisons. Merging is a sequential scan of two inputs, so it suits linked lists, external storage and parallel execution. Its standard array form needs Θ(n) extra space.

3. **Quicksort is fastest in practice because partitioning is cheap and local.** Pick a pivot, partition so smaller items come first and larger after, recurse on both sides. With random (or median-of-three) pivots it averages about 1.39 n log₂ n comparisons, slightly more than merge sort, but each step is a tight loop over contiguous memory with no extra array, so it usually wins by a constant factor. Its invariant during Lomuto or Hoare partitioning is that the scanned prefix is split into "≤ pivot" and "≥ pivot" regions.

4. **Quicksort's worst case is Θ(n²), and must be guarded against.** Bad pivots (the minimum each time, as with naive first-element pivots on sorted data) give splits of 0 and n − 1. Random pivots make this astronomically unlikely for any input; introsort (Musser, 1997) caps recursion depth at about 2 log₂ n and switches to heapsort, guaranteeing O(n log n). Many equal keys also hurt two-way partitioning; three-way partitioning (Dijkstra's Dutch national flag) handles them in linear time.

5. **Heapsort gives O(n log n) worst case in place, but loses on hardware.** It builds a heap in O(n), then extracts n maxima at O(log n) each, using O(1) extra memory. It is not stable, and sift-down jumps between index i and 2i, which defeats caches and prefetchers on large arrays. It is the safety net in introsort rather than a primary sort.

6. **Simple quadratic sorts win on tiny or nearly sorted inputs.** Insertion sort costs Θ(n + I), where I is the number of inversions (out-of-order pairs). On nearly sorted data I is small, and on arrays of under about 16–32 elements its low overhead beats any recursive method. Every serious library uses it for small subarrays.

7. **Stability and adaptivity are features, not details.** A stable sort keeps equal keys in their original order, which lets you sort by multiple keys in successive passes (sort by name, then stably by department). Merge sort and insertion sort are stable; quicksort and heapsort are not. Timsort (Tim Peters, 2002; used in Python and for objects in Java) finds existing sorted runs and merges them, so it is O(n) on sorted input and O(n log n) worst case.

8. **On real hardware, memory traffic and branch prediction rival comparison counts.** A random pivot comparison is a coin-flip branch, so roughly half are mispredicted, each costing ~10–20 cycles. Branchless partitioning (BlockQuicksort, pdqsort) and sorting networks in Single Instruction, Multiple Data (SIMD) registers trade extra instructions for fewer mispredictions and can be twice as fast. Parallel sorts and Graphics Processing Unit (GPU) sorts often prefer merge-based or radix-based designs because they partition work evenly.

## Key concepts

| Term | Meaning |
|---|---|
| Comparison model | Algorithm learns about keys only by comparing pairs |
| Decision tree | Binary tree of comparisons whose leaves are output orders |
| Inversion | Pair i < j with A[i] > A[j]; zero for sorted, n(n−1)/2 for reversed input |
| Stable sort | Equal keys keep their input order |
| In-place sort | Uses O(1) (or O(log n)) extra memory beyond the input |
| Partition | Rearranging around a pivot so smaller elements precede larger |
| Introsort | Quicksort that falls back to heapsort when recursion is too deep |
| Timsort | Adaptive, stable merge sort that exploits existing runs |

## How it fits

- **Below:** the lower bound counts permutations with [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md) and needs a [total order](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md); practical speed depends on [caches](../../04-computer-architecture/03-memory-hierarchy/cache-design.md) and [branch prediction](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md).
- **Above:** [sort-merge joins](../../09-data-management/03-query-processing/join-algorithms.md), `ORDER BY` and index builds in databases; the shuffle phase of [batch processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md); [external merge sort](../07-advanced-topics/external-memory-and-cache-oblivious.md); sorted input for [binary search](searching-and-selection.md), sweep-line [geometry](../07-advanced-topics/computational-geometry.md) and Kruskal's [Minimum Spanning Tree (MST)](../05-graph-algorithms/minimum-spanning-trees.md) algorithm.
- **Siblings:** [non-comparison sorting](non-comparison-sorting.md) escapes the lower bound by reading key digits; [selection](searching-and-selection.md) shows that finding one order statistic needs only Θ(n).

## Common misconceptions

- **"Quicksort is O(n log n)."** It is O(n log n) *expected* with random pivots; worst case is Θ(n²) unless guarded by introsort or a linear-time pivot.
- **"Radix sort beats the n log n lower bound."** The bound applies only to comparison sorts; radix sort uses a different model.
- **"Fewer comparisons means faster."** Merge sort makes fewer comparisons than quicksort but is usually slower in memory because of copying and the extra array.

## Go deeper

- Donald E. Knuth, *The Art of Computer Programming, Vol. 3: Sorting and Searching* (2nd ed., 1998): the definitive analysis of sorting.
- C. A. R. Hoare, "Quicksort" (1962): the original paper.
- Robert Sedgewick and Kevin Wayne, *Algorithms* (4th ed., 2011): practical engineering of quicksort and merge sort.
- David R. Musser, "Introspective Sorting and Selection Algorithms" (1997): introsort.
