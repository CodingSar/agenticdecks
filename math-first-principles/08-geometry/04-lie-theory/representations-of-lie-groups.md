# Representations of Lie Groups

> **Layer:** [08 Geometry](../README.md) › [Lie Theory](README.md)
> **Builds on:** [Lie groups and Lie algebras](lie-groups-and-lie-algebras.md), [The classification of simple Lie algebras](the-classification-of-simple-lie-algebras.md), [Representations of finite groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md), [Compactness](../../07-topology/01-point-set-topology/compactness.md)
> **Enables:** [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md), [The Langlands programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md), [Qubits and quantum circuits](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md)

## Essence

A representation of a Lie group G is a smooth homomorphism from G to the invertible linear maps of a vector space: a way for the group to act linearly. Representations are how symmetry is used in practice, because linear actions can be decomposed, measured by traces and compared. For compact groups the theory mirrors that of [finite groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md): every representation splits into irreducible pieces, and the irreducibles are labelled by highest weights drawn from the root geometry of the [classification](the-classification-of-simple-lie-algebras.md). The smallest case, SU(2), already contains spin, the quantum property that makes a rotation by 2π act as −1.

## Core tenets

1. **Group representations become Lie algebra representations.** Differentiating a representation at the identity gives a linear action of the Lie algebra respecting brackets. For a simply connected group the correspondence is exact: every Lie algebra representation integrates to a group representation. For other groups only some do, which is the algebraic trace of the [covering](lie-groups-and-lie-algebras.md) SU(2) → SO(3).

2. **Compact groups have completely reducible representations.** A compact group carries a Haar measure, an invariant way to average, normalised to total mass 1. Averaging any inner product over the group gives an invariant one, so the representation is unitary, and the orthogonal complement of an invariant subspace is invariant. Repeating splits the representation into irreducibles. [Compactness](../../07-topology/01-point-set-topology/compactness.md) is essential: the group ℝ acting on ℝ² by the shear matrices [[1, t], [0, 1]] fixes the line through (1, 0) but no complementary line. Weyl's unitarian trick transfers complete reducibility to complex semisimple algebras through their compact real forms.

3. **The irreducible representations of sl(2) are one per dimension.** In the basis E, F, H with [H, E] = 2E, [H, F] = −2F and [E, F] = H, eigenvectors of H have integer eigenvalues called weights; E raises a weight by 2 and F lowers it by 2. Starting from a vector killed by E and applying F repeatedly gives, for each n ≥ 0, a unique irreducible Vₙ of dimension n + 1 with weights n, n − 2, …, −n. Concretely, Vₙ is the space of homogeneous polynomials of degree n in two variables.

4. **SU(2) gives spin, and SO(3) sees only half of it.** Every Vₙ lifts to SU(2), since SU(2) is simply connected. The element −I acts on Vₙ as (−1)ⁿ, so Vₙ descends to SO(3) only when n is even: the irreducible representations of SO(3) have odd dimension 2l + 1, and on the sphere they are the spherical harmonics. Physicists write j = n/2. For half-integer j, such as the spin-½ representation V₁ describing an electron or a [qubit](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md), a rotation through 2π acts as −1 and only 4π returns to the identity. Tensor products decompose by the Clebsch–Gordan rule: Vₘ ⊗ Vₙ is the sum of Vₖ for k = m + n, m + n − 2, …, ∣m − n∣.

5. **Highest weights classify irreducibles for every semisimple algebra.** For a complex semisimple Lie algebra, the Cartan subalgebra acts diagonalisably on any finite-dimensional representation, and its eigenvalue functionals are the weights. The theorem of the highest weight, due to Cartan (1913), says the irreducible representations correspond one-to-one with the dominant integral weights: those with non-negative integer pairing against each simple coroot. For sl(3) these are pairs (a, b) of non-negative integers.

6. **Weyl's character formula computes everything at once.** Weyl (1925 to 1926) gave the character, the trace of each group element, as a ratio of alternating sums over the Weyl group, and deduced a dimension formula. For sl(3) it reads

```
dim V(a, b) = (a + 1)(b + 1)(a + b + 2) / 2
```

   giving 3, 3, 8, 6, 10, …; the 8-dimensional adjoint representation organised hadrons in Gell-Mann's eightfold way.

7. **Peter–Weyl generalises Fourier series to compact groups.** Peter and Weyl (1927) showed that for a compact group the matrix entries of the irreducible unitary representations, suitably scaled, form an orthonormal basis of L²(G), with each irreducible occurring as often as its dimension. For the circle U(1) the irreducibles are the characters e^(inθ), and the theorem is the completeness of Fourier series; for SO(3) acting on the sphere it gives the spherical harmonic expansion. This is the starting point of [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md).

8. **Non-compact groups need infinite dimensions.** A connected non-compact simple group such as SL(2, ℝ) has no non-trivial finite-dimensional unitary representations, so its interesting unitary representations act on Hilbert spaces. Wigner (1939) classified the unitary irreducible representations of the Poincaré group, the symmetry group of special relativity, and identified elementary particles with them, labelled by mass and spin. The representation theory of such groups, developed by Harish-Chandra and others, underlies the [Langlands programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md).

## Key concepts

| Term | Meaning |
|---|---|
| Representation | A smooth homomorphism G → GL(V) |
| Irreducible | Having no invariant subspaces but zero and V |
| Haar measure | The invariant measure on a locally compact group; finite for compact groups |
| Weight | An eigenvalue functional of the Cartan subalgebra on a representation |
| Highest weight | The weight of a vector killed by all raising operators |
| Character | g ↦ tr ρ(g); determines a representation of a compact group |
| Spin | The label j = n/2 of the SU(2) representation Vₙ |
| Clebsch–Gordan rule | How a tensor product of SU(2) representations splits |
| Peter–Weyl theorem | Matrix coefficients give an orthonormal basis of L²(G) |

## How it fits

- **Below:** Lie algebras let representations be differentiated; finite-group theory supplies characters and Schur's lemma; compactness gives Haar averaging.
- **Above:** [Quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) represents symmetries on Hilbert space; spinors on curved spacetime in [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md) come from the double cover of the Lorentz group; [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md) turns the generators into conserved quantities.
- **Siblings:** [The classification](the-classification-of-simple-lie-algebras.md) supplies weights and the Weyl group; [Riemannian manifolds](../02-differential-geometry/riemannian-manifolds.md) give the Laplacian whose eigenspaces on symmetric spaces are representations.

## Common misconceptions

- **"A rotation by 2π is always the identity"**: On spin representations of SU(2) it acts as −1.
- **"Every representation splits into irreducibles"**: The shear action of ℝ does not; compactness or semisimplicity is needed.
- **"Unitary representations are finite-dimensional"**: For non-compact simple groups the non-trivial ones are all infinite-dimensional.

## Go deeper

- Bröcker and tom Dieck, *Representations of Compact Lie Groups* (1985): Haar measure, Peter–Weyl and characters.
- Sternberg, *Group Theory and Physics* (1994): representations as physicists use them.
- Weyl, *The Theory of Groups and Quantum Mechanics* (1928): the founder's own account of spin and symmetry.
