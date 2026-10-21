# Query Optimization

> **Layer:** [09 Data Management](../README.md) › [Query Processing](README.md)
> **Builds on:** [Relational Algebra and SQL](../01-data-models/relational-algebra-and-sql.md), [Join Algorithms](join-algorithms.md), [B-Trees](../02-storage-and-indexing/b-trees.md), [Dynamic Programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md), [Statistical Inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md)
> **Enables:** [Batch and Stream Processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md), [Optimization (Compilers)](../../06-programming-languages/03-compilers/optimization.md), [Learning as Optimization](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md)

## Essence

A query optimizer takes a declarative query and chooses, among the many equivalent ways to execute it, one that is cheap. It works in three parts. A *plan space*: all algebra trees equivalent to the query, crossed with choices of access path and join algorithm for each node. A *cost model*: an estimate of each plan's Input/Output (I/O) and processor work, which depends on estimates of how many rows each operator produces. A *search strategy*: usually dynamic programming over join orders, as introduced by IBM's System R in 1979. The optimizer rarely finds the true best plan; its job is to avoid catastrophically bad ones, and its main weakness is that cardinality estimates can be wrong by orders of magnitude.

## Core tenets

1. **Equivalent plans can differ in cost by orders of magnitude.** Joining a 10-row filtered table to a billion-row table through an index costs ten lookups; joining in the other order without the filter can cost a full scan and a huge intermediate result. Because Structured Query Language (SQL) does not prescribe execution order, the system must make this choice, and the right choice depends on the data.

2. **Heuristic rewrites are almost always beneficial.** Push selections and projections as close to the base tables as possible, so later operators handle fewer and narrower rows. Unnest correlated subqueries into joins where possible. Remove redundant joins implied by foreign keys. These rewrites use the algebraic equivalences of relational algebra and rarely make things worse.

3. **Cardinality estimation drives every cost.** The cost of a join depends on the sizes of its inputs, which are the outputs of earlier operators. Optimizers estimate selectivity from statistics: row counts, distinct values per column, histograms of value distribution, and sometimes samples. For a predicate `a = 5` with 100 distinct values, a uniform assumption gives selectivity 1/100.

4. **Estimation errors compound across joins.** Optimizers typically assume predicates are independent and values uniformly distributed. Real data is correlated (city and postal code) and skewed. A 10× error per join becomes 1,000× after three joins. Leis et al. (2015) showed estimates in real workloads routinely off by orders of magnitude, and that this, more than the cost model, causes bad plans.

5. **Join ordering is the hard combinatorial core.** For n relations there are n! left-deep orders and far more bushy trees; the general problem of finding the optimal order is NP-hard. System R's insight: the best plan for joining a set S of relations can be built from the best plans for its subsets (principle of optimality), so dynamic programming over subsets finds the best left-deep plan in O(n·2^n) time rather than n!. That is practical for up to roughly 10–15 relations; beyond that, optimizers use greedy or randomised search.

6. **Interesting orders keep more than one plan per subset.** A plan that is slightly more expensive but produces output sorted on a useful key can make a later merge join or ORDER BY free. System R therefore keeps the cheapest plan for each subset *and each interesting sort order*. It is a small extension of dynamic programming that captures cross-operator effects.

7. **Physical choices are made alongside the order.** For each base table: full scan, index scan or index-only scan. For each join: nested-loop, index nested-loop, sort-merge or hash, with the build side chosen. Whether a secondary index helps depends on estimated selectivity: above a few percent of rows, random lookups usually lose to a sequential scan.

8. **Plans can adapt at runtime.** Because estimates are unreliable, modern systems re-optimise when observed cardinalities diverge from estimates, choose join algorithms adaptively once input sizes are known, or cache plans and recompile when statistics change. Extensible rule-based frameworks (Volcano/Cascades) let optimizers add new operators and rewrites without restructuring the search.

## Key concepts

| Term | Meaning |
|---|---|
| Logical plan | Tree of relational algebra operators |
| Physical plan | Tree of concrete algorithms and access paths |
| Selectivity | Fraction of input rows a predicate keeps |
| Cardinality estimate | Predicted number of rows an operator outputs |
| Histogram | Summary of a column's value distribution used for estimation |
| Left-deep plan | Join tree where every right input is a base table |
| Bushy plan | Join tree where both inputs of a join may be joins |
| Principle of optimality | Optimal plan for a set is built from optimal plans for subsets |
| Interesting order | Output sort order useful to a later operator |
| Adaptive execution | Revising plan choices at runtime using observed sizes |

## How it fits

- **Below:** rewrites are identities of [relational algebra](../01-data-models/relational-algebra-and-sql.md); operator costs come from [join algorithms](join-algorithms.md) and [B-tree](../02-storage-and-indexing/b-trees.md) access paths; join enumeration is [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md); estimation is applied [statistical inference](../../01-mathematical-foundations/06-probability-and-statistics/statistical-inference.md) from summaries and samples.
- **Above:** distributed engines for [batch and stream processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) use cost-based optimizers that also price network shuffles. Query optimizers share methods with [compiler optimisation](../../06-programming-languages/03-compilers/optimization.md) (rewrite rules, cost models), and recent work uses [learned models](../../13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) to estimate cardinalities.
- **Siblings:** [join algorithms](join-algorithms.md) supply the menu of operators and their cost formulas.

## Common misconceptions

- **"The optimizer finds the optimal plan."** It finds the cheapest plan under its estimates within a restricted search space; with bad estimates, it can pick a poor plan confidently.
- **"Adding an index always helps the optimizer."** Indexes add options, but they also add write cost, and stale statistics can lead the optimizer to use an index where a scan would be faster.
- **"Query hints are best practice."** Hints freeze a plan that may become wrong as data changes; fixing statistics or schema is usually better.

## Go deeper

- P. G. Selinger et al., *Access Path Selection in a Relational Database Management System* (SIGMOD 1979): the System R optimizer, still the template.
- G. Graefe, *The Cascades Framework for Query Optimization* (1995): rule-based extensible optimization.
- V. Leis et al., *How Good Are Query Optimizers, Really?* (VLDB 2015): measures where real optimizers go wrong.
- Y. E. Ioannidis, *Query Optimization* (ACM Computing Surveys, 1996): a concise overview.
