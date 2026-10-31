# Control Theory

> **Layer:** [14 Applied and Computational Mathematics](../README.md) › [Mathematical Modelling](README.md)
> **Builds on:** [Linear Systems and the Matrix Exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md), [Stability and Phase Portraits](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/stability-and-phase-portraits.md), [Singularities and Residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md), [Bayesian Inference](../../11-probability-and-statistics/04-statistical-inference/bayesian-inference.md), [Modelling and Dimensional Analysis](modelling-and-dimensional-analysis.md)
> **Enables:** [Mathematical Finance](../05-games-decisions-and-finance/mathematical-finance.md), [Feedback and Control (CS)](../../../cs-first-principles/00-engineering-foundations/04-signals-and-systems/feedback-and-control.md), [Reinforcement Learning (CS)](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md), [Congestion Control (CS)](../../../cs-first-principles/08-networking/04-transport-layer/congestion-control.md)

## Essence

Control theory asks how to choose the inputs to a dynamical system so that it behaves as intended despite disturbances and model error. Its central idea is feedback: measure the output, compare it with the goal, and let the difference drive the input. For the linear model x′ = Ax + Bu, the law u = −Kx turns A into A − BK, so stabilising a system becomes placing eigenvalues. Rudolf Kalman's work of 1960 said when that is possible (controllability), when the state can be recovered from measurements (observability), and how to do both optimally, by two dual constructions: the linear–quadratic regulator and the Kalman filter.

## Core tenets

1. **Feedback changes the dynamics, not just the input.** Take x′ = Ax + Bu, y = Cx, with state x ∈ ℝⁿ, input u and output y. An input computed in advance passes every error and disturbance through uncorrected. The closed loop u = −Kx gives x′ = (A − BK)x, whose eigenvalues can differ completely from those of A, so an unstable plant such as an inverted pendulum can be held upright.

2. **The transfer function turns dynamics into algebra, and stability into the location of poles.** With zero initial state the Laplace transform gives Y(s) = G(s)U(s), where G(s) = C(sI − A)⁻¹B. The system is asymptotically stable if and only if every eigenvalue of A has negative real part, since then e^(At) → 0. For a loop with open-loop transfer function L(s), Nyquist's criterion (1932) applies the argument principle to 1 + L(s) around the right half-plane: Z = N + P, where Z counts unstable closed-loop poles, P unstable open-loop poles, and N clockwise encirclements of −1 by the curve L(iω).

3. **Feedback cannot suppress disturbances at every frequency.** The sensitivity S = 1/(1 + L) measures how much of a disturbance survives the loop, and high loop gain makes it small. But if L is stable and falls off at least as fast as 1/s², and the closed loop is stable, Bode's integral ∫₀^∞ ln∣S(iω)∣ dω = 0 holds: attenuation at some frequencies forces amplification at others.

4. **Controllability: every state can be reached if and only if rank [B, AB, …, Aⁿ⁻¹B] = n.** The solution x(t) = e^(At)x₀ + ∫₀ᵗ e^(A(t−s))Bu(s) ds expands in powers of A, so the reachable directions lie in the span of the columns of the AᵏB, and by Cayley–Hamilton the powers from Aⁿ on add nothing new. Conversely, full rank makes the controllability Gramian invertible, which gives an explicit steering input for any time t > 0. The payoff is pole placement: for controllable (A, B), the eigenvalues of A − BK can be put anywhere, in conjugate pairs.

5. **Observability is the dual: the state can be reconstructed from the output if and only if the matrix stacking C, CA, …, CAⁿ⁻¹ has rank n.** With zero input, y and its first n − 1 derivatives equal Cx, CAx, …, CAⁿ⁻¹x, so x is determined exactly when this map is injective. Observability of (A, C) is controllability of (Aᵀ, Cᵀ). A mode that is unobservable or uncontrollable cancels out of G(s).

6. **The linear–quadratic regulator (LQR) is linear feedback from a Riccati equation.** Minimise J = ∫₀^∞ (xᵀQx + uᵀRu) dt, with Q positive semidefinite and R positive definite. If (A, B) is stabilisable and (A, Q^(1/2)) detectable, the algebraic Riccati equation has a unique stabilising solution P, and u = −R⁻¹BᵀPx is optimal:

   ```
   AᵀP + PA − PBR⁻¹BᵀP + Q = 0
   d/dt (xᵀPx) + xᵀQx + uᵀRu = (u + R⁻¹BᵀPx)ᵀ R (u + R⁻¹BᵀPx)
   so  J = x₀ᵀPx₀ + ∫₀^∞ (that square) dt,  least when the square vanishes
   ```

   Without stabilisability no input has finite cost; without detectability the cost is blind to an unstable mode.

7. **The Kalman filter is exact Bayesian estimation for linear Gaussian systems.** Let x_(k+1) = Ax_k + w_k and y_k = Cx_k + v_k, with independent Gaussian noise of covariances W and V. Conditioning a Gaussian on a linear observation leaves it Gaussian, so the posterior is carried by a mean x̂ and covariance P:

   ```
   predict:  x̂⁻ = A x̂,                  P⁻ = A P Aᵀ + W
   update:   K = P⁻Cᵀ (C P⁻ Cᵀ + V)⁻¹
             x̂ = x̂⁻ + K (y − C x̂⁻),     P = (I − K C) P⁻
   ```

   For non-Gaussian noise it is still the best linear estimator in mean square, but no longer the conditional mean. Its covariance recursion is the LQR's Riccati equation run forwards with (A, B) replaced by (Aᵀ, Cᵀ): estimation is dual to control.

8. **Separation holds, but optimality is not robustness.** With linear dynamics, Gaussian noise and quadratic cost, the optimal output-feedback controller applies the LQR gain to the Kalman estimate, and the two can be designed separately. Full-state LQR has guaranteed margins: in each input channel it tolerates gain changes from one half to infinity and 60° of phase lag. John Doyle (1978) showed that the combined linear–quadratic–Gaussian (LQG) controller has no guaranteed margins at all, which helped launch robust control.

## Key concepts

| Term | Meaning |
|---|---|
| Transfer function | G(s) = C(sI − A)⁻¹B, the input–output map after a Laplace transform |
| Pole | A value of s where G is infinite; an eigenvalue of A when no mode is hidden |
| Sensitivity function | S = 1/(1 + L), the fraction of a disturbance left after feedback |
| Controllable | Any state can be steered to any other in finite time |
| Observable | The output over an interval determines the initial state |
| Stabilisable, detectable | Every uncontrollable, or unobservable, mode is already stable |
| Riccati equation | The quadratic matrix equation whose solution gives the LQR gain and the filter covariance |

## How it fits

- **Below:** the matrix exponential solves the model, eigenvalues decide stability, the argument principle gives Nyquist's criterion, and the Kalman filter is Bayesian inference with Gaussian conjugacy.
- **Above:** [reinforcement learning](../../../cs-first-principles/13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) is optimal control with an unknown model, its Bellman equation generalising the Riccati equation; [mathematical finance](../05-games-decisions-and-finance/mathematical-finance.md) uses stochastic control for portfolios.
- **Siblings:** [modelling](modelling-and-dimensional-analysis.md) supplies the model; [mathematical biology](mathematical-biology-and-epidemics.md) studies feedback loops that nature built.

## Common misconceptions

- **"More gain is always better."** High gain amplifies sensor noise, saturates actuators and, with delays, destabilises.
- **"A stable transfer function means a stable system."** A cancelled unstable mode grows inside the system while the input–output map looks fine.
- **"An optimal controller is a robust one."** LQG controllers can be destabilised by arbitrarily small model errors.

## Go deeper

- K. J. Åström and R. M. Murray, *Feedback Systems* (2008): the gentle modern introduction.
- E. D. Sontag, *Mathematical Control Theory* (2nd edition, 1998): the rigorous treatment, linear and nonlinear.
- R. E. Kalman, "A New Approach to Linear Filtering and Prediction Problems" (1960): the filter's original paper.
