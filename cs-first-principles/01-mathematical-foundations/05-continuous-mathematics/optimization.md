# Optimization

> **Layer:** [01 Mathematical Foundations](../README.md) › [Continuous Mathematics](README.md)
> **Builds on:** [Calculus](calculus.md), [Linear Algebra](../04-algebra/linear-algebra.md)
> **Enables:** [Learning as Optimization](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md), [Training at Scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), [Approximation Algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md), [Network Flow](../../05-algorithms-and-data-structures/05-graph-algorithms/network-flow.md), [Query Optimization](../../09-data-management/03-query-processing/query-optimization.md)

## Essence

Optimization is the problem of choosing the input that minimises (or maximises) an objective function, possibly subject to constraints. A remarkable amount of computer science is optimization in disguise: training a model minimises a loss, routing minimises path cost, scheduling minimises completion time, compilers minimise instruction count, and congestion control seeks maximum throughput without loss. The mathematics divides problems into those whose structure guarantees that local improvement finds the global best (convex problems, linear programs) and those where it does not (most neural network training, integer programs). The working tools are gradients to find a descent direction, Lagrange multipliers and duality to handle constraints, and an understanding of curvature to choose step sizes.

## Core tenets

1. **Every optimization problem has the same parts.** A decision variable *x*, an objective *f(x)*, and a feasible set defined by constraints *g(x) ≤ 0*, *h(x) = 0*. Writing a problem in this form forces clarity about what is being traded off. Many engineering disputes are really disagreements about the objective (latency versus throughput, accuracy versus fairness).

2. **At an unconstrained smooth minimum the gradient is zero; curvature tells you what kind of point it is.** ∇f(x*) = 0 is necessary for a local minimum. The Hessian's eigenvalues then classify the point: all positive is a minimum, mixed signs is a saddle. In high-dimensional neural network losses, saddle points and flat regions vastly outnumber bad local minima, which helps explain why simple gradient methods work as well as they do.

3. **Gradient descent steps downhill, and the step size is bounded by curvature.** The update `x ← x − η∇f(x)` decreases *f* for small enough η. If the largest Hessian eigenvalue is *L*, steps with η < 2/L are stable; larger steps oscillate and diverge. The convergence rate depends on the condition number *L/μ* (largest over smallest curvature): long narrow valleys make plain gradient descent zig-zag, which is what momentum, preconditioning and adaptive methods such as Adam address.

4. **Stochastic gradients trade exactness for cost.** When *f* is an average over *n* training examples, Stochastic Gradient Descent (SGD) estimates the gradient from a small random minibatch. Each step costs O(batch) rather than O(n), and the noise is unbiased, so many cheap noisy steps beat few exact ones. The noise also helps escape saddle points. Batch size then becomes a systems knob: larger batches use parallel hardware better but give diminishing returns per example.

5. **Convexity makes local equal global.** A function is convex if the segment between any two points on its graph lies on or above the graph. For a convex function on a convex set, every local minimum is a global minimum, and efficient algorithms with guarantees exist. Least squares, logistic regression, Support Vector Machines (SVMs) and many resource-allocation problems are convex. Recognising convexity is the single most useful skill in applied optimization, because it decides whether you can trust the answer.

6. **Constraints become prices: Lagrange multipliers and duality.** At a constrained optimum, the objective's gradient is a combination of the active constraints' gradients; the coefficients (Lagrange multipliers) measure how much the optimum would improve if each constraint were relaxed slightly. The Karush–Kuhn–Tucker (KKT) conditions generalise this to inequalities. Every problem has a *dual* whose value bounds the original's. In networking, Kelly's analysis of congestion control interprets link prices as dual variables, and Transmission Control Protocol (TCP) as a distributed algorithm for a utility-maximisation problem.

7. **Linear programming is the polynomial-time workhorse of discrete optimization.** A Linear Program (LP) optimises a linear objective under linear constraints; its optimum lies at a vertex of the feasible polytope. The simplex method (Dantzig, 1947) is fast in practice; interior-point methods are polynomial in theory and practice. Max-flow, shortest paths and many scheduling problems are LPs, and LP duality is the max-flow min-cut theorem in general form.

8. **Integer constraints make problems hard, and relaxation is the standard escape.** Requiring variables to be integers (choose this server or not) makes optimization NP-hard in general (NP is Nondeterministic Polynomial time), since NP-complete problems such as the travelling salesman reduce to it. The standard technique is to relax to an LP, solve that, and round or branch. The LP value bounds the integer optimum, which is how [approximation algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md) prove guarantees and how [branch and bound](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md) prunes.

## Key concepts

| Term | Meaning |
|---|---|
| Objective / loss | The function being minimised |
| Feasible set | Inputs satisfying all constraints |
| Local / global minimum | Best in a neighbourhood / best overall |
| Learning rate (η) | Step size in gradient methods |
| Condition number | Ratio of largest to smallest curvature; slows first-order methods |
| SGD | Gradient descent using a random minibatch estimate of the gradient |
| Convex function | Lies below the chord between any two points; local minimum is global |
| Lagrange multiplier | Sensitivity of the optimum to relaxing a constraint |
| Duality | Paired problem whose optimum bounds the original's |
| LP | Linear objective with linear constraints; solvable in polynomial time |
| Relaxation | Dropping a hard constraint (such as integrality) to get a tractable bound |

## How it fits

- **Below:** [Calculus](calculus.md) supplies gradients and Hessians; [linear algebra](../04-algebra/linear-algebra.md) supplies the geometry of curvature and the machinery for LPs; [probability](../06-probability-and-statistics/probability.md) justifies stochastic gradients.
- **Above:** [Learning as optimization](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) and [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) are applied gradient methods. [Network flow](../../05-algorithms-and-data-structures/05-graph-algorithms/network-flow.md) and [approximation algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md) use LP and duality. [Congestion control](../../08-networking/04-transport-layer/congestion-control.md) is distributed optimization with feedback. [Query optimizers](../../09-data-management/03-query-processing/query-optimization.md) and [register allocators](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md) search discrete spaces for low-cost plans.
- **Siblings:** [Calculus](calculus.md) gives the local picture; optimization turns it into an algorithm with step sizes, stopping rules and guarantees.

## Common misconceptions

- **"Gradient descent finds the global minimum."** Only for convex problems; elsewhere it finds a stationary point that depends on initialisation and step size.
- **"A bigger learning rate trains faster."** Beyond about 2/L it diverges; the useful range is set by curvature.
- **"Rounding an LP solution gives the integer optimum."** Rounded solutions can be infeasible or far from optimal; guarantees need a proof for the specific problem.

## Go deeper

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004): the standard text, free online.
- Jorge Nocedal and Stephen Wright, *Numerical Optimization* (2nd ed., 2006): algorithms for smooth problems.
- Léon Bottou, Frank Curtis and Jorge Nocedal, "Optimization Methods for Large-Scale Machine Learning" (SIAM Review, 2018): why SGD dominates machine learning.
- Frank Kelly, Aman Maulloo and David Tan, "Rate Control for Communication Networks: Shadow Prices, Proportional Fairness and Stability" (1998): congestion control as optimization.
