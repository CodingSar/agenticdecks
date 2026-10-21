# Isolation Levels

> **Layer:** [09 Data Management](../README.md) › [Transactions](README.md)
> **Builds on:** [Concurrency Control](concurrency-control.md), [ACID](acid.md), [Memory Consistency Models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md)
> **Enables:** [Consistency Models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md), [Distributed Transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md), [Web Security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md)

## Essence

Full serializability costs concurrency, so databases offer weaker *isolation levels* that permit specific anomalies in exchange for throughput. The Structured Query Language (SQL) (Structured Query Language) standard defines four levels by which anomalies they forbid: Read Uncommitted, Read Committed, Repeatable Read and Serializable. In practice, implementations differ from the standard and from each other, and the most widely used level, Snapshot Isolation, is not in the standard's list at all. An isolation level is a contract about which interleavings the application must tolerate. Choosing one means knowing which anomalies your code could be exposed to and whether its invariants survive them.

## Core tenets

1. **Each level is defined by the anomalies it allows.** A *dirty read* sees another transaction's uncommitted write. A *non-repeatable read* reads the same row twice and gets different committed values. A *phantom* re-runs a query and sees new rows matching its predicate. A *lost update* overwrites a concurrent committed change. *Write skew* lets two transactions each read overlapping data and write disjoint items, jointly breaking an invariant. Weaker levels permit more of these.

2. **The standard's levels in brief.**

   | Level | Dirty read | Non-repeatable read | Phantom |
   |---|---|---|---|
   | Read Uncommitted | possible | possible | possible |
   | Read Committed | prevented | possible | possible |
   | Repeatable Read | prevented | prevented | possible |
   | Serializable | prevented | prevented | prevented |

   Mechanically, under locking: Read Committed takes short read locks released after each statement; Repeatable Read holds read locks on rows until commit; Serializable adds range or predicate locks.

3. **The standard's definitions are incomplete.** Berenson et al. (1995) showed that defining levels only by these three phenomena misses anomalies such as lost update and write skew, and that Snapshot Isolation satisfies the standard's wording for Repeatable Read (even preventing phantoms in the strict sense) while still allowing write skew. The standard's levels are better read as a rough guide than a precise specification.

4. **Snapshot Isolation is the practical default in many systems.** Each transaction reads from a consistent snapshot taken at its start and, at commit, aborts if another transaction committed a write to any row it also wrote ("first committer wins"). It prevents dirty reads, non-repeatable reads, read-only phantoms and lost updates, and readers never block. It permits write skew: two doctors each check "at least one other doctor is on call", each removes themself, and none is left.

5. **Read Committed is a common default and permits real bugs.** PostgreSQL, Oracle and SQL Server default to Read Committed (MySQL InnoDB defaults to Repeatable Read, implemented with snapshots). Under Read Committed, a read-modify-write such as "read stock, subtract one, write stock" can lose updates unless written as a single atomic UPDATE or protected with `SELECT ... FOR UPDATE`. Many application bugs, including some exploited in race-condition attacks on web applications, come from assuming serializability under a weaker default.

6. **Same name, different behaviour across systems.** "Repeatable Read" means locking-based isolation in some systems and Snapshot Isolation in others; "Serializable" in Oracle has historically been Snapshot Isolation. Correctness arguments must refer to what the engine actually does, which is why independent testing (for example the Jepsen analyses) has found many discrepancies.

7. **Weak isolation can be repaired locally.** Applications can materialise a conflict (make two transactions write a common row so the database detects it), use explicit locks (`SELECT ... FOR UPDATE`), add constraints the database checks, or switch only critical transactions to Serializable. This targets the cost of strong isolation at the places that need it.

8. **Isolation is the database cousin of memory consistency.** Hardware memory models (sequential consistency, weaker ordering) and distributed consistency models (linearizability, causal consistency) are answers to the same question for different systems: which interleavings may an observer see? Serializability concerns multi-operation transactions on many items; linearizability concerns single operations on single objects in real time; *strict serializability* combines both.

## Key concepts

| Term | Meaning |
|---|---|
| Isolation level | Contract specifying which concurrency anomalies may occur |
| Dirty read | Reading uncommitted data |
| Non-repeatable read | Re-reading a row yields a different committed value |
| Phantom | Re-running a predicate query yields new or missing rows |
| Lost update | Concurrent read-modify-write cycles overwrite each other |
| Write skew | Concurrent transactions jointly violate an invariant by writing disjoint items |
| Snapshot Isolation | Reads from a start-time snapshot; first committer wins on write conflicts |
| Strict serializability | Serializable, and the serial order respects real-time order |
| SELECT FOR UPDATE | Read that takes write locks to prevent concurrent modification |

## How it fits

- **Below:** each level is a weakening of a [concurrency control](concurrency-control.md) mechanism and of the I in [ACID](acid.md); the question parallels hardware [memory consistency models](../../04-computer-architecture/04-parallel-architecture/memory-consistency-models.md).
- **Above:** distributed [consistency models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md) extend the same lattice of guarantees to replicas; [distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md) must pick an isolation level that remains implementable across machines. Race conditions under weak isolation appear as vulnerabilities in [web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md) (double-spend, coupon reuse).
- **Siblings:** [concurrency control](concurrency-control.md) provides the mechanisms; [recovery and logging](recovery-and-logging.md) is independent of the chosen level.

## Common misconceptions

- **"Repeatable Read prevents all anomalies except phantoms."** Under Snapshot Isolation implementations it still permits write skew; under locking implementations it permits phantoms. The name does not tell you which.
- **"Serializable is too slow to use."** Modern Serializable Snapshot Isolation often costs modestly more than Snapshot Isolation; measure before assuming.
- **"My ORM handles concurrency."** An Object-Relational Mapper (ORM) issues statements under whatever isolation level is configured; it does not make read-modify-write sequences atomic.

## Go deeper

- H. Berenson, P. Bernstein, J. Gray, J. Melton, E. O'Neil, P. O'Neil, *A Critique of ANSI SQL Isolation Levels* (SIGMOD 1995): the essential paper.
- A. Adya, *Weak Consistency: A Generalized Theory and Optimistic Implementations for Distributed Transactions* (PhD thesis, MIT, 1999): implementation-independent definitions.
- M. Kleppmann, *Designing Data-Intensive Applications* (2017), chapter 7: clear practical walk-through of weak isolation anomalies.
