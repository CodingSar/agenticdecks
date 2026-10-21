# Imperative and Procedural Programming

> **Layer:** [06 Programming Languages](../README.md) › [Paradigms](README.md)
> **Builds on:** [The ISA contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [Turing machines](../../02-theory-of-computation/03-computability/turing-machines.md), [Stacks and queues](../../05-algorithms-and-data-structures/02-fundamental-data-structures/stacks-and-queues.md)
> **Enables:** [Object-oriented programming](object-oriented.md), [Hoare logic and program proofs](../05-formal-methods/hoare-logic-and-program-proofs.md), [Kernel architectures](../../07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md)

## Essence

Imperative programming describes computation as a sequence of commands that change a program's state: variables are named memory cells, assignment overwrites them, and control flow (sequence, branch, loop) decides which command runs next. It is the paradigm closest to the hardware, because a von Neumann processor does exactly this: fetch an instruction, update registers or memory, choose the next instruction. Procedural programming adds the procedure (function, subroutine), a named, parameterised block of commands with its own local state, so large programs can be split into pieces. The single idea is that a program is a *recipe of state changes*, and its meaning is the final state it produces.

## Core tenets

1. **Variables are names for mutable locations, not for values.** In `x = x + 1`, the left `x` means "the cell" and the right `x` means "the current contents of the cell". This distinction (an l-value and an r-value) is why imperative reasoning needs to track *when* a read happens: the same expression can give different results at different times.
2. **Structured control flow is enough.** The Böhm–Jacopini theorem (1966) shows that sequence, selection and iteration can express any computable control flow without `goto`. Dijkstra's argument against `goto` (1968) was about reasoning, not power: with structured blocks, each piece of code has one entry and one exit, so you can reason about it in isolation.
3. **Procedures are the first abstraction mechanism.** A procedure hides a sequence of steps behind a name and an interface (its parameters and result). The caller depends only on what the procedure promises, so the body can change. This is the seed of modularity in [software engineering](../../12-software-engineering/01-design/modularity-and-information-hiding.md).
4. **The call stack makes recursion and local state cheap.** Each call pushes an activation record (frame) holding parameters, locals and the return address; return pops it. Because calls nest strictly, last-in first-out allocation is exact and costs one pointer adjustment. This is why local variables vanish when a procedure returns, and why returning a pointer to a local is a bug in C.
5. **Parameter-passing mode changes meaning.** Call by value copies the argument; call by reference passes the location, so the callee can change the caller's variable. Most modern languages pass values, but when the value is itself a reference (an object in Java or Python), the callee can mutate the shared object while not being able to rebind the caller's variable.

   ```c
   void inc(int *p) { *p = *p + 1; }   /* caller's variable changes */
   int x = 1; inc(&x);                  /* x == 2 */
   ```

6. **Aliasing makes reasoning and optimisation hard.** When two names refer to the same location, writing through one silently changes the other. A compiler cannot keep `*p` in a register across a write to `*q` unless it can prove `p != q`. C's `restrict` keyword and Rust's ownership rules exist to rule aliasing out.
7. **Order of evaluation is part of the meaning.** Because commands have side effects, `f() + g()` can produce different results if `f` and `g` touch shared state. Languages either fix the order (Java: left to right) or leave it unspecified (C), and in the second case portable programs must not depend on it.

## Key concepts

| Term | Meaning |
|---|---|
| State | The contents of all variables and memory at a point in execution |
| Assignment | A command that overwrites a location with a new value |
| Side effect | Any observable change a computation makes besides returning a value |
| Activation record (frame) | Stack-allocated storage for one procedure call: arguments, locals, return address |
| l-value / r-value | An expression denoting a location vs one denoting a value |
| Aliasing | Two or more names referring to the same memory location |
| Structured programming | Control flow restricted to sequence, selection, iteration and procedure calls |
| Undefined behaviour | Program actions (in C/C++) for which the language imposes no requirements |

## How it fits

- **Below:** Imperative languages are a named, structured view of the [ISA](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md): variables map to registers and memory, loops to conditional branches, calls to the hardware's call and return instructions. The theoretical model is the [Turing machine](../../02-theory-of-computation/03-computability/turing-machines.md), a state machine with mutable tape.
- **Above:** Operating systems are written imperatively (C, increasingly Rust), and most [algorithms](../../05-algorithms-and-data-structures/README.md) are stated imperatively. [Hoare logic](../05-formal-methods/hoare-logic-and-program-proofs.md) was invented to reason about exactly this style.
- **Siblings:** [Object-oriented](object-oriented.md) programming organises imperative state into objects. [Functional](functional.md) programming removes assignment. [Logic and declarative](logic-and-declarative.md) programming removes explicit control flow.

## Common misconceptions

- **"Imperative means low-level."** Imperative is about mutable state and explicit sequencing, not abstraction level. Python and Java are high-level and largely imperative.
- **"Removing goto made languages less powerful."** Structured control flow is just as expressive; `break`, `return` and exceptions are disciplined forms of the jumps that remain useful.
- **"Undefined behaviour just means the result is unpredictable."** In C and C++ the compiler may assume undefined behaviour never happens and optimise accordingly, so a signed overflow or out-of-bounds read can change the behaviour of code far away from it.

## Go deeper

- Brian W. Kernighan and Dennis M. Ritchie, *The C Programming Language* (2nd ed., 1988): the canonical imperative language, close to the machine.
- Edsger W. Dijkstra, "Go To Statement Considered Harmful" (1968): the short argument that created structured programming.
- Harold Abelson and Gerald Jay Sussman, *Structure and Interpretation of Computer Programs* (2nd ed., 1996), chapter 3: why assignment destroys the simple substitution model.
