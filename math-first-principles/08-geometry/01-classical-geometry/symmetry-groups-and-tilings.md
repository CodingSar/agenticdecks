# Symmetry Groups and Tilings

> **Layer:** [08 Geometry](../README.md) › [Classical Geometry](README.md)
> **Builds on:** [Groups and subgroups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md), [Group actions](../../05-abstract-algebra/01-groups/group-actions.md), [Euclidean geometry](euclidean-geometry.md)
> **Enables:** [The Erlangen programme](the-erlangen-programme.md), [Polytopes](../03-convex-and-discrete-geometry/polytopes.md), [Lattices and sphere packing](../03-convex-and-discrete-geometry/lattices-and-sphere-packing.md), [Undecidable problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md)

## Essence

The symmetries of a pattern are the rigid motions that map it onto itself, and they always form a group. For repeating patterns this group is discrete and contains translations in independent directions, and a short argument shows that only rotations of order 1, 2, 3, 4 and 6 can occur. That restriction makes the classification finite: 7 frieze groups for strip patterns, 17 wallpaper groups for the plane and 230 space groups for crystals. Tilings that never repeat, such as Penrose's, escape the classification, and in 2023 a single tile was found that tiles the plane only non-periodically.

## Core tenets

1. **Symmetries form a group, and every plane isometry is one of four kinds.** A composite or inverse of maps preserving a pattern also preserves it, so the symmetries form a subgroup of the Euclidean group. Every isometry of the plane is a translation, a rotation, a reflection or a glide reflection (reflect, then translate along the mirror): by [Euclidean geometry](euclidean-geometry.md) it is x ↦ Ax + b with A orthogonal, and sorting by whether A is a rotation or a reflection and whether it has a fixed point gives the four cases.

2. **The crystallographic restriction: a lattice allows only rotations of order 1, 2, 3, 4 or 6.** If a rotation by θ maps a lattice to itself, its matrix in a lattice basis has integer entries, so its trace 2 cos θ is an integer in [−2, 2]. That leaves cos θ ∈ {±1, ±½, 0}, rotations of order 1, 2, 3, 4 and 6. Fivefold symmetry is therefore impossible for a periodic pattern, which is why it was so startling in quasicrystals.

3. **Strip patterns have 7 symmetry groups and plane patterns have 17.** A frieze group has translations in one direction; its possible extra symmetries (half-turns, horizontal and vertical mirrors, glides) combine in exactly 7 ways. A wallpaper group has translations in two independent directions; combining the five allowed rotation orders with mirrors and glides compatible with the lattice gives exactly 17, classified by Fedorov in 1891. Conway's orbifold notation reads each group off its quotient surface, and an Euler-characteristic count of the quotient shows why the list stops.

4. **In space there are 230 crystallographic groups.** Fedorov and Schoenflies independently found in 1891 that there are 230 space groups, built on 32 crystal classes (the possible groups of rotations and reflections fixing a point). Eleven of the 230 come in mirror-image pairs that differ only in handedness, so there are 219 up to orientation-reversing equivalence. Bieberbach proved that every dimension has only finitely many crystallographic groups, part of Hilbert's eighteenth problem, and that each contains a lattice of translations of finite index.

5. **Hyperbolic space has infinitely many regular tilings.** Regular p-gons meet q at a vertex in the Euclidean plane only when (p − 2)(q − 2) = 4, giving the square, triangle and hexagon tilings; the sphere needs (p − 2)(q − 2) < 4, the [Platonic solids](../03-convex-and-discrete-geometry/polytopes.md). In the [hyperbolic plane](non-euclidean-geometry.md), where polygon angles can be made as small as needed, every pair with (p − 2)(q − 2) > 4 works, so the crystallographic finiteness disappears.

6. **Aperiodic tilings exist, and their existence is tied to undecidability.** Wang asked whether every set of tiles that tiles the plane also tiles it periodically; if so, tileability would be decidable. Berger (1966) proved the domino problem undecidable, so aperiodic tile sets must exist, and he built one with thousands of tiles ([undecidable problems](../../13-structure-and-metamathematics/02-computability-and-incompleteness/undecidable-problems.md)). Penrose reduced the number to two, the kite and dart, in the 1970s. Aperiodicity is proved by substitution: every tiling can be grouped uniquely into larger tiles of the same shapes, and a periodic tiling would contradict that hierarchy. Penrose tilings have fivefold local symmetry, and Shechtman's discovery of quasicrystals in 1982 showed nature uses such order.

7. **A single tile can force aperiodicity.** In 2023 Smith, Myers, Kaplan and Goodman-Strauss announced the "hat", a polygon made of eight kites that tiles the plane, but never periodically; its tilings use the tile and its mirror image. Later that year the same authors gave the "spectre", a related tile that is aperiodic using only rotated and translated copies. Both proofs rest on substitution hierarchies.

## Key concepts

| Term | Meaning |
|---|---|
| Symmetry group | The isometries mapping a figure onto itself |
| Glide reflection | A reflection followed by a translation along the mirror line |
| Lattice | The integer combinations of n independent vectors |
| Crystallographic restriction | Lattice-preserving rotations have order 1, 2, 3, 4 or 6 |
| Frieze group | A discrete symmetry group of a strip pattern; there are 7 |
| Wallpaper group | A discrete plane symmetry group with two independent translations; there are 17 |
| Space group | A discrete group of isometries of ℝ³ with three independent translations; there are 230 |
| Aperiodic tile set | Tiles that tile the plane but never periodically |
| Substitution | Grouping tiles into larger copies of the same shapes, used to prove aperiodicity |

## How it fits

- **Below:** [Groups and subgroups](../../05-abstract-algebra/01-groups/groups-and-subgroups.md) and [group actions](../../05-abstract-algebra/01-groups/group-actions.md) supply the language; [Euclidean geometry](euclidean-geometry.md) the isometries.
- **Above:** Lattices return in [lattices and sphere packing](../03-convex-and-discrete-geometry/lattices-and-sphere-packing.md) and symmetric solids in [polytopes](../03-convex-and-discrete-geometry/polytopes.md); the [continuous symmetry groups](../04-lie-theory/lie-groups-and-lie-algebras.md) of Lie theory are the smooth counterpart.
- **Siblings:** [The Erlangen programme](the-erlangen-programme.md) makes the symmetry group the definition of a geometry; [non-Euclidean geometry](non-euclidean-geometry.md) hosts the hyperbolic tilings.

## Common misconceptions

- **"There are infinitely many kinds of wallpaper"**: The motifs vary endlessly, but the symmetry groups are exactly 17.
- **"Penrose tilings are random"**: They are highly ordered, with every finite patch recurring infinitely often; they lack only translational symmetry.
- **"The hat settled the problem only with a technicality"**: The need for mirror images was a genuine gap, and the spectre removed it.

## Go deeper

- Weyl, *Symmetry* (1952): the classic short essay on ornaments, crystals and groups.
- Grünbaum and Shephard, *Tilings and Patterns* (1987): the standard reference on tilings, including aperiodic sets.
- Conway, Burgiel and Goodman-Strauss, *The Symmetries of Things* (2008): the orbifold notation and the classification made visual.
