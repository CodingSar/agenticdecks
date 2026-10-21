# Time, Clocks and Ordering

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Distributed foundations](README.md)
> **Builds on:** [System models and failures](system-models-and-failures.md), [Relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), [Clocking and synchronous design](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md)
> **Enables:** [Consistency models](../03-consensus-and-replication/consistency-models.md), [Eventual consistency and conflict-free replicated data types (CRDTs)](../04-distributed-data/eventual-consistency-and-crdts.md), [Distributed transactions](../04-distributed-data/distributed-transactions.md)

## Essence

Machines in a distributed system have no shared clock. Each has a quartz oscillator that drifts, and synchronising them over a network with variable delay leaves an uncertainty of microseconds to milliseconds. So "which event happened first?" cannot be answered by comparing timestamps when events are close together. Lamport's insight (1978) was that what matters for correctness is usually not real time but **causality**: whether one event could have influenced another. The *happened-before* relation captures exactly that, and logical clocks (Lamport clocks, vector clocks) track it cheaply using only the messages the system already sends.

## Core tenets

1. **Physical clocks drift and can only be synchronised approximately.** Typical crystal oscillators drift on the order of 10–100 parts per million, which is up to about 9 seconds per day at the high end. The Network Time Protocol (NTP) corrects them by exchanging timestamps with a server and assuming the network delay is symmetric; asymmetric or variable delay leaves error from under a millisecond on a local network to tens of milliseconds on the internet. Clocks can also jump backward when corrected, so wall-clock time is not even monotonic unless the operating system (OS) provides a separate monotonic clock.

2. **Happened-before (→) is a partial order defined by causality.** Event a → b if a and b are on the same process and a comes first, or a is the sending of a message and b its receipt, or there is a chain of such steps (transitivity). If neither a → b nor b → a, the events are *concurrent* (a ∥ b): neither could have affected the other. This is the same idea as the light cone in physics: information cannot travel faster than messages.

3. **Lamport clocks give a total order consistent with causality.** Each process keeps a counter. It increments the counter before each event and attaches it to each message; on receipt it sets its counter to max(local, received) + 1. Then a → b implies L(a) < L(b). Breaking ties by process ID gives a total order every node agrees on, which is enough to build a replicated state machine or a mutual-exclusion algorithm. The converse fails: L(a) < L(b) does not imply a → b, so Lamport clocks cannot detect concurrency.

4. **Vector clocks capture causality exactly.** With n processes, each keeps a vector of n counters: entry i counts events seen from process i. On send, a process increments its own entry and attaches the vector; on receipt it takes the element-wise maximum, then increments its own entry. Then a → b if and only if V(a) ≤ V(b) element-wise and V(a) ≠ V(b); if neither vector dominates, the events are concurrent. The cost is O(n) space per timestamp, which is why systems use variants (version vectors per replica, dotted version vectors) to detect conflicting writes.

5. **Ordering is what replication actually needs.** If every replica applies the same deterministic operations in the same order, they reach the same state; this is the state machine approach (Lamport 1978, Schneider 1990). Agreeing on a total order of operations is equivalent to consensus, which is why ordering is hard and why [consensus](../03-consensus-and-replication/consensus.md) protocols are really ordering protocols.

6. **Physical time can be used safely only with bounded uncertainty.** Google's Spanner (2012) exposes time as an interval [earliest, latest] from its TrueTime service, backed by Global Positioning System (GPS) receivers and atomic clocks, with uncertainty of a few milliseconds. To make commit order match real-time order, a transaction waits out the uncertainty ("commit wait") before reporting success. Hybrid logical clocks combine a physical timestamp with a logical counter so timestamps stay close to real time and still respect causality. Both work because they reason about the error bound rather than ignoring it.

7. **Leases depend on bounded clock rate, and pauses break them.** A lease grants exclusive authority (for example, "you are leader") until time T. If the holder's process pauses (garbage collection, a virtual machine migration) past T, it may act on an expired lease while another node holds a new one. Safe designs pair leases with fencing tokens: a monotonically increasing number that storage servers check, rejecting requests carrying an older token.

## Key concepts

| Term | Meaning |
|---|---|
| Clock drift | Rate at which a clock diverges from true time |
| Clock skew | Difference between two clocks' readings at one instant |
| NTP | Protocol that estimates offset from a time server using round-trip timestamps |
| Monotonic clock | Clock that never goes backward; good for durations, not for cross-node comparison |
| Happened-before (→) | Causal partial order on events defined by process order and messages |
| Concurrent events | Events with no causal path between them |
| Lamport clock | Scalar counter consistent with →, giving a total order with tie-breaking |
| Vector clock | Per-process counter vector that characterises → exactly |
| TrueTime | Spanner's clock interface returning a bounded uncertainty interval |
| Fencing token | Monotonic number that lets storage reject requests from stale lease holders |

## How it fits

- **Below:** happened-before is a [partial order](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md); a single chip avoids this whole problem with a [global clock signal](../../03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md), which does not scale beyond a board; [message delay variance](../../08-networking/01-principles/latency-bandwidth-and-queueing.md) is what limits synchronisation accuracy.
- **Above:** [consistency models](../03-consensus-and-replication/consistency-models.md) are defined in terms of real-time and causal order; [CRDTs and eventual consistency](../04-distributed-data/eventual-consistency-and-crdts.md) use version vectors; [distributed transactions](../04-distributed-data/distributed-transactions.md) use timestamps for ordering; [version control](../../12-software-engineering/02-process/version-control.md) histories form the same kind of causal graph.
- **Siblings:** [System models](system-models-and-failures.md) set how unreliable timing is; [impossibility results](impossibility-results.md) show why logical order alone cannot settle agreement.

## Common misconceptions

- **"Use timestamps to decide which write wins."** Last-writer-wins by wall clock silently discards writes when clocks are skewed; a write made later in real time can carry an earlier timestamp.
- **"Lamport timestamps tell you whether events are concurrent."** Only vector clocks do. Lamport order is consistent with causality but adds arbitrary order between concurrent events.
- **"NTP-synchronised clocks are good enough for ordering."** Millisecond-level error is far larger than the time between events in a busy system.

## Go deeper

- Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System", *Communications of the ACM* (1978): the founding paper.
- Fidge (1988) and Mattern (1989), the independent introductions of vector clocks.
- Corbett et al., "Spanner: Google's Globally-Distributed Database", OSDI (2012): TrueTime and commit wait.
- Kleppmann, *Designing Data-Intensive Applications* (2017): clocks, leases and fencing in practice.
