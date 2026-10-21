# Cloud Computing

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Large-scale systems](README.md)
> **Builds on:** [Virtual machines and hypervisors](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md), [Containers](../../07-operating-systems/07-virtualization/containers.md), [Consensus](../03-consensus-and-replication/consensus.md), [Replication](../03-consensus-and-replication/replication.md)
> **Enables:** [Build and continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md), [Reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md), [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md)

## Essence

Cloud computing turns data centres into pooled resources (compute, storage, networking and higher-level services) that customers rent on demand through an Application Programming Interface (API) and pay for by use. Its economics come from **statistical multiplexing**: many customers' peaks do not coincide, so a shared pool needs far less capacity than the sum of private ones, and the provider amortises hardware, power and operations across them. Its technology comes from **virtualisation and automation**: hypervisors and containers carve machines into isolated slices, and a software control plane allocates, monitors and replaces them without humans. The result lets a team treat infrastructure as code and capacity as elastic, at the cost of depending on a provider and sharing hardware with strangers.

## Core tenets

1. **Pooling works because demand is bursty and uncorrelated.** A single company sized for its peak leaves most servers idle most of the time; aggregating many independent workloads smooths the total, raising utilisation. This is the same statistical multiplexing that makes [packet switching](../../08-networking/01-principles/packet-switching.md) more efficient than reserved circuits. It also explains the limits: correlated demand (a global event) or correlated failure (a region outage) breaks the averaging.

2. **Service models differ by what the customer still manages.** Infrastructure as a Service (IaaS) rents virtual machines, disks and networks; the customer runs the operating system (OS) and everything above. Platform as a Service (PaaS) and managed services (databases, queues) take over the runtime and operations. Function as a Service (FaaS), often called serverless, runs short functions on demand and bills per invocation, so idle code costs nothing; the price is cold-start latency and limits on state and run time. Each step up trades control for less operational work.

3. **Separating control plane from data plane is the core architecture.** The control plane decides (where a virtual machine runs, which servers back a load balancer, what the routing tables say) and keeps its state in consensus-backed stores. The data plane does the work (forwarding packets, serving reads) using the latest decisions, and keeps working from cached configuration if the control plane is down. This keeps expensive coordination out of the per-request path and limits the damage a control-plane outage causes.

4. **Disaggregated storage makes compute disposable.** Cloud designs keep durable state in replicated network storage services (object stores, replicated block devices, managed databases), not on the machine's local disk. Compute instances then become interchangeable: a failed one is replaced, not repaired, and capacity can be added in seconds. Object stores offer very high durability by replicating or erasure-coding data across failure domains, though bulk throughput and latency differ from local disks.

5. **Failure domains are explicit and must be used.** Providers expose regions (geographically separate) and availability zones (separate power and network within a region, a few milliseconds apart). An application is only as resilient as its spread: running in one zone means a zone outage is your outage. Replicating across regions protects against regional failure but pays tens of milliseconds per synchronous write.

6. **Orchestration is a control loop over declared state.** Systems like Kubernetes (descended from Google's Borg) store the desired state (run 10 copies of this container) and run controllers that repeatedly compare it with observed state and act to close the gap. This reconciliation pattern tolerates lost messages and crashed controllers, since the next loop iteration repairs whatever was missed, and makes autoscaling a feedback loop on measured load.

7. **Multi-tenancy makes isolation a security boundary.** Customers share physical machines, so hypervisor and container isolation must keep them from reading each other's memory or degrading each other's performance. Side-channel attacks across tenants (for example through shared caches and speculative execution) are a real threat, which is why providers use dedicated hardware isolation and lightweight virtual machines for untrusted code.

## Key concepts

| Term | Meaning |
|---|---|
| Elasticity | Adding and removing capacity automatically as load changes |
| Statistical multiplexing | Sharing capacity among uncorrelated demands to raise utilisation |
| IaaS / PaaS / FaaS | Rent machines / a managed platform / per-invocation functions |
| Control plane | Components that decide configuration and placement |
| Data plane | Components that carry the actual traffic or requests |
| Region / availability zone | Geographic area / independent failure domain within it |
| Object storage | Flat, replicated, web-accessed store of immutable blobs |
| Orchestrator | System that schedules containers and reconciles desired with actual state |
| Multi-tenancy | Many customers sharing the same physical infrastructure |

## How it fits

- **Below:** [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) and [containers](../../07-operating-systems/07-virtualization/containers.md) provide isolated slices; [replication](../03-consensus-and-replication/replication.md) and [consensus](../03-consensus-and-replication/consensus.md) keep control-plane state; [data-centre networks](../../08-networking/README.md) connect everything; [power limits](../../04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) and [energy costs](../../00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) shape data-centre design.
- **Above:** [continuous delivery](../../12-software-engineering/04-operations/build-and-continuous-delivery.md), [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) and [observability](../../12-software-engineering/04-operations/observability.md) assume programmable infrastructure; [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md) rents thousands of accelerators; [isolation](../../11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) and [side channels](../../11-security-and-cryptography/03-system-security/side-channels.md) define its security; [privacy law](../../15-computing-in-context/law-privacy-and-policy.md) constrains where data may live.
- **Siblings:** [batch and stream processing](batch-and-stream-processing.md) runs on elastic clusters; [scalability patterns](scalability-patterns.md) describe how services use elasticity well.

## Common misconceptions

- **"The cloud is someone else's reliable computer."** Individual instances fail routinely; reliability comes from the customer's architecture across zones, not from any single machine.
- **"Serverless means no servers to think about."** Servers, cold starts, concurrency limits and per-invocation costs all still shape the design.
- **"The cloud is always cheaper."** Pooling saves money for variable load; steady, predictable load at scale can be cheaper on owned hardware.

## Go deeper

- Barroso, Hölzle and Ranganathan, *The Datacenter as a Computer* (3rd ed., 2018): warehouse-scale computing from first principles.
- Armbrust et al., "A View of Cloud Computing", *Communications of the ACM* (2010): the economic argument.
- Verma et al., "Large-scale Cluster Management at Google with Borg", EuroSys (2015).
- Burns et al., "Borg, Omega, and Kubernetes", *ACM Queue* (2016): the reconciliation pattern.
