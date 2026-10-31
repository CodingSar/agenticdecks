# Symplectic Geometry

> **Layer:** [08 Geometry](../README.md) › [Differential Geometry](README.md)
> **Builds on:** [Differential forms and de Rham cohomology](differential-forms-and-de-rham-cohomology.md), [Vector bundles, connections and characteristic classes](vector-bundles-connections-and-characteristic-classes.md), [Riemannian manifolds](riemannian-manifolds.md), [Exterior algebra](../../04-linear-algebra/04-multilinear-algebra/exterior-algebra.md)
> **Enables:** [Hamiltonian systems and integrability](../../10-differential-equations-and-dynamics/04-dynamical-systems/hamiltonian-systems-and-integrability.md), [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

Riemannian geometry measures lengths with a symmetric form; symplectic geometry measures oriented areas with an antisymmetric one. A symplectic manifold carries a closed 2-form ω that is non-degenerate at every point, and it is the natural home of classical mechanics: phase space, positions paired with momenta, is symplectic, and every energy function generates a flow that preserves ω. Unlike a metric, a symplectic form has no local invariants, since Darboux's theorem makes all of them look alike near a point. Yet globally it is rigid in ways volume is not, as Gromov's non-squeezing theorem shows, and this mix of local flexibility and global rigidity defines the subject.

## Core tenets

1. **A symplectic vector space is even-dimensional, with a standard form.** A symplectic form on a real vector space V is a bilinear form ω that is antisymmetric and non-degenerate, an element of the [exterior algebra](../../04-linear-algebra/04-multilinear-algebra/exterior-algebra.md) Λ²V*. Its matrix Ω satisfies Ωᵀ = −Ω, so det Ω = (−1)^(dim V) det Ω, and non-degeneracy forces dim V to be even. Choosing vectors in pairs gives a basis q₁, …, qₙ, p₁, …, pₙ in which ω = Σ dpᵢ ∧ dqᵢ. Unlike an inner product, ω(v, v) = 0 for every v.

2. **A symplectic manifold has a closed non-degenerate 2-form, and its top power is a volume.** On a 2n-manifold M, a symplectic form is a [differential 2-form](differential-forms-and-de-rham-cohomology.md) ω with dω = 0 that is non-degenerate at each point. Then ωⁿ vanishes nowhere, so M is oriented, and on a closed M its class satisfies [ω]ⁿ ≠ 0 in de Rham cohomology. Hence H² is non-zero, and S⁴ has no symplectic form. Examples are any orientable surface with an area form, the complex projective spaces, and above all cotangent bundles.

3. **Cotangent bundles are phase spaces.** For a configuration space Q, the cotangent bundle T*Q, the [bundle](vector-bundles-connections-and-characteristic-classes.md) of covectors, has coordinates qᵢ for position and pᵢ for momentum. It carries a canonical 1-form θ = Σ pᵢ dqᵢ, defined without coordinates, and ω = dθ is symplectic. So mechanics on any configuration space comes with symplectic geometry built in, with no choices.

4. **Darboux's theorem: symplectic manifolds have no local invariants.** Near every point there are coordinates in which ω = Σ dpᵢ ∧ dqᵢ. Moser's proof joins ω to the standard form by the path ωₜ = ω₀ + t(ω₁ − ω₀), uses the Poincaré lemma to write ω₁ − ω₀ = dα, and solves for a flow carrying each ωₜ to ω₀; non-degeneracy makes the flow exist. Contrast [Riemannian manifolds](riemannian-manifolds.md), where curvature is a local invariant that no change of coordinates removes.

5. **Every function generates a flow that conserves it and preserves ω.** Non-degeneracy turns dH into a vector field X_H with ω(X_H, ·) = −dH; in Darboux coordinates its flow is Hamilton's equations q̇ = ∂H/∂p, ṗ = −∂H/∂q. Energy is conserved because dH(X_H) = −ω(X_H, X_H) = 0 by antisymmetry. The flow preserves ω because Cartan's formula gives the Lie derivative as −d(dH) plus a term in dω, both zero; this is where closedness is used. Preserving ωⁿ gives Liouville's theorem, conservation of phase-space volume.

6. **Poisson brackets and moment maps turn symmetries into conserved quantities.** The Poisson bracket {f, g} = ω(X_f, X_g) makes functions a Lie algebra, and f is conserved by the flow of H if and only if {f, H} = 0. When a [Lie group](../04-lie-theory/lie-groups-and-lie-algebras.md) acts preserving ω, a moment map assigns to each element of its Lie algebra a function generating that action; if H is invariant these functions are conserved. Rotations give angular momentum and translations linear momentum, the symplectic form of [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md).

7. **Global rigidity: non-squeezing and the Arnold conjecture.** Liouville's theorem allows a ball to be squeezed into a thin cylinder of the same volume, but Gromov's non-squeezing theorem (1985) says a ball of radius r embeds symplectically in B²(R) × ℝ²ⁿ⁻², a cylinder over a disc in one conjugate plane, only if r ≤ R. His proof used pseudoholomorphic curves, maps of Riemann surfaces into M. Arnold conjectured that a Hamiltonian diffeomorphism of a closed symplectic manifold, with non-degenerate fixed points, has at least as many fixed points as the sum of the Betti numbers, more than the Lefschetz fixed-point theorem forces; Floer proved it for large classes of manifolds by inventing Floer homology, and later work extended it.

## Key concepts

| Term | Meaning |
|---|---|
| Symplectic form | A closed 2-form, non-degenerate at every point |
| Darboux coordinates | Coordinates with ω = Σ dpᵢ ∧ dqᵢ |
| Cotangent bundle | T*Q, the phase space of a configuration space Q, with ω = dθ |
| Hamiltonian vector field | X_H with ω(X_H, ·) = −dH; its flow is Hamilton's equations |
| Symplectomorphism | A diffeomorphism preserving ω |
| Poisson bracket | {f, g} = ω(X_f, X_g); the Lie algebra of observables |
| Moment map | Functions generating a symmetry action; the conserved quantities |
| Lagrangian submanifold | A half-dimensional submanifold on which ω vanishes, such as the zero section of T*Q |

## How it fits

- **Below:** [Exterior algebra](../../04-linear-algebra/04-multilinear-algebra/exterior-algebra.md) supplies 2-forms, [differential forms](differential-forms-and-de-rham-cohomology.md) closedness and cohomology, and [vector bundles](vector-bundles-connections-and-characteristic-classes.md) the cotangent bundle.
- **Above:** [Hamiltonian systems](../../10-differential-equations-and-dynamics/04-dynamical-systems/hamiltonian-systems-and-integrability.md) are flows on symplectic manifolds; quantisation replaces Poisson brackets by commutators in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md).
- **Siblings:** [Riemannian geometry](riemannian-manifolds.md) is the symmetric counterpart, and a Kähler manifold carries both, compatibly; [Lie groups](../04-lie-theory/lie-groups-and-lie-algebras.md) act on symplectic manifolds through moment maps.

## Common misconceptions

- **"Symplectic maps are just volume-preserving maps"**: In dimension 2 they are the same, but in higher dimensions non-squeezing separates them.
- **"Every even-dimensional manifold is symplectic"**: A closed symplectic manifold needs a degree-2 class with non-zero top power, so S⁴ has none.
- **"Symplectic geometry has curvature, like Riemannian geometry"**: Darboux's theorem leaves no local invariants; all the information is global.

## Go deeper

- Arnold, *Mathematical Methods of Classical Mechanics* (1978): mechanics rebuilt on symplectic geometry.
- Cannas da Silva, *Lectures on Symplectic Geometry* (2001): a concise course from Darboux to moment maps.
- McDuff and Salamon, *Introduction to Symplectic Topology* (1995): the global theory, including non-squeezing.
