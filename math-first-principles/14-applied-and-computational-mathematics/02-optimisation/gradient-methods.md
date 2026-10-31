# Gradient Methods

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Optimisation](README.md)
> **Builds on:** [The Derivative as a Linear Map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Quadratic Forms and Positive Definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md), [Convex Optimisation and Duality](convex-optimisation-and-duality.md), [Monte Carlo Methods](../01-numerical-analysis/monte-carlo-methods.md), [Martingales](../../11-probability-and-statistics/03-stochastic-processes/martingales.md)
> **Enables:** [The Mathematics of Deep Learning](../06-data-and-learning/the-mathematics-of-deep-learning.md), [Statistical Learning Theory](../06-data-and-learning/statistical-learning-theory.md), [Learning as Optimization (CS)](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md)

## Essence

Gradient descent repeats one step: move against the gradient, xₖ₊₁ = xₖ − η∇f(xₖ). Each step costs one gradient and no matrix factorisation, so the method scales to problems with billions of variables where Newton's method cannot even store the Hessian. Its theory is a set of sharp rates that depend on two numbers: the smoothness constant L, bounding how fast the gradient changes, and the strong convexity constant μ, bounding how curved f is from below. Their ratio κ = L/μ, the condition number, governs everything. Two refinements define modern practice: Nesterov's acceleration, which reaches the best rate possible for any method using only gradients, and stochastic gradients, which replace the exact gradient by a cheap noisy estimate.

## Core tenets

1. **A small enough step always decreases f.** If ∇f is L-Lipschitz, then f(y) ≤ f(x) + ⟨∇f(x), y − x⟩ + (L/2)‖y − x‖², the descent lemma, obtained by integrating the gradient along the segment. With η = 1/L it gives f(xₖ₊₁) ≤ f(xₖ) − ‖∇f(xₖ)‖²/(2L). Summing over K steps, even for nonconvex f bounded below by f*, the smallest gradient seen satisfies min ‖∇f(xₖ)‖² ≤ 2L(f(x₀) − f*)/K: gradient descent finds approximate stationary points, not necessarily minima.

2. **Convexity and strong convexity give global rates.** For convex f with minimiser x*, step 1/L gives f(xₖ) − f* ≤ L‖x₀ − x*‖²/(2k), a sublinear rate. If f is also μ-strongly convex, f(xₖ) − f* ≤ (1 − μ/L)ᵏ(f(x₀) − f*), a linear rate in the numerical-analysis sense: a fixed number of correct digits per κ steps. On the quadratic f(x) = ½xᵀAx the error is multiplied by I − ηA, so the slowest eigendirection, with eigenvalue μ, sets the pace while the fastest, with eigenvalue L, limits the step: iterates zigzag across narrow valleys.

3. **The step-size limit is a stability limit.** On the quadratic, gradient descent converges if and only if η < 2/L, since otherwise 1 − ηL < −1 and the stiffest component grows. Gradient descent is the explicit Euler method applied to the gradient flow x′ = −∇f(x), and this is exactly Euler's stability restriction on a stiff linear system: ill-conditioned optimisation and stiff differential equations are the same phenomenon.

4. **Momentum accelerates, and nothing using only gradients can do better.** Yurii Nesterov's method (1983) adds a carefully weighted extrapolation, taking the gradient step from yₖ = xₖ + βₖ(xₖ − xₖ₋₁). It achieves f(xₖ) − f* = O(L‖x₀ − x*‖²/k²) for convex f and error decreasing like (1 − 1/√κ)ᵏ for strongly convex f, so the dependence on κ improves to √κ, the same gain the conjugate gradient method achieves on quadratics. Arkadi Nemirovski and David Yudin (1983) proved matching lower bounds: on suitably constructed quadratics, any method whose iterates lie in the span of previously computed gradients cannot do better than order 1/k² in the early iterations. Boris Polyak's heavy-ball method (1964) accelerates on quadratics but can fail on general strongly convex functions.

5. **Noisy gradients still converge if the steps shrink at the right rate.** Herbert Robbins and Sutton Monro (1951) sought a root of a function observable only with noise, taking steps aₙ with ∑aₙ = ∞, so the iterates can travel any distance, and ∑aₙ² < ∞, so the accumulated noise has finite variance. Stochastic gradient descent applies this to f(x) = average of fᵢ(x) over a large data set, using the gradient of one randomly chosen fᵢ, an unbiased Monte Carlo estimate of ∇f. Proofs treat the noise as a martingale difference sequence. The rates are slower, O(1/k) for strongly convex f with steps of order 1/k and O(1/√k) for convex f with averaging, but each step costs a single example rather than the whole data set, and these rates are optimal for stochastic first-order methods.

6. **Nonsmooth and constrained problems need modified steps.** For convex f without a gradient, the subgradient method converges at rate O(1/√k) with diminishing steps, and this cannot be improved for general nonsmooth convex functions. When f = g + h with g smooth and h simple but nonsmooth, such as the ℓ₁ norm of the lasso, the proximal gradient method takes a gradient step on g and then solves a small problem for h exactly, recovering the smooth rates, and accelerating like Nesterov's method.

## Key concepts

| Term | Meaning |
|---|---|
| L-smooth | ∇f is Lipschitz with constant L; equivalently, curvature at most L |
| Strongly convex | f minus (μ/2)‖x‖² is convex; curvature at least μ |
| Condition number | κ = L/μ; the iteration count of gradient descent grows like κ |
| Acceleration | Momentum that improves the dependence from κ to √κ |
| Stochastic gradient | An unbiased random estimate of the gradient from a sample of the data |
| Robbins–Monro conditions | Step sizes with ∑aₙ = ∞ and ∑aₙ² < ∞ |
| Proximal step | Exact minimisation of the simple part plus a quadratic penalty |

## How it fits

- **Below:** the gradient is the [derivative as a linear map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md) read through an inner product; L and μ are bounds on a [quadratic form](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md); [convexity](convex-optimisation-and-duality.md) turns stationary points into minima; stochastic gradients are [Monte Carlo](../01-numerical-analysis/monte-carlo-methods.md) estimates whose errors form [martingale](../../11-probability-and-statistics/03-stochastic-processes/martingales.md) differences.
- **Above:** training neural networks in [deep learning](../06-data-and-learning/the-mathematics-of-deep-learning.md) is stochastic gradient descent with momentum and adaptive variants such as Adam (Diederik Kingma and Jimmy Ba, 2015), on nonconvex functions where the theory above guarantees much less; [statistical learning theory](../06-data-and-learning/statistical-learning-theory.md) analyses what the minimiser generalises to; the computer-science view is in [learning as optimization](../../../cs-first-principles/13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md).
- **Siblings:** [Newton's method](../01-numerical-analysis/root-finding-and-newtons-method.md) converges quadratically but needs second derivatives; on quadratics, gradient descent is a [Krylov iteration](../01-numerical-analysis/numerical-linear-algebra.md); [interior-point methods](linear-programming.md) are preferred when high accuracy is needed.

## Common misconceptions

- **"Gradient descent converges to a minimum"**: it converges to stationary points, which for nonconvex f may be saddles or poor local minima; with random initialisation, strict saddles are almost surely avoided, but escaping them can be slow.
- **"Acceleration means faster on every step"**: Nesterov's method is not monotone; f can rise for a while, and its advantage is a better worst-case rate, not uniform improvement.

## Go deeper

- Yurii Nesterov, *Lectures on Convex Optimization* (2nd edition, 2018): the rates, lower bounds and acceleration, by their author.
- Jorge Nocedal and Stephen J. Wright, *Numerical Optimization* (2nd edition, 2006): line searches, quasi-Newton methods and practice.
- Léon Bottou, Frank E. Curtis and Jorge Nocedal, "Optimization Methods for Large-Scale Machine Learning", *SIAM Review* (2018): stochastic gradient theory for machine learning.
