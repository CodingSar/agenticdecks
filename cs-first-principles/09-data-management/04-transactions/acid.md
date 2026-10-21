# ACID

> **Layer:** [09 Data Management](../README.md) › [Transactions](README.md)
> **Builds on:** [The Relational Model](../01-data-models/the-relational-model.md), [Race Conditions and Critical Sections](../../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md), [Crash Consistency and Journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md), [Correctness and Invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md)
> **Enables:** [Concurrency Control](concurrency-control.md), [Recovery and Logging](recovery-and-logging.md), [Distributed Transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md), [Consistency Models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md)

## Essence

Atomicity, Consistency, Isolation, Durability (ACID) names the four guarantees of a database transaction: Atomicity (all of its effects happen or none do), Consistency (it moves the database from one state satisfying the integrity constraints to another), Isolation (concurrent transactions do not see each other's partial work; the result is as if they ran one at a time) and Durability (once committed, its effects survive crashes). Together they let a programmer write a sequence of operations as if it were the only thing running on a machine that never fails. The acronym was coined by Härder and Reuter in 1983, building on Jim Gray's work on the transaction concept. The four letters are not equally fundamental: A, I and D are mechanisms the system provides; C is the application's invariants, which those mechanisms protect.

## Core tenets

1. **A transaction is a unit of work with a clear boundary.** It begins, performs reads and writes, and ends with COMMIT (make all effects permanent) or ABORT (discard them all). The system may also abort it on its own (deadlock, conflict, crash). Programs are written as if each transaction were indivisible.

2. **Atomicity removes partial failure from the programmer's view.** Transferring money is two writes: debit one account, credit another. A crash between them would destroy money. Atomicity guarantees that after any failure, either both writes are visible or neither is. The mechanism is logging: the system records enough to undo uncommitted changes.

3. **Consistency is the application's invariants, preserved by construction.** The database enforces declared constraints (keys, foreign keys, checks); the application ensures each transaction, run alone on a consistent state, leaves a consistent state (total money unchanged by a transfer). Atomicity and isolation then guarantee the invariant holds under failures and concurrency. This "C" is unrelated to the "C" in the Consistency, Availability, Partition tolerance (CAP) theorem, which concerns replica agreement.

4. **Isolation makes concurrency invisible.** The ideal is *serializability*: the outcome of concurrent execution equals the outcome of some serial execution of the same transactions. Then any invariant preserved by each transaction alone is preserved by all of them together. Without isolation, two concurrent "read balance, add 10, write balance" transactions can lose one update, the classic race condition.

5. **Durability means committed work survives crashes, not every disaster.** A commit returns only after its log records are on persistent storage (with an fsync or equivalent). Power loss after that point cannot undo it. Surviving disk loss or site loss requires replication on top; durability is relative to a failure model.

6. **The guarantees are expensive, so systems relax them.** Serializability limits concurrency; forcing the log on every commit limits throughput to the device's flush rate (batched by group commit). Most systems default to weaker isolation levels, and some replicated systems acknowledge commits before they reach remote replicas. Knowing which guarantee was weakened, and what anomalies follow, is part of using a database correctly.

7. **Transactions are an abstraction, not a feature of one engine.** The same contract appears in file systems (atomic rename, journaling), in transactional memory in hardware and languages, and in distributed systems (distributed transactions, sagas). Wherever several updates must appear to happen together, the ACID vocabulary applies.

## Key concepts

| Term | Meaning |
|---|---|
| Transaction | Sequence of operations treated as one indivisible unit |
| Commit / abort | Make all effects permanent / discard all effects |
| Atomicity | All-or-nothing effects despite failures |
| Consistency | Integrity constraints and application invariants preserved |
| Isolation | Concurrent transactions do not observe each other's partial state |
| Durability | Committed effects survive crashes |
| Serializability | Concurrent outcome equals some serial order |
| Lost update | One transaction's write overwritten by another based on stale reads |
| Group commit | Flushing the log once for many committing transactions |
| BASE | "Basically Available, Soft state, Eventually consistent": a contrasting design stance in some distributed stores |

## How it fits

- **Below:** isolation solves the database version of [race conditions](../../07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md); atomicity and durability generalise [crash consistency and journaling](../../07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md); consistency is a set of [invariants](../../05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md) declared in [the relational model](../01-data-models/the-relational-model.md).
- **Above:** [distributed transactions](../../10-distributed-and-parallel-computing/04-distributed-data/distributed-transactions.md) provide ACID across machines; [consistency models](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md) relate serializability to linearizability and weaker guarantees.
- **Siblings:** [concurrency control](concurrency-control.md) implements I; [recovery and logging](recovery-and-logging.md) implement A and D; [isolation levels](isolation-levels.md) document the ways I is relaxed.

## Common misconceptions

- **"ACID consistency and CAP consistency are the same."** ACID's C is about invariants within one database; CAP's C is about replicas agreeing (linearizability).
- **"A database that says ACID gives serializable isolation."** Many default to Read Committed or Snapshot Isolation, which permit anomalies.
- **"Durable means the data can never be lost."** It means the commit survives the crashes in the failure model, typically power loss; media and site failures need replication and backups.

## Go deeper

- J. Gray, *The Transaction Concept: Virtues and Limitations* (VLDB 1981): the foundational essay.
- T. Härder, A. Reuter, *Principles of Transaction-Oriented Database Recovery* (ACM Computing Surveys, 1983): introduces the ACID acronym.
- J. Gray, A. Reuter, *Transaction Processing: Concepts and Techniques* (1993): the definitive reference.
