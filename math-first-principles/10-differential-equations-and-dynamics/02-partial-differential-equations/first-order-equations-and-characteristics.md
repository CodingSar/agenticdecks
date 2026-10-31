# First-Order Equations and Characteristics

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Partial Differential Equations](README.md)
> **Builds on:** [Existence and uniqueness](../01-ordinary-differential-equations/existence-and-uniqueness.md), [The derivative as a linear map](../../06-real-analysis/04-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Inverse and implicit function theorems](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), [Distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md)
> **Enables:** [The wave equation](the-wave-equation.md), [Weak solutions and Sobolev spaces](weak-solutions-and-sobolev-spaces.md), [Nonlinear partial differential equations](nonlinear-pdes.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [Hamiltonian systems and integrability](../04-dynamical-systems/hamiltonian-systems-and-integrability.md)

## Essence

A first-order partial differential equation (PDE) relates a function u of several variables to its first partial derivatives. The model is the transport equation uₜ + c·uₓ = 0, which says that the profile of u is carried along at speed c. The method of characteristics finds curves along which the PDE reduces to an ordinary differential equation (ODE), so that information travels along them. For nonlinear equations the characteristics can cross, and the smooth solution then ends in finite time: a shock forms. Continuing past it forces the idea of a weak solution, and a physical rule, the entropy condition, to pick the right one.

## Core tenets

1. **Characteristics reduce a first-order PDE to ODEs.** Along a curve with x′(t) = c the chain rule gives (d/dt)u(x(t), t) = uₜ + c·uₓ = 0, so u is constant on the lines x − ct = constant, and the solution with u(x, 0) = g(x) is u = g(x − ct). Variable speeds work the same way: for uₜ + x·uₓ = 0 the characteristics solve x′ = x, so x = x₀·eᵗ and u(x, t) = g(x·e^(−t)). In general a·∂u/∂x + b·∂u/∂y = c, with a, b, c depending on (x, y, u), becomes the ODE system x′ = a, y′ = b, u′ = c.

2. **Data must be given on a non-characteristic curve.** The ODE solutions sweep out a surface from the curve carrying the data, and the inverse function theorem makes that surface the graph of a function near the curve provided the characteristics cross it transversally. Data on a characteristic fail twice: for uₜ + uₓ = 0, values given on the line x = t must already be constant (or no solution exists) and then say nothing about the rest of the plane (so infinitely many exist).

3. **Nonlinear speeds make characteristics cross.** In the inviscid Burgers equation uₜ + u·uₓ = 0 the speed is u itself, so the characteristic from x₀ is the line x = x₀ + g(x₀)·t carrying the value g(x₀). Fast fluid behind slow fluid catches up: along it uₓ = g′(x₀)/(1 + g′(x₀)·t), which becomes infinite at the breaking time t* = −1/min g′ whenever g′ is somewhere negative. For g = 1 on x < 0, 1 − x on [0, 1] and 0 on x > 1, every characteristic from [0, 1] reaches x = 1 at t = 1. No smooth solution exists beyond t*, however smooth g is.

4. **Weak solutions and the Rankine–Hugoniot condition.** Writing Burgers' equation in conservation form uₜ + (u²/2)ₓ = 0 and integrating against smooth test functions defines solutions that may jump. Conservation across a jump moving at speed s forces s = [f(u)]/[u], the jump in flux over the jump in u; for Burgers, s = (u₋ + u₊)/2 with u₋ behind and u₊ ahead. In the example the shock leaves (1, 1) at speed 1/2. The form matters: the same smooth equation written as (u²/2)ₜ + (u³/3)ₓ = 0 gives speed 2/3 for that jump, so the physics must say which quantity is conserved.

5. **Weak solutions are not unique; the entropy condition picks the physical one.** For g = 0 on x < 0 and 1 on x > 0, the rarefaction fan u = x/t on 0 ≤ x ≤ t and a jump from 0 to 1 moving at speed 1/2 are both weak solutions. The jump is unphysical, since characteristics leave it. The Lax entropy condition f′(u₋) > s > f′(u₊) demands that characteristics run into a shock; it is what the limit ε → 0 of uₜ + u·uₓ = ε·uₓₓ produces. For scalar conservation laws with bounded data, entropy solutions exist and are unique (Kružkov, 1970); for systems, Glimm (1965) proved existence in one space dimension for data of small total variation, and large data in several dimensions remain largely open as of 2026.

6. **Fully nonlinear equations carry the gradient along.** For F(x, u, ∇u) = 0 the characteristics carry both u and p = ∇u, and for a Hamilton–Jacobi equation uₜ + H(x, ∇u) = 0 they are exactly Hamilton's equations x′ = ∂H/∂p, p′ = −∂H/∂x of mechanics. The eikonal equation |∇u| = 1 gives the distance to a set, with light rays as characteristics; where rays cross the gradient jumps, as the distance to two points has a kink along their bisector. Viscosity solutions (Crandall and Lions, 1983) select the right non-smooth solution, as the entropy condition does for shocks.

## Key concepts

| Term | Meaning |
|---|---|
| Characteristic | A curve along which the PDE reduces to an ODE and information travels |
| Breaking time | The first time characteristics cross, ending the smooth solution |
| Conservation law | uₜ + f(u)ₓ = 0: the change of ∫u over an interval equals flux in minus flux out |
| Weak solution | A function satisfying the equation integrated against every smooth compactly supported test function |
| Shock | A jump discontinuity moving at the Rankine–Hugoniot speed |
| Rarefaction fan | A continuous solution spreading from a point, u = x/t for Burgers |
| Entropy condition | The admissibility rule that characteristics enter a shock, never leave it |
| Viscosity solution | The weak solution of a Hamilton–Jacobi equation selected by vanishing viscosity |

## How it fits

- **Below:** each characteristic is an [ODE solution](../01-ordinary-differential-equations/existence-and-uniqueness.md), the [inverse function theorem](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md) assembles them into a function, and weak solutions use the test-function idea that [distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md) make general.
- **Above:** upwind and shock-capturing schemes in [numerical methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) follow the characteristics; the Hamilton–Jacobi equation links to [Hamiltonian systems](../04-dynamical-systems/hamiltonian-systems-and-integrability.md) and is the equation for the value function in [control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md).
- **Siblings:** the [wave equation](the-wave-equation.md) factors into two transport equations; [weak solutions and Sobolev spaces](weak-solutions-and-sobolev-spaces.md) generalise the weak formulation; [nonlinear PDEs](nonlinear-pdes.md) treat shocks as one of three ways smooth solutions fail.

## Common misconceptions

- **"Smooth initial data give smooth solutions."**: Burgers' equation breaks at time −1/min g′ for smooth g; nonlinearity, not roughness, creates the shock. A traffic queue forming behind slow cars is the same effect.
- **"Any function satisfying the integrated equation is the solution."**: weak solutions can be non-unique, and the entropy condition, which encodes vanishing viscosity or the second law of thermodynamics, chooses the one nature selects.
- **"Equivalent equations have the same shocks."**: equations equivalent for smooth solutions can disagree about shock speeds (1/2 or 2/3 in tenet 4).

## Go deeper

- Lawrence C. Evans, *Partial Differential Equations* (2nd edition, 2010): characteristics, conservation laws and Hamilton–Jacobi equations with full proofs.
- Peter D. Lax, *Hyperbolic Systems of Conservation Laws and the Mathematical Theory of Shock Waves* (1973): the short classic on shocks and entropy.
- Gerald B. Whitham, *Linear and Nonlinear Waves* (1974): traffic, flood waves and shocks from the applied side.
