# Linear Systems and Rank–Nullity

> **Layer:** [04 Linear Algebra](../README.md) › [Vector Spaces and Linear Maps](README.md)
> **Builds on:** [Linear maps and matrices](linear-maps-and-matrices.md), [Linear independence, bases and dimension](linear-independence-bases-and-dimension.md), [Equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md)
> **Enables:** [Dual spaces](dual-spaces.md), [Numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md), [Error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md), [Homology](../../07-topology/02-algebraic-topology/homology.md), [Linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md)

## Essence
A system of m linear equations in n unknowns is a single equation Ax = b for an m × n matrix A. Whether it has a solution, and how many, is decided by two subspaces: the image of A, which says which right-hand sides are reachable, and the kernel, which says how much freedom the solutions have. The rank–nullity theorem ties them together: the dimension of the kernel plus the rank equals n. Gaussian elimination computes all of this, and its by-products, such as the equality of row rank and column rank, are some of the most used facts in mathematics.

## Core tenets
1. **The solution set is empty or a translate of the kernel.** If x₀ solves Ax = b, then x solves it if and only if A(x − x₀) = 0, so the solutions are exactly x₀ + ker A. A system has no solution, exactly one, or (over an infinite field) infinitely many; it never has exactly two.

2. **Rank–nullity: dim ker T + dim im T = dim V.** Take a basis u₁, …, uₖ of ker T and extend it to a basis of V by v₁, …, vᵣ. The images Tv₁, …, Tvᵣ span im T, since the u's contribute nothing, and they are independent, since a relation among them would put a combination of the v's into the kernel. So r = rank T and k + r = dim V. Equivalently, V/ker T ≅ im T has dimension dim V − dim ker T.

3. **Rank–nullity has immediate consequences.** A map between spaces of equal finite dimension is injective if and only if it is surjective; a square matrix with a left inverse has a right inverse. A system with more unknowns than equations, if solvable, has infinitely many solutions. When Ax = b has no solution one asks instead for the closest Ax, which is [least squares](../03-inner-product-spaces/inner-products-and-orthogonality.md).

4. **Gaussian elimination computes everything.** Adding a multiple of one equation to another, swapping equations and scaling by non-zero numbers do not change the solution set. Repeating these reduces A to echelon form, at a cost of about n³/3 multiplications for an n × n system; the method appears in the Chinese *Nine Chapters on the Mathematical Art*, compiled about two thousand years ago. For example:

   ```
   x + 2y +  z =  4             x + 2y + z = 4
   2x + 4y + 3z = 9      →              z = 1
   3x + 6y + 4z = 13                    z = 1
   ```

   y is free, and the solutions are (3, 0, 1) + y(−2, 1, 0): one particular solution plus a line of kernel. Changing 13 to 14 turns the last row into z = 2, contradicting z = 1, and the system has no solution.

5. **Row rank equals column rank.** Row operations do not change the row space, and they preserve linear relations among the columns, so they preserve the column rank. In echelon form both ranks equal the number of pivots. Hence the rank of A equals the rank of its transpose, a fact with a cleaner proof through [dual spaces](dual-spaces.md).

6. **The Fredholm alternative: either Ax = b is solvable or a certificate says it is not.** Exactly one of the following holds: Ax = b has a solution, or there is y with yᵀA = 0 and yᵀb ≠ 0. In the example above with 14, y = (1, 1, −1) gives yᵀA = 0 and yᵀb = −1: subtracting the third equation from the sum of the first two exposes 0 = −1. Farkas's lemma is the analogue for inequalities and underlies duality in [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md).

7. **The index n − m does not depend on A.** For any A from an n-dimensional space to an m-dimensional one, dim ker A − dim coker A = n − m, where the cokernel is the target modulo the image. This stable count is the seed of index theory, culminating in the Atiyah–Singer index theorem, and of the [Euler characteristic](../../07-topology/02-algebraic-topology/the-euler-characteristic.md) as an alternating sum of ranks in [homology](../../07-topology/02-algebraic-topology/homology.md).

8. **Codes are kernels.** Over ℤ/2, the Hamming code is the kernel of a 3 × 7 matrix H whose columns are the seven non-zero vectors of (ℤ/2)³. Rank–nullity gives a kernel of dimension 4, so 16 codewords. If one bit of a codeword x flips to give y, the syndrome Hy equals the column of H at that position, and so names the error ([error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md)).

## Key concepts
| Term | Meaning |
|---|---|
| Linear system | Ax = b for an m × n matrix A |
| Homogeneous system | Ax = 0; its solutions form ker A |
| Nullity | Dimension of the kernel |
| Rank | Dimension of the image; number of pivots |
| Echelon form | Staircase shape reached by row operations |
| Pivot | Leading non-zero entry of a row in echelon form |
| Cokernel | Target space modulo the image |
| Fredholm alternative | Solvable, or a y with yᵀA = 0 and yᵀb ≠ 0 exists |

## How it fits
- **Below:** [linear maps](linear-maps-and-matrices.md) give kernel and image; [bases](linear-independence-bases-and-dimension.md) give the extension argument; [quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) give the cokernel.
- **Above:** [numerical linear algebra](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-linear-algebra.md) makes elimination stable and fast; [homology](../../07-topology/02-algebraic-topology/homology.md) measures kernels modulo images; [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) replaces equations by inequalities.
- **Siblings:** the [dual space](dual-spaces.md) explains the Fredholm alternative; [determinants](../02-determinants-and-eigenvalues/determinants.md) test square systems for unique solvability.

## Common misconceptions
- **"n equations in n unknowns have exactly one solution."**: only when the matrix is invertible. x + y = 1 and 2x + 2y = 2 have infinitely many solutions; change the 2 to a 3 and there are none.
- **"To solve Ax = b, compute A⁻¹ and multiply."**: elimination solves the system directly. Forming the inverse costs about three times as much and is usually less accurate in floating point.
- **"A system with more equations than unknowns has no solution."**: it may be consistent if the equations are dependent; when it is not, least squares gives the best approximate answer.

## Go deeper
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): elimination and the four fundamental subspaces.
- Lloyd N. Trefethen and David Bau III, *Numerical Linear Algebra* (1997): what elimination costs and when it is stable.
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): rank–nullity as the fundamental theorem of linear maps.
