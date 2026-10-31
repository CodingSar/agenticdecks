# The Wave Equation

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Partial Differential Equations](README.md)
> **Builds on:** [First-order equations and characteristics](first-order-equations-and-characteristics.md), [Boundary value problems and Sturm–Liouville theory](../01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md), [The Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md), [Vector calculus and the integral theorems](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md)
> **Enables:** [Nonlinear partial differential equations](nonlinear-pdes.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [Electromagnetism and charge](../../../cs-first-principles/00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md)

## Essence

The wave equation uₜₜ = c²Δu governs vibrating strings, sound, light and small ripples on water. It is the model hyperbolic partial differential equation (PDE), and it behaves as the opposite of the heat equation: signals travel at the finite speed c, energy is conserved, time can be reversed, and corners are carried along rather than smoothed. In one dimension it splits into two travelling waves. In three dimensions a sharp signal arrives sharply and leaves nothing behind (Huygens' principle), which is why sound carries speech; in two dimensions it does not, which is why a pond keeps rippling inside the ring.

## Core tenets

1. **In one dimension the equation factors into two transport equations.** Since uₜₜ − c²uₓₓ = (∂ₜ − c∂ₓ)(∂ₜ + c∂ₓ)u, the coordinates ξ = x − ct and η = x + ct turn it into ∂²u/∂ξ∂η = 0, whose solutions are F(x − ct) + G(x + ct): two profiles moving right and left at speed c. Fitting u(x, 0) = g and uₜ(x, 0) = h gives d'Alembert's formula (1747):

   ```
   u(x, t) = ½·[g(x + ct) + g(x − ct)] + (1/(2c))·∫ from x − ct to x + ct of h(s) ds.
   ```

   A kink in g is never smoothed: it travels along the characteristics x ± ct for ever.

2. **Signals travel at finite speed.** By d'Alembert's formula u(x, t) depends only on data in [x − ct, x + ct], its domain of dependence, and data near a point x₀ influence only the cone |x − x₀| ≤ ct. The same holds in every dimension, proved by an energy estimate on a shrinking cone: the energy inside the ball of radius R − ct about x₀ cannot increase, so zero data in the ball of radius R give zero solution inside the cone. This causality is what relativity demands, and Maxwell's equations imply wave equations whose c is the speed of light.

3. **Energy is conserved, so the evolution is unique and reversible.** Let E(t) = ½∫(uₜ² + c²|∇u|²) dx. Integrating by parts, E′(t) = ∫uₜ·(uₜₜ − c²Δu) dx = 0 for solutions vanishing on the boundary or at infinity. The difference of two solutions with the same data has zero energy, so it is constant, hence zero. Replacing t by −t gives another solution: there is no arrow of time, and regularity is neither gained nor lost.

4. **Bounded regions give normal modes.** For a string of length π fixed at both ends, separation of variables gives u = ∑ (aₙ·cos nct + bₙ·sin nct)·sin nx, the fundamental and its harmonics. On a drum the frequencies are c times the square roots of the Dirichlet eigenvalues of −Δ, so pitch is a spectral question. Mark Kac (1966) asked "Can one hear the shape of a drum?", and Carolyn Gordon, David Webb and Scott Wolpert (1992) answered no: two different planar regions have the same eigenvalues.

5. **Kirchhoff's formula and Huygens' principle.** In ℝ³, write M[f](x, r) for the average of f over the sphere of radius r about x. Then

   ```
   u(x, t) = ∂ₜ( t·M[g](x, ct) ) + t·M[h](x, ct).
   ```

   Only data on the sphere |y − x| = ct matter, not inside it: a flash at the origin is seen at distance r exactly at time r/c and then gone. This sharp form of Huygens' principle holds in every odd dimension n ≥ 3 and fails in even dimensions. Treating a planar solution as a spatial one independent of x₃ (the method of descent) turns the sphere average into an average over the whole disc, so a disturbance in the plane leaves a decaying tail behind its front.

6. **Every frequency travels at the same speed.** Plane waves e^(i(ξ·x − ωt)) solve the equation exactly when ω = c|ξ|, so all frequencies move together and a one-dimensional pulse keeps its shape. Equations where ω is not proportional to |ξ|, such as the Schrödinger equation with ω = |ξ|², are dispersive: wave packets spread out, which matters for the nonlinear theory.

## Key concepts

| Term | Meaning |
|---|---|
| Wave speed | The constant c in uₜₜ = c²Δu |
| Characteristic lines | The lines x ± ct along which signals and singularities travel |
| Domain of dependence | The ball of radius ct about x holding all initial data that determine u(x, t) |
| Light cone | The set ∣y − x∣ ≤ ct of points a disturbance at x can reach by time t |
| Energy | E = ½∫(uₜ² + c²∣∇u∣²), constant in time |
| Normal mode | A solution oscillating at one frequency with a fixed spatial shape |
| Huygens' principle | In its sharp form: a point disturbance is felt only on the sphere ∣y − x∣ = ct |
| Dispersion | Dependence of wave speed on frequency, absent for this equation |

## How it fits

- **Below:** d'Alembert's formula is the method of [characteristics](first-order-equations-and-characteristics.md) applied twice; string modes are [Sturm–Liouville](../01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md) eigenfunctions; the [Fourier transform](../../09-advanced-analysis/04-harmonic-analysis/the-fourier-transform.md) solves every case; Kirchhoff's formula rests on the [divergence theorem](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md).
- **Above:** Maxwell's equations carry [electromagnetic waves](../../../cs-first-principles/00-engineering-foundations/01-physics-of-computation/electromagnetism-and-charge.md); [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) is a nonlinear wave system for the metric; [numerical schemes](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) obey the Courant–Friedrichs–Lewy condition (1928): the time step must be at most of order h/c for grid spacing h.
- **Siblings:** the [heat equation](the-heat-equation.md) smooths, spreads instantly and forgets; [nonlinear PDEs](nonlinear-pdes.md) add self-interaction, giving shocks and solitons; [weak solutions](weak-solutions-and-sobolev-spaces.md) give meaning to waves with corners.

## Common misconceptions

- **"Waves in any dimension pass and leave no trace."**: only in odd dimensions from three up; in the plane a disturbance lingers inside its front.
- **"Rough data become smooth over time, as for heat."**: a corner stays a corner, transported along characteristics for ever.
- **"The frequencies of a drum determine its shape."**: different drums can share a spectrum (tenet 4), although the spectrum does determine the area.

## Go deeper

- Lawrence C. Evans, *Partial Differential Equations* (2nd edition, 2010): d'Alembert, Kirchhoff, descent and energy methods with full proofs.
- Fritz John, *Partial Differential Equations* (4th edition, 1982): a classic treatment of hyperbolic equations and spherical means.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics*, Volume II (1962): the classical account of hyperbolic equations and Huygens' principle.
