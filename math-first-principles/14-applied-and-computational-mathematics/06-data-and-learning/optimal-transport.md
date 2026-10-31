# Optimal Transport

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Data and Learning](README.md)
> **Builds on:** [Linear Programming](../02-optimisation/linear-programming.md), [Convex Optimisation and Duality](../02-optimisation/convex-optimisation-and-duality.md), [Matchings and Network Flows](../../03-combinatorics-and-graph-theory/02-graph-theory/matchings-and-network-flows.md), [Random Variables and Distributions](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md), [Modes of Convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md)
> **Enables:** [The Mathematics of Deep Learning](the-mathematics-of-deep-learning.md), [Generative Models (CS)](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/generative-models.md)

## Essence

Optimal transport asks for the cheapest way to move one distribution of mass onto another, when moving a unit of mass from x to y costs c(x, y). Gaspard Monge posed it in 1781 for moving earth; Leonid Kantorovich recast it in 1942 as a linear programme over couplings, which made it solvable and gave it a dual. The minimal cost, for c equal to a power of distance, is the Wasserstein distance between probability distributions. Unlike most ways of comparing distributions, it respects the geometry of the underlying space: shifting a distribution slightly changes it slightly.

## Core tenets

1. **Monge's problem asks for a map, and a map may not exist.** Given probability measures μ on X and ν on Y, Monge seeks T : X → Y pushing μ onto ν, so that ν(B) = μ(T⁻¹(B)) for every set B, minimising ∫ c(x, T(x)) dμ. If μ is a point mass at 0 and ν puts half its mass at −1 and half at 1, no map works: a map cannot split an atom. The constraint is also nonlinear in T.

2. **Kantorovich's relaxation is a linear programme with an optimal solution.** Instead of a map, choose a coupling π: a joint distribution on X × Y with marginals μ and ν, saying how much mass goes from each x to each y. Minimise ∫ c dπ over all couplings. The constraints are linear in π, the set of couplings is convex, and for distributions on finitely many points this is exactly the transportation problem of linear programming. On complete separable metric spaces the couplings form a weakly compact set by Prokhorov's theorem, so a lower semicontinuous cost bounded below attains its minimum.

3. **For n equally weighted points, the relaxation changes nothing.** If μ and ν each put mass 1/n on n points, couplings correspond to n × n doubly stochastic matrices scaled by 1/n. By the Birkhoff–von Neumann theorem the vertices of that polytope are permutation matrices, and a linear objective attains its minimum at a vertex. So some optimal coupling is a permutation, an optimal assignment, and Monge's and Kantorovich's problems agree.

4. **Kantorovich duality prices the transport.** The minimal cost equals the supremum of ∫ φ dμ + ∫ ψ dν over pairs of functions with φ(x) + ψ(y) ≤ c(x, y) for all x and y. Think of φ and ψ as loading and unloading prices that never exceed the cost of moving. Weak duality is one line, integrating the constraint against any coupling; strong duality is a separation argument, as in linear programming. Complementary slackness says optimal couplings live on the set where φ(x) + ψ(y) = c(x, y).

5. **For quadratic cost the optimal map is the gradient of a convex function.** Yann Brenier proved (1987 announcement, 1991 paper) that on ℝⁿ with c(x, y) = ∣x − y∣², if μ has a density and both measures have finite second moments, there is a unique optimal coupling, and it is given by a map T = ∇φ with φ convex. In one dimension this is the monotone rearrangement matching quantiles. Writing f and g for the densities of μ and ν, φ solves the Monge–Ampère equation det D²φ(x) = f(x)/g(∇φ(x)), a fully nonlinear partial differential equation.

6. **Wasserstein distances metrise convergence in distribution.** For p ≥ 1, W_p(μ, ν) is the p-th root of the minimal cost with c = dᵖ. It is a metric on distributions with finite p-th moment, and W_p(μₙ, μ) → 0 exactly when μₙ converges in distribution and the p-th moments converge. On the line, W₁ is the area between the two distribution functions. In general W₁ equals the supremum of ∫ f d(μ − ν) over functions with Lipschitz constant 1, the Kantorovich–Rubinstein duality.

7. **Entropy makes transport computable, but dimension makes it hard to estimate.** Exact solvers for n points cost roughly n³ operations. Adding ε times the relative entropy of π to the cost gives a strictly convex problem whose solution has the form diag(u) K diag(v) with K = e^(−c/ε); Richard Sinkhorn's alternating rescaling of rows and columns finds u and v with matrix–vector products. Marco Cuturi (2013) made this the standard method in machine learning. The empirical distribution of n samples in dimension d ≥ 3 is typically at W₁ distance of order n^(−1/d) from the truth, a curse of dimensionality.

8. **Transport turns diffusion into steepest descent.** Richard Jordan, David Kinderlehrer and Felix Otto (1998) showed that the heat equation is the gradient flow of entropy for the W₂ distance, and the Fokker–Planck equation that of a free energy: each small time step minimises the energy plus a W₂ penalty for moving. The same viewpoint defines lower bounds on Ricci curvature for metric spaces without smooth structure.

## Key concepts

| Term | Meaning |
|---|---|
| Transport map | A map T pushing μ onto ν; Monge's unknown |
| Coupling | A joint distribution with marginals μ and ν; Kantorovich's unknown |
| Kantorovich duality | Minimal cost equals the best total of prices φ, ψ with φ(x) + ψ(y) ≤ c(x, y) |
| Brenier's theorem | For quadratic cost and μ with a density, the optimal map is the gradient of a convex function |
| Wasserstein distance W_p | The p-th root of the minimal cost of transport with cost dᵖ |
| Entropic regularisation | Adding a multiple of relative entropy to make the problem smooth and fast to solve |

## How it fits

- **Below:** the discrete problem is a [linear programme](../02-optimisation/linear-programming.md) whose dual is [Lagrangian duality](../02-optimisation/convex-optimisation-and-duality.md); the assignment case is a bipartite [matching](../../03-combinatorics-and-graph-theory/02-graph-theory/matchings-and-network-flows.md); couplings are joint [distributions](../../11-probability-and-statistics/01-measure-theoretic-probability/random-variables-and-distributions.md), and W_p metrises a [mode of convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md); the gradient-flow view recovers the [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md).
- **Above:** Wasserstein generative adversarial networks and other [generative models](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/generative-models.md) train by moving one distribution onto another.
- **Siblings:** [statistical learning theory](statistical-learning-theory.md) asks how fast empirical distributions approach the truth; transport inequalities bound W₂ by relative entropy and so yield the Gaussian concentration of [high-dimensional geometry](high-dimensional-geometry-and-random-matrices.md); [deep learning](the-mathematics-of-deep-learning.md) uses Wasserstein losses.

## Common misconceptions

- **"The Wasserstein distance is just another divergence, like Kullback–Leibler."** The Kullback–Leibler divergence between distributions with disjoint supports is infinite whatever their positions; the Wasserstein distance measures how far apart they are.
- **"Optimal transport always moves mass along a map."** Atoms may need splitting; maps exist under conditions such as Brenier's.

## Go deeper

- C. Villani, *Topics in Optimal Transportation* (2003): the clearest graduate introduction.
- F. Santambrogio, *Optimal Transport for Applied Mathematicians* (2015): calculus of variations, partial differential equations and numerics.
- G. Peyré and M. Cuturi, *Computational Optimal Transport* (2019): algorithms and machine-learning applications.
