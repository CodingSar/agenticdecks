# Subspaces, Products and Quotients

> **Layer:** [07 Topology](../README.md) › [Point-Set Topology](README.md)
> **Builds on:** [Topological Spaces and Continuous Maps](topological-spaces-and-continuous-maps.md), [Equivalence Relations and Quotients](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md), [Functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md)
> **Enables:** [Compactness](compactness.md), [Homotopy and the Fundamental Group](../02-algebraic-topology/homotopy-and-the-fundamental-group.md), [Classification of Surfaces](../03-manifolds/classification-of-surfaces.md), [Universal Properties and Adjunctions](../../13-structure-and-metamathematics/01-category-theory/universal-properties-and-adjunctions.md)

## Essence

New spaces are made from old ones in three ways: by restricting to a subset, by multiplying spaces, and by gluing points together. Each time there is one right topology, fixed by a universal property: the coarsest or finest topology that makes the natural maps continuous, so that maps into a product or out of a quotient are easy to test. For infinite products this principle chooses the product topology, open in only finitely many coordinates at a time, over the more obvious box topology; only the product topology makes Tychonoff's theorem true. Quotients turn a square into a torus, a Klein bottle or a projective plane, which is how most spaces of algebraic topology are built.

## Core tenets

1. **The subspace topology makes the inclusion continuous and nothing more.** For A ⊆ X, the open sets of A are the sets U ∩ A with U open in X. So [0, 1/2) is open in [0, 1] but not in ℝ, and "open" always means "open in a stated space". A map into A is continuous if and only if it is continuous as a map into X.

2. **The product topology is the coarsest one making every projection continuous.** Each projection pᵢ: ∏ Xⱼ → Xᵢ must be continuous, so each pᵢ⁻¹(Uᵢ) must be open, and finite intersections of these must be open too. That forces exactly the basic sets ∏ Uᵢ with Uᵢ open and Uᵢ = Xᵢ for all but finitely many i. The payoff is the defining property: a map f into the product is continuous if and only if every coordinate pᵢ∘f is, and a sequence converges if and only if every coordinate does. For finitely many factors this is the usual topology, as on ℝⁿ.

3. **The box topology, which allows every product of open sets, is wrong for infinite products.** In ℝ^ℕ with the box topology, the diagonal map t ↦ (t, t, t, …) is not continuous although every coordinate is: the preimage of the open box ∏ₙ (−1/n, 1/n) is {0}, which is not open. Compactness fails too. In the box topology {0, 1}^ℕ is discrete, since each point is a product of open singletons, and infinite, so it is not compact; in the product topology the same set is homeomorphic to the Cantor set, which is compact.

4. **The quotient topology is the finest one making the gluing map continuous.** Given an equivalence relation ~ on X, let q: X → X/~ send each point to its class, and call U ⊆ X/~ open if and only if q⁻¹(U) is open. Its universal property mirrors the product's: a map g out of X/~ is continuous if and only if g∘q is. To define a continuous map on a glued space, define a continuous map on the pieces that respects the gluing.

5. **Gluing builds the standard spaces from simple pieces.** Identifying the endpoints of [0, 1] gives the circle S¹, through the map t ↦ (cos 2πt, sin 2πt). Gluing the sides of a square in pairs gives the torus, the Klein bottle or the real projective plane ℝP², according to the directions; gluing one pair of sides with a half-twist gives the Möbius band. Collapsing the boundary sphere of the disc Dⁿ to a point gives the sphere Sⁿ, and identifying each x ∈ Sⁿ with −x gives the projective space ℝPⁿ.

```
      torus               Klein bottle           projective plane
       a →                   a →                     a →
    ┌───────┐             ┌───────┐               ┌───────┐
  b ↑       ↑ b         b ↑       ↓ b           b ↑       ↓ b
    └───────┘             └───────┘               └───────┘
       a →                   a →                     ← a
```

6. **Quotients can destroy good properties, so each one must be checked.** Gluing two copies of ℝ along ℝ \ {0} gives the line with two origins: every point has a neighbourhood homeomorphic to ℝ, but the two origins have no disjoint neighbourhoods, so limits are not unique. In ℝ/ℚ, where x ~ y if x − y ∈ ℚ, the only open sets are ∅ and the whole space: the preimage of a non-empty open set would be a non-empty open set closed under rational translations, and density of ℚ forces it to be all of ℝ. By contrast, the quotient of a Hausdorff space by a finite group of homeomorphisms is again Hausdorff.

7. **Universal properties make these constructions canonical across mathematics.** The product is the space through which every family of maps into the factors passes uniquely; the quotient is the space through which every map respecting ~ passes uniquely. The same two properties define direct products and [quotient groups](../../05-abstract-algebra/01-groups/homomorphisms-and-quotient-groups.md), and category theory names them limits and colimits.

## Key concepts

| Term | Meaning |
|---|---|
| Subspace topology | The open sets U ∩ A for U open in X |
| Product topology | Generated by products ∏ Uᵢ of open sets with Uᵢ = Xᵢ for all but finitely many i |
| Box topology | Generated by all products ∏ Uᵢ of open sets |
| Projection pᵢ | The map from the product to Xᵢ taking a point to its i-th coordinate |
| Quotient map q | The map X → X/~ sending x to its class, with U open if and only if q⁻¹(U) is |
| ℝPⁿ | Real projective space: Sⁿ with each x identified with −x |
| Universal property | A characterisation of a construction by the maps into or out of it |

## How it fits

- **Below:** Quotients of sets by [equivalence relations](../../01-sets-and-foundations/01-sets-relations-and-functions/equivalence-relations-and-quotients.md) get a topology here; a product is a set of [functions](../../01-sets-and-foundations/01-sets-relations-and-functions/functions.md) on the index set, and an infinite product of non-empty sets is non-empty only by the [axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md).
- **Above:** Gluing builds the spaces whose [fundamental groups](../02-algebraic-topology/homotopy-and-the-fundamental-group.md) and [homology](../02-algebraic-topology/homology.md) are computed and the surfaces in the [classification](../03-manifolds/classification-of-surfaces.md); [universal properties](../../13-structure-and-metamathematics/01-category-theory/universal-properties-and-adjunctions.md) are a theme of category theory.
- **Siblings:** It builds on [topological spaces](topological-spaces-and-continuous-maps.md); [compactness](compactness.md) needs the product topology for Tychonoff's theorem, and the [separation axioms](separation-axioms-and-metrisability.md) say which quotients stay Hausdorff.

## Common misconceptions

- **"The box topology is the natural topology on an infinite product."**: It fails the coordinatewise tests for continuity and convergence, and Tychonoff's theorem is false for it.
- **"A quotient of a nice space is nice."**: The line with two origins is a quotient of two copies of ℝ and is not Hausdorff; ℝ/ℚ has no open sets except ∅ and itself.

## Go deeper

- James Munkres, *Topology* (2nd edition, 2000): the product, box and quotient topologies, with their counterexamples.
- M. A. Armstrong, *Basic Topology* (1983): gluing constructions and surfaces, with many pictures.
