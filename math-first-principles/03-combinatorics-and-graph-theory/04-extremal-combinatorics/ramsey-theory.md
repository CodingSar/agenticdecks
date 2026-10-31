# Ramsey Theory

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Extremal Combinatorics](README.md)
> **Builds on:** [Inclusion–exclusion and the pigeonhole principle](../01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md), [Graphs and connectivity](../02-graph-theory/graphs-and-connectivity.md), [The probabilistic method](../03-discrete-probability/the-probabilistic-method.md), [Countable sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md)
> **Enables:** [Extremal graph theory](extremal-graph-theory.md), [Additive combinatorics](additive-combinatorics.md), [Gödel's incompleteness theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md), [Proof theory and reverse mathematics](../../13-structure-and-metamathematics/02-computability-and-incompleteness/proof-theory-and-reverse-mathematics.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence
Ramsey theory says that complete disorder is impossible: every sufficiently large structure, however it is coloured or split, contains a large orderly substructure. The model statement is about graphs. For every k, if the edges of a large enough complete graph are coloured red and blue, there are k vertices whose edges all have the same colour. The least such size is the Ramsey number R(k, k). The theorem is a far-reaching pigeonhole principle, and its numbers are hard to compute. R(3, 3) = 6 has a short proof, but R(5, 5) is unknown. The best bounds sit between √2ᵏ and about 4ᵏ, and the exponential gap between them is one of the central problems of combinatorics.

## Core tenets
1. **R(3, 3) = 6: among any six people, three are mutual friends or three are mutual strangers.** Colour the edges of K₆. A vertex v has five edges, so by pigeonhole at least three share a colour, say red to a, b, c. If any edge among a, b, c is red, it forms a red triangle with v. Otherwise a, b, c form a blue triangle. Six is the least such number: colour the edges of a pentagon red and its diagonals blue, and K₅ has no monochromatic triangle.

2. **Ramsey's theorem: R(s, t) exists, and R(s, t) ≤ R(s − 1, t) + R(s, t − 1).** Here R(s, t) is the least n such that every red–blue colouring of Kₙ has a red Kₛ or a blue Kₜ. Pick a vertex v in a complete graph with R(s − 1, t) + R(s, t − 1) vertices. Then v has at least R(s − 1, t) red neighbours or at least R(s, t − 1) blue ones, and induction finishes inside that neighbourhood. Since the recursion matches Pascal's rule, R(s, t) ≤ C(s + t − 2, s − 1) (Erdős and Szekeres, 1935), and so R(k, k) < 4ᵏ.

3. **Erdős (1947): R(k, k) > 2^(k/2), by a random colouring.** Colour the edges of Kₙ by fair coins. The expected number of monochromatic k-sets is C(n, k) · 2^(1 − C(k, 2)), which is below 1 when n = ⌊2^(k/2)⌋ and k ≥ 3. So some colouring has none ([the probabilistic method](../03-discrete-probability/the-probabilistic-method.md)). No explicit colouring is known that achieves an exponential bound of this strength, though explicit constructions have improved greatly.

4. **The diagonal bounds are √2ᵏ < R(k, k) < 4ᵏ, and the gap is open as of 2026.** For decades the only improvements to either bound changed lower-order factors. In 2023 Campos, Griffiths, Morris and Sahasrabudhe proved an exponential improvement of the upper bound: R(k, k) ≤ (4 − ε)ᵏ for some fixed ε > 0. The lower bound's base √2 has not been improved since 1947. Whether R(k, k)^(1/k) has a limit, and what it is, remains unknown.

5. **Small Ramsey numbers are very hard to compute.** The known values include R(3, 4) = 9, R(3, 5) = 14, R(4, 4) = 18, and, with three colours, R(3, 3, 3) = 17. R(5, 5) is known only to lie between 43 and 48, and its exact value is open as of 2026. Brute force cannot settle it: K₄₃ has 903 edges and so 2⁹⁰³ red–blue colourings. Erdős joked that if aliens demanded R(5, 5) on pain of war, humanity should marshal all its computers; if they demanded R(6, 6), it should attack first.

6. **Infinite Ramsey theory is simpler, and compactness links it to the finite theory.** If the pairs of natural numbers are coloured with finitely many colours, some infinite subset has all its pairs the same colour. Ramsey proved this in 1930, in a paper on a problem in logic. A compactness argument through [König's lemma](../02-graph-theory/trees.md) recovers the finite theorem, but it gives no bounds. Paris and Harrington (1977) found a slight strengthening of finite Ramsey that is true yet unprovable in Peano arithmetic (PA, the standard axioms for the natural numbers). It was the first natural combinatorial example of [Gödel incompleteness](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md).

7. **The same phenomenon holds in arithmetic and geometry.** Schur (1916): any finite colouring of the positive integers has a monochromatic solution of x + y = z. Van der Waerden (1927): any finite colouring has arbitrarily long monochromatic arithmetic progressions. Hales and Jewett (1963) abstracted both to combinatorial lines in high-dimensional grids. Erdős and Szekeres also showed that enough points in general position in the plane contain the vertices of a convex k-gon. Density versions, in which one colour class is replaced by any set of positive density, belong to [additive combinatorics](additive-combinatorics.md).

## Key concepts
| Term | Meaning |
|---|---|
| Ramsey number R(s, t) | The least n such that every red–blue colouring of Kₙ has a red Kₛ or a blue Kₜ |
| Diagonal Ramsey number | R(k, k) |
| Monochromatic | All in one colour |
| Multicolour Ramsey number | R(s₁, …, sᵣ), defined in the same way with r colours |
| Infinite Ramsey theorem | Every finite colouring of the pairs of ℕ has an infinite monochromatic subset |
| Van der Waerden's theorem | Finite colourings of ℕ have long monochromatic arithmetic progressions |
| Paris–Harrington theorem | A finite Ramsey statement independent of Peano arithmetic |

## How it fits
- **Below:** Built on the [pigeonhole principle](../01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md), [graphs](../02-graph-theory/graphs-and-connectivity.md), random colourings from [the probabilistic method](../03-discrete-probability/the-probabilistic-method.md), and [countable sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md) for the infinite version.
- **Above:** Independence results lead to [Gödel's theorems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/godels-incompleteness-theorems.md) and [reverse mathematics](../../13-structure-and-metamathematics/02-computability-and-incompleteness/proof-theory-and-reverse-mathematics.md), which measures the strength of Ramsey's theorem. Large cardinal axioms extend Ramsey properties to the uncountable ([large cardinals](../../13-structure-and-metamathematics/03-model-theory-and-independence/large-cardinals.md)). Diagonal Ramsey bounds are on the list of [open problems](../../15-mathematics-in-context/open-problems.md).
- **Siblings:** [Extremal graph theory](extremal-graph-theory.md) asks the density question: how many edges force a subgraph. [Additive combinatorics](additive-combinatorics.md) proves density versions of van der Waerden's theorem.

## Common misconceptions
- **"Ramsey numbers just need a faster computer"**: the search space for R(5, 5) has more than 2⁹⁰⁰ colourings, so progress needs clever pruning and theory as well as hardware.
- **"A random colouring is a bad Ramsey colouring"**: random colourings are almost always better than every known explicit construction.
- **"Ramsey's theorem says patterns in data are meaningful"**: it says the opposite; large enough structures contain orderly patterns by necessity, so finding one proves nothing about design.

## Go deeper
- Graham, Rothschild and Spencer, *Ramsey Theory* (2nd edition, 1990): the classical theory, from Ramsey's theorem to Hales–Jewett.
- Alon and Spencer, *The Probabilistic Method* (4th edition, 2016): Erdős's lower bound and its refinements.
- Conlon, Fox and Sudakov, *Recent Developments in Graph Ramsey Theory* (2015): a survey of bounds and methods before the 2023 breakthrough.
