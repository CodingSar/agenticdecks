# 08 Geometry

> **Layer:** 08 Geometry
> **Children:** [Classical Geometry](01-classical-geometry/README.md) · [Differential Geometry](02-differential-geometry/README.md) · [Convex and Discrete Geometry](03-convex-and-discrete-geometry/README.md) · [Lie Theory](04-lie-theory/README.md)

## What this area is about

Geometry is the study of shape, size and symmetry, and of what stays the same when a space is moved, bent or projected. It is the oldest branch of mathematics with a deductive method: Euclid's *Elements* set the pattern of axioms, definitions and proofs that the rest of mathematics adopted. The modern subject has three threads. The first is axiomatic and synthetic: Euclid's postulates, the discovery that the parallel postulate is independent, and the projective and non-Euclidean geometries that followed. The second is analytic: curvature measured by calculus, from curves in the plane to Riemannian manifolds of any dimension, with the Gauss–Bonnet theorem tying local curvature to global topology. The third is algebraic: Klein's insight that a geometry is determined by its symmetry group, carried through by Lie theory, which classifies the continuous symmetry groups and their linear actions.

Alongside these runs a combinatorial strand, convex and discrete geometry, where separation by hyperplanes, polytopes and lattices meet optimisation and number theory, and where some of the most recent theorems, on sphere packing in dimensions 8 and 24, were proved.

## Why this layer sits here

Geometry draws on almost every earlier layer. [04 Linear Algebra](../04-linear-algebra/README.md) supplies inner products, determinants, eigenvalues and quadratic forms: Euclidean space is a real inner product space, and the classification of Lie algebras runs on diagonalisation and positive-definite forms. [05 Abstract Algebra](../05-abstract-algebra/README.md) supplies groups and group actions, which the Erlangen programme makes the definition of a geometry. [06 Real Analysis](../06-real-analysis/README.md) supplies the calculus of several variables and the implicit function theorem, without which curvature and smooth manifolds cannot be defined. [07 Topology](../07-topology/README.md) supplies manifolds, covering spaces and the Euler characteristic, the global invariants that curvature integrates to. Underneath, [00 Logic and Proof](../00-logic-and-proof/README.md) frames the independence of the parallel postulate.

In return, geometry is the setting for much of what follows. Harmonic analysis in 09 is Fourier analysis on Lie groups; differential equations in 10 live on manifolds, and their symmetries give conservation laws; algebraic geometry in 12 studies shapes cut out by polynomials; and the physics of 14 is written in the language of curvature and symmetry groups.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Classical Geometry](01-classical-geometry/README.md) | Euclidean, non-Euclidean and projective geometry; symmetry groups and tilings; the Erlangen programme | 00 axioms and consistency, 04 inner products, 05 group actions |
| [Differential Geometry](02-differential-geometry/README.md) | Curvature of curves and surfaces, Gauss–Bonnet, differential forms, Riemannian manifolds | 06 several-variable calculus, 07 manifolds and topology |
| [Convex and Discrete Geometry](03-convex-and-discrete-geometry/README.md) | Separation, polytopes, lattices and sphere packing | 04 linear algebra, 06 compactness, 07 Euler characteristic |
| [Lie Theory](04-lie-theory/README.md) | Continuous symmetry groups, their classification and representations | Classical and differential geometry, 05 groups, 07 coverings |

Classical geometry comes first because it poses the questions: which axioms describe space, how many geometries there are, and how symmetry organises them. Differential geometry answers the question of curvature, and shows that the hyperbolic plane of classical geometry is the surface of constant negative curvature. Convex and discrete geometry takes the linear structure of Euclidean space in a combinatorial direction. Lie theory closes the layer by making Klein's programme precise: the isometry groups of the classical geometries and of Riemannian manifolds are Lie groups, and their classification links back to the regular polytopes and the E₈ lattice of convex geometry.

```
            04 inner products     05 group actions     06 calculus     07 manifolds
                    │                    │                  │               │
                    ▼                    ▼                  ▼               ▼
  classical geometry ── Erlangen: geometry = space + group ──┐    differential geometry
  Euclid, hyperbolic, projective, tilings                    │    curvature, Gauss–Bonnet,
         │                                                   │    forms, Riemannian metrics
         ▼                                                   ▼               │
  convex and discrete geometry ◄── root systems, E₈ ──── Lie theory ◄────────┘
  separation, polytopes, lattices                       groups, roots, representations
```

## Connections to neighbouring layers

- **[04 Linear Algebra](../04-linear-algebra/README.md):** inner products define length and angle; quadratic forms describe lattices and the Killing form.
- **[05 Abstract Algebra](../05-abstract-algebra/README.md):** group actions define geometries; the representations of finite groups are the model for those of compact Lie groups.
- **[06 Real Analysis](../06-real-analysis/README.md):** the implicit function theorem builds surfaces and matrix groups; Stokes's theorem becomes the general Stokes theorem for forms.
- **[07 Topology](../07-topology/README.md):** Gauss–Bonnet makes the Euler characteristic a total curvature; de Rham cohomology recovers topology from calculus; SU(2) covers SO(3) twice.
- **[09 Advanced Analysis](../09-advanced-analysis/README.md):** Hahn–Banach is separation in infinite dimensions; the Peter–Weyl theorem is Fourier analysis on compact groups; Fourier methods proved the packing bounds.
- **[10 Differential Equations and Dynamics](../10-differential-equations-and-dynamics/README.md):** geodesics solve differential equations, Ricci flow deforms metrics, and [Noether's theorem](../10-differential-equations-and-dynamics/03-calculus-of-variations/noethers-theorem.md) turns Lie group symmetries into conserved quantities.
- **[12 Number Theory and Algebraic Geometry](../12-number-theory-and-algebraic-geometry/README.md):** projective space is where algebraic curves live; Minkowski's lattice theorem proves finiteness of class numbers; the Langlands programme is organised by reductive groups.
- **[14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md):** curvature of spacetime in [the geometry of general relativity](../14-applied-and-computational-mathematics/04-mathematical-modelling/the-geometry-of-general-relativity.md); spin and symmetry in quantum mechanics; convex optimisation and lattice cryptography.

## Connections across layers

Geometry is everywhere in computing. Homogeneous coordinates from projective geometry, and quaternions for rotations, are the working tools of [computer graphics](../../cs-first-principles/14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) and of camera models in [computer vision](../../cs-first-principles/14-human-and-visual-computing/03-media-and-vision/computer-vision.md). Convex hulls and polytopes are core problems of [computational geometry](../../cs-first-principles/05-algorithms-and-data-structures/07-advanced-topics/computational-geometry.md). Lattice problems underpin the post-quantum standards described in [public-key cryptography](../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md). In the history of ideas, the independence of the parallel postulate changed what mathematicians took axioms to be, a story told in the [history of mathematics](../15-mathematics-in-context/history-of-mathematics.md).

## Cross-cutting threads

- [Symmetry](../CROSS-CUTTING.md#symmetry): the Erlangen programme, crystallographic groups and Lie groups.
- [Invariants](../CROSS-CUTTING.md#invariants): Gaussian curvature, the Euler characteristic and cross-ratio.
- [Local to global](../CROSS-CUTTING.md#local-to-global): Gauss–Bonnet, de Rham's theorem and Lie algebras up to coverings.
- [Duality](../CROSS-CUTTING.md#duality): points and lines in the projective plane; points and half-spaces in convexity.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): the parallel postulate cannot be proved, and the Dehn invariant blocks dissections.
- [Decomposition and classification](../CROSS-CUTTING.md#decomposition-and-classification): wallpaper groups, regular polytopes and simple Lie algebras.
- [Linearisation](../CROSS-CUTTING.md#linearisation): tangent spaces, Lie algebras and the exponential map.
