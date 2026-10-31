# Numerical Methods for Differential Equations

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Numerical Analysis](README.md)
> **Builds on:** [Existence and Uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md), [First-Order Equations and Characteristics](../../10-differential-equations-and-dynamics/02-partial-differential-equations/first-order-equations-and-characteristics.md), [Weak Solutions and Sobolev Spaces](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), [Floating Point, Conditioning and Stability](floating-point-conditioning-and-stability.md), [Numerical Linear Algebra](numerical-linear-algebra.md)
> **Enables:** [Modelling and Dimensional Analysis](../04-mathematical-modelling/modelling-and-dimensional-analysis.md), [Control Theory](../04-mathematical-modelling/control-theory.md), [Mathematical Biology and Epidemics](../04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Mathematical Finance](../05-games-decisions-and-finance/mathematical-finance.md)

## Essence

A computer cannot follow a continuous trajectory; it takes steps. For an Ordinary Differential Equation (ODE) y′ = f(t, y), a method advances by a step h using a few evaluations of f, and its error is an accumulation of local errors, each amplified or damped by the equation itself. Accuracy, how fast the error shrinks as h → 0, and stability, whether errors stay bounded at step sizes you can afford, are separate demands; for stiff problems and waves, stability is the binding one. The organising theorem: consistency plus stability is equivalent to convergence.

## Core tenets

1. **Euler's method converges, with error proportional to h.** Explicit Euler sets y_(n+1) = yₙ + h f(tₙ, yₙ), following the tangent line. If f is Lipschitz in y with constant L, each step commits a local error of order h² (by Taylor's theorem) and multiplies earlier errors by at most 1 + hL ≤ e^(hL). Summing T/h local errors, each amplified by at most e^(LT), gives a global error of order h on [0, T].

2. **Runge–Kutta methods raise the order by sampling f inside the step.** The classical fourth-order method of Carl Runge (1895) and Wilhelm Kutta (1901), RK4, combines four evaluations of f per step to match the Taylor series of the solution through the h⁴ term; halving h cuts the error about 16-fold. From order 5 on, an explicit method needs more stages than its order. Production codes, such as the Dormand–Prince pair (1980), compare estimates of two orders to choose each step size.

3. **Stability is decided by the test equation y′ = λy.** On it, a one-step method gives y_(n+1) = R(hλ)yₙ, so it decays, as the true solution does when Re λ < 0, only if ∣R(hλ)∣ ≤ 1; the set of such z = hλ is the stability region. For explicit Euler R(z) = 1 + z, whose region is the disc of radius 1 centred at −1, so λ = −1000 forces h ≤ 0.002 however smooth the solution. An explicit Runge–Kutta method has a polynomial R, and a nonconstant polynomial is unbounded, so its stability region is bounded.

4. **Stiff problems need implicit methods.** A problem is stiff when some modes decay far faster than the solution of interest changes. For y′ = −1000(y − cos t) − sin t with y(0) = 1, the solution is just cos t, yet explicit Euler is accurate to 10⁻⁶ with h = 0.0015 and reaches −1.7 × 10¹⁵ by t = 0.3 with h = 0.0025. Backward Euler, y_(n+1) = yₙ + h f(t_(n+1), y_(n+1)), has R(z) = 1/(1 − z), with ∣R∣ ≤ 1 on the whole left half-plane: it is A-stable, and with h = 0.1 it is accurate to 3 × 10⁻⁵, at the price of a Newton solve per step. Germund Dahlquist proved (1963) that an A-stable linear multistep method has order at most 2, so the workhorses for stiff systems, backward differentiation formulas, give up a little stability for order.

5. **For a Partial Differential Equation (PDE), the numerical domain of dependence must contain the true one.** For uₜ + a uₓ = 0, information travels along characteristics at speed a. A scheme with grid spacing Δx and time step Δt that combines neighbouring values sees only Δx/Δt units of distance per unit time, so it cannot converge unless ∣a∣Δt/Δx ≤ 1: the Courant–Friedrichs–Lewy (CFL) condition (1928). It is necessary, not sufficient: the forward-time centred-space scheme multiplies the grid mode e^(ijθ) by a factor g with ∣g∣² = 1 + ν² sin²θ, where ν = aΔt/Δx, so it is unstable for every ν > 0. For the heat equation uₜ = uₓₓ the explicit scheme needs Δt ≤ Δx²/2; the Crank–Nicolson scheme (1947) needs no restriction.

6. **Consistency plus stability is equivalent to convergence.** The Lax equivalence theorem (Peter Lax and Robert Richtmyer, 1956) says that for a consistent finite-difference approximation to a well-posed linear initial value problem, stability is necessary and sufficient for convergence. Sufficiency is the argument of tenet 1; necessity is the uniform boundedness principle. Consistency is checked by Taylor expansion, stability by John von Neumann's Fourier analysis of grid modes.

7. **Finite elements solve the weak form in a finite-dimensional subspace.** Multiplying −Δu = f by a test function v and integrating by parts gives the weak form ∫ ∇u·∇v = ∫ fv for all v in a Sobolev space V. The Galerkin method imposes this only for v in a subspace Vₕ of piecewise polynomials on a mesh, giving a sparse symmetric positive definite system. Subtracting the two equations shows that the error is orthogonal to Vₕ in the energy inner product, so uₕ is the best approximation to u from Vₕ in the energy norm; for piecewise linear elements and smooth u that error is O(h). Richard Courant proposed the idea in 1943; its ease with irregular geometry made it the standard of structural mechanics.

## Key concepts

| Term | Meaning |
|---|---|
| Order p | Global error O(hᵖ) as the step h → 0 |
| Stability region | The set of z = hλ for which the method keeps solutions of y′ = λy bounded |
| Stiffness | Widely separated time scales, with fast modes that decay |
| A-stable | Stability region containing the whole left half-plane |
| CFL number | ∣a∣Δt/Δx: grid cells crossed by a wave in one time step |

## How it fits

- **Below:** convergence proofs use the Lipschitz condition of [existence and uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md); the CFL condition is the discrete shadow of [characteristics](../../10-differential-equations-and-dynamics/02-partial-differential-equations/first-order-equations-and-characteristics.md); finite elements stand on [weak solutions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md); von Neumann analysis is [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md) on a grid; necessity in Lax's theorem comes from [Baire category](../../09-advanced-analysis/03-functional-analysis/hahn-banach-and-baire-category.md).
- **Above:** simulations in [modelling](../04-mathematical-modelling/modelling-and-dimensional-analysis.md), [control](../04-mathematical-modelling/control-theory.md) and [epidemiology](../04-mathematical-modelling/mathematical-biology-and-epidemics.md) run on these methods; in [mathematical finance](../05-games-decisions-and-finance/mathematical-finance.md) the Black–Scholes equation, a [heat equation](../../10-differential-equations-and-dynamics/02-partial-differential-equations/the-heat-equation.md) after a change of variables, is solved by finite differences.
- **Siblings:** implicit steps call [Newton's method](root-finding-and-newtons-method.md), whose linear systems go to [numerical linear algebra](numerical-linear-algebra.md); multistep formulas integrate [interpolants](interpolation-and-approximation.md); stochastic differential equations combine these schemes with [Monte Carlo methods](monte-carlo-methods.md).

## Common misconceptions

- **"Instability is a rounding-error problem"**: explicit Euler on a stiff problem blows up in exact arithmetic too, amplifying its own truncation errors by ∣R(hλ)∣ > 1 per step.
- **"Higher order is always better"**: over long times structure can matter more. On the harmonic oscillator explicit Euler multiplies the energy by exactly 1 + h² per step, while the equally cheap symplectic Euler method keeps orbits bounded, which is why [Hamiltonian systems](../../10-differential-equations-and-dynamics/04-dynamical-systems/hamiltonian-systems-and-integrability.md) such as planetary orbits are integrated symplectically.

## Go deeper

- Ernst Hairer, Syvert P. Nørsett and Gerhard Wanner, *Solving Ordinary Differential Equations I* (2nd edition, 1993), and volume II, on stiff problems, by Hairer and Wanner (2nd edition, 1996): the reference.
- Arieh Iserles, *A First Course in the Numerical Analysis of Differential Equations* (2nd edition, 2009): concise and rigorous on ODEs and PDEs.
- Susanne C. Brenner and L. Ridgway Scott, *The Mathematical Theory of Finite Element Methods* (3rd edition, 2008): the analysis of finite elements.
