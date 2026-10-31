# Lie Groups and Lie Algebras

> **Layer:** [08 Geometry](../README.md) › [Lie Theory](README.md)
> **Builds on:** [Group actions](../../05-abstract-algebra/01-groups/group-actions.md), [Topological and smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md), [Inverse and implicit function theorems](../../06-real-analysis/03-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), [Covering spaces](../../07-topology/02-algebraic-topology/covering-spaces.md), [The Erlangen programme](../01-classical-geometry/the-erlangen-programme.md)
> **Enables:** [The classification of simple Lie algebras](the-classification-of-simple-lie-algebras.md), [Representations of Lie groups](representations-of-lie-groups.md), [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [Qubits and quantum circuits](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md)

## Essence

A Lie group is a group that is also a smooth manifold, with smooth multiplication and inversion: the rotations SO(3), the unitary matrices U(n), the Lorentz group. Sophus Lie's insight was that such a group is largely determined by its infinitesimal elements, the tangent vectors at the identity, which form a vector space with a bracket, the Lie algebra. The exponential map turns infinitesimal generators back into group elements, so questions about curved, non-linear groups become questions of linear algebra. The pair SU(2) and SO(3), which share a Lie algebra but differ globally, shows both the power and the limit of this linearisation.

## Core tenets

1. **Matrix groups defined by smooth equations are Lie groups.** GL(n, ℝ) is an open subset of all matrices, and subgroups cut out by equations, such as O(n) = {A : AᵀA = I} or SL(n, ℝ) = {det A = 1}, are smooth manifolds by the [implicit function theorem](../../06-real-analysis/03-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), because the defining map has full rank at the identity and hence, by translating, everywhere. More generally, Cartan's closed-subgroup theorem says every closed subgroup of a Lie group is a Lie group.

2. **The Lie algebra is the tangent space at the identity.** Differentiating a curve A(t) in the group with A(0) = I gives its Lie algebra. From AᵀA = I one gets Xᵀ + X = 0, so so(n) is the skew-symmetric matrices, of dimension n(n − 1)/2; since det e^X = e^(tr X), sl(n) is the trace-zero matrices. For SO(3), the three skew matrices are infinitesimal rotations about the three axes.

3. **The bracket measures the failure of the group to commute.** For matrices, [X, Y] = XY − YX. The group commutator of e^(tX) and e^(tY) is I + t²[X, Y] + O(t³), so the bracket is the second-order shadow of non-commutativity: the group is abelian near the identity if and only if the bracket vanishes. The Baker–Campbell–Hausdorff formula expresses log(e^X e^Y) as X + Y + ½[X, Y] + higher brackets, so the bracket determines the multiplication near the identity.

4. **The exponential map is a local diffeomorphism but need not be onto.** The map X ↦ e^X has derivative the identity at 0, so by the [inverse function theorem](../../06-real-analysis/03-calculus-of-several-variables/inverse-and-implicit-function-theorems.md) it maps a neighbourhood of 0 onto a neighbourhood of I, and those elements generate the identity component. For compact connected groups it is surjective, but not for SL(2, ℝ): the matrix diag(−2, −½) is not e^X for any X in sl(2, ℝ), because every such exponential has trace at least −2, with equality only at −I. For matrix groups e^(tX) solves the linear system of [the matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md).

5. **The Lie algebra determines the group up to coverings.** Every finite-dimensional real Lie algebra is the Lie algebra of exactly one simply connected Lie group, and every connected group with that algebra is its quotient by a discrete central subgroup, a [covering space](../../07-topology/02-algebraic-topology/covering-spaces.md). Homomorphisms of Lie algebras lift to homomorphisms of simply connected groups. Connectedness and global topology are invisible to the algebra: ℝ² and the torus have the same abelian Lie algebra.

6. **SU(2) is the double cover of SO(3).** SU(2) is the group of unit quaternions, topologically the 3-sphere S³. A unit quaternion q = cos(θ/2) + sin(θ/2)u, with u a unit imaginary quaternion, acts on imaginary quaternions by v ↦ qvq⁻¹ as rotation by θ about u. Both q and −q give the same rotation, so the map SU(2) → SO(3) is two-to-one; SO(3) is the projective space ℝP³ and its fundamental group is ℤ/2. Rotating an object through 2π is not contractible as a loop of rotations, but 4π is, as the belt trick shows. Quaternions are also how computer graphics interpolates rotations, and SU(2) is the group of single-[qubit](../../../cs-first-principles/02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md) gates up to phase.

7. **Groups act on their own Lie algebras, and symmetries give conservation laws.** Conjugation by g fixes the identity, so its derivative is a linear map Ad(g) of the Lie algebra: the adjoint representation, whose derivative is ad(X) = [X, ·]. Continuous symmetry groups of physical systems are Lie groups, and [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md) assigns a conserved quantity to each Lie algebra element: translations give momentum, rotations angular momentum, time translations energy.

## Key concepts

| Term | Meaning |
|---|---|
| Lie group | A group that is a smooth manifold with smooth operations |
| Lie algebra | A vector space with a bilinear, antisymmetric bracket satisfying the Jacobi identity |
| Exponential map | X ↦ e^X; the one-parameter subgroup with velocity X, at time 1 |
| One-parameter subgroup | A smooth homomorphism from ℝ into the group |
| so(n), su(n), sl(n) | Skew-symmetric, skew-Hermitian trace-zero, and trace-zero matrices |
| Baker–Campbell–Hausdorff formula | log(e^X e^Y) as a series of brackets |
| Universal cover | The simply connected group with a given Lie algebra |
| Adjoint representation | The action of the group on its Lie algebra by conjugation |
| Quaternions | ℍ, the four-dimensional division algebra; unit quaternions form SU(2) |

## How it fits

- **Below:** [Group actions](../../05-abstract-algebra/01-groups/group-actions.md) give the algebra, [smooth manifolds](../../07-topology/03-manifolds/topological-and-smooth-manifolds.md) the geometry, and covering spaces the global picture.
- **Above:** Conservation laws in mechanics, and symmetry in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), where SU(2) gives spin.
- **Siblings:** [The classification](the-classification-of-simple-lie-algebras.md) sorts the building-block algebras; [representations](representations-of-lie-groups.md) study how groups act linearly; [Riemannian manifolds](../02-differential-geometry/riemannian-manifolds.md) carry isometry groups that are Lie groups.

## Common misconceptions

- **"The Lie algebra determines the group"**: Only up to coverings and components; SU(2) and SO(3) share one.
- **"Every group element is an exponential"**: True for compact connected groups, false for SL(2, ℝ).
- **"Lie groups are always matrix groups"**: Most familiar ones are, but the universal cover of SL(2, ℝ) has no faithful finite-dimensional representation.

## Go deeper

- Stillwell, *Naive Lie Theory* (2008): matrix groups and quaternions with minimal prerequisites.
- Hall, *Lie Groups, Lie Algebras, and Representations* (2003): matrix Lie groups done properly.
- Needham's and Baez's expositions aside, the classic is Chevalley, *Theory of Lie Groups* (1946): the first modern global treatment.
