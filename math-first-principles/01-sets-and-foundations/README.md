# 01 Sets and Foundations

> **Layer:** 01 Sets and Foundations
> **Children:** [Sets, Relations and Functions](01-sets-relations-and-functions/README.md) · [Infinity and Cardinality](02-infinity-and-cardinality/README.md) · [Axiomatic Set Theory](03-axiomatic-set-theory/README.md)

## What this area is about

This layer supplies the language in which the rest of mathematics is written and the theory of infinite size. Its first area turns membership into sets, relations, functions and quotients: enough vocabulary to say what a group, a space or a probability is. Its second area asks how large infinite sets are, and finds that ℕ, ℤ and ℚ have the same size while ℝ is strictly larger, with no largest size at all. Its third area writes down the axioms that make this use of sets safe, after the paradoxes of around 1900 showed that naive set formation is contradictory, and shows what those axioms cannot decide.

The basic abstraction is **the set, with the function as the way to compare sets**. Almost every object later in this knowledge base is a set with extra structure, and almost every comparison between objects is a function that respects that structure.

## Why this layer sits here

This layer and [00 Logic and Proof](../00-logic-and-proof/README.md) are the twin roots of the knowledge base. Logic supplies the connectives, quantifiers and methods of proof; set theory supplies the objects they talk about. Neither is strictly prior. Zermelo–Fraenkel set theory (ZF) is written in [first-order logic](../00-logic-and-proof/01-formal-logic/predicate-logic-and-quantifiers.md), while the semantics of logic, what a model is in [soundness and completeness](../00-logic-and-proof/01-formal-logic/soundness-completeness-and-compactness.md), uses the sets, relations and functions defined here. The layer resolves this by building its first three leaves on the propositional and predicate logic of 00 and its methods of proof, and nothing else.

Everything above depends on this layer. [02 Number Systems](../02-number-systems/README.md) takes ℕ to be the ordinal ω and builds ℤ and ℚ as quotients; every later layer uses functions, products and equivalence classes without comment. ZF with the axiom of choice, ZFC, is the formal background against which the independence results of layer 13 are stated.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Sets, Relations and Functions](01-sets-relations-and-functions/README.md) | the vocabulary: sets, relations, orders, functions, quotients | 00 logic and proof methods |
| [Infinity and Cardinality](02-infinity-and-cardinality/README.md) | size and length of infinite sets: ℵ₀, Cantor's diagonal argument, cardinals, ordinals | sets, relations and functions |
| [Axiomatic Set Theory](03-axiomatic-set-theory/README.md) | the paradoxes, ZF and ZFC, the axiom of choice, type theory | both of the above, 00 consistency |

```
   00 Logic and Proof
        │  connectives, quantifiers, methods of proof
        ▼
   sets, relations and functions ─────────────────────────┐
        │  bijections, well-orders, equivalence classes    │ informal use
        ▼                                                  ▼ justified by
   infinity and cardinality ───────────────────► axiomatic set theory
     ℵ₀ < 2^ℵ₀ < …, ordinals, transfinite         paradoxes → ZF → ZFC,
     induction                                    type theories
        │                                                  │
        └──────────────► 02 Number Systems ◄───────────────┘
```

The order is language first, infinity second, axioms last. That is also roughly the historical order: Cantor developed cardinals and ordinals from the 1870s to the 1890s using sets informally, the paradoxes surfaced around 1900, and Zermelo published his axioms in 1908. Teaching the axioms last lets each one be motivated by a use already seen and a paradox it blocks.

## Connections to neighbouring layers

- **[00 Logic and Proof](../00-logic-and-proof/README.md):** set operations are logical connectives, indexed unions are quantifiers, and ZF is a first-order theory; logic's model theory in turn uses sets.
- **[02 Number Systems](../02-number-systems/README.md):** ℕ, ℤ, ℚ and ℝ are constructed from sets, quotients and Dedekind cuts; counting shows most reals are transcendental.
- **[03 Combinatorics and Graph Theory](../03-combinatorics-and-graph-theory/README.md):** the finite theory of sets, functions and partitions, from the pigeonhole principle to posets.
- **[04 Linear Algebra](../04-linear-algebra/README.md) and [05 Abstract Algebra](../05-abstract-algebra/README.md):** structures on sets, compared by structure-preserving functions and divided by quotients; bases and maximal ideals in general need the axiom of choice.
- **[07 Topology](../07-topology/README.md) and [09 Advanced Analysis](../09-advanced-analysis/README.md):** preimages define continuity and measurability; Tychonoff's theorem and the existence of non-measurable sets rest on choice.
- **[13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md):** categories generalise sets and functions; computability and incompleteness reuse Cantor's diagonal argument; forcing and large cardinals continue axiomatic set theory.
- **[15 Mathematics in Context](../15-mathematics-in-context/README.md):** the foundational crisis, the philosophy of sets, and the type theories behind proof assistants.

## Connections across layers

The deepest results of the layer are limits. Cantor's theorem says there is no largest infinity. The continuum hypothesis (CH), that nothing lies in size between ℕ and ℝ, is independent of ZFC: Gödel showed it consistent (1938; monograph 1940) and Cohen showed its negation consistent (1963), as developed in [forcing and independence](../13-structure-and-metamathematics/03-model-theory-and-independence/forcing-and-independence.md).

## Cross-cutting threads

- [Equivalence and quotients](../CROSS-CUTTING.md#equivalence-and-quotients): the general quotient construction lives in this layer.
- [Infinity and size](../CROSS-CUTTING.md#infinity-and-size): bijection decides size, and sizes form an unending ladder.
- [Structure and morphism](../CROSS-CUTTING.md#structure-and-morphism): sets are compared by functions, and category theory starts from that habit.
- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): the diagonal argument, the paradoxes and independence.
- [Induction and recursion](../CROSS-CUTTING.md#induction-and-recursion): well-orders and transfinite induction.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): the axiom of choice and its non-constructive consequences.
