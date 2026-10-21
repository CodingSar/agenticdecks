# Instruction Set Architecture

> **Layer:** [04 Computer Architecture](../README.md) › Instruction Set Architecture
> **Children:** [The ISA contract](the-isa-contract.md) · [RISC vs CISC](risc-vs-cisc.md) · [Instruction encoding and addressing](instruction-encoding-and-addressing.md)

## What this area is about

The Instruction Set Architecture (ISA) is the boundary between hardware and software: the complete list of what a program can observe about a processor. It names the registers, the instructions and their exact effects, how memory is addressed, which data types exist, what privilege levels there are, and what happens when something goes wrong (an exception or interrupt). A binary program is nothing more than a sequence of ISA instructions, so any processor that implements the same ISA runs the same binary.

The unifying idea of this area is that **an ISA is a design for longevity**. Microarchitectures last about five years; successful ISAs last decades (IBM System/360 from 1964, x86 from 1978, ARM from 1985, RISC-V from 2010). Every ISA decision, from how many registers to name to how instructions are encoded as bits, is a bet about what will remain cheap to implement and easy to compile for across many future generations of hardware.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [The ISA contract](the-isa-contract.md) | What an ISA promises and what it leaves free: architectural state, sequential semantics, privilege, exceptions | 03 Digital Logic |
| [RISC vs CISC](risc-vs-cisc.md) | The central design debate: Reduced Instruction Set Computer (RISC) vs Complex Instruction Set Computer (CISC), and why it converged | The ISA contract |
| [Instruction encoding and addressing](instruction-encoding-and-addressing.md) | How instructions become bits, and how operands name registers and memory | The ISA contract, RISC vs CISC |

Read [the ISA contract](the-isa-contract.md) first: it explains the architecture/microarchitecture split that everything else relies on. [RISC vs CISC](risc-vs-cisc.md) then shows the two philosophies for filling in the contract, and why the debate was largely settled by the 1990s once pipelining made instruction regularity decisive and x86 learned to translate its complex instructions into simple internal ones. [Instruction encoding and addressing](instruction-encoding-and-addressing.md) is the concrete layer: the bit layouts and addressing modes that a decoder must parse and a compiler must emit.

```
   source program
        | compiler (06)
        v
   ISA instructions  <-- contract: registers, memory, opcodes, privilege, exceptions
        | decoder
        v
   micro-operations / control signals (microarchitecture, 04.02)
```

## Connections to sibling areas

- **[Processor Microarchitecture](../02-processor-microarchitecture/README.md)**: implements the ISA. ISA choices directly decide how hard that is: fixed-length instructions make wide parallel decode easy, while x86's 1-to-15-byte instructions need predecoders and a micro-op cache.
- **[Memory Hierarchy](../03-memory-hierarchy/README.md)**: the ISA defines the address space and, for privileged software, the page-table format that the Memory Management Unit (MMU) walks. Load/store architectures make every memory access an explicit instruction, which simplifies cache and Translation Lookaside Buffer (TLB) handling.
- **[Parallel Architecture](../04-parallel-architecture/README.md)**: the ISA must specify atomic instructions (compare-and-swap, load-linked/store-conditional), fences, the memory consistency model, and vector or Single Instruction, Multiple Data (SIMD) extensions.
- **[I/O and Interconnect](../05-io-and-interconnect/README.md)**: the ISA defines how devices are reached (memory-mapped Input/Output (I/O) or port I/O instructions) and how interrupts enter the processor.
- **[Performance](../06-performance/README.md)**: the ISA sets instruction count, one of the three factors in the performance equation; compact encodings also affect instruction-cache misses.

## Connections across layers

The ISA is assembled from [03 Digital Logic](../../03-digital-logic/README.md): its integer and floating-point types are exactly the encodings in [two's complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md) and [floating point](../../03-digital-logic/01-number-representation/floating-point.md). Upward, it is the target language of [code generation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md), the format that [linkers and loaders](../../06-programming-languages/04-runtime-systems/linking-and-loading.md) manipulate, and the source of the privileged features behind [kernel mode and system calls](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md). Virtual machines such as the Java Virtual Machine and WebAssembly are software ISAs that reuse the same idea one level up ([interpreters and virtual machines](../../06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md)).

## Cross-cutting threads

- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): the ISA is the interface; each processor generation is an implementation.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): software is written once against the ISA and runs on every compatible chip.
- [Encoding and representation](../../CROSS-CUTTING.md#encoding-and-representation): fixed vs variable instruction length trades decode simplicity against code density.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): compatibility forever vs freedom to remove past mistakes.
