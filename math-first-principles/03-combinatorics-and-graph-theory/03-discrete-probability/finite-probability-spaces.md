# Finite Probability Spaces

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Discrete Probability](README.md)
> **Builds on:** [Counting principles and binomial coefficients](../01-enumeration/counting-principles-and-binomial-coefficients.md), [Inclusion–exclusion and the pigeonhole principle](../01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md), [Sets and set operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), [Countable sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md)
> **Enables:** [Expectation and variance](expectation-and-variance.md), [Probability spaces and Kolmogorov's axioms](../../11-probability-and-statistics/01-measure-theoretic-probability/probability-spaces-and-kolmogorovs-axioms.md), [Bayesian inference](../../11-probability-and-statistics/04-statistical-inference/bayesian-inference.md), [Bayesian reasoning in medicine](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md), [Probability in computing](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/probability.md)

## Essence
Probability on a finite or countable sample space is counting with weights. Each outcome ω in a set Ω gets a non-negative weight p(ω), the weights sum to 1, and the probability of an event, a subset of Ω, is the total weight of its outcomes. When all outcomes are equally likely this is the ratio of two counts, which is how probability began, in the 1654 correspondence of Pascal and Fermat on games of chance. Everything else, conditional probability, independence and Bayes' rule, is defined from this one structure, and every claim can be checked by summing finitely or countably many numbers. No measure theory is needed until the sample space is uncountable.

## Core tenets
1. **A discrete probability space is a countable set Ω with weights p(ω) ≥ 0 summing to 1.** The probability of an event A ⊆ Ω is P(A) = ∑ p(ω) over ω ∈ A. Because the terms are non-negative, the sum does not depend on the order of summation, so P is well defined even when Ω is countably infinite, and every subset is an event. With Ω finite and p constant, P(A) = ∣A∣/∣Ω∣ and probability is [counting](../01-enumeration/counting-principles-and-binomial-coefficients.md).

2. **The axioms follow from the definition.** P(Ω) = 1, P(A) ≥ 0, and P is countably additive: for pairwise disjoint A₁, A₂, …, P(⋃ Aᵢ) = ∑ P(Aᵢ), since a sum of non-negative terms may be regrouped freely. Consequences are inherited from counting: P(Aᶜ) = 1 − P(A), inclusion–exclusion for P(A ∪ B), and the union bound P(A₁ ∪ ⋯ ∪ Aₙ) ≤ ∑ P(Aᵢ).

3. **There is no uniform distribution on ℕ.** If every natural number had the same weight c, the total would be 0 if c = 0 and infinite if c > 0, never 1. So "a random natural number" has no meaning without a non-uniform weighting, and phrases such as "the probability that a random integer is even" really mean a limiting density, which is a different notion that is not countably additive.

4. **Conditioning restricts the space and renormalises.** For P(B) > 0, P(A ∣ B) = P(A ∩ B)/P(B) is a new probability on the outcomes of B. Splitting Ω into disjoint B₁, …, Bₙ gives the law of total probability P(A) = ∑ P(A ∣ Bᵢ)P(Bᵢ), and reversing the conditioning gives Bayes' rule P(B ∣ A) = P(A ∣ B)P(B)/P(A).

5. **Bayes' rule makes base rates decisive.** Suppose 1% of a population has a disease, a test detects it 99% of the time and gives a false positive 5% of the time. Then

   ```
   P(disease ∣ positive) = 0.99 · 0.01 / (0.99 · 0.01 + 0.05 · 0.99) = 1/6 ≈ 0.167
   ```

   because the healthy majority produces most positives. Confusing P(positive ∣ disease) with P(disease ∣ positive) is the base-rate fallacy, the central error in [diagnostic reasoning](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/01-probability-and-measurement/bayesian-reasoning.md).

6. **Independence is a numerical coincidence, and mutual independence is stronger than pairwise.** A and B are independent when P(A ∩ B) = P(A)P(B); events A₁, …, Aₙ are mutually independent when the product rule holds for every subfamily. Toss two fair coins and let A be "the first is heads", B "the second is heads", C "the two agree": each pair is independent, but P(A ∩ B ∩ C) = 1/4 ≠ 1/8. Products of spaces, with p(ω₁, ω₂) = p₁(ω₁)p₂(ω₂), are how independent experiments are modelled.

7. **Coincidences are likelier than intuition suggests.** The chance that n people have distinct birthdays, among 365 equally likely days, is (365 · 364 ⋯ (365 − n + 1))/365ⁿ, which falls below 1/2 at n = 23, giving a shared birthday with probability about 0.507. Collisions appear once n is around the square root of the number of possible values, because there are C(n, 2) pairs that could collide; this is why collision-resistant hash functions need outputs twice as long as the security level ([hashing](../../../cs-first-principles/11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md)).

8. **Uncountable sample spaces force measure theory.** For a point chosen uniformly from [0, 1], every single outcome has probability 0, so probabilities cannot be sums of point weights, and not every subset can be assigned a probability consistently. Kolmogorov's 1933 axioms keep countable additivity but restrict events to a σ-algebra, which is the subject of [measure-theoretic probability](../../11-probability-and-statistics/01-measure-theoretic-probability/probability-spaces-and-kolmogorovs-axioms.md) and [measure](../../09-advanced-analysis/01-measure-and-integration/measure-and-sigma-algebras.md). The discrete theory is its special case in which every set is measurable.

## Key concepts
| Term | Meaning |
|---|---|
| Sample space Ω | The set of possible outcomes, here finite or countable |
| Event | A subset of Ω |
| Probability mass function | The weights p(ω) ≥ 0 with total 1 |
| Countable additivity | P of a disjoint countable union is the sum of the probabilities |
| Conditional probability | P(A ∣ B) = P(A ∩ B)/P(B) for P(B) > 0 |
| Law of total probability | P(A) = ∑ P(A ∣ Bᵢ)P(Bᵢ) over a partition |
| Bayes' rule | P(B ∣ A) = P(A ∣ B)P(B)/P(A) |
| Independence | P(A ∩ B) = P(A)P(B), extended to every subfamily for mutual independence |

## How it fits
- **Below:** Events are [sets](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), uniform probabilities are [counts](../01-enumeration/counting-principles-and-binomial-coefficients.md), the union bound is truncated [inclusion–exclusion](../01-enumeration/inclusion-exclusion-and-the-pigeonhole-principle.md), and countable spaces need [countable sets](../../01-sets-and-foundations/02-infinity-and-cardinality/countable-sets.md).
- **Above:** The general theory is [Kolmogorov's axioms](../../11-probability-and-statistics/01-measure-theoretic-probability/probability-spaces-and-kolmogorovs-axioms.md) and [independence](../../11-probability-and-statistics/01-measure-theoretic-probability/independence-and-zero-one-laws.md); Bayes' rule grows into [Bayesian inference](../../11-probability-and-statistics/04-statistical-inference/bayesian-inference.md); the same ideas appear in [probability for computing](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/probability.md) and [for medicine](../../../medicine-first-principles/01-quantitative-and-scientific-foundations/01-probability-and-measurement/probability.md).
- **Siblings:** [Expectation and variance](expectation-and-variance.md) add numerical outcomes; [the probabilistic method](the-probabilistic-method.md) uses positive probability to prove existence.

## Common misconceptions
- **"Pairwise independent events are independent"**: the two-coin example has three pairwise independent events that are not mutually independent.
- **"P(A ∣ B) and P(B ∣ A) are about the same"**: they differ by the factor P(A)/P(B), which with rare conditions can be enormous, as the screening example shows.
- **"Probability zero means impossible"**: in a discrete space it does if every outcome has positive weight, but in continuous spaces every individual outcome has probability zero and one of them happens.

## Go deeper
- Feller, *An Introduction to Probability Theory and Its Applications*, Volume 1 (3rd edition, 1968): the classic development of discrete probability without measure theory.
- Blitzstein and Hwang, *Introduction to Probability* (2nd edition, 2019): conditioning and Bayes' rule taught through counting and stories.
- Grinstead and Snell, *Introduction to Probability* (2nd edition, 1997): an accessible discrete-first course.
