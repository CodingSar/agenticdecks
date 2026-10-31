# Quantifier Elimination and Decidable Theories

> **Layer:** [13 Structure and Metamathematics](../README.md) › [Model theory and independence](README.md)
> **Builds on:** [Models and the Löwenheim–Skolem theorems](models-and-the-lowenheim-skolem-theorems.md), [Undecidable problems](../02-computability-and-incompleteness/undecidable-problems.md), [Gödel's incompleteness theorems](../02-computability-and-incompleteness/godels-incompleteness-theorems.md), [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [Field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md)
> **Enables:** [Linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md), [Logic and declarative programming](../../../cs-first-principles/06-programming-languages/01-paradigms/logic-and-declarative.md), [Predicate logic (CS)](../../../cs-first-principles/01-mathematical-foundations/01-logic/predicate-logic.md)

## Essence

Gödel's theorems say arithmetic with addition and multiplication is undecidable, but many important theories are not: the first-order theory of the real numbers, of the complex numbers, and of the natural numbers with addition alone can all be decided by an algorithm. The usual method is quantifier elimination: show that every formula is equivalent in the theory to one without quantifiers, whose truth for given parameters can be checked by computation. The dividing line is whether a theory can define the integers with both addition and multiplication; once it can, Gödel's coding applies and decidability is lost.

## Core tenets

1. **Quantifier elimination replaces a question about existence by a computation.** A theory T eliminates quantifiers if every formula is T-equivalent to a quantifier-free one. Over the real numbers the formula ∃x (ax² + bx + c = 0) is equivalent to the formula below, which the school formula for quadratics justifies. If T eliminates quantifiers and decides quantifier-free sentences, which are just arithmetic on constants, it is complete and, when the elimination is effective, decidable.

   ```
   (a ≠ 0 ∧ b² − 4ac ≥ 0) ∨ (a = 0 ∧ b ≠ 0) ∨ (a = 0 ∧ b = 0 ∧ c = 0)
   ```

2. **Tarski: the theory of the real field is decidable.** Alfred Tarski proved that the theory of real closed fields, ordered fields in which positive elements have square roots and odd-degree polynomials have roots, eliminates quantifiers in the language of ordered rings. The key step eliminates ∃x from a conjunction of polynomial conditions in x, using Sturm sequences to count real roots in terms of the coefficients. So every first-order statement about ℝ with +, ·, < is decidable. Geometrically, the Tarski–Seidenberg theorem says that projections of semialgebraic sets are semialgebraic.

3. **The integers are not definable in the real field, and that is why it is decidable.** Every subset of ℝ definable in the real field is a finite union of points and intervals, so ℤ is not definable; arithmetic cannot be coded. Adding the sine function defines ℤ as the zeros of sin(πx), and the theory becomes undecidable. Whether adding the exponential function keeps the theory decidable is Tarski's problem, open as of 2026: Angus Macintyre and Alex Wilkie (1996) proved it decidable if Schanuel's conjecture holds, after Wilkie (1996) showed that every definable subset of ℝ is still a finite union of points and intervals.

4. **Decidable does not mean feasible.** George Collins's cylindrical algebraic decomposition (1975) decides the real field in time doubly exponential in the number of variables, and James Davenport and Joos Heintz (1988) showed that quantifier elimination over ℝ can require doubly exponential output. Michael Fischer and Michael Rabin (1974) proved that every decision procedure for Presburger arithmetic needs doubly exponential time in the worst case.

5. **Algebraically closed fields are decidable too, with algebraic consequences.** The theory of algebraically closed fields of a fixed characteristic eliminates quantifiers, so it is complete. Chevalley's theorem, that the image of a constructible set under a polynomial map is constructible, is the geometric form. The Lefschetz principle follows: a first-order sentence true in ℂ holds in algebraically closed fields of every large enough prime characteristic. The Ax–Grothendieck theorem, that an injective polynomial map ℂⁿ → ℂⁿ is surjective, follows from its obvious truth for finite fields.

6. **Arithmetic with addition alone is decidable.** Mojżesz Presburger (1929) showed that the natural numbers with + eliminate quantifiers once predicates for congruence modulo each n are added, so the definable sets of numbers are exactly the eventually periodic ones. Adding multiplication changes everything. Gödel's β-function, rem(a, 1 + (i + 1)·b), uses the Chinese remainder theorem to code any finite sequence by two numbers, so exponentiation and computations become definable; every consistent extension of Robinson arithmetic is undecidable. Julia Robinson (1949) defined ℤ inside the field ℚ, so the theory of ℚ is undecidable as well. Elsewhere the line falls in both directions: the p-adic fields (James Ax and Simon Kochen, and independently Yuri Ershov, 1965) and abelian groups (Wanda Szmielew, 1955) are decidable, while truth in all finite structures is not (Boris Trakhtenbrot, 1950).

## Key concepts

| Term | Meaning |
|---|---|
| Quantifier elimination | Every formula is equivalent to a quantifier-free one |
| Complete theory | Proves φ or ¬φ for every sentence φ |
| Decidable theory | An algorithm determines which sentences it proves |
| Real closed field | An ordered field with the first-order properties of ℝ |
| Semialgebraic set | A set defined by polynomial equalities and inequalities |
| Presburger arithmetic | The theory of ℕ with addition only |
| Essential undecidability | Every consistent extension is undecidable |

## How it fits

- **Below:** It uses the [completeness of ℝ](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md) and the algebra of [field extensions](../../05-abstract-algebra/02-rings-and-fields/field-extensions.md), and marks the boundary drawn by [undecidability](../02-computability-and-incompleteness/undecidable-problems.md) and [Gödel](../02-computability-and-incompleteness/godels-incompleteness-theorems.md).
- **Above:** Fourier–Motzkin elimination in [linear programming](../../14-applied-and-computational-mathematics/02-optimisation/linear-programming.md) is quantifier elimination for linear inequalities, and decision procedures are built into [automated proof](../../15-mathematics-in-context/computers-and-proof.md) and [logic programming](../../../cs-first-principles/06-programming-languages/01-paradigms/logic-and-declarative.md); see also [predicate logic in CS](../../../cs-first-principles/01-mathematical-foundations/01-logic/predicate-logic.md).
- **Siblings:** It starts from [models and Löwenheim–Skolem](models-and-the-lowenheim-skolem-theorems.md); [forcing](forcing-and-independence.md) shows the opposite situation, where set theory leaves questions open.

## Common misconceptions

- **"Quantifier elimination is a property of a structure."**: It depends on the language: the real field eliminates quantifiers with < but not without it, since x ≥ 0 then needs ∃y (x = y²).
- **"A decidable theory is complete."**: The theory of algebraically closed fields with unspecified characteristic is decidable, yet does not decide 1 + 1 = 0.
- **"Real arithmetic is undecidable because integer arithmetic is."**: The reals are simpler than the integers here: ℝ is decidable precisely because ℤ cannot be defined inside it.

## Go deeper

- Alfred Tarski, *A Decision Method for Elementary Algebra and Geometry* (1948; 2nd edition 1951): the original decision procedure.
- Lou van den Dries, *Tame Topology and O-minimal Structures* (1998): what happens beyond the real field.
- Saugata Basu, Richard Pollack and Marie-Françoise Roy, *Algorithms in Real Algebraic Geometry* (2003): the algorithms and their complexity.
