# SIMD and GPUs

> **Layer:** [04 Computer Architecture](../README.md) › [Parallel Architecture](README.md)
> **Builds on:** [Pipelining](../02-processor-microarchitecture/pipelining.md), [Locality and caching](../03-memory-hierarchy/locality-and-caching.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md), [Floating point](../../03-digital-logic/01-number-representation/floating-point.md)
> **Enables:** [Data and task parallelism](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md), [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), [Rasterization pipeline](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md), [Domain-specific accelerators](domain-specific-accelerators.md)

## Essence

Single Instruction, Multiple Data (SIMD) execution applies one instruction to many data elements at once: one fetch, decode and scheduling decision drives 4, 8, 16 or more arithmetic lanes. CPUs add SIMD as wide vector registers (x86 SSE, AVX, AVX-512; ARM NEON and SVE; RISC-V V). Graphics Processing Units (GPUs) take the idea to the extreme: thousands of simple lanes organised as groups of 32 or 64 threads executing in lockstep, with so many threads resident that whenever one group waits for memory, another is ready to run. The CPU optimises latency for a few threads; the GPU optimises throughput for many. That choice made GPUs the engine of graphics, scientific computing and deep learning.

## Core tenets

1. **SIMD amortises control over many data elements.** In an out-of-order core, most energy goes to fetching, decoding, renaming and scheduling, not to the arithmetic itself. A 512-bit AVX-512 instruction performs sixteen 32-bit floating-point operations for roughly the control cost of one, so operations per joule rise sharply. The price is that the work must be regular: the same operation applied across contiguous data.

2. **Flynn's taxonomy names the space.** Flynn (1966) classified machines by instruction and data streams: Single Instruction Single Data (SISD, a classic core), SIMD (vector units, array processors), Multiple Instruction Multiple Data (MIMD, multicore), and the rarely built MISD. GPUs are best described by NVIDIA's term Single Instruction, Multiple Threads (SIMT): a SIMD machine whose lanes are presented to the programmer as independent threads.

3. **GPUs hide latency with parallelism instead of caches and speculation.** A CPU core spends area on large caches, branch predictors and out-of-order windows to make one thread fast. A GPU streaming multiprocessor instead holds dozens of warps (groups of 32 threads on NVIDIA; wavefronts of 32 or 64 on AMD) with their registers resident, and switches between them every cycle at no cost. While one warp waits 400–800 cycles for memory, others compute. This requires enormous register files (256 KiB per streaming multiprocessor on recent NVIDIA designs) and enough parallel work to fill them.

4. **Branch divergence is the cost of lockstep.** All threads in a warp share one instruction stream. If they take different sides of an `if`, the hardware runs both paths with lanes masked off, so a warp split evenly runs at half speed. GPU code performs best when neighbouring threads follow the same control path.

5. **Memory coalescing and bandwidth decide performance.** When the 32 threads of a warp access 32 consecutive words, the hardware combines them into a few wide memory transactions; scattered accesses waste bandwidth. GPUs pair this with very high-bandwidth memory: about 1 TB/s on 2020-era cards, and 3–8 TB/s with stacked High Bandwidth Memory (HBM) on 2023–2025 data-centre accelerators such as NVIDIA H100 and B200. Many GPU workloads are limited by bandwidth, not arithmetic.

6. **Scale comes from simple cores, many of them.** A 2022 NVIDIA H100 has 132 streaming multiprocessors and over 16,000 FP32 lanes, delivering about 60 TFLOP/s in FP32 and around 1,000 TFLOP/s in dense FP16 on its tensor cores, against a peak of a few to about 10 TFLOP/s FP32 for a contemporary high-end server CPU. Each GPU lane is far slower than a CPU core on serial code; the advantage exists only when there are tens of thousands of independent operations.

7. **GPUs grew from fixed-function graphics to general purpose.** Early GPUs (late 1990s) were hardwired triangle pipelines. Programmable shaders (around 2001) and unified shader architectures (NVIDIA G80 and CUDA, 2006–2007) turned them into general data-parallel processors. Since 2017 (NVIDIA Volta), GPUs also include tensor cores: units that perform small matrix multiplies per instruction, blending SIMD with domain-specific acceleration.

8. **Vectorisation is a compiler and programmer problem.** Compilers auto-vectorise simple loops, but aliasing, unknown trip counts and irregular control often defeat them. Data layout matters: a structure of arrays lets a loop load contiguous lanes, while an array of structures forces gathers. Scalable vector ISAs (ARM SVE, RISC-V V) let one binary run on hardware of different vector widths.

## Key concepts

| Term | Meaning |
|---|---|
| SIMD | One instruction operating on multiple data elements in parallel lanes |
| Vector register | Wide register holding several elements (128 to 512 bits on CPUs; scalable on SVE and RISC-V V) |
| SIMT | Single Instruction, Multiple Threads: GPU model of lockstep threads in a warp |
| Warp / wavefront | Group of 32 (or 64) GPU threads that execute the same instruction together |
| Streaming multiprocessor | GPU core containing many lanes, a large register file and shared memory |
| Divergence | Threads in a warp following different control paths, serialising execution |
| Coalescing | Merging a warp's memory accesses to adjacent addresses into few transactions |
| Occupancy | Fraction of the maximum resident warps actually active, which determines latency hiding |
| Tensor core | GPU unit that executes small dense matrix multiply-accumulates per instruction |

## How it fits

- **Below:** lanes are pipelined [floating-point](../../03-digital-logic/01-number-representation/floating-point.md) units; the workloads are [linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md); the design depends on the [memory hierarchy](../03-memory-hierarchy/locality-and-caching.md) and on high-bandwidth DRAM.
- **Above:** [data parallelism](../../10-distributed-and-parallel-computing/01-parallel-computing/data-and-task-parallelism.md) and [parallel programming models](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md) (CUDA, OpenCL, SIMD intrinsics) target these machines; [neural network training](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) and the [graphics rasterization pipeline](../../14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md) run on GPUs.
- **Siblings:** contrasts with [multicore](multicore-and-cache-coherence.md) MIMD parallelism; [domain-specific accelerators](domain-specific-accelerators.md) push specialisation further; GPUs use weak, scoped [memory models](memory-consistency-models.md).

## Common misconceptions

- **"GPUs are faster processors."** Each GPU thread is much slower than a CPU thread; GPUs win only on throughput for massively parallel, regular work.
- **"A GPU has thousands of cores."** Marketing counts lanes as "cores"; architecturally a GPU has tens to about a hundred-odd streaming multiprocessors, each a wide SIMD engine.
- **"Moving work to the GPU always helps."** Copying data over the host interface and launching kernels has overhead; small or branchy workloads often run faster on the CPU.

## Go deeper

- Flynn, *Very High-Speed Computing Systems* (Proceedings of the IEEE, 1966): the origin of SISD/SIMD/MIMD.
- Lindholm et al., *NVIDIA Tesla: A Unified Graphics and Computing Architecture* (IEEE Micro, 2008): the architecture that made GPUs general purpose.
- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Chapter 4: vector, SIMD and GPU architectures compared.
- Kirk and Hwu, *Programming Massively Parallel Processors* (4th ed., 2022): how GPU architecture shapes GPU programs.
