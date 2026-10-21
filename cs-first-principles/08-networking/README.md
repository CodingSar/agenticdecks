# 08 Networking

> **Layer:** 08 Networking
> **Children:** [Principles](01-principles/README.md) · [Link Layer](02-link-layer/README.md) · [Network Layer](03-network-layer/README.md) · [Transport Layer](04-transport-layer/README.md) · [Application Layer](05-application-layer/README.md)

## What this area is about

Networking answers one question: how do programs on different machines exchange data reliably and efficiently when the only thing connecting them is a shared, lossy, delay-prone physical medium owned by many parties? The answer is a stack of protocols, each turning a weak service into a slightly stronger one. A wire carries noisy voltages; the link layer turns them into frames between neighbours; the network layer turns frames into best-effort packets between any two hosts on Earth; the transport layer turns packets into ordered, reliable byte streams between processes; and the application layer turns streams into names, documents and services.

The unifying idea is that networking *extends the Operating System's (OS's) abstractions across machines*. A socket looks like a file descriptor. A Transmission Control Protocol (TCP) connection looks like a pipe. A Uniform Resource Locator (URL) looks like a file path. Behind each familiar interface sits a mechanism that must survive loss, reordering, congestion, failure and the fact that no single party controls the whole system.

## Why this layer sits here

Networking needs three things from below:

- **Signals and physics (00).** Bits travel as electromagnetic waves on copper, glass or air. Bandwidth, attenuation and noise come from [analog vs digital signalling](../00-engineering-foundations/04-signals-and-systems/analog-vs-digital.md), [sampling and quantization](../00-engineering-foundations/04-signals-and-systems/sampling-and-quantization.md) and [noise and signal integrity](../00-engineering-foundations/02-electrical-circuits/noise-and-signal-integrity.md). Speed-of-light delay is a floor no protocol can beat.
- **Information theory and coding (02).** [Channel capacity and error correction](../02-theory-of-computation/01-information-theory/channel-capacity-and-error-correction.md) says how many bits a noisy link can carry and how redundancy detects or repairs damage. Every checksum and every modulation scheme is applied Shannon.
- **Operating-system Input/Output (I/O) (07).** The kernel owns the network card, runs the protocol stack, and exposes it through the socket interface and the [I/O models](../07-operating-systems/06-io-and-devices/io-models.md) (blocking, non-blocking, event-driven). [Device drivers and interrupt handling](../07-operating-systems/06-io-and-devices/device-drivers-and-interrupt-handling.md) move packets between wire and memory.

Graph algorithms from [shortest paths](../05-algorithms-and-data-structures/05-graph-algorithms/shortest-paths.md) power routing, and [queueing ideas from probability](../01-mathematical-foundations/06-probability-and-statistics/random-variables-and-distributions.md) explain delay.

The layers above need from networking a single abstraction: **a best-effort datagram service between any two addresses, and a reliable ordered byte stream between any two processes, built on top of it.** [Distributed systems (10)](../10-distributed-and-parallel-computing/README.md) assume exactly this, and their failure models (messages delayed, lost, duplicated; no bound on delay) are the honest description of what the Internet provides. [Security (11)](../11-security-and-cryptography/README.md) must protect traffic that crosses networks it does not control. [Data management (09)](../09-data-management/README.md) uses networks for client/server access and replication.

## How the children fit together

| Child | Its role in the whole | Depends on |
|---|---|---|
| [01 Principles](01-principles/README.md) | Why the stack is layered, why packets beat circuits, what limits latency and throughput | 00, 01, 02 |
| [02 Link Layer](02-link-layer/README.md) | Moves frames across one physical hop and shares a medium among many senders | Principles |
| [03 Network Layer](03-network-layer/README.md) | Gives every host an address and forwards packets across many hops; computes routes, between rival networks with the Border Gateway Protocol (BGP), or centrally inside a data center with Software-Defined Networking (SDN) | Link, Principles |
| [04 Transport Layer](04-transport-layer/README.md) | Turns host-to-host packets into process-to-process streams; adds reliability and congestion control end to end | Network |
| [05 Application Layer](05-application-layer/README.md) | Names (Domain Name System, DNS), documents (Hypertext Transfer Protocol, HTTP), and the caching that makes the web fast | Transport |

```
  Application   HTTP, DNS, CDN          names, documents, caching
  ------------------------------------------------------------------
  Transport     TCP, UDP, QUIC          ports, reliability, congestion
  ------------------------------------------------------------------
  Network       IP, BGP, OSPF           addresses, forwarding, routing
  ------------------------------------------------------------------
  Link          Ethernet, Wi-Fi         frames, media access
  ------------------------------------------------------------------
  Physical      copper, fibre, radio    signals (layer 00)
```

Read Principles first: the end-to-end argument and packet switching explain *why* each later layer does as little as it does. Then go bottom-up. Each layer adds a header on the way down and strips it on the way up; each layer trusts only the service the layer below promises. The Internet Protocol (IP) is the narrow waist: many link technologies below, many transports and applications above, one packet format in the middle. That waist is why the Internet could absorb Wi-Fi, fibre and cellular without changing a single web server.

## Connections to neighbouring layers

- **[00 Engineering Foundations](../00-engineering-foundations/README.md):** physical media, modulation and noise set the raw bit rate and error rate of every link. [Feedback and control](../00-engineering-foundations/04-signals-and-systems/feedback-and-control.md) is the theory behind congestion control.
- **[02 Theory of Computation](../02-theory-of-computation/README.md):** entropy bounds compression of payloads; channel coding bounds reliable rate; finite-state machines describe protocol endpoints.
- **[05 Algorithms and Data Structures](../05-algorithms-and-data-structures/README.md):** Dijkstra and Bellman-Ford are routing protocols in disguise; tries do longest-prefix match in routers; hash tables back connection tables.
- **[07 Operating Systems](../07-operating-systems/README.md):** the protocol stack lives in the kernel (or bypasses it for speed); sockets are file descriptors; buffering and interrupts decide end-host performance.
- **[09 Data Management](../09-data-management/README.md):** databases speak wire protocols over TCP and replicate logs across networks; network latency shapes how chatty a query interface can be.
- **[10 Distributed and Parallel Computing](../10-distributed-and-parallel-computing/README.md):** distributed algorithms take the network's asynchrony, loss and partitions as given and build agreement on top. In the other direction, [data center networks](03-network-layer/data-center-networks-and-sdn.md) are the fabric clusters and clouds run on, and their SDN controllers are themselves replicated with consensus.
- **[11 Security and Cryptography](../11-security-and-cryptography/README.md):** the original Internet assumed trusted peers; [Transport Layer Security (TLS)](../11-security-and-cryptography/02-cryptography/secure-protocols-and-tls.md) and [network defences](../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md) retrofit confidentiality and authenticity.
- **[12 Software Engineering](../12-software-engineering/README.md):** service architectures and observability are shaped by network failure and tail latency.

## Connections across layers

Networking takes bits-on-a-medium from 00, coding theory from 02, graph algorithms from 05 and sockets from 07. It gives 09, 10 and 11 a global, unreliable, asynchronous message service and a reliable stream on top. Its hardest lesson for the layers above is that a missing reply cannot be told apart from a slow one, which is the seed of the impossibility results in [10](../10-distributed-and-parallel-computing/02-distributed-foundations/impossibility-results.md).

## Cross-cutting threads

- [Abstraction and layering](../CROSS-CUTTING.md#abstraction-and-layering): the protocol stack is the textbook case of layers that each use only the one below.
- [The end-to-end argument](../CROSS-CUTTING.md#the-end-to-end-argument): reliability and security belong at the endpoints; the network core stays simple.
- [Indirection and naming](../CROSS-CUTTING.md#indirection-and-naming): DNS names map to addresses, addresses map to link-layer addresses.
- [Caching and locality](../CROSS-CUTTING.md#caching-and-locality): DNS caches, HTTP caches and Content Delivery Networks (CDNs) move data closer to readers.
- [Feedback and control](../CROSS-CUTTING.md#feedback-and-control): TCP congestion control infers network state from loss and delay and adjusts its rate.
- [Redundancy and fault tolerance](../CROSS-CUTTING.md#redundancy-and-fault-tolerance): checksums, retransmission and multipath routing survive damage and failure.
- [Pipelining and parallelism](../CROSS-CUTTING.md#pipelining-and-parallelism): sliding windows keep many packets in flight to fill the pipe.
- [Limits and impossibility](../CROSS-CUTTING.md#limits-and-impossibility): speed of light and Shannon capacity bound latency and rate.
