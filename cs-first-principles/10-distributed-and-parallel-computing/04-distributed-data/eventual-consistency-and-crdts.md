# Eventual Consistency and CRDTs

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Distributed data](README.md)
> **Builds on:** [Time, clocks and ordering](../02-distributed-foundations/time-clocks-and-ordering.md), [Consistency models](../03-consensus-and-replication/consistency-models.md), [Relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md), [Abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md)
> **Enables:** [Scalability patterns](../05-large-scale-systems/scalability-patterns.md), [Content delivery and caching](../../08-networking/05-application-layer/content-delivery-and-caching.md), [Version control](../../12-software-engineering/02-process/version-control.md)

## Essence

Eventual consistency lets every replica accept reads and writes locally, without waiting for others, and promises only that replicas converge once they have received the same updates. This keeps a system available during partitions and fast across continents, but leaves a hard question: what happens when two replicas accept conflicting writes? Conflict-free replicated data types (CRDTs), formalised by Shapiro, Preguiça, Baquero and Zawirski (2011), answer it with algebra. If replica states form a **join-semilattice** and merging takes the least upper bound, then merge is commutative, associative and idempotent, so replicas that have seen the same updates in any order, any number of times, are in the same state. This is **strong eventual consistency**, and it needs no coordination at all.

## Core tenets

1. **Convergence must be designed, not hoped for.** Without a merge rule, concurrent writes to one item leave replicas disagreeing forever, or a heuristic picks a winner. Last-writer-wins by timestamp is the common heuristic and it silently discards one of two concurrent writes, and with skewed clocks it can discard the later one. Correct eventual consistency needs a deterministic merge that preserves the intent of concurrent updates.

2. **Concurrency must be detected before it can be resolved.** Version vectors (one counter per replica) tell whether one version descends from another or the two are concurrent. A replica that receives a strictly newer version replaces its own; one that receives a concurrent version must merge or keep both as siblings for the application to resolve, as Amazon's Dynamo did with shopping carts.

3. **A semilattice merge makes order and duplication irrelevant.** If merge(a, b) is commutative (order of merges does not matter), associative (grouping does not matter) and idempotent (merging the same state twice does nothing), then any gossip pattern that eventually delivers every update yields the same result. This is why state-based CRDTs can be synchronised over unreliable channels that drop, duplicate and reorder messages.

4. **Simple CRDTs show the trick.** A *grow-only counter* (G-Counter) keeps one count per replica; increment bumps your own entry; merge takes the element-wise maximum; the value is the sum. A *PN-Counter* (positive–negative counter) pairs two G-Counters, one for increments and one for decrements. A *grow-only set* merges by union. An *observed-remove set* (OR-Set) tags each added element with a unique identifier, and remove deletes only the tags it has seen, so a concurrent add and remove resolve as "add wins" deterministically.

5. **State-based and operation-based CRDTs trade bandwidth for delivery requirements.** State-based CRDTs ship whole states (or deltas) and tolerate any delivery pattern. Operation-based CRDTs ship only operations, which is cheaper, but require reliable causal-order delivery and that concurrent operations commute. Both give the same convergence guarantee under their assumptions.

6. **Collaborative editing is the hardest case and the showcase.** Sequence CRDTs (as used in tools such as Automerge and Yjs) give every character a unique, densely ordered position identifier so concurrent inserts at the same place interleave deterministically. The older approach, operational transformation, used in Google Docs, rewrites concurrent operations against each other and generally relies on a central server for ordering. Both let users edit offline and merge later.

7. **CRDTs cannot express invariants that need agreement.** A CRDT can guarantee that replicas converge, but not that a global constraint holds, such as "the account balance never goes negative" or "a username is unique". Two replicas can each allow a withdrawal that is fine locally and together overdraw. Such invariants need coordination, at least for the operations that could break them. The CALM theorem (Consistency As Logical Monotonicity; Hellerstein and Alvaro, 2020) states the boundary: programs whose outputs only grow as inputs grow (monotonic programs) can run coordination-free; non-monotonic ones cannot.

## Key concepts

| Term | Meaning |
|---|---|
| Eventual consistency | Replicas converge once updates stop arriving |
| Strong eventual consistency | Replicas that received the same updates are in the same state, immediately |
| Join-semilattice | Partial order where every pair has a least upper bound (join) |
| CRDT | Replicated data type whose concurrent updates merge without conflict |
| State-based CRDT | Replicas exchange full states and merge with join |
| Operation-based CRDT | Replicas exchange commuting operations over causal delivery |
| Version vector | Per-replica counters that detect concurrent versions |
| Last-writer-wins | Resolve conflicts by highest timestamp, discarding others |
| OR-Set | Set CRDT where adds are tagged so removes affect only observed adds |
| CALM theorem | Monotonic programs are exactly those with coordination-free consistent implementations |

## How it fits

- **Below:** semilattices come from [relations and orders](../../01-mathematical-foundations/02-sets-relations-functions/relations-and-orders.md) and the commutative, associative, idempotent laws from [abstract algebra](../../01-mathematical-foundations/04-algebra/abstract-algebra.md); version vectors come from [vector clocks](../02-distributed-foundations/time-clocks-and-ordering.md); the choice of availability over linearizability is licensed by the [CAP (Consistency, Availability, Partition tolerance) theorem](../02-distributed-foundations/impossibility-results.md).
- **Above:** [scalability patterns](../05-large-scale-systems/scalability-patterns.md) use eventually consistent stores for global, low-latency data; the [Domain Name System (DNS)](../../08-networking/05-application-layer/naming-and-dns.md) and [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md) are eventually consistent; [version control](../../12-software-engineering/02-process/version-control.md) systems such as Git are replicated histories that merge, though with manual conflict resolution.
- **Siblings:** [distributed transactions](distributed-transactions.md) are the coordinated alternative for data with invariants; [partitioning](partitioning.md) is orthogonal: each partition can be replicated with CRDTs.

## Common misconceptions

- **"Eventual consistency means anything goes."** Strong eventual consistency with CRDTs is a precise, provable guarantee of convergence.
- **"Last-writer-wins is a CRDT, so it is safe."** It converges, but by discarding concurrent writes; convergence is not the same as preserving intent.
- **"CRDTs remove the need for coordination."** Only for monotonic operations; uniqueness and non-negativity constraints still need agreement.

## Go deeper

- Shapiro, Preguiça, Baquero and Zawirski, "Conflict-free Replicated Data Types", SSS (2011): the definitions and proofs.
- Vogels, "Eventually Consistent", *Communications of the ACM* (2009): the practitioner framing.
- Hellerstein and Alvaro, "Keeping CALM: When Distributed Consistency Is Easy", *Communications of the ACM* (2020).
- Kleppmann and Beresford, "A Conflict-Free Replicated JSON Datatype", *IEEE Transactions on Parallel and Distributed Systems* (2017).
