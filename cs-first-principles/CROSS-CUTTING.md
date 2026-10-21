# Cross-Cutting Principles

The rest of this knowledge base is a tree: sixteen layers, each split into areas and leaves. A tree gives every topic one parent, which is what makes bottom-up reading possible. But Computer Science (CS) is a graph. A small set of ideas solves problems in layer after layer, often decades apart and under different names. A processor cache, an operating system's page cache, a Content Delivery Network (CDN) and a memoised function are one idea applied at four distances. Seeing that saves learning it four times, and lets a lesson from one layer ("invalidation is the hard part of caching") warn you in another.

Each section below states one principle as a claim, explains the force that makes it recur, and follows it up the stack, lowest layer first, with a link to a leaf for each appearance. Each ends with the failure mode: when the principle hurts, and which neighbouring principle pulls against it.

**How to use it.** Read across, not down. Pick a principle, then open two leaves from distant layers in its table and compare them. Parent READMEs throughout the tree end with "Cross-cutting threads" that link back here. The last section, [Principles that pull against each other](#principles-that-pull-against-each-other), lists the tensions behind most hard design decisions.

## Contents

1. [Abstraction and layering](#abstraction-and-layering)
2. [Interface vs implementation](#interface-vs-implementation)
3. [Indirection and naming](#indirection-and-naming)
4. [Caching and locality](#caching-and-locality)
5. [Pipelining and parallelism](#pipelining-and-parallelism)
6. [Batching and amortization](#batching-and-amortization)
7. [Redundancy and fault tolerance](#redundancy-and-fault-tolerance)
8. [The end-to-end argument](#the-end-to-end-argument)
9. [Tradeoffs](#tradeoffs)
10. [Invariants and correctness](#invariants-and-correctness)
11. [Recursion and self-reference](#recursion-and-self-reference)
12. [Virtualization](#virtualization)
13. [State and time](#state-and-time)
14. [Encoding and representation](#encoding-and-representation)
15. [Limits and impossibility](#limits-and-impossibility)
16. [Feedback and control](#feedback-and-control)
17. [Composition](#composition)
18. [Trust and verification](#trust-and-verification)
19. [Principles that pull against each other](#principles-that-pull-against-each-other)

## Abstraction and layering

**Claim: a layer that keeps a simple promise and hides how it keeps it lets everything above be designed without knowing what is below.** Human minds hold only a few things at once, so this is the only known way to manage systems of billions of parts. It also lets the lower layers change faster than the designs above them: transistors shrink and processors are redesigned while software keeps running. Every abstraction works by discarding information (the exact voltage, gate or route) on the bet that the layer above does not need it.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Analog vs digital](00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md) | Continuous voltages collapse to two levels with noise margins: the most consequential abstraction in the stack. |
| 03 | [Logic gates](03-digital-logic/02-combinational-logic/logic-gates.md) | Transistor networks hide behind truth tables. |
| 04 | [The ISA contract](04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) | The Instruction Set Architecture (ISA) hides the microarchitecture; x86 code from 1978 still runs. |
| 05 | [Models of computation](05-algorithms-and-data-structures/01-foundations/models-of-computation.md) | The Random Access Machine (RAM) model hides hardware so analyses outlive it. |
| 07 | [Kernel mode and system calls](07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md) | System calls hide devices, scheduling and physical placement. |
| 08 | [Layering and the end-to-end principle](08-networking/01-principles/layering-and-the-end-to-end-principle.md) | Each protocol layer uses only the service of the layer beneath. |
| 09 | [The relational model](09-data-management/01-data-models/the-relational-model.md) | Data independence: the logical schema hides physical layout. |
| 12 | [Modularity and information hiding](12-software-engineering/01-design/modularity-and-information-hiding.md) | "Deep" modules hide much behind a small interface. |
| 14 | [Interaction design principles](14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md) | The user interface hides the whole stack behind a mental model. |
| 15 | [Ethics and professional responsibility](15-computing-in-context/ethics-and-professional-responsibility.md) | Abstraction hides harms as well as details, diffusing responsibility. |

**When it hurts.** Every abstraction leaks. The RAM model ignores caches, so algorithms with equal bounds differ tenfold in practice; side channels are leaks attackers exploit; and a layer cannot use what is hidden beneath it (the Transmission Control Protocol (TCP) cannot tell congestion from radio corruption). [The end-to-end argument](#the-end-to-end-argument) and [tradeoffs](#tradeoffs) keep re-negotiating where the lines go. See also [interface vs implementation](#interface-vs-implementation).

## Interface vs implementation

**Claim: separating what something promises from how it does it lets each side change independently, and lets many implementations serve one interface.** Layering stacks abstractions; this principle is about the contract itself. A contract is cheap to keep stable, while implementations must change with technology and scale. Once it is written down, callers can swap suppliers and teams can rewrite internals without telling anyone. What you may rely on is exactly what the interface states.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Circuit laws](00-engineering-foundations/02-electrical-circuits/circuit-laws.md) | A Thévenin equivalent describes any linear network by its two-terminal behaviour. |
| 01 | [Abstract algebra](01-mathematical-foundations/04-algebra/abstract-algebra.md) | A group or ring is an interface given by laws; every model inherits the theorems. |
| 03 | [Character encoding](03-digital-logic/01-number-representation/character-encoding.md) | Unicode code points are separate from their Unicode Transformation Format 8-bit (UTF-8) bytes. |
| 04 | [The ISA contract](04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) | Architecture versus microarchitecture, first named by the IBM System/360 team in 1964. |
| 06 | [Type systems](06-programming-languages/02-semantics-and-types/type-systems.md) | A type signature is a machine-checked interface. |
| 07 | [File-system implementation](07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) | Linux's Virtual File System (VFS) lets many file systems implement one interface. |
| 09 | [Query optimization](09-data-management/03-query-processing/query-optimization.md) | Structured Query Language (SQL) says what; the optimizer picks how. |
| 12 | [Abstraction and interfaces](12-software-engineering/01-design/abstraction-and-interfaces.md) | Parnas's information hiding made the principle a design method. |
| 14 | [Digital media and compression](14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) | Codec standards fix the decoder, leaving encoders free to improve. |

**When it hurts.** Interfaces rarely capture everything callers depend on. Timing, ordering and error messages leak, and with enough users every observable behaviour becomes depended upon (Hyrum's law). Performance is almost never in the contract, which is where [abstraction](#abstraction-and-layering) meets [tradeoffs](#tradeoffs). Interfaces are also where [trust and verification](#trust-and-verification) must happen.

## Indirection and naming

**Claim: referring to a thing by a name that is resolved only when used lets the thing move, be shared, be replaced or be protected without changing any reference.** The resolver in the middle (a page table, a symbol table, a name server) is a single control point: change one mapping and every holder of the name follows. That is why "any problem in computer science can be solved by another level of indirection", usually attributed to David Wheeler, keeps coming true. The price is a lookup on every use, so indirection almost always travels with [caching](#caching-and-locality).

| Layer | Where it appears | How it shows up |
|---|---|---|
| 04 | [Superscalar and out-of-order](04-computer-architecture/02-processor-microarchitecture/superscalar-and-out-of-order.md) | Register renaming maps architectural names onto many physical registers. |
| 04 | [Virtual-memory hardware](04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) | Page tables resolve virtual addresses; the Translation Lookaside Buffer (TLB) caches answers. |
| 05 | [Hash tables](05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) | A hash maps a key to a slot in constant expected time. |
| 06 | [Linking and loading](06-programming-languages/04-runtime-systems/linking-and-loading.md) | Symbols resolve to addresses at link, load or first call. |
| 06 | [Object-oriented programming](06-programming-languages/01-paradigms/object-oriented.md) | Virtual method tables pick the code for a method name at run time. |
| 07 | [File-system implementation](07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) | Paths resolve to inodes; inodes resolve to blocks. |
| 08 | [Naming and DNS](08-networking/05-application-layer/naming-and-dns.md) | The Domain Name System (DNS) maps stable names to changing addresses. |
| 10 | [Partitioning](10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) | Routing tables map keys to partitions, so data can move. |
| 11 | [Access control](11-security-and-cryptography/03-system-security/access-control.md) | Capabilities are unforgeable names that carry authority. |
| 12 | [Version control](12-software-engineering/02-process/version-control.md) | Branches are movable names for immutable, content-addressed commits. |

**When it hurts.** Every level adds latency, and every resolver can be redirected: DNS spoofing and Border Gateway Protocol (BGP) hijacks ([network attacks and defences](11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md)) corrupt the mapping, not the target. A name can also outlive its referent, as a dangling pointer or stale entry. See [virtualization](#virtualization) and [trust and verification](#trust-and-verification).

## Caching and locality

**Claim: programs reuse recently touched data and touch data near it, so a small fast copy of recent neighbourhoods serves most accesses at the small memory's speed.** Physics makes large memories slow: a bigger store is farther away and has more capacitance to charge, so a level-1 (L1) cache hit takes about 1 ns while a Dynamic Random-Access Memory (DRAM) access takes about 100 ns (2020s hardware). And real access patterns are skewed: a few items get most requests. The same gap and skew appear at every distance, from a register to another continent.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 04 | [Locality and caching](04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) | Registers, L1/L2/L3 caches and DRAM, each a cache for the next level. |
| 04 | [Hazards and branch prediction](04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) | A branch predictor caches past behaviour. |
| 05 | [Dynamic programming](05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) | Memoisation caches subproblem answers, turning exponential recursions polynomial. |
| 05 | [External-memory and cache-oblivious algorithms](05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md) | The theory of caching: count block transfers, not operations. |
| 06 | [JIT compilation](06-programming-languages/04-runtime-systems/jit-compilation.md) | Just-In-Time (JIT) compilers keep inline caches of each call site's last receiver type. |
| 07 | [Page replacement](07-operating-systems/04-memory-management/page-replacement.md) | Memory caches disk; Least Recently Used (LRU) approximations choose victims. |
| 08 | [Content delivery and caching](08-networking/05-application-layer/content-delivery-and-caching.md) | DNS caches, browser caches and CDNs move copies toward readers. |
| 09 | [B-trees](09-data-management/02-storage-and-indexing/b-trees.md) | The buffer pool keeps hot pages; upper tree levels almost always hit. |
| 12 | [Build and continuous delivery](12-software-engineering/04-operations/build-and-continuous-delivery.md) | Build caches reuse outputs whose inputs have not changed. |
| 13 | [Attention and transformers](13-artificial-intelligence/03-deep-learning/attention-and-transformers.md) | The key-value (KV) cache avoids recomputing past tokens during generation. |

**When it hurts.** Copies go stale, so every cache needs an invalidation story, and keeping many caches of one memory consistent is a subject of its own ([multicore and cache coherence](04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md)). Without locality a cache is pure overhead, and shared caches leak timing ([side channels](11-security-and-cryptography/03-system-security/side-channels.md)). See [state and time](#state-and-time) and [indirection and naming](#indirection-and-naming).

## Pipelining and parallelism

**Claim: when pieces of work do not depend on each other, doing them at the same time raises throughput.** Pipelining overlaps successive tasks in time, each at a different stage, so one finishes per stage-time though each still takes the whole pipeline. Parallelism replicates units in space. Two forces spread it everywhere. Around 2005 the end of Dennard scaling stopped clock rates rising, so extra transistors buy speed only through concurrency. And communication is slow, so a system must keep many operations in flight to fill a long pipe.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 01 | [Abstract algebra](01-mathematical-foundations/04-algebra/abstract-algebra.md) | Associativity lets a reduction run as a tree of logarithmic depth. |
| 03 | [Arithmetic and building blocks](03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md) | Parallel-prefix adders compute all carries at once, trading area for depth. |
| 04 | [Pipelining](04-computer-architecture/02-processor-microarchitecture/pipelining.md) | The instruction pipeline: the canonical example. |
| 04 | [SIMD and GPUs](04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) | Single Instruction, Multiple Data (SIMD) lanes and Graphics Processing Units (GPUs) process many items at once. |
| 05 | [Divide and conquer](05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) | Independent subproblems can be solved in parallel. |
| 08 | [Reliable delivery](08-networking/04-transport-layer/reliable-delivery.md) | Sliding windows keep many packets in flight. |
| 10 | [Work, span and parallel models](10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) | Total work and the longest dependency chain bound speed-up. |
| 13 | [Training at scale](13-artificial-intelligence/03-deep-learning/training-at-scale.md) | Data, tensor and pipeline parallelism across thousands of accelerators. |
| 14 | [Rasterization pipeline](14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md) | A fixed pipeline over millions of independent vertices and pixels. |

**When it hurts.** Dependencies stall pipelines, workers must coordinate, and the serial fraction caps everything ([Amdahl's law](04-computer-architecture/06-performance/amdahls-law.md)). Overlap also creates interleavings nobody planned for, the root of race conditions. See [state and time](#state-and-time) and [batching and amortization](#batching-and-amortization).

## Batching and amortization

**Claim: when an operation has a large fixed cost and a small per-item cost, grouping items pays the fixed cost once and drives the average toward the per-item cost.** Fixed costs are everywhere: a disk seek, a network round trip, an interrupt, a log flush, a load of model weights. They loom larger over time because latency improves much more slowly than bandwidth. Amortized analysis applies the same idea across time: a rare expensive step is fine if many cheap steps pay for it.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 04 | [DRAM and storage devices](04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) | Whole cache lines, DRAM rows and disk blocks move at once. |
| 04 | [DMA and devices](04-computer-architecture/05-io-and-interconnect/dma-and-devices.md) | Direct Memory Access (DMA) and interrupt coalescing spread one interrupt over many bytes. |
| 05 | [Amortized analysis](05-algorithms-and-data-structures/01-foundations/amortized-analysis.md) | A dynamic array doubles rarely, so appends average constant time. |
| 06 | [Memory management and garbage collection](06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) | Tracing collectors reclaim many objects in one pass. |
| 07 | [Memory allocation](07-operating-systems/04-memory-management/memory-allocation.md) | Slab caches and huge pages spread per-object and per-page overheads. |
| 09 | [LSM-trees](09-data-management/02-storage-and-indexing/lsm-trees.md) | Log-Structured Merge (LSM) trees turn random writes into sequential runs. |
| 09 | [Recovery and logging](09-data-management/04-transactions/recovery-and-logging.md) | Group commit shares one log flush among many transactions. |
| 12 | [Build and continuous delivery](12-software-engineering/04-operations/build-and-continuous-delivery.md) | The counter-case: big releases amortise overhead but delay feedback, so practice shrinks them. |
| 13 | [Learning as optimization](13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) | Mini-batches share one pass over the weights among many examples. |

**When it hurts.** The first item in a batch waits for the last, so batching buys throughput with latency. Amortized bounds also hide occasional long pauses (a resize, a collection, a compaction) that matter for tail latency. See [tradeoffs](#tradeoffs) and [feedback and control](#feedback-and-control).

## Redundancy and fault tolerance

**Claim: reliable systems can be built from unreliable parts by adding extra copies, bits or attempts, provided failures are detected or outvoted and are independent.** John von Neumann showed this in the 1950s, and there is no alternative: every component eventually fails, and a system needing all its parts fails more often than any one. Redundancy comes in space (replicas), information (check bits) and time (retries), and the same probability reasoning covers a noise margin and a replicated database.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Reliability and redundancy](00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md) | Parallel copies multiply failure probabilities; majority voting masks faults. |
| 00 | [Noise and signal integrity](00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md) | Noise margins are redundancy in voltage space. |
| 02 | [Channel capacity and error correction](02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) | Codes make communication reliable at any rate below capacity. |
| 04 | [DRAM and storage devices](04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) | Error-Correcting Code (ECC) memory survives bit flips. |
| 07 | [Crash consistency and journaling](07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md) | Journals and copy-on-write make crashes survivable. |
| 08 | [Encoding and framing](08-networking/02-link-layer/encoding-and-framing.md) | Cyclic Redundancy Checks (CRCs) detect damaged frames. |
| 09 | [Recovery and logging](09-data-management/04-transactions/recovery-and-logging.md) | The write-ahead log redoes committed and undoes uncommitted work. |
| 10 | [Replication](10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) | Copies plus quorums survive a bounded number of failed machines. |
| 11 | [Security design principles](11-security-and-cryptography/01-security-principles/security-design-principles.md) | Defence in depth: independent barriers, so one breach is not total. |
| 12 | [Reliability engineering](12-software-engineering/04-operations/reliability-engineering.md) | Multi-zone replicas, canaries and rollbacks keep services up through change. |

**When it hurts.** Redundancy helps only as far as failures are independent; a shared power feed, a bug in every replica or a bad configuration pushed everywhere defeats it. Copies cost money, add complexity that fails in its own ways, and writable copies must agree, which drags in [state and time](#state-and-time) and the [limits](#limits-and-impossibility) of consensus.

## The end-to-end argument

**Claim: a function that can be done completely and correctly only with knowledge held at the endpoints must be done there; doing it in a lower layer is at best a performance optimisation.** Saltzer, Reed and Clark stated it in "End-to-End Arguments in System Design" (1984). Every component between two endpoints can fail, reorder or lie, and only the endpoint knows what "correct" means for its data. Since the end must check anyway, the middle can stay simple.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 07 | [Page replacement](07-operating-systems/04-memory-management/page-replacement.md) | A database knows its access pattern better than the Operating System (OS), so it manages its own buffer. |
| 07 | [Crash consistency and journaling](07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md) | A consistent file system can hold a half-updated application file; applications must `fsync` and check. |
| 08 | [Layering and the end-to-end principle](08-networking/01-principles/layering-and-the-end-to-end-principle.md) | Where it was argued: reliability lives in hosts, the core stays simple. |
| 08 | [Wireless networks](08-networking/02-link-layer/wireless-networks.md) | Wi-Fi retransmission on a lossy hop: an optimisation, never a guarantee. |
| 08 | [UDP and TCP](08-networking/04-transport-layer/udp-and-tcp.md) | TCP builds reliable delivery in hosts over best-effort Internet Protocol (IP); the User Datagram Protocol (UDP) leaves it to the application. |
| 10 | [Batch and stream processing](10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) | "Exactly-once" effects come from idempotent endpoints, not reliable links. |
| 11 | [Secure protocols and TLS](11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md) | Transport Layer Security (TLS) protects data between the endpoints that hold the keys. |
| 11 | [Network attacks and defences](11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md) | Firewalls help; only endpoint authentication and encryption suffice. |

**When it hurts.** Pushing everything to the edges can waste resources (retransmitting across a continent what one hop could fix) and duplicates work in every application. Middleboxes erode the principle and freeze protocols in place. It is in permanent tension with [abstraction and layering](#abstraction-and-layering), and is a special case of [trust and verification](#trust-and-verification): check where the answer is actually known.

## Tradeoffs

**Claim: improving one property of a design almost always costs another, because the properties draw on the same limited resources.** Energy, time, area, bits, money and attention are finite, and physical and mathematical laws couple them: faster switching costs power, more replicas cost coordination, more generality costs speed. Good design chooses a side of each trade explicitly and measures it, rather than searching for a design with no costs.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Tradeoffs and constraints](00-engineering-foundations/05-engineering-method/tradeoffs-and-constraints.md) | The method: find the constraints and the Pareto frontier, then pick a point. |
| 03 | [Timing and power](03-digital-logic/04-hardware-design/timing-and-power.md) | Area, delay and power trade in every block. |
| 04 | [SIMD and GPUs](04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) | Latency versus throughput: the Central Processing Unit (CPU) finishes one thread fast, the GPU many slowly. |
| 05 | [Randomized algorithms](05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) | A tiny error probability buys speed or simplicity. |
| 07 | [Kernel architectures](07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md) | Monolithic kernels buy speed; microkernels buy isolation. |
| 08 | [Latency, bandwidth and queueing](08-networking/01-principles/latency-bandwidth-and-queueing.md) | Bigger buffers trade packet loss for queueing delay. |
| 09 | [LSM-trees](09-data-management/02-storage-and-indexing/lsm-trees.md) | Read, write and space amplification cannot all be minimised. |
| 10 | [Consistency models](10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md) | Stronger consistency costs latency and, under partition, availability. |
| 12 | [Reliability engineering](12-software-engineering/04-operations/reliability-engineering.md) | An error budget prices reliability against feature velocity. |
| 13 | [Generalization and bias-variance](13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) | Flexible models fit training data better but may generalise worse. |

**When it hurts.** The usual failure is forgetting a trade was made: optimising one measured number while an unmeasured one decays, or keeping a choice after the conditions that justified it are gone. Some trades are not choices but bounds; see [limits and impossibility](#limits-and-impossibility).

## Invariants and correctness

**Claim: a program's executions are too many to check one by one, so state a property that every step preserves, and induction proves it holds forever.** An invariant turns infinitely many behaviours into two finite checks: it holds at the start, and every step that begins with it ends with it. That is why one technique serves loops, data structures, circuits, locks, databases and consensus. Specifications split into safety ("nothing bad happens", an invariant) and liveness ("something good eventually happens").

| Layer | Where it appears | How it shows up |
|---|---|---|
| 01 | [Induction and recurrences](01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) | Induction is the proof engine behind every invariant. |
| 03 | [Clocking and synchronous design](03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md) | Setup and hold constraints must hold on every path. |
| 04 | [Superscalar and out-of-order](04-computer-architecture/02-processor-microarchitecture/superscalar-and-out-of-order.md) | In-order commit keeps visible state equal to some sequential execution. |
| 05 | [Correctness and invariants](05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md) | Loop and representation invariants are the main proof tool. |
| 06 | [Hoare logic and program proofs](06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) | Pre- and postconditions turn correctness into logic. |
| 07 | [Locks and semaphores](07-operating-systems/03-concurrency/locks-and-semaphores.md) | A lock hides the moment an invariant is broken from other threads. |
| 09 | [Concurrency control](09-data-management/04-transactions/concurrency-control.md) | Serializability preserves any invariant each transaction preserves alone. |
| 10 | [Consensus](10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) | "At most one value is chosen" is kept by quorum intersection. |
| 11 | [Memory-safety vulnerabilities](11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md) | Unsafe languages leave the memory-safety invariant to the programmer. |
| 12 | [Testing](12-software-engineering/03-quality/testing.md) | Assertions state what must hold; tests check it on examples. |

**When it hurts.** Most operations break an invariant briefly before restoring it, and that window is where crashes, interrupts and other threads do damage. An invariant is also only as good as the specification: a proved program can still do the wrong thing. See [state and time](#state-and-time) and [trust and verification](#trust-and-verification).

## Recursion and self-reference

**Claim: defining a thing by smaller instances of itself plus a base case gives a finite description of an unbounded structure; and because programs are data, programs can take programs as input.** The first half is why trees, grammars, divide-and-conquer and inductive proofs share one shape. The second gives universality (one machine runs any program) and, by the same move, the deepest impossibility results: a program asked about itself can contradict any claimed answer.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 01 | [Sets](01-mathematical-foundations/02-sets-relations-functions/sets.md) | Russell's paradox: unrestricted self-reference breaks naive set theory. |
| 02 | [Context-free grammars and pushdown automata](02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md) | Grammar rules are recursive; a stack executes recursion. |
| 02 | [Lambda calculus](02-theory-of-computation/03-computability/lambda-calculus.md) | The Y combinator builds recursion from function application alone. |
| 02 | [Halting problem and undecidability](02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) | A program fed its own description defeats any halting decider. |
| 05 | [Divide and conquer](05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) | Split, solve smaller instances, combine; a recurrence gives the cost. |
| 05 | [String matching](05-algorithms-and-data-structures/06-string-algorithms/string-matching.md) | The Knuth–Morris–Pratt failure function describes how a pattern matches itself. |
| 06 | [Lexing and parsing](06-programming-languages/03-compilers/lexing-and-parsing.md) | Recursive-descent parsers mirror the grammar, one function per rule. |
| 13 | [Reinforcement learning](13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) | The Bellman equation defines a state's value by its successors' values. |

**When it hurts.** Naive recursion can recompute subproblems exponentially often (fixed by [caching](#caching-and-locality) as memoisation) or exhaust the stack. Unrestricted self-reference yields paradox and undecidability, the source of many [limits](#limits-and-impossibility). Recursive proofs rest on [invariants](#invariants-and-correctness).

## Virtualization

**Claim: a layer that implements a resource's interface on top of a different resource can make one thing look like many, many look like one, or one kind look like another.** It recurs because hardware is expensive and must be shared safely, because programs should not care which machine runs them, and because an interposed layer is a natural place to enforce isolation. Popek and Goldberg (1974) gave the condition for efficient machine virtualization: every sensitive instruction must trap when run without privilege.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 02 | [Turing machines](02-theory-of-computation/03-computability/turing-machines.md) | The universal machine, the first virtual machine, imitates any other. |
| 04 | [Virtual-memory hardware](04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) | Hardware translation gives each program its own address space. |
| 06 | [Interpreters and virtual machines](06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md) | A process virtual machine presents a portable machine on a real one. |
| 07 | [Processes](07-operating-systems/02-process-management/processes.md) | Time-sharing makes one CPU look like many. |
| 07 | [File-system abstractions](07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md) | Numbered blocks become a tree of named, growable files. |
| 07 | [Virtual machines and hypervisors](07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) | One machine looks like many complete machines. |
| 07 | [Containers](07-operating-systems/07-virtualization/containers.md) | Virtualize the OS interface instead: lighter, but one shared kernel. |
| 10 | [Cloud computing](10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) | A data centre looks like one elastic pool. |
| 11 | [Isolation and sandboxing](11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) | Each principal gets its own virtual machine or address space. |

**When it hurts.** Each virtual layer costs performance, and the private resource is an imperfect illusion: tenants share caches, memory bandwidth and the hypervisor, giving noisy neighbours and cross-tenant side channels. Isolation is only as strong as what is still shared. Virtualization is usually built from [indirection](#indirection-and-naming); see also [trust and verification](#trust-and-verification).

## State and time

**Claim: once mutable state can be changed by more than one actor, behaviour depends on the order of events, and finite signal speed makes that order hard to know.** Concurrency bugs, crash inconsistencies and distributed anomalies are one bug: code assumed an order the system did not guarantee. Physics makes it universal. Even inside a chip "simultaneous" is approximate, and between machines a slow reply is indistinguishable from a dead machine. Every layer must define what "before" means and pay to enforce it.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Capacitance and timing](00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md) | Wires take time to charge, so signals arrive at different moments. |
| 03 | [Latches and flip-flops](03-digital-logic/03-sequential-logic/latches-and-flip-flops.md) | Metastability is the irreducible cost of forcing continuous time into steps. |
| 04 | [Memory consistency models](04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) | When one core's stores become visible to another is a contract, often weak. |
| 06 | [Functional programming](06-programming-languages/01-paradigms/functional.md) | Immutable values sidestep the problem for most code. |
| 07 | [Race conditions and critical sections](07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md) | Interleaved read-modify-write sequences lose updates. |
| 08 | [Reliable delivery](08-networking/04-transport-layer/reliable-delivery.md) | Sequence numbers restore order; timeouts guess at failure. |
| 09 | [Concurrency control](09-data-management/04-transactions/concurrency-control.md) | Locking and multiversioning order conflicting transactions. |
| 10 | [Time, clocks and ordering](10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md) | Lamport's happened-before relation (1978) replaces a global clock with a partial order. |
| 10 | [Eventual consistency and CRDTs](10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md) | Conflict-free Replicated Data Types (CRDTs) accept concurrent updates and merge them. |
| 12 | [Version control](12-software-engineering/02-process/version-control.md) | A history of state; merges reconcile concurrent changes. |

**When it hurts.** Enforcing order costs coordination, hence latency and, under partition, availability. So systems weaken ordering for speed and hand the complexity to programmers, who then write the bugs. See [tradeoffs](#tradeoffs), [invariants and correctness](#invariants-and-correctness) and [caching and locality](#caching-and-locality).

## Encoding and representation

**Claim: the same information can be written in many ways, and each makes some operations cheap and others expensive, so choosing a representation is choosing a cost profile.** Addition is easy in two's complement and hard in Roman numerals; range queries are easy in a sorted array and hard in a hash table. Computation always manipulates a representation, never the thing itself, so the biggest gains often come from changing the representation rather than the procedure.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Sampling and quantization](00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) | Sample rate and resolution decide what survives digitisation. |
| 02 | [Source coding and compression](02-theory-of-computation/01-information-theory/source-coding-and-compression.md) | Frequent messages get short codes; entropy bounds how short. |
| 03 | [Integers and two's complement](03-digital-logic/01-number-representation/integers-and-twos-complement.md) | One adder serves signed and unsigned numbers. |
| 03 | [Floating point](03-digital-logic/01-number-representation/floating-point.md) | Institute of Electrical and Electronics Engineers (IEEE) 754 trades exactness for range. |
| 05 | [Non-comparison sorting](05-algorithms-and-data-structures/04-sorting-and-searching/non-comparison-sorting.md) | Radix sort beats the comparison bound by reading key encodings. |
| 05 | [Tries and suffix structures](05-algorithms-and-data-structures/06-string-algorithms/tries-and-suffix-structures.md) | The Burrows–Wheeler transform is both an index and a compressor. |
| 09 | [Storage layouts](09-data-management/02-storage-and-indexing/storage-layouts.md) | Row stores suit transactions; column stores suit analytics. |
| 11 | [Web security](11-security-and-cryptography/04-network-and-application-security/web-security.md) | Injection happens when data and code share one representation. |
| 13 | [Retrieval and embeddings](13-artificial-intelligence/04-advanced-paradigms/retrieval-and-embeddings.md) | Embeddings turn meaning into geometry; similarity becomes distance. |
| 14 | [Geometry and transformations](14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) | Homogeneous coordinates make every transform a matrix multiply. |

**When it hurts.** Fixed-size encodings have edges (overflow, rounding), ambiguous encodings breed security holes, and formats outlive their reasons: stored data and deployed protocols are very hard to re-encode. See [limits and impossibility](#limits-and-impossibility) and [interface vs implementation](#interface-vs-implementation).

## Limits and impossibility

**Claim: some bounds hold for every possible design; knowing them tells you when to stop searching and which assumption to relax.** They come from four sources. Physics: the speed of light, thermal noise, the energy cost of erasing a bit. Information: entropy bounds compression and capacity bounds reliable rate. Counting: there are more problems than programs. Logic: diagonal arguments turn any claimed solver against itself.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Thermodynamics and energy](00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) | Erasing a bit costs at least `kT ln 2` (Boltzmann's constant times temperature times ln 2): the Landauer bound. |
| 01 | [Predicate logic](01-mathematical-foundations/01-logic/predicate-logic.md) | First-order validity is undecidable; Gödel showed rich theories incomplete. |
| 02 | [Entropy and information](02-theory-of-computation/01-information-theory/entropy-and-information.md) | No lossless code beats the source's entropy on average. |
| 02 | [Halting problem and undecidability](02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) | By Rice's theorem every non-trivial question about program behaviour is undecidable. |
| 02 | [P, NP and NP-completeness](02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) | NP-complete problems, the hardest whose answers are quickly checkable (NP), likely need super-polynomial time. |
| 04 | [Power and the end of scaling](04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) | Power density means not all of a chip can switch at once. |
| 05 | [Comparison sorting](05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md) | Ω(n log n) comparisons are needed to tell n! orders apart. |
| 10 | [Impossibility results](10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md) | Fischer–Lynch–Paterson (FLP), CAP (Consistency, Availability, Partition tolerance) and the Byzantine bound. |
| 11 | [Foundations of modern cryptography](11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) | Perfect secrecy needs a key as long as the message, so practice rests on assumed hardness. |
| 13 | [Generalization and bias-variance](13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) | No Free Lunch: averaged over all problems, no learner wins. |

**When it hurts.** A limit is a statement about a model, so it misleads when the model does not fit: worst-case hardness does not stop solvers handling most real instances, and FLP does not stop practical consensus. The productive response is to relax an assumption (randomise, approximate, add timeouts, restrict the language). See [tradeoffs](#tradeoffs) and [recursion and self-reference](#recursion-and-self-reference).

## Feedback and control

**Claim: when a system or its environment is unknown or changing, measuring the output and adjusting the input beats predicting in advance.** Negative feedback makes a system precise even when its parts are not, because errors are measured and opposed. Positive feedback drives a system to an extreme, which is what memory and clean decisions need. The loop recurs from amplifiers to network protocols to model training because no designer knows the load, the network or the data ahead of time.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Feedback and control](00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) | Negative feedback trades gain for precision; loop delay causes oscillation. |
| 01 | [Optimization](01-mathematical-foundations/05-continuous-mathematics/optimization.md) | Gradient descent measures the error's slope and steps against it. |
| 03 | [Latches and flip-flops](03-digital-logic/03-sequential-logic/latches-and-flip-flops.md) | Positive feedback between cross-coupled gates stores a bit. |
| 06 | [JIT compilation](06-programming-languages/04-runtime-systems/jit-compilation.md) | Run-time profiles decide what to optimise; failed guesses deoptimise. |
| 07 | [Scheduling](07-operating-systems/02-process-management/scheduling.md) | Multi-level feedback queues infer a job's nature from its past. |
| 08 | [Congestion control](08-networking/04-transport-layer/congestion-control.md) | TCP infers congestion from loss and delay and resizes its window. |
| 10 | [Scalability patterns](10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) | Backpressure, load shedding and autoscaling match capacity to load. |
| 12 | [Observability](12-software-engineering/04-operations/observability.md) | Metrics, logs and traces close the loop between system and operators. |
| 13 | [Reinforcement learning](13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) | Learned closed-loop control: act, observe reward, adjust. |
| 14 | [Interaction design principles](14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md) | Interaction is a human-in-the-loop cycle of action and feedback. |

**When it hurts.** A loop that reacts too late or too hard oscillates: retry storms, flapping autoscalers, thrashing. A loop optimises exactly what it measures, so a measure that becomes a target stops being a good measure (Goodhart's law), and a model whose outputs shape its future training data can amplify its errors. See [batching and amortization](#batching-and-amortization) and [state and time](#state-and-time).

## Composition

**Claim: big things can be built from small ones only when the whole's properties follow predictably from the parts' properties and the rule that combines them.** Where that holds, the field scales: gates into processors, functions into programs, operators into queries, layers into deep networks. It holds when the combining rule is closed (the result is the same kind of thing as the inputs) and the property survives it (delays add along a path; types check piece by piece).

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [CMOS](00-engineering-foundations/03-semiconductor-devices/cmos.md) | Complementary Metal-Oxide-Semiconductor (CMOS) transistors in series and parallel make AND and OR. |
| 01 | [Calculus](01-mathematical-foundations/05-continuous-mathematics/calculus.md) | The chain rule differentiates any composition of differentiable parts. |
| 02 | [Finite automata and regular languages](02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) | The product construction combines automata predictably. |
| 03 | [Logic gates](03-digital-logic/02-combinational-logic/logic-gates.md) | NAND alone composes into any Boolean function. |
| 04 | [Amdahl's law](04-computer-architecture/06-performance/amdahls-law.md) | Speed-ups of parts combine through Amdahl's law, not multiplication. |
| 06 | [Functional programming](06-programming-languages/01-paradigms/functional.md) | Pure functions compose predictably; shared mutable state does not. |
| 07 | [Deadlock](07-operating-systems/03-concurrency/deadlock.md) | Locks do not compose: two correct modules can deadlock together. |
| 09 | [Relational algebra and SQL](09-data-management/01-data-models/relational-algebra-and-sql.md) | Operators map relations to relations, so queries nest freely. |
| 10 | [Eventual consistency and CRDTs](10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md) | Merge is a semilattice join: associative, commutative, idempotent. |
| 11 | [Security design principles](11-security-and-cryptography/01-security-principles/security-design-principles.md) | Secure parts do not automatically compose into a secure whole. |
| 13 | [Neural networks and backpropagation](13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md) | Deep networks compose simple layers; gradients compose by the chain rule. |

**When it hurts.** Some properties are emergent: performance, security, deadlock-freedom and failure behaviour often belong to the combination, which is why [software architecture](12-software-engineering/01-design/software-architecture.md) is largely the study of which qualities survive combining parts. See [abstraction and layering](#abstraction-and-layering) and [state and time](#state-and-time).

## Trust and verification

**Claim: no one can check everything, so every system rests on a trusted base; good design makes that base small and checks the rest with methods cheaper than redoing the work.** Checking can be far cheaper than finding: a certificate, a signature or a proof is quick to verify even when expensive to produce. So the recurring move is to shrink what must be trusted (a kernel, a proof checker, a key) and verify whatever crosses it. The logic is the same for chips, protocols, code and learned models.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Measurement and modeling](00-engineering-foundations/05-engineering-method/measurement-and-modeling.md) | Measure rather than trust models or intuition. |
| 02 | [P, NP and NP-completeness](02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) | NP is exactly the problems whose answers can be checked quickly. |
| 03 | [FPGA and ASIC](03-digital-logic/04-hardware-design/fpga-and-asic.md) | Unlike a Field-Programmable Gate Array (FPGA), an Application-Specific Integrated Circuit (ASIC) cannot be patched, so verification dominates. |
| 06 | [Proof assistants and dependent types](06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) | A small trusted kernel makes huge machine-made proofs believable. |
| 07 | [Kernel architectures](07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md) | The kernel is the trusted base; seL4 shows a small one can be proved correct. |
| 08 | [Internet routing and BGP](08-networking/03-network-layer/internet-routing-and-bgp.md) | BGP believes neighbours' route claims; hijacks exploit that. |
| 10 | [Byzantine fault tolerance](10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md) | With `3f + 1` replicas, agreement survives `f` arbitrary liars. |
| 11 | [Public-key cryptography](11-security-and-cryptography/02-cryptography/public-key-cryptography.md) | Signatures and certificates move trust from channels to keys. |
| 12 | [Static analysis and code review](12-software-engineering/03-quality/static-analysis-and-code-review.md) | Layered checks, none sufficient alone, each shrinking what is taken on faith. |
| 13 | [Evaluation and experimentation](13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md) | Held-out data is the only check on a model without a specification. |

**When it hurts.** The trusted base is larger than it looks: everything beneath an abstraction is trusted by default. Ken Thompson's "Reflections on Trusting Trust" (1984) showed a compiler can plant a backdoor no source review finds ([software supply-chain security](11-security-and-cryptography/04-network-and-application-security/software-supply-chain-security.md)). Verification is also bounded by [undecidability](#limits-and-impossibility). See [the end-to-end argument](#the-end-to-end-argument) and [redundancy and fault tolerance](#redundancy-and-fault-tolerance).

## Principles that pull against each other

These principles are not a checklist to apply all at once. Many pull in opposite directions, and most hard design decisions are about where to stand between two of them.

| Tension | Why they conflict | Where you meet it |
|---|---|---|
| [Caching](#caching-and-locality) vs [state and time](#state-and-time) | A copy is fast because it is not checked against the original. | Cache coherence, DNS time-to-live, CDN invalidation. |
| [Abstraction](#abstraction-and-layering) vs performance ([tradeoffs](#tradeoffs)) | Hiding detail hides what you need to go fast. | The RAM model versus caches; kernel bypass. |
| [Layering](#abstraction-and-layering) vs [the end-to-end argument](#the-end-to-end-argument) | Layers want each function in one place; correctness says the ends must check anyway. | Link versus transport retransmission. |
| [Redundancy](#redundancy-and-fault-tolerance) vs cost and [state and time](#state-and-time) | Every copy costs money, and writable copies must agree. | Replication factor, quorum size, CAP. |
| [Batching](#batching-and-amortization) vs [feedback](#feedback-and-control) | Big batches are efficient but slow to finish and to learn from. | Group commit, mini-batch size, release size. |
| [Indirection](#indirection-and-naming) vs speed and [trust](#trust-and-verification) | Each name adds a lookup and a mapping that can be corrupted. | Page-table walks, DNS spoofing. |
| [Parallelism](#pipelining-and-parallelism) vs [invariants](#invariants-and-correctness) | Overlapped work creates interleavings that break assumptions. | Data races; speculative-execution leaks such as Spectre. |
| [Virtualization](#virtualization) vs [trust](#trust-and-verification) | Sharing hardware is the point, and sharing leaks. | Cross-tenant side channels. |
| [Composition](#composition) vs [state and time](#state-and-time) | Shared mutable state couples parts that looked independent. | Locks that deadlock together. |

[Limits and impossibility](#limits-and-impossibility) referee all of these: they mark corners of each trade-off that no design reaches. [Encoding and representation](#encoding-and-representation) is often the way out, because a better representation can move the whole frontier instead of sliding along it.
