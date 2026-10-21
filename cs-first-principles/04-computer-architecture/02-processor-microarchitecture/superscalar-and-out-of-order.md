# Superscalar and Out-of-Order Execution

> **Layer:** [04 Computer Architecture](../README.md) › [Processor Microarchitecture](README.md)
> **Builds on:** [Pipelining](pipelining.md), [Hazards and branch prediction](hazards-and-branch-prediction.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)
> **Enables:** [Multicore and cache coherence](../04-parallel-architecture/multicore-and-cache-coherence.md), [Memory consistency models](../04-parallel-architecture/memory-consistency-models.md), [Power and the end of scaling](../06-performance/power-and-the-end-of-scaling.md)

## Essence

A superscalar core fetches, decodes and executes several instructions per cycle. An out-of-order core goes further: it executes each instruction as soon as its operands are ready, not when its turn comes in program order. Together they turn a sequential instruction stream into a dataflow graph executed in parallel, extracting Instruction-Level Parallelism (ILP) that the programmer never wrote down. The key is a strict separation between the speculative, out-of-order *execution* of instructions and their in-order *commit*, which is the only point at which results become architecturally visible. Since the IBM 360/91 (1967) pioneered the core ideas and the Intel Pentium Pro (1995) brought them to the mainstream, nearly every high-performance core works this way.

## Core tenets

1. **A program is a dataflow graph hidden inside a sequence.** Each instruction depends only on the instructions that produce its inputs. In typical code many instructions in a window of a few hundred are independent, so they could run at once. Limits on ILP come from true data dependences, branch mispredictions and cache misses, not from program order itself.

2. **Register renaming removes false dependences.** With only 16 or 32 architectural registers, compilers reuse names, creating write-after-read and write-after-write conflicts that are not real data flow. The core maps each architectural destination to a fresh physical register (several hundred physical registers in 2020s cores) using a Register Alias Table. After renaming, only true read-after-write dependences remain, and the hardware can run independent instructions in any order.

3. **Instructions wait in a scheduler until their operands are ready.** After renaming, instructions enter issue queues (reservation stations, after Tomasulo's 1967 algorithm). When a producer finishes, it broadcasts its physical register tag; waiting instructions whose inputs are now all ready become eligible and are issued to free functional units, oldest first. This "wakeup and select" loop runs every cycle and is timing-critical.

4. **The reorder buffer restores the sequential illusion.** Every instruction gets an entry in a circular Reorder Buffer (ROB) in program order. Instructions may complete in any order, but they *retire* (commit) only from the head, in order, and only when all older instructions have retired. Exceptions and mispredictions are handled at retirement: everything younger is discarded. This gives precise exceptions and makes all speculation invisible to software.

5. **The window size decides how much latency can be hidden.** A load that misses to DRAM takes about 100 ns, which is 300–500 cycles at 3–5 GHz. A core with a 512-entry ROB (Intel Golden Cove, 2021) can keep finding independent work, including other loads that overlap their misses (memory-level parallelism), for much of that time. A window that fills up stalls the whole core, which is why ROB sizes grew from 40 (Pentium Pro) to around 600 (Apple M1 performance cores, 2020).

6. **Loads and stores need their own ordering machinery.** Memory dependences are not known until addresses are computed. A load–store queue holds memory operations in order; loads may run ahead of older stores whose addresses are unknown, speculatively, and are replayed if a conflict is later discovered. Store values stay in a store buffer until commit, because a speculative store must never reach memory. Loads check the store buffer first (store-to-load forwarding).

7. **Width is limited by dependences and by physics.** Doubling issue width does not double performance: typical integer code sustains two to four Instructions Per Cycle (IPC) even on six-to-eight-wide cores. The structures that make out-of-order work (rename tables, wakeup logic, register-file ports, bypass networks) grow faster than linearly with width and consume much of the core's power. This diminishing return, combined with the power wall around 2005, is why the industry turned from wider cores to more cores.

8. **Simultaneous multithreading reuses the machinery.** Because one thread rarely fills all functional units, Simultaneous Multithreading (SMT; Intel Hyper-Threading, 2002) lets two hardware threads share one out-of-order core, each with its own architectural registers and rename map. It adds tens of percent of throughput for a few percent of area, but shared caches and predictors create side channels.

```
 fetch/decode (in order) -> rename -> issue queues -> execute (out of order) -> ROB -> commit (in order)
                               |                         |                          ^
                               +--- allocate ROB entry --+--- write result, mark done --+
```

## Key concepts

| Term | Meaning |
|---|---|
| Superscalar | Issuing more than one instruction per cycle |
| Out-of-order execution | Executing instructions when their inputs are ready rather than in program order |
| Register renaming | Mapping architectural registers to physical registers to remove false dependences |
| Reservation station / issue queue | Buffer where renamed instructions wait for operands |
| ROB | Reorder Buffer: in-order record of in-flight instructions used for commit and recovery |
| Commit (retire) | Making an instruction's results architecturally visible, in program order |
| Load–store queue | Structure that tracks in-flight memory operations and detects ordering violations |
| Memory-Level Parallelism (MLP) | Number of cache misses outstanding at the same time |
| SMT | Simultaneous Multithreading: several threads sharing one core's execution resources |

## How it fits

- **Below:** the dependence structure is a directed acyclic [graph](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md); scheduler and rename circuits are limited by [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md).
- **Above:** compilers still matter (long dependence chains limit any core); the store buffer is why [memory consistency models](../04-parallel-architecture/memory-consistency-models.md) exist; [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md) exploit speculation and SMT sharing; [work–span analysis](../../10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) applies the same "critical path bounds speed" logic to parallel programs.
- **Siblings:** combines [pipelining](pipelining.md) with aggressive [prediction](hazards-and-branch-prediction.md) on top of a widened [datapath](datapath-and-control.md).

## Common misconceptions

- **"Out-of-order means results may appear out of order to the program."** Within a thread, never: commit is in order. Other cores may observe memory effects in unexpected orders, but that is governed by the memory consistency model, not by out-of-order execution as such.
- **"An eight-wide core runs eight instructions per cycle."** Sustained IPC on real code is usually two to four; the width serves bursts and recovery after stalls.
- **"Compilers no longer need to schedule code."** Out-of-order hardware hides short latencies, but the compiler still decides dependence chains, register pressure, vectorisation and memory layout, which the hardware cannot change.

## Go deeper

- Tomasulo, *An Efficient Algorithm for Exploiting Multiple Arithmetic Units* (IBM Journal, 1967): the original dynamic scheduling algorithm.
- Smith and Sohi, *The Microarchitecture of Superscalar Processors* (Proceedings of the IEEE, 1995): a clear survey of the whole mechanism.
- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Chapter 3: ILP and its limits with measurements.
