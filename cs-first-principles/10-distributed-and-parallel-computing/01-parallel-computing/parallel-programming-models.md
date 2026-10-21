# Parallel Programming Models

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Parallel computing](README.md)
> **Builds on:** [Threads](../../07-operating-systems/02-process-management/threads.md), [Multicore and cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [Memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md), [Data and task parallelism](data-and-task-parallelism.md)
> **Enables:** [Batch and stream processing](../05-large-scale-systems/batch-and-stream-processing.md), [System models and failures](../02-distributed-foundations/system-models-and-failures.md), [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md)

## Essence

A parallel programming model is the contract between the programmer and the parallel machine: how work is expressed, how data is shared or exchanged, and how workers synchronise. Two choices define most models. The **memory view** is either shared (all workers read and write one address space) or distributed (each worker owns its memory and exchanges messages). The **control style** is either independent threads, lock-step data-parallel kernels, or a dataflow graph run by a runtime. Each combination makes some patterns cheap and others hard, and each has its own typical bugs.

## Core tenets

1. **Shared memory makes communication implicit and synchronisation explicit.** Threads communicate by writing and reading the same variables, which is convenient but means every conflicting access needs a lock, an atomic operation or a barrier. The hardware keeps caches coherent, but the [memory consistency model](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) decides in what order other cores see writes; without proper synchronisation, compilers and processors may reorder accesses and the program has a data race. POSIX threads (the Portable Operating System Interface thread library), Open Multi-Processing (OpenMP) and Java threads are in this family.

2. **Message passing makes communication explicit and sharing impossible.** In the Message Passing Interface (MPI), each process has private memory and sends and receives messages, often with collective operations (broadcast, reduce, all-reduce, all-to-all). There are no data races on shared variables, and the cost of communication is visible in the code. The price is that the programmer must partition data by hand. Message passing is the only model that scales across machines, so shared-memory systems at large scale emulate it.

3. **Collective operations have known optimal algorithms, and they matter.** All-reduce (every worker ends up with the sum of every worker's vector) is the core of data-parallel training. The ring all-reduce sends each of the P workers about 2(P−1)/P times the vector size, nearly independent of P, so it is bandwidth-optimal. Choosing the right collective algorithm can change run time more than any local optimisation.

4. **Graphics Processing Unit (GPU) programming is Single Instruction, Multiple Threads (SIMT).** In CUDA (NVIDIA's Compute Unified Device Architecture) or OpenCL (Open Computing Language), the programmer writes a kernel for one thread; the hardware runs thousands of them in groups (warps of 32 threads on NVIDIA GPUs) that execute in lock-step. Branches where threads in a warp disagree run both paths serially (divergence). Performance depends on coalesced memory access (neighbouring threads touching neighbouring addresses) and on keeping enough threads in flight to hide memory latency of hundreds of cycles.

5. **Task-based and dataflow runtimes separate what from where.** In Cilk, Intel Threading Building Blocks, or task graphs in frameworks such as Spark and the dataflow engines in machine learning, the programmer states tasks and dependencies; the runtime schedules them, usually by work stealing. This gives portable performance and nearly optimal greedy scheduling, at the cost of runtime overhead and less control over data placement.

6. **Synchronisation primitives have costs and failure modes.** A barrier makes every worker wait for the slowest, so one straggler slows all. Locks serialise the critical section and can deadlock. Atomic read-modify-write instructions such as compare-and-swap are cheap without contention but bounce a cache line between cores under contention, costing on the order of 100 ns per transfer. Good parallel code minimises shared mutable state rather than protecting it more cleverly.

7. **Partitioned global address space (PGAS) and actors sit between the extremes.** PGAS languages (Unified Parallel C, Chapel) give one global address space but expose which part is local, so programmers can reason about locality. Actor systems (Erlang, Akka) give each actor private state and a mailbox, which is message passing inside one program; they map naturally onto distributed systems and their failure handling.

8. **Determinism is a property of the model, not just the program.** Pure data-parallel and dataflow models without shared mutable state produce the same answer on every run (up to floating-point reduction order). Threads with locks do not: the interleaving is chosen at run time, so bugs can be rare and unrepeatable. Models that restrict sharing trade expressiveness for easier reasoning.

## Key concepts

| Term | Meaning |
|---|---|
| Shared memory model | Workers communicate through one address space |
| Message passing | Workers have private memory and exchange messages |
| MPI | The standard library interface for message passing in high-performance computing |
| Collective | Communication involving all workers: broadcast, reduce, all-reduce |
| SIMT | Many scalar threads run in lock-step groups on a GPU |
| Warp divergence | Threads of one warp taking different branches, serialising them |
| Data race | Two unsynchronised accesses to the same location, at least one a write |
| Barrier | Point every worker must reach before any proceeds |
| Work stealing | Idle workers take tasks from other workers' queues |
| Actor | Unit with private state that reacts to messages in its mailbox |

## How it fits

- **Below:** shared-memory models rest on [cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md), [consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md), operating system (OS) [threads](../../07-operating-systems/02-process-management/threads.md) and [locks](../../07-operating-systems/03-concurrency/locks-and-semaphores.md); lock-free code uses [atomic primitives](../../07-operating-systems/03-concurrency/lock-free-synchronization.md); GPU models rest on [Single Instruction, Multiple Data (SIMD) hardware](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md); message passing rests on the [network](../../08-networking/README.md).
- **Above:** message passing generalises into the [distributed system model](../02-distributed-foundations/system-models-and-failures.md), where messages can also be lost and processes can crash; [batch and stream engines](../05-large-scale-systems/batch-and-stream-processing.md) are dataflow runtimes with fault tolerance; [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) combines GPU kernels with all-reduce.
- **Siblings:** [Work and span](work-span-and-parallel-models.md) predict how a program in any model can scale; [data and task parallelism](data-and-task-parallelism.md) are the patterns each model expresses.

## Common misconceptions

- **"Shared memory is easier than message passing."** It is easier to start and harder to get right. Data races and memory-ordering bugs are among the hardest bugs to find.
- **"A GPU is just a CPU with many cores."** A GPU core is a lane in a lock-step group with tiny caches per thread; code designed for independent Central Processing Unit (CPU) threads usually runs poorly on it.
- **"`volatile` makes shared variables thread-safe."** In C and C++ it neither makes accesses atomic nor orders them across threads; proper atomics or locks are required.

## Go deeper

- Herlihy and Shavit, *The Art of Multiprocessor Programming* (2008): shared-memory synchronisation from first principles.
- Gropp, Lusk and Skjellum, *Using MPI* (3rd ed., 2014): message passing as practised.
- Kirk and Hwu, *Programming Massively Parallel Processors* (several editions): the GPU model and its performance rules.
- Boehm, "Threads Cannot Be Implemented as a Library" (2005): why the language memory model matters.
