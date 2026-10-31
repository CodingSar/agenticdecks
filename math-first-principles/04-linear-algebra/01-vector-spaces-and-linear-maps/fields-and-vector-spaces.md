# Fields and Vector Spaces

> **Layer:** [04 Linear Algebra](../README.md) › [Vector Spaces and Linear Maps](README.md)
> **Builds on:** [Axioms, definitions and theorems](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md), [Equivalence relations and quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [The complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md), [Modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md)
> **Enables:** [Linear independence, bases and dimension](linear-independence-bases-and-dimension.md), [Modules](../../05-abstract-algebra/04-modules-and-representations/modules.md), [Field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md), [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), [Error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md)

## Essence
A vector space is a set whose elements can be added and multiplied by scalars, subject to the familiar rules of arithmetic. The scalars come from a field, a number system in which one can add, subtract, multiply and divide by anything non-zero. Arrows in the plane, polynomials, solutions of a linear differential equation, sound signals and strings of bits are all vector spaces, so one theory covers them all. Linear algebra is the study of these spaces and the maps between them; this leaf fixes the rules of the game.

## Core tenets
1. **A field is a number system with all four operations.** A field F is a set with addition and multiplication, both associative and commutative, with 0 and 1 (0 ≠ 1), additive inverses, inverses of non-zero elements, and multiplication distributing over addition. ℚ, ℝ and ℂ are fields; ℤ is not, since 2 has no inverse. The integers modulo n, ℤ/n, form a field if and only if n is prime: if p is prime and a is not divisible by p, Bézout gives ax + py = 1, so x inverts a; if n = ab with 1 < a, b < n, then ab = 0 and a cannot be invertible. In ℤ/2 one has 1 + 1 = 0, which is why the field must always be named.

2. **A vector space is defined by axioms, not by pictures.** A vector space over F is a set V with an addition making it an abelian group (associative, commutative, with a zero vector and negatives) and a scalar multiplication F × V → V satisfying a(u + v) = au + av, (a + b)v = av + bv, (ab)v = a(bv) and 1v = v. Consequences follow by short proofs: 0v = (0 + 0)v = 0v + 0v forces 0v = 0, and v + (−1)v = (1 − 1)v = 0 shows (−1)v = −v. Giuseppe Peano stated essentially these axioms in 1888, though they were widely used only decades later.

3. **The examples are wildly varied.** Fⁿ, the n-tuples with entrywise operations; the polynomials F[x]; all functions from a set to F; m × n matrices; the solutions of y'' + y = 0. ℂ is a vector space over ℝ (of dimension 2), and ℝ is one over ℚ, of infinite dimension, because a countable set of reals spans only countably many reals over ℚ. The bit strings (ℤ/2)ⁿ, with exclusive or as addition, are the setting of coding theory.

4. **Subspaces are the subsets closed under the operations.** A subset U is a subspace when it contains 0 and is closed under addition and scalar multiplication. Lines and planes through the origin in ℝ³ are subspaces; the union of the two coordinate axes in ℝ² is not, since (1, 0) + (0, 1) leaves it. The span of a set S, all finite linear combinations a₁s₁ + ⋯ + aₖsₖ, is the smallest subspace containing S.

5. **Linearity is superposition.** The solution set of a homogeneous linear equation is a subspace, so sums and multiples of solutions are solutions. An inhomogeneous equation has as solutions one particular solution plus the homogeneous ones: y'' + y = 1 is solved exactly by 1 + a cos x + b sin x. This single fact organises linear differential equations, linear circuits and wave physics.

6. **Quotients collapse a subspace to zero.** For a subspace U of V, the cosets v + U partition V, and they form a vector space V/U with (v + U) + (w + U) = (v + w) + U. Collapsing the x-axis in ℝ² leaves one coordinate, so ℝ²/(x-axis) behaves like ℝ. The same construction gives quotient groups and, later, homology.

7. **Scalars can be cancelled because the field divides.** If av = 0 with a ≠ 0, multiplying by a⁻¹ gives v = 0. Over a ring this fails: in ℤ/6 viewed over ℤ, 6 · 1 = 0, and no set of elements is independent. That is why the theory of [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md) is harder, and why a vector space always has a basis.

## Key concepts
| Term | Meaning |
|---|---|
| Field | Set with +, ×, inverses for all non-zero elements; ℚ, ℝ, ℂ, ℤ/p |
| Characteristic | Least n with 1 + ⋯ + 1 (n times) = 0, or 0 if none; p for ℤ/p |
| Vector space | Abelian group with scalar multiplication obeying the distributive laws |
| Linear combination | Finite sum a₁v₁ + ⋯ + aₖvₖ |
| Subspace | Subset containing 0 and closed under both operations |
| Span | Set of all linear combinations; smallest subspace containing the set |
| Coset | Translate v + U of a subspace |
| Quotient space | V/U, the cosets of U with the induced operations |

## How it fits
- **Below:** [the axiomatic method](../../00-logic-and-proof/03-the-axiomatic-method/axioms-definitions-and-theorems.md) supplies the style, [equivalence relations](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) the quotient, and [modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md) the finite fields ℤ/p.
- **Above:** [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md) replace the field by a ring; [field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md) view one field as a vector space over another; [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md) add a norm to infinite-dimensional spaces; [error-correcting codes](../../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/error-correcting-codes.md) are subspaces of (ℤ/2)ⁿ.
- **Siblings:** [bases and dimension](linear-independence-bases-and-dimension.md) measure these spaces; [linear maps](linear-maps-and-matrices.md) connect them.

## Common misconceptions
- **"A vector is an arrow with a length and a direction."**: arrows are one model. A polynomial or a bit string is a vector, and a general vector space has no notion of length at all until an [inner product](../03-inner-product-spaces/inner-products-and-orthogonality.md) is added.
- **"Closure under addition is enough for a subspace."**: the integer points ℤ² are closed under addition and negation but not under multiplication by 1/2, so they are not a subspace of ℝ².
- **"The field does not matter."**: over ℤ/2, v + v = 0 for every v, and the rotation of the plane by 90° has eigenvalues over ℂ but none over ℝ.

## Go deeper
- Sheldon Axler, *Linear Algebra Done Right* (4th edition, 2024): an axiomatic, determinant-light development.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (2nd edition, 1958): the classic written with infinite dimension in view.
- Gilbert Strang, *Introduction to Linear Algebra* (6th edition, 2023): the matrix-first route with many applications.
