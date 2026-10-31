# Mathematical Modelling

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › Mathematical Modelling
> **Children:** [Modelling and Dimensional Analysis](modelling-and-dimensional-analysis.md) · [Control Theory](control-theory.md) · [Mathematical Biology and Epidemics](mathematical-biology-and-epidemics.md) · [The Mathematics of Quantum Mechanics](the-mathematics-of-quantum-mechanics.md) · [The Geometry of General Relativity](the-geometry-of-general-relativity.md)

## What this area is about

A model maps a piece of the world to a mathematical object whose consequences can be computed and compared with measurement. This area asks how a physical, biological or engineered system is turned into equations, and what can be trusted about the answer. The unifying idea is that the structure of the phenomenon chooses the mathematics: units and scales fix the form of a law, feedback fixes the stability question, conservation laws fix the invariants, and symmetry fixes the dynamics.

Two kinds of model meet here. In modelling, control and biology the modeller chooses the equations, so every model must be scaled, simplified and then validated against data it was not fitted to. In quantum mechanics and general relativity a few principles force the mathematics, and within their domains no experiment has yet contradicted them. There the mathematics is the theory, and the hard questions concern interpretation and the regime where each theory stops.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Modelling and dimensional analysis](modelling-and-dimensional-analysis.md) | The method: the modelling cycle, units and scaling, the Buckingham π theorem, validation and limits | Nothing in this area |
| [Control theory](control-theory.md) | Models that act: feedback, stability, controllability, optimal control and filtering | Modelling |
| [Mathematical biology and epidemics](mathematical-biology-and-epidemics.md) | Nonlinear models of populations, epidemics and patterns, and the thresholds that govern them | Modelling |
| [The mathematics of quantum mechanics](the-mathematics-of-quantum-mechanics.md) | Hilbert spaces and self-adjoint operators as the language of the microscopic world | Functional analysis in layer 09 |
| [The geometry of general relativity](the-geometry-of-general-relativity.md) | Lorentzian geometry as the theory of gravity | Differential geometry in layer 08 |

Read modelling first. Control theory and mathematical biology then use the same toolkit for opposite purposes. Both linearise about an equilibrium and read stability from eigenvalues. Control designs the feedback that makes an equilibrium stable; biology infers the feedback that nature has built, and finds thresholds such as the basic reproduction number R₀, which is exactly the condition that the linearised infection grows.

The two physics leaves are independent of the first three and of each other. One is functional analysis at work, the other differential geometry. They share one theme: symmetry determines dynamics. Stone's theorem turns a one-parameter group of unitary symmetries into a Hamiltonian, and diffeomorphism invariance together with the Bianchi identity fixes the form of Einstein's equations.

```
          modelling and dimensional analysis
          (units, scales, validation)
              /                      \
     control theory            mathematical biology
     (design the feedback)     (infer the feedback, thresholds)

  quantum mechanics                 general relativity
  (operators on Hilbert space)      (curvature of spacetime)
         \______ symmetry fixes the dynamics ______/
```

## Connections to sibling areas

- **[Numerical analysis](../01-numerical-analysis/README.md):** few models have closed-form solutions. Numerical methods integrate them, conditioning says which outputs mean anything, and Monte Carlo propagates uncertainty in the parameters.
- **[Optimisation](../02-optimisation/README.md):** fitting a model to data is an optimisation problem, and optimal control is optimisation over whole trajectories.
- **[Information, codes and cryptography](../03-information-codes-and-cryptography/README.md):** the Kalman filter extracts a state from noisy signals, and the quantum mechanics behind quantum computing is what makes Shor's algorithm a threat to public-key cryptography.
- **[Games, decisions and finance](../05-games-decisions-and-finance/README.md):** finance models prices by stochastic differential equations, and evolutionary game theory is population dynamics with strategies as species.
- **[Data and learning](../06-data-and-learning/README.md):** the other end of the spectrum, where models are fitted from data with few structural assumptions, and learning theory says when such fits generalise.

## Connections across layers

From below, the area draws on the [ordinary differential equations](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/README.md) and [dynamical systems](../../10-differential-equations-and-dynamics/04-dynamical-systems/README.md) of layer 10 for stability, bifurcation and chaos; on its [partial differential equations](../../10-differential-equations-and-dynamics/02-partial-differential-equations/README.md) for diffusion and the field equations; on [linear algebra](../../04-linear-algebra/README.md) for rank and eigenvalues; on [functional analysis](../../09-advanced-analysis/03-functional-analysis/README.md) for Hilbert spaces; on [differential geometry](../../08-geometry/02-differential-geometry/README.md) and [Lie theory](../../08-geometry/04-lie-theory/README.md) for curvature and spin; and on [stochastic processes](../../11-probability-and-statistics/03-stochastic-processes/README.md) for noise and chance extinction.

Upward, the [philosophy of mathematics](../../15-mathematics-in-context/philosophy-of-mathematics.md) asks why such models work at all, and [mathematics and society](../../15-mathematics-in-context/mathematics-and-society.md) asks how they should inform public decisions. The engineering view of feedback is the [feedback and control](../../../cs-first-principles/00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) leaf of the computing tree, and the clinical view of epidemics is [infectious disease dynamics](../../../medicine-first-principles/10-epidemiology-and-evidence/01-epidemiology/infectious-disease-dynamics.md) in the medicine tree.

## Cross-cutting threads

- [Linearisation](../../CROSS-CUTTING.md#linearisation): stability, feedback design and the epidemic threshold are all read from the Jacobian at an equilibrium.
- [Approximation and limits](../../CROSS-CUTTING.md#approximation-and-limits): scaling exposes small parameters, and Newtonian gravity is the weak-field, slow-motion limit of general relativity.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): invariance under change of units gives the π theorem; unitary groups give Hamiltonians and spin.
- [Invariants](../../CROSS-CUTTING.md#invariants): dimensionless groups and the conserved quantities of predator–prey and epidemic models.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): optimal control minimises a quadratic cost, and free-falling clocks maximise proper time.
- [Randomness and averaging](../../CROSS-CUTTING.md#randomness-and-averaging): the Kalman filter, chance extinction of an epidemic and the Born rule.
