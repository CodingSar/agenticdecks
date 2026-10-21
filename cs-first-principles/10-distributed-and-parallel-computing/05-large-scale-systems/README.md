# Large-Scale Systems

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › Large-scale systems
> **Children:** [Batch and stream processing](batch-and-stream-processing.md) · [Cloud computing](cloud-computing.md) · [Scalability patterns](scalability-patterns.md)

## What this area is about

This area is about whole systems that run on thousands of machines and serve millions of users or process petabytes of data: data pipelines, cloud platforms and internet services. The theory of the earlier sections (work and span, failure models, consensus, partitioning) is necessary here but not sufficient. The new forces are **scale** (at 10,000 machines, something is always broken), **cost** (hardware, energy and operator time dominate design decisions) and **change** (software is deployed many times a day while the system runs).

The unifying idea is that large systems succeed by **avoiding coordination and making failure routine**. They partition work so that pieces run independently, make operations idempotent so they can be retried, replace failed machines automatically instead of repairing them, and reserve expensive agreement for a small control plane. The children cover the three canonical forms: data processing frameworks, the shared infrastructure they run on, and the architectural patterns used to build services.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [Batch and stream processing](batch-and-stream-processing.md) | Data-parallel frameworks (MapReduce, Spark, Flink) that hide distribution and recover from failures by recomputation or checkpoints | Data parallelism, partitioning |
| [Cloud computing](cloud-computing.md) | Pooled, virtualised infrastructure rented on demand; the substrate everything else runs on | Virtualization, consensus, networking |
| [Scalability patterns](scalability-patterns.md) | Recurring designs (stateless tiers, caching, sharding, queues, backpressure) that let a service grow | All of the above |

```
   services (scalability patterns)      data pipelines (batch / stream)
               \                           /
                \                         /
          cloud platform: compute, storage, network, control plane
                              |
          consensus-backed metadata  +  partitioned, replicated storage
```

The order is flexible. Batch and stream processing is the most direct application of the parallel-computing section. Cloud computing explains the economic and technical substrate. Scalability patterns pull everything together for request-serving systems. All three share techniques: partitioning, replication, idempotent retries and a small consensus-backed control plane.

## Connections to sibling areas

- **[Parallel computing](../01-parallel-computing/README.md):** batch frameworks are data-parallel programming models extended with fault tolerance; work and span still bound their speed-up, and stragglers are the span problem in practice.
- **[Distributed foundations](../02-distributed-foundations/README.md):** timeouts, retries and leases in production systems are direct consequences of the asynchronous model; grey failures are the main operational nuisance.
- **[Consensus and replication](../03-consensus-and-replication/README.md):** coordination services such as ZooKeeper and etcd run consensus for the whole cluster's metadata, leader election and configuration.
- **[Distributed data](../04-distributed-data/README.md):** sharding and replication of storage are the foundation; shuffles in batch jobs are repartitioning; eventually consistent caches and stores trade freshness for latency.

## Connections across layers

From [07 Operating Systems](../../07-operating-systems/README.md) this area takes [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) and [containers](../../07-operating-systems/07-virtualization/containers.md). From [08 Networking](../../08-networking/README.md) it takes [load-balanced Hypertext Transfer Protocol (HTTP) services](../../08-networking/05-application-layer/http-and-the-web.md), [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md) and [congestion control](../../08-networking/04-transport-layer/congestion-control.md). From [09 Data Management](../../09-data-management/README.md) it takes [query optimisation](../../09-data-management/03-query-processing/query-optimization.md) and [storage layouts](../../09-data-management/02-storage-and-indexing/storage-layouts.md) such as columnar formats. Upward, it is what [12 Software Engineering](../../12-software-engineering/README.md) builds, deploys and operates through [continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md), [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) and [observability](../../12-software-engineering/04-operations/observability.md), and what [13 Artificial Intelligence](../../13-artificial-intelligence/README.md) uses for [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md). Its security relies on [isolation and sandboxing](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) between tenants.

## Cross-cutting threads

- [Virtualization](../../CROSS-CUTTING.md#virtualization): the cloud turns a data centre into an elastic pool.
- [Caching and locality](../../CROSS-CUTTING.md#caching-and-locality): caches absorb most read load in web-scale services.
- [Feedback and control](../../CROSS-CUTTING.md#feedback-and-control): autoscaling and backpressure adjust capacity to load.
- [Batching and amortization](../../CROSS-CUTTING.md#batching-and-amortization): micro-batches and bulk writes amortise per-operation costs.
- [Redundancy and fault tolerance](../../CROSS-CUTTING.md#redundancy-and-fault-tolerance): recomputation, checkpoints and replicas make failure routine.
- [The end-to-end argument](../../CROSS-CUTTING.md#the-end-to-end-argument): exactly-once effects come from end-to-end idempotence, not reliable links.
