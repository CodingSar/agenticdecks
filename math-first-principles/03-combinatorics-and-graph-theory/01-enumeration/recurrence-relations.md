# Recurrence Relations

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Enumeration](README.md)
> **Builds on:** [Generating functions](generating-functions.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [The complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md)
> **Enables:** [Combinatorial sequences](combinatorial-sequences.md), [Eigenvalues and diagonalisation](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md), [Iterated maps](../../10-differential-equations-and-dynamics/04-dynamical-systems/iterated-maps.md), [Induction and recurrences in computing](../../../cs-first-principles/01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md)

## Essence
A recurrence relation defines each term of a sequence from earlier terms, as Fₙ = Fₙ₋₁ + Fₙ₋₂ does for the Fibonacci numbers. Recurrences are how counting problems usually arrive: split the objects of size n by what happens at the first step, and the count at n is expressed through smaller counts. Solving a recurrence means finding a closed form or at least the growth rate. For linear recurrences with constant coefficients the theory is complete: the solutions are combinations of powers of the roots of one polynomial, equivalently the sequences whose generating functions are rational. Nonlinear recurrences are a different world, reaching as far as chaos.

## Core tenets
1. **A recurrence with initial values defines exactly one sequence.** If aₙ is given by a rule from a₀, …, aₙ₋₁ (or from a fixed number of predecessors plus starting values), strong induction shows that two sequences obeying the rule agree everywhere, and the recursion theorem on ℕ shows that one exists. Without the initial values the solution is not unique: the Fibonacci rule alone has one solution for each choice of F₀ and F₁.

2. **Linear recurrences are solved by the characteristic polynomial.** For aₙ = c₁aₙ₋₁ + ⋯ + cₖaₙ₋ₖ with cₖ ≠ 0, the sequence rⁿ is a solution exactly when r is a root of χ(t) = tᵏ − c₁tᵏ⁻¹ − ⋯ − cₖ. Solutions form a vector space of dimension k, because the k initial values determine everything. If χ has distinct roots r₁, …, rₖ, the general solution is α₁r₁ⁿ + ⋯ + αₖrₖⁿ, with the αᵢ fixed by the initial values; a root of multiplicity m contributes rⁿ, nrⁿ, …, nᵐ⁻¹rⁿ. Roots may be complex even when every term is an integer, which is why [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) are needed.

3. **Binet's formula is the Fibonacci case.** χ(t) = t² − t − 1 has roots φ = (1 + √5)/2 and ψ = (1 − √5)/2, and F₀ = 0, F₁ = 1 give

   ```
   Fₙ = (φⁿ − ψⁿ)/√5
   ```

   Since ∣ψ∣ < 1, the term ψⁿ/√5 has absolute value below 1/2, so Fₙ is the integer nearest φⁿ/√5. The dominant root decides growth; the others only correct it.

4. **Linear recurrences correspond exactly to rational generating functions.** Multiplying A(x) = ∑ aₙxⁿ by Q(x) = 1 − c₁x − ⋯ − cₖxᵏ kills every coefficient from xᵏ on, because each is aₙ − c₁aₙ₋₁ − ⋯ − cₖaₙ₋ₖ = 0. So A = P/Q with deg P < k, and conversely any such quotient satisfies the recurrence. Partial fractions of P/Q recover the closed form, since 1/(1 − rx) = ∑ rⁿxⁿ; Q is χ with its coefficients reversed, so its roots are the reciprocals 1/rᵢ.

5. **A linear recurrence is a matrix power.** Writing vₙ = (aₙ, aₙ₋₁, …, aₙ₋ₖ₊₁) gives vₙ₊₁ = Mvₙ for a k × k companion matrix M whose characteristic polynomial is χ. For Fibonacci,

   ```
   ⎡Fₙ₊₁  Fₙ  ⎤   ⎡1 1⎤ⁿ
   ⎣Fₙ    Fₙ₋₁⎦ = ⎣1 0⎦       (n ≥ 1)
   ```

   so repeated squaring computes Fₙ in about log₂ n matrix multiplications, and diagonalising M is the closed form of tenet 2. The repeated-root case is where M fails to diagonalise; the full story belongs to [eigenvalues and diagonalisation](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md).

6. **Inhomogeneous terms add a particular solution.** For aₙ = c₁aₙ₋₁ + ⋯ + cₖaₙ₋ₖ + g(n), the difference of two solutions solves the homogeneous recurrence, so every solution is one particular solution plus the homogeneous family, exactly as for linear differential equations. The Tower of Hanoi recurrence Tₙ = 2Tₙ₋₁ + 1, T₀ = 0, has particular solution −1 and so Tₙ = 2ⁿ − 1.

7. **Divide-and-conquer recurrences are solved by unrolling.** Running times such as T(n) = 2T(n/2) + n for n a power of 2 unroll into log₂ n levels each costing n, so T(n) = n log₂ n + nT(1). The general pattern, comparing the work at the root with the number of leaves of the recursion tree, is the master theorem of [algorithm analysis](../../../cs-first-principles/02-theory-of-computation/04-complexity/asymptotic-analysis.md).

8. **Nonlinear recurrences have no general theory.** Some are tamed by generating functions: the Catalan numbers obey Cₙ₊₁ = ∑ CᵢCₙ₋ᵢ, which becomes the quadratic T = 1 + xT². Others are chaotic: the logistic map xₙ₊₁ = 4xₙ(1 − xₙ) is a [dynamical system](../../10-differential-equations-and-dynamics/04-dynamical-systems/iterated-maps.md) with sensitive dependence on initial conditions. Even for linear integer recurrences some basic questions remain open: whether one can always decide if a given sequence ever hits 0 (the Skolem problem) is open as of 2026, although the Skolem–Mahler–Lech theorem shows that the zero set is a finite set plus finitely many arithmetic progressions.

## Key concepts
| Term | Meaning |
|---|---|
| Recurrence relation | A rule giving each term from earlier terms |
| Order | How many earlier terms the rule uses |
| Characteristic polynomial | χ(t) = tᵏ − c₁tᵏ⁻¹ − ⋯ − cₖ for a linear recurrence |
| General solution | The k-dimensional family of all solutions, fixed by k initial values |
| Binet's formula | Fₙ = (φⁿ − ψⁿ)/√5 |
| Rational generating function | P(x)/Q(x); exactly the generating functions of linear recurrent sequences |
| Companion matrix | The matrix M with vₙ₊₁ = Mvₙ |
| Particular solution | One solution of an inhomogeneous recurrence |

## How it fits
- **Below:** Existence and uniqueness are [induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md); the rational-series view is [generating functions](generating-functions.md); complex roots come from [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md).
- **Above:** Matrix powers and diagonalisation are [linear algebra](../../04-linear-algebra/02-determinants-and-eigenvalues/eigenvalues-and-diagonalisation.md); nonlinear recurrences are [iterated maps](../../10-differential-equations-and-dynamics/04-dynamical-systems/iterated-maps.md); the shift operator and its eigenvectors foreshadow linear differential equations; running-time recurrences drive [algorithm design](../../../cs-first-principles/05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md).
- **Siblings:** [Combinatorial sequences](combinatorial-sequences.md) are mostly defined by recurrences; [counting principles](counting-principles-and-binomial-coefficients.md) supply the first-step decompositions.

## Common misconceptions
- **"Every integer recurrence has a closed form"**: linear constant-coefficient recurrences do, but most nonlinear ones have none, and even simple-looking ones can behave chaotically.
- **"Irrational or complex roots cannot produce integers"**: Binet's formula combines irrational powers into integers, and aₙ = −aₙ₋₂ has roots ±i yet produces 1, 0, −1, 0, 1, …
- **"Guessing a formula from the first terms solves the recurrence"**: a guess is proved only by checking that it satisfies the recurrence and the initial values, which by uniqueness then settles it.

## Go deeper
- Graham, Knuth and Patashnik, *Concrete Mathematics* (2nd edition, 1994): chapters 1 and 7 solve recurrences by every standard method.
- Wilf, *generatingfunctionology* (1990): the generating-function approach to recurrences, linear and not.
- Elaydi, *An Introduction to Difference Equations* (3rd edition, 2005): the theory as the discrete twin of differential equations.
