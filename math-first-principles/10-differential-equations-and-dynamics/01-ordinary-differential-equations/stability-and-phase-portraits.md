# Stability and Phase Portraits

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Ordinary Differential Equations](README.md)
> **Builds on:** [Linear systems and the matrix exponential](linear-systems-and-the-matrix-exponential.md), [Existence and uniqueness](existence-and-uniqueness.md), [The derivative as a linear map](../../06-real-analysis/04-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Topological spaces and continuous maps](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md)
> **Enables:** [Bifurcations](../04-dynamical-systems/bifurcations.md), [Chaos and strange attractors](../04-dynamical-systems/chaos-and-strange-attractors.md), [Control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md), [Mathematical biology and epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md)

## Essence

Most nonlinear systems x′ = f(x) have no solution formula, so one asks qualitative questions instead: where are the equilibria, which are stable, and what does the flow look like as a whole? A phase portrait answers by drawing the trajectories in state space. Two tools do most of the work. Linearisation replaces f near an equilibrium by its derivative and reads stability off the eigenvalues, which is valid exactly when no eigenvalue lies on the imaginary axis. A Lyapunov function, an energy-like quantity that never increases along trajectories, proves stability without solving anything.

## Core tenets

1. **Linearisation decides stability at a hyperbolic equilibrium.** If f(x*) = 0 and f is C¹, then near x* the system is x′ ≈ J(x − x*), with J = Df(x*) the Jacobian matrix. If every eigenvalue of J has negative real part, x* is asymptotically stable, because the linear part contracts in a suitable norm and the remainder, o(|x − x*|), is too small to undo it; one eigenvalue with positive real part makes x* unstable. On the imaginary axis the test is silent: x′ = −x³ and x′ = x³ share the linearisation x′ = 0, yet the first equilibrium attracts and the second repels.

2. **Hartman–Grobman theorem: near a hyperbolic equilibrium the flow is the linear flow in disguise.** If f is C¹ and no eigenvalue of J has zero real part, a homeomorphism of a neighbourhood of x* carries trajectories of x′ = f(x) onto those of x′ = J(x − x*), preserving time (Grobman, 1959; Hartman, 1960). The conjugacy is only continuous, so it keeps what topology sees, the numbers of stable and unstable directions, but not rates or the difference between a node and a spiral. Without hyperbolicity it fails: in polar coordinates r′ = −r³, θ′ = 1 spirals into the origin, while its linearisation is a centre with closed orbits.

3. **Planar equilibria are classified by trace and determinant.** A 2 × 2 Jacobian with trace τ and determinant Δ has eigenvalues (τ ± √(τ² − 4Δ))/2. So Δ < 0 gives a saddle; Δ > 0 and τ² ≥ 4Δ a node; Δ > 0 and τ² < 4Δ a spiral; the sign of τ decides stable or unstable; τ = 0 < Δ is a linear centre, the non-hyperbolic case the nonlinear terms decide. Two numbers place every planar equilibrium on a map, and a bifurcation is a path crossing one of its borders.

4. **Stable and unstable manifolds organise the portrait.** At a hyperbolic saddle the points whose trajectories converge to x* form a smooth curve or surface, the stable manifold, tangent to the stable eigenspace of J; the unstable manifold is the same with t → −∞. These separatrices divide regions of different fate. For the pendulum θ″ = −sin θ, separatrices through the saddles at θ = ±π divide oscillation from rotation over the top:

   ```
    θ′
    ^       rotations: θ keeps increasing
    |  >----->----->----->----->----->--
    |        .-----.     .-----.
    |      /         \ /         \
    |  ---X   ( o )   X   ( o )   X---
    |      \         / \         /
    |        '-----'     '-----'
    |  --<-----<-----<-----<-----<-----<
    +---------------------------------> θ
         −π     0     π    2π    3π
   ```

5. **Lyapunov's direct method proves stability without solving.** If V is C¹ with a strict minimum at x* and V̇ = ∇V·f ≤ 0, then x* is stable: a trajectory inside a small level set of V cannot climb out. If V̇ < 0 away from x*, it is asymptotically stable. For the damped pendulum θ″ = −sin θ − kθ′ with k > 0, the energy V = ½θ′² + 1 − cos θ gives V̇ = −kθ′², which vanishes on the line θ′ = 0; LaSalle's invariance principle finishes, since only the rest point stays on that line. For a stable linear part, V(x) = xᵀPx with JᵀP + PJ = −I always works, which is how tenet 1 is proved.

6. **Poincaré–Bendixson theorem: in the plane, bounded motion settles down.** For a C¹ planar system, if a forward trajectory stays in a compact region containing no equilibria, its limit set is a periodic orbit: the trajectory is periodic or spirals towards a limit cycle. Proof idea: a trajectory that crosses a transverse segment twice draws a closed curve that, by the Jordan curve theorem, traps it on one side, so its crossings move monotonically along the segment and converge. Chaos therefore needs three dimensions in continuous time, as in the [Lorenz system](../04-dynamical-systems/chaos-and-strange-attractors.md), but only one for [iterated maps](../04-dynamical-systems/iterated-maps.md).

## Key concepts

| Term | Meaning |
|---|---|
| Equilibrium | A point x* with f(x*) = 0 |
| Lyapunov stable | Trajectories starting close enough to x* stay within any prescribed distance of it |
| Asymptotically stable | Lyapunov stable, and nearby trajectories converge to x* |
| Jacobian matrix | J = Df(x*), the matrix of partial derivatives ∂fᵢ/∂xⱼ at x* |
| Hyperbolic equilibrium | One where no eigenvalue of J has zero real part |
| Stable manifold | The points whose trajectories converge to x* as t → ∞ |
| Separatrix | A trajectory bounding regions of different long-term behaviour |
| Lyapunov function | V with a strict minimum at x* that does not increase along trajectories |
| Limit cycle | An isolated periodic orbit |

## How it fits

- **Below:** the [derivative as a linear map](../../06-real-analysis/04-calculus-of-several-variables/the-derivative-as-a-linear-map.md) supplies J, [linear systems](linear-systems-and-the-matrix-exponential.md) supply the model behaviour, and a homeomorphism from [topology](../../07-topology/01-point-set-topology/topological-spaces-and-continuous-maps.md) says what "the same portrait" means.
- **Above:** a digital latch caught at its balanced point is a saddle, and a state starting at distance d from the stable manifold lingers for a time of order (1/λ)·ln(1/d), λ the unstable eigenvalue: the [metastability](../../../cs-first-principles/03-digital-logic/03-sequential-logic/latches-and-flip-flops.md) problem. [Gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md) follow x′ = −∇U, whose Lyapunov function is U, and [bifurcations](../04-dynamical-systems/bifurcations.md) happen exactly where hyperbolicity fails.
- **Siblings:** [existence and uniqueness](existence-and-uniqueness.md) supplies the flow the portrait draws; [linear systems](linear-systems-and-the-matrix-exponential.md) are its local model; [boundary value problems](boundary-value-problems-and-sturm-liouville-theory.md) ask about one trajectory joining two ends, not the whole flow.

## Common misconceptions

- **"The linearisation always tells you the stability."**: only at hyperbolic equilibria; x′ = ±x³ and r′ = −r³, θ′ = 1 show the nonlinear terms deciding.
- **"Stable means trajectories converge to the equilibrium."**: Lyapunov stability only keeps them close. The bottom of a frictionless pendulum is stable, but nearby motions oscillate for ever.
- **"A bounded trajectory must approach an equilibrium."**: it can approach a limit cycle, as a heartbeat does, and in three or more dimensions it can wander on a strange attractor for ever.

## Go deeper

- Steven H. Strogatz, *Nonlinear Dynamics and Chaos* (2nd edition): the clearest introduction to phase portraits, with applications in every chapter.
- Lawrence Perko, *Differential Equations and Dynamical Systems* (3rd edition, 2001): Hartman–Grobman, stable manifolds and Poincaré–Bendixson with proofs.
- Morris W. Hirsch, Stephen Smale and Robert L. Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos* (3rd edition, 2013): Lyapunov functions and planar systems at an introductory pace.
