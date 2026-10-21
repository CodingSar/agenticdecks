# Optimization

> **Layer:** [06 Programming Languages](../README.md) › [Compilers](README.md)
> **Builds on:** [Intermediate representations](intermediate-representations.md), [Relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), [Halting problem and undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Locality and caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md)
> **Enables:** [Code generation and register allocation](code-generation-and-register-allocation.md), [Just-in-time compilation](../04-runtime-systems/jit-compilation.md), [Vector units and graphics processors](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md)

## Essence

Compiler optimisation rewrites a program into one that computes the same observable result using less time, memory or energy. "Optimisation" is a misnomer: finding the truly optimal program is undecidable, so compilers apply a sequence of improving transformations, each justified by an analysis that proves it safe. The analyses are mostly dataflow problems solved on the Control-Flow Graph (CFG) of the Intermediate Representation (IR), and the transformations range from removing redundant arithmetic to restructuring loops for the cache and vector units. The single idea is **prove a fact about all possible executions, then exploit it**: a value that is always constant can be folded, a computation whose result is never used can be deleted, an access that never aliases a store can be moved.

## Core tenets

1. **Correctness means preserving observable behaviour, as defined by the language.** An optimisation may change anything not observable: timing, instruction order, which variables live in memory. It must not change output, side effects or the result of any defined computation. Where the language leaves behaviour undefined (signed overflow in C), the optimiser may assume it does not happen, which is why such code can behave unexpectedly at high optimisation levels.
2. **Perfect optimisation is undecidable, so analyses are conservative.** Deciding whether a piece of code is ever executed or whether two pointers can ever be equal is as hard as the [halting problem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md). Analyses therefore compute safe approximations: "may alias" when unsure, "possibly live" when unsure. Transformations fire only when the approximation proves safety.
3. **Dataflow analysis computes facts as a fixed point over a lattice.** Each analysis (reaching definitions, live variables, available expressions) associates a set of facts with each program point, with transfer functions per instruction and a merge rule at joins. Iterating until nothing changes converges because the facts form a finite-height [lattice](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) and the functions are monotone (Kildall, 1973). The same framework runs in reverse for backward problems such as liveness.
4. **Local and global scalar optimisations remove redundant work.** Constant folding and propagation compute at compile time what is known at compile time. Common subexpression elimination and value numbering reuse earlier results. Dead-code elimination deletes computations whose results are never used. Each is simple; iterated together, they are powerful.

   ```
   x = 4; y = x * 2; z = y + 1; if (false) w = z;      =>     z = 9
   ```

5. **Inlining is the enabling optimisation.** Replacing a call with the callee's body removes call overhead, but its real value is that it exposes the body to the caller's context, so constants propagate into it and dead branches disappear. It is limited by code growth, which can hurt instruction-cache behaviour, so compilers use size heuristics and profiles.
6. **Loops are where time goes, so loop optimisations matter most.** Loop-invariant code motion hoists computations that do not change per iteration. Strength reduction replaces `i * 4` with a running sum. Unrolling cuts branch overhead and exposes parallelism. Vectorisation turns scalar loops into Single Instruction, Multiple Data (SIMD) instructions. Tiling (blocking) reorders loop nests to reuse data while it is still in cache, which for matrix multiplication can change running time by an order of magnitude.
7. **Aliasing is the main obstacle in imperative languages.** If `p` and `q` might point to the same location, a store through `p` invalidates any cached value of `*q`, blocking reordering and register promotion. Alias analysis, C's `restrict`, strict-aliasing rules and Rust's exclusive mutable references all exist to give the optimiser this proof.
8. **Phase ordering and profiles decide real-world results.** Optimisations enable and disable each other, and the best order is program-dependent (the phase-ordering problem). Production compilers run fixed pipelines of dozens of passes. Profile-Guided Optimisation (PGO) records which branches and calls are hot in real runs and uses that to guide inlining, layout and unrolling, with typical gains of a few percent to around 20%, depending on how branchy and call-heavy the code is.

## Key concepts

| Term | Meaning |
|---|---|
| Observable behaviour | What the language guarantees: outputs, volatile accesses, defined side effects |
| Dataflow analysis | Computing facts at each program point by propagating them over the CFG to a fixed point |
| Lattice | A partial order with joins; gives dataflow analysis a guaranteed convergence |
| Liveness | A variable is live at a point if its current value may be read later |
| Constant propagation | Replacing variables with values known at compile time |
| Common subexpression elimination | Reusing a previously computed identical expression |
| Inlining | Substituting a function's body at a call site |
| Loop-invariant code motion | Moving computations that do not change within a loop to before the loop |
| Alias analysis | Determining whether two memory references may refer to the same location |
| Profile-Guided Optimisation (PGO) | Using measured execution profiles to steer optimisation decisions |

## How it fits

- **Below:** Optimisation relies on [IRs](intermediate-representations.md), lattice theory from [relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), and graph algorithms. Its goals come from the hardware: [caches and locality](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md), [pipelines](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md) and [SIMD units](../../04-computer-architecture/04-parallel-architecture/simd-and-gpus.md). The [performance equation](../../04-computer-architecture/06-performance/the-performance-equation.md) says what to reduce: instruction count, cycles per instruction, or both.
- **Above:** [Just-In-Time (JIT) compilers](../04-runtime-systems/jit-compilation.md) apply the same techniques at run time with profile data for free. Optimisers' treatment of undefined behaviour interacts with [memory-safety vulnerabilities](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), for example by deleting a bounds check that relied on overflow. Dataflow analysis is also the core of [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md) tools.
- **Siblings:** Consumes [static single assignment form IR](intermediate-representations.md) and hands improved IR to [code generation](code-generation-and-register-allocation.md); liveness analysis computed here is exactly what register allocation needs.

## Common misconceptions

- **"The compiler produces optimal code."** It produces improved code. Optimal code generation is undecidable in general, and even small sub-problems (instruction scheduling, register allocation) are hard enough that compilers rely on heuristics.
- **"Hand-optimising source beats the compiler."** Micro-tricks such as shifts instead of multiplies are already done automatically; what compilers cannot do is change the algorithm or the data layout, and that is where human effort pays.
- **"Optimisation bugs are compiler bugs."** Most surprising behaviour under `-O2` comes from programs with undefined behaviour that the optimiser was entitled to assume away.

## Go deeper

- Keith D. Cooper and Linda Torczon, *Engineering a Compiler* (2nd ed., 2011), chapters 8–10: scalar optimisation and dataflow analysis.
- Gary A. Kildall, "A Unified Approach to Global Program Optimization" (1973): the lattice framework for dataflow analysis.
- Randy Allen and Ken Kennedy, *Optimizing Compilers for Modern Architectures* (2001): dependence analysis, vectorisation and loop transformations.
