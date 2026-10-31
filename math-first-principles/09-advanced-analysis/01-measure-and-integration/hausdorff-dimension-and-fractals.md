# Hausdorff Dimension and Fractals

> **Layer:** [09 Advanced Analysis](../README.md) › [Measure and Integration](README.md)
> **Builds on:** [Measure and σ-Algebras](measure-and-sigma-algebras.md), [Metric Spaces and Continuity](../../06-real-analysis/04-metric-spaces/metric-spaces-and-continuity.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/04-metric-spaces/completeness-and-the-contraction-mapping-principle.md)
> **Enables:** [Iterated Maps](../../10-differential-equations-and-dynamics/04-dynamical-systems/iterated-maps.md), [Chaos and Strange Attractors](../../10-differential-equations-and-dynamics/04-dynamical-systems/chaos-and-strange-attractors.md), [Brownian Motion](../../11-probability-and-statistics/03-stochastic-processes/brownian-motion.md)

## Essence

Length, area and volume suit sets of dimension 1, 2 and 3 and fail on others: a square has infinite length and zero volume. Felix Hausdorff (1918) defined a measure Hˢ for every real s ≥ 0 by covering a set with small pieces and adding up (diameter)ˢ. For each set there is one critical s at which Hˢ jumps from ∞ to 0, and that s is its Hausdorff dimension. It need not be an integer: the Cantor set has dimension log 2/log 3 ≈ 0.631. For self-similar sets, built from N copies of themselves scaled by r, the dimension is log N/log(1/r).

## Core tenets

1. **Hausdorff measure weights small covers by a power of the diameter.** For E in a metric space:

   ```
   Hˢ_δ(E) = inf { ∑ (diam Uᵢ)ˢ  :  E ⊆ U₁ ∪ U₂ ∪ …,  diam Uᵢ ≤ δ }
   Hˢ(E)   = lim_(δ→0) Hˢ_δ(E)
   ```

   This is an outer measure, and [Carathéodory's construction](measure-and-sigma-algebras.md) makes it a measure on which every Borel set is measurable. H⁰ is counting measure, H¹ of a smooth curve is its length, and on ℝⁿ, Hⁿ is a constant multiple of Lebesgue measure. The limit δ → 0 matters: one set covers a circle, so without it H¹ would see only the diameter.

2. **Each set has exactly one critical exponent.** If t > s and every Uᵢ has diameter at most δ, then ∑ (diam Uᵢ)ᵗ ≤ δ^(t−s)·∑ (diam Uᵢ)ˢ. So Hˢ(E) < ∞ forces Hᵗ(E) = 0 for every t > s. Hence Hˢ(E) = ∞ below some value and 0 above it, and that value is the Hausdorff dimension dim_H E. At the critical exponent itself Hˢ(E) can be 0, finite or ∞. A square has H¹ = ∞, H² equal to a multiple of its area, and H³ = 0.

3. **The Cantor set has dimension log 2/log 3.** At stage n the middle-thirds Cantor set is covered by 2ⁿ intervals of length 3⁻ⁿ, so Hˢ is at most 2ⁿ·3^(−ns) = (2/3ˢ)ⁿ, which stays bounded exactly when 3ˢ ≥ 2. That gives dim ≤ log 2/log 3. The lower bound needs control of every cover. Spread unit mass evenly over the set, giving 2⁻ⁿ to each stage-n interval; any set of diameter d then carries mass at most 2dˢ when s = log 2/log 3. A cover of total mass 1 must therefore have ∑ (diam Uᵢ)ˢ ≥ 1/2. This "mass distribution principle" is the general method: one good cover bounds dimension above, an evenly spread measure bounds it below.

4. **Self-similar sets: N copies at ratio r give dimension log N/log(1/r).** If E is the union of N images of itself under similarities of ratio r, and the images do not overlap too much (the open set condition), then dim_H E is the s with N·rˢ = 1. With ratios r₁, …, r_N the equation becomes r₁ˢ + … + r_Nˢ = 1. Overlaps lower the answer: [0, 1] is the union of [0, 2/3] and [1/3, 1], two copies at ratio 2/3, yet its dimension is 1, not log 2/log(3/2) ≈ 1.71.

   | Set | Copies N | Ratio r | Dimension log N/log(1/r) |
   |---|---|---|---|
   | Cantor set | 2 | 1/3 | ≈ 0.631 |
   | Koch curve | 4 | 1/3 | ≈ 1.262 |
   | Sierpiński triangle | 3 | 1/2 | ≈ 1.585 |
   | Unit square | 4 | 1/2 | 2 |

5. **Fractal attractors exist by the contraction mapping principle.** Given contractions f₁, …, f_N of a complete metric space, the map K ↦ f₁(K) ∪ … ∪ f_N(K) is a contraction on the non-empty compact sets. These are measured by the Hausdorff metric, the least ε such that each set lies within ε of the other, and this space is complete. So there is a unique non-empty compact set fixed by the map, the attractor of the iterated function system, and iterating from any compact start converges to it (John Hutchinson, 1981).

6. **Dimension is a metric invariant, not a topological one.** If ∣f(x) − f(y)∣ ≤ L·∣x − y∣ for all x and y (f is Lipschitz), then the image of each cover is a cover with diameters scaled by at most L, so dim f(E) ≤ dim E; bi-Lipschitz maps preserve dimension. Homeomorphisms do not: the Koch curve is homeomorphic to [0, 1] yet has dimension about 1.26. Hausdorff dimension is never below topological dimension. Benoit Mandelbrot coined the word "fractal" (1975), and one working definition calls a set a fractal when its Hausdorff dimension is strictly larger.

7. **Hausdorff dimension is countably stable.** Countable subadditivity of Hˢ gives dim (E₁ ∪ E₂ ∪ …) = sup dim Eₙ, so every countable set has dimension 0. Box-counting dimension, lim log N(δ)/log(1/δ) with N(δ) the number of δ-boxes meeting E, is easier to estimate and agrees for the self-similar sets above, but it is not countably stable: ℚ ∩ [0, 1] is dense, so it has box dimension 1, and countable, so it has Hausdorff dimension 0.

## Key concepts

| Term | Meaning |
|---|---|
| Hausdorff measure Hˢ | The limit as δ → 0 of the cheapest ∑ (diam Uᵢ)ˢ over δ-covers |
| Hausdorff dimension | The exponent at which Hˢ(E) drops from ∞ to 0 |
| Self-similar set | A set that is a union of scaled copies of itself |
| Open set condition | An open set whose images under the similarities are disjoint and inside it |
| Iterated function system | A finite family of contractions; its attractor is the compact set they reproduce |
| Hausdorff metric | The distance between compact sets: the least ε putting each within ε of the other |
| Box-counting dimension | The growth exponent of the number of δ-boxes needed to cover a set |
| Lipschitz map | A map with ∣f(x) − f(y)∣ ≤ L·∣x − y∣ for a constant L |

## How it fits

- **Below:** diameters and covers live in [metric spaces](../../06-real-analysis/04-metric-spaces/metric-spaces-and-continuity.md); attractors exist by the [contraction mapping principle](../../06-real-analysis/04-metric-spaces/completeness-and-the-contraction-mapping-principle.md); the measure comes from [Carathéodory's construction](measure-and-sigma-algebras.md).
- **Above:** Julia sets of [iterated maps](../../10-differential-equations-and-dynamics/04-dynamical-systems/iterated-maps.md) and [strange attractors](../../10-differential-equations-and-dynamics/04-dynamical-systems/chaos-and-strange-attractors.md) have non-integer dimension, and the boundary of the Mandelbrot set has dimension 2 (Mitsuhiro Shishikura, 1998); paths of [Brownian motion](../../11-probability-and-statistics/03-stochastic-processes/brownian-motion.md) in the plane or higher have dimension 2 almost surely.
- **Siblings:** the Cantor measure of tenet 3 is the standard [singular measure](the-radon-nikodym-theorem.md); dimension tells apart the null sets of [Lebesgue measure](measure-and-sigma-algebras.md).

## Common misconceptions

- **"Measure zero means small in every sense"**: the Cantor set, the Koch curve and a line in the plane are all Lebesgue null in their ambient spaces, and dimension separates them.
- **"Dimension is topological"**: the Koch curve and a segment are homeomorphic but have different dimensions.
- **"A fractal must be exactly self-similar"**: Brownian paths and most Julia sets are not, and dimension is defined for every set.

## Go deeper

- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications* (1990): the standard account of how dimensions are computed.
- Benoit B. Mandelbrot, *The Fractal Geometry of Nature* (1982): the book that made fractals a subject.
