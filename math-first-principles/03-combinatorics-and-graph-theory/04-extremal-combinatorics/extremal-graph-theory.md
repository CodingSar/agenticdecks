# Extremal Graph Theory

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Extremal Combinatorics](README.md)
> **Builds on:** [Graphs and connectivity](../02-graph-theory/graphs-and-connectivity.md), [Colouring and planarity](../02-graph-theory/colouring-and-planarity.md), [The probabilistic method](../03-discrete-probability/the-probabilistic-method.md), [Ramsey theory](ramsey-theory.md), [Counting principles and binomial coefficients](../01-enumeration/counting-principles-and-binomial-coefficients.md)
> **Enables:** [Additive combinatorics](additive-combinatorics.md), [Finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md), [Projective geometry](../../08-geometry/01-classical-geometry/projective-geometry.md), [The spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence
Extremal graph theory asks how many edges a graph on n vertices can have without containing a given subgraph H. That maximum is the Turán number ex(n, H). Ramsey theory says that colouring cannot avoid structure; extremal theory says that density cannot avoid it, and it measures exactly how much density is needed. The answer has a surprising shape: to first order it depends only on the chromatic number of H. So the theory splits cleanly. For non-bipartite H the answer is a known constant times n². For bipartite H the answer is a smaller power of n, and that case is still poorly understood. Szemerédi's regularity lemma, the strongest structural tool, shows that every large graph looks random at a coarse scale.

## Core tenets
1. **Mantel (1907): a triangle-free graph on n vertices has at most n²/4 edges.** If xy is an edge, x and y have no common neighbour, so d(x) + d(y) ≤ n. Summing over the E edges gives ∑ d(v)² ≤ nE. Since ∑ d(v) = 2E, the mean of the squares is at least the square of the mean, so ∑ d(v)² ≥ 4E²/n. Together these give E ≤ n²/4. Equality holds for the complete bipartite graph with two equal halves, which shows the bound is sharp.

2. **Turán (1941): a graph with no Kᵣ₊₁ has at most (1 − 1/r) · n²/2 edges.** The extremal graph is the Turán graph: split the vertices into r nearly equal parts and join every pair in different parts. Zykov's symmetrisation gives a clean proof. Among Kᵣ₊₁-free graphs of maximum size, two non-adjacent vertices can be made to have the same neighbourhood without losing edges or creating a Kᵣ₊₁. Non-adjacency then becomes an equivalence relation, and the graph is complete multipartite with at most r parts. Balancing the parts maximises the edge count.

3. **Erdős–Stone (1946): for every H, ex(n, H) = (1 − 1/(χ(H) − 1)) · n²/2 plus an error that is a vanishing fraction of n².** Here χ(H) is the chromatic number from [colouring](../02-graph-theory/colouring-and-planarity.md). The lower bound is the Turán graph with χ(H) − 1 parts, which cannot contain H because H cannot be coloured with χ(H) − 1 colours. The upper bound shows that slightly more edges force a large complete multipartite graph, and H sits inside it. Erdős and Simonovits saw that this determines the asymptotics for every non-bipartite H at once.

4. **For bipartite H the Turán number is a smaller power of n.** The Kővári–Sós–Turán theorem (1954) gives ex(n, Kₛ,ₜ) ≤ c · n^(2 − 1/s), where Kₛ,ₜ is the complete bipartite graph with parts of sizes s ≤ t and c depends only on s and t. Its proof double counts stars of s edges. For the 4-cycle, ex(n, C₄) is asymptotically n^(3/2)/2. The matching construction comes from points and lines of a projective plane over a [finite field](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md), in which two lines meet in at most one point. For most bipartite H, including C₈ and K₄,₄, the correct exponent is unknown as of 2026.

5. **Random graphs give lower bounds, and algebra often does better.** Deleting one edge from each copy of H in a random graph with suitable edge probability gives an H-free graph with many edges ([alteration](../03-discrete-probability/the-probabilistic-method.md)). For cycles and complete bipartite graphs, algebraic constructions from [projective geometry](../../08-geometry/01-classical-geometry/projective-geometry.md) and finite fields beat random ones and sometimes match the upper bound.

6. **Szemerédi's regularity lemma: every large graph is a bounded number of random-looking pieces.** For every ε > 0 there is an M such that the vertices of every graph can be split into at most M nearly equal parts, with all but an ε fraction of the pairs of parts ε-regular. An ε-regular pair has edge densities that vary by less than ε between large subsets. M grows as a tower of exponentials, and Gowers (1997) showed that tower-type growth is unavoidable. The lemma turns problems about arbitrary graphs into problems about weighted graphs of bounded size.

7. **The removal lemma: few copies of a triangle means close to triangle-free.** If a graph on n vertices has fewer than δn³ triangles, it can be made triangle-free by deleting at most εn² edges, where δ depends on ε. The proof uses regularity. Ruzsa and Szemerédi used it to give a short proof of Roth's theorem, which says that a set of integers with positive density contains three-term arithmetic progressions. This connection is the start of [additive combinatorics](additive-combinatorics.md).

8. **For hypergraphs even the simplest case is open.** Turán asked for the largest density of a 3-uniform hypergraph (one whose edges are triples) with no complete 4-vertex hypergraph. He conjectured 5/9, from an explicit construction. The conjecture is open as of 2026, although computer-assisted flag-algebra methods have brought the upper bound close to 5/9.

## Key concepts
| Term | Meaning |
|---|---|
| Turán number ex(n, H) | The most edges in an H-free graph on n vertices |
| Turán graph | A complete r-partite graph with parts as equal as possible |
| Erdős–Stone theorem | ex(n, H) is governed asymptotically by χ(H) |
| Degenerate case | Bipartite H, where ex(n, H) is a smaller power than n² |
| Zarankiewicz problem | Determining ex(n, Kₛ,ₜ) |
| ε-regular pair | A pair of vertex sets whose edge density is nearly uniform on large subsets |
| Regularity lemma | Every graph splits into boundedly many parts, almost all pairs regular |
| Removal lemma | Few copies of H means few edges need deleting to destroy all copies |

## How it fits
- **Below:** Built on [graphs](../02-graph-theory/graphs-and-connectivity.md), the chromatic number from [colouring](../02-graph-theory/colouring-and-planarity.md), [double counting](../01-enumeration/counting-principles-and-binomial-coefficients.md) and random constructions from [the probabilistic method](../03-discrete-probability/the-probabilistic-method.md). It is the density version of [Ramsey theory](ramsey-theory.md).
- **Above:** Constructions use [finite fields](../../05-abstract-algebra/02-rings-and-fields/finite-fields.md) and [projective geometry](../../08-geometry/01-classical-geometry/projective-geometry.md). Eigenvalue bounds use [the spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md). Regularity has analytic versions in Fourier analysis on groups ([Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md)).
- **Siblings:** The removal lemma proves Roth's theorem in [additive combinatorics](additive-combinatorics.md). [Posets and extremal set theory](posets-and-extremal-set-theory.md) asks the same questions about families of sets instead of edges.

## Common misconceptions
- **"Forbidding a bigger subgraph always allows more edges"**: to first order only χ(H) matters, so forbidding K₃ and forbidding the Petersen graph, both with χ = 3, allow the same n²/4 asymptotically.
- **"The regularity lemma gives useful numbers"**: its bounds are towers of exponentials, so results proved with it are qualitative unless a different proof is found.
- **"Bipartite Turán problems are the easy case"**: their leading term is zero on the n² scale, but determining the true exponent is among the hardest open questions.

## Go deeper
- Bollobás, *Extremal Graph Theory* (1978): the classical results and methods.
- Zhao, *Graph Theory and Additive Combinatorics* (2023): regularity, removal and pseudorandomness linking graphs to arithmetic.
- Füredi and Simonovits, *The History of Degenerate (Bipartite) Extremal Graph Problems* (2013): a survey of the bipartite case.
