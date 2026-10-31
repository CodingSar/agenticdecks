# Statistical Inference

> **Layer:** [11 Probability and Statistics](../README.md) › Statistical Inference
> **Children:** [Estimation and Likelihood](estimation-and-likelihood.md) · [Hypothesis Tests and Confidence Intervals](hypothesis-tests-and-confidence-intervals.md) · [Bayesian Inference](bayesian-inference.md) · [Linear Models and Regression](linear-models-and-regression.md)

## What this area is about

Probability starts from a known distribution and predicts data; statistics starts from data and infers the distribution. This inverse problem has no unique answer, so it is made precise by fixing a statistical model, a family of distributions P_θ indexed by an unknown parameter θ, and asking what the data say about θ. The likelihood, the probability of the observed data as a function of θ, is the common currency. It can be maximised to estimate θ, compared between two values to test a hypothesis, or multiplied by a prior to give a posterior. The first two uses belong to the frequentist school, which judges procedures by their behaviour over repeated samples; the third is Bayesian, which treats θ as random and conditions on the data. The schools disagree about meaning more than about mathematics, and in large samples their answers usually agree.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Estimation and likelihood](estimation-and-likelihood.md) | Estimators, bias and variance, maximum likelihood, Fisher information and the Cramér–Rao bound | Nothing in this area; the limit theorems and conditional expectation |
| [Hypothesis tests and confidence intervals](hypothesis-tests-and-confidence-intervals.md) | Neyman–Pearson optimality, p-values and their misuse, intervals as inverted tests | Estimation and likelihood |
| [Bayesian inference](bayesian-inference.md) | Priors, posteriors, conjugacy, exchangeability and Markov chain Monte Carlo | Estimation and likelihood |
| [Linear models and regression](linear-models-and-regression.md) | Least squares as projection, Gauss–Markov, exact normal theory, regularisation | Estimation and likelihood |

Start with estimation, which introduces the likelihood and the limits on how well any procedure can do. The other three children then branch from it, and can be read in any order. Testing turns likelihood ratios into decisions with controlled error; Bayesian inference turns the likelihood into a distribution for θ; the linear model is the case where everything can be computed exactly. In the linear model with normal errors the three branches meet: the maximum likelihood estimate is least squares, the optimal tests are t and F tests, and with a flat prior the posterior is centred on the same estimate.

```
                    statistical model {P_θ} and data x
                                  │
                         likelihood L(θ) = f(x; θ)
                 ┌────────────────┼────────────────┐
                 ▼                ▼                ▼
          maximise it       compare values     multiply by a prior
          (estimation)      (tests, intervals)  (Bayesian posterior)
                 └────────────────┼────────────────┘
                                  ▼
                linear Gaussian model: all three agree
```

## Connections to sibling areas

- **[Measure-theoretic probability](../01-measure-theoretic-probability/README.md):** a model is a family of laws, a posterior is a regular conditional distribution, and Rao–Blackwell and least squares are both orthogonal projections.
- **[Limit theorems](../02-limit-theorems/README.md):** the law of large numbers gives consistency, the central limit theorem asymptotic normality and approximate intervals, and concentration inequalities give intervals valid at every sample size.
- **[Stochastic processes](../03-stochastic-processes/README.md):** Markov chain Monte Carlo makes Bayesian computation feasible, and martingale convergence proves posterior consistency.

## Connections across layers

From below, the area uses the [inner-product spaces](../../04-linear-algebra/03-inner-product-spaces/README.md) of 04 for regression, the inequalities of [real analysis](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md) in 06 for the Cramér–Rao bound, and the [discrete probability](../../03-combinatorics-and-graph-theory/03-discrete-probability/README.md) of 03 for Bayes' rule.

Upward, [statistical learning theory](../../14-applied-and-computational-mathematics/06-data-and-learning/statistical-learning-theory.md) in 14 extends estimation to prediction over rich classes of models, [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) supply Bayesian computation, and the social role of statistical evidence is part of [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) in 15. The sibling trees apply this material: medicine in its [quantitative foundations](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/README.md) and [causal inference](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/02-inference-and-causation/causal-inference.md), computer science in [statistical inference](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) and [generalisation and the bias–variance trade-off](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md).

## Cross-cutting threads

- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): maximum likelihood, least squares and most powerful tests are all solutions of optimisation problems.
- [Duality](../../CROSS-CUTTING.md#duality): confidence intervals and tests are the same object read in two directions.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the Cramér–Rao bound limits every unbiased estimator, and Stein's paradox shows that the obvious estimator can be beaten everywhere.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): inference works because averages of data concentrate around the quantities they estimate.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): most inference is justified asymptotically, through normal approximations to likelihoods and posteriors.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): exchangeability, invariance under permutations, is what de Finetti's theorem turns into a prior.
