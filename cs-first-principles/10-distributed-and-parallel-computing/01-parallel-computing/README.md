# Parallel Computing

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › Parallel computing
> **Children:** [Work, span and parallel models](work-span-and-parallel-models.md) · [Data and task parallelism](data-and-task-parallelism.md) · [Parallel programming models](parallel-programming-models.md)

## What this area is about

Parallel computing asks how to finish one computation faster by running parts of it at the same time on many processing units. Since about 2005, single-core clock speeds have stopped rising because of power limits, so extra transistors arrive as extra cores, vector lanes and accelerators. Software only gets faster if it exposes parallel work.

The unifying idea is that **a computation is a graph of dependencies, and its speed is limited by the longest chain in that graph and by the cost of moving data between workers**. Everything in this area either measures that graph (work and span), finds ways to cut a problem into independent pieces (data and task decomposition), or gives programmers a way to express the pieces and their communication (programming models).

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Work, span and parallel models](work-span-and-parallel-models.md) | The theory: what speed-up is possible, given dependencies and communication | Asymptotic analysis, Amdahl's law |
| [Data and task parallelism](data-and-task-parallelism.md) | The two basic ways to decompose a problem, and the patterns built on them | Work and span |
| [Parallel programming models](parallel-programming-models.md) | The concrete interfaces (threads, message passing, Graphics Processing Unit (GPU) kernels, dataflow) and what each makes cheap | Both of the above, plus hardware |

Read the theory first. Work and span tell you *whether* a decomposition can scale before you write any code. Decomposition then gives you the patterns (map, reduce, scan, stencil, pipeline, fork-join) that have good work and span. The programming models are how those patterns are written down on real machines; each model chooses a memory view (shared or distributed) and a synchronisation style, and that choice decides which patterns are natural.

```
  dependency graph --> work T1, span Tinf --> speed-up bound
          |
  decomposition: data-parallel / task-parallel / pipeline
          |
  model: shared memory | message passing | GPU kernels | dataflow
          |
  hardware: multicore, clusters, GPUs, accelerators
```

## Connections to sibling areas

- **[Distributed foundations](../02-distributed-foundations/README.md):** parallel computing usually assumes reliable processors and bounded communication; distributed computing drops both assumptions. A message-passing program on a supercomputer and a replicated service on a data centre network use the same primitives but face very different failure models.
- **[Consensus and replication](../03-consensus-and-replication/README.md):** coordination is a serial bottleneck. Consensus is the most expensive form of coordination, so the span of a replicated system includes its consensus round trips.
- **[Distributed data](../04-distributed-data/README.md):** partitioning data so that most work touches one partition is the distributed version of a data-parallel decomposition.
- **[Large-scale systems](../05-large-scale-systems/README.md):** MapReduce, Spark and stream processors are data-parallel programming models extended with fault tolerance.

## Connections across layers

From [04 Computer Architecture](../../04-computer-architecture/README.md) this area takes [multicore and cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [Single Instruction, Multiple Data (SIMD) and GPUs](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) and [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md). From [05 Algorithms](../../05-algorithms-and-data-structures/README.md) it takes [divide and conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) and the [Random Access Machine (RAM) model](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md), which it extends. From [07 Operating Systems](../../07-operating-systems/README.md) it takes [threads](../../07-operating-systems/02-process-management/threads.md) and [synchronisation](../../07-operating-systems/03-concurrency/locks-and-semaphores.md). It enables [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), scientific computing and graphics.

## Cross-cutting threads

- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): the subject itself.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): span and Amdahl's serial fraction cap speed-up.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): communication, not arithmetic, is usually the bottleneck.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): grain size amortizes scheduling and synchronisation cost.
- [Composition](../../CROSS-CUTTING.md#composition): fork-join and pipelines compose because their work and span add predictably.
