# Paradigms

> **Layer:** [06 Programming Languages](../README.md) › Paradigms
> **Children:** [Imperative and Procedural](imperative-and-procedural.md) · [Object-Oriented](object-oriented.md) · [Functional](functional.md) · [Logic and Declarative](logic-and-declarative.md)

## What this area is about

A paradigm is a model of what a program *is*. In the imperative view a program is a sequence of commands that change state. In the object-oriented view it is a collection of objects that hold state and respond to messages. In the functional view it is an expression to be evaluated, built from functions without hidden state. In the logic and declarative view it is a description of the answer, and a solver finds it.

All four are equally powerful: each can simulate the others, because each is Turing complete. They differ in what they make *easy to say and easy to reason about*. The unifying question is: **where does the program keep its state, and who controls the order of evaluation?** Imperative code keeps state in mutable memory and fixes the order explicitly. Object-oriented code partitions that state into encapsulated objects. Functional code removes mutation, so order mostly stops mattering. Declarative code hands the order to an engine entirely.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Imperative and Procedural](imperative-and-procedural.md) | The baseline: commands over mutable memory, mirroring the machine | The Instruction Set Architecture (ISA) and Turing machines |
| [Object-Oriented](object-oriented.md) | Groups state with the code allowed to touch it; dispatches by run-time type | Imperative (state), plus indirection |
| [Functional](functional.md) | Programs as expressions and pure functions; state made explicit | The lambda calculus |
| [Logic and Declarative](logic-and-declarative.md) | Programs as specifications; an engine chooses the evaluation strategy | Predicate logic, search |

```
   control order explicit  <------------------------------>  control order implicit
   Imperative --> Object-oriented --> Functional --> Logic / declarative
   (Turing machine)                   (lambda calculus)  (predicate logic)
```

Read imperative first, because it is closest to the hardware and every other paradigm is eventually compiled into it. Object orientation is a disciplined way to organise imperative state. Functional programming starts from a different root (Church's lambda calculus rather than Turing's machine), and declarative programming moves further still, from "how" to "what". Real languages mix paradigms: Python, Scala, Rust, C# and modern Java combine imperative, object and functional features, and Structured Query Language (SQL) embeds a declarative core inside imperative applications.

## Connections to sibling areas

- **[Semantics and Types](../02-semantics-and-types/README.md).** Each paradigm has a natural semantics: state transitions for imperative code, substitution for functional code, proof search for logic code. Type systems are richest in functional languages, where they began.
- **[Compilers](../03-compilers/README.md).** Compilers lower every paradigm to the same imperative machine code. Closures, dynamic dispatch and unification each need specific compilation techniques.
- **[Runtime Systems](../04-runtime-systems/README.md).** Object-oriented and functional languages allocate many short-lived objects, which is why they almost always rely on garbage collection; dynamic dispatch is a main target of Just-In-Time (JIT) compilation.
- **[Formal Methods](../05-formal-methods/README.md).** Pure functional code is easiest to prove, because equals can be replaced by equals; imperative code needs Hoare logic to reason about state.

## Connections across layers

The imperative paradigm is the [ISA](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) with names added, and its roots are in [Turing machines](../../02-theory-of-computation/03-computability/turing-machines.md). The functional paradigm grows from the [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md); the logic paradigm grows from [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md). Upward, paradigms shape [software design](../../12-software-engineering/01-design/README.md) (design patterns are largely object-oriented idioms), [data management](../../09-data-management/01-data-models/relational-algebra-and-sql.md) (SQL is declarative) and [parallel programming](../../10-distributed-and-parallel-computing/01-parallel-computing/parallel-programming-models.md) (immutability makes parallelism safe).

## Cross-cutting threads

- [State and time](../../CROSS-CUTTING.md#state-and-time): the paradigms differ mainly in how they treat mutable state.
- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): procedures, objects and higher-order functions are three ways to abstract.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): virtual method tables and first-class functions are both indirect calls.
- [Composition](../../CROSS-CUTTING.md#composition): pure functions compose predictably; shared mutable state does not.
