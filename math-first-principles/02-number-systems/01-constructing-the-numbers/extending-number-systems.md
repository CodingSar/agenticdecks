# Extending Number Systems

> **Layer:** [02 Number Systems](../README.md) › [Constructing the Numbers](README.md)
> **Builds on:** [The Complex Numbers](the-complex-numbers.md), [The Real Numbers](the-real-numbers.md), [Integers and Rational Numbers](integers-and-rational-numbers.md)
> **Enables:** [p-adic Numbers and Local Fields](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md), [Rings and Ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md), [Lie Groups and Lie Algebras](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md), [The Classification of Simple Lie Algebras](../../08-geometry/04-lie-theory/the-classification-of-simple-lie-algebras.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md)

## Essence

ℂ is algebraically closed, so polynomial equations give no reason to go further, but there are two other directions. Upwards, the doubling that turns ℝ into ℂ turns ℂ into the quaternions ℍ (Hamilton, 1843) and ℍ into the octonions 𝕆, and each step costs a law: first order, then commutativity, then associativity. Theorems of Frobenius and Hurwitz show that the list stops there. Sideways, ℚ can be completed for a different notion of size, in which pⁿ is small, giving the p-adic numbers, as basic to number theory as ℝ.

## Core tenets

1. **The quaternions ℍ are a four-dimensional real division algebra that is not commutative.** Hamilton found the rules on 16 October 1843: i² = j² = k² = ijk = −1, which give ij = k = −ji, jk = i = −kj and ki = j = −ik. The conjugate of q = a + bi + cj + dk is q̄ = a − bi − cj − dk, and q · q̄ = a² + b² + c² + d², so every q ≠ 0 has inverse q̄/|q|², and |pq| = |p| · |q|.

2. **No real division algebra with identity has odd dimension greater than 1.** Left multiplication by x is a linear map of ℝⁿ; for odd n its characteristic polynomial has odd degree, hence a real eigenvalue λ, so xy = λy for some y ≠ 0. Then (x − λ · 1)y = 0, and without zero divisors x = λ · 1. So every element is real and n = 1; associativity is not used.

3. **Unit quaternions describe rotations of space.** Identify vectors in ℝ³ with pure quaternions bi + cj + dk. For pure u and v, uv = −⟨u, v⟩ + u × v, so the dot and cross products are two halves of one multiplication. The unit quaternion q = cos(θ/2) + sin(θ/2) · n, for a unit vector n, acts by v ↦ qvq⁻¹ as the rotation by θ about n. Since q and −q give the same rotation, the unit quaternions, a 3-sphere, cover the rotation group twice.

4. **The Cayley–Dickson construction doubles an algebra with conjugation, and each doubling loses a property.** Pairs multiply by:

   ```
   (a, b) · (c, d) = (a·c − conj(d)·b,  d·a + b·conj(c))
   conj((a, b))    = (conj(a), −b)
   ```

   From ℝ with trivial conjugation this gives ℂ; from ℂ it gives ℍ, with j = (0, 1), ij = (0, i) = k and ji = −k. The double is commutative only if the old conjugation is trivial, associative only if the old algebra is commutative, and alternative (any two elements generate an associative subalgebra) only if the old one is associative. So ℍ loses commutativity, 𝕆 loses associativity but stays alternative and normed, and the sixteen-dimensional sedenions have zero divisors. Graves and Cayley found 𝕆 within two years of ℍ; its automorphism group is the exceptional Lie group G₂.

5. **Frobenius (1877): the only finite-dimensional associative real division algebras are ℝ, ℂ and ℍ.** Each element x generates a commutative field ℝ(x) of finite dimension, which by the fundamental theorem of algebra is ℝ or ℂ, so every element satisfies a real quadratic equation. The elements whose square is a non-positive real form a subspace with a positive definite form, and orthonormal elements i, j in it rebuild ℍ, or the process stops at ℝ or ℂ. Without associativity 𝕆 appears; without finite dimension, fields such as ℝ(x).

6. **Hurwitz (1898): the only real algebras with identity and a multiplicative Euclidean norm, |xy| = |x| · |y|, are ℝ, ℂ, ℍ and 𝕆.** Equivalently, a bilinear identity writing a product of two sums of n squares as a sum of n squares exists only for n = 1, 2, 4, 8: the identity of ℂ, Euler's four-square identity and Degen's eight-square identity. Without a norm, Kervaire and Bott–Milnor (1958) proved by topology that real division algebras exist only in dimensions 1, 2, 4 and 8.

7. **ℚ has other completions, the p-adic numbers.** For a prime p, set |x|ₚ = p^(−v) when x = pᵛ · a/b with a and b prime to p, and |0|ₚ = 0. This size is ultrametric, |x + y|ₚ ≤ max(|x|ₚ, |y|ₚ), and completing ℚ for it gives the field ℚₚ (Hensel, 1897). In ℚ₂ the series 1 + 2 + 4 + ⋯ converges to −1, since its partial sums 2ⁿ − 1 differ from −1 by 2ⁿ. Ostrowski (1916) proved that every non-trivial absolute value on ℚ is equivalent to the usual one or a p-adic one; they are linked by the product formula, as for 12, where 12 · (1/4) · (1/3) = 1. Layer 12 develops this, starting from Hensel's lemma.

## Key concepts

| Term | Meaning |
|---|---|
| Division algebra | An algebra with no zero divisors: ab = 0 forces a = 0 or b = 0 |
| Quaternions ℍ | a + bi + cj + dk with i² = j² = k² = ijk = −1 |
| Octonions 𝕆 | The eight-dimensional normed, alternative, non-associative algebra |
| Alternative algebra | Any two elements generate an associative subalgebra |
| Normed algebra | An algebra with \|xy\| = \|x\| · \|y\| for a Euclidean norm |
| p-adic absolute value | \|x\|ₚ = p^(−v), small when a high power of p divides x |
| Ultrametric | Satisfying \|x + y\| ≤ max(\|x\|, \|y\|) |

## How it fits

- **Below:** the doubling starts from [the complex numbers](the-complex-numbers.md) and [the real numbers](the-real-numbers.md); the p-adic completion repeats Cantor's construction on ℚ with a new distance.
- **Above:** rings and ideals (05) treat non-commutative rings; Lie theory (08) uses unit quaternions and finds G₂ in 𝕆; local fields (12) develop ℚₚ; quantum mechanics (14) uses ℍ through spin.
- **Siblings:** every earlier step, from [integers and rational numbers](integers-and-rational-numbers.md) to ℂ, was forced by an equation; here the motive is structure, and the theorems of Frobenius and Hurwitz say where it ends.

## Common misconceptions

- **"There is a number system in every dimension"**: real division algebras exist only in dimensions 1, 2, 4 and 8, the associative ones only in 1, 2 and 4.
- **"Quaternions are obsolete, replaced by vectors"**: vector notation split their product into dot and cross products; rotation software and the spin of the electron still use the whole.
- **"Any ordered field bigger than ℝ is still like ℝ"**: every Archimedean ordered field embeds in ℝ, so a proper ordered extension, such as Robinson's hyperreals, has infinitesimals and is not complete.

## Go deeper

- Heinz-Dieter Ebbinghaus and others, *Numbers* (Graduate Texts in Mathematics 123): quaternions, octonions, and the Frobenius and Hurwitz theorems.
- John Baez, "The Octonions", Bulletin of the American Mathematical Society (2002): why 𝕆 matters, from G₂ to physics.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (2003): their geometry and arithmetic.
