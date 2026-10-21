# Semantics and Types

> **Layer:** [06 Programming Languages](../README.md) › Semantics and Types
> **Children:** [Syntax and Semantics](syntax-and-semantics.md) · [Binding, Scope and Closures](binding-scope-and-closures.md) · [Type Systems](type-systems.md) · [Polymorphism and Type Inference](polymorphism-and-type-inference.md)

## What this area is about

This area answers two questions: *what does a program mean*, and *which programs should we refuse to run*? Without a precise answer to the first, a compiler cannot be called correct, two implementations of the same language will disagree, and nobody can prove anything about a program. Without an answer to the second, every error surfaces only when the faulty line happens to execute, perhaps in production.

The unifying idea is that **meaning is defined compositionally and checked statically**. The meaning of a whole program is built from the meanings of its parts, following the grammar's structure. Names get their meaning from the scope that binds them. A type system then assigns every expression a type by rules that also follow the grammar, and a sound type system guarantees that well-typed programs never reach certain bad states. Polymorphism and inference keep this checking from being a burden: one definition can serve many types, and the compiler can work out the types itself.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Syntax and Semantics](syntax-and-semantics.md) | Separates form from meaning; the three styles of formal semantics | Grammars, logic |
| [Binding, Scope and Closures](binding-scope-and-closures.md) | How names connect to the entities they denote, and how long those entities live | Syntax and semantics |
| [Type Systems](type-systems.md) | Static rules that classify expressions and rule out errors; soundness | Syntax, binding |
| [Polymorphism and Type Inference](polymorphism-and-type-inference.md) | Reusing code across types; letting the compiler find types | Type systems, unification |

```
 syntax (what can be written)
   -> binding (what each name refers to)
     -> semantics (what it computes)          -> compilers must preserve this
     -> types (what it is guaranteed not to do) -> formal methods extend this
        -> polymorphism and inference (generality without annotation burden)
```

Read them in order. Syntax and semantics sets up the distinction everything else uses. Binding is the first semantic question any language must answer, and closures are where binding meets lifetime. Type systems are a static approximation of semantics: they predict, before running, a property that every run will have. Polymorphism and inference are the extensions that make strong static types practical.

## Connections to sibling areas

- **[Paradigms](../01-paradigms/README.md).** Each paradigm has a natural semantic style: state transitions for imperative code, substitution for functional code, logical consequence for logic code. Object-oriented subtyping and functional parametric polymorphism are the two main forms of polymorphism.
- **[Compilers](../03-compilers/README.md).** The front end implements this area: parsing implements syntax, [semantic analysis](../03-compilers/semantic-analysis.md) implements scope and type rules, and every optimisation must preserve the semantics defined here.
- **[Runtime Systems](../04-runtime-systems/README.md).** Closures that escape their defining scope force heap allocation and hence garbage collection; dynamic typing moves type checks into the runtime.
- **[Formal Methods](../05-formal-methods/README.md).** Hoare logic is an axiomatic semantics. Dependent types extend type systems until types can state full specifications.

## Connections across layers

The foundations are in [layer 01](../../01-mathematical-foundations/README.md) and [layer 02](../../02-theory-of-computation/README.md): [context-free grammars](../../02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md) define syntax, the [lambda calculus](../../02-theory-of-computation/03-computability/lambda-calculus.md) is the standard core for semantics and types, and [propositional](../../01-mathematical-foundations/01-logic/propositional-logic.md) and [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md) supply inference rules. [Rice's theorem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) explains why static types must be conservative. Upward, types underpin [memory safety](../../11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md), [interfaces between modules](../../12-software-engineering/01-design/abstraction-and-interfaces.md) and [static analysis](../../12-software-engineering/03-quality/static-analysis-and-code-review.md).

## Cross-cutting threads

- [Invariants and correctness](../../CROSS-CUTTING.md#invariants-and-correctness): a type is an invariant the compiler checks everywhere.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): binding and environments are naming at the language level.
- [Limits and impossibility](../../CROSS-CUTTING.md#limits-and-impossibility): no decidable type system accepts exactly the safe programs.
- [Composition](../../CROSS-CUTTING.md#composition): compositional semantics and typing rules let meaning scale.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): a type signature is a machine-checked interface.
