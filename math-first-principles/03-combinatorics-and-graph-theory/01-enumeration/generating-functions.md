# Generating Functions

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Enumeration](README.md)
> **Builds on:** [Counting principles and binomial coefficients](counting-principles-and-binomial-coefficients.md), [Integers and rational numbers](../../02-number-systems/01-constructing-the-numbers/integers-and-rational-numbers.md), [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md)
> **Enables:** [Recurrence relations](recurrence-relations.md), [Combinatorial sequences](combinatorial-sequences.md), [Polynomial rings](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md), [Singularities and residues](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md), [Expectation and variance](../03-discrete-probability/expectation-and-variance.md)

## Essence
A generating function encodes a sequence a₀, a₁, a₂, … as a formal power series A(x) = ∑ aₙxⁿ, so that operations on combinatorial objects become algebra on series: disjoint union becomes addition, pairing becomes multiplication, and a recursive description becomes an equation. The series is formal: x is an indeterminate, not a number, and no convergence is ever needed, because every coefficient of a sum, product or composite is a finite computation. Solving the equation and extracting coefficients yields exact formulas and identities. In Wilf's phrase, a generating function is a clothesline on which we hang up a sequence of numbers for display.

## Core tenets
1. **Formal power series form a ring in which every coefficient is a finite computation.** Over a commutative ring R, the ring R[[x]] consists of sequences (a₀, a₁, …) with termwise addition and the Cauchy product (AB)ₙ = a₀bₙ + a₁bₙ₋₁ + ⋯ + aₙb₀. Two series are equal if and only if all their coefficients agree; a series has no "value at x". So ∑ n! xⁿ, which converges at no nonzero real x, is a perfectly good element of ℤ[[x]].

2. **A series is invertible if and only if its constant term is invertible.** AB = 1 means a₀b₀ = 1 and a₀bₙ + ⋯ + aₙb₀ = 0 for n ≥ 1; if a₀ is a unit these equations determine each bₙ from b₀, …, bₙ₋₁ by induction, and if it is not, a₀b₀ = 1 is impossible. Multiplying out shows (1 − x)(1 + x + x² + ⋯) = 1, while x has no inverse.

3. **Addition and multiplication mirror disjoint union and pairing.** If A(x) and B(x) count two classes of objects by size, A + B counts their disjoint union, and AB counts ordered pairs by total size, because the coefficient of xⁿ sums the product rule over the splits of n. Sequences of objects from a class with no object of size 0 are counted by 1/(1 − A). So (1 + x)ⁿ = ∑ C(n, k)xᵏ, each element being out (1) or in (x), and compositions of n, ordered sums of positive integers, are counted by 1/(1 − x/(1 − x)) = (1 − x)/(1 − 2x), giving 2ⁿ⁻¹ for n ≥ 1.

4. **Composition and differentiation are formal too.** A(B(x)) is defined when b₀ = 0, since then Bᵏ starts at xᵏ and each coefficient involves finitely many terms; if b₀ ≠ 0 the constant term would be the infinite sum ∑ aₖb₀ᵏ. The formal derivative ∑ naₙxⁿ⁻¹ obeys the product rule by direct computation. Over ℚ, define (1 + x)^r as ∑ C(r, k)xᵏ for any rational r; Vandermonde's identity, a polynomial identity in r and s that holds for all natural numbers and hence for all r and s, gives (1 + x)^r (1 + x)^s = (1 + x)^(r+s), so (1 + x)^(1/2) really squares to 1 + x.

5. **The Catalan numbers fall out of one quadratic equation.** A binary tree is empty or a root with a left and a right subtree, so the series T(x) counting binary trees by number of nodes satisfies T = 1 + xT². Hence T = (1 − √(1 − 4x))/(2x), where √(1 − 4x) is the series with constant term 1 whose square is 1 − 4x; the other sign is excluded because it would need a 1/x term. The generalised binomial theorem gives the Catalan numbers Cₙ = C(2n, n)/(n + 1): 1, 1, 2, 5, 14, 42, …

6. **Infinite products count partitions.** A partition of n writes n as an unordered sum of positive integers. Choosing independently how many parts of each size k to use gives ∑ p(n)xⁿ = ∏ 1/(1 − xᵏ), a legitimate product because only factors with k ≤ n affect the coefficient of xⁿ. Partitions into distinct parts have series ∏ (1 + xᵏ) = ∏ (1 − x²ᵏ)/(1 − xᵏ); the numerators cancel the even-indexed denominators, leaving the series for partitions into odd parts. So the two counts agree for every n, a theorem of Euler proved in one line.

7. **Exponential generating functions handle labelled structures.** For objects built on labels {1, …, n}, use ∑ aₙxⁿ/n!; the product of two such series counts pairs whose labels are shuffled together, because C(n, k) = n!/(k!(n − k)!) splits the labels. A set of labelled components has series exp(component series), where exp(x) = ∑ xⁿ/n!. Set partitions (components are non-empty sets, series eˣ − 1) give the Bell numbers via exp(eˣ − 1). A permutation is a set of fixed points together with a derangement of the rest, so eˣ D(x) = 1/(1 − x) and the derangement series is D(x) = e^(−x)/(1 − x).

8. **Analysis enters only for asymptotics.** When a series converges near 0 it defines a complex function, and its singularity nearest the origin governs coefficient growth: T has a square-root singularity at x = 1/4, which yields Cₙ ~ 4ⁿ/(√π · n^(3/2)). This singularity analysis needs [complex analysis](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md); exact counting never does.

## Key concepts
| Term | Meaning |
|---|---|
| Formal power series | A sequence written ∑ aₙxⁿ, multiplied by the Cauchy product, with no convergence |
| Ordinary generating function | ∑ aₙxⁿ, for unlabelled objects counted by size |
| Exponential generating function | ∑ aₙxⁿ/n!, for labelled objects |
| Cauchy product | (AB)ₙ = a₀bₙ + ⋯ + aₙb₀, a finite sum |
| Unit of R[[x]] | A series whose constant term is invertible |
| Composition | A(B(x)), defined when B has zero constant term |
| Catalan number Cₙ | C(2n, n)/(n + 1), the number of binary trees with n nodes |
| Partition function p(n) | The number of ways to write n as an unordered sum of positive integers |

## How it fits
- **Below:** Coefficients are computed with [counting principles](counting-principles-and-binomial-coefficients.md); series live over [ℤ and ℚ](../../02-number-systems/01-constructing-the-numbers/integers-and-rational-numbers.md); coefficient-by-coefficient arguments are [induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md).
- **Above:** R[[x]] completes the [polynomial ring](../../05-abstract-algebra/02-rings-and-fields/polynomial-rings.md) R[x]; [singularity analysis](../../09-advanced-analysis/02-complex-analysis/singularities-and-residues.md) extracts asymptotics; probability generating functions turn sums of independent variables into products ([expectation and variance](../03-discrete-probability/expectation-and-variance.md)).
- **Siblings:** [Recurrence relations](recurrence-relations.md) are exactly the sequences with rational generating functions; [combinatorial sequences](combinatorial-sequences.md) collects the classic series; [inclusion–exclusion](inclusion-exclusion-and-the-pigeonhole-principle.md) reaches derangements by a sieve instead.

## Common misconceptions
- **"A generating function must converge to mean anything"**: identities in R[[x]] are identities of coefficients; ∑ n! xⁿ has radius of convergence 0 and is still a valid series. Convergence matters only for analytic methods.
- **"x is a small number you can substitute"**: substitution is defined for polynomials, for composition with series of zero constant term, and for convergent series, not in general; reading 1/(1 − x) = ∑ xⁿ at x = 2 gives the false "−1 = 1 + 2 + 4 + ⋯".
- **"Generating functions only reproduce answers available directly"**: Euler's distinct-parts theorem falls out of one cancellation, long before anyone needs a bijection.

## Go deeper
- Wilf, *generatingfunctionology* (1990): the friendliest complete introduction, from formal series to asymptotics.
- Flajolet and Sedgewick, *Analytic Combinatorics* (2009): the symbolic method and singularity analysis in full.
- Stanley, *Enumerative Combinatorics*, Volume 2 (1999): composition of exponential generating functions, and the Catalan numbers.
