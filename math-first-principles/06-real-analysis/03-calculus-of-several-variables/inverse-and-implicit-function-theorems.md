# Inverse and Implicit Function Theorems

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of Several Variables](README.md)
> **Builds on:** [The derivative as a linear map](the-derivative-as-a-linear-map.md), [Completeness and the contraction mapping principle](../04-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [Linear systems and rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md)
> **Enables:** [Extrema and Lagrange multipliers](extrema-and-lagrange-multipliers.md), [Topological and smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [Lie groups and Lie algebras](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md), [Root-finding and Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md)

## Essence

Linear algebra says exactly when a linear system can be solved and how many free parameters the solutions have. The inverse and implicit function theorems say that, near a point, a nonlinear system behaves just like its linearisation, provided the derivative is invertible or has full rank. If Df(a) is invertible, f can be inverted near a. If n equations in n + m unknowns have a derivative of full rank, the solution set is locally the graph of a function of m of the variables. The theorems are local, and the proof is a contraction: solving f(x) = y is rewritten as a fixed-point problem. They are the reason smooth curves, surfaces and matrix groups can be described by equations.

## Core tenets

1. **The inverse function theorem.** Let U be open in ℝⁿ, let f: U → ℝⁿ be C¹ (continuously differentiable), and suppose Df(a) is invertible. Then there are open sets V containing a and W containing f(a) such that f maps V bijectively onto W, the inverse f⁻¹: W → V is C¹, and
   ```
   D(f⁻¹)(f(x)) = Df(x)⁻¹   for x in V
   ```
   The formula follows from the chain rule applied to f⁻¹ ∘ f = identity; the substance is that f⁻¹ exists and is differentiable.

2. **The proof solves f(x) = y with a contraction.** Let A = Df(a). For y near f(a), a solution of f(x) = y is a fixed point of
   ```
   Tᵧ(x) = x + A⁻¹(y − f(x))
   ```
   Its derivative is I − A⁻¹Df(x), which is 0 at a and, because Df is continuous, has operator norm at most ½ on a small closed ball around a. By the mean value inequality Tᵧ is a contraction there, and for y close enough to f(a) it maps the ball into itself. The [contraction mapping principle](../04-metric-spaces/completeness-and-the-contraction-mapping-principle.md) gives exactly one solution in the ball. Estimates from the same inequality show the inverse is differentiable. Newton's method is this iteration with A replaced by Df(xₙ) at each step.

3. **Each hypothesis is needed.**
   - Invertible derivative: x ↦ x³ is a bijection of ℝ, but its derivative at 0 is 0 and its inverse, the cube root, is not differentiable at 0. And x ↦ x² is not injective on any interval around 0.
   - Continuity of the derivative: f(x) = x + 2x² sin(1/x), with f(0) = 0, has f′(0) = 1, yet f′ takes negative values arbitrarily close to 0, so f is not injective on any neighbourhood of 0.
   - The conclusion is only local: the complex exponential, viewed as the map (x, y) ↦ (eˣ cos y, eˣ sin y) from ℝ² to ℝ², has Jacobian determinant e^(2x) ≠ 0 everywhere, but it is not injective, since adding 2π to y changes nothing.

4. **The implicit function theorem.** Write points of ℝⁿ⁺ᵐ as (x, y) with x in ℝⁿ and y in ℝᵐ. Let F: ℝⁿ⁺ᵐ → ℝᵐ be C¹ near (a, b), with F(a, b) = 0 and the m × m matrix D_yF(a, b) invertible. Then near a there is a unique C¹ function g with g(a) = b and F(x, g(x)) = 0, and differentiating that identity by the chain rule gives
   ```
   Dg(x) = −D_yF(x, g(x))⁻¹ · D_xF(x, g(x))
   ```
   Proof idea: apply the inverse function theorem to (x, y) ↦ (x, F(x, y)), whose derivative is invertible exactly when D_yF is. When F is linear this is [solving a linear system](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) for the pivot variables in terms of the free ones.

5. **The circle shows where the theorem stops.** For F(x, y) = x² + y² − 1, D_yF = 2y. Near any point with y ≠ 0, the circle is the graph of y = ±√(1 − x²), with dy/dx = −x/y. At (±1, 0), D_yF = 0 and no function y(x) describes the circle, since each nearby x has two y values or none. There D_xF ≠ 0, so the circle is a graph x(y) instead. The theorem fails only where the derivative of F has rank less than the number of equations.

6. **Regular level sets are manifolds.** If F: ℝᴺ → ℝᵐ is C¹ and DF has rank m at every point where F = 0, then near each such point the zero set is the graph of a C¹ function of N − m variables. So it is a smooth [manifold](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) of dimension N − m, with tangent space ker DF. The sphere is the zero set of ∥x∥² − 1. The orthogonal group, the matrices with AᵀA = I, is a regular level set in the space of matrices, which makes it a [Lie group](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md).

## Key concepts

| Term | Meaning |
|---|---|
| Local diffeomorphism | A C¹ bijection between open sets whose inverse is also C¹ |
| Inverse function theorem | Invertible Df(a) implies f is a local diffeomorphism near a |
| Implicit function theorem | Invertible D_yF lets F(x, y) = 0 be solved locally as y = g(x) |
| Regular value | A value c such that DF has full rank at every point with F = c |
| Level set | The set where F takes a given value |
| Tangent space | ker DF at a point of a regular level set |
| Simplified Newton iteration | x ↦ x + A⁻¹(y − f(x)) with A = Df(a) held fixed |

## How it fits

- **Below:** [The derivative as a linear map](the-derivative-as-a-linear-map.md) supplies Df and the mean value inequality; [completeness and the contraction mapping principle](../04-metric-spaces/completeness-and-the-contraction-mapping-principle.md) supplies the fixed point; [rank–nullity](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) is the linear model.
- **Above:** Smooth [manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) and [Lie groups](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md) are built from regular level sets and local charts. [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) turns the proof into an algorithm.
- **Siblings:** [Lagrange multipliers](extrema-and-lagrange-multipliers.md) use the implicit function theorem to parametrise a constraint set. [Change of variables](multiple-integrals-and-change-of-variables.md) needs a local diffeomorphism.

## Common misconceptions

- **"A non-zero Jacobian determinant everywhere makes f injective."** Only locally; the complex exponential is the counterexample (tenet 3).
- **"If f is a differentiable bijection, its inverse is differentiable."** x³ is a smooth bijection with a non-differentiable inverse (tenet 3).
- **"The implicit function theorem gives a formula for g."** It proves g exists and gives a formula for Dg. Usually g has no closed form and is computed numerically.

## Go deeper

- Michael Spivak, *Calculus on Manifolds* (1965): chapter 2 proves both theorems in a few pages.
- James R. Munkres, *Analysis on Manifolds* (1991): a careful proof with full error estimates.
- Steven G. Krantz and Harold R. Parks, *The Implicit Function Theorem: History, Theory, and Applications* (2002): its history, variants and uses.
