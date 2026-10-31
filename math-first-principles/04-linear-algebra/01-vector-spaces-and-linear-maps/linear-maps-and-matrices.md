# Linear Maps and Matrices

> **Layer:** [04 Linear Algebra](../README.md) › [Vector Spaces and Linear Maps](README.md)
> **Builds on:** [Linear independence, bases and dimension](linear-independence-bases-and-dimension.md), [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [Equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md)
> **Enables:** [Linear systems and rank–nullity](linear-systems-and-rank-nullity.md), [Eigenvalues and diagonalisation](../02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md), [The derivative as a linear map](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md), [Groups and subgroups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md), [Representations of finite groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md)

## Essence
A linear map is a function between vector spaces that respects addition and scalar multiplication: T(u + v) = Tu + Tv and T(av) = aTv. Once bases are chosen, every linear map between finite-dimensional spaces becomes a matrix, and composing maps becomes multiplying matrices. The matrix is a record of the map in particular coordinates, so a single map has many matrices, and the questions that matter are the ones whose answers do not depend on the coordinates. Linear maps are the structure-preserving maps of the subject, and nearly every object in mathematics that can be linearised is studied through them.

## Core tenets
1. **A linear map is fixed by its values on a basis, and those values are free.** If v₁, …, vₙ is a basis of V and w₁, …, wₙ are any vectors in W, there is exactly one linear T with Tvᵢ = wᵢ, namely T(a₁v₁ + ⋯ + aₙvₙ) = a₁w₁ + ⋯ + aₙwₙ. This one sentence is why bases are so powerful.

2. **The columns of a matrix are the images of the basis vectors.** With bases fixed in V (dimension n) and W (dimension m), T is recorded by the m × n matrix whose j-th column lists the coordinates of Tvⱼ. The space Hom(V, W) of all linear maps is therefore a vector space of dimension mn. Rotation of ℝ² by angle θ sends (1, 0) to (cos θ, sin θ) and (0, 1) to (−sin θ, cos θ), so its matrix, with rows listed in turn, is

   ```
   R(θ) = [[cos θ, −sin θ], [sin θ, cos θ]]
   ```

3. **Matrix multiplication is composition.** The rule (AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ is forced by requiring that the matrix of S ∘ T be the product of the matrices; associativity then comes free from associativity of composition. Order matters: rotating by 90° and then reflecting in the x-axis gives FR = [[0, −1], [−1, 0]], the reflection in the line y = −x, while the other order gives RF = [[0, 1], [1, 0]], the reflection in y = x. Multiplying R(α)R(β) = R(α + β) out yields the angle-addition formulas of trigonometry.

4. **Kernel and image measure failure of injectivity and surjectivity.** The kernel ker T = {v : Tv = 0} and image im T are subspaces; T is injective if and only if ker T = 0. The first isomorphism theorem holds: V/ker T ≅ im T, through v + ker T ↦ Tv. The same pattern recurs for groups and rings.

5. **Changing basis conjugates the matrix.** If P converts new coordinates in V to old ones and Q does so in W, the matrix of T in the new bases is Q⁻¹AP. For a map from V to itself one uses the same basis on both sides and gets P⁻¹AP; matrices related this way are similar. Quantities unchanged under similarity, such as the trace, the determinant and the eigenvalues, are properties of the map itself.

6. **Up to separate changes of basis, rank is everything.** Choosing a basis of V that extends one of ker T, and a basis of W that extends the images of the remaining vectors, puts the matrix in the form with r ones on the diagonal and zeros elsewhere, where r = dim im T is the rank. Two m × n matrices are equivalent under A ↦ Q⁻¹AP if and only if they have the same rank. Similarity is much finer; its classification is the [Jordan normal form](../02-determinants-and-eigenvalues/jordan-normal-form.md).

7. **The invertible maps form a group.** The invertible n × n matrices form the general linear group GL(n, F); inside it sit the orthogonal group O(n), which preserves lengths, and the special linear group SL(n, F) of determinant 1. Felix Klein's [Erlangen programme](../../08-geometry/01-classical-geometry/the-erlangen-programme.md) defines geometries by such groups, and [Lie theory](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md) studies them as smooth objects.

8. **In infinite dimension, injective and surjective come apart.** On ℝ[x], differentiation d/dx is surjective (every polynomial has an antiderivative) but not injective (constants die), while multiplication by x is injective but not surjective (nothing maps to 1). In finite dimension this cannot happen, by [rank–nullity](linear-systems-and-rank-nullity.md).

## Key concepts
| Term | Meaning |
|---|---|
| Linear map | Function with T(u + v) = Tu + Tv and T(av) = aTv |
| Matrix of T | Columns are coordinates of the images of basis vectors |
| Hom(V, W) | Vector space of all linear maps V → W |
| Kernel | Vectors sent to 0 |
| Image | Set of all outputs |
| Rank | Dimension of the image |
| Similar matrices | P⁻¹AP and A: one map seen in two bases |
| GL(n, F) | Group of invertible n × n matrices over F |

## How it fits
- **Below:** [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md) and [quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) give the vocabulary; [bases](linear-independence-bases-and-dimension.md) make maps into matrices.
- **Above:** [the derivative](../../06-real-analysis/03-calculus-of-several-variables/the-derivative-as-a-linear-map.md) is the best linear approximation of a smooth map; matrix groups are the first examples of [groups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md); a [representation](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md) is a group acting by linear maps.
- **Siblings:** [linear systems](linear-systems-and-rank-nullity.md) ask about Tx = b; the [transpose](dual-spaces.md) is a map between duals.

## Common misconceptions
- **"A matrix is a linear map."**: a matrix is a map together with a choice of bases. The same map has many matrices, and only the multiples of the identity look the same in every basis.
- **"AB = BA."**: rotations and reflections already fail to commute, as in tenet 3; even [[1, 1], [0, 1]] (rows listed in turn) and its transpose do not commute.
- **"A translation x ↦ x + b is linear."**: it moves 0, so it is affine, not linear. Graphics handles affine maps with an extra coordinate ([geometry and transformations](../../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md)).

## Go deeper
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): linear maps before matrices.
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): matrices as the working language.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (2nd edition, 1958): transformations as the primary objects.
