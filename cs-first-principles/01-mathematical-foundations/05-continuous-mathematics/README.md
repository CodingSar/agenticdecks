# Continuous Mathematics

> **Layer:** [01 Mathematical Foundations](../README.md) › Continuous Mathematics
> **Children:** [Calculus](calculus.md) · [Optimization](optimization.md)

## What this area is about

Continuous mathematics deals with quantities that vary smoothly: real numbers, rates of change, areas, and functions that can be approximated locally by straight lines. A computer is a discrete machine, so it may seem odd to need it. But much of what computers model is continuous (light, sound, motion, probability densities), and many discrete problems become tractable only when relaxed into continuous ones. The unifying idea is *local linearisation*: near any point, a smooth function behaves like a linear map, so a hard global problem can be attacked by many small, easy linear steps. Calculus provides the linearisation; optimisation turns it into algorithms that find the best answer.

Today this area is most visible in machine learning, where a model with billions of parameters is trained by following gradients computed by the chain rule. It is equally present in the analysis of algorithms (limits, integrals bounding sums), in graphics and simulation (differential equations, integrals over light paths), and in networking performance (fluid models of congestion control, optimisation views of fair bandwidth sharing).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Calculus](calculus.md) | Limits, derivatives, gradients, integrals, Taylor approximation, the chain rule | Functions, linear algebra |
| [Optimization](optimization.md) | Finding minima: gradient descent, convexity, constraints and duality, linear and integer programming | Calculus, linear algebra |

Read calculus first. It answers "which way is downhill and how curved is the ground?". Optimisation answers "how far should I step, when should I stop, and can I trust that the answer is the best one?".

```
     calculus                        optimization
  f(x+h) ≈ f(x) + ∇f·h      ──►   x ← x − η ∇f(x)
  chain rule (backprop)            convexity ⇒ local = global
  Hessian (curvature)       ──►   step size η < 2/L; condition number
  integrals                 ──►   expectations in stochastic gradients
```

The dependency is one-way but tight. Every first-order method needs gradients; every second-order method needs Hessians; every convergence guarantee is a statement about curvature. Conversely, optimisation explains why calculus matters so much to Computer Science (CS): most of the derivatives computed by computers are computed in order to minimise something.

## Connections to sibling areas

- **[Logic](../01-logic/README.md):** The ε–δ definition of a limit is a nested-quantifier statement; continuity proofs are predicate-logic proofs.
- **[Sets, Relations and Functions](../02-sets-relations-functions/README.md):** Calculus studies functions on the uncountable set of reals; computers can only represent a finite subset of them, the origin of [floating-point](../../03-digital-logic/01-number-representation/floating-point.md) rounding.
- **[Discrete Mathematics](../03-discrete-mathematics/README.md):** Integrals bound discrete sums in recurrence analysis, and linear-programming relaxations bound integer and graph problems such as matching and flow.
- **[Algebra](../04-algebra/README.md):** Multivariable calculus is linear algebra at each point: gradients are vectors, Jacobians and Hessians are matrices.
- **[Probability and Statistics](../06-probability-and-statistics/README.md):** Continuous distributions are defined by integrals; maximum-likelihood estimation is an optimisation problem; stochastic gradient descent uses probability to make optimisation cheap.

## Connections across layers

Downward, the area underlies the continuous models of [00 Engineering Foundations](../../00-engineering-foundations/README.md) ([signals and systems](../../00-engineering-foundations/04-signals-and-systems/README.md), [circuit timing](../../00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md)), though as mathematics it does not depend on them. Upward it feeds [asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [approximation algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md) and [network flow](../../05-algorithms-and-data-structures/05-graph-algorithms/network-flow.md), [congestion control](../../08-networking/04-transport-layer/congestion-control.md), [query optimization](../../09-data-management/03-query-processing/query-optimization.md), all of [machine learning](../../13-artificial-intelligence/02-machine-learning-foundations/README.md) and [deep learning](../../13-artificial-intelligence/03-deep-learning/README.md), and [computer graphics](../../14-human-and-visual-computing/02-computer-graphics/README.md).

## Cross-cutting threads

- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): gradient descent measures the error and adjusts the parameters, the same loop as congestion control.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): objectives and constraints make trade-offs explicit; Lagrange multipliers price them.
- [Composition](../../CROSS-CUTTING.md#composition): the chain rule differentiates compositions, making deep networks trainable.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): minibatches amortise gradient computation across examples.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): non-convex and integer problems admit no general efficient guarantee.
