# The Erlangen Programme

> **Layer:** [08 Geometry](../README.md) › [Classical Geometry](README.md)
> **Builds on:** [Group actions](../../05-abstract-algebra/01-groups/group-actions.md), [Non-Euclidean geometry](non-euclidean-geometry.md), [Projective geometry](projective-geometry.md), [Symmetry groups and tilings](symmetry-groups-and-tilings.md)
> **Enables:** [Lie groups and Lie algebras](../04-lie-theory/lie-groups-and-lie-algebras.md), [Riemannian manifolds](../02-differential-geometry/riemannian-manifolds.md), [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md), [Categories and functors](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md)

## Essence

By 1870 there were many geometries, Euclidean, hyperbolic, spherical, affine and projective, and no clear account of how they related. In his 1872 Erlangen programme Felix Klein proposed one: a geometry is a space together with a group acting on it, and its subject matter is whatever the group leaves invariant. Bigger groups preserve less, so geometries are ordered by their groups, and one space can carry several geometries. The idea turned geometry into the study of transformation groups and their invariants, and it fed directly into Lie theory, physics and, later, category theory.

## Core tenets

1. **A geometry is a group acting on a space, and its theorems are statements invariant under the group.** Two figures are "the same" when some group element carries one to the other. Because the transformations form a group, this sameness is an equivalence relation: the identity gives reflexivity, inverses give symmetry and composition gives transitivity, as in [group actions](../../05-abstract-algebra/01-groups/group-actions.md). Without the group axioms, "congruence" would not partition figures into classes. Euclidean geometry is the case of the rigid motions, whose invariants are lengths and angles.

2. **A bigger group means fewer invariants, so geometries form a hierarchy.** The rigid motions sit inside the similarities (which forget size but keep angles), these inside the affine maps (which keep parallelism and ratios along a line), and these inside the [projective maps](projective-geometry.md) (which keep only incidence and cross-ratio). Each enlargement deletes invariants and merges classes: all triangles are affinely equivalent, all ellipses, parabolas and hyperbolas projectively equivalent.

   ```
   Euclidean ⊂ similarity ⊂ affine ⊂ projective        (groups)
   length, angle ⊃ angle, ratio ⊃ parallelism, ratio on a line ⊃ cross-ratio, incidence
   ```

3. **Non-Euclidean geometries are subgeometries of projective geometry.** Fix a conic in the projective plane and keep only the projective maps preserving it. Inside the conic their invariants are those of the hyperbolic plane, the Beltrami–Klein model of [non-Euclidean geometry](non-euclidean-geometry.md), with distance measured by the cross-ratio. Klein's point was that hyperbolic geometry is not a rival to projective geometry but a chapter of it, picked out by a subgroup.

4. **Homogeneous spaces are quotients of the group.** If G acts transitively on X and H is the stabiliser of a point, the orbit–stabiliser theorem identifies X with the coset space G/H, so the space can be rebuilt from the group alone. The standard examples are below; their stabilisers say what a point "looks like" from inside, all directions being equivalent.

   ```
   ℝⁿ = E(n)/O(n)     Sⁿ = SO(n+1)/SO(n)     hyperbolic plane = PSL(2, ℝ)/SO(2)
   ```

5. **Invariants become the programme's working method.** To understand a geometry one finds a complete set of invariants, quantities that are unchanged by the group and that together decide when two objects are equivalent. Triangles under rigid motions are classified by three side lengths; four collinear points under projective maps by one cross-ratio; quadratic forms under change of basis by rank and signature. Invariant theory, the algebra of polynomials unchanged by a group, grew from this question.

6. **The programme's limit is that a curved space usually has no symmetries.** A generic Riemannian metric has only the identity as isometry, so Klein's description does not cover [Riemannian manifolds](../02-differential-geometry/riemannian-manifolds.md). Élie Cartan extended it by letting each point carry its own copy of a Klein geometry, glued with curvature measuring the failure to fit; the constant-curvature spaces are exactly the ones Klein covered.

7. **Groups-and-invariants thinking spread far beyond geometry.** Special relativity is the geometry of the Lorentz group, whose invariant is the space-time interval. [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md) turns each continuous symmetry of a physical system into a conserved quantity. Continuous transformation groups became [Lie groups](../04-lie-theory/lie-groups-and-lie-algebras.md), and the insistence on transformations rather than objects anticipates [categories and functors](../../13-structure-and-metamathematics/01-category-theory/categories-and-functors.md).

## Key concepts

| Term | Meaning |
|---|---|
| Transformation group | A group of bijections of a space, closed under composition and inverse |
| Invariant | A quantity or property unchanged by every element of the group |
| Congruence | Equivalence of figures under the group; an equivalence relation because the group is a group |
| Affine map | x ↦ Ax + b with A invertible; preserves parallelism and ratios along lines |
| Homogeneous space | A space on which the group acts transitively; it equals G/H |
| Stabiliser | The elements fixing a given point |
| Complete set of invariants | Invariants that together decide equivalence |
| Cartan geometry | A curved space modelled at each point on a homogeneous space |

## How it fits

- **Below:** [Group actions](../../05-abstract-algebra/01-groups/group-actions.md) supply orbits, stabilisers and the orbit–stabiliser theorem; the classical geometries supply examples.
- **Above:** [Lie groups](../04-lie-theory/lie-groups-and-lie-algebras.md) make the groups smooth; [Noether's theorem](../../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md) turns symmetry into conservation.
- **Siblings:** It organises [Euclidean](euclidean-geometry.md), [non-Euclidean](non-euclidean-geometry.md) and [projective geometry](projective-geometry.md), and takes discrete groups from [symmetry groups and tilings](symmetry-groups-and-tilings.md).

## Common misconceptions

- **"A geometry is a set of axioms"**: For Klein a geometry is a space with a group; the same space ℝ² carries Euclidean, affine and, after adding a line at infinity, projective geometry.
- **"A larger group gives a richer geometry"**: It gives fewer invariants and coarser equivalence; projective geometry says less about a triangle than Euclidean geometry does.
- **"The programme covers all of modern geometry"**: Generic curved spaces have no symmetries; Riemann's and Cartan's ideas were needed alongside Klein's.

## Go deeper

- Klein, "Vergleichende Betrachtungen über neuere geometrische Forschungen" (1872): the programme itself, a short pamphlet.
- Stillwell, *The Four Pillars of Geometry* (2005): the Euclidean, affine, projective and hyperbolic chain in the Erlangen spirit.
- Sharpe, *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program* (1997): how Cartan made Klein's idea curved.
