# 10 Differential Equations and Dynamics

> **Layer:** 10 Differential Equations and Dynamics
> **Children:** [Ordinary Differential Equations](01-ordinary-differential-equations/README.md) · [Partial Differential Equations](02-partial-differential-equations/README.md) · [Calculus of Variations](03-calculus-of-variations/README.md) · [Dynamical Systems](04-dynamical-systems/README.md)

## What this area is about

This layer asks how laws of change determine the future. Since Newton, the laws of science have mostly been written as differential equations: a rule giving the rate of change of a state in terms of the state itself. Knowing the law is only the start. One must show it has solutions and that they are unique, understand them when no formula exists, and describe what happens over long times.

Four areas share the work. Ordinary differential equations evolve a finite-dimensional state in time and supply existence, uniqueness, linearisation and stability. Partial differential equations evolve fields, functions of space and time, through three model types: elliptic for equilibrium, parabolic for diffusion and hyperbolic for waves. The calculus of variations finds the equations of physics as conditions for an integral to be stationary, and links symmetries to conservation laws. Dynamical systems study long-term behaviour qualitatively: bifurcations, chaos, ergodic statistics and the conservative world of Hamiltonian mechanics.

The common thread is a change of viewpoint, from solving equations to understanding solution spaces. A solution is a fixed point of an integral operator, a minimiser of an energy, an element of a Sobolev space, or an orbit of a flow, and each viewpoint brings the analysis of the lower layers to bear. The layer's contribution to the stack is this theory of evolution: when a law of change determines a future, what that future looks like, and how far it can be predicted.

## Why this layer sits here

It needs the limit, the derivative, the integral and the [contraction mapping principle](../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) from [real analysis](../06-real-analysis/README.md); eigenvalues and the Jordan form from [linear algebra](../04-linear-algebra/README.md) to solve linear systems; manifolds from [topology](../07-topology/README.md) and differential forms and Lie groups from [geometry](../08-geometry/README.md) for phase spaces and symmetries; and, from [advanced analysis](../09-advanced-analysis/README.md), measure theory, Lᵖ and Hilbert spaces, Fourier analysis and distributions, without which modern existence theory for partial differential equations cannot be stated.

Layers above depend on it. [Probability](../11-probability-and-statistics/README.md) links Brownian motion to the heat equation and Markov chains to ergodic theory, and stochastic differential equations, treated there, extend the ordinary ones of this layer. [Applied and computational mathematics](../14-applied-and-computational-mathematics/README.md) solves these equations numerically, controls them, and uses them to model quantum mechanics, relativity, populations and markets; numerical methods and control theory live in 14, not here.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Ordinary Differential Equations](01-ordinary-differential-equations/README.md) | Existence, linear systems, stability, boundary value problems | 06, 04 |
| [Partial Differential Equations](02-partial-differential-equations/README.md) | Characteristics, the three model equations, weak solutions, nonlinear equations | Ordinary differential equations, 09 |
| [Calculus of Variations](03-calculus-of-variations/README.md) | Euler–Lagrange equations, Noether's theorem, existence of minimisers | Ordinary and partial differential equations, 08, 09 |
| [Dynamical Systems](04-dynamical-systems/README.md) | Maps, bifurcations, chaos, ergodic theory, Hamiltonian systems | Ordinary differential equations, calculus of variations, 09 |

```
                ordinary differential equations
              (existence, linearisation, eigenvalues)
               │               │                │
               ▼               ▼                ▼
      partial differential   calculus of    dynamical systems
          equations    ◄──► variations ───► (chaos, ergodic theory,
      (fields, Sobolev)     (energy,          Hamiltonian systems)
                             symmetry)
```

Start with [ordinary differential equations](01-ordinary-differential-equations/README.md): every later area uses existence and uniqueness, linearisation at equilibria and eigenvalue expansions. [Partial differential equations](02-partial-differential-equations/README.md) extend these to fields, where separation of variables reduces to Sturm–Liouville problems and weak solutions replace formulas. The [calculus of variations](03-calculus-of-variations/README.md) sits between the two: its Euler–Lagrange equations are ordinary or partial differential equations, and the direct method shares its Sobolev spaces with weak solutions. [Dynamical systems](04-dynamical-systems/README.md) take the qualitative path from stability theory to chaos, and receive Hamiltonian mechanics from the variational principle.

## Connections to neighbouring layers

- **[04 Linear Algebra](../04-linear-algebra/README.md):** the matrix exponential, Jordan form and the spectral theorem solve linear systems and Sturm–Liouville problems.
- **[06 Real Analysis](../06-real-analysis/README.md):** the contraction mapping principle proves existence and uniqueness; the implicit function theorem governs bifurcations; vector calculus gives the integral identities of partial differential equations.
- **[07 Topology](../07-topology/README.md):** phase spaces are manifolds; Ricci flow, a geometric heat equation, proved the Poincaré conjecture.
- **[08 Geometry](../08-geometry/README.md):** symplectic forms structure Hamiltonian mechanics, Lie groups carry Noether's symmetries, and geodesics solve variational problems.
- **[09 Advanced Analysis](../09-advanced-analysis/README.md):** Lᵖ and Hilbert spaces, distributions and the Fourier transform are the language of partial differential equations; measure theory underlies ergodic theory and Hausdorff dimension measures strange attractors.
- **[11 Probability and Statistics](../11-probability-and-statistics/README.md):** the heat equation is the law of Brownian motion, the law of large numbers is an ergodic theorem, and stochastic differential equations add noise to the flows of this layer.
- **[14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md):** numerical methods, control theory, mathematical biology, quantum mechanics and general relativity all take their equations from here.
- **[15 Mathematics in Context](../15-mathematics-in-context/README.md):** computer-assisted proofs of chaos and the open Navier–Stokes problem are part of its story.

## Cross-cutting threads

- [Linearisation](../CROSS-CUTTING.md#linearisation): stability, bifurcation and perturbation theory begin by replacing a system with its derivative.
- [Completeness and compactness](../CROSS-CUTTING.md#completeness-and-compactness): solutions are fixed points in complete spaces or limits extracted by compactness.
- [Extremal principles and optimisation](../CROSS-CUTTING.md#extremal-principles-and-optimisation): the equations of physics are conditions for stationary action.
- [Symmetry](../CROSS-CUTTING.md#symmetry): Noether's theorem turns symmetries into conservation laws.
- [Approximation and limits](../CROSS-CUTTING.md#approximation-and-limits): weak solutions, Galerkin approximation and shadowing all reach solutions as limits.
- [Randomness and averaging](../CROSS-CUTTING.md#randomness-and-averaging): ergodic theory and the heat equation join deterministic dynamics to probability.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): sensitive dependence limits prediction, and small divisors obstruct integrability.
