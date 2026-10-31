# Hahn–Banach and Baire Category

> **Layer:** [09 Advanced Analysis](../README.md) › [Functional Analysis](README.md)
> **Builds on:** [Banach Spaces](banach-spaces.md), [The Axiom of Choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [Convex Sets and Separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md)
> **Enables:** [Spectral Theory](spectral-theory.md), [Fourier Series](../04-harmonic-analysis/fourier-series.md), [Convex Optimisation and Duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md), [Numerical Methods for Differential Equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md)

## Essence

Four theorems carry most of the weight of functional analysis. The Hahn–Banach theorem says there are enough continuous linear functionals: any functional on a subspace extends to the whole space without growing, and convex sets can be separated by hyperplanes. It rests on the axiom of choice. The other three, uniform boundedness, open mapping and closed graph, rest on the Baire category theorem, which says a complete metric space is not a countable union of thin sets. Together they turn qualitative information into quantitative bounds.

## Core tenets

1. **Hahn–Banach: functionals extend without increasing their size.** Let p be sublinear on a real vector space X, meaning p(x + y) ≤ p(x) + p(y) and p(tx) = t·p(x) for t ≥ 0. If f is linear on a subspace M with f ≤ p there, then f extends to a linear F on X with F ≤ p everywhere. Proof idea: extending to one more dimension, M + ℝx₀, requires a value c = F(x₀) squeezed between a supremum and an infimum, and sublinearity shows the supremum does not exceed the infimum. Zorn's lemma then extends to all of X. Hans Hahn and Stefan Banach proved it independently in the late 1920s.

2. **Hahn–Banach needs some choice and gives separation.** Without the [axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) the theorem can fail in general spaces, although it is weaker than the full axiom and needs no choice in separable spaces, where induction along a dense sequence suffices. Its geometric form says that a closed convex set and a point outside it in a normed space are separated by a closed hyperplane, extending [finite-dimensional separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md). Consequences: X′ separates points, ‖x‖ = max over ‖f‖ ≤ 1 of ∣f(x)∣, and X embeds isometrically in X′′. Duality in [convex optimisation](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md) is a separation argument.

3. **Baire: a complete metric space is not a countable union of nowhere dense sets.** Equivalently, a countable intersection of dense open sets is dense. Proof idea: given dense open sets U₁, U₂, …, pick a closed ball inside U₁, a smaller closed ball inside it and inside U₂, and so on, with radii tending to 0. The centres form a Cauchy sequence, and its limit lies in every Uₙ. Completeness is essential: ℚ is the countable union of its points, each nowhere dense.

4. **Uniform boundedness: pointwise bounded families of operators are uniformly bounded.** If X is a Banach space and a family of bounded operators Tₐ satisfies sup ‖Tₐx‖ < ∞ for each x, then sup ‖Tₐ‖ < ∞. Proof idea: the sets {x : ‖Tₐx‖ ≤ n for all a} are closed and cover X, so by Baire one contains a ball, and linearity spreads the bound everywhere. Banach and Steinhaus published it in 1927. Its most famous use is negative: the partial Fourier sums at 0 are functionals on C(𝕋) with norms, the Lebesgue constants, growing like (4/π²)·log n, so some continuous function has a [Fourier series](../04-harmonic-analysis/fourier-series.md) diverging at 0. Completeness matters: on the incomplete space of finitely supported sequences, the functionals x ↦ n·xₙ are pointwise bounded but not uniformly.

5. **Open mapping: a bounded surjection between Banach spaces is open.** If T : X → Y is bounded, linear and onto, with X and Y complete, then T maps open sets to open sets. Proof idea: Y is the union of the closures of T(n·ball), so by Baire one has interior; an iteration that uses the completeness of X removes the closure. The corollary is the bounded inverse theorem: a bounded linear bijection of Banach spaces has bounded inverse. Without completeness it fails: the identity from C[0,1] with the sup norm to C[0,1] with the L¹ norm is a bounded bijection whose inverse is unbounded, because a tall thin spike has small integral and large maximum.

6. **Closed graph: closed graph implies bounded.** A linear map T between Banach spaces whose graph {(x, Tx)} is closed in X × Y is bounded. Proof idea: the graph is a Banach space, and projection from it onto X is a bounded bijection, whose inverse is bounded by the open mapping theorem. In practice one checks only that xₙ → x and Txₙ → y imply y = Tx. Differentiation from C¹ to C has closed graph, which is consistent: C¹[0,1] with the sup norm is not complete.

7. **Baire proves existence by abundance.** In C[0,1], the functions with a derivative at some point lie in a countable union of nowhere dense sets, so the nowhere differentiable continuous functions are generic, as Banach and Mazurkiewicz showed in 1931. Weierstrass had exhibited one in 1872.

8. **Stability is boundedness.** The Lax equivalence theorem in [numerical analysis](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) says that a consistent scheme for a well-posed linear problem converges if and only if it is stable. That convergence implies stability is uniform boundedness: convergence for every initial datum makes the solution operators pointwise bounded.

## Key concepts

| Term | Meaning |
|---|---|
| Sublinear functional | p(x + y) ≤ p(x) + p(y) and p(tx) = t·p(x) for t ≥ 0 |
| Hahn–Banach theorem | Dominated linear functionals extend to the whole space |
| Separating hyperplane | {f = c} with a convex set on one side and a point on the other |
| Nowhere dense set | A set whose closure has empty interior |
| Baire category theorem | A complete metric space is not a countable union of nowhere dense sets |
| Uniform boundedness principle | Pointwise bounded operator families on a Banach space are norm bounded |
| Open mapping theorem | Bounded surjections of Banach spaces are open |
| Closed graph theorem | A linear map with closed graph between Banach spaces is bounded |

## How it fits

- **Below:** [completeness](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) for Baire; [Zorn's lemma](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) for Hahn–Banach; [convex separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md) in finite dimensions; [Banach spaces](banach-spaces.md) for the setting.
- **Above:** [convex duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md) and [numerical stability](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) in 14; a priori estimates for [partial differential equations](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) in 10.
- **Siblings:** [spectral theory](spectral-theory.md) uses Hahn–Banach to show the spectrum is non-empty and the bounded inverse theorem to define it; [Fourier series](../04-harmonic-analysis/fourier-series.md) meet uniform boundedness in the divergence of partial sums; [distributions](../04-harmonic-analysis/distributions.md) are functionals extended by these methods.

## Common misconceptions

- **"Baire category is about measure"**: a residual set can have measure zero; category and measure are independent notions of size.
- **"Hahn–Banach is constructive"**: in general it needs a form of choice, and the extension is rarely unique.
- **"A bijective bounded operator obviously has bounded inverse"**: only between complete spaces.

## Go deeper

- Walter Rudin, *Functional Analysis* (2nd edition, 1991): the four theorems in full generality, including topological vector spaces.
- John C. Oxtoby, *Measure and Category* (2nd edition, 1980): how Baire category and measure compare.
