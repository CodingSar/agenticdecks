# Software Architecture

> **Layer:** [12 Software Engineering](../README.md) › [Design](README.md)
> **Builds on:** [Modularity and information hiding](modularity-and-information-hiding.md), [Abstraction and interfaces](abstraction-and-interfaces.md), [System models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md)
> **Enables:** [Reliability engineering](../04-operations/reliability-engineering.md), [Build and continuous delivery](../04-operations/build-and-continuous-delivery.md), [Conway's law and teams](../02-process/conways-law-and-teams.md)

## Essence

Software architecture is the set of structural decisions about a whole system that are expensive to change: how it is divided into components, how they communicate, where state lives, and what is deployed together. Functional requirements rarely decide architecture, since almost any structure can compute the right answer. **Quality attributes** decide it: availability, latency, throughput, security, modifiability, deployability and cost. Each architectural style buys some of these by paying with others. So architecture is the explicit management of trade-offs at the scale of the system, and its decisions should be recorded with their reasons because the reasons, not the boxes, are what later engineers need.

## Core tenets

1. **Architecture is the decisions that are hard to reverse.** Choosing a programming language, splitting into services, choosing a database, or picking synchronous versus asynchronous communication each shapes thousands of later lines. Bass, Clements and Kazman (*Software Architecture in Practice*) define architecture as the structures needed to reason about the system: elements, relations and their properties. If a decision is cheap to change later, it is design, not architecture.
2. **Quality attributes drive structure, and they conflict.** A layered monolith is simple to reason about and fast in-process, but every change redeploys everything. Microservices allow independent deployment and scaling, but turn function calls into network calls that can fail, add latency (roughly 0.1–1 ms per call within a data centre, including serialisation, versus nanoseconds in-process) and lose cross-service transactions. Caching improves latency but complicates consistency. No style wins on all attributes.
3. **Every architecture is a few recurring styles combined.** Shaw and Garlan (*Software Architecture*, 1996) catalogued them: layers (each uses only the one below), pipes and filters (stream transformation, as in Unix shells and [batch processing](../../10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md)), client-server, event-driven publish-subscribe, repository (a shared central store), and plug-in or microkernel. Naming the style tells you its known strengths and failure modes.
4. **Distribution changes the failure model.** Once components talk over a network, a call may succeed, fail, or time out with unknown outcome. Deutsch's "fallacies of distributed computing" (the network is reliable, latency is zero, bandwidth is infinite, and so on) list the assumptions that local design silently makes. Distributed architectures need timeouts, retries with idempotency, and partial-failure handling everywhere; see [system models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md).
5. **Data ownership is the hardest boundary.** Splitting code is easy; splitting a database is hard, because shared tables are shared [information leakage](modularity-and-information-hiding.md). A service that owns its data behind an Application Programming Interface (API) can evolve its schema; services sharing a database cannot. Cross-boundary consistency then needs patterns such as sagas or event logs rather than [distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md).
6. **Architecture must fit the organisation.** By [Conway's law](../02-process/conways-law-and-teams.md), a system's structure tends to mirror the communication structure of the teams that build it. A service boundary that cuts across team lines will be under constant pressure; one that matches a team's ownership is stable.
7. **Record decisions and their reasons.** An architecture decision record (ADR), proposed by Michael Nygard (2011), is a short document stating context, decision and consequences. Code shows what was built; only the record shows which alternatives were rejected and why, which prevents later engineers from repeating old debates or unknowingly breaking a constraint.

## Key concepts

| Term | Meaning |
|---|---|
| Quality attribute | A measurable non-functional property such as availability, latency or modifiability |
| Architectural style | A named family of structures with known constraints and trade-offs (layers, pipes and filters, event-driven) |
| Monolith | A system built and deployed as one unit, possibly well modularised inside |
| Microservices | Independently deployable services, each owning its data, communicating over a network |
| Coupling in time | Whether components must be available simultaneously (synchronous calls) or not (queues) |
| Blast radius | How much of the system a single failure or bad change can affect |
| Architecture decision record (ADR) | A short, versioned note capturing one architectural decision with its context and consequences |

## How it fits

- **Below:** architectures are built from Operating System (OS) [processes](../../07-operating-systems/02-process-management/processes.md) and [containers](../../07-operating-systems/07-virtualization/containers.md), network protocols such as the [HyperText Transfer Protocol (HTTP)](../../08-networking/05-application-layer/http-and-the-web.md), and databases chosen for their [data model](../../09-data-management/01-data-models/non-relational-models.md). Large-scale styles reuse [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) and [partitioning](../../10-distributed-and-parallel-computing/04-distributed-data/partitioning.md).
- **Above:** architecture sets the unit of [deployment](../04-operations/build-and-continuous-delivery.md) and the boundaries along which [reliability](../04-operations/reliability-engineering.md) and [observability](../04-operations/observability.md) work.
- **Siblings:** it is [modularity](modularity-and-information-hiding.md) and [interfaces](abstraction-and-interfaces.md) applied at the largest scale; [design patterns](design-patterns.md) are its small-scale counterpart.

## Common misconceptions

- **"Microservices are the modern architecture; monoliths are legacy."** Microservices trade in-process simplicity for deployment independence, which pays off mainly when many teams must ship independently. A well-modularised monolith is often the better start.
- **"Architecture is decided up front and then implemented."** Requirements and scale change; good architecture is revised as quality-attribute needs become clear, ideally while changes are still cheap.
- **"The architecture is the diagram."** The diagram is a summary. The real architecture is what the code and deployment actually do, which drifts from the diagram unless checked.

## Go deeper

- Mary Shaw and David Garlan, *Software Architecture: Perspectives on an Emerging Discipline* (1996): the classic catalogue of styles.
- Len Bass, Paul Clements and Rick Kazman, *Software Architecture in Practice* (3rd ed., 2012): quality attributes and tactics.
- Martin Kleppmann, *Designing Data-Intensive Applications* (2017): architectural trade-offs for data systems, grounded in mechanism.
