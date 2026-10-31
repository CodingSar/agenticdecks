# Existence of Minimisers

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Calculus of Variations](README.md)
> **Builds on:** [The Euler–Lagrange equation](the-euler-lagrange-equation.md), [Weak solutions and Sobolev spaces](../02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md), [Compactness in metric spaces](../../06-real-analysis/04-metric-spaces/compactness-in-metric-spaces.md), [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md)
> **Enables:** [Convex optimisation and duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md), [Gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [History of mathematics](../../15-mathematics-in-context/history-of-mathematics.md)

## Essence

The Euler–Lagrange equation says what a minimiser must satisfy if there is one; whether there is one is a separate question. The nineteenth century learned this the hard way. Riemann built existence theorems on Dirichlet's principle, the assumption that the Dirichlet energy has a minimiser, and Weierstrass showed in 1870 that a functional bounded below need not attain its infimum. The direct method of the calculus of variations, developed by Hilbert, Tonelli and their successors, answers by compactness: take a minimising sequence, extract a convergent subsequence, and show the limit minimises. It needs three ingredients: coercivity, compactness in a weak topology and lower semicontinuity.

## Core tenets

1. **Assuming existence can prove nonsense.** Perron's paradox: let N be the largest positive integer; if N > 1 then N² > N, a contradiction, so N = 1. The Euler–Lagrange equation is equally conditional: it is a necessary condition on a minimiser, and says nothing until one is known to exist.

2. **Weierstrass's counterexample.** Minimise J[y] = ∫ from −1 to 1 of x²·y′² dx over C¹ functions with y(−1) = −1 and y(1) = 1. The functions y(x) = arctan(x/ε)/arctan(1/ε) are admissible and J → 0 as ε → 0. But J[y] = 0 forces y′ = 0 wherever x ≠ 0, so y is constant and cannot meet both boundary values. The infimum 0 is not attained: minimising sequences converge to a step, outside the class. The weight x², vanishing at 0, destroys the control that ∫y′² would give.

3. **The direct method.** Let X be a reflexive Banach space, A a non-empty weakly closed subset, and J: A → ℝ coercive, meaning J(u) → ∞ as ‖u‖ → ∞, and weakly sequentially lower semicontinuous, meaning uₖ ⇀ u implies J(u) ≤ lim inf J(uₖ). Then J attains its minimum on A. Proof: a minimising sequence is bounded by coercivity; in a reflexive space a bounded sequence has a weakly convergent subsequence; lower semicontinuity makes the limit a minimiser. Each hypothesis matters: eˣ on ℝ is not coercive and has no minimum, and Weierstrass's J is not coercive on the natural space.

4. **Weak convergence restores compactness; convexity supplies semicontinuity.** In infinite dimensions bounded sequences need not have norm-convergent subsequences: an orthonormal sequence eₖ has ‖eₖ − eⱼ‖ = √2, yet eₖ ⇀ 0 weakly. Weak limits lose information, since ‖eₖ‖ = 1 while the limit has norm 0, so continuity fails and only lower semicontinuity can survive. Convexity provides it: a continuous convex functional has closed convex sublevel sets, which are weakly closed. For integrals ∫ L(x, u, ∇u), Tonelli's insight was that convexity of L in the gradient variable is the condition that matters.

5. **Without convexity, minimising sequences oscillate.** Minimise ∫ from 0 to 1 of ((y′² − 1)² + y²) dx with y(0) = y(1) = 0. Sawtooth functions with slopes ±1 and k teeth make the first term vanish and the second at most 1/(4k²), so the infimum is 0; but J = 0 needs both y = 0 and |y′| = 1. Finer and finer oscillation, microstructure, is how crystals of shape-memory alloys behave (Ball and James, 1987). For vector-valued u the right condition is quasiconvexity (Morrey, 1952), implied by polyconvexity (Ball, 1977), which covers nonlinear elasticity.

6. **Dirichlet's principle rescued, and regularity.** On a bounded region, minimise ∫|∇u|² over u ∈ H¹ with u − g ∈ H¹₀. The Poincaré inequality gives coercivity and the energy is convex and continuous, so the direct method gives a minimiser: the weak solution of Laplace's equation, smooth by Weyl's lemma. Hilbert revived the principle in 1900, and his nineteenth problem asked whether minimisers of regular variational problems are always smooth. De Giorgi (1957) and Nash (1958) proved this for scalar problems; De Giorgi (1968) found a counterexample for systems.

7. **Beyond minima.** Critical points that are not minima can also be found by compactness. The mountain pass theorem (Ambrosetti and Rabinowitz, 1973): if two low points are separated by a ridge and the Palais–Smale compactness condition holds, there is a saddle-type critical point at the lowest pass.

## Key concepts

| Term | Meaning |
|---|---|
| Minimising sequence | A sequence uₖ with J(uₖ) tending to the infimum of J |
| Coercive | J(u) → ∞ as ‖u‖ → ∞ |
| Weak convergence | uₖ ⇀ u when ℓ(uₖ) → ℓ(u) for every bounded linear functional ℓ |
| Lower semicontinuous | J(u) ≤ lim inf J(uₖ) whenever uₖ converges to u in the given sense |
| Reflexive Banach space | One equal to its double dual; its bounded sequences have weakly convergent subsequences |
| Dirichlet's principle | The claim that the Dirichlet energy with given boundary values has a minimiser |
| Quasiconvexity | Morrey's condition on a vector integrand making its integral weakly lower semicontinuous |
| Microstructure | Ever finer oscillation of minimising sequences of a non-convex functional |

## How it fits

- **Below:** the [Euler–Lagrange equation](the-euler-lagrange-equation.md) is what a minimiser solves; [Sobolev spaces](../02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) are where it lives; [compactness in metric spaces](../../06-real-analysis/04-metric-spaces/compactness-in-metric-spaces.md) is the finite-dimensional model, and [Banach](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md) and [Hilbert spaces](../../09-advanced-analysis/03-functional-analysis/hilbert-spaces.md) supply weak topologies.
- **Above:** [convex optimisation](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md) is the finite-dimensional twin; [gradient methods](../../14-applied-and-computational-mathematics/02-optimisation/gradient-methods.md) generate minimising sequences, and [finite elements](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) minimise over subspaces; the Dirichlet principle controversy is a landmark in the [history](../../15-mathematics-in-context/history-of-mathematics.md) of rigour.
- **Siblings:** [Noether's theorem](noethers-theorem.md) concerns symmetries of the same functionals; [Laplace's equation](../02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) is the Euler–Lagrange equation of the Dirichlet energy.

## Common misconceptions

- **"A functional bounded below attains its minimum."**: Weierstrass's example has infimum 0 and no minimiser.
- **"A minimising sequence converges to the minimiser."**: it may converge only weakly, oscillate ever faster, or approach something outside the admissible class.
- **"No classical minimiser means the problem is meaningless."**: enlarging the space to Sobolev functions, or relaxing the functional, often produces a minimiser that regularity theory then shows to be classical.

## Go deeper

- Bernard Dacorogna, *Introduction to the Calculus of Variations*: the direct method at an advanced undergraduate level.
- Enrico Giusti, *Direct Methods in the Calculus of Variations* (2003): existence and regularity of minimisers, including De Giorgi's method.
- Michael Struwe, *Variational Methods* (4th edition, 2008): minimisation, mountain passes and compactness conditions.
