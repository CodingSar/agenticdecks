# The Relational Model

> **Layer:** [09 Data Management](../README.md) › [Data Models](README.md)
> **Builds on:** [Sets](../../01-mathematical-foundations/02-sets-relations-functions/sets.md), [Relations and Orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), [Predicate Logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [File System Abstractions](../../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md)
> **Enables:** [Relational Algebra and SQL](relational-algebra-and-sql.md), [Normalization](normalization.md), [Query Optimization](../03-query-processing/query-optimization.md), [ACID](../04-transactions/acid.md)

## Essence

The relational model represents all data as *relations*: named sets of tuples, where each tuple assigns a value to each of a fixed set of named attributes. Relationships between entities are expressed by matching values (keys), not by pointers. Before Codd's 1970 paper, databases were navigational: programs followed physical links record by record, so any change in storage broke them. By describing data purely in terms of values and sets, the relational model lets users state *what* they want while the system decides *how* to find it, and lets the physical layout change without touching applications.

## Core tenets

1. **A relation is a set of tuples over a schema.** Formally, given attribute domains D1, ..., Dn, a relation is a subset of D1 × ... × Dn. As a table: columns are attributes, rows are tuples. Because it is a set, rows have no order and no duplicates, and columns are identified by name, not position. SQL tables relax this (they allow duplicates and expose order), which is a source of subtle bugs and optimisation limits.

2. **All information is represented as values.** Codd's "information principle": the only way data is represented is as values in attributes of tuples. There are no hidden pointers or record positions that carry meaning. An employee's department is a department identifier stored in the employee row, not a physical link. This makes every relationship visible to, and queryable by, the same operations.

3. **Keys identify tuples and connect relations.** A *candidate key* is a minimal set of attributes whose values are unique across all tuples; one is chosen as the *primary key*. A *foreign key* is a set of attributes whose values must match a key in another relation. Joins follow foreign keys by value matching, so relationships can be traversed in any direction, and new relationships can be queried that the designer never anticipated.

4. **Integrity constraints are declared, and the system enforces them.** Key uniqueness, foreign-key existence (referential integrity), NOT NULL and CHECK predicates are stated once in the schema. The Database Management System (DBMS) rejects any change that would violate them. Every application gets the same guarantees without reimplementing them, which matters when dozens of programs share one database.

5. **Data independence separates logical from physical.** *Physical data independence*: the storage layout (indexes, file organisation, compression, row or column format) can change without changing queries. *Logical data independence*: views can present an old schema shape after the base tables evolve. This is abstraction applied to data, and it is the main reason relational systems outlived their navigational predecessors.

6. **Queries are expressions over relations, so they can be optimised.** Because a query describes a result as a set defined by logic, not as a sequence of record accesses, the system is free to choose any execution strategy that yields the same set. Codd proved relational algebra and relational calculus equally expressive ("relational completeness"), giving both a procedural and a declarative view of the same queries.

7. **NULL is a pragmatic hole in the logic.** Real data has missing or inapplicable values. SQL represents them with NULL and uses three-valued logic: comparisons with NULL yield UNKNOWN, and WHERE keeps only TRUE rows. So `x = NULL` is never true, `NOT IN` with a NULL in the list returns nothing, and aggregates silently skip NULLs. These rules are consistent but often surprising.

8. **The model is closed under its operations.** Every relational operation takes relations and returns a relation. So the output of any query can be the input to another, views are just named queries, and complex queries are built by composition. This closure is what makes the algebra an algebra.

## Key concepts

| Term | Meaning |
|---|---|
| Relation | A set of tuples sharing a schema; a table |
| Tuple | One row: a mapping from attribute names to values |
| Attribute / domain | A named column and its set of permitted values |
| Schema | Relation name plus attribute names and domains |
| Candidate key / primary key | Minimal unique attribute set / the one chosen to identify rows |
| Foreign key | Attributes that must match a key in another relation |
| Referential integrity | Every foreign key value refers to an existing row |
| Data independence | Applications unaffected by physical (or logical) schema changes |
| View | A named query presented as a virtual relation |
| NULL | Marker for a missing or inapplicable value, with three-valued logic |

## How it fits

- **Below:** a relation is a [set](../../01-mathematical-foundations/02-sets-relations-functions/sets.md) and an n-ary [relation](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) in the mathematical sense; constraints and queries are [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md). It replaces the byte-stream view of [files](../../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md) with typed, constrained sets.
- **Above:** [relational algebra and SQL](relational-algebra-and-sql.md) query it; [query optimization](../03-query-processing/query-optimization.md) exploits its freedom of execution; [ACID](../04-transactions/acid.md) transactions preserve its constraints. [Partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) splits relations across machines by key.
- **Siblings:** [normalization](normalization.md) tells you how to choose relations; [non-relational models](non-relational-models.md) relax one or more of the tenets above.

## Common misconceptions

- **"Relational means tables with relationships between them."** "Relation" is the mathematical term for the table itself; relationships between tables are expressed by keys.
- **"SQL is the relational model."** SQL departs from it in several ways (duplicates, NULL logic, column order); it is a practical approximation.
- **"Relational databases cannot scale."** Single-node systems handle terabytes and very high transaction rates; distributed SQL systems partition and replicate relations across many nodes.

## Go deeper

- E. F. Codd, *A Relational Model of Data for Large Shared Data Banks* (Communications of the ACM, 1970): the founding paper.
- C. J. Date, *An Introduction to Database Systems* (8th ed., 2003): a careful treatment of the model and its principles.
- S. Abiteboul, R. Hull, V. Vianu, *Foundations of Databases* (1995): the formal theory, freely available online.
