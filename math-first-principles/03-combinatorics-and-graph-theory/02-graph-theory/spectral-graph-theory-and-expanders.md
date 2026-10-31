# Spectral Graph Theory and Expanders

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Graph Theory](README.md)
> **Builds on:** [Graphs and connectivity](graphs-and-connectivity.md), [Trees](trees.md), [Matchings and network flows](matchings-and-network-flows.md)
> **Enables:** [Non-negative matrices and Perron–Frobenius](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md), [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md), [Error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md), [High-dimensional geometry and random matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md), [Randomized algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md)

## Essence
Spectral graph theory reads the structure of a graph from the eigenvalues of matrices attached to it, chiefly the adjacency matrix and the Laplacian. These matrices are symmetric, so their eigenvalues are real, and a handful of them reveal a great deal: the number of components, bipartiteness, the number of spanning trees, and above all how hard the graph is to cut in two. Graphs that are sparse yet impossible to cut cheaply are called expanders. They combine the economy of few edges with the robustness of a complete graph, and turn up from error-correcting codes to number theory.

## Core tenets
1. **The Laplacian is a sum of squares.** For a graph with adjacency matrix A and diagonal degree matrix D, the Laplacian L = D − A satisfies xᵀLx = Σ over edges uv of (xᵤ − xᵥ)². So L is positive semidefinite, with eigenvalues 0 = μ₁ ≤ μ₂ ≤ ⋯ ≤ μₙ, and xᵀLx = 0 exactly when x is constant on each component. Hence the multiplicity of the eigenvalue 0 is the number of components, and μ₂ > 0 if and only if the graph is connected; Miroslav Fiedler (1973) called μ₂ the algebraic connectivity.

2. **Adjacency eigenvalues see degrees, walks and bipartiteness.** The largest adjacency eigenvalue λ₁ lies between the average degree and the maximum degree Δ, equalling Δ, for a connected graph, only when the graph is regular. Since tr Aᵏ counts closed walks of length k, a graph is bipartite if and only if its spectrum is symmetric about 0: symmetry makes every odd trace vanish, so there are no odd closed walks and hence no odd cycles.

3. **Determinants count spanning trees.** Kirchhoff's matrix-tree theorem (1847) counts spanning trees as μ₂μ₃⋯μₙ/n, equivalently any cofactor of L ([trees](trees.md)). For Kₙ the non-zero Laplacian eigenvalues are all n, giving Cayley's nⁿ⁻² again.

4. **Cheeger's inequality ties eigenvalues to bottlenecks.** For a d-regular graph define the edge expansion h(G) as the minimum, over vertex sets S with ∣S∣ ≤ n/2, of the number of edges leaving S divided by ∣S∣. Then μ₂/2 ≤ h(G) ≤ √(2dμ₂), proved in discrete form in the mid-1980s by Jozef Dodziuk and by Noga Alon and Vitali Milman. The left side follows by putting a vector that is constant on S and on its complement, and sums to zero, into the Rayleigh quotient for μ₂. The right side's proof is an algorithm, spectral partitioning: sorting vertices by their entries in the eigenvector for μ₂ finds a sparse cut.

5. **Expanders are sparse graphs that are hard to cut.** A family of d-regular graphs with n → ∞ is an expander family when h(G), or equivalently the spectral gap d − λ₂, stays above a fixed positive constant. Random d-regular graphs with d ≥ 3 are expanders with high probability ([random graphs](../03-discrete-probability/random-graphs.md)). Explicit families are harder; Grigory Margulis gave the first in 1973, using group representations, and Cayley graphs of groups are still the main source ([free groups and presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md)).

6. **The expander mixing lemma: small eigenvalues mean random-looking edges.** For a d-regular graph whose eigenvalues other than d are at most λ in absolute value, any vertex sets S and T satisfy ∣e(S, T) − d∣S∣∣T∣/n∣ ≤ λ√(∣S∣∣T∣), where e(S, T) counts edges from S to T. Here d∣S∣∣T∣/n is the count expected in a random graph of the same density, so when λ is small any two large sets are joined by about that many edges.

7. **Ramanujan graphs are optimal expanders.** The Alon–Boppana bound says λ₂ ≥ 2√(d − 1) − o(1) for d-regular graphs as n → ∞, because a graph cannot expand better than the infinite d-regular tree it locally resembles. Graphs with every non-trivial eigenvalue at most 2√(d − 1) in absolute value are called Ramanujan. Alexander Lubotzky, Ralph Phillips and Peter Sarnak, and independently Margulis, built infinite families of them in 1988 with d − 1 a suitable prime, using deep number theory that gives the name. Adam Marcus, Daniel Spielman and Nikhil Srivastava proved in 2015 that bipartite Ramanujan graphs exist for every degree, and Joel Friedman proved that random regular graphs are almost Ramanujan.

8. **Random walks on expanders mix in logarithmic time.** On a connected non-bipartite d-regular graph, the distance of a random walk's distribution from uniform shrinks each step by the factor max(∣λ₂∣, ∣λₙ∣)/d, so on an expander it is small after O(log n) steps ([Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md)). That is why expanders save random bits in algorithms, give error-correcting codes decodable in linear time (Michael Sipser and Spielman, 1996), and underlie Omer Reingold's 2005 proof that connectivity in undirected graphs can be decided in logarithmic memory.

## Key concepts
| Term | Meaning |
|---|---|
| Adjacency matrix | A, with 1 in entry (u, v) for each edge uv |
| Laplacian | L = D − A; quadratic form Σ (xᵤ − xᵥ)² over edges |
| Algebraic connectivity | μ₂, the second-smallest Laplacian eigenvalue |
| Spectral gap | d − λ₂ for a d-regular graph |
| Edge expansion h(G) | Fewest edges leaving S per vertex of S, over sets with ∣S∣ ≤ n/2 |
| Expander family | d-regular graphs with h(G) bounded below as n → ∞ |
| Expander mixing lemma | Edge counts between sets are near the random value |
| Ramanujan graph | Non-trivial eigenvalues at most 2√(d − 1) in absolute value |

## How it fits
- **Below:** [connectivity](graphs-and-connectivity.md) supplies components, bipartiteness and the adjacency matrix; [trees](trees.md) supply the matrix-tree theorem; [cuts in network flows](matchings-and-network-flows.md) are what expansion measures.
- **Above:** eigenvalue facts rest on [the spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) and [Perron–Frobenius theory](../../04-linear-algebra/02-determinants-and-eigenvalues/non-negative-matrices-and-perron-frobenius.md); mixing times belong to [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md); expander codes are [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md); random graph spectra are [random matrices](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md).
- **Siblings:** [colouring](colouring-and-planarity.md) has spectral bounds too, since χ(G) ≤ λ₁ + 1; [matchings and flows](matchings-and-network-flows.md) find minimum cuts exactly between two given vertices, while Cheeger's inequality estimates the sparsest cut of all.

## Common misconceptions
- **"Expanders must be dense."**: degree 3 suffices. Such a graph has 3n/2 edges, yet every set of up to half the vertices has edges leaving it in proportion to its size.
- **"The adjacency and Laplacian spectra carry the same information."**: only for regular graphs, where L = dI − A. For irregular graphs they can differ.
- **"To certify an expander, check every cut."**: there are exponentially many cuts and no efficient way to find the sparsest is known; μ₂ is computable quickly and, through Cheeger's inequality, certifies expansion.

## Go deeper
- Hoory, Linial and Wigderson, "Expander graphs and their applications", *Bulletin of the American Mathematical Society* (2006): the standard survey, from Cheeger to codes.
- Chung, *Spectral Graph Theory* (1997): the normalised Laplacian and isoperimetric inequalities.
- Brouwer and Haemers, *Spectra of Graphs* (2012): adjacency and Laplacian spectra in depth.
