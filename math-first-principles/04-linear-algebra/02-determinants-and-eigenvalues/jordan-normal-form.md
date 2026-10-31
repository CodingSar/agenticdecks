# Jordan Normal Form

> **Layer:** [04 Linear Algebra](../README.md) › [Determinants and Eigenvalues](README.md)
> **Builds on:** [Eigenvalues and diagonalisation](eigenvalues-and-diagonalisation.md), [Linear systems and rank–nullity](../01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Divisibility and the Euclidean algorithm](../../02-number-systems/02-elementary-number-theory/divisibility-and-the-euclidean-algorithm.md)
> **Enables:** [Modules](../../05-abstract-algebra/04-modules-and-representations/modules.md), [Polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md), [Linear systems and the matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md), [Numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md)

## Essence
Not every matrix can be diagonalised, but over an algebraically closed field such as ℂ every matrix is similar to one that is almost diagonal: eigenvalues on the diagonal, some ones just above it, zeros everywhere else. This Jordan normal form, published by Camille Jordan in 1870, is unique up to the order of its blocks, so it completely classifies linear maps from a finite-dimensional space to itself up to change of basis. Along the way come the minimal polynomial, which detects diagonalisability, and the Cayley–Hamilton theorem, which says every matrix satisfies its own characteristic polynomial.

## Core tenets
1. **Every complex matrix is similar to a direct sum of Jordan blocks.** A Jordan block of size k with eigenvalue λ is

   ```
   J_k(λ) = λ on the diagonal, 1 just above it, 0 elsewhere
   J_3(λ) = [[λ, 1, 0], [0, λ, 1], [0, 0, λ]]   (rows listed in turn)
   ```

   The theorem says A = PJP⁻¹ with J block diagonal, and the multiset of blocks is determined by A. Diagonalisable means every block has size 1.

2. **The hypothesis is that the field is algebraically closed.** A field is algebraically closed when every non-constant polynomial over it has a root; ℂ is, ℝ and ℚ are not. The theorem works over any field in which the characteristic polynomial splits into linear factors. Without that, the rational canonical form built from companion matrices replaces it. Behind both lies one idea: V becomes a module over the polynomial ring F[t], with t acting as T, and a canonical form is a decomposition of that module.

3. **The minimal polynomial detects diagonalisability.** The n² + 1 matrices I, A, A², …, A^(n²) are dependent in the n²-dimensional space of matrices, so some non-zero polynomial kills A. The monic one of least degree, m(t), divides every polynomial p with p(A) = 0, by division with remainder. A is diagonalisable if and only if m has distinct linear factors only. The shear [[1, 1], [0, 1]] has m(t) = (t − 1)², so it is not diagonalisable; the identity has m(t) = t − 1.

4. **Cayley–Hamilton: every matrix satisfies its characteristic polynomial.** Over ℂ choose a basis v₁, …, vₙ making A upper triangular with diagonal λ₁, …, λₙ. Then (A − λ₁I)⋯(A − λₖI) kills v₁, …, vₖ, by induction on k, and at k = n it kills everything. So χ(A) = 0 and m divides χ. The identity holds over every commutative ring, since it is a polynomial identity in the entries. Arthur Cayley stated it in 1858, checking small cases, and Ferdinand Georg Frobenius gave a general proof in 1878.

5. **The space splits into generalised eigenspaces.** Factor χ(t) = (t − λ₁)^(a₁)⋯(t − λₛ)^(aₛ) with distinct λᵢ. Because the factors have no common root, Bézout's identity for polynomials gives polynomials summing to 1 that act as projections, and V = V₁ ⊕ ⋯ ⊕ Vₛ with Vᵢ = ker(A − λᵢI)^(aᵢ). On each Vᵢ, A − λᵢI is nilpotent: some power is zero.

6. **Nilpotent maps decompose into chains, and the block sizes are forced.** A nilpotent N has a basis of chains v, Nv, …, N^(k−1)v with Nᵏv = 0, each giving one block. The number of blocks of size at least k equals dim ker Nᵏ − dim ker N^(k−1), which depends only on N; this proves uniqueness. For example J₂(0) ⊕ J₂(0) and J₂(0) ⊕ J₁(0) ⊕ J₁(0) are both 4 × 4, square to zero and have the same characteristic and minimal polynomials, t⁴ and t², but have rank 2 and 1, so they are not similar.

7. **The Jordan form explains repeated roots in differential equations.** e^(tJ_k(λ)) = e^(λt) times a matrix whose entries are tʲ/j!. So y'' − 2y' + y = 0, with double root r = 1, has solutions eᵗ and teᵗ: the factor t is a Jordan block of size 2 at work. It also shows that x' = Ax decays when all eigenvalues have negative real part, because polynomials lose to exponentials.

8. **The Jordan form is exact but numerically fragile.** [[0, 1], [ε, 0]] (rows listed in turn) is diagonalisable with eigenvalues ±√ε for every ε > 0, but at ε = 0 it is a single block. An arbitrarily small change can change the form, so [numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md) prefers the Schur form: A = U T U∗ with U unitary and T upper triangular, which is stable to compute. Algebraically, the theorem is the structure theorem for [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md) over F[t].

## Key concepts
| Term | Meaning |
|---|---|
| Jordan block | λ on the diagonal, ones just above it |
| Jordan normal form | Block-diagonal J similar to A; unique up to block order |
| Algebraically closed field | Every non-constant polynomial has a root |
| Minimal polynomial | Monic polynomial of least degree with m(A) = 0 |
| Cayley–Hamilton theorem | χ(A) = 0 |
| Generalised eigenspace | ker(A − λI)ᵏ for large k |
| Nilpotent | Some power is the zero map |
| Rational canonical form | Companion-matrix blocks; works over every field |

## How it fits
- **Below:** [eigenvalues](eigenvalues-and-diagonalisation.md) give the diagonal; [rank–nullity](../01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) counts blocks; [the Euclidean algorithm](../../02-number-systems/02-elementary-number-theory/divisibility-and-the-euclidean-algorithm.md) for polynomials gives Bézout's identity.
- **Above:** [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md) over [polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md) give the general proof; [the matrix exponential](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/linear-systems-and-the-matrix-exponential.md) is computed from it.
- **Siblings:** [determinants](determinants.md) give χ; the Perron root of an irreducible non-negative matrix has a block of size 1 ([Perron–Frobenius](non-negative-matrices-and-perron-frobenius.md)).

## Common misconceptions
- **"Cayley–Hamilton is trivial: substitute A for λ in det(λI − A)."**: the substitution is illegitimate, since χ(A) is a matrix and det(AI − A) = det 0 is a number. The same trick would "prove" that tr(tI − A) vanishes at t = A, which is false.
- **"Characteristic and minimal polynomials determine a matrix up to similarity."**: true for n ≤ 3, false from n = 4 on, as tenet 6 shows.

## Go deeper
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (2nd edition, 1971): the rational and Jordan forms through polynomials.
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): generalised eigenvectors and the Jordan form.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (1985): Jordan and Schur forms side by side.
