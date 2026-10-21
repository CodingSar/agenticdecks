# Statistical Inference

> **Layer:** [01 Mathematical Foundations](../README.md) › [Probability and Statistics](README.md)
> **Builds on:** [Probability](probability.md), [Random Variables and Distributions](random-variables-and-distributions.md), [Optimization](../05-continuous-mathematics/optimization.md)
> **Enables:** [Evaluation and Experimentation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md), [Generalization and Bias-Variance](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md), [Supervised Learning](../../13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md), [Usability Evaluation](../../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md), [Measurement and Modeling](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md)

## Essence

Statistical inference runs probability backwards. Probability asks "given the model, how likely is this data?"; inference asks "given this data, what can we say about the model?". It provides principled ways to estimate unknown quantities (the mean latency, a model's accuracy, a conversion rate), to say how uncertain those estimates are, and to decide whether an observed difference is real or noise. Machine learning is statistical inference carried out at scale with flexible models, and every benchmark, A/B test and performance comparison in systems work is an inference problem. The central difficulty is that data are a finite random sample, so every conclusion carries sampling error that must be quantified rather than ignored.

## Core tenets

1. **A statistic is a random variable, so every estimate has a sampling distribution.** The sample mean of *n* observations is itself random: rerun the experiment and you get a different value. Its standard error is σ/√n, so quadrupling the data halves the uncertainty. Reporting a benchmark number without its spread, or comparing two numbers whose difference is smaller than their standard errors, is reporting noise.

2. **Maximum likelihood picks the parameters that make the data most probable.** Given a model with parameters θ, the likelihood L(θ) = P(data | θ) is maximised, usually by maximising its logarithm, which turns products over independent samples into sums. Least-squares regression is maximum likelihood under Gaussian noise, and minimising cross-entropy loss in classification is maximum likelihood for a categorical model. Training a model is thus an [optimization](../05-continuous-mathematics/optimization.md) of a likelihood.

3. **Bayesian inference treats parameters as uncertain and updates them with Bayes' rule.** Posterior ∝ likelihood × prior. The prior encodes what was believed before the data; with lots of data the likelihood dominates. Priors act as regularisers: a Gaussian prior on weights is equivalent to L2 weight decay in maximum a posteriori estimation. Bayesian methods give full uncertainty, at the cost of integrals that usually need sampling or approximation.

4. **Confidence intervals quantify uncertainty about a fixed quantity.** A 95% confidence interval is produced by a procedure that captures the true value in 95% of repeated experiments. Thanks to the Central Limit Theorem (CLT), mean ± 1.96 standard errors is approximately such an interval for large *n*. When distributions are skewed or heavy-tailed, the bootstrap (resampling the data with replacement) estimates the sampling distribution empirically without a formula.

5. **Hypothesis tests control false alarms, not truth.** A p-value is the probability, *assuming no real effect*, of seeing data at least as extreme as observed. Rejecting when p < 0.05 means a 5% false-positive rate when there is no effect. It is not the probability that the effect is real, and running many tests guarantees some false positives (with 20 independent tests at 0.05, the chance of at least one false alarm is about 64%). Corrections such as Bonferroni, and pre-registered metrics in A/B testing, exist for this.

6. **Bias and variance trade off in every estimator.** Expected squared error = bias² + variance + irreducible noise. Simple models are biased but stable; flexible models are unbiased but vary wildly with the sample. This decomposition is the statistical root of [overfitting and generalization](../../13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) in machine learning, and of why regularisation, more data, and ensembles help.

7. **Held-out data are the honest test of generalization.** Performance measured on the data used to fit a model is optimistically biased, because the model has partly fitted noise. Estimating future performance requires data the model never saw: a held-out test set or cross-validation. Reusing the test set for many design decisions slowly turns it into training data, the same multiple-comparisons problem as in tenet 5.

8. **Correlation is not causation; randomisation is the cure.** Observational data confound causes: users who enable a feature may differ from those who do not. Randomly assigning treatment (a randomised controlled trial, or an A/B test in software) makes the groups equal in expectation on every other factor, so a difference in outcome estimates the causal effect. Systems work has the same trap: a change measured on a busy afternoon and its baseline measured at night compares the load, not the change.

## Key concepts

| Term | Meaning |
|---|---|
| Population / sample | The whole distribution of interest / the finite data observed |
| Estimator | A rule computing a guess of a parameter from data |
| Standard error | Standard deviation of an estimator's sampling distribution |
| Likelihood | P(data ∣ parameters), viewed as a function of the parameters |
| MLE / MAP | Maximum likelihood estimate / maximum a posteriori estimate |
| Prior / posterior | Parameter distribution before / after seeing data |
| Confidence interval | Range from a procedure that covers the true value at a stated rate |
| p-value | Probability of data this extreme if the null hypothesis holds |
| Bootstrap | Resampling the data to approximate the sampling distribution |
| Bias–variance decomposition | Error = bias² + variance + noise |
| Cross-validation | Rotating held-out folds to estimate out-of-sample error |

## How it fits

- **Below:** It applies [probability](probability.md) and [distributions](random-variables-and-distributions.md) in reverse, and computes estimates with [optimization](../05-continuous-mathematics/optimization.md).
- **Above:** [Supervised learning](../../13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md) is likelihood maximisation; [evaluation and experimentation](../../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md) is hypothesis testing and held-out estimation; [probabilistic reasoning](../../13-artificial-intelligence/01-classical-ai/probabilistic-reasoning.md) is Bayesian inference. [Usability evaluation](../../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md) and [observability](../../12-software-engineering/04-operations/observability.md) rely on sound comparison of measurements. [Query optimizers](../../09-data-management/03-query-processing/query-optimization.md) estimate result sizes from sampled statistics.
- **Siblings:** [Probability](probability.md) reasons from model to data; this leaf reasons from data to model. [Random variables](random-variables-and-distributions.md) supply the CLT and tail behaviour that make intervals valid or invalid.

## Common misconceptions

- **"p < 0.05 means a 95% chance the effect is real."** The p-value assumes no effect; the probability of a real effect needs a prior and Bayes' rule.
- **"More features and a better training score mean a better model."** Training error falls with flexibility while test error eventually rises.
- **"One benchmark run shows which system is faster."** Without repeated runs and a measure of spread, the difference may be noise from caching, scheduling or frequency scaling.

## Go deeper

- Larry Wasserman, *All of Statistics* (2004): concise statistics for computer scientists.
- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning* (2nd ed., 2009): inference as the foundation of machine learning.
- Ron Kohavi, Diane Tang and Ya Xu, *Trustworthy Online Controlled Experiments* (2020): A/B testing done correctly.
