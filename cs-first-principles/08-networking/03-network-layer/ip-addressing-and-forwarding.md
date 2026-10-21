# IP Addressing and Forwarding

> **Layer:** [08 Networking](../README.md) › [Network Layer](README.md)
> **Builds on:** [Packet Switching](../01-principles/packet-switching.md), [Media Access and Ethernet](../02-link-layer/media-access-and-ethernet.md), [Tries and Suffix Structures](../../05-algorithms-and-data-structures/06-string-algorithms/tries-and-suffix-structures.md), [Binary and Positional Notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md)
> **Enables:** [Routing Algorithms](routing-algorithms.md), [UDP and TCP](../04-transport-layer/udp-and-tcp.md), [Naming and DNS](../05-application-layer/naming-and-dns.md), [Network Attacks and Defenses](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md)

## Essence

The Internet Protocol (IP) gives every network interface an address and defines a packet format that any network can carry. Addresses are hierarchical: a prefix names a network, the remaining bits name a host within it. A router does not know where every host is; it holds a table of prefixes and, for each arriving packet, picks the entry with the longest prefix matching the destination and sends the packet to that entry's next hop. Hierarchy lets a few hundred thousand to a million prefixes cover billions of hosts, and longest-prefix match lets specific routes override general ones.

## Core tenets

1. **Addresses are locations, not identities.** An IP version 4 (IPv4) address is 32 bits, written as four decimal bytes (192.0.2.17); IPv6 uses 128 bits. The address says *where* an interface attaches to the network. A laptop that moves to a new network gets a new address, which is why addresses are poor long-term identifiers and why naming (the Domain Name System, DNS) sits above them.

2. **Hierarchical prefixes make routing tables small.** Classless Inter-Domain Routing (CIDR) writes a block of addresses as prefix/length: 203.0.113.0/24 covers 256 addresses whose first 24 bits match. An Internet Service Provider (ISP) holding 198.51.0.0/16 advertises one route for all its customers. This aggregation is what keeps the global table around a million IPv4 prefixes (circa mid-2020s) instead of billions of hosts.

3. **Forwarding is longest-prefix match.** Given destination D, a router chooses the most specific table entry that covers D. With entries 10.0.0.0/8 → port 1 and 10.1.2.0/24 → port 2, a packet to 10.1.2.7 goes to port 2 and one to 10.9.9.9 to port 1. The default route 0.0.0.0/0 matches everything. Longest match lets exceptions coexist with aggregates.

4. **Fast forwarding needs special data structures and hardware.** A 400 Gbit/s port receives a minimum-size packet every few nanoseconds. Software routers use compressed binary tries (one level per address bit, collapsed for speed) to find the longest match in a handful of memory accesses. Hardware routers use Ternary Content-Addressable Memory (TCAM), which compares the address against all entries in parallel in one cycle at significant power cost.

5. **Each hop rewrites the link header but not the IP addresses.** The router decrements the Time To Live (TTL) field (discarding the packet at zero, which stops loops from circulating forever), recomputes the header checksum, and wraps the packet in a new link-layer frame addressed to the next hop's link address. Source and destination IP stay the same end to end, barring address translation.

6. **IPv4 exhaustion produced NAT, which broke end-to-end addressing.** 2^32 ≈ 4.3 billion addresses ran out at the regional registries in the 2010s. Network Address Translation (NAT) lets a whole home or company share one public address: the NAT rewrites outgoing source addresses and ports and keeps a table to reverse the mapping for replies. Hosts behind a NAT cannot easily accept incoming connections, which complicates peer-to-peer applications and requires traversal tricks.

7. **IPv6 fixes address scarcity but must coexist.** With 2^128 addresses, every device can have a globally unique address again, and the header is simplified (no header checksum, no fragmentation by routers). Because IP is the narrow waist, upgrading it requires every host, router and middlebox to change; dual-stack operation has gone on for over two decades.

8. **Packets that are too big must be fragmented or rejected.** Each link has a Maximum Transmission Unit (MTU), typically 1,500 bytes for Ethernet. IPv4 routers may split oversized packets into fragments that the destination reassembles; losing any fragment loses the whole packet. IPv6 forbids router fragmentation; senders discover the path MTU instead, using error messages from the Internet Control Message Protocol (ICMP).

9. **Hosts get addresses automatically.** The Dynamic Host Configuration Protocol (DHCP) leases an address, prefix, default router and DNS server to a joining host. IPv6 hosts can also build their own address from the router's advertised prefix (stateless autoconfiguration).

## Key concepts

| Term | Meaning |
|---|---|
| IP address | 32-bit (IPv4) or 128-bit (IPv6) interface locator |
| Prefix / CIDR | Leading bits naming a network, written addr/length |
| Forwarding table (FIB) | Forwarding Information Base: prefix → next hop, used per packet |
| Longest-prefix match | Choose the most specific matching prefix |
| TTL / hop limit | Counter decremented per hop; packet dropped at zero |
| MTU | Largest packet a link can carry |
| NAT | Rewriting addresses and ports so many hosts share one public address |
| ICMP | Control and error messages for IP (unreachable, time exceeded, echo) |
| DHCP | Protocol that assigns addresses and configuration to hosts |
| Anycast | Same address announced from many places; routing picks the nearest |

## How it fits

- **Below:** packets ride in [link-layer frames](../02-link-layer/media-access-and-ethernet.md), with the Address Resolution Protocol (ARP) for IPv4 or Neighbor Discovery for IPv6 finding the next hop's link address. Prefix arithmetic is [binary notation](../../03-digital-logic/01-number-representation/binary-and-positional-notation.md); lookup is a [trie](../../05-algorithms-and-data-structures/06-string-algorithms/tries-and-suffix-structures.md).
- **Above:** [routing algorithms](routing-algorithms.md) fill the forwarding table; [TCP and UDP](../04-transport-layer/udp-and-tcp.md) add ports to reach processes; [DNS](../05-application-layer/naming-and-dns.md) maps names to addresses. Source-address spoofing and denial of service are [network attacks](../../11-security-and-cryptography/04-network-and-application-security/network-attacks-and-defenses.md) that exploit IP's lack of authentication.
- **Siblings:** this leaf is the data plane; [routing algorithms](routing-algorithms.md) and [BGP](internet-routing-and-bgp.md) are the control plane that decides what the table says; [data center networks and SDN](data-center-networks-and-sdn.md) move that control plane into a central controller and make the data plane itself programmable.

## Common misconceptions

- **"An IP address identifies a computer."** It identifies an attachment point; one computer may have many, and many computers may share one behind a NAT.
- **"Routers look up the exact destination address."** They look up the longest matching prefix; no router has an entry per host on the Internet.
- **"NAT is a security feature."** It blocks unsolicited inbound connections as a side effect, but it is an address-sharing mechanism; firewalls provide security policy.

## Go deeper

- V. Cerf, R. Kahn, *A Protocol for Packet Network Intercommunication* (1974): the original internetworking design.
- J. Postel, *RFC 791: Internet Protocol* (1981): the IPv4 specification, short and readable.
- G. Varghese, *Network Algorithmics* (2005): how fast lookup, classification and forwarding are really built.
