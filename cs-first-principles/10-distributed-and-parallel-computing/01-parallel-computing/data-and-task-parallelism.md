# Data and Task Parallelism

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Parallel computing](README.md)
> **Builds on:** [Work, span and parallel models](work-span-and-parallel-models.md), [Divide and conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md), [Vector and graphics hardware](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md)
> **Enables:** [Parallel programming models](parallel-programming-models.md), [Batch and stream processing](../05-large-scale-systems/batch-and-stream-processing.md), [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md)

## Essence

There are two basic ways to find independent work. **Data parallelism** applies the same operation to many data items at once: the parallelism grows with the data. **Task parallelism** runs different operations at once: the parallelism is fixed by the structure of the program. Most real programs mix the two, and a small set of patterns (map, reduce, scan, stencil, fork-join, pipeline) covers most of what is parallel in practice. Choosing a decomposition is mostly about two questions: how much independent work does it expose, and how much data must move between the pieces?

## Core tenets

1. **Data parallelism scales with input size, which is why it dominates.** If a million pixels each need the same filter, there are a million independent tasks, and the program needs no change to use a bigger machine. This is why Graphics Processing Units (GPUs), vector units and MapReduce-style systems are built around it. Single Instruction, Multiple Data (SIMD) hardware exploits it directly: one instruction decoder drives many arithmetic lanes, saving the control cost per operation.

2. **Map, reduce and scan are the core data-parallel patterns.** *Map* applies a function to each element independently: work n, span 1. *Reduce* combines all elements with an associative operator such as + or max: work n, span log n using a tree. *Scan* (prefix sum) produces every running total: work n, span log n, and it unlocks surprising parallelism, such as parallel radix sort, stream compaction and solving linear recurrences. Associativity is the load-bearing property: it lets the combining tree be any shape.

3. **Floating-point reduction is not exactly reproducible.** Floating-point addition is not associative ((a + b) + c can differ from a + (b + c) because of rounding), so a parallel reduction whose tree shape depends on thread count or timing can give slightly different answers run to run. Deterministic results need a fixed reduction order, which costs flexibility.

4. **Task parallelism is bounded by program structure.** A compiler front end, optimiser and code generator running as separate tasks give at most three-way parallelism. Fork-join recursion (spawn subproblems, wait for them, combine) is the scalable form of task parallelism: parallel quicksort or mergesort generate a tree of tasks whose count grows with the input, so they behave like data parallelism.

5. **Pipelines trade latency for throughput.** Splitting work into stages lets stage k work on item i while stage k+1 works on item i−1. Throughput is set by the slowest stage, and the latency of one item is the sum of all stages. Balancing stage costs matters more than adding stages. This is the same idea as an [instruction pipeline](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md), applied to software.

6. **Decomposition must respect locality.** A stencil computation (each grid cell updated from its neighbours, as in weather or heat simulations) is split into blocks; each block must receive a halo of neighbour values from adjacent blocks every step. Communication grows with block surface and computation with block volume, so large, compact blocks have the best ratio. The general rule is to partition so that most data a piece touches is its own.

7. **Grain size balances overhead against load balance.** Each task costs scheduling and synchronisation overhead, often microseconds for a thread task and milliseconds for a cluster task. Too-fine tasks drown in overhead; too-coarse tasks leave processors idle when one task is slower (stragglers). Over-decomposing into many more tasks than processors, then letting a scheduler assign them dynamically (work stealing), handles uneven task costs well.

8. **Embarrassingly parallel problems are the common, easy case.** Many workloads have no dependencies between items: rendering frames, hyperparameter search, Monte Carlo trials, serving independent web requests. They scale nearly linearly until shared resources (memory bandwidth, a central database, the network) saturate. The hard engineering is then in the shared resource, not the computation.

## Key concepts

| Term | Meaning |
|---|---|
| Data parallelism | Same operation over many data items concurrently |
| Task parallelism | Different operations or functions run concurrently |
| Map | Independent per-element function application |
| Reduce | Combine all elements with an associative operator |
| Scan (prefix sum) | All running combinations of a sequence |
| Stencil | Each element updated from a fixed neighbourhood |
| Fork-join | Spawn subtasks recursively, then wait and combine |
| Pipeline | Chain of stages, each working on a different item |
| Grain size | Amount of work per task relative to scheduling overhead |
| Work stealing | Idle workers take queued tasks from busy workers |

## How it fits

- **Below:** relies on [SIMD and GPU hardware](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) for data parallelism, on [divide and conquer](../../05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) for fork-join, and on [floating-point](../../03-digital-logic/01-number-representation/floating-point.md) semantics for reductions.
- **Above:** [MapReduce and Spark](../05-large-scale-systems/batch-and-stream-processing.md) are map and reduce over a cluster; data parallelism, model parallelism and pipeline parallelism are the three axes of [large-model training](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md); the [rasterization pipeline](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md) is data-parallel per vertex and per pixel.
- **Siblings:** [Work and span](work-span-and-parallel-models.md) score each pattern; [programming models](parallel-programming-models.md) provide the syntax and runtime for them.

## Common misconceptions

- **"Parallelising a loop is always safe if iterations look independent."** Hidden shared state (a shared counter, an allocator, a random number generator) creates races or serialisation. Independence must be checked, not assumed.
- **"Task parallelism is the general case, data parallelism the special case."** In practice data parallelism supplies almost all scalable parallelism, because only data grows with the problem.
- **"A deeper pipeline is always faster."** Throughput is set by the slowest stage, and each stage adds latency and buffering.

## Go deeper

- McCool, Robison and Reinders, *Structured Parallel Programming* (2012): the pattern catalogue with work-span analysis.
- Blelloch, "Prefix Sums and Their Applications" (1990): why scan is a fundamental primitive.
- Dean and Ghemawat, "MapReduce: Simplified Data Processing on Large Clusters" (2004): data parallelism at data-centre scale.
