# Consensus

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Consensus and replication](README.md)
> **Builds on:** [Impossibility results](../02-distributed-foundations/impossibility-results.md), [System models and failures](../02-distributed-foundations/system-models-and-failures.md), [Replication](replication.md)
> **Enables:** [Distributed transactions](../04-distributed-data/distributed-transactions.md), [Cloud computing](../05-large-scale-systems/cloud-computing.md), [Byzantine fault tolerance](byzantine-fault-tolerance.md), [Model checking](../../06-programming-languages/05-formal-methods/model-checking.md)

## Essence

Consensus is the problem of getting a group of processes to agree on one value even though some may crash and messages may be delayed. Its properties are **agreement** (no two correct processes decide differently), **validity** (the decision was proposed by someone) and **termination** (every correct process eventually decides). Agreeing on one value repeatedly gives agreement on a log, and a log in one agreed order gives a replicated state machine, so consensus is the foundation of leader election, configuration management, locks and strongly consistent databases. Paxos and Raft solve it for crash failures with 2f + 1 nodes, using **majority quorums that always intersect**: any decision is known to at least one member of any later majority, so it can never be contradicted.

## Core tenets

1. **Consensus is equivalent to total-order broadcast and to a replicated log.** If you can agree on one value, you can agree on the value in slot 1, then slot 2, and so on. Conversely, a total-order broadcast lets everyone take the first proposal delivered. So leader election, atomic commit with a coordinator replaced by a group, distributed locks and linearizable storage all reduce to consensus, and none is easier.

2. **Majority quorums carry decisions forward.** With n = 2f + 1 nodes, any two majorities (f + 1 nodes each) share at least one node. A value is chosen only when a majority accepts it, so any later leader that consults a majority hears about it from the overlapping node. This is why the system tolerates f crashes and no more: with more than f down, no majority can form and the group must stop rather than risk disagreement.

3. **Paxos is two phases of "promise, then accept", ordered by ballot numbers.** In Phase 1, a proposer picks a unique ballot number b and asks acceptors to promise to ignore lower ballots; each acceptor replies with the highest-ballot value it has already accepted, if any. In Phase 2, the proposer must propose the value from the highest ballot reported (or its own if none) and asks acceptors to accept it under b. A value accepted by a majority is chosen. The rule "adopt the highest reported value" is the invariant that makes competing proposers converge rather than conflict (Lamport, "The Part-Time Parliament", 1998; "Paxos Made Simple", 2001).

4. **Multi-Paxos and Raft amortise Phase 1 with a stable leader.** Once one leader has won Phase 1 for all future slots, each new log entry needs only one round trip to a majority. Raft (Ongaro and Ousterhout, 2014) packages this as leader election with randomised timeouts and terms, log replication with a consistency check on the previous entry, and a rule that only a node whose log is at least as up to date as a majority's can win election. Raft and Multi-Paxos are close relatives; Raft was designed to be easier to understand and implement correctly.

5. **Safety never depends on timing; liveness does.** Paxos and Raft never let two nodes decide differently, whatever the delays, crashes or message losses. They can, however, fail to make progress: two proposers can keep pre-empting each other with higher ballots, or elections can keep splitting votes. Leader election with randomised timeouts makes this rare once the network is stable. This is exactly the escape from [FLP](../02-distributed-foundations/impossibility-results.md) through partial synchrony.

6. **Durability is part of correctness.** An acceptor's promise and accepted value must be written to stable storage before it replies; otherwise a crash and restart could let it forget a promise and accept a conflicting value. So each consensus step costs a disk flush (often batched) as well as a network round trip, typically around a millisecond inside one data centre and tens of milliseconds across regions.

7. **Real systems need more than the core algorithm.** Membership changes (adding or removing replicas) must themselves go through consensus, using joint consensus or one-at-a-time changes, so that old and new majorities cannot decide independently. Logs must be compacted with snapshots. Reads must be linearizable too, which needs either a round to a majority or a leader lease that relies on bounded clock drift. Most production bugs live in these extensions, not in the core protocol.

8. **Consensus is expensive, so systems use it sparingly.** A consensus group is limited by its leader and its quorum round trips, roughly thousands to hundreds of thousands of operations per second depending on batching. Large systems therefore keep metadata and leadership in a small consensus group (ZooKeeper, etcd, Chubby) and let the bulk data path use cheaper replication under the leaders that group appoints.

## Key concepts

| Term | Meaning |
|---|---|
| Agreement, validity, termination | The three properties defining consensus |
| Ballot (term, epoch) | Monotonic number ordering leadership attempts |
| Proposer, acceptor, learner | Paxos roles: suggests values, votes, learns outcome |
| Chosen value | Value accepted by a majority under one ballot |
| Multi-Paxos | Repeated Paxos with a stable leader skipping Phase 1 |
| Raft term | Election period with at most one leader |
| Log matching | Raft invariant: same index and term implies identical prefixes |
| Total-order broadcast | Delivering the same messages in the same order everywhere |
| Joint consensus | Membership change where both old and new majorities must agree |

## How it fits

- **Below:** quorum intersection is a [combinatorial](../../01-mathematical-foundations/03-discrete-mathematics/combinatorics.md) fact; acceptors' durable state uses [logging](../../09-data-management/04-transactions/recovery-and-logging.md) and [file-system crash consistency](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md); the timeouts rest on the [partial synchrony model](../02-distributed-foundations/system-models-and-failures.md).
- **Above:** [distributed transactions](../04-distributed-data/distributed-transactions.md) run two-phase commit over consensus groups so coordinators cannot block forever; [cloud](../05-large-scale-systems/cloud-computing.md) control planes and container orchestrators store their state in etcd; protocols are specified and checked with [model checking](../../06-programming-languages/05-formal-methods/model-checking.md).
- **Siblings:** [replication](replication.md) uses consensus for leader election and log order; [consistency models](consistency-models.md) describe what a consensus-backed store gives (linearizability); [BFT](byzantine-fault-tolerance.md) generalises consensus to arbitrary faults at 3f + 1.

## Common misconceptions

- **"Raft is a different, simpler kind of algorithm than Paxos."** It is a particular, well-specified form of Multi-Paxos-style leader-based consensus; its safety argument rests on the same quorum intersection.
- **"An even number of nodes adds fault tolerance."** Four nodes need a majority of three, so they tolerate one failure, the same as three nodes, while adding cost.
- **"Consensus guarantees progress."** Only when the network is stable for long enough. During instability it guarantees only that it will not decide inconsistently.

## Go deeper

- Lamport, "Paxos Made Simple", *ACM SIGACT News* (2001): the shortest correct explanation.
- Ongaro and Ousterhout, "In Search of an Understandable Consensus Algorithm", USENIX ATC (2014): Raft.
- Chandra, Griesemer and Redstone, "Paxos Made Live: An Engineering Perspective", PODC (2007): what the papers leave out.
- Howard, Malkhi and Spiegelman, "Flexible Paxos: Quorum Intersection Revisited" (2016): which quorums actually need to intersect.
