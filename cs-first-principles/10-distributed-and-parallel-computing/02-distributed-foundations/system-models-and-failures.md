# System Models and Failures

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Distributed foundations](README.md)
> **Builds on:** [Packet switching](../../08-networking/01-principles/packet-switching.md), [Latency, bandwidth and queueing](../../08-networking/01-principles/latency-bandwidth-and-queueing.md), [Reliability and redundancy](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md)
> **Enables:** [Impossibility results](impossibility-results.md), [Consensus](../03-consensus-and-replication/consensus.md), [Byzantine fault tolerance](../03-consensus-and-replication/byzantine-fault-tolerance.md), [Reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md)

## Essence

A system model is the precise list of assumptions a distributed algorithm is allowed to make: how processes can fail, how messages can misbehave, and what is known about timing. It matters because a distributed algorithm is only correct relative to its model, and the same problem (say, agreeing on one value) is easy in one model and provably impossible in another. The two axes are **timing** (synchronous, asynchronous, or partially synchronous) and **failures** (crash-stop, crash-recovery, omission, Byzantine). Correctness itself is split into **safety** (nothing bad ever happens) and **liveness** (something good eventually happens), and most designs guarantee safety always and liveness only when timing is well-behaved.

## Core tenets

1. **In an asynchronous system, a slow node and a dead node look the same.** If message delays and processing speeds have no known upper bound, then no amount of waiting proves that a silent node has crashed; its reply may still be on the way. This single fact underlies the Fischer–Lynch–Paterson (FLP) impossibility result and the need for timeouts that are guesses, not proofs.

2. **Timing models trade realism for power.** A *synchronous* model assumes known bounds on message delay, processing time and clock drift; algorithms can then detect crashes exactly by timeout, but the bounds are rarely guaranteed in practice (a garbage-collection pause or congested switch can exceed any bound). An *asynchronous* model assumes nothing about time; algorithms correct there are robust, but some problems become unsolvable. *Partial synchrony* (Dwork, Lynch and Stockmeyer, 1988) assumes bounds exist but are unknown, or hold only after some unknown time; it matches real networks, which are usually fast and occasionally terrible.

3. **Failure models form a hierarchy of adversary strength.** *Crash-stop*: a process halts and never returns. *Crash-recovery*: it may restart, having lost volatile memory but kept stable storage, so it must log its promises before making them. *Omission*: it fails to send or receive some messages. *Byzantine* (arbitrary): it can do anything, including lying, sending conflicting messages to different peers, or colluding, whether because of a bug, corrupted memory or an attacker. Each stronger model needs more replicas to tolerate f faults: 2f+1 for crash faults with majority quorums, 3f+1 for Byzantine faults.

4. **Networks can lose, delay, duplicate and reorder messages, and can partition.** A partition splits nodes into groups that can talk internally but not to each other. The Transmission Control Protocol (TCP) hides loss, duplication and reordering *within one connection*, but cannot deliver across a partition and cannot tell you whether a request that timed out was processed. So application protocols must tolerate retries, which means making operations idempotent or deduplicating them by request identifier.

5. **Failure detectors are where timing assumptions enter.** A failure detector is a module that outputs suspicions about which nodes have crashed. Chandra and Toueg (1996) showed that consensus becomes solvable in an asynchronous system augmented with even an unreliable detector, provided it is *eventually* accurate (the class ◇S, equivalently the weakest one, Ω, which eventually names one correct leader everywhere). Heartbeats with adaptive timeouts are the practical implementation.

6. **Every specification separates safety from liveness.** Safety properties ("two nodes never decide different values", "a committed write is never lost") can be violated in a finite prefix of an execution. Liveness properties ("every request eventually gets a response") can only be violated by infinite executions. The usual design stance is to keep safety under all asynchrony and failures, and to accept that liveness depends on the network calming down.

7. **In large systems, failure is constant, and partial failures are the hard ones.** With 10,000 servers, each failing once every few years, several fail each day. The worst failures are not clean crashes but grey failures: a disk that is slow but not dead, a node that answers health checks but drops real requests, a network that loses 1% of packets in one direction. Such failures defeat simple detectors.

8. **Fail-stop behaviour is engineered, not given.** Systems often convert messy failures into simple ones: a node that detects an internal inconsistency kills itself (crash rather than corrupt), checksums turn silent data corruption into detected omissions, and fencing tokens stop a node that was wrongly declared dead from acting on stale authority.

## Key concepts

| Term | Meaning |
|---|---|
| Synchronous model | Known bounds on message delay, processing time and clock drift |
| Asynchronous model | No timing bounds at all |
| Partial synchrony | Bounds exist but are unknown, or hold only after an unknown time |
| Crash-stop | Process halts permanently and silently |
| Crash-recovery | Process may restart with stable storage intact |
| Byzantine failure | Arbitrary behaviour, including malicious or inconsistent messages |
| Network partition | Nodes split into groups that cannot communicate |
| Failure detector | Module that outputs (possibly wrong) suspicions of crashed nodes |
| Safety | Nothing bad happens; violations are finite and observable |
| Liveness | Something good eventually happens |

## How it fits

- **Below:** the [network](../../08-networking/01-principles/packet-switching.md) supplies best-effort delivery with [queueing delay](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) that has no hard bound; [crash consistency](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md) and [logging](../../09-data-management/04-transactions/recovery-and-logging.md) make crash-recovery possible; [reliability engineering in hardware](../../00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md) supplies failure rates.
- **Above:** [consensus](../03-consensus-and-replication/consensus.md) and [replication](../03-consensus-and-replication/replication.md) are designed for crash-recovery under partial synchrony; [Byzantine fault tolerance](../03-consensus-and-replication/byzantine-fault-tolerance.md) for the Byzantine model; [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) and [observability](../../12-software-engineering/04-operations/observability.md) deal with grey failures in practice.
- **Siblings:** [Clocks](time-clocks-and-ordering.md) explain what ordering is possible in these models; [impossibility results](impossibility-results.md) prove what is not.

## Common misconceptions

- **"TCP makes the network reliable."** It makes one connection reliable while both ends are alive and connected. It cannot tell a sender whether its last request was processed before the connection broke.
- **"A timeout means the other node is dead."** It means you stopped waiting. The node may be alive and may even have completed your request.
- **"Byzantine means malicious."** It means arbitrary. Bit flips and software bugs can cause Byzantine behaviour with no attacker involved.

## Go deeper

- Cachin, Guerraoui and Rodrigues, *Introduction to Reliable and Secure Distributed Programming* (2nd ed., 2011): precise models and abstractions.
- Dwork, Lynch and Stockmeyer, "Consensus in the Presence of Partial Synchrony", *Journal of the ACM* (1988): the model that real protocols use.
- Kleppmann, *Designing Data-Intensive Applications* (2017), chapter "The Trouble with Distributed Systems": the practitioner's view.
