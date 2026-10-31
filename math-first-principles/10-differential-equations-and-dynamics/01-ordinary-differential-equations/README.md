# Ordinary Differential Equations

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › Ordinary Differential Equations
> **Children:** [Existence and Uniqueness](existence-and-uniqueness.md) · [Linear Systems and the Matrix Exponential](linear-systems-and-the-matrix-exponential.md) · [Stability and Phase Portraits](stability-and-phase-portraits.md) · [Boundary Value Problems and Sturm–Liouville Theory](boundary-value-problems-and-sturm-liouville-theory.md)

## What this area is about

An ordinary differential equation (ODE) prescribes how a state changes in time: y′ = f(t, y), with y a point of ℝⁿ. Newton's laws, chemical kinetics, population models and electrical circuits all take this form. Most such equations cannot be solved by formula, so the area asks three kinds of question instead. Is the future determined by the present? What can be computed exactly, and how does everything else resemble it? What does the flow look like as a whole, and which states are stable?

The unifying idea is that an equation of change defines a flow on state space, and that flow can be understood through its fixed points, its linear approximation and its spectrum. Initial value problems, which fix the state at one time, are about determinism and qualitative behaviour; boundary value problems, which impose conditions at two ends, are about eigenvalues, and lead into partial differential equations.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Existence and Uniqueness](existence-and-uniqueness.md) | Picard–Lindelöf and Peano: when the present determines the future | Contraction mapping, compactness |
| [Linear Systems and the Matrix Exponential](linear-systems-and-the-matrix-exponential.md) | The solvable case x′ = Ax, read off eigenvalues and Jordan blocks | Existence, linear algebra |
| [Stability and Phase Portraits](stability-and-phase-portraits.md) | Linearisation, Lyapunov functions and the global picture of nonlinear flows | Linear systems |
| [Boundary Value Problems and Sturm–Liouville Theory](boundary-value-problems-and-sturm-liouville-theory.md) | Two-point problems, eigenvalues and orthogonal expansions | Existence, spectral theorem |

```
              existence and uniqueness
               │                    │
               ▼                    ▼
        linear systems      boundary value problems ──► partial differential
               │            and Sturm–Liouville           equations (02)
               ▼
      stability and phase ──► dynamical systems (04)
           portraits
```

Read [existence and uniqueness](existence-and-uniqueness.md) first: turning the equation into an integral equation and applying the contraction mapping principle gives one solution for each initial state, the foundation of every later statement. [Linear systems](linear-systems-and-the-matrix-exponential.md) are solved completely by the matrix exponential, and their eigenvalues decide growth, decay and rotation. [Stability](stability-and-phase-portraits.md) uses that knowledge locally, since near a hyperbolic equilibrium a nonlinear flow looks like its linearisation, and adds Lyapunov functions and the Poincaré–Bendixson theorem for the global picture in the plane. [Boundary value problems](boundary-value-problems-and-sturm-liouville-theory.md) branch off: they ask for solutions meeting conditions at both ends, which exist only for special parameter values, and Sturm–Liouville theory turns these eigenvalue problems into a spectral theorem for differential operators.

## Connections to sibling areas

- **[Partial Differential Equations](../02-partial-differential-equations/README.md):** separation of variables reduces the heat, wave and Laplace equations to Sturm–Liouville problems, and characteristics reduce first-order partial differential equations to ordinary ones.
- **[Calculus of Variations](../03-calculus-of-variations/README.md):** the Euler–Lagrange equation of a one-dimensional variational problem is a boundary value problem, and Sturm–Liouville eigenvalues are minima of a Rayleigh quotient.
- **[Dynamical Systems](../04-dynamical-systems/README.md):** the qualitative theory of stability and phase portraits grows into bifurcation theory, chaos and Hamiltonian mechanics; existence and uniqueness is why chaos is deterministic.

## Connections across layers

From below, the area takes the [contraction mapping principle](../../06-real-analysis/04-metric-spaces/completeness-and-the-contraction-mapping-principle.md) and [compactness](../../06-real-analysis/04-metric-spaces/compactness-in-metric-spaces.md) from 06, [eigenvalues](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md) and the [spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) from 04, and [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) from 09. Upward, it feeds [numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md) and [mathematical biology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md) in 14, continuous-time [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md) and [stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md) in 11, and the eigenvalue problems of [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md).

## Cross-cutting threads

- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): completeness gives Picard–Lindelöf; compactness gives Peano's existence without uniqueness.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): near a hyperbolic equilibrium a flow behaves like its derivative.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): Jordan form classifies linear flows, and eigenfunction expansions decompose solutions.
- [Invariants](../../CROSS-CUTTING.md#invariants): Lyapunov functions and conserved energies constrain trajectories without solving.
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Picard iteration builds the solution it proves exists.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): solutions are limits of iterates and of polygonal approximations.
