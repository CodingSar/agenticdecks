# Divide and Conquer

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Design Paradigms](README.md)
> **Builds on:** [Induction and Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [Asymptotic Analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [Correctness and Invariants](../01-foundations/correctness-and-invariants.md)
> **Enables:** [Comparison Sorting](../04-sorting-and-searching/comparison-sorting.md), [Searching and Selection](../04-sorting-and-searching/searching-and-selection.md), [External Memory and Cache-Oblivious Algorithms](../07-advanced-topics/external-memory-and-cache-oblivious.md), [Data and Task Parallelism](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md)

## Essence

Divide and conquer solves a problem by splitting it into smaller independent instances of the same problem, solving each recursively, and combining their answers. When the split is balanced and the combine step is cheap, the work per level of recursion stays small and the number of levels is logarithmic, so you get algorithms like merge sort (Θ(n log n)), binary search (Θ(log n)) and the Fast Fourier Transform (FFT, Θ(n log n)). The running time is described by a recurrence such as T(n) = a·T(n/b) + f(n), which the Master Theorem solves by comparing the work at the leaves with the work at the root. Because the subproblems are independent, divide and conquer is also the most natural source of parallelism.

## Core tenets

1. **Three steps: divide, conquer, combine.** Divide the input into subproblems, solve each recursively (bottoming out at a base case solved directly), then combine. Where the work goes varies: merge sort's split is trivial and its merge does the work; quicksort's partition does the work and its combine is trivial. Correctness is proved by strong induction on input size.

2. **The recurrence T(n) = a·T(n/b) + f(n) captures the cost.** Here a is the number of subproblems, n/b their size, and f(n) the divide-plus-combine cost. The recursion tree has log_b n levels and a^(log_b n) = n^(log_b a) leaves.

3. **The Master Theorem compares root work with leaf work.** Let c = log_b a. If f(n) = O(n^(c−ε)), leaves dominate: T(n) = Θ(n^c). If f(n) = Θ(n^c), every level costs the same: T(n) = Θ(n^c log n). If f(n) = Ω(n^(c+ε)) (and a regularity condition holds), the root dominates: T(n) = Θ(f(n)). Merge sort (a = 2, b = 2, f = n) is the middle case: Θ(n log n). Binary search (a = 1, b = 2, f = 1) is also the middle case: Θ(log n).

4. **Reducing the number of subproblems beats the obvious bound.** Multiplying two n-digit numbers naively takes Θ(n²). Karatsuba (1962) computes the product from three half-size products instead of four, giving T(n) = 3T(n/2) + O(n) = Θ(n^(log₂ 3)) ≈ Θ(n^1.585). Strassen (1969) multiplies matrices with seven half-size products instead of eight: Θ(n^(log₂ 7)) ≈ Θ(n^2.807). The exponent comes from a, so saving one recursive call changes the asymptotic class.

5. **Balanced splits matter; unbalanced ones can be fatal.** If a split puts n − 1 elements on one side, T(n) = T(n − 1) + O(n) = Θ(n²): this is quicksort on already-sorted input with a naive pivot. Any constant-fraction split (even 1%:99%) still gives Θ(n log n) depth-times-work, which is why random pivots work so well.

6. **Independence of subproblems is what separates this from dynamic programming.** If subproblems overlap (Fibonacci's F(n−1) and F(n−2) both need F(n−3)), naive recursion recomputes them exponentially often. Divide and conquer is efficient only when subproblems are disjoint; otherwise store answers and use [dynamic programming](dynamic-programming.md).

7. **Divide and conquer is naturally parallel and cache-friendly.** Independent subproblems can run on different cores; merge sort with a parallel merge has polylogarithmic span (O(log³ n) for the simple version), so its parallelism is nearly n. Recursion also gives locality for free: eventually a subproblem fits in cache, and from then on all its work runs at cache speed without knowing the cache size. This is the principle behind [cache-oblivious algorithms](../07-advanced-topics/external-memory-and-cache-oblivious.md).

8. **In practice, stop recursing early.** Recursive calls have overhead, and small problems are faster with simple loops. Production sorts switch to insertion sort below about 16–32 elements; Strassen's algorithm only pays off above matrix sizes in the hundreds or thousands, and its numerical stability is worse than the classical method, so most linear-algebra libraries use blocked Θ(n³) multiplication instead.

## Key concepts

| Term | Meaning |
|---|---|
| Recurrence | Equation expressing T(n) in terms of T on smaller inputs |
| Recursion tree | Tree of subproblems; summing work per level solves the recurrence |
| Master Theorem | Closed-form solution for T(n) = a·T(n/b) + f(n) in three cases |
| Base case | Smallest instance, solved directly |
| Karatsuba multiplication | Three-multiplication split giving Θ(n^1.585) integer multiplication |
| Strassen's algorithm | Seven-multiplication split giving Θ(n^2.807) matrix multiplication |
| FFT | Θ(n log n) divide-and-conquer evaluation of a polynomial at roots of unity |
| Akra–Bazzi method | Generalisation of the Master Theorem for unequal subproblem sizes |

## How it fits

- **Below:** correctness is [strong induction](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md); cost uses [asymptotic notation](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md); the FFT relies on [complex roots of unity](../../01-mathematical-foundations/04-algebra/abstract-algebra.md).
- **Above:** [MapReduce and batch processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) are divide and conquer across machines; [fork–join parallelism](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md) is its shared-memory form; the FFT underpins [signal processing](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) and [media compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md); [k-d trees](../07-advanced-topics/computational-geometry.md) divide space recursively.
- **Siblings:** [dynamic programming](dynamic-programming.md) handles overlapping subproblems; [randomized algorithms](randomized-algorithms.md) choose good splits by chance; [greedy](greedy-algorithms.md) makes one choice and never recurses on alternatives.

## Common misconceptions

- **"Recursion makes it divide and conquer."** Naive recursive Fibonacci is recursive but exponential, because its subproblems overlap.
- **"Lower asymptotic exponent means faster."** Strassen and the newer "galactic" matrix-multiplication algorithms (exponent below 2.372) have constants so large that they never pay off in practice.
- **"The Master Theorem solves every recurrence."** It needs equal-size subproblems and polynomially separated cases; others need the recursion tree or Akra–Bazzi.

## Go deeper

- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (4th ed., 2022): divide-and-conquer chapter with the Master Theorem proof.
- Jon Kleinberg and Éva Tardos, *Algorithm Design* (2005): chapter 5, with clear recurrence-based reasoning.
- James W. Cooley and John W. Tukey, "An Algorithm for the Machine Calculation of Complex Fourier Series" (1965): the FFT paper.
