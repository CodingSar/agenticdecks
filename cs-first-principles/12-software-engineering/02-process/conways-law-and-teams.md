# Conway's Law and Teams

> **Layer:** [12 Software Engineering](../README.md) › [Process](README.md)
> **Builds on:** [Modularity and information hiding](../01-design/modularity-and-information-hiding.md), [Graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md), [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md)
> **Enables:** [Software architecture](../01-design/software-architecture.md), [Reliability engineering](../04-operations/reliability-engineering.md)

## Essence

Melvin Conway observed in 1968 ("How Do Committees Invent?") that "organizations which design systems ... are constrained to produce designs which are copies of the communication structures of these organizations." The mechanism is simple: two modules can only work together if the people building them agree on an interface, and people agree most easily with those they talk to often. So module boundaries settle where communication is weak, and tightly coupled parts end up owned by people who talk constantly. Together with Brooks's law, which says communication cost limits how far a project can be sped up by adding people, Conway's law makes team design part of software design.

## Core tenets

1. **Interfaces follow communication paths.** Designing an interface requires negotiation between the people on each side. Where teams are separate, the interface between their parts becomes formal and stable; within a team it stays informal and fluid. The system's dependency graph therefore tends to mirror the organisation's communication graph.
2. **Communication cost grows quadratically.** A team of n people has n(n−1)/2 possible pairs: 10 for 5 people, 45 for 10, 190 for 20. Brooks (*The Mythical Man-Month*, 1975) argued that this overhead, plus the time to train newcomers, is why "adding manpower to a late software project makes it later". Work that cannot be partitioned cleanly behaves like the serial fraction in [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md).
3. **The evidence supports a mirroring effect.** MacCormack, Rusnak and Baldwin ("Exploring the Duality between Product and Organizational Architectures", *Research Policy*, 2012) compared matched pairs of products and found that those built by loosely coupled, distributed organisations were significantly more modular than those built by tightly coupled ones. Studies of failure-prone code at Microsoft likewise found that organisational measures (how many teams touch a file) predicted defects.
4. **You can use the law deliberately.** The "inverse Conway manoeuvre" designs the team structure you want the architecture to have: if you want independent services, create independent teams that each own one, end to end. Fighting the organisation instead produces boundaries that erode back to its shape.
5. **Ownership must match boundaries.** A component with no clear owner decays; one owned by several teams becomes a coordination bottleneck. Assigning each service or module to exactly one team, which builds, deploys and is on call for it ("you build it, you run it"), aligns incentives: the people who make changes feel their operational cost.
6. **Team size is bounded by communication.** Small teams (often cited as five to nine people) can coordinate informally. Beyond that, sub-teams and formal interfaces become necessary. Skelton and Pais (*Team Topologies*, 2019) add cognitive load: a team should own no more than it can understand, which in turn limits how much system any one team can be responsible for.
7. **Brooks proposed structuring teams around design integrity.** His "surgical team" concentrated design in one or two minds, and he argued that **conceptual integrity**, one consistent set of design ideas, is the most important property of a system. Large systems keep it by giving a small group (architects, or owners of core interfaces) authority over the parts that must be consistent.

## Key concepts

| Term | Meaning |
|---|---|
| Conway's law | System structure tends to copy the communication structure of the organisation that builds it |
| Brooks's law | Adding people to a late software project makes it later |
| Communication overhead | Time spent coordinating rather than producing; grows roughly with the number of pairs |
| Inverse Conway manoeuvre | Shaping teams to match the architecture you want |
| Conceptual integrity | The coherence of a system's design ideas, as if from one mind |
| Ownership | A team's responsibility for building, changing and operating a component |
| Cognitive load | The amount a team must understand to own its part of the system safely |

## How it fits

- **Below:** pairs of communicating people form a complete [graph](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) whose edge count grows quadratically; the limit on speedup from adding people has the same shape as [Amdahl's law](../../04-computer-architecture/06-performance/amdahls-law.md) for processors.
- **Above:** decides the practical boundaries of [software architecture](../01-design/software-architecture.md) and on-call scope in [reliability engineering](../04-operations/reliability-engineering.md). It is a human counterpart to coordination costs in [distributed systems](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md): agreement is expensive when parties communicate slowly.
- **Siblings:** [requirements](requirements.md) that cut across teams are slow to deliver; [version control](version-control.md) layout (monorepo or many repos) often mirrors team boundaries; [lifecycles](development-lifecycles.md) set how often teams synchronise.

## Common misconceptions

- **"Conway's law is a joke about bureaucracy."** It is a structural claim with a clear mechanism and empirical support. It applies to well-run organisations as much as badly run ones.
- **"More people means faster delivery."** Only if the work divides into parts with narrow interfaces. Otherwise communication and integration costs grow faster than output.
- **"Reorganising teams is separate from architecture."** Every reorganisation changes which interfaces are cheap to change and which are expensive, so it is an architectural decision.

## Go deeper

- Melvin E. Conway, "How Do Committees Invent?", *Datamation* (1968): the original short paper.
- Frederick P. Brooks Jr., *The Mythical Man-Month* (1975; anniversary ed. 1995): Brooks's law, the surgical team and conceptual integrity.
- Matthew Skelton and Manuel Pais, *Team Topologies* (2019): designing teams around ownership and cognitive load.
