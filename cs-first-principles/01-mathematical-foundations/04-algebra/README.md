# Algebra

> **Layer:** [01 Mathematical Foundations](../README.md) › Algebra
> **Children:** [Boolean Algebra](boolean-algebra.md) · [Abstract Algebra](abstract-algebra.md) · [Linear Algebra](linear-algebra.md)

## What this area is about

Algebra is the study of operations and the laws they obey. Instead of asking what a particular number equals, it asks what follows from rules such as "this operation is associative" or "every element has an inverse". That shift is exactly the one programmers make when they code against an interface instead of a concrete type: any structure satisfying the laws inherits every theorem proved from them. The unifying idea of this area is that *laws, not objects, determine what you can compute*. Associativity permits parallel reduction, inverses permit undoing, a field permits solving equations, linearity permits representing a map by a finite matrix.

The three children are three algebras that computer science leans on hardest. Boolean algebra is the algebra of two values and of hardware. Abstract algebra (groups, rings, fields) is the algebra of cryptography and error correction. Linear algebra is the algebra of vectors and matrices, and therefore of graphics, scientific computing and machine learning.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Boolean Algebra](boolean-algebra.md) | Laws of AND, OR, NOT; canonical forms; the design language of circuits | Propositional logic, sets |
| [Abstract Algebra](abstract-algebra.md) | Groups, rings, finite fields; one-way functions and codes | Number theory, functions |
| [Linear Algebra](linear-algebra.md) | Vector spaces, matrices, eigenvalues, the SVD (Singular Value Decomposition) | Fields from abstract algebra |

Boolean algebra can be read first and alone: it needs only propositional logic. Abstract algebra provides the general vocabulary, and both other children are special cases of it in different directions. A Boolean algebra with exclusive OR (XOR) as addition is a ring, and {0, 1} under XOR and AND is the finite field GF(2). A vector space is defined over a field, so linear algebra over the reals serves geometry and learning while linear algebra over GF(2) serves parity checks and linear codes.

```
            abstract algebra (groups, rings, fields)
              /                         \
   Boolean algebra  ── GF(2) ──►  linear algebra
   (2-valued, bits)               (vectors over a field)
        │                                 │
   circuits, bitsets            graphics, ML, codes, quantum
```

## Connections to sibling areas

- **[Logic](../01-logic/README.md):** Boolean algebra is propositional logic in equational form; algebraic axioms are first-order sentences.
- **[Sets, Relations and Functions](../02-sets-relations-functions/README.md):** Algebraic structures are sets with operations (functions); a lattice is an order with join and meet.
- **[Discrete Mathematics](../03-discrete-mathematics/README.md):** [Number theory](../03-discrete-mathematics/number-theory.md) provides the first examples of groups and fields (residues mod *n* and mod *p*).
- **[Continuous Mathematics](../05-continuous-mathematics/README.md):** Derivatives in many dimensions are matrices (Jacobians, Hessians); optimisation is linear algebra plus calculus.
- **[Probability and Statistics](../06-probability-and-statistics/README.md):** Covariance matrices, Markov chains and Principal Component Analysis (PCA) are linear algebra applied to random data.

## Connections across layers

Boolean algebra is realised in [combinational logic](../../03-digital-logic/02-combinational-logic/README.md). Abstract algebra is the mathematics of [cryptography](../../11-security-and-cryptography/02-cryptography/README.md) and of [error correction](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md). Linear algebra is what [SIMD units and GPUs (Single Instruction, Multiple Data; Graphics Processing Units)](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md) are built to compute, and it is the substrate of [deep learning](../../13-artificial-intelligence/03-deep-learning/README.md), [computer graphics](../../14-human-and-visual-computing/02-computer-graphics/README.md) and [quantum computation](../../02-theory-of-computation/05-quantum-computation/README.md).

## Cross-cutting threads

- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): an algebraic structure is an interface given by laws.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): associativity allows tree-shaped parallel reductions.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): codes over finite fields add redundant symbols that correct errors.
- [Composition](../../CROSS-CUTTING.md#composition): composing linear maps is multiplying matrices.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): bytes as polynomials over GF(2); transforms as matrices.
