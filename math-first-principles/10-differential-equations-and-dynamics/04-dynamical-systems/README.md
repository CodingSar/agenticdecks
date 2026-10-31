# Dynamical Systems

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › Dynamical Systems
> **Children:** [Iterated Maps](iterated-maps.md) · [Bifurcations](bifurcations.md) · [Chaos and Strange Attractors](chaos-and-strange-attractors.md) · [Ergodic Theory](ergodic-theory.md) · [Hamiltonian Systems and Integrability](hamiltonian-systems-and-integrability.md) · [Complex Dynamics](complex-dynamics.md)

## What this area is about

A dynamical system is a rule for how a state evolves: a map applied repeatedly, xₙ₊₁ = f(xₙ), or the flow of a differential equation. Dynamical systems theory gives up on formulas for individual solutions and asks about long-term behaviour. Where do orbits end up? How does that change with a parameter? When is the future predictable, and when only its statistics? Poincaré founded the subject in the 1880s and 1890s, studying the three-body problem, when he realised that the qualitative shape of all solutions mattered more than any one of them.

Two distinctions organise it. Time may be discrete (maps) or continuous (flows), and the two are linked, since a flow sampled on a cross-section gives a map. And systems may be dissipative, with volumes shrinking onto attractors, or conservative, with volume preserved as in frictionless mechanics. Chaos appears in both kinds, but it looks different in each.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Iterated Maps](iterated-maps.md) | Discrete time; the logistic map, period doubling and symbolic coding | Stability, contraction mapping |
| [Bifurcations](bifurcations.md) | How behaviour changes qualitatively with a parameter | Stability, implicit function theorem |
| [Chaos and Strange Attractors](chaos-and-strange-attractors.md) | Sensitive dependence, the Lorenz attractor and the horseshoe | Maps, bifurcations |
| [Ergodic Theory](ergodic-theory.md) | Measure-preserving systems: recurrence, time averages, mixing, entropy | Measure theory, maps |
| [Hamiltonian Systems and Integrability](hamiltonian-systems-and-integrability.md) | Conservative mechanics: symplectic structure, integrable tori, Kolmogorov–Arnold–Moser theory | Calculus of variations, ergodic theory |
| [Complex Dynamics](complex-dynamics.md) | Iterating z ↦ z² + c: Julia sets and the Mandelbrot set | Iterated maps, complex analysis |

```
     iterated maps ──► bifurcations ──► chaos and strange attractors
          │  │                               │      (dissipative)
          │  └──► complex dynamics           │
          │       (Julia and Mandelbrot)     │
          │                                  ▼
          └────────────────────────► ergodic theory
                                             │   (statistics)
                                             ▼
                      Hamiltonian systems and integrability
                                (conservative)
```

[Iterated maps](iterated-maps.md) come first, because one-dimensional maps already show fixed points, cycles, period doubling and chaos in their simplest form. [Bifurcations](bifurcations.md) classify how equilibria and cycles appear and disappear as parameters change, and cascades of them lead into [chaos](chaos-and-strange-attractors.md), where the horseshoe makes unpredictability exact and the Lorenz attractor shows it in a flow. [Ergodic theory](ergodic-theory.md) changes the question from individual orbits to their statistics, which remain predictable when orbits are not. [Hamiltonian systems](hamiltonian-systems-and-integrability.md) treat the conservative case: no attractors, an invariant volume, and the delicate coexistence of integrable tori and chaotic zones described by Kolmogorov–Arnold–Moser (KAM) theory. [Complex dynamics](complex-dynamics.md) branches off from iterated maps: letting z² + c act on the complex plane brings in the rigidity of holomorphic functions, so the Julia and Mandelbrot sets, fractals first seen on computer screens, can be described by theorems.

## Connections to sibling areas

- **[Ordinary Differential Equations](../01-ordinary-differential-equations/README.md):** existence and uniqueness make flows deterministic, and linearisation and Lyapunov functions are the local tools every leaf here uses.
- **[Partial Differential Equations](../02-partial-differential-equations/README.md):** evolution equations are dynamical systems on infinite-dimensional spaces; reaction–diffusion equations bifurcate into patterns, and the Korteweg–de Vries equation is integrable.
- **[Calculus of Variations](../03-calculus-of-variations/README.md):** Hamilton's principle and the Legendre transform produce Hamiltonian systems, and Noether's theorem supplies their conserved quantities.

## Connections across layers

From below, the area uses the [contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) and [implicit function theorem](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md) of 06, [manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) from 07, [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md) from 08, [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [conformal maps](../../09-advanced-analysis/02-complex-analysis/conformal-maps-and-the-riemann-mapping-theorem.md), [measure theory](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md) and [fractal dimension](../../09-advanced-analysis/01-measure-and-integration/hausdorff-dimension-and-fractals.md) from 09; ergodic theory also reproved Szemerédi's theorem of [additive combinatorics](../../03-combinatorics-and-graph-theory/04-extremal-combinatorics/additive-combinatorics.md) in 03. Upward, it supports [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md), whose basins are Julia sets, [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md) in 11, and [mathematical biology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md), [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md) and [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) in 14. Computer-assisted proofs in chaos are examples for [computers and proof](../../15-mathematics-in-context/computers-and-proof.md) in 15.

## Cross-cutting threads

- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): ergodic theorems equate time averages with space averages.
- [Invariants](../../CROSS-CUTTING.md#invariants): conserved quantities, invariant measures and entropy classify systems.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): hyperbolic fixed points behave like their derivatives, and bifurcations occur exactly where this fails.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): symmetries force pitchfork bifurcations and give Hamiltonian systems their integrals.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): shadowing lets computed orbits stand for true ones.
- [Infinity and size](../../CROSS-CUTTING.md#infinity-and-size): strange attractors and horseshoes are Cantor-like sets of fractional dimension.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): sensitive dependence limits prediction, and small divisors obstruct integrability.
