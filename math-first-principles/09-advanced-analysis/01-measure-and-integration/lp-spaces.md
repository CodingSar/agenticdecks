# Lᵖ Spaces

> **Layer:** [09 Advanced Analysis](../README.md) › [Measure and Integration](README.md)
> **Builds on:** [The Lebesgue Integral](the-lebesgue-integral.md), [Estimates and Inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/04-metric-spaces/completeness-and-the-contraction-mapping-principle.md)
> **Enables:** [Banach Spaces](../03-functional-analysis/banach-spaces.md), [Hilbert Spaces](../03-functional-analysis/hilbert-spaces.md), [Fourier Series](../04-harmonic-analysis/fourier-series.md), [Weak Solutions and Sobolev Spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), [Modes of Convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md)

## Essence

For 1 ≤ p < ∞, the space Lᵖ(μ) consists of the measurable functions f with ∫ ∣f∣ᵖ dμ < ∞, measured by the norm ‖f‖ₚ = (∫ ∣f∣ᵖ dμ)^(1/p); L^∞ consists of the functions bounded outside a null set. They are the first infinite-dimensional spaces in which analysis can be done as in ℝⁿ: functions are points, and the distance between two functions is a number. Two inequalities, Hölder's and Minkowski's, make ‖·‖ₚ a norm, and the Riesz–Fischer theorem makes the space complete, the property that spaces of Riemann integrable functions lack. Large p penalises tall peaks; small p penalises wide spread.

## Core tenets

1. **An element of Lᵖ is a class of functions, not a function.** Since ∫ ∣f∣ᵖ = 0 only forces f = 0 almost everywhere, ‖·‖ₚ is a norm only after identifying functions that agree almost everywhere. So an L² function has no value at a single point. The norm on L^∞ is the essential supremum, the least M with ∣f∣ ≤ M almost everywhere; on a finite measure space ‖f‖ₚ → ‖f‖_∞ as p → ∞.

2. **Hölder's inequality: ‖fg‖₁ ≤ ‖f‖ₚ·‖g‖_q whenever 1/p + 1/q = 1.** The proof starts from Young's inequality ab ≤ aᵖ/p + b^q/q for a, b ≥ 0, which is the concavity of log: log(aᵖ/p + b^q/q) ≥ (1/p)·log aᵖ + (1/q)·log b^q = log ab. Normalise to ‖f‖ₚ = ‖g‖_q = 1, apply Young pointwise to ∣f∣ and ∣g∣, and integrate to get ∫ ∣fg∣ ≤ 1/p + 1/q = 1. The case p = q = 2 is the Cauchy–Schwarz inequality, and p = 1 pairs with q = ∞.

3. **Minkowski's inequality ‖f + g‖ₚ ≤ ‖f‖ₚ + ‖g‖ₚ holds for p ≥ 1 and fails for p < 1.** Split ∣f + g∣ᵖ ≤ ∣f∣·∣f + g∣^(p−1) + ∣g∣·∣f + g∣^(p−1) and apply Hölder with exponents p and p/(p − 1) to each term. For 0 < p < 1, take f = 1_[0, 1/2] and g = 1_(1/2, 1] on [0, 1]: then ‖f‖ₚ + ‖g‖ₚ = 2^(1 − 1/p) < 1 = ‖f + g‖ₚ. The unit ball is then not convex, and ‖·‖ₚ is not a norm.

4. **Riesz–Fischer: every Lᵖ is complete.** For 1 ≤ p ≤ ∞, every Cauchy sequence in Lᵖ(μ) converges in Lᵖ, and a subsequence converges almost everywhere; Frigyes Riesz and Ernst Fischer proved the case p = 2 in 1907. Proof idea: pass to a subsequence g_k with ‖g_(k+1) − g_k‖ₚ < 2^(−k). The function G = ∣g₁∣ + ∑ ∣g_(k+1) − g_k∣ has ‖G‖ₚ ≤ ‖g₁‖ₚ + 1 by Minkowski and monotone convergence, so G is finite almost everywhere. The telescoping series then converges almost everywhere, and dominated convergence, with G as bound, upgrades this to convergence in norm. Riemann integrable functions with the L¹ distance are not complete: step functions converge in L¹ to the indicator of a Cantor set of positive measure, which is discontinuous on a set of positive measure.

5. **Which Lᵖ contains which depends on the measure.** On a finite measure space Hölder gives ‖f‖ₚ ≤ μ(X)^(1/p − 1/q)·‖f‖_q for p ≤ q, so L^q ⊆ Lᵖ. For sequences with counting measure the order reverses, ℓᵖ ⊆ ℓ^q, because the terms of a sequence in ℓᵖ eventually have absolute value below 1. On ℝ there is no inclusion either way:

   ```
   x^(−1/2) on (0, 1]:   in L¹ (integral 2),  not in L² (∫ 1/x = ∞)      local singularity
   1/x on [1, ∞):        in L² (integral 1),  not in L¹ (∫ 1/x = ∞)      slow decay
   ```

6. **Convergence in norm and convergence almost everywhere differ.** The "typewriter" sequence runs indicators of [0, 1/2], [1/2, 1], [0, 1/3], [1/3, 2/3], [2/3, 1], … across [0, 1]. Their norms tend to 0, yet every point is covered infinitely often, so the sequence converges at no point. Conversely n·1_(0, 1/n) tends to 0 everywhere while its L¹ norm stays 1. The link is the one in the Riesz–Fischer proof: norm convergence gives a subsequence converging almost everywhere.

7. **The dual of Lᵖ is L^q.** Each g ∈ L^q defines the bounded linear functional f ↦ ∫ fg dμ, of norm exactly ‖g‖_q: Hölder gives the upper bound, and for q < ∞ the function f = ∣g∣^(q−1) times the sign of g attains it. Conversely, every bounded functional on Lᵖ has this form when 1 < p < ∞, and also when p = 1 if μ is σ-finite; the proof constructs g by the [Radon–Nikodym theorem](the-radon-nikodym-theorem.md). When Lᵖ is infinite-dimensional, the dual of L^∞ is strictly larger than L¹, which is why L¹ and L^∞ are not reflexive while Lᵖ for 1 < p < ∞ is.

8. **Only L² comes from an inner product.** A norm comes from an inner product if and only if it satisfies the parallelogram law ‖f + g‖² + ‖f − g‖² = 2‖f‖² + 2‖g‖². For the two indicators of tenet 3 the left side is 2 and the right side is 2^(2 − 2/p), equal only at p = 2. So L² is the one [Hilbert space](../03-functional-analysis/hilbert-spaces.md) in the family, with ⟨f, g⟩ = ∫ f·ḡ dμ, where ḡ is the complex conjugate.

## Key concepts

| Term | Meaning |
|---|---|
| Lᵖ(μ) | Classes of measurable f with ∫ ∣f∣ᵖ dμ < ∞, equal almost everywhere |
| ‖f‖ₚ | (∫ ∣f∣ᵖ dμ)^(1/p), the p-norm |
| Essential supremum | The least M with ∣f∣ ≤ M almost everywhere; the norm of L^∞ |
| ℓᵖ | Lᵖ of counting measure on ℕ: sequences with ∑ ∣aₙ∣ᵖ < ∞ |
| Conjugate exponents | p and q with 1/p + 1/q = 1 |
| Hölder's inequality | ‖fg‖₁ ≤ ‖f‖ₚ·‖g‖_q for conjugate p and q |
| Minkowski's inequality | The triangle inequality for ‖·‖ₚ, valid for p ≥ 1 |
| Riesz–Fischer theorem | Lᵖ is complete for 1 ≤ p ≤ ∞ |
| Reflexive | Equal to the dual of its dual under the natural map |

## How it fits

- **Below:** the [Lebesgue integral](the-lebesgue-integral.md) defines the norms; Young, Jensen and Cauchy–Schwarz come from [estimates and inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md); completeness is the notion from [metric spaces](../../06-real-analysis/04-metric-spaces/completeness-and-the-contraction-mapping-principle.md).
- **Above:** [Banach spaces](../03-functional-analysis/banach-spaces.md) abstract the Lᵖ family; [Sobolev spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) in 10 put derivatives in Lᵖ; [Fourier series](../04-harmonic-analysis/fourier-series.md) converge in L²; convergence in Lᵖ is one of the [modes of convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md) of random variables.
- **Siblings:** the [Radon–Nikodym theorem](the-radon-nikodym-theorem.md) identifies the dual of L¹, and its densities are L¹ functions; [measure](measure-and-sigma-algebras.md) supplies the null sets that are ignored.

## Common misconceptions

- **"A larger p always gives a smaller space"**: true on finite measure spaces, reversed for sequences, and false either way on ℝ.
- **"Convergence in L² implies convergence at each point"**: the typewriter sequence converges in every Lᵖ with p < ∞ and at no point.
- **"Every bounded functional on L^∞ is integration against an L¹ function"**: the dual of L^∞ is strictly larger.

## Go deeper

- Elias M. Stein and Rami Shakarchi, *Functional Analysis* (2011): opens with Lᵖ spaces and their duals.
- Elliott H. Lieb and Michael Loss, *Analysis* (2nd edition, 2001): sharp inequalities in Lᵖ, with care over every constant.
- Gerald B. Folland, *Real Analysis* (2nd edition, 1999): Lᵖ theory and duality in the standard graduate form.
