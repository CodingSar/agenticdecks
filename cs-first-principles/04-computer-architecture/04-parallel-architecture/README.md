# Parallel Architecture

> **Layer:** [04 Computer Architecture](../README.md) › Parallel Architecture
> **Children:** [Multicore and cache coherence](multicore-and-cache-coherence.md) · [Memory consistency models](memory-consistency-models.md) · [SIMD and GPUs](simd-and-gpus.md) · [Domain-specific accelerators](domain-specific-accelerators.md)

## What this area is about

Around 2005, single-core performance growth slowed sharply. Clock frequency stopped rising because power density could no longer be cooled, and Instruction-Level Parallelism (ILP) inside one instruction stream had largely been harvested. Transistor counts kept doubling, so architects spent them on explicit parallelism instead: more cores (multicore), wider vector units (Single Instruction Multiple Data (SIMD)), massively parallel Graphics Processing Units (GPUs), and accelerators specialised for one domain such as neural networks. The question this area answers is how to build machines in which many computations proceed at once, and what the software contract becomes when they share memory.

Two ideas unify the children. First, **parallelism trades generality for efficiency**: a general-purpose core spends most of its energy on fetching, decoding, scheduling and moving data, while a SIMD lane, a GPU thread or a systolic array spends more of it on arithmetic. Second, **shared memory needs rules**: once several processors hold copies of the same data, hardware must keep the copies coherent and the Instruction Set Architecture (ISA) must say in which order writes become visible.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Multicore and cache coherence](multicore-and-cache-coherence.md) | Several cores with private caches that agree on the value of each location | Cache design |
| [Memory consistency models](memory-consistency-models.md) | The contract for the order of memory operations across cores | Multicore and coherence, out-of-order execution |
| [SIMD and GPUs](simd-and-gpus.md) | Data parallelism: one instruction, many data elements; thousands of threads hiding latency | Pipelining, memory hierarchy |
| [Domain-specific accelerators](domain-specific-accelerators.md) | Hardware specialised for one class of computation (Tensor Processing Units (TPUs), codecs, crypto engines) | SIMD and GPUs, power limits |

```
   generality  <-----------------------------------------------------> efficiency (ops/joule)
   out-of-order core   multicore + SIMD      GPU (SIMT)        TPU / fixed-function
   (few fast threads)  (tens of cores)       (thousands of     (one domain,
                                              lanes)            systolic arrays)
```

Read [multicore and cache coherence](multicore-and-cache-coherence.md) and [memory consistency models](memory-consistency-models.md) together: coherence is about one location at a time, consistency about the ordering of all locations. [SIMD and GPUs](simd-and-gpus.md) shows a different style of parallelism, exploiting regular data rather than independent threads. [Domain-specific accelerators](domain-specific-accelerators.md) carries the trend to its end point, trading programmability for one to two orders of magnitude better efficiency on a narrow domain.

## Connections to sibling areas

- **[Instruction Set Architecture](../01-instruction-set-architecture/README.md)**: parallel features enter the contract as atomic instructions, fences, the memory model and vector extensions (x86 Advanced Vector Extensions (AVX-512), ARM Scalable Vector Extension (SVE), RISC-V V).
- **[Processor Microarchitecture](../02-processor-microarchitecture/README.md)**: each core is still an out-of-order engine; its store buffer is the reason weak memory models exist; simultaneous multithreading is parallelism inside one core.
- **[Memory Hierarchy](../03-memory-hierarchy/README.md)**: coherence protocols extend cache design; GPUs and accelerators depend on high-bandwidth memory because their arithmetic outruns any ordinary Dynamic Random-Access Memory (DRAM) interface.
- **[I/O and Interconnect](../05-io-and-interconnect/README.md)**: accelerators are Input/Output (I/O) devices that attach over Peripheral Component Interconnect Express (PCIe) or coherent links (Compute Express Link (CXL), NVIDIA's NVLink); on-chip networks connect cores and cache slices.
- **[Performance](../06-performance/README.md)**: Amdahl's law limits what more cores can deliver; the power wall explains why parallelism became the only path.

## Connections across layers

The physical reason for this area is in [power and the end of scaling](../06-performance/power-and-the-end-of-scaling.md) and [fabrication and scaling](../../00-engineering-foundations/03-semiconductor-devices/fabrication-and-scaling.md). Upward, [threads](../../07-operating-systems/02-process-management/threads.md), [locks](../../07-operating-systems/03-concurrency/locks-and-semaphores.md) and [lock-free synchronization](../../07-operating-systems/03-concurrency/lock-free-synchronization.md) sit directly on coherence, atomics and the memory model; [parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md) such as OpenMP and NVIDIA's Compute Unified Device Architecture (CUDA) target these machines; [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) is built on GPUs and TPUs; [graphics](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md) is where GPUs began.

## Cross-cutting threads

- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): parallelism in space (cores, lanes) replaces speed in time (clock rate).
- [State and time](../../CROSS-CUTTING.md#state-and-time): consistency models define what "before" means for memory shared by cores.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): coherence is the cost of having many caches of one memory.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): generality vs efficiency, latency-optimised Central Processing Units (CPUs) vs throughput-optimised GPUs.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): Amdahl's law and dark silicon bound what parallel hardware can deliver.
