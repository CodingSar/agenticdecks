# Determinants and Eigenvalues

> **Layer:** [04 Linear Algebra](../README.md) › Determinants and Eigenvalues
> **Children:** [Determinants](determinants.md) · [Eigenvalues and diagonalisation](eigenvalues-and-diagonalisation.md) · [Jordan normal form](jordan-normal-form.md) · [Non-negative matrices and Perron–Frobenius](non-negative-matrices-and-perron-frobenius.md)

## What this area is about
Rank classifies linear maps between two different spaces, but a map from a space to itself must be studied with one basis used on both sides, and then the classification is much richer. This area develops the invariants that survive such a change of basis. The determinant, the unique alternating multilinear form normalised on the identity, measures how a map scales volume and detects invertibility. The characteristic polynomial det(λI − A) built from it has the eigenvalues as roots: the directions a map only stretches. When enough eigenvectors exist the map is diagonal; when they do not, the Jordan normal form gives the complete answer over ℂ. For matrices with non-negative entries, Perron–Frobenius theory picks out one dominant eigenvalue and a positive eigenvector, which describe the long-run behaviour of growth and probability models.

## How the children fit together
| Child | Its role in the whole | Depends on |
|---|---|---|
| [Determinants](determinants.md) | Volume scaling, invertibility, the product rule | Vector spaces and linear maps |
| [Eigenvalues and diagonalisation](eigenvalues-and-diagonalisation.md) | Characteristic polynomial, eigenvectors, when A = PDP⁻¹ | Determinants |
| [Jordan normal form](jordan-normal-form.md) | Complete similarity classification; minimal polynomial; Cayley–Hamilton | Eigenvalues |
| [Non-negative matrices and Perron–Frobenius](non-negative-matrices-and-perron-frobenius.md) | Dominant positive eigenvector of non-negative matrices | Eigenvalues |

```
              determinants
                   |
     eigenvalues and diagonalisation
            /                \
   Jordan normal form     Perron–Frobenius
```

Determinants come first because the characteristic polynomial is defined through them, and because invertibility of λI − A is exactly what an eigenvalue breaks. Eigenvalues and diagonalisation then ask when a map is as simple as possible, a list of independent stretchings, and find the obstruction: too few eigenvectors when eigenvalues repeat. From there the area branches. The Jordan normal form resolves the obstruction in general, giving a canonical form for every complex matrix and explaining the minimal polynomial and Cayley–Hamilton. Perron–Frobenius goes the other way: instead of all matrices it treats a special class, the non-negative ones, and proves that their dominant eigenvalue is real, simple and comes with a positive eigenvector. The two branches meet in one fact: for an irreducible non-negative matrix the Perron root has a Jordan block of size 1.

## Connections to sibling areas
- [Vector spaces and linear maps](../01-vector-spaces-and-linear-maps/README.md): similarity P⁻¹AP and rank–nullity, both defined there, are the tools that organise eigenspaces and Jordan chains.
- [Inner product spaces](../03-inner-product-spaces/README.md): the spectral theorem shows that symmetric and normal matrices are always diagonalisable by an orthonormal basis, and singular values repair what eigenvalues cannot say about non-square matrices.
- [Multilinear algebra](../04-multilinear-algebra/README.md): the determinant is the action of a map on the top exterior power, and the coefficients of the characteristic polynomial are traces on the other exterior powers.

## Connections across layers
- Below, the area uses [permutations and counting](../../03-combinatorics-and-graph-theory/01-enumeration/counting-principles-and-binomial-coefficients.md), [the complex numbers](../../02-number-systems/01-constructing-the-numbers/the-complex-numbers.md), [recurrences](../../03-combinatorics-and-graph-theory/01-enumeration/recurrence-relations.md) and [graph connectivity](../../03-combinatorics-and-graph-theory/02-graph-theory/graphs-and-connectivity.md).
- Above, the Jacobian determinant drives [change of variables](../../06-real-analysis/04-calculus-of-several-variables/multiple-integrals-and-change-of-variables.md); eigenvalues decide [stability](../../10-differential-equations-and-dynamics/01-ordinary-differential-equations/stability-and-phase-portraits.md) and define [spectral theory](../../09-advanced-analysis/03-functional-analysis/spectral-theory.md); the Jordan form is a case of [modules](../../05-abstract-algebra/04-modules-and-representations/modules.md) over a polynomial ring; Perron vectors are stationary distributions of [Markov chains](../../11-probability-and-statistics/03-stochastic-processes/markov-chains.md).
- In computing, eigenvectors rank web pages and power iterative algorithms ([Markov chains in computing](../../../cs-first-principles/01-mathematical-foundations/06-probability-and-statistics/markov-chains.md)).

## Cross-cutting threads
- [Invariants](../../CROSS-CUTTING.md#invariants): determinant, trace, characteristic polynomial and Jordan blocks are unchanged by similarity.
- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): eigenspaces and Jordan blocks split a map into simple pieces, and the Jordan form is a complete classification.
- [Extremal principles and optimisation](../../CROSS-CUTTING.md#extremal-principles-and-optimisation): the Collatz–Wielandt formula finds the Perron root as an extremal ratio.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): eigenvalues of a linearised system decide the stability of the nonlinear one.
