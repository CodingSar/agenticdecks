# Additive Combinatorics

> **Layer:** [03 Combinatorics and Graph Theory](../README.md) › [Extremal Combinatorics](README.md)
> **Builds on:** [Ramsey theory](ramsey-theory.md), [Extremal graph theory](extremal-graph-theory.md), [Primes and unique factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md), [Modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md)
> **Enables:** [Sieves and additive problems](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md), [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md), [Ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md), [Primes in arithmetic progressions](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/primes-in-arithmetic-progressions.md), [Computers and proof](../../15-mathematics-in-context/computers-and-proof.md)

## Essence
Additive combinatorics studies the additive structure of sets: when a set of integers, or of elements of an abelian group, must contain arithmetic progressions, and what it means for a set to be nearly closed under addition. Its two central themes mirror each other. Density theorems, such as Szemerédi's, say that any large enough set contains structure. Inverse theorems, such as Freiman's, say that a set with few distinct sums must be structured. Both rest on a dichotomy between structure and randomness: a set either looks random, and then counting gives the patterns, or it correlates with some structure that can be exploited. The tools come from graph theory, Fourier analysis and ergodic theory, and the subject's most famous result is that the primes contain arbitrarily long arithmetic progressions.

## Core tenets
1. **Small sumsets: ∣A + A∣ ≥ 2∣A∣ − 1, with equality only for arithmetic progressions.** The sumset A + B is the set of all sums a + b with a ∈ A and b ∈ B. If a₁ < ⋯ < aₖ, the sums a₁ + a₁ < a₁ + a₂ < a₂ + a₂ < a₂ + a₃ < ⋯ < aₖ + aₖ are 2k − 1 distinct elements. A random set has about ∣A∣²/2 sums, so a small sumset signals structure. In ℤ/pℤ with p prime, the Cauchy–Davenport theorem gives ∣A + B∣ ≥ min(p, ∣A∣ + ∣B∣ − 1) ([modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md)).

2. **Freiman's theorem: sets with small doubling are dense in generalised progressions.** If A ⊂ ℤ is finite and ∣A + A∣ ≤ K∣A∣, then A sits inside a generalised arithmetic progression, a set {a + x₁d₁ + ⋯ + xᵣdᵣ : 0 ≤ xᵢ < Nᵢ}, whose dimension r and size relative to ∣A∣ are bounded in terms of K alone. Ruzsa's 1994 proof made the theorem accessible. Its key tool is the Plünnecke–Ruzsa inequality: if ∣A + A∣ ≤ K∣A∣, then any sum or difference of m copies of A has at most Kᵐ∣A∣ elements.

3. **The polynomial Freiman–Ruzsa (PFR) conjecture over 𝔽₂ⁿ was proved in 2023.** For a set A in the vector space 𝔽₂ⁿ over the field with two elements, small doubling ∣A + A∣ ≤ K∣A∣ should mean that A is covered by a number of cosets of a subgroup of size at most ∣A∣, with that number polynomial in K rather than exponential. Gowers, Green, Manners and Tao proved this in 2023 by an entropy argument. The proof was then formally verified in the Lean proof assistant ([computers and proof](../../15-mathematics-in-context/computers-and-proof.md)).

4. **Roth (1953): a set of integers with positive upper density contains a three-term arithmetic progression.** Upper density is the largest limiting proportion of {1, …, N} that the set occupies. Roth used Fourier analysis. If A has no progressions, its Fourier transform has a large coefficient, so A is denser on a long sub-progression, and iterating this density increment gives a contradiction ([Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md)). Behrend (1946) built progression-free subsets of {1, …, N} with N/exp(c · √(ln N)) elements. Kelley and Meka (2023) proved an upper bound of the same exponential-of-a-root-of-a-logarithm shape.

5. **Szemerédi (1975): positive upper density forces arithmetic progressions of every length.** His proof was combinatorial and introduced the [regularity lemma](extremal-graph-theory.md). Furstenberg (1977) gave a proof through [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md) by recasting it as multiple recurrence in a measure-preserving system. Gowers (2001) gave a Fourier-analytic proof with explicit bounds, introducing the Gowers norms that measure higher-order structure. Szemerédi's theorem is the density form of [van der Waerden's colouring theorem](ramsey-theory.md).

6. **Green and Tao (2004, published 2008): the primes contain arbitrarily long arithmetic progressions.** The primes have density zero, so Szemerédi's theorem does not apply directly. The transference principle shows that Szemerédi's theorem holds for dense subsets of suitably pseudorandom sets, and sieve weights from [analytic number theory](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md) supply a pseudorandom set in which the primes are dense. The result says nothing about where such progressions occur, beyond bounds on their size.

7. **The obvious next questions are open.** Erdős conjectured that any set A of positive integers with ∑ 1/a divergent contains arbitrarily long progressions. That would include Green–Tao, since the reciprocals of the primes diverge. It is open as of 2026, though the three-term case was settled by Bloom and Sisask (2020). The Erdős–Szemerédi sum–product conjecture says that a finite set of integers has either many sums or many products, at least ∣A∣^(2 − ε) of one kind for every ε > 0. It is also open as of 2026.

## Key concepts
| Term | Meaning |
|---|---|
| Sumset A + B | All sums a + b with a ∈ A, b ∈ B |
| Doubling constant | ∣A + A∣/∣A∣ |
| Arithmetic progression | a, a + d, a + 2d, …, a + (k − 1)d with d ≠ 0 |
| Generalised arithmetic progression | Sums a + x₁d₁ + ⋯ + xᵣdᵣ with each xᵢ in a range |
| Upper density | The largest limiting proportion of {1, …, N} occupied by a set |
| Density increment | Passing to a sub-structure on which the set is denser |
| Structure versus randomness | A set is either pseudorandom or correlates with structure |
| Transference | Carrying a dense-set theorem over to dense subsets of pseudorandom sets |

## How it fits
- **Below:** Built on [primes](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md), [modular arithmetic](../../02-number-systems/02-elementary-number-theory/modular-arithmetic.md), the colouring theorems of [Ramsey theory](ramsey-theory.md) and the regularity and removal lemmas of [extremal graph theory](extremal-graph-theory.md).
- **Above:** The analytic tools are [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) and [ergodic theory](../../10-differential-equations-and-dynamics/04-dynamical-systems/ergodic-theory.md); the number-theoretic side meets [sieves and additive problems](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/sieves-and-additive-problems.md) and [primes in arithmetic progressions](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/primes-in-arithmetic-progressions.md), where Dirichlet's theorem concerns one progression and Green–Tao finds progressions made of primes.
- **Siblings:** The removal lemma of [extremal graph theory](extremal-graph-theory.md) proves Roth's theorem. The entropy methods in PFR and the union-closed sets problem in [posets and extremal set theory](posets-and-extremal-set-theory.md) come from the same toolkit.

## Common misconceptions
- **"Green–Tao follows from Szemerédi's theorem"**: the primes have density zero, so the theorem had to be transferred to a sparse setting, which was the main new idea.
- **"Primes in arithmetic progression means Dirichlet's theorem"**: Dirichlet finds infinitely many primes in one progression a + nd; Green–Tao finds progressions whose terms are all prime.
- **"Additive combinatorics is about the integers only"**: its theorems hold in any abelian group, and finite vector spaces such as 𝔽₂ⁿ are often the model case.

## Go deeper
- Tao and Vu, *Additive Combinatorics* (2006): the standard reference for sumsets, Freiman's theorem and Szemerédi's theorem.
- Zhao, *Graph Theory and Additive Combinatorics* (2023): the graph-theoretic and Fourier routes to Roth and Szemerédi.
- Green, *Additive Combinatorics* (2009): a review of Tao and Vu that surveys the whole subject.
