# Naming and DNS

> **Layer:** [08 Networking](../README.md) › [Application Layer](README.md)
> **Builds on:** [UDP and TCP](../04-transport-layer/udp-and-tcp.md), [IP Addressing and Forwarding](../03-network-layer/ip-addressing-and-forwarding.md), [File System Abstractions](../../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md), [Locality and Caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md)
> **Enables:** [HTTP and the Web](http-and-the-web.md), [Content Delivery and Caching](content-delivery-and-caching.md), [Eventual Consistency and CRDTs](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md), [Web Security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md)

## Essence

People and programs want stable, meaningful names such as `www.example.com`; networks route by numeric addresses that change when services move. The Domain Name System (DNS) is a globally distributed database that maps names to addresses and other records. It scales to hundreds of millions of domains and trillions of queries a day through three ideas: a hierarchical namespace, so each part is managed by its owner; delegation, so each server knows only its own zone and who is responsible below it; and caching with a time-to-live, so most lookups never leave the local resolver. The price is that changes propagate slowly and stale answers are normal.

## Core tenets

1. **Names add a level of indirection between identity and location.** A service keeps its name while its servers' Internet Protocol (IP) addresses change. Clients look up the current address at connection time. This is the same move as virtual memory or file paths: a stable name, a mapping that can be updated, and a resolver that applies it.

2. **The namespace is a tree, managed by delegation.** The root delegates top-level domains (`.com`, `.org`, `.uk`) to their operators, who delegate second-level domains (`example.com`) to their registrants, and so on. Each delegated piece is a *zone* served by authoritative name servers. No single party stores the whole database, and each owner changes its own records without asking anyone.

3. **Resolution walks the tree from the root down.** A recursive resolver (typically run by the Internet Service Provider (ISP) or a public service) asks a root server for `www.example.com`, is referred to the `.com` servers, is referred to `example.com`'s authoritative servers, and gets the answer. The client's stub resolver asks only the recursive resolver. Thirteen root server names, each anycast from hundreds of sites, anchor the tree.

4. **Caching is what makes DNS scale.** Every record carries a Time To Live (TTL), in seconds. Resolvers cache answers, including referrals and negative answers, until the TTL expires. Because `.com`'s servers are cached for days, a typical lookup needs at most one query to an authoritative server, and popular names are answered from cache in under a millisecond.

5. **TTL trades freshness for load and latency.** A long TTL (a day) means few queries but slow changes: a moved server keeps receiving traffic from cached old addresses until TTLs expire. A short TTL (30 seconds) lets operators steer traffic quickly, which CDNs and failover systems rely on, at the cost of more queries and lookup latency. DNS is therefore *eventually consistent* by design.

6. **Records hold more than addresses.** A (IPv4 address), AAAA (IPv6 address), CNAME (alias to another name), MX (mail server for a domain), NS (delegation), TXT (arbitrary text, used for domain verification and email policy) and others. DNS is a general-purpose, read-mostly, globally replicated key-value store.

7. **DNS runs mostly over UDP for speed.** A query and answer usually fit in one User Datagram Protocol (UDP) packet each, so a lookup costs one round trip with no handshake. Large responses and zone transfers fall back to the Transmission Control Protocol (TCP). Encrypted variants (DNS over HTTPS, DNS over TLS) protect privacy from on-path observers at the cost of extra handshakes.

8. **Classic DNS trusts whatever answer arrives.** An attacker who can guess a query's ID and source port can inject a forged answer that resolvers will cache (cache poisoning; the 2008 Kaminsky attack made this practical). Randomised source ports raise the bar. The Domain Name System Security Extensions (DNSSEC) sign records along the delegation chain so resolvers can verify them, but deployment is partial.

9. **Name resolution is a performance and availability dependency.** Every new connection to a new name waits for DNS first. Outages at a major DNS provider have made large parts of the web unreachable even though the target servers were fine (the 2016 Dyn attack is a well-known example).

## Key concepts

| Term | Meaning |
|---|---|
| Domain name | Hierarchical, dot-separated name, read right to left from the root |
| Zone | Contiguous part of the namespace managed by one authority |
| Authoritative server | Server holding the definitive records for a zone |
| Recursive resolver | Server that performs full lookups on behalf of clients and caches results |
| Delegation | NS records handing responsibility for a subtree to other servers |
| TTL | Time a record may be cached |
| Resource record | Typed entry (A, AAAA, CNAME, MX, NS, TXT, ...) |
| Cache poisoning | Injecting forged answers into a resolver's cache |
| DNSSEC | Digital signatures on DNS records, chained from the root |

## How it fits

- **Below:** queries ride on [UDP and TCP](../04-transport-layer/udp-and-tcp.md); answers are [IP addresses](../03-network-layer/ip-addressing-and-forwarding.md). Hierarchical naming mirrors [file system paths](../../07-operating-systems/05-storage-and-file-systems/file-system-abstractions.md); TTL caches are [caching](../../04-computer-architecture/03-memory-hierarchy/locality-and-caching.md) with a time-based coherence rule.
- **Above:** every [HTTP](http-and-the-web.md) request begins with DNS; [CDNs](content-delivery-and-caching.md) use DNS answers to steer users; DNS is a canonical example of [eventual consistency](../../10-distributed-and-parallel-computing/04-distributed-data/eventual-consistency-and-crdts.md). Browser security relies on domain names as the basis of the same-origin policy ([web security](../../11-security-and-cryptography/04-network-and-application-security/web-security.md)), and TLS certificates are issued for names.
- **Siblings:** [HTTP](http-and-the-web.md) names resources with URLs whose host part is a DNS name; [content delivery](content-delivery-and-caching.md) is DNS indirection put to work for latency.

## Common misconceptions

- **"DNS changes propagate."** Nothing is pushed; old answers simply expire from caches when their TTL runs out.
- **"There are only thirteen root servers."** There are thirteen root server identities, each served by many anycast instances worldwide.
- **"DNS is just for websites."** Mail routing, service discovery, certificate validation and domain ownership checks all depend on it.

## Go deeper

- P. Mockapetris, *RFC 1034: Domain Names, Concepts and Facilities* (1987): the design, still the clearest description.
- P. Mockapetris, K. J. Dunlap, *Development of the Domain Name System* (SIGCOMM 1988): the design decisions in hindsight.
- J. Saltzer, *On the Naming and Binding of Network Destinations* (1982, published as RFC 1498 in 1993): names, addresses and routes as distinct concepts.
