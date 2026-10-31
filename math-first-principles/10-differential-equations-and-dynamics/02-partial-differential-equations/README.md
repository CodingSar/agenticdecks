# Partial Differential Equations

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › Partial Differential Equations
> **Children:** [First-Order Equations and Characteristics](first-order-equations-and-characteristics.md) · [Laplace's Equation and Harmonic Functions](laplaces-equation-and-harmonic-functions.md) · [The Heat Equation](the-heat-equation.md) · [The Wave Equation](the-wave-equation.md) · [Weak Solutions and Sobolev Spaces](weak-solutions-and-sobolev-spaces.md) · [Nonlinear Partial Differential Equations](nonlinear-pdes.md)

## What this area is about

A partial differential equation (PDE) relates an unknown function of several variables, such as position and time, to its partial derivatives. Fields are described this way: temperature, electric potential, the displacement of a drum, the velocity of a fluid, the curvature of spacetime. There is no general theory, so the subject proceeds through model equations, each the simplest member of a large class, and through a functional-analytic framework that handles all of them at once.

For a second-order equation a·uₓₓ + 2b·uₓᵧ + c·uᵧᵧ + (lower order) = 0 the sign of b² − ac sorts the field into three types, with different physics and different methods: elliptic (b² < ac), parabolic (b² = ac) and hyperbolic (b² > ac).

| | Laplace Δu = 0 | Heat uₜ = Δu | Wave uₜₜ = c²Δu |
|---|---|---|---|
| Type | Elliptic | Parabolic | Hyperbolic |
| Describes | Equilibrium | Diffusion | Propagation |
| Speed of signals | No time | Infinite | Finite, c |
| Smoothness | Always smooth | Smooth for t > 0 | Singularities travel |
| Reversible in time | Not applicable | No | Yes |

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [First-Order Equations and Characteristics](first-order-equations-and-characteristics.md) | Transport along curves; shocks and the first weak solutions | Ordinary differential equations |
| [Laplace's Equation and Harmonic Functions](laplaces-equation-and-harmonic-functions.md) | The elliptic model: mean values, maximum principle, Green's functions | Vector calculus |
| [The Heat Equation](the-heat-equation.md) | The parabolic model: heat kernel, smoothing, irreversibility | Laplace, Fourier analysis |
| [The Wave Equation](the-wave-equation.md) | The hyperbolic model: finite speed, energy, Huygens' principle | Characteristics, Fourier analysis |
| [Weak Solutions and Sobolev Spaces](weak-solutions-and-sobolev-spaces.md) | The general framework: existence in Hilbert space, then regularity | Laplace, characteristics, distributions |
| [Nonlinear Partial Differential Equations](nonlinear-pdes.md) | Shocks, solitons, blow-up and the Navier–Stokes problem | All of the above |

```
   characteristics ─────────────► wave equation ──────┐
        │                                              │
        │       Laplace's equation ──► heat equation ──┤
        │              │                               ▼
        └──────────────┴──────► weak solutions ──► nonlinear equations
```

Start with [characteristics](first-order-equations-and-characteristics.md), where a partial differential equation reduces to ordinary ones and shocks first force a weaker notion of solution. The three model equations come next: [Laplace](laplaces-equation-and-harmonic-functions.md) for equilibrium, then the [heat](the-heat-equation.md) and [wave](the-wave-equation.md) equations, which add time in the two opposite ways. Comparing them is the point: the table above is the core intuition of the subject. [Weak solutions](weak-solutions-and-sobolev-spaces.md) then replace explicit formulas with a method that works for variable coefficients and general domains, and [nonlinear equations](nonlinear-pdes.md) combine every earlier tool with scaling and conservation laws.

## Connections to sibling areas

- **[Ordinary Differential Equations](../01-ordinary-differential-equations/README.md):** characteristics and separation of variables reduce partial differential equations to ordinary ones, and Sturm–Liouville eigenfunctions supply the series solutions.
- **[Calculus of Variations](../03-calculus-of-variations/README.md):** Laplace's equation is the Euler–Lagrange equation of the Dirichlet energy, and the direct method uses Sobolev spaces to prove existence.
- **[Dynamical Systems](../04-dynamical-systems/README.md):** an evolution equation is a dynamical system on a space of functions; the Korteweg–de Vries equation is an infinite-dimensional integrable Hamiltonian system.

## Connections across layers

The area rests on [vector calculus](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md) from 06 and on [the Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md), [distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md) and [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) from 09; harmonic functions in the plane are the real parts of [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md). Upward, the heat equation is the law of [Brownian motion](../../11-probability-and-statistics/03-stochastic-processes/brownian-motion.md) in 11, and in 14 these equations underlie [numerical methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [mathematical finance](../../14-applied-and-computational-mathematics/05-games-decisions-and-finance/mathematical-finance.md), [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) and [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md). The Navier–Stokes question is among the [open problems](../../15-mathematics-in-context/open-problems.md) of 15.

## Cross-cutting threads

- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): weak solutions are limits of approximate ones, and Galerkin methods compute them.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): Sobolev spaces are complete, and Rellich's compact embedding turns bounds into convergence.
- [Duality](../../CROSS-CUTTING.md#duality): weak derivatives and weak solutions are defined by pairing with test functions.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): the heat equation is the random walk, and harmonic functions are expected values of Brownian motion.
- [Local to global](../../CROSS-CUTTING.md#local-to-global): elliptic equations couple every point to the whole boundary, while hyperbolic ones propagate information locally.
