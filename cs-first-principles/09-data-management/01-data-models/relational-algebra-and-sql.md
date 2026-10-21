# Relational Algebra and SQL

> **Layer:** [09 Data Management](../README.md) › [Data Models](README.md)
> **Builds on:** [The Relational Model](the-relational-model.md), [Sets](../../01-mathematical-foundations/02-sets-relations-functions/sets.md), [Predicate Logic](../../01-mathematical-foundations/01-logic/predicate-logic.md), [Logic and Declarative Programming](../../06-programming-languages/01-paradigms/logic-and-declarative.md)
> **Enables:** [Join Algorithms](../03-query-processing/join-algorithms.md), [Query Optimization](../03-query-processing/query-optimization.md), [Batch and Stream Processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md), [Web Security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md)

## Essence

Relational algebra is a small set of operators that each take one or two relations and return a relation: select rows, project columns, take products, union, difference and rename. Every query is an expression tree of these operators, and because they obey algebraic identities, one tree can be rewritten into an equivalent but cheaper one. Structured Query Language (SQL) is the practical, declarative surface over this algebra (plus aggregation, ordering and other extensions): users describe the result they want and the system compiles it into an algebraic plan. That separation of *what* from *how* is why SQL has lasted fifty years.

## Core tenets

1. **Six primitive operators are enough for the core.** Selection σ_p(R) keeps tuples satisfying predicate p. Projection π_A(R) keeps attributes A (removing duplicates in pure algebra). Cartesian product R × S pairs every tuple of R with every tuple of S. Union R ∪ S, difference R − S, and renaming ρ complete the set. Intersection and joins are derived: R ∩ S = R − (R − S), and a join is a product followed by a selection.

2. **Joins combine relations by matching values.** The theta-join R ⋈_θ S = σ_θ(R × S); the equi-join uses equality; the natural join matches all same-named attributes. Joins are how foreign keys are followed. Defining them as product plus selection gives meaning; implementing them that way would be ruinous, which is why join algorithms matter.

3. **Closure makes the algebra compositional.** Every operator returns a relation, so any query result can feed another operator. Complex queries are trees of simple operators, views are reusable subtrees, and the optimizer manipulates trees uniformly.

4. **Algebraic laws enable optimisation.** Selections commute and cascade; a selection can be pushed below a join if its predicate mentions only one side (σ_{R.a=5}(R ⋈ S) = σ_{R.a=5}(R) ⋈ S); joins are commutative and associative; projections can be pushed down to drop unneeded columns early. Each law preserves the result while potentially shrinking intermediate data by orders of magnitude.

5. **Relational calculus is the declarative twin.** Tuple relational calculus describes the result as {t | φ(t)} for a predicate-logic formula φ. Codd showed that safe calculus and algebra have the same expressive power. SQL's SELECT-FROM-WHERE is essentially calculus syntax, and the system translates it into algebra for execution.

6. **SQL extends the algebra with practical operations.** GROUP BY with aggregates (COUNT, SUM, AVG) partitions rows and summarises each group; ORDER BY sorts output; outer joins keep unmatched rows padded with NULL; window functions compute aggregates over sliding groups without collapsing rows. SQL uses multiset (bag) semantics by default, keeping duplicates unless DISTINCT is written, because eliminating duplicates costs a sort or hash.

   ```sql
   SELECT d.name, AVG(e.salary)
   FROM   employee e JOIN department d ON e.dept_id = d.id
   WHERE  e.hired > DATE '2020-01-01'
   GROUP  BY d.name;
   ```

7. **Pure relational algebra cannot express recursion.** Questions such as "all managers above this employee, at any depth" (transitive closure) cannot be written as a fixed algebra expression, because each expression joins a bounded number of times. SQL:1999 added recursive Common Table Expressions (CTEs, written WITH RECURSIVE), which compute a fixpoint, the same idea as Datalog's recursive rules.

8. **Declarative queries must be parameterised, not concatenated.** Because SQL is a language, building a query by pasting user input into a string lets that input become code: SQL injection. Prepared statements send the query structure and the parameter values separately, so data can never change the query's meaning.

## Key concepts

| Term | Meaning |
|---|---|
| σ (selection) | Keep tuples satisfying a predicate |
| π (projection) | Keep chosen attributes |
| × (product) | All pairs of tuples from two relations |
| ⋈ (join) | Product restricted to matching tuples |
| ∪, −, ∩ | Set union, difference, intersection on union-compatible relations |
| Relational calculus | Declarative, logic-based query formalism equivalent to the algebra |
| Bag semantics | Multisets: duplicates retained unless explicitly removed |
| Aggregation | Grouping rows and computing summaries per group |
| Recursive CTE | Common Table Expression that references itself to compute a fixpoint |
| Prepared statement | Query compiled with placeholders; parameters bound separately |

## How it fits

- **Below:** operators are [set](../../01-mathematical-foundations/02-sets-relations-functions/sets.md) operations; predicates and calculus are [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); SQL belongs to the family of [declarative languages](../../06-programming-languages/01-paradigms/logic-and-declarative.md).
- **Above:** query plans are algebra trees, executed by [join algorithms](../03-query-processing/join-algorithms.md) and chosen by [query optimization](../03-query-processing/query-optimization.md). Dataflow systems for [batch and stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) expose the same operators (map ≈ project, filter ≈ select, join, group-by). SQL injection is a staple of [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md).
- **Siblings:** the [relational model](the-relational-model.md) supplies the objects the algebra manipulates; [normalization](normalization.md) decides how many joins queries will need; [non-relational models](non-relational-models.md) often lack joins and push them into application code.

## Common misconceptions

- **"SQL executes in the order it is written."** Logically, FROM and WHERE come before SELECT; physically, the optimizer reorders everything it legally can.
- **"Joins are inherently slow."** A join on an indexed key or via hashing is close to linear in input size; slowness usually comes from missing indexes or bad cardinality estimates.
- **"SQL is relational algebra."** SQL has bag semantics, NULLs, ordering and aggregation, which make some algebraic rewrites invalid.

## Go deeper

- E. F. Codd, *Relational Completeness of Data Base Sublanguages* (1972): algebra and calculus equivalence.
- D. D. Chamberlin, R. F. Boyce, *SEQUEL: A Structured English Query Language* (1974): the origin of SQL.
- J. Widom, H. Garcia-Molina, J. D. Ullman, *Database Systems: The Complete Book* (2nd ed., 2008): algebra, SQL and their connection in depth.
