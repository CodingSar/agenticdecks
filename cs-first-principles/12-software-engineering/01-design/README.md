# Design

> **Layer:** [12 Software Engineering](../README.md) › Design
> **Children:** [Essential and accidental complexity](essential-and-accidental-complexity.md) · [Modularity and information hiding](modularity-and-information-hiding.md) · [Abstraction and interfaces](abstraction-and-interfaces.md) · [Design patterns](design-patterns.md) · [Software architecture](software-architecture.md)

## What this area is about

Software design answers one question: **how should a system be divided so that people can understand it and change it?** Any working program has *some* structure, and many structures produce the same behaviour. They differ in what happens next: how much code a change touches, how much a reader must hold in their head, and which mistakes are easy to make. Design is the choice among behaviourally equivalent structures by their cost of change.

The unifying idea is that complexity comes from **dependencies** between parts and from **obscurity** (information a reader needs but cannot see). Good design reduces both by drawing boundaries around decisions that are likely to change, and by making the interface at each boundary much simpler than what lies behind it. Brooks named the part of complexity design can remove; Parnas gave the criterion for drawing boundaries; Liskov and others made the boundary a formal contract; patterns and architecture reuse proven boundary shapes at small and large scale.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Essential and accidental complexity](essential-and-accidental-complexity.md) | Sets the goal: remove accidental complexity, contain essential complexity | none (the starting point) |
| [Modularity and information hiding](modularity-and-information-hiding.md) | Says *where* to draw boundaries: around design decisions likely to change | Complexity |
| [Abstraction and interfaces](abstraction-and-interfaces.md) | Says *what* a boundary looks like: a contract simpler than its implementation | Modularity |
| [Design patterns](design-patterns.md) | Named, reusable arrangements of a few modules and interfaces | Interfaces |
| [Software architecture](software-architecture.md) | The structure of the whole system and the quality attributes it buys | All of the above |

```
  complexity (why) -> modularity (where to cut) -> interfaces (what the cut exposes)
                                                        |
                              patterns (small recurring cuts) -- architecture (system-wide cuts)
```

Read in order. The first file explains why design matters at all: some complexity is inherent and cannot be removed, so it must be contained. The next two give the core method: hide each volatile decision inside one module, behind an interface that says what and not how. Patterns and architecture apply that method at two scales. A pattern such as Strategy or Observer is a few classes arranged to let one dimension vary. An architecture such as layers, microservices or event-driven pipelines arranges whole subsystems, and its choice is mostly decided by quality attributes (availability, latency, deployability) rather than by function.

## Connections to sibling areas

- **[Process](../02-process/README.md):** [Conway's law](../02-process/conways-law-and-teams.md) says module boundaries tend to copy team boundaries, so design and organisation must be planned together. [Requirements](../02-process/requirements.md) tell design which decisions are likely to change.
- **[Quality](../03-quality/README.md):** a module with a narrow interface and hidden state is easy to test in isolation. Hard-to-test code is usually a design smell (hidden dependencies, global state).
- **[Operations](../04-operations/README.md):** architecture decides the unit of deployment and the blast radius of a failure; [observability](../04-operations/observability.md) must be designed in, not added later.

## Connections across layers

Design is the human-scale version of ideas found throughout the stack. The [Instruction Set Architecture (ISA)](../../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) is an interface that hid microarchitecture for decades; the [Operating System (OS)](../../07-operating-systems/01-kernel-and-abstractions/the-role-of-the-os.md) hides devices behind files and processes; the [network stack](../../08-networking/01-principles/layering-and-the-end-to-end-principle.md) is a layered architecture. Languages supply the enforcement: [type systems](../../06-programming-languages/02-semantics-and-types/type-systems.md), visibility rules, and the [object-oriented](../../06-programming-languages/01-paradigms/object-oriented.md) and [functional](../../06-programming-languages/01-paradigms/functional.md) paradigms each offer different module mechanisms. Upward, design principles govern [Machine Learning (ML) systems](../../13-artificial-intelligence/README.md), where data dependencies create new hidden coupling.

## Cross-cutting threads

- [Abstraction and layering](../../CROSS-CUTTING.md#abstraction-and-layering): each module is a small layer hiding its implementation.
- [Interface vs implementation](../../CROSS-CUTTING.md#interface-vs-implementation): the defining move of information hiding.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): dependency injection, virtual dispatch and service discovery decouple caller from callee.
- [Composition](../../CROSS-CUTTING.md#composition): architecture asks which properties survive combining parts.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): every architectural style buys some quality attributes by paying with others.
