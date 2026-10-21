# Amdahl's Law

> **Layer:** [04 Computer Architecture](../README.md) › [Performance](README.md)
> **Builds on:** [The performance equation](the-performance-equation.md), [Calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md)
> **Enables:** [Multicore and cache coherence](../04-parallel-architecture/multicore-and-cache-coherence.md), [Work, span and parallel models](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md), [Scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md), [Debugging](../../12-software-engineering/03-quality/debugging.md)

## Essence

Amdahl's law says that the overall speedup from improving part of a system is limited by the fraction of time the improved part was used. If a fraction f of the run time is sped up by a factor s, the overall speedup is 1 / ((1 − f) + f/s). As s grows without bound, the speedup approaches 1 / (1 − f): if 10% of a program is serial, no number of processors can make it more than 10 times faster. Gene Amdahl stated the argument in 1967 to question massively parallel machines; it remains the first calculation to make before any optimisation, and the reason to profile before tuning.

## Core tenets

1. **The unimproved part dominates in the limit.** Let the original time be 1. After improvement it is (1 − f) + f/s. With f = 0.9 and s = 10, time is 0.1 + 0.09 = 0.19, a speedup of 5.3, not 10. With s = 1,000, time is 0.1009, a speedup of just under 10. Most of the benefit comes early; past a point, further acceleration of the improved part buys almost nothing.

2. **Make the common case fast.** The law turns into a design rule: put effort where time is spent. Speeding up something that takes 2% of run time by any factor gains at most 2%. This is why architects measure instruction mixes before adding instructions, why profilers exist, and why a 2x improvement in a hot loop beats a 100x improvement in start-up code.

3. **Parallel speedup is bounded by the serial fraction.** With p processors and a parallel fraction f, speedup = 1 / ((1 − f) + f/p). For f = 0.95, 8 cores give 5.9x, 64 cores give 15.4x and 1,024 cores give 19.6x, against a ceiling of 20x. Serial sections include start-up, I/O, synchronisation, reductions and any code nobody parallelised.

4. **Overheads make reality worse than the formula.** The basic law assumes the parallel part divides perfectly. In practice communication, load imbalance, lock contention and cache coherence traffic grow with the number of processors, so speedup often peaks and then declines as more processors are added. The law is an upper bound, not a prediction.

5. **Gustafson's law changes the question, not the arithmetic.** Gustafson (1988) observed that people use bigger machines to solve bigger problems in the same time, and the parallel part usually grows with problem size while the serial part does not. Under that "weak scaling" assumption, scaled speedup = (1 − f) + f × p grows nearly linearly. Amdahl describes strong scaling (fixed problem, more processors); Gustafson describes weak scaling (problem grows with processors). Both are correct for their assumptions.

6. **It applies to every resource, not just processors.** Making the Central Processing Unit (CPU) infinitely fast does not help a program that spends half its time waiting for disk. Speeding up the network does not help a request dominated by database time. Amdahl's law is a statement about composition of any sequential stages of a task, which is why it reappears in system design and in latency budgets for distributed services.

7. **It motivated heterogeneous designs.** Hill and Marty (2008) applied the law to multicore chips: if some code stays serial, a chip does best with one or a few large, fast cores for serial parts plus many small cores for parallel parts. ARM big.LITTLE (2011), Apple's performance and efficiency cores, and Intel's hybrid P-core and E-core designs (2021) follow this logic, as does pairing a CPU with a Graphics Processing Unit (GPU).

```
 speedup with p processors, serial fraction (1 - f)
 p:          1     8     64    1024   infinity
 f = 0.50   1.0   1.8   2.0    2.0     2
 f = 0.90   1.0   4.7   8.8    9.9    10
 f = 0.95   1.0   5.9  15.4   19.6    20
 f = 0.99   1.0   7.5  39.3   91.2   100
```

## Key concepts

| Term | Meaning |
|---|---|
| Speedup | Old execution time divided by new execution time |
| Improved fraction (f) | Fraction of original time spent in the part that is accelerated |
| Serial fraction | Part of the work that cannot be parallelised: 1 − f |
| Strong scaling | Fixed total problem size, increasing processors |
| Weak scaling | Problem size grows in proportion to processors |
| Gustafson's law | Scaled speedup (1 − f) + f × p under weak scaling |
| Parallel efficiency | Speedup divided by the number of processors |
| Heterogeneous multicore | Chip mixing large fast cores with small efficient ones |

## How it fits

- **Below:** it is arithmetic on the [performance equation](the-performance-equation.md); its limit is a simple [calculus](../../01-mathematical-foundations/05-continuous-mathematics/calculus.md) limit.
- **Above:** [work–span analysis](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) generalises it (span plays the role of the serial part); [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) attack serial bottlenecks in services; profiling-driven [debugging](../../12-software-engineering/03-quality/debugging.md) of performance follows its rule; [locks](../../07-operating-systems/03-concurrency/locks-and-semaphores.md) create serial sections.
- **Siblings:** it explains the limits of the [multicore](../04-parallel-architecture/multicore-and-cache-coherence.md) response to [the end of scaling](power-and-the-end-of-scaling.md).

## Common misconceptions

- **"Amdahl's law shows parallelism is pointless."** It shows that serial sections must shrink as processors grow; with weak scaling and careful design, machines with millions of cores do useful work.
- **"Doubling the speed of a component doubles system speed."** Only if that component accounted for all of the time.
- **"The law predicts the speedup you will get."** It gives an upper bound under perfect parallelisation; overheads typically make real speedups lower.

## Go deeper

- Amdahl, *Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities* (AFIPS, 1967): the original, short argument.
- Gustafson, *Reevaluating Amdahl's Law* (CACM, 1988): the weak-scaling counterpoint.
- Hill and Marty, *Amdahl's Law in the Multicore Era* (IEEE Computer, 2008): consequences for chip design.
