# Computer Science from First Principles

A layered knowledge base of Computer Science (CS). It starts with the physics and engineering that make a switch possible and climbs, one dependency at a time, to operating systems, networks, distributed systems, Artificial Intelligence (AI) and computing's place in society.

- **Leaves** (`*.md` files) hold the few load-bearing tenets you need to understand the essence of one topic.
- **Parents** (`README.md` in each folder) explain how their children fit together and how they connect to sibling areas.
- **[CROSS-CUTTING.md](CROSS-CUTTING.md)** follows ideas that recur in every layer (abstraction, caching, indirection, redundancy…) and links each one to where it appears.
- **[_meta/PLAN.md](_meta/PLAN.md)** explains why the tree has this shape, which alternative structures were considered, and what was rejected.

## The stack

Read from the bottom up. Each layer depends only on layers with lower numbers.

```
 15  Computing in Context ............ history, ethics, law, environment: computation meets society
 14  Human & Visual Computing ........ HCI, graphics, media, vision: computation meets perception
 13  Artificial Intelligence ......... search, learning, deep learning, LLMs
 12  Software Engineering ............ building large systems with people over time
 11  Security & Cryptography ......... keeping systems correct against an adversary
 10  Distributed & Parallel .......... many machines, partial failure, no global clock
 09  Data Management ................. durable, shared, queryable state
 08  Networking ...................... moving bits between machines
 07  Operating Systems ............... virtualise, share and protect one machine
 06  Programming Languages ........... notations for computation and their translation
 05  Algorithms & Data Structures .... efficient procedures on an idealised machine
 04  Computer Architecture ........... the ISA contract and the machine behind it
 03  Digital Logic ................... Boolean algebra built from transistors  <- pillars meet
 02  Theory of Computation ........... what can be computed, how fast, with how much information
 01  Mathematical Foundations ........ the formal root: logic, discrete math, algebra, probability
 00  Engineering Foundations ......... the physical root: charge, transistors, signals, trade-offs
```

CS has **two roots**. The *physical* one (00) explains how matter can be made to switch reliably. The *formal* one (01, then 02) explains what switching can compute. They meet in **03 Digital Logic**, where Boolean algebra is built out of transistors. Every layer from 04 upward uses both.

## Layers

| # | Layer | The question it answers | Its key contribution to the stack |
|---|---|---|---|
| 00 | [Engineering Foundations](00-engineering-foundations/README.md) | How can physical matter store and switch information reliably? | The digital switch: valid levels in, restored levels out, at a known delay and energy; plus the engineering habit of trade-offs |
| 01 | [Mathematical Foundations](01-mathematical-foundations/README.md) | What language lets us state and prove things about computation? | A shared formal vocabulary (logic, sets, discrete structures, algebra, probability) with proof as the standard of truth |
| 02 | [Theory of Computation](02-theory-of-computation/README.md) | What can be computed at all, and at what cost? | Models of computation with cost measures and proved limits: undecidability, complexity classes, entropy |
| 03 | [Digital Logic](03-digital-logic/README.md) | How do we build Boolean functions and memory from switches? | The synchronous digital system: registers and gates updating on a clock, plus number encodings |
| 04 | [Computer Architecture](04-computer-architecture/README.md) | How do we build a fast, programmable machine? | The Instruction Set Architecture (ISA): the hardware/software contract |
| 05 | [Algorithms & Data Structures](05-algorithms-and-data-structures/README.md) | How do we solve problems efficiently on that machine? | The algorithmic contract: a specification plus a cost bound in a named machine model |
| 06 | [Programming Languages](06-programming-languages/README.md) | How do humans express computation, and how is it translated down? | The language definition: program text with a fixed meaning, faithfully translated to the machine |
| 07 | [Operating Systems](07-operating-systems/README.md) | How do many programs share one machine safely? | The process behind a system-call interface: private memory, threads, files and sockets |
| 08 | [Networking](08-networking/README.md) | How do machines exchange data over unreliable links? | A best-effort datagram service between hosts, and a reliable byte stream between processes on top of it |
| 09 | [Data Management](09-data-management/README.md) | How do we store, query and update shared data correctly? | The transaction over declaratively queried, durable shared state |
| 10 | [Distributed & Parallel Computing](10-distributed-and-parallel-computing/README.md) | How do many machines act as one despite failures? | The illusion of one reliable, fast machine built from many unreliable ones |
| 11 | [Security & Cryptography](11-security-and-cryptography/README.md) | How do systems stay correct when someone attacks them? | Trust boundaries with stated guarantees: secure channels, isolation, access policies |
| 12 | [Software Engineering](12-software-engineering/README.md) | How do people build and evolve large software over time? | The change: a reviewed, tested, versioned, deployable delta to a running system |
| 13 | [Artificial Intelligence](13-artificial-intelligence/README.md) | How do machines act intelligently and learn from data? | The learned function: behaviour specified by an objective and data rather than code |
| 14 | [Human & Visual Computing](14-human-and-visual-computing/README.md) | How does computation meet human perception and action? | The perceptual interface: interaction design, rendering, media, vision |
| 15 | [Computing in Context](15-computing-in-context/README.md) | How does computing shape, and get shaped by, society? | Constraints and values (privacy, safety, fairness, sustainability) that become requirements |

## How to read this

- **Bottom-up (the intended path).** Start at 00 and read each layer's README, then dive into the leaves that interest you. You will never meet an idea that depends on something you have not seen.
- **Top-down (by need).** Start at the topic you care about. Each leaf's header lists what it **builds on**. Follow those links downward until things feel solid.
- **Across (by principle).** Pick an idea in [CROSS-CUTTING.md](CROSS-CUTTING.md), for example caching, and follow it from Central Processing Unit (CPU) caches (04) to page caches (07), Content Delivery Networks (08), buffer pools (09) and memoisation (05).

## Suggested short paths

| Goal | Path |
|---|---|
| How does a program actually run? | [the transistor](00-engineering-foundations/03-semiconductor-devices/the-mosfet.md) → [logic gates](03-digital-logic/02-combinational-logic/logic-gates.md) → [the ISA contract](04-computer-architecture/01-instruction-set-architecture/the-isa-contract.md) → [pipelining](04-computer-architecture/02-processor-microarchitecture/pipelining.md) → [code generation](06-programming-languages/03-compilers/code-generation-and-register-allocation.md) → [linking and loading](06-programming-languages/04-runtime-systems/linking-and-loading.md) → [processes](07-operating-systems/02-process-management/processes.md) |
| What are the limits of computation? | [entropy](02-theory-of-computation/01-information-theory/entropy-and-information.md) → [Turing machines](02-theory-of-computation/03-computability/turing-machines.md) → [halting problem](02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) → [P versus NP (polynomial versus nondeterministic polynomial time)](02-theory-of-computation/04-complexity/p-np-and-np-completeness.md) → [impossibility results in distributed systems](10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md) |
| Why is memory the bottleneck? | [capacitance and timing](00-engineering-foundations/02-electrical-circuits/capacitance-and-timing.md) → [locality and caching](04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) → [main memory and storage](04-computer-architecture/03-memory-hierarchy/dram-and-storage-devices.md) → [external-memory algorithms](05-algorithms-and-data-structures/07-advanced-topics/external-memory-and-cache-oblivious.md) → [B-trees](09-data-management/02-storage-and-indexing/b-trees.md) |
| How do Large Language Models (LLMs) work, from the ground up? | [linear algebra](01-mathematical-foundations/04-algebra/linear-algebra.md) → [optimization](01-mathematical-foundations/05-continuous-mathematics/optimization.md) → [Graphics Processing Units (GPUs)](04-computer-architecture/04-parallel-architecture/simd-and-gpus.md) → [backpropagation](13-artificial-intelligence/03-deep-learning/neural-networks-and-backpropagation.md) → [attention and transformers](13-artificial-intelligence/03-deep-learning/attention-and-transformers.md) → [large language models](13-artificial-intelligence/04-advanced-paradigms/large-language-models.md) |
| How does the internet stay up? | [packet switching](08-networking/01-principles/packet-switching.md) → [routing](08-networking/03-network-layer/routing-algorithms.md) → [congestion control](08-networking/04-transport-layer/congestion-control.md) → [replication](10-distributed-and-parallel-computing/03-consensus-and-replication/replication.md) → [consensus](10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md) → [reliability engineering](12-software-engineering/04-operations/reliability-engineering.md) |
| Why is software hard? | [halting problem](02-theory-of-computation/03-computability/halting-problem-and-undecidability.md) → [race conditions](07-operating-systems/03-concurrency/race-conditions-and-critical-sections.md) → [essential and accidental complexity](12-software-engineering/01-design/essential-and-accidental-complexity.md) → [modularity](12-software-engineering/01-design/modularity-and-information-hiding.md) → [Conway's law](12-software-engineering/02-process/conways-law-and-teams.md) |
| How does a search engine work? | [the web](08-networking/05-application-layer/http-and-the-web.md) → [graph theory](01-mathematical-foundations/03-discrete-mathematics/graph-theory.md) → [Markov chains and PageRank](01-mathematical-foundations/06-probability-and-statistics/markov-chains.md) → [tries and text indexes](05-algorithms-and-data-structures/06-string-algorithms/tries-and-suffix-structures.md) → [partitioning](10-distributed-and-parallel-computing/04-distributed-data/partitioning.md) → [retrieval and embeddings](13-artificial-intelligence/04-advanced-paradigms/retrieval-and-embeddings.md) |
| What can be learned about me from data? | [probability](01-mathematical-foundations/06-probability-and-statistics/probability.md) → [threat modelling](11-security-and-cryptography/01-security-principles/cia-and-threat-modeling.md) → [public-key cryptography](11-security-and-cryptography/02-cryptography/public-key-cryptography.md) → [privacy-enhancing technologies](11-security-and-cryptography/01-security-principles/privacy-enhancing-technologies.md) → [law, privacy and policy](15-computing-in-context/law-privacy-and-policy.md) |

## Maintenance

- Every path is fixed in [`_meta/TAXONOMY.md`](_meta/TAXONOMY.md). Change the taxonomy first, then the files.
- Run `python3 _meta/check.py` to check for missing files, missing sections, broken links and broken anchors.
- Style and templates: [`_meta/WRITER_BRIEF.md`](_meta/WRITER_BRIEF.md).
