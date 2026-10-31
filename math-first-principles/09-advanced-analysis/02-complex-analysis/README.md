# Complex Analysis

> **Layer:** [09 Advanced Analysis](../README.md) › Complex Analysis
> **Children:** [Holomorphic Functions](holomorphic-functions.md) · [Cauchy's Theorem and Its Consequences](cauchys-theorem-and-its-consequences.md) · [Singularities and Residues](singularities-and-residues.md) · [Conformal Maps and the Riemann Mapping Theorem](conformal-maps-and-the-riemann-mapping-theorem.md) · [Analytic Continuation and Riemann Surfaces](analytic-continuation-and-riemann-surfaces.md)

## What this area is about

Complex analysis is calculus with complex numbers, and it behaves nothing like its real counterpart. Asking a function of one complex variable to be differentiable once forces it to be differentiable infinitely often, to equal its Taylor series, and to be determined everywhere by its values on any small disc. These functions are rigid enough to be studied like polynomials and flexible enough to map any simply connected region of the plane onto a disc.

The engine is Cauchy's theorem: integrals of holomorphic functions around closed curves vanish unless the curve encircles a singularity, and the amount that survives is a residue. From this one fact come exact evaluation of real integrals, the counting of zeros, the fundamental theorem of algebra, and the link between the poles of a generating function and the growth of its coefficients. Topology enters as soon as a function is followed around a hole, and Riemann surfaces are the spaces that make multivalued functions single-valued. The area uses only [layer 06](../../06-real-analysis/README.md), the [complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) and some [topology](../../07-topology/README.md), so it stands apart from measure theory.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Holomorphic Functions](holomorphic-functions.md) | Complex differentiability, Cauchy–Riemann, power series, rigidity | Complex numbers, multivariable derivative |
| [Cauchy's Theorem and Its Consequences](cauchys-theorem-and-its-consequences.md) | Integrals around loops vanish; the integral formula and its corollaries | Holomorphic functions, Green's theorem |
| [Singularities and Residues](singularities-and-residues.md) | Laurent series, the residue theorem, counting zeros | Cauchy's theorem |
| [Conformal Maps and the Riemann Mapping Theorem](conformal-maps-and-the-riemann-mapping-theorem.md) | Angle-preserving maps; every simply connected proper region is a disc | Cauchy's estimates, compactness |
| [Analytic Continuation and Riemann Surfaces](analytic-continuation-and-riemann-surfaces.md) | Extending functions along paths; the surfaces on which they live | Identity theorem, covering spaces |

```
              holomorphic functions
                        │
                        ▼
            Cauchy's theorem and formula
             │          │            │
             ▼          ▼            ▼
      singularities   conformal   analytic continuation
      and residues      maps    ─►  and Riemann surfaces
             │                          ▲
             └────── branch points ─────┘
```

The story starts with [holomorphic functions](holomorphic-functions.md): the derivative must be a rotation and scaling, which gives the Cauchy–Riemann equations. [Cauchy's theorem](cauchys-theorem-and-its-consequences.md) then makes the integral formula possible, and from it come power series, Liouville's theorem and the maximum principle. Three directions open from there. [Residues](singularities-and-residues.md) look at isolated singularities and turn integrals into sums. [Conformal maps](conformal-maps-and-the-riemann-mapping-theorem.md) look at holomorphic functions as geometric transformations and, using Cauchy's estimates for compactness, prove the Riemann mapping theorem. [Analytic continuation](analytic-continuation-and-riemann-surfaces.md) looks at what happens when a function is pushed beyond its first domain; the branch points it meets are the singularities that residues cannot handle, and uniformisation extends the mapping theorem to every simply connected Riemann surface.

## Connections to sibling areas

- **[Measure and Integration](../01-measure-and-integration/README.md):** the basic theory needs only path integrals, but boundary values of holomorphic functions on the disc, the Hardy spaces, need Lebesgue measure and Lᵖ.
- **[Functional Analysis](../03-functional-analysis/README.md):** the spectrum of a bounded operator is non-empty by Liouville's theorem, and holomorphic functional calculus defines f(T) by Cauchy's integral formula; Hilbert-space methods prove that Riemann surfaces carry meromorphic functions.
- **[Harmonic Analysis](../04-harmonic-analysis/README.md):** a Fourier series is a Laurent series restricted to the unit circle, the Fourier transform is often computed by residues, and the Paley–Wiener theorem relates compact support to entire transforms.

## Connections across layers

Complex analysis rests on the [complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md) of 02, on [series](../../06-real-analysis/01-limits-and-convergence/series.md), [uniform convergence](../../06-real-analysis/01-limits-and-convergence/uniform-convergence.md) and the [integral theorems](../../06-real-analysis/04-calculus-of-several-variables/vector-calculus-and-the-integral-theorems.md) of 06, and on [homotopy](../../07-topology/02-algebraic-topology/homotopy-and-the-fundamental-group.md) and [covering spaces](../../07-topology/02-algebraic-topology/covering-spaces.md) of 07. Its symmetries are the [hyperbolic geometry](../../08-geometry/01-classical-geometry/non-euclidean-geometry.md) of 08. Upward, its main customer is layer 12: the [zeta function](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-riemann-zeta-function.md), the [prime number theorem](../../12-number-theory-and-algebraic-geometry/02-analytic-number-theory/the-prime-number-theorem.md), [modular forms](../../12-number-theory-and-algebraic-geometry/04-elliptic-curves-and-modular-forms/modular-forms.md) and [algebraic curves](../../12-number-theory-and-algebraic-geometry/03-algebraic-geometry/algebraic-curves-and-riemann-roch.md). In 10, [harmonic functions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/laplaces-equation-and-harmonic-functions.md) in the plane are real parts of holomorphic ones, and in 03 [generating functions](../../03-combinatorics-and-graph-theory/01-enumeration/generating-functions.md) are analysed through their singularities.

## Cross-cutting threads

- [Local to global](../../CROSS-CUTTING.md#local-to-global): a holomorphic function is determined everywhere by its germ at one point.
- [Invariants](../../CROSS-CUTTING.md#invariants): the winding number and the residue survive every deformation of the contour.
- [Symmetry](../../CROSS-CUTTING.md#symmetry): Möbius maps and the automorphisms of the disc are the isometries of hyperbolic geometry.
- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): Montel's theorem provides the extremal map in the Riemann mapping theorem.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): isolated singularities are of three kinds, and simply connected Riemann surfaces of three.
- [Dictionaries between fields](../../CROSS-CUTTING.md#dictionaries-between-fields): compact Riemann surfaces are algebraic curves.
