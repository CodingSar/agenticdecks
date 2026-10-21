# Cross-Cutting Principles

The rest of this knowledge base is a tree: sixteen layers, each split into areas, each area split into leaves. A tree gives every topic exactly one parent, which is what makes it readable bottom-up. But Computer Science (CS) is a graph. The same handful of ideas keeps solving problems in layer after layer, often decades apart and under different names. A processor's cache, an operating system's page cache, a web Content Delivery Network (CDN) and a memoised recursive function are one idea applied at four distances. Seeing that saves you from learning it four times, and lets a lesson learned in one layer (for example, "invalidation is the hard part of caching") warn you in another.

This file is the index of those ideas. Each section states one principle as a claim, explains the force that makes it recur, then follows it through the stack from the lowest layer where it appears to the highest. Each row links to a leaf where you can see the mechanism in detail. Each section ends with the failure mode: the situation in which the principle hurts, and the neighbouring principle that pulls against it.

**How to use it.** Read across, not down. Pick a principle, read the claim, then open two leaves from distant layers in its table and compare them. The parent READMEs throughout the tree end with "Cross-cutting threads" that link back here, so you can also arrive from any area and jump sideways. The final section, [Principles that pull against each other](#principles-that-pull-against-each-other), lists the tensions that make most real design decisions hard.

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

**Claim: a layer that keeps a simple promise and hides how it keeps it lets everything above be designed without knowing anything below.** This is the only known way to keep a system of billions of parts within the reach of a human mind, which can hold only a few things at once. It recurs for a second reason: the layers below change faster than the designs above. A layer boundary lets transistors shrink, processors be redesigned and networks be rebuilt while the software above keeps working. Every abstraction works by throwing information away (the exact voltage, the exact gate, the exact route) on the bet that the layer above does not need it.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Analog vs digital](00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md) | The digital abstraction collapses a continuous voltage into two levels with noise margins, so later stages restore rather than accumulate error. It is the most consequential abstraction in the stack. |
| 03 | [Logic gates](03-digital-logic/02-combinational-logic/logic-gates.md) | Transistor networks are hidden behind truth tables; designers think in AND, OR and NOT. |
| 03 | [Clocking and synchronous design](03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md) | The synchronous discipline hides settling times and glitches behind clean clock cycles. |
| 04 | [The ISA contract](04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) | The Instruction Set Architecture (ISA) hides the microarchitecture; x86 code from 1978 still runs on today's chips. |
| 05 | [Models of computation](05-algorithms-and-data-structures/01-foundations/models-of-computation.md) | The Random Access Machine (RAM) model abstracts away the hardware so algorithm analysis survives hardware changes. |
| 06 | [Intermediate representations](06-programming-languages/03-compilers/intermediate-representations.md) | A compiler lowers a program through a series of representations, each hiding the detail of the next. |
| 07 | [Kernel mode and system calls](07-operating-systems/01-kernel-and-abstractions/kernel-mode-and-system-calls.md) | The system-call interface hides devices, scheduling and physical placement from applications. |
| 08 | [Layering and the end-to-end principle](08-networking/01-principles/layering-and-the-end-to-end-principle.md) | The protocol stack is the textbook case: each layer uses only the service of the layer beneath and adds its own header. |
| 09 | [The relational model](09-data-management/01-data-models/the-relational-model.md) | Data independence: the logical schema hides physical layout, so storage can be reorganised without rewriting queries. |
| 12 | [Modularity and information hiding](12-software-engineering/01-design/modularity-and-information-hiding.md) | Each module is a small layer; "deep" modules hide much behind a small interface. |
| 14 | [Interaction design principles](14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md) | The user interface is the topmost abstraction, hiding the entire stack behind the user's mental model. |
| 15 | [Ethics and professional responsibility](15-computing-in-context/ethics-and-professional-responsibility.md) | Abstraction hides harms as well as details, spreading responsibility across many hands. |

**When it hurts.** Every abstraction leaks somewhere. The RAM model ignores caches, so two algorithms with equal bounds can differ tenfold in practice; side channels and undefined behaviour are leaks that attackers exploit; and a layer cannot use information hidden beneath it (the Transmission Control Protocol (TCP) cannot tell congestion loss from radio corruption). Strict layering also costs performance, which is why [the end-to-end argument](#the-end-to-end-argument) and [tradeoffs](#tradeoffs) keep re-negotiating where the lines go. See also [interface vs implementation](#interface-vs-implementation) and [virtualization](#virtualization).

## Interface vs implementation

**Claim: separating what something promises from how it does it lets each side change independently, and lets many implementations serve one interface.** Layering stacks abstractions vertically; this principle is about the contract itself. An interface is cheap to keep stable, while implementations must change as technology, scale and cost change. Once a contract is written down, a buyer can swap suppliers, a compiler can swap algorithms, and a team can rewrite a module without telling anyone. The interface also becomes the unit of compatibility: what you may rely on is exactly what it states.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Circuit laws](00-engineering-foundations/02-electrical-circuits/circuit-laws.md) | A Thévenin equivalent describes any linear network by its behaviour at two terminals, whatever is inside. |
| 01 | [Abstract algebra](01-mathematical-foundations/04-algebra/abstract-algebra.md) | An algebraic structure (group, ring, lattice) is an interface given by laws; any set satisfying them inherits every theorem. |
| 03 | [Character encoding](03-digital-logic/01-number-representation/character-encoding.md) | Unicode code points (what a character is) are separate from Unicode Transformation Format 8-bit (UTF-8) bytes (how it is stored). |
| 04 | [The ISA contract](04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) | Architecture versus microarchitecture: the distinction was first named by the IBM System/360 team in 1964. |
| 06 | [Type systems](06-programming-languages/02-semantics-and-types/type-systems.md) | A type signature is a machine-checked interface between caller and callee. |
| 07 | [File-system implementation](07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) | Linux's Virtual File System (VFS) lets many file systems implement one set of operations. |
| 08 | [Data-center networks and SDN](08-networking/03-network-layer/data-center-networks-and-sdn.md) | Software-Defined Networking (SDN) separates the control plane (which routes exist) from the data plane (how packets move). |
| 08 | [HTTP and the web](08-networking/05-application-layer/http-and-the-web.md) | The Hypertext Transfer Protocol (HTTP) uniform interface hides whether a response came from the origin, a cache or a CDN. |
| 09 | [Query optimization](09-data-management/03-query-processing/query-optimization.md) | Structured Query Language (SQL) states what is wanted; the optimizer chooses how, among many physical plans. |
| 12 | [Abstraction and interfaces](12-software-engineering/01-design/abstraction-and-interfaces.md) | Parnas's information hiding turned this principle into a design method. |
| 14 | [Digital media and compression](14-human-and-visual-computing/03-media-and-vision/digital-media-and-compression.md) | Codec standards fix the bitstream and decoder, leaving encoders free to improve for decades. |

**When it hurts.** An interface rarely captures everything callers depend on. Timing, memory use, error messages and ordering leak through, and with enough users every observable behaviour becomes depended upon (often called Hyrum's law). Performance is almost never in the contract, which is where [abstraction](#abstraction-and-layering) and [tradeoffs](#tradeoffs) collide. Interfaces are also the boundaries where [trust and verification](#trust-and-verification) must happen.

## Indirection and naming

**Claim: referring to a thing by a name that is resolved to its location only when used lets the thing move, be shared, be replaced or be protected without changing any reference.** The resolver in the middle (a page table, a symbol table, a name server) is a single control point. Change one mapping and every holder of the name follows. That is why the line "any problem in computer science can be solved by another level of indirection", usually attributed to David Wheeler, keeps coming true. The price is a lookup on every use, which is why indirection almost always travels with [caching](#caching-and-locality).

| Layer | Where it appears | How it shows up |
|---|---|---|
| 04 | [Instruction encoding and addressing](04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md) | Register and memory-indirect addressing modes: an instruction names where the operand is, not the operand. |
| 04 | [Superscalar and out-of-order](04-computer-architecture/02-processor-microarchitecture/superscalar-and-out-of-order.md) | Register renaming maps a few architectural register names onto many physical registers, removing false dependencies. |
| 04 | [Virtual-memory hardware](04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) | Virtual addresses are names resolved by page tables; the Translation Lookaside Buffer (TLB) caches the answers. |
| 05 | [Hash tables](05-algorithms-and-data-structures/02-fundamental-data-structures/hash-tables.md) | A hash function maps a key (a name) to a slot (a location) in constant expected time. |
| 06 | [Binding, scope and closures](06-programming-languages/02-semantics-and-types/binding-scope-and-closures.md) | Environments bind names to values; a closure carries its bindings with it. |
| 06 | [Linking and loading](06-programming-languages/04-runtime-systems/linking-and-loading.md) | Symbol resolution and procedure linkage tables let code call functions whose addresses are fixed only at load or first call. |
| 06 | [Object-oriented programming](06-programming-languages/01-paradigms/object-oriented.md) | Virtual method tables resolve a method name to code at run time. |
| 07 | [File-system implementation](07-operating-systems/05-storage-and-file-systems/file-system-implementation.md) | Path names resolve to inodes; inodes resolve to blocks. |
| 08 | [Naming and DNS](08-networking/05-application-layer/naming-and-dns.md) | The Domain Name System (DNS) maps stable names to changing addresses, decoupling identity from location. |
| 10 | [Partitioning](10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) | Routing tables map keys to partitions, so data can move between machines without clients noticing. |
| 11 | [Access control](11-security-and-cryptography/03-system-security/access-control.md) | Capabilities are unforgeable names that carry authority with them. |
| 12 | [Version control](12-software-engineering/02-process/version-control.md) | Branches and tags are movable names for immutable, content-addressed commits. |

**When it hurts.** Every level adds latency, and every resolver is a point an attacker can redirect: DNS spoofing and Border Gateway Protocol (BGP) hijacks (see [network attacks and defences](11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md)) work by corrupting the mapping, not the target. A name can also outlive its referent (a dangling pointer, a stale cache entry). See [caching and locality](#caching-and-locality), [virtualization](#virtualization) and [trust and verification](#trust-and-verification).

## Caching and locality

**Claim: programs reuse recently touched data and touch data near it, so keeping a small fast copy of recent neighbourhoods serves most accesses at the speed of the small memory.** Two forces make this universal. Physics makes large memories slow: a bigger store is physically farther away and has more capacitance to charge, so a level-1 (L1) cache hit takes about 1 ns while a Dynamic Random-Access Memory (DRAM) access takes about 100 ns (circa 2020s hardware). And real access patterns are skewed: a few items, pages or web objects get most of the requests. The same gap and the same skew appear at every distance, from a register to a data centre on another continent.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 04 | [Locality and caching](04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) | The memory hierarchy: registers, L1/L2/L3 caches and DRAM, each a cache for the next. |
| 04 | [Hazards and branch prediction](04-computer-architecture/02-processor-microarchitecture/hazards-and-branch-prediction.md) | A branch predictor is a cache of past behaviour, betting the future repeats it. |
| 04 | [Virtual-memory hardware](04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) | The TLB caches address translations so most memory accesses skip the page-table walk. |
| 05 | [Dynamic programming](05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) | Memoisation caches answers to subproblems, turning exponential recursions into polynomial ones. |
| 05 | [External-memory and cache-oblivious algorithms](05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md) | The theory of caching: count block transfers, not operations. |
| 06 | [JIT compilation](06-programming-languages/04-runtime-systems/jit-compilation.md) | Just-In-Time (JIT) compilers keep code caches and inline caches of the last receiver type at each call site. |
| 07 | [Page replacement](07-operating-systems/04-memory-management/page-replacement.md) | Physical memory is a cache for disk; Least Recently Used (LRU) approximations decide what to evict. |
| 08 | [Content delivery and caching](08-networking/05-application-layer/content-delivery-and-caching.md) | DNS caches, browser caches and CDNs move copies closer to readers to beat the speed of light. |
| 09 | [B-trees](09-data-management/02-storage-and-indexing/b-trees.md) | The buffer pool keeps hot pages in memory; a B-tree's upper levels almost always hit. |
| 10 | [Scalability patterns](10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) | A cache in front of a database absorbs most reads, trading freshness for load and latency. |
| 12 | [Build and continuous delivery](12-software-engineering/04-operations/build-and-continuous-delivery.md) | Build caches reuse outputs whose inputs have not changed. |
| 13 | [Attention and transformers](13-artificial-intelligence/03-deep-learning/attention-and-transformers.md) | The key-value (KV) cache stores past tokens' attention keys and values so generation does not recompute them. |

**When it hurts.** A copy can go stale, so every cache needs an invalidation story, and keeping many caches of one memory consistent is a whole subject ([multicore and cache coherence](04-computer-architecture/04-parallel-architecture/multicore-and-cache-coherence.md)). A workload without locality (a scan larger than the cache) makes caches pure overhead, and shared caches leak timing information ([side channels](11-security-and-cryptography/03-system-security/side-channels.md)). See [state and time](#state-and-time), [indirection and naming](#indirection-and-naming) and [batching and amortization](#batching-and-amortization).

## Pipelining and parallelism

**Claim: when pieces of work do not depend on each other, doing them at the same time raises throughput.** Pipelining overlaps successive tasks in time, each at a different stage, so one task finishes per stage-time even though each still takes the whole pipeline. Parallelism replicates units in space. Two forces push this into every layer. Since about 2005 the end of Dennard scaling stopped clock rates rising, so extra transistors could buy speed only through concurrency. And communication is slow relative to computation, so a system must keep many operations in flight to keep a long pipe full (the bandwidth-delay product).

| Layer | Where it appears | How it shows up |
|---|---|---|
| 01 | [Abstract algebra](01-mathematical-foundations/04-algebra/abstract-algebra.md) | Associativity lets a reduction be evaluated as a tree in logarithmic depth instead of a chain. |
| 03 | [Arithmetic and building blocks](03-digital-logic/02-combinational-logic/arithmetic-and-building-blocks.md) | Parallel-prefix adders compute all carries at once, trading area for depth. |
| 03 | [Clocking and synchronous design](03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md) | Inserting registers into a long path shortens the cycle: more latency, more throughput. |
| 04 | [Pipelining](04-computer-architecture/02-processor-microarchitecture/pipelining.md) | The instruction pipeline is the canonical example. |
| 04 | [SIMD and GPUs](04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) | Single Instruction, Multiple Data (SIMD) lanes and Graphics Processing Units (GPUs) apply one operation to many data items. |
| 04 | [DMA and devices](04-computer-architecture/05-io-and-interconnect/dma-and-devices.md) | Direct Memory Access (DMA) lets devices move data while the Central Processing Unit (CPU) computes. |
| 05 | [Divide and conquer](05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) | Independent subproblems can be solved in parallel. |
| 08 | [Reliable delivery](08-networking/04-transport-layer/reliable-delivery.md) | Sliding windows keep many packets in flight to fill the pipe between distant hosts. |
| 09 | [Join algorithms](09-data-management/03-query-processing/join-algorithms.md) | Tuples stream between operators without being stored; hash partitions are joined in parallel. |
| 10 | [Work, span and parallel models](10-distributed-and-parallel-computing/01-parallel-computing/work-span-and-parallel-models.md) | Total work and the longest dependency chain (span) bound the achievable speed-up. |
| 13 | [Training at scale](13-artificial-intelligence/03-deep-learning/training-at-scale.md) | Data, tensor and pipeline parallelism split one training run over thousands of accelerators. |
| 14 | [Rasterization pipeline](14-human-and-visual-computing/02-computer-graphics/rasterization-pipeline.md) | The graphics pipeline processes millions of independent vertices and pixels at once. |

**When it hurts.** Dependencies stall pipelines (hazards), parallel workers must coordinate, and the serial fraction caps everything ([Amdahl's law](04-computer-architecture/06-performance/amdahls-law.md)). Overlap also opens windows where operations interleave in unexpected orders, the root of race conditions. See [state and time](#state-and-time), [limits and impossibility](#limits-and-impossibility) and [batching and amortization](#batching-and-amortization).

## Batching and amortization

**Claim: when an operation has a large fixed cost and a small per-item cost, grouping many items pays the fixed cost once and drives the average cost toward the per-item cost.** Fixed costs are everywhere: a disk seek, a network round trip, an interrupt, a system call, a log flush to stable storage, a weight load from memory. They grow relative to everything else because latency improves much more slowly than bandwidth. Amortized analysis is the same idea applied to time: a rare expensive step is fine if many cheap steps pay for it.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 04 | [DRAM and storage devices](04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) | Whole cache lines, DRAM rows and disk blocks are moved at once to spread the access cost. |
| 04 | [DMA and devices](04-computer-architecture/05-io-and-interconnect/dma-and-devices.md) | DMA and interrupt coalescing spread one interrupt over a large transfer. |
| 05 | [Amortized analysis](05-algorithms-and-data-structures/01-foundations/amortized-analysis.md) | A dynamic array doubles rarely, so appends cost constant time on average. |
| 05 | [Union-find](05-algorithms-and-data-structures/02-fundamental-data-structures/union-find.md) | Path compression makes each find pay to flatten the tree for later finds. |
| 06 | [Memory management and garbage collection](06-programming-languages/04-runtime-systems/memory-management-and-garbage-collection.md) | Bump allocation and tracing collectors reclaim many objects in one pass. |
| 07 | [Memory allocation](07-operating-systems/04-memory-management/memory-allocation.md) | Slab caches and huge pages spread per-object and per-page overheads. |
| 09 | [LSM-trees](09-data-management/02-storage-and-indexing/lsm-trees.md) | Log-Structured Merge (LSM) trees buffer writes in memory and flush them as sorted sequential runs. |
| 09 | [Recovery and logging](09-data-management/04-transactions/recovery-and-logging.md) | Group commit shares one log flush among many transactions. |
| 10 | [Batch and stream processing](10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) | Micro-batches and bulk writes spread scheduling and coordination costs. |
| 12 | [Build and continuous delivery](12-software-engineering/04-operations/build-and-continuous-delivery.md) | The counter-example: large release batches amortise overhead but delay feedback, so modern practice shrinks them. |
| 13 | [Learning as optimization](13-artificial-intelligence/02-machine-learning-foundations/learning-as-optimization.md) | Mini-batch gradient descent shares one pass over the weights among many examples. |

**When it hurts.** The first item in a batch waits for the last, so batching buys throughput with latency. An amortized bound also hides occasional long pauses (a table resize, a collection, a compaction), which matter in real-time and tail-latency settings. See [tradeoffs](#tradeoffs), [pipelining and parallelism](#pipelining-and-parallelism) and [feedback and control](#feedback-and-control).

## Redundancy and fault tolerance

**Claim: a reliable system can be built from unreliable parts, by adding extra copies, extra bits or extra attempts, provided failures are detected or outvoted and are independent.** John von Neumann showed this in the 1950s, and it is the only option, because every component eventually fails and a system that needs all of its parts fails more often than any one of them. Redundancy comes in three forms: space (replicas), information (check bits) and time (retries). The same probability reasoning governs a noise margin and a replicated database.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Reliability and redundancy](00-engineering-foundations/05-engineering-method/reliability-and-redundancy.md) | Series systems multiply reliabilities; parallel ones multiply failure probabilities; majority voting masks a fault. |
| 00 | [Noise and signal integrity](00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md) | Noise margins are redundancy in voltage space. |
| 02 | [Channel capacity and error correction](02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) | Error-correcting codes add mathematically designed redundancy; Shannon showed reliable communication is possible at any rate below capacity. |
| 02 | [Qubits and quantum circuits](02-theory-of-computation/05-quantum-computation/qubits-and-quantum-circuits.md) | Quantum error correction spreads one logical qubit across many physical ones. |
| 04 | [DRAM and storage devices](04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) | Error-Correcting Code (ECC) memory and redundant disk arrays survive bit flips and device failures. |
| 07 | [Crash consistency and journaling](07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md) | Journals and copy-on-write keep a redundant record that makes crashes survivable. |
| 08 | [Encoding and framing](08-networking/02-link-layer/encoding-and-framing.md) | Cyclic Redundancy Checks (CRCs) add bits to detect damaged frames. |
| 08 | [Reliable delivery](08-networking/04-transport-layer/reliable-delivery.md) | Retransmission is redundancy in time. |
| 09 | [Recovery and logging](09-data-management/04-transactions/recovery-and-logging.md) | The write-ahead log lets committed work be redone and uncommitted work undone after a crash. |
| 10 | [Replication](10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) | Copies plus quorums survive a bounded number of failed machines. |
| 11 | [Security design principles](11-security-and-cryptography/01-security-principles/security-design-principles.md) | Defence in depth: several independent barriers, so one breach is not total. |
| 12 | [Reliability engineering](12-software-engineering/04-operations/reliability-engineering.md) | Replicas across zones, canaries and rollbacks keep a service up while it changes. |

**When it hurts.** Redundancy works only to the degree that failures are independent; a shared power supply, a bug present in every replica or a bad configuration pushed everywhere defeats it. Redundancy also adds cost and complexity, and complexity causes failures of its own. Replicas that can be updated must agree, which drags in [state and time](#state-and-time) and the [limits](#limits-and-impossibility) of consensus. See also [the end-to-end argument](#the-end-to-end-argument) and [tradeoffs](#tradeoffs).

## The end-to-end argument

**Claim: a function that can be done completely and correctly only with knowledge held at the endpoints of a system must be done there; doing it in a lower layer is at best a performance optimisation.** Saltzer, Reed and Clark stated it in "End-to-End Arguments in System Design" (1984). The force behind it is that every component between two endpoints can fail, reorder, or lie, and only the endpoint knows what "correct" means for its own data. So a check in the middle cannot replace a check at the end, and since the end must check anyway, the middle can stay simple.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 07 | [Page replacement](07-operating-systems/04-memory-management/page-replacement.md) | A database knows its access pattern better than the Operating System (OS) does, so it often manages its own buffer. |
| 07 | [Crash consistency and journaling](07-operating-systems/05-storage-and-file-systems/crash-consistency-and-journaling.md) | A consistent file system can still hold a half-updated application file; applications must `fsync` and check their own data. |
| 08 | [Layering and the end-to-end principle](08-networking/01-principles/layering-and-the-end-to-end-principle.md) | Where it was first argued: reliability lives in the hosts, and the network core stays simple and stateless. |
| 08 | [Wireless networks](08-networking/02-link-layer/wireless-networks.md) | Wi-Fi retransmits lost frames locally: a valid optimisation on a lossy hop, never a guarantee. |
| 08 | [UDP and TCP](08-networking/04-transport-layer/udp-and-tcp.md) | TCP builds reliable, ordered delivery in the end hosts on top of best-effort Internet Protocol (IP) packets. |
| 10 | [Batch and stream processing](10-distributed-and-parallel-computing/05-large-scale-systems/batch-and-stream-processing.md) | "Exactly-once" effects come from idempotent processing at the endpoints, not from perfectly reliable links. |
| 11 | [Secure protocols and TLS](11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md) | Transport Layer Security (TLS) encrypts and authenticates at the endpoints that hold the keys. |
| 11 | [Network attacks and defences](11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md) | Firewalls help, but only endpoint authentication and encryption are sufficient. |

**When it hurts.** Pushing everything to the edges can waste resources (retransmitting across a continent what one hop could have fixed) and duplicates work in every application. In practice middleboxes (address translators, firewalls, load balancers) erode the principle and freeze protocols in place. It sits in constant tension with [abstraction and layering](#abstraction-and-layering), and it is a special case of [trust and verification](#trust-and-verification): check where you actually know the answer.

## Tradeoffs

**Claim: improving one property of a design almost always costs another, because the properties draw on the same limited resources.** Energy, time, area, bits, money and human attention are finite, and physical and mathematical laws couple them. Faster switching costs power; more replicas cost money and coordination; more generality costs speed. A good design is therefore a choice of which side of each trade to take, made explicit and measured, not a search for a design with no costs. The specific trades change with each layer, but the habit of naming them is the same.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Tradeoffs and constraints](00-engineering-foundations/05-engineering-method/tradeoffs-and-constraints.md) | Introduced as a method: identify constraints, find the Pareto frontier, pick a point on it. |
| 03 | [Floating point](03-digital-logic/01-number-representation/floating-point.md) | A fixed number of bits splits between range (exponent) and precision (significand). |
| 03 | [Timing and power](03-digital-logic/04-hardware-design/timing-and-power.md) | Area, delay and power trade against each other in every block; supply voltage trades speed for energy. |
| 04 | [SIMD and GPUs](04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) | Latency versus throughput: a CPU is built to finish one thread fast, a GPU to finish many slowly. |
| 05 | [Randomized algorithms](05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) | A tiny probability of error or slowness buys speed or simplicity. |
| 07 | [Kernel architectures](07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md) | Monolithic kernels buy speed; microkernels buy isolation. |
| 07 | [Address spaces and paging](07-operating-systems/04-memory-management/address-spaces-and-paging.md) | Page size trades TLB reach against wasted memory inside pages. |
| 08 | [Latency, bandwidth and queueing](08-networking/01-principles/latency-bandwidth-and-queueing.md) | Bigger buffers trade packet loss for queueing delay. |
| 09 | [LSM-trees](09-data-management/02-storage-and-indexing/lsm-trees.md) | Read, write and space amplification cannot all be minimised at once. |
| 10 | [Consistency models](10-distributed-and-parallel-computing/03-consensus-and-replication/consistency-models.md) | Stronger consistency costs latency and, during partitions, availability. |
| 12 | [Reliability engineering](12-software-engineering/04-operations/reliability-engineering.md) | An error budget makes reliability versus feature velocity an explicit, measured trade. |
| 13 | [Generalization and bias-variance](13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) | A flexible model fits training data better but generalises worse unless data grows. |

**When it hurts.** The usual failure is to forget that a trade was made: optimising one measured number while an unmeasured one decays, or carrying a choice past the conditions that justified it. Some trades are not engineering choices at all but hard bounds; see [limits and impossibility](#limits-and-impossibility). Almost every pair in [Principles that pull against each other](#principles-that-pull-against-each-other) is a tradeoff in this sense.

## Invariants and correctness

**Claim: since a program's executions are too many to check one by one, state a property that every step preserves, and induction then proves it holds forever.** An invariant converts an infinite set of behaviours into two finite checks: it holds at the start, and each step that starts with it ends with it. That is why the same move works for a loop, a data structure, a circuit, a lock, a database and a consensus protocol. Specifications split into safety ("nothing bad ever happens", an invariant) and liveness ("something good eventually happens").

| Layer | Where it appears | How it shows up |
|---|---|---|
| 01 | [Induction and recurrences](01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) | Induction is the proof mechanism behind every invariant argument. |
| 03 | [Clocking and synchronous design](03-digital-logic/03-sequential-logic/clocking-and-synchronous-design.md) | Setup and hold constraints are invariants that every path must keep. |
| 04 | [Superscalar and out-of-order](04-computer-architecture/02-processor-microarchitecture/superscalar-and-out-of-order.md) | In-order commit keeps the visible state equal to some sequential execution, however wild the internal order. |
| 05 | [Correctness and invariants](05-algorithms-and-data-structures/01-foundations/correctness-and-invariants.md) | Loop invariants and representation invariants are the main proof tool for algorithms. |
| 05 | [Heaps and priority queues](05-algorithms-and-data-structures/02-fundamental-data-structures/heaps-and-priority-queues.md) | Heap order is restored after every insert and delete. |
| 06 | [Type systems](06-programming-languages/02-semantics-and-types/type-systems.md) | A type is an invariant the compiler checks at every use. |
| 06 | [Hoare logic and program proofs](06-programming-languages/05-formal-methods/hoare-logic-and-program-proofs.md) | Pre- and postconditions and loop invariants turn correctness into logic. |
| 07 | [Locks and semaphores](07-operating-systems/03-concurrency/locks-and-semaphores.md) | A lock marks the region where an invariant may be broken, so no other thread sees it broken. |
| 09 | [Concurrency control](09-data-management/04-transactions/concurrency-control.md) | Serializability preserves any invariant that each transaction preserves alone. |
| 10 | [Consensus](10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) | "At most one value is chosen" is kept by quorum intersection. |
| 11 | [Memory-safety vulnerabilities](11-security-and-cryptography/03-system-security/memory-safety-vulnerabilities.md) | Memory safety is an invariant that unsafe languages leave to the programmer, and attackers exploit its violations. |
| 12 | [Testing](12-software-engineering/03-quality/testing.md) | Assertions and contracts state what must hold; tests check it on examples. |

**When it hurts.** Most operations must break an invariant briefly on the way to restoring it, and that window is where crashes, interrupts and other threads cause damage. An invariant is also only as good as the specification it encodes: a proved program can still do the wrong thing. See [state and time](#state-and-time), [trust and verification](#trust-and-verification) and [recursion and self-reference](#recursion-and-self-reference).

## Recursion and self-reference

**Claim: defining a thing in terms of smaller instances of itself, plus a base case, gives a finite description of an unbounded structure; and because programs are data, programs can take programs as input.** The first half is why recursion and induction are everywhere: trees, grammars, divide-and-conquer and proofs all have this shape. The second half gives universality (one machine can run any program) and, by the same move, the deepest impossibility results: a program that asks about itself can be made to contradict any claimed answer.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 01 | [Induction and recurrences](01-mathematical-foundations/03-discrete-mathematics/induction-and-recurrences.md) | Recursive definitions and structural induction are two sides of one idea. |
| 01 | [Sets](01-mathematical-foundations/02-sets-relations-functions/sets.md) | Russell's paradox: unrestricted self-reference breaks naive set theory. |
| 02 | [Context-free grammars and pushdown automata](02-theory-of-computation/02-automata-and-formal-languages/context-free-grammars-and-pushdown-automata.md) | Grammar rules are recursive definitions, and a stack is how recursion is executed. |
| 02 | [Lambda calculus](02-theory-of-computation/03-computability/lambda-calculus.md) | The Y combinator builds recursion from nothing but function application. |
| 02 | [Turing machines](02-theory-of-computation/03-computability/turing-machines.md) | The universal machine takes another machine's description as input. |
| 02 | [Halting problem and undecidability](02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) | Diagonalisation: a program fed its own description defeats any halting decider. |
| 05 | [Divide and conquer](05-algorithms-and-data-structures/03-design-paradigms/divide-and-conquer.md) | Split, solve smaller instances, combine; the recurrence gives the cost. |
| 05 | [Dynamic programming](05-algorithms-and-data-structures/03-design-paradigms/dynamic-programming.md) | Optimal solutions defined from optimal sub-solutions, computed once each. |
| 05 | [String matching](05-algorithms-and-data-structures/06-string-algorithms/string-matching.md) | The Knuth–Morris–Pratt failure function describes how a pattern matches itself. |
| 06 | [Lexing and parsing](06-programming-languages/03-compilers/lexing-and-parsing.md) | Recursive-descent parsers mirror the recursive grammar one function per rule. |
| 13 | [Reinforcement learning](13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) | The Bellman equation defines a state's value in terms of the values of its successors. |

**When it hurts.** Naive recursion can recompute the same subproblem exponentially often (fixed by [caching](#caching-and-locality) as memoisation) or exhaust the stack. Unrestricted self-reference produces paradox and undecidability, which is the source of many [limits and impossibility](#limits-and-impossibility) results. Its proofs rely on [invariants](#invariants-and-correctness) by induction.

## Virtualization

**Claim: a layer that implements a resource's interface on top of a different resource can make one thing look like many, many look like one, or one kind of thing look like another.** It recurs because hardware is expensive and must be shared safely, because programs should not care which physical machine they run on, and because an interposed layer is a natural place to enforce isolation. Popek and Goldberg (1974) stated when a machine can be virtualized efficiently: every sensitive instruction must trap when run without privilege.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 02 | [Turing machines](02-theory-of-computation/03-computability/turing-machines.md) | The universal Turing machine is the first virtual machine: one machine imitating any other. |
| 04 | [Virtual-memory hardware](04-computer-architecture/03-memory-hierarchy/virtual-memory-hardware.md) | Hardware translation gives each program its own address space; virtualization extensions add a second level for guests. |
| 06 | [Interpreters and virtual machines](06-programming-languages/04-runtime-systems/interpreters-and-virtual-machines.md) | A process virtual machine (such as the Java Virtual Machine) presents a portable machine on top of a real one. |
| 07 | [Processes](07-operating-systems/02-process-management/processes.md) | Time-sharing makes one CPU look like many private processors. |
| 07 | [Address spaces and paging](07-operating-systems/04-memory-management/address-spaces-and-paging.md) | One physical memory becomes many private address spaces, each larger than physical memory. |
| 07 | [File-system abstractions](07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md) | A disk of numbered blocks becomes a tree of named, growable files. |
| 07 | [Virtual machines and hypervisors](07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md) | A hypervisor makes one machine look like many complete machines. |
| 07 | [Containers](07-operating-systems/07-virtualization/containers.md) | Virtualizing the OS interface instead of the hardware: lighter, but with a shared kernel. |
| 10 | [Cloud computing](10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) | The cloud makes a data centre look like an elastic pool, and many machines look like one service. |
| 11 | [Isolation and sandboxing](11-security-and-cryptography/03-system-security/isolation-and-sandboxing.md) | Isolation by giving each principal its own virtual machine or address space. |

**When it hurts.** Every virtual layer costs some performance, and the illusion of a private resource is imperfect: tenants share caches, memory bandwidth and the hypervisor, which produces noisy neighbours and cross-tenant side channels. The strength of isolation is the size of what is still shared. See [indirection and naming](#indirection-and-naming) (virtualization is usually built from it), [abstraction and layering](#abstraction-and-layering) and [trust and verification](#trust-and-verification).

## State and time

**Claim: once a system holds mutable state that more than one actor can change, its behaviour depends on the order of events, and signals that travel at finite speed make that order hard to know.** Concurrency bugs, crash inconsistencies and distributed anomalies are all the same bug: code assumed an order that the system did not guarantee. It recurs at every scale because the physics does: inside one chip, "simultaneous" is already approximate, and between machines a slow reply cannot be told apart from a dead one. Each layer must decide what "before" means and pay to enforce it.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Capacitance and timing](00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md) | Every wire takes time to charge, so signals arrive at different moments. |
| 03 | [Latches and flip-flops](03-digital-logic/03-sequential-logic/latches-and-flip-flops.md) | Flip-flops define "what was"; metastability is the irreducible cost of forcing continuous time into discrete steps. |
| 04 | [Buses and interrupts](04-computer-architecture/05-io-and-interconnect/buses-and-interrupts.md) | Interrupts arrive at arbitrary points in a program. |
| 04 | [Memory consistency models](04-computer-architecture/04-parallel-architecture/memory-consistency-models.md) | The order in which one core's stores become visible to another is a contract, and often a weak one. |
| 06 | [Functional programming](06-programming-languages/01-paradigms/functional.md) | Immutable values remove the problem for most code by never changing state in place. |
| 07 | [Race conditions and critical sections](07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md) | Interleaved read-modify-write sequences lose updates. |
| 08 | [Reliable delivery](08-networking/04-transport-layer/reliable-delivery.md) | Sequence numbers reconstruct order; timeouts guess at failure. |
| 09 | [Concurrency control](09-data-management/04-transactions/concurrency-control.md) | Locking and multiversion concurrency control order conflicting transactions. |
| 10 | [Time, clocks and ordering](10-distributed-and-parallel-computing/02-distributed-foundations/time-clocks-and-ordering.md) | Lamport's happened-before relation (1978) replaces the missing global clock with a partial order. |
| 10 | [Replication](10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) | Replication is agreement on the order of state changes. |
| 10 | [Eventual consistency and CRDTs](10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md) | Conflict-free Replicated Data Types (CRDTs) and version vectors accept concurrent updates and merge them. |
| 12 | [Version control](12-software-engineering/02-process/version-control.md) | A repository is a history of state; merges reconcile concurrent changes. |

**When it hurts.** Enforcing order costs coordination, which costs latency and, under network partition, availability. So systems weaken their ordering guarantees for speed and hand the complexity to programmers, who then write the bugs. See [tradeoffs](#tradeoffs), [invariants and correctness](#invariants-and-correctness), [caching and locality](#caching-and-locality) and [limits and impossibility](#limits-and-impossibility).

## Encoding and representation

**Claim: the same information can be written down in many ways, and each way makes some operations cheap and others expensive, so choosing a representation is choosing a cost profile.** Adding numbers is easy in two's complement and hard in Roman numerals; range queries are easy in a sorted array and hard in a hash table; analytic scans are fast over columns and slow over rows. This recurs because computation is always the manipulation of a representation, never of the thing itself. The best algorithmic gains often come from changing the representation, not the procedure.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Sampling and quantization](00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) | Choosing sample rate and resolution decides what information survives the move to digital. |
| 01 | [Functions and cardinality](01-mathematical-foundations/02-sets-relations-functions/functions-and-cardinality.md) | Bijections are exactly the lossless re-encodings. |
| 02 | [Source coding and compression](02-theory-of-computation/01-information-theory/source-coding-and-compression.md) | Give frequent messages short codes; entropy says how short they can get. |
| 03 | [Integers and two's complement](03-digital-logic/01-number-representation/integers-and-twos-complement.md) | One adder handles signed and unsigned numbers because of the encoding chosen. |
| 03 | [Floating point](03-digital-logic/01-number-representation/floating-point.md) | Institute of Electrical and Electronics Engineers (IEEE) 754 trades exactness for enormous range. |
| 04 | [Instruction encoding and addressing](04-computer-architecture/01-instruction-set-architecture/instruction-encoding-and-addressing.md) | Fixed-length instructions decode simply; variable-length ones are denser. |
| 05 | [Non-comparison sorting](05-algorithms-and-data-structures/04-sorting-and-searching/non-comparison-sorting.md) | Radix sort beats the comparison bound by looking at how keys are encoded. |
| 05 | [Tries and suffix structures](05-algorithms-and-data-structures/06-string-algorithms/tries-and-suffix-structures.md) | The Burrows–Wheeler transform is both an index and a compressor. |
| 08 | [Encoding and framing](08-networking/02-link-layer/encoding-and-framing.md) | Line codes choose signal shapes for clock recovery and balance. |
| 09 | [Storage layouts](09-data-management/02-storage-and-indexing/storage-layouts.md) | Row stores favour transactions; column stores favour analytics and compress well. |
| 11 | [Web security](11-security-and-cryptography/04-network-and-application-security/web-security.md) | Injection attacks happen when data and code share one representation. |
| 13 | [Retrieval and embeddings](13-artificial-intelligence/04-advanced-paradigms/retrieval-and-embeddings.md) | Learned embeddings turn meaning into geometry, so similarity becomes a distance. |
| 14 | [Geometry and transformations](14-human-and-visual-computing/02-computer-graphics/geometry-and-transformations.md) | Homogeneous coordinates make every transform, including translation, a matrix multiply. |

**When it hurts.** A fixed-size encoding has edges (overflow, rounding, truncation), and ambiguous encodings are a classic source of security holes. Formats also outlive their reasons: once data is stored or a protocol is deployed, its encoding is very hard to change. See [limits and impossibility](#limits-and-impossibility), [tradeoffs](#tradeoffs) and [interface vs implementation](#interface-vs-implementation).

## Limits and impossibility

**Claim: some bounds hold for every possible design, so no cleverness escapes them; knowing them tells you when to stop searching and which assumption to relax instead.** They come from four sources. Physics: the speed of light, thermal noise, the Landauer bound on erasing a bit. Information: entropy bounds compression and capacity bounds reliable rate. Counting: there are more problems than programs, and more orderings than a few comparisons can tell apart. Logic: diagonal arguments that turn any claimed solver against itself.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Thermodynamics and energy](00-engineering-foundations/01-physics-of-computation/thermodynamics-and-energy.md) | Erasing a bit dissipates at least `kT ln 2` of energy (the Landauer bound), and heat removal caps power density. |
| 00 | [Sampling and quantization](00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) | The Nyquist rate and quantization noise are hard bounds on digitising a signal. |
| 01 | [Predicate logic](01-mathematical-foundations/01-logic/predicate-logic.md) | First-order validity is undecidable, and Gödel showed rich theories are incomplete. |
| 02 | [Entropy and information](02-theory-of-computation/01-information-theory/entropy-and-information.md) | No lossless code beats the entropy of its source on average. |
| 02 | [Halting problem and undecidability](02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) | Halting and, by Rice's theorem, every non-trivial question about program behaviour is undecidable. |
| 02 | [P, NP and NP-completeness](02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) | NP-complete problems are believed to need super-polynomial time in the worst case. |
| 04 | [Amdahl's law](04-computer-architecture/06-performance/amdahls-law.md) | The serial fraction caps the speed-up from any amount of parallel hardware. |
| 04 | [Power and the end of scaling](04-computer-architecture/06-performance/power-and-the-end-of-scaling.md) | Power density means not all of a chip can switch at full speed at once. |
| 05 | [Comparison sorting](05-algorithms-and-data-structures/04-sorting-and-searching/comparison-sorting.md) | Any comparison sort needs Ω(n log n) comparisons, because there are n! orders to distinguish. |
| 10 | [Impossibility results](10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md) | The Fischer–Lynch–Paterson (FLP) result, the CAP (Consistency, Availability, Partition tolerance) theorem and the Byzantine bound. |
| 11 | [Foundations of modern cryptography](11-security-and-cryptography/02-cryptography/foundations-of-modern-cryptography.md) | Perfect secrecy needs a key as long as the message, so practical cryptography rests on assumed computational hardness. |
| 13 | [Generalization and bias-variance](13-artificial-intelligence/02-machine-learning-foundations/generalization-and-bias-variance.md) | No Free Lunch: averaged over all problems, no learner beats any other. |

**When it hurts.** A limit is a statement about a model, so it is misused when the model does not fit: worst-case hardness does not stop solvers from handling most real instances, and FLP does not stop consensus in practice. The productive response is to relax an assumption (randomise, approximate, add timeouts, restrict the language) rather than to give up. See [tradeoffs](#tradeoffs), [recursion and self-reference](#recursion-and-self-reference) and [trust and verification](#trust-and-verification).

## Feedback and control

**Claim: when a system or its environment is unknown or changing, measuring the output and adjusting the input works better than predicting in advance.** Negative feedback makes a system precise and robust even when its parts are not, because errors are measured and opposed. Positive feedback drives a system to an extreme, which is what memory and clean decisions need. The same loop recurs from amplifiers to TCP to training neural networks because, at every layer, the designer cannot know the load, the network or the data ahead of time.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Feedback and control](00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) | Negative feedback trades gain for precision; delay in the loop causes oscillation. |
| 01 | [Optimization](01-mathematical-foundations/05-continuous-mathematics/optimization.md) | Gradient descent measures the slope of the error and steps against it. |
| 03 | [Latches and flip-flops](03-digital-logic/03-sequential-logic/latches-and-flip-flops.md) | Positive feedback between cross-coupled gates is what stores a bit. |
| 03 | [Timing and power](03-digital-logic/04-hardware-design/timing-and-power.md) | Dynamic Voltage and Frequency Scaling (DVFS) adjusts the operating point from measured load and temperature. |
| 06 | [JIT compilation](06-programming-languages/04-runtime-systems/jit-compilation.md) | Profiles of real execution decide what to optimise, and failed guesses trigger deoptimisation. |
| 07 | [Scheduling](07-operating-systems/02-process-management/scheduling.md) | Multi-level feedback queues infer whether a job is interactive from its past behaviour. |
| 08 | [Media access and Ethernet](08-networking/02-link-layer/media-access-and-ethernet.md) | Exponential backoff adapts the retry rate to observed collisions. |
| 08 | [Congestion control](08-networking/04-transport-layer/congestion-control.md) | TCP infers congestion from loss and delay and grows or shrinks its window. |
| 10 | [Scalability patterns](10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) | Backpressure and load shedding push back on overload; autoscaling adjusts capacity to load. |
| 12 | [Observability](12-software-engineering/04-operations/observability.md) | Metrics, logs and traces close the loop between a running system and the people who change it. |
| 13 | [Reinforcement learning](13-artificial-intelligence/04-advanced-paradigms/reinforcement-learning.md) | Learned closed-loop control: act, observe reward, adjust the policy. |
| 14 | [Interaction design principles](14-human-and-visual-computing/01-human-computer-interaction/interaction-design-principles.md) | Interaction is a human-in-the-loop cycle of action, feedback and evaluation. |

**When it hurts.** A loop that reacts too late or too strongly oscillates: retry storms, flapping autoscalers, thrashing. A loop also optimises exactly what it measures, so a measure that becomes a target stops being a good measure (Goodhart's law), and a model whose outputs shape its future training data can reinforce its own errors. See [state and time](#state-and-time), [batching and amortization](#batching-and-amortization) and [trust and verification](#trust-and-verification).

## Composition

**Claim: you can build big things from small things only if the properties of the whole follow predictably from the properties of the parts and the rule that combines them.** Where that holds, the whole field scales: gates into processors, functions into programs, operators into queries, layers into deep networks. It holds when the combining rule is closed (the result is the same kind of thing as the inputs) and the property survives the rule (delays add along a path; types check piece by piece). Much of design is choosing building blocks whose important properties do compose.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [CMOS](00-engineering-foundations/03-semiconductor-devices/cmos.md) | Transistors in series and parallel compose into AND and OR, with a predictable dual network. |
| 01 | [Calculus](01-mathematical-foundations/05-continuous-mathematics/calculus.md) | The chain rule differentiates any composition of differentiable pieces. |
| 01 | [Linear algebra](01-mathematical-foundations/04-algebra/linear-algebra.md) | Composing linear maps is multiplying their matrices. |
| 02 | [Finite automata and regular languages](02-theory-of-computation/02-automata-and-formal-languages/finite-automata-and-regular-languages.md) | The product construction combines automata with predictable results. |
| 03 | [Logic gates](03-digital-logic/02-combinational-logic/logic-gates.md) | A functionally complete set (NAND alone) composes into any Boolean function. |
| 04 | [Amdahl's law](04-computer-architecture/06-performance/amdahls-law.md) | Speed-ups of parts combine through Amdahl's law, not by multiplication. |
| 06 | [Functional programming](06-programming-languages/01-paradigms/functional.md) | Pure functions compose predictably; shared mutable state does not. |
| 07 | [Deadlock](07-operating-systems/03-concurrency/deadlock.md) | Lock-based code does not compose: two correct modules can deadlock together. |
| 09 | [Relational algebra and SQL](09-data-management/01-data-models/relational-algebra-and-sql.md) | Relational operators take relations and return relations, so queries nest freely. |
| 10 | [Eventual consistency and CRDTs](10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md) | Replicas converge because merge is a join in a semilattice: associative, commutative, idempotent. |
| 11 | [Security design principles](11-security-and-cryptography/01-security-principles/security-design-principles.md) | Secure parts do not automatically compose into a secure whole. |
| 13 | [Neural networks and backpropagation](13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md) | Deep networks are compositions of simple layers whose gradients compose by the chain rule. |

**When it hurts.** Some properties are emergent: performance, security, deadlock-freedom and failure behaviour often belong to the combination, not the parts, which is why [software architecture](12-software-engineering/01-design/software-architecture.md) is largely the study of which qualities survive combining components. See [abstraction and layering](#abstraction-and-layering), [invariants and correctness](#invariants-and-correctness) and [state and time](#state-and-time).

## Trust and verification

**Claim: no one can check everything, so every system rests on some trusted base; good design makes that base small and checks the rest with methods cheaper than redoing the work.** Checking can be far cheaper than finding: an NP certificate, a digital signature or a proof is quick to verify even when it was expensive to produce. So the recurring move is to shrink what must be trusted (a kernel, a proof checker, a key) and verify everything that crosses it. The same logic applies to hardware, protocols, software and machine-learned models whose behaviour is not written down anywhere.

| Layer | Where it appears | How it shows up |
|---|---|---|
| 00 | [Measurement and modeling](00-engineering-foundations/05-engineering-method/measurement-and-modeling.md) | Measure what you can rather than trusting models or intuition. |
| 01 | [Proof techniques](01-mathematical-foundations/01-logic/proof-techniques.md) | A proof lets a reader check a claim without trusting its author. |
| 02 | [P, NP and NP-completeness](02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) | NP is exactly the problems whose answers can be checked quickly. |
| 03 | [FPGA and ASIC](03-digital-logic/04-hardware-design/fpga-and-asic.md) | An Application-Specific Integrated Circuit (ASIC) cannot be patched after fabrication, so verification dominates the effort. |
| 06 | [Proof assistants and dependent types](06-programming-languages/05-formal-methods/proof-assistants-and-dependent-types.md) | A small trusted proof kernel makes enormous machine-made proofs believable. |
| 07 | [Kernel architectures](07-operating-systems/01-kernel-and-abstractions/kernel-architectures.md) | The kernel is the trusted computing base; seL4's machine-checked proof shows a small one can be verified. |
| 08 | [Internet routing and BGP](08-networking/03-network-layer/internet-routing-and-bgp.md) | BGP accepts neighbours' route claims, and route hijacks exploit that trust. |
| 10 | [Byzantine fault tolerance](10-distributed-and-parallel-computing/03-consensus-and-replication/byzantine-fault-tolerance.md) | Trust no single replica; with `3f + 1` replicas, agreement survives `f` arbitrary liars. |
| 11 | [Public-key cryptography](11-security-and-cryptography/02-cryptography/public-key-cryptography.md) | Signatures and certificates move trust from the channel to the keys. |
| 11 | [Software supply-chain security](11-security-and-cryptography/04-network-and-application-security/software-supply-chain-security.md) | Every dependency and build tool is in the trusted base, whether or not it was checked. |
| 12 | [Static analysis and code review](12-software-engineering/03-quality/static-analysis-and-code-review.md) | Layered checks, none sufficient alone, each reducing what must be taken on faith. |
| 13 | [Evaluation and experimentation](13-artificial-intelligence/02-machine-learning-foundations/evaluation-and-experimentation.md) | Held-out data is the only check on a model that has no specification. |
| 13 | [Alignment and safety](13-artificial-intelligence/04-advanced-paradigms/alignment-and-safety.md) | Evaluating and steering systems whose internal goals cannot be read directly. |

**When it hurts.** The trusted base is usually larger than it looks: everything below an abstraction is trusted by default, including compilers, firmware and hardware (Ken Thompson's "Reflections on Trusting Trust", 1984, showed a compiler can hide a backdoor that no source review finds). Verification is also bounded by [undecidability](#limits-and-impossibility), so every automatic checker is incomplete, unsound or limited in scope. See [the end-to-end argument](#the-end-to-end-argument), [abstraction and layering](#abstraction-and-layering) and [redundancy and fault tolerance](#redundancy-and-fault-tolerance).

## Principles that pull against each other

The principles above are not a checklist to apply all at once. Many of them pull in opposite directions, and most hard design decisions are about where to stand between two of them.

| Tension | Why they conflict | Where you meet it |
|---|---|---|
| [Caching](#caching-and-locality) vs [state and time](#state-and-time) | A copy is fast because it is not checked against the original, so it can go stale. | Cache coherence, DNS time-to-live values, CDN invalidation, read replicas. |
| [Abstraction](#abstraction-and-layering) vs [tradeoffs](#tradeoffs) of performance | Hiding detail hides the detail you need to go fast. | The RAM model versus caches, ORMs versus hand-written SQL, `O_DIRECT` and kernel bypass. |
| [Layering](#abstraction-and-layering) vs [the end-to-end argument](#the-end-to-end-argument) | Layers want each function in one place; correctness says the ends must check anyway. | Link versus transport retransmission, file-system versus application consistency. |
| [Redundancy](#redundancy-and-fault-tolerance) vs cost and [state and time](#state-and-time) | Every copy costs money, and every writable copy must be kept in agreement. | Replication factor, quorum size, the CAP theorem. |
| [Batching](#batching-and-amortization) vs [feedback](#feedback-and-control) and latency | Big batches are efficient but slow to complete and slow to learn from. | Group commit, mini-batch size, release size. |
| [Indirection](#indirection-and-naming) vs speed and [trust](#trust-and-verification) | Each level of naming adds a lookup and a place where the mapping can be corrupted. | Page-table walks and TLBs, DNS spoofing, virtual dispatch versus inlining. |
| [Pipelining and parallelism](#pipelining-and-parallelism) vs [invariants](#invariants-and-correctness) | Overlapping work creates interleavings that break assumptions. | Pipeline hazards, data races, speculative execution leaks such as Spectre. |
| [Virtualization](#virtualization) vs [trust](#trust-and-verification) | Sharing hardware is the point, and sharing hardware leaks information. | Cross-tenant side channels, containers sharing one kernel. |
| [Composition](#composition) vs [state and time](#state-and-time) | Shared mutable state couples parts that looked independent. | Locks that deadlock together, global variables, distributed transactions. |

[Limits and impossibility](#limits-and-impossibility) referee all of these: they say which corners of each trade-off no design can reach. And [encoding and representation](#encoding-and-representation) is often the way out, because a better representation can move the whole frontier rather than slide along it.
