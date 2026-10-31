# Optimisation

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › Optimisation
> **Children:** [Linear Programming](linear-programming.md) · [Convex Optimisation and Duality](convex-optimisation-and-duality.md) · [Gradient Methods](gradient-methods.md)

## What this area is about

Optimisation chooses the best point of a set: minimise f(x) subject to constraints. Almost every applied question can be phrased this way, from scheduling and transport to estimating parameters, designing controllers and training neural networks, and Lagrange's multipliers already showed in the eighteenth century how constraints and objectives trade off. The modern subject, born with linear programming in the 1940s, adds two things. The first is a theory of when a problem is tractable: convexity, not linearity, is the dividing line, because convex problems have no false local minima and come with dual problems that certify their answers. The second is a theory of algorithms with guaranteed costs: how many iterations, each of what price, are needed to reach a given accuracy. Its central object is the pair of a problem and its dual, one minimising and one maximising, which meet at the optimum.

## How the children fit together

```
        linear programming
   (vertices, simplex, duality, interior points)
                 |
     convex optimisation and duality
   (Lagrangian, Slater, KKT, cone programmes)
                 |
           gradient methods
   (rates, acceleration, stochastic gradients)
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Linear programming](linear-programming.md) | The prototype: polyhedra, the simplex method, the ellipsoid and interior-point methods, and duality as a min–max theorem | Polytopes, separation, linear algebra |
| [Convex optimisation and duality](convex-optimisation-and-duality.md) | The general theory: weak and strong duality, Slater's condition, the Karush–Kuhn–Tucker (KKT) conditions, semidefinite programming | Linear programming, Lagrange multipliers |
| [Gradient methods](gradient-methods.md) | The scalable algorithms: convergence rates in terms of the condition number, Nesterov acceleration, stochastic gradient descent | Convex optimisation, Monte Carlo methods |

Linear programming is read first because everything in it generalises: the polyhedron becomes a convex set, linear programming duality becomes Lagrangian duality, complementary slackness becomes part of the KKT conditions, and the logarithmic barrier of interior-point methods becomes the self-concordant barriers that solve semidefinite programmes. Convex optimisation then supplies the structure that algorithms exploit, and gradient methods supply the algorithms that scale.

There are two families of algorithm. Second-order methods, such as interior-point methods built on Newton's method, reach high accuracy in a few dozen expensive steps, each a large linear solve. First-order methods use only gradients, each step cheap, and need many steps, a number governed by the condition number κ, or by √κ with acceleration. Lower bounds show the first-order rates are optimal, so the choice between families is a choice about problem size and required accuracy, not a matter of taste. Stochastic gradients push this further: when f is an average over millions of data points, a noisy gradient from one point is better value than an exact one.

## Connections to sibling areas

- [Numerical analysis](../01-numerical-analysis/README.md): interior-point methods are Newton's method plus numerical linear algebra; gradient descent is explicit Euler on the gradient flow, with the same stability limit; stochastic gradients are Monte Carlo estimates.
- [Information, codes and cryptography](../03-information-codes-and-cryptography/README.md): channel capacity is a maximisation of mutual information over input distributions, a concave problem, and linear programming relaxations give decoders and bounds on the size of codes.
- [Mathematical modelling](../04-mathematical-modelling/README.md): optimal control chooses inputs to minimise a cost, and model predictive control solves a convex programme at each step.
- [Games, decisions and finance](../05-games-decisions-and-finance/README.md): von Neumann's minimax theorem is linear programming duality, and mean–variance portfolio selection is a quadratic programme.
- [Data and learning](../06-data-and-learning/README.md): fitting a model is minimising a loss; the lasso and compressed sensing are convex, and deep networks are trained by stochastic gradient methods.

## Connections across layers

Optimisation rests on [convex geometry](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md), whose separation theorems are the source of every duality theorem, on [Lagrange multipliers](../../06-real-analysis/03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md) and on [positive definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md). The [calculus of variations](../../10-differential-equations-and-dynamics/03-calculus-of-variations/the-euler-lagrange-equation.md) is optimisation in infinite dimensions, and combinatorial optimisation meets it through [network flows](../../03-combinatorics-and-graph-theory/02-graph-theory/matchings-and-network-flows.md). Whether linear programming has a strongly polynomial algorithm is listed among [open problems](../../15-mathematics-in-context/open-problems.md), open as of 2026.

## Cross-cutting threads

- [Duality](../../CROSS-CUTTING.md#duality): every problem has a dual bounding it, and strong duality makes them meet.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): the area is the systematic study of extremal problems.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): gradient steps use first-order models, Newton steps second-order ones.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): stochastic gradients trade exactness for cheapness.
