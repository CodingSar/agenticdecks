# Posets and Extremal Set Theory

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Extremal Combinatorics](README.md)
> **Builds on:** [Relations and orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), [Counting principles and binomial coefficients](../01-enumeration/counting-principles-and-binomial-coefficients.md), [Matchings and network flows](../02-graph-theory/matchings-and-network-flows.md), [Finite probability spaces](../03-discrete-probability/finite-probability-spaces.md)
> **Enables:** [Linear independence, bases and dimension](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), [Fixed-point theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md), [Statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence
A partially ordered set, or poset, is a set with a reflexive, antisymmetric and transitive [order relation](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md) in which some pairs may be incomparable. Its two basic shapes are chains, in which every two elements are comparable, and antichains, in which no two are. Extremal set theory studies families of subsets of an n-element set, ordered by inclusion, and asks how large a family can be under a restriction. Examples are "no set contains another", "every two sets meet" or "every two sets share an even number of elements". The answers are exact and often attained by the most symmetric families. The proofs are some of the most elegant in combinatorics: double counting over random chains, cyclic orders, and arguments that turn sets into vectors.

## Core tenets
1. **Mirsky and Dilworth: chains and antichains are dual.** In a finite poset, the longest chain has as many elements as the fewest antichains that cover the poset (Mirsky, 1971). To see this, give each element the length of the longest chain ending at it; elements with the same value form an antichain. Dually, the largest antichain has as many elements as the fewest chains that cover the poset (Dilworth, 1950). Dilworth's theorem is harder. One proof builds a bipartite graph with an edge from x to y whenever x < y and applies [König's theorem](../02-graph-theory/matchings-and-network-flows.md): a maximum matching links elements into as few chains as possible.

2. **Sperner (1928): an antichain of subsets of an n-set has at most C(n, ⌊n/2⌋) members.** The middle layer, all subsets of size ⌊n/2⌋, attains this. The LYM inequality is a sharper statement: for an antichain 𝒜, the sum of 1/C(n, ∣A∣) over A ∈ 𝒜 is at most 1. To prove it, choose a random maximal chain ∅ ⊂ {x₁} ⊂ {x₁, x₂} ⊂ ⋯ by taking a random ordering of the elements. A fixed set A lies on the chain with probability 1/C(n, ∣A∣), and at most one member of an antichain can lie on any chain. Since each term is at least 1/C(n, ⌊n/2⌋), Sperner's bound follows.

3. **Erdős–Ko–Rado: an intersecting family of k-sets from an n-set with n ≥ 2k has at most C(n − 1, k − 1) members.** All k-sets containing one fixed element form such a family, called a star. Katona's proof places the n elements around a random cycle. At most k of the k arcs of consecutive elements can pairwise intersect. Averaging over cycles gives the bound. The condition n ≥ 2k is needed: if n < 2k, every two k-sets meet, and the whole family of C(n, k) sets is intersecting.

4. **Kneser graphs need topology.** The Kneser graph has the k-subsets of an n-set as vertices, with two adjacent when they are disjoint. Its independent sets are intersecting families, so Erdős–Ko–Rado bounds its independence number. Kneser conjectured that its chromatic number is n − 2k + 2. Lovász proved it in 1978 using the Borsuk–Ulam theorem ([fixed-point theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md)), which started topological combinatorics.

5. **Turning sets into vectors gives sharp bounds.** Oddtown: if m subsets of an n-set each have odd size and every two meet in an even number of elements, then m ≤ n. Their indicator vectors over the field with two elements are [linearly independent](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), because their Gram matrix is the identity. This linear algebra method, which comes from layer 04, gives the Frankl–Wilson theorems and the 1993 disproof by Kahn and Kalai of Borsuk's conjecture on dividing sets into pieces of smaller diameter.

6. **Shadows and traces control how families grow.** The Kruskal–Katona theorem gives the smallest possible shadow (the sets one element smaller) of a family of k-sets of given size; families of initial sets in the colexicographic order are best. The Sauer–Shelah lemma says that a family on n points that shatters no d-set has at most C(n, 0) + ⋯ + C(n, d − 1) members. Shattering a set S means cutting out every subset of S. The lemma is the combinatorial core of Vapnik–Chervonenkis dimension in [statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md).

7. **Simple statements can stay open.** Frankl's union-closed sets conjecture (1979) says that if a finite family of sets, not just the empty set, is closed under unions, some element lies in at least half the sets. Gilmer (2022) proved, by an entropy argument, that some element lies in a constant fraction of the sets, and later work raised the fraction. The full conjecture, with one half, is open as of 2026.

## Key concepts
| Term | Meaning |
|---|---|
| Poset | A set with a reflexive, antisymmetric, transitive relation ≤ |
| Chain / antichain | A set of pairwise comparable / pairwise incomparable elements |
| Boolean lattice | All subsets of an n-set, ordered by inclusion |
| LYM inequality | ∑ 1/C(n, ∣A∣) ≤ 1 over an antichain |
| Intersecting family | A family in which every two sets meet |
| Kneser graph | k-sets of an n-set, adjacent when disjoint |
| Shadow | The (k − 1)-subsets of members of a family of k-sets |
| Shattering | A family shatters S when it cuts out every subset of S |

## How it fits
- **Below:** Built on [orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), [binomial coefficients](../01-enumeration/counting-principles-and-binomial-coefficients.md), [König's theorem](../02-graph-theory/matchings-and-network-flows.md) and averaging over random orderings from [finite probability spaces](../03-discrete-probability/finite-probability-spaces.md).
- **Above:** The linear algebra method needs [linear independence](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md); Kneser's conjecture needs [fixed-point theorems](../../07-topology/02-algebraic-topology/fixed-point-theorems.md); shattering feeds [statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md); Dilworth's theorem is a case of [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) duality.
- **Siblings:** [Extremal graph theory](extremal-graph-theory.md) asks the same "how large without a pattern" question for graphs; [Ramsey theory](ramsey-theory.md) is the colouring counterpart, and Dilworth's theorem gives a second proof of the Erdős–Szekeres theorem on monotone subsequences.

## Common misconceptions
- **"The largest antichain is obviously a layer, so Sperner is trivial"**: an antichain may mix sizes, and showing that mixing never helps is the content of the LYM inequality.
- **"Every intersecting family is a star"**: for n > 2k, the largest ones are stars, but there are large non-star intersecting families too, as in the Hilton–Milner theorem.
- **"Extremal set theory is all counting"**: some of its sharpest results need linear algebra, entropy or algebraic topology.

## Go deeper
- Anderson, *Combinatorics of Finite Sets* (1987): Sperner, Erdős–Ko–Rado and Kruskal–Katona with full proofs.
- Babai and Frankl, *Linear Algebra Methods in Combinatorics* (1992): the method of tenet 5, from Oddtown to Borsuk.
- Jukna, *Extremal Combinatorics* (2nd edition, 2011): a survey of methods with computer science applications.
