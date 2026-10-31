# Modes of Convergence

> **Layer:** [11 Probability and Statistics](../README.md) › [Limit Theorems](README.md)
> **Builds on:** [Random Variables and Distributions](../01-measure-theoretic-probability/random-variables-and-distributions.md), [Independence and Zero–One Laws](../01-measure-theoretic-probability/independence-and-zero-one-laws.md), [Lᵖ Spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md), [The Lebesgue Integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md)
> **Enables:** [The Law of Large Numbers](the-law-of-large-numbers.md), [The Central Limit Theorem](the-central-limit-theorem.md), [Martingales](../03-stochastic-processes/martingales.md), [Estimation and Likelihood](../04-statistical-inference/estimation-and-likelihood.md)

## Essence

A sequence of random variables can converge in at least four inequivalent senses, and each limit theorem of probability is a statement in a specific one: the strong law of large numbers is almost sure convergence, the weak law is convergence in probability, the central limit theorem is convergence in distribution. Almost sure convergence asks that the numbers Xₙ(ω) converge for almost every outcome ω; convergence in probability, that a large error become unlikely; convergence in Lᵖ, that the mean p-th power of the error tend to 0; convergence in distribution, only that the laws approach one another. Knowing which mode implies which, and the counterexamples to the converses, is what keeps probabilistic arguments honest.

## Core tenets

1. **There are four definitions, and the fourth needs a proviso.** With Fₙ and F the distribution functions of Xₙ and X:

   ```
   almost surely:     P( { ω : Xₙ(ω) → X(ω) } ) = 1
   in probability:    P( ∣Xₙ − X∣ > ε ) → 0   for every ε > 0
   in Lᵖ (p ≥ 1):     E[ ∣Xₙ − X∣ᵖ ] → 0
   in distribution:   Fₙ(x) → F(x)   at every x where F is continuous
   ```

   The proviso matters: Xₙ = 1/n ought to converge to 0, yet Fₙ(0) = 0 for every n while F(0) = 1.

2. **The implications run one way.** Each arrow has a one-line proof:

   ```
   almost surely ─┐
                  ├─►  in probability  ─►  in distribution
   in Lᵖ ─────────┘
   in Lᵖ  ─►  in Lᵠ   whenever q ≤ p
   ```

   Almost sure convergence gives convergence in probability by dominated convergence applied to the indicators of {∣Xₙ − X∣ > ε}. Lᵖ gives it by Markov's inequality, P(∣Xₙ − X∣ > ε) ≤ E∣Xₙ − X∣ᵖ/εᵖ. Convergence in probability gives convergence in distribution by squeezing P(Xₙ ≤ x) between P(X ≤ x − ε) and P(X ≤ x + ε), up to the small probability P(∣Xₙ − X∣ > ε).

3. **In probability does not imply almost surely, but a subsequence does.** The typewriter sequence on [0, 1] is the indicators of [0, 1/2], [1/2, 1], [0, 1/4], [1/4, 1/2], …, sweeping the interval at ever finer scales: the chance of a non-zero value tends to 0, yet every point is covered infinitely often, so Xₙ(ω) converges for no ω. With independent Xₙ such that P(Xₙ = 1) = 1/n and Xₙ = 0 otherwise, Xₙ → 0 in probability, but ∑1/n = ∞, so by the second Borel–Cantelli lemma Xₙ = 1 infinitely often. Conversely, choose nₖ with P(∣X_(nₖ) − X∣ > 2⁻ᵏ) < 2⁻ᵏ, and the first Borel–Cantelli lemma gives X_(nₖ) → X almost surely.

4. **Almost sure convergence does not move means; uniform integrability is the missing condition.** On [0, 1], Xₙ = n·1_(0, 1/n) tends to 0 at every point, yet E[Xₙ] = 1 for every n: the mass escapes into an ever taller, thinner spike. Vitali's theorem says that Xₙ → X in L¹ if and only if Xₙ → X in probability and the family is uniformly integrable. Domination, ∣Xₙ∣ ≤ Y with E[Y] < ∞, is the usual sufficient condition; boundedness in Lᵖ for some p > 1 is another.

5. **Convergence in distribution says nothing about the variables themselves.** If Z is standard normal and Xₙ = −Z for every n, then Xₙ → Z in distribution, since all have the same law, while ∣Xₙ − Z∣ = 2∣Z∣ never shrinks; the Xₙ need not even live on the same space as Z. The one partial converse is that convergence in distribution to a constant implies convergence in probability. Skorokhod's representation theorem recovers the rest: if Xₙ → X in distribution, then Yₙ = Fₙ⁻¹(U) and Y = F⁻¹(U), built from one uniform U, have the same laws and converge almost surely.

6. **Convergence in distribution has many equivalent forms, which makes it the workhorse.** By the portmanteau theorem, it holds if and only if E[g(Xₙ)] → E[g(X)] for every bounded continuous g. By Lévy's continuity theorem, it holds if and only if the characteristic functions converge at every t, which reduces the central limit theorem to a Taylor expansion. The continuous mapping theorem (h(Xₙ) → h(X) for continuous h) and Slutsky's theorem (if Xₙ → X in distribution and Yₙ → c in probability, then Xₙ + Yₙ → X + c and Yₙ·Xₙ → c·X) let statisticians replace unknown quantities by estimates.

7. **Almost sure convergence is not convergence in any topology.** In a topological space, if every subsequence has a further subsequence converging to X, then the whole sequence converges to X. The typewriter sequence breaks this for almost sure convergence: by tenet 3 every subsequence has a further subsequence converging almost surely to 0, yet the sequence itself converges nowhere. Convergence in probability, by contrast, is convergence in the metric d(X, Y) = E[min(∣X − Y∣, 1)].

## Key concepts

| Term | Meaning |
|---|---|
| Almost sure convergence | Xₙ(ω) → X(ω) for every ω outside a null event |
| Convergence in probability | P(∣Xₙ − X∣ > ε) → 0 for every ε > 0 |
| Convergence in Lᵖ | E∣Xₙ − X∣ᵖ → 0 |
| Convergence in distribution | Fₙ(x) → F(x) at every continuity point x of F; also called weak convergence |
| Uniform integrability | supₙ E[∣Xₙ∣·1{∣Xₙ∣ > K}] → 0 as K → ∞ |
| Portmanteau theorem | The list of equivalent forms of convergence in distribution |
| Slutsky's theorem | Convergence in distribution survives adding or multiplying by variables converging in probability to a constant |
| Skorokhod representation | Convergence in distribution realised as almost sure convergence on a new space |

## How it fits

- **Below:** [Lᵖ spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md) and the convergence theorems of the [Lebesgue integral](../../09-advanced-analysis/01-measure-and-integration/the-lebesgue-integral.md) in 09 supply the tools; pointwise versus [uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md) in 06 is the deterministic shadow of the same distinctions.
- **Above:** the error of [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) in 14 is stated in L² and in distribution; consistency of an estimator is convergence in probability.
- **Siblings:** the [law of large numbers](the-law-of-large-numbers.md) is the model statement in probability and almost surely, the [central limit theorem](the-central-limit-theorem.md) in distribution, and [concentration inequalities](concentration-inequalities.md) give explicit rates in probability.

## Common misconceptions

- **"Convergence in distribution means the variables get close"**: Xₙ = −Z converges in distribution to Z while staying far from it. Only the laws get close.
- **"Almost sure convergence makes the means converge"**: the spike n·1_(0, 1/n) converges to 0 everywhere with mean 1. Uniform integrability is needed.
- **"Almost sure convergence is the strongest mode"**: it neither implies nor follows from L¹ convergence. The typewriter sequence converges in L¹ but nowhere pointwise; the spike converges everywhere but not in L¹.

## Go deeper

- Rick Durrett, *Probability: Theory and Examples* (5th edition, 2019): the modes and their relations, proved carefully.
- Patrick Billingsley, *Convergence of Probability Measures* (2nd edition, 1999): convergence in distribution on general spaces, the basis for limits of random paths.
- Jordan Stoyanov, *Counterexamples in Probability* (3rd edition, 2013): for every failed converse, the example that breaks it.
