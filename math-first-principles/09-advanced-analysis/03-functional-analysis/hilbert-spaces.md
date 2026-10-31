# Hilbert Spaces

> **Layer:** [09 Advanced Analysis](../README.md) › [Functional Analysis](README.md)
> **Builds on:** [Banach Spaces](banach-spaces.md), [Inner Products and Orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md), [Lᵖ Spaces](../01-measure-and-integration/lp-spaces.md), [Convex Sets and Separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md)
> **Enables:** [Spectral Theory](spectral-theory.md), [Fourier Series](../04-harmonic-analysis/fourier-series.md), [Weak Solutions and Sobolev Spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [Conditional Expectation](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md)

## Essence

A Hilbert space is a Banach space whose norm comes from an inner product ⟨x, y⟩, so that lengths and angles both make sense. It is the infinite-dimensional space in which Euclidean geometry still works: every closed subspace has an orthogonal complement, every point has a nearest point in a closed convex set, every bounded functional is an inner product with a fixed vector, and every vector expands in an orthonormal basis with Pythagoras' theorem intact. Up to isomorphism there is only one separable infinite-dimensional Hilbert space, ℓ², so L² functions, Fourier coefficients and quantum states all live in the same place.

## Core tenets

1. **The parallelogram law characterises inner-product norms.** In any inner-product space ‖x + y‖² + ‖x − y‖² = 2‖x‖² + 2‖y‖², by expanding both squares. Conversely, a norm satisfying this law comes from an inner product, recovered by polarisation. Among the Lᵖ spaces only L² satisfies it: in ℓᵖ with x = (1, 0) and y = (0, 1), the law reads 2·2^(2/p) = 4, which holds only for p = 2. So L² is the one Lᵖ space with geometry.

2. **Nearest points exist in closed convex sets.** If C is a non-empty closed convex subset of a Hilbert space H and x ∈ H, there is exactly one point of C nearest to x. Proof idea: take a sequence yₙ in C with ‖x − yₙ‖ tending to the infimum d. The parallelogram law applied to x − yₙ and x − yₘ, together with (yₙ + yₘ)/2 ∈ C, shows ‖yₙ − yₘ‖² ≤ 2‖x − yₙ‖² + 2‖x − yₘ‖² − 4d², which tends to 0. Completeness gives a limit, closedness puts it in C. Every hypothesis is needed: in ℓ¹ or C[0,1] nearest points can fail to exist or be non-unique, without convexity uniqueness fails, and without closedness the infimum need not be attained.

3. **Orthogonal projection splits the space.** For a closed subspace M, the nearest point Px to x satisfies x − Px ⊥ M, and H = M ⊕ M^⊥. The map P is linear, P² = P and ‖P‖ ≤ 1. In a Banach space, by contrast, a closed subspace need not have any closed complement; c₀ inside ℓ^∞ has none. Least squares, the best approximation by a subspace, is this projection, and in probability [conditional expectation](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md) of an L² random variable is projection onto the functions measurable with respect to a smaller σ-algebra.

4. **The Riesz representation theorem: H′ is H.** Every bounded linear functional φ on H has the form φ(x) = ⟨x, y⟩ for exactly one y, with ‖φ‖ = ‖y‖. Proof idea: the kernel of a non-zero φ is a closed subspace whose orthogonal complement is one-dimensional, spanned by some z; take y to be the multiple of z with ⟨z, y⟩ = φ(z). Frigyes Riesz and Maurice Fréchet published it independently in 1907. Completeness matters: on the incomplete space of polynomials with the L² norm, the functional "inner product with e^x" has no representing polynomial. The Lax–Milgram theorem, a version for non-symmetric forms, gives [weak solutions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) of elliptic equations.

5. **Orthonormal bases give coordinates with Pythagoras intact.** An orthonormal set {eₐ} satisfies Bessel's inequality ∑ ∣⟨x, eₐ⟩∣² ≤ ‖x‖², because the projection onto finitely many eₐ has smaller norm than x. The set is an orthonormal basis if its span is dense, and then x = ∑ ⟨x, eₐ⟩eₐ with Parseval's identity ‖x‖² = ∑ ∣⟨x, eₐ⟩∣². Zorn's lemma shows every Hilbert space has one. The sum is a convergent infinite series, not a finite combination; an algebraic (Hamel) basis of an infinite-dimensional Hilbert space is uncountable and useless for analysis.

6. **Every separable Hilbert space is ℓ².** A separable infinite-dimensional Hilbert space has a countable orthonormal basis (apply Gram–Schmidt to a dense sequence), and x ↦ (⟨x, eₙ⟩) is a unitary isomorphism onto ℓ². The most important instance is L²(𝕋) ≅ ℓ²(ℤ) by the functions e^(inx)/√(2π): a square-integrable function on the circle is the same thing as a square-summable sequence of [Fourier coefficients](../04-harmonic-analysis/fourier-series.md). Non-separable Hilbert spaces exist, with uncountable bases, but rarely arise.

7. **Bounded sets are weakly compact.** The orthonormal vectors eₙ satisfy ‖eₙ − eₘ‖ = √2, so they have no norm-convergent subsequence, but ⟨eₙ, y⟩ → 0 for every y by Bessel's inequality, so eₙ → 0 weakly. In general every bounded sequence in a Hilbert space has a weakly convergent subsequence. Norm is only lower semicontinuous under weak limits: ‖eₙ‖ = 1 while the weak limit has norm 0. Energy can escape to infinitely many dimensions, a theme of variational problems in 10.

## Key concepts

| Term | Meaning |
|---|---|
| Hilbert space | A complete inner-product space |
| Parallelogram law | ‖x + y‖² + ‖x − y‖² = 2‖x‖² + 2‖y‖² |
| Orthogonal complement M^⊥ | All vectors orthogonal to every vector in M |
| Orthogonal projection | The nearest-point map onto a closed subspace |
| Riesz representation | Every bounded functional is ⟨·, y⟩ for a unique y |
| Orthonormal basis | An orthonormal set with dense span |
| Parseval's identity | ‖x‖² = ∑ ∣⟨x, eₐ⟩∣² for an orthonormal basis |
| ℓ² | Square-summable sequences; the model separable Hilbert space |
| Unitary operator | A linear bijection preserving inner products |

## How it fits

- **Below:** [inner products](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md) and Gram–Schmidt from 04; [convex sets](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md) from 08; [Banach spaces](banach-spaces.md) and [L²](../01-measure-and-integration/lp-spaces.md) in this layer.
- **Above:** [quantum states](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) are unit vectors in a Hilbert space; [Sobolev spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) Hᵏ are Hilbert spaces; [conditional expectation](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md) and [linear regression](../../11-probability-and-statistics/04-statistical-inference/linear-models-and-regression.md) in 11 are projections.
- **Siblings:** [spectral theory](spectral-theory.md) diagonalises self-adjoint operators in orthonormal bases; [Fourier series](../04-harmonic-analysis/fourier-series.md) are expansions in the basis e^(inx); von Neumann's proof of the [Radon–Nikodym theorem](../01-measure-and-integration/the-radon-nikodym-theorem.md) is a Riesz representation.

## Common misconceptions

- **"An orthonormal basis spans the space"**: its finite linear combinations are only dense; vectors are infinite sums.
- **"Bounded sequences have convergent subsequences"**: only weakly; the basis vectors eₙ have no norm-convergent subsequence.
- **"Every Banach space is a Hilbert space with some other inner product"**: Lᵖ for p ≠ 2 has no equivalent inner-product norm.

## Go deeper

- Elias M. Stein and Rami Shakarchi, *Real Analysis* (2005): Hilbert spaces arising from L² and Fourier series.
- Haïm Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations* (2011): projections, Lax–Milgram and their use in equations.
- Nicholas Young, *An Introduction to Hilbert Space* (1988): a short, clear first course.
