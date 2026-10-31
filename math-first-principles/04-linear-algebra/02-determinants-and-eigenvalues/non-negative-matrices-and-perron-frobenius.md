# Non-negative Matrices and Perron–Frobenius

> **Layer:** [04 Linear Algebra](../README.md) › [Determinants and Eigenvalues](README.md)
> **Builds on:** [Eigenvalues and diagonalisation](eigenvalues-and-diagonalisation.md), [Graphs and connectivity](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md), [Finite probability spaces](../../03-combinatorics-and-graph-theory/03-discrete-probability/finite-probability-spaces.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md)
> **Enables:** [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md), [Mathematical biology and epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md), [Markov chains in computing](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/markov-chains.md)

## Essence
A matrix with no negative entries models anything that flows, grows or moves without cancellation: probabilities passing between states, populations passing between age classes, links passing importance between web pages. For such matrices the general theory of eigenvalues sharpens dramatically. Oskar Perron proved in 1907 that a matrix with all entries positive has a largest eigenvalue that is real, positive and simple, with an eigenvector that can be taken entirely positive. Georg Frobenius extended this in 1912 to non-negative matrices whose pattern of non-zero entries is connected. The positive eigenvector is the long-run state: the stationary distribution, the stable age structure, the ranking.

## Core tenets
1. **Perron: a positive matrix has a dominant positive eigenvector.** If every entry of A is positive, there is an eigenvalue r > 0, the Perron root, such that r is a simple root of the characteristic polynomial, every other eigenvalue λ satisfies ∣λ∣ < r, and the eigenvector for r can be chosen with all entries positive. No other eigenvalue has a non-negative eigenvector.

2. **The proof idea is a fixed point or an extremal ratio.** A maps the simplex of non-negative vectors with entries summing to 1 into itself after normalising, so [Brouwer's fixed-point theorem](../../07-topology/02-algebraic-topology/fixed-point-theorems.md) gives a non-negative eigenvector. An elementary route is the Collatz–Wielandt formula: r is the largest number such that Ax ≥ rx entrywise for some non-negative x ≠ 0. Positivity then forces the maximising x to be positive and unique up to scale.

3. **Frobenius: irreducible non-negative matrices keep most of the conclusion.** For n ≥ 2, a non-negative A is irreducible when its directed graph, with an edge i → j whenever aᵢⱼ > 0, is strongly connected. Then r is still positive and simple with a positive eigenvector, but other eigenvalues may also have absolute value r. The number h of them is the period, the greatest common divisor of the lengths of closed walks in the graph, and they are r times the h-th roots of unity. A is primitive when h = 1, equivalently when some power of A is positive; then ∣λ∣ < r for the other eigenvalues.

4. **Each hypothesis is needed.** The identity is non-negative but reducible: its Perron root 1 is not simple. diag(2, 1) is reducible and its eigenvector for 2 is (1, 0), not positive. The swap [[0, 1], [1, 0]] (rows listed in turn) is irreducible with period 2: its eigenvalues 1 and −1 have equal absolute value. And without non-negativity everything fails: [[1, −2], [−2, 1]] has dominant eigenvalue 3 with eigenvector (1, −1).

5. **The dominant eigenvector is what iteration finds.** For primitive A and any positive starting vector x, the normalised vectors Aᵏx converge to the Perron vector, with error shrinking like (∣λ₂∣/r)ᵏ, where λ₂ is the next largest eigenvalue in absolute value. The gap between r and ∣λ₂∣ sets the speed. This is the power method, and for huge sparse matrices it is often the only feasible algorithm.

6. **Stochastic matrices are the probabilistic case.** A matrix with non-negative entries and each row summing to 1 has Perron root 1 with eigenvector (1, …, 1). Its left Perron vector π, with πP = π, is a stationary distribution of the corresponding [Markov chain](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md). If P is irreducible, π is unique and positive; if it is also primitive (aperiodic), the distribution of the chain converges to π from any start.

7. **PageRank, Leslie matrices and epidemics are Perron vectors.** Sergey Brin and Lawrence Page's PageRank (1998) ranks web pages by the stationary distribution of a random surfer who follows a random link with probability α, typically about 0.85, and otherwise jumps to a random page; the jump makes the matrix positive, so Perron applies, and the power method converges with error of order αᵏ. Patrick Leslie's age-structured population model (1945) grows like rᵏ, with the Perron vector as the stable age distribution when the matrix is primitive. In compartmental [epidemic models](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), the basic reproduction number R₀ is the Perron root of the next-generation matrix; under the standard assumptions the disease-free state is locally stable if R₀ < 1 and unstable if R₀ > 1.

## Key concepts
| Term | Meaning |
|---|---|
| Non-negative matrix | Every entry ≥ 0 |
| Positive matrix | Every entry > 0 |
| Perron root | Largest real eigenvalue r, equal to the spectral radius |
| Perron vector | Positive eigenvector for r, normalised |
| Irreducible | Strongly connected graph of non-zero entries |
| Period | Greatest common divisor of closed-walk lengths |
| Primitive | Irreducible with period 1; some power is positive |
| Stochastic matrix | Non-negative with row sums 1 |

## How it fits
- **Below:** [eigenvalues](eigenvalues-and-diagonalisation.md) give the framework, [graph connectivity](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md) gives irreducibility, [finite probability](../../03-combinatorics-and-graph-theory/03-discrete-probability/finite-probability-spaces.md) gives stochastic matrices, and [the order of the reals](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) gives positivity.
- **Above:** convergence of [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md); R₀ in [epidemiology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md); in [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md), the entropy of a shift of finite type is the logarithm of a Perron root.
- **Siblings:** the Perron root has a [Jordan block](jordan-normal-form.md) of size 1; the [spectral theorem](../03-inner-product-spaces/the-spectral-theorem.md) is the other great special case where eigenvalues behave well.

## Common misconceptions
- **"A positive matrix is positive definite."**: positivity of entries says nothing about the quadratic form. [[1, 2], [2, 1]] is positive with eigenvalue −1.
- **"Every finite Markov chain converges to its stationary distribution."**: a periodic chain, such as the swap, oscillates forever; a reducible chain may have several stationary distributions.
- **"PageRank counts incoming links."**: it weights each link by the rank of the page it comes from, divided among that page's outgoing links: an eigenvector, not a count.

## Go deeper
- Carl D. Meyer, *Matrix Analysis and Applied Linear Algebra* (2000): a clear chapter on Perron–Frobenius theory.
- Amy N. Langville and Carl D. Meyer, *Google's PageRank and Beyond* (2006): the mathematics of web ranking.
- E. Seneta, *Non-negative Matrices and Markov Chains* (2nd edition, 1981): the standard monograph.
