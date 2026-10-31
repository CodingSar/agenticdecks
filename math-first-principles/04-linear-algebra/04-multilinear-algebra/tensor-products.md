# Tensor Products

> **Layer:** [04 Linear Algebra](../README.md) › [Multilinear Algebra](README.md)
> **Builds on:** [Dual spaces](../01-vector-spaces-and-linear-maps/dual-spaces.md), [Linear maps and matrices](../01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [Linear independence, bases and dimension](../01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md), [Equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md)
> **Enables:** [Exterior algebra](exterior-algebra.md), [Universal properties and adjunctions](../../13-structure-and-metamathematics/01-category-theory/universal-properties-and-adjunctions.md), [The mathematics of quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [Differential forms and de Rham cohomology](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md), [The geometry of general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md)

## Essence
The tensor product V ⊗ W is the space that turns bilinear maps into linear ones. A bilinear map, such as the dot product or matrix multiplication, is linear in each argument separately but not linear on the pair; the tensor product is built so that bilinear maps out of V × W correspond exactly to linear maps out of V ⊗ W. It is defined by this universal property, which pins it down up to unique isomorphism, and only then constructed. Tensors describe stress in materials, curvature of spacetime, states of several quantum particles and the multi-way arrays of data science, and their rank governs the cost of multiplying matrices.

## Core tenets
1. **The tensor product is defined by a universal property.** A tensor product of V and W is a vector space V ⊗ W with a bilinear map ⊗: V × W → V ⊗ W such that for every bilinear B: V × W → U there is exactly one linear L: V ⊗ W → U with B(v, w) = L(v ⊗ w).

   ```
   V × W ──⊗──▶ V ⊗ W
        \          │
       B \         │ L (unique, linear)
          ▼        ▼
              U
   ```

   Any two such spaces are isomorphic by a unique map compatible with ⊗, since each factors through the other. So it does not matter how it is built.

2. **It exists: take all formal sums and impose bilinearity.** Start from the vector space with a basis indexed by all pairs (v, w), and take the quotient by the subspace spanned by the relations (v + v', w) − (v, w) − (v', w), (av, w) − a(v, w), and the same in the second slot. The image of (v, w) is v ⊗ w, and the universal property holds because B kills exactly these relations.

3. **Bases multiply, so dimensions multiply.** If e₁, …, eₘ and f₁, …, fₙ are bases, the eᵢ ⊗ fⱼ form a basis of V ⊗ W, which has dimension mn, not m + n. For column vectors, v ⊗ w can be identified with the outer product vwᵀ, an m × n matrix of rank at most 1, and every element of V ⊗ W is a sum of such matrices.

4. **Not every tensor is a simple tensor: this is entanglement.** Elements of the form v ⊗ w are called simple or pure. A general element needs a sum, and the least number of simple terms is its rank. For two qubits, with state space ℂ² ⊗ ℂ², the Bell state (e₀ ⊗ e₀ + e₁ ⊗ e₁)/√2 corresponds to the matrix I/√2 of rank 2, so it cannot be written as one product: the two particles are entangled. The state space of a composite quantum system is the tensor product of the parts ([quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)).

5. **Linear maps are tensors.** In finite dimension the map V∗ ⊗ W → Hom(V, W) sending φ ⊗ w to the map v ↦ φ(v)w is an isomorphism, natural in V and W. Under it the trace of a map from V to itself is the contraction V∗ ⊗ V → F sending φ ⊗ v to φ(v), which explains why the trace does not depend on the basis.

6. **Tensors of type (p, q) are the objects of geometry and physics.** A tensor of type (p, q) on V is an element of V ⊗ ⋯ ⊗ V ⊗ V∗ ⊗ ⋯ ⊗ V∗ with p factors V and q factors V∗. Vectors are (1, 0), functionals (0, 1), linear maps (1, 1), inner products and quadratic forms (0, 2). Physicists' rules for raising and lowering indices are the [dual-space](../01-vector-spaces-and-linear-maps/dual-spaces.md) transformations applied to each factor.

7. **Tensor rank is subtle and controls fast matrix multiplication.** For tensors with three or more factors, rank behaves badly: the tensor a ⊗ a ⊗ b + a ⊗ b ⊗ a + b ⊗ a ⊗ a, with a and b independent, has rank 3 but is a limit of tensors of rank 2, so the set of tensors of rank at most 2 is not closed (Vin de Silva and Lek-Heng Lim, 2008). Matrix multiplication is a tensor, and Volker Strassen showed in 1969 that 2 × 2 matrices can be multiplied with 7 multiplications rather than 8, giving an algorithm with about n^2.81 operations. The best known exponent is now about 2.37; whether the exponent can be brought arbitrarily close to 2 is open as of 2026.

8. **Tensor products build new spaces from old.** Tensoring a real space with ℂ over ℝ gives its complexification. The tensor algebra, the direct sum of all V ⊗ ⋯ ⊗ V, has the symmetric algebra (polynomials) and the [exterior algebra](exterior-algebra.md) as quotients. Over rings the construction still works but can collapse: ℤ/2 ⊗ ℤ/3 = 0 over ℤ, since 1 ⊗ 1 = 3(1 ⊗ 1) − 2(1 ⊗ 1) = 1 ⊗ 3 − 2 ⊗ 1 = 0.

## Key concepts
| Term | Meaning |
|---|---|
| Bilinear map | Linear in each argument separately |
| Tensor product V ⊗ W | Universal target for bilinear maps out of V × W |
| Simple tensor | An element of the form v ⊗ w |
| Tensor rank | Least number of simple tensors summing to a given one |
| Contraction | Pairing a V∗ factor with a V factor |
| Type (p, q) | p copies of V and q copies of V∗ |
| Entanglement | A quantum state that is not a simple tensor |
| Tensor algebra | Direct sum of all tensor powers of V |

## How it fits
- **Below:** [dual spaces](../01-vector-spaces-and-linear-maps/dual-spaces.md) give the V∗ factors; [quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) give the construction; [bases](../01-vector-spaces-and-linear-maps/linear-independence-bases-and-dimension.md) give the dimension.
- **Above:** the [universal property](../../13-structure-and-metamathematics/01-category-theory/universal-properties-and-adjunctions.md) says − ⊗ W is left adjoint to Hom(W, −); tensor fields on manifolds lead to [differential forms](../../08-geometry/02-differential-geometry/differential-forms-and-de-rham-cohomology.md) and the curvature tensor of [general relativity](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md); tensor products of [representations](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md) are again representations.
- **Siblings:** the [exterior algebra](exterior-algebra.md) is a quotient of the tensor algebra.

## Common misconceptions
- **"A tensor is a multi-dimensional array."**: an array is a tensor's coordinates in chosen bases. What makes it a tensor is how those coordinates change when the bases change.
- **"V ⊗ W is the same as V × W."**: V × W has dimension m + n and V ⊗ W has dimension mn; the map (v, w) ↦ v ⊗ w is bilinear, not linear, and its image is not even a subspace.
- **"Every tensor is a product v ⊗ w."**: only the rank-one tensors are; entangled states and most matrices are sums.

## Go deeper
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (2nd edition, 1958): tensor products of finite-dimensional spaces.
- Serge Lang, *Algebra* (revised 3rd edition, 2002): tensor products of modules and the universal property.
- J. M. Landsberg, *Tensors: Geometry and Applications* (2012): tensor rank and matrix multiplication.
