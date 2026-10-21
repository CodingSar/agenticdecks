# Batch and Stream Processing

> **Layer:** [10 Distributed and Parallel Computing](../README.md) › [Large-scale systems](README.md)
> **Builds on:** [Data and task parallelism](../01-parallel-computing/data-and-task-parallelism.md), [Partitioning](../04-distributed-data/partitioning.md), [Join algorithms](../../09-data-management/03-query-processing/join-algorithms.md), [Functional programming](../../06-programming-languages/01-paradigms/functional.md)
> **Enables:** [Training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md), [Observability](../../12-software-engineering/04-operations/observability.md), [Scalability patterns](scalability-patterns.md)

## Essence

Batch processing runs a computation over a large, finite dataset and produces an output; stream processing runs a computation continuously over an unbounded sequence of events and updates its output as events arrive. Both are **data-parallel dataflow**: the programmer writes per-record functions (map, filter, aggregate by key, join), and a framework partitions the data across machines, moves records between stages, and recovers from failures. The key idea that made this practical, from MapReduce (Dean and Ghemawat, 2004), is that **if tasks are deterministic functions of immutable input, a failed task can simply be re-run**, so fault tolerance becomes cheap. Streaming adds two hard problems: reasoning about time when events arrive late and out of order, and keeping state consistent across failures.

## Core tenets

1. **MapReduce is map, shuffle, reduce.** Map tasks read input splits and emit key-value pairs; the framework partitions those pairs by key, sorts them and sends each partition to one reduce task (the shuffle); reduce tasks aggregate all values for each key. Because map and reduce are side-effect-free functions of their input, the framework can re-execute any failed or slow task elsewhere. The shuffle is a distributed sort and is usually the most expensive step, bounded by network bandwidth.

2. **Recomputation beats replication for intermediate data.** MapReduce wrote intermediate results to disk; Spark (Zaharia et al., 2012) keeps them in memory as resilient distributed datasets that record their *lineage*, the chain of transformations that produced them. A lost partition is rebuilt by re-running its lineage on the inputs. This cuts disk input and output for iterative jobs such as machine-learning training and graph algorithms by orders of magnitude.

3. **Stragglers set the finishing time.** A stage ends only when its slowest task ends, so one slow machine (a failing disk, a noisy neighbour, a skewed partition) delays the whole job. This is the span law in practice. Frameworks launch speculative backup copies of slow tasks and take whichever finishes first; data skew must be fixed by better partitioning, since backups do not help a task that simply has more work.

4. **Declarative plans let the engine optimise.** Expressing jobs as relational operators (Structured Query Language (SQL) on Spark, Hive or BigQuery-style engines) lets an optimiser reorder filters, choose join strategies (broadcast the small side or shuffle both), and prune columns. Columnar storage formats such as Parquet read only the needed columns and compress well, which often matters more than the number of machines.

5. **Streams need event time, not processing time.** An event's timestamp (when it happened) differs from when it reaches the processor, because of network delay, buffering on phones and retries. Grouping by event time into windows (fixed, sliding or session windows) gives correct answers, but the system never knows for sure that all events for a window have arrived. *Watermarks* are the system's estimate that no earlier events remain; results are emitted at the watermark and can be revised when late data arrives. This is the Dataflow model (Akidau et al., 2015).

6. **Exactly-once stream results come from consistent snapshots plus replay.** Stream processors such as Flink periodically take a distributed snapshot of all operator state, aligned with markers injected into the stream (a variant of the Chandy–Lamport snapshot algorithm, 1985). After a failure, every operator restores from the last snapshot and the input is replayed from a durable log such as Kafka from the matching offset. Records may be processed twice internally, but the effect on state is exactly once; effects on external systems need idempotent or transactional sinks.

7. **The log is the unifying abstraction.** A durable, partitioned, append-only log (Kafka is the canonical example) decouples producers from consumers, buffers bursts, and lets consumers replay history. A batch job is a computation over a bounded slice of the log; a stream job is one over its unbounded tail. Architectures that once ran separate batch and streaming code paths (the "Lambda architecture") increasingly use one streaming engine over a log for both.

## Key concepts

| Term | Meaning |
|---|---|
| Batch job | Computation over a bounded input that terminates with an output |
| Stream job | Continuous computation over an unbounded event sequence |
| Shuffle | Repartitioning records by key between stages; a distributed sort |
| Lineage | Recorded chain of transformations used to recompute lost data |
| Straggler | Task much slower than its peers, delaying stage completion |
| Event time | When an event occurred, as opposed to when it is processed |
| Window | Finite grouping of a stream, by time or by session |
| Watermark | Estimate that all events before a time have arrived |
| Checkpoint | Consistent snapshot of operator state used for recovery |
| Partitioned log | Durable append-only sequence of records, split for parallelism |

## How it fits

- **Below:** map and reduce come from [functional programming](../../06-programming-languages/01-paradigms/functional.md) and [data parallelism](../01-parallel-computing/data-and-task-parallelism.md); the shuffle is [partitioning](../04-distributed-data/partitioning.md) plus [external sorting](../../05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md); distributed joins are [join algorithms](../../09-data-management/03-query-processing/join-algorithms.md) across machines; windows and watermarks address [the absence of a global clock](../02-distributed-foundations/time-clocks-and-ordering.md); approximate stream summaries come from [streaming algorithms](../../05-algorithms-and-data-structures/07-advanced-topics/streaming-and-online-algorithms.md).
- **Above:** data preparation for [training at scale](../../13-artificial-intelligence/03-deep-learning/training-at-scale.md); metrics and log pipelines for [observability](../../12-software-engineering/04-operations/observability.md); event-driven [scalability patterns](scalability-patterns.md).
- **Siblings:** [cloud computing](cloud-computing.md) supplies elastic clusters and object storage these jobs read and write; [scalability patterns](scalability-patterns.md) use the same logs and queues for request-serving systems.

## Common misconceptions

- **"Streaming is just fast batch."** Unbounded input forces new concepts (event time, watermarks, continuous state) that batch never needs.
- **"Exactly-once means each record is processed once."** It means the final effect on state is as if it were; internally records may be replayed.
- **"More machines always speed up a job."** Shuffle bandwidth, skew and stragglers often dominate; a well-tuned single machine beats many small clusters for data that fits on it.

## Go deeper

- Dean and Ghemawat, "MapReduce: Simplified Data Processing on Large Clusters", OSDI (2004).
- Zaharia et al., "Resilient Distributed Datasets", NSDI (2012): Spark's lineage-based fault tolerance.
- Akidau et al., "The Dataflow Model", VLDB (2015): event time, windows and watermarks.
- Kreps, *I Heart Logs* (2014): the log as the unifying abstraction.
