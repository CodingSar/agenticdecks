# The Sylow Theorems

> **Layer:** [05 Abstract Algebra](../README.md) › [Groups](README.md)
> **Builds on:** [Groups and Subgroups](groups-and-subgroups.md), [Homomorphisms and Quotient Groups](homomorphisms-and-quotient-groups.md), [Group Actions](group-actions.md), [Counting Principles and Binomial Coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md)
> **Enables:** [Composition Series and Simple Groups](composition-series-and-simple-groups.md), [The Galois Correspondence](../03-galois-theory/the-galois-correspondence.md)

## Essence

Lagrange's theorem says that subgroup orders divide the group order, and its converse is false. Sylow showed in 1872 that the converse does hold for the largest power of each prime, and with remarkable control. If |G| = pⁿm with p prime and p not dividing m, then G has subgroups of order pⁿ, they are all conjugate, and their number is congruent to 1 mod p and divides m. These constraints are often strong enough to determine a group's structure from its order alone: every group of order 15 is cyclic, and no group of order 12 or 30 is simple. All three theorems are proved by letting G act on a well-chosen set.

## Core tenets

1. **Sylow's theorems.** Let G be a finite group with |G| = pⁿm, where p is prime, n ≥ 1 and p does not divide m. A Sylow p-subgroup is a subgroup of order pⁿ.
   ```
   (i)   Sylow p-subgroups exist.
   (ii)  Any two are conjugate, and every subgroup of p-power order lies in one.
   (iii) Their number n_p satisfies n_p ≡ 1 (mod p) and n_p divides m;
         in fact n_p = [G : N(P)] for any Sylow p-subgroup P.
   ```
   Here N(P) = {g : gPg⁻¹ = P} is the normaliser of P, the largest subgroup in which P is normal.

2. **Existence follows from a binomial coefficient (Wielandt's proof).** Let G act by left multiplication on the subsets of size pⁿ. Comparing coefficients of x^(pⁿ) in (1 + x)^(pⁿm) ≡ (1 + x^(pⁿ))^m (mod p) shows that their number C(pⁿm, pⁿ) is ≡ m, so not divisible by p, and some orbit has size prime to p. The stabiliser H of a subset S in that orbit then has order divisible by pⁿ. But h ↦ hs is injective from H into S for any s ∈ S, so |H| ≤ pⁿ, and |H| = pⁿ.

3. **Conjugacy follows from a fixed point.** Let P be a Sylow p-subgroup and Q any subgroup of p-power order. Q acts on the m cosets of P, and a p-group acting on a finite set has a number of fixed points congruent to the set's size mod p. As m ≢ 0 (mod p), some coset gP is fixed: QgP = gP, which says Q ⊆ gPg⁻¹. If Q is also Sylow, the orders force Q = gPg⁻¹.

4. **The count follows from orbit–stabiliser and one more fixed point.** The Sylow p-subgroups form a single conjugacy orbit, so n_p = [G : N(P)], which divides [G : P] = m because P ≤ N(P). Now let P act on the Sylow p-subgroups by conjugation. If P fixes Q, then P and Q are Sylow subgroups of N(Q), hence conjugate there, and Q is normal in N(Q), so P = Q. Exactly one fixed point gives n_p ≡ 1 (mod p).

5. **n_p = 1 if and only if the Sylow p-subgroup is normal.** All Sylow p-subgroups are conjugate, so a unique one equals all its conjugates; a normal one has no others. This is the main route to proving that groups are not simple, and to assembling them from their Sylow subgroups.

6. **Small orders are often forced.** For |G| = 15, n₃ divides 5 and is ≡ 1 (mod 3), so n₃ = 1; likewise n₅ = 1. Both Sylow subgroups are normal and meet trivially, so G ≅ ℤ/3 × ℤ/5 ≅ ℤ/15. For |G| = 12, if n₃ = 4 the four subgroups of order 3 contain eight elements of order 3, leaving room for exactly one subgroup of order 4. Either way some Sylow subgroup is normal, so no group of order 12 is simple. For |G| = 30, n₃ = 10 and n₅ = 6 together would need 20 + 24 = 44 elements, more than 30.

7. **A₅ shows the counts in action.** With |A₅| = 60 = 2² · 3 · 5, it has n₅ = 6 (24 elements of order 5), n₃ = 10 (20 elements of order 3) and n₂ = 5 (five Klein four-groups holding the 15 elements of order 2). With the identity, 24 + 20 + 15 + 1 = 60. No Sylow subgroup is normal, consistent with A₅ being simple. Sylow arguments, with some further counting, show that no group of composite order below 60 is simple, so A₅ is the smallest non-abelian simple group.

8. **G has subgroups of every prime-power order dividing |G|.** A group of order pⁿ has a non-trivial centre, which by Cauchy's theorem contains a central element of order p; quotienting by the subgroup it generates and inducting gives subgroups of every order pᵏ with k ≤ n. Combined with (i) this is the best general converse to Lagrange: A₄, of order 12, shows that divisors that are not prime powers can fail.

## Key concepts

| Term | Meaning |
|---|---|
| Sylow p-subgroup | A subgroup of order pⁿ, the largest power of p dividing ∣G∣ |
| n_p | The number of Sylow p-subgroups |
| Normaliser N(H) | The elements g with gHg⁻¹ = H; the largest subgroup in which H is normal |
| Conjugate subgroups | H and gHg⁻¹ for some g |
| p-group | A group whose order is a power of the prime p |
| Simple group | A non-trivial group whose only normal subgroups are 1 and itself |

## How it fits

- **Below:** the existence proof is a congruence for [binomial coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md); the others rest on the orbit–stabiliser theorem and the fixed-point congruence from [group actions](group-actions.md).
- **Above:** the study of Sylow subgroups and their normalisers, called local analysis, drove the [classification of finite simple groups](composition-series-and-simple-groups.md); a Sylow 2-subgroup argument gives an algebraic proof of the fundamental theorem of algebra in [the Galois correspondence](../03-galois-theory/the-galois-correspondence.md).
- **Siblings:** [group actions](group-actions.md) supply every proof; [composition series](composition-series-and-simple-groups.md) use Sylow counts to rule out small simple groups.

## Common misconceptions

- **"Sylow subgroups are normal."** Only when n_p = 1. S₃ has three Sylow 2-subgroups, one for each transposition.
- **"Groups of order pq are always cyclic."** Only when p < q and p does not divide q − 1. S₃ has order 6 = 2 · 3, and 2 divides 3 − 1.
- **"The Sylow numbers determine the group."** Every group of order 8 has n₂ = 1, yet there are five such groups.

## Go deeper

- Ludwig Sylow, "Théorèmes sur les groupes de substitutions", *Mathematische Annalen* (1872): the original paper.
- I. Martin Isaacs, *Finite Group Theory* (2008): Sylow theory and the local analysis that grew from it.
- David Dummit and Richard Foote, *Abstract Algebra* (3rd edition, 2004): many worked "groups of order n" arguments.
