# JIT Compilation

> **Layer:** [06 Programming Languages](../README.md) › [Runtime Systems](README.md)
> **Builds on:** [Interpreters and virtual machines](interpreters-and-virtual-machines.md), [Optimization](../03-compilers/optimization.md), [Code generation and register allocation](../03-compilers/code-generation-and-register-allocation.md), [Measurement and modeling](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md)
> **Enables:** [Web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md)

## Essence

Just-In-Time (JIT) compilation translates code to native machine instructions while the program is running, instead of before it starts. It exists to resolve a tension: portable, dynamic languages are naturally interpreted, and interpretation is slow. A JIT starts by interpreting (or quickly compiling) everything, measures which code is hot, and spends optimisation effort only there. Because it compiles at run time, it can optimise for what the program is *actually* doing (the real types at a call site, the branch that is always taken) and fall back safely if that assumption ever breaks. The single idea is **speculative optimisation guided by profiling, with a guaranteed escape hatch**: compile for the common case, guard it with cheap checks, and deoptimise when a guard fails.

## Core tenets

1. **Most execution time is spent in a small part of the code.** Programs typically spend most of their time in a small fraction of their code (often summarised as "90% of time in 10% of code"). A JIT counts calls and loop iterations, and compiles a method or loop only once a threshold is passed. Cold code stays interpreted, so compile time is spent where it pays back.
2. **Tiered compilation balances start-up against peak speed.** Compilation time is part of run time, so one optimiser cannot be both fast and thorough. HotSpot, V8 and .NET use tiers: an interpreter or baseline compiler starts instantly and collects profiles; an optimising compiler later recompiles the hottest code using those profiles. The result is fast start-up and near-native steady-state speed after a warm-up period.
3. **Run-time profiles enable speculation a static compiler cannot justify.** An ahead-of-time compiler must handle every possible type at `x.foo()`. A JIT that has seen only one receiver class there can inline that class's method directly, guarded by a one-instruction type check. In dynamically typed languages this is the difference between a hash-table lookup per property access and a single load at a fixed offset.
4. **Inline caches make dynamic dispatch fast.** At each call or property-access site, the runtime caches the last receiver's type and the resolved target (Deutsch and Schiffman, 1984, for Smalltalk). Monomorphic sites (one type) become a compare and a direct call; polymorphic inline caches (Hölzle, Chambers and Ungar, 1991) handle a few types; megamorphic sites fall back to a full lookup. Hidden classes (shapes) give objects with the same layout a shared type so the cache can hit.

   ```
   // JIT output for o.x at a monomorphic site (pseudo-assembly)
   cmp [o + shape_offset], ShapeA     ; guard
   jne deopt_stub                     ; assumption broken -> bail out
   mov rax, [o + 16]                  ; x lives at offset 16 in ShapeA
   ```

5. **Deoptimisation makes speculation safe.** When a guard fails (a new type appears, a class is loaded that overrides an inlined method), the JIT must abandon optimised code mid-execution. It reconstructs the interpreter's frames from metadata recorded at each guard and resumes in the interpreter (on-stack replacement in reverse), then may recompile with the new knowledge. Without this, speculative optimisation would be incorrect.
6. **Method JITs and tracing JITs choose different compilation units.** A method JIT (HotSpot, V8) compiles whole functions. A tracing JIT (LuaJIT, PyPy) records the actual path taken through a hot loop, across function boundaries, and compiles that straight-line trace with guards at every branch. Traces optimise well but multiply when control flow is irregular.
7. **JITs pay costs that ahead-of-time compilers do not.** Warm-up time, memory for profiles and code, and compiler threads competing with the application. Executable memory that is also writable is a security risk, so modern JITs map code pages write-xor-execute and switch permissions when emitting code; JIT bugs are a prominent source of browser exploits.
8. **The JIT idea now reaches beyond language virtual machines.** Database engines compile query plans to native code, packet filters (extended Berkeley Packet Filter (eBPF)) are JIT-compiled in the Linux kernel, and machine-learning frameworks JIT-compile tensor programs for Graphics Processing Units (GPUs) and accelerators.

## Key concepts

| Term | Meaning |
|---|---|
| Just-In-Time (JIT) compilation | Compiling code to native instructions during program execution |
| Hot code | Code executed often enough to justify optimising compilation |
| Tiered compilation | Several compilers of increasing optimisation level, promoted by profile counts |
| Speculative optimisation | Optimising for observed behaviour, protected by run-time guards |
| Guard | A cheap check that an assumption still holds before optimised code proceeds |
| Deoptimisation | Abandoning optimised code and resuming in a less optimised tier |
| On-Stack Replacement (OSR) | Switching a running function between code versions while it is on the stack |
| Inline cache | A per-call-site cache of receiver type and resolved target |
| Hidden class (shape) | A run-time descriptor shared by objects with the same field layout |
| Tracing JIT | A JIT that compiles recorded hot execution paths rather than whole methods |

## How it fits

- **Below:** A JIT is a whole compiler ([intermediate representation](../03-compilers/intermediate-representations.md), [optimisation](../03-compilers/optimization.md), [code generation](../03-compilers/code-generation-and-register-allocation.md)) running inside an [interpreter or virtual machine](interpreters-and-virtual-machines.md). It must flush [instruction caches](../../04-computer-architecture/03-memory-hierarchy/cache-design.md) after writing code and relies on the operating system to change [page permissions](../../07-operating-systems/04-memory-management/address-spaces-and-paging.md). Its decisions are a [measurement](../../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md)-driven control loop.
- **Above:** Fast JavaScript made the modern web application possible, and its bugs shape [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md). JIT warm-up affects autoscaling and cold starts in [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md). Tensor compilers used in [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) apply the same specialise-at-run-time idea.
- **Siblings:** It is the escape route from [interpretation](interpreters-and-virtual-machines.md) overhead; it must report pointer locations in compiled frames to the [garbage collector](memory-management-and-garbage-collection.md); it performs late [linking](linking-and-loading.md) of methods as classes load.

## Common misconceptions

- **"JIT code is always slower than ahead-of-time code."** After warm-up, profile-driven speculation can beat static compilation on dynamic code; for static, predictable code the two are usually comparable.
- **"JIT compiles everything on first run."** Good JITs deliberately leave most code interpreted; compiling cold code wastes time and memory.
- **"Benchmarks of a JIT are measured from start."** Peak and start-up performance differ greatly, so honest benchmarks report warm-up separately from steady state.

## Go deeper

- John Aycock, "A Brief History of Just-In-Time" (2003): a survey of JIT ideas from Lisp to Java.
- Urs Hölzle, Craig Chambers and David Ungar, "Optimizing Dynamically-Typed Object-Oriented Languages with Polymorphic Inline Caches" (1991): the technique behind fast dynamic dispatch.
- Andreas Gal et al., "Trace-based Just-in-Time Type Specialization for Dynamic Languages" (2009): tracing JITs applied to JavaScript.
