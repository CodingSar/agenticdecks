# Banach Spaces

> **Layer:** [09 Advanced Analysis](../README.md) › [Functional Analysis](README.md)
> **Builds on:** [Lᵖ Spaces](../01-measure-and-integration/lp-spaces.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [Compactness in Metric Spaces](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md), [Dual Spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md), [Linear Maps and Matrices](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md)
> **Enables:** [Hilbert Spaces](hilbert-spaces.md), [Hahn–Banach and Baire Category](hahn-banach-and-baire-category.md), [Spectral Theory](spectral-theory.md), [Existence and Uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), [Weak Solutions and Sobolev Spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md)

## Essence

A Banach space is a vector space with a norm, a notion of length, in which every Cauchy sequence converges. It is the setting in which linear algebra meets analysis: functions become points, operators such as integration become linear maps, and equations become questions about whether a map is invertible. Completeness is what lets limiting arguments work, from fixed-point iterations to infinite series of operators. The price of infinite dimensions is that much of linear algebra fails: linear maps need not be continuous, the unit ball is not compact, and the dual space must be defined with care.

## Core tenets

1. **A norm turns a vector space into a metric space, and completeness is extra.** A norm satisfies ‖x‖ = 0 only for x = 0, ‖λx‖ = ∣λ∣·‖x‖ and ‖x + y‖ ≤ ‖x‖ + ‖y‖. The standard examples are C[0,1] with ‖f‖_∞ = sup ∣f∣, the [Lᵖ spaces](../01-measure-and-integration/lp-spaces.md), the sequence spaces ℓᵖ, and c₀, the sequences tending to 0 with the sup norm. Completeness depends on the norm, not only on the space: C[0,1] with the L¹ norm ∫∣f∣ is not complete, because continuous functions that ramp ever more steeply from 0 to 1 form a Cauchy sequence whose limit is a step function.

2. **Completeness is the convergence of absolutely convergent series.** A normed space is complete if and only if every series with ∑‖xₙ‖ < ∞ converges. One direction is the triangle inequality on partial sums; for the other, pass to a subsequence of a Cauchy sequence whose successive gaps sum to a finite number. This form is the practical one: it is how one proves Lᵖ complete and how one sums the Neumann series in tenet 5.

3. **For linear maps, bounded and continuous are the same.** A linear map T is bounded if ‖Tx‖ ≤ C·‖x‖ for some C; the least such C is the operator norm ‖T‖. Continuity at 0 gives a ball mapped into the unit ball, and scaling gives the bound; the bound gives Lipschitz continuity. In finite dimensions every linear map is bounded. In infinite dimensions the most natural operators are not: differentiation on C¹[0,1] with the sup norm sends xⁿ, of norm 1, to n·xⁿ⁻¹, of norm n.

4. **The unit ball is compact if and only if the dimension is finite.** On a finite-dimensional space all norms are equivalent, so the Heine–Borel theorem applies. In infinite dimensions Riesz's lemma gives, for any closed proper subspace M, a unit vector at distance at least ½ from M; repeating it builds a sequence of unit vectors with pairwise distances at least ½, which has no convergent subsequence. In ℓ² the standard basis vectors are at mutual distance √2. So existence proofs by [compactness](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md) need a substitute: [compact operators](compact-operators-and-fredholm-theory.md), or weaker topologies.

5. **Bounded operators form a Banach space, and small perturbations of invertible ones are invertible.** If Y is complete, the space B(X, Y) of bounded operators with the operator norm is complete. If ‖T‖ < 1 on a Banach space, the Neumann series I + T + T² + ⋯ converges by tenet 2 and inverts I − T, exactly as 1/(1 − t) = ∑ tⁿ. Hence the invertible operators form an open set, the fact on which [spectral theory](spectral-theory.md) is built.

6. **The dual space X′ consists of the bounded linear functionals.** It is always a Banach space, by tenet 5 with Y = ℝ or ℂ. Hölder's inequality identifies many duals: (ℓᵖ)′ = ℓ^q with 1/p + 1/q = 1 for 1 ≤ p < ∞, (c₀)′ = ℓ¹ and (ℓ¹)′ = ℓ^∞. But (ℓ^∞)′ is strictly larger than ℓ¹; it contains limits along ultrafilters, whose existence needs the axiom of choice. A space is reflexive if the natural map into its double dual X′′ is onto: ℓᵖ for 1 < p < ∞ is, while ℓ¹, c₀ and C[0,1] are not. The [Hahn–Banach theorem](hahn-banach-and-baire-category.md) guarantees that X′ is large enough to separate points.

7. **Weak topologies restore compactness.** A sequence converges weakly if every functional converges on it. The Banach–Alaoglu theorem says that the closed unit ball of X′ is compact in the weak-∗ topology, convergence when tested against each x in X. In a reflexive space every bounded sequence has a weakly convergent subsequence. This is the standard way to find minimisers and [weak solutions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) of differential equations: take a minimising sequence, extract a weak limit, and show the limit works.

8. **Completeness turns iteration into existence.** The [contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) on the Banach space of continuous functions proves the Picard–Lindelöf theorem: for a Lipschitz right-hand side, the map y ↦ y₀ + ∫ F(s, y(s)) ds is a contraction on a short interval, so the [ordinary differential equation](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md) has exactly one solution. Not everything familiar survives: Per Enflo showed in 1973 that some separable Banach spaces have no Schauder basis, a sequence through which every vector expands uniquely.

## Key concepts

| Term | Meaning |
|---|---|
| Norm | A length function: positive, homogeneous and satisfying the triangle inequality |
| Banach space | A complete normed vector space |
| Bounded operator | A linear map with ‖Tx‖ ≤ C·‖x‖; the same as continuous |
| Operator norm | ‖T‖ = sup ‖Tx‖ over ‖x‖ ≤ 1 |
| Dual space X′ | The Banach space of bounded linear functionals on X |
| Reflexive | The natural map X → X′′ is onto |
| Weak convergence | f(xₙ) → f(x) for every f in X′ |
| Neumann series | (I − T)⁻¹ = ∑ Tⁿ when ‖T‖ < 1 |

## How it fits

- **Below:** [completeness](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) and [compactness](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md) from 06; [dual spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md) and [linear maps](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md) from 04; the [Lᵖ spaces](../01-measure-and-integration/lp-spaces.md) as examples.
- **Above:** [existence for ordinary differential equations](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md) and [Sobolev spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) in 10; [numerical stability](../../14-applied-and-computational-mathematics/01-numerical-analysis/floating-point-conditioning-and-stability.md) in 14 uses operator norms.
- **Siblings:** [Hilbert spaces](hilbert-spaces.md) are the Banach spaces with an inner product; [Hahn–Banach and Baire](hahn-banach-and-baire-category.md) supply the big theorems; [spectral theory](spectral-theory.md) studies when T − λ is invertible.

## Common misconceptions

- **"Every linear map is continuous"**: true in finite dimensions only; differentiation is an unbounded linear map.
- **"Closed and bounded means compact"**: the unit ball of any infinite-dimensional space is closed, bounded and not compact.
- **"A basis means a Hamel basis"**: in a Banach space one expands vectors in infinite series; an algebraic basis of an infinite-dimensional Banach space is uncountable.

## Go deeper

- Haïm Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations* (2011): Banach spaces aimed at differential equations.
- Peter D. Lax, *Functional Analysis* (2002): a broad, opinionated course with many applications.
- Erwin Kreyszig, *Introductory Functional Analysis with Applications* (1978): a gentle first pass with full details.
