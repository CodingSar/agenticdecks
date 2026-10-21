# Work, Span and Parallel Models

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Parallel computing](README.md)
> **Builds on:** [Asymptotic analysis](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md), [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md), [Models of computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md)
> **Enables:** [Data and task parallelism](data-and-task-parallelism.md), [Parallel programming models](parallel-programming-models.md), [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md)

## Essence

A parallel computation is a directed acyclic graph (DAG) of operations, where an edge means "this must finish before that starts". Two numbers summarise the graph. **Work** (T1) is the total number of operations, the time on one processor. **Span** (T∞, also called depth or critical-path length) is the length of the longest chain of dependencies, the time on unlimited processors. No schedule can beat either bound, and a simple greedy scheduler gets within a factor of two of the best possible. Real machines add a third cost, communication, which models such as the Bulk Synchronous Parallel (BSP) model and LogP charge for explicitly.

## Core tenets

1. **Two lower bounds hold for any schedule on P processors: T_P ≥ T1 / P and T_P ≥ T∞.** P processors do at most P operations per step, so they need at least T1/P steps (the work law). Operations on the critical path must run one after another, so no number of processors beats T∞ (the span law). Together they cap speed-up T1/T_P at min(P, T1/T∞).

2. **Parallelism is the ratio T1 / T∞.** It is the average number of operations available per step along the critical path, and it is the largest speed-up any number of processors can give. Summing n numbers with a balanced tree has work Θ(n) and span Θ(log n), so parallelism is Θ(n / log n): huge. A loop where each iteration needs the previous result has span Θ(n) and parallelism 1, no matter how many cores you buy.

3. **Greedy scheduling is nearly optimal: T_P ≤ T1/P + T∞.** A greedy scheduler never leaves a processor idle while ready work exists. Each step either keeps all P processors busy (at most T1/P such steps) or runs every ready node, shortening the remaining critical path (at most T∞ such steps). This is Brent's theorem (1974), and it means that when parallelism greatly exceeds P, near-linear speed-up follows automatically. Work-stealing schedulers achieve this bound in expectation.

4. **Amdahl's law is the span law for a fixed serial fraction.** If a fraction s of the work must run serially, speed-up is at most 1 / (s + (1 − s)/P), which tends to 1/s. With s = 5%, no machine gets more than 20×. Gustafson's law (1988) is the complementary view: if the problem grows with the machine, the serial fraction of the *larger* problem often shrinks, so scaled speed-up keeps rising. Both are true; they answer different questions (strong scaling with a fixed problem versus weak scaling with a growing one).

5. **A good parallel algorithm is work-efficient first.** If the parallel algorithm does asymptotically more work than the best serial one, then for large inputs it loses to the serial algorithm on any fixed number of cores. The goal is work equal to the best serial algorithm with polylogarithmic span. Parallel prefix sum (scan) shows the pattern: a naive version does Θ(n log n) work; the Blelloch scan does Θ(n) work with Θ(log n) span.

6. **Communication, not arithmetic, usually dominates.** Moving a word between cores, sockets or machines costs far more time and energy than an arithmetic operation on it (a floating-point operation costs on the order of picojoules; fetching its operand from Dynamic Random-Access Memory (DRAM) costs hundreds of times more, circa 2020s hardware). Work–span ignores this. The BSP model (Valiant, 1990) charges each superstep for computation, for the largest message volume h times a per-word cost g, and for a barrier cost L. LogP (Culler et al., 1993) charges latency L, overhead o, gap g and processor count P. The lesson of both: reduce data movement and the number of synchronisations, not just operations.

7. **The Parallel Random Access Machine (PRAM) is the idealised baseline, not a machine.** The PRAM gives P processors unit-time access to a shared memory in lock-step. It is useful for discovering what is inherently sequential (problems that are P-complete, such as circuit value, are believed to have no polylogarithmic-span algorithm). It hides contention and memory latency, so a PRAM-optimal algorithm can be slow in practice.

## Key concepts

| Term | Meaning |
|---|---|
| Work T1 | Total operations; running time on one processor |
| Span T∞ | Longest dependency chain; running time with unlimited processors |
| Parallelism | T1 / T∞; the maximum useful number of processors |
| Speed-up | T1 / T_P; linear when it equals P |
| Efficiency | Speed-up / P; the fraction of processor time doing useful work |
| Strong scaling | Fixed problem size, more processors (Amdahl regime) |
| Weak scaling | Problem size grows with processors (Gustafson regime) |
| Work-efficient | Parallel work is within a constant of the best serial algorithm |
| BSP / LogP | Models that add communication and synchronisation costs to the count |
| NC (Nick's Class) | Problems solvable in polylogarithmic span with polynomial work |

## How it fits

- **Below:** extends the [Random Access Machine (RAM) model](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md) with a dependency graph; uses [asymptotic notation](../../02-theory-of-computation/04-complexity/asymptotic-analysis.md) and [recurrences](../../01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) to compute span of [divide-and-conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) algorithms; communication costs come from the [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) and the [network](../../08-networking/01-principles/latency-bandwidth-and-queueing.md).
- **Above:** sizing a cluster, choosing batch size in [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), and judging whether a [batch job](../05-large-scale-systems/batch-and-stream-processing.md) will scale all use these bounds.
- **Siblings:** [Data and task parallelism](data-and-task-parallelism.md) are the patterns with good work and span; [parallel programming models](parallel-programming-models.md) are how they are written down and scheduled.

## Common misconceptions

- **"More cores always means faster."** Speed-up is capped by T1/T∞ and by the serial fraction; past that point, added cores add only overhead and contention.
- **"Amdahl's law proves massive parallelism is useless."** It applies to a fixed problem. Most large parallel workloads grow the problem with the machine, where Gustafson's view applies.
- **"Super-linear speed-up breaks the work law."** It happens when P caches together hold the working set that one cache could not. The serial baseline was slowed by memory, not the law broken.

## Go deeper

- Cormen, Leiserson, Rivest and Stein, *Introduction to Algorithms*, 3rd ed. (2009), chapter "Multithreaded Algorithms": the clearest treatment of work, span and greedy scheduling.
- Blelloch, "Programming Parallel Algorithms", *Communications of the ACM* (1996): why work and depth are the right measures.
- Valiant, "A Bridging Model for Parallel Computation", *Communications of the ACM* (1990): the BSP model.
- Herlihy and Shavit, *The Art of Multiprocessor Programming* (2008): the shared-memory side, from Amdahl to scheduling.
