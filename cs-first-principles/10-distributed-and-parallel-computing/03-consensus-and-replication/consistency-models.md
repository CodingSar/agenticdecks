# Consistency Models

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Consensus and replication](README.md)
> **Builds on:** [Memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md), [Isolation levels](../../09-data-management/04-transactions/isolation-levels.md), [Time, clocks and ordering](../02-distributed-foundations/time-clocks-and-ordering.md)
> **Enables:** [Eventual consistency and CRDTs](../04-distributed-data/eventual-consistency-and-crdts.md), [Distributed transactions](../04-distributed-data/distributed-transactions.md), [Scalability patterns](../05-large-scale-systems/scalability-patterns.md)

## Essence

A consistency model is a contract between a replicated store and its clients: it says which values a read may return, given the writes that happened. Strong models make many machines behave like one, so programs are easy to reason about, but they need coordination on every operation, which costs latency and, during partitions, availability. Weak models allow replicas to answer locally, so they are fast and available, but clients can see stale or reordered data. The models form a hierarchy from **linearizability** (behaves like a single copy in real time) through **sequential** and **causal** consistency down to **eventual consistency** (replicas agree only after writes stop). Choosing a model is choosing which anomalies your application can tolerate.

## Core tenets

1. **Linearizability: every operation appears to happen at one instant between its start and its end.** If write w completes before read r begins (in real time), r must see w or a later value. It makes a replicated register indistinguishable from a single copy, and it composes: a system of linearizable objects is linearizable (Herlihy and Wing, 1990). It is the C in CAP, and it requires coordination: at least one round trip to a quorum for some operations.

2. **Sequential consistency drops real time but keeps one global order.** All clients see all operations in some single order consistent with each client's program order, but that order need not respect real time across clients (Lamport, 1979). Defined first for multiprocessor memory, it is weaker than linearizability yet still needs global coordination, and unlike linearizability it does not compose.

3. **Causal consistency preserves exactly what could have influenced what.** If an operation causally depends on another (same client, or it read the other's result), every client sees them in that order; concurrent operations may appear in different orders at different replicas. Causal consistency is, in a precise sense, the strongest model that remains available during partitions (Mahajan, Alvisi and Dahlin, 2011, for a natural class of models). It prevents the classic anomaly of seeing a reply before the message it answers.

4. **Eventual consistency promises only convergence.** If writes stop, all replicas eventually return the same value. It says nothing about what reads return in the meantime, and nothing about how conflicting writes are merged; those must be specified separately (last-writer-wins, merge functions, CRDTs). It is the model of leaderless stores, Domain Name System (DNS) caches and many caches in general.

5. **Session guarantees fix the anomalies users actually notice.** Read-your-writes (you see your own updates), monotonic reads (you never go back in time), monotonic writes (your writes apply in order) and writes-follow-reads (a write made after reading x is ordered after x) can be provided per client on top of a weak store by tracking the versions that client has seen (Terry et al., 1994). Together they give causal consistency for one session.

6. **Transaction isolation and replica consistency are different axes.** Isolation levels (serializable, snapshot isolation, read committed) describe how concurrent multi-object transactions interleave; consistency models describe how replicas of single objects agree in time. *Strict serializability* combines both: transactions are serializable and the serial order respects real time. Systems such as Spanner provide it; many "serializable" databases provide only serializability, which may reorder non-overlapping transactions against real time.

7. **Stronger models cost latency in proportion to distance.** A linearizable write in a store replicated across continents needs a majority round trip, roughly 50–150 ms, while an eventually consistent write can return after a local disk write. This is the "else latency versus consistency" half of PACELC, and it is the reason most large systems mix models: strong for money and metadata, weak for timelines, counters and caches.

## Key concepts

| Term | Meaning |
|---|---|
| Linearizability | Single-copy behaviour respecting real-time order of non-overlapping operations |
| Sequential consistency | One global order consistent with each client's program order |
| Causal consistency | Causally related operations seen in the same order by all |
| Eventual consistency | Replicas converge once updates stop |
| Strict serializability | Serializable transactions whose order respects real time |
| Read-your-writes | A client sees its own prior writes |
| Monotonic reads | A client never sees older data after newer data |
| Stale read | Read that misses a write already acknowledged to some client |
| Convergence | All replicas reach the same state after the same set of updates |

## How it fits

- **Below:** the same hierarchy was first defined for shared memory in [memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md); the transaction side comes from [isolation levels](../../09-data-management/04-transactions/isolation-levels.md); causal order is the [happened-before relation](../02-distributed-foundations/time-clocks-and-ordering.md); the trade-off is forced by [CAP and PACELC](../02-distributed-foundations/impossibility-results.md).
- **Above:** [CRDTs](../04-distributed-data/eventual-consistency-and-crdts.md) make eventual consistency well-defined; [distributed transactions](../04-distributed-data/distributed-transactions.md) aim at strict serializability; [scalability patterns](../05-large-scale-systems/scalability-patterns.md) such as caching deliberately accept weaker models; [DNS](../../08-networking/05-application-layer/naming-and-dns.md) and [web caches](../../08-networking/05-application-layer/http-and-the-web.md) are eventually consistent by design.
- **Siblings:** [consensus](consensus.md) is how linearizability is implemented; [replication](replication.md) schemes map onto points in this hierarchy; [BFT](byzantine-fault-tolerance.md) can provide linearizability against lying replicas.

## Common misconceptions

- **"Consistency means the same thing in ACID and CAP."** ACID's C means the database keeps application invariants; CAP's C means linearizability. They are unrelated.
- **"Eventual consistency means data is usually up to date."** It gives no bound on staleness and no rule for merging conflicts unless the system adds one.
- **"Serializable implies linearizable."** Serializability allows an order that contradicts real time; strict serializability does not.

## Go deeper

- Herlihy and Wing, "Linearizability: A Correctness Condition for Concurrent Objects", *ACM TOPLAS* (1990).
- Terry et al., "Session Guarantees for Weakly Consistent Replicated Data", PDIS (1994).
- Viotti and Vukolić, "Consistency in Non-Transactional Distributed Storage Systems", *ACM Computing Surveys* (2016): a map of more than 50 models.
- Bailis et al., "Highly Available Transactions: Virtues and Limitations", VLDB (2014): which isolation levels survive partitions.
