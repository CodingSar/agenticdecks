# Composition Series and Simple Groups

> **Layer:** [05 Abstract Algebra](../README.md) › [Groups](README.md)
> **Builds on:** [Homomorphisms and Quotient Groups](homomorphisms-and-quotient-groups.md), [Group Actions](group-actions.md), [The Sylow Theorems](the-sylow-theorems.md), [Primes and Unique Factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md)
> **Enables:** [Solvability by Radicals](../03-galois-theory/solvability-by-radicals.md), [Representations of Finite Groups](../04-modules-and-representations/representations-of-finite-groups.md), [The Classification of Simple Lie Algebras](../../08-geometry/04-lie-theory/the-classification-of-simple-lie-algebras.md), [Computers and Proof](../../15-mathematics-in-context/computers-and-proof.md)

## Essence

As integers factor into primes, finite groups break into simple groups, those with no normal subgroups except the trivial one and themselves. A composition series is a chain of subgroups, each normal in the next, whose successive quotients are simple, and the Jordan–Hölder theorem says that every such chain yields the same list of quotients. Unlike prime factorisation, the factors do not determine the group, so the theory has two halves: find all simple groups, and understand how they glue together. The first half is the classification of finite simple groups, one of the longest proofs in mathematics. Solvable groups, whose factors are all cyclic, are the ones Galois theory needs.

## Core tenets

1. **A composition series is a chain 1 = G₀ ◁ G₁ ◁ ⋯ ◁ G_r = G in which every factor G_(i+1)/G_i is simple.** Every finite group has one: choose a maximal proper normal subgroup, which by the correspondence theorem has simple quotient, and recurse. The abelian simple groups are exactly the ℤ/p with p prime, since every subgroup of an abelian group is normal. Infinite groups need not have one: every non-trivial subgroup of ℤ is nℤ ≅ ℤ, which is not simple, so no chain can start.

2. **Jordan–Hölder theorem: any two composition series of a finite group have the same length and the same factors, up to order and isomorphism.** Induct on |G|. If the two series have different top terms M ≠ N, then MN = G, and the second isomorphism theorem gives G/M ≅ N/(M ∩ N) and G/N ≅ M/(M ∩ N). A composition series of M ∩ N, extended up through M or through N, links the given series with matching factors. Jordan proved that the factor orders agree (1870), Hölder that the factors do (1889). For ℤ/n the factors are ℤ/p for the primes dividing n, with multiplicity, so the theorem contains unique prime factorisation.

3. **The factors do not determine the group.** ℤ/4 and ℤ/2 × ℤ/2 both have factors ℤ/2, ℤ/2; S₃ and ℤ/6 both have ℤ/2, ℤ/3. Rebuilding a group from its factors is the extension problem, and it is wild: a computer enumeration found nearly 50 billion groups of order 2¹⁰ = 1024, every one with ten factors ℤ/2.

4. **A group is solvable if all its composition factors are cyclic of prime order.** Equivalently, the derived series G, [G, G], [[G, G], [G, G]], … reaches 1. Abelian groups and groups of prime-power order are solvable, and so is S₄ ▷ A₄ ▷ V₄ ▷ ℤ/2 ▷ 1, with factors ℤ/2, ℤ/3, ℤ/2, ℤ/2. Subgroups, quotients and extensions of solvable groups are solvable. Burnside proved in 1904 that groups of order pᵃqᵇ are solvable. Feit and Thompson proved in 1963 that every group of odd order is solvable, in a 255-page paper that a team led by Georges Gonthier verified in the Coq proof assistant in 2012.

5. **A₅ is simple, so S₅ is not solvable.** A normal subgroup is a union of conjugacy classes that includes e. The classes of A₅ have sizes 1, 15, 20, 12 and 12, and the only sums that include the 1 and divide 60 are 1 and 60 itself. So A₅ is a non-abelian simple group, and the composition factors of S₅ are ℤ/2 and A₅. Aₙ is simple for every n ≥ 5: the group theory behind the unsolvable quintic.

6. **The classification of finite simple groups (CFSG): every finite simple group is on this list.**
   ```
   cyclic groups ℤ/p, p prime
   alternating groups Aₙ, n ≥ 5
   groups of Lie type: 16 infinite families, such as PSLₙ(𝔽_q),
     the n × n determinant-one matrices over a finite field modulo scalars
   26 sporadic groups, the largest being the Monster, of order about 8 × 10⁵³
   ```
   Some authors count the Tits group as a 27th sporadic group. The Monster was predicted in the 1970s and constructed by Robert Griess in 1982.

7. **The proof's history: decades of work, a late gap, and a revision still in progress.** The proof fills tens of thousands of pages in several hundred papers by about a hundred authors, most of them published between 1955 and 2004. Completion was announced in the early 1980s, but the case of "quasithin" groups rested on an unpublished, incomplete manuscript. Michael Aschbacher and Stephen Smith closed that gap in a two-volume work of over a thousand pages published in 2004, and the classification has been regarded as complete since then. A second-generation proof by Daniel Gorenstein, Richard Lyons and Ronald Solomon has appeared in a series of volumes since 1994 and is still in progress as of 2026.

8. **Much of finite group theory now runs through the list.** Results such as Schreier's conjecture, that the outer automorphism group of every finite simple group is solvable, are proved by checking each family. Monstrous moonshine, conjectured by Conway and Norton in 1979 and proved by Richard Borcherds in 1992, ties the Monster to modular functions.

## Key concepts

| Term | Meaning |
|---|---|
| Simple group | A non-trivial group whose only normal subgroups are 1 and itself |
| Composition series | A chain of subgroups, each normal in the next, with simple factors |
| Solvable group | One whose composition factors are all cyclic of prime order |
| Group of Lie type | A matrix-like group over a finite field, such as PSLₙ(𝔽_q) |
| Sporadic group | One of the 26 simple groups outside the infinite families |
| Quasithin case | The last part of the classification to be completed, in 2004 |

## How it fits

- **Below:** Jordan–Hölder generalises [unique prime factorisation](../../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md); proofs that particular groups are not simple use [Sylow counts](the-sylow-theorems.md) and [actions on cosets](group-actions.md).
- **Above:** the groups of Lie type are finite analogues of the Lie groups in [the classification of simple Lie algebras](../../08-geometry/04-lie-theory/the-classification-of-simple-lie-algebras.md); the classification is a test case for [computers and proof](../../15-mathematics-in-context/computers-and-proof.md).
- **Siblings:** [solvability by radicals](../03-galois-theory/solvability-by-radicals.md) turns "S₅ is not solvable" into "the quintic has no formula"; [character theory](../04-modules-and-representations/representations-of-finite-groups.md) proves Burnside's pᵃqᵇ theorem.

## Common misconceptions

- **"A group is determined by its composition factors."** ℤ/4 and ℤ/2 × ℤ/2 share theirs. The factors are the primes; the gluing is the hard part.
- **"The classification is one proof that someone has read."** It is spread over hundreds of papers; the consolidated version is unfinished as of 2026.

## Go deeper

- Ronald Solomon, "A brief history of the classification of the finite simple groups", *Bulletin of the American Mathematical Society* (2001): the history by one of its authors.
- Robert A. Wilson, *The Finite Simple Groups* (2009): a graduate tour of every family.
