# Topological Spaces and Continuous Maps

> **Layer:** [07 Topology](../README.md) › [Point-Set Topology](README.md)
> **Builds on:** [Metric Spaces and Continuity](../../06-real-analysis/03-metric-spaces/metric-spaces-and-continuity.md), [Continuity](../../06-real-analysis/01-limits-and-convergence/continuity.md), [Sets and Set Operations](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md)
> **Enables:** [Subspaces, Products and Quotients](subspaces-products-and-quotients.md), [Compactness](compactness.md), [Topological and Smooth Manifolds](../03-manifolds/topological-and-smooth-manifolds.md), [Banach Spaces](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md), [Varieties and the Nullstellensatz](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md)

## Essence

A topological space is a set together with a chosen family of "open" sets, closed under arbitrary unions and finite intersections. It keeps exactly what continuity needs from a metric: the ε–δ definition of continuity can be rewritten as "the preimage of every open set is open", and that sentence makes sense with no distance at all. Topology studies the properties that survive continuous deformation, and its notion of sameness is the homeomorphism, a continuous bijection with continuous inverse. Many important topologies come from no metric (the Zariski topology of algebraic geometry, the weak topologies of functional analysis), so those subjects cannot be written without the abstraction.

## Core tenets

1. **Open sets are the primitive, and the axioms are what metric open sets satisfy.** A topology on a set X is a family 𝒯 of subsets of X that contains ∅ and X and is closed under arbitrary unions and finite intersections. In a metric space a set is open if it contains a small ball around each of its points; a union of such sets is open, and so is an intersection of two (take the smaller radius). An infinite intersection need not be: ⋂ₙ (−1/n, 1/n) = {0} is not open in ℝ. This asymmetry is why "finitely many" appears everywhere in topology.

2. **Continuity means that preimages of open sets are open.** In a metric space, f satisfies the ε–δ condition at every point if and only if f⁻¹(V) is open for every open V: if V contains the ε-ball around f(x), some δ-ball around x maps into it, which is what openness of f⁻¹(V) at x says. Preimages are used, not images, because preimages respect unions, intersections and complements, while images do not respect intersections. Composites are continuous at once, since (g∘f)⁻¹(W) = f⁻¹(g⁻¹(W)).

3. **Homeomorphism is sameness, and topological properties are those it preserves.** The inverse condition is not automatic. The map t ↦ (cos t, sin t) from [0, 2π) onto the circle S¹ is a continuous bijection, but its inverse tears the circle at (1, 0), and the spaces differ: removing any point other than 0 disconnects [0, 2π), while removing a point never disconnects S¹. Compactness, connectedness and the fundamental group are invariants. Length, boundedness and completeness are not: x ↦ 1/2 + arctan(x)/π is a homeomorphism from ℝ, which is complete, onto (0, 1), which is not.

4. **Different topologies on one set answer different questions.** The discrete topology (every set open) makes every map out of X continuous; the indiscrete topology (only ∅ and X open) makes every map into X continuous. A finer topology, one with more open sets, makes maps out of the space more often continuous and sequences less often convergent. On ℂⁿ the Zariski topology declares closed exactly the common zero sets of families of polynomials; any two of its non-empty open sets meet, so no metric produces it, since in a metric space distinct points have disjoint balls.

5. **Closure is defined from open sets, and sequences do not always detect it.** The closure Ā of A is the smallest closed set containing A: x ∈ Ā if and only if every open set containing x meets A. In a metric space Ā is the set of limits of sequences from A, but not in general. In the cocountable topology on ℝ (the closed sets are ℝ and the countable sets), a sequence converges only if it is eventually constant, so every set contains the limits of its convergent sequences, yet (0, 1) is not closed. General topology replaces sequences by nets or filters.

6. **A basis generates a topology, and continuity need only be checked on a basis.** A basis is a family ℬ of open sets such that every open set is a union of members of ℬ: the balls of a metric space, or the intervals with rational endpoints in ℝ. Since preimages respect unions, f is continuous once f⁻¹(B) is open for each basic set B. A space with a countable basis is second countable, a size condition built into the definition of a manifold and assumed in Urysohn's metrisation theorem.

7. **Different metrics can give the same topology.** On ℝⁿ the Euclidean, maximum and taxicab metrics have balls of different shapes, but every ball of one contains a ball of each other with the same centre, so all three have the same open sets and the same continuous maps. Which topologies come from some metric is the subject of [separation axioms and metrisability](separation-axioms-and-metrisability.md).

## Key concepts

| Term | Meaning |
|---|---|
| Topology | A family of subsets of X containing ∅ and X, closed under arbitrary unions and finite intersections |
| Open set, closed set | A member of the topology; the complement of one |
| Continuous map | A map f with f⁻¹(V) open for every open V |
| Homeomorphism | A continuous bijection with continuous inverse |
| Basis | A family of open sets whose unions are exactly the open sets |
| Closure Ā | The smallest closed set containing A |
| Second countable | Having a countable basis |
| Topological invariant | A property or quantity preserved by every homeomorphism |

## How it fits

- **Below:** It abstracts the open sets of [metric spaces](../../06-real-analysis/03-metric-spaces/metric-spaces-and-continuity.md) and the ε–δ [continuity](../../06-real-analysis/01-limits-and-convergence/continuity.md) of 06, in the language of [sets](../../01-sets-and-foundations/01-sets-relations-and-functions/sets-and-set-operations.md).
- **Above:** [Manifolds](../03-manifolds/topological-and-smooth-manifolds.md), the weak topologies of [functional analysis](../../09-advanced-analysis/03-functional-analysis/banach-spaces.md) and the Zariski topology of [algebraic geometry](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/varieties-and-the-nullstellensatz.md) all use this vocabulary.
- **Siblings:** [Subspaces, products and quotients](subspaces-products-and-quotients.md) make new spaces from old; [compactness](compactness.md), [connectedness](connectedness.md) and the [separation axioms](separation-axioms-and-metrisability.md) are the first invariants defined from open sets alone.

## Common misconceptions

- **"A continuous map sends open sets to open sets."**: That defines an open map, a different notion. A constant map ℝ → ℝ is continuous but sends ℝ to a point, which is not open.
- **"Any picture drawn from ℝⁿ is safe in a general space."**: In the indiscrete topology every sequence converges to every point; unique limits must be assumed (the Hausdorff property).
- **"A continuous bijection is a homeomorphism."**: The map [0, 2π) → S¹ above is a counterexample. The inverse is automatically continuous only under extra hypotheses, such as a compact domain and a Hausdorff target.

## Go deeper

- James Munkres, *Topology* (2nd edition, 2000): the standard first course; chapters 2 and 3 cover this material.
- John L. Kelley, *General Topology* (1955): the classic reference for point-set topology, including nets.
- Lynn Arthur Steen and J. Arthur Seebach Jr., *Counterexamples in Topology* (1970): a catalogue of spaces that break naive intuition.
