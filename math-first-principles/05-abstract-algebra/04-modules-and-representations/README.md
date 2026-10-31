# Modules and Representations

> **Layer:** [05 Abstract Algebra](../README.md) › Modules and Representations
> **Children:** [Modules](modules.md) · [Representations of Finite Groups](representations-of-finite-groups.md)

## What this area is about

Linear algebra is the best-understood part of mathematics, and this area extends its reach in two directions. Modules keep the vector space axioms but let the scalars come from a ring. That one change covers abelian groups, ideals and vector spaces equipped with a linear map, and over a principal ideal domain a single structure theorem classifies them all. Representations go the other way: they take an abstract group and make it act by matrices, so that questions about symmetry become questions about traces, eigenvalues and invariant subspaces.

The two halves meet in one observation: a representation of a group G is a module over its group algebra. Both halves are classification stories, decomposing an object into indecomposable pieces and recording a small invariant that determines it: the invariant factors of a module, and the character of a representation.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Modules](modules.md) | Vector spaces over rings; the structure theorem over a principal ideal domain, giving abelian groups and Jordan form | Rings and ideals, factorisation |
| [Representations of Finite Groups](representations-of-finite-groups.md) | Groups acting linearly; Maschke, Schur and character orthogonality | Modules, group actions |

Modules come first because they supply the language: subrepresentations are submodules, G-maps are module homomorphisms, and direct sums are the same in both. The structure theorem for modules over a principal ideal domain decomposes a module into cyclic pieces using the Euclidean algorithm; Maschke's theorem decomposes a representation into irreducible pieces using averaging over the group. The first works because the ring has division with remainder, the second because the order of the group can be divided by. Where these hypotheses fail, modules over general rings and modular representations, the theories become hard, and homological algebra takes over.

```
rings and ideals ──> modules ──> representations of finite groups
                        ^                 ^
       Jordan form ─────┘                 └───── group actions
```

## Connections to sibling areas

- [Groups](../01-groups/README.md): representations are linear group actions, and the classification of finitely generated abelian groups comes from the structure theorem; character theory gave Burnside's theorem that groups of order pᵃqᵇ are solvable.
- [Rings and Fields](../02-rings-and-fields/README.md): the structure theorem needs a principal ideal domain such as ℤ or F[t]; the group algebra is a non-commutative ring.
- [Galois Theory](../03-galois-theory/README.md): Galois groups acting on vector spaces, such as the points of an elliptic curve, are the representations that modern number theory studies.

## Connections across layers

- Below: [the Jordan normal form](../../04-linear-algebra/02-determinants-and-eigenvalues/jordan-normal-form.md) is a corollary of the structure theorem; [inner products](../../04-linear-algebra/03-inner-product-spaces/inner-products-and-orthogonality.md) make representations unitary.
- Above: [homology](../../07-topology/02-algebraic-topology/homology.md) groups are classified by the structure theorem; [homological algebra](../../13-structure-and-metamathematics/01-category-theory/homological-algebra.md) studies modules through resolutions; [representations of Lie groups](../../08-geometry/04-lie-theory/representations-of-lie-groups.md) and [Fourier analysis on groups](../../09-advanced-analysis/04-harmonic-analysis/fourier-analysis-on-groups.md) extend character theory; [quantum mechanics](../../14-applied-and-computational-mathematics/04-mathematical-modelling/the-mathematics-of-quantum-mechanics.md) uses representations to classify states.

## Cross-cutting threads

- [Decomposition and classification](../../CROSS-CUTTING.md#decomposition-and-classification): cyclic summands and irreducible representations.
- [Linearisation](../../CROSS-CUTTING.md#linearisation): representations replace groups by matrices.
- [Invariants](../../CROSS-CUTTING.md#invariants): invariant factors and characters determine the object up to isomorphism.
- [Abstraction and generalisation](../../CROSS-CUTTING.md#abstraction-and-generalisation): one definition covers abelian groups, matrices and group actions.
