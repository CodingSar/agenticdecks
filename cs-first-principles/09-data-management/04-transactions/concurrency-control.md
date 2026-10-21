# Concurrency Control

> **Layer:** [09 Data Management](../README.md) › [Transactions](README.md)
> **Builds on:** [ACID](acid.md), [Locks and Semaphores](../../07-operating-systems/03-concurrency/locks-and-semaphores.md), [Deadlock](../../07-operating-systems/03-concurrency/deadlock.md), [Graph Traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md)
> **Enables:** [Isolation Levels](isolation-levels.md), [Distributed Transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md), [Time, Clocks and Ordering](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md)

## Essence

Concurrency control lets many transactions run at once while guaranteeing the result is equivalent to running them one at a time in some order (serializability). Only *conflicting* operations matter: two operations on the same item, at least one a write, from different transactions. A schedule is safe if the order of its conflicts is consistent with some serial order, which can be checked by looking for cycles in a precedence graph. Systems enforce this in three main ways: *pessimistically*, by locking items so conflicts wait (two-phase locking); *optimistically*, by running freely and validating at commit (optimistic concurrency control); or *by keeping multiple versions*, so readers see a consistent snapshot and never block writers (multiversion concurrency control).

## Core tenets

1. **Only conflicts constrain order.** Two reads of the same item commute; operations on different items commute. A read and a write, or two writes, on the same item do not: their order changes the result. Serializability therefore reduces to ordering conflicting pairs consistently.

2. **Conflict serializability is a graph property.** Draw a node per transaction and an edge Ti → Tj whenever an operation of Ti conflicts with and precedes one of Tj. The schedule is conflict-serializable exactly when this precedence graph is acyclic; any topological order is an equivalent serial order. A cycle (T1 before T2 on x, T2 before T1 on y) means no serial order explains what each saw.

3. **Two-phase locking (2PL) guarantees serializability.** Each transaction acquires a shared lock to read and an exclusive lock to write, and never acquires a lock after releasing one: a growing phase, then a shrinking phase. At the lock point (when it holds all its locks), each transaction can be placed in the serial order. *Strict* 2PL holds write locks until commit, which also prevents others from reading uncommitted data and avoids cascading aborts. Most locking databases use strict 2PL.

4. **Locking brings deadlock, which databases detect and break.** T1 holds x and waits for y while T2 holds y and waits for x. Databases build a waits-for graph and search it for cycles, aborting a victim, or use timeouts or timestamp-based prevention (wait-die, wound-wait). Unlike most Operating System (OS) deadlock handling, aborting is cheap and safe because transactions can be rolled back and retried.

5. **Phantoms require locking predicates, not just rows.** If T1 counts rows `WHERE dept = 7` and T2 inserts a new row with `dept = 7`, locking existing rows cannot stop the insert. Serializable systems lock ranges in an index (key-range or next-key locking on B-trees) or predicates, so that new rows matching a read's condition are blocked too.

6. **Optimistic concurrency control bets on few conflicts.** Each transaction reads and writes privately, then at commit validates that nothing it read has been changed by a transaction that committed in the meantime. If validation fails it aborts and retries. With rare conflicts this avoids all lock overhead; with frequent conflicts it wastes work on repeated aborts.

7. **Multiversion concurrency control (MVCC) separates readers from writers.** Each write creates a new version of the item tagged with its transaction's timestamp; each transaction reads the newest version committed before its snapshot. Readers never wait for writers and writers never wait for readers, which is why PostgreSQL, Oracle, MySQL InnoDB and most modern systems use MVCC. Old versions must be garbage-collected once no snapshot needs them.

8. **MVCC alone gives snapshot isolation, not serializability.** Two transactions can each read a snapshot, check a constraint, and write different items, together violating the constraint (write skew). Serializable Snapshot Isolation (Cahill et al., 2008) tracks read/write dependencies between concurrent snapshot transactions and aborts one when a dangerous pattern appears, giving serializability with MVCC's read performance; PostgreSQL implements it.

9. **Granularity trades overhead for concurrency.** Locking whole tables is cheap but serialises everything; locking rows allows concurrency but costs memory and lock-manager time. Multigranularity locking with intention locks (IS, IX) lets a transaction lock a table coarsely or rows finely while others can still detect conflicts at either level.

## Key concepts

| Term | Meaning |
|---|---|
| Conflict | Two operations on the same item, from different transactions, at least one a write |
| Precedence graph | Transactions as nodes, conflict order as edges; acyclic means serializable |
| 2PL / strict 2PL | No lock acquired after any release / plus write locks held to commit |
| Shared / exclusive lock | Lock compatible with other readers / incompatible with all others |
| Waits-for graph | Graph of transactions blocked on each other; a cycle is a deadlock |
| Phantom | Row inserted by another transaction that matches an earlier read's predicate |
| OCC | Optimistic concurrency control: validate at commit, abort on conflict |
| MVCC | Multiversion concurrency control: readers see snapshots of committed versions |
| Write skew | Anomaly where concurrent transactions write disjoint items based on overlapping reads |

## How it fits

- **Below:** locks and deadlock come from [locks and semaphores](../../07-operating-systems/03-concurrency/locks-and-semaphores.md) and [deadlock](../../07-operating-systems/03-concurrency/deadlock.md) in operating systems, applied to logical data items instead of memory; cycle detection is [graph traversal](../../05-algorithms-and-data-structures/05-graph-algorithms/graph-traversal.md). It implements the I in [ACID](acid.md).
- **Above:** [distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md) combine local concurrency control with atomic commit; MVCC across machines needs globally meaningful timestamps ([time, clocks and ordering](../../10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md)).
- **Siblings:** [isolation levels](isolation-levels.md) are defined by which of these mechanisms are weakened; [recovery](recovery-and-logging.md) must undo aborted transactions while locks still protect their writes.

## Common misconceptions

- **"Locking every row I touch makes my transaction serializable."** Without range or predicate locks, phantoms still break serializability, and releasing locks early breaks two-phase discipline.
- **"MVCC means serializable."** Plain MVCC gives snapshot isolation, which permits write skew.
- **"Optimistic is always faster."** Under high contention, optimistic schemes can spend most of their time aborting and retrying.

## Go deeper

- K. P. Eswaran, J. N. Gray, R. A. Lorie, I. L. Traiger, *The Notions of Consistency and Predicate Locks in a Database System* (CACM, 1976): two-phase locking and phantoms.
- H. T. Kung, J. T. Robinson, *On Optimistic Methods for Concurrency Control* (ACM TODS, 1981): optimistic concurrency control.
- P. A. Bernstein, V. Hadzilacos, N. Goodman, *Concurrency Control and Recovery in Database Systems* (1987): the theory, freely available online.
- M. J. Cahill, U. Röhm, A. D. Fekete, *Serializable Isolation for Snapshot Databases* (SIGMOD 2008): Serializable Snapshot Isolation.
