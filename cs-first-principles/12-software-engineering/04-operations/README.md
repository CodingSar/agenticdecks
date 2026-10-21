# Operations

> **Layer:** [12 Software Engineering](../README.md) › Operations
> **Children:** [Build and continuous delivery](build-and-continuous-delivery.md) · [Reliability engineering](reliability-engineering.md) · [Observability](observability.md)

## What this area is about

Software delivers value only when it runs in front of users, and most modern software runs as a continuously operated service rather than a shipped product. Operations asks: **how do we turn source code into a running system, change it many times a day, keep it working, and learn what it is actually doing?** Once a system is live, failures are certain: disks die, networks partition, deploys go wrong, load spikes. The question is not whether things fail but how quickly the failure is detected, contained and repaired.

The unifying idea is **closing the loop between change and production**. Build and delivery pipelines make every change reproducible, tested and reversible. Reliability engineering sets explicit targets for how well the service must work and uses the gap between target and reality, the error budget, to decide how fast to change. Observability provides the measurements that make detection and diagnosis possible. The DevOps movement and Google's Site Reliability Engineering (SRE) practice both came from the same observation: separating the people who change systems from the people who run them creates opposing incentives, while treating operations as a software problem aligns them.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Build and continuous delivery](build-and-continuous-delivery.md) | Turn every commit into a tested, deployable artifact and release it safely | [Version control](../02-process/version-control.md), [testing](../03-quality/testing.md) |
| [Reliability engineering](reliability-engineering.md) | Define how reliable the service must be and manage risk to that target | Observability (to measure), delivery (to roll back) |
| [Observability](observability.md) | Make the internal state of a running system inferable from its outputs | [Architecture](../01-design/software-architecture.md) (what to instrument) |

```
   commit --> build --> test --> artifact --> canary --> full rollout
                                                 |             |
                                         observe (metrics, logs, traces)
                                                 |
                              objective met?  yes: keep shipping   no: roll back, spend less budget
```

Read [build and continuous delivery](build-and-continuous-delivery.md) first: it is the mechanism by which every change reaches production. [Observability](observability.md) and [reliability engineering](reliability-engineering.md) depend on each other: you cannot keep a promise you cannot measure, and measurements matter only relative to a promise. Together the three form a control loop: deploy a change, observe its effect, compare with the target, and adjust the rate of change.

## Connections to sibling areas

- **[Design](../01-design/README.md):** [architecture](../01-design/software-architecture.md) sets the deployable units and the failure boundaries. Graceful degradation, timeouts and retries are designed, not operated in.
- **[Process](../02-process/README.md):** continuous delivery is the operational end of an iterative [lifecycle](../02-process/development-lifecycles.md); [team ownership](../02-process/conways-law-and-teams.md) decides who is on call.
- **[Quality](../03-quality/README.md):** pre-release tests catch what they can; canaries, feature flags and production monitoring catch the rest. Incident investigation is [debugging](../03-quality/debugging.md) under time pressure with only recorded evidence.

## Connections across layers

Operations runs on the infrastructure of lower layers: [containers](../../07-operating-systems/07-virtualization/containers.md) and [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) as deployment units, [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) for elastic capacity, [replication](../../10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) and [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) for redundancy, and [load balancing and caching](../../08-networking/05-application-layer/content-delivery-and-caching.md) for traffic. Its thinking comes from [reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md) and [feedback control](../../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md). Its stakes appear in [ethics and professional responsibility](../../15-computing-in-context/ethics-and-professional-responsibility.md) when outages harm people.

## Cross-cutting threads

- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): error budgets throttle release velocity; autoscaling adjusts capacity to load.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): replicas, multiple zones and rollback paths.
- [Pipelining and parallelism](../../CROSS-CUTTING.md#pipelining-and-parallelism): delivery pipelines overlap stages; builds parallelise across machines.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): build caches reuse outputs whose inputs have not changed.
- [Tradeoffs](../../CROSS-CUTTING.md#tradeoffs): reliability versus velocity, and each extra nine of availability against its cost.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): small, frequent releases reduce risk per release.
