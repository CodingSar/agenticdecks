# Combinatorics

> **Layer:** [01 Mathematical Foundations](../README.md) › [Discrete Mathematics](README.md)
> **Builds on:** [Sets](../02-sets-relations-functions/sets.md), [Functions and Cardinality](../02-sets-relations-functions/functions-and-cardinality.md)
> **Enables:** [Asymptotic Analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [Probability](../06-probability-and-statistics/probability.md), [Comparison Sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md), [Hash Tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), [Hash Functions and MACs](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md)

## Essence

Combinatorics is the mathematics of counting finite structures: how many ways to arrange, choose or distribute things under constraints. Computer scientists count constantly, because the size of a search space is the running time of brute force, the number of possible keys is the security of a cipher, and the number of possible inputs bounds what any algorithm can distinguish. A few rules (sum, product, bijection, inclusion–exclusion, pigeonhole) combined with a few standard counts (permutations, combinations, binomial coefficients) cover most cases. The deepest use of counting in Computer Science (CS) is negative: if there are more cases than an algorithm can tell apart, the algorithm must be slow or wrong on some of them.

## Core tenets

1. **The product rule makes search spaces explode.** If a choice has *a* options followed by an independent choice with *b* options, there are *a·b* outcomes. So *n* binary choices give 2^n configurations, and *k* characters from an alphabet of 62 give 62^k passwords. Exponential growth from repeated independent choices is why brute-force search fails beyond small *n*, and why adding a bit to a key doubles the attacker's work.

2. **The sum rule and bijections count by splitting or by translating.** Disjoint cases add. When a set is hard to count directly, find a bijection to one that is easy: subsets of an *n*-set correspond to *n*-bit strings, so there are 2^n of them. Most clever counting is finding the right bijection.

3. **Permutations and combinations count orderings and selections.** There are n! orderings of *n* distinct items and C(n, k) = n! / (k!(n−k)!) ways to choose *k* of them when order does not matter. These numbers grow fast: 20! ≈ 2.4 × 10^18, which is why trying every route for a 20-city travelling-salesman instance is hopeless, and why C(n, 2) = n(n−1)/2 is the number of pairs an all-pairs comparison must touch.

4. **Counting gives lower bounds on algorithms.** A comparison sort must distinguish all n! input orders, and each comparison has two outcomes, so it needs at least log₂(n!) ≈ n log₂ n − 1.44n comparisons in the worst case. This is the classic information-theoretic bound behind [comparison sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md). The same argument shows a lossless compressor cannot shrink every input.

5. **Inclusion–exclusion corrects for overlap.** |A ∪ B ∪ C| = |A| + |B| + |C| − |A∩B| − |A∩C| − |B∩C| + |A∩B∩C|. It counts objects that avoid all of several bad properties, such as derangements (permutations with no fixed point, about n!/e of them). Its first term alone gives an upper bound, the union bound, which is the most used inequality in randomized algorithm analysis.

6. **Pigeonhole and the birthday bound force collisions.** With more items than boxes, two share a box. With *m* equally likely boxes, a collision becomes likely (probability about 1/2) after only about 1.18·√m random items. So a 64-bit random identifier collides after about 2^32 random draws, not 2^64, and a hash with *n*-bit output offers only about *n*/2 bits of collision resistance. This is why [cryptographic hashes](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md) use 256-bit outputs and why [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) must handle collisions from the start.

7. **Binomial coefficients and their estimates connect counting to probability and entropy.** (x + y)^n expands with C(n, k) as coefficients, and the number of *n*-bit strings with *k* ones is C(n, k) ≈ 2^(n·H(k/n)), where H is the binary entropy function. This is the bridge from counting to [entropy](../../02-theory-of-computation/01-information-theory/entropy-and-information.md): the information in a typical message is the logarithm of how many such messages there are. Stirling's approximation n! ≈ √(2πn)(n/e)^n makes these estimates usable.

8. **Generating functions and recurrences count recursively defined structures.** The number of binary trees with *n* nodes (the Catalan number C(2n, n)/(n+1)) or of tilings and parses satisfies a recurrence. Encoding the sequence as the coefficients of a power series turns the recurrence into algebra. This links counting to [recurrences](induction-and-recurrences.md) and to the analysis of recursive algorithms.

## Key concepts

| Term | Meaning |
|---|---|
| Product rule | Independent sequential choices multiply |
| Sum rule | Disjoint alternatives add |
| Permutation | An ordering; n! of n items, n!/(n−k)! of length k |
| Combination | An unordered selection; C(n, k) = n!/(k!(n−k)!) |
| Binomial theorem | (x+y)^n = Σ C(n,k) x^k y^(n−k) |
| Inclusion–exclusion | Alternating sum that counts unions exactly |
| Pigeonhole principle | n+1 objects in n boxes forces a shared box |
| Birthday bound | Collisions likely after about √m draws from m values |
| Stirling's approximation | n! ≈ √(2πn)(n/e)^n; log₂ n! ≈ n log₂ n − 1.44n |
| Catalan numbers | Count binary trees, balanced parentheses, and many parse structures |

## How it fits

- **Below:** Counting is the theory of [cardinality](../02-sets-relations-functions/functions-and-cardinality.md) for finite sets; bijections and products come from [sets](../02-sets-relations-functions/sets.md).
- **Above:** [Probability](../06-probability-and-statistics/probability.md) on finite, equally likely outcomes is counting divided by counting. [Asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md) estimates counts of steps. Lower bounds, collision analysis in [hash tables](../../05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md), key-space sizes in [cryptography](../../11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) and search-space sizes in [backtracking](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md) are all counts.
- **Siblings:** [Recurrences](induction-and-recurrences.md) count recursively; [graph theory](graph-theory.md) counts paths, matchings and trees; [number theory](number-theory.md) supplies modular arithmetic used in counting with symmetry.

## Common misconceptions

- **"A 64-bit random identifier will never collide."** It is expected to collide around 2^32 IDs, a number large systems do reach.
- **"Doubling the input doubles brute-force time."** For exponential search spaces, adding one element can double the time; doubling the input squares it.
- **"Lower bounds depend on cleverness."** A counting lower bound holds for every algorithm in the model, including ones not yet invented.

## Go deeper

- Ronald Graham, Donald Knuth and Oren Patashnik, *Concrete Mathematics* (2nd ed., 1994): sums, binomials and generating functions for CS.
- Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics* (2009): counting as a tool for analysing algorithms.
- Eric Lehman, F. Thomson Leighton and Albert Meyer, *Mathematics for Computer Science* (2017 revision, free online): counting chapters with computer-science examples.
