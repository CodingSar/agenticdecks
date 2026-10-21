# Learning as Optimization

> **Layer:** [13 Artificial Intelligence](../README.md) › [Machine learning foundations](README.md)
> **Builds on:** [Optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md)
> **Enables:** [Supervised learning](supervised-learning.md), [Neural networks and backpropagation](../03-deep-learning/neural-networks-and-backpropagation.md), [Training at scale](../03-deep-learning/training-at-scale.md)

## Essence

Machine Learning (ML) replaces hand-written rules with a parameterised function f_θ and a procedure that adjusts the parameters θ so that the function behaves well on examples. "Behaves well" is made precise by a **loss function** that scores each prediction; learning is then the optimisation problem of minimising average loss over the training data. Almost all modern ML solves this problem with variants of **gradient descent**: compute how the loss changes as each parameter changes, and move every parameter a small step downhill. The surprising empirical fact behind deep learning is that this simple local procedure, applied with noisy mini-batch gradients to models with billions of parameters, finds solutions that work on data never seen in training.

## Core tenets

1. **Learning is minimising empirical risk.** Given examples (x_i, y_i) and a loss ℓ, we choose

   θ* = argmin_θ (1/n) Σ_i ℓ(f_θ(x_i), y_i) + λ R(θ)

   The first term is the *empirical risk* (average training loss); R(θ) is an optional regulariser that prefers simpler parameters. What we actually want is low *expected* loss on new data from the same distribution, which the sample average only estimates; that gap is the subject of [generalisation](generalization-and-bias-variance.md).

2. **The loss encodes what you care about, often through likelihood.** Squared error corresponds to maximum likelihood under Gaussian noise; cross-entropy, −log p_θ(y | x), corresponds to maximum likelihood for categorical outputs. Choosing a loss is choosing a probabilistic model of the data. Losses must be differentiable (or have usable subgradients) for gradient methods, which is why we optimise cross-entropy rather than raw accuracy.

3. **Gradient descent follows the steepest local downhill direction.** The update is

   θ ← θ − η ∇_θ L(θ)

   with learning rate η. For a convex loss with L-Lipschitz gradient, a step size η ≤ 1/L guarantees convergence to the global minimum. Too large a step diverges; too small wastes compute. The learning rate is the single most important knob in practice.

4. **Stochastic gradients make learning scale.** Computing the exact gradient needs a pass over all n examples. Stochastic Gradient Descent (SGD) uses a random mini-batch of B examples (typically 32 to a few thousand) instead: an unbiased but noisy gradient estimate at B/n of the cost. Many cheap noisy steps beat few exact ones, and the noise helps escape sharp, poorly generalising regions.

5. **Momentum and adaptive methods tame bad curvature.** When the loss surface is a long narrow valley, plain gradient descent zig-zags. Momentum accumulates a running average of gradients, damping oscillation. Adam (2014) also rescales each parameter's step by a running estimate of its gradient magnitude; Adam and its weight-decay variant AdamW are the default optimisers for large neural networks as of the mid-2020s.

6. **Convex problems have one answer; neural networks do not.** Linear and logistic regression and Support Vector Machines (SVMs) have convex losses: every local minimum is global and solutions are reproducible. Neural network losses are non-convex with countless minima and saddle points, yet in high dimensions most critical points SGD meets are saddles it can escape, and many minima generalise comparably well. Theory here still lags practice.

7. **Gradients must be computed automatically.** Hand-deriving gradients for millions of parameters is impossible. Reverse-mode automatic differentiation computes the full gradient of a scalar loss at a cost of a small constant multiple of one forward evaluation, independent of the number of parameters. This is [backpropagation](../03-deep-learning/neural-networks-and-backpropagation.md), and it is what makes gradient-based learning practical at scale.

## Key concepts

| Term | Meaning |
|---|---|
| Parameters θ | Numbers inside the model that learning adjusts (weights and biases) |
| Hyperparameters | Settings chosen outside training: learning rate, batch size, model size |
| Loss function | Per-example penalty for a wrong prediction |
| Empirical risk | Average loss over the training set |
| Cross-entropy | −log of the probability the model assigns to the correct answer |
| Learning rate η | Step size of each gradient update |
| Mini-batch | Random subset of examples used to estimate one gradient |
| Epoch | One full pass over the training data |
| Regularisation | Penalty or constraint that biases learning toward simpler solutions |

## How it fits

- **Below:** The objective and the update come straight from [optimisation](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md) and [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md); the computation is matrix arithmetic from [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md); loss choices come from [maximum-likelihood estimation](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md). The rounding behaviour of [floating point](../../03-digital-logic/01-number-representation/floating-point.md) limits how small steps can be.
- **Above:** Every model in [supervised learning](supervised-learning.md) and [deep learning](../03-deep-learning/README.md) is trained this way; [training at scale](../03-deep-learning/training-at-scale.md) is the systems engineering of running this loop on thousands of accelerators.
- **Siblings:** [Generalisation](generalization-and-bias-variance.md) explains why minimising training loss is not the goal itself. [Evaluation](evaluation-and-experimentation.md) measures whether optimisation produced something useful.

## Common misconceptions

- **"Training finds the best possible model."** It finds a low-loss point reachable from the initialisation with the chosen optimiser, which is rarely the global minimum and need not be. What matters is test performance.
- **"Lower training loss is always better."** Driving training loss to zero on noisy data can memorise noise; the target is low loss on unseen data.
- **"Gradient descent needs the loss to be convex."** Convexity gives guarantees, not feasibility. Gradient methods work on non-convex losses, without global guarantees.

## Go deeper

- Léon Bottou, Frank Curtis and Jorge Nocedal, "Optimization Methods for Large-Scale Machine Learning" (2018): why SGD dominates and how its variants behave.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004): the theory of the well-behaved case.
- Diederik Kingma and Jimmy Ba, "Adam: A Method for Stochastic Optimization" (2014): the optimiser most deep networks use.
