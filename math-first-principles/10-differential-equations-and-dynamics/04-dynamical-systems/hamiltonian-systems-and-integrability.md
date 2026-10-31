# Hamiltonian Systems and Integrability

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Dynamical Systems](README.md)
> **Builds on:** [The Euler–Lagrange equation](../03-calculus-of-variations/the-euler-lagrange-equation.md), [Noether's theorem](../03-calculus-of-variations/noethers-theorem.md), [Differential forms and de Rham cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), [Topological and smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [Ergodic theory](ergodic-theory.md)
> **Enables:** [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md), [Numerical methods for differential equations](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md), [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md)

## Essence

Hamiltonian systems are the dynamics of mechanics without friction: planets, particles, light rays and, through quantisation, atoms. Their flows preserve a geometric structure, the symplectic form, which forbids attractors and makes phase-space volume constant. At one extreme are integrable systems, with enough conserved quantities that every motion winds quasi-periodically around a torus; generic systems are not integrable. Kolmogorov–Arnold–Moser (KAM) theory bridges the two: under small perturbations most tori survive, so order and chaos coexist, which is the modern picture of the solar system's stability.

## Core tenets

1. **Hamilton's equations come from the Legendre transform.** Given a Lagrangian L(q, q̇), set p = ∂L/∂q̇ and H(q, p) = p·q̇ − L. The Euler–Lagrange equations become the first-order system

   ```
   q̇ᵢ = ∂H/∂pᵢ,   ṗᵢ = −∂H/∂qᵢ,   or  ż = J·∇H(z)  with  z = (q, p),  J = [[0, I], [−I, 0]].
   ```

   H is conserved because dH/dt = ∇H·J∇H = 0, J being antisymmetric. For a particle, H = ∣p∣²/(2m) + V(q) is the total energy.

2. **Flows preserve the symplectic form.** The two-form ω = ∑ dpᵢ ∧ dqᵢ measures oriented areas projected onto the (qᵢ, pᵢ) planes. The Jacobian matrix M of a Hamiltonian flow map satisfies MᵀJM = J, which says the flow preserves ω. Taking determinants gives Liouville's theorem: phase-space volume is conserved, so there are no attractors and the motion carries a natural invariant measure. Darboux's theorem says every symplectic form looks like ω in suitable local coordinates, so, unlike Riemannian metrics, symplectic structures have no local invariants.

3. **Symplectic is more than volume-preserving.** Gromov's non-squeezing theorem (1985): a ball of radius r cannot be mapped symplectically into a cylinder {q₁² + p₁² < R²} with R < r, although a volume-preserving map can squeeze it in. This rigidity founded symplectic topology. Numerically, integrators such as Störmer–Verlet, which preserve ω exactly, keep energy errors bounded over very long runs, while ordinary methods let energy drift.

4. **Poisson brackets carry the algebra.** Any observable evolves by dF/dt = {F, H}, where {F, G} = ∑ (∂F/∂qᵢ·∂G/∂pᵢ − ∂F/∂pᵢ·∂G/∂qᵢ), so F is conserved if and only if {F, H} = 0. Dirac (1925) saw that quantum mechanics replaces this bracket by the commutator of operators divided by iħ; this is the route from classical to quantum dynamics.

5. **Integrable systems move on tori.** The Liouville–Arnold theorem: if a system with n degrees of freedom has n independent conserved quantities F₁, …, Fₙ with all {Fᵢ, Fⱼ} = 0, then each compact connected level set is an n-dimensional torus Tⁿ. Near it there are action–angle variables (I, θ) in which H = H(I), so the actions are constant and θ̇ = ω(I): quasi-periodic winding with frequencies ω. Examples are the Kepler problem, coupled oscillators, the spinning tops of Euler, Lagrange and Kovalevskaya (1888), the Toda lattice, and in infinite dimensions the Korteweg–de Vries equation of [nonlinear partial differential equations](../02-partial-differential-equations/nonlinear-pdes.md).

6. **Integrability is rare.** Poincaré showed that the three-body problem, treated as a perturbation of Kepler motion, has no further conserved quantities depending analytically on the perturbation parameter. The obstruction is small divisors: perturbation series contain denominators k·ω, for integer vectors k, which come arbitrarily close to zero and make the series diverge. Near resonances tori break into chains of islands surrounded by thin chaotic layers.

7. **KAM: most tori survive.** For H = H₀(I) + εH₁(θ, I) with H₀ non-degenerate, Kolmogorov (1954) announced, and Arnold (1963) and Moser (1962) proved in different settings, that for small ε most invariant tori persist, deformed. The survivors have Diophantine frequencies,

   ```
   ∣k·ω∣ ≥ γ / ∣k∣^τ   for every non-zero integer vector k,   with  τ > n − 1,
   ```

   badly approximable as with [algebraic numbers](../../02-number-systems/01-constructing-the-numbers/algebraic-and-transcendental-numbers.md), and the destroyed tori occupy a measure tending to 0 with ε. So typical Hamiltonian systems are neither integrable nor ergodic.

8. **Stability: forever, or only for a very long time.** With two degrees of freedom, surviving two-dimensional tori divide each three-dimensional energy surface, trapping orbits forever. With three or more they do not, and Arnold (1964) gave an example of slow drift through the gaps, Arnold diffusion. Nekhoroshev (1977) showed such drift takes a time exponentially long in a power of 1/ε. Numerical integrations, beginning with Laskar's in 1989, indicate that the inner solar system is chaotic on timescales of millions of years.

## Key concepts

| Term | Meaning |
|---|---|
| Hamiltonian | The function H(q, p), usually total energy, generating the flow |
| Symplectic form | The two-form ω = ∑ dpᵢ ∧ dqᵢ preserved by Hamiltonian flows |
| Liouville's theorem | Hamiltonian flows preserve phase-space volume |
| Poisson bracket | {F, G}, the bracket with dF/dt = {F, H} |
| Involution | Conserved quantities with pairwise vanishing Poisson brackets |
| Action–angle variables | Coordinates (I, θ) in which an integrable flow is θ̇ = ω(I) |
| Small divisors | Denominators k·ω that come close to zero in perturbation series |
| Diophantine frequency | A frequency vector with ∣k·ω∣ ≥ γ/∣k∣^τ for all non-zero integer k |
| Arnold diffusion | Slow drift of actions through gaps between invariant tori |

## How it fits

- **Below:** the [Euler–Lagrange equation](../03-calculus-of-variations/the-euler-lagrange-equation.md) and the Legendre transform give the equations; [Noether's theorem](../03-calculus-of-variations/noethers-theorem.md) supplies conserved quantities; phase space is a [smooth manifold](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) carrying a [differential form](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md).
- **Above:** canonical quantisation in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), with computing's view in [quantum mechanics and band theory](../../../cs-first-principles/00-engineering-foundations/01-physics-of-computation/quantum-mechanics-and-band-theory.md); geodesics in [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) are Hamiltonian; symplectic integrators in [numerical methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md); Hamiltonian Monte Carlo in [Monte Carlo methods](../../14-applied-and-computational-mathematics/01-numerical-analysis/monte-carlo-methods.md).
- **Siblings:** [ergodic theory](ergodic-theory.md) receives Liouville's invariant measure; [chaos](chaos-and-strange-attractors.md) appears near broken tori, through homoclinic tangles.

## Common misconceptions

- **"Conservative systems are predictable."**: most are not integrable, and their chaotic zones show sensitive dependence.
- **"Small perturbations destroy integrability completely."**: KAM theory shows most tori survive.
- **"The solar system is proved stable."**: KAM applies only to unrealistically small perturbations, and numerical evidence points to long-term chaos.

## Go deeper

- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (2nd edition, 1989): symplectic geometry, integrability and KAM theory.
- Jürgen Moser, *Stable and Random Motions in Dynamical Systems* (1973): small divisors and the horseshoe in celestial mechanics.
- Henri Poincaré, *Les méthodes nouvelles de la mécanique céleste* (1892–1899): the founding work on non-integrability.
