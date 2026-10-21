# Replication

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Consensus and replication](README.md)
> **Builds on:** [System models and failures](../02-distributed-foundations/system-models-and-failures.md), [Recovery and logging](../../09-data-management/04-transactions/recovery-and-logging.md), [Reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md)
> **Enables:** [Consensus](consensus.md), [Consistency models](consistency-models.md), [Partitioning](../04-distributed-data/partitioning.md), [Content delivery and caching](../../08-networking/05-application-layer/content-delivery-and-caching.md)

## Essence

Replication keeps copies of the same data on several machines, for three reasons: to survive machine loss (durability and availability), to serve more reads (throughput), and to put data near users (latency). Copying immutable data is easy; the whole difficulty is **changes**. Every replication scheme answers two questions: *who may accept a write* (one leader, several leaders, or any replica) and *how many replicas must confirm before the write counts* (all, a majority quorum, or one, with the rest updated later). The answers decide what a client can read, what happens in a failure, and how much latency each write pays.

## Core tenets

1. **Replicate operations in order, not states.** Shipping a log of deterministic changes, in one agreed order, makes all replicas converge to the same state; this is the replicated state machine. Databases replicate their write-ahead log or a logical change log; the order is the hard part, and a single leader is the simplest way to impose it.

2. **Single-leader replication is simple until the leader fails.** All writes go to the leader, which streams its log to followers. Failover is where systems break: deciding the leader is dead needs a timeout (a guess), the new leader may lack the old leader's last writes, and the old leader may still be running and accepting writes (split brain). Safe failover requires consensus on who the leader is and fencing of the old one, which is why leader election is built on [consensus](consensus.md).

3. **Synchronous replication trades latency for durability; asynchronous does the reverse.** Waiting for followers to acknowledge before confirming a write means a confirmed write survives the leader's loss, but every write pays a round trip and a slow follower stalls writes. Asynchronous replication confirms immediately, so a leader crash can lose the last writes that clients were told succeeded. Many systems wait for a majority, which tolerates minority failures without waiting for the slowest replica.

4. **Quorums make overlapping reads and writes see each other.** With n replicas, writing to w and reading from r with w + r > n guarantees that every read set intersects every write set, so a read sees the latest acknowledged write's version. Majority quorums (w = r = ⌊n/2⌋ + 1) tolerate ⌊(n−1)/2⌋ failures, which is why replica groups have 3 or 5 members: 5 survives 2 failures. Quorum overlap is necessary but not sufficient for linearizability; leaderless systems also need read repair and careful handling of concurrent writes.

5. **Multi-leader and leaderless replication accept concurrent conflicting writes.** Letting each data centre or each replica accept writes gives low latency and availability during partitions, but two clients can update the same item at once on different replicas. The system must then detect the conflict (with version vectors) and resolve it: last-writer-wins (which silently drops data), application merge functions, or data types designed to merge automatically ([conflict-free replicated data types, CRDTs](../04-distributed-data/eventual-consistency-and-crdts.md)).

6. **Replication lag creates visible anomalies.** A follower behind the leader serves stale reads. Users notice specific anomalies: a user does not see their own just-posted comment (violating read-your-writes), or sees a value and then an older one on a refresh (violating monotonic reads). These can be prevented by routing a user's reads to the leader for a while, or by tracking the version the client has seen.

7. **Replicas protect against independent failures only.** Copies on the same rack share a power supply and switch; copies running the same software share its bugs; a deleted table replicates its deletion instantly. So replicas are spread across failure domains (racks, availability zones, regions), and replication never replaces backups, which protect against mistakes that replicate.

8. **Primary-backup and chain replication are other points in the space.** In chain replication (van Renesse and Schneider, 2004), writes enter at the head and flow down a chain; the tail answers reads and acknowledges writes, giving strong consistency with high throughput, at the cost of latency proportional to chain length and a separate configuration service to repair the chain.

## Key concepts

| Term | Meaning |
|---|---|
| Leader (primary) | Replica that orders and accepts writes |
| Follower (secondary, replica) | Replica that applies the leader's log |
| Failover | Promoting a follower when the leader is believed dead |
| Split brain | Two nodes both acting as leader at once |
| Quorum | Set of replicas whose acknowledgement makes an operation count |
| w + r > n | Condition for read and write quorums to intersect |
| Replication lag | Delay between a write on the leader and its application on a follower |
| Read-your-writes | A client always sees its own earlier writes |
| Failure domain | Set of components that can fail together |

## How it fits

- **Below:** the replicated log is the [write-ahead log](../../09-data-management/04-transactions/recovery-and-logging.md) of a single database; redundancy for reliability is an [engineering principle](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md) also used in [Redundant Array of Independent Disks (RAID) storage](../../04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) and [error-correcting codes](../../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md); [cache coherence](../../04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md) is replication inside a chip.
- **Above:** [content delivery networks](../../08-networking/05-application-layer/content-delivery-and-caching.md) replicate read-mostly data near users; [partitioned databases](../04-distributed-data/partitioning.md) replicate each partition; [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) sizes replica counts against availability targets.
- **Siblings:** [consensus](consensus.md) makes leader election and log order safe; [consistency models](consistency-models.md) name what each scheme guarantees; [Byzantine fault tolerant (BFT)](byzantine-fault-tolerance.md) replication tolerates lying replicas.

## Common misconceptions

- **"Replication is a backup."** A mistaken delete or corrupting bug is replicated in milliseconds. Backups and point-in-time snapshots are separate.
- **"w + r > n gives strong consistency."** Concurrent writes, failed partial writes and clock-based conflict resolution can still produce non-linearizable reads.
- **"More replicas always improve availability."** Each write must reach more of them, and majority quorums grow; past 5 to 7 replicas, consensus-based groups usually get slower without much benefit.

## Go deeper

- Kleppmann, *Designing Data-Intensive Applications* (2017), chapter "Replication": the clearest survey.
- Schneider, "Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial", *ACM Computing Surveys* (1990).
- DeCandia et al., "Dynamo: Amazon's Highly Available Key-value Store", SOSP (2007): leaderless replication with quorums.
- van Renesse and Schneider, "Chain Replication for Supporting High Throughput and Availability", OSDI (2004).
