# Compilers

> **Layer:** [06 Programming Languages](../README.md) › Compilers
> **Children:** [Lexing and Parsing](lexing-and-parsing.md) · [Semantic Analysis](semantic-analysis.md) · [Intermediate Representations](intermediate-representations.md) · [Optimization](optimization.md) · [Code Generation and Register Allocation](code-generation-and-register-allocation.md)

## What this area is about

A compiler translates a program from a source language into a target language, usually machine code for an Instruction Set Architecture (ISA), while preserving its meaning. It is the bridge from the human-oriented abstractions of [layer 06](../README.md) back down to the [hardware of layer 04](../../04-computer-architecture/README.md). Its correctness requirement is absolute: the compiled program must do what the source program means, for every input. Its performance goal is pragmatic: run as fast as possible on the real processor.

The unifying idea is **a pipeline of meaning-preserving transformations through progressively lower representations**. Each phase takes one representation, checks or improves it, and produces the next. Text becomes tokens, tokens become a syntax tree, the tree becomes a checked and annotated tree, that becomes an Intermediate Representation (IR), the IR is optimised, and finally it is lowered to machine instructions with physical registers. Splitting the work this way means each phase solves one problem and can be reused: many source languages can share one optimiser and many back ends.

## How the children fit together

```
 source text
   | Lexing and parsing      (front end: is this a legal program? build the tree)
   v
 abstract syntax tree
   | Semantic analysis       (front end: do names and types make sense?)
   v
 annotated tree
   | lowering
   v
 intermediate representation  <--+
   | Optimization                |  (middle end: many passes, each preserving meaning)
   +-----------------------------+
   v
 optimised IR
   | Code generation and register allocation  (back end: target-specific)
   v
 machine code / object file  --> linker (see Runtime Systems)
```

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Lexing and Parsing](lexing-and-parsing.md) | Turns characters into a syntax tree; rejects malformed programs | Finite automata, context-free grammars |
| [Semantic Analysis](semantic-analysis.md) | Resolves names, checks types, annotates the tree | Lexing and parsing; scope and type rules |
| [Intermediate Representations](intermediate-representations.md) | The machine-independent form on which analysis and optimisation work | Semantic analysis |
| [Optimization](optimization.md) | Rewrites IR to run faster or smaller without changing meaning | IRs, dataflow analysis |
| [Code Generation and Register Allocation](code-generation-and-register-allocation.md) | Maps IR onto real instructions and a finite register file | Optimised IR, the target ISA |

The front end (first two children) depends on the source language and not on the machine. The back end (last child) depends on the machine and not on the source language. The IR in the middle is the contract between them. With *m* languages and *n* machines, a shared IR needs *m + n* components instead of *m × n* compilers, which is why LLVM and GCC (the GNU Compiler Collection) are organised this way.

## Connections to sibling areas

- **[Paradigms](../01-paradigms/README.md).** Each paradigm brings compilation problems: closures need closure conversion, dynamic dispatch needs vtables, tail calls need frame reuse, logic programs need unification machinery.
- **[Semantics and Types](../02-semantics-and-types/README.md).** Semantics defines what "correct compilation" means; types are checked in semantic analysis and then used by the optimiser and code generator to pick representations.
- **[Runtime Systems](../04-runtime-systems/README.md).** The compiler's output is completed by the linker and loader, and some languages defer compilation to run time with a Just-In-Time (JIT) compiler. The compiler must also cooperate with the garbage collector, for example by recording where pointers live.
- **[Formal Methods](../05-formal-methods/README.md).** Compilers are themselves programs that can be verified. CompCert (Leroy, 2009) is a C compiler proved in the Coq proof assistant to preserve semantics.

## Connections across layers

Lexers are [finite automata](../../02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) and parsers are [pushdown automata](../../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md). Optimisation is limited by [undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) and uses [graph algorithms](../../05-algorithms-and-data-structures/05-graph-algorithms/README.md), [dynamic programming](../../05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) and fixed-point iteration. Code generation targets the [ISA](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) and schedules for the [pipeline](../../04-computer-architecture/02-processor-microarchitecture/pipelining.md) and [memory hierarchy](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md). Upward, compilers build [operating systems](../../07-operating-systems/README.md), shape [memory-safety](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md) outcomes through how they exploit undefined behaviour, and form the core of [build systems](../../12-software-engineering/04-operations/build-and-continuous-delivery.md) and [static analysers](../../12-software-engineering/03-quality/static-analysis-and-code-review.md).

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): each IR level hides the details of the next.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): the IR separates front ends from back ends.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): the compiler is a pipeline, and it schedules instructions for the processor's pipeline.
- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): every pass must preserve observable behaviour.
- [Recursion and self-reference](../../CROSS-CUTTING.md#recursion-and-self-reference): compilers compile themselves (bootstrapping).
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): optimal code generation is undecidable in general, and its parts (register allocation, scheduling) are NP-hard.
