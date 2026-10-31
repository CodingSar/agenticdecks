# Extrema and Lagrange Multipliers

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of Several Variables](README.md)
> **Builds on:** [The derivative as a linear map](the-derivative-as-a-linear-map.md), [Inverse and implicit function theorems](inverse-and-implicit-function-theorems.md), [Taylor expansion](../02-calculus-of-one-variable/taylor-expansion.md), [Compactness in metric spaces](../04-metric-spaces/compactness-in-metric-spaces.md), [Quadratic forms and positive definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md)
> **Enables:** [Convex optimisation and duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md), [Gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md), [The Euler–Lagrange equation](../../10-differential-equations-and-dynamics/03-calculus-of-variations/the-euler-lagrange-equation.md), [Optimization (CS)](../../../cs-first-principles/01-mathematical-foundations/05-continuous-mathematics/optimization.md)

## Essence

Finding the largest or smallest value of a function of several variables takes three separate steps. First, show that an extremum exists, usually by compactness. Second, find the candidates: in the interior they are the points where the gradient vanishes, and on a constraint surface they are the points where the gradient of f is a combination of the gradients of the constraints, the method of Lagrange multipliers. Third, decide which candidates are maxima, minima or saddles, using the Hessian. Each step has hypotheses, and in two or more dimensions intuitions from one variable fail in surprising ways.

## Core tenets

1. **At an interior local extremum of a differentiable function, the gradient vanishes.** If f has a local maximum or minimum at an interior point a, then for each direction u the one-variable function t ↦ f(a + tu) has an extremum at t = 0, so its derivative ⟨∇f(a), u⟩ is 0. Hence ∇f(a) = 0. The converse fails: x² − y² has gradient 0 at the origin, which is a saddle point. At boundary points the gradient need not vanish: x on [0, 1] is largest at x = 1, where its derivative is 1.

2. **Existence comes first, and in two dimensions one critical point is not enough.** A continuous function on a non-empty compact set attains its maximum and minimum, by the extreme value theorem (EVT) of [compactness](../04-metric-spaces/compactness-in-metric-spaces.md). Without compactness, strange things happen. In one variable, a differentiable function whose only critical point is a local minimum has a global minimum there. In two variables this fails:
   ```
   f(x, y) = x² + y²·(1 − x)³
   ```
   has exactly one critical point, the origin, which is a strict local minimum with f = 0. Yet f(4, 1) = 16 − 27 = −11, and f is unbounded below.

3. **The Hessian classifies non-degenerate critical points.** Let f be C² with ∇f(a) = 0 and Hessian H at a. Then f(a + h) = f(a) + ½⟨h, Hh⟩ + o(∥h∥²). If H is positive definite, ⟨h, Hh⟩ ≥ λ·∥h∥² where λ > 0 is its smallest eigenvalue, which beats the error, so a is a strict local minimum. Negative definite gives a strict local maximum, and indefinite, with eigenvalues of both signs, gives a saddle. If H is only semidefinite the test is silent: x² + y⁴ and x² − y⁴ both have Hessian with eigenvalues 2 and 0 at the origin, but the first has a minimum and the second a saddle.

4. **Lagrange multipliers find extrema on a constraint set.** Let f and g₁, …, g_k be C¹ on an open set in ℝⁿ, let M be the set where every gᵢ = 0, and let a in M be a local extremum of f restricted to M. If the gradients ∇g₁(a), …, ∇g_k(a) are linearly independent, there are numbers λ₁, …, λ_k with
   ```
   ∇f(a) = λ₁∇g₁(a) + ⋯ + λ_k∇g_k(a)
   ```
   Proof idea: by the [implicit function theorem](inverse-and-implicit-function-theorems.md), M near a is a smooth surface whose tangent vectors form ker Dg(a). Along every curve in M through a, f has a critical point, so ∇f(a) is orthogonal to that kernel. The orthogonal complement of the kernel is the span of the ∇gᵢ.

5. **The independence condition cannot be dropped.** Minimise f(x, y) = x on the cusp y² = x³. Every point has x = y^(2/3) ≥ 0, so the minimum is at the origin. There ∇g = (−3x², 2y) = (0, 0), while ∇f = (1, 0) is no multiple of it. The equation of tenet 4 fails at the true minimum. In practice, points where the constraint gradients are dependent must be checked separately.

6. **Applied to a quadratic form, the method proves that symmetric matrices have eigenvectors.** For a symmetric matrix A, maximise ⟨x, Ax⟩ on the unit sphere ⟨x, x⟩ = 1. The sphere is compact, so a maximum exists. The Lagrange condition reads 2Ax = 2λx: the maximiser is an eigenvector, and the maximum value is the largest eigenvalue. Repeating on the orthogonal complement gives the [spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md).

7. **A multiplier is the price of its constraint.** If the constraint is g = c and f* is the optimal value, then df*/dc = λ under mild conditions. Maximising xy subject to x + y = c gives x = y = c/2, value c²/4 and λ = c/2, which is exactly d(c²/4)/dc. In economics λ is a shadow price. With inequality constraints, the Karush–Kuhn–Tucker (KKT) conditions add λ ≥ 0 and require λ = 0 when a constraint is slack, and they lead to [convex duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md).

## Key concepts

| Term | Meaning |
|---|---|
| Critical point | A point where ∇f = 0 |
| Saddle point | A critical point that is neither a local maximum nor a local minimum |
| Hessian | The symmetric matrix of second partial derivatives |
| Positive definite | ⟨h, Hh⟩ > 0 for every h ≠ 0; all eigenvalues positive |
| Constraint set | The points where g₁ = ⋯ = g_k = 0 |
| Lagrange multiplier | The coefficient λᵢ in ∇f = ∑λᵢ∇gᵢ |
| Lagrangian | f − ∑λᵢgᵢ, whose unconstrained critical points give the Lagrange conditions |
| Constraint qualification | A condition, such as independent ∇gᵢ, under which the multiplier rule holds |

## How it fits

- **Below:** [The derivative as a linear map](the-derivative-as-a-linear-map.md) defines the gradient and Hessian; the second-order expansion comes from [Taylor expansion](../02-calculus-of-one-variable/taylor-expansion.md); [quadratic forms](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md) classify the Hessian.
- **Above:** [Convex optimisation](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md) turns multipliers into a dual problem, and [gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md) search for critical points numerically. The [Euler–Lagrange equation](../../10-differential-equations-and-dynamics/03-calculus-of-variations/the-euler-lagrange-equation.md) is ∇f = 0 in a space of functions. Machine learning is mostly [optimization (CS)](../../../cs-first-principles/01-mathematical-foundations/05-continuous-mathematics/optimization.md) of this kind.
- **Siblings:** The [implicit function theorem](inverse-and-implicit-function-theorems.md) justifies the multiplier rule.

## Common misconceptions

- **"A unique critical point that is a local minimum must be the global minimum."** True in one variable, false in two (tenet 2).
- **"The second derivative test always gives an answer."** A semidefinite Hessian leaves the question open (tenet 3).
- **"Lagrange multipliers find the extremum."** They find candidates, and only where the constraint gradients are independent. Existence and the degenerate points must be handled separately (tenets 2 and 5).

## Go deeper

- Jerrold E. Marsden and Anthony Tromba, *Vector Calculus* (6th edition, 2012): extrema, the Hessian test and Lagrange multipliers with many examples.
- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004): multipliers, duality and the KKT conditions.
- Jorge Nocedal and Stephen J. Wright, *Numerical Optimization* (2nd edition, 2006): optimality conditions and the algorithms built on them.
