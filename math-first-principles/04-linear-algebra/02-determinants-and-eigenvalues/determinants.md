# Determinants

> **Layer:** [04 Linear Algebra](../README.md) › [Determinants and Eigenvalues](README.md)
> **Builds on:** [Linear maps and matrices](../01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [Linear systems and rank–nullity](../01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md), [Counting principles and binomial coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md)
> **Enables:** [Eigenvalues and diagonalisation](eigenvalues-and-diagonalisation.md), [Exterior algebra](../04-multilinear-algebra/exterior-algebra.md), [Multiple integrals and change of variables](../../06-real-analysis/04-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md), [Inverse and implicit function theorems](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md), [Homomorphisms and quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md)

## Essence
The determinant assigns to each square matrix a single number that says by what factor the corresponding linear map scales volume, with a sign recording whether orientation is reversed. It is characterised by three properties: it is linear in each column separately, it vanishes when two columns are equal, and it equals 1 on the identity. From this definition follow the product rule det(AB) = det A · det B and the criterion that a matrix is invertible exactly when its determinant is non-zero. The determinant is the gateway to eigenvalues, through the characteristic polynomial, and to the change-of-variables formula for integrals.

## Core tenets
1. **Every permutation has a sign.** A permutation σ of {1, …, n} is a bijection of that set to itself. Its sign is

   ```
   sgn σ = ∏ over i < j of (σ(j) − σ(i)) / (j − i)
   ```

   Each unordered pair {i, j} appears once in the numerator and once in the denominator, up to sign, so the product is ±1: it is −1 to the power of the number of inversions, pairs that σ puts out of order. The formula shows sgn(στ) = sgn σ · sgn τ, and a transposition, which swaps two elements, has sign −1.

2. **There is exactly one alternating multilinear form with det I = 1.** Call D a function of the n columns of a matrix that is linear in each column and zero when two columns coincide. Then swapping two columns changes the sign of D, since expanding D(…, u + v, …, u + v, …) = 0 leaves D(…, u, …, v, …) + D(…, v, …, u, …) = 0. Expanding each column in the standard basis and discarding terms with a repeated basis vector gives

   ```
   D(A) = D(I) · Σ over permutations σ of sgn σ · a_σ(1),1 · a_σ(2),2 ⋯ a_σ(n),n
   ```

   so D is determined by D(I), and the sum, called det A, is the unique such form with value 1 on I. For 2 × 2 matrices it is ad − bc.

3. **The determinant is signed volume.** The volume of the parallelepiped spanned by the columns is multiplied by c when one column is scaled by c, is unchanged by a shear (adding a multiple of one column to another, by Cavalieri's principle), and is 1 for the unit cube. These are the defining properties up to sign, so ∣det A∣ is that volume. When the columns are dependent the solid is flat, and both the volume and the determinant are 0.

4. **det(AB) = det A · det B.** Fix A and set D(x₁, …, xₙ) = det(Ax₁, …, Axₙ). It is alternating and multilinear, so D(B) = D(I) det B = det A · det B. So det is a homomorphism from the general linear group GL(n, F) of invertible matrices to the non-zero scalars, with kernel the special linear group SL(n, F), and det(P⁻¹AP) = det A: the determinant is a property of the map, not of the basis.

5. **A is invertible if and only if det A ≠ 0.** If A is invertible then det A · det A⁻¹ = det I = 1. If not, its columns are dependent, one column is a combination of the others, and multilinearity with the alternating property gives det A = 0. An integer matrix has an inverse with integer entries if and only if det A = ±1.

6. **Compute by elimination, not by the formula.** Transposing does not change the determinant, because σ and σ⁻¹ have the same sign, so rows behave like columns. Row operations change det in known ways (adding a multiple: no change; swapping: sign; scaling: factor), and a triangular matrix has determinant equal to the product of its diagonal. The permutation formula has n! terms, about 2.4 × 10¹⁸ for n = 20, while elimination needs a few thousand operations.

7. **Cramer's rule and the adjugate express the inverse.** Gabriel Cramer published the rule in 1750: if det A ≠ 0, the solution of Ax = b has xᵢ = det Aᵢ / det A, where Aᵢ has its i-th column replaced by b. Collecting cofactors gives A · adj A = (det A) I. These formulas matter in theory (the inverse depends smoothly on the entries) more than in computation.

8. **The determinant is the top exterior power.** An n-dimensional space has a one-dimensional space of alternating n-forms, and any linear map acts on it by multiplication by a single scalar, its determinant. This basis-free view is developed in [exterior algebra](../04-multilinear-algebra/exterior-algebra.md).

## Key concepts
| Term | Meaning |
|---|---|
| Permutation | Bijection of {1, …, n} to itself |
| Sign | ±1, multiplicative, −1 on a transposition |
| Multilinear | Linear in each argument separately |
| Alternating | Zero whenever two arguments coincide |
| Determinant | Unique alternating multilinear form on columns with det I = 1 |
| Orientation | Sign of the determinant: preserved or reversed |
| Cofactor | Signed determinant of a matrix with one row and column deleted |
| SL(n, F) | Matrices of determinant 1 |

## How it fits
- **Below:** [linear maps](../01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md) and [rank](../01-vector-spaces-and-linear-maps/linear-systems-and-rank-nullity.md) supply the objects; [counting](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md) supplies permutations.
- **Above:** the Jacobian determinant rescales volume in [change of variables](../../06-real-analysis/04-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md) and decides local invertibility in the [inverse function theorem](../../06-real-analysis/04-calculus-of-several-variables/inverse-and-implicit-function-theorems.md); det is the standard example of a [group homomorphism](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md).
- **Siblings:** det(λI − A) defines [eigenvalues](eigenvalues-and-diagonalisation.md); [exterior algebra](../04-multilinear-algebra/exterior-algebra.md) explains the determinant.

## Common misconceptions
- **"det(A + B) = det A + det B."**: the determinant is multiplicative, not additive: det(I + I) = 2ⁿ, not 2.
- **"A small determinant means nearly singular."**: det(εI) = εⁿ is tiny for small ε, yet εI is perfectly well conditioned. Closeness to singularity is measured by the smallest [singular value](../03-inner-product-spaces/singular-value-decomposition.md) relative to the largest.
- **"Determinants are how one solves linear systems."**: Cramer's rule is far slower than elimination for large n; determinants are for theory and for small cases.

## Go deeper
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): determinants defined through alternating forms.
- Kenneth Hoffman and Ray Kunze, *Linear Algebra* (2nd edition, 1971): the uniqueness theorem in full.
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): determinants as volumes, with computations.
