# Intermediate Representations

> **Layer:** [06 Programming Languages](../README.md) › [Compilers](README.md)
> **Builds on:** [Semantic analysis](semantic-analysis.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [The ISA contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md)
> **Enables:** [Optimization](optimization.md), [Code generation and register allocation](code-generation-and-register-allocation.md), [Just-in-time compilation](../04-runtime-systems/jit-compilation.md)

## Essence

An Intermediate Representation (IR) is the compiler's internal language: a form of the program that sits between source and machine code and is designed for analysis and transformation rather than for people. Source code is too rich (nested expressions, many statement forms, implicit conversions) and machine code too specific (a fixed register set, target quirks) for optimisation to work well on either. An IR is small and uniform: a few kinds of instruction, explicit temporaries, explicit control flow. The dominant design today is Static Single Assignment (SSA) form inside a Control-Flow Graph (CFG), used by LLVM, the GNU Compiler Collection (GCC), HotSpot, V8 and most other modern compilers. The single idea is **make every fact the optimiser needs explicit in the structure**, so that analyses become graph walks instead of searches.

## Core tenets

1. **An IR decouples languages from machines.** Front ends for C, Rust and Swift all emit LLVM IR; back ends for x86-64, ARM and RISC-V all consume it. With m languages and n targets, the shared IR needs m + n components rather than m × n compilers, and every optimisation written once benefits all pairs.
2. **Three-address code flattens expressions into simple steps.** Each instruction has at most one operator and names its result: `a = b * c + d` becomes `t1 = b * c; t2 = t1 + d; a = t2`. Every intermediate value now has a name, so it can be reused, moved or eliminated.
3. **The control-flow graph makes branching explicit.** A basic block is a straight-line sequence with one entry at the top and one exit at the bottom. The CFG has blocks as nodes and possible jumps as edges. Loops appear as cycles, and graph concepts such as dominators (block A dominates B if every path from entry to B passes through A) identify loop headers and safe places to move code.
4. **SSA form gives every variable exactly one definition.** Each assignment creates a new version (`x1`, `x2`, ...). Where control flow merges and different versions could arrive, a φ (phi) function selects the right one. Because each name has one definition, "where did this value come from?" has a single answer, and def-use chains become explicit edges. Constant propagation, dead-code elimination and value numbering become simple and fast.

   ```
   if (c) x = 1; else x = 2;        if (c) x1 = 1; else x2 = 2;
   y = x + 1;                 =>    x3 = φ(x1, x2); y1 = x3 + 1
   ```

5. **SSA construction is efficient, and φ functions vanish before execution.** Cytron et al. (1991) showed how to place φ functions using dominance frontiers in near-linear time in practice. Processors have no φ instruction, so the back end replaces each one with copies on the incoming edges, which register allocation then tries to remove.
6. **Real compilers use several IRs at different levels.** A high-level IR keeps loops, array indexing and types (good for loop transformations and devirtualisation). A mid-level SSA IR is target-independent and does most scalar optimisation. A low-level IR exposes machine instructions and registers. Each lowering step discards information that later phases no longer need. Frameworks such as MLIR (Multi-Level Intermediate Representation) make this multi-level structure explicit, especially for machine-learning compilers.
7. **Stack-based bytecode is also an IR, optimised for compactness and portability.** Java Virtual Machine (JVM) bytecode and WebAssembly use an operand stack instead of named temporaries, which makes code small and easy to verify and to ship. Just-In-Time (JIT) compilers convert it to SSA internally before optimising.
8. **The IR must have a precise semantics of its own.** Every pass is only correct if it preserves the IR's meaning, so the IR needs rules for overflow, undefined values and memory. LLVM's `undef` and `poison` values exist to model C's undefined behaviour precisely enough that optimisations can be checked, and subtle mistakes in those rules have caused real miscompilations.

## Key concepts

| Term | Meaning |
|---|---|
| Intermediate Representation (IR) | The compiler's internal program form, between source and machine code |
| Three-address code | Instructions of the form `x = y op z`, with explicit temporaries |
| Basic block | A maximal straight-line instruction sequence with one entry and one exit |
| Control-Flow Graph (CFG) | A directed graph of basic blocks connected by possible jumps |
| Dominator | Block A dominates B if every path from the entry to B passes through A |
| Static Single Assignment (SSA) | IR form in which each variable is assigned exactly once |
| φ (phi) function | An SSA pseudo-instruction choosing a value by the incoming control-flow edge |
| Def-use chain | A link from a value's definition to each of its uses |
| Bytecode | A compact, portable, often stack-based instruction set for a virtual machine |

## How it fits

- **Below:** IRs are built on [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) (CFGs, dominator trees) and [graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md). Low-level IRs mirror the [instruction set architecture](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) closely enough that lowering is mechanical.
- **Above:** IRs are the substrate for [optimisation](optimization.md) and [code generation](code-generation-and-register-allocation.md); bytecode IRs feed [interpreters and virtual machines](../04-runtime-systems/interpreters-and-virtual-machines.md) and [JIT compilers](../04-runtime-systems/jit-compilation.md). Machine-learning frameworks compile tensor graphs through IRs for [accelerators](../../04-computer-architecture/04-parallel-architecture/domain-specific-accelerators.md).
- **Siblings:** It receives the annotated tree from [semantic analysis](semantic-analysis.md) and is the contract between the language-specific front end and the target-specific back end.

## Common misconceptions

- **"SSA means the program cannot reassign variables."** The source program can; SSA renames each assignment to a new version internally.
- **"Bytecode is just slow machine code."** It is a portable IR; a JIT compiles hot bytecode to native code that is often as fast as ahead-of-time output.
- **"One good IR is enough."** Each level makes some transformations easy and others hard, so production compilers use a stack of IRs.

## Go deeper

- Ron Cytron, Jeanne Ferrante, Barry K. Rosen, Mark N. Wegman and F. Kenneth Zadeck, "Efficiently Computing Static Single Assignment Form and the Control Dependence Graph" (1991): the SSA construction algorithm.
- Chris Lattner and Vikram Adve, "LLVM: A Compilation Framework for Lifelong Program Analysis and Transformation" (2004): the design that made a shared IR mainstream.
- Keith D. Cooper and Linda Torczon, *Engineering a Compiler* (2nd ed., 2011), chapters 5 and 9: IR design and SSA in depth.
