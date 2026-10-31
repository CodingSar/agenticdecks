# Calculus of Variations

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › Calculus of Variations
> **Children:** [The Euler–Lagrange Equation](the-euler-lagrange-equation.md) · [Noether's Theorem](noethers-theorem.md) · [Existence of Minimisers](existence-of-minimisers.md)

## What this area is about

The calculus of variations optimises over functions instead of numbers. A functional J[y] = ∫ L(x, y, y′) dx assigns a number to each curve or surface, and one asks which function makes it smallest, or at least stationary: the shortest path, the fastest slide, the soap film of least area, the motion of least action. Its classical problems, the brachistochrone of 1696 and Dido's isoperimetric problem, are among the oldest in analysis, and its principles organise all of classical and quantum physics.

Three questions unify the area, and each child answers one. What equation must an optimiser satisfy? What do the symmetries of the functional tell us about its solutions? Is there an optimiser at all? The first leads to differential equations, the second to conservation laws, the third to functional analysis.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The Euler–Lagrange Equation](the-euler-lagrange-equation.md) | The necessary condition: a stationary function solves a differential equation | Calculus of several variables, boundary value problems |
| [Noether's Theorem](noethers-theorem.md) | Symmetries of the functional give conserved quantities | Euler–Lagrange equation, Lie groups |
| [Existence of Minimisers](existence-of-minimisers.md) | The direct method: coercivity, weak compactness and lower semicontinuity | Euler–Lagrange equation, Sobolev spaces |

```
                 the Euler–Lagrange equation
                  (what a minimiser solves)
                   │                     │
                   ▼                     ▼
          Noether's theorem       existence of minimisers
       (symmetry → conservation)  (does a minimiser exist?)
                   │                     │
                   ▼                     ▼
          Hamiltonian systems     weak solutions, regularity
```

Read [the Euler–Lagrange equation](the-euler-lagrange-equation.md) first. Setting the first variation to zero turns minimisation into a boundary value problem, and Hamilton's principle shows that Newton's laws are of this form; the second variation then separates minima from saddles. [Noether's theorem](noethers-theorem.md) takes the equation as given and reads conservation laws off continuous symmetries: momentum from translations, energy from time shifts. [Existence of minimisers](existence-of-minimisers.md) goes back to the logical gap left by the first leaf. The equation describes a minimiser only if one exists, Weierstrass showed one need not, and the direct method fills the gap by compactness in Sobolev spaces. The two later leaves are independent of each other and can be read in either order.

## Connections to sibling areas

- **[Ordinary Differential Equations](../01-ordinary-differential-equations/README.md):** one-dimensional Euler–Lagrange equations are boundary value problems, and Sturm–Liouville eigenvalues are minima of Rayleigh quotients.
- **[Partial Differential Equations](../02-partial-differential-equations/README.md):** many equations are Euler–Lagrange equations: Laplace's of the Dirichlet energy, the minimal surface equation of area. Weak solutions and minimisers are found by the same Sobolev-space methods.
- **[Dynamical Systems](../04-dynamical-systems/README.md):** the Legendre transform turns Lagrangian mechanics into Hamiltonian systems, where Noether's conserved quantities decide integrability.

## Connections across layers

The area extends [extrema and Lagrange multipliers](../../06-real-analysis/03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md) from 06 to infinitely many variables, uses [Lie groups](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md) from 08 for symmetries, and draws weak compactness from [Banach](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md) and [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) in 09; geodesics in [Riemannian manifolds](../../08-geometry/02-differential-geometry/riemannian-manifolds.md) are its solutions too. Upward, [optimal control](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md), [convex optimisation](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md), [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) and [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) in 14 are all built on variational principles, and the Dirichlet principle controversy belongs to the [history of mathematics](../../15-mathematics-in-context/history-of-mathematics.md).

## Cross-cutting threads

- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): physical laws as conditions for stationary action.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): Noether's theorem turns continuous symmetries into conservation laws.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): the direct method finds minimisers by weak compactness.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Dirichlet's principle assumed existence, and its failure forced the modern theory.
- [Duality](../../CROSS-CUTTING.md#duality): the Legendre transform exchanges velocities and momenta, Lagrangian and Hamiltonian.
