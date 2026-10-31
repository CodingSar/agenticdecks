# Linear Programming

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Optimisation](README.md)
> **Builds on:** [Polytopes](../../08-geometry/03-convex-and-discrete-geometry/polytopes.md), [Convex Sets and Separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md), [Linear Systems and Rank–Nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Matchings and Network Flows](../../03-combinatorics-and-graph-theory/02-graph-theory/matchings-and-network-flows.md), [Root-Finding and Newton's Method](../01-numerical-analysis/root-finding-and-newtons-method.md)
> **Enables:** [Convex Optimisation and Duality](convex-optimisation-and-duality.md), [Game Theory](../05-games-decisions-and-finance/game-theory.md), [Network Flow (CS)](../../../cs-first-principles/05-algorithms-and-data-structures/05-graph-algorithms/network-flow.md), [Approximation Algorithms (CS)](../../../cs-first-principles/05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md)

## Essence

A linear programme asks for the maximum of a linear function cᵀx subject to linear inequalities Ax ≤ b. The feasible set is a polyhedron, and a bounded optimum is always attained at a vertex, so the problem is combinatorial in disguise: which constraints are tight? Three landmark algorithms answer it: the simplex method walks along edges, the ellipsoid method proved the problem solvable in polynomial time, and interior-point methods made that guarantee practical. Behind all of them is duality: every linear programme has a twin whose optimal value is the same, and the dual solution certifies the primal one.

## Core tenets

1. **If an optimum exists, one is attained at a vertex.** A linear function on a polyhedron with at least one vertex either is unbounded above or attains its maximum on a face, and every face contains a vertex. Algebraically, writing the constraints in standard form Ax = b, x ≥ 0 with A of rank m, vertices are basic feasible solutions: choose m linearly independent columns, solve for those variables and set the rest to zero. There are at most C(n, m) of them: finitely many, but exponentially many.

2. **The simplex method walks uphill along edges.** George Dantzig's method (1947) moves from a vertex to an adjacent one, exchanging one basic column for another, whenever an edge improves the objective; when none does, the vertex is optimal, since local optima of linear functions on convex sets are global. Robert Bland's smallest-index rule (1977) prevents cycling at degenerate vertices. In practice its step count is roughly proportional to the number of constraints.

3. **In the worst case simplex takes exponential time, and the reason is still not fully understood.** Victor Klee and George Minty (1972) built a squashed n-dimensional cube on which Dantzig's pivot rule visits all 2ⁿ vertices; similar examples defeat most known rules. Whether some pivot rule always runs in polynomial time is open as of 2026; so is the polynomial Hirsch conjecture, that the graph of every polytope has diameter polynomial in its dimension and number of facets. The original Hirsch bound, facets minus dimension, was refuted by Francisco Santos (announced 2010, published 2012) with a 43-dimensional polytope with 86 facets. Daniel Spielman and Shang-Hua Teng (2001) explained the practical speed by smoothed analysis: after a small random perturbation of the data, the expected running time is polynomial.

4. **The ellipsoid method proved linear programming polynomial.** Leonid Khachiyan (1979) adapted an ellipsoid method from nonlinear optimisation: keep an ellipsoid containing the feasible region, test its centre, and cut through the centre by a violated constraint; the half-ellipsoid fits in a new ellipsoid whose volume is smaller by a factor at most e^(−1/(2(n+1))). Bounding the initial volume and the smallest relevant volume by the bit length L of the data gives a polynomial bound. Slow in practice, it needs only a separation oracle, which Martin Grötschel, László Lovász and Alexander Schrijver exploited to show many combinatorial problems polynomial.

5. **Interior-point methods follow a central path through the inside.** Narendra Karmarkar (1984) gave a polynomial method fast in practice. In its modern barrier form, maximise cᵀx + μ ∑ log sᵢ, where the sᵢ are the slacks in the constraints, so the logarithm keeps iterates strictly inside; as μ → 0 the maximisers trace the central path to an optimal vertex. Each step is a Newton step; O(√n L) steps suffice in theory, a few dozen in practice. Whether linear programming has a strongly polynomial algorithm, with step count depending only on the numbers of variables and constraints, is open as of 2026 (Stephen Smale's ninth problem).

6. **Every linear programme has a dual with the same optimal value.** The dual of maximising cᵀx subject to Ax ≤ b, x ≥ 0 is minimising bᵀy subject to Aᵀy ≥ c, y ≥ 0. Weak duality is one line: cᵀx ≤ (Aᵀy)ᵀx = yᵀAx ≤ yᵀb. Strong duality, equality when either side has an optimum, follows from Farkas's lemma (Gyula Farkas, 1902): either Ax ≤ b has a solution or a nonnegative combination of the inequalities gives the contradiction 0 ≤ −1. At optimality complementary slackness holds: a constraint with positive dual price is tight. The dual variables are shadow prices, the rate at which the optimum improves as each bᵢ is relaxed, as Leonid Kantorovich (1939) and Tjalling Koopmans read them in economics.

7. **Duality explains combinatorial min–max theorems.** The maximum flow through a network, written as a linear programme, has as dual a fractional minimum cut; because the constraint matrix is totally unimodular (every square submatrix has determinant 0, 1 or −1), both have integral optimal vertices, and linear programming duality becomes the max-flow min-cut theorem. Von Neumann's minimax theorem for zero-sum games is likewise duality. Restricting variables to integers destroys this picture: integer programming is NP-hard, at least as hard as every problem in NP (nondeterministic polynomial time).

## Key concepts

| Term | Meaning |
|---|---|
| Linear programme | Optimise a linear function subject to linear equalities and inequalities |
| Basic feasible solution | A vertex: m linearly independent tight columns, the other variables zero |
| Dual programme | The linear programme whose variables price the primal constraints |
| Complementary slackness | At optimality, each dual variable is zero or its primal constraint is tight |
| Central path | The curve of barrier maximisers leading to the optimum as μ → 0 |

## How it fits

- **Below:** the feasible set is a [polyhedron](../../08-geometry/03-convex-and-discrete-geometry/polytopes.md); strong duality is a [separation theorem](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md); basic solutions come from [rank and linear systems](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), and [network flows](../../03-combinatorics-and-graph-theory/02-graph-theory/matchings-and-network-flows.md) are the prototype.
- **Above:** [convex optimisation](convex-optimisation-and-duality.md) generalises both duality and interior-point methods; the minimax theorem of [game theory](../05-games-decisions-and-finance/game-theory.md) is a duality theorem; rounding relaxations is a basic tool for [approximation algorithms](../../../cs-first-principles/05-algorithms-and-data-structures/07-advanced-topics/approximation-algorithms.md); ℓ₁ minimisation in [compressed sensing](../06-data-and-learning/sampling-and-compressed-sensing.md) is a linear programme.
- **Siblings:** [gradient methods](gradient-methods.md) are the first-order alternative for very large problems; each interior-point step is a [Newton step](../01-numerical-analysis/root-finding-and-newtons-method.md) solved by [numerical linear algebra](../01-numerical-analysis/numerical-linear-algebra.md).

## Common misconceptions

- **"Simplex is exponential, so it is a bad algorithm"**: exponential examples are carefully constructed; on real problems simplex remains competitive with interior-point methods, and smoothed analysis explains part of why.
- **"An integer optimum is the rounded real optimum"**: rounding can be infeasible or far from optimal; only special structure, such as total unimodularity, makes the relaxation exact.

## Go deeper

- Vašek Chvátal, *Linear Programming* (1983): simplex and duality, clearly.
- Alexander Schrijver, *Theory of Linear and Integer Programming* (1986): the complete theory.
- Jiří Matoušek and Bernd Gärtner, *Understanding and Using Linear Programming* (2007): short and modern.
