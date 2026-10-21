# Reliability Engineering

> **Layer:** [12 Software Engineering](../README.md) › [Operations](README.md)
> **Builds on:** [Reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md), [System models and failures](../../10-distributed-and-parallel-computing/02-distributed-foundations/system-models-and-failures.md)
> **Enables:** [Build and continuous delivery](build-and-continuous-delivery.md), [Ethics and professional responsibility](../../15-computing-in-context/ethics-and-professional-responsibility.md)

## Essence

Reliability engineering keeps a service working well enough for its users while it changes. Site Reliability Engineering (SRE), as described by Google (Beyer, Jones, Petoff and Murphy, *Site Reliability Engineering*, 2016), treats this as a software problem with an explicit, measurable target. The key move is to stop aiming for 100% reliability. Users cannot tell 99.99% from 100% when their own network and devices fail more often than that, and every extra nine costs much more than the last. Instead, pick a **service level objective (SLO)**. The difference between the SLO and perfection is an **error budget**: an allowance of failure that can be spent on shipping changes, and whose exhaustion slows releases down. Reliability then becomes a quantitative trade-off rather than a fight between developers and operators.

## Core tenets

1. **Define reliability from the user's point of view.** A service level indicator (SLI) is a measured ratio such as "fraction of requests served successfully in under 300 ms". An SLO is a target for it over a window ("99.9% over 30 days"). A service level agreement (SLA) is a contract with consequences if the target is missed, and is usually looser than the internal SLO. Measuring server Central Processing Unit (CPU) load instead of user-visible success measures the wrong thing.
2. **Each nine is ten times harder.** 99.9% availability allows about 43 minutes of downtime in 30 days; 99.99% allows about 4.3 minutes; 99.999% about 26 seconds. At four or five nines there is no time for a human to notice and respond, so recovery must be automatic, and every dependency must itself be more reliable than the target.
3. **Dependencies multiply.** If a request needs five services in series, each 99.9% available, the best case is 0.999^5 ≈ 99.5%. Reliability is gained by removing serial dependencies, adding redundancy (replicas fail mostly independently, so two 99% replicas give about 99.99% if failures are truly independent), and degrading gracefully when a non-critical dependency is down.
4. **Availability depends as much on recovery as on failure rate.** With mean time between failures (MTBF) and mean time to repair (MTTR), availability ≈ MTBF / (MTBF + MTTR). Halving repair time improves availability as much as doubling the time between failures, and is often far cheaper. Fast detection, fast rollback and practised incident response are the main levers.
5. **Error budgets align speed and safety.** If the service is well within its SLO, the team may ship faster and take more risk; if the budget is spent, releases slow down and effort shifts to reliability. The rule is agreed in advance, so the decision is mechanical rather than political. This is [feedback control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) on the rate of change.
6. **Most outages are caused by changes.** Google's SRE book reports roughly 70% of outages stem from changes to a live system (binary pushes, configuration changes). So progressive rollout, automatic rollback and treating configuration as code are among the most effective reliability practices.
7. **Complex systems fail in combinations, so blame is useless.** Richard Cook ("How Complex Systems Fail", 1998) observed that serious failures need several faults lining up, and that systems run in a degraded mode all the time. Blameless postmortems ask what in the system allowed the failure, not who erred, because punishing individuals hides information and the same conditions will catch the next person.
8. **Toil must be bounded and automated away.** Toil is manual, repetitive, automatable operational work that scales with service size. Google caps it at 50% of an SRE's time so that the rest goes to engineering that removes it; otherwise operational load grows linearly with the system and swamps the team.

## Key concepts

| Term | Meaning |
|---|---|
| Service level indicator (SLI) | A quantitative measure of service behaviour as users experience it |
| Service level objective (SLO) | A target value or range for an SLI over a time window |
| Service level agreement (SLA) | A contract specifying consequences if service levels are missed |
| Error budget | 1 − SLO: the amount of unreliability permitted in a window |
| MTBF / MTTR | Mean time between failures / mean time to repair (or restore) |
| Graceful degradation | Continuing with reduced function when part of the system fails |
| Blameless postmortem | A written incident analysis focused on systemic causes and follow-up actions |
| Toil | Manual, repetitive, automatable operational work without lasting value |
| Cascading failure | A failure that spreads as overloaded components shift load onto others |

## How it fits

- **Below:** builds on the engineering theory of [reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md) and on [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) of independent and correlated failures. Mechanisms come from [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md), [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) and [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) such as load shedding. Overload behaviour follows [queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md): latency explodes as utilisation nears 100%.
- **Above:** reliability failures in critical systems become questions of [professional responsibility](../../15-computing-in-context/ethics-and-professional-responsibility.md) and, in regulated sectors, [law](../../15-computing-in-context/law-privacy-and-policy.md).
- **Siblings:** [observability](observability.md) produces SLIs and evidence for incidents; [continuous delivery](build-and-continuous-delivery.md) provides the canaries and rollbacks that keep change-induced outages short.

## Common misconceptions

- **"The goal is 100% uptime."** Beyond a point, extra reliability is invisible to users and steals effort from features. The right target is set by user needs and cost.
- **"Redundancy guarantees reliability."** Replicas share software, configuration and operators, so failures correlate. A bad config pushed everywhere takes down every replica at once.
- **"Find the root cause and the person responsible."** Complex failures have several contributing causes. Focusing on one person removes the evidence needed to fix the system.

## Go deeper

- Betsy Beyer, Chris Jones, Jennifer Petoff and Niall Richard Murphy (eds.), *Site Reliability Engineering: How Google Runs Production Systems* (2016): SLOs, error budgets, toil and postmortems.
- Richard I. Cook, "How Complex Systems Fail" (1998): eighteen short observations on failure in complex systems.
- Michael T. Nygard, *Release It!* (2007; 2nd ed. 2018): stability patterns such as timeouts, bulkheads and circuit breakers.
