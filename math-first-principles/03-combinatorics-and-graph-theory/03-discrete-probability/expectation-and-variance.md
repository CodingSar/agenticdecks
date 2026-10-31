# Expectation and Variance

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Discrete Probability](README.md)
> **Builds on:** [Finite probability spaces](finite-probability-spaces.md), [Counting principles and binomial coefficients](../01-enumeration/counting-principles-and-binomial-coefficients.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md)
> **Enables:** [The probabilistic method](the-probabilistic-method.md), [Random variables and distributions](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md), [The law of large numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md), [Concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md), [Randomised algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md)

## Essence
A random variable is a numerical function of the outcome, and its expectation is its probability-weighted average. Expectation is the single most useful number in probability because it is linear: the expectation of a sum is the sum of the expectations, whether or not the parts are independent. That lets one compute averages of complicated counts by splitting them into indicator variables, one per small event. Variance measures spread around the mean, and the inequalities of Markov and Chebyshev turn means and variances into bounds on probabilities, which is the first step from averages to certainty and the seed of the law of large numbers.

## Core tenets
1. **Expectation is a weighted average, defined when the sum converges absolutely.** For X : Ω → ℝ on a discrete space, E[X] = ∑ X(ω)p(ω) = ∑ x · P(X = x). Absolute convergence matters on infinite spaces: in the St Petersburg game a fair coin is tossed until it lands heads, paying 2ᵏ if that happens on toss k, so each k contributes 2ᵏ · 2⁻ᵏ = 1 and the expectation is infinite, although every actual payout is finite.

2. **Expectation is linear, with no independence needed.** E[aX + bY] = aE[X] + bE[Y] follows by splitting the defining sum over outcomes ω; the joint behaviour of X and Y never enters. This is what makes expectation computable: write a complicated count as a sum of simple pieces and add their expectations.

3. **Indicator variables turn expected counts into sums of probabilities.** If X counts how many of the events A₁, …, Aₙ occur, then X = 𝟙(A₁) + ⋯ + 𝟙(Aₙ), with 𝟙(A) equal to 1 on A and 0 off it, and E[X] = P(A₁) + ⋯ + P(Aₙ). A random permutation of n items has on average exactly one fixed point, since each item is fixed with probability 1/n, even though fixed points are far from independent. Collecting all n coupon types, drawn uniformly, takes on average n(1 + 1/2 + ⋯ + 1/n) ≈ n ln n draws: the wait for the next new type is geometric with mean n/(n − i) when i types are held.

4. **Some outcome is at least the mean, and some is at most the mean.** If X < E[X] for every outcome, averaging would give E[X] < E[X]. This averaging principle is the engine of [the probabilistic method](the-probabilistic-method.md): to show some object has at least m good features, show that a random one has at least m on average.

5. **Variance measures spread, and it adds only for uncorrelated variables.** Var X = E[(X − μ)²] = E[X²] − μ², with μ = E[X]. Expanding gives Var(X + Y) = Var X + Var Y + 2 Cov(X, Y), where Cov(X, Y) = E[XY] − E[X]E[Y] vanishes when X and Y are independent, because then E[XY] = E[X]E[Y]. Hence a binomial count of successes in n independent trials with success probability p has mean np and variance np(1 − p), a sum of n indicator variances p(1 − p). For X and −X, which are perfectly dependent, the variances do not add: Var(X + (−X)) = 0.

6. **Markov's and Chebyshev's inequalities turn moments into tail bounds.** For X ≥ 0 and a > 0, P(X ≥ a) ≤ E[X]/a, because X ≥ a · 𝟙(X ≥ a) pointwise. Applying this to (X − μ)² gives Chebyshev: P(∣X − μ∣ ≥ t) ≤ Var X/t². Without non-negativity Markov's inequality fails, and both bounds are sharp for some distributions, though often weak in practice.

7. **Averaging many independent trials concentrates the result: the weak law of large numbers.** If X₁, …, Xₙ are independent with mean μ and variance σ², their average has mean μ and variance σ²/n, so Chebyshev gives P(∣average − μ∣ ≥ ε) ≤ σ²/(nε²), which tends to 0. Using all moments instead of two, through E[e^(tX)], gives exponentially small Chernoff bounds, developed in [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md).

8. **Generating functions encode whole distributions.** For X with values in ℕ, the probability generating function G(s) = E[s^X] = ∑ P(X = k)sᵏ is a [generating function](../01-enumeration/generating-functions.md) of the distribution; G′(1) = E[X], and for independent X and Y the function of X + Y is the product of theirs. The binomial distribution has G(s) = (1 − p + ps)ⁿ, the binomial theorem in probabilistic form. Replacing sᵏ by e^(itk) gives the characteristic function, the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) of the distribution, which leads to the [central limit theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md).

## Key concepts
| Term | Meaning |
|---|---|
| Random variable | A real-valued function of the outcome |
| Expectation E[X] | The probability-weighted average ∑ X(ω)p(ω) |
| Indicator variable | 𝟙(A), equal to 1 on the event A and 0 elsewhere; E[𝟙(A)] = P(A) |
| Variance | E[(X − μ)²], the mean squared deviation from the mean |
| Covariance | E[XY] − E[X]E[Y]; zero for independent variables |
| Binomial distribution | The number of successes in n independent trials with success probability p |
| Markov's inequality | P(X ≥ a) ≤ E[X]/a for X ≥ 0 |
| Chebyshev's inequality | P(∣X − μ∣ ≥ t) ≤ Var X/t² |
| Probability generating function | E[s^X] = ∑ P(X = k)sᵏ for ℕ-valued X |

## How it fits
- **Below:** Built on [finite probability spaces](finite-probability-spaces.md), [binomial coefficients](../01-enumeration/counting-principles-and-binomial-coefficients.md) and real-number sums from [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md).
- **Above:** The general theory of [random variables](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md) replaces sums by integrals; the [law of large numbers](../../11-probability-and-statistics/02-limit-theorems/the-law-of-large-numbers.md) and [concentration inequalities](../../11-probability-and-statistics/02-limit-theorems/concentration-inequalities.md) sharpen tenet 7; expected running times drive [randomised algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) and [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md).
- **Siblings:** [Finite probability spaces](finite-probability-spaces.md) supply the setting; [the probabilistic method](the-probabilistic-method.md) applies linearity, the averaging principle and second moments to prove existence.

## Common misconceptions
- **"Linearity of expectation needs independence"**: it holds for any random variables; independence is needed for E[XY] = E[X]E[Y] and for variances to add.
- **"Uncorrelated means independent"**: if X is −1, 0 or 1 with equal probability, then X and X² have covariance 0, yet X² is a function of X.
- **"The expected value is the value to expect"**: a fair die has mean 3.5, which never occurs, and the St Petersburg game has infinite mean but finite payouts.

## Go deeper
- Feller, *An Introduction to Probability Theory and Its Applications*, Volume 1 (3rd edition, 1968): random variables, generating functions and limit theorems in the discrete setting.
- Mitzenmacher and Upfal, *Probability and Computing* (2nd edition, 2017): linearity, moments and Chernoff bounds as tools for algorithms.
- Blitzstein and Hwang, *Introduction to Probability* (2nd edition, 2019): expectation by indicators, with many worked examples.
