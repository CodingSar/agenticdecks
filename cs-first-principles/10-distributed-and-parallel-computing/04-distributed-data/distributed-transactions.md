# Distributed Transactions

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Distributed data](README.md)
> **Builds on:** [Atomicity, Consistency, Isolation and Durability (ACID)](../../09-data-management/04-transactions/acid.md), [Concurrency control](../../09-data-management/04-transactions/concurrency-control.md), [Consensus](../03-consensus-and-replication/consensus.md), [Partitioning](partitioning.md)
> **Enables:** [Scalability patterns](../05-large-scale-systems/scalability-patterns.md), [Cloud computing](../05-large-scale-systems/cloud-computing.md)

## Essence

A distributed transaction reads and writes data on several nodes and must still be atomic (all nodes commit or all abort) and isolated (concurrent transactions appear to run one at a time). Atomicity across nodes is the **atomic commitment** problem, classically solved by **two-phase commit (2PC)**: a coordinator asks every participant to prepare, and commits only if all vote yes. Isolation across nodes extends single-node concurrency control with distributed locking or with globally ordered timestamps. The fundamental cost is coordination: extra round trips, durable log writes on every participant, and blocking when the coordinator fails at the wrong moment. Modern systems make 2PC fault-tolerant by running each participant and the coordinator as consensus groups.

## Core tenets

1. **Two-phase commit separates "can you?" from "do it".** Phase 1: the coordinator sends *prepare*; each participant makes the transaction's effects durable, holds its locks, and votes yes or no. A yes vote is a promise: the participant can no longer abort on its own. Phase 2: if every vote is yes, the coordinator durably logs *commit* and tells everyone; otherwise it logs and sends *abort*. The coordinator's log record is the single point at which the decision is made.

2. **2PC blocks if the coordinator fails after participants vote yes.** A prepared participant has given up its right to abort and does not know the decision, so it must hold its locks and wait until the coordinator recovers. Asking other participants helps only if one of them already knows the outcome. This is why 2PC is called a blocking protocol, and why its availability is no better than its coordinator's. Three-phase commit avoids blocking only under synchronous assumptions that real networks violate.

3. **Atomic commit is not consensus, but consensus fixes it.** In atomic commit, every participant has a veto, and one "no" forces abort; in consensus, any proposed value may win. The practical fix is to replicate the coordinator's decision (and each participant's prepared state) with [consensus](../03-consensus-and-replication/consensus.md), so a crashed coordinator is replaced and the decision survives. Gray and Lamport's "Paxos Commit" (2006) formalises this; Spanner and CockroachDB run 2PC over Paxos or Raft groups.

4. **Distributed isolation needs a global order.** Two-phase locking works across nodes if every participant holds locks until commit, but distributed deadlocks then need global detection or timeouts. The alternative is timestamp ordering: each transaction gets a timestamp, and conflicting operations are applied in timestamp order. Generating timestamps that respect real time across machines is the hard part; Spanner uses TrueTime intervals and commit wait, while others use a central timestamp oracle or hybrid logical clocks.

5. **Every participant adds latency and failure exposure.** A transaction across k partitions costs at least two round trips plus durable writes, and it holds locks for that whole time, which reduces concurrency. Its availability is roughly the product of the availabilities of everything it touches. So the best distributed transaction is one avoided by partitioning data so that most transactions are single-partition.

6. **Sagas trade isolation for availability in long workflows.** A saga (Garcia-Molina and Salem, 1987) splits a long business process into local transactions, each with a compensating action that semantically undoes it (refund a charge, release a reservation). If a step fails, earlier steps are compensated. Sagas avoid holding locks across services, but intermediate states are visible to others, so the application must tolerate anomalies that isolation would have prevented.

7. **Exactly-once effects come from idempotence plus atomic recording.** Across a network, a message may be delivered twice or a reply lost, so "exactly once" delivery is impossible in general. What systems actually deliver is exactly-once *effect*: each operation carries a unique identifier, and the receiver atomically applies the operation and records the identifier, discarding duplicates. The transactional outbox pattern applies the same idea: write the outgoing message into the same local transaction as the state change, then publish it asynchronously.

## Key concepts

| Term | Meaning |
|---|---|
| Atomic commitment | All participants commit or all abort |
| Two-phase commit (2PC) | Prepare-and-vote, then commit-or-abort, driven by a coordinator |
| Prepared state | Participant has voted yes and can no longer abort unilaterally |
| In-doubt transaction | Prepared participant waiting for an unknown decision |
| Distributed deadlock | Wait-for cycle spanning several nodes |
| Timestamp oracle | Service that hands out globally ordered transaction timestamps |
| Saga | Chain of local transactions with compensating actions |
| Idempotency key | Unique identifier that lets a receiver discard duplicate requests |
| Transactional outbox | Writing outgoing messages in the same transaction as state changes |

## How it fits

- **Below:** extends [ACID](../../09-data-management/04-transactions/acid.md), [concurrency control](../../09-data-management/04-transactions/concurrency-control.md) and [recovery logging](../../09-data-management/04-transactions/recovery-and-logging.md) to many nodes; uses [consensus](../03-consensus-and-replication/consensus.md) to make the decision fault-tolerant and [clocks](../02-distributed-foundations/time-clocks-and-ordering.md) for timestamp ordering; distributed deadlock is [deadlock](../../07-operating-systems/03-concurrency/deadlock.md) across machines.
- **Above:** [scalability patterns](../05-large-scale-systems/scalability-patterns.md) such as microservices replace distributed transactions with sagas and events; [cloud](../05-large-scale-systems/cloud-computing.md) databases sell globally consistent transactions as a managed service.
- **Siblings:** [partitioning](partitioning.md) decides how often transactions must span nodes; [CRDTs](eventual-consistency-and-crdts.md) are the opposite strategy, avoiding coordination altogether.

## Common misconceptions

- **"2PC is a consensus protocol."** It needs every participant's vote and blocks on coordinator failure; it becomes fault-tolerant only when layered on consensus.
- **"Exactly-once delivery is possible with the right broker."** Delivery can be retried, so duplicates are always possible; exactly-once *processing* is built from deduplication and atomic state updates.
- **"Distributed transactions do not scale, so never use them."** Systems such as Spanner run them at global scale; the cost is latency, which is acceptable for many workloads when transactions are mostly single-partition.

## Go deeper

- Bernstein, Hadzilacos and Goodman, *Concurrency Control and Recovery in Database Systems* (1987): the classical theory, freely available.
- Gray and Lamport, "Consensus on Transaction Commit", *ACM Transactions on Database Systems* (2006).
- Corbett et al., "Spanner: Google's Globally-Distributed Database", OSDI (2012).
- Garcia-Molina and Salem, "Sagas", SIGMOD (1987).
