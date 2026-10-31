# Stochastic Calculus

> **Layer:** [11 Probability and Statistics](../README.md) › [Stochastic Processes](README.md)
> **Builds on:** [Brownian Motion](brownian-motion.md), [Martingales](martingales.md), [Lᵖ Spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md), [Taylor Expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md), [Existence and Uniqueness](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md)
> **Enables:** [Mathematical Finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md), [Numerical Methods for Differential Equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [Mathematical Biology and Epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [The Mathematics of Deep Learning](../../14-applied-and-computational-mathematics/06-data-and-learning/the-mathematics-of-deep-learning.md), [Generative Models](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/generative-models.md)

## Essence

To model a quantity driven by noise, one wants to write dXₜ = b(Xₜ)·dt + σ(Xₜ)·dBₜ, a stochastic differential equation (SDE), where B is Brownian motion. But Brownian paths have no derivative and infinite length, so ∫ H·dB cannot be a Riemann–Stieltjes integral. Kiyosi Itô's answer (1944) defines it as a limit in L², using the fact that martingale increments are orthogonal. The resulting calculus has one new rule: because the squared increments of B add up to elapsed time, second-order terms survive, and the chain rule acquires an extra term. Everything else, from solving SDEs to pricing options, follows from that correction.

## Core tenets

1. **The integral starts from simple integrands.** If H is a step process, equal on [tₖ, tₖ₊₁) to a random variable Hₖ known at time tₖ, define ∫₀ᵀ H dB = ∑ₖ Hₖ·(B_(tₖ₊₁) − B_(tₖ)). This is the martingale transform of the discrete theory: the integrand is chosen before the increment is seen, so the integral is a martingale with mean 0.

2. **The Itô isometry extends it to all square-integrable adapted integrands.** For simple H, the cross terms vanish because each increment is independent of the past with mean 0, leaving

   ```
   E[ (∫₀ᵀ H dB)² ]  =  E[ ∫₀ᵀ Hₜ² dt ].
   ```

   The map H ↦ ∫ H dB is therefore an isometry from a dense subspace of an L² space of processes into L²(P), and it extends uniquely to the closure. The integral is defined only up to null events and only as a limit in L², not path by path.

3. **The evaluation point matters, unlike in ordinary calculus.** Approximate ∫₀ᵀ B dB by sums over a partition with mesh tending to 0:

   ```
   left endpoints   ∑ B_(tₖ)·ΔBₖ        →  ½B_T² − ½T     (Itô)
   right endpoints  ∑ B_(tₖ₊₁)·ΔBₖ      →  ½B_T² + ½T
   midpoints        ∑ ½(B_(tₖ) + B_(tₖ₊₁))·ΔBₖ  →  ½B_T²   (Stratonovich)
   ```

   The difference between right and left is ∑(ΔBₖ)², the quadratic variation, which tends to T. Itô's choice keeps the martingale property; Ruslan Stratonovich's keeps the ordinary chain rule.

4. **Itô's formula: the chain rule with a second-order term.** Expand f(Bₜ) by Taylor's theorem to second order. The term ½f″·(ΔB)² does not vanish, because (ΔB)² ≈ Δt on average and sums to t. The rule is (dB)² = dt, dB·dt = 0, (dt)² = 0, and for a process with dX = b·dt + σ·dB:

   ```
   df(t, Xₜ)  =  ( ∂f/∂t + b·∂f/∂x + ½σ²·∂²f/∂x² ) dt  +  σ·∂f/∂x · dB.
   ```

   For f(x) = x² this gives d(B²) = 2B·dB + dt, which is tenet 3 again. Itô published the formula in 1951.

5. **Stochastic differential equations are solved by Picard iteration.** If b and σ are Lipschitz, the SDE has a unique solution, by the same contraction argument that proves existence and uniqueness for an ordinary differential equation (ODE), with the Itô isometry in place of the integral estimate. The Ornstein–Uhlenbeck process dX = −θX·dt + σ·dB is pulled towards 0 and has stationary law N(0, σ²/(2θ)). Geometric Brownian motion dS = μS·dt + σS·dB has the explicit solution S₀·exp((μ − σ²/2)t + σBₜ), where the −σ²/2 is the Itô correction.

6. **Diffusions and partial differential equations are two descriptions of one object.** The generator L = b·∂/∂x + ½σ²·∂²/∂x² governs expectations: u(t, x) = E[f(Xₜ) ∣ X₀ = x] solves the Kolmogorov backward equation ∂u/∂t = Lu, while the density of Xₜ solves the forward (Fokker–Planck) equation. The Feynman–Kac formula (Mark Kac, 1949) adds a potential and represents the solution of a partial differential equation (PDE) as an average over paths. Fischer Black, Myron Scholes and Robert Merton (1973) priced options by exactly this correspondence.

7. **Girsanov's theorem changes the drift by changing the measure.** Under a new probability Q with density exp(∫θ dB − ½∫θ² dt) with respect to P, the process Bₜ − ∫₀ᵗ θₛ ds is a Brownian motion (Igor Girsanov, 1960). Drift can be removed by reweighting paths; volatility cannot, since quadratic variation is visible on almost every path, so diffusions with different σ have mutually singular laws. This is the mathematics of risk-neutral pricing.

## Key concepts

| Term | Meaning |
|---|---|
| Adapted integrand | A process whose value at time t depends only on the information up to t |
| Itô integral | ∫ H dB, the L² limit of left-endpoint sums |
| Itô isometry | E[(∫H dB)²] = E[∫H² dt] |
| Quadratic variation | The limit of ∑(ΔX)²; equal to t for Brownian motion |
| Itô's formula | The chain rule with the extra term ½σ²·f″·dt |
| Stochastic differential equation | dX = b(X)·dt + σ(X)·dB, meaning the corresponding integral equation |
| Generator | The second-order differential operator L describing a diffusion's infinitesimal behaviour |
| Girsanov's theorem | Changing the measure by an exponential martingale shifts the drift |

## How it fits

- **Below:** [Brownian motion](brownian-motion.md) and its quadratic variation, the [martingale](martingales.md) transform, [L² spaces](../../09-advanced-analysis/01-measure-and-integration/lp-spaces.md) for the isometry, [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md) for Itô's formula, and the Picard argument for [ordinary differential equations](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/existence-and-uniqueness.md).
- **Above:** [mathematical finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md) prices derivatives with Itô's formula and Girsanov; the Euler–Maruyama scheme in [numerical methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) simulates SDEs; diffusion-based [generative models](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/generative-models.md) run an SDE backwards in time; stochastic gradient descent is studied as an SDE in [deep learning](../../14-applied-and-computational-mathematics/06-data-and-learning/the-mathematics-of-deep-learning.md).
- **Siblings:** the generator of a diffusion plays the role that P − I plays for a [Markov chain](markov-chains.md) and the rate matrix Q for a [continuous-time chain](poisson-processes-and-continuous-time-markov-chains.md).

## Common misconceptions

- **"Stochastic calculus is ordinary calculus with noise added"**: the chain rule changes. Ignoring the ½σ² term misprices options and gives the wrong long-run growth rate μ − σ²/2 of geometric Brownian motion.
- **"Itô and Stratonovich give different physics"**: they are two conventions related by an explicit drift correction. Smooth approximations of noise converge to the Stratonovich solution (the Wong–Zakai theorem), so the modelling question is which one the approximations represent.
- **"dB/dt is a function"**: white noise exists only as a generalised function; the equation is shorthand for an integral equation.

## Go deeper

- Bernt Øksendal, *Stochastic Differential Equations* (6th edition, 2003): the standard first text, with applications.
- Ioannis Karatzas and Steven Shreve, *Brownian Motion and Stochastic Calculus* (2nd edition, 1991): the full theory for continuous martingales.
- Steven Shreve, *Stochastic Calculus for Finance II: Continuous-Time Models* (2004): the calculus as used in pricing.
