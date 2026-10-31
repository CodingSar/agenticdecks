# The Derivative as a Linear Map

> **Layer:** [06 Real Analysis](../README.md) › [Calculus of Several Variables](README.md)
> **Builds on:** [The derivative and the mean value theorem](../02-calculus-of-one-variable/the-derivative-and-the-mean-value-theorem.md), [Continuity](../01-limits-and-convergence/continuity.md), [Linear maps and matrices](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [Inner products and orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md)
> **Enables:** [Inverse and implicit function theorems](inverse-and-implicit-function-theorems.md), [Extrema and Lagrange multipliers](extrema-and-lagrange-multipliers.md), [Topological and smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [Gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md), [Neural networks and backpropagation (CS)](../../../cs-first-principles/13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md)

## Essence

In one variable the derivative looks like a number, the slope. In several variables it must be what that number always secretly was: the linear map that best approximates the change in f near a point. For f from ℝⁿ to ℝᵐ, the derivative at a is an m × n matrix, the Jacobian, and differentiability means that f(a + h) − f(a) is that matrix applied to h, plus an error small compared with ∥h∥. Partial derivatives alone do not capture this, and examples show how they can exist while f is not even continuous. Seeing the derivative as a linear map makes the chain rule a product of matrices, which is all of backpropagation, and makes the gradient a vector determined by an inner product.

## Core tenets

1. **f is differentiable at a when a linear map approximates it to first order.** Let U be open in ℝⁿ and f: U → ℝᵐ. Then f is differentiable at a if there is a linear map Df(a): ℝⁿ → ℝᵐ with
   ```
   f(a + h) = f(a) + Df(a)h + o(∥h∥)   as h → 0
   ```
   Such a map is unique, and its matrix is the Jacobian, whose entry in row i and column j is the partial derivative ∂fᵢ/∂xⱼ(a). For n = m = 1 the matrix is 1 × 1 and the definition is the familiar one.

2. **Partial derivatives, and even all directional derivatives, do not imply differentiability.** Let f(x, y) = xy/(x² + y²) away from 0 and f(0, 0) = 0. Both partial derivatives at 0 are 0, because f vanishes on the axes, yet f = ½ along the line y = x, so f is not even continuous at 0. Worse, g(x, y) = x²y/(x⁴ + y²), with g(0, 0) = 0, has a directional derivative at 0 in every direction, but g = ½ along the parabola y = x², so g is not differentiable there. Partial derivatives see only the axes, and directional derivatives see only straight lines.

3. **Continuous partial derivatives do imply differentiability.** If all the partial derivatives exist near a and are continuous at a, then f is differentiable at a. Proof idea: move from a to a + h one coordinate at a time, and apply the one-variable mean value theorem (MVT) to each step. Continuity of the partials makes the error of each step o(∥h∥). Such f is called C¹, and nearly every function met in practice is.

4. **The chain rule is matrix multiplication.** If f is differentiable at a and g at f(a), then D(g ∘ f)(a) = Dg(f(a))·Df(a): the best linear approximation of a composite is the composite of the best linear approximations. A neural network is a long composite of simple maps ending in a single number, the loss. Multiplying the Jacobians from the output end, so that each step is a row vector times a matrix, gives the gradient with respect to every parameter at a cost comparable to evaluating the network once. That is [backpropagation](../../../cs-first-principles/13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md).

5. **The gradient is the vector that represents the derivative through the inner product.** For real-valued f, Df(a) is a linear functional, so there is a unique vector ∇f(a) with Df(a)h = ⟨∇f(a), h⟩. For a unit vector u, Cauchy–Schwarz gives |Df(a)u| ≤ ∥∇f(a)∥, with equality when u points along ∇f(a). So the gradient points in the direction of steepest ascent, and it is perpendicular to the level set through a. Changing the inner product changes the gradient but not the derivative, which is the idea behind preconditioning in [gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md).

6. **The mean value theorem becomes an inequality.** If f is differentiable on an open set containing the segment from a to b, then
   ```
   ∥f(b) − f(a)∥ ≤ sup ∥Df(x)∥ · ∥b − a∥
   ```
   with the sup over the segment and ∥Df(x)∥ the operator norm, the largest factor by which Df(x) stretches a vector. Proof idea: apply the one-variable MVT to t ↦ ⟨f(a + t(b − a)), v⟩, where v is the unit vector along f(b) − f(a). No equality version holds for vector-valued maps: (cos t, sin t) has non-zero derivative but returns to its start at t = 2π. One consequence: if Df = 0 on a connected open set, f is constant.

7. **The second derivative is a symmetric bilinear form when f is C².** For real-valued f, the Hessian is the matrix of second partials ∂²f/∂xᵢ∂xⱼ, and Taylor's theorem becomes f(a + h) = f(a) + ⟨∇f(a), h⟩ + ½⟨h, Hh⟩ + o(∥h∥²). If the second partials are continuous, the Hessian is symmetric: the order of differentiation does not matter. Without continuity it can: Peano's example xy(x² − y²)/(x² + y²), with value 0 at the origin, has mixed partials −1 and 1 there, depending on the order.

## Key concepts

| Term | Meaning |
|---|---|
| Derivative Df(a) | The linear map with f(a + h) = f(a) + Df(a)h + o(∥h∥) |
| Jacobian | The m × n matrix of Df(a), with entries ∂fᵢ/∂xⱼ |
| Partial derivative | The derivative along one coordinate axis, others held fixed |
| Directional derivative | The derivative of t ↦ f(a + tu) at t = 0 |
| C¹ function | One whose partial derivatives exist and are continuous |
| Gradient ∇f | The vector with Df(a)h = ⟨∇f(a), h⟩ |
| Operator norm | The largest value of ∥Ah∥ over unit vectors h |
| Hessian | The symmetric matrix of second partial derivatives of a C² function |

## How it fits

- **Below:** The one-variable [derivative and MVT](../02-calculus-of-one-variable/the-derivative-and-the-mean-value-theorem.md) supply the definition's shape and every proof; [linear maps and matrices](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md) supply the target; [inner products](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md) turn the derivative into the gradient.
- **Above:** Manifolds are spaces where this derivative still makes sense, via [smooth charts](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md). [Gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md) step along −∇f.
- **Siblings:** The [inverse and implicit function theorems](inverse-and-implicit-function-theorems.md) say that an invertible derivative makes f locally invertible. [Extrema](extrema-and-lagrange-multipliers.md) occur where the derivative vanishes, and the Hessian classifies them.

## Common misconceptions

- **"If all the partial derivatives exist, f is differentiable."** Not even continuity follows (tenet 2); continuous partials are needed (tenet 3).
- **"The gradient belongs to the function alone."** It depends on the inner product; the derivative, a linear functional, is the intrinsic object (tenet 5).
- **"Mixed partial derivatives always commute."** Only when they are continuous; Peano's example shows otherwise (tenet 7).

## Go deeper

- Michael Spivak, *Calculus on Manifolds* (1965): a short, rigorous account built entirely on the derivative as a linear map.
- James R. Munkres, *Analysis on Manifolds* (1991): a patient development of differentiation and integration in ℝⁿ.
- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): chapter 9 treats functions of several variables.
