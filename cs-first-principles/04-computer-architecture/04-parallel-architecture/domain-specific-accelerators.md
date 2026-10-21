# Domain-Specific Accelerators

> **Layer:** [04 Computer Architecture](../README.md) › [Parallel Architecture](README.md)
> **Builds on:** [SIMD and GPUs](simd-and-gpus.md), [Power and the end of scaling](../06-performance/power-and-the-end-of-scaling.md), [FPGA and ASIC](../../03-digital-logic/04-hardware-design/fpga-and-asic.md), [Linear algebra](../../01-mathematical-foundations/04-algebra/linear-algebra.md)
> **Enables:** [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), [Large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md), [Digital media and compression](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md), [Symmetric encryption](../../11-security-and-cryptography/02-cryptography/symmetric-encryption.md)

## Essence

A domain-specific accelerator is hardware designed for one class of computation, such as neural-network inference, video encoding or encryption, rather than for arbitrary programs. When general-purpose performance stopped improving quickly (from the late 2000s), and power rather than transistors became the limit, specialisation became the main way to get more work per joule: removing the overhead of instruction fetch, decode, speculation and general caches can improve efficiency by 10 to 1,000 times on the target workload. The canonical modern example is Google's Tensor Processing Unit (TPU), whose systolic matrix unit performs tens of thousands of multiply-accumulates per cycle. The price is narrowness: an accelerator is only valuable while its domain is important and its algorithms are stable enough to freeze into silicon.

## Core tenets

1. **General-purpose cores spend most energy on overhead.** On a 45 nm process, Horowitz (2014) estimated that a 32-bit integer add costs about 0.1 pJ and a 32-bit floating-point multiply about 4 pJ, while a 64-bit read costs about 10 pJ from an 8 KiB SRAM, about 100 pJ from a 1 MiB SRAM and over 1,000 pJ from DRAM. A whole instruction on an out-of-order core costs on the order of 100 times more energy than the arithmetic it performs. Accelerators win by doing more arithmetic per instruction and per byte moved.

2. **Specialisation exploits structure the general machine cannot assume.** Dense neural-network layers are matrix multiplies with known shapes and massive reuse of each weight and activation. An accelerator can use lower precision (8-bit integers, 16-bit bfloat16, even 4-bit formats), fixed dataflow, software-managed scratchpad memories instead of caches, and no branch prediction at all. Each removed generality saves area and energy.

3. **Systolic arrays maximise reuse of each operand.** A systolic array (Kung and Leiserson, late 1970s) is a grid of multiply-accumulate cells in which data flows rhythmically from neighbour to neighbour. Each value read from memory is used by many cells as it passes through, so arithmetic per memory access is high. The first TPU (deployed 2015, described 2017) used a 256 × 256 array of 8-bit multiply-accumulate units, 65,536 per cycle, and reported roughly 15–30 times the performance and 30–80 times the performance per watt of contemporary CPUs and GPUs on Google's inference workloads.

4. **Memory bandwidth and data movement remain the bottleneck.** Arithmetic is cheap; feeding it is not. Accelerators therefore surround compute units with large on-chip buffers and attach High Bandwidth Memory (HBM) stacks. Algorithms are restructured to increase arithmetic intensity (operations per byte), which the roofline model makes explicit.

5. **The spectrum runs from programmable to fixed-function.** Field-Programmable Gate Arrays (FPGAs) can be reconfigured after manufacture and suit changing workloads (Microsoft deployed them in Azure for networking and search). Application-Specific Integrated Circuits (ASICs) are faster and more efficient but fixed once fabricated, and cost tens of millions of dollars to design at leading-edge nodes. GPUs with tensor cores sit between general-purpose and fixed-function; Apple's Neural Engine, video codec blocks and crypto engines are close to fixed-function.

6. **Accelerators are everywhere already, often invisibly.** A 2020s phone System-on-Chip (SoC) contains CPU cores plus a GPU, a neural processing unit, an image signal processor, video encoders and decoders, and security processors. Instruction-set extensions are small accelerators too: x86 AES-NI (2010) and ARMv8 cryptography instructions run an Advanced Encryption Standard (AES) round in a few cycles.

7. **The software stack is the hard part.** An accelerator needs compilers, libraries and frameworks before anyone can use it. NVIDIA's lead in machine learning owes as much to CUDA and its libraries (from 2007) as to its hardware. Successful accelerators expose a narrow, high-level interface (matrix multiply, a compiler such as XLA for TPUs) that matches how the domain's programmers already think.

8. **Specialise only where the domain is large and stable.** Designing an ASIC takes years. If the algorithm changes faster than the chip can be built, or the market is small, the general-purpose machine wins. Hennessy and Patterson's 2017 Turing lecture argued that, with Moore's law and Dennard scaling fading, domain-specific architectures are the main remaining path to large gains, which the scale of deep learning has borne out.

## Key concepts

| Term | Meaning |
|---|---|
| Domain-Specific Architecture (DSA) | Processor tailored to one application domain |
| TPU | Tensor Processing Unit: Google's neural-network accelerator built around a systolic matrix unit |
| Systolic array | Grid of processing elements passing data to neighbours each cycle, reusing operands |
| Arithmetic intensity | Operations performed per byte moved from memory |
| Scratchpad memory | Software-managed on-chip memory, used instead of a hardware-managed cache |
| Reduced precision | Using 16-, 8- or 4-bit number formats to save energy, area and bandwidth |
| FPGA | Field-Programmable Gate Array: reconfigurable hardware |
| ASIC | Application-Specific Integrated Circuit: fixed custom chip |
| Dark silicon | Transistors that cannot all be powered at once, making specialised blocks attractive |

## How it fits

- **Below:** accelerators are realised as [FPGAs or ASICs](../../03-digital-logic/04-hardware-design/fpga-and-asic.md); their reduced-precision formats extend [floating point](../../03-digital-logic/01-number-representation/floating-point.md); their motivation is [the end of scaling](../06-performance/power-and-the-end-of-scaling.md).
- **Above:** [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) and [large language models](../../13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) depend on them; [media codecs](../../14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) and [encryption](../../11-security-and-cryptography/02-cryptography/symmetric-encryption.md) use fixed-function blocks; [JIT and domain compilers](../../06-programming-languages/04-runtime-systems/jit-compilation.md) map high-level operations onto them.
- **Siblings:** the end point of the trend that runs from [multicore](multicore-and-cache-coherence.md) through [SIMD and GPUs](simd-and-gpus.md); attached through [I/O and interconnect](../05-io-and-interconnect/README.md).

## Common misconceptions

- **"Accelerators are just faster CPUs."** They are faster only on their domain; most cannot run an operating system or arbitrary code at all.
- **"The arithmetic units are what make them efficient."** The gains come mostly from removing control overhead and reducing data movement, not from better multipliers.
- **"Specialisation is new."** Floating-point coprocessors (Intel 8087, 1980), graphics chips and digital signal processors are decades old; what is new is that specialisation became the main source of improvement.

## Go deeper

- Jouppi et al., *In-Datacenter Performance Analysis of a Tensor Processing Unit* (ISCA 2017): the first TPU, with measured comparisons.
- Hennessy and Patterson, *A New Golden Age for Computer Architecture* (Communications of the ACM, 2019): the case for domain-specific architectures.
- Kung, *Why Systolic Architectures?* (IEEE Computer, 1982): the original argument for systolic arrays.
- Horowitz, *Computing's Energy Problem (and What We Can Do About It)* (ISSCC 2014): the energy numbers behind specialisation.
