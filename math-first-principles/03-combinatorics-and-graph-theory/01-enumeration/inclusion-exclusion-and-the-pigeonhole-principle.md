# Inclusion–Exclusion and the Pigeonhole Principle

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Enumeration](README.md)
> **Builds on:** [Counting principles and binomial coefficients](counting-principles-and-binomial-coefficients.md), [Sets and set operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md), [Primes and unique factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md)
> **Enables:** [Combinatorial sequences](combinatorial-sequences.md), [Finite probability spaces](../03-discrete-probability/finite-probability-spaces.md), [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md), [Posets and extremal set theory](../04-extremal-combinatorics/posets-and-extremal-set-theory.md), [Sieves and additive problems](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md)

## Essence
Two complementary tools for finite sets. Inclusion–exclusion computes the size of a union of overlapping sets from the sizes of their intersections, adding and subtracting in turn; it turns "count the objects with none of the bad properties" into a signed sum of easy counts. The pigeonhole principle says that if more than km objects go into m boxes, some box receives more than k; it proves that something exists without saying where. One counts exactly, the other forces structure, and they are the seeds of sieve methods and of Ramsey theory.

## Core tenets
1. **Inclusion–exclusion is the binomial identity ∑ (−1)ʲ C(m, j) = 0 in disguise.** The formula reads

   ```
   |A₁ ∪ ⋯ ∪ Aₙ| = ∑ |Aᵢ| − ∑ |Aᵢ ∩ Aⱼ| + ∑ |Aᵢ ∩ Aⱼ ∩ Aₖ| − ⋯ + (−1)ⁿ⁺¹ |A₁ ∩ ⋯ ∩ Aₙ|
   ```

   with each sum over indices i < j < k. An element lying in exactly m ≥ 1 of the sets is counted C(m, 1) − C(m, 2) + ⋯ ± C(m, m) = 1 − (1 − 1)ᵐ = 1 time, and an element in none is counted 0 times. No independence, symmetry or equal sizes are needed.

2. **Truncating the sum gives alternating bounds.** Stopping after r terms counts an element of m sets 1 − (−1)ʳ C(m − 1, r) times, by Pascal's rule, so odd r overestimates the union and even r underestimates it: the Bonferroni inequalities. The case r = 1 is the union bound ∣A₁ ∪ ⋯ ∪ Aₙ∣ ≤ ∑ ∣Aᵢ∣, which in probability becomes the workhorse of the probabilistic method.

3. **Derangements, surjections and Euler's φ are signed sums.** Let Aᵢ be the permutations of {1, …, n} fixing i; then ∣Aᵢ ∩ Aⱼ ∩ ⋯∣ depends only on how many indices are fixed, so the number of derangements (permutations with no fixed point) is D(n) = ∑ (−1)ʲ C(n, j)(n − j)! = n! ∑ (−1)ʲ/j!, the nearest integer to n!/e for n ≥ 1. Excluding each missed value gives ∑ (−1)ʲ C(k, j)(k − j)ⁿ surjections from an n-set onto a k-set. Excluding multiples of each prime p dividing n gives Euler's totient φ(n) = n ∏ (1 − 1/p), the number of integers in {1, …, n} coprime to n.

4. **Inclusion–exclusion is Möbius inversion on the subsets of a set.** If f(S) = ∑ g(T) over all T ⊇ S, then g(S) = ∑ (−1)^∣T ∖ S∣ f(T). Replacing subsets by divisors gives the Möbius function of number theory; replacing them by any finite partially ordered set gives Rota's general Möbius inversion. Carried to large ranges with error terms, the same idea becomes the sieve methods of [analytic number theory](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md).

5. **Pigeonhole: if N objects lie in m boxes, some box holds at least ⌈N/m⌉.** Otherwise every box holds at most ⌈N/m⌉ − 1 < N/m objects and the total is below N. Equivalently, a map from an N-set to an m-set with N > m is not injective. The principle is trivial; its power lies in choosing the pigeons and the boxes.

6. **Well-chosen boxes prove surprising facts.** Among any n + 1 numbers from {1, …, 2n}, one divides another: write each as 2ᵃ · b with b odd; only n odd values of b exist, so two numbers share b, and the one with the smaller power of 2 divides the other. For real α and integer N ≥ 1, the N + 1 fractional parts of 0, α, …, Nα lie in N intervals of length 1/N, so two lie in one interval, giving integers p and 1 ≤ q ≤ N with ∣qα − p∣ < 1/N (Dirichlet's approximation theorem).

7. **Every sequence of n² + 1 distinct reals has a monotone subsequence of length n + 1 (Erdős and Szekeres, 1935).** Label each term with the length of the longest increasing subsequence starting there. If no label exceeds n, some n + 1 terms share a label, and they decrease: if an earlier one were smaller than a later one, prepending it would make its label larger. The bound is sharp: n decreasing blocks of n increasing terms have no monotone subsequence of length n + 1. This is an early Ramsey-type theorem.

8. **Pigeonhole proves existence, not construction, and it needs finiteness.** It shows that two of any 13 people share a birth month but not which two. The map n ↦ 2n injects ℕ into a proper subset of itself, so the principle fails for infinite sets. What survives is the infinite pigeonhole principle, that infinitely many objects in finitely many boxes put infinitely many in one box, which drives infinite [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md).

## Key concepts
| Term | Meaning |
|---|---|
| Inclusion–exclusion | The size of a union as an alternating sum of the sizes of intersections |
| Bonferroni inequalities | Truncations of inclusion–exclusion alternately over- and underestimate |
| Union bound | ∣A₁ ∪ ⋯ ∪ Aₙ∣ ≤ ∑ ∣Aᵢ∣ |
| Derangement | A permutation with no fixed point; there are D(n) of an n-set |
| Euler's totient φ(n) | The number of integers in {1, …, n} coprime to n |
| Möbius inversion | Inverting sums over a partial order; inclusion–exclusion is the subset case |
| Pigeonhole principle | N objects in m boxes put at least ⌈N/m⌉ in some box |
| Monotone subsequence | A subsequence that is increasing or decreasing |

## How it fits
- **Below:** The sum rule and the binomial theorem come from [counting principles](counting-principles-and-binomial-coefficients.md); unions and intersections from [sets](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md); the primes behind φ from [unique factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md).
- **Above:** The union bound opens [finite probability spaces](../03-discrete-probability/finite-probability-spaces.md) and [the probabilistic method](../03-discrete-probability/the-probabilistic-method.md); pigeonhole is the base case of [Ramsey theory](../04-extremal-combinatorics/ramsey-theory.md); Möbius inversion on orders returns in [posets and extremal set theory](../04-extremal-combinatorics/posets-and-extremal-set-theory.md).
- **Siblings:** [Generating functions](generating-functions.md) give a second route to D(n); [combinatorial sequences](combinatorial-sequences.md) relate surjections to Stirling numbers.

## Common misconceptions
- **"Inclusion–exclusion needs independent or equal-sized sets"**: it is an exact identity for any finite sets. Symmetry only makes the terms easy to evaluate, as for derangements.
- **"With many guests, someone almost surely gets their own hat back"**: the chance that no guest does is D(n)/n!, which tends to 1/e ≈ 0.368 and is already 0.375 for n = 4. It does not tend to 0.
- **"The pigeonhole principle is too simple to prove anything deep"**: Dirichlet approximation, the Erdős–Szekeres theorem and the finite Ramsey theorem are all pigeonhole arguments; the depth is in the choice of boxes.

## Go deeper
- Aigner and Ziegler, *Proofs from THE BOOK* (1998): its pigeonhole and double-counting chapter collects the classic applications.
- Lovász, *Combinatorial Problems and Exercises* (2nd edition, 1993): graded problems on sieves and inclusion–exclusion, with full solutions.
- Stanley, *Enumerative Combinatorics*, Volume 1 (2nd edition, 2012): its chapters on sieve methods and on posets develop inclusion–exclusion into Möbius inversion.
