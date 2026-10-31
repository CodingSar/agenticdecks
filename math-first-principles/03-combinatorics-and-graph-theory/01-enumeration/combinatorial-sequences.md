# Combinatorial Sequences

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Enumeration](README.md)
> **Builds on:** [Counting principles and binomial coefficients](counting-principles-and-binomial-coefficients.md), [Inclusion–exclusion and the pigeonhole principle](inclusion-exclusion-and-the-pigeonhole-principle.md), [Generating functions](generating-functions.md), [Recurrence relations](recurrence-relations.md)
> **Enables:** [Trees](../02-graph-theory/trees.md), [Representations of finite groups](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md), [Modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md), [Series](../../06-real-analysis/01-limits-and-convergence/series.md)

## Essence
A handful of number sequences recur across combinatorics because the same few constructions recur: the Fibonacci numbers, the Catalan numbers, the Stirling and Bell numbers, and the partition numbers. Each counts many apparently unrelated families of objects, and each comes with a recurrence, a generating function and a growth rate. Knowing them turns a new counting problem into recognition: compute the first terms, recognise the sequence, then prove the match with a bijection. The sequences also mark the boundaries of the method, from closed forms (Catalan) to recurrences without closed form (partitions) whose asymptotics need analysis and whose congruences need modular forms.

## Core tenets
1. **The Fibonacci numbers count tilings, and tilings prove their identities.** A strip of n cells tiled by squares and dominoes starts with a square or a domino, so the number of tilings satisfies the Fibonacci recurrence and equals Fₙ₊₁. Splitting a tiling of m + n cells at the boundary after cell m, which is either free or covered by a domino, gives Fₘ₊ₙ₊₁ = Fₘ₊₁Fₙ₊₁ + FₘFₙ with no algebra. Fibonacci numbers also count binary strings with no two adjacent 1s.

2. **The Catalan numbers Cₙ = C(2n, n)/(n + 1) count recursively balanced structures.** Binary trees with n nodes, sequences of n pairs of balanced parentheses, lattice paths of n up and n down steps that never go below the start (Dyck paths), and triangulations of a convex (n + 2)-gon all split at a first return or a root into two smaller pieces, giving Cₙ₊₁ = C₀Cₙ + C₁Cₙ₋₁ + ⋯ + CₙC₀. Stanley catalogues more than two hundred such families.

3. **The reflection principle proves the Catalan formula bijectively.** Of the C(2n, n) paths with n up and n down steps, those that go below the start touch level −1; reflecting the part after the first touch maps them bijectively onto all paths ending at level −2, of which there are C(2n, n + 1). Hence Cₙ = C(2n, n) − C(2n, n + 1) = C(2n, n)/(n + 1). The same reflection solves the ballot problem.

4. **Stirling numbers of the second kind count set partitions.** S(n, k) is the number of ways to split an n-set into k non-empty unlabelled blocks. The element n is either a block on its own or joins one of k blocks of a partition of the rest, so S(n, k) = S(n − 1, k − 1) + kS(n − 1, k). Labelling the blocks gives k! S(n, k) surjections, matching the inclusion–exclusion count, and the Bell number Bₙ = S(n, 0) + ⋯ + S(n, n) counts all partitions, with exponential generating function exp(eˣ − 1).

5. **Unsigned Stirling numbers of the first kind count permutations by cycles.** c(n, k) is the number of permutations of an n-set with k cycles. Inserting element n either as a new fixed point or directly after one of the other n − 1 elements in its cycle gives

   ```
   ∑ c(n, k) xᵏ = x(x + 1)(x + 2)⋯(x + n − 1)
   ```

   so a random permutation has on average 1 + 1/2 + ⋯ + 1/n cycles. With signs, the two kinds of Stirling numbers are inverse matrices converting between powers xⁿ and falling factorials.

6. **The partition numbers have a recurrence but no closed form.** Euler's pentagonal number theorem, ∏ (1 − xᵏ) = ∑ (−1)ʲ x^(j(3j − 1)/2) over all integers j, inverts the product ∑ p(n)xⁿ = ∏ 1/(1 − xᵏ) into p(n) = p(n − 1) + p(n − 2) − p(n − 5) − p(n − 7) + ⋯. Hardy and Ramanujan (1918) found p(n) ~ exp(π√(2n/3))/(4n√3) by the circle method, and Ramanujan's congruences p(5n + 4) ≡ 0 (mod 5), p(7n + 5) ≡ 0 (mod 7) and p(11n + 6) ≡ 0 (mod 11) are explained by [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md).

7. **Growth rates sort sequences into classes.** C(n, k) for fixed k grows polynomially; Fₙ ~ φⁿ/√5 and Cₙ ~ 4ⁿ/(√π n^(3/2)) grow exponentially; p(n) grows faster than any polynomial but slower than any exponential; n! and Bₙ grow faster than any exponential. The exponential rate equals the reciprocal of the radius of convergence of the generating function, which is why asymptotics lead to [series](../../06-real-analysis/01-limits-and-convergence/series.md) and complex analysis.

8. **Matching first terms suggests a theorem but proves nothing.** The On-Line Encyclopedia of Integer Sequences (OEIS) lets anyone look up a sequence from its first terms, and many bijections were found this way. But a guess becomes a theorem only through a proof: a bijection, a shared recurrence with shared initial values, or equal generating functions.

## Key concepts
| Term | Meaning |
|---|---|
| Fibonacci number Fₙ | F₀ = 0, F₁ = 1, Fₙ = Fₙ₋₁ + Fₙ₋₂; counts tilings by squares and dominoes |
| Catalan number Cₙ | C(2n, n)/(n + 1); counts binary trees, Dyck paths and triangulations |
| Dyck path | A path of up and down steps that never goes below its start and ends at its start level |
| Stirling number S(n, k) | Partitions of an n-set into k non-empty blocks |
| Bell number Bₙ | The number of partitions of an n-set |
| Stirling number c(n, k) | Permutations of an n-set with k cycles |
| Partition number p(n) | Ways to write n as an unordered sum of positive integers |
| Reflection principle | Reflecting a path after its first touch of a line to count paths that cross it |

## How it fits
- **Below:** The sequences come from [counting principles](counting-principles-and-binomial-coefficients.md), [inclusion–exclusion](inclusion-exclusion-and-the-pigeonhole-principle.md), [generating functions](generating-functions.md) and [recurrences](recurrence-relations.md).
- **Above:** Catalan structures are [trees](../02-graph-theory/trees.md); partitions index the irreducible [representations](../../05-abstract-algebra/04-modules-and-representations/representations-of-finite-groups.md) of the symmetric group; partition congruences are [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md); computing uses the same numbers to count data structures ([combinatorics in computing](../../../cs-first-principles/01-mathematical-foundations/03-discrete-mathematics/combinatorics.md)).
- **Siblings:** This leaf is the catalogue; the other four enumeration leaves are the methods that produce it.

## Common misconceptions
- **"A pattern in the first terms continues"**: joining n points on a circle by all chords cuts the disc into at most 1, 2, 4, 8, 16 regions for n = 1 to 5, but 31, not 32, for n = 6.
- **"The partition numbers grow exponentially"**: log p(n) grows like π√(2n/3), so p(n) is subexponential, although it still outgrows every polynomial.
- **"Catalan numbers are about trees"**: trees are one of hundreds of families; the common feature is a first-return decomposition into two smaller pieces.

## Go deeper
- Graham, Knuth and Patashnik, *Concrete Mathematics* (2nd edition, 1994): chapter 6 on special numbers covers Stirling, Fibonacci and harmonic numbers.
- Stanley, *Catalan Numbers* (2015): the definitive catalogue of Catalan families.
- Andrews, *The Theory of Partitions* (1976): partitions from Euler's identities to Ramanujan's congruences.
