# p-adic Numbers and Local Fields

> **Layer:** [12 Number Theory and Algebraic Geometry](../README.md) › [Algebraic Number Theory](README.md)
> **Builds on:** [Number Fields and Algebraic Integers](number-fields-and-algebraic-integers.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [The Real Numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [Quadratic Forms and Positive Definiteness](../../04-linear-algebra/03-inner-product-spaces/quadratic-forms-and-positive-definiteness.md), [Modular Arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md)
> **Enables:** [Class Field Theory](class-field-theory.md), [Elliptic Curves](../04-elliptic-curves-and-modular-forms/elliptic-curves.md), [The Langlands Programme](../04-elliptic-curves-and-modular-forms/the-langlands-programme.md), [Root-Finding and Newton's Method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md)

## Essence

The real numbers complete ℚ for the usual distance, but ℚ has one other kind of distance for each prime p, in which a number is small when it is divisible by a high power of p. Completing for that distance gives the field ℚ_p of p-adic numbers, where congruences mod p, p², p³, … are bundled into a single object. Solving an equation in ℚ_p means solving it mod every power of p at once, and Hensel's lemma says that a good solution mod p usually lifts. The local-to-global question then asks when solutions in ℝ and in every ℚ_p force a solution in ℚ: always for quadratic forms (Hasse–Minkowski), not always for cubics (Selmer).

## Core tenets

1. **The p-adic absolute value is ultrametric.** Write x = pᵛ·(a/b) with a, b prime to p, and set v_p(x) = v and ∣x∣_p = p^(−v). Then ∣x + y∣_p ≤ max(∣x∣_p, ∣y∣_p), stronger than the triangle inequality, because a sum of two multiples of pᵛ is a multiple of pᵛ. So every triangle is isosceles, every point of a ball is its centre, and balls are open and closed at once. A series converges exactly when its terms tend to 0.

2. **There are no other absolute values on ℚ (Ostrowski, 1916).** Every non-trivial absolute value on ℚ is a power of the usual one ∣·∣_∞ or of one ∣·∣_p. Proof idea: if ∣n∣ > 1 for some integer n, writing integers in base n forces the archimedean case; otherwise ∣n∣ ≤ 1 for all n, the integers with ∣n∣ < 1 form a prime ideal pℤ, and the value is fixed by ∣p∣. The places fit together in the product formula ∏_v ∣x∣_v = 1 for x ∈ ℚ, x ≠ 0, which is unique factorisation in disguise.

3. **ℚ_p is a completion with a compact ring of integers.** ℚ_p is the completion of ℚ for ∣·∣_p, and ℤ_p = {x : ∣x∣_p ≤ 1} is the set of sequences of residues mod pⁿ that agree with each other, a compact ring. Every p-adic integer is a series ∑ aᵢpⁱ with digits 0 ≤ aᵢ < p, infinite to the left. Example: in ℚ₂, 1 + 2 + 4 + 8 + ⋯ converges, and multiplying by 1 − 2 shows its sum is −1.

4. **Hensel's lemma lifts simple roots.** If f ∈ ℤ_p[x], f(a) ≡ 0 mod p and f′(a) ≢ 0 mod p, there is a unique root α ∈ ℤ_p with α ≡ a mod p. The proof is Newton's method, aₙ₊₁ = aₙ − f(aₙ)/f′(aₙ), which here at least doubles the number of correct digits at each step. So √−1 ∈ ℚ₅, since 2² ≡ −1 mod 5. The hypothesis on f′ matters: x² + 1 has the root 1 mod 2, where f′(1) = 2 ≡ 0, and no root in ℚ₂, since x² ≡ −1 mod 4 is impossible.

5. **Local fields are the completions.** A local field is a field complete for a non-trivial absolute value with a locally compact topology: ℝ, ℂ, the finite extensions of ℚ_p, and the Laurent series fields 𝔽_q((t)). Each completion of a number field K at a prime ideal or an embedding is one of these. Locally, arithmetic is simple: a finite extension of ℚ_p has a single prime.

6. **Hasse–Minkowski: quadratic forms obey the local-to-global principle.** A quadratic form with rational coefficients represents 0 non-trivially over ℚ if and only if it does so over ℝ and over every ℚ_p. One direction is trivial. The other is proved by induction on the number of variables, using quadratic reciprocity and Dirichlet's theorem on primes in progressions. Example: x² + y² = 3z² has real solutions, but none in ℚ₃. If x, y, z are integers not all divisible by 3, then 3 ∣ x² + y² forces 3 ∣ x and 3 ∣ y, since −1 is not a square mod 3; then 9 ∣ 3z², so 3 ∣ z. The test is finite: for a diagonal integer form only ℝ, p = 2 and the primes dividing the coefficients need checking.

7. **Cubics can fail it: Selmer's curve.** Selmer showed in 1951 that 3x³ + 4y³ + 5z³ = 0 has non-zero solutions in ℝ and in every ℚ_p but none in ℚ. The failure is measured by a group, the Tate–Shafarevich group Ш of the associated elliptic curve, whose non-zero elements are curves like this one: soluble everywhere locally but not globally. Whether Ш is always finite is part of the Birch and Swinnerton-Dyer conjecture, open as of 2026.

8. **The adeles hold all places at once.** The adele ring 𝔸_ℚ is the restricted product of ℝ and all the ℚ_p, in which almost every coordinate lies in ℤ_p. ℚ sits inside it diagonally as a discrete subgroup with compact quotient 𝔸_ℚ/ℚ, just as ℤ sits in ℝ. This is the stage on which class field theory and automorphic forms are set.

## Key concepts

| Term | Meaning |
|---|---|
| p-adic valuation v_p(x) | The exponent of p in x |
| p-adic absolute value | ∣x∣_p = p^(−v_p(x)); small means divisible by a high power of p |
| ℚ_p, ℤ_p | The completion of ℚ, and its compact subring {∣x∣_p ≤ 1} |
| Hensel's lemma | A root mod p with non-zero derivative lifts to a unique p-adic root |
| Local field | ℝ, ℂ, a finite extension of ℚ_p, or 𝔽_q((t)) |
| Place | An equivalence class of absolute values: ∞ or a prime p |
| Local-to-global principle | Solubility in ℝ and every ℚ_p implies solubility in ℚ |

## How it fits

- **Below:** the [real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) are built by the same completion; [contraction mappings](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md) explain why Newton's iteration converges; [modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md) supplies the finite approximations.
- **Above:** [elliptic curves](../04-elliptic-curves-and-modular-forms/elliptic-curves.md) use local conditions in Mordell's theorem and the Birch and Swinnerton-Dyer conjecture; [the Langlands programme](../04-elliptic-curves-and-modular-forms/the-langlands-programme.md) is phrased over the adeles; p-adic lifting is [Newton's method](../../14-applied-and-computational-mathematics/01-numerical-analysis/root-finding-and-newtons-method.md) in exact arithmetic.
- **Siblings:** [number fields](number-fields-and-algebraic-integers.md) are completed at their primes; [class field theory](class-field-theory.md) has a local version over each ℚ_p.

## Common misconceptions

- **"p-adic numbers are just integers mod p"**: they hold residues mod every power of p, form a field of characteristic 0, and contain ℚ.
- **"Local solubility everywhere implies a rational solution"**: true for quadratic forms, false for Selmer's cubic.

## Go deeper

- Fernando Q. Gouvêa, *p-adic Numbers: An Introduction* (2nd edition, 1997): the gentlest full introduction.
- Jean-Pierre Serre, *A Course in Arithmetic* (1973): ℚ_p and a complete proof of Hasse–Minkowski in a few pages.
- Neal Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions* (2nd edition, 1984): p-adic analysis through to zeta functions.
