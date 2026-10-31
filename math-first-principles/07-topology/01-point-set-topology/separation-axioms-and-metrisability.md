# Separation Axioms and Metrisability

> **Layer:** [07 Topology](../README.md) › [Point-Set Topology](README.md)
> **Builds on:** [Topological Spaces and Continuous Maps](topological-spaces-and-continuous-maps.md), [Subspaces, Products and Quotients](subspaces-products-and-quotients.md), [Compactness](compactness.md), [Metric Spaces and Continuity](../../06-real-analysis/03-metric-spaces/metric-spaces-and-continuity.md)
> **Enables:** [Topological and Smooth Manifolds](../03-manifolds/topological-and-smooth-manifolds.md), [Banach Spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), [Varieties and the Nullstellensatz](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md)

## Essence

The axioms of a topology alone allow spaces in which a sequence converges to two limits or a point cannot be told apart from a closed set. The separation axioms add, in increasing strength, the ability to separate points and closed sets by disjoint open sets: the Hausdorff axiom (two points), regularity (a point and a closed set) and normality (two closed sets). Normality is where open sets start to produce functions: Urysohn's lemma builds a continuous function equal to 0 on one closed set and 1 on another. With countably many such functions a space embeds in a cube of countably many dimensions, which gives Urysohn's metrisation theorem: every second-countable regular Hausdorff space is metrisable. This answers the question of when a topology comes from a distance.

## Core tenets

1. **The Hausdorff axiom is what makes limits unique.** If distinct points x and y have disjoint neighbourhoods, a sequence cannot eventually lie in both, so it has at most one limit. Without the axiom, limits multiply: in the line with two origins the sequence 1/n converges to both origins, and in the cofinite topology on ℂ (the Zariski topology in one variable) every sequence of distinct points converges to every point. Metric spaces are Hausdorff (use balls of radius d(x, y)/2), subspaces and products of Hausdorff spaces are Hausdorff, and quotients need not be.

2. **The axioms form a ladder, and each rung is strictly higher.** A space is T₁ if points are closed, Hausdorff (T₂) if distinct points have disjoint neighbourhoods, regular if a point and a closed set not containing it have disjoint neighbourhoods, and normal if disjoint closed sets do. Among T₁ spaces, normal ⇒ regular ⇒ Hausdorff, and every Hausdorff space is T₁. No arrow reverses: the cofinite topology on an infinite set is T₁ but not Hausdorff, and the Sorgenfrey plane below is regular but not normal. Conventions differ on whether "regular" and "normal" include T₁, so check a source's definitions before quoting it.

3. **Metric spaces and compact Hausdorff spaces are normal.** In a metric space, disjoint closed sets A and B are separated by the sets where d(x, A) < d(x, B) and where d(x, B) < d(x, A), and the function d(x, A)/(d(x, A) + d(x, B)) is 0 on A and 1 on B. In a compact Hausdorff space, the argument that separates a point from a compact set is applied twice, first to points and then to closed sets, which are compact. Normality is not preserved by products: the square of the Sorgenfrey line (ℝ with the half-open intervals [a, b) as a basis) is regular but not normal.

4. **Urysohn's lemma: in a normal space X, for disjoint closed sets A and B there is a continuous f: X → [0, 1] equal to 0 on A and 1 on B.** Without a metric there is no formula, so f is built from open sets. Normality lets one fit an open set V between a closed set C and an open set W ⊇ C, with C ⊆ V and the closure of V inside W. Repeating this for every dyadic rational r in [0, 1], starting from U₁ = X \ B, gives open sets U_r containing A, each with closure inside U_s whenever r < s. Then f(x) = inf {r : x ∈ U_r}, with f = 1 off all of them, is continuous. The Tietze extension theorem follows: a continuous real function on a closed subset of a normal space extends to the whole space.

5. **Urysohn's metrisation theorem: every second-countable regular Hausdorff space is metrisable.** Such a space is normal, so Urysohn's lemma supplies countably many functions fₙ: X → [0, 1] that separate points from closed sets, one for each suitable pair of basic open sets. The map x ↦ (f₁(x), f₂(x), …) embeds X in the Hilbert cube [0, 1]^ℕ, whose product topology comes from the metric below, and X inherits it.

   ```
   d(s, t) = ∑ₙ 2⁻ⁿ · |sₙ − tₙ|
   ```

   Regular and Hausdorff are necessary, since every metric space has both properties. Second countability is not: an uncountable discrete space is metrisable but has no countable basis. The Nagata–Smirnov theorem gives the exact condition, a regular Hausdorff space with a basis that is a countable union of locally finite families.

6. **For compact spaces and manifolds the answer is simple.** A compact Hausdorff space is metrisable if and only if it is second countable. Manifolds are defined to be Hausdorff and second countable, and being locally Euclidean they are regular, so every manifold is metrisable. The Hausdorff clause is not redundant: the line with two origins is locally Euclidean and second countable but not Hausdorff.

## Key concepts

| Term | Meaning |
|---|---|
| T₁ space | Every single point is a closed set |
| Hausdorff (T₂) | Distinct points have disjoint neighbourhoods |
| Regular | A point and a closed set not containing it have disjoint neighbourhoods |
| Normal | Disjoint closed sets have disjoint neighbourhoods |
| Metrisable | The topology is induced by some metric |
| Embedding | A continuous injection that is a homeomorphism onto its image |
| Hilbert cube | [0, 1]^ℕ with the product topology |

## How it fits

- **Below:** [Metric spaces](../../06-real-analysis/03-metric-spaces/metric-spaces-and-continuity.md) are the model, since a distance separates everything; this leaf asks which topologies admit one. It uses the product topology of [subspaces, products and quotients](subspaces-products-and-quotients.md) and the arguments of [compactness](compactness.md).
- **Above:** [Manifolds](../03-manifolds/topological-and-smooth-manifolds.md) assume Hausdorff and second countable, which buys metrics and partitions of unity. Compact Hausdorff spaces K and their Urysohn functions underlie the spaces C(K) of continuous functions in [Banach spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md). The Zariski topology of [varieties](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md) is T₁ but not Hausdorff, and still the right notion of nearness there.
- **Siblings:** It completes the toolkit begun in [topological spaces](topological-spaces-and-continuous-maps.md), and with [compactness](compactness.md) it proves that continuous bijections from compact spaces to Hausdorff spaces are homeomorphisms.

## Common misconceptions

- **"Every reasonable space is metrisable."**: An uncountable product of copies of [0, 1] is compact Hausdorff but not metrisable, because no point has a countable neighbourhood basis; spaces of functions under pointwise convergence are of this kind.
- **"Normal is just a stronger Hausdorff."**: Normality is the axiom that produces continuous functions, and unlike the Hausdorff property it is not inherited by products or by all subspaces.

## Go deeper

- James Munkres, *Topology* (2nd edition, 2000): chapter 4 proves Urysohn's lemma, the metrisation theorem and the Tietze extension theorem in full.
- Lynn Arthur Steen and J. Arthur Seebach Jr., *Counterexamples in Topology* (1970): a space for each gap between the separation axioms.
