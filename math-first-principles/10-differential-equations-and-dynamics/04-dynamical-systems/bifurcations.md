# Bifurcations

> **Layer:** [10 Differential Equations and Dynamics](../README.md) › [Dynamical Systems](README.md)
> **Builds on:** [Stability and phase portraits](../01-ordinary-differential-equations/stability-and-phase-portraits.md), [Iterated maps](iterated-maps.md), [Inverse and implicit function theorems](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md)
> **Enables:** [Chaos and strange attractors](chaos-and-strange-attractors.md), [Mathematical biology and epidemics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md), [Control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md), [Nonlinear dynamics, oscillations and networks](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md)

## Essence

A bifurcation is a qualitative change in a system's behaviour as a parameter passes a critical value: equilibria appear or vanish, exchange stability, or give way to oscillation. Such changes can happen only where hyperbolicity fails, and near them a system of any dimension reduces to a few one- or two-variable normal forms. That small catalogue explains tipping points, switches with memory, the onset of epidemics and the birth of rhythms such as a heartbeat, which is why the same pictures recur in ecology, engineering and physiology.

## Core tenets

1. **Nothing happens at a hyperbolic equilibrium.** For x′ = f(x, μ) with f(x*, μ₀) = 0, if the Jacobian matrix of f in x is invertible there, the implicit function theorem gives a unique smooth branch of equilibria x*(μ) near μ₀; if no eigenvalue lies on the imaginary axis, hyperbolicity persists and the local portrait stays the same. A bifurcation therefore needs an eigenvalue crossing the imaginary axis: a zero eigenvalue, or a complex pair ±iω. For maps the boundary is the unit circle, crossed at 1, at −1 (period doubling) or by a complex pair.

2. **Saddle-node: equilibria are born and die in pairs.** The normal form x′ = μ − x² has equilibria ±√μ for μ > 0, one stable and one unstable; they merge at μ = 0 and vanish for μ < 0. Every one-parameter family with a simple zero eigenvalue and non-zero quadratic term looks like this. After the collision a ghost remains: trajectories crawl through the bottleneck, taking time about π/√|μ|.

3. **Constraints and symmetry change the generic picture.** If an equilibrium must exist for every μ, as an empty population does, the generic case is transcritical, x′ = μx − x², where two branches cross and exchange stability; an epidemic takes off when the reproduction number passes 1 in exactly this way. A symmetry x ↦ −x gives the pitchfork x′ = μx − x³: zero loses stability and two stable branches ±√μ appear. In the subcritical pitchfork x′ = μx + x³ unstable branches close in, and at μ = 0 the state leaves for distant parts. A small imperfection h, as in x′ = h + μx − x³, breaks the pitchfork apart.

4. **Hysteresis: tipping points with memory.** The equation x′ = μ + x − x³ has three equilibria, two stable and one unstable, when |μ| < 2/(3√3) ≈ 0.385, and one otherwise. Raising μ past 0.385 destroys the lower stable branch in a saddle-node and the state jumps to the upper one; lowering μ again does not bring it back until μ passes −0.385. Near the fold the eigenvalue tends to 0, so recovery from small disturbances slows: critical slowing down, studied as an early warning of a tipping point.

5. **Hopf bifurcation: oscillations are born.** When a complex pair of eigenvalues crosses the imaginary axis, the dynamics reduce in polar coordinates to r′ = μr + ℓr³ and θ′ ≈ ω, where ℓ is a computable coefficient. If ℓ < 0 (supercritical), a stable limit cycle of radius √(μ/|ℓ|) appears for μ > 0, so amplitude grows like √μ at frequency near ω. If ℓ > 0 (subcritical), an unstable cycle shrinks onto the equilibrium and the system jumps to a large oscillation. Hopf (1942) proved the theorem in every dimension. Example: x″ − (μ − x²)·x′ + x = 0 has eigenvalues with real part μ/2 and a limit cycle of amplitude close to 2√μ for small μ > 0.

6. **Centre manifolds reduce dimension; codimension counts parameters.** Near a bifurcation the strongly stable directions are enslaved to an invariant centre manifold tangent to the critical eigenvectors, and the bifurcation happens on it, so one- and two-dimensional normal forms serve systems of any dimension. The codimension of a bifurcation is the number of parameters needed to meet it generically: saddle-node and Hopf have codimension one and are seen in every one-parameter family, while a pitchfork needs symmetry or tuning. Global bifurcations, such as a limit cycle colliding with a saddle, involve whole orbits and are invisible to local analysis.

## Key concepts

| Term | Meaning |
|---|---|
| Bifurcation | A qualitative change of the phase portrait as a parameter passes a critical value |
| Normal form | The simplest equation exhibiting a bifurcation, to which generic cases reduce |
| Saddle-node | Two equilibria colliding and vanishing, as in x′ = μ − x² |
| Pitchfork | One equilibrium splitting into three under a symmetry, as in x′ = μx − x³ |
| Hopf bifurcation | Birth of a limit cycle as a complex pair of eigenvalues crosses the imaginary axis |
| Hysteresis | Dependence of the state on the history of the parameter, not only its value |
| Centre manifold | An invariant manifold tangent to the eigenvectors whose eigenvalues lie on the imaginary axis |
| Codimension | The number of parameters needed to meet a bifurcation generically |

## How it fits

- **Below:** the [implicit function theorem](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md) says when nothing happens, [Taylor expansion](../../06-real-analysis/02-calculus-of-one-variable/taylor-expansion.md) produces the normal forms, [stability theory](../01-ordinary-differential-equations/stability-and-phase-portraits.md) supplies hyperbolicity, and [iterated maps](iterated-maps.md) supply period doubling.
- **Above:** epidemic thresholds and biological switches in [mathematical biology](../../14-applied-and-computational-mathematics/04-mathematical-modelling/mathematical-biology-and-epidemics.md); feedback in [control theory](../../14-applied-and-computational-mathematics/04-mathematical-modelling/control-theory.md) keeps eigenvalues away from the imaginary axis; nerve firing and cardiac rhythms in medicine's [nonlinear dynamics](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/03-systems-and-models/nonlinear-dynamics-oscillations-and-networks.md) begin at Hopf bifurcations.
- **Siblings:** cascades of bifurcations lead into [chaos](chaos-and-strange-attractors.md); [Hamiltonian systems](hamiltonian-systems-and-integrability.md) have no attractors and bifurcate differently.

## Common misconceptions

- **"Small changes in a parameter cause small changes in behaviour."**: at a fold an arbitrarily small change causes a jump, and hysteresis means reversing it may not undo the jump.
- **"Loss of stability is always gradual."**: supercritical bifurcations are gentle, but subcritical ones jump straight to large amplitude.
- **"Bifurcation theory needs special models."**: the normal forms are generic, so they describe any smooth system near a codimension-one event.

## Go deeper

- Steven H. Strogatz, *Nonlinear Dynamics and Chaos* (2nd edition): bifurcations in one and two dimensions with many applications.
- John Guckenheimer and Philip Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields* (1983): centre manifolds, normal forms and global bifurcations.
- Yuri A. Kuznetsov, *Elements of Applied Bifurcation Theory* (3rd edition, 2004): the systematic catalogue, with computational methods.
