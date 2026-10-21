# Datapath and Control

> **Layer:** [04 Computer Architecture](../README.md) › [Processor Microarchitecture](README.md)
> **Builds on:** [Arithmetic and building blocks](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md), [Latches and flip-flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md), [Finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md), [The ISA contract](../01-instruction-set-architecture/the-isa-contract.md)
> **Enables:** [Pipelining](pipelining.md), [The performance equation](../06-performance/the-performance-equation.md)

## Essence

A processor core divides into two parts. The **datapath** holds and transforms data: the register file, the Arithmetic Logic Unit (ALU), adders for addresses, memory interfaces and the multiplexers and wires between them. The **control** decides, for each instruction, which paths through the datapath are active: which registers are read, which ALU operation runs, whether memory is read or written, and where the result goes. Executing an instruction means the control unit decodes its bits into a set of control signals that configure the datapath for one operation. Every faster design, from pipelines to out-of-order cores, is this same split with more overlap.

## Core tenets

1. **Every instruction follows the same five steps.** Fetch the instruction at the Program Counter (PC); decode it and read source registers; execute (ALU operation or address calculation); access memory (for loads and stores); write the result back to a register. Designing the datapath means providing hardware for each step and multiplexers where instructions differ (for example, the second ALU input is a register for `add` and an immediate for `addi`).

2. **The datapath is combinational logic between state elements.** State lives in the PC, the register file and memory, all clocked. Between them is combinational logic whose outputs settle some time after the inputs change. In a single-cycle design, one clock edge latches the results of a whole instruction, so the clock period must cover the slowest instruction's full path (usually a load: fetch, decode, register read, address add, memory read, write-back).

3. **Control is a function from instruction bits to signals.** In a simple RISC core, control is combinational: the opcode and function fields map to signals such as `RegWrite`, `MemRead`, `ALUSrc` and `ALUOp`. Regular encodings make this table small. In a multi-cycle design, control becomes a finite-state machine that steps through the phases of each instruction, reusing the same ALU in different cycles.

4. **Hardwired and microcoded control are two implementations of the same function.** Hardwired control builds the decode table directly in gates: fast, but hard to change. Microcoded control stores a small program per instruction in a Read-Only Memory (ROM), which made complex Complex Instruction Set Computer (CISC) instructions practical (IBM System/360, 1964). Modern x86 cores hardwire the common instructions into simple micro-operations and keep a microcode ROM for rare, complex ones, such as string operations and some system instructions; microcode can also be patched after shipping to fix bugs.

5. **The register file is a small, many-ported memory.** A three-operand instruction needs two reads and one write per cycle. A core that issues six instructions per cycle needs roughly twelve read ports and six write ports, and register-file area and energy grow roughly with the square of the port count. This physical cost is one of the reasons cores cannot simply be made arbitrarily wide.

6. **Single-cycle is simple but wasteful.** Because the clock must fit the slowest instruction, a fast instruction like `add` idles most of the cycle. Multi-cycle designs give each instruction only as many short cycles as it needs. Pipelining goes further: it keeps every part of the datapath busy with a different instruction in every cycle.

## Key concepts

| Term | Meaning |
|---|---|
| Datapath | Hardware that stores and transforms data: registers, ALU, memory ports, multiplexers |
| Control unit | Logic that turns instruction bits into datapath control signals |
| ALU | Combinational block performing integer arithmetic and logic on two operands |
| Register file | Array of architectural (or physical) registers with several read and write ports |
| Control signal | Single wire or field selecting a datapath behaviour, such as a multiplexer input or write enable |
| Critical path | Longest combinational delay between two state elements; sets the minimum clock period |
| Microcode | Stored sequence of control words implementing a complex instruction |
| Multi-cycle datapath | Design in which each instruction takes several short cycles and shares hardware across them |

## How it fits

- **Below:** the ALU is built from [adders and multiplexers](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md); registers are [flip-flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md); multi-cycle control is a [finite-state machine](../../03-digital-logic/03-sequential-logic/finite-state-machines.md); the clock period comes from [timing analysis](../../03-digital-logic/04-hardware-design/timing-and-power.md). The core is described in a [hardware description language](../../03-digital-logic/04-hardware-design/hardware-description-languages.md).
- **Above:** what the datapath must do is fixed by [the ISA contract](../01-instruction-set-architecture/the-isa-contract.md) and [instruction encoding](../01-instruction-set-architecture/instruction-encoding-and-addressing.md); its clock period and cycles per instruction feed the [performance equation](../06-performance/the-performance-equation.md).
- **Siblings:** [pipelining](pipelining.md) cuts this datapath into stages; [hazards](hazards-and-branch-prediction.md) arise from sharing it among overlapping instructions; [out-of-order cores](superscalar-and-out-of-order.md) replicate its functional units.

## Common misconceptions

- **"The CPU executes the instruction's text."** The Central Processing Unit (CPU) only ever sees bits; decode turns those bits into dozens of control wires, and the "meaning" of an instruction is exactly which wires go high.
- **"Microcode means a slow processor."** Microcode handles only rare complex instructions in modern x86 cores; common instructions are decoded directly into micro-operations by hardwired decoders.
- **"A wider core is just more ALUs."** ALUs are cheap; the register-file ports, bypass network and scheduling logic needed to feed them grow faster than linearly and dominate the cost.

## Go deeper

- Patterson and Hennessy, *Computer Organization and Design* (RISC-V edition, 2017), Chapter 4: builds a single-cycle and pipelined RISC-V datapath step by step.
- Harris and Harris, *Digital Design and Computer Architecture* (RISC-V edition, 2021): goes from gates to a working processor in a hardware description language.
- Nisan and Schocken, *The Elements of Computing Systems* (2nd ed., 2021): build a complete simple CPU yourself, from NAND gates up.
