# Searching and Selection

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Sorting and Searching](README.md)
> **Builds on:** [Comparison Sorting](comparison-sorting.md), [Correctness and Invariants](../01-foundations/correctness-and-invariants.md), [Divide and Conquer](../03-design-paradigms/divide-and-conquer.md), [Randomized Algorithms](../03-design-paradigms/randomized-algorithms.md)
> **Enables:** [B-Trees](../../09-data-management/02-storage-and-indexing/b-trees.md), [IP Addressing and Forwarding](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md), [Debugging](../../12-software-engineering/03-quality/debugging.md), [Computational Geometry](../07-advanced-topics/computational-geometry.md)

## Essence

Searching asks "where is key x?" and selection asks "which item has rank k?" (the minimum, the median, the 99th percentile). On a sorted array, binary search answers the first in Θ(log n) comparisons by halving the candidate range each step, and that is optimal for comparison-based search. Selection looks as if it needs sorting first, Θ(n log n), but it does not: quickselect finds the k-th smallest in expected Θ(n), and the median-of-medians algorithm does it in worst-case Θ(n). Both ideas generalise far beyond arrays. Binary search works on any monotone predicate, and selection's "discard a constant fraction each round" is a template for linear-time algorithms.

## Core tenets

1. **Binary search is optimal for comparison-based search in a sorted array.** Each comparison with the middle element eliminates half of the remaining candidates, so ⌈log₂(n + 1)⌉ comparisons suffice. A decision tree with n + 1 possible outcomes (n positions plus "absent") has height at least log₂(n + 1), so no comparison algorithm does better. For n = 10⁹, that is 30 comparisons.

2. **Binary search is correct only if its invariant is exact.** State it as: "if x is present, it lies in A[lo..hi)" with half-open bounds. Then `mid = lo + (hi − lo)/2` (avoiding overflow), and the updates `lo = mid + 1` or `hi = mid` both preserve the invariant and strictly shrink the range. Writing the invariant first prevents the off-by-one errors and infinite loops that made Bentley observe that most programmers get binary search wrong.

3. **Binary search works on any monotone predicate, not just arrays.** If P(i) is false then true as i increases, binary search finds the boundary in O(log range) evaluations. This finds square roots, the smallest feasible capacity in an optimisation problem, the first bad commit in a version history (`git bisect`), and the right threshold in a tuning sweep. The array is incidental; monotonicity is the requirement.

4. **Using key values can beat log n on nice data.** Interpolation search guesses the position by linear interpolation between the endpoint values. On uniformly distributed keys it takes O(log log n) expected probes, but O(n) worst case on skewed data. Exponential (galloping) search finds the range first in O(log i) when the target is at index i, which helps with unbounded or nearly sorted data and is used inside Timsort's merges.

5. **Binary search on large arrays is limited by the memory hierarchy.** Each probe of a large sorted array touches a different cache line and early probes jump across pages, so a search of 10⁹ elements costs about 30 cache misses. The Eytzinger (breadth-first) layout stores the implicit search tree level by level so the next probes are near each other and can be prefetched; B-tree layouts pack many keys per cache line. Both can be several times faster than plain binary search, with the same Θ(log n) comparison count.

6. **Quickselect finds the k-th smallest in expected Θ(n).** Partition around a random pivot as in quicksort, then recurse into *only* the side containing rank k. Expected work is n + n/2 + n/4 + … with a constant-fraction shrink, which sums to O(n) (about 3.4n comparisons for the median). Worst case is Θ(n²), with the same pivot risk as quicksort.

7. **Median of medians guarantees worst-case linear selection.** Blum, Floyd, Pratt, Rivest and Tarjan (1973) choose a pivot by splitting the input into groups of 5, taking each group's median, and recursively selecting the median of those medians. That pivot is guaranteed to have at least about 3n/10 elements on each side, giving T(n) ≤ T(n/5) + T(7n/10) + O(n) = O(n), because 1/5 + 7/10 < 1. Its constant is large, so practical libraries use quickselect or introselect and fall back to it only when recursion degrades.

8. **Selection lower bounds are linear, and the minimum has an exact answer.** Finding the minimum needs exactly n − 1 comparisons: every non-minimum must lose at least once. Finding both the minimum and maximum needs only ⌈3n/2⌉ − 2 by comparing pairs first. Finding the median needs at least about 2n comparisons; the exact constant remains an open problem.

## Key concepts

| Term | Meaning |
|---|---|
| Binary search | Halve a sorted range by comparing with its middle element |
| Monotone predicate | A true/false test that switches value at most once along an ordered domain |
| Interpolation search | Probe at the position predicted by key values; O(log log n) on uniform data |
| Exponential (galloping) search | Double the step until overshooting, then binary search the bracket |
| Order statistic | The k-th smallest element; median is k = ⌈n/2⌉ |
| Quickselect | Partition-based selection recursing on one side; expected Θ(n) |
| Median of medians | Deterministic pivot choice guaranteeing worst-case Θ(n) selection |
| Eytzinger layout | Array order of a complete search tree stored breadth-first, for cache-friendly search |

## How it fits

- **Below:** correctness is an [invariant](../01-foundations/correctness-and-invariants.md) argument; selection is [divide and conquer](../03-design-paradigms/divide-and-conquer.md) that recurses on one side; practical speed is set by [caches and Translation Lookaside Buffers](../../04-computer-architecture/03-memory-hierarchy/cache-design.md).
- **Above:** [B-tree](../../09-data-management/02-storage-and-indexing/b-trees.md) node search, [longest-prefix match](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md) in routers, `git bisect` in [debugging](../../12-software-engineering/03-quality/debugging.md), percentile monitoring in [observability](../../12-software-engineering/04-operations/observability.md), and median-based splits in [k-d trees](../07-advanced-topics/computational-geometry.md).
- **Siblings:** depends on [comparison sorting](comparison-sorting.md) for sorted input and shares quicksort's partition; [search trees](../02-fundamental-data-structures/search-trees.md) are its dynamic form and [hash tables](../02-fundamental-data-structures/hash-tables.md) its unordered alternative.

## Common misconceptions

- **"To find the median you must sort."** Selection is Θ(n); sorting is Θ(n log n).
- **"Binary search is trivial."** It is short, but subtle bounds handling has caused bugs in widely used libraries for decades.
- **"Interpolation search is always better."** Its O(log log n) needs roughly uniform keys; adversarial or skewed data drives it to O(n).

## Go deeper

- Jon Bentley, *Programming Pearls* (2nd ed., 1999): column 4 on writing and verifying binary search.
- Manuel Blum, Robert Floyd, Vaughan Pratt, Ronald Rivest, Robert Tarjan, "Time Bounds for Selection" (1973): linear-time worst-case selection.
- Donald E. Knuth, *The Art of Computer Programming, Vol. 3* (2nd ed., 1998): section 6.2.1 on searching an ordered table.
