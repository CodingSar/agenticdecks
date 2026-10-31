# Counting Principles and Binomial Coefficients

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Enumeration](README.md)
> **Builds on:** [Mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md), [Sets and set operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md), [Natural numbers and the Peano axioms](../../02-number-systems/01-constructing-the-numbers/natural-numbers-and-the-peano-axioms.md)
> **Enables:** [Inclusion–exclusion and the pigeonhole principle](inclusion-exclusion-and-the-pigeonhole-principle.md), [Generating functions](generating-functions.md), [Finite probability spaces](../03-discrete-probability/finite-probability-spaces.md), [Group actions](../../05-abstract-algebra/01-groups/group-actions.md), [Combinatorics in computing](../../../cs-first-principles/01-mathematical-foundations/03-discrete-mathematics/combinatorics.md)

## Essence
Counting answers "how many?" for a finite set without listing it. The subject rests on one idea: two finite sets have the same size exactly when there is a bijection between them, so a hard count is solved by a bijection to a set that is easy to count, or by counting one set in two ways. From this come the sum and product rules, the counts of functions, arrangements and subsets, and the binomial coefficient C(n, k), the number of k-element subsets of an n-element set. Every binomial identity says that two counts of one set agree.

## Core tenets
1. **Size is defined by bijection, so counting means building bijections.** A set has size n when it is in bijection with {1, …, n}; n is unique because, by induction on n, no injection maps {1, …, n + 1} into {1, …, n}. A bijection A → B therefore proves ∣A∣ = ∣B∣. Subsets of an n-set S correspond to indicator functions S → {0, 1}, so there are 2ⁿ of them.

2. **The sum and product rules are the two basic operations.** For disjoint A and B, ∣A ∪ B∣ = ∣A∣ + ∣B∣, and always ∣A × B∣ = ∣A∣ · ∣B∣; both follow by induction on ∣B∣. The product rule also covers a sequence of choices whose number of options is fixed at each stage even when the options depend on earlier choices, which gives n(n − 1)⋯(n − k + 1) injections from a k-set into an n-set. Without disjointness the sum rule overcounts; inclusion–exclusion is the correction.

3. **Functions, arrangements and selections have closed counts.** There are nᵏ functions from a k-set to an n-set, since each element chooses its image independently, and n! permutations of an n-set. Whether order matters and whether repetition is allowed gives four cases:

   ```
                         order matters      order ignored
   repetition allowed    nᵏ                 C(n + k − 1, k)
   no repetition         n!/(n − k)!        C(n, k)
   ```

4. **C(n, k) = n!/(k!(n − k)!) because each subset appears k! times among ordered selections.** Count injective sequences of length k from an n-set twice: directly, n!/(n − k)!; or choose the subset in C(n, k) ways and order it in k! ways. Equating gives the formula and shows the quotient is an integer. Counting one set twice is double counting, the most productive technique in combinatorics.

5. **Pascal's rule and the binomial theorem come from following one element or one factor.** A k-subset of an n-set either contains a fixed element or not, so C(n, k) = C(n − 1, k − 1) + C(n − 1, k). In (a + b)ⁿ each term picks a or b from each of the n factors, and terms with k copies of b match k-subsets of the factors, so (a + b)ⁿ = ∑ C(n, k) aⁿ⁻ᵏ bᵏ. Collecting terms uses ab = ba: for non-commuting matrices, (A + B)² = A² + AB + BA + B² and the theorem fails.

6. **Stars and bars converts multisets into subsets.** A size-k multiset from n types is a row of k stars cut by n − 1 bars into n groups, so it is a choice of k star positions out of n + k − 1: C(n + k − 1, k). The same bijection counts non-negative integer solutions of x₁ + ⋯ + xₙ = k. The multinomial coefficient n!/(k₁! ⋯ kᵣ!) counts words with kᵢ copies of the i-th letter.

7. **Identities are proved by a double count or an explicit bijection.** Vandermonde's identity C(m + n, k) = ∑ C(m, i) C(n, k − i) counts k-subsets of a disjoint union of an m-set and an n-set by how many elements come from each part. Setting a = 1, b = −1 in the binomial theorem gives ∑ (−1)ᵏ C(n, k) = 0 for n ≥ 1, and "toggle a fixed element" pairs even-sized subsets with odd-sized ones, which explains why.

8. **Counting up to symmetry and estimating large counts need more structure.** Counting necklaces up to rotation means counting orbits, done by Burnside's lemma in [group actions](../../05-abstract-algebra/01-groups/group-actions.md). Estimating n! needs limits: Stirling's formula n! ~ √(2πn)(n/e)ⁿ belongs to [estimates and inequalities](../../06-real-analysis/01-limits-and-convergence/estimates-and-inequalities.md). Exact counting needs neither.

## Key concepts
| Term | Meaning |
|---|---|
| Bijection principle | Finite sets in bijection have the same size |
| Sum rule | A disjoint union has the sum of the sizes |
| Product rule | A product, or a sequence of choices with fixed numbers of options, has the product of the sizes |
| Falling factorial | n(n − 1)⋯(n − k + 1), the number of injections from a k-set into an n-set |
| Binomial coefficient | C(n, k), the number of k-element subsets of an n-set; 0 when k > n |
| Multiset coefficient | C(n + k − 1, k), the number of size-k multisets from n types |
| Multinomial coefficient | n!/(k₁! ⋯ kᵣ!), the number of words with prescribed letter counts |
| Double counting | Proving an identity by counting one set in two ways |

## How it fits
- **Below:** Finite sets and bijections come from [sets](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md) and [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md); every "by induction on n" rests on [mathematical induction](../../00-logic-and-proof/02-methods-of-proof/mathematical-induction.md).
- **Above:** Finite probability is a count divided by a count ([finite probability spaces](../03-discrete-probability/finite-probability-spaces.md)); the binomial theorem returns as the binomial distribution ([expectation and variance](../03-discrete-probability/expectation-and-variance.md)) and, through [the central limit theorem](../../11-probability-and-statistics/02-limit-theorems/the-central-limit-theorem.md), as the bell curve.
- **Siblings:** [Inclusion–exclusion](inclusion-exclusion-and-the-pigeonhole-principle.md) corrects the sum rule for overlaps; [generating functions](generating-functions.md) package the row C(n, 0), …, C(n, n) as (1 + x)ⁿ; [combinatorial sequences](combinatorial-sequences.md) catalogue the numbers these rules produce.

## Common misconceptions
- **"Choosing k items from n with repetition gives nᵏ/k! possibilities"**: dividing by k! assumes every multiset has k! orderings, but one with repeats has fewer. For n = k = 2 the formula gives 2, yet there are 3 multisets, {a, a}, {a, b} and {b, b}.
- **"A bijective proof is only an illustration"**: a bijection between finite sets is a complete proof that they have the same size, since that is what equal size means.
- **"C(n, k) only makes sense for 0 ≤ k ≤ n"**: as a count it is 0 for k > n, and r(r − 1)⋯(r − k + 1)/k! defines C(r, k) for any number r, so C(−1, k) = (−1)ᵏ. This drives the generalised binomial theorem in [generating functions](generating-functions.md).

## Go deeper
- Graham, Knuth and Patashnik, *Concrete Mathematics* (2nd edition, 1994): chapter 5 is the standard working treatment of binomial identities.
- van Lint and Wilson, *A Course in Combinatorics* (2nd edition, 2001): a rigorous first course built from these principles.
- Benjamin and Quinn, *Proofs that Really Count* (2003): binomial and Fibonacci identities proved purely by counting.
