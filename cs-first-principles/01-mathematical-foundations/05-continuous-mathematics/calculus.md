# Calculus

> **Layer:** [01 Mathematical Foundations](../README.md) › [Continuous Mathematics](README.md)
> **Builds on:** [Functions and Cardinality](../02-sets-relations-functions/functions-and-cardinality.md), [Linear Algebra](../04-algebra/linear-algebra.md)
> **Enables:** [Optimization](optimization.md), [Neural Networks and Backpropagation](../../13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md), [Asymptotic Analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [Random Variables and Distributions](../06-probability-and-statistics/random-variables-and-distributions.md), [Sampling and Quantization](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md)

## Essence

Calculus is the mathematics of change and accumulation. The derivative measures how fast a quantity changes, by approximating a function near a point with a straight line (or, in many dimensions, with a linear map). The integral adds up infinitely many small contributions, giving areas, totals and probabilities. The fundamental theorem of calculus says these two operations undo each other. For computer science the most important idea is *local linearisation*: near any point, a smooth function behaves like a linear one, so problems that are hard globally become tractable step by step. Gradient-based training of every modern neural network, the analysis of algorithms by integrals and limits, the physics in graphics and simulation, and continuous probability all rest on it.

## Core tenets

1. **A limit makes "arbitrarily close" precise.** `lim_{x→a} f(x) = L` means *f(x)* can be forced within any tolerance ε of *L* by taking *x* close enough to *a*. Limits define derivatives, integrals and infinite sums, and they are also how asymptotic notation is grounded: `f = O(g)` is a statement about the long-run ratio *f(n)/g(n)*. L'Hôpital's rule and comparison of growth rates (log n ≪ n^ε ≪ n^k ≪ 2^n) come from limits.

2. **The derivative is the best linear approximation.** `f(x + h) ≈ f(x) + f'(x)·h` for small *h*, with error shrinking faster than *h*. In many dimensions the gradient ∇f collects the partial derivatives and points in the direction of steepest increase; for vector-valued functions the Jacobian matrix plays the role of *f'*. This is the step that turns a nonlinear problem into a [linear algebra](../04-algebra/linear-algebra.md) problem.

3. **The chain rule composes derivatives, and backpropagation is the chain rule.** If `y = g(f(x))`, then `dy/dx = g'(f(x))·f'(x)`, and in many dimensions Jacobians multiply. A neural network is a long composition of simple functions. Computing the gradient of the loss with respect to every parameter by applying the chain rule from the output backwards (reverse-mode automatic differentiation) costs only a small constant multiple of one forward evaluation, regardless of the number of parameters. That cost result is why training networks with billions of parameters is possible ([backpropagation](../../13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md)).

4. **Automatic differentiation is exact, unlike numerical differencing.** Approximating `f'(x)` by `(f(x+h) − f(x))/h` suffers both truncation error (h too large) and floating-point cancellation (h too small), so it is accurate to only about half the available digits. Automatic differentiation applies the chain rule to the program's operations and is exact up to rounding. Symbolic differentiation is exact too but can blow up in expression size.

5. **Taylor series explain approximation error.** `f(x + h) = f(x) + f'(x)h + f''(x)h²/2 + …`. Truncating after *k* terms leaves an error of order h^(k+1). This tells you how fast numerical methods converge, why the second derivative (curvature) decides whether a gradient step overshoots, and how libraries compute sin, exp and log from polynomials on small ranges.

6. **Integration accumulates, and sums can be bounded by integrals.** The integral of a rate gives a total; the integral of a probability density gives a probability. For algorithm analysis, a monotone sum is sandwiched by integrals: Σ_{k=1}^{n} 1/k = ln n + O(1), which gives the O(log n) expected depth of random binary search trees and the analysis of quicksort, and Σ k^p grows like n^(p+1)/(p+1).

7. **Exponentials and logarithms are the natural functions of growth and halving.** *e^x* is the function equal to its own derivative, so it describes anything whose growth rate is proportional to its size (compound growth, epidemic-style spread of gossip messages, exponential decay of a moving average). Logarithms count how many times you can halve, so they appear wherever divide-and-conquer or balanced trees do. The approximation (1 − 1/n)^n ≈ 1/e appears in hashing, Bloom filters and random sampling analyses.

8. **Continuous models of discrete systems are approximations to be checked.** Computers are discrete: integers wrap, floats round, time advances in steps. Differential equations simulated with step size Δt accumulate error that depends on the method's order and on stability; too large a step makes a physically stable system explode. The same caution applies to treating large discrete counts as continuous in performance models.

## Key concepts

| Term | Meaning |
|---|---|
| Limit | The value a function approaches as its input approaches a point |
| Derivative | Instantaneous rate of change; slope of the best linear approximation |
| Gradient (∇f) | Vector of partial derivatives; direction of steepest ascent |
| Jacobian | Matrix of partial derivatives of a vector-valued function |
| Hessian | Matrix of second partial derivatives; describes curvature |
| Chain rule | Derivative of a composition is the product of derivatives |
| Integral | Accumulated sum of infinitesimal contributions |
| Taylor series | Polynomial approximation built from derivatives at a point |
| Automatic differentiation | Exact derivative computation by applying the chain rule to a program |
| Convergence | A sequence or iteration approaching a limit |

## How it fits

- **Below:** Calculus works with [functions](../02-sets-relations-functions/functions-and-cardinality.md) on the real numbers; its multivariable form uses vectors and matrices from [linear algebra](../04-algebra/linear-algebra.md).
- **Above:** [Optimization](optimization.md) uses gradients and Hessians to find minima. [Machine learning](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) trains by gradient descent. [Continuous probability](../06-probability-and-statistics/random-variables-and-distributions.md) defines expectations as integrals. [Asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md) uses limits and integral bounds. [Graphics](../../14-human-and-visual-computing/02-computer-graphics/ray-tracing-and-global-illumination.md) computes light transport as an integral estimated by sampling. [Signals](../../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) and [control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) are described by differential equations and Fourier analysis, as is [congestion control](../../08-networking/04-transport-layer/congestion-control.md) modelled as a fluid system.
- **Siblings:** [Optimization](optimization.md) is the main consumer of calculus in computer science: calculus says which way is downhill, optimization decides how far to step and when to stop.

## Common misconceptions

- **"Backpropagation is a special learning algorithm."** It is the chain rule evaluated in reverse order, a general technique (reverse-mode automatic differentiation) that predates deep learning.
- **"Smaller h always gives a better finite-difference derivative."** Below a point, floating-point cancellation dominates and the estimate gets worse.
- **"Discrete computer science does not need calculus."** Algorithm analysis uses limits, integrals and series constantly; machine learning (ML), graphics and networking performance use far more.

## Go deeper

- Michael Spivak, *Calculus* (4th ed., 2008): rigorous single-variable calculus.
- Marc Peter Deisenroth, A. Aldo Faisal and Cheng Soon Ong, *Mathematics for Machine Learning* (2020): vector calculus and its use in ML.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives* (2nd ed., 2008): the theory of automatic differentiation.
