# Classical AI

> **Layer:** [13 Artificial Intelligence](../README.md) › Classical AI
> **Children:** [Search and planning](search-and-planning.md) · [Constraint satisfaction](constraint-satisfaction.md) · [Knowledge representation and reasoning](knowledge-representation-and-reasoning.md) · [Probabilistic reasoning](probabilistic-reasoning.md)

## What this area is about

Classical Artificial Intelligence (AI), dominant from the 1956 Dartmouth workshop to the 1990s, asks: if a human writes down what the world is like and what the goal is, can a general algorithm work out what to do? Its unifying idea is **model-based reasoning**: build an explicit model (states and actions, variables and constraints, logical facts, probabilistic dependencies) and apply a domain-independent procedure (search, propagation, inference) to it. The intelligence lies in the combination of a well-chosen representation and an algorithm that exploits its structure.

Every child faces the same enemy: combinatorial explosion. State spaces, assignments, proofs and joint distributions all grow exponentially with problem size, and the relevant decision problems are NP-hard or worse. Classical AI is the study of the structure (heuristics, locality of constraints, restricted logics, conditional independence) that makes real instances solvable despite the worst case.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Search and planning](search-and-planning.md) | Finding action sequences in implicit state graphs; the core loop of a goal-directed agent | Graph algorithms, heuristics |
| [Constraint satisfaction](constraint-satisfaction.md) | Finding assignments that satisfy local constraints; Boolean satisfiability (SAT) as the universal engine | Search, propositional logic |
| [Knowledge representation and reasoning](knowledge-representation-and-reasoning.md) | Writing down facts and rules and deriving their consequences soundly | Logic; uses constraint solving and search as engines |
| [Probabilistic reasoning](probabilistic-reasoning.md) | Replacing true/false with degrees of belief and updating them with evidence | Probability, graph structure |

Read search first: it introduces the state-space view and the idea that a heuristic buys tractability, and its diagram row below uses Monte Carlo Tree Search (MCTS). Constraint satisfaction specialises search to problems where only the final answer matters and adds propagation; Conflict-Driven Clause Learning (CDCL) is its workhorse algorithm. Knowledge representation steps back to ask what language the agent's model should be written in and what that choice costs. Probabilistic reasoning relaxes the assumption that the model is certain.

```
           representation                        algorithm
   states + actions ----------------------> heuristic search (A*, MCTS)
   variables + constraints ---------------> backtracking + propagation (CDCL)
   logical sentences ---------------------> resolution, chaining
   probabilistic graph -------------------> variable elimination, sampling
                    \___ all exploit structure to beat exponential worst cases ___/
```

The four are tightly interlinked. Planning problems compile into SAT; logical inference is a search over proofs; probabilistic inference on a graph is the same dynamic programming as solving a tree-structured constraint problem, with sums in place of logical "or".

## Connections to sibling areas

- **[Machine learning foundations](../02-machine-learning-foundations/README.md):** Classical AI writes the model by hand; machine learning fits it from data. Probabilistic reasoning is the bridge: learning the parameters of a Bayesian network is statistical estimation, and many learning algorithms are inference in a probabilistic model.
- **[Deep learning](../03-deep-learning/README.md):** Neural networks replaced hand-engineered features and heuristics in perception, where explicit models had failed. Hand-written heuristics for search are now often replaced by learned value functions.
- **[Advanced paradigms](../04-advanced-paradigms/README.md):** Reinforcement learning is planning in a Markov Decision Process whose model may be unknown; AlphaGo-style systems combine tree search with learned networks. Language-model agents as of the mid-2020s rediscover planning, tool use and verification, often calling classical solvers as tools.

## Connections across layers

From below, classical AI takes [logic](../../01-mathematical-foundations/01-logic/README.md), [probability](../../01-mathematical-foundations/06-probability-and-statistics/README.md), [graph algorithms](../../05-algorithms-and-data-structures/05-graph-algorithms/README.md), [design paradigms](../../05-algorithms-and-data-structures/03-design-paradigms/README.md) such as backtracking and dynamic programming, and the hardness results of [complexity theory](../../02-theory-of-computation/04-complexity/README.md) and [computability](../../02-theory-of-computation/03-computability/README.md). Its descendants spread back down the stack: SAT and Satisfiability Modulo Theories (SMT) solvers drive [formal methods](../../06-programming-languages/05-formal-methods/README.md), Datalog shapes [query languages](../../09-data-management/01-data-models/README.md), and constraint solvers schedule work in [large-scale systems](../../10-distributed-and-parallel-computing/05-large-scale-systems/README.md).

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): separate the problem description from the general solver.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): the choice of representation decides which inferences are cheap.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): NP-hardness and semi-decidability bound every reasoner.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): expressiveness versus tractability; optimality versus memory in search.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): learned clauses, transposition tables and cached factors avoid repeated work.
