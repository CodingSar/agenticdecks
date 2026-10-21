# Media Access and Ethernet

> **Layer:** [08 Networking](../README.md) › [Link Layer](README.md)
> **Builds on:** [Encoding and Framing](encoding-and-framing.md), [Packet Switching](../01-principles/packet-switching.md), [Probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md), [Randomized Algorithms](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md)
> **Enables:** [Wireless Networks](wireless-networks.md), [IP Addressing and Forwarding](../03-network-layer/ip-addressing-and-forwarding.md), [Network Attacks and Defenses](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md)

## Essence

When several stations share one transmission medium, two frames sent at once collide and both are lost. A Medium Access Control (MAC) protocol decides who may send when, with no central coordinator and no prior knowledge of who has data. Classic Ethernet solved this with randomness: listen before sending, stop on collision, wait a random and exponentially growing time, try again. Modern Ethernet largely removed the problem by giving every station its own full-duplex cable to a switch, which learns where each address lives and forwards frames only where they need to go. Ethernet's frame format and 48-bit addresses survived both transitions and now run from 10 Mbit/s to 800 Gbit/s.

## Core tenets

1. **Shared media need a way to take turns without a scheduler.** The three families are: *channel partitioning* (divide by time or frequency, as in Time-Division Multiple Access (TDMA) and Frequency-Division Multiple Access (FDMA)), *taking turns* (polling, token passing), and *random access* (send and recover from collisions). Partitioning wastes idle slots under bursty load; turn-taking adds latency and a single point of failure; random access is simple and efficient at low load.

2. **Pure random access has low peak efficiency.** In ALOHA (University of Hawaii, 1970), a station sends whenever it has a frame. Two frames overlap if either starts within one frame time of the other, so peak throughput is 1/(2e) ≈ 18% of capacity. Slotted ALOHA, which aligns sends to slot boundaries, halves the vulnerable window and reaches 1/e ≈ 37%.

3. **Carrier sense and collision detection recover most of the waste.** Carrier Sense Multiple Access with Collision Detection (CSMA/CD), used by classic Ethernet, listens before sending and aborts as soon as it hears a collision. Collisions still happen because a signal takes time to propagate, so two stations can both hear silence and start. The cost of a collision shrinks to the propagation time, so efficiency approaches 1 when frames are long relative to propagation delay.

4. **Binary exponential backoff adapts to unknown load.** After the n-th collision a station waits a random number of slot times chosen from 0 to 2^n − 1 (capped at 1,023). With few contenders, retries are fast; with many, the spread grows until collisions become rare. It is a feedback loop that estimates contention without measuring it directly.

5. **Collision detection imposes a minimum frame size.** A sender must still be transmitting when news of a collision returns from the far end, or it will not know its frame was lost. That ties minimum frame length to the round-trip propagation time of the longest allowed cable: 64 bytes for 10 Mbit/s Ethernet. Faster rates made this constraint untenable on shared media, which is one reason Ethernet moved to switches.

6. **Switches turn a shared medium into many point-to-point links.** A switch receives frames on one port and forwards them out another. Each station has a dedicated full-duplex link, so there are no collisions at all, and CSMA/CD is disabled in modern Ethernet. Many pairs can talk at once at full rate.

7. **Switches learn addresses by watching traffic.** Each frame carries a 48-bit MAC address for source and destination. When a frame arrives, the switch records "source address is reachable via this port". To forward, it looks up the destination; if unknown, it floods the frame out all other ports. This self-learning means plug-and-play with no configuration, but it requires a loop-free topology, enforced by the Spanning Tree Protocol, because a flooded frame on a loop circulates forever.

8. **A Local Area Network (LAN) is a broadcast domain, which limits its size.** Broadcasts (and floods of unknown destinations) reach every station. That is convenient for discovery, such as the Address Resolution Protocol (ARP) asking "who has this Internet Protocol (IP) address?", but it does not scale to millions of hosts and lets any local host spoof replies. Beyond a building, networks are joined by IP routers, which do not flood.

## Key concepts

| Term | Meaning |
|---|---|
| MAC protocol | Rules for sharing a medium among stations |
| MAC address | 48-bit link-layer identifier, normally assigned by the manufacturer |
| ALOHA | Send at will; retransmit after random delay on collision |
| CSMA/CD | Listen before sending, stop on collision; classic Ethernet |
| Exponential backoff | Random retry delay whose range doubles after each collision |
| Switch | Device forwarding frames between ports based on learned MAC addresses |
| Full duplex | Both directions transmit simultaneously on separate paths |
| Spanning tree | Protocol that disables links to make a switched LAN loop-free |
| VLAN | Virtual LAN: logical partition of a switched network into separate broadcast domains |
| ARP | Address Resolution Protocol: maps an IP address to a MAC address on a LAN |

## How it fits

- **Below:** uses [framing](encoding-and-framing.md) to delimit and check frames; the throughput analysis is [probability](../../01-mathematical-foundations/06-probability-and-statistics/probability.md) over Poisson arrivals; backoff is a [randomized algorithm](../../05-algorithms-and-data-structures/03-design-paradigms/randomized-algorithms.md) for symmetry breaking.
- **Above:** IP packets travel between routers inside Ethernet frames; ARP glues [IP addressing](../03-network-layer/ip-addressing-and-forwarding.md) to MAC addresses. ARP spoofing and MAC flooding are classic [local network attacks](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md). [Data-centre fabrics](../03-network-layer/data-center-networks-and-sdn.md) are built from Ethernet switches.
- **Siblings:** [wireless networks](wireless-networks.md) still face true shared-medium contention and cannot detect collisions, so they use avoidance instead.

## Common misconceptions

- **"Ethernet still uses CSMA/CD."** Switched full-duplex Ethernet has no collisions; CSMA/CD survives only in the standard for half-duplex compatibility.
- **"MAC addresses identify a device globally and securely."** They are only meaningful on one LAN, are not routed, and can be changed in software.
- **"A switch and a router do the same thing."** A switch forwards by flat MAC address within one broadcast domain; a router forwards by hierarchical IP prefix between networks.

## Go deeper

- R. M. Metcalfe, D. R. Boggs, *Ethernet: Distributed Packet Switching for Local Computer Networks* (1976): the original Ethernet design.
- N. Abramson, *The ALOHA System: Another Alternative for Computer Communications* (1970): the first random-access network.
- R. Perlman, *Interconnections: Bridges, Routers, Switches, and Internetworking Protocols* (2nd ed., 1999): by the inventor of the spanning tree algorithm.
