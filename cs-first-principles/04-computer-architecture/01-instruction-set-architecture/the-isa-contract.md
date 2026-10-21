# The ISA Contract

> **Layer:** [04 Computer Architecture](../README.md) › [Instruction Set Architecture](README.md)
> **Builds on:** [Turing machines](../../02-theory-of-computation/03-computability/turing-machines.md), [Finite-state machines](../../03-digital-logic/03-sequential-logic/finite-state-machines.md), [Integers and two's complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md)
> **Enables:** [Datapath and control](../02-processor-microarchitecture/datapath-and-control.md), [Code generation and register allocation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md), [Kernel mode and system calls](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [Models of computation](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md)

## Essence

An Instruction Set Architecture (ISA) is a specification of a processor as software sees it: a set of architectural state (registers, program counter, memory, control registers) and a set of instructions, each defined as a function from one state to the next. It is a contract: hardware promises that every instruction behaves as specified, and software promises to rely on nothing else. The contract deliberately says nothing about *how* instructions run, how long they take, or how many run at once. That silence is what lets the same binary run on a 1990s in-order chip and a 2020s eight-wide out-of-order core, and it is why the ISA is the most important interface in the computing stack.

## Core tenets

1. **Architecture and implementation are separate things.** The IBM System/360 (1964) introduced the split: one ISA, several machines from cheap to fast, all running the same software. The microarchitecture (pipeline depth, cache size, number of execution units) can change every generation; the ISA must not, because the world's installed software depends on it.

2. **The state machine view is the definition.** Architectural state is the program counter (PC), the general-purpose registers (16 on x86-64, 31 plus a zero register on 64-bit ARM, 32 on RISC-V with x0 hardwired to zero), floating-point and vector registers, status flags, and memory. Each instruction reads some state and writes some state, then sets the next PC. A program's meaning is the sequence of states this produces; nothing else is observable.

3. **Sequential semantics is the illusion every implementation must preserve.** Within one thread, each instruction must appear to finish completely before the next starts. Real cores overlap dozens to hundreds of instructions and execute them out of order, but they commit results in program order so that, at every point, the visible state matches some sequential execution. Precise exceptions are the strongest form of this: when an instruction faults, all earlier instructions have completed and no later one has changed state.

4. **The stored-program principle makes code just data.** Instructions live in the same memory as data and are fetched by address (the von Neumann model, 1945). This is what lets a compiler write a program, a loader place it, and a Just-In-Time (JIT) compiler generate code at run time. It also means self-modifying code needs care: ARM and RISC-V require an explicit instruction-cache synchronisation step after writing code.

5. **Privilege levels let one program control others.** ISAs define at least two modes: user mode, where privileged instructions and protected memory are off-limits, and supervisor (kernel) mode, where they are not. x86 has rings 0–3 (in practice 0 and 3), ARMv8 has exception levels EL0–EL3, and RISC-V has U, S and M modes. The only ways from user to kernel are controlled entry points: system-call instructions (`syscall`, `svc`, `ecall`), exceptions and interrupts. An Operating System (OS) can enforce isolation only because the ISA makes these the only doors.

6. **Exceptions and interrupts are part of the contract.** A synchronous exception (page fault, divide by zero, illegal instruction) is caused by an instruction; an asynchronous interrupt (timer, network card) is caused by the outside world. In both cases the ISA specifies that the processor saves the PC and cause, switches to kernel mode, and jumps to a handler address set by the OS. The timer interrupt is what lets an OS take the processor back from a program that never yields.

7. **Timing is outside the contract, and that has consequences.** The ISA promises results, not speed. This freedom allows caches and speculation, but it also means two correct implementations can differ by 100x in running time, and that the timing of a correct program can leak secrets (cache side channels, Spectre in 2018).

8. **The memory model is part of the ISA once there is more than one core.** With one core, "a load returns the last store" is simple. With many, the ISA must say which orderings of stores other cores may observe: x86 promises Total Store Order, ARM and RISC-V promise much less and provide fence instructions.

## Key concepts

| Term | Meaning |
|---|---|
| Architectural state | Everything an instruction can read or write and software can observe: PC, registers, flags, memory, control registers |
| Microarchitecture | A particular implementation of an ISA: pipeline, caches, predictors, execution units |
| Program counter (PC) | Register holding the address of the next instruction to execute |
| Precise exception | An exception after which state reflects exactly all instructions before the faulting one and none after |
| Privilege mode | Hardware mode that decides which instructions and memory are accessible |
| Application Binary Interface (ABI) | Conventions layered on the ISA: calling convention, register use, stack layout, object file format |
| Trap / system call | A deliberate instruction that transfers control to the kernel at a fixed entry point |

## How it fits

- **Below:** an ISA is a large [finite-state machine](../../03-digital-logic/03-sequential-logic/finite-state-machines.md) whose state lives in [flip-flops](../../03-digital-logic/03-sequential-logic/latches-and-flip-flops.md) and memory, and whose data types are the encodings of [two's complement](../../03-digital-logic/01-number-representation/integers-and-twos-complement.md) and [floating point](../../03-digital-logic/01-number-representation/floating-point.md). Its universality comes from the [Church–Turing thesis](../../02-theory-of-computation/03-computability/church-turing-thesis.md): any reasonable ISA with enough memory can compute anything computable.
- **Above:** compilers target it ([code generation](../../06-programming-languages/03-compilers/code-generation-and-register-allocation.md)), the [RAM model](../../05-algorithms-and-data-structures/01-foundations/models-of-computation.md) idealises it, and [OS kernels](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md) depend on its privilege and exception mechanisms.
- **Siblings:** [RISC vs CISC](risc-vs-cisc.md) is about which instructions to put in the contract; [instruction encoding](instruction-encoding-and-addressing.md) is about how to write them down as bits.

## Common misconceptions

- **"The ISA is the processor."** The ISA is a specification; Intel and AMD build very different microarchitectures for the same x86-64 ISA, and Apple, Qualcomm and Arm build different cores for the same ARMv8/v9 ISA.
- **"Instructions run one at a time in order."** They only *appear* to. A modern core has hundreds of instructions in flight; the in-order appearance is maintained by in-order commit.

## Go deeper

- Amdahl, Blaauw and Brooks, *Architecture of the IBM System/360* (1964): the paper that defined "architecture" as distinct from implementation.
- Patterson and Hennessy, *Computer Organization and Design: The Hardware/Software Interface* (RISC-V edition, 2017): the standard introduction, built around this contract.
- Waterman and Asanović (eds.), *The RISC-V Instruction Set Manual, Volume I: Unprivileged ISA*: a short, readable real ISA specification with design rationale.
