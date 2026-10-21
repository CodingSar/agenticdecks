# Code Generation and Register Allocation

> **Layer:** [06 Programming Languages](../README.md) › [Compilers](README.md)
> **Builds on:** [Instruction encoding and addressing](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md), [Pipelining](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [Optimization](optimization.md)
> **Enables:** [Linking and loading](../04-runtime-systems/linking-and-loading.md), [Just-in-time compilation](../04-runtime-systems/jit-compilation.md), [Kernel-mode and system calls](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md)

## Essence

Code generation is the compiler's back end: it maps the machine-independent Intermediate Representation (IR) onto the concrete instructions, registers and calling conventions of one Instruction Set Architecture (ISA). It solves three linked problems. Instruction selection chooses which machine instructions implement each IR operation. Register allocation decides which of the unlimited IR values live in the processor's few registers (16 general-purpose on x86-64, 31 on 64-bit ARM) and which must be "spilled" to memory. Instruction scheduling orders the instructions to keep the pipeline busy. Each problem is NP-hard (as hard as the hardest problems in the class NP, nondeterministic polynomial time) in its general form, so back ends use well-chosen heuristics. The single idea is that **registers are a tiny, fast cache that the compiler manages by hand**, and most back-end effort goes into using them well.

## Core tenets

1. **Instruction selection is tree pattern matching.** Each machine instruction covers a small pattern of IR operations: on x86, `mov eax, [rbx + rcx*4 + 8]` covers an add, a multiply, another add and a load. Selection tiles the IR tree with such patterns at minimum total cost. On trees this is solvable optimally by [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) (as in Bottom-Up Rewrite System (BURS) generators); on general directed acyclic graphs it is NP-hard, so compilers split them into trees or use greedy matching.
2. **Register allocation is graph colouring.** Compute liveness: two values that are live at the same time *interfere* and cannot share a register. Build the interference graph (values as nodes, interference as edges). Assigning k registers is colouring the graph with k colours. Chaitin (1981) made this the standard approach; colouring is NP-complete, but a simplify-and-select heuristic works very well in practice.

   ```
   a = ...        live: {a}
   b = ...        live: {a, b}      interference: a-b, b-c
   c = a + b      live: {b, c}      a and c never overlap -> may share a register
   ... = b + c
   ```

3. **Spilling trades memory traffic for registers.** When the graph cannot be coloured with k colours, some values are kept in memory (the stack frame) and loaded before each use. The allocator chooses victims by estimated cost: rarely used values outside loops are spilled first. Because memory is far slower than registers, poor spilling inside a hot loop can cost more than any other optimisation gains.
4. **Linear scan trades quality for speed.** Poletto and Sarkar (1999) allocate registers in one pass over live intervals sorted by start point. It runs in roughly linear time and produces code a little worse than colouring, which makes it the usual choice for [Just-In-Time (JIT) compilers](../04-runtime-systems/jit-compilation.md), where compile time is part of run time.
5. **Calling conventions are a contract between separately compiled code.** The Application Binary Interface (ABI) fixes which registers carry arguments and return values, which registers a callee must preserve (callee-saved) and which the caller must save (caller-saved), and how the stack frame is laid out. Every compiler targeting a platform obeys it, which is what lets C, Rust and Fortran code call each other and the [operating system](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md).
6. **Instruction scheduling hides latency.** A load may take 4 cycles on a cache hit and hundreds on a miss; a multiply several. Scheduling reorders independent instructions so the pipeline has useful work while waiting, using a dependence graph and list scheduling. Out-of-order processors do much of this in hardware, so static scheduling matters most on in-order cores, Very Long Instruction Word (VLIW) machines and Graphics Processing Units (GPUs).
7. **The three problems interact.** Scheduling to hide latency lengthens live ranges and raises register pressure; allocating registers first adds false dependences that limit scheduling. Compilers usually schedule, allocate, then schedule again, accepting that the order is a heuristic compromise.
8. **The output is an object file, not a program.** The back end emits machine code with symbolic references to functions and data in other files left unresolved, plus relocation records saying where addresses must be patched. The [linker](../04-runtime-systems/linking-and-loading.md) completes the job.

## Key concepts

| Term | Meaning |
|---|---|
| Instruction selection | Choosing machine instructions that implement IR operations |
| Tiling | Covering an IR tree with instruction patterns of known cost |
| Live range | The span of program points over which a value may still be used |
| Interference graph | Values as nodes, with edges between values live at the same time |
| Graph colouring | Assigning colours (registers) so that adjacent nodes differ |
| Spill | Storing a value in memory because no register is available |
| Linear scan | A fast register allocator over sorted live intervals |
| Application Binary Interface (ABI) | The binary-level contract: calling convention, data layout, system call interface |
| Callee-saved / caller-saved register | Registers preserved across calls by the callee / by the caller |
| List scheduling | Greedy ordering of ready instructions from a dependence graph |

## How it fits

- **Below:** The target is defined by [instruction encoding and addressing](../../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md) and shaped by [reduced versus complex instruction set](../../04-computer-architecture/01-instruction-set-architecture/risc-vs-cisc.md) design: a load/store ISA with many registers makes allocation easier. Scheduling targets the [pipeline](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md) and its [hazards](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md). Colouring comes from [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) and its hardness from [complexity theory](../../02-theory-of-computation/04-complexity/p-np-and-np-completeness.md).
- **Above:** Object files go to the [linker and loader](../04-runtime-systems/linking-and-loading.md); [JIT compilers](../04-runtime-systems/jit-compilation.md) run a fast version of this back end at run time; the ABI is what [system calls](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md) and libraries rely on.
- **Siblings:** Receives optimised IR from [optimisation](optimization.md) and reuses its liveness analysis; it is the only phase of the [compiler](README.md) that must know the target machine in detail.

## Common misconceptions

- **"Out-of-order hardware makes compiler scheduling irrelevant."** It reduces its importance on big cores, but register allocation still matters, and in-order cores, GPUs and embedded processors still depend on static scheduling.
- **"More registers always help."** More architectural registers mean longer instruction encodings and more state to save on context switches; the right number is a trade-off, which is why ISAs settle on 16 to 32.
- **"Assembly written by hand is faster."** For whole programs, modern back ends usually match or beat hand-written code; hand-written assembly wins mainly in small kernels using special instructions.

## Go deeper

- Gregory J. Chaitin, "Register Allocation and Spilling via Graph Coloring" (1982): the classic colouring allocator.
- Massimiliano Poletto and Vivek Sarkar, "Linear Scan Register Allocation" (1999): the fast alternative used in JIT compilers.
- Andrew W. Appel, *Modern Compiler Implementation in ML* (1998), chapters 9–11: instruction selection, liveness and colouring, implemented.
