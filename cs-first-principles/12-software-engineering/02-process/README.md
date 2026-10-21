# Process

> **Layer:** [12 Software Engineering](../README.md) › Process
> **Children:** [Requirements](requirements.md) · [Development lifecycles](development-lifecycles.md) · [Version control](version-control.md) · [Conway's law and teams](conways-law-and-teams.md)

## What this area is about

Design decides the shape of the code. Process decides how a group of people, over time, discovers what to build, builds it in steps, and keeps a coherent record of every change. Its central problem is **coordination under uncertainty**: nobody knows the full requirements at the start, people misunderstand each other, and the cost of communication grows with team size. Brooks's law, "adding manpower to a late software project makes it later" (*The Mythical Man-Month*, 1975), states the problem bluntly: new people need training and add communication paths, and the work does not divide perfectly.

The idea that unifies the children is **feedback**. Requirements are hypotheses about what users need; a lifecycle sets how quickly those hypotheses are tested against reality; version control makes every step recorded and reversible, so small steps are safe; and team structure decides who must talk to whom for a change to happen. Process that shortens and cheapens the feedback loop tends to win, because software's main risk is building the wrong thing well.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Requirements](requirements.md) | Define what problem the system must solve, and for whom | [Essential complexity](../01-design/essential-and-accidental-complexity.md) |
| [Development lifecycles](development-lifecycles.md) | Order the work and set the length of the feedback loop | Requirements |
| [Version control](version-control.md) | Record every change, allow parallel work and safe reversal | Lifecycles (small steps need cheap history) |
| [Conway's law and teams](conways-law-and-teams.md) | Relate the system's structure to the organisation's | All three, plus [architecture](../01-design/software-architecture.md) |

```
  what to build      in what order       how changes are kept      who builds which part
  requirements  -->  lifecycle      -->  version control     <-->  teams (Conway's law)
       ^                  |
       +---- feedback ----+
```

Start with [requirements](requirements.md): Brooks called deciding precisely what to build the hardest part of the job. [Lifecycles](development-lifecycles.md) then explain why the industry moved from long plan-driven phases to short iterations: requirements change and are only discovered by showing working software. [Version control](version-control.md) is the mechanism that makes frequent, parallel, reversible change possible. Finally, [Conway's law](conways-law-and-teams.md) ties the process back to design: the organisation's communication structure ends up in the system's structure, whether planned or not.

## Connections to sibling areas

- **[Design](../01-design/README.md):** design is where requirements turn into structure. Team boundaries and module boundaries must match, which makes [architecture](../01-design/software-architecture.md) as much an organisational decision as a technical one.
- **[Quality](../03-quality/README.md):** code review and continuous integration run on top of version control; requirements give tests their oracle (what "correct" means).
- **[Operations](../04-operations/README.md):** [continuous delivery](../04-operations/build-and-continuous-delivery.md) is the operational end of an iterative lifecycle; production incidents and metrics feed new requirements.

## Connections across layers

Process is the most human part of the stack. Its quantitative side borrows from [queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) (work in progress and lead time follow Little's law, L = λW) and from [graph theory](../../01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) (n people have n(n−1)/2 possible communication pairs). Version control is built on [hash functions](../../11-security-and-cryptography/02-cryptography/hash-functions-and-macs.md) and directed acyclic graphs. Requirements meet [human-computer interaction](../../14-human-and-visual-computing/01-human-computer-interaction/README.md) where needs are discovered by watching users, and [law and policy](../../15-computing-in-context/law-privacy-and-policy.md) where regulations become requirements.

## Cross-cutting threads

- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): iterative lifecycles are a control loop on the product.
- [State and time](../../CROSS-CUTTING.md#state-and-time): version control is a history of state, with merges as concurrent updates to reconcile.
- [Indirection and naming](../../CROSS-CUTTING.md#indirection-and-naming): branches and tags are movable names for immutable, content-addressed commits.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): large batches of change amortise release overhead but delay feedback; modern process shrinks batch size.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): predictability versus adaptability in choosing a lifecycle.
