# Convex Optimisation and Duality

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Optimisation](README.md)
> **Builds on:** [Convex Sets and Separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md), [Extrema and Lagrange Multipliers](../../06-real-analysis/04-calculus-of-several-variables/extrema-and-lagrange-multipliers.md), [Quadratic Forms and Positive Definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md), [Linear Programming](linear-programming.md), [Root-Finding and Newton's Method](../01-numerical-analysis/root-finding-and-newtons-method.md)
> **Enables:** [Gradient Methods](gradient-methods.md), [Statistical Learning Theory](../06-data-and-learning/statistical-learning-theory.md), [Sampling and Compressed Sensing](../06-data-and-learning/sampling-and-compressed-sensing.md), [Mathematical Finance](../05-games-decisions-and-finance/mathematical-finance.md), [Control Theory](../04-mathematical-modelling/control-theory.md)

## Essence

A convex optimisation problem minimises a convex function over a convex set, typically given by convex inequalities fᵢ(x) ≤ 0 and affine equations. R. Tyrrell Rockafellar (1993) put its importance in one sentence: the great watershed in optimisation is not between linearity and nonlinearity but between convexity and nonconvexity. Convex problems have no spurious local minima, they come with a dual problem that bounds and usually matches the optimum, their optima are characterised by the Karush–Kuhn–Tucker (KKT) conditions, and they can be solved efficiently by interior-point methods. Linear programming is the special case where everything is linear; least squares, portfolio selection, sparse regression and many relaxations of hard combinatorial problems are others.

## Core tenets

1. **For convex problems, local minima are global.** If x is a local minimiser and y is feasible with f(y) < f(x), then points (1 − t)x + ty on the segment are feasible, because the set is convex, and satisfy f((1 − t)x + ty) ≤ (1 − t)f(x) + tf(y) < f(x), because f is convex; taking t small contradicts local minimality. So any descent method that stops at a local minimum has found the answer, and the set of minimisers is itself convex, a single point when f is strictly convex.

2. **Every problem has a concave dual that bounds it from below.** For the problem of minimising f₀(x) subject to fᵢ(x) ≤ 0, form the Lagrangian and the dual function:

   ```
   L(x, λ) = f₀(x) + λ₁f₁(x) + ⋯ + λₘfₘ(x)
   g(λ)    = inf over x of L(x, λ)
   ```

   Then g is concave, as an infimum of affine functions of λ, and weak duality holds: for λ ≥ 0 and feasible x, g(λ) ≤ L(x, λ) ≤ f₀(x), since each λᵢfᵢ(x) ≤ 0. The dual problem, maximise g(λ) over λ ≥ 0, is convex even when the primal is not, so it always gives a computable lower bound d* ≤ p*.

3. **Slater's condition closes the gap.** If the problem is convex and some point satisfies every inequality strictly, then d* = p* and the dual optimum is attained (Morton Slater, 1950). The proof separates two convex sets in the space of (constraint values, objective value): the set of achievable pairs and the set of pairs strictly better than optimal; the separating hyperplane's normal is the optimal multiplier, and strict feasibility keeps it from being vertical. Without such a condition convexity alone is not enough: minimising e^(−x) subject to x²/y ≤ 0 over y > 0 is convex with p* = 1, yet d* = 0.

4. **The Karush–Kuhn–Tucker conditions characterise optima.** For a convex problem with differentiable fᵢ and strong duality, as under Slater's condition, x* and λ* are primal and dual optimal if and only if

   ```
   ∇f₀(x*) + λ₁*∇f₁(x*) + ⋯ + λₘ*∇fₘ(x*) = 0     (stationarity)
   fᵢ(x*) ≤ 0,   λᵢ* ≥ 0,   λᵢ*fᵢ(x*) = 0       (feasibility, complementary slackness)
   ```

   They generalise Lagrange multipliers to inequalities: an inactive constraint has zero multiplier, and at the optimum −∇f₀ lies in the cone spanned by the gradients of the active constraints. William Karush stated them in a master's thesis (1939); Harold Kuhn and Albert Tucker rediscovered them (1951). Without convexity they are only necessary, and then only under a constraint qualification.

5. **Multipliers are prices.** If the constraint fᵢ(x) ≤ 0 is relaxed to fᵢ(x) ≤ uᵢ, the optimal value p*(u) is convex in u, and under strong duality −λ* is a subgradient of p* at u = 0. A large multiplier marks a constraint whose loosening pays; a zero multiplier marks one that does not matter locally. This is the economic reading of linear programming duality, now for every convex problem.

6. **A hierarchy of cones is solvable in polynomial time.** Linear programmes sit inside convex quadratic programmes, which sit inside second-order cone programmes, which sit inside semidefinite programmes, where the variable is a symmetric matrix constrained to be positive semidefinite. Yurii Nesterov and Arkadi Nemirovski (1994) showed that interior-point methods with self-concordant barriers solve all of them to accuracy ε in a number of Newton steps growing like the square root of a barrier parameter times log(1/ε). Semidefinite relaxation gives the Goemans–Williamson algorithm (1995), which finds a cut within a factor about 0.878 of the maximum cut of a graph, a problem that is itself intractable to solve exactly.

## Key concepts

| Term | Meaning |
|---|---|
| Convex problem | Minimising a convex function over a convex feasible set |
| Lagrangian | The objective plus multiplier-weighted constraints |
| Dual function | The infimum of the Lagrangian over x; always concave |
| Duality gap | p* − d*, always nonnegative; zero under Slater's condition |
| Complementary slackness | At an optimum, each multiplier is zero or its constraint is active |
| Semidefinite programme | Linear objective over affine slices of the cone of positive semidefinite matrices |

## How it fits

- **Below:** strong duality is a [separation theorem](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md); the conditions extend [Lagrange multipliers](../../06-real-analysis/04-calculus-of-several-variables/extrema-and-lagrange-multipliers.md) to inequalities; convexity of a smooth function is [positive semidefiniteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md) of its Hessian; [linear programming](linear-programming.md) is the prototype.
- **Above:** regularised estimators such as the lasso (Robert Tibshirani, 1996) and support vector machines are convex programmes studied in [statistical learning theory](../06-data-and-learning/statistical-learning-theory.md); ℓ₁ recovery in [compressed sensing](../06-data-and-learning/sampling-and-compressed-sensing.md) is convex; Harry Markowitz's portfolio selection (1952) in [mathematical finance](../05-games-decisions-and-finance/mathematical-finance.md) is a quadratic programme; model predictive [control](../04-mathematical-modelling/control-theory.md) solves one at every time step.
- **Siblings:** [gradient methods](gradient-methods.md) solve large convex problems to moderate accuracy; interior-point methods take [Newton steps](../01-numerical-analysis/root-finding-and-newtons-method.md) whose systems are solved by [numerical linear algebra](../01-numerical-analysis/numerical-linear-algebra.md).

## Common misconceptions

- **"Convex problems always have zero duality gap"**: they need a constraint qualification such as Slater's condition; the example in tenet 3 is convex with gap 1.
- **"Nonconvex means hopeless"**: duality still gives lower bounds, convex relaxations give approximation guarantees, and some nonconvex problems, such as finding the best low-rank approximation of a matrix, are solved exactly by the singular value decomposition.

## Go deeper

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004): the standard text, free online.
- R. Tyrrell Rockafellar, *Convex Analysis* (1970): the foundations, including conjugate duality.
- Dimitri Bertsekas, *Convex Optimization Theory* (2009): duality developed geometrically.
