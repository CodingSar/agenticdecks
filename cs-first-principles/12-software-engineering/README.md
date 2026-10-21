# 12 Software Engineering

> **Layer:** 12 Software Engineering
> **Children:** [Design](01-design/README.md) · [Process](02-process/README.md) · [Quality](03-quality/README.md) · [Operations](04-operations/README.md)

## What this area is about

Programming is making a computer do something. Software engineering is keeping that working while the code, the people and the requirements all change. Titus Winters puts it as "programming integrated over time" (Winters, Manshreck and Wright, *Software Engineering at Google*, 2020): a script you run once and throw away needs no engineering, but a system that must survive ten years, a hundred contributors and a thousand requirement changes does. Time adds two forces that pure programming ignores. Things change (dependencies, hardware, laws, users), so the code must be cheap to change. And many people touch the code, so it must be understandable by people who did not write it.

The one idea that unifies this layer is **managing complexity**. Fred Brooks argued that software is hard mainly because of *essential* complexity: the problem itself is intricate, changes constantly, must conform to arbitrary outside systems, and is invisible ("No Silver Bullet", 1986). David Parnas showed that the way you divide a system into modules decides how far a change spreads ("On the Criteria To Be Used in Decomposing Systems into Modules", 1972). John Ousterhout defines complexity operationally as anything that makes a system hard to understand or modify, and traces it to two causes, dependencies and obscurity (*A Philosophy of Software Design*, 2018). Every practice in this layer, from information hiding to code review to error budgets, is a way to keep the cost of the next change bounded.

## Why this layer sits here

Software engineering uses every technical layer below it, because a real system is built from all of them at once:

- It designs with the abstractions of [programming languages](../06-programming-languages/README.md): types, modules and interfaces are the raw material of [modularity](01-design/modularity-and-information-hiding.md).
- It deploys onto [operating systems](../07-operating-systems/README.md), [networks](../08-networking/README.md) and [distributed systems](../10-distributed-and-parallel-computing/README.md), whose partial failures are what [reliability engineering](04-operations/reliability-engineering.md) exists to manage.
- It stores state in [data systems](../09-data-management/README.md) and must evolve their schemas without downtime.
- It treats [security](../11-security-and-cryptography/README.md) as a practice applied at every step (threat models in design, memory-safe languages, review, patching), which is why it sits above layer 11.
- It borrows its limits from [theory](../02-theory-of-computation/README.md): [undecidability](../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) is why no tool can find every bug and why testing can only sample behaviour.

What the layers above need from it: [machine learning](../13-artificial-intelligence/README.md) systems are software systems with extra data dependencies, and they inherit every problem here (versioning, testing, monitoring) plus new ones. [Human and visual computing](../14-human-and-visual-computing/README.md) supplies the user-facing half of [requirements](02-process/requirements.md), and [computing in context](../15-computing-in-context/README.md) asks who is responsible when engineered systems fail.

The abstraction this layer contributes is **the change**: a reviewed, tested, versioned, deployable delta to a running system. Design makes changes local, process coordinates who makes them, quality checks them, and operations ships and observes them.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Design](01-design/README.md) | Decide the structure so that most changes touch one module | Languages (06), the theory of complexity |
| [Process](02-process/README.md) | Decide what to build, in what order, by whom, and record every change | Design (structure mirrors teams) |
| [Quality](03-quality/README.md) | Gain confidence that a change is correct before it ships | Design (testable seams), Process (review, history) |
| [Operations](04-operations/README.md) | Build, ship and run the change, and learn from production | All three above |

```
   requirements --> design --> code --> review/test --> build --> deploy --> observe
        ^                                                                       |
        +----------------------- feedback from users and incidents <-----------+
```

Read [design](01-design/README.md) first: it holds the ideas (essential complexity, information hiding, interfaces) that every other part refers to. [Process](02-process/README.md) adds people and time: [requirements](02-process/requirements.md) define the problem, [lifecycles](02-process/development-lifecycles.md) set the length of the feedback loop, [version control](02-process/version-control.md) records history, and [Conway's law](02-process/conways-law-and-teams.md) ties the system's shape to the organisation's. [Quality](03-quality/README.md) is the set of filters a change passes through. [Operations](04-operations/README.md) closes the loop: the fastest feedback about whether software works comes from running it.

The loop is the point. Every modern practice in this layer shortens it, because a short loop turns big, risky, rarely tested changes into small, cheap, frequently tested ones. Forsgren, Humble and Kim (*Accelerate*, 2018) found that teams who deploy more often also have *lower* change failure rates, so speed and stability are not a trade-off at the level of the whole process.

## Connections to neighbouring layers

- **[06 Programming Languages](../06-programming-languages/README.md):** languages provide the mechanisms (modules, types, visibility, exceptions); software engineering decides how to use them. Static [type systems](../06-programming-languages/02-semantics-and-types/type-systems.md) are the most widely deployed form of [static analysis](03-quality/static-analysis-and-code-review.md).
- **[07 Operating Systems](../07-operating-systems/README.md):** the Operating System (OS) is the canonical case study in layered design and in hiding hardware behind stable interfaces. [Containers](../07-operating-systems/07-virtualization/containers.md) are the unit of modern deployment.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md):** services fail partially, so [reliability engineering](04-operations/reliability-engineering.md) and [observability](04-operations/observability.md) are mostly about distributed failure. Architecture choices such as microservices are distribution choices.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md):** [security design principles](../11-security-and-cryptography/01-security-principles/security-design-principles.md) such as least privilege and economy of mechanism are software-design principles applied to adversaries.
- **[13 Artificial Intelligence](../13-artificial-intelligence/README.md):** learned components have behaviour specified by data rather than code, which weakens testing and review; [evaluation](../13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md) becomes part of quality.
- **[14 Human and Visual Computing](../14-human-and-visual-computing/README.md):** [usability evaluation](../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md) is requirements validation with real users.
- **[15 Computing in Context](../15-computing-in-context/README.md):** the 1968 North Atlantic Treaty Organization (NATO) conference that named "software engineering" was a response to a [historical](../15-computing-in-context/history-of-computing.md) "software crisis"; [professional responsibility](../15-computing-in-context/ethics-and-professional-responsibility.md) is the ethical side of engineering practice.

## Connections across layers

From below, this layer takes the guarantee that each lower abstraction mostly holds: the [Instruction Set Architecture (ISA) contract](../04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md), the [system-call interface](../07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md), [the Transmission Control Protocol's (TCP's)](../08-networking/04-transport-layer/udp-and-tcp.md) reliable byte stream, a database's [atomic, consistent, isolated, durable (ACID)](../09-data-management/04-transactions/acid.md) transactions. Much of the hard work happens where those guarantees leak, such as timeouts, partial failures and resource exhaustion. From [engineering method](../00-engineering-foundations/05-engineering-method/README.md) it takes the habit of [measurement](../00-engineering-foundations/05-engineering-method/measurement-and-modeling.md) and explicit [trade-offs](../00-engineering-foundations/05-engineering-method/tradeoffs-and-constraints.md). Upward, it gives Artificial Intelligence (AI) and human-facing systems the means to be built, shipped and maintained at all.

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the main tool against complexity; deep modules hide much behind little.
- [Interface vs implementation](../CROSS-CUTTING.md#interface-vs-implementation): Parnas's information hiding is this principle made into a design method.
- [Composition](../CROSS-CUTTING.md#composition): architecture is about which properties survive when components are combined.
- [Feedback and control](../CROSS-CUTTING.md#feedback-and-control): continuous delivery, error budgets and postmortems are control loops on the development process.
- [Redundancy and fault tolerance](../CROSS-CUTTING.md#redundancy-and-fault-tolerance): replicas, canaries and rollbacks keep a service up while it changes.
- [Trust and verification](../CROSS-CUTTING.md#trust-and-verification): testing, review and static analysis are layered checks, none sufficient alone.
- [Tradeoffs](../CROSS-CUTTING.md#tradeoffs): reliability versus feature velocity is made explicit by an error budget.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): Rice's theorem bounds every analysis tool; Brooks's law bounds adding people.
