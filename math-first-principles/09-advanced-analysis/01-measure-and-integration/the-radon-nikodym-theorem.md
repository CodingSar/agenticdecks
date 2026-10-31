# The Radon–Nikodym Theorem

> **Layer:** [09 Advanced Analysis](../README.md) › [Measure and Integration](README.md)
> **Builds on:** [Measure and σ-Algebras](measure-and-sigma-algebras.md), [The Lebesgue Integral](the-lebesgue-integral.md), [Lᵖ Spaces](lp-spaces.md)
> **Enables:** [Conditional Expectation](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md), [Random Variables and Distributions](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md), [Stochastic Calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md), [Information Theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md), [Mathematical Finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md)

## Essence

Given two measures μ and ν on the same σ-algebra, when is ν given by a density, ν(A) = ∫ over A of f dμ? An obvious necessary condition is that every μ-null set is ν-null. The Radon–Nikodym theorem says this condition is also sufficient, provided both measures are σ-finite. The density f, written dν/dμ, generalises the probability density of a random variable, and it is how probability defines conditional expectation, how statistics compares hypotheses and how finance changes from real-world to pricing probabilities.

## Core tenets

1. **A density turns one measure into another, and forces absolute continuity.** For measurable f ≥ 0, ν(A) = ∫ over A of f dμ is a measure, by monotone convergence. If μ(A) = 0 then ν(A) = 0; this is written ν ≪ μ, "ν is absolutely continuous with respect to μ". The normal distribution is the measure with density e^(−x²/2)/√(2π) with respect to Lebesgue measure m.

2. **The theorem: absolute continuity is the only obstruction.** Let μ and ν be σ-finite measures on (X, Σ) with ν ≪ μ. Then there is a measurable f ≥ 0 with ν(A) = ∫ over A of f dμ for every A ∈ Σ, and f is unique up to μ-almost-everywhere equality. Johann Radon proved the case of ℝⁿ in 1913 and Otton Nikodym the general case in 1930. The name "derivative" is earned: the chain rule dλ/dμ = (dλ/dν)·(dν/dμ) holds when λ ≪ ν ≪ μ, and on ℝ, if ν ≪ m with distribution function F(x) = ν((−∞, x]), then F′ = dν/dm almost everywhere.

3. **Von Neumann's proof: a density is a Riesz representation.** Take μ and ν finite and set ρ = μ + ν. The map g ↦ ∫ g dν is bounded on L²(ρ), since ∣∫ g dν∣ ≤ ∫ ∣g∣ dρ ≤ ρ(X)^(1/2)·‖g‖₂. The Riesz representation theorem in the [Hilbert space](../03-functional-analysis/hilbert-spaces.md) L²(ρ) gives h with:

   ```
   ∫ g dν = ∫ g·h d(μ + ν)              for every g ∈ L²(ρ)
   ⇒  ∫ g·(1 − h) dν = ∫ g·h dμ
   g = 1_A/(1 − h):   ν(A) = ∫_A h/(1 − h) dμ
   ```

   Testing indicators shows 0 ≤ h ≤ 1, and ν ≪ μ makes {h = 1} null, so f = h/(1 − h) works after a truncation argument. The σ-finite case follows by cutting X into countably many pieces of finite measure.

4. **Without σ-finiteness the theorem fails.** Let μ be counting measure on the Borel sets of [0, 1] and ν = m. Only ∅ is μ-null, so ν ≪ μ trivially. A density would need m({x}) = f(x)·μ({x}) = f(x) for every x, so f = 0 and ν = 0, which is false. Counting measure on an uncountable set is not σ-finite, and that alone breaks the theorem.

5. **Without absolute continuity, the Lebesgue decomposition says what is left.** When μ and ν are σ-finite, ν splits uniquely as νₐ + νₛ, with νₐ ≪ μ and νₛ concentrated on a μ-null set (νₛ ⊥ μ, "singular"). The point mass δ₀ is singular to m. Subtler is the Cantor measure: the distribution of ∑ 2εₙ/3ⁿ for independent fair bits εₙ ∈ {0, 1}. It gives each point measure 0, yet lives on the Cantor set, a null set, so it has no density although its distribution function, the Cantor staircase, is continuous. Every distribution on ℝ is a mixture of a density part, an atomic part and such a singular continuous part.

6. **Conditional expectation is a Radon–Nikodym derivative.** Let X ≥ 0 be integrable on a probability space (Ω, ℱ, P) and 𝒢 ⊆ ℱ a smaller σ-algebra, the information available. On 𝒢, the measure ν(G) = ∫ over G of X dP satisfies ν ≪ P, so it has a 𝒢-measurable density E[X ∣ 𝒢] with ∫ over G of E[X ∣ 𝒢] dP = ∫ over G of X dP for every G ∈ 𝒢. This is Andrey Kolmogorov's definition (1933), and it gives meaning to conditioning on events of probability 0, such as the value of a continuous random variable; [layer 11](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md) builds on it.

7. **Changing measure reweights expectations.** If Q ≪ P are probability measures and L = dQ/dP, then E_Q[Y] = E_P[Y·L] for every Q-integrable Y. In statistics L is the likelihood ratio, the optimal test statistic between two simple hypotheses. In [information theory](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/information-theory.md) the Kullback–Leibler divergence is D(Q ‖ P) = ∫ log L dQ. In [finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md) prices are expectations under a risk-neutral measure equivalent to the real one, and Girsanov's theorem in [stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md) gives L for Brownian motion with a drift. Importance sampling in Monte Carlo methods uses the same identity.

## Key concepts

| Term | Meaning |
|---|---|
| Absolutely continuous ν ≪ μ | Every μ-null set is ν-null |
| Radon–Nikodym derivative dν/dμ | The density f with ν(A) = ∫_A f dμ, unique μ-almost everywhere |
| Singular ν ⊥ μ | ν and μ are concentrated on disjoint sets |
| Lebesgue decomposition | ν = νₐ + νₛ with νₐ ≪ μ and νₛ ⊥ μ |
| Equivalent measures | Each is absolutely continuous with respect to the other |
| Cantor measure | A measure with no atoms concentrated on the null Cantor set |
| Conditional expectation E[X ∣ 𝒢] | The 𝒢-measurable density of G ↦ ∫_G X dP with respect to P |
| Likelihood ratio | dQ/dP for two probability measures |

## How it fits

- **Below:** σ-finiteness and null sets come from [measure](measure-and-sigma-algebras.md); densities are integrated with the [Lebesgue integral](the-lebesgue-integral.md) and lie in L¹ of [Lᵖ spaces](lp-spaces.md).
- **Above:** [conditional expectation](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md) and densities of [random variables](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md) in 11; Kullback–Leibler divergence and risk-neutral pricing in 14.
- **Siblings:** the theorem identifies the dual of L¹ in [Lᵖ spaces](lp-spaces.md); the Cantor measure is, up to a constant, the [Hausdorff measure](hausdorff-dimension-and-fractals.md) of dimension log 2/log 3 on the Cantor set; von Neumann's proof is a Riesz representation in a [Hilbert space](../03-functional-analysis/hilbert-spaces.md).

## Common misconceptions

- **"A distribution with no atoms has a density"**: the Cantor measure gives every point probability 0 and still has no density.
- **"dν/dμ is a function with definite values"**: it is unique only almost everywhere, so two versions may differ on any μ-null set.
- **"Conditioning on a probability-zero event is meaningless"**: the Radon–Nikodym theorem defines it, almost everywhere, relative to a σ-algebra; different σ-algebras that contain the same event can give different answers.

## Go deeper

- Walter Rudin, *Real and Complex Analysis* (3rd edition, 1987): von Neumann's Hilbert space proof, presented in full.
- Gerald B. Folland, *Real Analysis* (2nd edition, 1999): signed measures and the Lebesgue–Radon–Nikodym theorem in one statement.
- David Williams, *Probability with Martingales* (1991): conditional expectation built carefully and put to work.
