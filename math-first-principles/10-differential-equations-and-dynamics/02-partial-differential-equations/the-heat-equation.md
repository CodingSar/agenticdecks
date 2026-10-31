# The Heat Equation

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Partial Differential Equations](README.md)
> **Builds on:** [Laplace's equation and harmonic functions](laplaces-equation-and-harmonic-functions.md), [Boundary value problems and Sturm–Liouville theory](../01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md), [The Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md), [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md)
> **Enables:** [Nonlinear partial differential equations](nonlinear-pdes.md), [Brownian motion](../../11-probability-and-statistics/03-stochastic-processes/brownian-motion.md), [Stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md), [Mathematical finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md)

## Essence

The heat equation uₜ = Δu says that the temperature at a point rises at a rate proportional to how far it lies below the average of its neighbours. It is the model parabolic partial differential equation (PDE), the equation of every diffusion: heat in a bar, dye in water, probability for a random walker. Its solution is a convolution with a Gaussian, the heat kernel, and three features follow that set it apart from the wave equation: rough data become smooth at once, a disturbance is felt everywhere immediately, and the process cannot be run backwards.

## Core tenets

1. **Fourier analysis solves it: each frequency decays at its own rate.** The Fourier transform in x turns uₜ = Δu on ℝⁿ into ûₜ = −|ξ|²û for each frequency ξ, so û(ξ, t) = e^(−t|ξ|²)·ĝ(ξ), where g is the initial value. Inverting the product gives a convolution:

   ```
   u(x, t) = (Φ(·, t) ∗ g)(x),    Φ(x, t) = (4πt)^(−n/2)·e^(−|x|²/(4t))   for t > 0.
   ```

   The heat kernel Φ is a Gaussian of total mass 1 and width of order √t: heat spreads a distance √t in time t, so doubling the distance quadruples the time.

2. **Diffusion smooths instantly.** For bounded continuous g, u(·, t) is infinitely differentiable for every t > 0, because derivatives fall on the smooth kernel rather than on g; in Fourier terms, e^(−t|ξ|²) kills high frequencies faster than any power of |ξ| grows. A jump in the initial temperature is rounded off at once. As t → 0 the kernel concentrates at the origin and u → g: Φ is an approximate identity.

3. **The backward problem is ill-posed.** Running time backwards multiplies frequency ξ by e^(t|ξ|²), amplifying small errors without limit. For uₜ = −uₓₓ, the heat equation reversed, u = e^(n²t)·sin(nx)/n starts with size 1/n, as small as one likes, and reaches size e^(n²t)/n at time t, as large as one likes. So the solution, when it exists, does not depend continuously on the data, failing Hadamard's test of a well-posed problem: yesterday's temperature cannot be recovered stably from today's.

4. **Heat travels at infinite speed.** If g ≥ 0 and g is not identically zero, then u(x, t) > 0 for every x and every t > 0, since Φ is positive everywhere. A burst of heat at one point is felt at every distance immediately. The effect is of size e^(−|x|²/(4t)), negligible far away, which is why diffusion is still a good model, and why signals obey the wave equation instead.

5. **The maximum principle gives uniqueness, given a growth bound.** On a bounded region Ω over a time interval [0, T], a solution attains its maximum on the parabolic boundary, never in the interior or at the final time. Proof idea: at such an interior maximum uₜ ≥ 0 and Δu ≤ 0; to make this contradictory apply it to v = u + ε|x|², for which vₜ − Δv = −2nε < 0, then let ε → 0. On all of ℝⁿ a growth bound is essential: Tychonoff (1935) built a non-zero solution with zero initial data, and uniqueness holds among solutions with |u| ≤ A·e^(a|x|²).

6. **Energy decays, and the flow runs downhill to a harmonic state.** On a bounded region with u = 0 on the boundary, d/dt ∫u² = 2∫u·Δu = −2∫|∇u|², so the heat equation is the gradient flow of the Dirichlet energy ½∫|∇u|². With the Poincaré inequality, ∫u² ≤ e^(−2λ₁t)∫g², where λ₁ is the first Dirichlet eigenvalue; with fixed non-zero boundary values, u converges to the harmonic function taking them. Hamilton's Ricci flow (1982) is a nonlinear heat equation for the metric of a manifold, and Perelman's analysis of its singularities (2002–2003) proved the [Poincaré conjecture](../../07-topology/03-manifolds/three-manifolds-and-the-poincare-conjecture.md).

7. **Diffusion is the average of random walks.** For a walk stepping ±h every τ seconds, the probability p(x, t) of being at x satisfies p(x, t + τ) = ½p(x − h, t) + ½p(x + h, t); Taylor expansion with h² = 2τ gives pₜ = pₓₓ in the limit. The limit walk is Brownian motion B, with B(t) of variance t, and u(x, t) = E[g(x + B(2t))], the expected value, solves uₜ = Δu. Adding a potential term gives the Feynman–Kac formula, and the Black–Scholes equation for option prices becomes the heat equation after a change of variables.

## Key concepts

| Term | Meaning |
|---|---|
| Heat kernel | Φ(x, t) = (4πt)^(−n/2)·e^(−∣x∣²/(4t)), the temperature due to a unit point source at time 0 |
| Diffusive scaling | The equation is unchanged under x ↦ λx, t ↦ λ²t, so spreading distance grows like √t |
| Parabolic boundary | The initial slice together with the spatial boundary, where maxima are attained |
| Well-posed problem | One with existence, uniqueness and continuous dependence on the data |
| Infinite speed of propagation | Non-negative, non-zero data make the solution positive everywhere at every positive time |
| Gradient flow | Motion in the direction in which an energy decreases fastest |
| Diffusivity | The constant k in uₜ = kΔu, measured in length² per unit time |

## How it fits

- **Below:** the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) diagonalises the equation on ℝⁿ, and [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) on an interval, as the [Sturm–Liouville](../01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md) expansion with time factors; the Laplacian as "average minus value" comes from [Laplace's equation](laplaces-equation-and-harmonic-functions.md).
- **Above:** [Brownian motion](../../11-probability-and-statistics/03-stochastic-processes/brownian-motion.md) is the heat kernel made random, and Itô's formula in [stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md) extends tenet 7 to all diffusions; [mathematical finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md) prices options this way; [numerical methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) meet stiffness here, since explicit schemes need time steps of order h² for grid spacing h.
- **Siblings:** the [wave equation](the-wave-equation.md) is the opposite in each respect: finite speed, no smoothing, reversible; Duhamel's formula with Φ drives [nonlinear PDEs](nonlinear-pdes.md); [weak solutions](weak-solutions-and-sobolev-spaces.md) handle rough coefficients.

## Common misconceptions

- **"Heat spreads with a front moving at finite speed."**: the kernel is positive everywhere at once; what spreads like √t is the bulk of the heat, not an edge.
- **"Since the past determined the present, the present determines the past."**: backward uniqueness holds on bounded regions, but reconstruction is unstable, since errors at frequency ξ grow like e^(t|ξ|²); inverse problems need regularisation.
- **"A smooth solution needs smooth initial data."**: a jump, or any bounded measurable g, gives a solution that is smooth at every positive time.

## Go deeper

- Lawrence C. Evans, *Partial Differential Equations* (2nd edition, 2010): the heat kernel, maximum principle and energy methods with full proofs.
- Joseph Fourier, *Théorie analytique de la chaleur* (1822): the founding text, where Fourier series were introduced to solve this equation.
- David V. Widder, *The Heat Equation* (1975): a classical monograph on the heat kernel and uniqueness classes.
