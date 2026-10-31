# Nonlinear Partial Differential Equations

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Partial Differential Equations](README.md)
> **Builds on:** [First-order equations and characteristics](first-order-equations-and-characteristics.md), [The heat equation](the-heat-equation.md), [The wave equation](the-wave-equation.md), [Weak solutions and Sobolev spaces](weak-solutions-and-sobolev-spaces.md), [Existence and uniqueness](../01-ordinary-differential-equations/existence-and-uniqueness.md)
> **Enables:** [Hamiltonian systems and integrability](../04-dynamical-systems/hamiltonian-systems-and-integrability.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md), [Mathematical biology and epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [Open problems](../../15-mathematics-in-context/open-problems.md)

## Essence

Nonlinear partial differential equations (PDEs) describe fluids, gravity, chemical reactions and biological patterns, and there is no general theory of them. Nonlinearity can do three things a linear equation cannot: steepen a wave into a shock, balance dispersion to form a soliton, and feed on itself until the solution blows up in finite time. Each equation is studied by the same tools: local existence by a contraction, scaling to see which quantities can control which, and conservation laws to extend solutions in time. The flagship question, whether smooth fluid flows in three dimensions stay smooth, is a Millennium Prize problem, open as of 2026.

## Core tenets

1. **Local existence comes from the linear part and a contraction.** Write uₜ = Lu + N(u), with L linear (such as Δ) and N nonlinear, in Duhamel's integral form u(t) = e^(tL)g + ∫ from 0 to t of e^((t − s)L)·N(u(s)) ds, and apply the contraction mapping principle in a space such as H^s with s > n/2, where products of functions are controlled. This gives a unique solution for a time depending on the size of g. As for ordinary differential equations, the solution then continues until its norm becomes infinite, so global existence needs an a priori bound, usually from a conserved energy.

2. **Shocks: nonlinearity steepens.** The inviscid Burgers equation breaks in finite time. Adding viscosity, uₜ + u·uₓ = ε·uₓₓ, the Hopf–Cole substitution u = −2ε·(log φ)ₓ turns it into the heat equation φₜ = ε·φₓₓ (Hopf, 1950; Cole, 1951), so the viscous equation is solved exactly, and as ε → 0 the solutions converge to the entropy solution with its shocks.

3. **Solitons: nonlinearity balances dispersion.** In the Korteweg–de Vries (KdV) equation uₜ + 6u·uₓ + uₓₓₓ = 0 for shallow water waves, the third derivative spreads waves out and the product term steepens them. They balance in solitary waves

   ```
   u(x, t) = (c/2)·sech²( (√c/2)·(x − ct) ),    c > 0,
   ```

   so taller waves travel faster. Zabusky and Kruskal (1965) found numerically that two such waves pass through each other intact, and named them solitons. Gardner, Greene, Kruskal and Miura (1967) solved the equation exactly by inverse scattering, and Lax (1968) explained why: KdV is equivalent to Lₜ = BL − LB for a Schrödinger operator L, whose eigenvalues are therefore conserved. It is an integrable system with infinitely many conservation laws.

4. **Blow-up: nonlinearity can win in finite time.** The ordinary differential equation y′ = yᵖ with p > 1 blows up; adding diffusion, uₜ = Δu + uᵖ on ℝⁿ, the Laplacian spreads mass away. Fujita (1966) found the balance point: for 1 < p < 1 + 2/n every non-negative, non-zero solution blows up in finite time, while for p > 1 + 2/n small data give global solutions. In low dimensions diffusion is too weak to win.

5. **Scaling decides what conservation laws can control.** The incompressible Navier–Stokes equations, for velocity u, pressure p and viscosity ν,

   ```
   uₜ + (u·∇)u = νΔu − ∇p,      ∇·u = 0,
   ```

   are unchanged by u(x, t) ↦ λ·u(λx, λ²t). Energy ∫|u|² never increases, but under this scaling it changes by the factor λ^(2−n). In two dimensions it is scale-invariant, and smooth solutions are known to exist for all time. In three dimensions it shrinks at small scales (λ large), so a bound on energy cannot stop the flow concentrating: the equation is supercritical.

6. **The Navier–Stokes problem is open as of 2026.** The Clay Millennium problem, stated by Charles Fefferman (2000), asks whether for smooth, divergence-free, rapidly decaying initial data on ℝ³ a smooth solution with bounded energy exists for all time, or whether a counterexample exists. Leray (1934) proved that global weak solutions of finite energy exist, but not that they are smooth or unique. Caffarelli, Kohn and Nirenberg (1982) showed that the possible singular set is small, of one-dimensional parabolic Hausdorff measure zero; Escauriaza, Seregin and Šverák (2003) showed that solutions bounded in L³ never blow up. Tao (2016) built an averaged equation with the same energy identity that does blow up, so energy arguments alone cannot settle it, and Buckmaster and Vicol (2019) proved that very weak solutions, rougher than Leray's, are not unique.

## Key concepts

| Term | Meaning |
|---|---|
| Duhamel formulation | The equation rewritten as an integral equation built from the linear propagator |
| Blow-up | A norm of the solution becoming infinite in finite time |
| Soliton | A solitary wave that keeps its shape and survives collisions with others |
| Integrable equation | One with infinitely many conservation laws, solvable by inverse scattering |
| Critical exponent | The power at which nonlinear growth and linear smoothing balance under scaling |
| Supercritical | Conserved quantities weaken at small scales and cannot prevent concentration |
| Leray weak solution | A finite-energy weak solution of the Navier–Stokes equations obeying an energy inequality |

## How it fits

- **Below:** [existence and uniqueness](../01-ordinary-differential-equations/existence-and-uniqueness.md) supplies the template of contraction and blow-up alternative; the [heat](the-heat-equation.md) and [wave](the-wave-equation.md) equations supply propagators, [Sobolev spaces](weak-solutions-and-sobolev-spaces.md) the function spaces, and [characteristics](first-order-equations-and-characteristics.md) the shocks.
- **Above:** Einstein's equations of [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) are a nonlinear wave system; reaction–diffusion equations make Turing's patterns (1952) in [mathematical biology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md); turbulence strains [numerical methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md); Navier–Stokes heads many lists of [open problems](../../15-mathematics-in-context/open-problems.md).
- **Siblings:** KdV is an infinite-dimensional [Hamiltonian system](../04-dynamical-systems/hamiltonian-systems-and-integrability.md); the [Lorenz system](../04-dynamical-systems/chaos-and-strange-attractors.md) is a three-mode truncation of the equations of convection.

## Common misconceptions

- **"Weak solutions settle the Navier–Stokes problem."**: Leray's have existed since 1934; whether they are smooth and unique is exactly what is open.
- **"Blow-up means the model is wrong."**: sometimes it is real physics, as in shocks, the self-focusing of lasers and gravitational collapse; sometimes it signals missing terms.
- **"Nonlinear means chaotic and unsolvable."**: integrable equations such as KdV are solved exactly, and many nonlinear equations have complete, stable theories.

## Go deeper

- Lawrence C. Evans, *Partial Differential Equations* (2nd edition, 2010): the nonlinear chapters, on conservation laws, reaction–diffusion and calculus of variations.
- Terence Tao, *Nonlinear Dispersive Equations: Local and Global Analysis* (2006): scaling, criticality and well-posedness for wave and Schrödinger equations.
- Charles L. Fefferman, "Existence and Smoothness of the Navier–Stokes Equation" (2000): the official statement of the Millennium Prize problem.
- P. G. Drazin and R. S. Johnson, *Solitons: An Introduction* (1989): KdV, inverse scattering and Lax pairs at an accessible level.
