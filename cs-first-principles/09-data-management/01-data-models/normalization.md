# Normalization

> **Layer:** [09 Data Management](../README.md) › [Data Models](README.md)
> **Builds on:** [The Relational Model](the-relational-model.md), [Functions and Cardinality](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md), [Proof Techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md)
> **Enables:** [Join Algorithms](../03-query-processing/join-algorithms.md), [Non-Relational Models](non-relational-models.md), [Modularity and Information Hiding](../../12-software-engineering/01-design/modularity-and-information-hiding.md)

## Essence

Normalization is the theory of designing relational schemas so that each fact is stored exactly once. When the same fact appears in many rows, updates must change all copies, inserts may need data that does not exist yet, and deletes may lose unrelated facts: these are *update anomalies*. The tool for finding redundancy is the *functional dependency*: attribute set X determines Y if any two rows that agree on X must agree on Y. Normal forms are conditions on dependencies that rule out classes of redundancy; decomposition splits a relation into smaller ones that satisfy them, without losing information. The cost is more joins at read time, so real designs sometimes denormalise on purpose.

## Core tenets

1. **Redundancy causes anomalies.** Store `(student, course, instructor)` where each course has one instructor. Changing a course's instructor requires updating every enrolment row (update anomaly); a course with no students cannot record its instructor (insertion anomaly); dropping the last student loses the instructor (deletion anomaly). All three come from storing "course → instructor" in many rows.

2. **Functional dependencies capture the rules of the domain.** X → Y means Y is a function of X in every legal instance of the relation. They are facts about the world (each course has one instructor), not about the current data, so the designer must state them. A key is a set of attributes that functionally determines all attributes.

3. **Dependencies can be reasoned about mechanically.** Armstrong's axioms (reflexivity, augmentation, transitivity) are sound and complete: every dependency implied by a set F can be derived from F using them. The *closure* X+ of an attribute set, computed by repeatedly applying dependencies, tells whether X is a key and whether a dependency is implied. This turns schema design into an algorithmic problem.

4. **Each normal form forbids a class of redundancy.** First Normal Form (1NF): attribute values are atomic (no repeating groups). Second (2NF): no non-key attribute depends on part of a candidate key. Third (3NF): for every non-trivial X → A, X is a superkey or A is part of some key. Boyce-Codd Normal Form (BCNF): for every non-trivial X → A, X is a superkey. BCNF eliminates all redundancy that functional dependencies can detect.

5. **Decomposition must be lossless.** Splitting R into R1 and R2 is lossless if joining them always gives back exactly R, with no spurious tuples. It is lossless if the common attributes are a key of R1 or of R2. In the example, splitting into `(course, instructor)` and `(student, course)` is lossless because `course` is a key of the first.

6. **BCNF and dependency preservation can conflict.** Some schemas have no BCNF decomposition that keeps every dependency checkable within a single table; enforcing the lost dependency then needs a join. 3NF always has a lossless, dependency-preserving decomposition (by the synthesis algorithm), at the cost of a little residual redundancy. Designers choose between them.

7. **Higher normal forms handle other dependency types.** Multivalued dependencies arise when two independent multi-valued facts share a key (an employee's skills and languages stored in one table produce a cross product). Fourth Normal Form (4NF) removes them; Fifth Normal Form (5NF) handles join dependencies. They matter less often in practice but follow the same logic.

8. **Denormalisation is a deliberate performance trade.** Normalised schemas minimise update cost and anomalies but require joins to reassemble data. Analytical warehouses use star schemas, with a wide fact table and denormalised dimension tables, because reads vastly outnumber writes. Materialised views and caches denormalise while letting the system, not the application, keep copies consistent.

## Key concepts

| Term | Meaning |
|---|---|
| Update anomaly | Inconsistency risk from storing one fact in many places |
| Functional dependency X → Y | Rows equal on X are equal on Y |
| Armstrong's axioms | Sound and complete inference rules for functional dependencies |
| Attribute closure X+ | All attributes determined by X under given dependencies |
| Superkey | Attribute set that determines all attributes (a key or a superset of one) |
| 3NF | Each dependency has a superkey on the left or a key attribute on the right |
| BCNF | Each non-trivial dependency has a superkey on the left |
| Lossless-join decomposition | Split whose join reproduces the original relation exactly |
| Dependency preservation | All dependencies checkable on individual decomposed relations |
| Denormalisation | Intentionally reintroducing redundancy for read performance |

## How it fits

- **Below:** a functional dependency is the mathematical notion of a [function](../../01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) between attribute projections; Armstrong's axioms are a small formal system proved sound and complete with standard [proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md). It works within [the relational model](the-relational-model.md).
- **Above:** more normalised schemas mean more [joins](../03-query-processing/join-algorithms.md) per query. "One fact in one place" is the data analogue of [modularity and information hiding](../../12-software-engineering/01-design/modularity-and-information-hiding.md) in software design.
- **Siblings:** [non-relational models](non-relational-models.md) often denormalise by default, embedding related data in one document, and inherit the anomalies normalization was designed to prevent.

## Common misconceptions

- **"Normalization is about saving disk space."** It is about consistency: eliminating the possibility of contradictory copies. Space savings are a side effect.
- **"Higher normal form is always better."** Each step may add joins and lose dependency preservation; 3NF or BCNF is the usual target, and analytics often prefers denormalised schemas.
- **"Normalization can be done from sample data."** Dependencies are rules about all legal data; a sample can disprove a dependency but never prove one.

## Go deeper

- E. F. Codd, *Further Normalization of the Data Base Relational Model* (1971): 2NF and 3NF.
- W. W. Armstrong, *Dependency Structures of Data Base Relationships* (1974): the axioms.
- R. Ramakrishnan, J. Gehrke, *Database Management Systems* (3rd ed., 2003): clear chapter on schema refinement and normal forms.
