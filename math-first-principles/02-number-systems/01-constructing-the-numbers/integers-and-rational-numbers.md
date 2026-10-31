# Integers and Rational Numbers

> **Layer:** [02 Number Systems](../README.md) › [Constructing the Numbers](README.md)
> **Builds on:** [Natural Numbers and the Peano Axioms](natural-numbers-and-the-peano-axioms.md), [Equivalence Relations and Quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [Relations and Orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md)
> **Enables:** [The Real Numbers](the-real-numbers.md), [Divisibility and the Euclidean Algorithm](../02-elementary-number-theory/divisibility-and-the-euclidean-algorithm.md), [Rings and Ideals](../../05-abstract-algebra/02-rings-and-fields/rings-and-ideals.md), [Fields and Vector Spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/fields-and-vector-spaces.md)

## Essence

ℕ cannot solve 3 + x = 2 or 2 · x = 3. The integers and the rationals repair this without postulating anything new: an integer is a formal difference a − b, recorded as a pair (a, b) of naturals, and a rational is a formal quotient a/b, recorded as a pair of integers with b ≠ 0. Different pairs name the same number, since (5, 2) and (4, 1) both mean 3, so the number is the equivalence class, and ℤ and ℚ are quotient sets in the sense of set theory (01). One move, used twice, does the work: adjoin inverses to an operation that has cancellation.

## Core tenets

1. **Integers are classes of pairs of naturals under (a, b) ~ (c, d) if and only if a + d = b + c, and transitivity needs cancellation.** The pair (a, b) stands for a − b, but subtraction does not exist yet, so the relation uses addition only. If (a, b) ~ (c, d) and (c, d) ~ (e, f), adding gives a + d + c + f = b + c + d + e, and cancelling c + d gives a + f = b + e. Without cancellation the construction fails: in ℕ ∪ {∞} with ∞ + n = ∞, (0, 0) ~ (∞, ∞) ~ (1, 0) but (0, 0) ≁ (1, 0).

2. **Addition and multiplication are defined on representatives, and the content is that the answer does not depend on the choice.** Set [(a, b)] + [(c, d)] = [(a + c, b + d)] and [(a, b)] · [(c, d)] = [(ac + bd, ad + bc)], which is what (a − b)(c − d) expands to. Replacing a pair by an equivalent one changes the output only to an equivalent pair, a short check by distributivity and cancellation. Then n ↦ [(n, 0)] embeds ℕ, [(b, a)] is the negative of [(a, b)], and every integer is n or −n. ℤ is the universal way to make ℕ a ring: every map from ℕ into a ring that respects + and · extends uniquely to ℤ.

3. **Rationals are classes of pairs (a, b) with b ≠ 0 under (a, b) ~ (c, d) if and only if ad = bc, and transitivity needs the absence of zero divisors.** From ad = bc and cf = de, multiplying gives adf = bcf = bde, and cancelling d ≠ 0 gives af = be. Allowing b = 0 breaks this: (1, 2) ~ (0, 0) and (0, 0) ~ (1, 3), but (1, 2) ≁ (1, 3). Forcing transitivity anyway would make all fractions equal and collapse ℚ to a point, which is the precise sense in which one cannot divide by zero.

4. **The rules for fractions make ℚ a field, the smallest one containing ℤ.** Set a/b + c/d = (ad + bc)/bd and (a/b) · (c/d) = ac/bd; again the work is independence of representatives. Each non-zero a/b has inverse b/a. Any field containing ℤ contains a unique copy of ℚ, the quotients of its integers. The same construction turns any integral domain into its field of fractions (05); polynomials over a field give rational functions.

5. **ℚ is an ordered field that is dense and Archimedean.** With positive denominators, a/b < c/d means ad < bc, and this order is compatible with addition and with multiplication by positives. Between any two rationals lies their average, so no rational has a neighbour. Every rational lies below some integer (the Archimedean property), so ℚ has no infinitely large or infinitely small elements.

6. **Density is not completeness: ℚ has holes, and √2 marks the first.** Suppose p/q is a fraction with p² = 2q² and the smallest possible positive denominator q. Since 1 < p/q < 2, we have 0 < p − q < q, and (2q − p)² = 2(p − q)², so (2q − p)/(p − q) is a representation with a smaller denominator, a contradiction. So the set {x ∈ ℚ : x² < 2} is bounded above but has no least upper bound in ℚ.

7. **ℚ is countable, and its decimals are exactly the eventually periodic ones.** Listing pairs (a, b) by |a| + b shows countability. Long division of a by b has only b possible remainders, so by the pigeonhole principle some remainder repeats within b steps and the digits cycle from there: 1/7 = 0.142857142857…, with period 6. Conversely, an eventually periodic decimal sums a geometric series and is rational, so a decimal such as 0.1010010001… is irrational.

## Key concepts

| Term | Meaning |
|---|---|
| Formal difference | A pair (a, b) of naturals standing for a − b |
| Formal quotient | A pair (a, b) of integers with b ≠ 0, standing for a/b |
| Well-defined | Said of an operation on classes whose result does not depend on the representatives |
| Cancellation | a + c = b + c implies a = b; ac = bc with c ≠ 0 implies a = b |
| Integral domain | A commutative ring with 1 ≠ 0 in which ab = 0 forces a = 0 or b = 0 |
| Field of fractions | The smallest field containing an integral domain, built from formal quotients |
| Dense order | Between any two elements lies a third |
| Archimedean | Every element lies below some natural number |

## How it fits

- **Below:** pairs and quotient sets (01) supply the construction and relations (01) the order; ℕ and its cancellation laws come from the [Peano axioms](natural-numbers-and-the-peano-axioms.md).
- **Above:** ℤ is the model ring for rings and ideals (05) and ℚ the first field of linear algebra (04); divisibility in ℤ opens elementary number theory.
- **Siblings:** with the algebraic gaps closed, [the real numbers](the-real-numbers.md) close the order gap that √2 exposes, by completion; [extending number systems](extending-number-systems.md) completes ℚ in other ways, giving the p-adic numbers.

## Common misconceptions

- **"−1 is just a new symbol added to ℕ"**: adding symbols proves nothing; the pair construction shows that arithmetic with negatives has a model built from ℕ alone, and it forces (−1)(−1) = 1, since [(0, 1)] · [(0, 1)] = [(1, 0)].
- **"1/2 and 2/4 are different numbers that happen to be equal"**: they are two names for one class, and every operation must give the same class whichever names it is fed.
- **"Dense means no gaps"**: ℚ is dense yet misses √2, π and almost every point of the line; density is about the order between points, completeness about the existence of limits.

## Go deeper

- Herbert Enderton, *Elements of Set Theory* (1977): builds ℤ, ℚ and ℝ inside set theory with every verification.
- Edmund Landau, *Foundations of Analysis* (German original 1930): builds positive fractions from pairs of naturals and checks every law; negative numbers enter only with the reals.
