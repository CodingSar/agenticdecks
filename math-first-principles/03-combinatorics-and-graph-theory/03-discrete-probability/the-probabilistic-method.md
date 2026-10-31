# The Probabilistic Method

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Discrete Probability](README.md)
> **Builds on:** [Expectation and variance](expectation-and-variance.md), [Finite probability spaces](finite-probability-spaces.md), [Graphs and connectivity](../02-graph-theory/graphs-and-connectivity.md)
> **Enables:** [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md), [Extremal graph theory](../04-extremal-combinatorics/extremal-graph-theory.md), [Information theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md), [Approximation algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md)

## Essence
The probabilistic method proves that an object with some property exists by showing that a randomly chosen object has the property with positive probability. Nothing random is in the conclusion: in a finite space, positive probability means at least one outcome qualifies. The method, pioneered by Erdős, routinely beats every explicit construction, as in his 1947 lower bound for Ramsey numbers, and it comes with a toolkit of increasing strength: the union bound, linearity of expectation, alteration, the second moment method and the Lovász Local Lemma. Its price is that the proof usually gives no way to find the object, and turning such proofs into algorithms is a subject of its own.

## Core tenets
1. **Positive probability means existence.** If a random object from a finite space fails each of the bad events B₁, …, Bₘ, and ∑ P(Bᵢ) < 1, then by the union bound P(no Bᵢ occurs) > 0, so some object avoids them all. The argument is pure counting in disguise: it says the bad objects are fewer than all objects.

2. **Erdős (1947): R(k, k) > ⌊2^(k/2)⌋ for k ≥ 3.** Colour each edge of Kₙ red or blue by a fair coin. A fixed k-set is monochromatic with probability 2^(1 − C(k, 2)), so the expected number of monochromatic k-sets is C(n, k) · 2^(1 − C(k, 2)). For n = ⌊2^(k/2)⌋ this is at most 2^(1 + k/2)/k!, which is below 1 for k ≥ 3, so some colouring has no monochromatic Kₖ. No explicit construction comes close to √2ᵏ; see [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md).

3. **Linearity of expectation gives existence through averages.** Every graph with m edges has a cut, a split of the vertices into two sides, crossed by at least m/2 edges: put each vertex on a random side, so each edge crosses with probability 1/2, the expected number of crossing edges is m/2, and some split achieves at least the mean. The method of conditional expectations derandomises this, placing vertices one at a time on the side that keeps the conditional expectation at least m/2, which yields a fast greedy algorithm.

4. **Alteration: make a random object, then repair it.** Erdős (1959) showed there are graphs with no short cycles and arbitrarily large chromatic number. Take a random graph on n vertices with edge probability n^(θ − 1) for small θ > 0: on average it has fewer than n/2 short cycles and no large independent set, so deleting one vertex from each short cycle leaves a graph with at least n/2 vertices, no short cycles and no independent set of size n/(2k), hence chromatic number above k. Local sparsity does not force global colourability.

5. **The second moment method shows that something occurs, not merely that it can fail to.** For a count X ≥ 0, Chebyshev gives P(X = 0) ≤ Var X/(E[X])², so if the variance is small relative to the squared mean, X > 0 almost surely in the limit. This proves threshold phenomena in the random graph G(n, p), where each edge is present independently with probability p: properties such as containing a triangle appear abruptly as p crosses a threshold (here 1/n), and connectivity appears at p = ln n/n.

6. **The Lovász Local Lemma handles many rare, mostly independent bad events.** If each bad event has probability at most p and is independent of all but at most d others, and e · p · (d + 1) ≤ 1, then with positive probability none occurs, even though the union bound would fail when there are many events. For example, a family of k-element sets, each meeting at most 2^(k−1)/e − 1 others, can be 2-coloured with no monochromatic set. Moser and Tardos (2010) made the lemma algorithmic: resampling the variables of any violated event finds a good outcome quickly.

7. **Random choices beat explicit constructions in coding and computing.** Shannon's channel coding theorem (1948) proves that good codes exist by showing that a random code is good on average; explicit codes approaching capacity took decades more ([information theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md)). Random graphs are expanders with high probability, and randomised rounding gives [approximation algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md).

8. **The method is non-constructive, and that is a real limitation.** A proof that most graphs on 2^(k/2) vertices avoid monochromatic Kₖ gives no efficient way to exhibit one and certify it, because checking all k-sets takes superpolynomial time. Constructive versions exist for some arguments (conditional expectations, Moser–Tardos), but finding explicit objects as good as random ones, such as Ramsey graphs, remains a major research direction.

## Key concepts
| Term | Meaning |
|---|---|
| Probabilistic method | Proving existence by showing positive probability |
| Union bound | P(B₁ ∪ ⋯ ∪ Bₘ) ≤ ∑ P(Bᵢ) |
| Averaging principle | Some outcome is at least the expectation |
| Alteration | Delete or repair the few defects of a random object |
| Second moment method | P(X = 0) ≤ Var X/(E[X])² |
| Random graph G(n, p) | n vertices, each edge present independently with probability p |
| Threshold | The value of p at which a property switches from unlikely to likely |
| Lovász Local Lemma | Positive probability of avoiding many rare, mostly independent bad events |
| Derandomisation | Converting a probabilistic existence proof into a deterministic algorithm |

## How it fits
- **Below:** The tools are the union bound from [finite probability spaces](finite-probability-spaces.md) and linearity and Chebyshev from [expectation and variance](expectation-and-variance.md); the objects are mostly [graphs](../02-graph-theory/graphs-and-connectivity.md).
- **Above:** Sharper tails come from [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md); random codes from [information theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md); random matrices and high-dimensional geometry from [data and learning](../../14-applied-and-computational-mathematics/06-data-and-learning/high-dimensional-geometry-and-random-matrices.md).
- **Siblings:** The method is the main source of lower bounds in [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md) and [extremal graph theory](../04-extremal-combinatorics/extremal-graph-theory.md), where it shows that bounds proved by counting are close to the truth.

## Common misconceptions
- **"A probabilistic proof only shows the statement is likely"**: the conclusion is certain: an event of positive probability in a finite space contains an actual outcome.
- **"If random objects work, writing one down is easy"**: random graphs are almost all good Ramsey graphs, yet no explicit construction matches them.
- **"The union bound is too crude to be useful"**: it already gives Erdős's exponential Ramsey bound; when it fails because events are too many, the Local Lemma often succeeds.

## Go deeper
- Alon and Spencer, *The Probabilistic Method* (4th edition, 2016): the standard text, from first-moment arguments to martingales and the Local Lemma.
- Mitzenmacher and Upfal, *Probability and Computing* (2nd edition, 2017): the method as a tool for designing and analysing algorithms.
- Aigner and Ziegler, *Proofs from THE BOOK* (1998): short probabilistic proofs among the most elegant in combinatorics.
