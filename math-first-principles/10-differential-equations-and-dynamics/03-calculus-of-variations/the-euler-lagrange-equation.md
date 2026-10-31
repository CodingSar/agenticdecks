# The Euler–Lagrange Equation

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Calculus of Variations](README.md)
> **Builds on:** [Extrema and Lagrange multipliers](../../06-real-analysis/03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md), [The fundamental theorem of calculus](../../06-real-analysis/02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md), [The derivative as a linear map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Boundary value problems and Sturm–Liouville theory](../01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md)
> **Enables:** [Noether's theorem](noethers-theorem.md), [Existence of minimisers](existence-of-minimisers.md), [Hamiltonian systems and integrability](../04-dynamical-systems/hamiltonian-systems-and-integrability.md), [Control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md)

## Essence

The calculus of variations looks for functions that make an integral as small as possible, or at least stationary: shortest paths, the curve of fastest descent, soap films, the motion of planets. A minimum of an ordinary function has zero derivative; a minimiser of a functional J[y] = ∫ L(x, y, y′) dx satisfies a differential equation, the Euler–Lagrange equation, which Euler and Lagrange developed in the 1740s and 1750s. It turns optimisation over an infinite-dimensional space into a boundary value problem, and through Hamilton's principle it makes all of classical mechanics an instance of one idea.

## Core tenets

1. **The first variation must vanish.** Perturb a candidate y by εη, where η(a) = η(b) = 0 so the boundary values stay fixed. If y minimises J, then ε ↦ J[y + εη] has a minimum at 0, so its derivative there vanishes. Differentiating under the integral and integrating the η′ term by parts gives, for y of class C²,

   ```
   (d/dε) J[y + εη] at ε = 0  =  ∫ from a to b of ( ∂L/∂y − (d/dx)(∂L/∂y′) )·η dx  =  0.
   ```

2. **The fundamental lemma turns "for every η" into an equation.** If G is continuous and ∫G·η = 0 for every smooth η vanishing at the ends, then G ≡ 0: otherwise take η to be a bump where G > 0. So ∂L/∂y − (d/dx)(∂L/∂y′) = 0, the Euler–Lagrange equation. For arc length L = √(1 + y′²) it says ∂L/∂y′ is constant, so y′ is constant: the shortest curve is a straight line. Du Bois-Reymond showed that a C¹ minimiser already satisfies an integrated form, without assuming a second derivative.

3. **When L does not involve x, a first integral comes free.** Along solutions y′·∂L/∂y′ − L is constant (the Beltrami identity). Johann Bernoulli's brachistochrone problem (1696) asks for the curve of fastest descent under gravity; with y measured downwards the time is proportional to ∫ √((1 + y′²)/y) dx, and the identity gives y·(1 + y′²) = constant, whose solutions are cycloids. In mechanics the same identity is conservation of energy, the first instance of [Noether's theorem](noethers-theorem.md).

4. **Hamilton's principle makes mechanics variational.** For a particle with kinetic energy ½mẋ² in a potential V, the action ∫(½mẋ² − V(x)) dt has Euler–Lagrange equation mẍ = −V′(x): Newton's law. Physical paths are stationary, not necessarily minimal. For the oscillator L = ½(ẋ² − x²) on [0, T] with fixed ends, the trial variation η = sin(πt/T) gives second variation ∫(η̇² − η²) dt = (T/2)·((π/T)² − 1), negative once T > π: the solution through those ends is then a saddle point of the action.

5. **The second variation separates minima from saddles.** A minimiser must satisfy Legendre's condition ∂²L/∂y′² ≥ 0 along it. Jacobi's condition adds that there be no conjugate point inside the interval: no point where a nearby family of solutions from the starting point refocuses. In the oscillator the first conjugate point is at t = π; on a sphere it is the antipode, which is why a great-circle arc longer than half a great circle is not the shortest path.

6. **Several variables give partial differential equations.** For J[u] = ∫ over Ω of L(x, u, ∇u), the equation is ∂L/∂u − div(∂L/∂∇u) = 0. The Dirichlet energy ½∫|∇u|² − ∫f·u gives Poisson's equation −Δu = f, and the area ∫√(1 + |∇u|²) of a graph gives the minimal surface equation div(∇u/√(1 + |∇u|²)) = 0, satisfied by soap films.

7. **Constraints bring Lagrange multipliers; free ends bring natural conditions.** To make J stationary while K stays fixed, make J − λK stationary. Dido's problem, the most area A enclosed by a curve of length ℓ, has the circle as answer and gives the isoperimetric inequality 4πA ≤ ℓ². Minimising ∫y′² subject to ∫y² = 1 gives −y″ = λy, a Sturm–Liouville eigenvalue problem with λ as the multiplier. At an end left free, the variation forces ∂L/∂y′ = 0 there.

## Key concepts

| Term | Meaning |
|---|---|
| Functional | A map from functions to numbers, such as J[y] = ∫ L(x, y, y′) dx |
| Lagrangian | The integrand L; in mechanics kinetic minus potential energy |
| First variation | The derivative of J at y in the direction of a perturbation η |
| Euler–Lagrange equation | ∂L/∂y − (d/dx)(∂L/∂y′) = 0, the condition for J to be stationary |
| Action | The time integral of the Lagrangian along a path |
| Conjugate point | A point beyond which a stationary path stops being a local minimum |
| Natural boundary condition | ∂L/∂y′ = 0 at an end where y is left free |

## How it fits

- **Below:** this is [extrema and Lagrange multipliers](../../06-real-analysis/03-calculus-of-several-variables/extrema-and-lagrange-multipliers.md) in infinitely many variables, with the first variation a directional [derivative](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md) and integration by parts from the [fundamental theorem of calculus](../../06-real-analysis/02-calculus-of-one-variable/the-fundamental-theorem-of-calculus.md); the result is a [boundary value problem](../01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md).
- **Above:** Pontryagin's maximum principle in [control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md) extends the equation to constrained controls; Einstein's equations are the Euler–Lagrange equations of the Einstein–Hilbert action in [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md).
- **Siblings:** [Noether's theorem](noethers-theorem.md) reads conservation laws off symmetries of L; [existence of minimisers](existence-of-minimisers.md) asks whether there is anything to find; the Legendre transform p = ∂L/∂q̇, H = p·q̇ − L turns the equation into [Hamilton's equations](../04-dynamical-systems/hamiltonian-systems-and-integrability.md).

## Common misconceptions

- **"Solving the Euler–Lagrange equation finds the minimiser."**: it finds stationary functions, which may be saddles (tenet 4), and a minimiser may not exist at all, as Weierstrass showed.
- **"Nature minimises the action."**: the principle of least action is one of stationary action; minimality holds only over short enough times.
- **"Any function satisfying the boundary conditions can compete."**: the class of competitors matters, and enlarging it can lower the infimum or let a minimiser exist; choosing it well is the subject of the direct method.

## Go deeper

- I. M. Gelfand and S. V. Fomin, *Calculus of Variations* (1963): a concise classic covering first and second variations and the Hamilton–Jacobi theory.
- Richard P. Feynman, *The Feynman Lectures on Physics*, Volume II, chapter 19 (1964): the principle of least action explained by a physicist.
- Cornelius Lanczos, *The Variational Principles of Mechanics* (1949): the variational view of mechanics developed historically and philosophically.
