# RISC vs CISC

> **Layer:** [04 Computer Architecture](../README.md) › [Instruction Set Architecture](README.md)
> **Builds on:** [The ISA contract](the-isa-contract.md), [Logic minimization](../../03-digital-logic/02-combinational-logic/logic-minimization.md)
> **Enables:** [Pipelining](../02-processor-microarchitecture/pipelining.md), [Superscalar and out-of-order execution](../02-processor-microarchitecture/superscalar-and-out-of-order.md), [Compiler optimization](../../06-programming-languages/03-compilers/optimization.md)

## Essence

Reduced Instruction Set Computer (RISC) and Complex Instruction Set Computer (CISC) are two philosophies for what to put in an Instruction Set Architecture (ISA). CISC (VAX, x86, IBM System/360) offers many instructions that do a lot each, with memory operands and variable-length encodings, because in the 1960s–70s memory was expensive and much code was written by hand. RISC (MIPS, SPARC, ARM, RISC-V) offers fewer, simpler, fixed-length instructions in which only loads and stores touch memory, because by 1980 compilers wrote most code and a simple, regular ISA could be pipelined to complete roughly one instruction per cycle. The debate largely ended in convergence: modern x86 cores translate CISC instructions into RISC-like micro-operations internally, and the remaining differences are mostly in decode cost, code density and energy.

## Core tenets

1. **CISC was a rational answer to 1970s constraints.** Main memory was small and slow, and instruction fetch competed with data for it, so dense code mattered. Microcode (a small internal program per instruction, stored in Read-Only Memory (ROM)) made complex instructions cheap to add. The VAX had instructions for polynomial evaluation and string copy; x86 has `rep movsb` and instructions with memory source and destination.

2. **RISC came from measuring what compilers actually used.** Studies in the late 1970s and early 1980s (the IBM 801 project, Berkeley RISC, Stanford MIPS) found that compilers emitted mostly simple loads, stores, adds and branches, and rarely used the complex instructions. Spending chip area and design effort on rare instructions slowed the common ones. Moving complexity into the compiler, which runs once, beat moving it into hardware, which pays on every execution.

3. **Regularity is what makes pipelining easy.** If every instruction is 32 bits, has register fields in fixed positions, and touches memory in at most one stage, then fetch, decode, register read, execute and write-back can each take one stage of a pipeline. Variable-length instructions with optional memory operands make it hard to even find where the next instruction begins, and an instruction that can fault halfway through a memory-to-memory operation complicates precise exceptions.

4. **Load/store architecture plus many registers is the core RISC idea.** Arithmetic operates only on registers; memory is reached only by explicit loads and stores. With 32 registers (MIPS, RISC-V; 31 on ARMv8), compilers keep most hot values in registers and the separation lets the pipeline treat memory access as one well-defined stage. 32-bit x86 had only 8 general-purpose registers, which forced frequent spills to memory; x86-64 (2003) raised it to 16 and Intel's Advanced Performance Extensions announced in 2023 raise it to 32.

5. **The performance equation frames the tradeoff.** Time = instructions × cycles per instruction × seconds per cycle. CISC lowers instruction count; RISC lowers cycles per instruction and makes short cycles easier. Neither wins on one factor alone; what matters is the product, and pipelining made the second and third factors dominant.

6. **Translation made the debate mostly moot for performance.** Since the Intel P6 (Pentium Pro, 1995), x86 cores decode each instruction into one or more internal micro-operations that look like RISC instructions, then pipeline and reorder those. The CISC ISA remains for compatibility, while the execution engine is RISC-like. The cost is a complex front end: length decoding, multiple decoders and a micro-op cache that avoids re-decoding hot code.

7. **What remains different is decode cost, code density and ecosystem.** Variable-length x86 encoding gives good density but costs decode energy and limits decode width. Fixed-length RISC is easy to decode eight-wide (Apple's M1 cores decode eight instructions per cycle) but less dense, which compressed extensions recover (ARM Thumb, RISC-V C with 16-bit forms). In practice, ISA choice today is driven more by licensing, software ecosystem and power targets than by RISC vs CISC purity.

## Key concepts

| Term | Meaning |
|---|---|
| RISC | ISA style with simple, fixed-length instructions, load/store memory access and many registers |
| CISC | ISA style with many complex, variable-length instructions, often with memory operands |
| Load/store architecture | Only load and store instructions access memory; arithmetic uses registers |
| Microcode | Internal sequence of control steps that implements a complex instruction |
| Micro-operation (micro-op, µop) | Simple internal operation into which a modern core decodes an ISA instruction |
| Code density | Bytes of instructions needed for a given program; affects instruction-cache and memory footprint |
| Orthogonality | Any instruction can use any register or addressing mode, simplifying compilers |
| Compressed instructions | Short (16-bit) encodings of common instructions to recover density in a RISC ISA |

## How it fits

- **Below:** microcode is a [finite-state machine](../../03-digital-logic/03-sequential-logic/finite-state-machines.md) stored in ROM; hardwired RISC control is combinational logic that [logic minimization](../../03-digital-logic/02-combinational-logic/logic-minimization.md) keeps small.
- **Above:** RISC shifted work to [compiler optimization](../../06-programming-languages/03-compilers/optimization.md) and [register allocation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md). It also made [pipelining](../02-processor-microarchitecture/pipelining.md) straightforward and paved the way for [superscalar](../02-processor-microarchitecture/superscalar-and-out-of-order.md) cores.
- **Siblings:** [the ISA contract](the-isa-contract.md) says what any ISA must define; [instruction encoding](instruction-encoding-and-addressing.md) shows the concrete formats that make RISC easy and x86 hard to decode.

## Common misconceptions

- **"RISC means fewer instructions."** It means *simpler* instructions. ARMv8 and RISC-V with extensions have hundreds of instructions; the point is that each is regular and does a bounded amount of work.
- **"x86 is slow because it is CISC."** Modern x86 cores match or beat contemporary RISC cores in single-thread performance; the CISC tax is real but mostly a few percent of area and power in the front end.
- **"ARM won phones because RISC is inherently low-power."** Licensing, a design culture aimed at low power, and the ecosystem mattered at least as much; the ISA's share of total chip power is small.

## Go deeper

- Patterson and Ditzel, *The Case for the Reduced Instruction Set Computer* (1980): the short paper that started the debate.
- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Appendix A: instruction set principles with measured data.
- Radin, *The 801 Minicomputer* (1982): IBM's first RISC design and its compiler-driven rationale.
