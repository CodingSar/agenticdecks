# Machine Learning Foundations

> **Layer:** [13 Artificial Intelligence](../README.md) › Machine learning foundations
> **Children:** [Learning as optimization](learning-as-optimization.md) · [Generalization and bias-variance](generalization-and-bias-variance.md) · [Supervised learning](supervised-learning.md) · [Unsupervised learning](unsupervised-learning.md) · [Evaluation and experimentation](evaluation-and-experimentation.md)

## What this area is about

Machine Learning (ML) answers the question: how can a program acquire behaviour from examples instead of from a programmer? Its answer has three parts that every child of this node elaborates. Choose a **family of functions** with adjustable parameters. Define a **loss** that measures how wrong the function is on data. **Optimise** the parameters to reduce the loss. Then comes the catch that makes ML a science rather than curve fitting: the goal is not low loss on the data you have but on data you will see later. Everything here, from regularisation to held-out test sets, exists to bridge that gap between fitting and generalising.

The unifying idea is **statistical**: data are samples from an unknown distribution, a learned model is an estimate, and every claim about a model is a claim about that distribution, made with uncertainty.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Learning as optimization](learning-as-optimization.md) | The mechanism: loss functions, gradient descent, stochastic gradients | Calculus, optimisation |
| [Generalization and bias-variance](generalization-and-bias-variance.md) | The goal and its obstacle: why fitting the sample is not enough | Statistics; optimisation |
| [Supervised learning](supervised-learning.md) | Learning input-to-output maps from labelled examples | Both of the above |
| [Unsupervised learning](unsupervised-learning.md) | Finding structure, compression and representations without labels | Optimisation, probability |
| [Evaluation and experimentation](evaluation-and-experimentation.md) | Measuring generalisation honestly; the referee for everything else | Statistics; generalisation |

```
              optimisation  ----minimises----> training loss
                   |                                |
                   v                                v  (proxy for)
      supervised / unsupervised models       test loss  <---- generalisation theory
                   \                                ^
                    \------- evaluated by ----------/   evaluation & experimentation
```

Read optimisation first (how parameters move), then generalisation (why that movement is only a proxy), then the two families of tasks, and finish with evaluation, which turns all of the above into claims you can trust. Supervised and unsupervised learning are less separate than their names suggest: self-supervised learning manufactures supervised targets from unlabelled data, and modern systems pre-train without labels and fine-tune with them.

## Connections to sibling areas

- **[Classical AI](../01-classical-ai/README.md):** Classical Artificial Intelligence (AI) hand-writes the model and reasons with it; ML learns the model from data. Probabilistic reasoning is shared ground: a Bayesian network can be hand-built or learned, and maximum likelihood is the common training principle.
- **[Deep learning](../03-deep-learning/README.md):** Deep learning is ML with deep neural networks as the function family, so every principle here applies unchanged. What changes is that features are learned rather than designed, and scale changes the practical behaviour of optimisation and generalisation.
- **[Advanced paradigms](../04-advanced-paradigms/README.md):** Reinforcement learning drops fixed labelled data in favour of rewards from interaction; generative models are unsupervised density estimation you can sample; language models are self-supervised learning at the largest scale. Each inherits the evaluation problems here in harder forms.

## Connections across layers

ML is built from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [calculus and optimisation](../../01-mathematical-foundations/05-continuous-mathematics/README.md), and [probability and statistics](../../01-mathematical-foundations/06-probability-and-statistics/README.md); its compression view comes from [information theory](../../02-theory-of-computation/01-information-theory/README.md). Its data come from [data management](../../09-data-management/README.md) and [batch processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) pipelines. Upward, it supplies learned components to [computer vision](../../14-human-and-visual-computing/03-media-and-vision/computer-vision.md) and interfaces in [Layer 14](../../14-human-and-visual-computing/README.md), and raises the fairness, privacy and accountability questions of [ethics](../../15-computing-in-context/ethics-and-professional-responsibility.md) and [law](../../15-computing-in-context/law-privacy-and-policy.md).

## Cross-cutting threads

- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): training is a feedback loop that measures error and adjusts parameters.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): bias versus variance; precision versus recall; compute versus accuracy.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): features and embeddings decide what a linear model can separate.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): No Free Lunch: no learner wins on every problem.
- [Trust and verification](../../CROSS-CUTTING.md#trust-and-verification): held-out evaluation is the only check on a model without a specification.
