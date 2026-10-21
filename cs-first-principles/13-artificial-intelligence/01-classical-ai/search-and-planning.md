# Search and Planning

> **Layer:** [13 Artificial Intelligence](../README.md) › [Classical AI](README.md)
> **Builds on:** [Graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md), [Shortest paths](../../05-algorithms-and-data-structures/05-graph-algorithms/shortest-paths.md), [Propositional logic](../../01-mathematical-foundations/01-logic/propositional-logic.md), [P, NP and NP-completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md)
> **Enables:** [Constraint satisfaction](constraint-satisfaction.md), [Reinforcement learning](../04-advanced-paradigms/reinforcement-learning.md), [Large language models](../04-advanced-paradigms/large-language-models.md)

## Essence

Many problems an intelligent agent faces can be stated as: here is where I am, here is what I want, here are the moves I can make; find a sequence of moves. Classical Artificial Intelligence (AI) treats this as search in a **state space**, a graph whose nodes are world states and whose edges are actions. The graph is almost never written down: it is generated on demand from a start state and a successor function, and it is usually far too large to explore fully. The whole craft is deciding *which node to expand next*. A good **heuristic**, an estimate of the remaining cost, lets the search ignore most of the space while still guaranteeing an optimal answer. Planning is the same idea with states described in logic, so that general-purpose heuristics can be computed from the problem description itself.

## Core tenets

1. **A problem is a start state, a successor function, a goal test and a cost.** Once a problem is in this form, one generic algorithm solves every instance: the agent does not need domain-specific code, only a domain description. This separation of *problem definition* from *solver* is the central move of classical AI.

2. **The state space is implicit and exponential.** With branching factor *b* and solution depth *d*, uninformed search touches O(b^d) nodes. A 15-puzzle has about 10^13 reachable states; chess about 10^44 legal positions. Storing the graph is impossible, so search algorithms generate nodes lazily and keep only a frontier and (sometimes) a visited set.

3. **Search strategy is the order in which the frontier is expanded.** Breadth-first search (a queue) finds the shallowest goal but stores the whole frontier, O(b^d) memory. Depth-first search (a stack) uses O(bd) memory but can wander forever. Iterative deepening runs depth-first search with depth limits 1, 2, 3, ... and gets both: optimal depth and linear memory, at a constant-factor time cost, because most nodes in an exponential tree are at the deepest level.

4. **A\* is optimal when its heuristic never overestimates.** A\* expands the node with the smallest f(n) = g(n) + h(n), where g is the cost so far and h estimates the cost to go. If h is *admissible* (h(n) ≤ true remaining cost), the first goal popped is optimal, because any cheaper path would have an f-value below it and would have been expanded first. If h is also *consistent* (h(n) ≤ c(n, n') + h(n')), no node needs reopening. With h = 0, A\* reduces to Dijkstra's algorithm.

5. **Good heuristics come from relaxed problems.** The exact cost of a simplified problem (drop a rule) is an admissible heuristic for the original. Manhattan distance for sliding puzzles is the cost if tiles could pass through each other. The closer h is to the true cost, the fewer nodes A\* expands; a perfect h expands only the solution path.

6. **Adversarial search assumes the opponent plays well.** In two-player zero-sum games, minimax assigns each position the value it would have under optimal play by both sides. Alpha-beta pruning skips branches that cannot change the decision and, with good move ordering, reduces O(b^d) to about O(b^(d/2)), doubling the reachable depth. Monte Carlo Tree Search (MCTS) replaces exhaustive expansion with sampled playouts and an exploration bonus; combined with learned value and policy networks it beat top human Go players in 2016.

7. **Planning searches over logical state descriptions.** A planning language such as STRIPS (Stanford Research Institute Problem Solver) or its descendant PDDL (Planning Domain Definition Language) describes states as sets of true facts and actions by preconditions and effects. Because the representation is explicit, planners can derive domain-independent heuristics automatically, for example by ignoring delete effects. Plan existence for STRIPS is PSPACE-complete, so heuristics, not completeness proofs, decide what is practical.

## Key concepts

| Term | Meaning |
|---|---|
| State space | Graph of world states connected by actions, generated lazily from a successor function |
| Frontier | Set of generated but not yet expanded nodes; its ordering defines the algorithm |
| Branching factor | Average number of successors per state; drives the exponential blow-up |
| Heuristic h(n) | Estimate of the cheapest cost from n to a goal |
| Admissible | Never overestimates the true remaining cost; guarantees A\* optimality |
| Consistent | Satisfies a triangle inequality along edges; implies admissible |
| Minimax | Game value assuming both players maximise their own outcome |
| Alpha-beta pruning | Skipping subtrees that provably cannot affect the minimax decision |
| STRIPS / PDDL | Languages describing actions by preconditions, add effects and delete effects |

## How it fits

- **Below:** Search is graph traversal from [Layer 05](../../05-algorithms-and-data-structures/README.md) applied to graphs too large to store; A\* is Dijkstra's [shortest-path](../../05-algorithms-and-data-structures/05-graph-algorithms/shortest-paths.md) algorithm with a goal-directed bias. The hardness of planning comes from [complexity theory](../../02-theory-of-computation/04-complexity/complexity-classes.md), and pruning strategies echo [branch and bound](../../05-algorithms-and-data-structures/03-design-paradigms/backtracking-and-branch-and-bound.md).
- **Above:** Reinforcement learning generalises search to unknown, stochastic environments and learns the heuristic (a value function) instead of hand-writing it. Language-model "agents" as of the mid-2020s wrap a learned policy in a search-and-act loop that is recognisably a planner.
- **Siblings:** [Constraint satisfaction](constraint-satisfaction.md) is search where the path does not matter, only the final assignment. [Knowledge representation](knowledge-representation-and-reasoning.md) supplies the logical state language planners use. [Probabilistic reasoning](probabilistic-reasoning.md) handles the uncertainty that classical planning assumes away.

## Common misconceptions

- **"A\* is always the best choice."** A\* stores every generated node, so memory, not time, usually runs out first. Iterative-deepening A\* and other memory-bounded variants exist for this reason.
- **"A better heuristic is one that is larger."** Only among admissible heuristics. An overestimating heuristic can be faster but loses the optimality guarantee.
- **"Game-playing AI searches the whole game tree."** No practical program does; it searches to a limited depth and evaluates the leaves with a heuristic or learned value function.

## Go deeper

- Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach* (4th ed., 2020): chapters 3–6 and 11 are the standard treatment of search, games and planning.
- Peter Hart, Nils Nilsson and Bertram Raphael, "A Formal Basis for the Heuristic Determination of Minimum Cost Paths" (1968): the original A\* paper and its optimality proof.
- Malik Ghallab, Dana Nau and Paolo Traverso, *Automated Planning: Theory and Practice* (2004): planning representations and algorithms in depth.
