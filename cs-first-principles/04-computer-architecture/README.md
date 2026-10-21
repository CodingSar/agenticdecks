# 04 Computer Architecture

> **Layer:** 04 Computer Architecture
> **Children:** [Instruction Set Architecture](01-instruction-set-architecture/README.md) · [Processor Microarchitecture](02-processor-microarchitecture/README.md) · [Memory Hierarchy](03-memory-hierarchy/README.md) · [Parallel Architecture](04-parallel-architecture/README.md) · [I/O and Interconnect](05-io-and-interconnect/README.md) · [Performance](06-performance/README.md)

## What this area is about

Computer architecture answers one question: how do you turn a pile of gates and flip-flops into a machine that runs *any* program fast, and keep running the same programs as the hardware underneath changes every two years? The answer is a contract. The Instruction Set Architecture (ISA) defines what a program can see: registers, memory, instructions, privilege levels, and what happens on an exception. Everything below the ISA (pipelines, caches, branch predictors, out-of-order engines) is *implementation*, free to change as long as the contract holds. Everything above it (compilers, operating systems, every application) is written against the contract and never needs to know which implementation runs it.

The second half of the story is that the contract hides a brutal physical reality. A Central Processing Unit (CPU) core can start several instructions per nanosecond, but a trip to main memory takes about 100 ns (2020s hardware), and since about 2005 the power budget, not the transistor budget, limits clock speed. Almost every idea in this layer (pipelining, caching, speculation, multicore, Single Instruction Multiple Data (SIMD), accelerators) is a way to keep the illusion of a simple, sequential, uniformly fast machine while the real machine is parallel, speculative and dominated by data movement.

## Why this layer sits here

**What it needs from below.** Architecture is built from [03 Digital Logic](../03-digital-logic/README.md): combinational blocks (adders, multiplexers, decoders) form the datapath, flip-flops and clocking form registers and pipeline stages, [memory cells](../03-digital-logic/03-sequential-logic/memory-cells.md) form caches, main memory and flash storage, finite-state machines form control, and the number encodings (two's complement, Institute of Electrical and Electronics Engineers (IEEE) 754 floating point) fix what arithmetic instructions mean. From [00 Engineering Foundations](../00-engineering-foundations/README.md) it inherits the physical limits that shape every design decision: wire delay, the energy of switching a capacitor, heat removal, and the end of Dennard scaling. From [02 Theory of Computation](../02-theory-of-computation/README.md) it takes the stored-program idea: a [Turing machine](../02-theory-of-computation/03-computability/turing-machines.md) whose program is just data on its tape is the logical ancestor of the von Neumann machine.

**What the layers above need from it.** The ISA is the central hardware/software contract of the whole stack:

- [05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md) analyses programs on the Random Access Machine (RAM) model, an idealised ISA with unit-cost memory access and word-sized arithmetic. The memory hierarchy explains when that model lies, which is why cache-aware and external-memory algorithms exist.
- [06 Programming Languages](../06-programming-languages/README.md) needs a target. Compilers lower source code to ISA instructions, allocate the ISA's registers, and obey its calling conventions and memory model.
- [07 Operating Systems](../07-operating-systems/README.md) is built on mechanisms only hardware can provide: privilege modes (user vs kernel), the Memory Management Unit (MMU) for address translation and protection, interrupts and exceptions for regaining control, and atomic instructions for synchronisation. An Operating System (OS) cannot enforce isolation that the ISA does not support.

The single abstraction this layer contributes is **the sequential execution of an instruction stream over a flat, protected address space**: each instruction appears to finish before the next begins, and each load returns the last value stored. Every other layer stands on that illusion.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Instruction Set Architecture](01-instruction-set-architecture/README.md) | Defines the contract: what software sees | 03 Digital Logic |
| [Processor Microarchitecture](02-processor-microarchitecture/README.md) | Implements the contract fast: datapath, pipelining, speculation | ISA |
| [Memory Hierarchy](03-memory-hierarchy/README.md) | Makes memory look large and fast: caches, virtual memory, Dynamic Random-Access Memory (DRAM) | ISA, microarchitecture |
| [Parallel Architecture](04-parallel-architecture/README.md) | Many cores, vector units, Graphics Processing Units (GPUs), accelerators, and what shared memory means | All three above |
| [I/O and Interconnect](05-io-and-interconnect/README.md) | Input/Output (I/O): connects the processor to devices and the outside world | ISA (interrupts), memory hierarchy (Direct Memory Access (DMA)) |
| [Performance](06-performance/README.md) | The quantitative laws that judge every design choice | All of the above |

```
              software (05, 06, 07 ...)
  ============== ISA contract ==============
   microarchitecture  <->  memory hierarchy  <->  I/O
            \               |               /
             parallel architecture (many of the above)
                 judged by: performance laws
  ==========================================
              digital logic (03)
```

Read the ISA first, because it states what must be preserved. Microarchitecture then shows how a single core preserves it while overlapping and reordering work. The memory hierarchy is the other half of single-core performance: most cycles in real programs are spent waiting for data. Parallel architecture follows, because it multiplies cores and must then define what "the last value stored" means when several cores store. I/O closes the machine to the outside world. Performance can be read first as motivation or last as a summary; its three laws (the performance equation, Amdahl's law, and the power wall) explain why the field moved from faster single cores (1980–2005) to multicore, GPUs and domain-specific accelerators (2005 onwards).

## Connections to neighbouring layers

- **[03 Digital Logic](../03-digital-logic/README.md)**: the raw material. A pipeline stage is combinational logic between two banks of flip-flops; the clock period is set by the slowest stage's critical path.
- **[00 Engineering Foundations](../00-engineering-foundations/README.md)**: power density and wire delay set the rules. The end of Dennard scaling (around 2005) is the single biggest force on modern architecture.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md)**: the RAM model abstracts this layer; [external-memory and cache-oblivious algorithms](../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md) restore the costs it hides.
- **[06 Programming Languages](../06-programming-languages/README.md)**: compilers schedule instructions around pipeline hazards, allocate registers, vectorise loops, and insert fences required by the memory model.
- **[07 Operating Systems](../07-operating-systems/README.md)**: the OS is the main client of privileged ISA features: page tables, Translation Lookaside Buffers (TLBs), interrupts, timers, and virtualisation extensions.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md)**: parallel programming models sit directly on multicore, coherence and consistency; a cluster is many of this layer's machines joined by a network.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md)**: hardware provides isolation (privilege rings, page permissions) and also leaks through it ([side channels](../11-security-and-cryptography/03-system-security/side-channels.md) such as Spectre exploit speculation and caches).
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md)**: modern deep learning exists at its current scale because GPUs and Tensor Processing Units (TPUs) made dense matrix arithmetic cheap.

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the ISA is the textbook example of an interface that has outlived dozens of implementations (x86 code from 1978 still runs).
- [Interface vs implementation](../CROSS-CUTTING.md#interface-vs-implementation): architecture (ISA) vs microarchitecture is where the distinction was first named, by the IBM System/360 team in 1964.
- [Caching and locality](../CROSS-CUTTING.md#caching-and-locality): register file, level-1/2/3 (L1/L2/L3) caches, TLBs, branch predictors and DRAM row buffers are all caches.
- [Pipelining and parallelism](../CROSS-CUTTING.md#pipelining-and-parallelism): instruction pipelines, superscalar issue, SIMD, multicore and GPUs.
- [Indirection and naming](../CROSS-CUTTING.md#indirection-and-naming): virtual addresses are names resolved by page tables; register renaming resolves architectural names to physical registers.
- [State and time](../CROSS-CUTTING.md#state-and-time): memory consistency models define the order in which stores from different cores become visible.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): the memory wall, the power wall and Amdahl's law.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): latency vs throughput (CPU vs GPU), generality vs efficiency (CPU vs accelerator).
- [Virtualization](../CROSS-CUTTING.md#virtualization): virtual memory gives every process its own address space; hardware virtualisation extensions let one machine look like many.
