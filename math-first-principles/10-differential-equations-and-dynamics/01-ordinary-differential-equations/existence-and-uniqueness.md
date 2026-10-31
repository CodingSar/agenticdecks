# Existence and Uniqueness

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Ordinary Differential Equations](README.md)
> **Builds on:** [Completeness and the contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [The fundamental theorem of calculus](../../06-real-analysis/02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md), [Uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md), [Compactness in metric spaces](../../06-real-analysis/03-metric-spaces/compactness-in-metric-spaces.md)
> **Enables:** [Linear systems and the matrix exponential](linear-systems-and-the-matrix-exponential.md), [Stability and phase portraits](stability-and-phase-portraits.md), [Chaos and strange attractors](../04-dynamical-systems/chaos-and-strange-attractors.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [Stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md)

## Essence

An ordinary differential equation (ODE) y′ = f(t, y) prescribes the velocity of a state y ∈ ℝⁿ at each time t; with a starting value y(t₀) = y₀ it becomes an initial value problem (IVP). Does this law of change determine one future, and only one? Integrate both sides: a solution becomes a fixed point of a map on a complete space of continuous functions, and the contraction mapping principle gives existence and uniqueness together. If f is merely continuous, solutions still exist by compactness but can branch; if f grows faster than linearly, a solution can reach infinity in finite time. Every qualitative statement about dynamics starts from these facts.

## Core tenets

1. **An IVP is the same as an integral equation.** By the fundamental theorem of calculus, a continuous y solves y′ = f(t, y), y(t₀) = y₀ on an interval I if and only if, for all t ∈ I,

   ```
   y(t) = y₀ + ∫ from t₀ to t of f(s, y(s)) ds   =:  (Ty)(t).
   ```

   The integral form needs no derivative of y, and T acts on the space C(I) of continuous functions with the sup norm ‖y‖ = max over I of |y(t)|, which is complete because uniform limits of continuous functions are continuous.

2. **Picard–Lindelöf theorem: a Lipschitz condition gives a unique local solution.** Let f be continuous on the box R = {|t − t₀| ≤ a, |y − y₀| ≤ b}, with |f| ≤ M and |f(t, y) − f(t, z)| ≤ L|y − z| on R. Then exactly one solution exists on [t₀ − h, t₀ + h], where h = min(a, b/M). Proof idea: T keeps functions inside the box, since |Ty(t) − y₀| ≤ M|t − t₀| ≤ b, and iterating the Lipschitz bound gives ‖Tᵏy − Tᵏz‖ ≤ ((Lh)ᵏ/k!)·‖y − z‖, so some power of T is a contraction with a unique fixed point. For y′ = y, y(0) = 1 the iterates 1, 1 + t, 1 + t + t²/2, … are the partial sums of eᵗ.

3. **Grönwall's inequality: solutions depend continuously on their data.** If y and z solve the same Lipschitz equation, then |y(t) − z(t)| ≤ |y(t₀) − z(t₀)|·e^(L·|t − t₀|). The difference u = |y − z| satisfies u ≤ u(t₀) + L∫u, and comparison with u′ = Lu gives the exponential. Over a fixed time this is continuity; over long times it permits exponential separation of neighbours, the mechanism of [chaos](../04-dynamical-systems/chaos-and-strange-attractors.md).

4. **Peano's theorem: continuity alone gives existence, not uniqueness.** If f is only continuous on R, a solution still exists on [t₀ − h, t₀ + h]. Proof idea: Euler polygons with step 1/k have slopes at most M, so they are uniformly bounded and equicontinuous; the Arzelà–Ascoli theorem extracts a uniformly convergent subsequence, whose limit satisfies the integral equation. Nothing forces uniqueness: y′ = 2√|y|, y(0) = 0 is solved by y ≡ 0 and, for each c ≥ 0, by y = 0 for t ≤ c and y = (t − c)² for t ≥ c, because √|y| is not Lipschitz at 0. Without continuity even existence fails: if f(y) = 1 for y ≤ 0 and −1 for y > 0, then y(0) = 0 pushes y above 0, where slope −1 forces y(t) = −t < 0.

5. **Solutions end only by escaping: blow-up in finite time.** The smooth equation y′ = y², y(0) = 1 has the solution y = 1/(1 − t), which tends to infinity as t → 1. If f is continuous and locally Lipschitz on an open set U, the local theorem restarts from any endpoint, so a maximal solution on (α, β) with β < ∞ must leave every compact subset of U as t → β. Under linear growth, |f(t, y)| ≤ A + B|y|, Grönwall's inequality keeps |y| finite on bounded intervals, so solutions are global.

6. **The flow turns an equation into a dynamical system.** For an autonomous equation y′ = f(y) with f locally Lipschitz, write φₜ(y₀) for the state at time t starting from y₀. Uniqueness gives φ₀ = identity and φₛ ∘ φₜ = φₛ₊ₜ wherever defined, since running for time t and then s solves the same IVP as running for s + t. Trajectories never cross, and if f is Cᵏ then φₜ is Cᵏ in y₀, its derivative solving the linearised equation Z′ = Df(y(t))·Z. An n-th order equation is a first-order system for (y, y′, …, y⁽ⁿ⁻¹⁾), so Newton's law needs exactly position and velocity as its state.

## Key concepts

| Term | Meaning |
|---|---|
| Lipschitz condition | ∣f(t, y) − f(t, z)∣ ≤ L·∣y − z∣ for one constant L; holds locally whenever ∂f/∂y is continuous |
| Picard iteration | yₖ₊₁ = T(yₖ) starting from the constant function y₀; converges uniformly to the solution |
| Grönwall's inequality | u ≤ c + L∫u implies u ≤ c·e^(L(t − t₀)) |
| Equicontinuous family | For each ε > 0 a single δ > 0 works for every function in the family |
| Arzelà–Ascoli theorem | A uniformly bounded, equicontinuous sequence of functions on a compact interval has a uniformly convergent subsequence |
| Blow-up | ∣y(t)∣ → ∞ as t approaches a finite time |
| Flow | The map (t, y₀) ↦ φₜ(y₀) sending an initial state to the state at time t |

## How it fits

- **Below:** the proof is the [contraction mapping principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) in a function space, and Peano's theorem is compactness of equicontinuous families; the same contraction proves the [inverse function theorem](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md).
- **Above:** Picard iteration gives existence for stochastic differential equations (SDEs) in [stochastic calculus](../../11-probability-and-statistics/03-stochastic-processes/stochastic-calculus.md); run in Sobolev spaces, it gives local existence for [nonlinear partial differential equations (PDEs)](../02-partial-differential-equations/nonlinear-pdes.md); Euler polygons become [numerical methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), whose error analysis is Grönwall's inequality again.
- **Siblings:** [linear systems](linear-systems-and-the-matrix-exponential.md) are the case where solutions are explicit and global; [stability](stability-and-phase-portraits.md) studies the flow defined here; [boundary value problems](boundary-value-problems-and-sturm-liouville-theory.md) show that data at two ends, unlike data at one time, can fail to fix a solution.

## Common misconceptions

- **"A smooth right-hand side gives a solution for all time."**: y′ = y² is smooth and blows up at t = 1. Smoothness controls the local theory; growth controls the global one.
- **"Without a Lipschitz condition there may be no solution."**: Peano's theorem gives existence from continuity alone; the Lipschitz condition buys uniqueness.
- **"Non-uniqueness only happens in contrived examples."**: Torricelli's law h′ = −k√h for a draining tank has the same square root, so an empty tank could have emptied at any earlier time.

## Go deeper

- Vladimir I. Arnold, *Ordinary Differential Equations*: geometric from the first page, with flows in place of formulas.
- Morris W. Hirsch, Stephen Smale and Robert L. Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos* (3rd edition, 2013): the existence theory proved alongside the dynamics it supports.
- Gerald Teschl, *Ordinary Differential Equations and Dynamical Systems* (2012): a modern rigorous course with complete proofs.
