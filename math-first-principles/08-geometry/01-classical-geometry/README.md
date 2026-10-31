# Classical Geometry

> **Layer:** [08 Geometry](../README.md) › Classical Geometry
> **Children:** [Euclidean Geometry](euclidean-geometry.md) · [Non-Euclidean Geometry](non-euclidean-geometry.md) · [Projective Geometry](projective-geometry.md) · [Symmetry Groups and Tilings](symmetry-groups-and-tilings.md) · [The Erlangen Programme](the-erlangen-programme.md)

## What this area is about

Classical geometry is the story of how geometry stopped being a single body of truths about space and became a family of theories. It starts with Euclid's postulates and the suspicious fifth one, passes through the discovery that denying it gives a consistent hyperbolic geometry, adds the points at infinity of projective geometry, and ends with Klein's 1872 answer to "what is a geometry?": a space with a group acting on it, studied through the group's invariants.

Two themes run through it. The first is the axiomatic method: Hilbert's axioms and the hyperbolic models are the founding examples of categoricity, relative consistency and independence. The second is symmetry: the rigid motions, the projective group and the discrete crystallographic groups are the groups whose invariants define each geometry.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Euclidean geometry](euclidean-geometry.md) | The original axiom system, its gaps and Hilbert's repair; the rigid-motion group | Axiomatic method, real numbers |
| [Non-Euclidean geometry](non-euclidean-geometry.md) | Denies the parallel postulate; models prove its independence | Euclidean geometry |
| [Projective geometry](projective-geometry.md) | Adds points at infinity; duality, cross-ratio, Desargues and Pappus | Euclidean geometry, linear algebra |
| [Symmetry groups and tilings](symmetry-groups-and-tilings.md) | Classifies discrete groups of rigid motions; aperiodic tilings | Euclidean geometry, groups |
| [The Erlangen programme](the-erlangen-programme.md) | Unifies the rest: geometry = group plus invariants | All four siblings |

Euclidean geometry comes first because every other child modifies it: non-Euclidean geometry changes one axiom, projective geometry enlarges the space and the group, and symmetry groups study the discrete subgroups of its rigid motions. The Erlangen programme comes last because it explains the others as one pattern. In Klein's hierarchy the Euclidean group sits inside the affine group, which sits inside the projective group, while the hyperbolic plane is the part of projective geometry that preserves a fixed conic.

```
                 Erlangen programme: (space, group) -> invariants
                /            |               |                  \
        Euclidean  ->  non-Euclidean     projective      symmetry groups
       (rigid motions)  (PSL(2,ℝ))     (PGL(3,ℝ))      (discrete subgroups)
```

## Connections to sibling areas

- [Differential geometry](../02-differential-geometry/README.md): hyperbolic and spherical geometry are the constant-curvature cases; Gauss–Bonnet explains the angle-sum formulas.
- [Convex and discrete geometry](../03-convex-and-discrete-geometry/README.md): lattices from crystallography return in sphere packing, and symmetric solids in polytopes.
- [Lie theory](../04-lie-theory/README.md): the continuous groups of the Erlangen programme, such as SO(3) and PSL(2, ℝ), are Lie groups.

## Connections across layers

- [00 Logic and proof](../../00-logic-and-proof/README.md): Hilbert's axioms and the independence of the parallel postulate are the model cases of the axiomatic method.
- [05 Abstract algebra](../../05-abstract-algebra/README.md): group actions, and fields for ruler-and-compass constructions and for the coordinates behind Desargues and Pappus.
- [12 Number theory and algebraic geometry](../../12-number-theory-and-algebraic-geometry/README.md): projective space is the home of varieties and elliptic curves.
- [13 Structure and metamathematics](../../13-structure-and-metamathematics/README.md): Tarski's decidability of elementary geometry and the undecidability of tiling.

## Cross-cutting threads

- [Symmetry](../../CROSS-CUTTING.md#symmetry): a geometry is defined by its symmetry group.
- [Invariants](../../CROSS-CUTTING.md#invariants): cross-ratio, angle deficit and lengths as the content of each geometry.
- [Duality](../../CROSS-CUTTING.md#duality): points and lines exchange in the projective plane.
- [Impossibility and obstruction](../../CROSS-CUTTING.md#impossibility-and-obstruction): the parallel postulate cannot be proved; fivefold periodic symmetry cannot occur.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): 7 frieze, 17 wallpaper and 230 space groups.
