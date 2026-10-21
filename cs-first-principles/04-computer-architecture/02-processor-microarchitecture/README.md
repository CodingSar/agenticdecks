# Processor Microarchitecture

> **Layer:** [04 Computer Architecture](../README.md) › Processor Microarchitecture
> **Children:** [Datapath and control](datapath-and-control.md) · [Pipelining](pipelining.md) · [Hazards and branch prediction](hazards-and-branch-prediction.md) · [Superscalar and out-of-order](superscalar-and-out-of-order.md)

## What this area is about

Microarchitecture is how a processor core implements the Instruction Set Architecture (ISA) contract in gates and flip-flops. The question it answers is: given an instruction stream that must *appear* to execute one instruction at a time, how do you finish as many instructions per second as possible? The answer, developed from the 1960s (IBM Stretch, CDC 6600, IBM 360/91) to the mid-1990s and refined ever since, is to exploit **Instruction-Level Parallelism (ILP)**: independent instructions in a single thread can be overlapped, reordered and run side by side, as long as the visible results match sequential execution.

The children form a progression of increasingly aggressive overlap. A single-cycle datapath executes one instruction per long clock cycle. Pipelining overlaps the stages of successive instructions. Hazards and branch prediction deal with the dependences that break that overlap. Superscalar, out-of-order execution removes the remaining artificial limits by issuing several instructions per cycle in dataflow order and committing them in program order. A 2020s high-end core (Apple Firestorm, Intel Golden Cove, AMD Zen 4) decodes four to eight instructions per cycle (more when supplied from a micro-op cache) and keeps 300–600 instructions in flight.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Datapath and control](datapath-and-control.md) | The baseline machine: functional units, registers, wiring, and the control that steers them | ISA, 03 Digital Logic |
| [Pipelining](pipelining.md) | Overlap instructions in stages to raise throughput | Datapath and control |
| [Hazards and branch prediction](hazards-and-branch-prediction.md) | Detect and resolve the dependences that stall a pipeline; guess branch outcomes | Pipelining |
| [Superscalar and out-of-order](superscalar-and-out-of-order.md) | Issue many instructions per cycle, in dataflow order, with speculation and in-order commit | All three above |

```
 single-cycle      pipelined          + prediction        superscalar OoO
 [F D E M W]       F D E M W          F D E M W           F F F F  (wide fetch)
 [F D E M W]         F D E M W          guess -> F D...    rename -> window -> many FUs
                       F D E M W                           -> reorder buffer -> commit in order
 CPI = 1, long     CPI ~1, short      CPI ~1 despite      CPI < 1 (IPC 2-5 typical)
 cycle             cycle              branches
```

Read in order. Each child exists because the previous design leaves performance on the table: the single-cycle machine wastes most of each cycle, pipelining exposes dependences, prediction hides control dependences, and out-of-order execution hides data dependences and memory latency.

## Connections to sibling areas

- **[Instruction Set Architecture](../01-instruction-set-architecture/README.md)**: the specification this area implements. Regular Reduced Instruction Set Computer (RISC) encodings make wide decode cheap; precise exceptions force in-order commit.
- **[Memory Hierarchy](../03-memory-hierarchy/README.md)**: the pipeline's memory stage is only fast if the level-1 (L1) cache hits (about 4–5 cycles on 2020s cores). Out-of-order execution exists largely to keep working while a cache miss (hundreds of cycles to Dynamic Random-Access Memory (DRAM)) is outstanding.
- **[Parallel Architecture](../04-parallel-architecture/README.md)**: when ILP ran out (around 2005), designers replicated whole cores instead of widening one. Simultaneous multithreading reuses an out-of-order core's resources across two threads.
- **[I/O and Interconnect](../05-io-and-interconnect/README.md)**: Input/Output (I/O) interrupts must enter the pipeline at a precise point, which is one more reason for in-order commit.
- **[Performance](../06-performance/README.md)**: every technique here attacks cycles per instruction or clock period in the performance equation, and each pays in power, which the power wall eventually capped.

## Connections across layers

Pipeline stages are combinational logic between registers, so the clock period comes from [timing and power](../../03-digital-logic/04-hardware-design/timing-and-power.md) analysis and [clocking](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md). Upward, [compiler optimization](../../06-programming-languages/03-compilers/optimization.md) schedules instructions to avoid stalls, and [Just-In-Time (JIT) compilers](../../06-programming-languages/04-runtime-systems/jit-compilation.md) tune for specific cores. Speculative execution leaves traces in caches, which is the basis of the Spectre family of [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md).

## Cross-cutting threads

- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): the instruction pipeline is the canonical example.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): branch predictors and micro-op caches are caches of past behaviour.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): register renaming maps architectural names to physical registers.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): in-order commit preserves the invariant that visible state equals some sequential execution.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): deeper pipelines raise frequency but raise misprediction cost and power.
