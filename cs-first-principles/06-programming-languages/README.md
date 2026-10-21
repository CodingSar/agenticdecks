# 06 Programming Languages

> **Layer:** 06 Programming Languages
> **Children:** [Paradigms](01-paradigms/README.md) · [Semantics and Types](02-semantics-and-types/README.md) · [Compilers](03-compilers/README.md) · [Runtime Systems](04-runtime-systems/README.md) · [Formal Methods](05-formal-methods/README.md)

## What this area is about

A programming language is a precisely defined notation for computation that humans can read, write and reason in, and that a machine can still execute. The hardware below offers only an Instruction Set Architecture (ISA): numbered registers, flat memory addresses and a few hundred instructions. Nobody can hold a million-line system in their head at that level. Languages add names, scopes, procedures, data types, modules and guarantees, so that a programmer can think in terms of "a list of customers" instead of "the 64-bit word at address 0x7ffe3a10".

The unifying idea is that **a language is an abstraction with a meaning**. Its syntax says which programs can be written. Its semantics says what each program means. Its type system says which meaningful-looking programs are rejected because they would go wrong. Then a compiler or interpreter has to make the machine behave exactly as that meaning says. Every child of this layer is about one side of that contract: how to design the notation (paradigms), how to define its meaning (semantics and types), how to translate it faithfully (compilers), how to support it while it runs (runtime systems) and how to prove that a program does what it should (formal methods).

## Why this layer sits here

Languages need two things from below.

- **From the formal pillar.** Grammars and parsing come from [automata and formal languages](../02-theory-of-computation/02-automata-and-formal-languages/README.md): every language's surface syntax is a [context-free grammar](../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md). The [lambda calculus](../02-theory-of-computation/03-computability/lambda-calculus.md) is the core of functional languages and the standard setting for studying types and scope. [Computability](../02-theory-of-computation/03-computability/README.md) sets the hard ceiling: by [the halting problem and Rice's theorem](../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), no tool can decide every interesting property of every program, which is why type systems and analysers must approximate. [Logic](../01-mathematical-foundations/01-logic/README.md) supplies the rules of inference behind type checking and program proofs, and the Curry–Howard correspondence makes types and propositions the same thing.
- **From the physical pillar.** The target of every language is the [ISA contract](../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md). Compilers must know about [registers and addressing](../04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md), [pipelines](../04-computer-architecture/02-processor-microarchitecture/pipelining.md), the [memory hierarchy](../04-computer-architecture/03-memory-hierarchy/README.md) and [memory consistency models](../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) to emit fast, correct code. The [algorithms layer](../05-algorithms-and-data-structures/README.md) supplies the graph algorithms, hash tables and dynamic programming that compilers and runtimes are built from.

What the layers above need from this one is **a notation with a defined meaning, plus a faithful translation of that meaning to the machine**. Operating systems are written in languages such as C and Rust and compiled to the ISA. Security depends on whether the language guarantees memory safety. Software engineering depends on the modules, interfaces and types that languages provide.

The single interface this layer adds to the stack is **the language definition**: a promise that a program text means a particular computation, independent of the machine it runs on.

## How the children fit together

```
            Paradigms  (what styles of thought the notation supports)
                |
       Semantics and Types  (what programs mean; which are rejected)
           /          \
     Compilers      Formal Methods
  (translate meaning   (prove the program, or the
   down to the ISA)     compiler, meets a specification)
           \
      Runtime Systems  (what must still exist while the program runs:
                        loader, interpreter, JIT, garbage collector)
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Paradigms](01-paradigms/README.md) | The main ways to organise computation: commands over state, objects, functions, relations | 02 (lambda calculus, Turing machines), 04 (the imperative machine model) |
| [Semantics and Types](02-semantics-and-types/README.md) | Defines meaning, scope and the static rules that rule out errors | Paradigms, 01 logic, 02 grammars |
| [Compilers](03-compilers/README.md) | Turns source text into machine code while preserving meaning | Semantics and Types, 02 automata, 04 ISA, 05 graph algorithms |
| [Runtime Systems](04-runtime-systems/README.md) | Linking, loading, interpretation, Just-In-Time (JIT) compilation and memory management at run time | Compilers, 04 memory hierarchy |
| [Formal Methods](05-formal-methods/README.md) | Proves programs correct against a specification | Semantics and Types, 01 logic, 02 computability |

Read paradigms first to see what languages are trying to express. Semantics and types come next, because every later topic assumes a precise meaning to preserve or prove. Compilers and runtime systems are two halves of implementation: what is done once ahead of time, and what must be done while the program runs. The boundary between them moves: a JIT compiler is a compiler inside a runtime. Formal methods sit beside compilers as the other consumer of semantics: one translates meaning, the other reasons about it.

## Connections to neighbouring layers

- **[02 Theory of Computation](../02-theory-of-computation/README.md).** Lexers are finite automata; parsers are pushdown automata. Every general-purpose language is Turing complete, so undecidability limits every analysis a compiler or verifier can perform.
- **[03 Digital Logic](../03-digital-logic/README.md).** Integer types inherit [two's complement](../03-digital-logic/01-number-representation/integers-and-twos-complement.md) overflow and floating-point types inherit [IEEE 754 rounding](../03-digital-logic/01-number-representation/floating-point.md). Hardware description languages apply language ideas to circuits.
- **[04 Computer Architecture](../04-computer-architecture/README.md).** Compilers are the bridge back down to 04: register allocation, instruction selection and scheduling exist because of how processors are built, and much of a modern processor's design assumes compiled code.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md).** Algorithms are expressed in languages, and language implementations are heavy users of algorithms: graph colouring for registers, dataflow fixed points, tracing for garbage collection.
- **[07 Operating Systems](../07-operating-systems/README.md).** Kernels are programs written in languages and built by compilers and linkers. Runtimes rely on the OS for virtual memory, threads and loading; the OS relies on the language's ability to express low-level, unsafe operations.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md).** [Memory-safety vulnerabilities](../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md) are a property of language design: undefined behaviour in C and C++ is the root of most exploitable bugs, and safe languages remove whole classes of them.
- **[12 Software Engineering](../12-software-engineering/README.md).** Modules, interfaces, types and static analysis are the tools that let large teams build large systems.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md).** Logic programming grew out of AI, and machine-learning frameworks rely on compiler techniques such as automatic differentiation and tensor compilers.

## Connections across layers

This layer takes grammars, the lambda calculus and undecidability from 02, logic and type-theory roots from 01, and the ISA and memory hierarchy from 04. It gives the OS (07) the means to be written at all, gives security (11) its memory-safety story, and gives software engineering (12) its units of modularity. Distributed and parallel programming models in [10](../10-distributed-and-parallel-computing/README.md) are language-level abstractions over threads, messages and data parallelism.

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the language hides the ISA; the compiler restores it.
- [Interface vs implementation](../CROSS-CUTTING.md#interface-vs-implementation): language definition vs compiler; module signature vs body.
- [Indirection and naming](../CROSS-CUTTING.md#indirection-and-naming): binding, scope, symbol resolution in linkers, virtual dispatch.
- [Invariants and correctness](../CROSS-CUTTING.md#invariants-and-correctness): types and loop invariants are machine-checked or proved invariants.
- [Recursion and self-reference](../CROSS-CUTTING.md#recursion-and-self-reference): compilers compile themselves; interpreters interpret programs.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): Rice's theorem forces every analysis to be approximate.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): compile time vs run time, static vs dynamic checking, garbage collection throughput vs pause time.
- [Trust and verification](../CROSS-CUTTING.md#trust-and-verification): small trusted proof kernels and verified compilers.
