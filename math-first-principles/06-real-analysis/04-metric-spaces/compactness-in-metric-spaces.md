# Compactness in Metric Spaces

> **Layer:** [06 Real Analysis](../README.md) › [Metric Spaces](README.md)
> **Builds on:** [Metric spaces and continuity](metric-spaces-and-continuity.md), [Completeness and the contraction mapping principle](completeness-and-the-contraction-mapping-principle.md), [Sequences and limits](../01-limits-and-convergence/sequences-and-limits.md), [Continuity](../01-limits-and-convergence/continuity.md), [Uniform convergence](../01-limits-and-convergence/uniform-convergence.md)
> **Enables:** [Compactness (topology)](../../07-topology/01-point-set-topology/compactness.md), [Extrema and Lagrange multipliers](../03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md), [Existence of minimisers](../../10-differential-equations-and-dynamics/03-calculus-of-variations/existence-of-minimisers.md), [Existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), [Spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md)

## Essence

A compact space is one in which infinite processes cannot escape: every sequence has a convergent subsequence, and every covering by open sets can be cut down to finitely many. Compactness is the property that makes a closed bounded interval [a, b] so useful, and it is the reason continuous functions on [a, b] attain their extremes and are uniformly continuous. In ℝⁿ the compact sets are exactly the closed bounded ones. In spaces of functions that fails, and the Arzelà–Ascoli theorem says what replaces it. Many existence proofs extract a convergent subsequence from approximate solutions.

## Core tenets

1. **For metric spaces, three definitions of compactness agree.** A metric space K is compact if and only if each of the following holds:
   - every sequence in K has a subsequence converging to a point of K (sequential compactness);
   - every cover of K by open sets has a finite subcover;
   - K is complete and totally bounded: for each ε > 0 it is covered by finitely many balls of radius ε.
   
   The cover form turns local facts into global ones. A continuous function is bounded near each point; finitely many such neighbourhoods cover K, so it is bounded on K. In general [topological spaces](../../07-topology/01-point-set-topology/compactness.md) the sequential and cover forms differ, and the cover form is the one that survives.

2. **Heine–Borel: a subset of ℝⁿ is compact if and only if it is closed and bounded.** Given a bounded sequence, apply Bolzano–Weierstrass to the first coordinate, then to the second along that subsequence, and so on; closedness keeps the limit in the set. Outside ℝⁿ the theorem fails. In ℚ, the set ℚ ∩ [0, 2] is closed and bounded, but the decimals of √2 have no convergent subsequence in it. In the space ℓ² of square-summable sequences, the unit vectors e₁, e₂, … are all at distance √2 from each other, so the closed unit ball is not compact. In C[0, 1] with the sup metric, the sequence xⁿ lies in the closed unit ball but has no uniformly convergent subsequence, because its pointwise limit is discontinuous.

3. **Continuous images of compact sets are compact, which gives the extreme value theorem (EVT).** If xₙ is any sequence in K, some subsequence converges, and continuity carries that convergence to f(xₙ). So f(K) is compact. If f is real-valued, f(K) is closed and bounded and contains its sup and inf: f attains a maximum and a minimum. Each hypothesis is needed. 1/x is unbounded on the non-closed set (0, 1]; x has no maximum on the unbounded set ℝ; a function that jumps can miss its sup. It also shows that all norms on ℝⁿ are equivalent, since each is bounded above and below by positive constants on the compact Euclidean unit sphere.

4. **Continuous functions on compact spaces are uniformly continuous (Heine–Cantor).** Suppose not. Then for some ε there are points xₙ and yₙ with d(xₙ, yₙ) < 1/n but d(f(xₙ), f(yₙ)) ≥ ε. Pass to a subsequence with xₙ → x; then yₙ → x as well, and continuity at x gives a contradiction. Without compactness it fails: 1/x on (0, 1] and x² on ℝ are continuous but not uniformly so.

5. **Arzelà–Ascoli: a family of continuous functions on a compact space has compact closure in the sup metric if and only if it is uniformly bounded and equicontinuous.** Equicontinuous means that for each ε > 0 one δ works for every function in the family at once. Proof idea: choose a countable dense set of points. A diagonal argument extracts a subsequence that converges at each of those points. Then an ε/3 argument, using equicontinuity to pass from the dense set to all points, shows the convergence is uniform. The family sin(nx) on [0, π] is bounded but not equicontinuous, since its slopes grow without bound, and indeed no subsequence converges uniformly.

6. **Compactness is the standard route to existence.** Peano's theorem constructs approximate solutions of y′ = f(t, y) for merely continuous f by joining short straight segments, then uses Arzelà–Ascoli to extract a solution; uniqueness can fail, as y′ = 3y^(2/3) with y(0) = 0 is solved by both 0 and t³. In the [calculus of variations](../../10-differential-equations-and-dynamics/03-calculus-of-variations/existence-of-minimisers.md), a minimising sequence is shown to have a convergent subsequence whose limit is the minimiser. [Compact operators](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md), which map bounded sets to sets with compact closure, have a spectral theory almost as clean as that of matrices.

## Key concepts

| Term | Meaning |
|---|---|
| Sequentially compact | Every sequence has a subsequence converging in the space |
| Open cover | A family of open sets whose union is the whole space |
| Compact | Every open cover has a finite subcover; for metric spaces, equivalent to sequentially compact |
| Totally bounded | Coverable by finitely many ε-balls for every ε > 0 |
| Relatively compact | Having compact closure |
| Uniformly bounded family | All functions bounded by one constant |
| Equicontinuous family | For each ε, one δ serves every function at every point |
| Diagonal argument | Extracting nested subsequences and taking the n-th term of the n-th one |

## How it fits

- **Below:** Bolzano–Weierstrass from [sequences and limits](../01-limits-and-convergence/sequences-and-limits.md) is the seed of Heine–Borel; [continuity](../01-limits-and-convergence/continuity.md) gave the EVT and Heine–Cantor on [a, b], and this leaf proves them for every compact space. [Uniform convergence](../01-limits-and-convergence/uniform-convergence.md) is the convergence in Arzelà–Ascoli, and [completeness](completeness-and-the-contraction-mapping-principle.md) is half of compactness.
- **Above:** [Topology](../../07-topology/01-point-set-topology/compactness.md) makes the cover form the definition. In several variables, the EVT guarantees that [constrained extrema](../03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md) exist before Lagrange multipliers find them. Arzelà–Ascoli underlies Peano's theorem beside [existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), and the theory of [minimisers](../../10-differential-equations-and-dynamics/03-calculus-of-variations/existence-of-minimisers.md).
- **Siblings:** [Metric spaces and continuity](metric-spaces-and-continuity.md) supplies the setting.

## Common misconceptions

- **"Closed and bounded means compact."** Only in ℝⁿ and similar spaces; the unit ball of ℓ² and of C[0, 1] are counterexamples (tenet 2).
- **"Compactness is about being small."** It is about being finite in disguise. ℝ is unbounded and not compact, yet [0, 1] with its infinitely many points is compact.
- **"A bounded sequence of functions has a uniformly convergent subsequence."** sin(nx) does not; equicontinuity is needed (tenet 5).

## Go deeper

- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): compactness in chapter 2 and equicontinuity in chapter 7.
- Terence Tao, *Analysis II* (2006): metric spaces, compactness and uniform convergence in a careful axiomatic style.
- Wilson A. Sutherland, *Introduction to Metric and Topological Spaces* (2nd edition, 2009): the three forms of compactness and their equivalence.
