# 13 Structure and Metamathematics

> **Layer:** 13 Structure and Metamathematics
> **Children:** [Category Theory](01-category-theory/README.md) · [Computability and Incompleteness](02-computability-and-incompleteness/README.md) · [Model Theory and Independence](03-model-theory-and-independence/README.md)

## What this area is about

The earlier layers built mathematics: numbers, algebra, spaces, analysis. This layer steps back and makes mathematics itself the object of study, in two ways. The first looks at the *structures* mathematicians use. Groups, rings, modules, vector spaces and topological spaces each come with structure-preserving maps, and category theory studies that pattern in general, so that products, quotients, free objects and homology are each defined once and recognised everywhere. The second looks at *theories and proofs*. Logic, as developed in layer 00, becomes a branch of mathematics with its own theorems about what proofs, algorithms and axioms can and cannot do.

The answers are among the most surprising in the subject. There are precisely stated problems that no algorithm can solve, including whether a polynomial equation has integer solutions. Any consistent theory strong enough for arithmetic leaves some true statements unproved and cannot prove its own consistency. No first-order axioms fix the natural numbers or the real numbers up to isomorphism, and the standard axioms for sets do not decide how many real numbers there are. Yet the same methods also show that the theory of the real field is decidable, and they measure exactly how strong a theory must be to prove a given theorem.

The basic abstraction is **the theory as a mathematical object**: a structure is known by its maps, a proof by its code number, and a theory by its models.

## Why this layer sits here

This layer cannot come earlier because its subject is the rest of mathematics. Category theory needs examples before it can generalise them: the homomorphisms and modules of [05 Abstract Algebra](../05-abstract-algebra/README.md), the tensor products of [04 Linear Algebra](../04-linear-algebra/README.md), and the fundamental group and homology of [07 Topology](../07-topology/README.md). Without them a functor is a definition with no content. Metamathematics needs the logic of [00 Logic and Proof](../00-logic-and-proof/README.md), whose completeness and compactness theorems it uses rather than repeats, the sets, ordinals, cardinals and axiom of choice of [01 Sets and Foundations](../01-sets-and-foundations/README.md), and the Peano arithmetic of [02 Number Systems](../02-number-systems/README.md), which is the theory Gödel's theorems are first about.

Placing the layer after algebraic geometry in layer 12 also reflects history: schemes, sheaf cohomology and derived functors were the setting in which category theory became indispensable. Above it, layer 14 uses decision procedures and the theory of computation, and layer 15 discusses what incompleteness and independence mean for the foundations and practice of mathematics. Sideways, the computer science tree studies computability and type theory from the machine side.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Category Theory](01-category-theory/README.md) | The language of structure: functors, Yoneda, adjunctions, homological algebra, higher categories | 01 functions, 04 tensors, 05 algebra, 07 homology |
| [Computability and Incompleteness](02-computability-and-incompleteness/README.md) | The limits of algorithms and proofs: undecidability, Gödel's theorems, proof-theoretic strength | 00 proof systems, 01 diagonal argument and ordinals, 02 Peano axioms |
| [Model Theory and Independence](03-model-theory-and-independence/README.md) | Theories through their models: Löwenheim–Skolem, decidable theories, forcing, large cardinals | 00 compactness, 01 ZFC and cardinals, computability |

The three areas are less a sequence than three views of one question: what does a mathematical description determine? Category theory answers at the level of structure: an object is determined up to unique isomorphism by its maps. Computability answers at the level of proof: a formal theory is a program that lists theorems, and diagonalisation shows that no such program captures all arithmetic truth. Model theory answers at the level of meaning: a theory is determined by its models, and building a model where a statement fails is how independence is proved.

```
   00 logic        01 sets, ordinals     05 algebra, 07 topology
      │                 │                         │
      ▼                 ▼                         ▼
 computability ──► model theory           category theory
 and incompleteness  and independence     structure and maps
 limits of proof     models, forcing,             │
 and algorithm       large cardinals              │
      │                 │                         │
      └──── Curry–Howard; Lawvere's fixed-point theorem; toposes ────┘
                        │
                        ▼
      14 algorithms, 15 foundations and computer proof, CS theory
```

The arrows inside the layer are real dependencies. Gödel's second theorem explains why independence results in set theory take the form of relative consistency proofs, and the ordinals that measure the strength of arithmetic continue upward as large cardinals. The links to category theory are correspondences rather than prerequisites: under Curry–Howard, proofs are programs and arrows of a cartesian closed category; Lawvere's fixed-point theorem gives Cantor, Turing and Gödel one diagonal argument; and topos theory recasts forcing geometrically.

## Connections to neighbouring layers

- **[00 Logic and Proof](../00-logic-and-proof/README.md):** completeness and compactness are the engine of model theory; formal proof systems become objects whose consistency can be studied.
- **[01 Sets and Foundations](../01-sets-and-foundations/README.md):** Cantor's diagonal argument becomes the halting problem; ordinals measure the strength of theories; the continuum hypothesis is shown independent of ZFC (Zermelo–Fraenkel set theory with choice).
- **[02 Number Systems](../02-number-systems/README.md):** Peano arithmetic is the theory Gödel's theorems concern; Hilbert's tenth problem on Diophantine equations is undecidable.
- **[05 Abstract Algebra](../05-abstract-algebra/README.md):** homomorphisms and modules are the first examples of categories and functors; the word problem for finitely presented groups is undecidable.
- **[07 Topology](../07-topology/README.md):** the fundamental group is the first functor, homology the source of homological algebra, and homotopy the model for higher categories.
- **[12 Number Theory and Algebraic Geometry](../12-number-theory-and-algebraic-geometry/README.md):** schemes are written in the language of categories, and quantifier elimination proves the Nullstellensatz.
- **[14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md):** Fourier–Motzkin elimination in linear programming is quantifier elimination; decidability sets the outer limit of what algorithms can do.
- **[15 Mathematics in Context](../15-mathematics-in-context/README.md):** the philosophy of mathematics, computer-checked proof and the open problems of foundations all draw on this layer.

## Connections across layers

The theory of computation in the computer science tree is this layer seen from the machine side. Its [computability](../../cs-first-principles/02-theory-of-computation/03-computability/README.md) area treats [Turing machines](../../cs-first-principles/02-theory-of-computation/03-computability/turing-machines.md), the [Church–Turing thesis](../../cs-first-principles/02-theory-of-computation/03-computability/church-turing-thesis.md), the [λ-calculus](../../cs-first-principles/02-theory-of-computation/03-computability/lambda-calculus.md) and the [halting problem](../../cs-first-principles/02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), and its [complexity](../../cs-first-principles/02-theory-of-computation/04-complexity/README.md) area asks which decidable problems are feasible. Category theory reaches programming through [functional languages](../../cs-first-principles/06-programming-languages/01-paradigms/functional.md) and [type systems](../../cs-first-principles/06-programming-languages/02-semantics-and-types/type-systems.md), and the dependent type theories of the last category theory leaf are what [proof assistants](../../cs-first-principles/06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) implement.

## Cross-cutting threads

- [Structure and morphism](../CROSS-CUTTING.md#structure-and-morphism): category theory makes maps, not elements, the primary data.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): one definition of limit, adjoint or derived functor serves every field.
- [Duality](../CROSS-CUTTING.md#duality): reversing arrows exchanges products and coproducts, Tor and Ext.
- [Equivalence and quotients](../CROSS-CUTTING.md#equivalence-and-quotients): equivalence of categories, elementary equivalence of models and univalence each refine "the same".
- [Invariants](../CROSS-CUTTING.md#invariants): functors carry isomorphic objects to isomorphic objects; proof-theoretic ordinals are invariants of theories.
- [Dictionaries between fields](../CROSS-CUTTING.md#dictionaries-between-fields): Gödel coding, Curry–Howard and functors translate one subject into another.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): the halting problem, incompleteness and the independence of the continuum hypothesis.
- [Induction and recursion](../CROSS-CUTTING.md#induction-and-recursion): recursive functions and transfinite induction up to ε₀.
- [Infinity and size](../CROSS-CUTTING.md#infinity-and-size): Löwenheim–Skolem, the continuum and large cardinals.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): non-computable existence proofs and models built to order.
- [Completeness and compactness](../CROSS-CUTTING.md#completeness-and-compactness): Gödel's completeness theorem against his incompleteness theorems.
