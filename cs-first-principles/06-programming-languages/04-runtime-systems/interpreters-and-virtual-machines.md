# Interpreters and Virtual Machines

> **Layer:** [06 Programming Languages](../README.md) › [Runtime Systems](README.md)
> **Builds on:** [Syntax and semantics](../02-semantics-and-types/syntax-and-semantics.md), [Intermediate representations](../03-compilers/intermediate-representations.md), [Turing machines](../../02-theory-of-computation/03-computability/turing-machines.md), [Hazards and branch prediction](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md)
> **Enables:** [Just-in-time compilation](jit-compilation.md), [Isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md), [Web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md)

## Essence

An interpreter executes a program directly, reading its representation and performing each operation, instead of translating the whole program to machine code first. The idea is as old as computability itself: Turing's universal machine is an interpreter for other Turing machines. Most production interpreters do not walk source text; they compile it once to a compact bytecode for a process virtual machine (VM), an idealised machine defined in software, and then run a loop that fetches, decodes and executes one bytecode at a time. The Java Virtual Machine (JVM), Python's CPython, Lua, the .NET Common Language Runtime (CLR) and WebAssembly engines all follow this design. The single idea is **trade raw speed for portability, simplicity and control**: one VM implementation per platform runs the same program everywhere, starts instantly, and can check every operation as it happens.

## Core tenets

1. **An interpreter is an executable semantics.** A tree-walking interpreter is a recursive function `eval(node, env)` with one case per syntax construct, mirroring the language's operational semantics almost line for line. This makes an interpreter the quickest correct implementation of a language.

   ```python
   def eval(e, env):
       match e:
           case Num(n):        return n
           case Var(x):        return env[x]
           case Add(a, b):     return eval(a, env) + eval(b, env)
           case Lam(x, body):  return Closure(x, body, env)
           case App(f, a):
               c = eval(f, env); return eval(c.body, {**c.env, c.x: eval(a, env)})
   ```

2. **Interpretation costs a constant factor, mostly in dispatch.** Each operation pays for fetching and decoding the next instruction and an indirect jump to its handler, on top of the real work. Typical bytecode interpreters run roughly 3 to 30 times slower than optimised native code, depending on how much work each instruction does; tree-walkers are slower still because they chase pointers between nodes.
3. **Bytecode moves work from run time to a one-time compile step.** Compiling source to a linear, compact bytecode resolves names to slot numbers, flattens expressions and improves cache locality, so the inner loop does less per operation. This is why CPython compiles `.py` files to bytecode before running them, even though it remains an interpreter.
4. **Stack VMs are simpler; register VMs execute fewer instructions.** A stack machine (JVM, CPython, WebAssembly) takes operands from an implicit operand stack, so instructions are short and compilation is easy. A register machine (Lua 5, Android's Dalvik) names virtual registers in each instruction, so `a = b + c` is one instruction instead of four. Shi et al. (2005) measured register VMs executing about 47% fewer instructions at the cost of about 25% larger code.

   ```
   stack VM:  load b; load c; add; store a       register VM:  add a, b, c
   ```

5. **Dispatch technique matters because of branch prediction.** A `switch` in a loop sends every instruction through one indirect branch, which the processor's [branch predictor](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) predicts poorly. Threaded code (computed `goto` at the end of each handler) gives each handler its own indirect branch, whose history is more predictable, and was historically worth tens of percent. Recent predictors have narrowed this gap.
6. **A VM defines a portable, checkable machine.** The JVM specification fixes bytecode semantics, a memory model, class loading and a verifier that checks type safety of bytecode before it runs. Because every operation passes through the VM, it can enforce bounds checks, type checks and security policies, which is why browsers run untrusted JavaScript and WebAssembly inside VMs as a [sandbox](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md).
7. **Interpreters enable dynamic features that compilers find hard.** `eval`, run-time code loading, live code reloading, debuggers that inspect any variable, and Read–Eval–Print Loops (REPLs) are natural in an interpreter because the program's representation and environment are available at run time.
8. **Interpreting and compiling are ends of a spectrum.** Real systems mix them: the JVM and JavaScript engines start interpreting and use [Just-In-Time (JIT) compilation](jit-compilation.md) for hot code; ahead-of-time compilers ship with small interpreters for debugging. A partial evaluator can even turn an interpreter plus a program into a compiled program (the first Futamura projection, 1971), an idea that the GraalVM Truffle framework exploits in practice.

## Key concepts

| Term | Meaning |
|---|---|
| Interpreter | A program that executes another program by performing its operations directly |
| Process virtual machine (VM) | A software-defined machine with its own instruction set that runs on a real one |
| Bytecode | A compact, portable instruction encoding for a VM |
| Dispatch loop | The fetch–decode–execute loop at the core of an interpreter |
| Stack-based VM | A VM whose instructions take operands from an implicit stack |
| Register-based VM | A VM whose instructions name virtual registers explicitly |
| Threaded code | Dispatch by jumping directly from handler to handler, avoiding a central switch |
| Bytecode verifier | A static check that bytecode is type-safe before execution |
| Futamura projection | Specialising an interpreter to a program yields a compiled version of that program |

## How it fits

- **Below:** Interpreters realise [operational semantics](../02-semantics-and-types/syntax-and-semantics.md) and Turing's [universal machine](../../02-theory-of-computation/03-computability/turing-machines.md). Bytecode is an [intermediate representation](../03-compilers/intermediate-representations.md). Interpreter speed depends on [branch prediction](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) and [caches](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md).
- **Above:** VMs are the basis of browser engines and their [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md) model, of portable deployment in [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), and of scripting in nearly every large application. Process VMs differ from the system VMs of [hypervisors](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md), which virtualise a whole hardware machine.
- **Siblings:** [JIT compilation](jit-compilation.md) is how VMs escape the interpretation penalty; [garbage collection](memory-management-and-garbage-collection.md) is almost always part of a VM; [linking and loading](linking-and-loading.md) has a VM analogue in class loading.

## Common misconceptions

- **"Python and Java are interpreted, C is compiled."** Being interpreted or compiled is a property of an implementation, not a language: there are C interpreters, Python compilers (PyPy uses a tracing JIT) and the JVM compiles most hot code to native instructions.
- **"Interpreters are only for toy languages."** CPython, Ruby's standard interpreter and many embedded scripting engines run production workloads as interpreters, because start-up time and simplicity matter more there than peak speed.
- **"A JVM is the same kind of thing as VMware."** One virtualises a language-level machine for a single process; the other virtualises hardware for whole operating systems.

## Go deeper

- Robert Nystrom, *Crafting Interpreters* (2021): builds a tree-walker and a bytecode VM from scratch.
- Tim Lindholm, Frank Yellin, Gilad Bracha and Alex Buckley, *The Java Virtual Machine Specification* (Java SE 8 edition, 2014): the canonical example of a defined VM.
- Yunhe Shi, Kevin Casey, M. Anton Ertl and David Gregg, "Virtual Machine Showdown: Stack Versus Registers" (2005/2008): the measured trade-off.
