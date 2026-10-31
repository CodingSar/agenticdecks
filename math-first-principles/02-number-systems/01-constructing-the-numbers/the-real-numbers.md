# The Real Numbers

> **Layer:** [02 Number Systems](../README.md) › [Constructing the Numbers](README.md)
> **Builds on:** [Integers and Rational Numbers](integers-and-rational-numbers.md), [Relations and Orders](../../01-sets-and-foundations/01-sets-relations-and-functions/relations-and-orders.md), [Equivalence Relations and Quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [Cantor's Diagonal Argument](../../01-sets-and-foundations/02-infinity-and-cardinality/cantors-diagonal-argument.md)
> **Enables:** [Sequences and Limits](../../06-real-analysis/01-limits-and-convergence/sequences-and-limits.md), [Completeness and the Contraction Mapping Principle](../../06-real-analysis/03-metric-spaces/completeness-and-the-contraction-mapping-principle.md), [The Complex Numbers](the-complex-numbers.md), [p-adic Numbers and Local Fields](../../12-number-theory-and-algebraic-geometry/01-algebraic-number-theory/p-adic-numbers-and-local-fields.md), [Floating Point, Conditioning and Stability](../../14-applied-and-computational-mathematics/01-numerical-analysis/floating-point-conditioning-and-stability.md)

## Essence

ℚ is dense but full of holes: the rationals whose square is below 2 have no rational least upper bound. The real numbers fill every such hole. Two constructions, both published in 1872, do it: Dedekind takes a real number to be a cut, the set of rationals below it, and Cantor a class of Cauchy sequences of rationals. Either way the result is a complete ordered field, in which every non-empty set bounded above has a least upper bound, and any two such fields are isomorphic. Analysis runs on completeness: limits, the intermediate value theorem and √2 itself all fail in ℚ.

## Core tenets

1. **ℚ has a gap at √2.** Let A = {x ∈ ℚ : x ≤ 0 or x² < 2}, which is bounded above by 2. No rational u > 0 is its least upper bound. If u² > 2, the Newton step u′ = (u² + 2)/(2u) is a smaller upper bound, since u − u′ = (u² − 2)/(2u) > 0 and u′² − 2 = (u² − 2)²/(4u²) > 0. If u² < 2, then 4u/(u² + 2) is a larger element of A. And u² = 2 has no rational solution.

2. **Dedekind: a real number is a cut, a non-empty proper subset of ℚ that is closed downwards and has no largest element.** The rational r becomes the cut {x ∈ ℚ : x < r}, and √2 becomes A. Cuts are ordered by inclusion, and the least upper bound of a bounded set of cuts is their union, which is again a cut, so completeness is almost built in. Addition is elementwise, A + B = {a + b : a ∈ A, b ∈ B}; multiplication needs cases by sign.

3. **Cantor: a real number is a class of Cauchy sequences of rationals, two sequences being equivalent when their difference tends to 0.** A sequence is Cauchy when, for every rational ε > 0, its terms are eventually within ε of each other; only rationals are mentioned, so the definition is legitimate before ℝ exists. Sums and products are taken term by term. The delicate lemma is inversion: a Cauchy sequence not equivalent to 0 is eventually bounded away from 0, so its reciprocals are eventually defined and Cauchy. The same method completes any metric space, and with the p-adic distance on ℚ it yields the p-adic numbers.

4. **Any two complete ordered fields are isomorphic, by exactly one isomorphism.** Each contains a copy of ℚ, and completeness makes every element the supremum of the rationals below it, so the map sending sup{r ∈ ℚ : r < x} to the matching supremum is forced, and it preserves + and ·. Indeed the identity is the only field automorphism of ℝ: it must fix ℚ, and it preserves order, because the non-negative reals are exactly the squares. So every construction gives the same ℝ.

5. **Completeness implies the Archimedean property, which excludes infinitesimals.** If ℕ had an upper bound in ℝ it would have a least one, s; but n + 1 ≤ s for every n gives n ≤ s − 1, a smaller bound. So no positive real lies below every 1/n. Other ordered fields do have infinitesimals: in the rational functions ℝ(x), ordered so that x exceeds every real, 1/x is one, and that field is not complete.

6. **Completeness has several equivalent forms, each a tool of analysis.** In an ordered field these are equivalent: every non-empty set bounded above has a least upper bound; every bounded increasing sequence converges; every bounded sequence has a convergent subsequence (Bolzano–Weierstrass); the field is Archimedean and every Cauchy sequence converges. All of them fail in ℚ. The intermediate value theorem is proved by taking the supremum of the points where a function is negative, and in ℚ the polynomial x² − 2 is negative at 1, positive at 2 and never zero.

7. **ℝ is uncountable, so almost every real can never be named.** Cantor proved this in 1874 by nested intervals; his diagonal argument of 1891 gives another proof, here in decimal form: from any list of reals in (0, 1), build a decimal whose n-th digit differs from that of the n-th number, avoiding 0 and 9 so that no number has two expansions. Formulas and programs are finite strings, of which there are countably many; the computable reals, whose digits some program prints (Turing, 1936), form a countable field.

## Key concepts

| Term | Meaning |
|---|---|
| Least upper bound | The smallest upper bound of a set, also called its supremum |
| Complete ordered field | An ordered field in which every non-empty set bounded above has a least upper bound |
| Dedekind cut | A non-empty, proper, downward-closed set of rationals with no largest element |
| Cauchy sequence | A sequence whose terms eventually stay within any given ε > 0 of one another |
| Archimedean property | Every element lies below some natural number |
| Computable real | A real whose decimal digits some program can print one by one |

## How it fits

- **Below:** built from [integers and rational numbers](integers-and-rational-numbers.md), with orders and quotient sets from 01; uncountability is Cantor's diagonal argument (01).
- **Above:** real analysis (06) starts from completeness; completing metric spaces (06) generalises Cantor's construction; the p-adic numbers (12) complete ℚ for another distance; floating point (14) approximates ℝ by finitely many rationals.
- **Siblings:** [the complex numbers](the-complex-numbers.md) add the root of x² + 1 that ℝ lacks while keeping completeness; [algebraic and transcendental numbers](algebraic-and-transcendental-numbers.md) sort the new reals by whether they solve a polynomial with integer coefficients.

## Common misconceptions

- **"0.999… is slightly less than 1"**: a decimal denotes the limit of its partial sums, and 0.9, 0.99, 0.999, … converge to 1; two reals with no positive distance between them are equal.
- **"A real number is its decimal expansion"**: an expansion is one name for it; 0.999… and 1.000… name the same real, and most reals have no finite description at all.
- **"Completeness is an algebraic property"**: the real algebraic numbers form a countable field in which every polynomial that changes sign has a root, yet that field has holes everywhere; and complete ℝ has no root of x² + 1.

## Go deeper

- Richard Dedekind, *Stetigkeit und irrationale Zahlen* (1872): the cut construction, with its claim to give the first real proof that √2 · √3 = √6.
- Walter Rudin, *Principles of Mathematical Analysis* (3rd edition, 1976): the appendix to chapter 1 builds ℝ by cuts in full.
- Terence Tao, *Analysis I* (2006): builds ℝ from Cauchy sequences, every step checked.
