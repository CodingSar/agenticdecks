# Bayesian Inference

> **Layer:** [11 Probability and Statistics](../README.md) › [Statistical Inference](README.md)
> **Builds on:** [Estimation and Likelihood](estimation-and-likelihood.md), [Conditional Expectation](../01-measure-theoretic-probability/conditional-expectation.md), [Markov Chains](../03-stochastic-processes/markov-chains.md), [Martingales](../03-stochastic-processes/martingales.md), [Finite Probability Spaces](../../03-combinatorics-and-graph-theory/03-discrete-probability/finite-probability-spaces.md)
> **Enables:** [Monte Carlo Methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md), [Statistical Learning Theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md), [Bayesian Reasoning](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md), [Probabilistic Reasoning](../../../cs-first-principles/13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md)

## Essence

Bayesian inference treats the unknown parameter θ as a random variable. Before the data it has a prior distribution expressing what is believed; after the data it has a posterior distribution, the conditional law of θ given the observations, obtained by Bayes' theorem as prior times likelihood, renormalised. Every conclusion (an estimate, an interval, a prediction, a decision) is then read off the posterior. The approach answers directly the question a p-value is often mistaken for, the probability of a hypothesis given the data, at the price of requiring a prior. Its computational engine is Markov chain Monte Carlo (MCMC), which samples from posteriors too complicated to compute in closed form.

## Core tenets

1. **The posterior is the prior reweighted by the likelihood.** With prior density π(θ) and likelihood f(x ∣ θ):

   ```
   π(θ ∣ x)  =  f(x ∣ θ)·π(θ) / m(x),       m(x) = ∫ f(x ∣ θ)·π(θ) dθ.
   ```

   The normalising constant m(x), the marginal likelihood, is often the hard part. Measure-theoretically, the posterior is a regular conditional distribution of θ given the data. Thomas Bayes's essay was published posthumously in 1763; Pierre-Simon Laplace developed the method independently and far more generally from 1774.

2. **Conjugate priors make updating arithmetic.** For n coin tosses with k heads and a Beta(a, b) prior on the heads probability p, the posterior is Beta(a + k, b + n − k), with mean (a + k)/(a + b + n): the prior acts like a + b earlier tosses, a of them heads. The uniform prior a = b = 1 gives Laplace's rule of succession, (k + 1)/(n + 2). A family of priors is conjugate when it is closed under updating; normal priors are conjugate for normal means, gamma priors for Poisson rates.

3. **Decisions come from minimising posterior expected loss.** Under squared-error loss the best estimate is the posterior mean, under absolute error the posterior median, and under 0–1 loss the posterior mode. A 95% credible interval is a set with posterior probability 0.95, a direct statement about θ given the data. Abraham Wald's complete class theorems link the two schools: under broad conditions, every admissible decision rule is a Bayes rule or a limit of Bayes rules.

4. **Exchangeability explains where priors come from.** A sequence is exchangeable when its law is unchanged by permuting finitely many terms. Bruno de Finetti's theorem (1931, for binary sequences) says that every infinite exchangeable sequence is a mixture of i.i.d. (independent and identically distributed) sequences: there is a random p such that, given p, the tosses are i.i.d. with heads probability p. So anyone who regards the order of trials as irrelevant is already acting as if there were a prior on p. Edwin Hewitt and Leonard Savage (1955) extended the theorem to general spaces.

5. **With enough data the prior washes out, in finite dimensions.** The posterior mean E[θ ∣ X₁, …, Xₙ] is a Doob martingale, so it converges; Joseph Doob (1949) deduced consistency of the posterior for prior-almost every θ. The Bernstein–von Mises theorem says that in smooth finite-dimensional models the posterior is approximately normal, centred at the maximum likelihood estimate with variance 1/(n·I(θ)), so credible and confidence intervals nearly coincide. In infinite-dimensional models this can fail: Persi Diaconis and David Freedman (1986) gave natural priors whose posteriors converge to the wrong answer.

6. **Markov chain Monte Carlo replaces integration by sampling.** The posterior is known up to the constant m(x), and the Metropolis–Hastings algorithm needs only ratios π(θ′ ∣ x)/π(θ ∣ x), in which m(x) cancels. It builds a Markov chain whose stationary distribution is the posterior and uses ergodic averages along the chain. Gibbs sampling, which updates one coordinate at a time from its conditional law, was introduced to image analysis by Stuart and Donald Geman (1984) and brought to Bayesian statistics by Alan Gelfand and Adrian Smith (1990). Variational inference instead approximates the posterior by the closest member of a simpler family.

7. **Choosing a prior is the contested step.** Harold Jeffreys proposed π(θ) ∝ √I(θ), where I is the Fisher information, because it gives the same answer under any reparametrisation; for a coin it is Beta(1/2, 1/2). Some "non-informative" priors, such as a flat density on the whole real line, are improper: they do not integrate to 1. They can still give proper posteriors, but they can also give improper ones or paradoxes, and the posterior must be checked.

## Key concepts

| Term | Meaning |
|---|---|
| Prior | The distribution of θ before seeing the data |
| Posterior | The conditional distribution of θ given the data |
| Marginal likelihood | m(x) = ∫ f(x ∣ θ)·π(θ) dθ, the normalising constant |
| Conjugate prior | A family of priors closed under updating by a given likelihood |
| Credible interval | A set with posterior probability 1 − α |
| Exchangeable sequence | A sequence whose law is unchanged by finite permutations |
| Bernstein–von Mises theorem | Posteriors are asymptotically normal around the maximum likelihood estimate |
| Jeffreys prior | π(θ) ∝ √I(θ), invariant under reparametrisation |

## How it fits

- **Below:** Bayes' rule for events is in [finite probability spaces](../../03-combinatorics-and-graph-theory/03-discrete-probability/finite-probability-spaces.md) of 03; the posterior is a [conditional distribution](../01-measure-theoretic-probability/conditional-expectation.md); MCMC is applied [Markov chains](../03-stochastic-processes/markov-chains.md); consistency is [martingale](../03-stochastic-processes/martingales.md) convergence.
- **Above:** MCMC is a central topic of [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) in 14; regularisation in [learning](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md) is often a prior in disguise; diagnostic reasoning in medicine is [Bayes' theorem](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md) applied to tests.
- **Siblings:** ridge regression in [linear models](linear-models-and-regression.md) is the posterior mode under a normal prior; the [likelihood](estimation-and-likelihood.md) is shared with frequentist inference; [credible and confidence intervals](hypothesis-tests-and-confidence-intervals.md) answer different questions.

## Common misconceptions

- **"Bayesian inference is subjective and frequentist inference objective"**: both rest on modelling choices. The prior is explicit; the likelihood, the stopping rule and the choice of test are just as much assumptions.
- **"A flat prior expresses ignorance"**: flat in θ is not flat in log θ or θ², so flatness depends on the parametrisation; Jeffreys priors were designed to address this.
- **"MCMC output is a sample from the posterior"**: only after the chain has mixed, and successive draws are dependent, so the effective sample size is smaller than the number of draws.

## Go deeper

- Andrew Gelman, John Carlin, Hal Stern, David Dunson, Aki Vehtari and Donald Rubin, *Bayesian Data Analysis* (3rd edition, 2013): the standard applied text.
- E. T. Jaynes, *Probability Theory: The Logic of Science* (2003): Bayesian probability as extended logic, argued forcefully.
- Christian Robert and George Casella, *Monte Carlo Statistical Methods* (2nd edition, 2004): the theory of MCMC.
