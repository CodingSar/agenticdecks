# Data Models

> **Layer:** [09 Data Management](../README.md) › Data Models
> **Children:** [The Relational Model](the-relational-model.md) · [Relational Algebra and SQL](relational-algebra-and-sql.md) · [Normalization](normalization.md) · [Non-Relational Models](non-relational-models.md)

## What this area is about

A data model is the vocabulary a database offers for describing and querying data: what shapes data can take, what constraints it must obey, and what operations exist. It is the logical interface between applications and storage. Choose it well and applications can ask rich questions without knowing how bytes are laid out; choose it badly and every application reimplements navigation, consistency checks and query logic by hand.

The unifying idea is that a good model is *declarative and mathematical*. The relational model, proposed by Codd in 1970, represents all data as relations (sets of tuples) and all queries as operations on relations. Because those operations obey algebraic laws, the system can rewrite and optimise queries; because constraints are stated logically, the system can enforce them. Every non-relational model is best understood by what it gives up from this design, and what it gains in exchange.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The Relational Model](the-relational-model.md) | Defines relations, keys, constraints and data independence | Sets, predicate logic |
| [Relational Algebra and SQL](relational-algebra-and-sql.md) | The query languages: a closed algebra of operators and its practical, declarative surface | Relational model |
| [Normalization](normalization.md) | Schema design theory: how to split relations to avoid redundancy and update anomalies | Relational model, functional dependencies |
| [Non-Relational Models](non-relational-models.md) | Document, key-value, wide-column and graph models: what they trade away and why | All of the above |

Read the relational model first. Relational algebra and Structured Query Language (SQL) show how querying works on it. Normalization shows how to design schemas within it. Non-relational models are a contrast: they relax schema, joins or transactions to fit particular access patterns or scale-out needs, and recent history has seen many of them add those features back.

## Connections to sibling areas

- **[Storage and Indexing](../02-storage-and-indexing/README.md):** the logical model says nothing about layout; storage chooses rows or columns, heaps or trees. Physical data independence is what lets the two evolve separately.
- **[Query Processing](../03-query-processing/README.md):** the algebra defined here is the optimizer's working language: query plans are trees of relational operators, and equivalence rules come from algebraic identities.
- **[Transactions](../04-transactions/README.md):** integrity constraints defined in the model are the invariants that transactions must preserve; the "C" in Atomicity, Consistency, Isolation, Durability (ACID) refers to them.

## Connections across layers

The relational model is applied [set theory](../../01-mathematical-foundations/02-sets-relations-functions/sets.md) and [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); SQL is a [declarative language](../../06-programming-languages/01-paradigms/logic-and-declarative.md), closely related to Datalog and logic programming. Above, data models shape [distributed data](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) (how data can be partitioned) and [software architecture](../../12-software-engineering/01-design/software-architecture.md) (schema as a shared contract), and feed feature tables to [machine learning](../../13-artificial-intelligence/02-machine-learning-foundations/supervised-learning.md).

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): logical schema hides physical layout.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): declarative queries leave the "how" to the system.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): keys and constraints are enforced invariants.
- [Composition](../../CROSS-CUTTING.md#composition): relational operators are closed, so queries compose freely.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): the model chosen decides which queries are cheap to express.
