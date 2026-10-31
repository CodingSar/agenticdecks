# Knot Theory

> **Layer:** [07 Topology](../README.md) › [Manifolds](README.md)
> **Builds on:** [Topological and Smooth Manifolds](topological-and-smooth-manifolds.md), [Homotopy and the Fundamental Group](../02-algebraic-topology/homotopy-and-the-fundamental-group.md), [Covering Spaces](../02-algebraic-topology/covering-spaces.md), [Free Groups and Presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md)
> **Enables:** [Three-Manifolds and the Poincaré Conjecture](three-manifolds-and-the-poincare-conjecture.md), [The Mathematics of Quantum Mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [Nucleic Acids (medicine)](../../../medicine-first-principles/02-biochemistry-and-molecular-biology/01-macromolecules/nucleic-acids.md)

## Essence

A knot is a closed loop of string in space with the ends fused, and two knots are the same if one can be moved into the other without cutting. The question "is this tangle really knotted?" sounds like a puzzle but is a deep problem: there is no obvious way to prove that no sequence of moves will undo a knot. The answer is to find invariants, quantities computed from a drawing that do not change under any move. A non-trivial value proves knottedness. The history of the subject is a sequence of ever sharper invariants: colourings, the linking number, the knot group, Alexander's polynomial of 1928 and Jones's polynomial of 1984, which came from operator algebras and turned out to be physics in disguise.

## Core tenets

1. **A knot is a tame embedding of a circle in ℝ³, up to ambient isotopy.** Tame means smooth or polygonal, which excludes wild knots with infinitely many tangles shrinking to a point. Two knots are equivalent if a continuous family of homeomorphisms of space carries one to the other. A mere homotopy would let the loop pass through itself and undo every knot. Dimension matters: in ℝ⁴ every knotted circle can be undone, because there is room to pass strands round each other.

2. **Reidemeister's theorem reduces knots to diagrams.** Project a knot to a plane, recording at each crossing which strand is on top. Two diagrams represent the same knot if and only if they are related by planar deformations and three local moves: adding or removing a twist (R1), sliding one strand over another (R2), and sliding a strand past a crossing (R3). So any quantity computed from a diagram and unchanged by the three moves is a knot invariant.

3. **Tricolourability proves the trefoil is knotted.** Colour each arc of a diagram with one of three colours so that at every crossing the three arcs meeting there are all the same colour or all different, using at least two colours. One checks that each Reidemeister move preserves the existence of such a colouring. The standard trefoil diagram is tricolourable; the unknot's diagram, a single arc, cannot use two colours. Hence the trefoil is not the unknot. The figure-eight knot is not tricolourable, yet it is also knotted: this invariant is too coarse to see it.

4. **The linking number counts how two loops wind round each other.** For a two-component link, add +1 or −1 for each crossing between the two components, according to its handedness, and halve the total. It is unchanged by the Reidemeister moves and equals Gauss's linking integral. The Hopf link (two interlocked rings) has linking number ±1, so it cannot be pulled apart. The Whitehead link has linking number 0 yet cannot be separated, showing that a zero invariant proves nothing.

5. **The knot group and its covers.** The [fundamental group](../02-algebraic-topology/homotopy-and-the-fundamental-group.md) of the complement ℝ³ − K is a strong invariant; a diagram gives a presentation with one generator per arc and one relation per crossing. The unknot's group is ℤ. The trefoil's group is ⟨x, y ∣ x² = y³⟩, which is not abelian (it maps onto the symmetric group S₃), so the trefoil is knotted. But deciding whether two presented groups are isomorphic is hard in general, so one passes to computable shadows.

6. **The Alexander polynomial (1928) is homology of a covering space.** The complement has an infinite cyclic [covering space](../02-algebraic-topology/covering-spaces.md), and the deck transformation t acts on its first homology. The resulting Laurent polynomial Δ(t), defined up to multiplication by ±tⁿ, is 1 for the unknot, t − 1 + t⁻¹ for the trefoil and −t + 3 − t⁻¹ for the figure-eight, which distinguishes all three. It satisfies Conway's skein relation, computed from three diagrams L₊, L₋, L₀ that differ at one crossing:

   ```
   Δ(L₊) − Δ(L₋) = (t^(1/2) − t^(−1/2)) · Δ(L₀)
   ```

   Its limits: it cannot tell a knot from its mirror image, and there are non-trivial knots with Δ = 1, such as the Conway knot.

7. **The Jones polynomial (1984) sees chirality, and its limits are open.** Vaughan Jones found a new polynomial V(t) while studying von Neumann algebras; Kauffman's bracket later gave a short combinatorial definition. The Jones polynomial distinguishes the left- and right-handed trefoils: mirroring replaces t by t⁻¹, and the trefoil's V is not symmetric. Witten interpreted it through a quantum field theory, opening the field of quantum invariants. Whether a non-trivial knot can have V = 1 is open as of 2026. Khovanov homology, a refinement of V, does detect the unknot, by a theorem of Kronheimer and Mrowka.

## Key concepts

| Term | Meaning |
|---|---|
| Knot | A tame embedding of a circle in ℝ³ or S³, up to ambient isotopy |
| Link | Several disjoint knotted circles considered together |
| Unknot | The round circle, the trivial knot |
| Reidemeister moves | Three local diagram changes that generate knot equivalence |
| Tricolourability | Existence of a 3-colouring of arcs obeying the crossing rule |
| Linking number | Signed count of crossings between two components, halved |
| Knot group | π₁ of the knot's complement |
| Skein relation | A linear rule relating invariants of diagrams that differ at one crossing |

## How it fits

- **Below:** knots are 1-manifolds embedded in a 3-[manifold](topological-and-smooth-manifolds.md); the knot group uses [π₁](../02-algebraic-topology/homotopy-and-the-fundamental-group.md) and [presentations](../../05-abstract-algebra/01-groups/free-groups-and-presentations.md); Alexander's invariant is homology of a [covering space](../02-algebraic-topology/covering-spaces.md).
- **Above:** surgery on knots builds every closed orientable [3-manifold](three-manifolds-and-the-poincare-conjecture.md); quantum invariants tie knots to [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) and field theory; in biology, topoisomerases and recombinases change the linking and knotting of [DNA](../../../medicine-first-principles/02-biochemistry-and-molecular-biology/01-macromolecules/nucleic-acids.md), and enzymes are identified partly by the knots they produce.
- **Siblings:** every knot bounds an orientable surface, a Seifert surface, and the least genus of such a surface is the knot's genus ([classification of surfaces](classification-of-surfaces.md)).

## Common misconceptions

- **"If a knot diagram looks complicated, the knot is complicated."**: Some unknot diagrams must first be made more complicated before they can be simplified.
- **"A knot is the same as its mirror image."**: The figure-eight knot is, but the trefoil is not; the Jones polynomial proves it, though the Alexander polynomial cannot.
- **"A zero linking number means the components come apart."**: The Whitehead link and the Borromean rings have all pairwise linking numbers 0 and are still linked.

## Go deeper

- Colin Adams, *The Knot Book* (1994): an inviting introduction with many open questions.
- Dale Rolfsen, *Knots and Links* (1976): the classic graduate text, rich in examples.
- W. B. Raymond Lickorish, *An Introduction to Knot Theory* (1997): the Jones polynomial and 3-manifolds.
