# Data Center Networks and SDN

> **Layer:** [08 Networking](../README.md) › [Network Layer](README.md)
> **Builds on:** [Routing Algorithms](routing-algorithms.md), [IP Addressing and Forwarding](ip-addressing-and-forwarding.md), [Media Access and Ethernet](../02-link-layer/media-access-and-ethernet.md), [DMA and Devices](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md), [Virtual Machines and Hypervisors](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md)
> **Enables:** [Congestion Control](../04-transport-layer/congestion-control.md), [Cloud Computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md), [Scalability Patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md), [Consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md)

## Essence

A large data center holds tens to hundreds of thousands of servers owned by one operator, and its network is a different problem from the Internet. Most traffic flows between servers inside the building (east-west), so every server needs high bandwidth to every other at low, predictable latency. Operators wire many small, cheap switches into a Clos (fat-tree) topology with many equal-cost paths and spread traffic across them. With one owner, distributed routing can give way to a logically central controller that programs the switches: Software-Defined Networking (SDN), separating the control plane (deciding routes) from the data plane (forwarding packets).

## Core tenets

1. **East-west traffic dominates, so the network must look like one big switch.** Requests fan out to many backend services, and storage, batch jobs and machine learning training shuffle data among thousands of machines. The goal is high *bisection bandwidth*: if any half of the servers sends to the other half, the network carries it at close to full rate. A classic tree under a few big core routers cannot: inter-rack traffic funnels through the top.

2. **A Clos topology builds a big non-blocking fabric from small identical switches.** Clos (1953) showed that multistage networks of small crossbars can act as one large non-blocking switch. In a data center this becomes leaf-spine or a three-tier fat-tree: every top-of-rack (leaf) switch connects to every spine, so any two racks are a few hops apart over many parallel paths. A fat-tree of k-port commodity switches connects k³/4 hosts at full bisection bandwidth (27,648 hosts with 48-port switches; Al-Fares et al., 2008). Losing one switch removes only a fraction of the paths.

3. **Equal-Cost Multi-Path (ECMP) routing spreads flows by hashing.** Each switch hashes a packet's flow identifier (addresses, ports, protocol) to pick one of several next hops. A flow stays on one path, avoiding reordering that would confuse the Transmission Control Protocol (TCP). But hashing ignores load: two large "elephant" flows can collide on one link while others sit idle.

4. **Short distances shift the bottleneck to queues and bursts.** Round trips inside a building take tens of microseconds, so a few queued packets dominate latency. Buffers are shallow, and many servers answering one request at once overflow the receiver's port (*incast*). Data Center TCP (DCTCP; Alizadeh et al., 2010) reacts to the *fraction* of packets marked with Explicit Congestion Notification (ECN) to keep queues near empty.

5. **Separating control from data plane is the core idea of SDN.** SDN moves that computation to a controller that sees the whole topology and writes match-action rules into switches through an open interface such as OpenFlow (McKeown et al., 2008); switches only forward. Global knowledge simplifies traffic engineering and isolation; Google's B4 wide-area network (Jain et al., 2013) used it to run links far hotter than distributed routing allows.

6. **Centralisation moves the hard problems, it does not remove them.** The controller is replicated for availability, its state kept consistent with [consensus](../../10-distributed-and-parallel-computing/03-consensus-and-replication/consensus.md). Rule updates reach switches at different times, so they must be ordered to avoid transient loops. Switches keep their last rules when the controller is unreachable, so its failure stops change, not traffic.

7. **Programmable data planes make forwarding itself software.** Fixed-function chips understand only the protocols their designers chose. P4 (Bosshart et al., 2014) describes how a programmable switch, network card or software switch parses headers and applies a pipeline of match-action tables. Programs have no unbounded loops and fixed per-stage work, so they run at line rate, enabling new headers and in-network telemetry without new silicon.

8. **Virtualization runs tenant networks on top of the physical fabric.** Each cloud tenant wants private addresses and isolation. Overlays wrap tenant packets in an outer header (Virtual Extensible Local Area Network (VXLAN) carries a 24-bit network identifier, about 16 million segments), and virtual switches in the hypervisor or Network Interface Card (NIC) apply tenant policy. The fabric routes outer addresses only.

9. **RDMA removes the host's software from the fast path.** Remote Direct Memory Access (RDMA) lets a NIC read or write another machine's registered memory directly, bypassing both kernels and the remote Central Processing Unit (CPU), for microsecond-scale latency. RDMA over Converged Ethernet (RoCE) brings it from InfiniBand clusters to data centers but needs a nearly lossless fabric, enforced by link-level pause frames that can spread congestion or deadlock.

## Key concepts

| Term | Meaning |
|---|---|
| East-west traffic | Traffic between servers inside the data center |
| Bisection bandwidth | Minimum capacity across any cut splitting the servers in half |
| Clos / fat-tree / leaf-spine | Multistage topologies of small switches with many equal paths between racks |
| ECMP | Hashing flows across several equal-cost next hops |
| Incast | Synchronised many-to-one responses overflowing one switch port |
| Control plane / data plane | Computing forwarding state / applying it to each packet |
| Match-action table | Rule list: header pattern, then action (forward, rewrite, drop) |
| Overlay | Virtual network carried by encapsulation over a physical one |

## How it fits

- **Below:** the fabric is built from [Ethernet switches](../02-link-layer/media-access-and-ethernet.md) and [Internet Protocol (IP) forwarding](ip-addressing-and-forwarding.md); controllers reuse [routing algorithms](routing-algorithms.md). RDMA stretches [Direct Memory Access (DMA)](../../04-computer-architecture/05-io-and-interconnect/dma-and-devices.md) across machines; overlays serve [virtual machines](../../07-operating-systems/07-virtualization/virtual-machines-and-hypervisors.md).
- **Above:** the substrate of [cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md); its tail latency shapes [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md); it needs its own [congestion control](../04-transport-layer/congestion-control.md).
- **Siblings:** [routing algorithms](routing-algorithms.md) assume cooperating routers with partial knowledge; SDN assumes one owner with global knowledge; [Internet routing and BGP](internet-routing-and-bgp.md) is the opposite extreme, many owners and no central view. Many fabrics still run the Border Gateway Protocol (BGP) internally for its robustness.

## Common misconceptions

- **"SDN means one controller box."** It is logically central but physically replicated.
- **"A data center network is a small Internet."** One owner, regular topology and microsecond round trips permit designs (central control, lossless fabrics) the Internet cannot use.
- **"ECMP balances load evenly."** It balances flow *counts* statistically; a few large flows can still overload one path.

## Go deeper

- C. Clos, *A Study of Non-Blocking Switching Networks* (Bell System Technical Journal, 1953): the multistage idea.
- M. Al-Fares, A. Loukissas, A. Vahdat, *A Scalable, Commodity Data Center Network Architecture* (SIGCOMM 2008): commodity fat-trees.
- N. McKeown et al., *OpenFlow: Enabling Innovation in Campus Networks* (ACM SIGCOMM Computer Communication Review, 2008): the interface that launched SDN.
- A. Singh et al., *Jupiter Rising: A Decade of Clos Topologies and Centralized Control in Google's Datacenter Network* (SIGCOMM 2015): both ideas in production.
