# Metric Spaces and Continuity

> **Layer:** [06 Real Analysis](../README.md) › [Metric Spaces](README.md)
> **Builds on:** [Sequences and limits](../01-limits-and-convergence/sequences-and-limits.md), [Continuity](../01-limits-and-convergence/continuity.md), [Estimates and inequalities](../01-limits-and-convergence/estimates-and-inequalities.md), [Sets and set operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md)
> **Enables:** [Completeness and the contraction mapping principle](completeness-and-the-contraction-mapping-principle.md), [Compactness in metric spaces](compactness-in-metric-spaces.md), [Topological spaces and continuous maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md), [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), [Separation axioms and metrisability](../../07-topology/01-point-set-topology/separation-axioms-and-metrisability.md)

## Essence

The proofs about limits and continuity in ℝ use almost nothing but the distance |x − y| and the triangle inequality. A metric space keeps exactly that: a set with a distance function obeying three axioms. Every definition from the real line then transfers word for word, to points of ℝⁿ, to functions, to binary strings and to p-adic numbers. Fréchet introduced the idea in his 1906 thesis, and Hausdorff named it in 1914. The open-set description of continuity that falls out of it is the bridge to topology.

## Core tenets

1. **A metric is a distance function with three properties.** A metric on a set X is a function d: X × X → [0, ∞) such that d(x, y) = 0 if and only if x = y; d(x, y) = d(y, x); and d(x, z) ≤ d(x, y) + d(y, z). A sequence xₙ converges to x when d(xₙ, x) → 0. The first axiom makes limits unique: if xₙ tends to both x and y, then d(x, y) ≤ d(x, xₙ) + d(xₙ, y) → 0.

2. **One set can carry many metrics, and on ℝⁿ the standard ones agree.** On ℝⁿ take the sum of coordinate differences d₁, the Euclidean distance d₂, or the largest coordinate difference d∞. Each pair is comparable:
   ```
   d∞ ≤ d₂ ≤ d₁ ≤ n·d∞
   ```
   so the three metrics have the same convergent sequences and the same open sets. Other examples go further. The discrete metric, with d(x, y) = 1 whenever x ≠ y, makes only eventually constant sequences converge. The Hamming distance counts the positions where two strings differ, and underlies [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md). The [p-adic metric](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md) on ℚ makes numbers close when their difference is divisible by a high power of p, and obeys the stronger rule d(x, z) ≤ max(d(x, y), d(y, z)).

3. **On spaces of functions, different metrics give different convergence.** On C[0, 1], the continuous functions on [0, 1], compare the sup metric, the largest value of |f − g|, with the L¹ metric ∫|f − g|. Let fₙ be a tent of height 1 on [0, 2/n]. Then the L¹ distance from fₙ to 0 is 1/n → 0, but the sup distance is always 1. Convergence in the sup metric is exactly [uniform convergence](../01-limits-and-convergence/uniform-convergence.md).

4. **Open and closed sets are defined through balls.** The open ball B(x, r) is the set of points at distance less than r from x. A set U is open when each of its points has a ball around it inside U. A set is closed when its complement is open, which happens if and only if it contains the limit of every convergent sequence of its points. Unions of open sets are open, but the intersection of the intervals (−1/n, 1/n) is {0}, which is not. Openness depends on the ambient space: in ℚ, the set of rationals with x² < 2 is both open and closed.

5. **Continuity has three equivalent forms, and one of them never mentions distance.** For f: X → Y between metric spaces, these are equivalent:
   - for every ε > 0 there is δ > 0 with d(x, a) < δ implying d(f(x), f(a)) < ε (at each a);
   - f(xₙ) → f(a) whenever xₙ → a;
   - the preimage of every open set is open.
   
   The third form mentions only open sets. Taking it as the definition is the step to [topological spaces](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md).

6. **Lipschitz implies uniformly continuous implies continuous, and neither converse holds.** f is Lipschitz with constant L when d(f(x), f(y)) ≤ L·d(x, y), and uniformly continuous when one δ works for every point. √x on [0, 1] is uniformly continuous but not Lipschitz, since its slope is unbounded near 0, and x² on ℝ is continuous but not uniformly so. The distance to a set A, d(x, A) = inf of d(x, a) over a in A, is Lipschitz with constant 1. So disjoint closed sets A and B are separated by the continuous function d(x, A)/(d(x, A) + d(x, B)), which is why every metric space is normal in the sense of [separation axioms](../../07-topology/01-point-set-topology/separation-axioms-and-metrisability.md).

7. **Some metric properties are topological and some are not.** A homeomorphism is a continuous bijection with continuous inverse, and it preserves open sets, convergence and continuity. It need not preserve boundedness: min(d(x, y), 1) has the same open sets as d, yet every set is bounded in it. Nor does it preserve completeness: (0, 1) and ℝ are homeomorphic, but only ℝ is complete, as the [next leaf](completeness-and-the-contraction-mapping-principle.md) shows.

## Key concepts

| Term | Meaning |
|---|---|
| Metric | A distance function: zero only on equal points, symmetric, with the triangle inequality |
| Open ball B(x, r) | The points at distance less than r from x |
| Open set | Contains a ball around each of its points |
| Closed set | Complement is open; equivalently, contains the limits of its convergent sequences |
| Closure | The smallest closed set containing a given set |
| Equivalent metrics | Metrics with the same open sets, and so the same convergent sequences |
| Lipschitz map | d(f(x), f(y)) ≤ L·d(x, y) for a fixed constant L |
| Homeomorphism | A continuous bijection whose inverse is also continuous |
| Ultrametric | A metric with d(x, z) ≤ max(d(x, y), d(y, z)) |

## How it fits

- **Below:** [Sequences and limits](../01-limits-and-convergence/sequences-and-limits.md) and [continuity](../01-limits-and-convergence/continuity.md) supply the definitions being generalised, and [estimates and inequalities](../01-limits-and-convergence/estimates-and-inequalities.md) proves the triangle inequality for d₂ via Cauchy–Schwarz.
- **Above:** [Topology](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) keeps only the open sets; [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md) are normed spaces that are complete; the norm ∥·∥ on ℝⁿ is the setting for [calculus of several variables](../03-calculus-of-several-variables/README.md).
- **Siblings:** [Completeness](completeness-and-the-contraction-mapping-principle.md) and [compactness](compactness-in-metric-spaces.md) are the two properties that make metric spaces behave like closed bounded intervals.

## Common misconceptions

- **"A set that is not open must be closed."** [0, 1) is neither; ∅ and the whole space are both.
- **"If functions are close in one sense, they are close in every sense."** The tents of tenet 3 are close to 0 in L¹ and far from it in the sup metric.
- **"Boundedness is part of the shape of a space."** Replacing d by min(d, 1) bounds every set without changing any open set.

## Go deeper

- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 2 sets up metric spaces as the frame for all of analysis.
- Wilson A. Sutherland, *Introduction to Metric and Topological Spaces* (2nd edition, 2009): from metric spaces to topology in gentle steps.
- Mícheál Ó Searcóid, *Metric Spaces* (2007): a thorough undergraduate treatment with many examples.
