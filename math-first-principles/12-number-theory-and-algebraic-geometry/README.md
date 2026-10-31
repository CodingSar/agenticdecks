# 12 Number Theory and Algebraic Geometry

> **Layer:** 12 Number Theory and Algebraic Geometry
> **Children:** [Algebraic Number Theory](01-algebraic-number-theory/README.md) · [Analytic Number Theory](02-analytic-number-theory/README.md) · [Algebraic Geometry](03-algebraic-geometry/README.md) · [Elliptic Curves and Modular Forms](04-elliptic-curves-and-modular-forms/README.md)

## What this area is about

Number theory asks about the integers: which equations have integer solutions, how the primes are distributed, which numbers are sums of squares. Its questions are easy to state and often extraordinarily hard to answer, and the answers have repeatedly required the rest of mathematics. Algebraic geometry asks about the solution sets of polynomial equations, treated as shapes. The two were once separate. In the twentieth century they merged, because the way to understand integer solutions of an equation turned out to be to understand the shape it defines, over ℂ, over finite fields and over the p-adic numbers, all at once.

The layer has four areas. Algebraic number theory enlarges ℤ to rings of algebraic integers, repairs the failure of unique factorisation with ideals, and studies one prime at a time with p-adic numbers, culminating in class field theory. Analytic number theory counts primes with the zeta function and its relatives, proving the prime number theorem (PNT) and Dirichlet's theorem and reaching the limits of current knowledge in the Riemann Hypothesis (RH) and the twin prime conjecture. Algebraic geometry builds the dictionary between ideals and varieties, makes intersection counts exact in projective space, classifies curves by genus, and generalises everything to schemes. Elliptic curves and modular forms bring the strands together: the modularity theorem, which proved Fermat's Last Theorem, is a two-dimensional instance of the Langlands programme.

## Why this layer sits here

This layer uses almost every earlier one. It needs groups, rings, fields and Galois theory from [05 Abstract Algebra](../05-abstract-algebra/README.md) on every page; complex analysis and Fourier analysis from [09 Advanced Analysis](../09-advanced-analysis/README.md) for the zeta function and modular forms; projective and hyperbolic geometry and Lie groups from [08 Geometry](../08-geometry/README.md); the Zariski topology, compactness and surfaces from [07 Topology](../07-topology/README.md); and completeness from real analysis to build the p-adic numbers. It comes after these because it combines them, not because it is more abstract. It comes before [13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md) because much of category theory and homological algebra was developed to serve algebraic geometry and class field theory, and the examples should come first.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Algebraic Number Theory](01-algebraic-number-theory/README.md) | number fields, ideals and class groups, p-adic fields, class field theory | 05 algebra, 02 elementary number theory |
| [Analytic Number Theory](02-analytic-number-theory/README.md) | the zeta function, the PNT, primes in progressions, sieves | 09 complex and Fourier analysis |
| [Algebraic Geometry](03-algebraic-geometry/README.md) | varieties, Bézout, curves and Riemann–Roch, schemes | 05 rings, 07 topology, 08 projective geometry |
| [Elliptic Curves and Modular Forms](04-elliptic-curves-and-modular-forms/README.md) | elliptic curves, modular forms, Fermat's Last Theorem, Langlands | all three |

The first three areas are largely independent and can be read in any order, though each borrows from the others: the class number formula joins the first two, and schemes treat rings of integers as curves. The fourth area needs all three. Its central theorem says that the point counts of an elliptic curve mod p, a geometric and arithmetic quantity, are the Hecke eigenvalues of a modular form, an analytic one.

```
 algebraic number theory     analytic number theory     algebraic geometry
 (ideals, p-adics, CFT)      (ζ, L-functions, sieves)   (varieties, curves, schemes)
            │                          │                          │
            └──────────────┬───────────┴──────────────┬───────────┘
                           ▼                          ▼
                    elliptic curves  ◄─ modularity ─► modular forms
                           │                          │
                           └──── Fermat's Last Theorem ┘
                                          │
                                          ▼
                               the Langlands programme
```

Here CFT stands for class field theory.

## Connections to neighbouring layers

- [02 Number Systems](../02-number-systems/README.md): primes, unique factorisation, congruences and quadratic reciprocity are the elementary results this layer generalises.
- [05 Abstract Algebra](../05-abstract-algebra/README.md): Dedekind domains, Galois groups, finite fields and representations are the working language.
- [07 Topology](../07-topology/README.md): the Zariski topology, the genus of a surface, and compactness of ℤ_p and of projective space.
- [08 Geometry](../08-geometry/README.md): projective space for Bézout, the hyperbolic plane for modular forms, Lie groups for the automorphic side of Langlands.
- [09 Advanced Analysis](../09-advanced-analysis/README.md): analytic continuation, residues, Riemann surfaces and Fourier analysis on groups.
- [13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md): schemes and class field theory shaped category theory and homological algebra; the Nullstellensatz underlies quantifier elimination for algebraically closed fields; Hilbert's tenth problem shows that solvability of Diophantine equations is undecidable.
- [14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md): elliptic curves, prime density and number fields in cryptography; curves over finite fields in error-correcting codes.
- [15 Mathematics in Context](../15-mathematics-in-context/README.md): the Riemann Hypothesis, the Birch and Swinnerton-Dyer conjecture, twin primes and Goldbach are open as of 2026; the proof of Fermat's Last Theorem is a case study in how mathematics is done.

## Connections across layers

- **Below:** [primes and unique factorisation](../02-number-systems/02-elementary-number-theory/primes-and-unique-factorisation.md), [quadratic reciprocity](../02-number-systems/02-elementary-number-theory/quadratic-reciprocity.md), [the Galois correspondence](../05-abstract-algebra/03-galois-theory/the-galois-correspondence.md) and [analytic continuation](../09-advanced-analysis/02-complex-analysis/analytic-continuation-and-riemann-surfaces.md) are the most-used inputs.
- **Above:** [homological algebra](../13-structure-and-metamathematics/01-category-theory/homological-algebra.md), [cryptography](../14-applied-and-computational-mathematics/03-information-codes-and-cryptography/cryptography.md) and [open problems](../15-mathematics-in-context/open-problems.md) draw directly on this layer.
- **In computer science:** [public-key cryptography](../../cs-first-principles/11-security-and-cryptography/02-cryptography/public-key-cryptography.md) uses prime density, modular arithmetic and elliptic curves.

## Cross-cutting threads

- [Local to global](../CROSS-CUTTING.md#local-to-global): p-adic fields, Hasse–Minkowski, and L-functions assembled prime by prime.
- [Dictionaries between fields](../CROSS-CUTTING.md#dictionaries-between-fields): ideals and varieties, primes and zeros of ζ, elliptic curves and modular forms.
- [Duality](../CROSS-CUTTING.md#duality): functional equations, Serre duality and Langlands dual groups.
- [Equivalence and quotients](../CROSS-CUTTING.md#equivalence-and-quotients): class groups, Picard groups and modular curves.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): class groups, the Tate–Shafarevich group and the parity problem.
- [Approximation and limits](../CROSS-CUTTING.md#approximation-and-limits): asymptotic prime counts and p-adic approximation.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): from varieties to schemes, and from class field theory to Langlands.
- [Symmetry](../CROSS-CUTTING.md#symmetry): Galois groups and the modular group.
