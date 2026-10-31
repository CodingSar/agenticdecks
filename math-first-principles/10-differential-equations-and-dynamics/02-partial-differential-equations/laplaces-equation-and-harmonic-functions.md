# Laplace's Equation and Harmonic Functions

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Partial Differential Equations](README.md)
> **Builds on:** [Vector calculus and the integral theorems](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md), [Holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md), [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md), [Distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md)
> **Enables:** [The heat equation](the-heat-equation.md), [Weak solutions and Sobolev spaces](weak-solutions-and-sobolev-spaces.md), [Existence of minimisers](../03-calculus-of-variations/existence-of-minimisers.md), [Brownian motion](../../11-probability-and-statistics/03-stochastic-processes/brownian-motion.md)

## Essence

Laplace's equation Δu = 0, where the Laplacian Δu = ∂²u/∂x₁² + … + ∂²u/∂xₙ², describes every steady state of diffusion: equilibrium temperature, electrostatic potential away from charges, the velocity potential of an ideal fluid. Its solutions, harmonic functions, are characterised by one property: the value at each point equals the average over every sphere centred there. From that mean value property follow the maximum principle, uniqueness for the Dirichlet problem (prescribed boundary values), smoothness and rigidity. Laplace's equation is the model elliptic partial differential equation (PDE): no time, no direction of propagation, and every point influenced by the whole boundary.

## Core tenets

1. **The Laplacian measures the gap between a value and its local average.** Taylor expansion and symmetry give, for u of class C²,

   ```
   (average of u over the sphere of radius r about x) = u(x) + (r²/2n)·Δu(x) + o(r²).
   ```

   So Δu > 0 means u lies below the average of its surroundings, as at the bottom of a bowl. Harmonic means exactly balanced, the state diffusion reaches when it stops changing.

2. **The mean value property holds exactly and characterises harmonic functions.** If Δu = 0 on a region containing the closed ball B(x, r), then u(x) equals the average of u over the sphere and over the ball. Proof idea: if φ(r) is the sphere average, the divergence theorem gives φ′(r) = (r/n)·(average of Δu over the ball) = 0, and φ(r) → u(x) as r → 0. Conversely, a continuous function with the mean value property on all small spheres is harmonic.

3. **Maximum principle: on a bounded connected region, the extremes lie on the boundary.** If u had an interior maximum M, every small sphere about that point would average to M with no value above M, so u = M on a ball; connectedness spreads this, and u is constant. Hence the Dirichlet problem Δu = 0 in Ω, u = g on ∂Ω has at most one solution, and the maximum of |u₁ − u₂| over Ω is at most the maximum of |g₁ − g₂| over ∂Ω, so solutions depend continuously on their data. On unbounded regions this fails (misconception 1).

4. **Harmonic functions are smooth and rigid.** Averaging is smoothing: writing u as its own average against a smooth bump shows u is infinitely differentiable, indeed real analytic, and the divergence theorem gives |∇u(x)| ≤ (n/r)·max of |u| over B(x, r). Letting r → ∞ gives Liouville's theorem: a bounded harmonic function on ℝⁿ is constant. Weyl's lemma says even a weak, integrated solution is smooth, the first case of elliptic regularity. In the plane, harmonic functions on simply connected regions are exactly the real parts of holomorphic functions.

5. **The fundamental solution inverts the Laplacian.** Φ(x) = −(1/2π)·ln|x| in the plane and Φ(x) = 1/(4π|x|) in space satisfy −ΔΦ = δ, the unit point mass at 0: Φ is the potential of a point charge. Superposing, u = Φ ∗ f solves Poisson's equation −Δu = f for smooth compactly supported f. On a bounded region the Green's function corrects Φ to vanish on the boundary; for the unit disc it gives Poisson's formula, with kernel

   ```
   Pᵣ(θ) = (1 − r²)/(1 − 2r·cos θ + r²) = ∑ over n ∈ ℤ of r^|n|·e^(inθ),
   ```

   so the harmonic extension is the Fourier series of g with mode n damped by r^|n|.

6. **Existence depends on the boundary.** On the punctured disc 0 < |x| < 1 with g = 0 on the circle and g = 1 at the centre, no solution exists: a bounded harmonic function cannot feel an isolated point, so it extends across it with value 0. Perron's method builds the solution as the supremum of all subharmonic functions below the data, and it attains the boundary values at every point that admits a barrier. In the plane every boundary point of a simply connected region does; in space a sharp inward spike, Lebesgue's spine, does not.

7. **Brownian motion solves the Dirichlet problem.** Kakutani (1944): if a Brownian path starts at x and first hits ∂Ω at the random time τ, then u(x) = E[g(B(τ))], the expected boundary value at the exit point. The mean value property is the statement that the path is equally likely to leave a small sphere through any point of it, and irregular boundary points are those a path can miss at first contact.

## Key concepts

| Term | Meaning |
|---|---|
| Harmonic function | A C² function with Δu = 0 |
| Mean value property | u(x) equals its average over every sphere centred at x inside the region |
| Dirichlet problem | Find u with Δu = 0 in Ω and u = g on the boundary ∂Ω |
| Fundamental solution | Φ with −ΔΦ = δ: the potential of a unit point source |
| Green's function | The fundamental solution corrected to vanish on ∂Ω |
| Poisson kernel | The kernel turning boundary values into the harmonic extension |
| Subharmonic function | u with Δu ≥ 0, lying below its sphere averages |
| Elliptic equation | A second-order PDE whose leading part behaves like Δ, with no real characteristic directions |

## How it fits

- **Below:** the [divergence theorem](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md) gives every identity here; [holomorphic functions](../../09-advanced-analysis/02-complex-analysis/holomorphic-functions.md) supply the planar case; the Poisson kernel is an approximate identity from [Fourier series](../../09-advanced-analysis/04-harmonic-analysis/fourier-series.md); −ΔΦ = δ is a statement about [distributions](../../09-advanced-analysis/04-harmonic-analysis/distributions.md).
- **Above:** Kakutani's formula is a theorem about [Brownian motion](../../11-probability-and-statistics/03-stochastic-processes/brownian-motion.md), and E denotes its expectation; harmonic functions minimise the Dirichlet energy ∫|∇u|², whose troubled history is told in [existence of minimisers](../03-calculus-of-variations/existence-of-minimisers.md).
- **Siblings:** the [heat equation](the-heat-equation.md) relaxes to a harmonic steady state; [weak solutions](weak-solutions-and-sobolev-spaces.md) prove existence by energy instead of Perron's method; the [wave equation](the-wave-equation.md) shares the Laplacian but propagates at finite speed and has no maximum principle.

## Common misconceptions

- **"Uniqueness for the Dirichlet problem holds on any region."**: it needs boundedness or a growth condition; u = y on the half-plane is a second solution with zero boundary values.
- **"Any boundary values can be met."**: an isolated boundary point, or an inward spike in space, cannot be given arbitrary values (tenet 6).
- **"Harmonic functions are solutions of one special equation."**: they are the steady states of all diffusion, the real parts of holomorphic functions and the averages of Brownian motion, one object seen from physics, complex analysis and probability.

## Go deeper

- Lawrence C. Evans, *Partial Differential Equations* (2nd edition, 2010): mean value property, maximum principle and Green's functions with full proofs.
- Sheldon Axler, Paul Bourdon and Wade Ramey, *Harmonic Function Theory* (2nd edition, 2001): an elegant, elementary account of harmonic functions themselves.
- Peter Mörters and Yuval Peres, *Brownian Motion* (2010): the probabilistic side, including the Dirichlet problem.
