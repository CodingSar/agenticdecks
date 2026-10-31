# Group Actions

> **Layer:** [05 Abstract Algebra](../README.md) › [Groups](README.md)
> **Builds on:** [Groups and Subgroups](groups-and-subgroups.md), [Homomorphisms and Quotient Groups](homomorphisms-and-quotient-groups.md), [Counting Principles and Binomial Coefficients](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md)
> **Enables:** [The Sylow Theorems](the-sylow-theorems.md), [Representations of Finite Groups](../04-modules-and-representations/representations-of-finite-groups.md), [The Erlangen Programme](../../08-geometry/01-classical-geometry/the-erlangen-programme.md), [Covering Spaces](../../07-topology/02-algebraic-topology/covering-spaces.md)

## Essence

Groups matter because they act: an action lets each element of a group G move the points of a set X, compatibly with the group law. Every action splits X into orbits, and the orbit–stabiliser theorem says that each orbit has as many points as a stabiliser has cosets, so in a finite group orbit sizes divide |G|. Counting fixed points in two ways gives Burnside's lemma, which counts objects up to symmetry. Letting G act on itself by conjugation gives the class equation, and with it the first structure theorems for groups of prime-power order. Much of finite group theory is the art of choosing a good set for G to act on.

## Core tenets

1. **An action of G on X is a rule (g, x) ↦ g·x with e·x = x and g·(h·x) = (gh)·x; equivalently, a homomorphism from G to the group Sym(X) of bijections of X.** Each g acts as a bijection, with inverse given by g⁻¹. Examples: Sₙ on {1, …, n}; GLₙ(ℝ) on ℝⁿ; the rotations of a cube on its faces; G on itself by conjugation, g·x = gxg⁻¹; G on the cosets of a subgroup. "y = g·x for some g" is an equivalence relation, so the orbits G·x = {g·x : g ∈ G} partition X.

2. **Orbit–stabiliser theorem: |G·x| = [G : G_x], where the stabiliser is G_x = {g : g·x = x}.** The map gG_x ↦ g·x is a well-defined bijection from cosets to the orbit, because g·x = h·x if and only if g⁻¹h ∈ G_x. So for finite G, |G| = |G·x|·|G_x|. A cube's rotations can carry a given face to any of the 6 faces, and 4 rotations fix that face, so there are 6 × 4 = 24 rotations.

3. **Burnside's lemma: the number of orbits is the average number of fixed points, (1/|G|)·∑ |Fix(g)| over g ∈ G.** Count the pairs (g, x) with g·x = x. Grouped by g they number ∑ |Fix(g)|; grouped by x they number ∑ |G_x| = ∑ |G|/|G·x|, and each orbit contributes exactly |G|. Necklaces of 4 beads in 2 colours, up to rotation: the identity fixes 16 colourings, each quarter turn 2, the half turn 4, giving (16 + 2 + 4 + 2)/4 = 6. The naive 16/4 = 4 is wrong because symmetric colourings have smaller orbits. Frobenius knew the lemma before Burnside's book made it famous.

4. **The class equation: |G| = |Z(G)| + ∑ [G : C(xᵢ)].** Under conjugation the orbits are the conjugacy classes, the stabiliser of x is its centraliser C(x) = {g : gx = xg}, and the fixed points form the centre Z(G), the elements that commute with everything. The sum runs over one xᵢ from each class with more than one element, and each term divides |G|. For S₃: 6 = 1 + 2 + 3.

5. **A group of prime-power order has a non-trivial centre.** If |G| = pⁿ with n ≥ 1, every class outside the centre has size a power of p greater than 1, so p divides |Z(G)|. The same argument shows that when a p-group acts on a finite set, |X| ≡ |Fix| (mod p), since every non-trivial orbit has size divisible by p. Consequence: every group of order p² is abelian, since G/Z(G) has order 1 or p, hence is cyclic, and G is abelian whenever G/Z(G) is cyclic.

6. **Cayley's theorem: every group is a group of permutations.** Left multiplication gives an injective homomorphism G → Sym(G), so a group of order n embeds in Sₙ. Acting on the k cosets of a proper subgroup H gives a homomorphism G → S_k whose kernel lies in H. If |G| does not divide k!, the kernel is non-trivial, and G has a proper non-trivial normal subgroup. This is a standard tool for proving that groups are not simple.

7. **Cauchy's theorem falls out of a well-chosen action.** Let a prime p divide |G| and let ℤ/p rotate the set X of p-tuples (g₁, …, g_p) with g₁g₂⋯g_p = e. The last entry is determined by the others, so |X| = |G|^(p−1), divisible by p. The fixed tuples are the constant ones (g, …, g) with gᵖ = e, and their number is congruent to |X|, hence to 0, mod p. As (e, …, e) is one, there are others: elements of order p. This proof is due to McKay (1959).

## Key concepts

| Term | Meaning |
|---|---|
| Action | A homomorphism G → Sym(X) |
| Orbit G·x | All points g·x reachable from x |
| Stabiliser G_x | The subgroup of elements fixing x |
| Fix(g) | The points that g leaves where they are |
| Transitive action | One with a single orbit |
| Faithful action | One where only e acts as the identity map |
| Conjugacy class | An orbit of G acting on itself by conjugation |
| Centraliser C(x) | The elements that commute with x |
| Centre Z(G) | The elements that commute with every element |
| p-group | A group whose order is a power of a prime p |

## How it fits

- **Below:** Burnside's lemma is double counting from [counting principles](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md); an action is a [homomorphism](homomorphisms-and-quotient-groups.md) into a permutation group.
- **Above:** the [Erlangen programme](../../08-geometry/01-classical-geometry/the-erlangen-programme.md) defines a geometry by the group acting on it; the fundamental group acts on the fibres of a [covering space](../../07-topology/02-algebraic-topology/covering-spaces.md).
- **Siblings:** [the Sylow theorems](the-sylow-theorems.md) are proved entirely by actions; [representations](../04-modules-and-representations/representations-of-finite-groups.md) are actions by linear maps; a Galois group acts on the roots of a polynomial in [the Galois correspondence](../03-galois-theory/the-galois-correspondence.md).

## Common misconceptions

- **"The number of orbits is |X|/|G|."** Only when every stabiliser is trivial. Symmetric objects have small orbits, which is why Burnside's lemma averages fixed points instead.
- **"Points in one orbit have the same stabiliser."** Their stabilisers are conjugate: the stabiliser of g·x is gG_xg⁻¹. They coincide only in special cases, such as when G_x is normal.
- **"A group has one natural action."** One group acts in many ways, and the choice of set is the whole art: Sylow's proofs use actions on subsets, on cosets and on subgroups.

## Go deeper

- M. A. Armstrong, *Groups and Symmetry* (1988): actions, orbit counting and the class equation through geometric examples.
- I. Martin Isaacs, *Finite Group Theory* (2008): a graduate text in which actions are the main tool.
