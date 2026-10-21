# Generalization and Bias-Variance

> **Layer:** [13 Artificial Intelligence](../README.md) › [Machine learning foundations](README.md)
> **Builds on:** [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md), [Random variables and distributions](../../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md), [Learning as optimization](learning-as-optimization.md)
> **Enables:** [Evaluation and experimentation](evaluation-and-experimentation.md), [Supervised learning](supervised-learning.md), [Training at scale](../03-deep-learning/training-at-scale.md)

## Essence

A model is useful only if it performs well on data it has not seen. Generalisation is the gap between training performance and performance on new data drawn from the same distribution. Because infinitely many functions fit any finite training set, learning is impossible without an **inductive bias**: a preference for some functions over others. Too strong a bias and the model cannot represent the truth (underfitting, high bias); too weak and it fits noise in the particular sample (overfitting, high variance). Classical theory frames this as a trade-off controlled by model capacity. Modern deep learning complicates the picture: hugely over-parameterised networks that can memorise random labels still generalise well on real data, because the optimiser and architecture supply implicit bias.

## Core tenets

1. **No inductive bias, no learning.** The No Free Lunch theorems show that averaged over all possible target functions, every learner has the same expected performance off the training set. Learning works in practice only because real-world functions are not arbitrary: they are smooth, compositional or sparse, and a good learner's bias matches that structure. Choosing a model class is a claim about the world.

2. **Test error decomposes into bias, variance and noise.** For squared loss, the expected error of a learned predictor at a point is

   E[(y − f̂(x))²] = Bias[f̂(x)]² + Var[f̂(x)] + σ²

   Bias is the error of the average learned model; variance is how much the learned model changes with the particular training sample; σ² is irreducible noise. More capacity usually lowers bias and raises variance.

3. **Overfitting means fitting the sample, not the distribution.** A degree-9 polynomial through 10 noisy points has zero training error and wild predictions between them. The signature is a widening gap between training and validation loss as training proceeds or capacity grows. More data narrows the gap, because the sample becomes a better proxy for the distribution.

4. **Capacity bounds give guarantees, loosely.** Statistical learning theory bounds the generalisation gap in terms of capacity measures such as Vapnik–Chervonenkis (VC) dimension: with probability 1 − δ, the gap is roughly O(√((d + log(1/δ)) / n)) for VC dimension d and n examples. These bounds explain why more data helps and why capacity matters, but for deep networks they are numerically vacuous, since d far exceeds n.

5. **Regularisation adds bias to cut variance.** Weight decay (an L2 penalty), early stopping, dropout, data augmentation and parameter sharing all restrict the effective set of functions the learner will reach. Each encodes a belief: small weights, smooth functions, invariance to crops or rotations.

6. **Over-parameterised models can generalise anyway.** Zhang et al. (2017) showed that standard image networks can fit randomly shuffled labels perfectly, yet the same networks generalise on true labels. Test error can even fall again as capacity grows past the point of perfect interpolation ("double descent"). The working explanation is implicit regularisation: Stochastic Gradient Descent (SGD) from small initialisations prefers simple, flat solutions among the many that fit. As of the mid-2020s this is an active research area without a complete theory.

7. **Generalisation assumes the future looks like the past.** All guarantees assume training and test data are independent and identically distributed (i.i.d.) draws from one distribution. Real deployments break this through distribution shift: new users, new sensors, changing behaviour. A model can generalise perfectly in the i.i.d. sense and still fail in production.

## Key concepts

| Term | Meaning |
|---|---|
| Generalisation gap | Test error minus training error |
| Inductive bias | Assumptions that make a learner prefer some hypotheses over others |
| Capacity | Richness of the function class a model can represent |
| Bias | Systematic error from a model class too restricted to capture the truth |
| Variance | Sensitivity of the learned model to the particular training sample |
| Overfitting / underfitting | Fitting noise in the sample / failing to fit the signal |
| VC dimension | Largest number of points a hypothesis class can label in every possible way |
| Double descent | Test error rising then falling again as capacity passes the interpolation threshold |
| Distribution shift | Test data drawn from a different distribution than training data |

## How it fits

- **Below:** The decomposition and the bounds are [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) applied to learned functions; concentration of sample averages comes from [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md).
- **Above:** Regularisation choices shape every architecture in [deep learning](../03-deep-learning/README.md); the empirical [scaling laws](../03-deep-learning/training-at-scale.md) are statements about how test loss falls with data and parameters; [alignment](../04-advanced-paradigms/alignment-and-safety.md) failures are often generalisation failures under shift.
- **Siblings:** [Optimisation](learning-as-optimization.md) minimises training loss; this file explains why that is only a proxy. [Evaluation](evaluation-and-experimentation.md) supplies the held-out data that measures generalisation honestly.

## Common misconceptions

- **"More parameters always overfit."** Classical intuition, partly overturned: large networks trained well often generalise better than small ones, given enough data and implicit regularisation.
- **"Zero training error means overfitting."** Interpolating the training set is compatible with good test error; overfitting is diagnosed on held-out data, not training data.
- **"A model that generalises is robust."** i.i.d. generalisation says nothing about adversarial inputs or shifted distributions.

## Go deeper

- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning* (2nd ed., 2009): bias-variance, regularisation and model selection.
- Shai Shalev-Shwartz and Shai Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (2014): Probably Approximately Correct (PAC) learning and VC theory.
- Chiyuan Zhang et al., "Understanding Deep Learning Requires Rethinking Generalization" (2017): the random-label experiments.
- Mikhail Belkin et al., "Reconciling Modern Machine-Learning Practice and the Classical Bias–Variance Trade-off" (2019): double descent.
