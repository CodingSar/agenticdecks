# Impossibility Results

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Distributed foundations](README.md)
> **Builds on:** [System models and failures](system-models-and-failures.md), [Time, clocks and ordering](time-clocks-and-ordering.md), [Halting problem and undecidability](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md), [Proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md)
> **Enables:** [Consensus](../03-consensus-and-replication/consensus.md), [Consistency models](../03-consensus-and-replication/consistency-models.md), [Byzantine fault tolerance](../03-consensus-and-replication/byzantine-fault-tolerance.md), [Eventual consistency and conflict-free replicated data types (CRDTs)](../04-distributed-data/eventual-consistency-and-crdts.md)

## Essence

A handful of theorems mark the boundaries of what distributed systems can do; their value lies in their exact assumptions. **Two Generals**: no protocol over a lossy channel guarantees that two parties agree to act together. **FLP** (Fischer, Lynch and Paterson): no deterministic protocol guarantees consensus in an asynchronous system if even one process may crash. **Byzantine bound**: agreement with f arbitrary faults needs n ≥ 3f + 1 processes, unless the system is synchronous and messages are signed. **CAP** (Consistency, Availability, Partition tolerance): during a network partition, a replicated register cannot be both linearizable and available. Every practical protocol escapes one by changing an assumption.

## Core tenets

1. **Two Generals: common knowledge cannot be reached over an unreliable channel.** Two parties communicate by messages that may be lost. Suppose a protocol guarantees both act or neither does, and take its shortest run in which they act. Drop the last message: the sender's view is unchanged, so it still acts, and the receiver must then act too, without that message. So a shorter run also works, contradicting minimality. No finite exchange of acknowledgements makes both sides certain, so systems settle for probabilistic or eventual agreement, or for one side owning the decision.

2. **FLP: deterministic asynchronous consensus is impossible with one crash.** Fischer, Lynch and Paterson (1985) proved that in the asynchronous model with reliable message delivery, no deterministic algorithm can guarantee that all non-faulty processes decide the same value (agreement), that the value was proposed (validity), and that they always decide in finite time (termination), if even one process may crash-stop. The proof shows there is always an undecided ("bivalent") configuration from which some message delay keeps the system undecided forever. The result is about *termination*, not safety: protocols can keep agreement and validity always, and lose only the guarantee of finishing.

3. **Every consensus protocol escapes FLP through a stated door.** *Partial synchrony*: Paxos and Raft are always safe and terminate once message delays settle below the timeout. *Failure detectors*: an eventually accurate leader oracle (Ω) is enough. *Randomisation*: Ben-Or (1983) showed that coin flips give termination with probability 1. Each adds an assumption FLP excluded.

4. **Byzantine agreement needs n ≥ 3f + 1.** Lamport, Shostak and Pease (1982) proved that in a synchronous system with f arbitrarily faulty processes and unauthenticated (oral) messages, agreement is possible if and only if n ≥ 3f + 1. In the core case, n = 3 and f = 1, a loyal lieutenant told "attack" by the commander and "the commander said retreat" by the other lieutenant cannot tell which one lies. With unforgeable signatures, the synchronous problem is solvable for any number of faults. In partially synchronous or asynchronous models, n ≥ 3f + 1 is required even with signatures: a node can wait for only n − f replies (f may be silent), up to f of those may be lies, so honest replies (n − 2f) must outnumber liars (f).

5. **CAP is a theorem about one register under one partition.** Brewer's conjecture (2000), proved by Gilbert and Lynch (2002): in an asynchronous network that can lose messages, no read/write register can be both *linearizable* (consistency, C) and *available*, meaning every request to a non-failed node eventually gets a non-error response (A), in the presence of network partitions (P). Proof sketch: split the nodes, write on one side, read on the other; either the read waits (unavailable) or returns stale data (not linearizable).

6. **CAP is widely misread.** It does not say "pick any two of three": partitions are not optional, so the choice is only what to do *during* a partition. Its C means linearizability, not the C in ACID (Atomicity, Consistency, Isolation and Durability), and its A means every non-failed node responds, far stronger than "high uptime". Outside partitions it says nothing, yet the everyday trade-off lives there: PACELC (Abadi, 2012) adds that Else, with no partition, systems trade Latency against Consistency. A system claiming to be "CA" (consistent and available) is assuming partitions away.

7. **Some costs are lower bounds, not impossibilities.** Any linearizable replicated register needs a round trip to a quorum on some operations, so its latency is at least the network distance to a majority. Crash-tolerant consensus without synchrony needs n ≥ 2f + 1 so that any two quorums intersect. Synchronous consensus with f crash failures needs f + 1 rounds in the worst case.

## Key concepts

| Term | Meaning |
|---|---|
| Agreement | No two correct processes decide different values |
| Termination | Every correct process eventually decides |
| Bivalent configuration | A state from which both decision values are still reachable |
| 3f + 1 bound | Minimum processes to tolerate f Byzantine faults (without synchrony plus signatures) |
| Linearizability | Every operation appears to take effect at one instant between its call and return |
| CAP availability | Every request to a non-failed node eventually gets a non-error response |
| PACELC | Partition: Availability vs Consistency; Else: Latency vs Consistency |

## How it fits

- **Below:** proofs by contradiction and indistinguishability, the same [proof techniques](../../01-mathematical-foundations/01-logic/proof-techniques.md) as the [halting problem](../../02-theory-of-computation/03-computability/halting-problem-and-undecidability.md).
- **Above:** [consensus](../03-consensus-and-replication/consensus.md) protocols choose how to escape FLP; [consistency models](../03-consensus-and-replication/consistency-models.md) map the design space CAP opens; [Byzantine fault tolerant (BFT)](../03-consensus-and-replication/byzantine-fault-tolerance.md) protocols are sized by 3f + 1; [CRDTs](../04-distributed-data/eventual-consistency-and-crdts.md) choose availability; [cryptographic signatures](../../11-security-and-cryptography/02-cryptography/public-key-cryptography.md) change what the Byzantine bound requires.
- **Siblings:** [system models](system-models-and-failures.md) supply the assumptions; [clocks](time-clocks-and-ordering.md) show that causal order is cheap, while agreement is not.

## Common misconceptions

- **"FLP means consensus is impossible in practice."** It means no algorithm *guarantees* termination under total asynchrony. Real protocols stay safe and terminate once the network behaves.
- **"Choose two of C, A and P."** A partition is something that happens to you. The choice is between C and A while it lasts.

## Go deeper

- Fischer, Lynch and Paterson, "Impossibility of Distributed Consensus with One Faulty Process", *Journal of the ACM* (1985).
- Lamport, Shostak and Pease, "The Byzantine Generals Problem", *ACM Transactions on Programming Languages and Systems* (1982).
- Gilbert and Lynch, "Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services", *SIGACT News* (2002).
- Brewer, "CAP Twelve Years Later: How the 'Rules' Have Changed", *IEEE Computer* (2012): the author's own corrections.
