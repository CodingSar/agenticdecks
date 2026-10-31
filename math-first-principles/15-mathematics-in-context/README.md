# 15 Mathematics in Context

> **Layer:** 15 Mathematics in Context
> **Children:** [History of mathematics](history-of-mathematics.md) · [Philosophy of mathematics](philosophy-of-mathematics.md) · [Mathematical practice and discovery](mathematical-practice-and-discovery.md) · [Computers and proof](computers-and-proof.md) · [Open problems](open-problems.md) · [Learning and teaching mathematics](learning-and-teaching-mathematics.md) · [Mathematics and society](mathematics-and-society.md)

## What this area is about

Every layer below states definitions, theorems and proofs. This layer asks about the activity that produces them: where the ideas came from, what kind of truth they have, how mathematicians actually find and check them, what machines now contribute, what is still unknown, how the subject is learned, and what it does in the world. These are questions about mathematics rather than within it, but they are not vague. Each has sharp examples: the 1931 incompleteness theorems settled a philosophical programme; the four colour theorem (1976) forced a decision about whether a computer-assisted proof counts; a flawed statistical argument helped convict an innocent mother.

The unifying idea is that **mathematics is a human practice that produces unusually reliable knowledge**, and the reliability has a mechanism. Proofs can be checked step by step, by people and increasingly by computers; definitions are revised when counterexamples appear; problems that resist attack are named and kept in view until they fall. Understanding that mechanism, including where it fails, is the point of the layer.

## Why this layer sits here

The layer needs material from almost everything below. History and philosophy need the [axiomatic method and proof](../00-logic-and-proof/README.md), the [set-theoretic foundations](../01-sets-and-foundations/README.md) and their paradoxes, and the [incompleteness and independence results](../13-structure-and-metamathematics/README.md) that changed what foundations could promise. Open problems are stated in the languages of [number theory](../12-number-theory-and-algebraic-geometry/README.md), [topology](../07-topology/README.md) and analysis. Computers and proof rest on formal logic and on [computation and optimisation](../14-applied-and-computational-mathematics/README.md); mathematics and society rests on [probability and statistics](../11-probability-and-statistics/README.md) and the applied layer. Nothing depends on this layer in turn: it is the top of the stack.

Its contribution is a view of the whole: the **reflective layer**, which explains why the stack has the shape it has and how anyone can trust what it contains.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [History of mathematics](history-of-mathematics.md) | How the subject grew, from Babylonian tablets to computer proofs, and why rigour and foundations arrived when they did | All lower layers |
| [Philosophy of mathematics](philosophy-of-mathematics.md) | What mathematical objects are and why mathematics applies to the world: Platonism, logicism, formalism, intuitionism, structuralism | History, logic and foundations (00, 01, 13) |
| [Mathematical practice and discovery](mathematical-practice-and-discovery.md) | How results are actually found and checked: examples, conjectures, heuristics, errors, refereeing, collaboration | History, philosophy, methods of proof |
| [Computers and proof](computers-and-proof.md) | Computer-assisted proofs, proof assistants and machine learning in research | Practice, formal logic, type theory |
| [Open problems](open-problems.md) | The Millennium problems and other famous conjectures, with their status as of 2026 | Practice, computers and proof, layers 07 and 12 |
| [Learning and teaching mathematics](learning-and-teaching-mathematics.md) | What research says about how mathematical understanding forms and how to teach for it | Practice, philosophy |
| [Mathematics and society](mathematics-and-society.md) | Mathematics in technology, law, finance, politics and public policy, and the community that makes it | Applied layers 11 and 14, practice |

Read history first: it explains why the nineteenth century demanded rigour, why paradoxes in set theory provoked a foundations crisis, and why the twentieth century prized abstraction. Philosophy then takes the positions that crisis produced, logicism, formalism and intuitionism, and asks what survived Gödel's theorems. Practice turns from ideals to what mathematicians do: guess from examples, prove, find errors, repair. Computers and proof follows the newest change to practice, from the four colour theorem to formal verification in Lean and other proof assistants. Open problems show practice at its frontier, and why some questions have resisted for centuries. Learning and teaching ask how a newcomer acquires all this, and mathematics and society asks what the finished product does outside the subject, for good and ill.

## Connections to neighbouring layers

- **[00 Logic and Proof](../00-logic-and-proof/README.md):** the standard of proof the whole layer examines; formal proof systems are what proof assistants implement.
- **[01 Sets and Foundations](../01-sets-and-foundations/README.md):** the paradoxes and the axiomatic set theory that resolved them are the core episode of history and philosophy.
- **[13 Structure and Metamathematics](../13-structure-and-metamathematics/README.md):** incompleteness, independence and undecidability bound what any foundation or machine can achieve.
- **[14 Applied and Computational Mathematics](../14-applied-and-computational-mathematics/README.md):** the route by which mathematics reaches society, and the source of the machine learning now entering research.
- **[12 Number Theory and Algebraic Geometry](../12-number-theory-and-algebraic-geometry/README.md):** home of the Riemann hypothesis, the Birch and Swinnerton-Dyer conjecture, abc and Fermat's last theorem.
- **[11 Probability and Statistics](../11-probability-and-statistics/README.md):** statistical reasoning, and its misuse, is where mathematics most often meets law and policy.
- **[03 Combinatorics and Graph Theory](../03-combinatorics-and-graph-theory/README.md):** the source of the first computer-assisted proofs and of the large SAT-solver proofs.

## Connections across layers

The layer takes from every other layer and gives back no theorems, but it gives context: the [history](history-of-mathematics.md) of each idea, the [open problems](open-problems.md) that each area is aiming at, and the standard of [formal verification](computers-and-proof.md) that any proof below could in principle meet. Its counterparts in the sibling trees are the computing tree's [computing in context](../../cs-first-principles/15-computing-in-context/README.md) layer and the medicine tree's [history of medicine](../../medicine-first-principles/15-medicine-in-society/03-populations-and-the-future/history-of-medicine.md).

## Cross-cutting threads

- [Impossibility and obstruction](../CROSS-CUTTING.md#impossibility-and-obstruction): incompleteness ended Hilbert's programme, and proofs that problems are hard shape which open problems are attacked.
- [Existence and construction](../CROSS-CUTTING.md#existence-and-construction): the intuitionist critique of non-constructive proof, and the computer's demand for explicit constructions.
- [Abstraction and generalisation](../CROSS-CUTTING.md#abstraction-and-generalisation): the twentieth century's turn to structures, and why learners find it hard.
- [Dictionaries between fields](../CROSS-CUTTING.md#dictionaries-between-fields): Fermat's last theorem fell to a bridge between elliptic curves and modular forms; open problems often wait for such bridges.
- [Infinity and size](../CROSS-CUTTING.md#infinity-and-size): Cantor's infinities provoked the foundations crisis.
