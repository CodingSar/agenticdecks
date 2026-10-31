# Compactness

> **Layer:** [07 Topology](../README.md) › [Point-Set Topology](README.md)
> **Builds on:** [Topological Spaces and Continuous Maps](topological-spaces-and-continuous-maps.md), [Subspaces, Products and Quotients](subspaces-products-and-quotients.md), [Compactness in Metric Spaces](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md), [The Axiom of Choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md)
> **Enables:** [Separation Axioms and Metrisability](separation-axioms-and-metrisability.md), [Fixed-Point Theorems](../02-algebraic-topology/fixed-point-theorems.md), [Functional Analysis](../../09-advanced-analysis/03-functional-analysis/README.md), [Existence of Minimisers](../../10-differential-equations-and-dynamics/03-calculus-of-variations/existence-of-minimisers.md)

## Essence

A space is compact if every cover of it by open sets has a finite subcover. This is the abstraction of "closed and bounded" in ℝⁿ that keeps what existence proofs use: a statement that holds near each point with a local bound holds everywhere with one bound, because finitely many neighbourhoods suffice. Continuous real functions on compact spaces attain their maxima, and this drives existence proofs from the extreme value theorem to minimisers in the calculus of variations. Tychonoff's theorem, that every product of compact spaces is compact, is the deepest result of point-set topology and is equivalent to the axiom of choice.

## Core tenets

1. **Compactness turns local bounds into global ones.** If each point of a compact space X has an open neighbourhood on which a statement holds with some bound, finitely many of these neighbourhoods cover X, and the largest of their bounds works everywhere. So a continuous real function on a compact space is bounded, a continuous function on a compact metric space is uniformly continuous, and every open cover of a compact metric space has a Lebesgue number δ > 0: each set of diameter less than δ lies inside one member of the cover.

2. **In ℝⁿ, compact means closed and bounded (the Heine–Borel theorem).** A compact set is bounded, since finitely many of the balls of radius k about the origin cover it, and closed by tenet 4. Conversely, a closed bounded set lies in a cube, and a cube is compact by bisection: if a cover had no finite subcover, one of the 2ⁿ half-size cubes would also lack one, and the nested cubes shrink to a point inside some member of the cover, which then contains a whole small cube. Completeness of ℝ supplies that point. In ℚ the closed bounded set [0, 2] ∩ ℚ is covered by the open sets {q : |q − √2| > 1/n}, with no finite subcover.

3. **Continuous images of compact spaces are compact, so maxima exist.** An open cover of f(X) pulls back to an open cover of X, and a finite subcover pushes forward. For f: X → ℝ the image is closed and bounded, so it contains its supremum, and f attains its maximum. Both hypotheses matter: the identity on the non-compact (0, 1) has no maximum, and a discontinuous function on [0, 1] can be unbounded.

4. **In a Hausdorff space compact sets are closed, which makes bijections easy to invert.** In a Hausdorff space distinct points have disjoint neighbourhoods. A point x outside a compact set K can be separated from each point of K; finitely many of those neighbourhoods cover K, and the intersection of the matching neighbourhoods of x misses K. Closed subsets of compact spaces are compact. Hence a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism: it maps closed sets to compact sets, which are closed.

5. **Tychonoff's theorem: every product of compact spaces is compact in the product topology.** For two factors an elementary argument (the tube lemma) suffices, and induction handles finitely many. For infinitely many, the proof uses Zorn's lemma to enlarge a family of sets with the finite intersection property to a maximal one, then chooses a limit point in each coordinate. Kelley showed in 1950 that the converse holds: Tychonoff's theorem implies the axiom of choice, so over Zermelo–Fraenkel set theory (ZF) the two are equivalent. For Hausdorff factors the theorem is equivalent to the strictly weaker ultrafilter lemma, and for the box topology it is false.

6. **Outside metric spaces, compactness and sequential compactness come apart.** In a metric space, compact and sequentially compact (every sequence has a convergent subsequence) are equivalent. In general neither implies the other. The product [0, 1]^[0, 1] is compact by Tychonoff, but the sequence fₙ, where fₙ(x) is the n-th binary digit of x, has no pointwise convergent subsequence; the space of countable ordinals is sequentially compact but not compact. Open covers are the right definition because they are what the proofs above use.

7. **Non-compact spaces can be compactified.** Adding one point ∞ to a locally compact Hausdorff space X, with neighbourhoods of ∞ the complements of compact subsets of X, gives a compact Hausdorff space. In this way ℝⁿ becomes the sphere Sⁿ and ℂ becomes the Riemann sphere, and statements "at infinity" become statements about one more point.

## Key concepts

| Term | Meaning |
|---|---|
| Open cover | A family of open sets whose union is the whole space |
| Compact | Every open cover has a finite subcover |
| Finite intersection property | Every finite subfamily has non-empty intersection |
| Lebesgue number | A δ > 0 such that each set of diameter less than δ lies in one member of the cover |
| Sequentially compact | Every sequence has a convergent subsequence |
| Locally compact | Every point has a neighbourhood contained in a compact set |
| One-point compactification | X ∪ {∞}, with neighbourhoods of ∞ the complements of compact sets |

## How it fits

- **Below:** 06 proved that [compactness in metric spaces](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md) is equivalent to sequential compactness; here the open-cover definition is primary. Tychonoff's theorem rests on the [axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md).
- **Above:** Compactness gives [fixed points](../02-algebraic-topology/fixed-point-theorems.md), the compactness of unit balls in weak topologies in [functional analysis](../../09-advanced-analysis/03-functional-analysis/README.md), and [minimisers](../../10-differential-equations-and-dynamics/03-calculus-of-variations/existence-of-minimisers.md). The compactness theorem of propositional [logic](../../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md) is the compactness of the product space {0, 1}^V of truth assignments to the variables V.
- **Siblings:** It uses the product topology of [subspaces, products and quotients](subspaces-products-and-quotients.md), feeds normality in the [separation axioms](separation-axioms-and-metrisability.md), and shares with [connectedness](connectedness.md) the property of surviving continuous images.

## Common misconceptions

- **"Closed and bounded means compact."**: Only in ℝⁿ and spaces like it. The closed unit ball of an infinite-dimensional Hilbert space is closed and bounded, but its orthonormal vectors are all √2 apart, so no subsequence of them converges.
- **"Compact means every sequence has a convergent subsequence."**: That is sequential compactness, and the two agree only for metric spaces and some others.
- **"Tychonoff's theorem is a technicality."**: It is equivalent to the axiom of choice, and it supplies existence proofs across analysis and logic.

## Go deeper

- James Munkres, *Topology* (2nd edition, 2000): the tube lemma and the finite-intersection proof of Tychonoff's theorem.
- John L. Kelley, "The Tychonoff product theorem implies the axiom of choice", *Fundamenta Mathematicae* (1950): the short proof that Tychonoff implies choice.
- John L. Kelley, *General Topology* (1955): compactness through nets and filters.
