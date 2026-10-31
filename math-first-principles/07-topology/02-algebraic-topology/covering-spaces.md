# Covering Spaces

> **Layer:** [07 Topology](../README.md) › [Algebraic Topology](README.md)
> **Builds on:** [Homotopy and the Fundamental Group](homotopy-and-the-fundamental-group.md), [Group Actions](../../05-abstract-algebra/01-groups/group-actions.md), [Homomorphisms and Quotient Groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), [The Galois Correspondence](../../05-abstract-algebra/03-galois-theory/the-galois-correspondence.md)
> **Enables:** [Analytic Continuation and Riemann Surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md), [Knot Theory](../03-manifolds/knot-theory.md), [Three-Manifolds and the Poincaré Conjecture](../03-manifolds/three-manifolds-and-the-poincare-conjecture.md), [Lie Groups and Lie Algebras](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md)

## Essence

A covering map p: E → X looks, over each small open set of X, like a stack of disjoint copies of that set; the real line wrapping round the circle is the model. Paths and homotopies in X lift uniquely to E once a starting point is chosen, and this lifting is what computes fundamental groups. For reasonable spaces the connected covers of X correspond exactly to the subgroups of π₁(X): a cover corresponds to the image of its own fundamental group, its number of sheets is the index, and its symmetries form a quotient of π₁(X). This is the topological twin of the Galois correspondence between field extensions and subgroups, and the parallel is exact enough that each theory explains the other.

## Core tenets

1. **A covering map has evenly covered neighbourhoods.** Every x ∈ X has an open neighbourhood U whose preimage p⁻¹(U) is a disjoint union of open sets, the sheets, each mapped homeomorphically onto U. Examples are ℝ → S¹, t ↦ (cos 2πt, sin 2πt); z ↦ zⁿ on the unit circle, with n sheets; and Sⁿ → ℝPⁿ, identifying antipodes, with 2 sheets. Being a local homeomorphism is not enough: the restriction of ℝ → S¹ to (0, 3/2) is one, but some points have one preimage and others two.

2. **Paths and homotopies lift uniquely, and the lifts detect π₁.** Given a path γ in X and a point e over γ(0), exactly one path γ̃ in E starts at e and satisfies p∘γ̃ = γ; it is built piece by piece over evenly covered sets, and homotopies lift the same way. So p_*: π₁(E, e) → π₁(X, x) is injective, and a loop in X lifts to a closed loop if and only if its class lies in the subgroup p_*π₁(E, e). The endpoints of lifted loops define an action of π₁(X, x) on the fibre p⁻¹(x).

3. **The lifting criterion decides when a map lifts.** For Y path-connected and locally path-connected, a map f: Y → X lifts to E through chosen base points if and only if f_*π₁(Y) ⊆ p_*π₁(E). Every map from a simply connected space therefore lifts. Applied to two covers with the same subgroup, the criterion gives maps between them in both directions, so the covers are isomorphic.

4. **Classification: connected covers correspond to subgroups of π₁.** Let X be path-connected, locally path-connected and semilocally simply connected (each point has a neighbourhood whose loops contract in X). Then based connected covers, up to isomorphism, correspond one to one to subgroups H of π₁(X, x), through H = p_*π₁(E, e); forgetting base points replaces H by its conjugacy class. The number of sheets is the index of H. The trivial subgroup gives the universal cover, which is simply connected and covers every connected cover. The local hypothesis matters: the Hawaiian earring, circles of radius 1/n all touching at one point, has no universal cover.

5. **Normal subgroups give regular covers, whose symmetries form a quotient of π₁.** A deck transformation is a homeomorphism φ: E → E with p∘φ = p. When H is normal, the deck group acts transitively on each fibre and is isomorphic to π₁(X)/H; for the universal cover it is π₁(X) itself. So X is its universal cover divided by π₁(X): S¹ = ℝ/ℤ, the torus is ℝ²/ℤ², and ℝPⁿ = Sⁿ/{±1}, which gives π₁(ℝPⁿ) ≅ ℤ/2 for n ≥ 2. Conversely, if a group G acts on a simply connected, locally path-connected E so that each point has a neighbourhood whose translates are pairwise disjoint, then E → E/G is a cover and π₁(E/G) ≅ G.

6. **The parallel with Galois theory is a dictionary.** Both correspondences reverse inclusion, and their entries match row by row.

   | Galois theory | Covering spaces |
   |---|---|
   | Finite extension L ⊇ K | Connected cover E → X |
   | Separable closure of K | Universal cover of X |
   | Absolute Galois group of K | π₁(X) |
   | Degree [L : K] | Number of sheets |
   | Galois extension, group Gal(L/K) | Regular cover, deck group π₁(X)/H |

   The parallel is more than analogy: the finite branched covers of a compact Riemann surface correspond to the finite extensions of its field of meromorphic functions.

7. **Covers explain free groups and multivalued functions.** A connected cover of a graph is a graph, and graphs have free fundamental groups, so every subgroup of a free group is free (the Nielsen–Schreier theorem). Counting Euler characteristics, a subgroup of index n in a free group of rank k has rank n(k − 1) + 1. In complex analysis, √z and log z are not functions on ℂ \ {0}, but they are genuine functions on its 2-sheeted and universal covers.

## Key concepts

| Term | Meaning |
|---|---|
| Covering map | A map p: E → X under which every point of X has an evenly covered neighbourhood |
| Sheet | One of the disjoint open sets in p⁻¹(U) mapped homeomorphically onto U |
| Fibre | The preimage p⁻¹(x) of a point |
| Universal cover | A simply connected cover; it covers every connected cover |
| Deck transformation | A homeomorphism φ of E with p∘φ = p |
| Regular cover | A cover whose deck group acts transitively on fibres; its subgroup is normal |
| Semilocally simply connected | Each point has a neighbourhood whose loops contract in X |

## How it fits

- **Below:** Path lifting and π₁ come from [homotopy and the fundamental group](homotopy-and-the-fundamental-group.md); [group actions](../../05-abstract-algebra/01-groups/group-actions.md) and [quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md) describe fibres and deck groups; [the Galois correspondence](../../05-abstract-algebra/03-galois-theory/the-galois-correspondence.md) is the algebraic model.
- **Above:** Multivalued functions live on [Riemann surfaces](../../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md); cyclic covers of a knot complement give the Alexander polynomial in [knot theory](../03-manifolds/knot-theory.md); universal covers carry the geometries of [three-manifolds](../03-manifolds/three-manifolds-and-the-poincare-conjecture.md); a connected [Lie group](../../08-geometry/04-lie-theory/lie-groups-and-lie-algebras.md) has a simply connected cover with the same Lie algebra.
- **Siblings:** The proof that π₁(S¹) ≅ ℤ in the [previous leaf](homotopy-and-the-fundamental-group.md) is the cover ℝ → S¹ at work; [the Euler characteristic](the-euler-characteristic.md) multiplies by n under an n-sheeted cover.

## Common misconceptions

- **"Every local homeomorphism is a covering map."**: The restriction of ℝ → S¹ to (0, 3/2) is a local homeomorphism with fibres of different sizes; even covering is a condition on whole neighbourhoods.
- **"Bigger subgroups give bigger covers."**: The correspondence reverses inclusion, as in Galois theory. The whole group gives the one-sheeted cover X → X, and the trivial subgroup gives the largest, universal cover.

## Go deeper

- Allen Hatcher, *Algebraic Topology* (2002): section 1.3 proves the classification, and section 1.A applies covers to free groups.
- William S. Massey, *Algebraic Topology: An Introduction* (1967): a careful classical account of covering spaces and deck transformations.
