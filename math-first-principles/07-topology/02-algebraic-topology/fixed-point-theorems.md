# Fixed-Point Theorems

> **Layer:** [07 Topology](../README.md) › [Algebraic Topology](README.md)
> **Builds on:** [Homology](homology.md), [Homotopy and the Fundamental Group](homotopy-and-the-fundamental-group.md), [Compactness](../01-point-set-topology/compactness.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md)
> **Enables:** [Game Theory](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/game-theory.md), [Nonlinear PDEs](../../10-differential-equations-and-dynamics/02-partial-differential-equations/nonlinear-pdes.md), [Convex Sets and Separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md)

## Essence

Stir a cup of coffee and let it settle: some point of the liquid ends where it started. These are instances of Brouwer's fixed-point theorem: every continuous map from a closed disc (or ball) to itself fixes a point. The proof is not a calculation that finds the point; it is an argument that a world without one would contain an impossible object, a retraction of the disc onto its boundary, which homology forbids. Lefschetz turned this into a computable count, Borsuk and Ulam found a cousin about antipodal points, and through Kakutani's version the theorem guarantees that every finite game has an equilibrium.

## Core tenets

1. **Brouwer: every continuous map f: Dⁿ → Dⁿ has a fixed point.** Suppose f(x) ≠ x for every x. Draw the ray from f(x) through x and let r(x) be where it leaves the disc. Then r is continuous, maps Dⁿ onto the sphere Sⁿ⁻¹, and fixes every boundary point: a retraction. But the inclusion Sⁿ⁻¹ → Dⁿ followed by r is the identity of Sⁿ⁻¹, so on homology the identity of Hₙ₋₁(Sⁿ⁻¹) ≅ ℤ would factor through Hₙ₋₁(Dⁿ) = 0, which is impossible. For n = 2 the fundamental group gives the same contradiction, since π₁(S¹) ≅ ℤ cannot factor through the trivial group. It holds for any space homeomorphic to a disc, such as a compact convex body.

2. **Each hypothesis is needed.** Without compactness it fails: x ↦ x + 1 on ℝ, or a map of the open disc pushing every point towards one boundary point. Without the "no holes" condition it fails: a rotation of an annulus or a circle moves every point. Without continuity it fails trivially: on [0, 1], send x to x + 1/2 when x < 1/2, to x − 1/2 when x > 1/2, and 1/2 to 0. In dimension 1 Brouwer is the intermediate value theorem.

3. **Brouwer is existence without construction.** The proof gives no point and no algorithm. Combinatorics supplies one: Sperner's lemma says that a suitably labelled triangulation of a simplex has a fully labelled small simplex, and refining the triangulation squeezes these down onto a fixed point. Computing an approximate Brouwer fixed point is, in general, as hard as a complete class of search problems, so the existence proof hides real computational cost.

4. **Contrast: Banach's theorem is constructive and needs a metric.** A contraction of a complete metric space has exactly one fixed point, found by iterating from any start ([contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md)). Brouwer asks far less of the map, only continuity, but far more of the space, and gives neither uniqueness nor a method. Schauder's theorem extends Brouwer to compact convex subsets of Banach spaces (and to continuous maps with relatively compact image), which is how many existence proofs for [nonlinear PDEs](../../10-differential-equations-and-dynamics/02-partial-differential-equations/nonlinear-pdes.md) go.

5. **Lefschetz counts fixed points with homology.** For a continuous map f of a compact polyhedron X to itself, define the Lefschetz number

   ```
   L(f) = ∑ₙ (−1)ⁿ · trace( f_* : Hₙ(X; ℚ) → Hₙ(X; ℚ) )
   ```

   If L(f) ≠ 0, then f has a fixed point. For a disc, or any contractible polyhedron, only H₀ survives and L(f) = 1, which recovers Brouwer. For the identity map L = χ(X), the [Euler characteristic](the-euler-characteristic.md); so on a space with χ ≠ 0, such as an even-dimensional sphere, every map homotopic to the identity has a fixed point. L(f) depends only on the homotopy class of f.

6. **Borsuk–Ulam: every continuous map Sⁿ → ℝⁿ identifies some pair of antipodal points.** For n = 2: at any moment there are two antipodal places on Earth with the same temperature and the same pressure. The proof idea for n = 1 is the intermediate value theorem applied to g(x) = f(x) − f(−x), which changes sign between x and −x; in general one shows that a map Sⁿ → Sⁿ⁻¹ commuting with the antipodal map cannot exist, a degree or homology argument. Its corollary, the ham sandwich theorem, says that any n finite-volume regions in ℝⁿ can be bisected simultaneously by one hyperplane. It also powers results in combinatorics, such as Lovász's theorem on Kneser graphs.

7. **Kakutani's version gives Nash equilibria.** Kakutani extended Brouwer to set-valued maps: if F assigns to each point of a compact convex set K ⊂ ℝⁿ a non-empty convex subset of K, and the graph of F is closed, then x ∈ F(x) for some x. In a finite game, let F send a profile of mixed strategies to the set of profiles where each player best-responds to the others. Best-response sets are convex and the graph is closed, so a fixed point exists, and a fixed point is exactly a profile where no player gains by deviating. This is Nash's existence theorem ([game theory](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/game-theory.md)).

## Key concepts

| Term | Meaning |
|---|---|
| Fixed point | A point x with f(x) = x |
| Retraction | A continuous map r: X → A onto a subspace with r(a) = a for every a ∈ A |
| No-retraction theorem | There is no retraction of Dⁿ onto its boundary Sⁿ⁻¹ |
| Lefschetz number L(f) | Alternating sum of traces of f on rational homology; non-zero forces a fixed point |
| Sperner's lemma | A combinatorial count that locates approximate fixed points in a triangulated simplex |
| Set-valued map | A rule assigning a set F(x) to each point x; Kakutani's theorem concerns these |

## How it fits

- **Below:** the obstruction comes from [homology](homology.md) and, in the plane, from [the fundamental group](homotopy-and-the-fundamental-group.md); [compactness](../01-point-set-topology/compactness.md) is the hypothesis every counterexample attacks; [Banach's principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) is the metric, constructive counterpart.
- **Above:** Kakutani and Nash in [game theory](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/game-theory.md); Schauder and Leray–Schauder in [nonlinear PDEs](../../10-differential-equations-and-dynamics/02-partial-differential-equations/nonlinear-pdes.md); convexity in [convex sets and separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md).
- **Siblings:** the Lefschetz number of the identity is the [Euler characteristic](the-euler-characteristic.md); lifting arguments from [covering spaces](covering-spaces.md) give the n = 2 case of Borsuk–Ulam.

## Common misconceptions

- **"Brouwer says the fixed point is unique."**: It says only that one exists. The identity map fixes every point.
- **"A fixed-point theorem for the disc works for any bounded set."**: The shape matters: an annulus is compact and bounded, yet a rotation has no fixed point. What counts is the topology (no holes), not the size.
- **"If L(f) = 0, then f has no fixed point."**: The theorem runs one way only. The identity of the torus has L = 0 and fixes everything.

## Go deeper

- John Milnor, *Topology from the Differentiable Viewpoint* (1965): a short, smooth proof of Brouwer through regular values.
- Jiří Matoušek, *Using the Borsuk–Ulam Theorem* (2003): proofs and many combinatorial applications.
- Allen Hatcher, *Algebraic Topology* (2002): the no-retraction theorem, Borsuk–Ulam and the Lefschetz theorem.
