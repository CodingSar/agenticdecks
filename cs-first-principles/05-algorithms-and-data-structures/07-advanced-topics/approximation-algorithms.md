# Approximation Algorithms

> **Layer:** [05 Algorithms and Data Structures](../README.md) › [Advanced Topics](README.md)
> **Builds on:** [P, NP and NP-Completeness](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md), [Greedy Algorithms](../03-design-paradigms/greedy-algorithms.md), [Optimization](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md), [Randomized Algorithms](../03-design-paradigms/randomized-algorithms.md)
> **Enables:** [Constraint Satisfaction](../../13-artificial-intelligence/01-classical-ai/constraint-satisfaction.md), [Scheduling](../../07-operating-systems/02-process-management/scheduling.md), [Query Optimization](../../09-data-management/03-query-processing/query-optimization.md), [Partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md)

## Essence

For NP-hard optimisation problems (vertex cover, set cover, travelling salesperson, bin packing, scheduling) we do not expect an algorithm that is both exact and polynomial-time. An approximation algorithm gives up exactness but keeps a proof: it runs in polynomial time and always returns a solution within a known factor α of optimal. The core technique is to compare the algorithm's output not with the unknown optimum directly but with a *lower bound* on the optimum that is easy to compute (a matching, a spanning tree, a linear-programming relaxation). Complexity theory also tells us where this stops: for many problems, achieving a better factor than some threshold is itself NP-hard.

## Core tenets

1. **An α-approximation is a worst-case guarantee, not a heuristic.** For a minimisation problem, ALG ≤ α · OPT on every instance (α ≥ 1); for maximisation, ALG ≥ OPT / α. A heuristic may do well on typical inputs with no promise; an approximation algorithm comes with a proof covering adversarial ones.

2. **The analysis hinges on a computable lower bound for OPT.** You cannot compute OPT, so you bound it. For vertex cover, any *maximal matching* M gives a bound: every cover must include an endpoint of each matched edge, so OPT ≥ |M|. Taking both endpoints of every matched edge gives a cover of size 2|M| ≤ 2·OPT. The proof never needed to know OPT.

3. **Linear-programming relaxation plus rounding is the general method.** Write the problem as an integer program, drop integrality to get a Linear Program (LP) solvable in polynomial time, and note that LP-OPT ≤ OPT for minimisation. Then round the fractional solution to an integral one, bounding how much rounding costs. For vertex cover, round every variable ≥ 1/2 up to 1: cost ≤ 2 · LP-OPT ≤ 2 · OPT. Randomized rounding (treat fractional values as probabilities) gives O(log n) for set cover. The *integrality gap* (worst ratio of OPT to LP-OPT) limits what any rounding of that LP can achieve.

4. **Greedy often gives logarithmic or constant factors.** Greedy set cover (repeatedly pick the set covering the most uncovered elements) is within H(n) ≤ ln n + 1 of optimal. List scheduling (assign each job to the least-loaded machine) is within 2 − 1/m of the optimal makespan; sorting jobs longest first improves it to 4/3. These are among the most used algorithms in practice because they are simple and their guarantees hold everywhere.

5. **Some problems admit arbitrarily good approximations.** A Polynomial-Time Approximation Scheme (PTAS) achieves 1 + ε for any fixed ε > 0, with running time polynomial in n for each fixed ε (possibly like n^(1/ε)). A Fully Polynomial-Time Approximation Scheme (FPTAS) is polynomial in both n and 1/ε. Knapsack has an FPTAS: scale and round item values so the pseudo-polynomial dynamic program becomes polynomial, losing at most a factor 1 + ε. Euclidean travelling salesperson has a PTAS (Arora 1998; Mitchell 1999).

6. **Others cannot be approximated beyond a threshold unless P = NP.** The PCP (Probabilistically Checkable Proofs) theorem, proved in the early 1990s, implies that for MAX-3SAT, satisfying more than a 7/8 + ε fraction of clauses is NP-hard (Håstad, 2001), while a random assignment achieves 7/8. Set cover cannot be approximated within (1 − ε) ln n (Dinur and Steurer, 2014), so greedy is essentially optimal. General travelling salesperson without the triangle inequality cannot be approximated within any polynomial-time computable factor, because such an algorithm would decide Hamiltonian cycle.

7. **Problem structure decides approximability.** Metric travelling salesperson (distances obey the triangle inequality) has a 2-approximation via doubled MSTs (Minimum Spanning Trees) and 1.5 via Christofides (1976), slightly improved in 2020 by Karlin, Klein and Oveis Gharan. Without the triangle inequality it is inapproximable. Recognising which structural property your instance has (metric, planar, bounded degree, small integers) often decides whether a good guarantee exists.

8. **In practice, approximation guarantees are floors, not predictions.** Real instances typically come out far closer to optimal than the worst-case ratio, and practitioners combine approximation algorithms with local search, integer-programming solvers and heuristics. The guarantee's value is that it rules out catastrophic outcomes and provides a starting incumbent for [branch and bound](../03-design-paradigms/backtracking-and-branch-and-bound.md).

## Key concepts

| Term | Meaning |
|---|---|
| Approximation ratio α | Worst-case bound on ALG / OPT (minimisation) or OPT / ALG (maximisation) |
| Lower bound on OPT | Easily computed quantity that no feasible solution can beat |
| LP relaxation | The integer program with integrality constraints dropped |
| Rounding | Converting a fractional LP solution into an integral one with bounded loss |
| Integrality gap | Worst-case ratio between integer and LP optima |
| PTAS / FPTAS | 1 + ε approximation for any ε; polynomial in n / in n and 1/ε |
| Inapproximability | Proof that a better ratio than some threshold is NP-hard |
| PCP theorem | Every NP proof can be checked by reading a constant number of random bits of it |

## How it fits

- **Below:** NP-hardness from [complexity theory](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) motivates it; [linear programming and duality](../../01-mathematical-foundations/05-continuous-mathematics/optimization.md) supply bounds; [greedy](../03-design-paradigms/greedy-algorithms.md), [dynamic programming](../03-design-paradigms/dynamic-programming.md) and [randomization](../03-design-paradigms/randomized-algorithms.md) supply techniques; MSTs come from [graph algorithms](../05-graph-algorithms/minimum-spanning-trees.md).
- **Above:** [job and cluster scheduling](../../07-operating-systems/02-process-management/scheduling.md), [data partitioning and placement](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) (bin packing of shards and virtual machines), [query optimization](../../09-data-management/03-query-processing/query-optimization.md) heuristics for many-way joins, chip layout in [hardware design](../../03-digital-logic/04-hardware-design/fpga-and-asic.md), facility location, and k-means-style [clustering](../../13-artificial-intelligence/02-machine-learning-foundations/unsupervised-learning.md) (k-means++ is an O(log k) approximation in expectation).
- **Siblings:** [online algorithms](streaming-and-online-algorithms.md) use a similar ratio (competitive ratio) but against an opponent who knows the future; [computational geometry](computational-geometry.md) supplies the Euclidean structure that enables PTASs.

## Common misconceptions

- **"NP-hard means we must give up on quality."** Many NP-hard problems have constant-factor or 1 + ε guarantees in polynomial time.
- **"All NP-complete problems are equally hard to approximate."** They are equivalent for exact solution, but approximability ranges from FPTAS (knapsack) to essentially none (general travelling salesperson, maximum clique).
- **"A 2-approximation typically returns twice the optimum."** The ratio is a worst case; typical results are much closer.

## Go deeper

- Vijay V. Vazirani, *Approximation Algorithms* (2001): the standard text, organised by technique.
- David P. Williamson and David B. Shmoys, *The Design of Approximation Algorithms* (2011): comprehensive and freely available.
- Sanjeev Arora and Boaz Barak, *Computational Complexity: A Modern Approach* (2009): PCP theorem and hardness of approximation.
