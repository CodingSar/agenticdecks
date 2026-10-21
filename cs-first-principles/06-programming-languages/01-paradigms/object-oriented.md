# Object-Oriented Programming

> **Layer:** [06 Programming Languages](../README.md) › [Paradigms](README.md)
> **Builds on:** [Imperative and procedural programming](imperative-and-procedural.md), [Binding, scope and closures](../02-semantics-and-types/binding-scope-and-closures.md), [Hazards and branch prediction](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md)
> **Enables:** [Design patterns](../../12-software-engineering/01-design/design-patterns.md), [Abstraction and interfaces](../../12-software-engineering/01-design/abstraction-and-interfaces.md), [Just-in-time compilation](../04-runtime-systems/jit-compilation.md)

## Essence

Object-oriented programming (OOP) organises a program as a set of objects, each bundling some private state with the operations allowed to read or change it. Code asks an object to do something by sending it a message (calling a method), and the object itself decides, at run time, which code runs. That late decision, called dynamic dispatch, lets new kinds of objects be added without changing the code that uses them. The paradigm came from simulation (Simula 67, Dahl and Nygaard) and from Alan Kay's Smalltalk, and it became the dominant way to structure large imperative programs. The single idea is **encapsulated state plus dynamic dispatch**: callers depend on what an object promises, never on how it is built.

## Core tenets

1. **Encapsulation protects invariants.** If only an object's own methods can touch its fields, then any invariant those methods preserve (a balance never negative, a list always sorted) holds at every call boundary. This turns a global reasoning problem ("who might have changed this?") into a local one.
2. **Dynamic dispatch selects code by the receiver's run-time class.** A call `shape.area()` runs `Circle.area` or `Square.area` depending on the object, not on the variable's declared type. This is subtype polymorphism: code written against an interface works for all present and future implementations.
3. **Dispatch is implemented by indirection through a table.** In C++, Java and C#, each object holds a pointer to its class's virtual method table (vtable), an array of function pointers. A virtual call loads that pointer, indexes the table and jumps. The cost is one or two extra memory loads plus an indirect branch that may defeat inlining; Just-In-Time (JIT) compilers recover much of this by inline caching.

   ```
   obj --> [ vptr | fields... ]
              |
              v
           vtable: [ &Circle::area | &Circle::draw | ... ]
   ```

4. **Inheritance mixes two separate things: reuse and subtyping.** Inheriting from a class both copies its implementation and declares "my objects can stand in for yours". The two can conflict. The fragile base class problem is when a harmless-looking change in a parent breaks a child that relied on its internals. This is why modern guidance says "prefer composition over inheritance" and why languages such as Go and Rust offer interfaces or traits without implementation inheritance.
5. **Subtyping must respect behaviour, not just signatures.** The Liskov Substitution Principle (Liskov and Wing, 1994) says a subtype must honour every promise of its supertype: it may accept more inputs and promise more, never less. A `Square` that inherits from a mutable `Rectangle` breaks this, because code that sets width and height independently will fail.
6. **Objects are closures, and closures are objects.** An object is a set of functions sharing captured private state; a closure is a function with captured state. Each can encode the other. This is why functional and object-oriented languages converge in practice (Scala, Kotlin, Swift).
7. **The expression problem marks OOP's trade-off.** With classes, adding a new data variant (a new shape) is easy, but adding a new operation (export to a vector-drawing format) means editing every class. Functional programming with algebraic data types has the reverse trade-off. The visitor pattern and type classes are attempts to get both.

## Key concepts

| Term | Meaning |
|---|---|
| Object | A run-time entity with identity, private state and behaviour |
| Class | A template that defines the fields and methods of its instances |
| Encapsulation | Restricting access to state so only the object's methods can change it |
| Dynamic dispatch | Choosing the method body at run time from the receiver's actual class |
| Virtual method table (vtable) | Per-class array of method pointers used to implement dispatch |
| Inheritance | Defining a class by extending another, reusing its fields and methods |
| Subtype polymorphism | Using a value of a subtype wherever its supertype is expected |
| Interface / trait | A named set of method signatures with no (or default-only) implementation |
| Liskov Substitution Principle | Subtypes must preserve the observable contract of their supertypes |

## How it fits

- **Below:** OOP is built on [imperative](imperative-and-procedural.md) mutable state and on indirection: vtables are arrays of function pointers, and dispatch relies on the processor's indirect branch and its [branch predictor](../../04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md).
- **Above:** OOP vocabulary shaped [design patterns](../../12-software-engineering/01-design/design-patterns.md) and much of [software architecture](../../12-software-engineering/01-design/software-architecture.md). Its typing questions belong to [polymorphism and type inference](../02-semantics-and-types/polymorphism-and-type-inference.md). Allocation-heavy object graphs drive the need for [garbage collection](../04-runtime-systems/memory-management-and-garbage-collection.md).
- **Siblings:** OOP organises the state that [imperative](imperative-and-procedural.md) code mutates. [Functional](functional.md) programming reaches the same modularity goals with closures and modules instead of objects. [Logic programming](logic-and-declarative.md) has no notion of encapsulated state at all.

## Common misconceptions

- **"OOP means inheritance."** Kay's original emphasis was messaging and encapsulation. Many successful object systems (Go, Rust traits, JavaScript prototypes) have little or no class inheritance.
- **"Virtual calls are slow."** The cost is a few nanoseconds at most on modern hardware, and JIT compilers often devirtualise hot calls entirely. The real cost is lost inlining, which matters only in tight loops.
- **"Private fields make a program secure."** Access modifiers are a compile-time discipline for programmers, not a security boundary; reflection or memory corruption can bypass them.

## Go deeper

- Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, *Design Patterns* (1994): the canonical catalogue of object-oriented structure.
- Barbara Liskov and Jeannette Wing, "A Behavioral Notion of Subtyping" (1994): the precise meaning of substitutability.
- Bertrand Meyer, *Object-Oriented Software Construction* (2nd ed., 1997): classes as contracts, with preconditions, postconditions and invariants.
