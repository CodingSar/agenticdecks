# Design Patterns

> **Layer:** [12 Software Engineering](../README.md) › [Design](README.md)
> **Builds on:** [Abstraction and interfaces](abstraction-and-interfaces.md), [Object-oriented programming](../../06-programming-languages/01-paradigms/object-oriented.md), [Functional programming](../../06-programming-languages/01-paradigms/functional.md)
> **Enables:** [Software architecture](software-architecture.md), [Static analysis and code review](../03-quality/static-analysis-and-code-review.md)

## Essence

A design pattern is a named, reusable solution to a problem that recurs in a context, described with its trade-offs. The idea comes from the architect Christopher Alexander (*A Pattern Language*, 1977) and entered software through Gamma, Helm, Johnson and Vlissides, the "Gang of Four" (*Design Patterns: Elements of Reusable Object-Oriented Software*, 1994), which catalogued 23 patterns. Most patterns do one thing: they isolate a single dimension of variation (which algorithm, which object to create, who gets notified) behind an interface, so that dimension can change without touching the rest. Their main value is a shared vocabulary; their main risk is applying them where nothing varies.

## Core tenets

1. **A pattern is a problem, a context and a solution with consequences.** "Observer" is not a class diagram; it is the problem "many objects must react when one changes, and the subject should not know who they are", solved by a subscription interface, with the consequence that update order and cascades become hard to reason about. Without the forces and consequences, a pattern is cargo cult.
2. **Most patterns encapsulate what varies.** Strategy hides which algorithm runs; Factory hides which concrete class is built; Adapter hides a mismatched interface; Iterator hides how a collection is traversed; Decorator lets behaviour be added in layers. Each is [information hiding](modularity-and-information-hiding.md) applied to one recurring kind of change.
3. **Prefer composition to inheritance.** The Gang of Four's two principles were "program to an interface, not an implementation" and "favour object composition over class inheritance". Inheritance fixes the relationship at compile time and exposes the parent's internals to the child (the "fragile base class" problem); composition lets parts be swapped at run time through a narrow interface.
4. **Many patterns are workarounds for missing language features.** Peter Norvig observed (1996) that 16 of the 23 Gang of Four patterns become invisible or simpler in languages with first-class functions, dynamic types or multiple dispatch. Strategy is a function argument; Command is a closure; Visitor is pattern matching on an algebraic data type. A pattern names a need; a language may meet it directly.
5. **Patterns exist at every scale.** Idioms are patterns within one language (resource acquisition is initialization (RAII) in C++). Design patterns arrange a few classes. Architectural patterns arrange a whole system (layers, pipes and filters, publish-subscribe). Distributed-systems patterns (retry with backoff, circuit breaker, idempotency keys) arrange services. The same reasoning applies at each scale.
6. **Every pattern adds indirection, and indirection has a price.** An extra interface makes the code more flexible and harder to follow: a reader must find which implementation runs. A pattern is justified only if the variation it supports is real or very likely. Applying patterns speculatively is a main source of accidental complexity.
7. **Anti-patterns name recurring mistakes.** God object (one class knows everything), shotgun surgery (one change touches many classes), and the Singleton used as hidden global state are named so that reviewers can point to them quickly. Martin Fowler's "code smells" (*Refactoring*, 1999) serve the same role for small-scale structure.

## Key concepts

| Term | Meaning |
|---|---|
| Design pattern | A named solution to a recurring design problem in a context, with its trade-offs |
| Creational patterns | Patterns that hide how objects are created (Factory Method, Builder) |
| Structural patterns | Patterns that compose objects into larger structures (Adapter, Decorator, Composite) |
| Behavioural patterns | Patterns that distribute responsibility and communication (Strategy, Observer, Visitor) |
| Dependency injection | Passing a module its collaborators instead of letting it construct them, so they can be replaced |
| Anti-pattern | A commonly used structure that predictably causes problems |
| Refactoring | Changing code structure without changing its observable behaviour |
| Code smell | A surface symptom that usually indicates a deeper design problem |

## How it fits

- **Below:** patterns are expressed with language mechanisms: [object-oriented](../../06-programming-languages/01-paradigms/object-oriented.md) dynamic dispatch, [functional](../../06-programming-languages/01-paradigms/functional.md) higher-order functions and [closures](../../06-programming-languages/02-semantics-and-types/binding-scope-and-closures.md), and [parametric polymorphism](../../06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md).
- **Above:** [software architecture](software-architecture.md) uses the same thinking with services in place of objects. Patterns give [code reviewers](../03-quality/static-analysis-and-code-review.md) a compact language for design feedback, and some smells can be detected by static analysis.
- **Siblings:** a pattern is a specific arrangement of [interfaces](abstraction-and-interfaces.md) that realises [information hiding](modularity-and-information-hiding.md) for a common kind of change.

## Common misconceptions

- **"Using more patterns makes code better designed."** Patterns solve specific problems. Used where that problem is absent, they add indirection and nothing else.
- **"Design patterns are an object-oriented thing."** The catalogue was written for C++ and Smalltalk, but the problems are universal. Functional and systems code have their own patterns (monads, actors, ring buffers), and many Gang of Four patterns survive as plain functions.
- **"Patterns are invented."** The Gang of Four documented solutions they had seen work repeatedly in existing systems. A pattern earns its name from recurrence.

## Go deeper

- Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software* (1994): the original catalogue; read the introduction even if you skip the patterns.
- Christopher Alexander et al., *A Pattern Language* (1977): the source of the pattern form.
- Martin Fowler, *Refactoring: Improving the Design of Existing Code* (1999; 2nd ed. 2018): how to move code toward better structure safely.
