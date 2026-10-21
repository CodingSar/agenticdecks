# 01 Mathematical Foundations

> **Layer:** 01 Mathematical Foundations
> **Children:** [Logic](01-logic/README.md) · [Sets, Relations and Functions](02-sets-relations-functions/README.md) · [Discrete Mathematics](03-discrete-mathematics/README.md) · [Algebra](04-algebra/README.md) · [Continuous Mathematics](05-continuous-mathematics/README.md) · [Probability and Statistics](06-probability-and-statistics/README.md)

## What this area is about

This layer is the formal root of Computer Science (CS). It collects the mathematics in which every higher layer is stated and analysed: logic to say precisely what is true, sets and functions to build objects, discrete mathematics to count and to reason about structures and recursion, algebra to capture operations by their laws, continuous mathematics to approximate and optimise, and probability and statistics to reason under uncertainty. None of it is about computers as such. All of it is what a computer scientist reaches for when asking whether a design is correct, how fast it can be, or what it cannot do.

The unifying idea is that *precise definitions make claims checkable*. A circuit's behaviour, an algorithm's running time, a protocol's security and a model's accuracy can each be stated as a mathematical claim and then proved, bounded or tested. Every leaf in this layer is written with that use in view: each tenet says which part of CS depends on it.

## Why this layer sits here

CS has two roots. [00 Engineering Foundations](../00-engineering-foundations/README.md) is the physical root: charge, transistors, signals, the stuff machines are made of. This layer is the formal root: Turing's machine is a mathematical object, not a physical one, and the theorems here would be true if no computer had ever been built. So **01 does not depend on 00**. Nothing in logic or number theory needs a transistor.

It is numbered 01 rather than placed beside 00 only because a directory tree must list one root first. The numbering is a topological order, and both 00 and 01 have no dependencies below them, so either order would be valid. Placing the physical root first matches the bottom-up story of the stack; placing mathematics immediately after it reflects that mathematics is the *language* of everything from [02 Theory of Computation](../02-theory-of-computation/README.md) upward. The two roots first meet in [03 Digital Logic](../03-digital-logic/README.md), where Boolean algebra from this layer is built out of transistors from 00. (00 itself uses calculus and linear algebra to describe circuits and signals, but as engineering it takes that mathematics as given; the dependency of 00 on 01 is one of description, not of construction.)

The one interface this layer contributes is **a shared formal vocabulary with proof as its standard of truth**: sets, functions, relations, structures with laws, and probability spaces, together with the proof techniques that establish facts about them. Higher layers draw on different parts of it:

| Mathematics (this layer) | Main consumers higher in the stack |
|---|---|
| [Logic](01-logic/README.md), [Boolean algebra](04-algebra/boolean-algebra.md) | [Digital logic](../03-digital-logic/README.md) (gates compute Boolean functions), [formal methods and verification](../06-programming-languages/05-formal-methods/README.md), [computability](../02-theory-of-computation/03-computability/README.md), type systems, database query languages |
| [Sets, relations, functions](02-sets-relations-functions/README.md) | [Automata and formal languages](../02-theory-of-computation/02-automata-and-formal-languages/README.md), the [relational model](../09-data-management/01-data-models/the-relational-model.md), event ordering in [distributed systems](../10-distributed-and-parallel-computing/02-distributed-foundations/README.md) |
| [Discrete mathematics](03-discrete-mathematics/README.md) | [Algorithms and data structures](../05-algorithms-and-data-structures/README.md) (counting, graphs, recurrences), [complexity](../02-theory-of-computation/04-complexity/README.md), [routing](../08-networking/03-network-layer/routing-algorithms.md) |
| [Number theory](03-discrete-mathematics/number-theory.md), [abstract algebra](04-algebra/abstract-algebra.md) | [Cryptography](../11-security-and-cryptography/02-cryptography/README.md) (groups, finite fields, one-way functions), [error correction](../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) (codes over finite fields), machine integer arithmetic |
| [Linear algebra](04-algebra/linear-algebra.md), [calculus](05-continuous-mathematics/calculus.md), [optimization](05-continuous-mathematics/optimization.md) | [Machine learning](../13-artificial-intelligence/README.md) (training is gradient-based optimisation of matrix computations), [graphics](../14-human-and-visual-computing/02-computer-graphics/README.md) (transforms, light-transport integrals), [Graphics Processing Unit (GPU) design](../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) |
| [Probability and statistics](06-probability-and-statistics/README.md) | [Information theory](../02-theory-of-computation/01-information-theory/README.md), [randomized algorithms](../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md), [networking performance and queueing](../08-networking/01-principles/latency-bandwidth-and-queueing.md), [reliability](../12-software-engineering/04-operations/reliability-engineering.md), machine learning evaluation |

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Logic](01-logic/README.md) | The language of statements and proofs | Nothing |
| [Sets, Relations and Functions](02-sets-relations-functions/README.md) | The building blocks of all mathematical objects; sizes of infinite sets | Logic |
| [Discrete Mathematics](03-discrete-mathematics/README.md) | Counting, graphs, induction and recurrences, number theory | Logic, sets |
| [Algebra](04-algebra/README.md) | Boolean, abstract and linear algebra: operations defined by laws | Logic, sets, number theory |
| [Continuous Mathematics](05-continuous-mathematics/README.md) | Calculus and optimisation | Functions, linear algebra |
| [Probability and Statistics](06-probability-and-statistics/README.md) | Uncertainty, randomness and inference | Sets, combinatorics, calculus, optimisation |

The reading order is itself a dependency order:

```
                      logic
                        │
              sets, relations, functions
               ┌────────┼──────────────┐
               ▼        ▼              ▼
          discrete    algebra ◄── number theory
          mathematics   │  (Boolean, abstract, linear)
               │        ▼
               │   continuous mathematics (calculus, optimisation)
               │        │
               └──► probability and statistics ◄┘
```

Logic and sets come first because everything else is defined with them. Discrete mathematics and algebra then split the work: discrete mathematics counts and recurses, algebra abstracts operations. Linear algebra feeds calculus in many variables, and calculus feeds optimisation. Probability sits last because it uses all of them: counting for finite cases, integrals for continuous ones, linear algebra for Markov chains and covariance, and optimisation for estimation.

## Connections to neighbouring layers

- **[00 Engineering Foundations](../00-engineering-foundations/README.md):** The parallel root. Engineering *uses* calculus (circuit dynamics, signals), linear algebra (circuit analysis) and probability (noise, reliability) as tools, but neither root is built from the other.
- **[02 Theory of Computation](../02-theory-of-computation/README.md):** The direct heir. Automata are sets and functions; undecidability is diagonalisation; complexity is counting and asymptotics; information theory is probability; quantum computation is linear algebra over complex numbers.
- **[03 Digital Logic](../03-digital-logic/README.md):** Where the two roots meet. Boolean algebra and modular arithmetic become gates, adders and two's-complement integers.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md):** Runs on discrete mathematics: invariants and induction for correctness, recurrences and counting for cost, graph theory for structure, probability for randomized methods.
- **[06 Programming Languages](../06-programming-languages/README.md):** Semantics, types and formal methods are applied logic; lambda calculus is a theory of functions.
- **[08 Networking](../08-networking/README.md) and [10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md):** Queueing theory, graph theory for topology and routing, optimisation for congestion control, partial orders and lattices for ordering and replication.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md):** Number theory, finite fields and probability define what a secure scheme is and why it resists attack.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** Linear algebra, calculus, optimisation, probability and statistics are the whole mathematical substance of modern Machine Learning (ML).

## Connections across layers

This layer takes nothing from lower layers; it is a root. It gives every higher layer its notation and its standard of proof. The most heavily used edges upward are: logic to [digital logic](../03-digital-logic/02-combinational-logic/README.md) and [formal methods](../06-programming-languages/05-formal-methods/README.md); discrete mathematics to [algorithms](../05-algorithms-and-data-structures/README.md); number theory and abstract algebra to [cryptography](../11-security-and-cryptography/02-cryptography/README.md) and [coding](../02-theory-of-computation/01-information-theory/README.md); continuous mathematics, linear algebra and probability to [machine learning](../13-artificial-intelligence/02-machine-learning-foundations/README.md), [graphics](../14-human-and-visual-computing/02-computer-graphics/README.md) and [networking performance](../08-networking/01-principles/README.md).

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): mathematics is the most general abstraction, describing what holds of every implementation.
- [Interface vs implementation](../CROSS-CUTTING.md#interface-vs-implementation): algebraic structures are interfaces defined by laws.
- [Invariants and correctness](../CROSS-CUTTING.md#invariants-and-correctness): induction and proof are the mechanism of every correctness argument.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): diagonalisation, counting and incompleteness give the first hard limits in the stack.
- [Recursion and self-reference](../CROSS-CUTTING.md#recursion-and-self-reference): recursive definitions, inductive proofs, and the self-reference behind paradoxes.
- [Encoding and representation](../CROSS-CUTTING.md#encoding-and-representation): bijections, residues and bases decide what is cheap to compute.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): optimisation makes trade-offs explicit as objectives and constraints.
