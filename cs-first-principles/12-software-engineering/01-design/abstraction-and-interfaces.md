# Abstraction and Interfaces

> **Layer:** [12 Software Engineering](../README.md) › [Design](README.md)
> **Builds on:** [Modularity and information hiding](modularity-and-information-hiding.md), [Type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), [Hoare logic and program proofs](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md)
> **Enables:** [Design patterns](design-patterns.md), [Software architecture](software-architecture.md), [Testing](../03-quality/testing.md)

## Essence

An abstraction is a simplified view of something that keeps what a user needs and omits the rest. An interface is the concrete form of that view: the operations, their types and the promises about their behaviour. Barbara Liskov and Stephen Zilles ("Programming with Abstract Data Types", 1974) made the idea precise: an abstract data type is defined by its operations and their meaning, not by its representation. A good interface lets the caller reason about the module using only the interface, and lets the implementer change everything behind it without telling anyone. Most of the design work is deciding what the interface promises and, just as important, what it refuses to promise.

## Core tenets

1. **An interface is a contract with two sides.** It states preconditions (what the caller must ensure), postconditions (what the module then guarantees) and invariants (what always holds between calls). Bertrand Meyer called this Design by Contract (*Object-Oriented Software Construction*, 1988). The formal basis is the [Hoare triple](../../06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) `{P} op {Q}`. Writing the contract down, even informally, exposes vague designs.
2. **Types capture part of the contract and check it mechanically.** A signature `withdraw(account: Account, amount: Money) -> Result<Receipt, Error>` rules out whole classes of misuse at compile time. Behaviour that types cannot express (ordering rules, performance, thread-safety) must be documented and tested. The more of the contract the [type system](../../06-programming-languages/02-semantics-and-types/type-systems.md) carries, the less depends on discipline.
3. **Substitutability defines correct subtyping.** The Liskov Substitution Principle (Liskov, 1987; Liskov and Wing, 1994): an implementation of an interface must be usable anywhere the interface is expected without surprising the caller. In contract terms, it may weaken preconditions and strengthen postconditions, never the reverse. A `Square` that breaks a `Rectangle` caller's expectation that width and height vary independently violates it.
4. **Good abstractions are general-purpose but not over-general.** Ousterhout's advice is to make interfaces "somewhat general-purpose": shaped around the concept, not around today's single caller. A text editor's buffer exposing `insert(position, text)` and `delete(range)` serves many features; one exposing `backspace()` serves one. Over-generalising, with hooks for every imagined need, adds interface surface without hiding anything.
5. **Pull complexity downward and define errors out of existence.** If either the caller or the module must deal with some complexity, it is usually better for the module to do it once than for every caller to do it. Ousterhout's example: a `substring` or `delete` that clamps out-of-range indices instead of throwing removes error-handling code from every call site. Exceptions are part of the interface and often its most complex part.
6. **All non-trivial abstractions leak.** Joel Spolsky's "Law of Leaky Abstractions" (2002) observes that hidden details surface under stress: the Transmission Control Protocol's (TCP's) reliable stream stalls when the network does; a virtual-memory array becomes thousands of times slower (up to ~100,000 times on spinning disks) when it pages to storage; an Object-Relational Mapper (ORM) generates a slow query. An interface should document its performance model and failure modes, because callers will depend on them anyway.
7. **Interfaces are expensive to change once they have users.** An implementation can change in one commit. An interface used by many callers needs a migration: add the new form, move callers, remove the old. Published interfaces (public Application Programming Interfaces (APIs), network protocols, file formats) may never be fully retired. So effort spent on interfaces pays more than effort spent on implementations.

## Key concepts

| Term | Meaning |
|---|---|
| Abstraction | A model that keeps relevant properties and suppresses irrelevant detail |
| Interface | The set of operations and promises through which a module is used |
| Abstract data type (ADT) | A type defined by its operations and their behaviour, independent of representation |
| Precondition / postcondition | What must hold before a call / what the module guarantees after it |
| Representation invariant | A condition on the hidden data that every operation preserves |
| Liskov Substitution Principle | Subtypes must honour the supertype's contract |
| Leaky abstraction | An abstraction whose hidden details affect callers in some circumstances |
| API | An interface published for other programs or teams to use |

## How it fits

- **Below:** the same idea runs through the stack: the [Instruction Set Architecture (ISA) contract](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), [system calls](../../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [file-system abstractions](../../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md). Languages supply [polymorphism](../../06-programming-languages/02-semantics-and-types/polymorphism-and-type-inference.md) so one interface can have many implementations.
- **Above:** [testing](../03-quality/testing.md) checks an implementation against its contract; [architecture](software-architecture.md) is mostly about interfaces between large components, such as service APIs and message schemas.
- **Siblings:** [modularity](modularity-and-information-hiding.md) says where to put a boundary; this file says what crosses it. [Design patterns](design-patterns.md) are recurring interface arrangements.

## Common misconceptions

- **"An interface is just the list of method signatures."** Signatures are the syntax. The semantics (what each call means, what it costs, how it fails) is the larger and more important part.
- **"More abstraction layers are always better."** Each layer that merely passes calls through adds code to read and a place for bugs without hiding anything. Ousterhout calls these pass-through methods a red flag.
- **"Subclassing is how you reuse code."** Inheritance couples a subclass to its parent's implementation; composition through an interface usually hides more. This was a central lesson of the *Design Patterns* book.

## Go deeper

- Barbara Liskov and John Guttag, *Abstraction and Specification in Program Development* (1986): specifications, abstraction functions and representation invariants taught rigorously.
- Bertrand Meyer, *Object-Oriented Software Construction*, 2nd ed. (1997): Design by Contract in depth.
- John Ousterhout, *A Philosophy of Software Design* (2018): general-purpose interfaces and defining errors out of existence.
