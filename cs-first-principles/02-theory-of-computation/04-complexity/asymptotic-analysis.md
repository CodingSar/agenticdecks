# Asymptotic Analysis

> **Layer:** [02 Theory of Computation](../README.md) › [Complexity](README.md)
> **Builds on:** [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), [Induction and Recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md), [Turing Machines](../03-computability/turing-machines.md)
> **Enables:** [Complexity Classes](complexity-classes.md), [Models of Computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md), [Divide and Conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md), [Amortized Analysis](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md)

## Essence

Asymptotic analysis describes how the resources an algorithm uses (time, memory, messages) grow as the input gets large, ignoring constant factors and small inputs. It does this with Big-O and its relatives, which compare functions by their eventual growth rate. The point is to get a statement about the *algorithm* that survives changes of machine, compiler and programming language: those change running time by constant factors, while the growth rate (linear, quadratic, exponential) is a property of the method. This is what lets complexity theory classify problems and lets engineers predict, before running anything, which approach will survive a thousandfold increase in data.

## Core tenets

1. **Big-O is an upper bound up to a constant, for large enough inputs.** f(n) = O(g(n)) means there exist c > 0 and n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀. Big-Omega, Ω, is the matching lower bound, and Big-Theta, Θ, means both. Little-o, f = o(g), means f/g → 0: f grows strictly slower. So 3n² + 100n + 7 = Θ(n²), and n log n = o(n²).

2. **Constants are dropped because machines differ by constants.** Any reasonable model of computation simulates another with at most polynomial (often only constant or logarithmic) overhead, and a faster processor speeds everything by a constant. A Θ(n²) algorithm on a machine 100 times faster still loses to a Θ(n log n) algorithm once n is in the low thousands. The asymptotic class is the part of the cost that no hardware change fixes.

3. **The growth hierarchy is steep, and it decides feasibility.** 1 < log n < √n < n < n log n < n² < n³ < 2ⁿ < n! < nⁿ. At about 10⁹ simple steps per second (circa 2020s hardware), n = 10⁶ is instant for n log n (~2×10⁷ steps), ~17 minutes for n² (10¹² steps), and 2ⁿ is hopeless already at n = 100 (~10³⁰ steps, about 4×10¹³ years). The boundary between polynomial and exponential growth is the boundary of [tractability](p-np-and-np-completeness.md).

4. **Analyses state which case and which model.** Worst-case bounds hold for every input of size n; average-case bounds assume an input distribution; expected bounds for randomised algorithms average over the algorithm's own coin flips but hold for every input; amortised bounds average over a sequence of operations. Quicksort is Θ(n²) worst case and Θ(n log n) expected with random pivots. The cost model (unit-cost word operations on a Random Access Machine (RAM), bit operations, or memory transfers) must also be stated, because it changes the answers.

5. **Input size is measured in bits.** n is the length of the input's encoding. An algorithm that loops k times on the number k is linear in k but exponential in its bit length log₂ k ("pseudo-polynomial"). This is why trial division is not a polynomial-time factoring algorithm, and why the 0/1 knapsack dynamic program, O(nW), does not put the problem in P (the class of problems solvable in polynomial time).

6. **Recurrences capture divide-and-conquer costs.** T(n) = aT(n/b) + f(n) describes splitting into a subproblems of size n/b plus f(n) work to divide and combine. The master theorem compares f(n) with n^(log_b a): if f is polynomially smaller, T = Θ(n^(log_b a)); if equal up to Θ, T = Θ(n^(log_b a) log n); if polynomially larger (with a regularity condition), T = Θ(f(n)). Merge sort, T(n) = 2T(n/2) + Θ(n), gives Θ(n log n).

7. **Lower bounds are about the problem, not one algorithm.** An upper bound needs one algorithm; a lower bound must defeat all of them. In restricted models we can prove them: any comparison sort needs Ω(n log n) comparisons, because a decision tree distinguishing n! orderings has depth at least log₂ n! ≈ n log₂ n. In general models, proving strong lower bounds is extraordinarily hard: for Boolean circuits, the best proven lower bound for any explicit function in NP (nondeterministic polynomial time) is only about 3n gates.

8. **Asymptotics can mislead at real sizes.** Big-O hides constants and lower-order terms, and real machines have caches. Fast matrix-multiplication algorithms with exponents near 2.37 are never used because their constants are astronomical ("galactic algorithms"), and an O(n) linked-list scan can lose to an O(n) array scan by 10–100× because of [cache misses](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md). Choose a class asymptotically, then measure.

## Key concepts

| Term | Meaning |
|---|---|
| O(g) | Eventually at most a constant times g |
| Ω(g) | Eventually at least a constant times g |
| Θ(g) | Both O(g) and Ω(g): same growth rate |
| o(g) | Grows strictly slower than g |
| Worst / average / expected / amortised | Max over inputs / mean over input distribution / mean over random choices / mean over an operation sequence |
| Pseudo-polynomial | Polynomial in a numeric value but exponential in its bit length |
| Master theorem | Closed-form solution of T(n) = aT(n/b) + f(n) |
| Lower bound | A cost every algorithm for a problem must pay |

## How it fits

- **Below:** Limits and growth rates come from [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md); recurrences from [induction and recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md); counting arguments for lower bounds from [combinatorics](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md). Time and space are defined as steps and cells of a [Turing machine](../03-computability/turing-machines.md).
- **Above:** It is the language of all [algorithm analysis](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md), from [divide and conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) and [comparison sorting](../../05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md) to [amortised analysis](../../05-algorithms-and-data-structures/01-foundations/amortized-analysis.md). It reappears as scalability analysis in [query optimisation](../../09-data-management/03-query-processing/query-optimization.md), [parallel work and span](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) and [large systems](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md).
- **Siblings:** It supplies the measuring stick that [complexity classes](complexity-classes.md) and [P vs NP](p-np-and-np-completeness.md) use to group problems by growth rate.

## Common misconceptions

- **"O(n) means it takes exactly n steps" or "Big-O means worst case."** Big-O is an upper bound on a function; which function (worst, average, best case) is a separate choice.
- **"A lower Big-O is always faster in practice."** Only for large enough n. Constants, memory behaviour and input sizes in your workload decide real performance.
- **"Polynomial means fast."** n¹⁰⁰ is polynomial and useless. Polynomial is a robust *theoretical* dividing line; in practice most useful polynomial algorithms have small exponents.

## Go deeper

- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein, *Introduction to Algorithms* (4th ed., 2022), chapters 3–4: notation and recurrences.
- Robert Sedgewick and Philippe Flajolet, *An Introduction to the Analysis of Algorithms* (2nd ed., 2013): precise analysis beyond Big-O.
