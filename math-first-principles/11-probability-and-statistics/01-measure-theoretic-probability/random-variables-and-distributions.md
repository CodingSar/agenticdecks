# Random Variables and Distributions

> **Layer:** [11 Probability and Statistics](../README.md) › [Measure-Theoretic Probability](README.md)
> **Builds on:** [Probability Spaces and Kolmogorov's Axioms](probability-spaces-and-kolmogorovs-axioms.md), [The Lebesgue Integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md), [The Radon–Nikodym Theorem](../../09-advanced-analysis/01-measure-and-integration/the-radon-nikodym-theorem.md), [Expectation and Variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md)
> **Enables:** [Conditional Expectation](conditional-expectation.md), [Modes of Convergence](../02-limit-theorems/modes-of-convergence.md), [The Central Limit Theorem](../02-limit-theorems/the-central-limit-theorem.md), [Estimation and Likelihood](../04-statistical-inference/estimation-and-likelihood.md), [Monte Carlo Methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md)

## Essence

A random variable is a measurable function X : Ω → ℝ, a number whose value depends on the outcome ω. Measurability is exactly what is needed to ask "what is the probability that X ≤ x?", and the answers, collected as the law μ of X on ℝ or as the distribution function F(x) = P(X ≤ x), are all that most of probability uses. Expectation is the Lebesgue integral of X against P, which is why the convergence theorems of measure theory become theorems about averages. A density is not a basic notion but a Radon–Nikodym derivative: it exists exactly when the law gives zero mass to every set of zero length.

## Core tenets

1. **Measurability makes the probabilities of values well defined.** X is a random variable when {X ≤ x} = {ω : X(ω) ≤ x} is an event for every real x. Since the half-lines (−∞, x] generate the Borel σ-algebra, {X ∈ B} is then an event for every Borel set B. Sums, products, limits and continuous functions of random variables are random variables, so the class is closed under everything analysis does; in practice measurability is checked once and then forgotten.

2. **The law forgets the sample space.** The law of X is the measure μ(B) = P(X ∈ B) on the Borel sets, written μ = P∘X⁻¹. The change-of-variables formula E[g(X)] = ∫ g dμ, proved for indicators, then simple functions, then monotone limits, shows that every expectation of a function of X depends on μ alone. Different random variables can therefore share a law: if U is uniform on [0, 1], then U and 1 − U have the same law yet are equal only on the null event {U = 1/2}. "The distribution is normal" is a statement about μ; "X = Y almost surely" is a statement about the functions.

3. **The distribution function determines the law, and every candidate occurs.** F is non-decreasing and right-continuous, with limits 0 at −∞ and 1 at +∞. Two laws that agree on all half-lines agree on the σ-algebra they generate, by the π–λ theorem: measures that agree on a class closed under intersection agree on the σ-algebra it generates. Conversely, every such F is the distribution function of X = F⁻¹(U), where F⁻¹(u) = inf{x : F(x) ≥ u} and U is uniform, because F⁻¹(U) ≤ x exactly when U ≤ F(x). This is inverse-transform sampling, the first trick of simulation.

4. **A density is a Radon–Nikodym derivative.** X has a density f, meaning P(X ∈ B) = ∫_B f(x) dx for every Borel set B, if and only if μ is absolutely continuous: μ(B) = 0 whenever B has length 0. Then f = dμ/dx, unique up to a null set. By Lebesgue's decomposition every law splits into atoms (point masses, as for a die), an absolutely continuous part and a singular continuous part. The Cantor law, the law of ∑ₖ 2εₖ/3ᵏ with independent fair εₖ ∈ {0, 1}, has no atoms and no density: it lives on the Cantor set, which has length 0.

5. **Expectation is a Lebesgue integral, and it may not exist.** E[X] = ∫ X dP is defined when E∣X∣ < ∞, and monotone convergence, dominated convergence, Fatou's lemma and Jensen's inequality transfer verbatim. The Cauchy law, with density 1/(π(1 + x²)), has E∣X∣ = ∞ because the integrand ∣x∣/(π(1 + x²)) decays only like 1/(π∣x∣). It has no mean, and later it breaks both the law of large numbers and the central limit theorem.

6. **The characteristic function always exists and turns sums into products.** φ_X(t) = E[e^(itX)] is defined for every law, because ∣e^(itX)∣ = 1; it is the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) of μ. Lévy's inversion formula recovers μ from φ_X, so φ_X determines the law, and for independent X and Y, φ_(X+Y) = φ_X · φ_Y. The moment generating function E[e^(tX)] uses a real exponent and can be infinite: for the Cauchy law it is infinite for every t ≠ 0, while φ(t) = e^(−∣t∣) is perfectly finite.

7. **The joint law carries the dependence; the marginals do not.** A random vector (X, Y) has a law on ℝ², and its two marginal laws do not determine it. If X′ is an independent copy of X, then (X, X) and (X, X′) have identical marginals but different joint laws: the first lives on the diagonal. Densities of transformed vectors follow from the Jacobian formula for [multiple integrals](../../06-real-analysis/04-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md).

## Key concepts

| Term | Meaning |
|---|---|
| Random variable | A measurable function from Ω to ℝ |
| Law μ | The measure B ↦ P(X ∈ B) on the Borel sets of ℝ |
| Distribution function F | F(x) = P(X ≤ x) |
| Quantile function | F⁻¹(u) = inf{x : F(x) ≥ u}, the generalised inverse of F |
| Density f | A function with P(X ∈ B) = ∫_B f(x) dx for every Borel set B |
| Absolutely continuous law | A law that gives probability 0 to every set of length 0 |
| Atom | A point x with P(X = x) > 0 |
| Expectation E[X] | The integral ∫ X dP, defined when E∣X∣ < ∞ |
| Characteristic function φ_X | t ↦ E[e^(itX)], the Fourier transform of the law |
| Marginal law | The law of one coordinate of a random vector |

## How it fits

- **Below:** the [Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) and the [Radon–Nikodym theorem](../../09-advanced-analysis/01-measure-and-integration/the-radon-nikodym-theorem.md) of 09 supply expectation and densities; [expectation and variance](../../03-combinatorics-and-graph-theory/03-discrete-probability/expectation-and-variance.md) in 03 are the finite case.
- **Above:** a statistical model is a family of laws ([estimation](../04-statistical-inference/estimation-and-likelihood.md)); [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) in 14 manufacture random variables from uniform ones by the quantile trick and its relatives.
- **Siblings:** built on [probability spaces](probability-spaces-and-kolmogorovs-axioms.md); [independence](independence-and-zero-one-laws.md) is a property of the joint law; [conditional expectation](conditional-expectation.md) refines E[X] given partial information.

## Common misconceptions

- **"A density value is a probability"**: the uniform law on [0, 1/2] has density 2. Only integrals of a density over sets are probabilities, and P(X = x) = 0 for every x when X has a density.
- **"Every continuous distribution has a density"**: the Cantor law has a continuous distribution function and no density. Continuity of F rules out atoms only.
- **"The moments determine the law"**: the log-normal law, the law of e^Z for a standard normal Z, has the same moments as other laws. Moments do determine the law when E[e^(tX)] is finite for all t near 0.

## Go deeper

- Patrick Billingsley, *Probability and Measure* (3rd edition, 1995): laws, distribution functions and their decomposition in full.
- David Williams, *Probability with Martingales* (1991): a short, crisp treatment of random variables as measurable functions.
- William Feller, *An Introduction to Probability Theory and Its Applications*, Volume 2 (2nd edition, 1971): the classic source for densities, characteristic functions and examples.
