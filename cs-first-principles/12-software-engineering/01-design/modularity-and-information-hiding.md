# Modularity and Information Hiding

> **Layer:** [12 Software Engineering](../README.md) › [Design](README.md)
> **Builds on:** [Essential and accidental complexity](essential-and-accidental-complexity.md), [Binding, scope and closures](../../06-programming-languages/02-semantics-and-types/binding-scope-and-closures.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md)
> **Enables:** [Abstraction and interfaces](abstraction-and-interfaces.md), [Software architecture](software-architecture.md), [Conway's law and teams](../02-process/conways-law-and-teams.md)

## Essence

A module is a part of a system that can be designed, understood and changed with limited knowledge of the rest. Splitting a system into modules is easy; splitting it so that changes stay inside one module is the hard part. David Parnas gave the criterion in "On the Criteria To Be Used in Decomposing Systems into Modules" (1972): **make each module hide one design decision that is likely to change**, and expose only what other modules need to use it. Dividing by processing steps (read, then sort, then print) feels natural but spreads each decision, such as a data format, across every step. Dividing by secrets keeps each decision in one place.

## Core tenets

1. **Decompose by decisions, not by steps.** Parnas compared two designs of a keyword-in-context (KWIC) index program. The flowchart design (input, circular shift, alphabetise, output) shared one in-memory data layout among all modules, so changing that layout changed every module. The information-hiding design gave each module a secret (how lines are stored, how shifts are represented) behind access functions. Both worked; only the second survived likely changes cheaply.
2. **A module's value is the ratio of what it hides to what it exposes.** Ousterhout calls modules with simple interfaces and large implementations *deep*: Unix file input/output (I/O) hides disk layout, caching, permissions and device drivers behind about five calls (`open`, `read`, `write`, `lseek`, `close`). *Shallow* modules, whose interface is almost as complex as their body, add a name to learn without saving work.
3. **Coupling is what crosses the boundary; cohesion is what stays inside.** Low coupling means a change in one module rarely forces changes in others. High cohesion means a module's parts change for the same reason. Constantine and Yourdon's *Structured Design* (1979) made these the measures of a decomposition; they remain the right questions.
4. **Information leakage is the main failure.** When one decision is reflected in two modules, for example both a writer and a reader know a file format, they are coupled even if neither calls the other. Temporal decomposition (structuring code by the order things happen) is a common cause, because the same data is touched at each stage.
5. **Dependencies form a graph, and its shape matters.** If modules are nodes and "uses" relations are edges, an acyclic graph can be built, tested and understood bottom-up, layer by layer. Cycles force a group of modules to be understood and changed together. Parnas ("Designing Software for Ease of Extension and Contraction", 1979) proposed the "uses" hierarchy so that useful subsets of a system can be delivered.
6. **Hiding must be enforced or it erodes.** A boundary that relies on convention leaks under deadline pressure. Language features (private fields, module export lists, separate compilation), build-system visibility rules and process boundaries enforce it. The stronger the enforcement, the more the boundary costs to cross, which is also the point.
7. **Every observable behaviour becomes part of the interface.** Hyrum's Law (Winters et al., *Software Engineering at Google*, 2020): with enough users, all observable behaviour of an interface will be depended on by somebody, including timing, ordering and error text. Hiding is therefore never perfect, and widely used modules must change slowly and test for compatibility.

## Key concepts

| Term | Meaning |
|---|---|
| Module | A unit of design with an interface and a hidden implementation (function, class, package, service) |
| Information hiding | Placing each changeable design decision inside one module so that others cannot depend on it |
| Secret | The decision a module hides, such as a data representation, algorithm or device detail |
| Coupling | The degree to which modules depend on each other's details |
| Cohesion | The degree to which a module's contents belong together and change together |
| Deep module | A module whose interface is small relative to the functionality it provides |
| Information leakage | One design decision being reflected in more than one module |
| Uses relation | Module A uses B if A's correctness requires a correct B |

## How it fits

- **Below:** relies on language mechanisms for [scope and binding](../../06-programming-languages/02-semantics-and-types/binding-scope-and-closures.md) and for [types](../../06-programming-languages/02-semantics-and-types/type-systems.md) that check use across boundaries. The dependency structure is a directed [graph](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), and acyclic layering is a [topological order](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md).
- **Above:** [software architecture](software-architecture.md) applies the same criterion to services and subsystems; [Conway's law](../02-process/conways-law-and-teams.md) says those boundaries will mirror teams.
- **Siblings:** [abstraction and interfaces](abstraction-and-interfaces.md) describes what the visible side of the boundary should promise; [design patterns](design-patterns.md) are known ways to hide a particular kind of variation; [essential complexity](essential-and-accidental-complexity.md) explains why the work is worth doing.

## Common misconceptions

- **"Modular means small."** Many tiny classes or functions with chatty interfaces raise complexity: each adds an interface to learn. Depth, not size, is the measure.
- **"Information hiding is about secrecy or security."** It is about limiting what other code *can depend on*, so that the hidden part can change. It is a maintainability tool, though it overlaps with the [least-privilege](../../11-security-and-cryptography/01-security-principles/security-design-principles.md) principle.
- **"If modules don't call each other, they are independent."** Shared formats, shared databases and shared assumptions couple modules as strongly as calls do.

## Go deeper

- David L. Parnas, "On the Criteria To Be Used in Decomposing Systems into Modules", *Communications of the ACM* (1972): the founding paper; short and still exact.
- John Ousterhout, *A Philosophy of Software Design* (2018): deep modules, information leakage and temporal decomposition.
- Edward Yourdon and Larry Constantine, *Structured Design* (1979): coupling and cohesion as design measures.
