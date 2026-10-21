# Evaluation and Experimentation

> **Layer:** [13 Artificial Intelligence](../README.md) › [Machine learning foundations](README.md)
> **Builds on:** [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md), [Generalization and bias-variance](generalization-and-bias-variance.md), [Measurement and modeling](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md)
> **Enables:** [Testing](../../12-software-engineering/03-quality/testing.md), [Alignment and safety](../04-advanced-paradigms/alignment-and-safety.md), [Usability evaluation](../../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md)

## Essence

A learned model has no specification to verify against; its behaviour is defined by data. The only way to know whether it works is to measure it on data it has never seen, with a metric that reflects the real goal, and to trust the measurement only if the experiment was designed so that nothing about the test data leaked into training or model selection. Evaluation is therefore the empirical-science core of Machine Learning (ML): held-out splits, honest metrics, uncertainty estimates and controlled comparisons. Most published and production ML failures trace back to an evaluation error (leakage, a misleading metric, a test set that does not resemble deployment) rather than to the learning algorithm.

## Core tenets

1. **Split data into training, validation and test sets, and use each once for its purpose.** The model fits on training data; hyperparameters and architecture are chosen on validation data; the test set is touched only for the final estimate. Every decision informed by a dataset fits the model a little to that dataset, so a test set used repeatedly for selection becomes a second validation set and its score becomes optimistic.

2. **Leakage silently inflates results.** Leakage is any path by which information about the test labels reaches training: duplicates across splits, features computed with future data, normalising with statistics from the whole dataset, or patients appearing in both train and test. For time-ordered data, split by time; for grouped data, split by group. A suspiciously good result is more often leakage than a breakthrough.

3. **Cross-validation trades compute for a lower-variance estimate.** k-fold cross-validation trains k models, each validated on a different fold, and averages. It uses all data for both fitting and evaluation and gives a spread of scores, which matters when data is scarce. It does not fix leakage and it is usually too expensive for large neural networks, which rely on a single large held-out split.

4. **The metric must match the cost of errors.** Accuracy hides failure on rare classes. Precision (of predicted positives, how many are right) and recall (of true positives, how many are found) trade off as the threshold moves; the Receiver Operating Characteristic (ROC) curve and its Area Under the Curve (AUC) summarise all thresholds. If a missed fraud costs 100 times a false alarm, optimise for that ratio, not for accuracy.

5. **Every score has an error bar.** A test accuracy measured on n examples has a standard error of about √(p(1 − p)/n): on 1,000 examples at 90% accuracy, about ±1 percentage point. Differences between models smaller than that, or than the variation across random seeds, are not evidence. Paired tests on the same examples and multiple seeds make comparisons honest.

6. **Benchmarks saturate and get overfit by the community.** When thousands of papers tune against one public test set, the field collectively selects for its quirks. Benchmarks also leak into the web-scale training data of large models ("contamination"). As of the mid-2020s, evaluating Large Language Models (LLMs) relies on fresh held-out tasks, private test sets, human preference comparisons and, increasingly, model-graded evaluation, each with known biases.

7. **Offline metrics are proxies; online experiments measure the real effect.** A model that wins offline can lose in deployment because users react to it, data drifts, or the metric missed what matters. Randomised controlled experiments (A/B tests) in production compare variants on real outcomes, and monitoring after launch catches drift that no static test set can.

## Key concepts

| Term | Meaning |
|---|---|
| Held-out set | Data excluded from training and used only for measurement |
| Validation set | Held-out data used to choose hyperparameters and models |
| Test set | Held-out data used once, for the final unbiased estimate |
| Data leakage | Information about evaluation labels reaching the training process |
| Cross-validation | Rotating which part of the data is held out and averaging results |
| Precision / recall | Fraction of predicted positives that are correct / of actual positives that are found |
| ROC curve / AUC | True-positive rate vs false-positive rate across thresholds / the area under it |
| Contamination | Benchmark test items appearing in a model's training data |
| A/B test | Randomised comparison of two variants on live traffic |

## How it fits

- **Below:** Confidence intervals and hypothesis tests come from [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md); the discipline of controlled measurement comes from [engineering method](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md).
- **Above:** Evaluation is ML's counterpart to [software testing](../../12-software-engineering/03-quality/testing.md), and in production it merges with [observability](../../12-software-engineering/04-operations/observability.md). Red-teaming and capability evaluations are the measurement arm of [alignment and safety](../04-advanced-paradigms/alignment-and-safety.md). User-facing systems also need [usability evaluation](../../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md).
- **Siblings:** It makes the abstract [generalisation](generalization-and-bias-variance.md) gap measurable and is the referee for [supervised](supervised-learning.md) and [unsupervised](unsupervised-learning.md) methods alike.

## Common misconceptions

- **"Cross-validation prevents overfitting."** It estimates generalisation; it does not stop you from overfitting the validation procedure through repeated selection.
- **"State-of-the-art on a benchmark means state-of-the-art in practice."** Benchmarks capture a narrow slice of the deployment distribution and may be contaminated or saturated.
- **"A bigger test set is always enough."** Size reduces variance, not bias: a large test set drawn from the wrong distribution gives a precise wrong answer.

## Go deeper

- Trevor Hastie, Robert Tibshirani and Jerome Friedman, *The Elements of Statistical Learning* (2nd ed., 2009), chapter 7: model assessment and selection, including the right and wrong way to cross-validate.
- Ron Kohavi, Diane Tang and Ya Xu, *Trustworthy Online Controlled Experiments* (2020): A/B testing done properly.
- D. Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (2015): why production ML fails in ways offline evaluation misses.
