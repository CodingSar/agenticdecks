# Functional Analysis

> **Layer:** [09 Advanced Analysis](../README.md) › Functional Analysis
> **Children:** [Banach Spaces](banach-spaces.md) · [Hilbert Spaces](hilbert-spaces.md) · [Hahn–Banach and Baire Category](hahn-banach-and-baire-category.md) · [Spectral Theory](spectral-theory.md)

## What this area is about

Functional analysis is linear algebra in infinite dimensions, made workable by analysis. Its objects are spaces of functions, such as the continuous functions on an interval or the square-integrable functions on a domain, treated as single points in a vector space with a norm. Its maps are operators such as differentiation, integration against a kernel, or the solution map of a differential equation. Its questions are the ones linear algebra asks: is this map invertible, what are its eigenvalues, can the space be decomposed into simple pieces?

Two things change in infinite dimensions. First, topology matters: a linear map can fail to be continuous, the unit ball is not compact, and the answers depend on which norm one uses. Completeness, the property that makes Banach and Hilbert spaces special, is what rescues limiting arguments. Second, a handful of general theorems do the work that dimension counting does in finite dimensions. The subject grew in the first decades of the twentieth century from the integral equations of Fredholm and Hilbert, and Banach's 1932 book gave it its modern form.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Banach Spaces](banach-spaces.md) | Complete normed spaces, bounded operators, duals | Metric completeness, Lᵖ, linear algebra |
| [Hilbert Spaces](hilbert-spaces.md) | Inner products: projection, Riesz representation, orthonormal bases | Banach spaces, inner products |
| [Hahn–Banach and Baire Category](hahn-banach-and-baire-category.md) | The four big theorems: extension, uniform boundedness, open mapping, closed graph | Banach spaces, choice, completeness |
| [Spectral Theory](spectral-theory.md) | When T − λ is invertible; diagonalising compact self-adjoint operators | All three siblings, Liouville |

```
                    Banach spaces
                   │             │
                   ▼             ▼
            Hilbert spaces    Hahn–Banach and Baire
                   │             │
                   └──────┬──────┘
                          ▼
                    spectral theory
```

The story begins with [Banach spaces](banach-spaces.md): complete normed spaces, where bounded and continuous coincide and the dual space is defined. Two branches grow from there. Adding an inner product gives [Hilbert spaces](hilbert-spaces.md), where Euclidean geometry survives: nearest points, orthogonal complements, and expansion in orthonormal bases. Staying general, [Hahn–Banach and Baire category](hahn-banach-and-baire-category.md) supply the tools: functionals exist in abundance, and pointwise information becomes uniform. [Spectral theory](spectral-theory.md) uses everything: the bounded inverse theorem to define the spectrum, Hahn–Banach and Liouville's theorem to show it is non-empty, and Hilbert-space geometry to prove the spectral theorem for compact self-adjoint operators.

## Connections to sibling areas

- **[Measure and Integration](../01-measure-and-integration/README.md):** the Lᵖ spaces are the founding examples of Banach spaces and L² of Hilbert spaces; the Radon–Nikodym theorem has a Hilbert-space proof.
- **[Complex Analysis](../02-complex-analysis/README.md):** the resolvent is a holomorphic operator-valued function, Liouville's theorem shows the spectrum is non-empty, and Cauchy's integral formula defines functions of operators.
- **[Harmonic Analysis](../04-harmonic-analysis/README.md):** Fourier series are orthonormal expansions in L², Plancherel's theorem makes the Fourier transform unitary, and distributions are elements of a dual space.

## Connections across layers

Downward, the area extends the [linear maps](../../04-linear-algebra/01-vector-spaces-and-linear-maps/linear-maps-and-matrices.md), [dual spaces](../../04-linear-algebra/01-vector-spaces-and-linear-maps/dual-spaces.md) and [spectral theorem](../../04-linear-algebra/03-inner-product-spaces/the-spectral-theorem.md) of 04, uses the [complete metric spaces](../../06-real-analysis/04-metric-spaces/completeness-and-the-contraction-mapping-principle.md) of 06 and the [axiom of choice](../../01-sets-and-foundations/03-axiomatic-set-theory/the-axiom-of-choice.md) of 01, and generalises the [convex separation](../../08-geometry/03-convex-and-discrete-geometry/convex-sets-and-separation.md) of 08. Upward, [Sobolev spaces and weak solutions](../../10-differential-equations-and-dynamics/02-partial-differential-equations/weak-solutions-and-sobolev-spaces.md) and [Sturm–Liouville theory](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/boundary-value-problems-and-sturm-liouville-theory.md) in 10 are functional analysis applied; [conditional expectation](../../11-probability-and-statistics/01-measure-theoretic-probability/conditional-expectation.md) in 11 is a projection; [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md), [convex duality](../../14-applied-and-computational-mathematics/02-optimisation/convex-optimisation-and-duality.md) and the stability of [numerical schemes](../../14-applied-and-computational-mathematics/01-numerical-analysis/numerical-methods-for-differential-equations.md) in 14 rest on it.

## Cross-cutting threads

- [Completeness and compactness](../../CROSS-CUTTING.md#completeness-and-compactness): completeness powers Baire and the Neumann series; the loss of compactness is repaired by weak topologies and compact operators.
- [Duality](../../CROSS-CUTTING.md#duality): every space has a dual, and the Riesz theorem identifies a Hilbert space with its own.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): nonlinear problems are attacked through the bounded linear operators that approximate them.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): the spectral theorem splits a space into eigenspaces; separable Hilbert spaces are all ℓ².
- [Existence and construction](../../CROSS-CUTTING.md#existence-and-construction): Hahn–Banach and Baire prove existence without producing an example.
- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): functions become points, and analysis becomes geometry.
