# Representations of Finite Groups

> **Layer:** [05 Abstract Algebra](../README.md) › [Modules and Representations](README.md)
> **Builds on:** [Modules](modules.md), [Group Actions](../01-groups/group-actions.md), [Inner Products and Orthogonality](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md), [Eigenvalues and Diagonalisation](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md)
> **Enables:** [Fourier Analysis on Groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md), [Representations of Lie Groups](../../08-geometry/04-lie-theory/representations-of-lie-groups.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [The Langlands Programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md)

## Essence

A representation of a group G is a way for G to act by invertible linear maps on a vector space: a homomorphism ρ from G to the group GL(V) of invertible linear maps. It turns abstract symmetry into matrices, where linear algebra can work on it. Over the complex numbers, for a finite group, the theory is complete and beautiful. Every representation splits into irreducible pieces (Maschke's theorem), maps between irreducibles are almost trivial (Schur's lemma), and each representation is determined by its character, the function sending g to the trace of ρ(g). The irreducible characters are orthonormal, and the character table of a group, a small square array of numbers, encodes much of its structure. Frobenius created the theory in 1896.

## Core tenets

1. **A representation is a module over the group algebra.** The group algebra ℂ[G] consists of formal combinations ∑ a_g·g, multiplied using the group law. A representation ρ makes V a ℂ[G]-module by (∑ a_g·g)·v = ∑ a_g·ρ(g)v, and conversely. Examples: the trivial representation, every g acting as 1; the sign representation of Sₙ; any action on a set X, which permutes the basis of ℂ^X; and the regular representation, G acting on ℂ[G] itself.

2. **Maschke's theorem: if the characteristic of the field does not divide ∣G∣, every subrepresentation W of V has an invariant complement.** Take any linear projection π of V onto W and average it over the group.
   ```
   π′ = (1/∣G∣) · ∑ over g in G of  ρ(g) π ρ(g)⁻¹
   ```
   Then π′ is still a projection onto W, now commutes with every ρ(g), and its kernel is the invariant complement. So every representation is a direct sum of irreducible ones, which have no invariant subspaces but 0 and V. The division by ∣G∣ is essential. Over 𝔽ₚ, ℤ/p acting by the matrix [[1, 1], [0, 1]] (rows listed in turn) fixes the line spanned by the first basis vector but has no invariant complement; over ℂ, the infinite group ℤ acting by the same matrix fails in the same way.

3. **Schur's lemma: a G-map between irreducible representations is zero or an isomorphism, and over ℂ every G-map from an irreducible to itself is a scalar.** The kernel and image of a G-map are subrepresentations, so each is 0 or everything. Over ℂ, a G-map φ from V to V has an eigenvalue λ, and φ − λ is a G-map that is not invertible, hence zero. Algebraic closure matters: ℤ/4 acting on ℝ² by rotation through 90° is irreducible over ℝ, yet the rotation itself commutes with the action and is not a scalar. A consequence over ℂ: every irreducible representation of an abelian group is one-dimensional.

4. **The character χ_V(g) = trace ρ(g) is constant on conjugacy classes.** Trace is unchanged by conjugation, so χ(hgh⁻¹) = χ(g), and χ(1) = dim V. The eigenvalues of ρ(g) are roots of unity, because gⁿ = 1 for n = ∣G∣, so χ(g⁻¹) is the complex conjugate of χ(g). Characters add over direct sums and multiply over tensor products.

5. **The irreducible characters are orthonormal.** With the inner product
   ```
   ⟨χ, ψ⟩ = (1/∣G∣) · ∑ over g in G of  χ(g) · conj(ψ(g))
   ```
   distinct irreducible characters have ⟨χ, ψ⟩ = 0 and each has ⟨χ, χ⟩ = 1. The proof applies Schur's lemma to averaged maps between two irreducibles. Hence the multiplicity of an irreducible in V is ⟨χ_V, χ⟩, and a representation is determined up to isomorphism by its character.

6. **There are exactly as many irreducibles as conjugacy classes, and their dimensions satisfy ∑ (dim)² = ∣G∣.** The regular representation has character ∣G∣ at the identity and 0 elsewhere, so it contains each irreducible as many times as its dimension, which gives the sum of squares. The irreducible characters also span the space of functions constant on conjugacy classes, which gives the count. Each dimension divides ∣G∣.

7. **The character table of S₃.** S₃ has three classes: the identity, three transpositions and two 3-cycles.
   ```
                    e    (12)   (123)
   trivial          1      1      1
   sign             1     −1      1
   standard         2      0     −1
   ```
   Check: 1² + 1² + 2² = 6, and the standard row has norm (4 + 0 + 2·1)/6 = 1. The permutation representation on ℂ³ has character (3, 1, 0), which is trivial plus standard.

8. **For cyclic groups, character theory is the discrete Fourier transform.** The irreducible characters of ℤ/n are χₖ(m) = e^(2πikm/n) for k = 0, …, n − 1, and their orthogonality is the orthogonality of the Fourier basis. Expanding a function on ℤ/n in characters is the discrete Fourier transform, the algebra behind the fast Fourier transform. For non-abelian groups, the same expansion uses matrix-valued pieces.

## Key concepts

| Term | Meaning |
|---|---|
| Representation | A homomorphism ρ from G to GL(V) |
| Irreducible | No invariant subspaces except 0 and V |
| G-map | A linear map commuting with the action of every g |
| Group algebra ℂ[G] | Formal combinations of group elements; representations are its modules |
| Character | g ↦ trace ρ(g), a function constant on conjugacy classes |
| Character table | The values of the irreducible characters on the conjugacy classes |
| Regular representation | G acting on ℂ[G] by left multiplication |

## How it fits

- **Below:** representations are [modules](modules.md) over ℂ[G] and linear versions of [group actions](../01-groups/group-actions.md); averaging an [inner product](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md) makes every representation unitary; Schur's lemma rests on the existence of [eigenvalues](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md) over ℂ.
- **Above:** [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) extends tenet 8; [representations of Lie groups](../../08-geometry/04-lie-theory/representations-of-lie-groups.md) replace sums by integrals; in [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) symmetries act on state spaces, and irreducibles explain degenerate energy levels; [the Langlands programme](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/the-langlands-programme.md) is phrased in representations of Galois groups.
- **Siblings:** [modules](modules.md) give the language; the decomposition into irreducibles parallels the structure theorem there.

## Common misconceptions

- **"Every representation splits into irreducibles."** For a finite group this needs the characteristic not to divide ∣G∣, and modular representation theory, where it does divide, is far harder. For infinite groups, such as ℤ in tenet 2, it can fail even over ℂ.
- **"Irreducible over ℝ means irreducible over ℂ."** The 90° rotation of ℝ² splits over ℂ into two one-dimensional pieces.
- **"Groups with the same character table are isomorphic."** The dihedral group of order 8 and the quaternion group have identical character tables.

## Go deeper

- Jean-Pierre Serre, *Linear Representations of Finite Groups* (1977): a short, precise first part covering everything above.
- Gordon James and Martin Liebeck, *Representations and Characters of Groups* (2nd edition, 2001): a gentle undergraduate treatment with many character tables.
