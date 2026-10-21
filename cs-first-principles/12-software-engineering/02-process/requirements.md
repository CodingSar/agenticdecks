# Requirements

> **Layer:** [12 Software Engineering](../README.md) › [Process](README.md)
> **Builds on:** [Essential and accidental complexity](../01-design/essential-and-accidental-complexity.md), [Predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md)
> **Enables:** [Development lifecycles](development-lifecycles.md), [Software architecture](../01-design/software-architecture.md), [Testing](../03-quality/testing.md), [Reliability engineering](../04-operations/reliability-engineering.md)

## Essence

Requirements say what a system must do and how well, in terms of the world it serves rather than the code inside it. Brooks wrote that "the hardest single part of building a software system is deciding precisely what to build" ("No Silver Bullet", 1986), because no later step can repair a system that solves the wrong problem. Requirements are hard for three reasons: users cannot fully state what they need until they see something working, needs change while the system is built, and natural language is ambiguous. So requirements engineering is less about writing a complete specification up front and more about discovering, stating precisely, prioritising and validating needs, repeatedly.

## Core tenets

1. **Requirements live in the world; specifications live at the interface.** Michael Jackson and Pamela Zave ("Four Dark Corners of Requirements Engineering", 1997) separate the requirement R (a desired condition in the environment, such as "a train never enters an occupied block"), domain knowledge D (facts about the world, such as "trains stop when the signal is red") and the specification S (what the machine does at its interface, such as "set signal red when the block is occupied"). The machine is correct if S together with D implies R. Many failures come from false domain assumptions, not from bad code.
2. **Functional and non-functional requirements shape different things.** Functional requirements (what outputs for which inputs) shape features. Non-functional requirements, or quality attributes (latency under 200 ms at the 99th percentile, 99.9% availability, data kept within the European Union (EU)), shape [architecture](../01-design/software-architecture.md). The second kind is often unstated and discovered late, which makes it expensive.
3. **Users cannot fully specify needs in advance.** People describe what they do today, not what they would do with a new tool, and they leave out what feels obvious. Prototypes, observation of real work, and incremental delivery reveal needs that interviews miss. This is the main argument for [iterative lifecycles](development-lifecycles.md).
4. **Every requirement must be testable or it is a wish.** "The system shall be fast" cannot be checked; "95% of searches return in under 300 ms with 1,000 concurrent users" can. Writing an acceptance test or a measurable target forces the precision that prose lacks, and gives [testing](../03-quality/testing.md) its oracle. Service level objectives in [reliability engineering](../04-operations/reliability-engineering.md) are testable non-functional requirements.
5. **Errors found late cost more to fix.** A misunderstood requirement found in review costs a conversation; found in production it may cost a redesign, a data migration and lost trust. Boehm (*Software Engineering Economics*, 1981) reported large cost multipliers by phase; the exact ratios are debated and smaller in iterative work, but the direction is robust because late fixes must undo more dependent work.
6. **Requirements conflict and must be prioritised.** Stakeholders want different things (security wants friction, sales wants none; legal wants retention limits, analytics wants history). Resolving conflicts is a decision, not a discovery, and someone with authority must own it. Explicit prioritisation, such as MoSCoW (must, should, could, won't), makes trade-offs visible.
7. **Constraints from law and ethics are requirements.** Privacy rules such as the General Data Protection Regulation (GDPR), accessibility standards and safety regulations impose requirements no user asked for. They must be gathered as deliberately as features; see [law, privacy and policy](../../15-computing-in-context/law-privacy-and-policy.md).

## Key concepts

| Term | Meaning |
|---|---|
| Stakeholder | Anyone affected by or with influence over the system: users, operators, owners, regulators |
| Functional requirement | A required behaviour: given these inputs, produce these effects |
| Non-functional requirement | A required quality: performance, availability, security, usability, cost |
| Specification | A precise description of the machine's behaviour at its interface |
| Domain assumption | A fact about the environment that the design relies on |
| Acceptance criterion | A concrete, checkable condition that a feature must satisfy to be accepted |
| User story | A short statement of a need from a user's view ("As a ..., I want ..., so that ..."), used in agile methods |
| Traceability | The ability to link each requirement to the design, code and tests that satisfy it |

## How it fits

- **Below:** precise specifications use [predicate logic](../../01-mathematical-foundations/01-logic/predicate-logic.md); formal ones can be checked by [model checking](../../06-programming-languages/05-formal-methods/model-checking.md), as done for safety-critical and some cloud systems (for example Amazon's use of the Temporal Logic of Actions (TLA+)).
- **Above:** requirements feed [architecture](../01-design/software-architecture.md) (quality attributes), [testing](../03-quality/testing.md) (oracles) and [reliability engineering](../04-operations/reliability-engineering.md) (service level objectives). Human needs are discovered with [Human-Computer Interaction (HCI)](../../14-human-and-visual-computing/01-human-computer-interaction/usability-evaluation.md) methods.
- **Siblings:** [lifecycles](development-lifecycles.md) decide how often requirements are revisited; [Conway's law](conways-law-and-teams.md) explains why requirements spanning several teams are the hardest to deliver.

## Common misconceptions

- **"Get the requirements right first, then build."** For most software, full and stable requirements do not exist at the start. Trying to freeze them produces a precise specification of the wrong system.
- **"Requirements describe the software."** They describe effects in the world. A correct program that relies on a false assumption about the world still fails its requirement.
- **"Non-functional requirements are secondary."** They decide the architecture, and they are the hardest to retrofit. Security and performance added at the end are usually costly and partial.

## Go deeper

- Michael Jackson, *Software Requirements and Specifications* (1995): short essays on the world/machine distinction.
- Pamela Zave and Michael Jackson, "Four Dark Corners of Requirements Engineering", *ACM TOSEM* (1997): the formal relation between requirements, domain and specification.
- Frederick P. Brooks Jr., "No Silver Bullet" (1986): why deciding what to build is the essential difficulty.
