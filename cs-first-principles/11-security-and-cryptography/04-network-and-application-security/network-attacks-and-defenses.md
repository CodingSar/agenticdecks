# Network Attacks and Defenses

> **Layer:** [11 Security and Cryptography](../README.md) › [Network and application security](README.md)
> **Builds on:** [Layering and the end-to-end principle](../../08-networking/01-principles/layering-and-the-end-to-end-principle.md), [Internet routing and the Border Gateway Protocol](../../08-networking/03-network-layer/internet-routing-and-bgp.md), [Naming and the Domain Name System](../../08-networking/05-application-layer/naming-and-dns.md), [Secure protocols and Transport Layer Security](../02-cryptography/secure-protocols-and-tls.md)
> **Enables:** [Reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md), [Scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md), [Cloud computing](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md)

## Essence

The Internet's core protocols were designed for a cooperative network of research institutions. Source addresses are not verified, routing announcements are mostly believed, name lookups are not authenticated, and anyone can send traffic to anyone. Network attacks exploit these trust assumptions to **impersonate** (spoof addresses, names or routes), **intercept and modify** (man-in-the-middle), and **exhaust** (denial of service). Defences come in two kinds: **filtering and hardening** inside the network (firewalls, ingress filtering, route validation, rate limiting), and **cryptography at the endpoints** (Transport Layer Security (TLS), virtual private networks, signed records). The end-to-end argument predicts which one is sufficient: only endpoint authentication and encryption guarantee confidentiality and integrity; network-level measures reduce exposure and protect availability.

## Core tenets

1. **Anything not authenticated can be forged.** An Internet Protocol (IP) packet's source address is just a field the sender fills in. Address Resolution Protocol (ARP) replies on a local network are accepted without proof, so an attacker can claim another machine's address and receive its traffic (ARP spoofing). Unauthenticated protocols therefore must not be used for trust decisions: an IP address is a routing hint, not an identity.

2. **Routing and naming attacks redirect traffic at scale.** The Border Gateway Protocol (BGP) trusts neighbours' announcements of which networks they can reach. A wrong or malicious announcement of a more specific prefix can divert a large share of a target's traffic worldwide, as in the 2008 Pakistan Telecom hijack of YouTube's prefix. Domain Name System (DNS) cache poisoning (made practical by Kaminsky's 2008 technique) inserts forged answers into resolvers so a name points to the attacker. Defences are Resource Public Key Infrastructure (RPKI), which lets networks sign which origins may announce their prefixes, DNSSEC (DNS Security Extensions), which signs DNS records, and above all endpoint TLS, which makes redirected traffic fail certificate checks.

3. **Man-in-the-middle is defeated only by authenticated encryption end to end.** An attacker on the path (a hostile Wi-Fi access point, a compromised router, a hijacked route) can read and modify unprotected traffic. Encryption without authentication is not enough, because the attacker can terminate the connection and re-encrypt. TLS with certificate validation, or Secure Shell (SSH) with verified host keys, makes interception detectable.

4. **Denial of service exploits asymmetry.** An attack succeeds when it costs the attacker less to send than the victim to handle. Volumetric floods from botnets of compromised devices reached about 1 terabit per second with the Mirai botnet in 2016, and attacks of several terabits per second have since been reported. Reflection and amplification make it worse: the attacker sends small queries with the victim's spoofed source address to open servers (DNS, the Network Time Protocol (NTP), memcached) that reply with much larger responses, amplification factors from tens to tens of thousands.

5. **State exhaustion is cheaper than bandwidth exhaustion.** A Transmission Control Protocol (TCP) SYN (synchronise) flood sends connection requests without completing the handshake, filling the server's table of half-open connections. SYN cookies defeat it by encoding the connection state into the server's initial sequence number, so the server keeps no state until the client proves it received the reply. The general lesson: do not commit resources to an unauthenticated peer.

6. **Ingress filtering would stop spoofing at the source, but deployment is partial.** If every network dropped outgoing packets whose source addresses did not belong to it (BCP 38, "Best Current Practice 38", 2000), spoofed reflection attacks would largely disappear. Because the benefit goes to others and the cost to the deployer, adoption remains incomplete, which is a reminder that network security is partly an economic coordination problem.

7. **Perimeter defences are necessary but not sufficient.** Firewalls filter traffic by address, port and connection state; intrusion detection systems look for known attack signatures or anomalies. They reduce attack surface but assume the inside is trustworthy, and attackers who phish one employee are inside. "Zero trust" architectures drop that assumption: every request is authenticated, authorised and encrypted regardless of network location, applying complete mediation to the network.

8. **Large-scale absorption is the practical defence against floods.** Since an attacker can out-send any single site, large services rely on anycast routing to spread attack traffic over many data centres, on content delivery networks with huge aggregate capacity, and on upstream scrubbing that filters attack traffic before it reaches the origin.

## Key concepts

| Term | Meaning |
|---|---|
| Spoofing | Forging a source address, name or identity |
| ARP spoofing | Claiming another host's IP address on a local network |
| BGP hijack | Announcing routes for address space one does not own |
| DNS cache poisoning | Inserting forged records into a resolver's cache |
| DDoS | Distributed denial of service from many sources |
| Amplification | Small spoofed requests causing large replies to a victim |
| SYN cookie | Stateless encoding of handshake state to resist SYN floods |
| RPKI / DNSSEC | Signed route origins / signed DNS records |
| Zero trust | Authenticating every request regardless of network location |

## How it fits

- **Below:** attacks target [Ethernet and ARP](../../08-networking/02-link-layer/media-access-and-ethernet.md), [wireless links](../../08-networking/02-link-layer/wireless-networks.md), [IP forwarding](../../08-networking/03-network-layer/ip-addressing-and-forwarding.md), [BGP](../../08-networking/03-network-layer/internet-routing-and-bgp.md), [TCP](../../08-networking/04-transport-layer/udp-and-tcp.md) and [DNS](../../08-networking/05-application-layer/naming-and-dns.md); defences rest on [TLS](../02-cryptography/secure-protocols-and-tls.md) and [signatures](../02-cryptography/public-key-cryptography.md); the [end-to-end principle](../../08-networking/01-principles/layering-and-the-end-to-end-principle.md) says where protection belongs.
- **Above:** [reliability engineering](../../12-software-engineering/04-operations/reliability-engineering.md) plans for attacks as for outages; [scalability patterns](../../10-distributed-and-parallel-computing/05-large-scale-systems/scalability-patterns.md) and [content delivery](../../08-networking/05-application-layer/content-delivery-and-caching.md) absorb floods; [cloud](../../10-distributed-and-parallel-computing/05-large-scale-systems/cloud-computing.md) networks implement zero-trust access; [policy](../../15-computing-in-context/law-privacy-and-policy.md) governs interception and lawful access.
- **Siblings:** [authentication](authentication.md) replaces address-based trust; [web security](web-security.md) relies on HTTPS (the Hypertext Transfer Protocol Secure) to survive interception; [supply chain security](software-supply-chain-security.md) protects the update channel itself.

## Common misconceptions

- **"A firewall makes the internal network safe."** Phishing, compromised devices and insiders are already inside; internal traffic needs authentication too.
- **"DNSSEC encrypts DNS."** It authenticates records; confidentiality needs DNS over TLS or over HTTPS.
- **"Blocking an attacking IP address stops a DDoS."** Distributed attacks use many thousands of addresses, often spoofed or belonging to innocent reflectors.

## Go deeper

- Bellovin, "Security Problems in the TCP/IP Protocol Suite", *ACM Computer Communication Review* (1989), with his 2004 retrospective.
- Ferguson and Senie, "Network Ingress Filtering", RFC 2827 / BCP 38 (2000).
- Rossow, "Amplification Hell: Revisiting Network Protocols for DDoS Abuse", NDSS (2014).
- Kurose and Ross, *Computer Networking: A Top-Down Approach* (8th ed., 2021), chapter on network security.
