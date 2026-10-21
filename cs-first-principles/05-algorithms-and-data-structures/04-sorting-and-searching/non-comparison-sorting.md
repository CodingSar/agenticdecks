# Non-Comparison Sorting

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Sorting and Searching](README.md)
> **Builds on:** [Comparison Sorting](comparison-sorting.md), [Models of Computation](../01-foundations/models-of-computation.md), [Binary and Positional Notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md), [Integers and Two's Complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md)
> **Enables:** [Tries and Suffix Structures](../06-string-algorithms/tries-and-suffix-structures.md), [SIMD and GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md), [Join Algorithms](../../09-data-management/03-query-processing/join-algorithms.md)

## Essence

Comparison sorts cannot do better than Ω(n log n) because each comparison yields one bit. If keys are integers, strings or anything with a fixed-width digit representation, you can learn far more per step by using a key's digits as an *array index*. Counting sort places each key directly into its slot in O(n + k) time for keys in a range of size k. Radix sort applies a stable counting sort digit by digit, sorting n keys of d digits in base b in O(d(n + b)) time, which is linear in the total input size. Bucket sort distributes keys into ranges and is linear in expectation for uniformly distributed inputs. These algorithms are faster when keys fit their assumptions and useless or slower when they do not.

## Core tenets

1. **Indexing by key extracts log k bits per step.** A comparison distinguishes two outcomes. Using a key as an array index distinguishes k outcomes in one memory access. That is the whole trick, and it is why these algorithms sit outside the decision-tree lower bound: they are not comparison algorithms, so the bound does not apply.

2. **Counting sort is O(n + k) and stable.** Count occurrences of each key value in an array of size k, compute prefix sums so count[v] is the number of keys less than v, then scan the input and place each item at its computed position, incrementing as you go. Scanning the input in order makes it *stable*. It is linear when k = O(n) and terrible when k is huge (sorting ten 64-bit numbers with k = 2⁶⁴ is impossible).

3. **Radix sort splits big keys into small digits.** Least-significant-digit (LSD) radix sort runs a stable counting sort on the lowest digit, then the next, up to the highest. Stability is essential: after pass i, keys are sorted by their lowest i digits, and the next stable pass preserves that order among keys with equal higher digits. With d digits of base b: O(d(n + b)). Sorting n 32-bit integers with b = 2⁸ = 256 needs 4 passes over the data.

4. **Choosing the radix balances passes against table size.** For w-bit keys and radix 2ʳ, there are w/r passes, each O(n + 2ʳ). Choosing r ≈ log₂ n gives O(n · w / log n), which beats n log n whenever w = O(log n) words (keys that fit in a machine word for practical n). In practice r is chosen so the count table (2⁸ to 2¹⁶ entries) fits in L1 or L2 cache, because each pass scatters writes across 2ʳ output positions.

5. **Most-significant-digit (MSD) radix sort handles strings and variable lengths.** Partition on the first character into buckets, then recurse into each bucket on the next character. It inspects only as many characters as needed to distinguish keys, so it is fast for strings with distinct prefixes. It is the idea behind tries and the [suffix array](../06-string-algorithms/tries-and-suffix-structures.md) construction algorithms, and behind American flag sort (in-place MSD).

6. **Bucket sort is linear in expectation for uniform data.** For n keys uniform in [0, 1), divide the range into n equal buckets, put each key in its bucket, sort buckets with insertion sort, and concatenate. Expected bucket size is O(1), so expected time is O(n). For skewed data many keys land in one bucket and the bound collapses to the inner sort's cost. Sample sort, which picks bucket boundaries from a random sample, adapts this idea to unknown distributions and to parallel machines.

7. **Non-integer keys can often be mapped to integers that sort correctly.** Signed two's-complement integers sort correctly after flipping the sign bit. Institute of Electrical and Electronics Engineers (IEEE) 754 floating-point numbers sort as unsigned integers after flipping the sign bit of positives and all bits of negatives. Strings sort by their byte sequences under binary collation.

8. **In practice the theory-practice gap runs both ways.** Radix sort's passes stream through memory and parallelise well, so it is the standard sort on Graphics Processing Units (GPUs) and in many database engines for fixed-width keys. On a single core with large keys or small n, a well-tuned comparison sort often wins, because radix sort's scattered writes cause cache and Translation Lookaside Buffer (TLB) misses, and its passes touch every key even when keys are already distinguished by their top bits.

## Key concepts

| Term | Meaning |
|---|---|
| Counting sort | Count key frequencies, prefix-sum to positions, place items; O(n + k) |
| Radix (base) b | Number of distinct digit values per pass |
| LSD radix sort | Stable passes from least to most significant digit |
| MSD radix sort | Recursive partitioning from most significant digit; suits strings |
| Bucket sort | Distribute by value range into buckets; expected O(n) on uniform data |
| Prefix sum | Running total that converts counts into output positions |
| Stability | Equal keys keep input order; required for LSD correctness |
| Key transformation | Mapping keys (floats, signed ints) to unsigned integers with the same order |

## How it fits

- **Below:** depends on keys having a [positional representation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md) with fixed-width digits, on [two's complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md) and [floating-point](../../03-digital-logic/01-number-representation/floating-point.md) bit layouts, and on the [word RAM](../01-foundations/models-of-computation.md) model.
- **Above:** [GPU](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) sorting libraries, [hash and radix partitioning](../../09-data-management/03-query-processing/join-algorithms.md) in database joins, [suffix array](../06-string-algorithms/tries-and-suffix-structures.md) construction, and [batch-processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) shuffles that partition by key range.
- **Siblings:** [comparison sorting](comparison-sorting.md) is general but bounded by n log n; [searching](searching-and-selection.md) has an analogue in interpolation search, which also uses key values rather than just comparisons.

## Common misconceptions

- **"Radix sort is always faster because it is linear."** It is O(d·n); with long keys d can exceed log n, and its memory pattern is less cache-friendly.
- **"Counting sort works for any integers."** Its O(k) table makes it impractical when the key range is much larger than n.
- **"LSD radix sort works with any per-digit sort."** Each pass must be stable, or earlier passes' work is destroyed.

## Go deeper

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): sorting in linear time chapter.
- Robert Sedgewick and Kevin Wayne, *Algorithms* (4th ed., 2011): string sorts chapter on LSD and MSD radix sort.
- Peter M. McIlroy, Keith Bostic, M. Douglas McIlroy, "Engineering Radix Sort" (1993): practical MSD radix sorting of strings.
