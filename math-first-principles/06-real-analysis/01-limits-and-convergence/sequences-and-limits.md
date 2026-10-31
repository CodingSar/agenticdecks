# Sequences and Limits

> **Layer:** [06 Real Analysis](../README.md) › [Limits and Convergence](README.md)
> **Builds on:** [The real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), [Predicate logic and quantifiers](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md)
> **Enables:** [Series](series.md), [Continuity](continuity.md), [Metric spaces and continuity](../04-metric-spaces/metric-spaces-and-continuity.md), [Modes of convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md), [Asymptotic analysis](../../../cs-first-principles/02-theory-of-computation/04-complexity/asymptotic-analysis.md)

## Essence

A sequence is a function from ℕ to ℝ, written a₁, a₂, a₃, …. Saying that aₙ tends to L means: for every tolerance ε > 0 there is a stage N after which every term lies within ε of L. This replaces the "infinitely close" of early calculus with a game of finite checks: you name an error, I name a stage. Limits exist only because ℝ has no holes: completeness guarantees that sequences which ought to converge, such as bounded monotone ones, have something to converge to. Every later notion in analysis (the sum of a series, continuity, the derivative, the integral) is a limit of a sequence.

## Core tenets

1. **A limit is a statement with three nested quantifiers.** aₙ → L means ∀ε > 0 ∃N ∀n ≥ N: |aₙ − L| < ε. The order carries the meaning: N may depend on ε, and putting "∃N" first would demand that every term from N on equals L. To prove 1/n → 0, given ε choose N > 1/ε, which exists by the Archimedean property; then n ≥ N gives 1/n ≤ 1/N < ε. Negating the sentence says what divergence from L means: for some ε > 0, infinitely many terms miss L by at least ε.

2. **A limit is unique, and a convergent sequence is bounded.** If aₙ → L and aₙ → M with L ≠ M, take ε = |L − M|/2. Late terms lie within ε of both, so |L − M| ≤ |L − aₙ| + |aₙ − M| < 2ε = |L − M|, a contradiction. The triangle inequality does the work, as in most limit proofs. Boundedness follows because all terms after N lie within 1 of L and only finitely many come before.

3. **Limits respect arithmetic and weak inequalities, not strict ones.** If aₙ → a and bₙ → b, then aₙ + bₙ → a + b, aₙbₙ → ab, and aₙ/bₙ → a/b when b ≠ 0. The proof splits the error, aₙbₙ − ab = aₙ(bₙ − b) + b(aₙ − a), and each part is small because aₙ is bounded. If aₙ ≤ bₙ for all n then a ≤ b, but strict inequality is lost: 1/n > 0 for every n, while the limit is 0.

4. **A bounded monotone sequence converges, and this is completeness at work.** Let aₙ be increasing and bounded above, with supremum (sup) s, the least upper bound of its terms. For ε > 0, s − ε is not an upper bound, so some a_N exceeds it, and then s − ε < a_N ≤ aₙ ≤ s for all n ≥ N. In ℚ the sequence 1, 1.4, 1.41, 1.414, … is bounded and increasing but has no limit, because its limit would be √2. Most existence theorems in this layer trace back to this tenet.

5. **Every bounded sequence has a convergent subsequence (Bolzano–Weierstrass).** Put the terms in [a, b] and halve it: one half holds terms with infinitely many indices. Keep halving, and pick one term from each nested interval, with increasing indices. The intervals shrink to a single point, which exists by completeness, and the chosen subsequence converges to it. The theorem fails without boundedness (aₙ = n) and without completeness (in ℚ). This bisection is the prototype of compactness.

6. **A Cauchy sequence converges, so convergence can be tested without knowing the limit.** A sequence is Cauchy when its late terms are close to each other: ∀ε > 0 ∃N ∀m, n ≥ N: |aₘ − aₙ| < ε. Every convergent sequence is Cauchy, by the triangle inequality. In ℝ the converse holds: a Cauchy sequence is bounded, so it has a convergent subsequence, and the whole sequence must follow that subsequence. So 1 + 1/4 + 1/9 + ⋯ can be shown to converge without knowing its sum, π²/6.

7. **The completeness properties are equivalent, and together they characterise ℝ.** For an ordered field the following are equivalent: every nonempty set bounded above has a sup; bounded monotone sequences converge; Bolzano–Weierstrass holds; the field is Archimedean and Cauchy sequences converge. The Archimedean clause cannot be dropped, since some non-Archimedean ordered fields have convergent Cauchy sequences but lack sups. Up to isomorphism ℝ is the only complete ordered field, so each property says exactly what ℝ adds to ℚ.

## Key concepts

| Term | Meaning |
|---|---|
| Sequence | A function ℕ → ℝ, n ↦ aₙ |
| Limit | A number L with ∀ε > 0 ∃N ∀n ≥ N: ∣aₙ − L∣ < ε |
| Divergence | Failure to converge: by growth (aₙ → ∞) or by oscillation |
| Supremum (sup) | The least upper bound of a set; infimum (inf) is the greatest lower bound |
| Subsequence | A selection a_(n₁), a_(n₂), … with n₁ < n₂ < ⋯ |
| Cauchy sequence | ∀ε > 0 ∃N ∀m, n ≥ N: ∣aₘ − aₙ∣ < ε |
| limsup, liminf | The limits of sup{aₖ : k ≥ n} and inf{aₖ : k ≥ n}; a bounded aₙ converges if and only if they agree |
| Archimedean property | Every real x is exceeded by some n ∈ ℕ; equivalently 1/n → 0 |

## How it fits

- **Below:** The completeness of ℝ, built from ℚ in [the real numbers](../../02-number-systems/01-constructing-the-numbers/the-real-numbers.md), is the one assumption behind tenets 4 to 7. The ε–N definition is a sentence of [predicate logic](../../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), and its quantifier order is its whole content.
- **Above:** [Series](series.md) are sequences of partial sums, [continuity](continuity.md) is the preservation of limits, and derivatives and [integrals](../02-calculus-of-one-variable/the-riemann-integral.md) are limits. [Metric spaces](../04-metric-spaces/metric-spaces-and-continuity.md) keep only the distance the definition uses. Random sequences have several inequivalent [modes of convergence](../../11-probability-and-statistics/02-limit-theorems/modes-of-convergence.md).
- **Siblings:** [Estimates and inequalities](estimates-and-inequalities.md) supplies the bounds every ε–N proof needs. [Uniform convergence](uniform-convergence.md) asks the same question of sequences of functions, where it splits into two inequivalent questions.

## Common misconceptions

- **"A sequence converges if consecutive terms get closer and closer."** The gaps can shrink to 0 while the sequence diverges: the partial sums 1 + 1/2 + ⋯ + 1/n differ by 1/(n + 1) yet grow without bound. The Cauchy condition asks all pairs of late terms to be close, not just neighbours.
- **"The limit is the value the sequence finally reaches."** Most convergent sequences never reach their limit: 1/n ≠ 0 for every n. The limit is the number that late terms approximate as well as you like.
- **"∞ is a limit like any other."** "aₙ → ∞" is shorthand for "every bound is eventually exceeded", and such a sequence diverges. The arithmetic rules fail for it: n → ∞ and c − n → −∞, yet their sum is c, whatever c is.

## Go deeper

- Stephen Abbott, *Understanding Analysis* (2nd edition, 2015): a gentle first course built around these questions.
- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): the classic terse treatment.
- Terence Tao, *Analysis I* (2006): builds ℝ from Cauchy sequences of rationals, then proves these tenets.
