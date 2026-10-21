# Instruction Encoding and Addressing

> **Layer:** [04 Computer Architecture](../README.md) › [Instruction Set Architecture](README.md)
> **Builds on:** [Binary and positional notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md), [Arithmetic and building blocks](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md), [The ISA contract](the-isa-contract.md)
> **Enables:** [Datapath and control](../02-processor-microarchitecture/datapath-and-control.md), [Code generation and register allocation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md), [Linking and loading](../../06-programming-languages/04-runtime-systems/linking-and-loading.md)

## Essence

Every instruction must be written as a string of bits that a decoder can turn into control signals, and every operand must be named: a register number, a constant embedded in the instruction (an immediate), or a memory address computed from registers and constants. The encoding decides how many registers an Instruction Set Architecture (ISA) can name, how large a constant fits in one instruction, how far a branch can jump, and how hard it is to decode many instructions per cycle. Addressing modes decide how arrays, structures, stack frames and position-independent code are reached. These choices are small in bits but large in consequence, because they are frozen for the life of the ISA.

## Core tenets

1. **Field widths are a budget.** A 32-bit RISC-V instruction spends 7 bits on the opcode, 5 bits for each register specifier (hence 32 registers), and the rest on function codes or immediates. Naming 64 registers would need 6 bits per field and 18 bits for a three-operand instruction, squeezing the opcode and immediate space. This is why most Reduced Instruction Set Computer (RISC) ISAs settled on 32 registers and three operands (`add rd, rs1, rs2`).

2. **Fixed-length encodings make decode simple and parallel.** With 32-bit instructions, the n-th instruction in a fetch block starts at byte 4n, so a decoder can split a 32-byte block into eight instructions at once. x86 instructions range from 1 to 15 bytes, built from optional prefixes, opcode bytes, a ModR/M byte, a Scale-Index-Base (SIB) byte, a displacement and an immediate; finding instruction boundaries is serial unless the hardware guesses at every byte offset or caches predecoded results.

3. **Immediates trade range for space.** A 32-bit instruction cannot contain a 32-bit constant and anything else, so RISC ISAs give 12- to 16-bit immediates and build larger constants in two steps (RISC-V `lui` loads the upper 20 bits, then `addi` adds the lower 12). Most constants in real code are small, so the common case costs one instruction. x86, with variable length, simply embeds a full 32-bit or 64-bit immediate.

4. **Addressing modes map directly to data structures.** Register-plus-displacement (`ld x5, 16(x10)`) reaches a field of a structure or a local variable in a stack frame. Base-plus-scaled-index (x86 `[rbx + rcx*8 + 16]`) reaches element `i` of an array of 8-byte values in one instruction. Program Counter (PC)-relative addressing reaches code and constants at a fixed distance from the current instruction, which is what makes position-independent code and shared libraries work without rewriting addresses at load time. RISC ISAs keep few modes and compute other addresses with ordinary arithmetic.

5. **Branches are encoded relative to the PC.** A conditional branch stores a signed offset, not an absolute address, so code can be moved and the offset fits in few bits: RISC-V conditional branches reach ±4 KiB, jumps ±1 MiB. Far targets need a register-indirect jump. Indirect jumps through registers (function pointers, virtual calls, `return`) are what branch predictors find hardest.

6. **Byte order and alignment are part of the encoding contract.** Little-endian machines (x86, ARM and RISC-V in practice) store the least significant byte of a multi-byte value at the lowest address; big-endian machines (classic SPARC, IBM System/360 descendants, network byte order) store the most significant byte first. Many RISC ISAs historically required naturally aligned loads (a 4-byte load at an address divisible by 4) because an unaligned access may span two cache lines or two pages; modern cores usually support unaligned access but may pay extra cycles for it.

7. **Leaving room is the most important encoding decision.** An ISA that uses all its opcode space cannot grow. x86 grew by stacking prefix bytes (REX for 64-bit registers, VEX and EVEX for vector extensions), which works but lengthens instructions. RISC-V reserves major opcodes for custom and future extensions and defines a 16-bit compressed format whose low two bits distinguish it from 32-bit instructions.

## Key concepts

| Term | Meaning |
|---|---|
| Opcode | Bits that select which operation an instruction performs |
| Register specifier | Field naming a register; n bits name 2^n registers |
| Immediate | Constant embedded in the instruction itself |
| Effective address | The memory address an instruction actually accesses, after combining base, index, scale and displacement |
| PC-relative addressing | Address computed as an offset from the current program counter |
| Endianness | Order in which bytes of a multi-byte value are placed in memory |
| Alignment | Whether an address is a multiple of the access size |
| Position-independent code | Code that runs correctly at any load address, typically by using PC-relative addressing |
| Prefix | Extra byte(s) in x86 that modify the following instruction (operand size, register extension, vector form) |

## How it fits

- **Below:** instructions are [binary numbers](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md); decoders and address adders are [combinational building blocks](../../03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md); signed offsets use [two's complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md).
- **Above:** the [code generator](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md) chooses addressing modes and encodings; [linkers and loaders](../../06-programming-languages/04-runtime-systems/linking-and-loading.md) patch addresses and rely on PC-relative forms for shared libraries; [Just-In-Time (JIT) compilers](../../06-programming-languages/04-runtime-systems/jit-compilation.md) emit encodings directly at run time.
- **Siblings:** this is the concrete face of [RISC vs CISC](risc-vs-cisc.md), and every field here is part of [the ISA contract](the-isa-contract.md). The decoder that reads these bits is the front of the [datapath](../02-processor-microarchitecture/datapath-and-control.md).

## Common misconceptions

- **"More addressing modes make faster code."** Rarely used modes cost decode logic and complicate pipelines; compilers can synthesise complex addresses from simple arithmetic, often in parallel with other work.
- **"Endianness is a performance choice."** Neither order is faster; it is a convention that matters only when bytes cross between machines or between byte and word views of memory.
- **"Variable-length encoding is strictly worse."** Shorter encodings for common instructions reduce instruction-cache misses. Fixed-length ISAs adopt a limited form of variable length to get this benefit: adding RISC-V's 16-bit compressed forms shrinks typical programs by about 25–30%, and x86-64's density turns out to be no better than compressed RISC encodings because its prefixes add bytes.

## Go deeper

- Hennessy and Patterson, *Computer Architecture: A Quantitative Approach* (6th ed., 2017), Appendix A: measured frequencies of addressing modes and immediate sizes.
- Waterman, *Design of the RISC-V Instruction Set Architecture* (PhD thesis, UC Berkeley, 2016): explains each encoding choice and the compressed extension.
- Intel, *Intel 64 and IA-32 Architectures Software Developer's Manual*, Volume 2: the reference for x86 instruction formats.
