# 09 Advanced Analysis

> **Layer:** 09 Advanced Analysis
> **Children:** [Measure and Integration](01-measure-and-integration/README.md) · [Complex Analysis](02-complex-analysis/README.md) · [Functional Analysis](03-functional-analysis/README.md) · [Harmonic Analysis](04-harmonic-analysis/README.md)

## What this area is about

This layer asks how we measure, integrate and decompose in infinite dimensions. Real analysis in [layer 06](../06-real-analysis/README.md) handles one function at a time: its limits, derivatives and Riemann integral. Advanced analysis treats whole spaces of functions as geometric objects and asks which tools survive when the number of dimensions is infinite.

Four answers make up the layer. Measure theory decides which sets have a size and builds the Lebesgue integral, which commutes with limits and produces the complete function spaces Lᵖ. Complex analysis discovers that a single complex derivative makes a function rigid, analytic and controlled by contour integrals, with consequences from the fundamental theorem of algebra to the distribution of primes. Functional analysis studies Banach and Hilbert spaces and the operators between them, and generalises eigenvalues to the spectrum. Harmonic analysis decomposes functions into oscillations, from Fourier series on the circle to characters on arbitrary groups, with distributions making room for the Dirac delta.

What unites them is a pattern: an object that is hard to study directly, such as a rough function, a differential operator or a signal, is placed in a complete space where limits exist, and then decomposed into simple pieces, such as level sets, power series, eigenvectors or frequencies. The layer's contribution to the whole is measure, holomorphy, Banach and Hilbert spaces, and Fourier analysis.

## Why this layer sits here

It sits after [real analysis](../06-real-analysis/README.md) because every construction here starts from limits, metric completeness and compactness, and after [linear algebra](../04-linear-algebra/README.md) because Banach and Hilbert spaces are vector spaces and the spectral theorem has a finite-dimensional model. It needs [topology](../07-topology/README.md) for compactness in general spaces and for the covering spaces on which multivalued complex functions become single-valued, [abstract algebra](../05-abstract-algebra/README.md) for groups and their representations, and [sets and foundations](../01-sets-and-foundations/README.md) for cardinality and the axiom of choice, which make non-measurable sets and the Hahn–Banach theorem possible.

It sits before [differential equations](../10-differential-equations-and-dynamics/README.md), [probability](../11-probability-and-statistics/README.md) and [number theory](../12-number-theory-and-algebraic-geometry/README.md) because each of them is, in large part, an application of this layer: weak solutions live in Sobolev spaces built from Lᵖ and distributions; probability is measure theory with total mass 1; the prime number theorem is proved by contour integration. [Applied mathematics](../14-applied-and-computational-mathematics/README.md) uses it for quantum mechanics, signal processing and the stability of numerical methods.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Measure and Integration](01-measure-and-integration/README.md) | Size of sets, the Lebesgue integral, Lᵖ spaces, densities, fractal dimension | 06, 01 |
| [Complex Analysis](02-complex-analysis/README.md) | Holomorphic functions, Cauchy's theorem, residues, conformal maps, Riemann surfaces | 06, 02, 07 |
| [Functional Analysis](03-functional-analysis/README.md) | Banach and Hilbert spaces, the big four theorems, spectral theory, Fredholm operators | Measure and integration, 04, 06 |
| [Harmonic Analysis](04-harmonic-analysis/README.md) | Fourier series and transforms, distributions, groups | All three siblings, 05 |

```
   06 real analysis ──► measure and integration
                               │
                               ▼  (Lᵖ, L²)
                      Banach and Hilbert spaces ──► spectral theory
                               │
                               ▼
06 + 07 ──► complex analysis ─► harmonic analysis ◄── 05 groups
           (stands alone)      (uses all three)
```

The order of the arrows is the order of dependence. Measure theory comes first, because the Lᵖ spaces it produces are the first examples of Banach spaces and L² is the model Hilbert space. Functional analysis then abstracts the structure of those spaces and, through spectral theory and Fredholm theory, generalises diagonalisation and the rank–nullity count. Complex analysis needs neither: it grows directly from 06 and 07 and could be read first. Harmonic analysis draws on all three: Lebesgue integrals for its coefficients, Hilbert-space geometry for L² convergence, uniform boundedness for divergence, and complex analysis for transforms and Laurent series. Two links cross the diagram: Liouville's theorem from complex analysis proves that every operator has a non-empty spectrum, and Hilbert-space methods prove that Riemann surfaces carry meromorphic functions.

## Connections to neighbouring layers

- **[01 Sets and Foundations](../01-sets-and-foundations/README.md):** the axiom of choice produces non-measurable sets and powers Hahn–Banach; cardinality compares Borel and Lebesgue-measurable sets.
- **[04 Linear Algebra](../04-linear-algebra/README.md):** inner products, dual spaces and the finite-dimensional spectral theorem are the models that functional analysis extends.
- **[05 Abstract Algebra](../05-abstract-algebra/README.md):** groups and their representations underlie Fourier analysis on groups and the symmetries of the disc.
- **[06 Real Analysis](../06-real-analysis/README.md):** limits, uniform convergence, the Riemann integral and metric completeness are the starting point of every child.
- **[07 Topology](../07-topology/README.md):** compactness drives existence proofs; homotopy and covering spaces explain Cauchy's theorem and Riemann surfaces.
- **[08 Geometry](../08-geometry/README.md):** the disc's automorphisms are hyperbolic isometries; convex separation in finite dimensions becomes Hahn–Banach; Hausdorff dimension measures fractal sets.
- **[10 Differential Equations and Dynamics](../10-differential-equations-and-dynamics/README.md):** Sobolev spaces, weak solutions, Sturm–Liouville expansions and ergodic theory are built from this layer.
- **[11 Probability and Statistics](../11-probability-and-statistics/README.md):** probability spaces are measure spaces, conditional expectation is a Radon–Nikodym derivative, and the central limit theorem is proved with Fourier transforms.
- **[12 Number Theory and Algebraic Geometry](../12-number-theory-and-algebraic-geometry/README.md):** the zeta function, modular forms and algebraic curves are complex-analytic objects, and characters prove Dirichlet's theorem.
- **[14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md):** quantum mechanics is spectral theory of unbounded operators; the Fast Fourier Transform, sampling and numerical stability rest on this layer.

## Connections across layers

The layer is the great consumer of the foundations and the great supplier of the applications. It takes the real numbers of [02](../02-number-systems/README.md) and the limits of 06 and turns them into infinite-dimensional geometry, and in return it supplies the language of 10, 11, 12 and 14. Its results also feed [metamathematics](../13-structure-and-metamathematics/README.md): which sets are measurable without choice is a question settled by forcing, and how much choice Hahn–Banach needs is a question in reverse mathematics. The [history of mathematics](../15-mathematics-in-context/history-of-mathematics.md) in 15 shows how the convergence of Fourier series drove the creation of set theory and the rigorous theory of functions.

## Cross-cutting threads

- [Completeness and compactness](../CROSS-CUTTING.md#completeness-and-compactness): completeness of Lᵖ and Banach spaces makes limits exist; compactness, or its weak substitutes, makes extremal problems solvable.
- [Approximation and limits](../CROSS-CUTTING.md#approximation-and-limits): when a limit passes through an integral, and in which sense a Fourier series converges.
- [Decomposition and classification](../CROSS-CUTTING.md#decomposition-and-classification): Laurent series, spectral decompositions and Fourier expansions split objects into simple parts.
- [Duality](../CROSS-CUTTING.md#duality): dual spaces, Riesz representation and Pontryagin duality.
- [Local to global](../CROSS-CUTTING.md#local-to-global): analytic continuation and the identity theorem determine a function from a germ.
- [Infinity and size](../CROSS-CUTTING.md#infinity-and-size): measure, Baire category and Hausdorff dimension are three notions of how large a set is.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): non-measurable sets, divergent Fourier series and the impossibility of multiplying distributions.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): Carathéodory, Hahn–Banach, Baire and the Riemann mapping theorem prove existence without formulas.
